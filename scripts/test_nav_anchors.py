#!/usr/bin/env python3
"""站点导航锚点回归自测。

背景：gen_html.py 的 HEADER 里硬编码了导航 / 侧栏链接，而标题 id 由
生成器按「小写 + 去标点 + 保留 emoji / 全角括号」规则算出。历史上导航写的是
简写（如 #快速索引），与实际 id（1-快速索引）不匹配，导致站点侧栏大面积失效。
本测试把「所有硬编码锚点必须命中 index.html 的真实 id」固化为回归防护。

运行：python3 -m unittest scripts.test_nav_anchors.py -v
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import unicodedata
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def header_text() -> str:
    g = (ROOT / "gen_html.py").read_text(encoding="utf-8")
    s = g.index("HEADER = r")
    e = g.index("'''", s + 20)
    return g[s:e]


def html_ids() -> set[str]:
    h = (ROOT / "index.html").read_text(encoding="utf-8")
    return set(re.findall(r'id="([^"]+)"', h))


def gen_anchor(line: str) -> str:
    """复现 gen_html.py 的标题锚点算法。"""
    raw = line.lstrip("#").strip().rstrip("* ")
    clean = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", raw)
    return (
        clean.lower()[:80]
        .replace(" ", "-").replace("/", "-")
        .replace("?", "").replace(":", "")
        .replace("(", "").replace(")", "")
        .replace(",", "").replace(".", "")
        .replace("[", "").replace("]", "")
    )


class TestNavAnchors(unittest.TestCase):
    def test_every_hardcoded_anchor_hits_a_real_id(self):
        ids = html_ids()
        links = [x for x in re.findall(r'href="#([^"]+)"', header_text())
                 if not x.startswith("${")]
        self.assertGreaterEqual(len(links), 25)
        missing = [x for x in links if x not in ids]
        self.assertEqual(missing, [], f"站点导航存在失效锚点: {missing}")

    def test_no_legacy_sota_anchor(self):
        hdr = header_text()
        self.assertNotIn("110-sota-", hdr)
        self.assertIn('href="#110-🏆-官方榜单口径"', hdr)

    def test_page_links_exist(self):
        hdr = header_text()
        self.assertIn('href="benchmarks.html"', hdr)
        self.assertTrue((ROOT / "benchmarks.html").exists())
        board = (ROOT / "benchmarks.html").read_text(encoding="utf-8")
        self.assertIn('href="index.html"', board)

    def test_readme_toc_uses_github_style_for_110(self):
        # README 目录面向 GitHub Markdown 渲染，规则与站点不同：emoji 会被移除。
        md = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("](#110-官方榜单口径)", md)
        self.assertNotIn("](#110-🏆-官方榜单口径)", md)

    def test_anchor_algorithm_matches_generated_ids(self):
        md = (ROOT / "README.md").read_text(encoding="utf-8")
        heads = [l for l in md.split("\n") if re.match(r"^#{1,4}\s+", l)]
        expected = {gen_anchor(l) for l in heads}
        ids = html_ids()
        # 抽查若干代表性标题，确认测试里复现的算法与生成器一致
        for sample in ("2-通用基础模型", "4-技术对比", "110-🏆-官方榜单口径",
                       "20-模型汇总核实总表-截至-2026-11-05"):
            self.assertIn(sample, expected, f"算法未产出 {sample}")
            self.assertIn(sample, ids, f"index.html 缺少 {sample}")

    def test_footer_js_template_is_not_counted_as_static_link(self):
        g = (ROOT / "gen_html.py").read_text(encoding="utf-8")
        # 动态模板 `.tol a[href="#${id}"]` 属于运行时代码，不应被静态校验误报
        self.assertIn('href="#${id}"', g)

    def test_runtime_remap_and_safe_click_handler_present(self):
        g = (ROOT / "gen_html.py").read_text(encoding="utf-8")
        self.assertIn("唯一映射到真实 id", g)
        # 侧栏点击改用 getElementById，避免含 emoji / 全角括号的 id 触发 CSS 选择器解析异常
        self.assertIn("document.getElementById(a.getAttribute('href').slice(1))", g)
        self.assertNotIn("document.querySelector(a.getAttribute('href'))", g)

    def test_readme_toc_links_all_resolvable_after_remap(self):
        """34 个目录链接：已命中或可唯一映射，不允许歧义 / 无匹配。"""
        md = (ROOT / "README.md").read_text(encoding="utf-8")
        toc = md[md.index("## 📑 目录"):md.index("## 1. 快速索引")]
        links = list(dict.fromkeys(re.findall(r"\]\(#([^)]+)\)", toc)))
        ids = html_ids()

        def norm(x):
            x = re.sub(r"^[0-9]+[-.]+", "", x)
            x = "".join(c for c in x if not unicodedata.category(c).startswith("So"))
            return re.sub(r"[^0-9a-z\u4e00-\u9fff]+", "", x.lower())

        self.assertGreaterEqual(len(links), 30)
        for link in links:
            if link in ids:
                continue
            n = norm(link)
            cand = [i for i in ids if norm(i) == n]
            if len(cand) != 1:
                cand = [i for i in ids if n and n in norm(i)]
            self.assertEqual(len(cand), 1, f"目录链接 {link} 无法唯一映射到站点 id")

    def test_runtime_remap_actually_rewrites_hrefs(self):
        """可选：用 Node 执行生成器里的兼容层，验证 href 真的被改写。"""
        node = shutil.which("node")
        if not node:
            self.skipTest("node 不可用")
        g = (ROOT / "gen_html.py").read_text(encoding="utf-8")
        mm = re.search(r"\(function\(\)\{\n  const ids=.*?\n\}\)\(\);", g, re.S)
        self.assertIsNotNone(mm, "未找到运行时兼容层代码")
        stub = (
            "const headings=['1-快速索引','2-通用基础模型',"
            "'16-🃏-按扑克牌花色分类','110-🏆-官方榜单口径'];"
            "const links=['#16-按扑克牌花色分类','#2-通用基础模型','#110-官方榜单口径']"
            ".map(h=>({_h:h,getAttribute(){return this._h},setAttribute(k,v){this._h=v}}));"
            "global.document={querySelectorAll(sel){"
            "if(sel.startsWith('h'))return headings.map(id=>({id}));"
            "if(sel.startsWith('a'))return links;return [];}};"
        )
        probe = "console.log(links.map(a=>a._h).join('|'));"
        r = subprocess.run([node, "-e", stub + mm.group(0) + probe],
                           capture_output=True, text=True, timeout=20)
        self.assertEqual(r.returncode, 0, r.stderr[:400])
        out = r.stdout.strip()
        self.assertIn("#16-🃏-按扑克牌花色分类", out)
        self.assertIn("#110-🏆-官方榜单口径", out)
        self.assertIn("#2-通用基础模型", out)


if __name__ == "__main__":
    unittest.main(verbosity=2)
