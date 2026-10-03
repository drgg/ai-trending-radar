"""用当前提示词重新生成抽检样本的介绍，输入与 v2 相同（同一版 README、同一份元数据），结果写入 eval/v3/，不动 data/intros。"""
import json, sys, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import yaml
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from summarize import Summarizer, PROMPT_VERSION, length_violations

cfg = yaml.safe_load((ROOT / "config.yml").read_text(encoding="utf-8"))
out_dir = ROOT / "eval" / f"v{PROMPT_VERSION}"
out_dir.mkdir(exist_ok=True)
sample = json.loads((ROOT / (sys.argv[1] if len(sys.argv) > 1 else "eval/sample.json")).read_text(encoding="utf-8"))["sample"]

def run(s):
    key = s["repo"].replace("/", "__")
    path = out_dir / f"{key}.json"
    if path.exists():
        return s["repo"], "cached", 0
    v2 = json.loads((ROOT / "eval/v2" / f"{key}.json").read_text(encoding="utf-8"))
    repo = {**s["meta"], "readme_sha": v2["readme_sha"],
            "readme": (ROOT / "eval/readmes" / f"{key}.md").read_text(encoding="utf-8")}
    summ = Summarizer(cfg)
    t = time.time()
    intro = summ.generate(repo)
    intro.update(prompt_version=PROMPT_VERSION, model=cfg["model"], calls=summ.calls,
                 still_over=length_violations(intro))
    path.write_text(json.dumps(intro, ensure_ascii=False, indent=2), encoding="utf-8")
    return s["repo"], f"{time.time()-t:.0f}s", summ.calls

with ThreadPoolExecutor(int(sys.argv[2]) if len(sys.argv) > 2 else 4) as ex:
    for repo, took, calls in ex.map(run, sample):
        print(repo, took, "调用", calls, flush=True)
