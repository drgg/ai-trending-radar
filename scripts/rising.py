"""短期榜：新星（近 7 天创建）、新锐（8–30 天创建）、升星（近 7 天星数增量）。

时间窗口都按 UTC 完整自然日切，D = 运行当天（不完整，不计入）：
  近 7 天 = D-7 … D-1　　前 7 天 = D-14 … D-8
周一出刊时，近 7 天正好是上周一到周日；相邻两期的窗口首尾相接、互不重叠，
所以新星里每个项目只会出现一次，之后按年龄进新锐、再进主榜（主榜是 ≤90 天且 >5000★）。

星数增量来自 GET /repos/{o}/{r}/stargazers/history（按周、周内逐日计数）。
2026-06-30 起 stargazers 名单只对仓库管理员开放，逐颗数星的老办法已不可用。

Actions 里的 GITHUB_TOKEN 每小时只有 1000 次请求，候选池按两段取以控制在约 750 次：
  创建 ≤90 天 且 ≥1000★；创建 91–365 天 且 ≥5000★（2026-10-23 实测：近 7 天涨 ≥2000 的老项目 40 个只漏 1 个）
配额将尽时等到重置再继续，宁可慢也不失败。
"""
import datetime as dt
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

import fetch

API = fetch.API


class Client:
    """读 X-RateLimit-Remaining，余量见底就睡到重置；搜索接口另按 Retry-After 退避。"""

    def __init__(self):
        self.s = fetch._session()
        self.calls = 0

    def get(self, path, **params):
        for _ in range(6):
            r = self.s.get(f"{API}{path}", params=params, timeout=30)
            self.calls += 1
            if r.status_code in (403, 429) and ("rate limit" in r.text.lower() or "Retry-After" in r.headers):
                wait = int(r.headers.get("Retry-After") or max(5, int(r.headers.get("X-RateLimit-Reset", time.time() + 60)) - time.time() + 2))
                print(f"   配额用尽，等待 {wait}s")
                time.sleep(min(wait, 3700))
                continue
            left = int(r.headers.get("X-RateLimit-Remaining", 999))
            if left < 15 and r.headers.get("X-RateLimit-Resource") == "core":
                wait = max(5, int(r.headers["X-RateLimit-Reset"]) - time.time() + 2)
                print(f"   core 配额只剩 {left}，等待 {wait:.0f}s 到重置")
                time.sleep(min(wait, 3700))
            return r
        r.raise_for_status()
        return r


def _days(d0, d1):
    return [d0 + dt.timedelta(days=i) for i in range((d1 - d0).days + 1)]


def windows(today):
    return {"last7": (today - dt.timedelta(days=7), today - dt.timedelta(days=1)),
            "prev7": (today - dt.timedelta(days=14), today - dt.timedelta(days=8))}


def _search_all(cl, kw, d0, d1, stars):
    """created:d0..d1 的全部结果；超过 1000 条（搜索上限）就把日期区间对半拆开再查。"""
    q = f"{kw} created:{d0.isoformat()}..{d1.isoformat()} stars:{stars}"
    first = cl.get("/search/repositories", q=q, sort="stars", order="desc", per_page=100, page=1).json()
    if first.get("total_count", 0) > 1000 and d0 < d1:
        mid = d0 + (d1 - d0) / 2
        return _search_all(cl, kw, d0, mid, stars) + _search_all(cl, kw, mid + dt.timedelta(days=1), d1, stars)
    items, page = list(first.get("items", [])), 1
    while len(items) < first.get("total_count", 0) and page < 10:
        page += 1
        items += cl.get("/search/repositories", q=q, sort="stars", order="desc", per_page=100, page=page).json()["items"]
    return items


def _slim(it):
    return {"full_name": it["full_name"], "html_url": it["html_url"], "owner": it["full_name"].split("/")[0],
            "stars": it["stargazers_count"], "forks": it["forks_count"], "created_at": it["created_at"][:10],
            "description": it.get("description") or "", "topics": it.get("topics") or [],
            "language": it.get("language")}


def _history(cl, name, win):
    """近 7 天、前 7 天的新增星数；取 4 周足够覆盖两个窗口。"""
    r = cl.get(f"/repos/{name}/stargazers/history", per_page=4)
    if r.status_code != 200:
        return None
    daily = {}
    for w in r.json():
        start = dt.datetime.fromtimestamp(w["week"], tz=dt.timezone.utc).date()
        for i, n in enumerate(w["days"]):
            daily[start + dt.timedelta(days=i)] = n
    return {k: sum(daily.get(d, 0) for d in _days(*win[k])) for k in ("last7", "prev7")}


