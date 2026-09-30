import json, sys
for r in sys.argv[1:]:
    k = r.replace("/", "__")
    b = json.load(open(f"eval/blind/{k}.json", encoding="utf-8"))
    print("=" * 30, r)
    for lab in "AB":
        print(f"--- {lab}")
        for f, v in b[lab].items():
            print(f"[{f}]", v)
    print("--- README ---")
    print(open(f"eval/readmes/{k}.md", encoding="utf-8").read())
