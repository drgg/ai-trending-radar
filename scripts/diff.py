"""与上一期快照对比，生成变化摘要。

「正式期」和「临时更新」：
- 正式期 = 每周一的定时运行（或手动运行时显式加 --issue）。只有正式期编期号、推送通知、进 RSS。
- 临时更新 = 其他手动运行（例如升级提示词后重新生成介绍）。照常写快照和页面，但不编期号。
- 无论哪种，都只和**上一个正式期**比较，所以正式期之间永远是周对周，
  临时更新插在中间也不会把下一期的对比基准缩成两三天（2026-09-30 那次就是这样出错的）。
"""
import json
from datetime import date
from pathlib import Path

SNAP_DIR = Path(__file__).resolve().parent.parent / "data" / "snapshots"


def is_issue(snap):
    """快照里有 issue 字段就以它为准；早期快照没有，按「周一 = 定时运行」推断。"""
    if "issue" in snap:
        return bool(snap["issue"])
    return date.fromisoformat(snap["date"]).weekday() == 0


def load_all():
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(SNAP_DIR.glob("????-??-??.json"))]


def previous_issue(today_str, snaps=None):
    """日期早于 today_str 的最近一个正式期；没有则 None。"""
    snaps = load_all() if snaps is None else snaps
    earlier = [s for s in snaps if s["date"] < today_str and is_issue(s)]
    return earlier[-1] if earlier else None


def compute(entries, prev, top_n):
    if prev is None:
        return {"first": True, "prev_date": None, "new": [], "dropped": [], "gainers": []}
    old = {e["full_name"]: e for e in prev["entries"]}
    cur = {e["full_name"]: e for e in entries}
    for e in entries:
        e["delta"] = e["stars"] - old[e["full_name"]]["stars"] if e["full_name"] in old else None
    gainers = sorted((e for e in entries if e["delta"]), key=lambda e: e["delta"], reverse=True)
    return {
        "first": False,
        "prev_date": prev["date"],
        "new": [e["full_name"] for e in entries if e["full_name"] not in old],
        "dropped": [{"full_name": n, "stars": o["stars"], "created_at": o["created_at"]}
                    for n, o in old.items() if n not in cur],
        "gainers": [{"full_name": e["full_name"], "delta": e["delta"], "stars": e["stars"]}
                    for e in gainers[:top_n]],
    }
