#!/usr/bin/env python3
r"""cost.py -- the two registered bands of r7332's first stride, with their decisive fractions.

Committed and pushed BEFORE one receipt is repaired.  r7331 ④⑤ orders the per-receipt cost reported
with a band and its decisive fraction registered first, and r7329 ④ makes the decisive fraction
standing on every registration after 70 weighted the U-PASS class at 0.002.

The decisive fraction here is 70's weighted form, credited: the probability that the outcome lands
OUTSIDE the registered band GIVEN THE REGISTRATION'S OWN CENTRAL.  A band whose weighted fraction is
near zero could not have failed even if its own prediction were right, which is the thing this seat's
r7328 declaration and r7325's standing rule are about.

Both outcome spaces are small integers and are enumerated exactly -- no continuum, no simulation.
"""
import io
import os
from math import comb

HERE = os.path.dirname(os.path.abspath(__file__))

# ── arm (a): the figure the order asks for ────────────────────────────────────────────────────────
A_SPACE = 9          # the receipts of the first two blocks: L147_two_arm 5, L165_defining_the_sum 4
A_CENTRAL = 6        # this seat's own prediction, registered
A_BAND = (5, 9)      # refutation at or below 4

# ── arm (b): the quantity that decides whether the AMENDMENT holds ────────────────────────────────
B_SPACE = 13         # the owed rows of L147_two_arm, every one decided by cc66's Test 5 clause
B_CENTRAL = 10       # this seat's own prediction, registered
B_BAND = (9, 13)     # refutation at or below 8


def binom(n, p):
    return [comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(n + 1)]


def decisive(space, central, band):
    """70's weighted decisive fraction: P(outside the band | the registration's own central)."""
    d = binom(space, central / space)
    lo, hi = band
    return sum(d[:lo]) + sum(d[hi + 1:]), d


def owed_rows(prefix):
    """the owed rows of a prefix, read off the trunk's ledger rather than retyped."""
    out = []
    p = os.path.join(HERE, '..', '..', '..', 'corpus', 'quote_pin_baseline.tsv')
    for l in io.open(p, encoding='utf-8'):
        c = l.rstrip('\n').split('\t')
        if len(c) >= 7 and c[0].startswith('receipts/') and c[5] == 'REPAIR-OWED' and prefix in c[0]:
            out.append(c)
    return out


if __name__ == '__main__':
    rows = owed_rows('/L147_two_arm/')
    recs = sorted({c[0] for c in rows})
    print(f'the first block as the ledger carries it: {len(rows)} owed rows in {len(recs)} receipts')
    for r in recs:
        n = sum(1 for c in rows if c[0] == r)
        print(f'   {n:2d}  {r.split("/")[-1]}')
    assert len(rows) == B_SPACE and len(recs) == 5, (
        f'the stride says 13 rows in 5 receipts; the ledger says {len(rows)} in {len(recs)}')
    print()
    for nm, space, central, band, what in (
            ('a', A_SPACE, A_CENTRAL, A_BAND,
             'receipts of the first two blocks fully repaired in this one revision'),
            ('b', B_SPACE, B_CENTRAL, B_BAND,
             'L147 rows repaired by the named form WITHOUT a rule case written beside them')):
        frac, d = decisive(space, central, band)
        lo, hi = band
        print(f'── arm ({nm}): {what}')
        print(f'   space 0–{space};  central {central};  band {lo}–{hi};  '
              f'refutation at or below {lo - 1}')
        print(f'   ⇒ DECISIVE FRACTION {frac:.3f}   '
              f'({"FAILABLE" if frac >= 0.10 else "WEAKLY DECISIVE -- said so in the registration"})')
        print(f'   the outcome space, weighted at the central: '
              f'{[round(x, 3) for x in d]}')
        print()
    print('for comparison, the figures 70 published at r7327: this seat\'s r7320 band 0.002, '
          'W-c 0.000,\n   r7311 IS IT A RULE 0.926, and 16 of 25 U-PASS entries below 0.10')
