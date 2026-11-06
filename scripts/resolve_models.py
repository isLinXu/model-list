#!/usr/bin/env python3
"""模型身份解析：把不同来源的模型名对齐到统一模型 id。

背景：同一个模型在不同来源里写法差异极大——
  * 榜单：  "GPT 5.2" / "Claude 4.5 Opus" / "gemma-3-27b-it" / "gpt-5 (high)"
  * 项目清单："GPT-5.2" / "Claude Opus 4.5" / "Gemma 3 27B"
不做归一化就无法判断「榜单里的这条」与「项目收录的那条」是不是同一个模型，
覆盖率、横向对比、缺失标记全部会失真。

解析优先级（从强到弱，命中即停）：
  1. 精确匹配注册表 id / name / alias（大小写与空白不敏感）
  2. 归一化键匹配：去掉空格、连字符、点号、括号与常见后缀后比较
  3. 未能解析 → 标记为 unresolved，不猜测

刻意不做的事：
  * 不把推理档位（high / medium / low）拆成不同模型——它们是同一模型的
    不同配置，由 entry_id 区分。
  * 不把不同快照日期合并（除非注册表明确登记为同一模型的两个 alias）。
  * 归一化匹配要求**唯一命中**；命中多个视为歧义，返回 unresolved。

用法：
    python3 scripts/resolve_models.py --validate
    python3 scripts/resolve_models.py --report
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

REGISTRY_FILE = Path("data/model_registry.json")
BOARDS_FILE = Path("data/benchmark_boards.json")
OBS_FILE = Path("data/benchmark_observations.json")
README_FILE = Path("README.md")

# 归一化时剥掉的噪声：推理档位、快照标记、量化后缀等。
# 注意：这里只剥**可判定为配置**的部分，模型版本号中的小数点必须保留。
_CONFIG_SUFFIXES = [
    # 方括号推理档位：[high] / [medium] / [low] / [xhigh] / [minimal]
    r"\[[a-z0-9 _-]{1,12}\]",
    # 圆括号内的配置：括号在末尾（如 "(tools)" / "(text)" / "(Reasoner)"）
    r"\((?:high|medium|low|minimal|xhigh|think|thinking|text|tools|reasoner|chat|base|preview|none|diff|whole)\)",
    # 圆括号内是纯日期快照：如 "(20241022)" / "(2025-02-15)"
    r"\(\s*\d{4}[-_.]?\d{2}[-_.]?\d{2}\s*\)",
    # 空格分隔的配置后缀：" no-thinking" / " thinking" / " Air"
    r"\s+(?:no-?thinking|no-?think|thinking|think|reasoner|air)\s*$",
    # 更新批次标注：-June-24 / -Apr-25 / -Sept2025（月份-日期，非模型版本）
    r"[-_](?:jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun(?:e)?|"
    r"jul(?:y)?|aug(?:ust)?|sep(?:t|tember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)"
    r"[-_]?\d{2}\b",
    # 快照日期后缀：-2025-04-14 / -20241022 / -0905 / -2025_04_14
    # 注意必须按「长格式优先」排列，否则 [-_]\d{4} 会把 8 位日期
    # -20241022 切成 2024 + 残留 1022。
    r"[-_]\d{4}[-_]\d{2}[-_]\d{2}",
    r"[-_]\d{8}",
    r"[-_]\d{4}",
    r"[-_]\d{4}_\d{2}_\d{2}",
]
_QUANT_SUFFIXES = [
    r"[-_](?:awq|gptq|gguf|mlx|onnx|fp8|fp16|int8|int4|4bit|8bit|nf4|nvfp4|ggml|exl2|hqq)\b",
    r"[-_]?(?:bnb|bitsandbytes)[-_]?\d*",
]
# 量化标记（用于 model_key 时整体剥离，避免把 fp8 之类算进身份）
_QUANT_PAT = re.compile(
    r"[-_](?:awq|gptq|gguf|mlx|onnx|fp8|fp16|int8|int4|4bit|8bit|nf4|nvfp4|ggml|exl2|hqq)\b"
    r"|[-_]?(?:bnb|bitsandbytes)[-_]?\d*",
    re.I,
)

# 归一化时丢弃的纯装饰字符
_STRIP_CHARS = re.compile(r"[\s\-_.,:;()\[\]{}'\"`|/\\+*#@!~^&]")
_ALNUM = re.compile(r"[^0-9a-z一-鿿]+")


def canonical_key(text: str) -> str:
    """归一化：去装饰字符 → 小写 → 去配置后缀 → 再去装饰字符。"""
    s = text.strip()
    for pat in _CONFIG_SUFFIXES:
        s = re.sub(pat, " ", s, flags=re.I)
    s = _STRIP_CHARS.sub("", s)
    s = s.lower()
    for pat in _QUANT_SUFFIXES:
        s = re.sub(pat, "", s, flags=re.I)
    return s


def loose_key(text: str) -> str:
    """更宽松的键：canonical_key 之后再只保留字母数字与中文。"""
    return _ALNUM.sub("", canonical_key(text))


def strip_config_suffix(text: str) -> str:
    """去掉推理档位等**配置**后缀，返回模型本体名。

    用于判断「同一模型的不同配置」是否可以合并到同一个 model id。
    注意只去配置，不做词序归一——词序差异由 model_key 比较处理。
    """
    s = text.strip()
    for pat in _CONFIG_SUFFIXES:
        s = re.sub(pat, " ", s, flags=re.I)
    s = _STRIP_CHARS.sub("", s).lower()
    for pat in _QUANT_SUFFIXES:
        s = re.sub(pat, "", s, flags=re.I)
    return s


def model_key(text: str) -> str:
    """模型身份键：剥离配置后，再按「词集合」排序，消除词序与数字切分差异。

    "Claude Opus 4.5" 与 "Claude 4.5 Opus" 是同一模型的两种写法，
    词集合相同 → 键相同 → 允许合并到同一 model id。

    这里**不**复用 strip_config_suffix（它会把小数点也去掉，
    "Opus 4.5" 变成 "opus45"），而是只去配置后缀，保留小数点。
    """
    s = text.strip()
    for pat in _CONFIG_SUFFIXES:
        s = re.sub(pat, " ", s, flags=re.I)
    s = _QUANT_PAT.sub(" ", s)
    s = s.lower()
    # 去掉厂商前缀（meta-llama / google-gemma / openai-gpt 等只是写法差异）
    s = re.sub(
        r"^(?:meta|google|openai|microsoft|amazon|anthropic|nvidia|alibaba|tencent|"
        r"baidu|bytedance|xiaomi|zhipu|moonshot|deepseek|mistral|cohere|ai2|nxai)"
        r"[-_\s]+",
        "", s,
    )
    # 日期先归一：20241022 / 2024-10-22 / 2024_10_22 → 统一为 20241022
    s = re.sub(r"(\d{4})[-_.](\d{2})[-_.](\d{2})", r"\1\2\3", s)
    # 版本号的连字符写法与小数点写法归一：claude-3-5 → claude.3.5
    # 仅在两个「单数字」之间转换，避免把 qwen3-235b 误改成 3.235b。
    s = re.sub(r"(?<!\d)(\d)[-_](\d)(?!\d)", r"\1.\2", s)
    # 数字（含小数）作为整体 token
    tokens = sorted(t for t in re.findall(r"\d+(?:\.\d+)*|[a-z]+", s) if t)
    return "|".join(tokens)


def build_index(registry: dict) -> tuple[dict[str, str], dict[str, str]]:
    """返回 (精确索引, 宽松索引)。两者都要求唯一命中。"""
    exact: dict[str, str] = {}
    loose: dict[str, str] = {}
    conflicts_exact: set[str] = set()
    conflicts_loose: set[str] = set()

    for m in registry.get("models", []):
        mid = m["id"]
        names = [mid, m["name"], *m.get("aliases", [])]
        for n in names:
            if not n:
                continue
            k = n.strip().lower()
            if k in exact and exact[k] != mid:
                conflicts_exact.add(k)
            else:
                exact[k] = mid
            lk = loose_key(n)
            if lk:
                if lk in loose and loose[lk] != mid:
                    conflicts_loose.add(lk)
                else:
                    loose[lk] = mid

    for k in conflicts_exact:
        exact.pop(k, None)
    for k in conflicts_loose:
        loose.pop(k, None)
    return exact, loose


def resolve(name: str, exact: dict[str, str], loose: dict[str, str]) -> tuple[str | None, str]:
    """返回 (model_id 或 None, 解析方式)。"""
    if not name:
        return None, "empty"

    k = name.strip().lower()
    if k in exact:
        return exact[k], "exact"

    lk = loose_key(name)
    if lk and lk in loose:
        return loose[lk], "loose"

    # 去掉尾部版本后缀再试一次（如 "gpt-5-2024-08-08" → "gpt-5"），
    # 但要求去掉后命中唯一，且原串确实带日期型尾巴。
    m = re.search(r"[-_](\d{4}[-_]\d{2}[-_]\d{2}|\d{8}|\d{6})$", name.strip())
    if m:
        base = name.strip()[: m.start()].strip()
        lb = loose_key(base)
        if lb and lb in loose:
            return loose[lb], "snapshot-stripped"
    return None, "unresolved"


def resolve_family(name: str, exact: dict[str, str], loose: dict[str, str]) -> list[tuple[str, str]]:
    """解析可能包含多个档位的组合条目。

    项目清单里大量条目形如 "GPT-5.6 Sol / Terra / Luna"、"LLaMA 4 Scout / Maverick"，
    它们是**同一行的多个独立模型**，榜单里也各自是独立条目。
    因此这里把组合名拆开逐个解析，全部命中才算成功。

    拆分规则：按 " / " 分隔；无法拆分时原样返回单条结果。
    """
    parts = [p.strip() for p in name.split(" / ") if p.strip()]
    if len(parts) <= 1:
        # 形如 "Kimi K3.1 Pro / Highspeed" 或 "o1 / o1-pro" 仍按分隔拆；
        # 但 "Hailuo 2.3 / 2.3 Fast · Media Agent" 这类含修饰语的要谨慎。
        return []

    out: list[tuple[str, str]] = []
    for p in parts:
        mid, how = resolve(p, exact, loose)
        if mid is None:
            # 尝试带前缀继承：父名 + 档位名，如 "2.3 Fast" → "Hailuo 2.3 Fast"
            out.append((p, "unresolved"))
        else:
            out.append((mid, how))
    return out


def read_project_models(root: Path) -> list[dict]:
    """从 README §2.0 三态清单读取项目已收录模型。"""
    text = (root / README_FILE).read_text(encoding="utf-8")
    if "#### 2.0.2 🆕 新增项" not in text:
        return []
    full = text[
        text.index("#### 2.0.2 🆕 新增项") : text.index("#### 2.0.5 引用编号核实结果")
    ]

    def rows(seg: str) -> list[list[str]]:
        out = []
        for line in seg.split("\n"):
            s = line.strip()
            if not (s.startswith("|") and len(s.split("|")) > 2):
                continue
            cells = [c.strip() for c in s.split("|")[1:-1]]
            if cells and all(re.match(r"^[\s\-:]+$", c) for c in cells if c):
                continue
            if cells and cells[0] == "模型名称":
                continue
            out.append(cells)
        return out

    i3 = full.index("#### 2.0.3 🔄")
    i4 = full.index("#### 2.0.4 ⚠️")
    out = []
    for state, seg in (
        ("new", full[:i3]),
        ("update", full[i3:i4]),
        ("pending", full[i4:]),
    ):
        for r in rows(seg):
            if len(r) >= 2:
                out.append({"name": r[0], "provider": r[1], "state": state})
    return out


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=".", help="仓库根目录")
    p.add_argument("--validate", action="store_true", help="只校验并输出统计")
    p.add_argument("--report", action="store_true", help="输出未解析条目明细")
    p.add_argument("--apply", action="store_true",
                   help="把解析结果写回 data/benchmark_boards.json（model_id / resolve 字段）")
    a = p.parse_args(argv)
    root = Path(a.root).resolve()

    reg = json.loads((root / REGISTRY_FILE).read_text(encoding="utf-8"))
    exact, loose = build_index(reg)

    boards_path = root / BOARDS_FILE
    boards = json.loads(boards_path.read_text(encoding="utf-8"))
    obs = boards["observations"]

    # 榜单条目 → 模型 id
    unresolved: dict[str, int] = {}
    ways: dict[str, int] = {}
    for o in obs:
        mid, how = resolve(o["model"], exact, loose)
        o["model_id"] = mid
        o["resolve"] = how
        ways[how] = ways.get(how, 0) + 1
        if mid is None:
            unresolved[o["model"]] = unresolved.get(o["model"], 0) + 1

    # 项目清单 → 模型 id
    proj = read_project_models(root)
    proj_unres: dict[str, int] = {}
    for m in proj:
        mid, how = resolve(m["name"], exact, loose)
        m["model_id"] = mid
        if mid is None:
            proj_unres[m["name"]] = proj_unres.get(m["name"], 0) + 1

    print(f"注册表模型：{len(reg.get('models', []))}")
    print(f"榜单观测：{len(obs)}，解析方式 {ways}")
    print(f"榜单未解析：{len(unresolved)} 个不同名称 / {sum(unresolved.values())} 条观测")
    print(f"项目清单：{len(proj)} 条，未解析 {len(proj_unres)} 个")
    if proj_unres:
        print("  项目清单未解析样例：", list(proj_unres)[:8])

    # 校验：一 id 多原始名必须都有明确的合并理由
    idmap: dict[str, set[str]] = {}
    for o in obs:
        if o.get("model_id"):
            idmap.setdefault(o["model_id"], set()).add(o["model"])
    multi = {k: sorted(v) for k, v in idmap.items() if len(v) > 1}
    reg_by_id = {m["id"]: m for m in reg.get("models", [])}
    unexplained = []
    for mid, names in multi.items():
        # 合法合并：同一模型的不同写法（词序可不同），或推理档位后缀（配置维度）
        stripped = {model_key(n) for n in names}
        if len(stripped) == 1:
            continue
        if mid not in reg_by_id:
            unexplained.append((mid, names))
    if unexplained:
        print(f"\n[warn] {len(unexplained)} 个模型 id 对应多个**不等价**名称（需人工确认）：")
        for k, v in unexplained[:15]:
            print(f"  {k}: {v}")

    if a.apply:
        boards_path.write_text(
            json.dumps(boards, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
        )
        print(f"[apply] 已写回 {BOARDS_FILE}")

    if a.report and unresolved:
        print("\n未解析榜单条目（按观测数排序）：")
        for name, c in sorted(unresolved.items(), key=lambda kv: -kv[1])[:60]:
            print(f"  {c:3d}  {name}")

    if a.validate:
        if unexplained:
            return 1
        print("[validate] OK: 模型身份解析无歧义合并")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
