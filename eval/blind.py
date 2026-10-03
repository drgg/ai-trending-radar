"""留出集盲评：每个仓库的 v2/v3 随机标为 A/B，对应关系写入 eval/blind_key.json，评完再揭晓。"""
import json, secrets
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
KEEP = ["is_ai_product", "category", "tagline", "positioning", "features", "highlights",
        "audience", "quickstart_cmd", "quickstart_note", "risks"]
hold = json.loads((ROOT / "eval/holdout.json").read_text(encoding="utf-8"))["sample"]
key = {}
for h in hold:
    k = h["repo"].replace("/", "__")
    v = {"v2": json.loads((ROOT / "eval/v2" / f"{k}.json").read_text(encoding="utf-8")),
         "v3": json.loads((ROOT / "eval/v3" / f"{k}.json").read_text(encoding="utf-8"))}
    order = ["v2", "v3"] if secrets.randbits(1) else ["v3", "v2"]
    key[h["repo"]] = {"A": order[0], "B": order[1]}
    blind = {lab: {f: v[ver].get(f) for f in KEEP} for lab, ver in zip("AB", order)}
    (ROOT / "eval/blind" / f"{k}.json").write_text(json.dumps(blind, ensure_ascii=False, indent=1), encoding="utf-8")
(ROOT / "eval/blind_key.json").write_text(json.dumps(key, ensure_ascii=False, indent=1), encoding="utf-8")
print("已生成", len(key), "组")
