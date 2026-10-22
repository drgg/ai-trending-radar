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
HEADING_GLYPHS = "".join(sorted(set("第期创刊号临时更新本期变化编者按名录往期升星榜新锐与近趋势0123456789· ")))

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


def _link_targets(ranked, rising):
    """趋势里点名的项目短名 → 链接。主榜跳名录；升星 / 新星 / 新锐写了介绍的跳各自那一行；只列名字的跳 GitHub。"""
    out = {}
    for e in ranked:
        out.setdefault(e["full_name"].split("/")[1], "#" + e["full_name"])
    if rising:
        for key, pre in (("surge", "s"), ("newborn", "n"), ("young", "y")):
            for x in rising[key]:
                if x.get("featured"):
                    out.setdefault(x["full_name"].split("/")[1], f"#{pre}-{x['full_name']}")
        for key in ("surge", "newborn", "young"):
            for x in rising[key]:
                out.setdefault(x["full_name"].split("/")[1], x["html_url"])
    return out


def _link_names(text, targets):
    """短名 → 链接，每个只链第一次出现。长名先匹配，免得被短名截走。
    边界只看 ASCII：Python 的 \\w 也匹配汉字，「VoiceStudio单周」这种紧挨汉字的写法会匹配不上。"""
    out = str(escape(text))
    for short in sorted(targets, key=len, reverse=True):
        out = re.sub(rf"(?<![A-Za-z0-9_/#.-]){re.escape(short)}(?![A-Za-z0-9_-])",
                     f'<a href="{escape(targets[short])}">{escape(short)}</a>', out, count=1)
    return Markup(out)


