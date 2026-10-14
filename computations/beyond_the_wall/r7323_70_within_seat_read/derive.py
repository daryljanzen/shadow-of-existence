#!/usr/bin/env python3
"""r7323+70: derive cc66's READ_half_{A,B}.tsv (receipt, literal, verdict, FLAG or '') mechanically from this seat's raw
APPLICATION_70_half_{A,B}.tsv, and print both margins per agent (Wilson) and the A - B spread on each (Newcombe), never
pooled.  The verdict on the spread is cc66's.

    python3 derive.py"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'r7303_70_redraft_score'))
from score_redraft import wilson  # noqa: E402

OWED, UND = 'REPAIR-OWED', 'UNDECIDED'


def raw(h):
    rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(HERE, f'APPLICATION_70_half_{h}.tsv'), encoding='utf-8')
            if l.strip() and not l.startswith('#')]
    return rows[1:]


def newcombe(k1, n1, k2, n2):
    p1, p2 = k1 / n1, k2 / n2
    l1, u1 = wilson(k1, n1)
    l2, u2 = wilson(k2, n2)
    d = p1 - p2
    return d, d - math.sqrt((p1 - l1) ** 2 + (u2 - p2) ** 2), d + math.sqrt((u1 - p1) ** 2 + (p2 - l2) ** 2)


def main():
    m = {}
    for h in 'AB':
        r = raw(h)
        with open(os.path.join(HERE, f'READ_half_{h}.tsv'), 'w', encoding='utf-8') as f:
            f.write(f'# derived by derive.py from APPLICATION_70_half_{h}.tsv; columns: receipt, literal, verdict, flag\n')
            for c in r:
                f.write(f'{c[0]}\t{c[1]}\t{c[3].strip()}\t{"FLAG" if c[7].lower().startswith("yes") else ""}\n')
        dec = [c for c in r if c[3].strip() != UND]
        m[h] = {'n': len(r), 'dec': len(dec), 'und': len(r) - len(dec),
                'owed': sum(c[3].strip() == OWED for c in dec), 'flag': sum(c[7].lower().startswith('yes') for c in dec)}
    for h in 'AB':
        x = m[h]
        for k in ('owed', 'flag'):
            a, b = wilson(x[k], x['dec'])
            print(f'half {h}: {k} {x[k]}/{x["dec"]} = {100 * x[k] / x["dec"]:.1f}% (95% {100 * a:.1f}–{100 * b:.1f}); '
                  f'UNDECIDED {x["und"]} of {x["n"]}')
    for k in ('owed', 'flag'):
        d = newcombe(m['A'][k], m['A']['dec'], m['B'][k], m['B']['dec'])
        print(f'A - B on {k}: {100 * d[0]:+.1f} (95% {100 * d[1]:+.1f} to {100 * d[2]:+.1f})')


if __name__ == '__main__':
    main()
