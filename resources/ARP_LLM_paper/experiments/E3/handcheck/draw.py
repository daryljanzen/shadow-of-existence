"""E3 hand-check draw (registered r7758/r7759): 20% of the Opus main run's 240 scored reviews, 12 per condition, seed 3755.
Each packet carries what the scorer saw (document, key, review) plus the scorer's list of other problems with its
valid/invalid marks removed; I mark flaws found and each listed problem valid/invalid.  The condition and the scorer's
marks are in KEY.json, opened only after scores.json is committed.  Documents are written once per item (docs/)."""
import glob, json, os, random, re
HERE = os.path.dirname(os.path.abspath(__file__)); E3 = os.path.dirname(HERE); rnd = random.Random(3755); draw = []
for c in ('C0', 'C1', 'C2', 'C3'):
    draw += [(c, f) for f in rnd.sample(sorted(glob.glob(os.path.join(E3, 'scores_main', c, '*.json'))), 12)]
rnd.shuffle(draw); key = {}
for d in ('packets', 'docs'): os.makedirs(os.path.join(HERE, d), exist_ok=True)
for n, (c, f) in enumerate(draw, 1):
    r = json.load(open(f)); p = f'Q{n:02d}'; s = json.loads(re.search(r'\{.*\}', r['response'], re.S).group(0))
    m = r['message']; item = r['item']
    doc = m.split('DOCUMENT:\n', 1)[1].split('\n\nKEY (three known flaws):\n')[0]
    rest = m.split('\n\nKEY (three known flaws):\n', 1)[1]; k, rev = rest.split('\n\nREVIEW:\n', 1)
    open(os.path.join(HERE, 'docs', item + '.txt'), 'w').write(doc + '\n')
    issues = '\n'.join(f'  O{i + 1}. {o["issue"]}' for i, o in enumerate(s.get('other', [])))
    open(os.path.join(HERE, 'packets', p + '.txt'), 'w').write(f'ITEM: {item}\n\nKEY:\n{k}\n\nREVIEW:\n{rev}\n\nOTHER PROBLEMS LISTED:\n{issues}\n')
    key[p] = dict(cond=c, item=item, record=os.path.relpath(f, E3), scorer=s)
json.dump(key, open(os.path.join(HERE, 'KEY.json'), 'w'), indent=1); print(len(draw), 'packets')
