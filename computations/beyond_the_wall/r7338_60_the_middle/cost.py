#!/usr/bin/env python3
"""r7338+60 -- THE MIDDLE OF THE STRIDE: the arithmetic of the registration, written and pushed
BEFORE the first repair of this revision.

** WHAT WAS ORDERED. **  `r7337` ④: *carry on through the middle of the stride -- the tail is closed
and the dense blocks are done, so what is left is the part the `3.31` rows-a-receipt figure actually
prices.  Report both readings with the assignment named, which is standing; AND from this revision
also report the keys MINTED AND ADJUDICATED beside the owed count, because a falling owed count is
not by itself a measure of what the corpus gained.*

⛭ ** THE SECOND REPORT IS THE NEW ONE AND IT COMES FROM ANOTHER SEAT'S OWN FAILURE. **  `cc66` found
that `7` of `10` of its retired rows went into text the quote-pin instrument does not read as a pin
at all -- so the row left the owed list and nothing took its place in the ledger.  *This seat met the
same class one revision ago from the other side: two of its own minted rows came back STALE because a
normaliser applied inside a receipt's reader mints no key.*  ⇒ ** So the quantity below is the share
of retired rows whose replacement the INSTRUMENT CANNOT SEE, and it is registered two-sidedly. **

** COMPUTES: ** the two registered bands and their decisive fractions under an exact binomial, and
the census of this revision's block read at a pinned commit.  No paper quantity.
"""
import collections
import io
import os
import subprocess
from math import comb

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    '..', '..', '..'))

# ── the census commit: the block is read HERE, before the registration commit itself ─────────────
CENSUS = 'b850ed71'
PREFIXES = ('L165_interacting_tower', 'L211_closure_adjacency',
            'L175_dimensional_descent', 'L204_physics_reach')

# ── arm ⒜: receipts of this block CLOSED in this revision ────────────────────────────────────────
#   The same arbiter as the two strides before it: a receipt counts as closed only when every one of
#   its owed rows is repaired or withdrawn WITH ITS CASE, its minted keys are adjudicated in the
#   same push, and the receipt re-runs green.
A_SPACE = 19
A_CENTRAL = 11
A_BAND = (9, 14)
#   ⌗ *AND THE POPULATION IS DELIBERATELY LARGER THAN THE EXPECTED RATE.*  The tail's arm was
#   CENSORED at its own ceiling because the population was `14` and the rate came in at `14`; this
#   block holds `19` receipts against a central of `11`, so the arm can fail in BOTH directions and
#   a clean sweep is not the only way to land high.

# ── arm ⒝: the share of retired rows whose replacement the instrument cannot see ─────────────────
#   A retired row's replacement is INSTRUMENT-READ when the minted ledger row survives the quote-pin
#   gate's own stale check -- the gate reports a key the instrument does not report as STALE, so the
#   measurement is the gate's and not this seat's reading of it.  A row counts as INVISIBLE when its
#   repair mints no key at all (a structural assertion parsed out of a syntax tree), when its
#   replacement is a form the instrument cannot key (a literal normalised at comparison time), or
#   when it is withdrawn.
B_CENTRAL = 0.15
B_BAND = (0.08, 0.22)
B_MIN_READABLE = 30
#   ⚠ *TWO-SIDED ON PURPOSE.*  Failing LOW says the class `cc66` found barely touches this seat's
#   repairs; failing HIGH says the invisibility is systemic and the owed count is measuring the
#   wrong thing.  ** Both are results, and `cc66`'s own figure on the same quantity was `0.70`. **

RESULT = {}                     # filled by the result block appended after the stride


def decisive(space, central, band):
    """P(outcome outside the band | the registration's own central), exact binomial."""
    p = central / space
    return sum(comb(space, k) * p ** k * (1 - p) ** (space - k)
               for k in range(space + 1) if k < band[0] or k > band[1])


