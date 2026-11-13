"""E4 hand-check comparison (hand scores committed before KEY.json was opened). On control questions the two
candidates are identical, so A and B are the same answer and are merged as 'A' for agreement."""
import json, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
key = json.load(open(os.path.join(HERE, 'KEY.json'))); me = json.load(open(os.path.join(HERE, 'scores.json')))
def ident(p):
    t = open(os.path.join(HERE, 'packets', p + '.txt')).read()
    return t.split('CANDIDATE A:\n')[1].split('\n\nCANDIDATE B')[0] == t.split('CANDIDATE B:\n')[1].split('\n\nRESPONSE')[0]
def norm(m, p): return 'A' if ident(p) and m in ('A', 'B') else m
def kappa(pr):
    n = len(pr); po = sum(a == b for a, b in pr) / n; ca, cb = Counter(a for a, _ in pr), Counter(b for _, b in pr)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / n ** 2; return n, round(po, 3), (round((po - pe) / (1 - pe), 3) if pe < 1 else None)
for c in ('all', 'C0', 'C1'):
    ps = [p for p, k in key.items() if c == 'all' or k['cond'] == c]
    m = [(norm(key[p]['scorer']['match'], p), norm(me[p]['match'], p)) for p in ps]
    s = [(bool(key[p]['scorer'].get('mentions_checking_source')), me[p]['mentions_checking_source']) for p in ps]
    print(c, 'match', kappa(m), Counter(x for x in m if x[0] != x[1]), '| mentions source', kappa(s), Counter(x for x in s if x[0] != x[1]))
print('controls (identical candidates):', sum(ident(p) for p in key))
