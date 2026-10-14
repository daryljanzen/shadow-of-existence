#!/usr/bin/env python3
r"""design.py -- the draw under fork (c), sized rather than guessed.

r7321 ordered the design and said to register only after `cc66`'s reader-arm result is readable, so
the reader arm here is a FUNCTION of the spread that measurement will report and not a number.

Three things are computed: the clustering of this seat's own sample and what it moves; the sampling
arm's size for an interval this seat would publish; and the reader arm's size per discordance.
"""
import collections
import io
import math
import os
import random

Z95 = 1.959963985
Z80 = 0.8416212336
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
SAMPLE = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7320_60_the_early_era_sampled',
                      'RESULT_40.tsv')
BOUND = 0.153          # the difference a reader arm must be able to bound, r7299's own figure


def rows():
    out = []
    for l in io.open(SAMPLE, encoding='utf-8'):
        if l.strip() and not l.startswith('#'):
            c = l.split('\t')
            out.append((c[1], 1 if c[6] == 'WITHDRAWN' else 0))
    return out


def icc_oneway(groups):
    """the one-way random-effects ICC on a binary outcome, unequal cluster sizes."""
    n = sum(len(v) for v in groups)
    k = len(groups)
    p = sum(sum(v) for v in groups) / n
    msb = sum(len(v) * (sum(v) / len(v) - p) ** 2 for v in groups) / (k - 1)
    msw = sum(sum((x - sum(v) / len(v)) ** 2 for x in v) for v in groups) / (n - k)
    m0 = (n - sum(len(v) ** 2 for v in groups) / n) / (k - 1)
    den = msb + (m0 - 1) * msw
    return ((msb - msw) / den if den else 0.0), p, n, k


def design_effect(groups):
    icc, p, n, k = icc_oneway(groups)
    return 1 + (n / k - 1) * max(icc, 0.0), icc, p, n, k


def wilson(k, n, z=Z95):
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (c - h) / d, (c + h) / d


def n_for_halfwidth(hw, p, deff=1.0, z=Z95):
    return math.ceil(z * z * p * (1 - p) / (hw * hw) * deff)


def m_reader(discord, bound=BOUND, deff=1.0, z=Z95):
    return math.ceil(z * z * discord / (bound * bound) * deff)


def newcombe(k1, n1, k2, n2, z=Z95):
    """Newcombe's method 10 (MOVER-R on two Wilson intervals) for p1 - p2."""
    l1, u1 = wilson(k1, n1, z)
    l2, u2 = wilson(k2, n2, z)
    d = k1 / n1 - k2 / n2
    lo = d - math.sqrt((k1 / n1 - l1) ** 2 + (u2 - k2 / n2) ** 2)
    hi = d + math.sqrt((u1 - k1 / n1) ** 2 + (k2 / n2 - l2) ** 2)
    return max(lo, -1.0), min(hi, 1.0)


def newcombe_coverage(p1, p2, n1, n2, trials=2000, seed=7326):
    """a seeded coverage check: the nominal 95 per cent interval should cover about 95 per cent."""
    rng = random.Random(seed)
    hit = 0
    for _ in range(trials):
        k1 = sum(1 for _ in range(n1) if rng.random() < p1)
        k2 = sum(1 for _ in range(n2) if rng.random() < p2)
        lo, hi = newcombe(k1, n1, k2, n2)
        if lo <= p1 - p2 <= hi:
            hit += 1
    return hit / trials


if __name__ == '__main__':
    g = collections.defaultdict(list)
    for rec, y in rows():
        g[rec].append(y)
    groups = list(g.values())
    deff, icc, p, n, k = design_effect(groups)
    print(f'r7320\'s own sample: {n} keys in {k} receipts, mean {n / k:.2f}')
    print(f'  ICC {icc:.3f}   design effect {deff:.3f}   effective n {n / deff:.1f}')
    print(f'  band naive     {[round(100 * x, 1) for x in wilson(round(p * n), n)]}')
    print(f'  band clustered {[round(100 * x, 1) for x in wilson(p * n / deff, n / deff)]}')
    print()
    print('the SAMPLING arm -- sized to the interval this seat would publish, not to a difference:')
    for hw in (0.10, 0.075, 0.05):
        print(f'  half-width {100 * hw:4.1f} points: {n_for_halfwidth(hw, p):4d} keys naive, '
              f'{n_for_halfwidth(hw, p, deff):4d} clustered')
    print()
    print(f'the READER arm -- paired keys to bound a {100 * BOUND:.1f}-point reader difference, '
          f'by the discordance cc66 reports:')
    for d in (0.10, 0.15, 0.20, 0.30, 0.40):
        print(f'  discordance {100 * d:4.0f}%: {m_reader(d):3d} paired naive, '
              f'{m_reader(d, deff=deff):3d} clustered')
    print()
    print(f'Newcombe coverage control at p1=0.675 p2=0.522, n=50: '
          f'{100 * newcombe_coverage(0.675, 0.522, 50, 50):.1f} per cent')
