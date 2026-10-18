"""把快照渲染成刊物版网页（最新一期 + 全部存档）、RSS 和 Markdown 报告。

每次运行都从 data/snapshots/ 重新渲染整站：存档页和往期列表始终用同一套样式，
对比关系也按 diff.previous_issue() 的规则重算（早期快照里存的 diff 可能是对临时更新比的）。
设计规格见 design/issue/DESIGN.md。
"""
import copy
import datetime as dt
import re
import xml.etree.ElementTree as ET
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup, escape

import diff

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
ARCHIVE = SITE / "archive"

# 衬线标题只用这些字，scripts/fetch_font.py 按它下载字体子集；改了标题文字要重跑那个脚本
HEADING_GLYPHS = "".join(sorted(set("第期创刊号临时更新本期变化编者按名录往期0123456789· ")))

# 兜底长度：模型偶尔超出提示词里的字数上限
LIMITS = {"tagline": 60, "positioning": 140, "item": 70, "audience": 90, "note": 90}
_BULLET = re.compile(r"^\s*(?:[-•·*]|\d+[.)、])\s*")


def _clip(text, n):
    text = " ".join((text or "").split())
    return text if len(text) <= n else text[:n - 1].rstrip("，,；;、 ") + "…"


def _as_list(value, n_items, n_chars):
    """新格式是数组；旧格式是带伪列表符号的长字符串，按行拆开。"""
    if isinstance(value, str):
        value = [_BULLET.sub("", ln) for ln in value.splitlines()] if "\n" in value else [value]
    return [_clip(v, n_chars) for v in value if v and v.strip()][:n_items]


def view(intro):
    """把缓存里的介绍规整成模板直接使用的字段（兼容 prompt_version 1 和 2）。"""
    positioning = intro.get("positioning", "")
    tagline = intro.get("tagline") or re.split(r"[。；;]", positioning, maxsplit=1)[0]
    return {
        "tagline": _clip(tagline, LIMITS["tagline"]),
        "positioning": _clip(positioning, LIMITS["positioning"]),
        "features": _as_list(intro.get("features"), 5, LIMITS["item"]),
        "highlights": _as_list(intro.get("highlights"), 3, LIMITS["item"]),
        "audience": _clip(intro.get("audience"), LIMITS["audience"]),
        "cmd": (intro.get("quickstart_cmd") or "").strip(),
        "note": _clip(intro.get("quickstart_note") or intro.get("quickstart"), LIMITS["note"]),
        "risks": intro.get("risks", []),
        "category": intro.get("category", "其他"),
    }


def _prepare(snapshot, categories):
    ranked = sorted(snapshot["entries"], key=lambda e: e["stars"], reverse=True)
    for i, e in enumerate(ranked, 1):
        e["rank"] = i
        e["v"] = view(e["intro"])
    groups = {c: [] for c in categories}
    for e in ranked:
        groups.setdefault(e["v"]["category"], []).append(e)
    return ranked, [(c, es) for c, es in groups.items() if es]


# ---------- 一期的完整上下文：页面、通知、RSS、报告共用 ----------

def _md(d):
    return f"{d.month:02d}-{d.day:02d}"


def _cn(d):
    return f"{d.year} 年 {d.month} 月 {d.day} 日"


def _absolutize(flag, e):
    """「已 N 天未更新」每天都在变旧，改成带最后推送日期的说法。"""
    return re.sub(r"已 (\d+) 天未更新",
                  lambda m: f"快照当日已 {m.group(1)} 天未更新（最后推送 {e['pushed_at']}）", flag)


def _link_names(text, ranked):
    """编者按里点名的项目短名 → 页内锚点。长名先匹配，免得被短名截走。"""
    names = sorted(((e["full_name"].split("/")[1], e["full_name"]) for e in ranked), key=lambda x: -len(x[0]))
    out = str(escape(text))
    for short, full in names:
        out = re.sub(rf"(?<![\w/#-]){re.escape(short)}(?![\w-])",
                     f'<a href="#{escape(full)}">{escape(short)}</a>', out, count=1)
    return Markup(out)