def _owner_scan(cl, owners, known, today, win, rc):
    """作者名下近一年创建、≥spam_min_each★、不在测速池里的仓库，补测增量（每人最多 8 个）。"""
    extra = []
    since = (today - dt.timedelta(days=365)).isoformat()
    for owner in sorted(owners):
        r = cl.get("/search/repositories", q=f"user:{owner} created:>={since} stars:>={rc['spam_min_each']}",
                   sort="stars", order="desc", per_page=8)
        for it in r.json().get("items", []) if r.status_code == 200 else []:
            if it["full_name"] in known:
                continue
            x = _slim(it)
            h = _history(cl, x["full_name"], win)
            if h:
                x.update(h)
                extra.append(x)
    return extra


def build(cfg, today, main_entries, summ):
    """采集 → 标注（一句话介绍 + 是否与 AI 相关）→ 定档。返回写进快照的 rising 字段。"""
    cl = Client()
    raw = _collect(cl, cfg, today, {e["full_name"] for e in main_entries})
    excluded = _annotate(cl, raw, cfg, summ, main_entries)
    out = _finalize(raw, cfg)
    out["excluded"] = excluded
    out["stats"]["api_calls"] = cl.calls
    return out


def _collect(cl, cfg, today, main_names):
    rc, kw = cfg["rising"], " OR ".join(cfg["keywords"])
    win = windows(today)
    d = lambda n: today - dt.timedelta(days=n)  # noqa: E731

    newborn = [_slim(x) for x in _search_all(cl, kw, d(7), d(1), f"{rc['newborn_min']}..{cfg['min_stars']}")]
    young = [_slim(x) for x in _search_all(cl, kw, d(30), d(8), f"{rc['young_list_min']}..{cfg['min_stars']}")]
    pool = {x["full_name"]: _slim(x) for x in
            _search_all(cl, kw, d(90), d(1), f">={rc['pool_recent_min']}")
            + _search_all(cl, kw, d(365), d(91), f">={rc['pool_old_min']}")}
    for x in newborn + young:
        pool.setdefault(x["full_name"], x)
    print(f"   短期榜候选：新星 {len(newborn)}，新锐 {len(young)}，测速池 {len(pool)}")

    with ThreadPoolExecutor(4) as ex:
        hist = dict(zip(pool, ex.map(lambda n: _history(cl, n, win), pool)))
    measured = 0
    for name, x in pool.items():
        h = hist.get(name)
        x["in_main"] = name in main_names
        x["age"] = (today - dt.date.fromisoformat(x["created_at"])).days
        if h:
            measured += 1
            # 创建不满 14 天的没有完整的「前 7 天」可比，不标加速
            x.update(h, accel=x["age"] > 14 and h["last7"] >= rc["surge_list_min"]
                     and (h["prev7"] == 0 or h["last7"] >= rc["accel_ratio"] * h["prev7"]))
    for x in newborn + young:  # 指向池里同一份（带增量）
        x.update(pool[x["full_name"]])

    # 刷星：同一作者有 ≥N 个项目同一周各涨 ≥500，整组不进榜。
    # 测速池只含 ≥5000★ 的老项目，作者名下星数低的仓库不在池里会漏判（2026-10-23 实测漏了一个 6 仓库同涨的作者），
    # 所以对每个可能写介绍的项目，再按作者把他近一年的仓库补测一遍。
    featured_owners = {x["owner"] for x in newborn}
    featured_owners |= {x["owner"] for x in young if x["stars"] >= rc["young_intro_min"]}
    featured_owners |= {x["owner"] for x in sorted(pool.values(), key=lambda x: -x.get("last7", 0))
                        [:rc["surge_intro_max"] + 10]}
    extra = _owner_scan(cl, featured_owners, set(pool), today, win, rc)
    hot = Counter(x["owner"] for x in list(pool.values()) + extra if x.get("last7", 0) >= rc["spam_min_each"])
    spam_owners = {o for o, n in hot.items() if n >= rc["spam_same_owner"]}
    suspects = sorted((x for x in list(pool.values()) + extra
                       if x["owner"] in spam_owners and x.get("last7", 0) >= rc["spam_min_each"]),
                      key=lambda x: -x["last7"])

    def clean(xs):
        return [x for x in xs if x["owner"] not in spam_owners]

    return {"window": {k: [a.isoformat(), b.isoformat()] for k, (a, b) in win.items()},
            "pool": len(pool), "measured": measured, "spam_owners": sorted(spam_owners), "suspects": suspects,
            "surge": sorted((x for x in clean(pool.values()) if x.get("last7", 0) >= rc["surge_list_min"]),
                            key=lambda x: -x["last7"]),
            "newborn": sorted(clean(newborn), key=lambda x: -x["stars"]),
            "young": sorted(clean(young), key=lambda x: -x["stars"])}


