import json,sys
for r in sys.argv[1:]:
    k=r.replace('/','__')
    i=json.load(open(f"eval/v2/{k}.json",encoding='utf-8'))
    print('='*30,r)
    for f in ['is_ai_product','category','tagline','positioning','features','highlights','audience','quickstart_cmd','quickstart_note','risks']:
        print(f'[{f}]',i.get(f))
    print('--- README ---')
    print(open(f'eval/readmes/{k}.md',encoding='utf-8').read())
