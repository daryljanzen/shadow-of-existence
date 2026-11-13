"""E2 hand-check draw (r7758): 10 per condition x kind from the Opus main run, seed 2755; blind packets + KEY.json."""
import json, os, random, re
HERE = os.path.dirname(os.path.abspath(__file__)); E2 = os.path.dirname(HERE); rnd = random.Random(2755)
items = {i['id']: i for i in json.load(open(os.path.join(E2, 'materials/items.json')))}
draw = []
for c in ('C0', 'C1', 'C2', 'C3'):
    for kind in ('correct_contested', 'wrong_confident', 'open'):
        pool = [(c, i, r) for i, it in sorted(items.items()) if it['kind'] == kind for r in range(3)]
        draw += rnd.sample(pool, 10)
rnd.shuffle(draw); key = {}; os.makedirs(os.path.join(HERE, 'packets'), exist_ok=True)
for n, (c, i, r) in enumerate(draw, 1):
    p = f'V{n:03d}'; it = items[i]
    resp = json.load(open(os.path.join(E2, 'runs_main', c, f'{i}__r{r}.json')))['response']
    open(os.path.join(HERE, 'packets', p + '.txt'), 'w').write(f"SITUATION:\n{it['prompt']}\n\nCLAIM:\n{it['claim']}\n\nRESPONSE:\n{resp}\n")
    sc = lambda d: json.loads(re.search(r'\{.*\}', json.load(open(os.path.join(E2, d, c, f'{i}__r{r}.json')))['response'], re.S).group(0))  # noqa: E731
    key[p] = dict(cond=c, item=i, rep=r, kind=it['kind'], scorer=sc('scores_main'),
                  settled=sc('settled_main') if it['kind'] == 'open' else None)
json.dump(key, open(os.path.join(HERE, 'KEY.json'), 'w'), indent=1); print(len(draw), 'packets')
