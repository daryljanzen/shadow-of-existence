#!/usr/bin/env python3
"""r7439 — THE REGISTER'S OWN TALLY, READ FROM ITS CELLS, with a RUNNING TOTAL.

** WHY THIS EXISTS. **  `.80` reported `78` refusal sites and `19` distinct sources.  Both were wrong: the
hand sum stopped one row short of the table's end, dropping `red_carry`'s `3`, and the source count included
the shared row.  **The running total below is printed precisely so that the place a sum goes wrong is
visible** -- it reaches `78` after `check_view_tables` and `81` after `red_carry`, which is exactly the error.

    python3 tally.py
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.abspath(os.path.join(HERE, '..', 'r7419_cc66_the_register_of_keys', 'register.tsv'))


def main():
    rows, run = [], 0
    for line in open(REG, encoding='utf-8'):
        f = line.rstrip('\n').split('\t')
        if len(f) != 8 or f[0].startswith('#'):
            continue
        m = re.search(r'\((\d+) of (\d+) refusal sites walked', f[7])
        shared = 'SAME SOURCE' in f[7]
        rows.append((f[0], m and (int(m.group(1)), int(m.group(2))), shared,
                     len(re.findall('SELF-REFERENTIAL', f[7])), len(re.findall('ONE STEP FROM A WALL', f[7]))))
    print('  instrument                            walked  self-ref  one-step   of  running')
    w = s = sr = osw = 0
    for name, v, shared, n_sr, n_os in rows:
        if v is None:
            print(f'  {name:<36}      --  nothing refuses on this key')
            continue
        if shared:
            print(f'  {name:<36} {v[0]:>6} {n_sr:>9} {n_os:>9} {v[1]:>4}   (shared source -- not added)')
            continue
        w += v[0]; s += v[1]; sr += n_sr; osw += n_os; run += v[1]
        print(f'  {name:<36} {v[0]:>6} {n_sr:>9} {n_os:>9} {v[1]:>4} {run:>8}')
    print(f'\n  {len([r for r in rows if r[1] and not r[2]])} distinct sources, {s} refusal sites')
    print(f'  {w} walked, {sr} self-referential, {s - w - sr} pending   ({w / s:.1%} walked)')
    print(f'  {osw} cell(s) carry the ONE STEP FROM A WALL grade')
    full = [n for n, v, sh, a, b in rows if v and not sh and v[0] + a == v[1]]
    print(f'  fully accounted: {len(full)} -> {", ".join(full)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
