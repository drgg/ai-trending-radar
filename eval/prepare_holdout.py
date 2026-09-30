"""留出集：缓存池中没被抽进 sample.json 的介绍，调提示词时没看过，用来检验 v3 是否只是贴合了那 20 条。"""
import base64, json, sys
from pathlib import Path
sys.path.insert(0, "scripts")
from fetch import _session, _get, clean_readme

ROOT = Path(__file__).resolve().parent.parent
MAX = 12000
sample = {s["repo"] for s in json.loads((ROOT / "eval/sample.json").read_text(encoding="utf-8"))["sample"]}
meta = {}
for snap in sorted((ROOT / "data/snapshots").glob("*.json")):
    for e in json.loads(snap.read_text(encoding="utf-8"))["entries"]:
        meta[e["full_name"]] = {k: e.get(k) for k in ("full_name", "description", "stars", "forks",
                                "language", "license", "topics", "homepage", "created_at", "pushed_at")}
names = sorted(p.stem.replace("__", "/", 1) for p in (ROOT / "data/intros").glob("*.json"))
holdout = [n for n in names if n not in sample]
s = _session()
out = []
for name in holdout:
    key = name.replace("/", "__")
    intro = json.loads((ROOT / "data/intros" / f"{key}.json").read_text(encoding="utf-8"))
    r = _get(s, f"https://api.github.com/repos/{name}/git/blobs/{intro['readme_sha']}")
    ok = r.status_code == 200
    raw = base64.b64decode(r.json()["content"]).decode("utf-8", "replace") if ok else ""
    (ROOT / "eval/readmes" / f"{key}.md").write_text(clean_readme(raw, MAX), encoding="utf-8")
    out.append({"repo": name, "readme_ok": ok, "readme_chars": len(raw), "meta": meta.get(name)})
    print(name, r.status_code, len(raw))
(ROOT / "eval/holdout.json").write_text(json.dumps({"pool": len(names), "sample": out},
                                                    ensure_ascii=False, indent=1), encoding="utf-8")
