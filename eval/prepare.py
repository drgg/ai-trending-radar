"""抽检准备：固定种子抽 20 个仓库，按 intro 里记录的 readme_sha 取回模型当时看到的 README。"""
import base64, json, random, sys
from pathlib import Path
sys.path.insert(0, "scripts")
from fetch import _session, _get, clean_readme

ROOT = Path(__file__).resolve().parent.parent
SEED, N, MAX = 20261001, 20, 12000

meta = {}
for snap in sorted((ROOT / "data/snapshots").glob("*.json")):
    for e in json.loads(snap.read_text(encoding="utf-8"))["entries"]:
        meta[e["full_name"]] = {k: e.get(k) for k in ("full_name", "description", "stars", "forks",
                                "language", "license", "topics", "homepage", "created_at", "pushed_at")}
names = sorted(p.stem.replace("__", "/", 1) for p in (ROOT / "data/intros").glob("*.json"))
sample = sorted(random.Random(SEED).sample(names, N))
s = _session()
out = []
for name in sample:
    intro = json.loads((ROOT / "data/intros" / (name.replace("/", "__") + ".json")).read_text(encoding="utf-8"))
    r = _get(s, f"https://api.github.com/repos/{name}/git/blobs/{intro['readme_sha']}")
    ok = r.status_code == 200
    raw = base64.b64decode(r.json()["content"]).decode("utf-8", "replace") if ok else ""
    (ROOT / "eval/readmes" / (name.replace("/", "__") + ".md")).write_text(clean_readme(raw, MAX), encoding="utf-8")
    out.append({"repo": name, "readme_ok": ok, "readme_chars": len(raw), "meta": meta.get(name)})
    print(name, r.status_code, len(raw))
(ROOT / "eval/sample.json").write_text(json.dumps({"seed": SEED, "pool": len(names), "sample": out},
                                                   ensure_ascii=False, indent=1), encoding="utf-8")
