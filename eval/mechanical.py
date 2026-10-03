"""可自动判定的两项：字段字数/条数超限；quickstart_cmd 是否在 README 中原样出现。"""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
LIMIT = {"tagline": 40, "positioning": 100, "audience": 60, "quickstart_note": 60}
LIST = {"features": (3, 5, 40), "highlights": (1, 3, 50)}

def check(intro, readme):
    issues = []
    for f, n in LIMIT.items():
        if len(intro.get(f, "")) > n:
            issues.append(f"{f} {len(intro[f])}/{n} 字")
    for f, (lo, hi, n) in LIST.items():
        items = intro.get(f, [])
        if not lo <= len(items) <= hi:
            issues.append(f"{f} {len(items)} 条（应 {lo}–{hi}）")
        for i, t in enumerate(items, 1):
            if len(t) > n:
                issues.append(f"{f}[{i}] {len(t)}/{n} 字")
    cmd = intro.get("quickstart_cmd", "")
    cmd_ok = (not cmd) or " ".join(cmd.split()) in " ".join(readme.split())
    return issues, cmd_ok

if __name__ == "__main__":
    import sys
    intro_dir = ROOT / (sys.argv[1] if len(sys.argv) > 1 else "eval/v2")
    out = ROOT / (sys.argv[2] if len(sys.argv) > 2 else "eval/mechanical.json")
    sys.path.insert(0, str(ROOT / "scripts"))
    from summarize import length_violations
    sample = json.loads((ROOT / (sys.argv[3] if len(sys.argv) > 3 else "eval/sample.json")).read_text(encoding="utf-8"))["sample"]
    res = {}
    for s in sample:
        key = s["repo"].replace("/", "__")
        intro = json.loads((intro_dir / f"{key}.json").read_text(encoding="utf-8"))
        readme = (ROOT / "eval/readmes" / f"{key}.md").read_text(encoding="utf-8")
        issues, cmd_ok = check(intro, readme)
        res[s["repo"]] = {"length_issues": issues, "length_issues_word": length_violations(intro), "cmd_verbatim": cmd_ok, "cmd": intro.get("quickstart_cmd", "")}
        print(s["repo"], "| 超限:", issues or "无", "| 命令照抄:", cmd_ok)
    out.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
