"""E1: the three registered measures RESULT.md did not report (r7755, on 60's r7754 read), computed on the banked
judgements: (a) coverage, mean ask score over all asks, per condition and C1-C0 paired; McNemar's exact p on each
paired H contrast; H by receipt presence (amendment (a)), within C3 and pooled.  Each with E1-09 in and out.
Usage: python3 analyse_e1_registered.py <tag>     (main | main_sonnet)"""
import json, os, random, re, sys
from math import comb
tag = sys.argv[1]; HERE = os.path.dirname(os.path.abspath(__file__))
items = {i['id']: i for i in json.load(open(os.path.join(HERE, 'materials/items.json')))}
C = ('C0', 'C1', 'C2', 'C3'); H, COV, REC = {c: {} for c in C}, {c: {} for c in C}, {c: {} for c in C}
for c in C:
    for iid, it in items.items():
        s = json.loads(re.search(r'\{.*\}', json.load(open(os.path.join(HERE, f'scores_{tag}', c, iid + '.json')))['response'], re.S).group(0))['scores']
        H[c][iid] = int(int(s.get(str(it['hard_k']), 0)) == 2)
        COV[c][iid] = sum(int(v) for v in s.values()) / len(s)
        r = json.load(open(os.path.join(HERE, f'receiptcode_{tag}', c, iid + '.json')))['response']
        REC[c][iid] = bool(json.loads(re.search(r'\{.*\}', r, re.S).group(0))['restates_asks_first'])
def boot(a, b, ids, n=10000):
    random.seed(1); d = [a[i] - b[i] for i in ids]; m = sum(d) / len(d)
    bs = sorted(sum(random.choice(d) for _ in d) / len(d) for _ in range(n))
    return m, bs[int(.025 * n)], bs[int(.975 * n)]
def mcnemar(a, b, ids):
    b10 = sum(1 for i in ids if a[i] == 1 and b[i] == 0); b01 = sum(1 for i in ids if a[i] == 0 and b[i] == 1)
    n = b10 + b01
    if n == 0:
        return b10, b01, 1.0
    p = 2 * sum(comb(n, k) for k in range(0, min(b10, b01) + 1)) / 2 ** n
    return b10, b01, min(1.0, p)
for label, ids in (('all 40', sorted(items)), ('E1-09 excluded', sorted(i for i in items if i != 'E1-09'))):
    print(f'== {tag}, {label} (n={len(ids)})')
    for c in C:
        print(f'  {c}: coverage (mean ask score, 0-2) {sum(COV[c][i] for i in ids) / len(ids):.4f}   H {sum(H[c][i] for i in ids)}/{len(ids)}')
    m, lo, hi = boot(COV['C1'], COV['C0'], ids); print(f'  (a) coverage C1-C0: {m:+.4f}  95% CI [{lo:+.4f}, {hi:+.4f}]')
    for a, b in (('C1', 'C0'), ('C1', 'C2'), ('C1', 'C3')):
        b10, b01, p = mcnemar(H[a], H[b], ids)
        print(f'  McNemar {a} vs {b} on H: discordant {a}-only {b10}, {b}-only {b01}, exact p = {p:.3f}')
    yes = [i for i in ids if REC['C3'][i]]; no = [i for i in ids if not REC['C3'][i]]
    print(f'  C3 by receipt presence: restated {sum(H["C3"][i] for i in yes)}/{len(yes)}, did not {sum(H["C3"][i] for i in no)}/{len(no)}')
    py = [(c, i) for c in C for i in ids if REC[c][i]]; pn = [(c, i) for c in C for i in ids if not REC[c][i]]
    print(f'  pooled over conditions: restated {sum(H[c][i] for c, i in py)}/{len(py)}, did not {sum(H[c][i] for c, i in pn)}/{len(pn)}')
    print(f'  receipt presence by condition: ' + ', '.join(f'{c} {sum(REC[c][i] for i in ids)}/{len(ids)}' for c in C))
