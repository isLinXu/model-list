#!/usr/bin/env python3
"""从 data/benchmark_observations.json 生成多榜单可视化看板 benchmarks.html。

设计要点（对应「避免重复或错误聚合」）：
  * 观测长表：一条 = 模型 × 榜单 × 指标 × 口径组，主键唯一。
  * 单位与方向由可比组统一定义，不同单位/方向不进入同一次排序或求和。
  * 排名只在组内有效；跨组数值排序在界面上被禁用并给出提示。
  * 同名指标出现在不同口径组时（如 HLE）分行展示并标注「不可直接比较」。
  * value=null 必须标记 not_disclosed；覆盖矩阵的空缺显示「未披露」而非 0。

零第三方依赖，产出为自包含 HTML（数据内联，可直接本地打开）。

用法：
    python3 scripts/render_benchmark_board.py                 # 生成 benchmarks.html
    python3 scripts/render_benchmark_board.py --dry-run       # 预览，不写文件
    python3 scripts/render_benchmark_board.py --validate      # 只校验数据，不写文件
    python3 -m unittest scripts.test_benchmark_board.py
"""

from __future__ import annotations

import argparse
import html
import json
import sys
from dataclasses import dataclass
from pathlib import Path

DATA_FILE = Path("data/benchmark_observations.json")
OUTPUT_FILE = Path("benchmarks.html")

VALID_UNITS = {"percent", "score", "elo", "tokens", "billion"}
VALID_DIRECTIONS = {"higher", "lower"}
VALID_STATUSES = {"verified", "not_disclosed"}
REQUIRED_OBS = ("model", "provider", "benchmark", "metric", "key", "group", "src")


@dataclass
class Config:
    root: Path
    dry_run: bool = False
    validate_only: bool = False


# ---------------------------------------------------------------------------
# 数据加载与校验
# ---------------------------------------------------------------------------

