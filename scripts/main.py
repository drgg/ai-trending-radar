"""每周流水线：fetch → summarize → diff → render。

用法：
  python scripts/main.py            正式运行（需要 ANTHROPIC_API_KEY）
  python scripts/main.py --dry-run  不调用模型，用占位介绍验证流程
  python scripts/main.py --limit 3  只处理星数最高的前 N 个（调试用）
"""
import argparse
import json
import sys
from datetime import date
from pathlib import Path

import yaml

import diff
import fetch
import render
from summarize import Summarizer

ROOT = Path(__file__).resolve().parent.parent


def risk_flags(repo, cfg, today):
    r = cfg["risk"]
    flags = []
    if repo["stars"] and repo["forks"] / repo["stars"] < r["min_fork_ratio"]:
        flags.append(f"fork/star 比例异常（{repo['forks']}/{repo['stars']}），热度可能有水分")
    if repo["license"] in (None, "NOASSERTION"):
        flags.append("许可证未声明或非标准，商用前请确认授权")
    idle = (today - date.fromisoformat(repo["pushed_at"])).days
    if idle > r["stale_days"]:
        flags.append(f"已 {idle} 天未更新")
    return flags


def main():
    sys.stdout.reconfigure(encoding="utf-8")  # Windows 控制台默认 GBK
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int)
    args = ap.parse_args()

    cfg = yaml.safe_load((ROOT / "config.yml").read_text(encoding="utf-8"))
    today = date.today()

    print("① 抓取候选仓库…")
    query, repos = fetch.fetch_all(cfg, today)
    if args.limit:
        repos = repos[:args.limit]
    print(f"   {len(repos)} 个候选")

    print("② 生成介绍…")
    summ = Summarizer(cfg, dry_run=args.dry_run)
    entries, excluded = [], []
    for repo in repos:
        intro = summ.intro(repo, today)
        repo.pop("readme", None)
        if not intro["is_ai_product"]:
            excluded.append({"full_name": repo["full_name"], "html_url": repo["html_url"],
                             "stars": repo["stars"], "reason": intro["positioning"]})
            continue
        entries.append({**repo, "intro": intro, "flags": risk_flags(repo, cfg, today), "delta": None})
    print(f"   上榜 {len(entries)}，排除 {len(excluded)}，模型调用 {summ.calls} 次")

    print("③ 对比上一期…")
    changes = diff.compute(entries, diff.previous_snapshot(today.isoformat()), cfg["top_gainers"])
    trends = summ.trends(entries)

    snapshot = {"date": today.isoformat(), "query": query, "window_days": cfg["window_days"],
                "min_stars": cfg["min_stars"], "model": cfg["model"], "dry_run": args.dry_run,
                "entries": entries, "excluded": excluded, "diff": changes, "trends": trends}
    diff.SNAP_DIR.mkdir(parents=True, exist_ok=True)
    (diff.SNAP_DIR / f"{today.isoformat()}.json").write_text(
        json.dumps(snapshot, ensure_ascii=False, indent=1), encoding="utf-8")

    print("④ 渲染页面…")
    render.render(snapshot, cfg["categories"])
    print(f"完成：site/index.html、report.md（本次模型调用共 {summ.calls} 次）")


if __name__ == "__main__":
    main()