def decisive_share(n, central, band):
    """the same number for a band stated as a SHARE, at a given size"""
    lo, hi = band[0] * n, band[1] * n
    return sum(comb(n, k) * central ** k * (1 - central) ** (n - k)
               for k in range(n + 1) if k < lo or k > hi)


def _ledger(sha=CENSUS):
    text = (subprocess.run(['git', '-C', ROOT, 'show', f'{sha}:corpus/quote_pin_baseline.tsv'],
                           capture_output=True, text=True, errors='replace').stdout if sha
            else io.open(os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv'),
                         encoding='utf-8').read())
    return [l.split('\t') for l in text.split('\n') if l.startswith('receipts/')]


def block(sha=CENSUS):
    """{receipt: owed rows} for this revision's block, read at the census commit"""
    return collections.Counter(c[0] for c in _ledger(sha)
                               if c[5] == 'REPAIR-OWED' and c[0].split('/')[1] in PREFIXES)


def mine(sha=CENSUS):
    """the whole of this seat's remaining stride at the census commit"""
    import io as _io
    pref = {l.split('\t')[1] for l in subprocess.run(
        ['git', '-C', ROOT, 'show', f'{sha}:THE_REPAIR_STRIDE.tsv'],
        capture_output=True, text=True, errors='replace').stdout.split('\n')
        if l and not l.startswith('#') and l.split('\t')[0] == '60'}
    del _io
    return collections.Counter(c[0] for c in _ledger(sha)
                               if c[5] == 'REPAIR-OWED' and c[0].split('/')[1] in pref)


def scored():
    """the two arms against their registered bands, from the result block"""
    out = {}
    got_a = RESULT.get('A_CLOSED')
    out['a'] = ((got_a, A_BAND, A_BAND[0] <= got_a <= A_BAND[1], decisive(A_SPACE, A_CENTRAL, A_BAND))
                if got_a is not None else (None, A_BAND, None, decisive(A_SPACE, A_CENTRAL, A_BAND)))
    inv, ret = RESULT.get('B_INVISIBLE'), RESULT.get('B_RETIRED')
    if inv is None or not ret:
        out['b'] = (None, B_BAND, None, decisive_share(B_MIN_READABLE, B_CENTRAL, B_BAND))
        return out
    share = inv / ret
    out['b'] = (share, B_BAND, B_BAND[0] <= share <= B_BAND[1],
                decisive_share(ret, B_CENTRAL, B_BAND))
    return out


if __name__ == '__main__':
    _b = block()
    _m = mine()
    print()
    print('  r7338+60 -- THE MIDDLE OF THE STRIDE, REGISTERED BEFORE THE FIRST REPAIR')
    print()
    print(f'    this seat\'s remaining stride at {CENSUS}: {sum(_m.values())} rows in {len(_m)} '
          f'receipts, {sum(_m.values()) / len(_m):.2f} a receipt')
    print(f'    this revision\'s block, four prefixes: {sum(_b.values())} rows in {len(_b)} '
          f'receipts, {sum(_b.values()) / len(_b):.2f} a receipt -- the forward figure, not an end')
    print()
    print(f'    arm (a): central {A_CENTRAL} of {A_SPACE}, band {A_BAND[0]}-{A_BAND[1]}, '
          f'decisive {decisive(A_SPACE, A_CENTRAL, A_BAND):.3f}')
    print(f'    arm (b): central {B_CENTRAL}, band {B_BAND[0]}-{B_BAND[1]}, two-sided, '
          f'decisive {decisive_share(sum(_b.values()), B_CENTRAL, B_BAND):.3f} at '
          f'{sum(_b.values())} retired rows '
          f'({decisive_share(B_MIN_READABLE, B_CENTRAL, B_BAND):.3f} at the minimum readable '
          f'{B_MIN_READABLE})')
    print()
    for _r, _n in sorted(_b.items()):
        print(f'      {_n}  {_r}')
    print()
