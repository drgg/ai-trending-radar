"""把快照渲染成 HTML 网页（本期 + 存档）和 Markdown 报告。"""
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
ARCHIVE = SITE / "archive"


def _group(snapshot, categories):
    groups = {c: [] for c in categories}
    for e in snapshot["entries"]:
        groups.setdefault(e["intro"]["category"], []).append(e)
    return [(c, es) for c, es in groups.items() if es]


def render(snapshot, categories):
    env = Environment(loader=FileSystemLoader(ROOT / "templates"),
                      autoescape=select_autoescape(["html", "j2"]))
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    groups = _group(snapshot, categories)
    ctx = dict(s=snapshot, groups=groups)

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
            i = e["intro"]
            out += ["", f"### [{e['full_name']}]({e['html_url']}) ⭐ {e['stars']:,}"]
            for label, key in (("定位", "positioning"), ("能做什么", "features"), ("亮点", "highlights"),
                               ("适合", "audience"), ("上手", "quickstart")):
                if i.get(key):
                    out.append(f"- **{label}**：{i[key]}")
            for r in i.get("risks", []) + e["flags"]:
                out.append(f"- ⚠️ {r}")
    if s["excluded"]:
        out += ["", "## 已排除（判定与 AI 无关）"] + [f"- {x['full_name']}：{x['reason']}" for x in s["excluded"]]
    return "\n".join(out) + "\n"
