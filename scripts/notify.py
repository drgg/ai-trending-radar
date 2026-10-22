"""为最新的正式期写一份 GitHub Issue 通知：build/notify/{key,title}.txt 和 body.md。

只写文件，不调 GitHub API。发不发、会不会重复由工作流判断：
已有标题以 key（「第 N 期 · 日期」）开头的 Issue 就跳过，所以重跑同一期不会重复通知。
@ 提到仓库主人，确保 GitHub 发邮件 / App 通知（NOTIFY_MENTION，工作流里传 github.repository_owner）。
"""
import os
from pathlib import Path

from render import title_of

OUT = Path(__file__).resolve().parent.parent / "build" / "notify"


def write(ctx, cfg):
    if ctx is None:
        return None
    OUT.mkdir(parents=True, exist_ok=True)
    s, site = ctx["s"], cfg.get("site_url", "").rstrip("/")
    page = f"{site}/archive/{s['date']}.html"
    mention = os.environ.get("NOTIFY_MENTION", "").strip()
    lines = [f"{'@' + mention + ' ' if mention else ''}第 {ctx['no']} 期已发布：[网页版]({site}/) · [本期存档]({page}) · [RSS]({site}/feed.xml)", ""]
    if ctx.get("outlook_plain") or ctx["trends_plain"]:
        lines += ["### 近期趋势"] + ([ctx["outlook_plain"]] if ctx.get("outlook_plain") else []) + [f"- {t}" for t in ctx["trends_plain"]] + [""]
    if not ctx["prev"]:
        lines.append(f"创刊号，共收录 {len(ctx['ranked'])} 个项目。")
    else:
        p = ctx["prev"]
        lines.append(f"较第 {p['no']} 期（{p['date']}，{p['days']} 天），本期共 {len(ctx['ranked'])} 个项目。")
        lines += ["", f"### 新上榜 {len(ctx['new'])}"]
        lines += [f"- **[{e['full_name']}]({e['html_url']})** ★ {e['stars']:,}　{e['v']['tagline']}"
                  for e in ctx["new"]] or ["本期没有新上榜的项目。"]
        lines += ["", f"### 移出 {len(ctx['dropped'])}"]
        lines += [f"- {x['full_name']}：{x['reason']}" for x in ctx["dropped"]] or ["本期没有项目移出。"]
        lines += ["", f"### 涨星（{p['days']} 天）"]
        lines += [f"- {g['full_name']} **+{g['delta']:,}**（现 {g['stars']:,}）" for g in ctx["gainers"]] or ["无"]
    R = ctx.get("rising")
    if R:
        st = "，".join(f"{k} 的 {v} 个" for k, v in R["surge_stats"])
        lines += ["", f"### 升星榜（近 7 天 {R['last7']}）", f"近 7 天涨星 {st}；{R['surge_accel']} 个在加速，"
                  f"{R['surge_older']} 个创建已超过 {R['window_days']} 天。前 10："]
        top = [x for _, _, items in R["surge_groups"] for x in items][:10]
        lines += [f"- **[{x['full_name']}]({x['html_url']})** +{x['last7']:,}（前 7 天 +{x['prev7']:,}）"
                  f"{' 🔺加速' if x['accel'] else ''}　{x['tagline']}" for x in top]
        nb = [x for _, items in R["newborn_groups"] for x in items]
        lines += ["", f"### 新星（创建于 {R['newborn_range']}，≥{R['rc']['newborn_min']}★）"]
        lines += [f"- **[{x['full_name']}]({x['html_url']})** ★ {x['stars']:,}　{x['tagline']}" for x in nb] or ["本期没有。"]
        if R["young_featured"]:
            lines += ["", f"### 新锐（创建于 {R['young_range']}，≥{R['rc']['young_intro_min']:,}★）",
                      "、".join(f"[{x['full_name']}]({x['html_url']}) ★{x['stars']:,}" for x in R["young_featured"])]
    lines += ["", "---", "这条 Issue 由每周自动运行创建；新一期发布时会自动关闭。"]
    key = f"第 {ctx['no']} 期 · {s['date']}"
    (OUT / "key.txt").write_text(key, encoding="utf-8")
    (OUT / "title.txt").write_text(title_of(ctx), encoding="utf-8")
    (OUT / "body.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return key
