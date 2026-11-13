"""E1 hand-check comparison (r7755): the hand scores (scores.json, committed first) against the banked scorer (KEY.json)."""
import json, os
from collections import Counter
from math import comb
HERE = os.path.dirname(os.path.abspath(__file__))
key = json.load(open(os.path.join(HERE, 'KEY.json'))); me = json.load(open(os.path.join(HERE, 'scores.json')))
def kappa(pairs):
    n = len(pairs); po = sum(a == b for a, b in pairs) / n
    ca, cb = Counter(a for a, _ in pairs), Counter(b for _, b in pairs)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / n ** 2
    return po, pe, (None if pe == 1 else (po - pe) / (1 - pe))
def cp(k, n, a=0.05):  # Clopper-Pearson by bisection on the binomial tail
    def tail_ge(p): return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k, n + 1))
    def tail_le(p): return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(0, k + 1))
    def solve(f, target, inc):
        lo, hi = 0.0, 1.0
        for _ in range(100):
            m = (lo + hi) / 2
            (lo, hi) = (m, hi) if (f(m) < target) == inc else (lo, m)
        return (lo + hi) / 2
    low = 0.0 if k == 0 else solve(tail_ge, a / 2, True)
    high = 1.0 if k == n else solve(tail_le, a / 2, False)
    return low, high
hard, easy, fp, cells = [], [], [], Counter()
for p, k in sorted(key.items()):
    hk = str(k['hard_k']); s, m = k['scorer'], me[p]['scores']
    assert set(s) == set(m), p
    for a in s:
        (hard if a == hk else easy).append((int(s[a]), m[a]))
    if m[hk] < 2:
        fp.append(p)
    cells[(k['model'], k['cond'])] += 1
print('sample cells:', dict(cells))
fpk = len(fp); lo, hi = cp(fpk, len(key))
print(f'(i) hard-ask false passes: {fpk}/{len(key)}  95% CI [{lo:.3f}, {hi:.3f}]  {fp}')
print('    scorer hard column:', Counter(a for a, _ in hard), ' hand:', Counter(b for _, b in hard))
for name, pr in (('easy', easy), ('pooled', hard + easy)):
    po, pe, k = kappa(pr)
    dis = [(a, b) for a, b in pr if a != b]
    print(f'(ii) {name}: n={len(pr)} agreement {po:.4f}  chance {pe:.4f}  kappa {k if k is None else round(k, 3)}  disagreements {Counter(dis)}')
for p in sorted(me):
    s = key[p]['scorer']; m = me[p]['scores']
    d = [a for a in s if int(s[a]) != m[a]]
    if d:
        print('   ', p, key[p]['model'], key[p]['cond'], key[p]['item'], 'asks', d, 'scorer', [s[a] for a in d], 'hand', [m[a] for a in d], '|', me[p]['note'])
