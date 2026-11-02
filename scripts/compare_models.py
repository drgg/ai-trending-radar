"""以同一期元数据和原 README SHA 生成 DeepSeek 对照稿，不改正式快照或缓存。

DEEPSEEK_API_KEY 必须在环境中；示例：python scripts/compare_models.py --snapshot 2026-10-26
"""
import argparse
import base64
import copy
import html
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

import diff
import fetch
import render
from summarize import Summarizer, length_violations, PROMPT_VERSION

ROOT = Path(__file__).resolve().parent.parent


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--snapshot", required=True)
    ap.add_argument("--workers", type=int, default=4)
    args = ap.parse_args()
    date.fromisoformat(args.snapshot)
    cfg = yaml.safe_load((ROOT / "config.yml").read_text(encoding="utf-8"))
    if cfg["backend"] != "deepseek":
        raise SystemExit("对比脚本需要 backend: deepseek")
    source = json.loads((ROOT / "data/snapshots" / f"{args.snapshot}.json").read_text(encoding="utf-8"))
    out = ROOT / "build" / f"deepseek-comparison-{args.snapshot}"
    out.mkdir(parents=True, exist_ok=True)
    (out / "readmes").mkdir(exist_ok=True)
    (out / "intros").mkdir(exist_ok=True)

    def generate(entry):
        name = entry["full_name"]
        key = name.replace("/", "__")
        sha = entry["intro"].get("readme_sha")
        if not sha:
            raise RuntimeError(f"{name} 缺少原 README SHA，不能进行同输入对比")
        readme_path = out / "readmes" / f"{sha}.md"
        if not readme_path.exists():
            response = fetch._session().get(f"{fetch.API}/repos/{name}/git/blobs/{sha}", timeout=30)
            response.raise_for_status()
            raw = base64.b64decode(response.json()["content"]).decode("utf-8", errors="replace")
            readme_path.write_text(fetch.clean_readme(raw, cfg["readme_max_chars"]), encoding="utf-8")
        intro_path = out / "intros" / f"{key}.json"
        if intro_path.exists():
            record = json.loads(intro_path.read_text(encoding="utf-8"))
            if (record.get("model"), record.get("prompt_version"), record.get("readme_sha")) == (cfg["model"], PROMPT_VERSION, sha):
                return {**copy.deepcopy(entry), "intro": record}
        summ = Summarizer(cfg)
        repo = {**entry, "readme": readme_path.read_text(encoding="utf-8")}
        intro = summ.generate(repo)
        intro.update(model=cfg["model"], prompt_version=PROMPT_VERSION, readme_sha=sha,
                     generated_at=date.today().isoformat(), usage=summ.usage, calls=summ.calls,
                     length_violations=length_violations(intro))
        intro_path.write_text(json.dumps(intro, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"完成 {name}：{summ.calls} 次调用，超长字段 {len(intro['length_violations'])}", flush=True)
        return {**copy.deepcopy(entry), "intro": intro}

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        entries = list(executor.map(generate, source["entries"]))
    revised = copy.deepcopy(source)
    revised["entries"] = [e for e in entries if e["intro"]["is_ai_product"]]
    revised["model"] = cfg["model"]
    revised["comparison"] = {"source_date": source["date"], "generated_at": date.today().isoformat(),
                             "note": "同一期历史数据复刊；未抓取新星数。短期榜沿用原期，仅主榜介绍和趋势重写。"}
    history = [s for s in diff.load_all() if s["date"] < source["date"]]
    revised["diff"] = diff.compute(revised["entries"], diff.previous_issue(source["date"], history), cfg["top_gainers"])
    summ = Summarizer(cfg)
    revised["outlook"], revised["trends"] = summ.outlook(revised["entries"], revised["diff"],
        revised.get("rising"), [s for s in history if diff.is_issue(s)][-3:])
    if not revised["outlook"]:
        raise RuntimeError("趋势生成不合格，对比稿未完成")
    (out / "snapshot.json").write_text(json.dumps(revised, ensure_ascii=False, indent=2), encoding="utf-8")
    snaps = history + [revised]
    context = render.issue_context(revised, snaps, cfg)
    env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=select_autoescape(["html", "j2"]),
                      trim_blocks=True, lstrip_blocks=True)
    page = env.get_template("index.html.j2").render(**context, nav=[], latest_date=source["date"],
        site_url=cfg["site_url"], repo_url=cfg["repo_url"], built=date.today().isoformat(), root="../../site/")
    banner = '<aside style="padding:16px;background:#fff3cd;color:#332701;text-align:center">DeepSeek 本地对比稿 · 数据截至 ' + source["date"] + ' · 主榜及趋势重新生成，短期榜沿用原期</aside>'
    import re
    page = re.sub(r"(<body[^>]*>)", lambda m: m.group(0) + banner, page, count=1)
    (out / "issue.html").write_text(page, encoding="utf-8")
    rows = ["# Claude / DeepSeek 同期对比", "", f"数据日期：{source['date']}；生成日期：{date.today().isoformat()}。",
            "同一批主榜项目、同一份元数据、按原 SHA 取回 README，使用当前同一套提示词。",
            "未刷新 GitHub 星数；短期榜保留原文，不计入本次文案对比。", "",
            "## 趋势分析", "", "### 原稿", source.get("outlook", ""), "", "### DeepSeek", revised["outlook"], ""]
    sections = []
    for old, new in zip(source["entries"], entries):
        rows += [f"## {old['full_name']}", ""]
        columns = []
        for label, record in [("原稿", old["intro"]), ("DeepSeek", new["intro"])]:
            rows += [f"### {label}", "", "```json", json.dumps(record, ensure_ascii=False, indent=2), "```", ""]
            columns.append("<div><h3>" + label + "</h3><pre>" + html.escape(json.dumps(record, ensure_ascii=False, indent=2)) + "</pre></div>")
        sections.append("<section><h2>" + html.escape(old["full_name"]) + "</h2><article>" + "".join(columns) + "</article></section>")
    usage = {k: sum(e["intro"]["usage"].get(k, 0) for e in entries) + summ.usage[k] for k in summ.usage}
    summary = {"projects": len(entries), "usage": usage,
               "category_changes": [e["full_name"] for old, e in zip(source["entries"], entries) if old["intro"]["category"] != e["intro"]["category"]],
               "excluded_by_deepseek": [e["full_name"] for e in entries if not e["intro"]["is_ai_product"]],
               "length_violations": {e["full_name"]: e["intro"]["length_violations"] for e in entries if e["intro"]["length_violations"]}}
    (out / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    rows += ["## 机械检查统计", "", "```json", json.dumps(summary, ensure_ascii=False, indent=2), "```", ""]
    (out / "comparison.md").write_text("\n".join(rows), encoding="utf-8")
    style = "body{font:16px/1.7 system-ui;max-width:1300px;margin:32px auto;padding:0 20px;color:#222}article{display:grid;grid-template-columns:1fr 1fr;gap:24px}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#f6f6f6;padding:16px;font:14px/1.65 system-ui}section{border-top:1px solid #ddd;margin-top:32px}@media(max-width:700px){article{grid-template-columns:1fr}}"
    intro_html = "<h1>Claude / DeepSeek 同期对比</h1><p>历史数据：" + source["date"] + "；主榜同元数据、同 README SHA。短期榜未重写。本稿未发布。</p><p><a href='issue.html'>打开 DeepSeek 复刊预览</a></p>"
    intro_html += f"<p>项目 {len(entries)} 个；分类变化 {len(summary['category_changes'])} 个；超长项目 {len(summary['length_violations'])} 个；总 token {usage['total_tokens']:,}。分类变化不代表分类更准确。</p>"
    trends_html = "<h2>趋势分析</h2><article><div><h3>原稿</h3><p>" + html.escape(source.get("outlook", "")) + "</p></div><div><h3>DeepSeek</h3><p>" + html.escape(revised["outlook"]) + "</p></div></article>"
    (out / "comparison.html").write_text('<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Claude / DeepSeek 同期对比</title><style>' + style + '</style><body>' + intro_html + trends_html + "".join(sections) + '</body></html>', encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False), flush=True)
    print(f"对比稿：{out / 'comparison.html'}", flush=True)


if __name__ == "__main__":
    main()