def _annotate(cl, raw, cfg, summ, main_entries):
    """给所有上榜项目批量写一句话定位，顺带剔除与 AI 无关的（关键词搜索的噪音）。
    主榜里已有完整介绍的直接复用其 tagline；可能写介绍的项目补读 README 摘录，其余只看描述和 topics。"""
    from render import view
    rc = cfg["rising"]
    main_tag = {e["full_name"]: view(e["intro"])["tagline"] for e in main_entries}
    listed = {x["full_name"]: x for k in ("newborn", "young", "surge") for x in raw[k]}
    likely = set(x["full_name"] for x in raw["newborn"])
    likely |= {x["full_name"] for x in raw["young"] if x["stars"] >= rc["young_intro_min"]}
    likely |= {x["full_name"] for x in [x for x in raw["surge"] if x["last7"] >= rc["surge_intro_min"]][:rc["surge_intro_max"] + 10]}
    todo = [x for n, x in listed.items() if n not in main_tag]
    for x in todo:
        if x["full_name"] in likely and not summ.has_tagline(x["full_name"]):
            fetch.add_readme(cl.s, x, 1500)
    tags = summ.taglines(todo)
    excluded = []
    # 同一项目在几个榜里可能是不同的对象，每个都要写上
    for x in (x for k in ("newborn", "young", "surge") for x in raw[k]):
        n = x["full_name"]
        t = {"tagline": main_tag[n], "is_ai_product": True} if n in main_tag else tags.get(n)
        x.pop("readme", None), x.pop("readme_sha", None), x.pop("topics", None)
        x["tagline"] = (t or {}).get("tagline") or x["description"]
        if t and not t["is_ai_product"] and n not in {e["full_name"] for e in excluded}:
            excluded.append({"full_name": n, "html_url": x["html_url"], "tagline": x["tagline"]})
    gone = {e["full_name"] for e in excluded}
    for k in ("newborn", "young", "surge"):
        raw[k] = [x for x in raw[k] if x["full_name"] not in gone]
    return excluded


def _finalize(raw, cfg):
    rc = cfg["rising"]
    # 同一项目可能同时在新锐和升星里：各榜各自一份，免得一个榜的「是否介绍」覆盖另一个榜
    surge, newborn, young = ([dict(x) for x in raw[k]] for k in ("surge", "newborn", "young"))
    suspects = raw["suspects"]
    spam_owners = raw["spam_owners"]
    intro_surge = {x["full_name"] for x in [x for x in surge if x["last7"] >= rc["surge_intro_min"]][:rc["surge_intro_max"]]}
    for x in newborn:
        x["featured"] = True
    for x in young:
        x["featured"] = x["stars"] >= rc["young_intro_min"]
    for x in surge:
        x["featured"] = x["full_name"] in intro_surge
        x["tier"] = "暴涨" if x["last7"] >= rc["surge_boom"] else "猛涨" if x["last7"] >= rc["surge_intro_min"] else "上涨"

    stats = {
        "pool": raw["pool"], "measured": raw["measured"],
        "newborn": {f"≥{t}": sum(1 for x in newborn if x["stars"] >= t) for t in rc["newborn_tiers"]},
        "young": {f"{rc['young_list_min']}–{rc['young_intro_min'] - 1}": sum(1 for x in young if x["stars"] < rc["young_intro_min"]),
                  f"≥{rc['young_intro_min']}": sum(1 for x in young if x["stars"] >= rc["young_intro_min"])},
        "surge": {f"≥{t}": sum(1 for x in surge if x["last7"] >= t)
                  for t in (rc["surge_list_min"], rc["surge_intro_min"], rc["surge_boom"])},
        "surge_accel": sum(1 for x in surge if x["accel"]),
        "surge_in_main": sum(1 for x in surge if x["in_main"]),
        "surge_older_than_main": sum(1 for x in surge if x["age"] > cfg["window_days"]),
        "spam_owners": spam_owners,
    }
    print(f"   升星：≥{rc['surge_list_min']} 共 {len(surge)}，介绍 {len(intro_surge)}；"
          f"新星 {len(newborn)}；新锐 {len(young)}；疑似刷星 {len(suspects)}（作者 {len(spam_owners)}）")
    return {"window": raw["window"], "newborn": newborn, "young": young, "surge": surge,
            "suspects": [{k: x.get(k) for k in ("full_name", "html_url", "stars", "last7", "prev7", "created_at")}
                         for x in suspects],
            "stats": stats}
