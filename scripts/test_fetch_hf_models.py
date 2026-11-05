#!/usr/bin/env python3
"""fetch_hf_models.py 的离线自测（不访问网络）。

运行：python3 -m unittest scripts/test_fetch_hf_models.py -v
"""

from __future__ import annotations

import datetime as dt
import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fetch_hf_models as m  # noqa: E402

NOW = dt.datetime(2026, 11, 5, 9, 0, tzinfo=dt.timezone.utc)
TODAY = NOW.date()


def cfg(**kw) -> m.Config:
    base = dict(date="2026-11-05", root=Path(tempfile.gettempdir()))
    base.update(kw)
    return m.Config(**base)


def model(mid: str, **kw) -> dict:
    base = {
        "id": mid,
        "author": mid.split("/")[0],
        "createdAt": "2026-11-05T06:00:00.000Z",
        "lastModified": "2026-11-05T06:00:00.000Z",
        "downloads": 0,
        "likes": 0,
        "private": False,
        "gated": False,
        "sha": "sha-new",
        "pipeline_tag": "text-generation",
        "tags": ["transformers", "safetensors", "text-generation", "license:apache-2.0", "en"],
        "_feeds": ["created"],
    }
    base.update(kw)
    return base


class TestParsing(unittest.TestCase):
    def test_parse_ts(self):
        self.assertEqual(m.parse_ts("2026-11-05T08:07:16.000Z").year, 2026)
        self.assertIsNone(m.parse_ts(None))
        self.assertIsNone(m.parse_ts("not-a-date"))

    def test_official_and_noise(self):
        self.assertTrue(m.is_official(model("Qwen/Qwen3.8-27B")))
        self.assertTrue(m.is_official(model("baidu/ERNIE-5.5-Flash-Base")))
        self.assertFalse(m.is_official(model("someone/my-model")))
        self.assertTrue(m.noise_hit(model("someone/Qwen3.8-GGUF")))
        self.assertTrue(m.noise_hit(model("someone/x-abliterated")))
        self.assertFalse(m.noise_hit(model("nvidia/Nemotron-3.5")))

    def test_infer_pipeline(self):
        self.assertEqual(m.infer_pipeline(model("x/y"))[0], "通用 / 对话")
        self.assertEqual(
            m.infer_pipeline(model("x/y", pipeline_tag="image-text-to-text"))[0], "多模态 VLM"
        )
        self.assertEqual(m.infer_pipeline(model("x/y", pipeline_tag=None, tags=[]))[0], "其他 / 未标注")


class TestQualify(unittest.TestCase):
    def setUp(self):
        self.c = cfg()
        self.now = NOW

    def test_official_zero_heat_new_model_passes(self):
        ok, why = m.qualify(model("Qwen/Qwen3.9-Max"), self.now, self.c)
        self.assertTrue(ok, why)

    def test_private_rejected(self):
        ok, why = m.qualify(model("Qwen/x", private=True), self.now, self.c)
        self.assertFalse(ok)
        self.assertEqual(why, "private")

    def test_outside_window_rejected(self):
        old = "2026-10-01T00:00:00.000Z"
        ok, why = m.qualify(model("Qwen/x", createdAt=old, lastModified=old), self.now, self.c)
        self.assertFalse(ok)
        self.assertEqual(why, "outside-window")

    def test_unofficial_quantized_rejected(self):
        ok, why = m.qualify(
            model("someone/Qwen3.8-GGUF", likes=999, downloads=10 ** 6), self.now, self.c
        )
        self.assertFalse(ok)
        self.assertEqual(why, "quantized-or-derived")

    def test_unofficial_cold_rejected(self):
        ok, why = m.qualify(model("someone/tiny-ft", likes=1, downloads=10), self.now, self.c)
        self.assertFalse(ok)
        self.assertEqual(why, "below-heat-threshold")

    def test_hot_unofficial_passes(self):
        ok, why = m.qualify(
            model("someone/hot-model", likes=200, downloads=50000, trendingScore=120),
            self.now, self.c,
        )
        self.assertTrue(ok, why)

    def test_fallback_category_inference(self):
        self.assertEqual(
            m.infer_pipeline(model("Comfy-Org/MOSS-Image", pipeline_tag=None, tags=["comfyui"]))[0],
            "图像生成",
        )
        self.assertEqual(
            m.infer_pipeline(model("tencent/Hy-Nomas", pipeline_tag=None, tags=["world-model"]))[0],
            "世界模型",
        )

    def test_official_quantized_is_also_excluded(self):
        ok, why = m.qualify(model("nvidia/DeepSeek-V4.1-NVFP4"), self.now, self.c)
        self.assertFalse(ok)
        self.assertEqual(why, "quantized-or-derived")

    def test_official_non_quantized_still_passes(self):
        ok, why = m.qualify(model("nvidia/Nemotron-3.5-Transcribe"), self.now, self.c)
        self.assertTrue(ok, why)

    def test_official_scores_above_unofficial_at_equal_heat(self):
        off = model("Qwen/Q3", likes=100, downloads=5000)
        non = model("someone/Q3", likes=100, downloads=5000)
        self.assertGreater(m.score(off, self.now, self.c), m.score(non, self.now, self.c))