def issue_context(snap, snaps, cfg):
    d = dt.date.fromisoformat(snap["date"])
    issues = [s for s in snaps if diff.is_issue(s)]
    official = diff.is_issue(snap)
    prev = diff.previous_issue(snap["date"], snaps)
    entries = copy.deepcopy(snap["entries"])
    changes = diff.compute(entries, prev, cfg["top_gainers"])
    ranked, groups = _prepare({**snap, "entries": entries}, cfg["categories"])
    by_name = {e["full_name"]: e for e in ranked}
    for e in ranked:
        e["notes"] = e["v"]["risks"] + [_absolutize(f, e) for f in e["flags"]]
    win_start = d - dt.timedelta(days=snap["window_days"])

    dropped = []
    for x in changes["dropped"]:
        created = dt.date.fromisoformat(x["created_at"])
        reason = (f"创建于 {created.isoformat()}，已超出 {snap['window_days']} 天收录窗口"
                  if created < win_start else "星数跌破门槛，或被判定与 AI 无关")
        dropped.append({**x, "reason": reason})

    p = None
    if prev:
        pd = dt.date.fromisoformat(prev["date"])
        p = {"date": prev["date"], "md": _md(pd), "days": (d - pd).days,
             "no": [s["date"] for s in issues].index(prev["date"]) + 1}
    return dict(
        s=snap, official=official, d=d, date_cn=_cn(d), md=_md(d),
        no=[s["date"] for s in issues].index(snap["date"]) + 1 if official else None,
        win=f"{win_start.isoformat()} 至 {d.isoformat()}",
        prev=p, ranked=ranked, groups=groups,
        new=[by_name[n] for n in changes["new"] if n in by_name],
        gainers=[{**g, "e": by_name.get(g["full_name"])} for g in changes["gainers"]],
        dropped=dropped,
        trends=[_link_names(t, ranked) for t in snap["trends"]],
        trends_plain=snap["trends"],
        noted=sum(1 for e in ranked if e["notes"]),
        warn=cfg.get("warn_categories") or {},
    )


def title_of(ctx):
    head = f"第 {ctx['no']} 期 · {ctx['s']['date']}" if ctx["official"] else f"临时更新 · {ctx['s']['date']}"
    if not ctx["prev"]:
        return head + ("：创刊号" if ctx["official"] else "：首次运行，无可对比的正式期")
    return f"{head}：新上榜 {len(ctx['new'])} · 移出 {len(ctx['dropped'])}"


# ---------- 输出 ----------

def render_site(cfg, snaps=None):
    """从全部快照重渲染整站，返回最新一个正式期的上下文（给通知用，没有正式期时为 None）。"""
    snaps = diff.load_all() if snaps is None else snaps
    ctxs = [issue_context(s, snaps, cfg) for s in snaps]
    env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=select_autoescape(["html", "j2"]),
                      trim_blocks=True, lstrip_blocks=True)
    tpl = env.get_template("index.html.j2")
    nav = [{"no": c["no"], "date": c["s"]["date"], "md": c["md"], "cn": c["date_cn"],
            "count": len(c["ranked"]), "official": c["official"]} for c in reversed(ctxs)]
    latest = ctxs[-1]
    common = dict(nav=nav, latest_date=latest["s"]["date"], site_url=cfg.get("site_url", ""),
                  repo_url=cfg.get("repo_url", "").rstrip("/"), built=dt.date.today().isoformat())

    ARCHIVE.mkdir(parents=True, exist_ok=True)
    for c in ctxs:
        (ARCHIVE / f"{c['s']['date']}.html").write_text(tpl.render(**c, **common, root="../"),
                                                        encoding="utf-8", newline="\n")
    (SITE / "index.html").write_text(tpl.render(**latest, **common, root=""), encoding="utf-8", newline="\n")
    _write_feed(cfg, [c for c in ctxs if c["official"]])
    (ROOT / "report.md").write_text(_markdown(latest), encoding="utf-8")
    official = [c for c in ctxs if c["official"]]
    return official[-1] if official else None


def _summary_html(c, url):
    """RSS 条目正文：本期变化 + 编者按，阅读器里不点开也能看个大概。"""
    parts = []
    if not c["prev"]:
        parts.append(f"<p>创刊号，共收录 {len(c['ranked'])} 个项目。</p>")
    else:
        parts.append(f"<p>较第 {c['prev']['no']} 期（{c['prev']['date']}，{c['prev']['days']} 天）：</p>")
        if c["new"]:
            parts.append("<h3>新上榜</h3><ul>" + "".join(
                f"<li><a href=\"{escape(e['html_url'])}\">{escape(e['full_name'])}</a> ★ {e['stars']:,} — "
                f"{escape(e['v']['tagline'])}</li>" for e in c["new"]) + "</ul>")
        if c["dropped"]:
            parts.append("<h3>移出</h3><ul>" + "".join(
                f"<li>{escape(x['full_name'])}：{escape(x['reason'])}</li>" for x in c["dropped"]) + "</ul>")
        if c["gainers"]:
            parts.append("<h3>涨星</h3><ul>" + "".join(
                f"<li>{escape(g['full_name'])} +{g['delta']:,}</li>" for g in c["gainers"]) + "</ul>")
    if c["trends_plain"]:
        parts.append("<h3>编者按</h3><ul>" + "".join(f"<li>{escape(t)}</li>" for t in c["trends_plain"]) + "</ul>")
    parts.append(f'<p><a href="{escape(url)}">阅读完整一期 →</a></p>')
    return "".join(parts)


