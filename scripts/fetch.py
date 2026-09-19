"""从 GitHub Search API 获取候选仓库，并补充 README 摘录。"""
import base64
import os
import re
import subprocess
import time
from datetime import date, timedelta

import requests

API = "https://api.github.com"
_SKIP_LINE = re.compile(r"^\s*(<|</|!\[|\[!\[|&nbsp)")


def _token():
    tok = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if tok:
        return tok
    try:  # 本地运行时借用 gh CLI 的登录态
        return subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def _session():
    s = requests.Session()
    s.headers["Accept"] = "application/vnd.github+json"
    s.headers["X-GitHub-Api-Version"] = "2022-11-28"
    tok = _token()
    if tok:
        s.headers["Authorization"] = f"Bearer {tok}"
    return s


def _get(s, url, **kw):
    for attempt in range(4):
        r = s.get(url, timeout=30, **kw)
        if r.status_code in (403, 429) and "rate limit" in r.text.lower():
            reset = int(r.headers.get("X-RateLimit-Reset", time.time() + 60))
            time.sleep(max(5, min(reset - time.time() + 2, 120)))
            continue
        return r
    r.raise_for_status()
    return r


def search(cfg, today):
    since = (today - timedelta(days=cfg["window_days"])).isoformat()
    q = f"{' OR '.join(cfg['keywords'])} created:>={since} stars:>{cfg['min_stars']}"
    s = _session()
    items = []
    for page in range(1, 11):  # Search API 上限 1000 条
        r = _get(s, f"{API}/search/repositories",
                 params={"q": q, "sort": "stars", "order": "desc", "per_page": 100, "page": page})
        r.raise_for_status()
        batch = r.json()["items"]
        items.extend(batch)
        if len(batch) < 100:
            break
    return q, [_slim(it) for it in items], s


def _slim(it):
    return {
        "full_name": it["full_name"],
        "html_url": it["html_url"],
        "description": it.get("description") or "",
        "stars": it["stargazers_count"],
        "forks": it["forks_count"],
        "language": it.get("language"),
        "license": (it.get("license") or {}).get("spdx_id"),
        "topics": it.get("topics") or [],
        "homepage": it.get("homepage") or "",
        "created_at": it["created_at"][:10],
        "pushed_at": it["pushed_at"][:10],
    }


def clean_readme(text, max_chars):
    lines = [ln.rstrip() for ln in text.splitlines()]
    kept = [ln for ln in lines if ln.strip() and not _SKIP_LINE.match(ln)]
    return "\n".join(kept)[:max_chars]


def add_readme(s, repo, max_chars):
    r = _get(s, f"{API}/repos/{repo['full_name']}/readme")
    if r.status_code != 200:
        repo["readme_sha"], repo["readme"] = None, ""
        return repo
    data = r.json()
    raw = base64.b64decode(data.get("content", "")).decode("utf-8", errors="replace")
    repo["readme_sha"] = data.get("sha")
    repo["readme"] = clean_readme(raw, max_chars)
    return repo


def fetch_all(cfg, today=None):
    today = today or date.today()
    q, repos, s = search(cfg, today)
    for repo in repos:
        add_readme(s, repo, cfg["readme_max_chars"])
    return q, repos
