#!/usr/bin/env python3
"""抓取 Hugging Face 之外的一手公开 benchmark 榜单，落盘为可复现的原始快照。

与 scripts/fetch_hf_models.py 的分工：
  * fetch_hf_models.py      —— 发现「哪些模型值得关注」
  * fetch_benchmark_boards.py —— 抓取「这些模型在各榜单上的官方分数」

设计要点：
  * 只取有稳定机器可读端点的一手榜单（官方 GitHub 仓库 / 官方文档站表格）。
    不解析需要登录、需要执行 JS 或没有结构化端点的页面。
  * 原始响应落盘到 data/benchmarks/ 缓存，解析结果写 data/benchmark_boards.json。
    缓存命中则不联网，保证离线可复现。
  * 每个榜单记录一条 source（含 level / url / 抓取时间），观测继承其来源等级。
  * 榜单本身带「口径」信息（agent 脚手架、reasoning effort、编辑格式等），
    这些维度会影响分数，必须随观测一起保存，不能只留模型名和分数。

用法：
    python3 scripts/fetch_benchmark_boards.py            # 抓取 + 生成
    python3 scripts/fetch_benchmark_boards.py --offline   # 仅用缓存，不联网
    python3 scripts/fetch_benchmark_boards.py --validate  # 校验产物
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import html as H
import io
import json
import re
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

CACHE_DIR = Path("data/benchmarks")
OUTPUT_FILE = Path("data/benchmark_boards.json")

# 大文件分块下载的块大小。raw.githubusercontent 对单次 4MB 传输会中途截断，
# 按 400KB 分块 Range 请求可稳定拿全。
CHUNK_SIZE = 400_000

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
)

# 榜单源定义。每个 source 必须能取到「该榜单的全部参评条目」，
# 否则只能算抽样，不能标记为 roster（参评名单）。
SWE_BENCH_URL = (
    "https://raw.githubusercontent.com/SWE-bench/swe-bench.github.io/master/data/leaderboards.json"
)
AIDER_URL = "https://aider.chat/docs/leaderboards/"
AIDER_EDIT_URL = "https://aider.chat/docs/leaderboards/edit.html"
AIDER_REFACTOR_URL = "https://aider.chat/docs/leaderboards/refactor.html"
LMARENA_URL = (
    "https://huggingface.co/spaces/lmarena-ai/chatbot-arena-leaderboard/resolve/main/"
    "leaderboard_table_20250804.csv"
)
ARENA_HARD_URL = (
    "https://huggingface.co/spaces/lmarena-ai/arena-leaderboard/resolve/main/"
    "arena_hard_auto_leaderboard_v0.1.csv"
)
# SWE-rebench 排行榜是 Next.js 应用，数据以 flight 流形式内联在 HTML 中。
# 它的结构是「一榜多期」：同一批模型在连续多个月份的评测切片上的分数，
# 因此需要同时保留模型维度与时间维度。
SWE_REBENCH_URL = "https://swe-rebench.com/leaderboard"

# 占位符：SWE-bench 用 "Undisclosed" / "Multiple" 表示模型未公开或多模型组合，
# 它们不是具体模型版本，不能当作一个模型收录。
PLACEHOLDER_MODELS = {"undisclosed", "multiple", "unknown", "n/a", "-"}


@dataclass
class Config:
    root: Path
    offline: bool = False
    validate_only: bool = False
    refresh: bool = False
    timeout: int = 120
    sources: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# 网络与缓存
# ---------------------------------------------------------------------------

def fetch(url: str, cfg: Config, cache_name: str) -> bytes:
    """取回原始响应；优先读缓存。缓存文件损坏时自动重新下载。

    大文件（如 SWE-bench 榜单 4MB）单次请求会被中途截断，
    因此按固定分块用 Range 请求逐段拉取并校验总长度。
    """
    cache = cfg.root / CACHE_DIR / cache_name
    if cache.exists() and not cfg.refresh:
        raw = cache.read_bytes()
        try:
            if cache_name.endswith(".json"):
                json.loads(raw.decode("utf-8"))
            return raw
        except (ValueError, UnicodeDecodeError):
            print(f"[cache] {cache_name} 损坏，重新下载", file=sys.stderr)

    if cfg.offline:
        raise FileNotFoundError(f"离线模式且无缓存: {cache_name}")

    cache.parent.mkdir(parents=True, exist_ok=True)
    total = _content_length(url, cfg)
    if total and total > CHUNK_SIZE:
        raw = _fetch_chunked(url, cfg, total, cache_name)
    else:
        raw = _fetch_whole(url, cfg, cache_name)
    if cache_name.endswith(".json"):
        json.loads(raw.decode("utf-8"))
    print(f"[fetch] {cache_name}: {len(raw)} bytes", file=sys.stderr)
    return raw


def _content_length(url: str, cfg: Config) -> int:
    """用 HEAD 探测内容长度；失败时返回 0（退化为整块下载）。"""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT}, method="HEAD")
        with urllib.request.urlopen(req, timeout=cfg.timeout) as resp:
            return int(resp.headers.get("Content-Length") or 0)
    except (urllib.error.URLError, OSError, ValueError):
        return 0


def _fetch_whole(url: str, cfg: Config, cache_name: str) -> bytes:
    last: Exception | None = None
    for attempt in range(1, 6):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=cfg.timeout) as resp:
                body = resp.read()
            (cfg.root / CACHE_DIR / cache_name).write_bytes(body)
            return body
        except (urllib.error.URLError, OSError) as exc:
            last = exc
            print(f"[fetch] {cache_name} 第 {attempt} 次失败: {exc}", file=sys.stderr)
    raise RuntimeError(f"抓取失败: {url} ({last})")


def _fetch_chunked(url: str, cfg: Config, total: int, cache_name: str) -> bytes:
    """按 CHUNK_SIZE 分块 Range 请求，规避大文件单次传输被截断。"""
    out = cfg.root / CACHE_DIR / cache_name
    parts: list[bytes] = []
    got = 0
    attempt = 0
    while got < total and attempt < 60:
        attempt += 1
        start = got
        end = min(got + CHUNK_SIZE, total) - 1
        req = urllib.request.Request(
            url, headers={"User-Agent": USER_AGENT, "Range": f"bytes={start}-{end}"}
        )
        try:
            with urllib.request.urlopen(req, timeout=cfg.timeout) as resp:
                body = resp.read()
                if resp.status != 206:
                    # 服务端忽略 Range：退回整块下载
                    print(f"[fetch] {cache_name}: 服务端忽略 Range，改整块下载", file=sys.stderr)
                    return _fetch_whole(url, cfg, cache_name)
            if not body:
                raise OSError("空响应")
            parts.append(body)
            got += len(body)
        except (urllib.error.URLError, OSError) as exc:
            print(f"[fetch] {cache_name} 分块 {start} 第 {attempt} 次失败: {exc}", file=sys.stderr)
            time.sleep(1.5)
    if got < total:
        raise RuntimeError(f"抓取不完整: {cache_name} 仅得 {got}/{total} 字节")
    raw = b"".join(parts)
    out.write_bytes(raw)
    return raw


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()[:16]


# ---------------------------------------------------------------------------
# 解析：SWE-bench 官方榜单（5 个子榜）
# ---------------------------------------------------------------------------

# SWE-bench 子榜 -> 中文名与口径说明。resolved 的含义是「被解决的问题比例」，
# 因此单位为百分比、方向为越高越好，且**分数受 agent 脚手架影响**，
# 同一模型换 agent 会得到不同分数，不能跨 agent 直接比大小。
SWE_BENCH_BOARDS = {
    "Verified": {
        "label": "SWE-bench Verified",
        "scope": "SWE-bench Verified（500 题人工确认可解子集），resolved 为已解决比例；"
                 "分数同时取决于模型与 agent 脚手架，跨 agent 不可直接比较",
    },
    "Lite": {
        "label": "SWE-bench Lite",
        "scope": "SWE-bench Lite（300 题），resolved 为已解决比例；"
                 "分数同时取决于模型与 agent 脚手架，跨 agent 不可直接比较",
    },
    "Test": {
        "label": "SWE-bench Test",
        "scope": "SWE-bench Test（内部测试集），resolved 为已解决比例；"
                 "分数同时取决于模型与 agent 脚手架，跨 agent 不可直接比较",
    },
    "Multilingual": {
        "label": "SWE-bench Multilingual",
        "scope": "SWE-bench Multilingual（多语言扩展子集），resolved 为已解决比例",
    },
    "Multimodal": {
        "label": "SWE-bench Multimodal",
        "scope": "SWE-bench Multimodal（多模态子集），resolved 为已解决比例",
    },
}


def parse_swebench(raw: bytes) -> tuple[list[dict], list[dict]]:
    data = json.loads(raw.decode("utf-8"))
    boards = {b["name"]: b.get("results", []) for b in data.get("leaderboards", [])}

    sources: list[dict] = []
    observations: list[dict] = []

    for board_key, meta in SWE_BENCH_BOARDS.items():
        results = boards.get(board_key)
        if not results:
            continue
        source_id = f"swebench_{board_key.lower()}"
        sources.append({
            "id": source_id,
            "level": "A",
            "url": "https://www.swebench.com/",
            "data_url": SWE_BENCH_URL,
            "ref": f"SWE-bench 官方 leaderboards.json · {board_key}",
            "note": "SWE-bench 官方榜单原始 JSON，条目为该子榜全部参评记录",
            "captured": "",
        })

        for row in results:
            model_raw = str(row.get("model_display") or "").strip()
            if not model_raw or model_raw.lower() in PLACEHOLDER_MODELS:
                # 「Undisclosed」「Multiple」不是具体模型版本，无法归一化，
                # 收录会污染模型维度；此处剔除但记录条目数以便口径说明。
                continue
            resolved = row.get("resolved")
            if not isinstance(resolved, (int, float)) or isinstance(resolved, bool):
                continue

            agent = str(row.get("agent") or "").strip()
            effort = str(row.get("reasoning_effort") or "").strip()
            org = str(row.get("model_org") or "").strip()
            date = str(row.get("date") or "").strip()
            release = row.get("model_release_date")
            release_s = str(release) if release not in (None, "None") else ""

            # 榜单内的条目身份 = 模型 + agent + reasoning effort。
            # 只用模型名做键会把不同脚手架的分数混为一谈。
            entry_id = "|".join([
                model_raw,
                agent or "—",
                effort or "—",
            ])

            observations.append({
                "board": source_id,
                "board_label": meta["label"],
                "model_raw": model_raw,
                "provider_raw": org,
                "metric_key": "resolved_rate",
                "metric_label": "已解决问题比例",
                "metric_unit": "percent",
                "metric_max": 100,
                "value": round(float(resolved), 2),
                "rank": None,
                "date": date,
                "entry_id": entry_id,
                "agent": agent,
                "reasoning_effort": effort,
                "model_release_date": release_s,
                "note": (f"agent: {agent}" if agent else "") +
                        (f" · reasoning effort: {effort}" if effort else ""),
                "src": source_id,
            })

    return observations, sources


# ---------------------------------------------------------------------------
# 解析：Aider polyglot 官方榜单
# ---------------------------------------------------------------------------

def parse_aider(raw: bytes) -> tuple[list[dict], list[dict]]:
    text = raw.decode("utf-8", "replace")
    tables = re.findall(r"<table.*?</table>", text, re.S)
    if not tables:
        return [], []

    rows = re.findall(r"<tr.*?</tr>", tables[0], re.S)
    parsed: list[dict] = []
    for row in rows[1:]:
        cells = [
            H.unescape(re.sub("<[^>]+>", "", c)).strip()
            for c in re.findall(r"<t[dh].*?</t[dh]>", row, re.S)
        ]
        if len(cells) < 7:
            continue
        model_raw = cells[1]
        pct = re.match(r"([\d.]+)%", cells[2])
        if not model_raw or not pct:
            continue
        parsed.append({
            "model_raw": model_raw,
            "pct": float(pct.group(1)),
            "cost": cells[3],
            "command": cells[4],
            "edit_rate": cells[5],
            "edit_format": cells[6],
        })

    sources = [{
        "id": "aider_polyglot",
        "level": "A",
        "url": "https://aider.chat/docs/leaderboards/",
        "data_url": AIDER_URL,
        "ref": "Aider 官方 polyglot 榜单页",
        "note": "Aider 官方文档站榜单表格，含全部参评模型条目",
        "captured": "",
    }]

    observations = []
    for p in parsed:
        # 模型名自带配置后缀（如 gpt-5 (high)），必须整体保留：
        # 去掉后缀会把不同推理档位合并成同一模型，丢失可比较性信息。
        observations.append({
            "board": "aider_polyglot",
            "board_label": "Aider polyglot（exercism）",
            "model_raw": p["model_raw"],
            "provider_raw": "",
            "metric_key": "pass_rate",
            "metric_label": "测试通过率",
            "metric_unit": "percent",
            "metric_max": 100,
            "value": p["pct"],
            "rank": None,
            "date": "",
            "entry_id": p["model_raw"],
            "agent": "aider " + (p["edit_format"] or ""),
            "reasoning_effort": "",
            "model_release_date": "",
            "note": (f"成本 {p['cost']}" if p["cost"] else "") +
                    (f" · 编辑格式 {p['edit_format']}" if p["edit_format"] else "") +
                    (f" · 命令 {p['command']}" if p["command"] else ""),
            "src": "aider_polyglot",
        })

    return observations, sources


# ---------------------------------------------------------------------------
# 解析：LMArena 官方榜单 CSV
# ---------------------------------------------------------------------------

def parse_lmarena(raw: bytes) -> tuple[list[dict], list[dict]]:
    """LMArena 官方导出的 leaderboard_table CSV。

    该表包含两个**单位不同**的指标：MT-bench（1–10 分）与 MMLU（0–1 比例）。
    二者不可同榜比较，因此拆成两个独立榜单，各自独立排名。
    """
    text = raw.decode("utf-8", "replace")
    rows = list(csv.DictReader(io.StringIO(text)))
    if not rows or "Model" not in (rows[0].keys() if rows else {}):
        return [], []

    sources = [
        {
            "id": "lmarena_mtbench",
            "level": "A",
            "url": "https://lmarena.ai/leaderboard",
            "data_url": LMARENA_URL,
            "ref": "LMArena 官方 leaderboard_table CSV · MT-bench (score)",
            "note": "LMArena 官方 Space 导出的榜单表，含全部参评模型条目",
            "captured": "",
        },
        {
            "id": "lmarena_mmlu",
            "level": "A",
            "url": "https://lmarena.ai/leaderboard",
            "data_url": LMARENA_URL,
            "ref": "LMArena 官方 leaderboard_table CSV · MMLU",
            "note": "LMArena 官方 Space 导出的榜单表，含全部参评模型条目",
            "captured": "",
        },
    ]

    def num(row: dict, key: str) -> float | None:
        v = (row.get(key) or "").strip()
        if not v or v.startswith("-"):
            return None
        m = re.match(r"([\d.]+)", v)
        return float(m.group(1)) if m else None

    observations = []
    seen_models: set[str] = set()
    for row in rows:
        model_raw = (row.get("Model") or "").strip()
        if not model_raw:
            continue
        # 该表存在同一模型被登记多行的情况（如 gemini-1.5-pro-api-0514 与
        # gemini-1.5-pro-001 同名同分），按模型名去重，保留首次出现的条目，
        # 避免同一模型在同一榜出现两条观测。
        if model_raw in seen_models:
            continue
        mt = num(row, "MT-bench (score)")
        mmlu = num(row, "MMLU")
        if mt is None and mmlu is None:
            # 两个指标都没值的行（如 chatgpt-4o-latest 两列均为 -）不含信息，跳过
            continue
        seen_models.add(model_raw)

        org = (row.get("Organization") or "").strip()
        cutoff = (row.get("Knowledge cutoff date") or "").strip()
        lic = (row.get("License") or "").strip()
        note = (f"知识截止 {cutoff}" if cutoff else "") + (f" · 许可 {lic}" if lic else "")

        if mt is not None:
            observations.append({
                "board": "lmarena_mtbench",
                "board_label": "LMArena · MT-bench",
                "model_raw": model_raw,
                "provider_raw": org,
                "metric_key": "mt_bench",
                "metric_label": "MT-bench 分",
                "metric_unit": "score",
                "metric_max": 10,
                "value": mt,
                "rank": None,
                "date": "",
                "entry_id": model_raw,
                "agent": "",
                "reasoning_effort": "",
                "model_release_date": "",
                "note": note,
                "src": "lmarena_mtbench",
            })

        if mmlu is not None:
            observations.append({
                "board": "lmarena_mmlu",
                "board_label": "LMArena · MMLU",
                "model_raw": model_raw,
                "provider_raw": org,
                "metric_key": "mmlu",
                "metric_label": "MMLU",
                "metric_unit": "percent",
                "metric_max": 1,
                "value": round(mmlu * 100, 1),
                "rank": None,
                "date": "",
                "entry_id": model_raw,
                "agent": "",
                "reasoning_effort": "",
                "model_release_date": "",
                "note": note + "（原表为 0–1 比例，已换算为百分比）",
                "src": "lmarena_mmlu",
            })

    return observations, sources


# ---------------------------------------------------------------------------
# 解析：SWE-rebench 官方排行榜（一榜多期）
# ---------------------------------------------------------------------------

def parse_swe_rebench(raw: bytes) -> tuple[list[dict], list[dict]]:
    """SWE-rebench 排行榜。

    与其他榜不同，它不是「一个榜一个分数」，而是**同一批模型在连续多个月份的
    评测切片上的分数**（如 2025-01 ~ 2026-06 共 18 期）。页面是 Next.js 应用，
    数据以 flight 流形式内联在 HTML 中，需要先把流拼回完整字符串再抽 JSON。

    模型名带两种配置标注，必须保留：
      * ``[high]`` / ``[medium]`` —— 推理档位
      * ``(text)`` / ``(tools)``  —— 调用模式
    """
    text = raw.decode("utf-8", "replace")
    chunks: list[str] = []
    for m in re.finditer(r'self\.__next_f\.push\(\[1,"((?:[^"\\]|\\.)*)"\]\)', text):
        try:
            chunks.append(json.loads('"' + m.group(1) + '"'))
        except ValueError:
            continue
    if not chunks:
        return [], []
    blob = "".join(chunks)

    # 逐个定位 {"data":[{"type":"line","name":... 的图表数组并括号配平。
    # 真实页面里 JSON 无空格，但测试样例经 json.dumps 后可能带空格，故允许空白。
    arrays: list[tuple[list[str], list[dict]]] = []
    for m in re.finditer(r'\{"data":\s*\[\s*\{"type":\s*"line"', blob):
        start = m.start()
        depth = 0
        i = start
        while i < len(blob):
            c = blob[i]
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    break
            i += 1
        raw_arr = blob[start : i + 1]
        try:
            arr = json.loads(raw_arr)
        except ValueError:
            continue
        pre = blob[max(0, start - 800) : start]
        cats_raw = re.findall(r'"categories":\[([^\]]*)\]', pre)
        cats: list[str] = []
        if cats_raw:
            try:
                cats = json.loads("[" + cats_raw[-1] + "]")
            except ValueError:
                cats = []
        arrays.append((cats, arr.get("data", [])))

    if not arrays:
        return [], []

    sources = [{
        "id": "swe_rebench",
        "level": "A",
        "url": "https://swe-rebench.com/leaderboard",
        "data_url": SWE_REBENCH_URL,
        "ref": "SWE-rebench 官方排行榜页面内嵌数据（Next.js flight 流）",
        "note": "由 Nebius 维护的 SWE-rebench 排行榜，模型在连续多个月的评测切片上的分数",
        "captured": "",
    }]

    observations: list[dict] = []
    # 同一个模型可能在多个图表数组里出现（页面按不同视图重复渲染），
    # 这里以 (条目, 期间, 指标) 去重。
    seen: set[tuple[str, str, str]] = set()

    for cats, series in arrays:
        # 该数组覆盖的月份：优先用 categories 与实际数据点的交集
        points: set[str] = set()
        for s in series:
            for p in s.get("data", []):
                points.add(p["x"])
        periods = sorted(points, key=lambda x: (len(x), x))
        if not periods:
            continue

        for s in series:
            name = str(s.get("name") or "").strip()
            if not name:
                continue
            # 拆出配置：模型本体 / 推理档位 / 调用模式
            base = name
            effort = ""
            mode = ""
            m_eff = re.search(r"\[([^\]]+)\]", base)
            if m_eff:
                effort = m_eff.group(1)
                base = base.replace(m_eff.group(0), "").strip()
            m_mode = re.search(r"\(([^)]+)\)\s*$", base)
            if m_mode:
                mode = m_mode.group(1)
                base = base[: m_mode.start()].strip()

            for p in s.get("data", []):
                period = str(p.get("x") or "")
                val = p.get("y")
                if not period or not isinstance(val, (int, float)):
                    continue
                # 同一模型在不同评测期的分数是不同数据点，
                # 条目身份必须含评测期，否则会被去重逻辑吃掉。
                entry_id = f"{name}@{period}"
                pk = (entry_id, "resolved_rate")
                if pk in seen:
                    continue
                seen.add(pk)
                observations.append({
                    "board": "swe_rebench",
                    "board_label": "SWE-rebench",
                    "model_raw": name,
                    "provider_raw": "",
                    "metric_key": "resolved_rate",
                    "metric_label": "已解决问题比例",
                    "metric_unit": "percent",
                    "metric_max": 100,
                    "value": round(float(val), 2),
                    "rank": None,
                    "date": _period_to_date(period),
                    "entry_id": entry_id,
                    "agent": mode,
                    "reasoning_effort": effort,
                    "model_release_date": "",
                    "note": (f"评测期 {period}" +
                            (f" · 推理档位 {effort}" if effort else "") +
                            (f" · 调用模式 {mode}" if mode else "")),
                    "src": "swe_rebench",
                    # 该源特有字段：期间
                    "period": period,
                })

    return observations, sources


_MONTHS = {
    "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06",
    "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12",
}


def _period_to_date(period: str) -> str:
    """把 "Mar 2026" 这样的期间标签转成 "2026-03"（仅到月，无日）。"""
    m = re.match(r"([A-Z][a-z]{2})\s+(\d{4})", period.strip())
    if not m:
        return ""
    mon = _MONTHS.get(m.group(1))
    return f"{m.group(2)}-{mon}" if mon else ""


# ---------------------------------------------------------------------------
# 解析：Aider edit / refactor 榜
# ---------------------------------------------------------------------------

AIDER_TABLES = {
    "aider_edit": {
        "url": AIDER_EDIT_URL,
        "label": "Aider edit（代码编辑）",
        "scope": "Aider 官方 edit 榜；测的是把代码编辑成目标形态的成功率，"
                 "与 polyglot 榜（多语言编程题）任务不同，分数不可互相比较",
        "metric_label": "正确完成率",
    },
    "aider_refactor": {
        "url": AIDER_REFACTOR_URL,
        "label": "Aider refactor（代码重构）",
        "scope": "Aider 官方 refactor 榜；测的是重构既有代码的正确率，"
                 "与 polyglot / edit 榜任务不同，分数不可互相比较",
        "metric_label": "正确完成率",
    },
}


def parse_aider_tables(raw: bytes, board_id: str) -> tuple[list[dict], list[dict]]:
    """解析 Aider 的 edit / refactor 榜单页。

    两页的表结构与 polyglot **不同**：
      * polyglot 7 列：标记列 / Model / Percent / Cost / Command / Edit rate / Edit format
      * edit 与 refactor 5 列：Model / Percent / Command / Edit format（无标记列与成本列）
    """
    meta = AIDER_TABLES[board_id]
    text = raw.decode("utf-8", "replace")
    tables = re.findall(r"<table.*?</table>", text, re.S)
    if not tables:
        return [], []
    rows = re.findall(r"<tr.*?</tr>", tables[0], re.S)

    parsed: list[dict] = []
    for row in rows[1:]:
        cells = [
            H.unescape(re.sub("<[^>]+>", "", c)).strip()
            for c in re.findall(r"<t[dh].*?</t[dh]>", row, re.S)
        ]
        if len(cells) >= 7:
            model_raw = cells[1]
            pct = re.match(r"([\d.]+)%", cells[2])
            cost, command, edit_rate, edit_format = cells[3], cells[4], cells[5], cells[6]
        elif len(cells) >= 5:
            model_raw = cells[0]
            pct = re.match(r"([\d.]+)%", cells[1])
            cost, command, edit_rate, edit_format = "", cells[2], "", cells[4]
        else:
            continue
        if not model_raw or not pct:
            continue
        parsed.append({
            "model_raw": model_raw,
            "pct": float(pct.group(1)),
            "cost": cost,
            "command": command,
            "edit_rate": edit_rate,
            "edit_format": edit_format,
        })

    sources = [{
        "id": board_id,
        "level": "A",
        "url": meta["url"],
        "data_url": meta["url"],
        "ref": f"Aider 官方 {board_id.split('_')[1]} 榜单页",
        "note": "Aider 官方文档站榜单表格，含全部参评模型条目",
        "captured": "",
    }]

    observations = []
    for p in parsed:
        observations.append({
            "board": board_id,
            "board_label": meta["label"],
            "model_raw": p["model_raw"],
            "provider_raw": "",
            "metric_key": "pass_rate",
            "metric_label": meta["metric_label"],
            "metric_unit": "percent",
            "metric_max": 100,
            "value": p["pct"],
            "rank": None,
            "date": "",
            "entry_id": p["model_raw"],
            "agent": "aider " + (p["edit_format"] or ""),
            "reasoning_effort": "",
            "model_release_date": "",
            "note": (f"成本 {p['cost']}" if p["cost"] else "") +
                    (f" · 编辑格式 {p['edit_format']}" if p["edit_format"] else ""),
            "src": board_id,
        })
    return observations, sources


# ---------------------------------------------------------------------------
# 解析：Arena-Hard-Auto 榜
# ---------------------------------------------------------------------------

def parse_arena_hard(raw: bytes) -> tuple[list[dict], list[dict]]:
    """LMArena 官方 Space 导出的 Arena-Hard-Auto 榜。

    该表带 Bradley-Terry 评分的置信区间与平均 token 消耗；
    置信区间说明**分数本身有统计误差**，不能按点估计精确排序。
    """
    text = raw.decode("utf-8", "replace")
    rows = list(csv.DictReader(io.StringIO(text)))
    if not rows or "model" not in (rows[0].keys() if rows else {}):
        return [], []

    sources = [{
        "id": "arena_hard_auto",
        "level": "A",
        "url": "https://lmarena.ai/leaderboard",
        "data_url": ARENA_HARD_URL,
        "ref": "LMArena 官方 Space · arena_hard_auto_leaderboard_v0.1.csv",
        "note": "Arena-Hard-Auto 自动评测榜，含置信区间与平均 token 消耗",
        "captured": "",
    }]

    observations = []
    for row in rows:
        model_raw = (row.get("model") or "").strip()
        if not model_raw:
            continue
        try:
            score = float(row.get("score") or "")
        except ValueError:
            continue
        lo = (row.get("rating_q025") or "").strip()
        hi = (row.get("rating_q975") or "").strip()
        ci = (row.get("CI") or "").strip()
        tok = (row.get("avg_tokens") or "").strip()
        date = (row.get("date") or "").strip()

        observations.append({
            "board": "arena_hard_auto",
            "board_label": "Arena-Hard-Auto",
            "model_raw": model_raw,
            "provider_raw": "",
            "metric_key": "arena_hard_score",
            "metric_label": "Arena-Hard-Auto 分数",
            "metric_unit": "score",
            "metric_max": 100,
            "value": score,
            "rank": None,
            "date": date,
            "entry_id": model_raw,
            "agent": "",
            "reasoning_effort": "",
            "model_release_date": "",
            "note": (f"95% 置信区间 {lo}–{hi}" if lo and hi else "") +
                    (f" · CI {ci}" if ci else "") +
                    (f" · 平均 {tok} tokens" if tok else ""),
            "src": "arena_hard_auto",
        })

    return observations, sources


# ---------------------------------------------------------------------------
# 模型归一化
# ---------------------------------------------------------------------------

# 提供方别名 → 统一名。榜单里的 org 字段写法不统一（Mistral/mistral、Moonshot AI…）。
PROVIDER_ALIASES = {
    "mistral": "Mistral AI",
    "mistral ai": "Mistral AI",
    "moonshot ai": "月之暗面",
    "moonshotai": "月之暗面",
    "google deepmind": "Google",
    "deepmind": "Google",
    "z.ai": "智谱 AI",
    "zhipu": "智谱 AI",
    "zai": "智谱 AI",
    "minimax": "MiniMax",
    "alibaba": "阿里巴巴",
    "qwen": "阿里巴巴",
    "meta ai": "Meta",
    "meta-llama": "Meta",
    "openai": "OpenAI",
    "anthropic": "Anthropic",
    "google": "Google",
    "x-ai": "xAI",
    "xai": "xAI",
    "deepseek": "DeepSeek",
    "microsoft": "Microsoft",
    "nvidia": "NVIDIA",
    "amazon": "Amazon",
    "cohere": "Cohere",
    "cohere labs": "Cohere",
    "baidu": "百度",
    "tencent": "腾讯",
    "bytedance": "字节跳动",
    "seed": "字节跳动",
    "moonshot": "月之暗面",
    "01 ai": "零一万物",
    "inclusion ai": "零一万物",
}

# 从模型名里识别提供方（org 字段缺失时兜底）。
MODEL_PROVIDER_HINTS = [
    ("gpt-", "OpenAI"), ("o1", "OpenAI"), ("o3", "OpenAI"), ("o4", "OpenAI"),
    ("claude", "Anthropic"), ("gemini", "Google"), ("gemma", "Google"),
    ("llama", "Meta"), ("qwen", "阿里巴巴"), ("qwq", "阿里巴巴"),
    ("deepseek", "DeepSeek"), ("kimi", "月之暗面"), ("moonshot", "月之暗面"),
    ("glm", "智谱 AI"), ("minimax", "MiniMax"), ("mistral", "Mistral AI"),
    ("mixtral", "Mistral AI"), ("magistral", "Mistral AI"),
    ("grok", "xAI"), ("doubao", "字节跳动"), ("seed-", "字节跳动"),
    ("ernie", "百度"), ("hunyuan", "腾讯"), ("step-", "阶跃星辰"),
    ("nova", "Amazon"), ("phi-", "Microsoft"), ("command", "Cohere"),
    ("yi-", "零一万物"), ("ling-", "蚂蚁集团"), ("gpt4", "OpenAI"),
]


def normalize_provider(raw: str, model_raw: str) -> str:
    key = (raw or "").strip().lower()
    if key in PROVIDER_ALIASES:
        return PROVIDER_ALIASES[key]
    low = model_raw.lower()
    for prefix, name in MODEL_PROVIDER_HINTS:
        if low.startswith(prefix):
            return name
    return raw.strip() or "未标注"


def normalize_model(model_raw: str) -> str:
    """把榜单里的模型写法归一为项目口径的展示名。

    原则：**只做空白、大小写与常见分隔符的规整，不合并不同版本**。
    "gpt-5 (high)" 与 "gpt-5 (low)" 是不同配置，必须保持可区分；
    因此这里只去掉首尾空白并统一多余空格。
    """
    s = re.sub(r"\s+", " ", model_raw.strip())
    return s


def build_boards(cfg: Config) -> dict:
    """抓取并解析全部榜单源，返回合并后的板级数据。"""
    now = dt.datetime.now(dt.timezone.utc)
    captured = now.strftime("%Y-%m-%d")

    all_obs: list[dict] = []
    all_sources: list[dict] = []

    plan = [
        ("swebench", SWE_BENCH_URL, "swebench_leaderboards.json", parse_swebench),
        ("aider", AIDER_URL, "aider_polyglot.html", parse_aider),
        ("lmarena", LMARENA_URL, "lmarena_leaderboard.csv", parse_lmarena),
        ("swerebench", SWE_REBENCH_URL, "swe_rebench_leaderboard.html", parse_swe_rebench),
        ("aideredit", AIDER_EDIT_URL, "aider_edit.html",
         lambda raw: parse_aider_tables(raw, "aider_edit")),
        ("aiderrefactor", AIDER_REFACTOR_URL, "aider_refactor.html",
         lambda raw: parse_aider_tables(raw, "aider_refactor")),
        ("arenahard", ARENA_HARD_URL, "arena_hard_auto.csv", parse_arena_hard),
    ]

    for key, url, cache_name, parser in plan:
        if cfg.sources and key not in cfg.sources:
            continue
        try:
            raw = fetch(url, cfg, cache_name)
        except (RuntimeError, FileNotFoundError) as exc:
            print(f"[skip] {key}: {exc}", file=sys.stderr)
            continue
        obs, srcs = parser(raw)
        if not obs:
            print(f"[skip] {key}: 未解析到条目", file=sys.stderr)
            continue
        for s in srcs:
            s["captured"] = captured
            s["sha256"] = sha256(raw)
        all_obs.extend(obs)
        all_sources.extend(srcs)
        print(f"[ok] {key}: {len(obs)} 条观测 / {len(srcs)} 个来源", file=sys.stderr)

    # 去重：同一 board 内 (entry_id, metric_key) 必须唯一
    seen: set[tuple[str, str]] = set()
    deduped: list[dict] = []
    for o in all_obs:
        pk = (o["board"], o["entry_id"], o["metric_key"])
        if pk in seen:
            continue
        seen.add(pk)
        deduped.append(o)

    # 补齐归一化字段
    for o in deduped:
        o["model"] = normalize_model(o["model_raw"])
        o["provider"] = normalize_provider(o.get("provider_raw", ""), o["model_raw"])

    # 指标元数据：单位与值域由 metric 决定（同一榜内不同指标单位可能不同，
    # 例如 MT-bench 是 1–10 分、MMLU 是 0–1 比例），因此从观测派生并去重。
    metrics: dict[str, dict] = {}
    for o in deduped:
        mk = o["metric_key"]
        unit = o.get("metric_unit", "percent")
        vmax = o.get("metric_max")
        if mk not in metrics:
            metrics[mk] = {
                "key": mk,
                "label": o["metric_label"],
                "unit": unit,
                "max": vmax,
                "boards": sorted({x["board"] for x in deduped if x["metric_key"] == mk}),
            }
        else:
            m = metrics[mk]
            if m["unit"] != unit:
                raise ValueError(f"指标 {mk} 单位冲突: {m['unit']} vs {unit}")
            m["boards"] = sorted(set(m["boards"]) | {o["board"]})

    # 每个 board 内按 metric 计算排名（同 metric、同 board 内排名才有效）。
    # 一榜多期的源（如 SWE-rebench 逐月榜单）必须**按评测期分组**后再排名，
    # 否则跨期混排得到的名次没有任何意义。
    by_board_metric: dict[tuple[str, str, str], list[dict]] = {}
    for o in deduped:
        period = str(o.get("period") or "")
        by_board_metric.setdefault((o["board"], o["metric_key"], period), []).append(o)
    for group in by_board_metric.values():
        group.sort(key=lambda x: -x["value"])
        for i, o in enumerate(group, 1):
            o["rank"] = i

    boards = {}
    for s in all_sources:
        bobs = [o for o in deduped if o["board"] == s["id"]]
        bid = s["id"]
        if bid.startswith("swebench_"):
            scope = SWE_BENCH_BOARDS.get(bid.replace("swebench_", "").title(), {}).get("scope", "")
        elif bid == "aider_polyglot":
            scope = ("Aider polyglot（exercism）官方榜单；分数取决于模型与 aider 编辑格式，"
                     "跨编辑格式不可直接比较")
        elif bid == "lmarena_mtbench":
            scope = "LMArena 官方榜单 MT-bench 列（1–10 分）；与 MMLU 列单位不同，已单独成榜"
        elif bid == "lmarena_mmlu":
            scope = ("LMArena 官方榜单 MMLU 列（原表 0–1 比例，此处换算为百分比）；"
                     "与 MT-bench 列单位不同，已单独成榜")
        elif bid == "swe_rebench":
            scope = ("SWE-rebench 官方排行榜（Nebius 维护）：模型在**连续多个月的评测切片**上的"
                     "已解决比例。同一条目对应多个评测期（2025-01 ~ 2026-06），"
                     "不同期的任务集不同，**分数不可跨期直接比较**；"
                     "模型名带推理档位 [high/medium] 与调用模式 (text/tools) 标注")
        elif bid == "aider_edit":
            scope = ("Aider 官方 edit 榜：把代码编辑成目标形态的成功率；"
                     "与 polyglot 榜（多语言编程题）、refactor 榜任务不同，分数不可互相比较")
        elif bid == "aider_refactor":
            scope = ("Aider 官方 refactor 榜：重构既有代码的正确率；"
                     "与 polyglot 榜（多语言编程题）、edit 榜任务不同，分数不可互相比较")
        elif bid == "arena_hard_auto":
            scope = ("LMArena 官方 Arena-Hard-Auto 榜：自动评测的困难提示词集，"
                     "分数为 Bradley-Terry 评分，**带 95% 置信区间**，"
                     "点估计相近时不应据此强行排序")
        else:
            scope = ""
        boards[bid] = {
            "id": bid,
            "label": bobs[0]["board_label"] if bobs else bid,
            "scope": scope,
            "kind": "leaderboard",
            "metrics": sorted({o["metric_key"] for o in bobs}),
            "source": s,
            "entries": len({o["entry_id"] for o in bobs}),
            "observations": len(bobs),
            "models": len({o["model"] for o in bobs}),
        }

    return {
        "meta": {
            "version": "1.0",
            "updated": captured,
            "principle": "本文件只收录来自一手公开榜单的官方分数。榜单条目 = 模型 × 配置"
                         "（agent 脚手架 / reasoning effort / 编辑格式），"
                         "同一模型换配置分数不同，因此条目身份由 (board, entry_id, metric) 唯一确定，"
                         "不得把不同配置的分数合并成一个「模型分」。",
            "roster_note": "boards[].entries / models 是该榜单官方公布的参评规模，"
                           "与项目 §2.0 已核实清单是两套口径：前者是「榜单里有哪些模型」，"
                           "后者是「项目收录了哪些模型」。差异在看板上以覆盖率呈现。",
            "exclusion_note": "SWE-bench 榜单中的 Undisclosed / Multiple 为占位条目"
                               "（模型未公开或多模型组合），不是具体模型版本，已剔除。",
            "metric_note": "单位与值域由 metric 定义；同一榜内不同指标单位可能不同，"
                           "换算过的值在观测 note 中注明。",
        },
        "boards": list(boards.values()),
        "metrics": list(metrics.values()),
        "sources": all_sources,
        "observations": deduped,
    }


# ---------------------------------------------------------------------------
# 校验
# ---------------------------------------------------------------------------

def validate(data: dict) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    boards = {b["id"]: b for b in data.get("boards", [])}
    sources = {s["id"]: s for s in data.get("sources", [])}
    metrics = {m["key"]: m for m in data.get("metrics", [])}
    obs = data.get("observations", [])

    if not boards:
        errors.append("缺少 boards")
    if not sources:
        errors.append("缺少 sources")
    if not metrics:
        errors.append("缺少 metrics")
    if not obs:
        errors.append("缺少 observations")
        return errors, warnings

    for mid, m in metrics.items():
        if m.get("unit") not in ("percent", "score"):
            errors.append(f"指标 {mid}: 非法 unit {m.get('unit')}")
        if not m.get("label"):
            errors.append(f"指标 {mid}: 缺少 label")
        if not m.get("boards"):
            errors.append(f"指标 {mid}: 未声明所属榜单")

    for bid, b in boards.items():
        if not b.get("scope"):
            errors.append(f"榜单 {bid}: 缺少口径说明 scope")
        if bid not in sources:
            errors.append(f"榜单 {bid}: 缺少对应来源")
        for mk in b.get("metrics", []):
            if mk not in metrics:
                errors.append(f"榜单 {bid}: 引用未知指标 {mk}")

    for sid, s in sources.items():
        if not str(s.get("url", "")).startswith("https://"):
            errors.append(f"来源 {sid}: 非 HTTPS 链接")
        if s.get("level") != "A":
            errors.append(f"来源 {sid}: 榜单来源必须为 A 级一手")
        if not s.get("captured"):
            errors.append(f"来源 {sid}: 缺少抓取日期 captured")
        if not s.get("sha256"):
            errors.append(f"来源 {sid}: 缺少内容指纹 sha256")

    seen: set[tuple] = set()
    for i, o in enumerate(obs, 1):
        for f in ("board", "model", "provider", "metric_key", "metric_label", "src"):
            if not o.get(f):
                errors.append(f"观测 {i}: 缺少字段 {f}")
        if o.get("board") not in boards:
            errors.append(f"观测 {i}: 未知榜单 {o.get('board')}")
        if o.get("src") not in sources:
            errors.append(f"观测 {i}: 未知来源 {o.get('src')}")
        mk = o.get("metric_key")
        if mk not in metrics:
            errors.append(f"观测 {i}: 未知指标 {mk}")
        v = o.get("value")
        if not isinstance(v, (int, float)) or isinstance(v, bool):
            errors.append(f"观测 {i}: value 必须是数值")
        else:
            unit = metrics.get(mk, {}).get("unit")
            vmax = metrics.get(mk, {}).get("max")
            if unit == "percent" and not (0 <= v <= 100):
                errors.append(f"观测 {i}: percent 越界 {v}")
            elif unit == "score" and vmax and not (0 <= v <= vmax):
                errors.append(f"观测 {i}: score 越界 {v}（上限 {vmax}）")
        pk = (o.get("board"), o.get("entry_id"), o.get("metric_key"))
        if pk in seen:
            errors.append(f"观测 {i}: 主键重复 {pk}")
        seen.add(pk)
        if not o.get("entry_id"):
            errors.append(f"观测 {i}: 缺少 entry_id（条目身份）")

    # 榜单声明的条目数与观测数必须一致
    for bid, b in boards.items():
        bobs = [o for o in obs if o["board"] == bid]
        actual_entries = len({o["entry_id"] for o in bobs})
        if actual_entries != b.get("entries"):
            errors.append(
                f"榜单 {bid}: 声明 entries={b.get('entries')} 但实际 {actual_entries} 条"
            )
        if len(bobs) != b.get("observations"):
            errors.append(
                f"榜单 {bid}: 声明 observations={b.get('observations')} 但实际 {len(bobs)} 条"
            )
        if len({o["model"] for o in bobs}) != b.get("models"):
            errors.append(f"榜单 {bid}: 声明 models 数与实际不符")

    # 一榜多期的源：名次必须严格按评测期分组，
    # 否则会出现「某期只有 19 条却给出 rank=239」这类无意义名次。
    for bid, b in boards.items():
        bobs = [o for o in obs if o["board"] == bid]
        if not any(o.get("period") for o in bobs):
            continue
        by_period: dict[str, list[dict]] = {}
        for o in bobs:
            by_period.setdefault(str(o.get("period") or ""), []).append(o)
        for period, group in by_period.items():
            ranks = sorted(o["rank"] for o in group if o.get("rank") is not None)
            if ranks != list(range(1, len(group) + 1)):
                errors.append(
                    f"榜单 {bid} 评测期 {period}: 名次非该期内连续 1..{len(group)}"
                )

    # 同一 entry 在同一榜内只能有一个指标值（不同指标除外）
    entry_metrics: dict[tuple[str, str], set[str]] = {}
    for o in obs:
        entry_metrics.setdefault((o["board"], o["entry_id"]), set()).add(o["metric_key"])
    for (bid, eid), mks in entry_metrics.items():
        if len(mks) > 1:
            errors.append(f"榜单 {bid} 条目 {eid}: 出现多个指标 {sorted(mks)}，口径应拆榜")

    return errors, warnings


# ---------------------------------------------------------------------------
# 运行
# ---------------------------------------------------------------------------

def run(cfg: Config) -> dict[str, bool]:
    root = cfg.root
    out_path = root / OUTPUT_FILE
    if cfg.validate_only:
        data = json.loads(out_path.read_text(encoding="utf-8"))
        errors, warnings = validate(data)
        for w in warnings:
            print(f"[warning] {w}", file=sys.stderr)
        if errors:
            for e in errors:
                print(f"[validate] ERROR: {e}", file=sys.stderr)
            raise ValueError(f"校验失败：{len(errors)} 项")
        print("[validate] OK: 榜单 / 来源 / 主键 / 值域 / 条目数 一致")
        return {"validated": True}

    data = build_boards(cfg)
    if not data["observations"]:
        raise RuntimeError("未抓取到任何榜单条目")
    errors, _ = validate(data)
    if errors:
        for e in errors:
            print(f"[error] {e}", file=sys.stderr)
        raise ValueError(f"抓取结果校验失败：{len(errors)} 项")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
    )
    print(
        f"[result] {len(data['observations'])} 条观测 / {len(data['boards'])} 个榜单 "
        f"/ {len({o['model'] for o in data['observations']})} 个模型 → {OUTPUT_FILE}",
        file=sys.stderr,
    )
    return {"written": True}


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=".", help="仓库根目录")
    p.add_argument("--offline", action="store_true", help="只用本地缓存，不联网")
    p.add_argument("--validate", action="store_true", help="只校验已有产物")
    p.add_argument("--refresh", action="store_true", help="忽略缓存重新抓取")
    p.add_argument("--timeout", type=int, default=120, help="单次请求超时（秒）")
    p.add_argument("--source", action="append", default=[], help="只抓指定源（可重复）")
    a = p.parse_args(argv)
    root = Path(a.root).resolve()
    cfg = Config(
        root=root,
        offline=a.offline,
        validate_only=a.validate,
        refresh=a.refresh,
        timeout=a.timeout,
        sources=a.source,
    )
    try:
        run(cfg)
    except (RuntimeError, OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f"[error] {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
