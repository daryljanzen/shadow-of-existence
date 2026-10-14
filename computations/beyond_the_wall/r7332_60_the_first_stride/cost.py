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
import subprocess
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


PREG = 'ad66413b'      # the commit that PUSHED this registration, before one receipt was repaired
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))


def owed_rows(prefix, sha=PREG):
    """the owed rows of a prefix, read off the ledger AT A PINNED COMMIT rather than live.

    Pinned because the claim is historical: what the block held when the bands were registered.
    Read live it would go to zero as the repairs land -- the fail-on-success shape this seat's own
    r7320 recipe cures by naming a commit.  Pass sha='' for the live tree.
    """
    if sha:
        text = subprocess.run(['git', '-C', ROOT, 'show', f'{sha}:corpus/quote_pin_baseline.tsv'],
                              capture_output=True, text=True, errors='replace').stdout
    else:
        text = io.open(os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv'),
                       encoding='utf-8').read()
    out = []
    for l in text.split('\n'):
        c = l.rstrip('\n').split('\t')
        if len(c) >= 7 and c[0].startswith('receipts/') and c[5] == 'REPAIR-OWED' and prefix in c[0]:
            out.append(c)
    return out


if __name__ == '__main__':
    rows = owed_rows('/L147_two_arm/')
    live = owed_rows('/L147_two_arm/', sha='')
    recs = sorted({c[0] for c in rows})
    print(f'the first block as the ledger carried it AT {PREG}: {len(rows)} owed rows in '
          f'{len(recs)} receipts;  live now: {len(live)} owed')
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


# ══════════════════════════════════════════════════════════════════════════════════════════════════
# THE RESULT.  Appended after the stride ran; the bands above are untouched and were pushed first.
# ══════════════════════════════════════════════════════════════════════════════════════════════════
A_DONE = 9            # receipts of the first two blocks fully repaired in this revision
B_CLEAN = 12          # L147 rows repaired by the named form with NO case written beside them
ROWS = 39             # owed rows the stride cleared
KEYS = 24             # keys the repairs minted
CASES = 2             # cases written beside a repair
STRIDE_RECEIPTS = 67  # this seat's whole stride, r7331 ②
CYCLE_TOP = 8         # the band's top, r7331 ①: past it and the secondment reverses


def scored():
    """both arms scored against the bands registered before the stride ran."""
    out = {}
    for nm, space, central, band, got in (('a', A_SPACE, A_CENTRAL, A_BAND, A_DONE),
                                          ('b', B_SPACE, B_CENTRAL, B_BAND, B_CLEAN)):
        frac, _ = decisive(space, central, band)
        out[nm] = (got, band, band[0] <= got <= band[1], frac)
    return out


if __name__ == '__main__' and os.environ.get('RESULT', '1') == '1':
    print()
    print('══ THE RESULT, against the bands pushed before the stride ran ══\n')
    for nm, (got, band, inside, frac) in scored().items():
        print(f'   arm ({nm}): {got}, band {band[0]}–{band[1]} ⇒ '
              f'{"INSIDE" if inside else "OUTSIDE"}   (decisive fraction {frac:.3f})')
    print()
    print(f'   {ROWS} owed rows cleared in {A_DONE} receipts, closing on {KEYS} minted keys, '
          f'with {CASES} cases filed')
    print(f'   ⇒ rows a receipt {ROWS / A_DONE:.2f};  keys a row {KEYS / ROWS:.2f} '
          f'-- below 1 because fragments of ONE sentence are ONE pin')
    print()
    print('══ WHAT IT SAYS ABOUT THE BOUND, AND THE PART THAT IS NOT MEASURED ══\n')
    print(f'   measured: {A_DONE} receipts in one revision, against 66\'s predicted 11–16 a cycle')
    print(f'   ⇒ this seat\'s {STRIDE_RECEIPTS} receipts at that rate: '
          f'{STRIDE_RECEIPTS / A_DONE:.1f} cycles, against a band top of {CYCLE_TOP}')
    print(f'   {"INSIDE" if STRIDE_RECEIPTS / A_DONE <= CYCLE_TOP else "PAST"} the top, '
          f'by {abs(CYCLE_TOP - STRIDE_RECEIPTS / A_DONE):.1f} of a cycle')
    print()
    print('   ⚠ AND THE RATE IS MEASURED ON THE EXPENSIVE END ONLY, which the order chose on purpose:')
    print('     the two blocks were the densest anyone holds and the Test-5 block, 4.33 rows a')
    print('     receipt.  The remaining 58 receipts of this stride average 2.67 rows each and the')
    print('     tail is single-row receipts, which the order asked to be priced SECOND and which this')
    print('     revision did not reach.')
    print(f'   ⇒ So {A_DONE} a revision is a LOWER bound on the rate and {STRIDE_RECEIPTS / A_DONE:.1f}')
    print('     cycles an UPPER bound on the cost.  The cheap end is unmeasured and the figure moves')
    print('     DOWN when it is measured, never up.')
