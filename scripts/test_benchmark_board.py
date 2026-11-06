#!/usr/bin/env python3
"""benchmark 看板的数据校验、渲染与交互离线自测。

运行：python3 -m unittest scripts.test_benchmark_board.py -v
"""

from __future__ import annotations

import contextlib
import copy
import io
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import render_benchmark_board as m  # noqa: E402


def obs(**kw) -> dict:
    base = {
        "model": "M1", "provider": "P1", "benchmark": "B1", "metric": "指标1",
        "key": "k1", "value": 80.0, "group": "g1", "date": "2026-11-06",
        "src": "s1", "note": "自测观测",
    }
    base.update(kw)
    return base


def make_data() -> dict:
    return {
        "meta": {
            "version": "1.0", "updated": "2026-11-06",
            "principle": "长表", "missing_policy": "缺失显式标注",
            "duplicate_policy": "主键唯一", "unit_policy": "组统一",
            "source_note": "自测",
        },
        "groups": [
            {"id": "g1", "label": "组一", "unit": "percent", "direction": "higher",
             "scope": "口径一", "kind": "benchmark"},
            {"id": "g2", "label": "组二", "unit": "percent", "direction": "lower",
             "scope": "口径二（越低越好）", "kind": "safety"},
        ],
        "sources": [
            {"id": "s1", "level": "A", "url": "https://example.com/a", "ref": "fixture", "note": ""},
            {"id": "s2", "level": "B", "url": "https://example.com/b", "ref": "fixture", "note": ""},
        ],
        "observations": [
            obs(model="M1", benchmark="B1", key="k1", value=80.0, group="g1", rank=1),
            obs(model="M2", benchmark="B1", key="k1", value=65.0, group="g1", rank=2),
            obs(model="M1", benchmark="B2", key="k2", value=3.3, group="g2", src="s2"),
            obs(model="M3", benchmark="B3", key="k3", value=None, group="g1",
                status="not_disclosed", note="官方未披露"),
        ],
        "leaderboards": [
            {"id": "lb1", "label": "榜单一", "scope": "口径：官方榜", "kind": "leaderboard",
             "metrics": ["rk1"], "entries": 2, "observations": 2, "models": 1,
             "source": {"id": "lbs1", "level": "A", "url": "https://example.com/lb",
                        "ref": "fixture", "captured": "2026-11-06"}},
        ],
        "leaderboard_metrics": [
            {"key": "rk1", "label": "榜内指标", "unit": "percent", "max": 100,
             "boards": ["lb1"]},
        ],
        "leaderboard_sources": [
            {"id": "lbs1", "level": "A", "url": "https://example.com/lb",
             "ref": "fixture", "captured": "2026-11-06", "note": ""},
        ],
        "leaderboard_meta": {"principle": "榜单原则", "roster_note": "roster 说明"},
        "leaderboard_observations": [
            {"board": "lb1", "board_label": "榜单一", "model_raw": "M1", "model": "M1",
             "provider_raw": "P1", "provider": "P1", "metric_key": "rk1",
             "metric_label": "榜内指标", "value": 75.0, "rank": 1, "date": "2026-11-06",
             "entry_id": "M1|agentA", "agent": "agentA", "reasoning_effort": "",
             "model_release_date": "", "note": "agent: agentA", "src": "lbs1"},
            {"board": "lb1", "board_label": "榜单一", "model_raw": "M1", "model": "M1",
             "provider_raw": "P1", "provider": "P1", "metric_key": "rk1",
             "metric_label": "榜内指标", "value": 68.0, "rank": 2, "date": "2026-11-06",
             "entry_id": "M1|agentB", "agent": "agentB", "reasoning_effort": "",
             "model_release_date": "", "note": "agent: agentB", "src": "lbs1"},
        ],
        "registry": [
            {"id": "p1-m1", "name": "M1", "provider": "P1", "aliases": ["M1"],
             "snapshot": "", "note": ""},
        ],
    }


