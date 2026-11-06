#!/usr/bin/env python3
"""为榜单中出现但注册表缺失的模型批量补登记条目。

从 data/benchmark_observations.json / data/benchmark_boards.json 里收集
所有出现过的模型名，剥离配置后缀（推理档位、调用模式、快照日期），
对注册表中尚未收录的 base 名生成条目。

原则：
  * 只登记**能从名称可靠判定**的模型（去掉配置后缀后仍是一个明确的产品名）。
  * 工具型 agent（Claude Code、Cursor、Codex、Junie 等）单独标注 kind=agent，
    它们不是基础模型，与模型不可混谈。
  * 无法可靠判定提供方的写「未标注」，不猜。

用法：
    python3 scripts/expand_registry.py            # 预览将新增的条目
    python3 scripts/expand_registry.py --apply    # 写回 data/model_registry.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import resolve_models as rm  # noqa: E402

REGISTRY_FILE = Path("data/model_registry.json")
BOARDS_FILE = Path("data/benchmark_boards.json")
OBS_FILE = Path("data/benchmark_observations.json")

# 工具型 agent：不是基础模型，单独标注
AGENT_NAMES = {
    "claude code": "Anthropic", "codex": "OpenAI", "cursor": "Cursor",
    "junie": "JetBrains", "roo code": "Roo", "cline": "Cline",
    "aider": "Aider", "devin": "Cognition", "replit agent": "Replit",
}

# 已知的模型家族 → 提供方，用于给新条目填 provider
FAMILY_PROVIDER = [
    ("gpt-oss", "OpenAI"), ("gpt-", "OpenAI"), ("o3", "OpenAI"), ("o4", "OpenAI"),
    ("claude", "Anthropic"), ("gemini", "Google"), ("gemma", "Google"),
    ("llama", "Meta"), ("codestral", "Mistral AI"), ("mistral", "Mistral AI"),
    ("mixtral", "Mistral AI"), ("magistral", "Mistral AI"), ("devstral", "Mistral AI"),
    ("command", "Cohere"), ("qwen", "阿里巴巴"), ("qwq", "阿里巴巴"),
    ("deepseek", "DeepSeek"), ("kimi", "月之暗面"), ("glm", "智谱 AI"),
    ("minimax", "MiniMax"), ("grok", "xAI"), ("doubao", "字节跳动"),
    ("ernie", "百度"), ("hunyuan", "腾讯"), ("nova", "Amazon"),
    ("phi-", "Microsoft"), ("yi-", "零一万物"), ("mimo", "小米"),
    ("lingma", "阿里巴巴"), ("ling-", "蚂蚁集团"), ("athene", "无问芯穹"),
    ("reka", "Reka"), ("deepcog", "DeepCog"), ("fable", "Anthropic"),
    ("junie", "JetBrains"), ("muse", "Meta"), ("olmo", "AI2"),
    ("nemotron", "NVIDIA"), ("jamba", "AI21 Labs"), ("baize", "Baize"),
    ("dbrx", "Databricks"), ("falcon", "TII"), ("vicuna", "LMSYS"),
    ("alpaca", "Stanford"), ("guanaco", "Meta"), ("koala", "HuggingFace"),
    ("zephyr", "HuggingFace"), ("wizardlm", "Microsoft"), ("tulu", "AI2"),
    ("olmo", "AI2"), ("starling", "Nvidia"), ("solar", "Upstage"),
    ("openchat", "OpenChat"), ("openassistant", "OpenAssistant"),
    ("nous", "Nous Research"), ("h2o", "H2O.ai"), ("rwkv", "RWKV"),
    ("mpt", "MosAIC AI"), ("xgen", "Salesforce"), ("xgen", "xAI"),
    ("mpt", "MosAIC AI"), ("fuyu", "Adept"), ("snowflake", "Snowflake"),
    ("chatglm", "智谱 AI"), ("mcts refine", "华为"), ("lingma swe", "阿里巴巴"),
    ("frog", "Frog"), ("horizon", "Horizon Robotics"), ("dracarys", "Nous Research"),
    ("peanut", "Peanut"), ("atlas", "Atlas"), ("gpt4all", "GPT4All"),
    ("chatgpt", "OpenAI"), ("dolly", "Databricks"), ("fastchat", "FastChat"),
    ("codeqwen", "阿里巴巴"), ("copatcher", "Cohere"), ("codellama", "Meta"),
    ("codeact", "THUDM"), ("sweagent", "Princeton"), ("openhands", "All Hands AI"),
    ("sonnet", "Anthropic"), ("opus", "Anthropic"), ("haiku", "Anthropic"),
    ("mythos", "Anthropic"), ("fable", "Anthropic"),
]


def detect_provider(base: str) -> str:
    """按去配置后的 base 名判定提供方。

    注意 base 已剥离标点（如 "GPT 4.1" → "gpt41"），因此匹配时
    也要用同样归一化的前缀，避免 "gpt41" 匹配不上 "gpt-"。
    """
    low = base.lower()
    flat = re.sub(r"[^0-9a-z]+", "", low)
    for key, prov in AGENT_NAMES.items():
        if low == key or low.startswith(key + " ") or low.startswith(key + "-"):
            return prov
        if flat == re.sub(r"[^0-9a-z]+", "", key):
            return prov
    # 用「去标点后仍可辨识」的前缀表
    flat = re.sub(r"[^0-9a-z]+", "", low)
    for prefix, prov in FAMILY_PROVIDER:
        p = re.sub(r"[^0-9a-z]+", "", prefix.lower())
        if flat.startswith(p):
            return prov
    return "未标注"


def is_agent(base: str) -> bool:
    """判断是否工具型 agent。

    base 已剥离标点（"Claude Code" → "claudecode"），
    因此比较时需同时尝试「原名」与「去标点名」两种形态。
    """
    low = base.lower()
    flat = re.sub(r"[^0-9a-z]+", "", low)
    for k in AGENT_NAMES:
        if low == k or low.startswith(k + " ") or low.startswith(k + "-"):
            return True
        if flat == re.sub(r"[^0-9a-z]+", "", k):
            return True
    return False


def clean_display(raw: str) -> str:
    """把原始榜单写法清理成可读展示名。

    只去掉**末尾**的配置标注（调用模式 / 推理档位 / 快照日期），
    保留模型主体原有的可读形式（如 "GPT-4.1" 不会被压成 "gpt41"）。
    """
    s = raw.strip()
    # 末尾圆括号：先判断是否是配置（text/tools/thinking 等），是则去掉整段
    for _ in range(3):
        m = re.search(r"\s*\(([^()]*)\)\s*$", s)
        if not m:
            break
        inner = m.group(1).lower()
        if re.search(r"text|tools|think|reason|chat|base|preview|diff|whole|none|k_?m|q\d", inner):
            s = s[: m.start()].strip()
            continue
        break
    # 末尾方括号推理档位
    s = re.sub(r"\s*\[[a-z0-9 _-]{1,12}\]\s*$", "", s, flags=re.I).strip()
    # 空格分隔的 no-thinking / thinking / Air
    s = re.sub(r"\s+(?:no-?thinking|no-?think|thinking|think|reasoner|air)\s*$", "", s,
               flags=re.I).strip()
    return s or raw.strip()


def collect_names(root: Path) -> dict[str, dict]:
    """收集所有出现过的模型名 → {base: {display, count, boards, agent}}"""
    found: dict[str, dict] = {}

    def add(raw: str, board: str, agent: str) -> None:
        base = rm.strip_config_suffix(raw)
        if not base:
            return
        rec = found.setdefault(base, {"display": clean_display(raw), "count": 0,
                                      "boards": set(), "agent": agent})
        rec["count"] += 1
        rec["boards"].add(board)
        if agent:
            rec["agent"] = agent

    boards_path = root / BOARDS_FILE
    if boards_path.exists():
        b = json.loads(boards_path.read_text(encoding="utf-8"))
        for o in b.get("observations", []):
            add(o.get("model_raw") or o.get("model", ""),
                o.get("board", ""), o.get("agent", ""))

    obs_path = root / OBS_FILE
    if obs_path.exists():
        d = json.loads(obs_path.read_text(encoding="utf-8"))
        for o in d.get("observations", []):
            add(o.get("model", ""), o.get("group", ""), "")

    return found


def make_id(base: str) -> str:
    s = re.sub(r"[^0-9a-zA-Z]+", "-", base).strip("-").lower()
    return s or "unknown-model"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=".", help="仓库根目录")
    p.add_argument("--apply", action="store_true", help="写回注册表")
    p.add_argument("--min-count", type=int, default=1,
                   help="只收录出现次数不少于该值的模型")
    a = p.parse_args(argv)
    root = Path(a.root).resolve()

    reg_path = root / REGISTRY_FILE
    reg = json.loads(reg_path.read_text(encoding="utf-8"))
    exact, loose = rm.build_index(reg)
    existing_ids = {m["id"] for m in reg["models"]}

    found = collect_names(root)
    new_models: list[dict] = []
    skipped = 0

    for base, rec in sorted(found.items(), key=lambda kv: -kv[1]["count"]):
        if rec["count"] < a.min_count:
            continue
        mid, how = rm.resolve(rec["display"], exact, loose)
        if mid:
            continue
        # base 本身可能已被注册（只是写法不同）——用 base 再查一次
        mid, how = rm.resolve(base, exact, loose)
        if mid:
            continue
        if not base or len(base) < 2:
            skipped += 1
            continue

        mid = make_id(base)
        if mid in existing_ids:
            mid = mid + "-x"
        existing_ids.add(mid)

        provider = detect_provider(base)
        new_models.append({
            "id": mid,
            "name": rec["display"],
            "provider": provider,
            "aliases": [base] if base != rec["display"] else [],
            "snapshot": "",
            "note": ("工具型 agent，非基础模型" if is_agent(base) else "") +
                    ("；由榜单抓取自动登记" if not is_agent(base) else ""),
            "_count": rec["count"],
            "_boards": sorted(rec["boards"]),
            "_agent": is_agent(base),
        })

    print(f"注册表现有 {len(reg['models'])} 条；新增候选 {len(new_models)} 条（跳过 {skipped}）")
    for m in new_models[:60]:
        print(f"  + {m['id']:44s} {m['name'][:40]:40s} {m['provider']:12s} ×{m['_count']}")
    if len(new_models) > 60:
        print(f"  ... 还有 {len(new_models) - 60} 条")

    if a.apply:
        for m in new_models:
            m.pop("_count", None)
            m.pop("_boards", None)
            m.pop("_agent", None)
        reg["models"].extend(new_models)
        reg["meta"]["auto_expanded"] = (
            "部分条目由 scripts/expand_registry.py 依据榜单抓取结果自动登记，"
            "provider 可能为「未标注」，引用前建议核对官方模型卡。"
        )
        reg_path.write_text(json.dumps(reg, ensure_ascii=False, indent=2) + "\n",
                            encoding="utf-8")
        print(f"[apply] 已写入 {REGISTRY_FILE}，共 {len(reg['models'])} 条")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
