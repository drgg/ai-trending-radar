"""把快照渲染成 HTML 网页（本期 + 存档）和 Markdown 报告。"""
import re
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
ARCHIVE = SITE / "archive"

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


def render(snapshot, categories):
    env = Environment(loader=FileSystemLoader(ROOT / "templates"),
                      autoescape=select_autoescape(["html", "j2"]))
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    ranked, groups = _prepare(snapshot, categories)
    ctx = dict(s=snapshot, groups=groups, ranked=ranked, new=set(snapshot["diff"]["new"]))

    tpl = env.get_template("index.html.j2")
    (ARCHIVE / f"{snapshot['date']}.html").write_text(tpl.render(**ctx, base="../", is_archive=True),
                                                      encoding="utf-8")
    archives = sorted((p.stem for p in ARCHIVE.glob("????-??-??.html")), reverse=True)
    (SITE / "index.html").write_text(tpl.render(**ctx, base="", is_archive=False, archives=archives),
                                     encoding="utf-8")
    (ROOT / "report.md").write_text(_markdown(snapshot, groups), encoding="utf-8")


def _markdown(s, groups):
    d = s["diff"]
    out = [f"# GitHub 近 {s['window_days']} 天 AI 热门项目（Stars > {s['min_stars']}）", "",
           f"- 数据快照：{s['date']}　共 {len(s['entries'])} 个项目", ""]
    out.append("## 本期变化")
    if d["first"]:
        out.append("首期，暂无对比。")
    else:
        out.append(f"对比 {d['prev_date']}：")
        out.append("- 新上榜：" + ("、".join(d["new"]) or "无"))
        out.append("- 移出：" + ("、".join(x["full_name"] for x in d["dropped"]) or "无"))
        out.append("- 涨幅榜：" + ("、".join(f"{g['full_name']} +{g['delta']}" for g in d["gainers"]) or "无"))
    if s["trends"]:
        out += ["", "## 趋势小结"] + [f"- {b}" for b in s["trends"]]
    for cat, es in groups:
        out += ["", f"## {cat}"]
        for e in es:
            v = e["v"]
            out += ["", f"### [{e['full_name']}]({e['html_url']}) ⭐ {e['stars']:,}", "", f"> {v['tagline']}", ""]
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
            for r in v["risks"] + e["flags"]:
                out.append(f"- ⚠️ {r}")
    if s["excluded"]:
        out += ["", "## 已排除（判定与 AI 无关）"] + [f"- {x['full_name']}：{x['reason']}" for x in s["excluded"]]
    return "\n".join(out) + "\n"
