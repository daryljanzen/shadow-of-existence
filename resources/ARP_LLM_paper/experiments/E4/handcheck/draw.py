"""E4 hand-check draw (r7758): 32 per condition of the main run's question-level scorings, seed 4755."""
import glob, json, os, random, re
HERE = os.path.dirname(os.path.abspath(__file__)); E4 = os.path.dirname(HERE); rnd = random.Random(4755); draw = []
for c in ('C0', 'C1'):
    draw += [(c, f) for f in rnd.sample(sorted(glob.glob(os.path.join(E4, 'scores_main', c, '*.json'))), 32)]
rnd.shuffle(draw); key = {}; os.makedirs(os.path.join(HERE, 'packets'), exist_ok=True)
for n, (c, f) in enumerate(draw, 1):
    r = json.load(open(f)); p = f'W{n:02d}'
    open(os.path.join(HERE, 'packets', p + '.txt'), 'w').write(r['message'] + '\n')
    key[p] = dict(cond=c, record=os.path.relpath(f, E4), scorer=json.loads(re.search(r'\{.*\}', r['response'], re.S).group(0)))
json.dump(key, open(os.path.join(HERE, 'KEY.json'), 'w'), indent=1); print(len(draw), 'packets')
