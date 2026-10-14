#!/usr/bin/env python3
r"""power.py -- the within-unit reference and what it costs, for r7319's ruling (3).

No population, no salt, no band: this is ARITHMETIC ON A DESIGN and not a pre-registration of a
measurement.  It answers the question r7319 put -- a per-seat comparison needs a within-unit
reference -- by measuring the one spread this seat can measure on data already read (r7320's 40 rows)
and then costing the one it cannot.
"""
import itertools
import math

K, N = 27, 40                      # r7320's own result: withdrawn of drawn
GAP_SEAT = 0.153                   # r7299's between-seat gap, the figure the campaign was calibrated on
GAP_READER = 0.300                 # 70's measured between-agent gap on the SAME keys (r7319 ruling 3)
Z95, Z80 = 1.959963985, 0.8416212336


def wilson(k, n, z=Z95):
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (c - h) / d, (c + h) / d


def split_half_exact(k, n):
    """the exact distribution of |p1 - p2| over every way of splitting n rows into two halves.

    Hypergeometric: of the n/2 rows in the first half, j are withdrawals.  This is the SAMPLING
    spread of one reader's own verdicts -- it is NOT reader disagreement, which needs two readers.
    """
    h = n // 2
    tot = math.comb(n, h)
    out = []
    for j in range(max(0, h - (n - k)), min(h, k) + 1):
        w = math.comb(k, j) * math.comb(n - k, h - j)
        d = abs(j / h - (k - j) / h)
        out.append((d, w / tot))
    mean = sum(d * p for d, p in out)
    var = sum(p * d * d for d, p in out) - mean * mean
    p95 = 0.0
    acc = 0.0
    for d, p in sorted(out):
        acc += p
        if acc >= 0.95:
            p95 = d
            break
    return mean, math.sqrt(max(var, 0.0)), p95


def n_two_proportion(delta, p1, power_z=Z80, alpha_z=Z95):
    """rows PER UNIT to resolve a difference `delta` between two units, independent reads."""
    p2 = p1 - delta
    v = p1 * (1 - p1) + p2 * (1 - p2)
    return math.ceil((alpha_z + power_z) ** 2 * v / (delta * delta))


def m_paired_bound(bound, discord, alpha_z=Z95):
    """double-read keys PER UNIT to bound a reader difference below `bound`, paired."""
    return math.ceil(alpha_z ** 2 * discord / (bound * bound))


def floor_between(n, p1, alpha_z=Z95):
    """the 95% half-width on a difference between two units of n rows each -- its NOISE FLOOR."""
    return alpha_z * math.sqrt(2 * p1 * (1 - p1) / n)


def m_unpaired_bound(bound, p1, alpha_z=Z95):
    """the same bound with two independent reads of different keys -- the conservative form."""
    return math.ceil(alpha_z ** 2 * 2 * p1 * (1 - p1) / (bound * bound))


if __name__ == '__main__':
    p = K / N
    lo, hi = wilson(K, N)
    mean, sd, p95 = split_half_exact(K, N)
    print(f'r7320 read {K} of {N} = {100 * p:.1f}%  (Wilson {100 * lo:.1f}-{100 * hi:.1f})')
    print(f'  binomial SE                      {100 * math.sqrt(p * (1 - p) / N):.1f} points')
    print(f'  exact split-half |p1-p2|: mean   {100 * mean:.1f} points,  sd {100 * sd:.1f},'
          f'  95th pct {100 * p95:.1f}')
    print()
    print(f'rows per seat to resolve a {100 * GAP_SEAT:.1f}-point between-seat gap at 80% power: '
          f'{n_two_proportion(GAP_SEAT, p)}')
    print(f'rows per seat to resolve a {100 * GAP_READER:.1f}-point gap at 80% power:            '
          f'{n_two_proportion(GAP_READER, p)}')
    print()
    print('  the NOISE FLOOR of a between-unit difference, 95 per cent half-width:')
    for n in (N, 69, n_two_proportion(GAP_SEAT, p)):
        print(f'    at {n:3d} keys per unit: {100 * floor_between(n, p):.1f} points'
              f"   {'-- the gap is INSIDE it' if GAP_SEAT < floor_between(n, p) else '-- outside'}")
    print()
    print(f'double-read keys per seat to bound a reader difference under {100 * GAP_SEAT:.1f} points:')
    print(f'  paired, at 70\'s observed discordance of {100 * GAP_READER:.0f}%: '
          f'{m_paired_bound(GAP_SEAT, GAP_READER)}')
    print(f'  unpaired (different keys), conservative:            '
          f'{m_unpaired_bound(GAP_SEAT, p)}')
