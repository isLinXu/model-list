#!/usr/bin/env python3
"""render_source_tables.py 的离线自测（不访问网络）。

运行：python3 -m unittest scripts/test_render_source_tables.py -v
"""

from __future__ import annotations

import contextlib
import copy
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import render_source_tables as m  # noqa: E402

COLUMNS = ["模型", "提供方", "官方评测来源", "指标", "日期", "范围", "核实状态", "备注"]


def row(name: str, **kw) -> list[str]:
    base = [
        name, "测试厂商", "[官方页](https://example.com/doc)",
        "指标 1.0", "2026-11-06", "仅该口径", "✅ `[A]`", "备注",
    ]
    for k, v in kw.items():
        base[int(k)] = v
    return base


def make_data() -> dict:
    return {
        "meta": {"version": "1.0", "updated": "2026-11-06", "source_count": 3},
        "tables": {
            key: {"section": sec, "title": title, "columns": COLUMNS,
                  "rows": [row(f"{key}-模型-A"), row(f"{key}-模型-B")]}
            for key, sec, title in (
                ("benchmarks", "4.1", "官方评测来源索引"),
                ("pricing", "4.2", "官方价目页索引"),
                ("leaderboards", "1.10", "可核实的官方榜单口径"),
            )
        },
    }


def fixture(root: Path, data: dict | None = None, render: bool = True) -> dict:
    (root / "data").mkdir(parents=True, exist_ok=True)
    payload = data if data is not None else make_data()
    (root / m.DATA_FILE).write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    blocks = []
    for key in m.TABLE_KEYS:
        start, end = m.MARKERS[key]
        blocks.append(f"{start}\nPLACEHOLDER_{key}\n{end}")
    (root / "README.md").write_text("\n\n".join(blocks) + "\n", encoding="utf-8")
    if render:
        m.run(m.Config(root=root))
    return payload


class TestRendering(unittest.TestCase):
    def test_block_has_markers_and_eight_columns(self):
        with tempfile.TemporaryDirectory() as td:
            data = fixture(Path(td))
            block = m.render_block("benchmarks", data["tables"]["benchmarks"])
            self.assertTrue(block.startswith(m.MARKERS["benchmarks"][0]))
            self.assertTrue(block.rstrip().endswith(m.MARKERS["benchmarks"][1]))
            self.assertNotIn("PLACEHOLDER", block)
            self.assertIn("| 模型 | 提供方 |", block)
            self.assertEqual(m.table_column_counts(block), [])

    def test_render_replaces_all_three_markers(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            fixture(root)
            text = (root / "README.md").read_text(encoding="utf-8")
            self.assertNotIn("PLACEHOLDER", text)
            for key in m.TABLE_KEYS:
                self.assertIn(f"动态表 · 由 `data/official_sources.json` 生成", text)
                self.assertIn(f"{key}-模型-A", text)

    def test_dry_run_writes_nothing(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            fixture(root, render=False)
            before = (root / "README.md").read_text(encoding="utf-8")
            with contextlib.redirect_stdout(io.StringIO()):
                m.run(m.Config(root=root, dry_run=True))
            self.assertEqual(before, (root / "README.md").read_text(encoding="utf-8"))

    def test_missing_marker_raises(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            fixture(root, render=False)
            p = root / "README.md"
            p.write_text(p.read_text(encoding="utf-8").replace(
                m.MARKERS["pricing"][1], ""), encoding="utf-8")
            with self.assertRaises(ValueError):
                m.run(m.Config(root=root))


class TestValidation(unittest.TestCase):
    def test_valid_fixture_passes(self):
        with tempfile.TemporaryDirectory() as td:
            fixture(Path(td))
            self.assertEqual(m.validate(Path(td)), [])

    def test_column_mismatch_detected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            data = make_data()
            data["tables"]["pricing"]["rows"][0] = data["tables"]["pricing"]["rows"][0][:6]
            fixture(root, data, render=False)
            self.assertTrue(any("列数" in e for e in m.validate(root)))

    def test_duplicate_first_cell_detected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            data = make_data()
            data["tables"]["benchmarks"]["rows"][1][0] = "benchmarks-模型-A"
            fixture(root, data, render=False)
            self.assertTrue(any("首列重复" in e for e in m.validate(root)))

    def test_non_https_link_detected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            data = make_data()
            data["tables"]["leaderboards"]["rows"][0][2] = "[页](http://example.com)"
            fixture(root, data, render=False)
            self.assertTrue(any("非 HTTPS" in e for e in m.validate(root)))

    def test_missing_table_detected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            data = make_data()
            del data["tables"]["pricing"]
            fixture(root, data, render=False)
            self.assertTrue(any("缺少表 pricing" in e for e in m.validate(root)))

    def test_readme_out_of_sync_detected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            fixture(root)
            p = root / "README.md"
            p.write_text(p.read_text(encoding="utf-8").replace(
                "benchmarks-模型-A", "手工改坏了"), encoding="utf-8")
            self.assertTrue(any("不一致" in e for e in m.validate(root)))

    def test_legacy_value_table_detected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            fixture(root)
            p = root / "README.md"
            p.write_text(
                p.read_text(encoding="utf-8") + "\n| GPT-5.4 | 93.5% | 97.5% | 98.8% | 82.7% | 23.5% | ♥A |\n",
                encoding="utf-8",
            )
            self.assertTrue(any("已废弃" in e for e in m.validate(root)))

    def test_real_repository_passes(self):
        root = Path(__file__).resolve().parent.parent
        readme = root / "README.md"
        if (root / m.DATA_FILE).exists() and readme.exists() and all(
            m.MARKERS[k][0] in readme.read_text(encoding="utf-8") for k in m.TABLE_KEYS
        ):
            self.assertEqual(m.validate(root), [])
        else:
            self.skipTest("真实仓库尚未接入 marker，跳过")


class TestUrlCollection(unittest.TestCase):
    def test_urls_are_unique_and_sorted(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            fixture(root)
            urls = m.collect_urls(root)
            self.assertEqual(urls, sorted(set(urls)))
            self.assertIn("https://example.com/doc", urls)

    def test_cli_validate_exit_code(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            fixture(root)
            self.assertEqual(m.main(["--root", str(root), "--validate"]), 0)
            data = make_data()
            data["tables"]["pricing"]["rows"][0][2] = "[页](http://example.com)"
            fixture(root, data, render=False)
            self.assertEqual(m.main(["--root", str(root), "--validate"]), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