class TestClassify(unittest.TestCase):
    def setUp(self):
        self.c = cfg()
        self.mdl = model("Qwen/Q3")

    def test_new(self):
        self.assertEqual(m.classify(self.mdl, {}, TODAY, self.c, NOW), "new")

    def test_first_seen_but_old_repo_is_not_new(self):
        old = model("Qwen/Q3", createdAt="2026-10-01T00:00:00.000Z")
        self.assertEqual(m.classify(old, {}, TODAY, self.c, NOW), "update")

    def test_suppressed_within_cooldown(self):
        seen = {"Qwen/Q3": {"last": "2026-11-04", "sha": "sha-old", "lastModified": "old"}}
        self.assertIsNone(m.classify(self.mdl, seen, TODAY, self.c, NOW))

    def test_update_after_cooldown(self):
        seen = {"Qwen/Q3": {"last": "2026-10-20", "sha": "sha-old", "lastModified": "old"}}
        self.assertEqual(m.classify(self.mdl, seen, TODAY, self.c, NOW), "update")

    def test_no_change_never_reported(self):
        seen = {"Qwen/Q3": {"last": "2026-10-01", "sha": "sha-new",
                            "lastModified": "2026-11-05T06:00:00.000Z"}}
        self.assertIsNone(m.classify(self.mdl, seen, TODAY, self.c, NOW))

    def test_prune_seen(self):
        seen = {"old": {"last": "2020-01-01"}, "fresh": {"last": "2026-11-04"}}
        self.assertEqual(list(m.prune_seen(seen, TODAY)), ["fresh"])


class TestRendering(unittest.TestCase):
    def test_table_has_eight_columns_and_escapes_pipe(self):
        row = m.build_row(model("someone/a|b", likes=30, downloads=5000), "new", cfg())
        table = m.render_table([row])
        header = table.split("\n")[0]
        self.assertEqual(len(header.split("|")) - 2, 8)
        self.assertIn("a\\|b", table)
        self.assertEqual(len(m.TABLE_COLS), 8)

    def test_readme_block_contains_disclaimer_and_marker_safe(self):
        row = m.build_row(model("Qwen/Q3"), "new", cfg())
        meta = dict(generated_at="2026-11-05 09:00 UTC", window_hours=36, scanned=10,
                    qualified=5, new_count=1, update_count=0)
        block = m.render_readme_block([row], meta)
        self.assertIn("未经人工核实", block)
        self.assertIn("不得作为确定内容引用", block)
        self.assertIn("⚙️ 机器抓取 · 待人工核实", block)

    def test_empty_block(self):
        meta = dict(generated_at="2026-11-05 09:00 UTC", window_hours=36, scanned=10,
                    qualified=0, new_count=0, update_count=0)
        self.assertIn("无符合条件", m.render_readme_block([], meta))

    def test_readme_marker_replace_is_idempotent(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "README.md").write_text(
                "before\n" + m.MARKER_START + "\nOLD\n" + m.MARKER_END + "\nafter\n",
                encoding="utf-8",
            )
            self.assertTrue(m.update_readme(root, "NEW", dry_run=False))
            self.assertFalse(m.update_readme(root, "NEW", dry_run=False))
            text = (root / "README.md").read_text(encoding="utf-8")
            self.assertIn("NEW", text)
            self.assertNotIn("OLD", text)
            self.assertIn("before", text)
            self.assertIn("after", text)

    def test_missing_marker_raises(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "README.md").write_text("no markers", encoding="utf-8")
            with self.assertRaises(RuntimeError):
                m.update_readme(root, "NEW", dry_run=False)


