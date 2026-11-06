"""主榜项目的维护信号：近 30 天提交数、提交作者数、未关闭的 issue 与 PR、项目自设的社交预览图。

用 GraphQL 一次批量查（每批 20 个仓库），不占 REST 配额，短期榜那边的约 900 次 REST 请求不受影响。
结果写到 data/activity/<快照日期>.json，带采集日期；价值分析页（scripts/analysis.py）读它。
失败不影响出刊：分析页会退回只用最后推送日期判断维护情况。

单独补采某一期：python scripts/activity.py 2026-11-02
"""
import datetime as dt
import json
import sys
from pathlib import Path

import fetch

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "activity"
GQL = "https://api.github.com/graphql"
FIELDS = """
  stargazerCount forkCount pushedAt usesCustomOpenGraphImage openGraphImageUrl
  issues(states: OPEN) { totalCount } pullRequests(states: OPEN) { totalCount }
  defaultBranchRef { target { ... on Commit { history(since: $since, first: 100) { totalCount nodes { author { user { login } email } } } } } }
"""


def _query(s, names, since):
    parts = []
    for i, n in enumerate(names):
        owner, name = n.split("/")
        parts.append(f'r{i}: repository(owner: {json.dumps(owner)}, name: {json.dumps(name)}) {{{FIELDS}}}')
    q = "query($since: GitTimestamp!) {" + "\n".join(parts) + "}"
    r = s.post(GQL, json={"query": q, "variables": {"since": since}}, timeout=60)
    r.raise_for_status()
    body = r.json()
    data = body.get("data") or {}
    out = {}
    for i, n in enumerate(names):
        x = data.get(f"r{i}")
        if not x:
            continue
        h = ((x.get("defaultBranchRef") or {}).get("target") or {}).get("history") or {}
        authors = {(nd["author"].get("user") or {}).get("login") or nd["author"].get("email") for nd in h.get("nodes", []) if nd.get("author")}
        out[n] = {
            "stars": x["stargazerCount"], "forks": x["forkCount"], "pushed_at": (x.get("pushedAt") or "")[:10],
            "commits30": h.get("totalCount", 0), "authors30": len(authors - {None}),
            "open_issues": x["issues"]["totalCount"], "open_prs": x["pullRequests"]["totalCount"],
            "og_image": x["openGraphImageUrl"] if x.get("usesCustomOpenGraphImage") else None,
        }
    return out


def collect(names, today=None, batch=20):
    today = today or dt.date.today()
    since = (today - dt.timedelta(days=30)).isoformat() + "T00:00:00Z"
    s = fetch._session()
    repos = {}
    for i in range(0, len(names), batch):
        repos.update(_query(s, names[i:i + batch], since))
    return {"collected_at": today.isoformat(), "since": since[:10], "repos": repos}


def save(snapshot_date, data):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{snapshot_date}.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")


def load(snapshot_date):
    p = OUT / f"{snapshot_date}.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    date = sys.argv[1]
    snap = json.loads((ROOT / "data" / "snapshots" / f"{date}.json").read_text(encoding="utf-8"))
    data = collect([e["full_name"] for e in snap["entries"]])
    save(date, data)
    print(f"写入 data/activity/{date}.json：{len(data['repos'])}/{len(snap['entries'])} 个仓库，采集于 {data['collected_at']}")
