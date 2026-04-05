#!/usr/bin/env python3
"""Generate beautiful preview.html from README.md — v2 (fixed tables, badges, images)"""

import re, html as html_mod

with open('README.md', 'r', encoding='utf-8') as f:
    md = f.read()

# ========== HTML HEADER ==========
HEADER = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🃏 House of Model Cards (HOMC) — AI模型扑克牌分类体系</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🃏</text></svg>">
<script>
window.MathJax={tex:{inlineMath:[['$','$'],['\\(','\\)']],displayMath:[]},svg:{fontCache:'global'}};
</script>
<script id="MJS" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
<style>
:root{--bg:#0d1117;--bg2:#161b22;--bg3:#1c2333;--bgc:#1c2333;--tx:#e6edf3;--tx2:#8b949e;--tx3:#6e7681;--bd:#30363d;
--bl:#58a6ff;--pr:#bc8cff;--gr:#3fb950;--rd:#f85149;--or:#d29922;--cy:#39c5cf;--pk:#db61a2;
--sp:#79c0ff;--ht:#ff7b72;--dm:#d2a8ff;--cl:#7ee787}
*{margin:0;padding:0;box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:64px}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans SC',Helvetica,Arial,sans-serif;background:var(--bg);color:var(--tx);line-height:1.7;font-size:15.5px}
::-webkit-scrollbar{width:8px}::-webkit-scrollbar-thumb{background:var(--bd);border-radius:4px}

/* Navbar */
.nav{position:fixed;top:0;left:0;right:0;z-index:1000;background:rgba(13,17,23,.92);backdrop-filter:blur(16px);border-bottom:1px solid var(--bd);height:64px;display:flex;align-items:center;justify-content:space-between;padding:0 24px}
.nb a{display:flex;align-items:center;gap:10px;font-size:18px;font-weight:700;color:var(--tx);text-decoration:none}
.nb a span{background:linear-gradient(135deg,var(--bl),var(--pr),var(--pk));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.nl{display:flex;gap:4px}.nl a{color:var(--tx2);padding:6px 14px;border-radius:6px;font-size:13.5px;text-decoration:none;transition:.25s}
.nl a:hover{color:var(--tx);background:#252d40}

/* Layout */
.ly{display:flex;max-width:1440px;margin:0 auto;padding-top:64px}
.sd{width:260px;flex-shrink:0;position:sticky;top:64px;height:calc(100vh-64px);overflow-y:auto;padding:20px 0 20px 16px;border-right:1px solid var(--bd)}
.tot{font-size:12px;text-transform:uppercase;letter-spacing:1.5px;color:var(--tx3);padding:0 12px 12px;font-weight:600}
.tol{list-style:none}.tol a{display:block;color:var(--tx2);text-decoration:none;padding:4px 12px 4px 18px;font-size:13px;border-left:2px solid transparent;transition:.25s;line-height:1.5}
.tol a:hover,.tol a.on{color:var(--bl);border-left-color:var(--bl);font-weight:600}
.mc{flex:1;min-width:0;padding:24px 32px 60px;max-width:920px}

/* Hero */
.hero{text-align:center;padding:36px 0 28px}
.hero h1{font-size:clamp(26px,4vw,38px);font-weight:800;line-height:1.25;margin-bottom:14px;
  background:linear-gradient(135deg,var(--bl),var(--pr),var(--pk),var(--or));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.hero p{font-size:16px;color:var(--tx2);max-width:680px;margin:0 auto 20px;line-height:1.65}
.bdg{display:flex;flex-wrap:wrap;gap:7px;justify-content:center}.bdg img{height:21px;border-radius:4px}

/* Stats */
.sts{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin:28px 0}
.st{background:var(--bgc);border:1px solid var(--bd);border-radius:10px;padding:16px 12px;text-align:center;transition:.25s}
.st:hover{border-color:var(--bl);transform:translateY(-2px)}
.si{font-size:24px}.sn{font-size:24px;font-weight:800;color:var(--bl)}.sl{font-size:12px;color:var(--tx3)}

/* Features */
.fea{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:8px;margin:20px 0 28px}
.fe{background:var(--bg2);border:1px solid var(--bd);border-radius:6px;padding:11px 14px;display:flex;align-items:center;gap:9px;font-size:14px;transition:.25s}
.fe:hover{border-color:var(--bl)}
.fe .ck{color:var(--gr);font-weight:700}

/* Headings */
h2{font-size:24px;font-weight:800;margin:48px 0 16px;padding-bottom:10px;border-bottom:1px solid var(--bd);scroll-margin-top:72px;line-height:1.3}
h3{font-size:18px;font-weight:700;margin:28px 0 12px;color:var(--cy);scroll-margin-top:72px}
h4{font-size:15.5px;font-weight:600;margin:18px 0 8px;scroll-margin-top:72px}

/* Tables */
.tw{overflow-x:auto;margin:16px 0;border-radius:10px;border:1px solid var(--bd)}
table{width:100%;border-collapse:collapse;font-size:14px}
thead{background:var(--bg3)}th{padding:9px 12px;text-align:left;font-weight:600;font-size:12.5px;text-transform:uppercase;letter-spacing:.5px;color:var(--tx);border-bottom:1px solid var(--bd)}
td{padding:9px 12px;border-bottom:1px solid var(--bd);color:var(--tx2);vertical-align:middle}
tbody tr:hover{background:#252d40}

/* Code */
code{background:var(--bg3);color:var(--cy);padding:2px 6px;border-radius:4px;font-size:88%;font-family:'SF Mono','Fira Code',Consolas,monospace;border:1px solid rgba(88,166,255,.15)}
pre{background:var(--bg2);border:1px solid var(--bd);border-radius:10px;padding:16px 18px;overflow-x:auto;margin:16px 0;font-size:13px;line-height:1.55}
pre code{background:none;border:none;padding:0;color:var(--tx2)}

/* Misc */
a{color:var(--bl);text-decoration:none}a:hover{color:var(--cy);text-decoration:underline}
ul,ol{padding-left:20px;margin:10px 0}li{margin:5px 0;color:var(--tx2)}
blockquote{border-left:4px solid var(--bl);margin:16px 0;padding:14px 18px;background:linear-gradient(90deg,rgba(88,166,255,.05),transparent);border-radius:0 6px 6px 0;color:var(--tx2)}
hr{border:none;height:1px;background:var(--bd);margin:32px 0;opacity:.5}
img{max-width:100%;border-radius:6px}

/* Suit badges */
.sb{display:inline-flex;align-items:center;gap:3px;padding:2px 9px;border-radius:20px;font-size:12px;font-weight:700}
.s-s{background:rgba(121,192,255,.12);color:var(--sp);border:1px solid rgba(121,192,255,.25)}.s-h{background:rgba(255,123,114,.12);color:var(--ht);border:1px solid rgba(255,123,114,.25)}
.s-d{background:rgba(210,168,255,.12);color:var(--dm);border:1px solid rgba(210,168,255,.25)}.s-c{background:rgba(126,231,135,.12);color:var(--cl);border:1px solid rgba(126,231,135,.25)}
.s-j{background:linear-gradient(135deg,rgba(255,215,0,.15),rgba(255,107,53,.1));border:1px solid rgba(255,215,0,.3);color:#ffd700}

/* Cards */
.cd{background:var(--bgc);border:1px solid var(--bd);border-radius:12px;margin:18px 0;overflow:hidden;transition:.25s}
.cd:hover{border-color:rgba(88,166,255,.3);box-shadow:0 4px 16px rgba(0,0,0,.35)}
.ch{padding:14px 18px;border-bottom:1px solid var(--bd);background:var(--bg3);font-weight:700;font-size:16px}
.cb{padding:14px 18px}

/* BTT & Progress */
.btt{position:fixed;bottom:28px;right:28px;z-index:999;width:42px;height:42px;border-radius:50%;background:var(--bg3);border:1px solid var(--bd);color:var(--tx2);cursor:pointer;opacity:0;visibility:hidden;transition:.25s;font-size:20px;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 14px rgba(0,0,0,.4)}
.btt.vis{opacity:1;visibility:visible}.btt:hover{background:var(--bl);color:#fff}
.prog{position:fixed;top:64px;left:0;width:0;height:2px;background:linear-gradient(90deg,var(--bl),var(--pr));z-index:1001}

/* Footer */
.ft{text-align:center;padding:30px 0 24px;border-top:1px solid var(--bd);color:var(--tx3);font-size:13px;margin-top:50px}

@media(max-width:1024px){.sd{display:none}.mc{padding:20px 18px 50px;max-width:100%}}
@media(max-width:640px){body{font-size:14px}h2{font-size:20px}.sts{grid-template-columns:repeat(2,1fr)}.fea{grid-template-columns:1fr}}
</style>
</head>
<body><div class="prog"id="pg"></div>

<nav class="nav"><div class="nb"><a href="#">🃏 <span>HOMC Model List</span></a></div>
<div class="nl">
<a href="#快速索引">📑 索引</a><a href="#通用基础模型">🤖 模型</a><a href="#评测基准详解">📏 评测</a>
<a href="#微调工具链与实战">🔧 微调</a><a href="#安全与对齐">🛡️ 安全</a>
</div></nav>

<div class="ly">
<aside class="sd" id="sd">
<div class="tot">📑 目录导航</div>
<ul class="tol">
<li><a href="#核心统计">📊 核心统计</a></li>
<li><a href="#项目特色">🌟 项目特色</a></li>
<li><a href="#house-of-model-cards">🎴 扑克牌分类体系</a></li>
<li><a href="#快速索引">1️⃣ 快速索引</a></li>
<li><a href="#通用基础模型">2️⃣ 通用基础模型</a></li>
<li><a href="#专项领域模型">3️⃣ 专项领域模型</a></li>
<li><a href="#技术对比">4️⃣ 技术对比</a></li>
<li><a href="#部署指南">5️⃣ 部署指南</a></li>
<li><a href="#llm-发展时间线">6️⃣ 发展时间线</a></li>
<li><a href="#训练方法与对齐技术">7️⃣ 训练与对齐</a></li>
<li><a href="#场景化模型选择指南">8️⃣ 选型指南</a></li>
<li><a href="#开源生态地图">9️⃣ 开源生态</a></li>
<li><a href="#2026-技术趋势展望">🔮 趋势展望</a></li>
<li><a href="#faq-常见问题">❓ FAQ</a></li>
<li><a href="#安全与对齐">🛡️ 安全与对齐</a></li>
<li><a href="#评测基准详解">📏 评测基准</a></li>
<li><a href="#微调工具链与实战">🔧 微调工具链</a></li>
<li><a href="#行业应用案例">🏭 行业案例</a></li>
<li><a href="#prompt-engineering-指南">💡 Prompt工程</a></li>
<li><a href="#视频生成与世界模型">🎬 视频与世界模型</a></li>
<li><a href="#参考文献">📚 参考文献</a></li>
</ul></aside>

<main class="mc"
'''

FOOTER = r'''
<div class="btt"id="bt" onclick="window.scrollTo({top:0,behavior:'smooth'})">↑</div>
<footer class="ft">
<p>🃏 <strong>House of Model Cards (HOMC)</strong> — AI模型扑克牌分类体系 |
<a href="https://github.com/gatilin/model-list" target="_blank">GitHub ⭐</a> | MIT License | Last Updated: 2026-04-05<br/>
<span style="opacity:.6">Made with ❤️ by gatilin · GitHub Pages + Jekyll Primer Theme</span></p></footer>
<script>
window.addEventListener('scroll',()=>{
  const h=document.documentElement.scrollHeight-window.innerHeight;
  const y=window.scrollY;
  document.getElementById('pg').style.width=(y/h*100)+'%';
  document.getElementById('bt').classList.toggle('vis',y>400);
});
const hs=document.querySelectorAll('h2[id],h3[id]');
const tls=document.querySelectorAll('.tol a');
const ob=new IntersectionObserver(es=>{es.forEach(e=>{
  if(e.isIntersecting){
    const id=e.target.getAttribute('id');tls.forEach(l=>l.classList.remove('on'));
    const ac=document.querySelector(`.tol a[href="#${id}"]`);if(ac)ac.classList.add('on');
  }});},{threshold:.15,rootMargin:"-80px 0 -70% 0"});
hs.forEach(h=>ob.observe(h));
document.querySelectorAll('.tol a').forEach(a=>{a.addEventListener('click',e=>{e.preventDefault();
  const t=document.querySelector(a.getAttribute('href'));if(t)t.scrollIntoView({behavior:'smooth'});});
});
</script></body></html>'''


def process_inline(text):
    """Process inline markdown elements: images, bold, italic, code, links, suit badges."""
    # 1. Images / badges: ![alt](url)
    def replace_img(m):
        alt = m.group(1).strip()
        url = m.group(2)
        if not url:
            return ''
        # Badge-style images (shields.io etc.) get smaller sizing
        is_badge = 'shields.io' in url or 'badge' in url.lower()
        cls = 'class="bdg-img"' if is_badge else ''
        return f'<img src="{html_mod.escape(url)}" alt="{html_mod.escape(alt)}" {cls}/>'
    
    text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', replace_img, text)

    # 2. Bold + Italic: ***text*** or **_text_**
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    
    # 3. Bold: **text**
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    
    # 4. Italic: *text*
    text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', text)
    
    # 5. Inline code: `code`
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    
    # 6. Links: [text](url)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank">\1</a>', text)
    
    # 7. Suit badges
    text = re.sub(r'(♥[AQJK0-9]+)', r'<span class="sb s-h">\1</span>', text)
    text = re.sub(r'(♠[AQJK0-9]+)', r'<span class="sb s-s">\1</span>', text)
    text = re.sub(r'(♦[AQJK0-9]+)', r'<span class="sb s-d">\1</span>', text)
    text = re.sub(r'(♣[AQJK0-9]+)', r'<span class="sb s-c">\1</span>', text)
    text = re.sub(r'(🃏\s*Joker|🃏)', r'<span class="sb s-j">\1</span>', text)
    
    return text


def is_table_separator(cells):
    """Check if all cells look like a table separator line (e.g., :---:, ---, :--)"""
    for c in cells:
        stripped = c.strip()
        if stripped and not re.match(r'^[\s\-:]+$', stripped):
            return False
    return True


def md2html(md_text):
    lines = md_text.split('\n')
    out = []
    in_tbl = in_pre = in_bq = False
    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Skip the first few lines that we render manually in HEADER
        if i < 5:
            i += 1
            continue

        # ===== Code blocks =====
        if stripped.startswith('```'):
            if not in_pre:
                in_pre = True
                lang = stripped[3:] or ''
                out.append(f'<pre><code class="lang-{lang}">')
            else:
                in_pre = False
                out.append('</code></pre>')
            i += 1
            continue

        if in_pre:
            out.append(html_mod.escape(line))
            i += 1
            continue

        # ===== Tables =====
        # A table row starts with | and has at least 2 columns
        if stripped.startswith('|') and len(stripped.split('|')) > 2:
            cells_raw = [c for c in line.split('|')[1:-1]]
            
            if is_table_separator(cells_raw):
                # This is a header separator row - skip it but close thead & open tbody
                if in_tbl:
                    out.append('</thead><tbody>')
                else:
                    # Edge case: separator before any data row (shouldn't happen in valid MD)
                    pass
                i += 1
                continue
            
            # Data/header row
            if not in_tbl:
                in_tbl = True
                out.append('<div class="tw"><table><thead>')
                
            cells_html = []
            for c in cells_raw:
                cell_content = process_inline(c.strip())
                cells_html.append(cell_content)
            
            out.append('<tr>' + ''.join('<td>' + c + '</td>' for c in cells_html) + '</tr>')
            i += 1
            continue
        
        # End of table (current line doesn't start with |)
        elif in_tbl:
            in_tbl = False
            out.append('</tbody></table></div>')

        # ===== Headers =====
        m = re.match(r'^(#{1,4})\s+(.+)', line)
        if m:
            lvl = len(m.group(1))
            text_raw = m.group(2).strip().rstrip('* ')
            text_clean = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', text_raw)
            anchor = text_clean.lower()[:80].replace(' ','-').replace('/','-').replace('?','').replace(':','').replace('(','').replace(')','').replace(',','').replace('.','').replace('[','').replace(']','')
            tag = ['h2','h3','h4','h4'][lvl-1]
            out.append(f'<{tag} id="{anchor}">{process_inline(text_raw)}</{tag}>')
            i += 1
            continue

        # ===== HR =====
        if stripped == '---':
            out.append('<hr/>')
            i += 1
            continue

        # ===== Blockquote =====
        if stripped.startswith('> '):
            if not in_bq:
                in_bq = True
                out.append('<blockquote>\n<p>')
            else:
                out.append('<br/>\n')
            out.append(process_inline(stripped[2:]))
            i += 1
            continue
        elif in_bq and stripped:
            out.append(process_inline(stripped))
            i += 1
            continue
        elif in_bq:
            in_bq = False
            out.append('\n</p></blockquote>')

        # ===== Empty line =====
        if stripped == '':
            out.append('')
            i += 1
            continue

        # ===== List items =====
        if stripped.startswith('- ') or stripped.startswith('* '):
            text = process_inline(stripped[2:])
            out.append(f'<li>{text}</li>')
            i += 1
            continue
        if re.match(r'^\d+\.\s', stripped):
            text = process_inline(re.sub(r'^\d+\.\s+', '', stripped))
            out.append(f'<li>{text}</li>')
            i += 1
            continue

        # ===== Regular paragraph =====
        out.append(process_inline(stripped))
        i += 1

    # Close any remaining table
    if in_tbl:
        out.append('</tbody></table></div>')
    if in_bq:
        out.append('\n</p></blockquote>')

    return '\n'.join(out)


# ========== Generate ==========
with open('preview.html', 'w', encoding='utf-8') as f:
    f.write(HEADER)
    body = md2html(md)
    f.write(body + '\n')
    f.write(FOOTER)

print(f'Done! preview.html created ({len(HEADER)+len(body)+len(FOOTER)} bytes)')