def _write_feed(cfg, issues):
    """Atom 订阅源：只收正式期，最新 20 期。"""
    base = cfg.get("site_url", "").rstrip("/") + "/"
    A = "http://www.w3.org/2005/Atom"
    ET.register_namespace("", A)
    feed = ET.Element(f"{{{A}}}feed")
    ET.SubElement(feed, f"{{{A}}}title").text = "GitHub AI 热门项目周报"
    ET.SubElement(feed, f"{{{A}}}subtitle").text = "每周一期：近 90 天新建、星数超过门槛的 AI 项目，先报本期变化"
    ET.SubElement(feed, f"{{{A}}}link", href=base)
    ET.SubElement(feed, f"{{{A}}}link", rel="self", href=base + "feed.xml")
    ET.SubElement(feed, f"{{{A}}}id").text = base
    last = issues[-1]["s"]["date"] if issues else dt.date.today().isoformat()
    ET.SubElement(feed, f"{{{A}}}updated").text = f"{last}T01:00:00Z"
    ET.SubElement(ET.SubElement(feed, f"{{{A}}}author"), f"{{{A}}}name").text = "AI Trending Radar"
    for c in reversed(issues[-20:]):
        url = f"{base}archive/{c['s']['date']}.html"
        e = ET.SubElement(feed, f"{{{A}}}entry")
        ET.SubElement(e, f"{{{A}}}title").text = title_of(c)
        ET.SubElement(e, f"{{{A}}}link", href=url)
        ET.SubElement(e, f"{{{A}}}id").text = url
        ET.SubElement(e, f"{{{A}}}updated").text = f"{c['s']['date']}T01:00:00Z"
        ET.SubElement(e, f"{{{A}}}content", type="html").text = _summary_html(c, url)
    ET.ElementTree(feed).write(SITE / "feed.xml", encoding="utf-8", xml_declaration=True)


def _markdown(c):
    s = c["s"]
    out = [f"# GitHub AI 热门项目周报 · {title_of(c)}", "",
           f"- 收录：{c['win']} 创建、Stars > {s['min_stars']:,} 的 AI 项目，共 {len(c['ranked'])} 个", ""]
    out.append("## 本期变化")
    if not c["prev"]:
        out.append("创刊号，暂无对比。")
    else:
        out.append(f"较第 {c['prev']['no']} 期（{c['prev']['date']}，{c['prev']['days']} 天）：")
        out.append("- 新上榜：" + ("、".join(e["full_name"] for e in c["new"]) or "无"))
        out.append("- 移出：" + ("；".join(f"{x['full_name']}（{x['reason']}）" for x in c["dropped"]) or "无"))
        out.append("- 涨星：" + ("、".join(f"{g['full_name']} +{g['delta']:,}" for g in c["gainers"]) or "无"))
    if c["trends_plain"]:
        out += ["", "## 编者按"] + [f"- {b}" for b in c["trends_plain"]]
    out += ["", "## 名录"]
    for cat, es in c["groups"]:
        out += ["", f"### {cat}"]
        if cat in c["warn"]:
            out += ["", f"> ⚠️ {c['warn'][cat]}"]
        for e in es:
            v = e["v"]
            out += ["", f"#### [{e['full_name']}]({e['html_url']}) ⭐ {e['stars']:,}", "", f"> {v['tagline']}", ""]
            if v["positioning"]:
                out.append(f"- **定位**：{v['positioning']}")
            for label, key in (("能做什么", "features"), ("亮点", "highlights")):
                if v[key]:
                    out.append(f"- **{label}**：")
                    out += [f"  - {x}" for x in v[key]]
            if v["audience"]:
                out.append(f"- **适合**：{v['audience']}")
            if v["cmd"] or v["note"]:
                out.append("- **上手**：" + (f"`{v['cmd']}` " if v["cmd"] else "") + v["note"])
            for r in e["notes"]:
                out.append(f"- ⚠️ {r}")
    if s["excluded"]:
        out += ["", "## 已排除（判定与 AI 无关）"] + [f"- {x['full_name']}：{x['reason']}" for x in s["excluded"]]
    return "\n".join(out) + "\n"