def fixture(root: Path, data: dict | None = None) -> dict:
    (root / "data").mkdir(parents=True, exist_ok=True)
    payload = data if data is not None else make_data()
    (root / m.DATA_FILE).write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    # 榜单数据单独成文件，fixture 同步写出，使合并路径被真实覆盖
    boards = {
        "meta": {"principle": "榜单原则", "roster_note": "roster 说明"},
        "boards": payload.get("leaderboards", []),
        "metrics": payload.get("leaderboard_metrics", []),
        "sources": payload.get("leaderboard_sources", []),
        "observations": payload.get("leaderboard_observations", []),
    }
    (root / m.BOARDS_FILE).write_text(
        json.dumps(boards, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return payload


class TestValidation(unittest.TestCase):
    def test_valid_fixture_passes(self):
        errs, _ = m.validate(make_data())
        self.assertEqual(errs, [])

    def test_duplicate_primary_key_detected(self):
        d = make_data()
        d["observations"].append(obs(model="M1", benchmark="B1", key="k1", value=99))
        self.assertTrue(any("主键重复" in e for e in m.validate(d)[0]))

    def test_null_value_requires_not_disclosed(self):
        d = make_data()
        d["observations"].append(obs(model="M4", benchmark="B4", key="k4", value=None))
        self.assertTrue(any("not_disclosed" in e for e in m.validate(d)[0]))

    def test_not_disclosed_with_value_detected(self):
        d = make_data()
        d["observations"].append(obs(model="M4", benchmark="B4", key="k4",
                                     value=10, status="not_disclosed"))
        self.assertTrue(any("有数值却标记" in e for e in m.validate(d)[0]))

    def test_percent_out_of_range_detected(self):
        d = make_data()
        d["observations"][0]["value"] = 120
        self.assertTrue(any("越界" in e for e in m.validate(d)[0]))

    def test_unknown_group_and_source_detected(self):
        d = make_data()
        d["observations"][0]["group"] = "ghost"
        d["observations"][1]["src"] = "ghost"
        errs = m.validate(d)[0]
        self.assertTrue(any("未知可比组" in e for e in errs))
        self.assertTrue(any("未知来源" in e for e in errs))

    def test_observation_must_not_declare_unit(self):
        d = make_data()
        d["observations"][0]["unit"] = "score"
        self.assertTrue(any("应由 group 统一定义" in e for e in m.validate(d)[0]))

    def test_invalid_rank_detected(self):
        d = make_data()
        d["observations"][0]["rank"] = 0
        self.assertTrue(any("rank 必须" in e for e in m.validate(d)[0]))

    def test_rank_on_disclosed_value_detected(self):
        d = make_data()
        d["observations"][3]["rank"] = 1
        self.assertTrue(any("未披露的观测不得有排名" in e for e in m.validate(d)[0]))

    def test_non_https_source_detected(self):
        d = make_data()
        d["sources"][0]["url"] = "http://example.com/a"
        self.assertTrue(any("非 HTTPS" in e for e in m.validate(d)[0]))

    def test_cross_group_metric_is_warning_not_error(self):
        d = make_data()
        # 同名 key 出现在两个不同口径组
        d["observations"].append(obs(model="M5", benchmark="B5", key="k1",
                                     value=58, group="g2"))
        errs, warns = m.validate(d)
        self.assertEqual(errs, [])
        self.assertTrue(any("禁止直接比较" in w for w in warns))


class TestViewModel(unittest.TestCase):
    def test_build_view_enriches_and_counts(self):
        v = m.build_view(make_data())
        self.assertEqual(v["stats"]["models"], 3)
        self.assertEqual(v["stats"]["observations"], 6)  # 4 条公告 + 2 条榜单
        self.assertEqual(v["stats"]["valued"], 5)   # 3 条公告 + 2 条榜单
        self.assertEqual(v["stats"]["not_disclosed"], 1)
        self.assertEqual(v["observations"][2]["direction"], "lower")
        self.assertEqual(v["observations"][2]["level"], "B")

    def test_coverage_excludes_disclosed_nulls(self):
        v = m.build_view(make_data())
        self.assertEqual(v["coverage"]["M3"]["groups"], 0)
        self.assertEqual(v["coverage"]["M1"]["groups"], 3)  # g1 / g2 / lb1
        self.assertEqual(v["coverage"]["M1"]["ratio"], 1.0)

    def test_real_repository_data_valid(self):
        root = Path(__file__).resolve().parent.parent
        if (root / m.DATA_FILE).exists():
            errs, _ = m.validate(m.load_data(root))
            self.assertEqual(errs, [])
            v = m.build_view(m.load_data(root))
            self.assertGreater(v["stats"]["models"], 10)
            self.assertGreater(v["stats"]["observations"], 40)
            self.assertGreater(v["stats"]["not_disclosed"], 0)


class TestRendering(unittest.TestCase):
    def test_html_contains_inline_data_and_key_widgets(self):
        d = make_data()
        page = m.render_html(d, m.build_view(d))
        for frag in ("const DATA =", "renderStats()", "renderMatrix()", "renderCompare()",
                     "跨组按数值排序已禁用", "未披露", "同名跨口径",
                     "--bg:#0d1117", "index.html"):
            self.assertIn(frag, page)
        self.assertEqual(page.count("<script>"), 1)
        self.assertEqual(page.count("</script>"), 1)
        self.assertNotIn("__DATA__", page)

    def test_script_injection_is_escaped(self):
        d = make_data()
        d["observations"][0]["note"] = "</script><script>alert(1)</script>"
        page = m.render_html(d, m.build_view(d))
        self.assertEqual(page.count("<script>"), 1)
        self.assertNotIn("<script>alert(1)", page)

    def test_dry_run_writes_nothing(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            fixture(root)
            with contextlib.redirect_stdout(io.StringIO()):
                m.run(m.Config(root=root, dry_run=True))
            self.assertFalse((root / m.OUTPUT_FILE).exists())

    def test_render_writes_file(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            fixture(root)
            changed = m.run(m.Config(root=root))
            self.assertTrue(changed[str(m.OUTPUT_FILE)])
            self.assertTrue((root / m.OUTPUT_FILE).exists())
            # 二次渲染内容不变（可重复构建）
            self.assertFalse(m.run(m.Config(root=root))[str(m.OUTPUT_FILE)])

    def test_invalid_data_blocks_render(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            d = make_data()
            d["observations"].append(obs(model="M1", benchmark="B1", key="k1", value=99))
            fixture(root, d)
            with self.assertRaises(ValueError):
                m.run(m.Config(root=root))

    def test_cli_validate_exit_codes(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            fixture(root)
            self.assertEqual(m.main(["--root", str(root), "--validate"]), 0)
            d = make_data()
            d["observations"][0]["value"] = 150
            fixture(root, d)
            self.assertEqual(m.main(["--root", str(root), "--validate"]), 1)


class TestJavascript(unittest.TestCase):
    """可选：Node 可用时执行内联 JS，验证渲染逻辑不抛异常且结果正确。"""

    NODE = shutil.which("node")

    def setUp(self):
        if not self.NODE:
            self.skipTest("node 不可用，跳过 JS 集成检查")
        root = Path(__file__).resolve().parent.parent
        if not (root / "benchmarks.html").exists():
            self.skipTest("benchmarks.html 尚未生成")
        page = (root / "benchmarks.html").read_text(encoding="utf-8")
        s = page.index("<script>") + len("<script>")
        e = page.index("</script>")
        self.js = page[s:e]

    def _run(self, probe: str) -> str:
        stub = (
            "const store={};const mk=id=>({_id:id,innerHTML:'',textContent:'',checked:false,"
            "value:'',classList:{toggle(){},add(){},remove(){}},addEventListener(){}});"
            "global.document={getElementById(id){return store[id]||(store[id]=mk(id));}};"
            "global.window={addEventListener(){},scrollY:0};"
        )
        script = stub + self.js + "\n" + probe
        r = subprocess.run([self.NODE, "-e", script], capture_output=True,
                           text=True, timeout=30)
        if r.returncode != 0:
            self.fail(f"JS 执行失败: {r.stderr[:600]}")
        return r.stdout.strip()

    def test_initial_render_produces_all_widgets(self):
        out = self._run(
            "const need=['stats','principle','filtersBox','obsHead','obsBody','covTable',"
            "'covBars','cmpChips','caveatsBox','filterTip'];"
            "console.log(need.filter(k=>!store[k]||((store[k].innerHTML||'')===''"
            "&&(store[k].textContent||'')==='')).join(',')||'OK');"
            "console.log('rows='+(store.obsBody.innerHTML.match(/<tr>/g)||[]).length);"
        )
        self.assertIn("OK", out)
        # 真实仓库数据会随榜单扩充而增长，这里断言下限而非固定值
        rows = int(out.split("rows=")[1].split()[0])
        self.assertGreater(rows, 40)

    def test_cross_group_value_sort_blocked(self):
        out = self._run(
            "st.sort='value';refresh();"
            "console.log(store.sortWarn.innerHTML.includes('已禁用')?'BLOCKED':'NOT_BLOCKED');"
            "st.group='healthbench';refresh();"
            "console.log(store.sortWarn.innerHTML.length===0?'GROUP_OK':'GROUP_BAD');"
            "console.log('first='+filtered()[0].value);"
        )
        self.assertIn("BLOCKED", out)
        self.assertIn("GROUP_OK", out)
        self.assertIn("first=44.4", out)

    def test_lower_is_better_sorts_ascending(self):
        out = self._run(
            "st.group='hallucination';st.sort='value';st.dir=1;refresh();"
            "console.log('first='+filtered()[0].value);"
        )
        self.assertIn("first=3.3", out)

    def test_compare_marks_missing_and_cross_scope(self):
        out = self._run(
            "st.compare=['Baichuan-M4','Baichuan-M3-235B'];renderCompare();"
            "console.log('shared='+(store.cmpTable.innerHTML.match(/共同可比/g)||[]).length);"
            "st.compare=['Qwen3.7-Max','Muse Spark'];renderCompare();"
            "console.log('cross='+store.cmpWarn.innerHTML.includes('同名跨口径'));"
        )
        self.assertIn("shared=3", out)
        self.assertIn("cross=true", out)


if __name__ == "__main__":
    unittest.main(verbosity=2)
