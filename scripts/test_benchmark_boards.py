#!/usr/bin/env python3
"""新增榜单源与跨榜拼图的离线自测。

运行：python3 -m unittest scripts.test_benchmark_boards.py -v
"""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fetch_benchmark_boards as fb  # noqa: E402
import resolve_models as rm  # noqa: E402
import expand_registry as er  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


# ---------------------------------------------------------------------------
# SWE-rebench（一榜多期）
# ---------------------------------------------------------------------------

# 模拟 Next.js flight 流的最小片段。真实页面的结构是：
#   ..."categories":[...],"series":[{"data":[{"type":"line","name":...,"data":[...]}]}]}
# 解析器从 `{"data":[{"type":"line"` 开始配平，故 fixture 必须让
# `"data"` 紧跟 `{`（真实页面正是如此）。
def _flight_chunk(obj) -> str:
    import json as _json
    payload = _json.dumps(obj, ensure_ascii=False)
    return 'self.__next_f.push([1,' + _json.dumps(payload) + '])'


SWE_REBENCH_HTML = (
    '<html><body><script>'
    + _flight_chunk({"data": [{"type": "line", "name": "gpt-5 [high] (tools)",
                               "data": [{"x": "Jan 2025", "y": 40.0},
                                        {"x": "Feb 2025", "y": 45.0}]},
                              {"type": "line", "name": "GLM-4.7 [high] (tools)",
                               "data": [{"x": "Jan 2025", "y": 30.0},
                                        {"x": "Feb 2025", "y": 35.0}]}]})
    + '</script></body></html>'
)


class TestSweRebenchParsing(unittest.TestCase):
    def setUp(self):
        self.obs, self.srcs = fb.parse_swe_rebench(SWE_REBENCH_HTML.encode("utf-8"))

    def test_all_periods_kept(self):
        """一榜多期：同一条目在多期的分数都必须保留，不能被去重吃掉。"""
        self.assertEqual(len(self.obs), 4)  # 2 模型 × 2 期

    def test_entry_id_includes_period(self):
        ids = {o["entry_id"] for o in self.obs}
        self.assertEqual(len(ids), 4)
        self.assertTrue(any("Jan 2025" in i for i in ids))

    def test_reasoning_effort_and_mode_extracted(self):
        o = next(x for x in self.obs if x["model_raw"] == "gpt-5 [high] (tools)")
        self.assertEqual(o["reasoning_effort"], "high")
        self.assertEqual(o["agent"], "tools")

    def test_period_converted_to_date(self):
        o = next(x for x in self.obs if x.get("period") == "Jan 2025")
        self.assertEqual(o["date"], "2025-01")

    def test_month_conversion(self):
        self.assertEqual(fb._period_to_date("Mar 2026"), "2026-03")
        self.assertEqual(fb._period_to_date("Dec 2025"), "2025-12")
        self.assertEqual(fb._period_to_date("garbage"), "")

    def test_source_is_level_a(self):
        self.assertTrue(self.srcs)
        self.assertEqual(self.srcs[0]["level"], "A")
        self.assertTrue(self.srcs[0]["url"].startswith("https://"))


# ---------------------------------------------------------------------------
# Aider edit / refactor（5 列表结构，与 polyglot 的 7 列不同）
# ---------------------------------------------------------------------------

AIDER_5COL = """
<table><thead><tr><th>Model</th><th>Percent completed correctly</th>
<th>Percent using correct edit format</th><th>Command</th><th>Edit Format</th></tr></thead><tbody>
<tr><td>o1</td><td>84.2%</td><td>99.2%</td><td>aider --model openai/o1</td><td>diff</td></tr>
<tr><td>claude-3-5-sonnet-20241022</td><td>80.0%</td><td>95.0%</td>
<td>aider --model anthropic/claude</td><td>diff</td></tr>
</tbody></table>
"""


class TestAiderFiveColumnTables(unittest.TestCase):
    def setUp(self):
        self.obs, self.srcs = fb.parse_aider_tables(AIDER_5COL.encode("utf-8"), "aider_edit")

    def test_rows_parsed(self):
        self.assertEqual(len(self.obs), 2)

    def test_model_name_read_from_first_column(self):
        self.assertEqual({o["model_raw"] for o in self.obs},
                         {"o1", "claude-3-5-sonnet-20241022"})

    def test_percentage_read_from_second_column(self):
        o = next(x for x in self.obs if x["model_raw"] == "o1")
        self.assertAlmostEqual(o["value"], 84.2)

    def test_scope_declares_task_difference(self):
        """不同任务的榜必须写明不可互相比较。"""
        self.assertIn("不可互相比较", fb.AIDER_TABLES["aider_edit"]["scope"])


# ---------------------------------------------------------------------------
# Arena-Hard-Auto（带置信区间）
# ---------------------------------------------------------------------------

ARENA_HARD_CSV = """model,score,rating_q025,rating_q975,CI,avg_tokens,date
gpt-4o-2024-05-13,79.21,77.42,80.71,"(1.8, 1.5)",696.0,2024-07-31
claude-3-5-sonnet-20240620,79.35,77.25,80.62,"(2.1, 1.3)",567.0,2024-07-31
"""


