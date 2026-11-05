#!/usr/bin/env python3
"""每日从 Hugging Face Hub 拉取最新发布 / 更新且值得关注的模型。

零第三方依赖（仅标准库），可由 GitHub Actions 的定时任务直接调用。

产出（均相对于仓库根目录）：
    data/hf-daily/YYYY-MM-DD.md   当日归档日报（Git 可追溯）
    HF_DAILY.md                   最新一期快照（滚动覆盖）
    data/hf-daily/latest.json     机器可读结果
    data/hf-daily/seen.json       跨天去重与更新冷却状态
    README.md                     §2.0.8 marker 块（站点可见摘要）

重要：本脚本输出的是「机器抓取候选」，**未经人工核实**，
不并入 README §2.0.1–2.0.7 的三态清单，也不得作为确定内容引用。
经人工核实后才可迁入 🆕 新增项。

用法：
    python3 scripts/fetch_hf_models.py --dry-run
    python3 scripts/fetch_hf_models.py --lookback-hours 36 --top-n 12
    python3 scripts/fetch_hf_models.py --force          # 覆盖当天已生成的日报
    python3 scripts/fetch_hf_models.py --validate       # 只校验已有产物（CI 用）
    python3 scripts/fetch_hf_models.py --offline-fixture sample.json --dry-run
    python3 -m unittest scripts/test_fetch_hf_models.py
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, asdict, field
from pathlib import Path
from typing import Any

API_BASE = "https://huggingface.co/api/models"
HF_WEB = "https://huggingface.co"
USER_AGENT = "awesome-llm-model-list/hf-daily (+https://github.com/gatilin/model-list)"

MARKER_START = "<!-- HF_DAILY_START -->"
MARKER_END = "<!-- HF_DAILY_END -->"

# 三路数据源：热门榜带 trendingScore，创建榜捕获全新仓库，修改榜捕获版本更新。
FEEDS = (
    ("trending", "trendingScore"),
    ("created", "createdAt"),
    ("modified", "lastModified"),
)

# 官方 / 主要实验室组织。命中后放宽热度门槛、加分，且不被量化关键词直接排除。
OFFICIAL_ORGS = frozenset(
    x.lower()
    for x in (
        "openai", "anthropic", "google", "google-deepmind", "deepmind", "meta-llama",
        "mistralai", "Qwen", "deepseek-ai", "moonshotai", "MiniMaxAI", "zai-org",
        "THUDM", "internlm", "Shanghai_AI_Laboratory", "baidu", "tencent",
        "Tencent-Hunyuan", "ByteDance", "ByteDance-Seed", "XiaomiMiMo", "baichuan-inc",
        "01-ai", "StepFun", "stepfun-ai", "iFlytek", "openbmb", "nvidia", "NVIDIA",
        "microsoft", "apple", "ai2", "allenai", "cohere", "CohereLabs", "stabilityai",
        "black-forest-labs", "Lightricks", "Comfy-Org", "runwayml", "Kuaishou",
        "Wan-AI", "HunyuanVideo", "LiquidAI", "Pika-Labs", "Viggle", "unsloth",
        "HuggingFaceTB", "huggingface", "bigscience", "EleutherAI", "tiiuae",
        "ai21", "databricks", "Snowflake", "ServiceNow", "Salesforce", "amazon",
        "Mila", "rinna", "skytogether", "kyutai", "transformers", "ricursiveAI",
        "RecursiveAI", "OpenBMB", "ZhipuAI",
    )
)

# 派生 / 量化 / 个人微调仓库特征。非官方作者命中即排除，官方作者仅降权。
NOISE_TOKENS = (
    "gguf", "ggml", "-awq", "awq-", "gptq", "-exl2", "exl2", "-hqq", "bnb-4bit",
    "-int4", "-int8", "-fp8", "-nvfp4", "quantiz", "quantized", "-q4", "-q8",
    "-4bit", "-8bit", "-bnb", "-onnx", "-mlx", "abliterat", "uncensored", "heretic",
    "-lora", "lora-", "-merge", "backup", "-copy", "-test", "-demo", "-tmp",
    "-finetune", "-distill", "reverseengineer", "primal_vae",
)

# 「跨组织再分发」判定：仓库名干净但 base_model 指向别家，且属于纯再打包格式。
# 这类仓库即使作者是知名组织，也不是原厂模型发布（如 ComfyUI 单文件、GGUF 量化）。
# 有独立技术贡献的后训练模型（如 Pika-H3-Flex）不在此列，因此只匹配明确的再打包标记。
REDISTRIBUTION_LIBS = frozenset({"diffusion-single-file", "gguf"})
REDISTRIBUTION_TAGS = frozenset(
    "comfyui gguf ggml quantized onnx mlx awq gptq exl2".split()
)

# 关注的任务类型 → 中文类别（与 README §2.0「模型类别」命名风格一致），以及加分权重。
PIPELINE_CN = {
    "text-generation": ("通用 / 对话", 10),
    "text2text-generation": ("通用 / 文本生成", 6),
    "image-text-to-text": ("多模态 VLM", 10),
    "any-to-any": ("全模态", 10),
    "audio-text-to-text": ("音频语言", 8),
    "text-to-image": ("图像生成", 8),
    "image-to-image": ("图像编辑", 6),
    "text-to-video": ("视频生成", 8),
    "image-to-video": ("视频生成", 8),
    "video-to-video": ("视频编辑", 6),
    "automatic-speech-recognition": ("语音识别", 7),
    "text-to-speech": ("语音合成", 7),
    "audio-classification": ("音频理解", 5),
    "sentence-similarity": ("嵌入模型", 8),
    "feature-extraction": ("嵌入模型", 6),
    "document-question-answering": ("文档理解", 6),
    "visual-question-answering": ("视觉问答", 6),
    "image-to-3d": ("3D 生成", 7),
    "text-to-3d": ("3D 生成", 7),
    "translation": ("翻译", 5),
    "summarization": ("摘要", 4),
    "question-answering": ("问答", 4),
    "fill-mask": ("预训练基座", 4),
    "conversational": ("通用 / 对话", 5),
    "object-detection": ("视觉检测", 4),
    "image-classification": ("图像分类", 4),
    "depth-estimation": ("视觉理解", 4),
    "text-classification": ("文本分类", 3),
    "token-classification": ("序列标注", 3),
    "zero-shot-classification": ("零样本分类", 3),
    "reinforcement-learning": ("强化学习", 3),
    "robotics": ("具身 / 机器人", 5),
    "tabular-classification": ("表格理解", 2),
    "table-question-answering": ("表格问答", 3),
    "time-series-forecasting": ("时序预测", 2),
}

# 从 tags 中挑能力线索时忽略的元数据标签。
TAG_SKIP_PREFIX = ("license:", "region:", "base_model", "dataset:", "arxiv:", "doi:",
                   "language:", "pipeline_tag:", "model-index", "eval-results")
TAG_SKIP_EXACT = frozenset(
    "transformers safetensors pytorch endpoints_compatible conversational "
    "text-generation-inference diffusers en zh region:us region:eu custom_code "
    "gguf model-index eval-results has_space spaces".split()
)
LANG_CODE = re.compile(r"^[a-z]{2}(-[a-z]{2})?$")


@dataclass
class Config:
    lookback_hours: int = 36
    min_likes: int = 5
    min_downloads: int = 50
    top_n: int = 12
    cooldown_days: int = 7
    per_feed_limit: int = 200
    pages: int = 1
    min_score: float = 24.0
    date: str = ""
    dry_run: bool = False
    force: bool = False
    validate: bool = False
    offline_fixture: str = ""
    root: Path = field(default_factory=lambda: Path.cwd())

    @property
    def today(self) -> dt.date:
        return dt.date.fromisoformat(self.date) if self.date else dt.datetime.now(dt.timezone.utc).date()


def parse_ts(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    try:
        return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (ValueError, AttributeError):
        return None


def http_get_json(url: str, attempts: int = 3, timeout: int = 25) -> tuple[list[dict], str | None]:
    """GET JSON，带重试与退避；返回 (data, next_cursor_url)。"""
    headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    token = os.environ.get("HF_TOKEN", "").strip()
    if token:
        headers["Authorization"] = f"Bearer {token}"
    last: Exception | None = None
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = json.load(resp)
                link = resp.headers.get("Link") or ""
                nxt = None
                for part in link.split(","):
                    if 'rel="next"' in part:
                        m = re.search(r"<([^>]+)>", part)
                        if m:
                            nxt = m.group(1)
                if not isinstance(data, list):
                    raise ValueError(f"unexpected payload type: {type(data).__name__}")
                return data, nxt
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError,
                json.JSONDecodeError, ValueError) as exc:
            last = exc
            if i < attempts - 1:
                time.sleep(2 ** i)
    raise RuntimeError(f"HF API request failed after {attempts} attempts: {url} :: {last}")


def feed_url(sort_key: str, limit: int, cursor: str | None = None) -> str:
    if cursor:
        return cursor
    q = urllib.parse.urlencode(
        {"sort": sort_key, "direction": -1, "limit": limit, "full": "true"}
    )
    return f"{API_BASE}?{q}"


def fetch_all(cfg: Config) -> list[dict]:
    """合并三路数据源，按 model id 去重，并保留命中的来源标签。"""
    by_id: dict[str, dict] = {}
    errors: list[str] = []
    for name, sort_key in FEEDS:
        url: str | None = feed_url(sort_key, cfg.per_feed_limit)
        for page in range(cfg.pages):
            if not url:
                break
            try:
                batch, url = http_get_json(url)
            except RuntimeError as exc:
                errors.append(f"{name}/p{page + 1}: {exc}")
                break
            for raw in batch:
                mid = raw.get("id") or raw.get("modelId")
                if not mid:
                    continue
                if mid in by_id:
                    by_id[mid]["_feeds"].add(name)
                    # trending 榜独有 trendingScore，合并时补齐
                    if raw.get("trendingScore") is not None:
                        by_id[mid].setdefault("trendingScore", raw["trendingScore"])
                else:
                    item = dict(raw)
                    item["_feeds"] = {name}
                    by_id[mid] = item
            print(f"[fetch] {name} page {page + 1}: {len(batch)} rows, unique so far {len(by_id)}",
                  file=sys.stderr)
    if not by_id and errors:
        raise RuntimeError("all HF feeds failed: " + " | ".join(errors))
    if errors:
        print("[warn] partial feed failures: " + " | ".join(errors), file=sys.stderr)
    for item in by_id.values():
        item["_feeds"] = sorted(item["_feeds"])
    return list(by_id.values())


def _tags(model: dict) -> list[str]:
    """HF API 的 tags 偶尔为 None / 字符串；统一成 list[str]，避免逐字符迭代。"""
    raw = model.get("tags")
    if isinstance(raw, (list, tuple)):
        return [str(t) for t in raw]
    if isinstance(raw, str):
        return [raw]
    return []


def _num(model: dict, key: str) -> int:
    """把可能缺失或类型异常的计数安全转成非负整数。"""
    try:
        return max(0, int(model.get(key) or 0))
    except (TypeError, ValueError):
        return 0


def is_official(model: dict) -> bool:
    author = str(model.get("author") or "").lower()
    mid = str(model.get("id") or "").lower()
    org = mid.split("/")[0] if "/" in mid else ""
    return author in OFFICIAL_ORGS or org in OFFICIAL_ORGS


def noise_hit(model: dict) -> bool:
    name = str(model.get("id") or "").lower()
    return any(tok in name for tok in NOISE_TOKENS)


def base_model_ids(model: dict) -> list[str]:
    """从 cardData.base_model 与 tags 的 base_model: 标记中提取基座仓库 id。"""
    out: list[str] = []
    card = model.get("cardData")
    if isinstance(card, dict):
        bm = card.get("base_model")
        if isinstance(bm, str):
            out.append(bm)
        elif isinstance(bm, (list, tuple)):
            out.extend(str(x) for x in bm)
    for t in _tags(model):
        if t.lower().startswith("base_model:"):
            raw = t.split(":", 1)[1]
            # base_model:finetune:xxx / base_model:adapter:xxx 是修饰前缀，取真正的仓库名
            if raw.lower().startswith(("finetune:", "adapter:", "quantized:")):
                raw = raw.split(":", 1)[1]
            if "/" in raw:
                out.append(raw)
    return out


def is_cross_org_redistribution(model: dict) -> bool:
    own = str(model.get("author") or "").lower()
    if not own:
        mid = str(model.get("id") or "")
        own = mid.split("/")[0].lower() if "/" in mid else ""
    if not own:
        return False
    cross = any(
        "/" in b and b.split("/")[0].lower() != own for b in base_model_ids(model)
    )
    if not cross:
        return False
    lib = str(model.get("library_name") or "").lower()
    tags = {t.lower() for t in _tags(model)}
    return lib in REDISTRIBUTION_LIBS or bool(tags & REDISTRIBUTION_TAGS)


def infer_pipeline(model: dict) -> tuple[str, int]:
    tag = model.get("pipeline_tag")
    if tag in PIPELINE_CN:
        return PIPELINE_CN[tag][0], PIPELINE_CN[tag][1]
    tags = _tags(model)
    for t in tags:
        if t in PIPELINE_CN and PIPELINE_CN[t][1] >= 6:
            return PIPELINE_CN[t][0], PIPELINE_CN[t][1] - 2
    # 无 pipeline_tag 时按仓库名 / 标签兜底推断，避免全部落到「其他」。
    hay = (str(model.get("id") or "") + " " + " ".join(tags)).lower()
    for needle, label in FALLBACK_CATEGORY:
        if needle in hay:
            return label, 3
    return "其他 / 未标注", 0


FALLBACK_CATEGORY = (
    ("world-model", "世界模型"),
    ("world_model", "世界模型"),
    ("ocr", "文档 / OCR"),
    ("text-to-video", "视频生成"),
    ("image-to-video", "视频生成"),
    ("video", "视频生成"),
    ("text-to-image", "图像生成"),
    ("image", "图像生成"),
    ("audio", "语音 / 音频"),
    ("speech", "语音 / 音频"),
    ("embedding", "嵌入模型"),
    ("reranker", "重排序"),
    ("coder", "代码模型"),
    ("vl", "多模态 VLM"),
    ("3d", "3D 生成"),
)


def capability_text(model: dict, category: str) -> str:
    hints: list[str] = []
    for t in _tags(model):
        low = t.lower()
        if low.startswith(TAG_SKIP_PREFIX) or low in TAG_SKIP_EXACT or LANG_CODE.match(low):
            continue
        if t in PIPELINE_CN:
            continue
        hints.append(t)
        if len(hints) == 3:
            break
    suffix = "、".join(hints) if hints else "标签信息不足"
    return f"{category}；{suffix}（按 HF 标签推断）"


def in_window(model: dict, now: dt.datetime, cfg: Config) -> bool:
    stamps = [parse_ts(model.get("createdAt")), parse_ts(model.get("lastModified"))]
    stamps = [s for s in stamps if s is not None]
    if not stamps:
        return False
    return max(stamps) >= now - dt.timedelta(hours=cfg.lookback_hours)


def is_hot(model: dict, cfg: Config) -> bool:
    likes = _num(model, "likes")
    downloads = _num(model, "downloads")
    try:
        trending = max(0.0, float(model.get("trendingScore") or 0))
    except (TypeError, ValueError):
        trending = 0.0
    return (
        (likes >= cfg.min_likes and downloads >= cfg.min_downloads)
        or likes >= max(25, cfg.min_likes * 5)
        or downloads >= max(2000, cfg.min_downloads * 40)
        or trending >= 50
    )


def qualify(model: dict, now: dt.datetime, cfg: Config) -> tuple[bool, str]:
    """硬门槛。返回 (是否合格, 淘汰原因)。"""
    if model.get("private"):
        return False, "private"
    if not in_window(model, now, cfg):
        return False, "outside-window"
    official = is_official(model)
    # 量化 / 派生仓库一律排除（含知名组织），本项目跟踪的是模型发布而非权重再分发。
    if noise_hit(model):
        return False, "quantized-or-derived"
    # 名字干净但 base_model 指向其他组织、且属于纯再打包格式的仓库同样排除。
    if is_cross_org_redistribution(model):
        return False, "cross-org-redistribution"
    if not official and not is_hot(model, cfg):
        return False, "below-heat-threshold"
    if score(model, now, cfg) < cfg.min_score:
        return False, "below-score-threshold"
    return True, ""


def score(model: dict, now: dt.datetime, cfg: Config) -> float:
    """「值得关注」打分。热度为主，官方/新发布/任务类型加权，派生仓库降权。"""
    likes = _num(model, "likes")
    downloads = _num(model, "downloads")
    try:
        trending = max(0.0, float(model.get("trendingScore") or 0))
    except (TypeError, ValueError):
        trending = 0.0
    s = min(30.0, 6.0 * math.log10(downloads + 1))
    s += min(25.0, 5.0 * math.sqrt(likes))
    s += min(20.0, trending / 10.0)
    official = is_official(model)
    if official:
        s += 25.0
    created = parse_ts(model.get("createdAt"))
    if created and created >= now - dt.timedelta(hours=cfg.lookback_hours):
        s += 12.0
    _, pipeline_bonus = infer_pipeline(model)
    s += pipeline_bonus
    if model.get("gated"):
        s -= 5.0
    if model.get("pipeline_tag") is None:
        s -= 8.0
    if noise_hit(model):
        s -= 15.0
    if not official and any(t.lower().startswith("base_model") for t in _tags(model)):
        s -= 10.0
    if "trending" in (model.get("_feeds") or []):
        s += 4.0
    return round(s, 2)


def load_seen(path: Path) -> dict[str, dict]:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data.get("models", {}) if isinstance(data, dict) else {}
    except (json.JSONDecodeError, OSError):
        return {}


def prune_seen(seen: dict[str, dict], today: dt.date, keep_days: int = 180) -> dict[str, dict]:
    cutoff = today - dt.timedelta(days=keep_days)
    out = {}
    for mid, meta in seen.items():
        try:
            if dt.date.fromisoformat(str(meta.get("last", ""))) >= cutoff:
                out[mid] = meta
        except (ValueError, TypeError):
            continue
    return out


def classify(model: dict, seen: dict[str, dict], today: dt.date, cfg: Config,
             now: dt.datetime | None = None) -> str | None:
    """返回 new / update / None（None 表示本次不报）。

    「new」只用于本次窗口内真正新建且首次见到的仓库；
    窗口内只是被修改（含首次见到但创建已久）的仓库一律归为「update」，
    避免把两周前创建、今天改了 README 的模型标成「新发布」。
    """
    now = now or dt.datetime.now(dt.timezone.utc)
    mid = model["id"]
    created = parse_ts(model.get("createdAt"))
    created_in_window = bool(
        created and created >= now - dt.timedelta(hours=cfg.lookback_hours)
    )
    prev = seen.get(mid)
    if prev is None:
        return "new" if created_in_window else "update"
    days = 10 ** 6
    try:
        days = (today - dt.date.fromisoformat(str(prev.get("last", "")))).days
    except (ValueError, TypeError):
        days = 10 ** 6
    changed = (prev.get("sha") != model.get("sha")) or (
        prev.get("lastModified") != model.get("lastModified")
    )
    if changed and days >= cfg.cooldown_days:
        return "update"
    return None


def md_cell(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def model_link(mid: str) -> str:
    return f"{HF_WEB}/{urllib.parse.quote(mid, safe='/')}"


def build_row(model: dict, kind: str, cfg: Config,
              now: dt.datetime | None = None) -> dict[str, str]:
    now = now or dt.datetime.now(dt.timezone.utc)
    mid = model["id"]
    author = model.get("author") or mid.split("/")[0]
    official = is_official(model)
    category, _ = infer_pipeline(model)
    created = parse_ts(model.get("createdAt"))
    modified = parse_ts(model.get("lastModified"))
    shown = created if kind == "new" else (modified or created)
    when = shown.strftime("%Y-%m-%d %H:%M UTC") if shown else "未披露"
    likes = _num(model, "likes")
    downloads = _num(model, "downloads")
    status = "需申请（gated）" if model.get("gated") else "公开仓库"
    status += f"；HF 下载 {downloads} / 赞 {likes}（未核实）"
    kind_label = "🆕 新发布" if kind == "new" else "🔄 近期有更新"
    license_tags = [t.split(":", 1)[1] for t in _tags(model) if t.lower().startswith("license:")]
    return {
        "模型名称": f"[{md_cell(mid)}]({model_link(mid)})",
        "提供方": ("⭐ " if official else "") + md_cell(author),
        "发布或更新时间": f"{when}（{kind_label}）",
        "模型类别": md_cell(category),
        "核心能力": md_cell(capability_text(model, category)),
        "可用状态": md_cell(status),
        "信息来源": f"[HF API]({API_BASE}/{urllib.parse.quote(mid, safe='/')}) · [模型卡]({model_link(mid)})",
        "标记": "⚙️ 机器抓取 · 待人工核实",
        "_score": str(score(model, now, cfg)),
        "_kind": kind,
        "_id": mid,
        "_sha": model.get("sha") or "",
        "_lastModified": model.get("lastModified") or "",
        "_feeds": ",".join(model.get("_feeds") or []),
        "_license": " / ".join(dict.fromkeys(license_tags)) or "未披露",
        "_heat": f"赞 {likes} · 下载 {downloads}",
    }


TABLE_COLS = ("模型名称", "提供方", "发布或更新时间", "模型类别", "核心能力", "可用状态", "信息来源", "标记")
DISCLAIMER = (
    "> ⚠️ 本节由 GitHub Action 每日自动更新，数据直接来自 Hugging Face Hub API，"
    "**未经人工核实，不得作为确定内容引用**；不并入 §2.0.1–2.0.7 的 🆕 / 🔄 / ⚠️ 三态清单。"
    "「核心能力」由 HF 标签推断，「可用状态」仅反映仓库可见性。经人工核实后方可迁入 🆕 新增项。"
)


def render_table(rows: list[dict[str, str]]) -> str:
    out = ["| " + " | ".join(TABLE_COLS) + " |", "|" + "|".join([":---"] * len(TABLE_COLS)) + "|"]
    for r in rows:
        out.append("| " + " | ".join(r.get(c, "") for c in TABLE_COLS) + " |")
    return "\n".join(out)


def render_readme_block(rows: list[dict[str, str]], meta: dict) -> str:
    stamp = meta["generated_at"]
    head = (
        "#### 2.0.8 每日 HF 自动抓取候选\n\n"
        f"{DISCLAIMER}\n\n"
        f"**最近抓取**：{stamp} · 时间窗 {meta['window_hours']}h · "
        f"扫描 {meta['scanned']} 个仓库 · 合格候选 {meta['qualified']} 条 · "
        f"本期上报 {len(rows)} 条（🆕 {meta['new_count']} / 🔄 {meta['update_count']}）\n\n"
    )
    if rows:
        body = render_table(rows) + "\n\n"
    else:
        body = "> 本次抓取无符合条件的新模型或更新（可能因去重冷却或热度门槛）。\n\n"
    tail = (
        "📄 [完整日报 HF_DAILY.md](HF_DAILY.md) · "
        "[历史归档](data/hf-daily/) · [机器可读 latest.json](data/hf-daily/latest.json) · "
        "[抓取脚本](scripts/fetch_hf_models.py) · [定时工作流](.github/workflows/hf-daily.yml)\n"
    )
    return head + body + tail


def render_daily_md(rows: list[dict[str, str]], meta: dict, root_level: bool = True) -> str:
    """root_level=True 生成根目录的 HF_DAILY.md；False 生成 data/hf-daily/ 内的归档副本。"""
    lines = [
        "# 🤗 Hugging Face 每日值得关注模型（自动抓取 · 未经人工核实）",
        "",
        f"- **抓取时间**：{meta['generated_at']}",
        f"- **时间窗**：最近 {meta['window_hours']} 小时（createdAt 或 lastModified 落入窗口）",
        f"- **数据源**：HF Hub API `trendingScore` / `createdAt` / `lastModified` 三路榜单，每路 {meta['per_feed_limit']} 条",
        f"- **扫描**：{meta['scanned']} 个去重仓库 → 合格候选 {meta['qualified']} 条 → 去重后上报 {len(rows)} 条",
        f"- **参数**：min_likes={meta['min_likes']}、min_downloads={meta['min_downloads']}、"
        f"min_score={meta['min_score']}、top_n={meta['top_n']}、cooldown={meta['cooldown_days']}d",
        "",
        DISCLAIMER,
        "",
        "## 本期候选",
        "",
    ]
    lines.append(render_table(rows) if rows else "> 本次抓取无符合条件的新模型或更新。")
    lines += [
        "",
        "## 打分明细（用于调参，非模型规格）",
        "",
        "| 模型 | 分数 | 类型 | 命中的榜单 | 热度 | HF 许可标记 |",
        "|:---|---:|:---|:---|:---|:---|",
    ]
    for r in rows:
        lines.append(
            f"| {r['模型名称']} | {r['_score']} | "
            f"{'新发布' if r['_kind'] == 'new' else '有更新'} | {r['_feeds']} | "
            f"{r['_heat']} | `{md_cell(r['_license'])}` |"
        )
    if not rows:
        lines.append("| — | — | — | — | — | — |")
    lines += [
        "",
        "## 筛选规则",
        "",
        "1. 排除私有仓库；量化 / abliterated / LoRA / 备份类仓库一律排除（含知名组织），本项目跟踪模型发布而非权重再分发。",
        "2. 排除「跨组织再分发」：`base_model` 指向其他组织且属于 ComfyUI 单文件 / GGUF / ONNX 等纯再打包格式的仓库；有独立技术贡献的后训练模型不在此列。",
        "3. 非官方仓库需满足热度门槛（点赞与下载组合，或高点赞 / 高下载 / trendingScore ≥ 50）。",
        "4. 打分 = 下载量与点赞的对数项 + trendingScore + 官方组织加权 + 新发布加权 + 任务类型加权；量化与纯微调降权。",
        "5. 「新发布」保留 1/3 名额，避免高热度老仓库的小改动挤掉当天真正的新模型。",
        "6. 跨天去重：`seen.json` 记录已上报仓库；已上报仓库仅在 sha / lastModified 变化且超过冷却期后，才以「🔄 近期有更新」再次上报。",
        "7. 「值得关注」是启发式排序，不代表模型质量结论；排序分数不可用于横向比较模型能力。",
        "",
        "## 历史归档",
        "",
    ]
    for d in meta.get("archive", []):
        link = f"data/hf-daily/{d}.md" if root_level else f"{d}.md"
        lines.append(f"- [{d}]({link})")
    lines += [
        "",
        "---",
        "",
        "由 `.github/workflows/hf-daily.yml` 每日自动生成；请勿手工编辑本文件的抓取结果。",
        "",
        "返回 [项目 README]({}) · [最新一期]({})".format(
            "README.md" if root_level else "../../README.md",
            "HF_DAILY.md" if root_level else "../../HF_DAILY.md",
        ),
        "",
    ]
    return "\n".join(lines)


def update_readme(root: Path, block: str, dry_run: bool) -> bool:
    path = root / "README.md"
    text = path.read_text(encoding="utf-8")
    if MARKER_START not in text or MARKER_END not in text:
        raise RuntimeError("README.md 缺少 HF_DAILY marker，请先插入标记块")
    pre, rest = text.split(MARKER_START, 1)
    _, post = rest.split(MARKER_END, 1)
    new = pre + MARKER_START + "\n" + block.strip() + "\n" + MARKER_END + post
    changed = new != text
    if changed and not dry_run:
        path.write_text(new, encoding="utf-8")
    return changed


def write_outputs(root: Path, rows: list[dict[str, str]], meta: dict,
                  seen: dict[str, dict], cfg: Config) -> dict[str, bool]:
    daily_dir = root / "data" / "hf-daily"
    daily_dir.mkdir(parents=True, exist_ok=True)
    day = cfg.today.isoformat()
    public_rows = [{k: v for k, v in r.items() if not k.startswith("_")} for r in rows]
    meta_out = dict(meta)
    meta_out["counts"] = {"new": meta["new_count"], "update": meta["update_count"], "total": len(rows)}
    meta_out["disclaimer"] = "机器抓取候选，未经人工核实，不得作为确定内容引用"
    payload = {"generated_at": meta["generated_at"], "meta": meta_out, "models": public_rows}

    daily_md = render_daily_md(rows, meta, root_level=True)
    archive_md = render_daily_md(rows, meta, root_level=False)
    block = render_readme_block(rows, meta)
    targets = {
        daily_dir / f"{day}.md": archive_md,
        root / "HF_DAILY.md": daily_md,
        daily_dir / "latest.json": json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        daily_dir / "seen.json": json.dumps(
            {"updated_at": meta["generated_at"], "models": seen}, ensure_ascii=False, indent=2
        ) + "\n",
    }
    changed: dict[str, bool] = {}
    for path, content in targets.items():
        old = path.read_text(encoding="utf-8") if path.exists() else None
        changed[str(path.relative_to(root))] = old != content
        if not cfg.dry_run:
            path.write_text(content, encoding="utf-8")
    changed["README.md"] = update_readme(root, block, cfg.dry_run)
    return changed


def build_meta(models: list[dict], qualified: list[dict], rows: list[dict],
               cfg: Config, now: dt.datetime, root: Path) -> dict:
    archives = sorted(
        (p.stem for p in (root / "data" / "hf-daily").glob("20??-??-??.md")),
        reverse=True,
    )[:10]
    if cfg.today.isoformat() not in archives:
        archives.insert(0, cfg.today.isoformat())
    return {
        "generated_at": now.strftime("%Y-%m-%d %H:%M UTC"),
        "window_hours": cfg.lookback_hours,
        "scanned": len(models),
        "qualified": len(qualified),
        "new_count": sum(1 for r in rows if r["_kind"] == "new"),
        "update_count": sum(1 for r in rows if r["_kind"] == "update"),
        "min_likes": cfg.min_likes,
        "min_downloads": cfg.min_downloads,
        "min_score": cfg.min_score,
        "top_n": cfg.top_n,
        "cooldown_days": cfg.cooldown_days,
        "per_feed_limit": cfg.per_feed_limit,
        "archive": archives[:10],
    }


def run(cfg: Config) -> dict[str, bool]:
    root = cfg.root
    now = dt.datetime.now(dt.timezone.utc)
    today_archive = root / "data" / "hf-daily" / f"{cfg.today.isoformat()}.md"

    # 每天只产出一份日报。定时 + 手动触发或失败重试导致同一天二次运行时直接跳过，
    # 避免把已发布的当期日报换成另一批候选；需要刷新时显式传 --force。
    if today_archive.exists() and not cfg.dry_run and not cfg.force:
        print(f"[result] daily digest for {cfg.today.isoformat()} already exists; "
              "skipping (use --force to overwrite)", file=sys.stderr)
        return {"kept_existing_digest": True}

    if cfg.offline_fixture:
        raw = json.loads(Path(cfg.offline_fixture).read_text(encoding="utf-8"))
        models = raw.get("models", raw) if isinstance(raw, dict) else raw
        for m in models:
            m.setdefault("_feeds", ["fixture"])
        print(f"[fetch] offline fixture: {len(models)} models", file=sys.stderr)
    else:
        models = fetch_all(cfg)

    qualified: list[dict] = []
    rejected: dict[str, int] = {}
    for m in models:
        ok, why = qualify(m, now, cfg)
        if ok:
            qualified.append(m)
        elif why:
            rejected[why] = rejected.get(why, 0) + 1
    print(f"[filter] scanned={len(models)} qualified={len(qualified)} rejected={rejected}",
          file=sys.stderr)

    seen_path = root / "data" / "hf-daily" / "seen.json"
    seen = load_seen(seen_path)
    candidates: list[tuple[dict, str]] = []
    for m in qualified:
        kind = classify(m, seen, cfg.today, cfg, now)
        if kind:
            candidates.append((m, kind))

    def rank(pairs: list[tuple[dict, str]]) -> list[tuple[dict, str]]:
        return sorted(pairs, key=lambda pair: score(pair[0], now, cfg), reverse=True)

    # 新发布与更新分开排队：先给「新发布」保留 1/3 配额，避免高热度老仓库
    # 的 README 小改动把当天真正的新模型全部挤出榜单。
    new_items = rank([p for p in candidates if p[1] == "new"])
    upd_items = rank([p for p in candidates if p[1] == "update"])
    new_quota = max(1, math.ceil(cfg.top_n / 3))
    selected = new_items[:new_quota]
    rest = rank(new_items[new_quota:] + upd_items)
    selected += rest[: max(0, cfg.top_n - len(selected))]
    print(f"[filter] reportable: new={len(new_items)} update={len(upd_items)} "
          f"(new_quota={new_quota})", file=sys.stderr)

    rows = [build_row(m, kind, cfg, now) for m, kind in selected]
    meta = build_meta(models, qualified, rows, cfg, now, root)

    # 仅对实际入选的仓库更新去重状态；避免候选被 top_n 截掉后永久失去上报机会。
    for m, kind in selected:
        seen[m["id"]] = {
            "first": seen.get(m["id"], {}).get("first", cfg.today.isoformat()),
            "last": cfg.today.isoformat(),
            "kind": kind,
            "sha": m.get("sha") or "",
            "lastModified": m.get("lastModified") or "",
        }
    seen = prune_seen(seen, cfg.today)

    changed = write_outputs(root, rows, meta, seen, cfg)
    print(f"[result] reported={len(rows)} (new={meta['new_count']}, update={meta['update_count']})",
          file=sys.stderr)
    print(f"[result] changed files: {[k for k, v in changed.items() if v]}", file=sys.stderr)
    if cfg.dry_run:
        print("\n----- README block preview -----\n")
        print(render_readme_block(rows, meta))
        print("\n----- daily md preview (first 40 lines) -----\n")
        print("\n".join(render_daily_md(rows, meta).split("\n")[:40]))
    return changed


def table_column_counts(path: Path) -> list[set[int]]:
    """按「连续表格块」分别统计数据列数；日报里主表与打分明细表列数本就不同。"""
    blocks: list[set[int]] = []
    cur: set[int] = set()

    def flush() -> None:
        nonlocal cur
        if cur:
            blocks.append(cur)
            cur = set()

    for line in path.read_text(encoding="utf-8").split("\n"):
        if line.strip().startswith("|"):
            if re.match(r"^\s*\|[\s\-:|]+\|\s*$", line):
                continue
            cur.add(len(re.split(r"(?<!\\)\|", line.strip())) - 2)
        else:
            flush()
    flush()
    return blocks


def validate_outputs(root: Path) -> list[str]:
    """校验自动产物完整性；返回错误列表，空列表代表通过。"""
    errors: list[str] = []
    daily = root / "data" / "hf-daily"

    payload_path = daily / "latest.json"
    if not payload_path.exists():
        errors.append("缺少 data/hf-daily/latest.json")
    else:
        try:
            payload = json.loads(payload_path.read_text(encoding="utf-8"))
            models = payload.get("models")
            if not isinstance(models, list):
                errors.append("latest.json 的 models 不是数组")
            else:
                for row in models:
                    missing = [c for c in TABLE_COLS if c not in row]
                    if missing:
                        errors.append(f"latest.json 条目缺字段: {','.join(missing)}")
                        break
            if "未经人工核实" not in str(payload.get("meta", {}).get("disclaimer", "")):
                errors.append("latest.json 缺少未核实免责声明")
        except (json.JSONDecodeError, OSError) as exc:
            errors.append(f"latest.json 无法解析: {exc}")

    readme = root / "README.md"
    if not readme.exists():
        errors.append("缺少 README.md")
    else:
        text = readme.read_text(encoding="utf-8")
        if text.count(MARKER_START) != 1 or text.count(MARKER_END) != 1:
            errors.append("README.md 的 HF_DAILY marker 缺失或重复")
        else:
            block = text.split(MARKER_START, 1)[1].split(MARKER_END, 1)[0]
            if "未经人工核实" not in block:
                errors.append("README §2.0.8 缺少未核实免责声明")

    archives = sorted(daily.glob("20??-??-??.md")) if daily.exists() else []
    if not (root / "HF_DAILY.md").exists():
        errors.append("缺少 HF_DAILY.md")
    if not archives:
        errors.append("缺少当日归档 data/hf-daily/YYYY-MM-DD.md")

    for f in [root / "HF_DAILY.md"] + archives[-1:]:
        if not f.exists():
            continue
        for idx, counts in enumerate(table_column_counts(f), 1):
            if len(counts) > 1:
                errors.append(f"{f.name} 第 {idx} 个表格列数不一致: {sorted(counts)}")
    return errors


def parse_args(argv: list[str] | None = None) -> Config:
    p = argparse.ArgumentParser(description="每日抓取 Hugging Face 值得关注的模型")
    p.add_argument("--lookback-hours", type=int, default=36, help="时间窗（小时），默认 36")
    p.add_argument("--min-likes", type=int, default=5)
    p.add_argument("--min-downloads", type=int, default=50)
    p.add_argument("--top-n", type=int, default=12, help="每期最多上报条数")
    p.add_argument("--cooldown-days", type=int, default=7, help="同一仓库「有更新」的冷却天数")
    p.add_argument("--per-feed-limit", type=int, default=200)
    p.add_argument("--pages", type=int, default=1, help="每路榜单翻页数（跟随 Link header）")
    p.add_argument("--min-score", type=float, default=24.0)
    p.add_argument("--date", default="", help="覆盖日期 YYYY-MM-DD（测试用）")
    p.add_argument("--dry-run", action="store_true", help="只预览，不写文件")
    p.add_argument("--force", action="store_true", help="覆盖当天已存在的日报")
    p.add_argument("--validate", action="store_true", help="只校验已有产物完整性，不联网、不写入")
    p.add_argument("--offline-fixture", default="", help="从本地 JSON 读候选，跳过网络")
    p.add_argument("--root", default="", help="仓库根目录，默认当前目录")
    a = p.parse_args(argv)
    return Config(
        lookback_hours=a.lookback_hours, min_likes=a.min_likes,
        min_downloads=a.min_downloads, top_n=a.top_n,
        cooldown_days=a.cooldown_days, per_feed_limit=a.per_feed_limit,
        pages=a.pages, min_score=a.min_score, date=a.date,
        dry_run=a.dry_run, force=a.force, validate=a.validate,
        offline_fixture=a.offline_fixture,
        root=Path(a.root).resolve() if a.root else Path.cwd(),
    )


def main(argv: list[str] | None = None) -> int:
    cfg = parse_args(argv)
    if cfg.validate:
        errors = validate_outputs(cfg.root)
        for err in errors:
            print(f"[validate] ERROR: {err}", file=sys.stderr)
        if errors:
            return 1
        print("[validate] OK: latest.json / README marker / 日报归档 / 表格列数 全部通过",
              file=sys.stderr)
        return 0
    try:
        run(cfg)
    except (RuntimeError, OSError, ValueError) as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
