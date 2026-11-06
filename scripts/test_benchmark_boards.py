#!/usr/bin/env python3
"""榜单抓取、模型身份解析与看板 roster 呈现的离线自测。

运行：python3 -m unittest scripts.test_benchmark_boards.py -v
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fetch_benchmark_boards as fb  # noqa: E402
import resolve_models as rm  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


# ---------------------------------------------------------------------------
# 样例数据
# ---------------------------------------------------------------------------

SWE_SAMPLE = {
    "leaderboards": [
        {
            "name": "Verified",
            "results": [
                {
                    "model_display": "GPT-5", "model_org": "OpenAI", "agent": "mini-SWE-agent",
                    "reasoning_effort": "high", "resolved": 79.2, "date": "2026-02-13",
                    "model_release_date": 20250901,
                },
                {
                    "model_display": "GPT-5", "model_org": "OpenAI", "agent": "OpenHands",
                    "reasoning_effort": None, "resolved": 70.1, "date": "2026-02-20",
                    "model_release_date": 20250901,
                },
                {
                    "model_display": "Undisclosed", "model_org": None, "agent": "RAG baseline",
                    "reasoning_effort": None, "resolved": 55.0, "date": "2026-01-01",
                },
                {
                    "model_display": "Multiple", "model_org": None, "agent": "Tools",
                    "reasoning_effort": None, "resolved": 40.0, "date": "2026-01-02",
                },
                {
                    "model_display": "Claude 4.5 Opus", "model_org": "Anthropic",
                    "agent": "mini-SWE-agent", "reasoning_effort": None, "resolved": 60.5,
                    "date": "2026-02-26", "model_release_date": 20251101,
                },
            ],
        },
        {"name": "Lite", "results": []},
    ]
}

AIDER_SAMPLE = """
<table><thead><tr><th></th><th>Model</th><th>Percent correct</th><th>Cost</th>
<th>Command</th><th>Correct edit format</th><th>Edit Format</th></tr></thead><tbody>
<tr><td>&#9654;</td><td>gpt-5 (high)</td><td>88.0%</td><td>$29.08</td>
<td>aider --model openai/gpt-5</td><td>91.6%</td><td>diff</td></tr>
<tr><td></td><td>Claude 4.5 Opus</td><td>70.0%</td><td>$12.00</td>
<td>aider --model anthropic/claude</td><td>88.0%</td><td>diff</td></tr>
<tr><td></td><td>broken row</td><td>-</td><td>$0</td><td>x</td><td>0%</td><td>diff</td></tr>
</tbody></table>
"""

LMARENA_SAMPLE = """key,Model,MT-bench (score),MMLU,Knowledge cutoff date,License,Organization,Link
gpt-4o,ChatGPT-4o,9.26,0.880,2023-10,Custom,OpenAI,https://example.com
claude,Claude 3.5 Sonnet,8.90,0.810,2024-04,Custom,Anthropic,https://example.com
old,GPT-2,3.10,0.320,2019-01,MIT,OpenAI,https://example.com
"""


# ---------------------------------------------------------------------------
# SWE-bench 解析
# ---------------------------------------------------------------------------

class TestSwebenchParsing(unittest.TestCase):
    def setUp(self):
        raw = json.dumps(SWE_SAMPLE).encode("utf-8")
        self.obs, self.srcs = fb.parse_swebench(raw)

    def test_placeholder_entries_are_excluded(self):
        """Undisclosed / Multiple 不是具体模型版本，必须剔除。"""
        names = {o["model_raw"] for o in self.obs}
        self.assertNotIn("Undisclosed", names)
        self.assertNotIn("Multiple", names)

    def test_same_model_different_agent_are_separate_entries(self):
        """同一模型换 agent 分数不同，必须是两条独立条目。"""
        gpt5 = [o for o in self.obs if o["model_raw"] == "GPT-5"]
        self.assertEqual(len(gpt5), 2)
        self.assertNotEqual(gpt5[0]["entry_id"], gpt5[1]["entry_id"])
        self.assertNotEqual(gpt5[0]["value"], gpt5[1]["value"])

    def test_entry_id_contains_agent_and_effort(self):
        o = next(x for x in self.obs if x["model_raw"] == "GPT-5"
                 and x["agent"] == "mini-SWE-agent")
        self.assertIn("mini-SWE-agent", o["entry_id"])
        self.assertIn("high", o["entry_id"])

    def test_reasoning_effort_recorded(self):
        o = next(x for x in self.obs if x["reasoning_effort"] == "high")
        self.assertEqual(o["model_raw"], "GPT-5")
        self.assertIn("reasoning effort", o["note"])

    def test_source_is_level_a_with_https(self):
        self.assertTrue(self.srcs)
        for s in self.srcs:
            self.assertEqual(s["level"], "A")
            self.assertTrue(s["url"].startswith("https://"))

    def test_release_date_preserved(self):
        o = next(x for x in self.obs if x["model_raw"] == "Claude 4.5 Opus")
        self.assertEqual(o["model_release_date"], "20251101")


# ---------------------------------------------------------------------------
# Aider 解析
# ---------------------------------------------------------------------------

class TestAiderParsing(unittest.TestCase):
    def setUp(self):
        self.obs, self.srcs = fb.parse_aider(AIDER_SAMPLE.encode("utf-8"))

    def test_rows_parsed(self):
        self.assertEqual(len(self.obs), 2)

    def test_config_suffix_preserved_in_model_name(self):
        """gpt-5 (high) 与 gpt-5 (low) 是不同配置，模型名必须保留档位后缀。"""
        names = {o["model_raw"] for o in self.obs}
        self.assertIn("gpt-5 (high)", names)

    def test_invalid_percent_rows_skipped(self):
        self.assertNotIn("broken row", {o["model_raw"] for o in self.obs})

    def test_edit_format_recorded_as_agent(self):
        o = next(x for x in self.obs if x["model_raw"] == "gpt-5 (high)")
        self.assertIn("diff", o["agent"])


# ---------------------------------------------------------------------------
# LMArena 解析
# ---------------------------------------------------------------------------

class TestLmarenaParsing(unittest.TestCase):
    def setUp(self):
        self.obs, self.srcs = fb.parse_lmarena(LMARENA_SAMPLE.encode("utf-8"))

    def test_two_metrics_split_into_two_boards(self):
        """MT-bench（1–10 分）与 MMLU（0–1 比例）单位不同，必须拆榜。"""
        boards = {o["board"] for o in self.obs}
        self.assertEqual(boards, {"lmarena_mtbench", "lmarena_mmlu"})

    def test_mmlu_converted_to_percent(self):
        o = next(x for x in self.obs if x["metric_key"] == "mmlu"
                 and x["model_raw"] == "ChatGPT-4o")
        self.assertAlmostEqual(o["value"], 88.0)
        self.assertIn("换算", o["note"])

    def test_mt_bench_keeps_original_scale(self):
        o = next(x for x in self.obs if x["metric_key"] == "mt_bench"
                 and x["model_raw"] == "ChatGPT-4o")
        self.assertAlmostEqual(o["value"], 9.26)

    def test_duplicate_model_rows_deduped(self):
        raw = (LMARENA_SAMPLE + "gpt-4o,ChatGPT-4o,9.26,0.880,2023-10,Custom,OpenAI,x\n").encode()
        obs, _ = fb.parse_lmarena(raw)
        self.assertEqual(len([o for o in obs if o["model_raw"] == "ChatGPT-4o"
                              and o["metric_key"] == "mt_bench"]), 1)

    def test_rows_without_any_metric_skipped(self):
        raw = (LMARENA_SAMPLE + "x,Unknown Model,-,-,-,-,-,-\n").encode()
        obs, _ = fb.parse_lmarena(raw)
        self.assertNotIn("Unknown Model", {o["model_raw"] for o in obs})


# ---------------------------------------------------------------------------
# 模型身份解析
# ---------------------------------------------------------------------------

class TestModelResolution(unittest.TestCase):
    def setUp(self):
        self.reg = {
            "models": [
                {"id": "openai-gpt-5", "name": "GPT-5", "provider": "OpenAI",
                 "aliases": ["GPT 5"], "snapshot": "", "note": ""},
                {"id": "anthropic-claude-opus-4.5", "name": "Claude Opus 4.5",
                 "provider": "Anthropic", "aliases": ["Claude 4.5 Opus"], "snapshot": "", "note": ""},
                {"id": "google-gemma-2-9b", "name": "Gemma 2 9B", "provider": "Google",
                 "aliases": ["gemma-2-9b"], "snapshot": "", "note": ""},
            ]
        }
        self.exact, self.loose = rm.build_index(self.reg)

    def test_exact_alias_match(self):
        mid, how = rm.resolve("GPT 5", self.exact, self.loose)
        self.assertEqual(mid, "openai-gpt-5")
        self.assertEqual(how, "exact")

    def test_loose_match_for_format_variants(self):
        mid, _ = rm.resolve("GPT-5", self.exact, self.loose)
        self.assertEqual(mid, "openai-gpt-5")

    def test_config_suffix_does_not_create_new_model(self):
        """gpt-5 (high) 与 gpt-5 是同一模型的不同配置。"""
        mid, _ = rm.resolve("gpt-5 (high)", self.exact, self.loose)
        self.assertEqual(mid, "openai-gpt-5")

    def test_unrelated_name_unresolved(self):
        mid, how = rm.resolve("Totally Unknown Model", self.exact, self.loose)
        self.assertIsNone(mid)
        self.assertEqual(how, "unresolved")

    def test_strip_config_suffix_identifies_same_model(self):
        self.assertEqual(
            rm.strip_config_suffix("gpt-5 (high)"),
            rm.strip_config_suffix("GPT-5"),
        )

    def test_conflicting_alias_is_dropped_from_index(self):
        reg = {"models": [
            {"id": "a", "name": "X", "aliases": ["same"], "provider": "p"},
            {"id": "b", "name": "Y", "aliases": ["same"], "provider": "p"},
        ]}
        exact, _ = rm.build_index(reg)
        self.assertNotIn("same", exact)


# ---------------------------------------------------------------------------
# 真实仓库数据
# ---------------------------------------------------------------------------

class TestRealRepositoryData(unittest.TestCase):
    def test_boards_data_validates(self):
        path = ROOT / fb.OUTPUT_FILE
        if not path.exists():
            self.skipTest("缺少榜单数据文件")
        data = json.loads(path.read_text(encoding="utf-8"))
        errors, _ = fb.validate(data)
        self.assertEqual(errors, [], f"榜单数据校验失败: {errors[:5]}")

    def test_boards_roster_entries_match_declared(self):
        path = ROOT / fb.OUTPUT_FILE
        if not path.exists():
            self.skipTest("缺少榜单数据文件")
        data = json.loads(path.read_text(encoding="utf-8"))
        for b in data["boards"]:
            actual = len({o["entry_id"] for o in data["observations"]
                          if o["board"] == b["id"]})
            self.assertEqual(actual, b["entries"], f"榜单 {b['id']} 条目数不符")

    def test_leaderboard_sources_are_all_level_a(self):
        path = ROOT / fb.OUTPUT_FILE
        if not path.exists():
            self.skipTest("缺少榜单数据文件")
        data = json.loads(path.read_text(encoding="utf-8"))
        for s in data["sources"]:
            self.assertEqual(s["level"], "A", f"来源 {s['id']} 不是 A 级")
            self.assertTrue(s["url"].startswith("https://"))

    def test_registry_validates(self):
        path = ROOT / rm.REGISTRY_FILE
        if not path.exists():
            self.skipTest("缺少模型注册表")
        reg = json.loads(path.read_text(encoding="utf-8"))
        ids = [m["id"] for m in reg["models"]]
        self.assertEqual(len(ids), len(set(ids)), "注册表存在重复 id")
        for m in reg["models"]:
            self.assertTrue(m.get("id") and m.get("name") and m.get("provider"),
                            f"注册表条目缺字段: {m}")
            self.assertNotIn(" ", m["id"], f"模型 id 不应含空格: {m['id']}")

    def test_board_observations_have_model_id_resolved(self):
        path = ROOT / fb.OUTPUT_FILE
        if not path.exists():
            self.skipTest("缺少榜单数据文件")
        data = json.loads(path.read_text(encoding="utf-8"))
        reg = json.loads((ROOT / rm.REGISTRY_FILE).read_text(encoding="utf-8"))
        exact, loose = rm.build_index(reg)
        resolved = 0
        for o in data["observations"]:
            mid, _ = rm.resolve(o["model"], exact, loose)
            if mid:
                resolved += 1
        # 至少一半的榜单条目应能归一到注册表（其余为长尾模型，需人工补录）
        self.assertGreater(resolved, len(data["observations"]) * 0.3)


if __name__ == "__main__":
    unittest.main()
