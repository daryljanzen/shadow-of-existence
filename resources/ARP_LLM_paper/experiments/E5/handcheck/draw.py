"""E5 hand-check draw (r7755): R0 11, R1 11, R2 14 of the main run's 180 match records, seed 5755. Packets carry the
matcher's recorded input verbatim (no level); KEY.json holds level and the matcher's judgements."""
import glob, json, os, random, re
HERE = os.path.dirname(os.path.abspath(__file__)); E5 = os.path.dirname(HERE); rnd = random.Random(5755); draw = []
for lvl, k in (('R0', 11), ('R1', 11), ('R2', 14)):
    draw += [(lvl, f) for f in rnd.sample(sorted(glob.glob(os.path.join(E5, 'match_main', lvl, '*.json'))), k)]
rnd.shuffle(draw); key = {}; os.makedirs(os.path.join(HERE, 'packets'), exist_ok=True)
for n, (lvl, f) in enumerate(draw, 1):
    r = json.load(open(f)); p = f'Q{n:02d}'
    open(os.path.join(HERE, 'packets', p + '.txt'), 'w').write(r['message'] + '\n')
    key[p] = dict(level=lvl, record=os.path.relpath(f, E5), matcher=json.loads(re.search(r'\{.*\}', r['response'], re.S).group(0))['judgements'])
json.dump(key, open(os.path.join(HERE, 'KEY.json'), 'w'), indent=1); print(len(draw), 'packets')
