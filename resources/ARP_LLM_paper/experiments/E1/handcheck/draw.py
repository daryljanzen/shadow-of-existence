"""E1 hand-check draw (r7755). Population: main-run trials, both models, whose hard ask the banked scorer scored 2,
E1-09 excluded. Sample: 8 per model x condition (64 = the registered 20% of 320), seed 7755. Writes packets/P##.txt
(what the scorer saw: message, requests with the key, the answer as the scorer received it) in shuffled order, and
KEY.json (packet -> model, condition, item, the scorer's scores), which is not opened until scores.json is committed."""
import json, os, random, re
HERE = os.path.dirname(os.path.abspath(__file__)); E1 = os.path.dirname(HERE)
items = {i['id']: i for i in json.load(open(os.path.join(E1, 'materials/items.json')))}
strip = lambda t: re.sub(r'<receipt>.*?</receipt>', '', t or '', flags=re.S).replace('<receipt>', '').replace('</receipt>', '').strip()
rnd = random.Random(7755); draw = []
for tag in ('main', 'main_sonnet'):
    for c in ('C0', 'C1', 'C2', 'C3'):
        pool = []
        for iid, it in sorted(items.items()):
            if iid == 'E1-09':
                continue
            s = json.load(open(os.path.join(E1, f'scores_{tag}', c, iid + '.json')))['response']
            sc = json.loads(re.search(r'\{.*\}', s, re.S).group(0))['scores']
            if int(sc.get(str(it['hard_k']), 0)) == 2:
                pool.append((iid, sc))
        draw += [(tag, c, iid, sc) for iid, sc in rnd.sample(pool, 8)]
rnd.shuffle(draw); key = {}
os.makedirs(os.path.join(HERE, 'packets'), exist_ok=True)
for n, (tag, c, iid, sc) in enumerate(draw, 1):
    it = items[iid]; p = f'P{n:02d}'
    asks = '\n'.join(f"{a['k']}. {a['text']}" + (f"  KEY: {it['hard_key']}" if a['hard'] else '') for a in it['asks'])
    ans = strip(json.load(open(os.path.join(E1, f'runs_{tag}', c, iid + '.json')))['response'])
    open(os.path.join(HERE, 'packets', p + '.txt'), 'w').write(f"MESSAGE:\n{it['message']}\n\nREQUESTS:\n{asks}\n\nANSWER:\n{ans}\n")
    key[p] = dict(model=tag, cond=c, item=iid, hard_k=it['hard_k'], scorer=sc)
json.dump(key, open(os.path.join(HERE, 'KEY.json'), 'w'), indent=1)
print(len(draw), 'packets')
