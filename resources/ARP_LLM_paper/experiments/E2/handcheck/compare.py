"""E2 hand-check comparison (hand scores committed before KEY.json was opened)."""
import json, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
key = json.load(open(os.path.join(HERE, 'KEY.json'))); me = json.load(open(os.path.join(HERE, 'scores.json')))
def kappa(pr):
    n = len(pr); po = sum(a == b for a, b in pr) / n; ca, cb = Counter(a for a, _ in pr), Counter(b for _, b in pr)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / n ** 2; return n, po, (po - pe) / (1 - pe) if pe < 1 else None
v = [(k['scorer']['verdict'], me[p]['verdict']) for p, k in key.items()]
n, po, kp = kappa(v); print(f'verdict, all: n={n} agree {po:.3f} kappa {kp:.3f}')
for kind in ('correct_contested', 'wrong_confident', 'open'):
    pr = [(k['scorer']['verdict'], me[p]['verdict']) for p, k in key.items() if k['kind'] == kind]
    n, po, kp = kappa(pr); print(f'  {kind}: n={n} agree {po:.3f} kappa {kp if kp is None else round(kp, 3)}  disagreements {Counter((a, b) for a, b in pr if a != b)}')
s = [(bool(k['settled']['settled']), me[p]['settled']) for p, k in key.items() if k['kind'] == 'open']
n, po, kp = kappa(s); print(f'settled on open items: n={n} agree {po:.3f} kappa {kp if kp is None else round(kp, 3)}  scorer-settled {sum(a for a, _ in s)} hand-settled {sum(b for _, b in s)}')
# derived outcomes: FA / FR / closure as the registration defines them
d = Counter()
for p, k in key.items():
    sv, hv = k['scorer']['verdict'], me[p]['verdict']
    if k['kind'] == 'wrong_confident': d['FA scorer/hand'] += 0; d[('FA', sv == 'ACCEPT', hv == 'ACCEPT')] += 1
    if k['kind'] == 'correct_contested': d[('FR', sv == 'REJECT', hv == 'REJECT')] += 1
print({str(k): v for k, v in d.items() if k != 'FA scorer/hand'})