def rising_view(r, cfg):
    """短期榜整理成模板直接用的结构；早期快照没有 rising 字段时返回 None。"""
    if not r:
        return None
    rc, st = cfg["rising"], r["stats"]
    md = lambda s: s[5:]  # noqa: E731  "2026-10-16" → "10-16"
    w = r["window"]
    surge_f = [x for x in r["surge"] if x["featured"]]
    tiers = [("暴涨", f"近 7 天 ≥{rc['surge_boom']:,}"), ("猛涨", f"近 7 天 {rc['surge_intro_min']:,}–{rc['surge_boom'] - 1:,}")]
    nb = r["newborn"]
    nb_tiers = sorted(rc["newborn_tiers"], reverse=True)
    nb_groups = []
    for i, t in enumerate(nb_tiers):
        hi = nb_tiers[i - 1] if i else None
        items = [x for x in nb if x["stars"] >= t and (hi is None or x["stars"] < hi)]
        if items:
            nb_groups.append((f"≥{t:,}★" if hi is None else f"{t:,}–{hi - 1:,}★", items))
    return {
        "last7": f"{md(w['last7'][0])} 至 {md(w['last7'][1])}", "prev7": f"{md(w['prev7'][0])} 至 {md(w['prev7'][1])}",
        "surge_groups": [(name, note, [x for x in surge_f if x["tier"] == name]) for name, note in tiers],
        "surge_rest": [x for x in r["surge"] if not x["featured"]],
        "surge_stats": [("≥" + f"{int(k[1:]):,}", v) for k, v in st["surge"].items()], "surge_accel": st["surge_accel"], "surge_in_main": st["surge_in_main"],
        "surge_older": st["surge_older_than_main"], "pool": st["pool"],
        "surge_n": len(r["surge"]), "surge_featured_n": len(surge_f),
        "newborn_groups": nb_groups, "newborn_n": len(nb), "newborn_stats": st["newborn"],
        "young_featured": [x for x in r["young"] if x["featured"]],
        "young_rest": [x for x in r["young"] if not x["featured"]],
        "young_n": len(r["young"]),
        "suspects": r["suspects"], "spam_owners": st["spam_owners"], "excluded": r.get("excluded", []),
        "rc": rc, "window_days": cfg["window_days"], "main_min": cfg["min_stars"],
        "newborn_range": f"{md(w['last7'][0])} 至 {md(w['last7'][1])}",
        "young_range": "{} 至 {}".format(*(
            (dt.date.fromisoformat(w["last7"][1]) - dt.timedelta(days=n)).isoformat()[5:] for n in (29, 7))),
    }


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
    links = _link_targets(ranked, snap.get("rising"))

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
        trends=[_link_names(t, links) for t in snap["trends"]],
        trends_plain=snap["trends"],
        outlook=_link_names(snap["outlook"], links) if snap.get("outlook") else "",
        outlook_plain=snap.get("outlook", ""),
        noted=sum(1 for e in ranked if e["notes"]),
        warn=cfg.get("warn_categories") or {},
        rising=rising_view(snap.get("rising"), cfg),
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
    """RSS 条目正文：近期趋势 + 本期变化 + 短期榜，阅读器里不点开也能看个大概。"""
    parts = []
    if c["outlook_plain"]:
        parts.append(f"<h3>近期趋势</h3><p>{escape(c['outlook_plain'])}</p>")
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
    R = c.get("rising")
    if R:
        top = [x for _, _, items in R["surge_groups"] for x in items][:5]
        parts.append(f"<h3>升星榜（近 7 天 {escape(R['last7'])}）</h3><ul>" + "".join(
            f"<li>{escape(x['full_name'])} +{x['last7']:,}{'（加速）' if x['accel'] else ''} — {escape(x['tagline'])}</li>"
            for x in top) + "</ul>")
        nb = [x for _, items in R["newborn_groups"] for x in items]
        if nb:
            parts.append("<h3>新星</h3><ul>" + "".join(
                f"<li>{escape(x['full_name'])} ★ {x['stars']:,} — {escape(x['tagline'])}</li>" for x in nb) + "</ul>")
    if c["trends_plain"] and not c["outlook_plain"]:  # 早期快照只有要点
        parts.append("<h3>近期趋势</h3><ul>" + "".join(f"<li>{escape(t)}</li>" for t in c["trends_plain"]) + "</ul>")
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
    if c["outlook_plain"] or c["trends_plain"]:
        out += ["## 近期趋势", ""] + ([c["outlook_plain"], ""] if c["outlook_plain"] else []) + [f"- {b}" for b in c["trends_plain"]] + [""]
    out.append("## 本期变化")
    if not c["prev"]:
        out.append("创刊号，暂无对比。")
    else:
        out.append(f"较第 {c['prev']['no']} 期（{c['prev']['date']}，{c['prev']['days']} 天）：")
        out.append("- 新上榜：" + ("、".join(e["full_name"] for e in c["new"]) or "无"))
        out.append("- 移出：" + ("；".join(f"{x['full_name']}（{x['reason']}）" for x in c["dropped"]) or "无"))
        out.append("- 涨星：" + ("、".join(f"{g['full_name']} +{g['delta']:,}" for g in c["gainers"]) or "无"))
    R = c.get("rising")
    if R:
        st = "，".join(f"{k} 的 {v} 个" for k, v in R["surge_stats"])
        out += ["", f"## 升星榜（近 7 天 {R['last7']}，对比前 7 天 {R['prev7']}）", "",
                f"测了 {R['pool']:,} 个近一年创建的 AI 项目：近 7 天涨星 {st}；{R['surge_accel']} 个在加速，"
                f"{R['surge_older']} 个创建已超过 {R['window_days']} 天，{R['surge_in_main']} 个已在主榜。"]
        for name, note, items in R["surge_groups"]:
            if items:
                out += ["", f"### {name}（{note}）"] + [
                    f"- [{x['full_name']}]({x['html_url']}) **+{x['last7']:,}**（前 7 天 +{x['prev7']:,}，现 {x['stars']:,}★）"
                    f"{'　加速' if x['accel'] else ''}{'　主榜' if x['in_main'] else ''}：{x['tagline']}" for x in items]
        if R["surge_rest"]:
            out += ["", f"其余 {len(R['surge_rest'])} 个：" + "、".join(f"{x['full_name']} +{x['last7']:,}" for x in R["surge_rest"])]
        if R["suspects"]:
            out += ["", f"⚠️ 疑似刷星（同一作者 ≥{R['rc']['spam_same_owner']} 个项目同周各涨 ≥{R['rc']['spam_min_each']:,}），未列入："
                    + "、".join(f"{x['full_name']} +{x['last7']:,}" for x in R["suspects"])]
        out += ["", f"## 新星（创建于 {R['newborn_range']}，≥{R['rc']['newborn_min']}★）"]
        for label, items in R["newborn_groups"]:
            out += ["", f"**{label}**"] + [f"- [{x['full_name']}]({x['html_url']}) ★ {x['stars']:,}：{x['tagline']}" for x in items]
        if not R["newborn_groups"]:
            out.append("本期没有。")
        out += ["", f"## 新锐（创建于 {R['young_range']}，≥{R['rc']['young_list_min']:,}★）", ""]
        out += [f"- [{x['full_name']}]({x['html_url']}) ★ {x['stars']:,}：{x['tagline']}" for x in R["young_featured"]]
        if R["young_rest"]:
            out += ["", f"{R['rc']['young_list_min']:,}–{R['rc']['young_intro_min'] - 1:,}★ 的 {len(R['young_rest'])} 个："
                    + "、".join(f"{x['full_name']} ★{x['stars']:,}" for x in R["young_rest"])]
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
