"""与上一期快照对比，生成变化摘要。"""
import json
from pathlib import Path

SNAP_DIR = Path(__file__).resolve().parent.parent / "data" / "snapshots"


def previous_snapshot(today_str):
    snaps = sorted(p for p in SNAP_DIR.glob("*.json") if p.stem < today_str)
    return json.loads(snaps[-1].read_text(encoding="utf-8")) if snaps else None


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