def load_data(root: Path) -> dict:
    path = root / DATA_FILE
    if not path.exists():
        raise FileNotFoundError(f"缺少数据文件: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def validate(data: dict) -> tuple[list[str], list[str]]:
    """返回 (errors, warnings)。warnings 是口径提示，不阻止渲染。"""
    errors: list[str] = []
    warnings: list[str] = []

    groups = {g.get("id"): g for g in data.get("groups", [])}
    sources = {s.get("id"): s for s in data.get("sources", [])}
    obs = data.get("observations", [])

    if not groups:
        errors.append("缺少 groups")
    if not sources:
        errors.append("缺少 sources")
    if not obs:
        errors.append("缺少 observations")
        return errors, warnings

    for gid, g in groups.items():
        if g.get("unit") not in VALID_UNITS:
            errors.append(f"组 {gid}: 非法 unit {g.get('unit')}")
        if g.get("direction") not in VALID_DIRECTIONS:
            errors.append(f"组 {gid}: 非法 direction {g.get('direction')}")
        if not g.get("scope"):
            errors.append(f"组 {gid}: 缺少口径说明 scope")
    for sid, s in sources.items():
        if not str(s.get("url", "")).startswith("https://"):
            errors.append(f"来源 {sid}: 非 HTTPS 链接")
        if s.get("level") not in ("A", "B"):
            errors.append(f"来源 {sid}: 非法来源等级")

    seen: set[tuple] = set()
    by_key: dict[str, set[str]] = {}
    for i, o in enumerate(obs, 1):
        for f in REQUIRED_OBS:
            if not o.get(f):
                errors.append(f"观测 {i}: 缺少字段 {f}")
        gid = o.get("group")
        if gid not in groups:
            errors.append(f"观测 {i}: 未知可比组 {gid}")
        if o.get("src") not in sources:
            errors.append(f"观测 {i}: 未知来源 {o.get('src')}")
        # unit / direction 必须由组继承，观测层重复声明会造成口径冲突
        if "unit" in o or "direction" in o:
            errors.append(f"观测 {i}: unit/direction 应由 group 统一定义，不得在观测层声明")

        pk = (o.get("model"), o.get("benchmark"), o.get("key"), gid)
        if pk in seen:
            errors.append(f"观测 {i}: 主键重复 {pk}")
        seen.add(pk)

        value = o.get("value", "MISSING")
        status = o.get("status", "verified")
        if status not in VALID_STATUSES:
            errors.append(f"观测 {i}: 非法 status {status}")
        if value is None:
            if status != "not_disclosed":
                errors.append(f"观测 {i}: value=null 必须标记 status=not_disclosed")
        elif value == "MISSING":
            errors.append(f"观测 {i}: 缺少 value 字段")
        else:
            if status == "not_disclosed":
                errors.append(f"观测 {i}: 有数值却标记 not_disclosed")
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                errors.append(f"观测 {i}: value 必须是数值")
            else:
                unit = groups.get(gid, {}).get("unit")
                if unit == "percent" and not (0 <= value <= 100):
                    errors.append(f"观测 {i}: percent 越界 {value}")
                elif unit in ("elo", "tokens", "billion", "score") and value < 0:
                    errors.append(f"观测 {i}: {unit} 不得为负 {value}")

        rank = o.get("rank")
        if rank is not None and (not isinstance(rank, int) or isinstance(rank, bool) or rank < 1):
            errors.append(f"观测 {i}: rank 必须是正整数或 null")
        if rank is not None and value is None:
            errors.append(f"观测 {i}: 未披露的观测不得有排名")

        by_key.setdefault(str(o.get("key")), set()).add(str(gid))

    for key, gids in by_key.items():
        if len(gids) > 1:
            warnings.append(f"指标 {key} 出现在 {len(gids)} 个不同口径组（{', '.join(sorted(gids))}），禁止直接比较")
    return errors, warnings


def build_view(data: dict) -> dict:
    """纯逻辑：构造看板需要的派生统计，便于离线自测。"""
    groups = {g["id"]: g for g in data["groups"]}
    sources = {s["id"]: s for s in data["sources"]}
    obs = data["observations"]
    enriched = []
    for i, o in enumerate(obs):
        g, s = groups[o["group"]], sources[o["src"]]
        enriched.append({
            **o,
            "_i": i,
            "unit": g["unit"],
            "direction": g["direction"],
            "group_label": g["label"],
            "group_scope": g["scope"],
            "kind": g.get("kind", "benchmark"),
            "level": s["level"],
            "url": s["url"],
            "ref": s["ref"],
        })
    models = sorted({o["model"] for o in enriched})
    benchmarks = sorted({o["benchmark"] for o in enriched})
    group_ids = [g["id"] for g in data["groups"]]

    # 覆盖率：只统计「有数值的观测」落在多少个可比组里。
    coverage = {}
    for m in models:
        covered = {o["group"] for o in enriched if o["model"] == m and o.get("value") is not None}
        coverage[m] = {
            "groups": len(covered),
            "total": len(group_ids),
            "ratio": round(len(covered) / len(group_ids), 4) if group_ids else 0.0,
            "observations": sum(1 for o in enriched if o["model"] == m),
            "valued": sum(1 for o in enriched if o["model"] == m and o.get("value") is not None),
        }
    valued = sum(1 for o in enriched if o.get("value") is not None)
    return {
        "observations": enriched,
        "groups": data["groups"],
        "sources": data["sources"],
        "models": models,
        "benchmarks": benchmarks,
        "coverage": coverage,
        "stats": {
            "models": len(models),
            "benchmarks": len(benchmarks),
            "groups": len(group_ids),
            "metrics": len({o["key"] for o in enriched}),
            "observations": len(enriched),
            "valued": valued,
            "not_disclosed": len(enriched) - valued,
            "level_a": sum(1 for o in enriched if o["level"] == "A"),
            "overall_coverage": round(
                sum(c["groups"] for c in coverage.values()) / (len(models) * len(group_ids)), 4
            ) if models and group_ids else 0.0,
        },
    }


# ---------------------------------------------------------------------------
# HTML 渲染
# ---------------------------------------------------------------------------

TEMPLATE = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>📊 Benchmark 看板 — House of Model Cards</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>📊</text></svg>">
<style>
:root{--bg:#0d1117;--bg2:#161b22;--bg3:#1c2333;--bgc:#1c2333;--tx:#e6edf3;--tx2:#8b949e;--tx3:#6e7681;--bd:#30363d;
--bl:#58a6ff;--pr:#bc8cff;--gr:#3fb950;--rd:#f85149;--or:#d29922;--cy:#39c5cf;--pk:#db61a2}
*{margin:0;padding:0;box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:64px}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans SC',Helvetica,Arial,sans-serif;background:var(--bg);color:var(--tx);line-height:1.7;font-size:15.5px}
::-webkit-scrollbar{width:8px}::-webkit-scrollbar-thumb{background:var(--bd);border-radius:4px}
.nav{position:fixed;top:0;left:0;right:0;z-index:1000;background:rgba(13,17,23,.92);backdrop-filter:blur(16px);border-bottom:1px solid var(--bd);height:64px;display:flex;align-items:center;justify-content:space-between;padding:0 24px}
.nb a{display:flex;align-items:center;gap:10px;font-size:18px;font-weight:700;color:var(--tx);text-decoration:none}
.nb a span{background:linear-gradient(135deg,var(--bl),var(--pr),var(--pk));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.nl{display:flex;gap:4px}.nl a{color:var(--tx2);padding:6px 14px;border-radius:6px;font-size:13.5px;text-decoration:none;transition:.25s}
.nl a:hover{color:var(--tx);background:#252d40}
.ly{display:flex;max-width:1440px;margin:0 auto;padding-top:64px}
.sd{width:250px;flex-shrink:0;position:sticky;top:64px;height:calc(100vh-64px);overflow-y:auto;padding:20px 0 20px 16px;border-right:1px solid var(--bd)}
.tot{font-size:12px;text-transform:uppercase;letter-spacing:1.5px;color:var(--tx3);padding:0 12px 12px;font-weight:600}
.tol{list-style:none}.tol a{display:block;color:var(--tx2);text-decoration:none;padding:4px 12px 4px 18px;font-size:13px;border-left:2px solid transparent;transition:.25s;line-height:1.5}
.tol a:hover,.tol a.on{color:var(--bl);border-left-color:var(--bl);font-weight:600}
.mc{flex:1;min-width:0;padding:24px 32px 60px;max-width:1120px}
.hero{text-align:center;padding:30px 0 22px}
.hero h1{font-size:clamp(24px,3.6vw,34px);font-weight:800;line-height:1.25;margin-bottom:12px;
  background:linear-gradient(135deg,var(--bl),var(--cy),var(--pr));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.hero p{font-size:15px;color:var(--tx2);max-width:820px;margin:0 auto;line-height:1.65}
h2{font-size:22px;font-weight:800;margin:42px 0 14px;padding-bottom:9px;border-bottom:1px solid var(--bd);scroll-margin-top:72px;line-height:1.3}
h3{font-size:16px;font-weight:700;margin:22px 0 10px;color:var(--cy)}
a{color:var(--bl);text-decoration:none}a:hover{color:var(--cy);text-decoration:underline}
code{background:var(--bg3);color:var(--cy);padding:2px 6px;border-radius:4px;font-size:88%;font-family:'SF Mono','Fira Code',Consolas,monospace;border:1px solid rgba(88,166,255,.15)}
blockquote{border-left:4px solid var(--bl);margin:14px 0;padding:12px 16px;background:linear-gradient(90deg,rgba(88,166,255,.05),transparent);border-radius:0 6px 6px 0;color:var(--tx2);font-size:14px}
.sts{display:grid;grid-template-columns:repeat(auto-fit,minmax(132px,1fr));gap:10px;margin:22px 0}
.st{background:var(--bgc);border:1px solid var(--bd);border-radius:10px;padding:14px 10px;text-align:center;transition:.25s}
.st:hover{border-color:var(--bl);transform:translateY(-2px)}
.sn{font-size:23px;font-weight:800;color:var(--bl)}.sl{font-size:11.5px;color:var(--tx3)}
.cd{background:var(--bgc);border:1px solid var(--bd);border-radius:12px;margin:16px 0;overflow:hidden}
.ch{padding:12px 16px;border-bottom:1px solid var(--bd);background:var(--bg3);font-weight:700;font-size:15px}
.cb{padding:12px 16px;font-size:14px;color:var(--tx2)}
.tw{overflow-x:auto;margin:14px 0;border-radius:10px;border:1px solid var(--bd)}
table{width:100%;border-collapse:collapse;font-size:13.5px}
thead{background:var(--bg3)}th{padding:8px 10px;text-align:left;font-weight:600;font-size:12px;color:var(--tx);border-bottom:1px solid var(--bd);white-space:nowrap}
td{padding:8px 10px;border-bottom:1px solid var(--bd);color:var(--tx2);vertical-align:middle}
tbody tr:hover{background:#252d40}
th.s{cursor:pointer;user-select:none}th.s:hover{color:var(--bl)}th.s.act{color:var(--bl)}
.fl{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:10px;margin:14px 0}
.fl label{display:block;font-size:11.5px;color:var(--tx3);margin-bottom:4px;text-transform:uppercase;letter-spacing:.5px}
input[type=text],select{width:100%;background:var(--bg2);border:1px solid var(--bd);border-radius:6px;color:var(--tx);padding:7px 9px;font-size:13px;outline:none;font-family:inherit}
input[type=text]:focus,select:focus{border-color:var(--bl)}
.chk{display:flex;align-items:center;gap:7px;font-size:13px;color:var(--tx2);margin-top:20px}
.chk input{accent-color:var(--bl)}
.tip{font-size:12.5px;color:var(--tx3);margin:8px 0}
.warn{background:rgba(210,153,34,.1);border:1px solid rgba(210,153,34,.3);color:var(--or);border-radius:6px;padding:8px 12px;font-size:13px;margin:10px 0}
.chip{display:inline-flex;align-items:center;gap:5px;padding:2px 9px;border-radius:20px;font-size:11.5px;font-weight:600;border:1px solid var(--bd);background:var(--bg3);color:var(--tx2);cursor:pointer;user-select:none;margin:3px 4px 3px 0}
.chip.on{background:rgba(88,166,255,.15);border-color:var(--bl);color:var(--bl)}
.lvA{color:var(--gr);font-weight:700}.lvB{color:var(--or);font-weight:700}
.miss{color:var(--tx3);font-style:italic}.none{color:var(--tx3);opacity:.55}
.low{color:var(--or);font-weight:700}.high{color:var(--gr);font-weight:700}
.bar{height:6px;border-radius:4px;background:var(--bg3);overflow:hidden;min-width:70px;display:inline-block;vertical-align:middle}
.bar>i{display:block;height:100%;background:linear-gradient(90deg,var(--bl),var(--cy))}
.mx td,.mx th{text-align:center;font-size:12px;padding:6px 7px}
.mx td:first-child,.mx th:first-child{text-align:left;position:sticky;left:0;background:var(--bg2);z-index:1}
.hv{background:rgba(63,185,80,.14);color:var(--cl,#7ee787);border-radius:4px;padding:2px 5px;font-weight:600}
.hv0{background:rgba(248,81,73,.1);color:var(--rd);border-radius:4px;padding:2px 5px}
.ft{text-align:center;padding:26px 0 20px;border-top:1px solid var(--bd);color:var(--tx3);font-size:13px;margin-top:44px}
.btt{position:fixed;bottom:26px;right:26px;z-index:999;width:40px;height:40px;border-radius:50%;background:var(--bg3);border:1px solid var(--bd);color:var(--tx2);cursor:pointer;opacity:0;visibility:hidden;transition:.25s}
.btt.vis{opacity:1;visibility:visible}.btt:hover{background:var(--bl);color:#fff}
@media(max-width:1024px){.sd{display:none}.mc{padding:18px 16px 50px;max-width:100%}}
@media(max-width:640px){body{font-size:14px}h2{font-size:19px}.sts{grid-template-columns:repeat(2,1fr)}}
</style>
</head>
<body>
<nav class="nav"><div class="nb"><a href="index.html">🃏 <span>HOMC · Benchmark 看板</span></a></div>
<div class="nl"><a href="index.html">← 返回主站</a><a href="#filters">筛选</a><a href="#matrix">覆盖率</a><a href="#compare">横向对比</a><a href="#caveats">口径说明</a></div></nav>
<div class="ly">
<aside class="sd"><div class="tot">📑 看板导航</div><ul class="tol">
<li><a href="#overview">📊 总览</a></li><li><a href="#filters">🔍 筛选与排序</a></li>
<li><a href="#detail">📋 观测明细</a></li><li><a href="#matrix">🧩 覆盖矩阵</a></li>
<li><a href="#compare">⚖️ 横向对比</a></li><li><a href="#caveats">⚠️ 口径与缺失</a></li>
<li><a href="index.html">← HOMC 主站</a></li></ul></aside>
<main class="mc">
<div class="hero" id="overview"><h1>📊 多榜单 Benchmark 可视化看板</h1>
<p>统一收录项目内全部可核实的模型指标。每条观测绑定模型、榜单、指标与口径组；排名只在同组内有效，不同单位、方向或 harness 的指标不参与混算。缺失指标显式标注，不做补零或跨口径平均。</p></div>
<div class="sts" id="stats"></div>
<div class="cd"><div class="ch">📐 数据口径（先看这里）</div><div class="cb" id="principle"></div></div>

<h2 id="filters">🔍 筛选与排序</h2>
<div class="fl" id="filtersBox"></div>
<label class="chk"><input type="checkbox" id="onlyValued"> 仅显示有数值的观测（隐藏「官方未披露」）</label>
<div class="tip" id="filterTip"></div>
<div id="sortWarn"></div>

<h2 id="detail">📋 观测明细</h2>
<div class="tip">点击表头可排序。<b>跨口径组的数值排序已禁用</b>——不同单位或方向的分数放在一起排序没有意义；请先选定单个可比组。</div>
<div class="tw"><table id="obsTable"><thead><tr id="obsHead"></tr></thead><tbody id="obsBody"></tbody></table></div>

<h2 id="matrix">🧩 模型 × 榜单 覆盖矩阵与指标覆盖率</h2>
<div class="tip" id="covTip"></div>
<div style="margin:10px 0"><button class="chip on" id="btnGroup" onclick="setMatrix('group')">按可比组（12）</button><button class="chip" id="btnBench" onclick="setMatrix('benchmark')">按榜单（23）</button></div>
<div class="tw"><table class="mx" id="covTable"></table></div>
<div class="cd"><div class="ch">📈 各模型指标覆盖率</div><div class="cb" id="covBars"></div></div>

<h2 id="compare">⚖️ 模型横向对比</h2>
<div class="tip">勾选 2–4 个模型。对比表只列出<strong>至少两个所选模型都有数值</strong>的行，缺失显示「未披露」；同名但跨口径的指标分行展示并标注不可比较。</div>
<div id="cmpChips"></div><div id="cmpWarn"></div>
<div class="tw"><table id="cmpTable"></table></div>

<h2 id="caveats">⚠️ 口径差异与缺失清单</h2>
<div id="caveatsBox"></div>

<div class="ft">🃏 <strong>House of Model Cards (HOMC)</strong> · Benchmark 看板 |
<a href="index.html">返回主站</a> | 数据截至 __UPDATED__ · 自 <code>data/benchmark_observations.json</code> 生成</div>
</main></div>
<div class="btt" id="bt" onclick="window.scrollTo({top:0,behavior:'smooth'})">↑</div>
<script>
const DATA = __DATA__;
const G = Object.fromEntries(DATA.groups.map(g=>[g.id,g]));
const S = Object.fromEntries(DATA.sources.map(s=>[s.id,s]));
const OBS = DATA.observations.map((o,i)=>Object.assign({},o,{_i:i,unit:G[o.group].unit,direction:G[o.group].direction,
  group_label:G[o.group].label,group_scope:G[o.group].scope,kind:G[o.group].kind||'benchmark',
  level:S[o.src].level,url:S[o.src].url,ref:S[o.src].ref}));
const MODELS = [...new Set(OBS.map(o=>o.model))].sort();
const BENCHS = [...new Set(OBS.map(o=>o.benchmark))].sort();
const PROVIDERS = [...new Set(OBS.map(o=>o.provider))].sort();
const GROUPS = DATA.groups;
const esc = s => String(s==null?'':s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const st = {q:'',provider:'',benchmark:'',group:'',level:'',kind:'',onlyValued:false,
  sort:'model',dir:1,compare:[],matrix:'group'};

function fmt(o){
  if(o.value==null) return '<span class="miss">未披露</span>';
  const v=o.value;
  if(o.unit==='percent') return Number(v).toFixed(1)+'%';
  if(o.unit==='elo') return Number(v).toLocaleString();
  if(o.unit==='tokens') return v>=1000000 ? (v/1000000)+'M' : (v>=1000 ? (v/1000)+'K' : String(v));
  if(o.unit==='billion') return v+'B';
  return String(v);
}
function unitCn(u){return {percent:'百分比',score:'指数分',elo:'Elo',tokens:'Token',billion:'十亿参数'}[u]||u;}
function dirTag(o){return o.direction==='lower'
  ? '<span class="low">↓ 越低越好</span>' : '<span class="high">↑ 越高越好</span>';}

function filtered(){
  let r=OBS.filter(o=>{
    if(st.q && !(o.model+' '+o.provider+' '+o.benchmark+' '+o.metric+' '+o.key).toLowerCase().includes(st.q.toLowerCase())) return false;
    if(st.provider && o.provider!==st.provider) return false;
    if(st.benchmark && o.benchmark!==st.benchmark) return false;
    if(st.group && o.group!==st.group) return false;
    if(st.level && o.level!==st.level) return false;
    if(st.kind && o.kind!==st.kind) return false;
    if(st.onlyValued && o.value==null) return false;
    return true;
  });
  const groupsInResult=new Set(r.map(o=>o.group));
  const crossGroupValueSort = st.sort==='value' && groupsInResult.size>1;
  document.getElementById('sortWarn').innerHTML = crossGroupValueSort
    ? '<div class="warn">⚠️ 当前结果包含 '+groupsInResult.size+' 个可比组，<b>跨组按数值排序已禁用</b>（单位 / 方向 / harness 不同）。请先在「可比组」下拉中选定单个组。</div>' : '';
  const key=st.sort;
  r.sort((a,b)=>{
    let x,y;
    if(key==='value'){
      if(crossGroupValueSort){x=a.model;y=b.model;}
      else {x=a.value==null?Infinity:a.value;y=b.value==null?Infinity:b.value;}
    } else if(key==='rank'){x=a.rank==null?9999:a.rank;y=b.rank==null?9999:b.rank;}
    else {x=a[key]||'';y=b[key]||'';}
    if(typeof x==='string') return x.localeCompare(y,'zh')*st.dir;
    return (x-y)*st.dir;
  });
  // direction 只作为「表现方向」标注，不自动反转排序：升序恒为数值从小到大，
  // 对 lower-is-better 的指标而言这恰好把最优值排在前面，行为可预期。
  return r;
}

function renderStats(){
  const valued=OBS.filter(o=>o.value!=null).length;
  const cov={};
  MODELS.forEach(m=>{cov[m]=new Set(OBS.filter(o=>o.model===m&&o.value!=null).map(o=>o.group)).size;});
  const overall=(Object.values(cov).reduce((a,b)=>a+b,0)/(MODELS.length*GROUPS.length)*100).toFixed(1);
  const cards=[
    ['🤖',MODELS.length,'模型'],['🏁',BENCHS.length,'榜单 / 规格'],['🧪',new Set(OBS.map(o=>o.key)).size,'指标'],
    ['📌',OBS.length,'观测'],['✅',valued,'有数值'],['⚠️',OBS.length-valued,'未披露'],
    ['🔬',GROUPS.length,'可比组'],['🧩',overall+'%','整体覆盖率']
  ];
  document.getElementById('stats').innerHTML=cards.map(c=>
    '<div class="st"><div class="sn">'+c[1]+'</div><div class="sl">'+c[0]+' '+c[2]+'</div></div>').join('');
  document.getElementById('principle').innerHTML=
    '<p>'+esc(DATA.meta.principle)+'</p><p style="margin-top:8px">'+esc(DATA.meta.missing_policy)+'</p>'+
    '<p style="margin-top:8px">'+esc(DATA.meta.unit_policy)+'</p>'+
    '<blockquote style="margin-top:10px">'+esc(DATA.meta.duplicate_policy)+'</blockquote>';
}

function sel(id,label,opts,val){
  return '<div><label>'+label+'</label><select id="'+id+'"><option value="">全部</option>'+
    opts.map(o=>'<option value="'+esc(o[0])+'"'+(o[0]===val?' selected':'')+'>'+esc(o[1])+'</option>').join('')+'</select></div>';
}
function renderFilters(){
  document.getElementById('filtersBox').innerHTML=
    '<div><label>关键词（模型 / 指标）</label><input type="text" id="fq" placeholder="如 HLE、HealthBench…" value="'+esc(st.q)+'"></div>'+
    sel('fprovider','提供方',PROVIDERS.map(x=>[x,x]),st.provider)+
    sel('fbenchmark','榜单',BENCHS.map(x=>[x,x]),st.benchmark)+
    sel('fgroup','可比组（决定排序口径）',GROUPS.map(g=>[g.id,g.label]),st.group)+
    sel('flevel','来源等级',[['A','A · 一手'],['B','B · 二手交叉']],st.level)+
    sel('fkind','类型',[['benchmark','评测'],['ranking','榜单'],['safety','安全对齐'],['spec','官方规格']],st.kind)+
    '<div><label>排序字段</label><select id="fsort">'+
      [['model','模型名'],['benchmark','榜单'],['value','数值（仅同组）'],['rank','组内排名'],['date','日期'],['level','来源等级']]
      .map(o=>'<option value="'+o[0]+'"'+(o[0]===st.sort?' selected':'')+'>'+o[1]+'</option>').join('')+'</select></div>'+
    '<div><label>排序方向</label><select id="fdir"><option value="1"'+(st.dir===1?' selected':'')+'>升序 / A→Z</option><option value="-1"'+(st.dir===-1?' selected':'')+'>降序 / Z→A</option></select></div>';
  const bind=(id,fn)=>document.getElementById(id).addEventListener(fn[0],e=>{fn[1](e.target.value);});
  bind('fq',['input',v=>{st.q=v;refresh();}]);
  [['fprovider','provider'],['fbenchmark','benchmark'],['fgroup','group'],['flevel','level'],['fkind','kind'],['fsort','sort'],['fdir','dir']]
    .forEach(([id,k])=>bind(id,['change',v=>{st[k]=(k==='dir')?Number(v):v;refresh();}]));
  document.getElementById('onlyValued').checked=st.onlyValued;
  document.getElementById('onlyValued').addEventListener('change',e=>{st.onlyValued=e.target.checked;refresh();});
}

const HEADS=[['model','模型'],['provider','提供方'],['benchmark','榜单 / 规格'],['metric','指标'],['value','数值'],
  ['unit','单位'],['direction','方向'],['rank','组内排名'],['group_label','可比组'],['level','来源'],['date','日期'],['group_scope','口径说明']];
function renderTable(){
  document.getElementById('obsHead').innerHTML=HEADS.map((h,i)=>
    '<th class="s'+(st.sort===h[0]?' act':'')+'" onclick="setSort(\''+h[0]+'\')">'+h[1]+(st.sort===h[0]?(st.dir===1?' ↑':' ↓'):'')+'</th>').join('');
  const r=filtered();
  document.getElementById('obsBody').innerHTML=r.map(o=>
    '<tr><td><b>'+esc(o.model)+'</b></td><td>'+esc(o.provider)+'</td><td>'+esc(o.benchmark)+'</td><td>'+esc(o.metric)+
    '</td><td><b>'+fmt(o)+'</b></td><td>'+unitCn(o.unit)+'</td><td>'+dirTag(o)+'</td><td>'+
    (o.rank!=null?'#'+o.rank:'<span class="none">—</span>')+'</td><td>'+esc(o.group_label)+'</td>'+
    '<td><span class="lv'+o.level+'">['+o.level+']</span> <a href="'+esc(o.url)+'" target="_blank" title="'+esc(o.ref)+'">来源 ↗</a></td>'+
    '<td>'+esc(o.date||'未标注')+'</td><td style="font-size:12px">'+esc(o.group_scope)+'</td></tr>').join('');
  document.getElementById('filterTip').textContent='显示 '+r.length+' / '+OBS.length+' 条观测';
}
function setSort(k){ if(st.sort===k) st.dir=-st.dir; else {st.sort=k;st.dir=1;} refresh(); }

function setMatrix(mode){
  st.matrix=mode;
  document.getElementById('btnGroup').classList.toggle('on',mode==='group');
  document.getElementById('btnBench').classList.toggle('on',mode==='benchmark');
  renderMatrix();
}
function renderMatrix(){
  const cols = st.matrix==='group' ? GROUPS.map(g=>[g.id,g.label]) : BENCHS.map(b=>[b,b]);
  const idx = st.matrix==='group' ? (o=>o.group) : (o=>o.benchmark);
  let h='<thead><tr><th>模型</th>'+cols.map(c=>'<th title="'+esc(c[1])+'">'+esc(c[1].length>12?c[1].slice(0,11)+'…':c[1])+'</th>').join('')+'<th>覆盖率</th></tr></thead><tbody>';
  MODELS.forEach(m=>{
    const mine=OBS.filter(o=>o.model===m);
    const covered=new Set(mine.filter(o=>o.value!=null).map(idx)).size;
    const ratio=covered/cols.length;
    h+='<tr><td><b>'+esc(m)+'</b></td>';
    cols.forEach(c=>{
      const cell=mine.filter(o=>idx(o)===c[0]&&o.value!=null);
      const nd=mine.filter(o=>idx(o)===c[0]&&o.value==null);
      if(cell.length) h+='<td><span class="hv" title="'+esc(cell.map(o=>o.metric+': '+fmt(o).replace(/<[^>]+>/g,'')).join(' · '))+'">'+cell.length+' 项</span></td>';
      else if(nd.length) h+='<td><span class="hv0" title="官方明确未披露">未披露</span></td>';
      else h+='<td class="none">—</td>';
    });
    h+='<td><span class="bar"><i style="width:'+Math.round(ratio*100)+'%"></i></span> '+(ratio*100).toFixed(0)+'%</td></tr>';
  });
  h+='</tbody>';
  document.getElementById('covTable').innerHTML=h;
  document.getElementById('covTip').innerHTML='列为'+(st.matrix==='group'?'<b>可比组</b>':'<b>榜单 / 规格</b>')+
    '。绿色 = 有数值（悬停看明细），红色「未披露」= 官方明确未公布，灰色「—」= 该模型未参与该评测。'+
    '<b>「—」不等于 0 分，也不代表能力不足</b>；覆盖率只按有数值的格子计算。';
  const cov=MODELS.map(m=>({m,n:new Set(OBS.filter(o=>o.model===m&&o.value!=null).map(idx)).size}))
    .sort((a,b)=>b.n-a.n);
  document.getElementById('covBars').innerHTML=cov.map(c=>
    '<div style="display:flex;align-items:center;gap:10px;margin:5px 0;font-size:13px">'+
    '<span style="min-width:170px">'+esc(c.m)+'</span><span class="bar" style="flex:1"><i style="width:'+
    Math.round(c.n/cols.length*100)+'%"></i></span><span style="min-width:74px;text-align:right">'+c.n+' / '+cols.length+'</span></div>').join('');
}

function renderCompare(){
  document.getElementById('cmpChips').innerHTML=MODELS.map(m=>
    '<span class="chip'+(st.compare.includes(m)?' on':'')+'" onclick="toggleCmp(\''+esc(m).replace(/'/g,"\\'")+'\')">'+
    (st.compare.includes(m)?'✓ ':'+ ')+esc(m)+'</span>').join('');
  const sel=st.compare;
  document.getElementById('cmpWarn').innerHTML = sel.length<2
    ? '<div class="warn">请至少勾选 2 个模型以生成对比。</div>'
    : sel.length>4 ? '<div class="warn">最多对比 4 个模型，请取消部分勾选。</div>' : '';
  if(sel.length<2||sel.length>4){document.getElementById('cmpTable').innerHTML='';return;}
  const rows=new Map();
  OBS.filter(o=>sel.includes(o.model)).forEach(o=>{
    const k=o.key+'|'+o.group;
    if(!rows.has(k)) rows.set(k,{metric:o.metric,key:o.key,group:o.group,label:o.group_label,unit:o.unit,dir:o.direction,vals:{}});
    rows.get(k).vals[o.model]=o;
  });
  const list=[...rows.values()].filter(r=>Object.values(r.vals).some(o=>o.value!=null));
  const shared=list.filter(r=>Object.values(r.vals).filter(o=>o.value!=null).length>=2);
  const sameKeyCrossGroup=[...new Set(list.map(r=>r.key))].filter(k=>new Set(list.filter(r=>r.key===k).map(r=>r.group)).size>1);
  let h='<thead><tr><th>指标</th><th>可比组 / 单位</th>'+sel.map(m=>'<th>'+esc(m)+'</th>').join('')+'<th>可比性</th></tr></thead><tbody>';
  list.forEach(r=>{
    const n=Object.values(r.vals).filter(o=>o.value!=null).length;
    h+='<tr'+(n<2?' style="opacity:.72"':'')+'><td><b>'+esc(r.metric)+'</b></td><td style="font-size:12px">'+esc(r.label)+
      '<br><span class="none">'+unitCn(r.unit)+' · '+(r.dir==='lower'?'越低越好':'越高越好')+'</span></td>';
    sel.forEach(m=>{
      const o=r.vals[m];
      h+='<td>'+(o? (o.value==null?'<span class="miss">未披露</span>':'<b>'+fmt(o)+'</b>'+(o.rank!=null?' <span class="none">#'+o.rank+'</span>':''))
        : '<span class="none">—</span>')+'</td>';
    });
    h+='<td style="font-size:12px">'+(n>=2?'<span class="high">共同可比</span>':'<span class="miss">仅 1 个有值</span>')+
      (sameKeyCrossGroup.includes(r.key)?'<br><span class="low">同名跨口径 ⚠</span>':'')+'</td></tr>';
  });
  h+='</tbody>';
  document.getElementById('cmpTable').innerHTML=h;
  if(sameKeyCrossGroup.length){
    document.getElementById('cmpWarn').innerHTML+='<div class="warn">⚠️ <b>同名跨口径</b>：指标 <b>'+sameKeyCrossGroup.join('、')+
      '</b> 出现在不同口径组，表格已分行展示；<b>请勿把这两行的数值直接相减或并列排名</b>。</div>';
  }
}
function toggleCmp(m){
  const i=st.compare.indexOf(m);
  if(i>=0) st.compare.splice(i,1); else if(st.compare.length<4) st.compare.push(m);
  renderCompare();
}

function renderCaveats(){
  const byKey={};
  OBS.forEach(o=>{(byKey[o.key]=byKey[o.key]||new Set()).add(o.group);});
  const cross=Object.entries(byKey).filter(([k,v])=>v.size>1);
  const lower=GROUPS.filter(g=>g.direction==='lower');
  const nd=OBS.filter(o=>o.value==null);
  const b=OBS.filter(o=>o.level==='B');
  const units=[...new Set(GROUPS.map(g=>g.unit))];
  let h='<div class="cd"><div class="ch">🔀 同名指标跨口径（禁止直接比较）</div><div class="cb">'+
    (cross.length? cross.map(([k,v])=>'<p>• <code>'+esc(k)+'</code> → '+esc([...v].join(' / '))+
      '：'+esc(OBS.filter(o=>o.key===k).map(o=>o.model+' '+fmt(o).replace(/<[^>]+>/g,'')).join('；'))+'</p>').join('')
      : '<p>无。</p>')+'</div></div>';
  h+='<div class="cd"><div class="ch">↓ 方向相反与单位隔离</div><div class="cb"><p>越低越好的组：<b>'+
    esc(lower.map(g=>g.label).join('、')||'无')+'</b>，排序时已自动反向。</p><p>本次收录单位：<b>'+
    esc(units.map(unitCn).join(' / '))+'</b>；不同单位不进入同一次排序、平均或求和。</p></div></div>';
  h+='<div class="cd"><div class="ch">⚠️ 官方明确未披露（'+nd.length+' 条，不参与统计）</div><div class="cb">'+
    nd.map(o=>'<p>• <b>'+esc(o.model)+'</b> / '+esc(o.metric)+' — <span class="miss">未披露</span> <span style="font-size:12px">'+esc(o.note||'')+'</span></p>').join('')+'</div></div>';
  h+='<div class="cd"><div class="ch">📎 二手来源观测（'+b.length+' 条，引用前复核）</div><div class="cb">'+
    (b.length?b.map(o=>'<p>• <b>'+esc(o.model)+'</b> / '+esc(o.metric)+' = '+fmt(o)+
      ' <a href="'+esc(o.url)+'" target="_blank">来源 ↗</a> <span style="font-size:12px">'+esc(o.note||'')+'</span></p>').join('')
      :'<p>无。</p>')+'</div></div>';
  h+='<div class="cd"><div class="ch">🧮 去重与聚合规则</div><div class="cb"><p>'+esc(DATA.meta.duplicate_policy)+
    '</p><p style="margin-top:8px">'+esc(DATA.meta.missing_policy)+'</p></div></div>';
  document.getElementById('caveatsBox').innerHTML=h;
}

function refresh(){renderTable();renderMatrix();renderCompare();}
renderStats();renderFilters();renderCaveats();refresh();
window.addEventListener('scroll',()=>document.getElementById('bt').classList.toggle('vis',window.scrollY>400));
</script>
</body></html>
'''


def render_html(data: dict, view: dict) -> str:
    payload = json.dumps({
        "meta": data["meta"],
        "groups": data["groups"],
        "sources": data["sources"],
        "observations": data["observations"],
    }, ensure_ascii=False, separators=(",", ":"))
    # 把内联数据里的尖括号与 & 全部转成 Unicode 转义，确保数据中的
    # <script> / </script> / HTML 注释都不会被浏览器当作标记解析。
    payload = (
        payload.replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("&", "\\u0026")
    )
    return (
        TEMPLATE.replace("__DATA__", payload)
        .replace("__UPDATED__", html.escape(str(data["meta"].get("updated", ""))))
    )


def run(cfg: Config) -> dict[str, bool]:
    data = load_data(cfg.root)
    errors, warnings = validate(data)
    if errors:
        raise ValueError("数据校验失败:\n  " + "\n  ".join(errors))
    view = build_view(data)
    page = render_html(data, view)
    out = cfg.root / OUTPUT_FILE
    old = out.read_text(encoding="utf-8") if out.exists() else None
    if not cfg.dry_run:
        out.write_text(page, encoding="utf-8")
    if cfg.dry_run:
        print(page[:1200])
    for w in warnings:
        print(f"[warning] {w}", file=sys.stderr)
    return {"benchmarks.html": old != page}


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=".", help="仓库根目录")
    p.add_argument("--dry-run", action="store_true", help="只预览，不写文件")
    p.add_argument("--validate", action="store_true", help="只校验数据，不写文件")
    a = p.parse_args(argv)
    root = Path(a.root).resolve()
    try:
        if a.validate:
            errors, warnings = validate(load_data(root))
            for w in warnings:
                print(f"[warning] {w}", file=sys.stderr)
            if errors:
                for e in errors:
                    print(f"[validate] ERROR: {e}", file=sys.stderr)
                return 1
            print("[validate] OK: 主键 / 单位 / 方向 / 值域 / 排名 / 来源 / 缺失标记 全部通过")
            return 0
        changed = run(Config(root=root, dry_run=a.dry_run))
        if not a.dry_run:
            print(f"[result] changed: {changed}", file=sys.stderr)
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f"[error] {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
