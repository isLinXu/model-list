#!/usr/bin/env python3
"""把 §4.1 / §4.2 / §1.10 三张表渲染成「官方来源索引」动态表。

背景：这三张表原先是 2026-04 的无来源数值快照（基准分数、API 价格、SOTA 排名），
找不到评测 harness、统计时间与计费口径，前几轮只能加警示并列入 ⚠️ 待确认。
本脚本把它们改为由 data/official_sources.json 驱动的可复核链接索引：
**只登记有一手官方链接的条目，不固化无来源数字**。

零第三方依赖（仅标准库），可作为 GitHub Actions 的离线校验步骤。

用法：
    python3 scripts/render_source_tables.py                 # 重渲染 README 三个 marker 块
    python3 scripts/render_source_tables.py --dry-run       # 只预览，不写文件
    python3 scripts/render_source_tables.py --validate      # 离线校验数据与 README 一致性
    python3 scripts/render_source_tables.py --verify        # 联网检查官方链接可达性（报告，不改文件）
    python3 -m unittest scripts.test_render_source_tables
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path

DATA_FILE = Path("data/official_sources.json")
TABLE_KEYS = ("benchmarks", "pricing", "leaderboards")

MARKERS = {
    key: (f"<!-- SOURCES_{key.upper()}_START -->", f"<!-- SOURCES_{key.upper()}_END -->")
    for key in TABLE_KEYS
}

# 展示文案由脚本维护；数据行与表头由 JSON 维护。
NOTES = {
    "benchmarks": (
        "本表只收录**有官方一手来源**的评测口径，字段与 §2.0 一致（8 列）。"
        "厂商自评与第三方指数已分别标注，harness 与采样条件以来源原文为准；"
        "**不得把不同来源的分数横向拼接成排行榜**。原 2026-04 无来源分数表已移除，"
        "历史数值可从 Git 记录查阅，不作为确定内容。"
    ),
    "pricing": (
        "本表提供**官方实时价目页入口**而非静态价格结论：价格随版本、档位、缓存命中与"
        "长上下文计价变动，固化数字必然过期。仅当厂商官方公告明确给出价格时才写入示例，"
        "并附公告链接与日期。原 2026-04 无来源定价表已移除。"
    ),
    "leaderboards": (
        "本表只登记**可追溯到官方公告**的名次与分数，并写明榜单版本与日期。"
        "榜单快照随投票与评测版本变动，跨版本不可直接比较；"
        "未获一手依据的排名（含原 2026-04 Top 10 双赛道榜）不予收录。"
    ),
}

# 防止旧的无来源数值表被重新粘贴回来。
FORBIDDEN_PATTERNS = (
    r"^\|\s*GPT-5\.4\s*\|\s*93\.5%",
    r"^\|\s*GPT-5\.4\s*\|\s*\$35\.00",
    r"^\|\s*🥇\s*\|\s*\*\*GPT-5\.4\*\*",
    r"^\|\s*LLaMA 4 Maverick\s*\|\s*88\.5%",
    r"^\|\s*Claude 4\.6 Opus\s*\|\s*91\.8%",
    r"本表为 \*\*2026-04 基线快照\*\*",
)

URL_RE = re.compile(r"\]\((https?://[^)]+)\)")
ROW_RE = re.compile(r"^\|.*\|\s*$", re.M)


@dataclass
class Config:
    root: Path
    dry_run: bool = False
    validate_only: bool = False
    verify_links: bool = False


def load_data(root: Path) -> dict:
    path = root / DATA_FILE
    if not path.exists():
        raise FileNotFoundError(f"缺少数据源: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def render_block(key: str, table: dict) -> str:
    """生成一个完整的 marker 块（含表头、数据行与说明）。"""
    start, end = MARKERS[key]
    cols = table["columns"]
    lines = [
        start,
        "",
        f"> ℹ️ **动态表 · 由 `data/official_sources.json` 生成**（{table['section']} {table['title']}）。{NOTES[key]}",
        "",
        "| " + " | ".join(cols) + " |",
        "|" + "|".join([":---"] * len(cols)) + "|",
    ]
    for row in table["rows"]:
        lines.append("| " + " | ".join(str(c) for c in row) + " |")
    lines += [
        "",
        f"> 🔎 共 {len(table['rows'])} 条可核实来源；`✅ [A]` 为一手，`[B]` 为二手交叉。"
        "需要更新时编辑 JSON 后重跑本脚本，不要直接改表格。",
        "",
        end,
    ]
    return "\n".join(lines)


def render_all(data: dict) -> dict[str, str]:
    return {k: render_block(k, data["tables"][k]) for k in TABLE_KEYS}


def update_readme(root: Path, blocks: dict[str, str], dry_run: bool) -> dict[str, bool]:
    path = root / "README.md"
    text = path.read_text(encoding="utf-8")
    changed: dict[str, bool] = {}
    for key, block in blocks.items():
        start, end = MARKERS[key]
        pattern = re.compile(
            re.escape(start) + r".*?" + re.escape(end), re.S
        )
        if not pattern.search(text):
            raise ValueError(f"README 缺少 {key} 的 marker 对: {start} / {end}")
        new_text, n = pattern.subn(lambda _m: block, text, count=1)
        if n != 1:
            raise ValueError(f"README 中 {key} marker 出现多次，请检查")
        changed[key] = new_text != text
        text = new_text
    if not dry_run and any(changed.values()):
        path.write_text(text, encoding="utf-8")
    return changed


def table_column_counts(markdown: str) -> list[int]:
    """按表格块统计列数，返回每个异常块的列数集合。"""
    bad: list[int] = []
    block: list[str] = []

    def flush() -> None:
        if not block:
            return
        counts = {
            len(re.split(r"(?<!\\)\|", line.strip())) - 2
            for line in block
            if not re.match(r"^\s*\|[\s\-:|]+\|\s*$", line)
        }
        if len(counts) > 1:
            bad.append(sorted(counts)[0])
        block.clear()

    for line in markdown.split("\n"):
        if line.strip().startswith("|"):
            block.append(line)
        else:
            flush()
    flush()
    return bad


def validate(root: Path) -> list[str]:
    """离线校验：数据结构、列数、去重、URL、marker、README 一致性与旧数值残留。"""
    errors: list[str] = []
    try:
        data = load_data(root)
    except (OSError, json.JSONDecodeError) as exc:
        return [f"数据源读取失败: {exc}"]

    tables = data.get("tables", {})
    for key in TABLE_KEYS:
        if key not in tables:
            errors.append(f"缺少表 {key}")
            continue
        t = tables[key]
        cols, rows = t.get("columns", []), t.get("rows", [])
        if len(cols) != 8:
            errors.append(f"{key}: 表头应为 8 列，实际 {len(cols)}")
        if not rows:
            errors.append(f"{key}: 无数据行")
        seen: set[str] = set()
        for i, row in enumerate(rows, 1):
            if len(row) != len(cols):
                errors.append(f"{key} 第 {i} 行: 列数 {len(row)} != {len(cols)}")
            first = str(row[0]) if row else ""
            if first in seen:
                errors.append(f"{key} 第 {i} 行: 首列重复「{first}」")
            seen.add(first)
            for cell in row:
                for url in URL_RE.findall(str(cell)):
                    if not url.startswith("https://"):
                        errors.append(f"{key} 第 {i} 行: 非 HTTPS 链接 {url}")
        if table_column_counts(render_block(key, t)):
            errors.append(f"{key}: 渲染结果表格列数不一致")

    readme = root / "README.md"
    if not readme.exists():
        errors.append("缺少 README.md")
        return errors
    text = readme.read_text(encoding="utf-8")
    if all(k in tables for k in TABLE_KEYS):
        for key, block in render_all(data).items():
            start, end = MARKERS[key]
            if text.count(start) != 1 or text.count(end) != 1:
                errors.append(f"README 中 {key} marker 数量不为 1")
            elif block not in text:
                errors.append(f"README 中 {key} 内容与 JSON 不一致，请重跑渲染脚本")
    for pat in FORBIDDEN_PATTERNS:
        if re.search(pat, text, re.M):
            errors.append(f"检测到已废弃的无来源数值表残留: {pat}")
    return errors


def collect_urls(root: Path) -> list[str]:
    data = load_data(root)
    urls: set[str] = set()
    for key in TABLE_KEYS:
        for row in data["tables"][key]["rows"]:
            for cell in row:
                urls.update(URL_RE.findall(str(cell)))
    return sorted(urls)


def verify_links(root: Path, timeout: float = 8.0) -> int:
    """联网检查官方链接可达性。403/429 视为反爬而非失效；只报告，不改文件。"""
    urls = collect_urls(root)
    print(f"[verify] {len(urls)} 个唯一官方链接", file=sys.stderr)
    ok = redirected = blocked = failed = 0
    for url in urls:
        req = urllib.request.Request(
            url, headers={"User-Agent": "model-list-link-check/1.0"}, method="GET"
        )
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                code = resp.status
                if 200 <= code < 300:
                    ok += 1
                elif 300 <= code < 400:
                    redirected += 1
                elif code in (401, 403, 429):
                    blocked += 1
                    print(f"  [反爬/需授权] {code} {url}", file=sys.stderr)
                else:
                    failed += 1
                    print(f"  [异常] {code} {url}", file=sys.stderr)
        except (urllib.error.URLError, OSError) as exc:
            failed += 1
            print(f"  [失败] {type(exc).__name__} {url}", file=sys.stderr)
    print(
        f"[verify] 正常 {ok} / 跳转 {redirected} / 反爬 {blocked} / 失败 {failed}",
        file=sys.stderr,
    )
    return 0  # 报告性质，不因第三方站点反爬让 CI 失败


def run(cfg: Config) -> dict[str, bool]:
    data = load_data(cfg.root)
    blocks = render_all(data)
    changed = update_readme(cfg.root, blocks, cfg.dry_run)
    if cfg.dry_run:
        for key in TABLE_KEYS:
            print(f"----- {key} -----")
            print(blocks[key])
    return changed


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=".", help="仓库根目录")
    p.add_argument("--dry-run", action="store_true", help="只预览，不写文件")
    p.add_argument("--validate", action="store_true", help="离线校验，不写文件")
    p.add_argument("--verify", action="store_true", help="联网检查官方链接可达性")
    a = p.parse_args(argv)
    root = Path(a.root).resolve()

    if a.validate:
        errors = validate(root)
        if errors:
            for e in errors:
                print(f"[validate] ERROR: {e}", file=sys.stderr)
            return 1
        print("[validate] OK: 数据源 / README marker / 表格列数 / 旧数值残留 全部通过")
        return 0
    if a.verify:
        return verify_links(root)

    try:
        changed = run(Config(root=root, dry_run=a.dry_run))
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f"[error] {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1
    if not a.dry_run:
        print(f"[result] changed: {changed}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
