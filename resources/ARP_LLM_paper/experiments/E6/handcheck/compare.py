"""E6 hand-check comparison (hand scores committed at 68293080c, before KEY.json was opened)."""
import json, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
key = json.load(open(os.path.join(HERE, 'KEY.json'))); me = json.load(open(os.path.join(HERE, 'scores.json')))
def kappa(pr):
    n = len(pr); po = sum(a == b for a, b in pr) / n; ca, cb = Counter(a for a, _ in pr), Counter(b for _, b in pr)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / n ** 2
    return dict(n=n, agree=round(po, 3), kappa=(round((po - pe) / (1 - pe), 3) if pe < 1 else None), disagree=dict(Counter((a, b) for a, b in pr if a != b)))
for c in ('all', 'S', 'G-ARP', 'G-noR'):
    ps = sorted(p for p, k in key.items() if c == 'all' or k['cond'] == c)
    fl = [(int(key[p]['scorer']['corrected'][str(i + 1)]), me[p]['corrected'][i]) for p in ps for i in range(4)]
    ex = [(int(key[p]['scorer']['extensions'][i]), me[p]['extensions'][i]) for p in ps for i in range(3)]
    ie = [(int(key[p]['scorer']['introduced_errors']), me[p]['introduced_errors']) for p in ps]
    print(c, '| flaws', kappa(fl), '| extensions', kappa(ex),
          '| introduced: exact', sum(a == b for a, b in ie), 'within1', sum(abs(a - b) <= 1 for a, b in ie), 'of', len(ie), 'scorer total', sum(a for a, _ in ie))
for p in sorted(key):
    s = key[p]['scorer']; m = me[p]
    sc = [int(s['corrected'][str(i + 1)]) for i in range(4)]; se = [int(x) for x in s['extensions']]
    if sc != m['corrected'] or se != m['extensions'] or int(s['introduced_errors']) != m['introduced_errors']:
        print(p, key[p]['cond'], 'scorer', sc, se, s['introduced_errors'], '| me', m['corrected'], m['extensions'], m['introduced_errors'], m['note'])
