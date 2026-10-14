#!/usr/bin/env python3
"""r7327+70: the DECISIVE FRACTION of every classed entry of r7321's power sweep, by PREDICTION.md in this directory.

    python3 decisive.py          # reads ../r7321_70_power_sweep/{ENTRIES,TABLE}.tsv, writes DECISIVE.tsv

The form is cc66's, `r7323_cc66_recurrence_registered/reachability.py` (r7323+cc66): enumerate every integer outcome
the frame can produce, decide each under the registered rule, count the share that decides anything.  Its wilson,
newcombe and magnitude rule are reproduced here verbatim in effect (same constant, same formulae):
  rate against line L with central c   -- indecisive iff the Wilson 95% interval holds both L and c;
  difference with |delta|              -- indecisive iff the Newcombe interval holds both 0 and |delta| (cc66's verdict);
  band [lo, hi] (rate or difference)   -- indecisive iff the interval straddles a band edge.
Uniform over the integer outcome space (cc66's count), and beside it weighted by the binomial at the registered
central (for a difference: the two arms at 50 +/- delta/2).  Not enumerable, and said so: no alternative registered,
not_proportion, census.  Nothing is re-scored; bucket and outcome are read from TABLE.tsv as filed."""
import csv
import math
import os
from statistics import median

HERE = os.path.dirname(os.path.abspath(__file__))
SW = os.path.join(HERE, '..', 'r7321_70_power_sweep')
Z = 1.959963985


def wilson(k, n):                                     # cc66's, returning (p, lo, hi)
    p = k / n
    d = 1 + Z * Z / n
    c = (p + Z * Z / (2 * n)) / d
    h = Z * math.sqrt(p * (1 - p) / n + Z * Z / (4 * n * n)) / d
    return p, max(0.0, c - h), min(1.0, c + h)


def newcombe(k1, n1, k2, n2):                         # cc66's
    p1, l1, u1 = wilson(k1, n1)
    p2, l2, u2 = wilson(k2, n2)
    d = p1 - p2
    return d, d - math.sqrt((p1 - l1) ** 2 + (u2 - p2) ** 2), d + math.sqrt((u1 - p1) ** 2 + (p2 - l2) ** 2)


def binom(n, p):
    p = min(max(p, 1e-9), 1 - 1e-9)
    return [math.comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(n + 1)]


def f(x):
    try:
        return float(str(x).strip())
    except ValueError:
        return None


def decisive(r):
    kind = r['kind']
    c, lo, hi, line = (f(r[x]) for x in ('central', 'band_lo', 'band_hi', 'line'))
    n, n2 = f(r['scored_n']), f(r['arm2_n'])
    diff = (r.get('effect_basis') == 'diff' or kind == 'difference') and n and n2
    if kind in ('census', 'not_proportion') or not n:
        return None, None, f'not enumerable: {kind}'
    n, n2 = int(n), int(n2) if n2 else None
    if kind == 'band' and lo is not None and hi is not None:
        if c is None:
            c = (lo + hi) / 2
        L, H = lo / 100, hi / 100
        if diff:
            outs = [((k1, k2), newcombe(k1, n, k2, n2)) for k1 in range(n + 1) for k2 in range(n2 + 1)]
            dec = {o: (b[1] >= L and b[2] <= H) or b[2] < L or b[1] > H for o, b in outs}
            w1, w2 = binom(n, 0.5 + c / 200), binom(n2, 0.5 - c / 200)
            pw = sum(w1[a] * w2[b] for (a, b), v in dec.items() if v)
        else:
            outs = [(k, wilson(k, n)) for k in range(n + 1)]
            dec = {o: (b[1] >= L and b[2] <= H) or b[2] < L or b[1] > H for o, b in outs}
            w = binom(n, c / 100)
            pw = sum(w[k] for k, v in dec.items() if v)
        return sum(dec.values()) / len(dec), pw, f'{len(dec)} outcomes'
    if kind == 'rate_vs_line':
        if c is None or line is None or c == line:
            return None, None, 'not enumerable: no alternative registered'
        a, b = sorted((line / 100, c / 100))
        dec = {k: not (w[1] <= a and w[2] >= b) for k in range(n + 1) for w in [wilson(k, n)]}
        wt = binom(n, c / 100)
        return sum(dec.values()) / len(dec), sum(wt[k] for k, v in dec.items() if v), f'{len(dec)} outcomes'
    if kind == 'difference' and n2:
        d = c if c is not None else line
        if not d:
            return None, None, 'not enumerable: no alternative registered (direction only)'
        dd = abs(d) / 100
        dec = {}
        for k1 in range(n + 1):
            for k2 in range(n2 + 1):
                _, l_, u_ = newcombe(k1, n, k2, n2)
                m_lo, m_hi = (0.0 if l_ <= 0 <= u_ else min(abs(l_), abs(u_))), max(abs(l_), abs(u_))
                dec[(k1, k2)] = not (m_lo <= 0 and m_hi >= dd)       # cc66: the magnitude interval holds 0 and |delta|
        w1, w2 = binom(n, 0.5 + dd / 2), binom(n2, 0.5 - dd / 2)
        return sum(dec.values()) / len(dec), sum(w1[a] * w2[b] for (a, b), v in dec.items() if v), f'{len(dec)} outcomes'
    return None, None, 'not enumerable: no alternative registered'


def main():
    ent = {(r['file'], r['entry_id']): r for r in csv.DictReader(open(os.path.join(SW, 'ENTRIES.tsv'), encoding='utf-8'), delimiter='\t')}
    tab = list(csv.DictReader(open(os.path.join(SW, 'TABLE.tsv'), encoding='utf-8'), delimiter='\t'))
    out, by = [], {}
    for t in tab:
        if t['bucket'] in ('C', 'P'):
            continue
        dfrac, pw, note = decisive(ent[(t['file'], t['entry_id'])])
        out.append({'file': t['file'].split('/')[-2], 'entry_id': t['entry_id'], 'bucket': t['bucket'], 'h': t['h'],
                    'delta': t['delta'], 'n_scored': t['n_scored'], 'n80': t['n80'],
                    'decisive_fraction': '' if dfrac is None else f'{dfrac:.3f}',
                    'decisive_prob_at_central': '' if pw is None else f'{pw:.3f}', 'note': note})
        if dfrac is not None:
            by.setdefault(t['bucket'], []).append(dfrac)
    with open(os.path.join(HERE, 'DECISIVE.tsv'), 'w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0]), delimiter='\t')
        w.writeheader()
        w.writerows(out)
    print(f'{len(out)} classed entries; enumerable: {sum(len(v) for v in by.values())}')
    for b in ('R', 'U-PASS', 'U-FAIL', 'U-?'):
        v = by.get(b, [])
        if v:
            print(f'  {b:7} n={len(v):3}  median {median(v):.3f}  min {min(v):.3f}  max {max(v):.3f}  '
                  f'<0.10: {sum(x < 0.10 for x in v)}  0.10-0.40: {sum(0.10 <= x < 0.40 for x in v)}  >=0.40: {sum(x >= 0.40 for x in v)}')
    if by.get('R') and by.get('U-PASS'):
        print(f'  D-d  median R minus median U-PASS = {median(by["R"]) - median(by["U-PASS"]):+.3f}')


if __name__ == '__main__':
    main()
