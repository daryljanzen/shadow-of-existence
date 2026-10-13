#!/usr/bin/env python3
"""r7297+70: how many keys, read three ways, before a convergence difference is believable.

The per-key score is MEAN PAIRWISE AGREEMENT among three blind readers: 1 (unanimous), 1/3 (two of three), 0 (all differ).
Its distribution is taken from the 44 three-way keys of THREE_READERS.tsv (66, r7297).  Two arms of n keys each are
compared one-sided at alpha = 0.05 with power 0.80:

    n = 2 sigma^2 (z_alpha + z_beta)^2 / delta^2          (normal approximation)

and the approximation is checked by simulation: the null arm draws from the empirical distribution; the alternative arm
moves probability mass from 1/3 to 1 until its mean is delta higher -- which is what a rule that settles a two-of-three
split does -- and a Welch one-sided test (normal reference) is run 20,000 times per n.

    python3 power.py
"""
import math
import os
import random
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.join(HERE, '..', 'r7297_66_three_readers', 'THREE_READERS.tsv')
ZA, ZB = 1.6449, 0.8416


def scores():
    out = []
    for ln in open(T, encoding='utf-8'):
        if ln.startswith('#') or not ln.strip():
            continue
        a, b, c = ln.rstrip('\n').split('\t')[2:5]
        out.append(((a == b) + (a == c) + (b == c)) / 3)
    return out


def n_formula(sd, delta):
    return math.ceil(2 * sd * sd * (ZA + ZB) ** 2 / (delta * delta))


def power(dist, delta, n, reps=20000, rng=random.Random(7297)):
    vals = sorted(dist)
    p = {v: dist[v] for v in vals}
    m = delta / (1 - 1 / 3)                               # mass moved from 1/3 to 1 raises the mean by m * 2/3
    alt = dict(p)
    alt[1 / 3] -= m
    alt[1.0] += m
    if alt[1 / 3] < 0:
        return float('nan')
    hits = 0
    for _ in range(reps):
        x = rng.choices(vals, [p[v] for v in vals], k=n)
        y = rng.choices(vals, [alt[v] for v in vals], k=n)
        mx, my = sum(x) / n, sum(y) / n
        vx = sum((t - mx) ** 2 for t in x) / (n - 1)
        vy = sum((t - my) ** 2 for t in y) / (n - 1)
        se = math.sqrt(vx / n + vy / n) or 1e-9
        hits += (my - mx) / se > ZA
    return hits / reps


def main():
    s = scores()
    c = Counter(round(v, 4) for v in s)
    dist = {v: c[round(v, 4)] / len(s) for v in (0.0, 1 / 3, 1.0)}
    mu = sum(s) / len(s)
    sd = math.sqrt(sum((v - mu) ** 2 for v in s) / len(s))
    print(f'  44 keys: mean pairwise {mu:.3f}, sd {sd:.3f}, unanimous {c[1.0]}, two-of-three {c[round(1/3, 4)]}, '
          f'all differ {c[0.0]}')
    print('  delta | n per arm (formula) | simulated power at that n | keys, rule vs no rule | reads (x3)')
    for d in (0.10, 0.15, 0.20):
        n = n_formula(sd, d)
        print(f'  {d:.2f}  | {n:>4} | {power(dist, d, n):.3f} | {2 * n} | {6 * n}')


if __name__ == '__main__':
    main()