class TestArenaHardParsing(unittest.TestCase):
    def setUp(self):
        self.obs, self.srcs = fb.parse_arena_hard(ARENA_HARD_CSV.encode("utf-8"))

    def test_rows_parsed(self):
        self.assertEqual(len(self.obs), 2)

    def test_confidence_interval_kept(self):
        o = next(x for x in self.obs if x["model_raw"] == "gpt-4o-2024-05-13")
        self.assertIn("置信区间", o["note"])
        self.assertIn("77.42", o["note"])

    def test_token_usage_kept(self):
        o = self.obs[0]
        self.assertIn("tokens", o["note"])

    def test_unit_is_score_not_percent(self):
        for o in self.obs:
            self.assertEqual(o["metric_unit"], "score")
            self.assertEqual(o["metric_max"], 100)


# ---------------------------------------------------------------------------
# 注册表自动扩充
# ---------------------------------------------------------------------------

class TestRegistryExpansion(unittest.TestCase):
    def test_display_name_keeps_readable_form(self):
        """清洗配置后缀不应把 "GPT 4.1" 压成 "gpt41"。"""
        self.assertEqual(er.clean_display("gpt-4.1-2025-04-14 (tools)"), "gpt-4.1-2025-04-14")
        self.assertEqual(er.clean_display("Claude Opus 4.6-high (tools)"), "Claude Opus 4.6-high")
        self.assertEqual(er.clean_display("GLM-4.5 Air (tools)"), "GLM-4.5")

    def test_provider_detection_by_flattened_prefix(self):
        self.assertEqual(er.detect_provider("gpt41"), "OpenAI")
        self.assertEqual(er.detect_provider("qwen332b"), "阿里巴巴")
        self.assertEqual(er.detect_provider("llama3370binstruct"), "Meta")

    def test_agent_models_are_flagged(self):
        self.assertTrue(er.is_agent("claudecode"))
        self.assertTrue(er.is_agent("cursor"))
        self.assertFalse(er.is_agent("gpt41"))

    def test_id_generation_is_slug(self):
        self.assertEqual(er.make_id("GPT 4.1"), "gpt-4-1")
        self.assertNotIn(" ", er.make_id("Claude Opus 4.6"))


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

    def test_multi_period_ranks_are_period_local(self):
        """一榜多期的名次必须严格按评测期分组，不能跨期混排。"""
        path = ROOT / fb.OUTPUT_FILE
        if not path.exists():
            self.skipTest("缺少榜单数据文件")
        data = json.loads(path.read_text(encoding="utf-8"))
        for b in data["boards"]:
            bobs = [o for o in data["observations"] if o["board"] == b["id"]]
            if not any(o.get("period") for o in bobs):
                continue
            by_period: dict[str, list[dict]] = {}
            for o in bobs:
                by_period.setdefault(str(o.get("period") or ""), []).append(o)
            for period, group in by_period.items():
                ranks = sorted(o["rank"] for o in group if o.get("rank") is not None)
                self.assertEqual(ranks, list(range(1, len(group) + 1)),
                                 f"榜单 {b['id']} 评测期 {period} 名次非期内连续")

    def test_registry_expanded(self):
        path = ROOT / rm.REGISTRY_FILE
        if not path.exists():
            self.skipTest("缺少模型注册表")
        reg = json.loads(path.read_text(encoding="utf-8"))
        ids = [m["id"] for m in reg["models"]]
        self.assertEqual(len(ids), len(set(ids)), "注册表存在重复 id")
        self.assertGreater(len(reg["models"]), 200, "注册表条目过少")

    def test_leaderboard_sources_are_all_level_a(self):
        path = ROOT / fb.OUTPUT_FILE
        if not path.exists():
            self.skipTest("缺少榜单数据文件")
        data = json.loads(path.read_text(encoding="utf-8"))
        for s in data["sources"]:
            self.assertEqual(s["level"], "A", f"来源 {s['id']} 不是 A 级")
            self.assertTrue(s["url"].startswith("https://"))

    def test_most_leaderboard_entries_resolved(self):
        """绝大多数榜单条目应能归一到注册表。"""
        path = ROOT / fb.OUTPUT_FILE
        if not path.exists():
            self.skipTest("缺少榜单数据文件")
        data = json.loads(path.read_text(encoding="utf-8"))
        reg = json.loads((ROOT / rm.REGISTRY_FILE).read_text(encoding="utf-8"))
        exact, loose = rm.build_index(reg)
        resolved = sum(1 for o in data["observations"]
                       if rm.resolve(o["model"], exact, loose)[0])
        self.assertGreater(resolved / len(data["observations"]), 0.9)

    def test_no_ambiguous_merge(self):
        path = ROOT / fb.OUTPUT_FILE
        if not path.exists():
            self.skipTest("缺少榜单数据文件")
        data = json.loads(path.read_text(encoding="utf-8"))
        reg = json.loads((ROOT / rm.REGISTRY_FILE).read_text(encoding="utf-8"))
        exact, loose = rm.build_index(reg)
        idmap: dict[str, set[str]] = {}
        for o in data["observations"]:
            mid, _ = rm.resolve(o["model"], exact, loose)
            if mid:
                idmap.setdefault(mid, set()).add(o["model"])
        for mid, names in idmap.items():
            stripped = {rm.model_key(n) for n in names}
            self.assertEqual(len(stripped), 1,
                             f"模型 id {mid} 对应多个不等价名称: {sorted(names)}")


if __name__ == "__main__":
    unittest.main()