class TestEndToEndOffline(unittest.TestCase):
    def test_dry_run_writes_nothing(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "README.md").write_text(
                m.MARKER_START + "\nOLD\n" + m.MARKER_END + "\n", encoding="utf-8"
            )
            fixture = root / "fixture.json"
            fixture.write_text(json.dumps({"models": [
                model("Qwen/Qwen3.9-Max"),
                model("someone/Qwen3.8-GGUF", likes=999, downloads=10 ** 6),
                model("someone/tiny-ft", likes=0, downloads=0),
                model("someone/hot-model", likes=200, downloads=50000, trendingScore=120),
            ]}), encoding="utf-8")
            c = cfg(root=root, offline_fixture=str(fixture), dry_run=True)
            with contextlib.redirect_stdout(io.StringIO()):
                changed = m.run(c)
            self.assertTrue(all(changed.values()))
            self.assertFalse((root / "HF_DAILY.md").exists())
            self.assertIn("OLD", (root / "README.md").read_text(encoding="utf-8"))

    def test_real_write_creates_outputs(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "README.md").write_text(
                m.MARKER_START + "\nOLD\n" + m.MARKER_END + "\n", encoding="utf-8"
            )
            fixture = root / "fixture.json"
            fixture.write_text(json.dumps({"models": [
                model("Qwen/Qwen3.9-Max"),
                model("someone/hot-model", likes=200, downloads=50000, trendingScore=120),
            ]}), encoding="utf-8")
            c = cfg(root=root, offline_fixture=str(fixture))
            m.run(c)
            self.assertTrue((root / "HF_DAILY.md").exists())
            self.assertTrue((root / "data/hf-daily/2026-11-05.md").exists())
            payload = json.loads((root / "data/hf-daily/latest.json").read_text(encoding="utf-8"))
            self.assertEqual(len(payload["models"]), 2)
            seen = json.loads((root / "data/hf-daily/seen.json").read_text(encoding="utf-8"))
            self.assertEqual(len(seen["models"]), 2)
            # 第二次运行：同一天、同 sha、无变化 → 不覆盖当天日报，保持上一期成果
            before = (root / "HF_DAILY.md").read_text(encoding="utf-8")
            c2 = cfg(root=root, offline_fixture=str(fixture))
            m.run(c2)
            after = (root / "HF_DAILY.md").read_text(encoding="utf-8")
            self.assertEqual(before, after)
            payload2 = json.loads((root / "data/hf-daily/latest.json").read_text(encoding="utf-8"))
            self.assertEqual(len(payload2["models"]), 2)
            self.assertIn("未经人工核实", (root / "README.md").read_text(encoding="utf-8"))

    def test_force_overwrites_today(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "README.md").write_text(
                m.MARKER_START + "\nOLD\n" + m.MARKER_END + "\n", encoding="utf-8"
            )
            fixture = root / "fixture.json"
            fixture.write_text(json.dumps({"models": [model("Qwen/Q3")]}), encoding="utf-8")
            m.run(cfg(root=root, offline_fixture=str(fixture)))
            first = (root / "README.md").read_text(encoding="utf-8")
            m.run(cfg(root=root, offline_fixture=str(fixture), force=True))
            second = (root / "README.md").read_text(encoding="utf-8")
            # --force 后 seen 已存在且无变化，本期为空；日报确实被重写
            self.assertNotEqual(first, second)
            self.assertIn("无符合条件", second)

    def test_first_run_with_zero_candidates_still_writes_empty_digest(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "README.md").write_text(
                m.MARKER_START + "\nOLD\n" + m.MARKER_END + "\n", encoding="utf-8"
            )
            fixture = root / "fixture.json"
            fixture.write_text(json.dumps({"models": [
                model("someone/tiny-ft", likes=0, downloads=0),
            ]}), encoding="utf-8")
            m.run(cfg(root=root, offline_fixture=str(fixture)))
            payload = json.loads((root / "data/hf-daily/latest.json").read_text(encoding="utf-8"))
            self.assertEqual(len(payload["models"]), 0)
            self.assertIn("无符合条件", (root / "README.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
