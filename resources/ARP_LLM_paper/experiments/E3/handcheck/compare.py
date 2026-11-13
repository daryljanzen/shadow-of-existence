"""E3 hand-check comparison (hand scores committed at 25de00511, before KEY.json was opened)."""
import json, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
key = json.load(open(os.path.join(HERE, 'KEY.json'))); me = json.load(open(os.path.join(HERE, 'scores.json')))
def kappa(pr):
    n = len(pr); po = sum(a == b for a, b in pr) / n; ca, cb = Counter(a for a, _ in pr), Counter(b for _, b in pr)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / n ** 2
    return dict(n=n, agree=round(po, 3), kappa=(round((po - pe) / (1 - pe), 3) if pe < 1 else None), disagree=dict(Counter((a, b) for a, b in pr if a != b)))
for c in ('all', 'C0', 'C1', 'C2', 'C3'):
    ps = sorted(p for p, k in key.items() if c == 'all' or k['cond'] == c)
    fl = [(int(key[p]['scorer']['flaws'][str(i + 1)]), me[p]['flaws'][i]) for p in ps for i in range(3)]
    ov = [(bool(o['valid']), me[p]['other_valid'][i]) for p in ps for i, o in enumerate(key[p]['scorer']['other'])]
    vs, vm = sum(a for a, _ in ov), sum(b for _, b in ov)
    print(c, '| flaws', kappa(fl), '| other valid', kappa(ov), f'| valid per review: scorer {vs / len(ps):.2f} hand {vm / len(ps):.2f}')
assert all(len(key[p]['scorer']['other']) == len(me[p]['other_valid']) for p in key)
for p in sorted(key):
    d = [(i + 1, bool(o['valid']), me[p]['other_valid'][i]) for i, o in enumerate(key[p]['scorer']['other']) if bool(o['valid']) != me[p]['other_valid'][i]]
    if d: print(p, key[p]['cond'], d, me[p]['note'])
