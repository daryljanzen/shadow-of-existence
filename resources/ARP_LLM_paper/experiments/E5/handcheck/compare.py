"""E5 hand-check comparison: hand judgements (scores.json, committed first) against the matcher (KEY.json)."""
import json, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
key = json.load(open(os.path.join(HERE, 'KEY.json'))); me = json.load(open(os.path.join(HERE, 'scores.json')))
def kappa(pairs):
    n = len(pairs); po = sum(a == b for a, b in pairs) / n
    ca, cb = Counter(a for a, _ in pairs), Counter(b for _, b in pairs)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / n ** 2
    return n, po, pe, (po - pe) / (1 - pe) if pe < 1 else None
out = {}
for field in ('valid', 'anticipated'):
    for lvl in ('all', 'R0', 'R1', 'R2'):
        pr, mism = [], 0
        for p, k in key.items():
            if lvl != 'all' and k['level'] != lvl:
                continue
            m = [bool(j.get(field)) for j in k['matcher']]; h = me[p][field]
            if len(m) != len(h):
                mism += 1; continue
            pr += list(zip(m, h))
        n, po, pe, kp = kappa(pr)
        print(f'{field:11s} {lvl}: n={n} agree {po:.3f} chance {pe:.3f} kappa {kp:.3f}  matcher+ {sum(a for a, _ in pr)} hand+ {sum(b for _, b in pr)}  '
              f'(matcher yes/hand no {sum(a and not b for a, b in pr)}, matcher no/hand yes {sum(b and not a for a, b in pr)}) length-mismatched packets {mism}')
