#!/usr/bin/env python3
"""Score the within-seat spread once both halves are read.  Nothing is pooled.

Expects, beside this file, one TSV per half:

    READ_half_A.tsv   # columns: receipt, literal, verdict, flag   (flag: FLAG or '')
    READ_half_B.tsv

and reports, per half and never pooled:

  * the OWEDNESS margin -- the fraction verdicted REPAIR-OWED, with a Wilson interval;
  * the FLAG margin -- the fraction carrying the judgement flag, likewise;
  * the SPREAD between halves on each margin, with a NEWCOMBE hybrid-score interval, which is
    `70`'s standing form.

Then it fires the registered refutation conditions by the numbers alone.
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
Z = 1.959963985  # 95 per cent, two-sided
BAND = (8.0, 24.0)
POINT = 16.0


def wilson(k, n):
    """Score interval for one proportion."""
    if n == 0:
        return 0.0, 0.0, 0.0
    p = k / n
    d = 1 + Z * Z / n
    c = (p + Z * Z / (2 * n)) / d
    h = Z * math.sqrt(p * (1 - p) / n + Z * Z / (4 * n * n)) / d
    return p, max(0.0, c - h), min(1.0, c + h)


def newcombe(k1, n1, k2, n2):
    """Hybrid score interval for p1 - p2 (Newcombe method 10)."""
    p1, l1, u1 = wilson(k1, n1)
    p2, l2, u2 = wilson(k2, n2)
    d = p1 - p2
    lo = d - math.sqrt((p1 - l1) ** 2 + (u2 - p2) ** 2)
    hi = d + math.sqrt((u1 - p1) ** 2 + (p2 - l2) ** 2)
    return d, lo, hi


def read(half):
    p = os.path.join(HERE, f'READ_half_{half}.tsv')
    if not os.path.exists(p):
        return None
    rows = []
    for ln in open(p, encoding='utf-8'):
        if ln.startswith('#') or not ln.strip():
            continue
        f = ln.rstrip('\n').split('\t')
        if len(f) < 3:
            continue
        rows.append((f[0], json.loads(f[1]), f[2].strip(),
                     (f[3].strip() if len(f) > 3 else '')))
    return rows


def margin(rows, which):
    if which == 'owed':
        k = sum(1 for _, _, v, _ in rows if v == 'REPAIR-OWED')
    else:
        k = sum(1 for _, _, _, g in rows if g.upper().startswith('FLAG'))
    return k, len(rows)


def main():
    a, b = read('A'), read('B')
    print()
    print('  WITHIN-SEAT SPREAD -- r7321+cc66, text 1a3c13a6, halves never pooled')
    print()
    if a is None or b is None:
        missing = [h for h, r in (('A', a), ('B', b)) if r is None]
        print(f'  NOT YET READ: READ_half_{" and READ_half_".join(missing)}.tsv absent.')
        print('  The instrument is complete and the pre-registration is pushed; what is missing is')
        print('  the two fresh reads, which this seat may not perform -- see PREREGISTRATION.md.')
        return 2

    fired = []
    out = {}
    for name in ('owed', 'flag'):
        ka, na = margin(a, name)
        kb, nb = margin(b, name)
        pa, la, ua = wilson(ka, na)
        pb, lb, ub = wilson(kb, nb)
        d, lo, hi = newcombe(ka, na, kb, nb)
        out[name] = abs(d) * 100
        print(f'  {name.upper()} margin')
        print(f'    half A : {ka}/{na} = {pa:6.1%}   95% [{la:.1%}, {ua:.1%}]')
        print(f'    half B : {kb}/{nb} = {pb:6.1%}   95% [{lb:.1%}, {ub:.1%}]')
        print(f'    SPREAD : {abs(d) * 100:5.1f} points   Newcombe 95% '
              f'[{lo * 100:+.1f}, {hi * 100:+.1f}]')
        print(f'    {"clears zero" if lo > 0 or hi < 0 else "DOES NOT clear zero"}; '
              f'{"excludes 30" if not (lo * 100 <= 30 <= hi * 100) else "does NOT exclude 30"}')
        print()

    o = out['owed']
    if o < BAND[0]:
        fired.append(f'① owedness spread {o:.1f} < {BAND[0]} -- tighter than registered')
    if o > BAND[1]:
        fired.append(f'② owedness spread {o:.1f} > {BAND[1]} -- wider than registered')
    if out['flag'] <= o:
        fired.append(f'③ flag spread {out["flag"]:.1f} <= owedness {o:.1f} -- secondary refuted')
    for h, rows in (('A', a), ('B', b)):
        k, n = margin(rows, 'owed')
        if n and not (0.40 <= k / n <= 0.80):
            fired.append(f'④ half {h} owed {k / n:.1%} outside 40-80% -- frame not reproducing')

    print(f'  registered band {BAND[0]}-{BAND[1]}, point {POINT}; observed {o:.1f}')
    print(f'  refutation conditions fired: {len(fired)}')
    for f in fired:
        print(f'    - {f}')
    if not fired:
        print('    none -- the result sits inside the registered band')
    return 0


if __name__ == '__main__':
    sys.exit(main())
