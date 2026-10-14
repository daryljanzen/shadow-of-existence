#!/usr/bin/env python3
"""r7336+60 -- THE SPAN-LENGTH EXPERIMENT's DESIGN, written and pushed BEFORE the first count.

`r7335` ② ordered it: the quantity, the band, the decisive fraction and `N` fixed first, with the
symmetric negative registered beside the prediction.  ** This file fixes them and counts NOTHING:
every function here either prices a band or inventories a POPULATION, and the outcome functions
raise until the counting revision fills them. **

** COMPUTES: ** the two arms' bands and their decisive fractions under an exact binomial, the
retrospective arm's minimum readable size, and the prospective arm's two span inventories read at
pinned commits.  No paper quantity, and no outcome.
"""
import io
import os
import subprocess
from math import comb

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    '..', '..', '..'))

# ── the pins ─────────────────────────────────────────────────────────────────────────────────────
PIN = '23cecc99'                # the commit the retrospective population is cut at
MINE = '2fda7677'               # this seat's own spans for the five twice-repaired receipts
TRUNK_FRONT = 'r7335'           # the front at this registration; arm ⒜'s window starts here
N_REVISIONS = 8                 # arm ⒜'s window, in revision ids on the trunk
FIVE = ('receipts/L147_two_arm/B2_the_prose_duplicate_did_not_reach_main.py',
        'receipts/L147_two_arm/B3_a_dichotomy_stated_is_not_a_dichotomy_proved.py',
        'receipts/L147_two_arm/B8_the_zero_velocity_band_is_a_third_of_the_gap.py',
        'receipts/L147_two_arm/B9_the_admissible_pair_is_forced_not_merely_distinguished.py',
        'receipts/L147_two_arm/B10_the_thermal_mechanism_needs_an_exponential_approach.py')

# ── arm ⒜: prospective, as ordered ───────────────────────────────────────────────────────────────
A_PREDICTION = 'the 70-side count exceeds the 60-side count'
A_NEGATIVE = ('equal counts at N -- both zero included -- leave the length argument UNSUPPORTED, '
              'and the rule stands on claim-completeness and uniqueness alone')
A_HAZARD_ASSUMED = 0.10         # per span per window, for the power statement only

# ── arm ⒝: retrospective, stratified by span length ──────────────────────────────────────────────
B_NULL = 1 / 3                  # staleness independent of length
B_CENTRAL = 0.50
B_BAND = (0.42, 1.00)
B_MIN_READABLE = 30             # below this the arm is declared UNDERPOWERED, not read


def decisive_share(n, central, band):
    """P(share outside the band | the registration's own central), exact binomial on `n` draws.

    `r7325`'s standing rule in `70`'s weighted form: the number that says whether a band could have
    failed at the size it will be scored at.  Stated here for the sizes this population can give.
    """
    lo, hi = band[0] * n, band[1] * n
    return sum(comb(n, k) * central ** k * (1 - central) ** (n - k)
               for k in range(n + 1) if k < lo or k > hi)


def zero_zero(n_per_side, hazard=A_HAZARD_ASSUMED):
    """arm ⒜'s own power statement: the chance that NEITHER side has a touched span."""
    return (1 - hazard) ** (2 * n_per_side)


def _ledger(sha):
    text = (subprocess.run(['git', '-C', ROOT, 'show', f'{sha}:corpus/quote_pin_baseline.tsv'],
                           capture_output=True, text=True, errors='replace').stdout if sha
            else io.open(os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv'),
                         encoding='utf-8').read())
    return [l.split('\t') for l in text.split('\n') if l.startswith('receipts/')]


def sides():
    """arm ⒜'s two inventories, read at pinned commits: {'70': [...], '60': [...]}.

    The `70`-side is what the trunk carries on the five receipts; the `60`-side is what this seat
    asserted on the same receipts, recoverable from the ledger at its own last content commit.
    ** An inventory is not an outcome: nothing here asks whether a span is still present. **
    """
    # ⌗ both sides are restricted to the spans each seat MINTED for the thirteen owed rows, by the
    #   revision stamp in each row's note -- not to every span the receipts carry, or the
    #   comparison would put one seat's repair against the other seat's whole history.
    now = [c for c in _ledger(PIN) if c[0] in FIVE and 'r7329+70' in c[6]]
    mine = [c for c in _ledger(MINE) if c[0] in FIVE and 'r7332+60' in c[6]]
    return {'70': [c[1][1:-1] for c in now], '60': [c[1][1:-1] for c in mine]}


def population():
    """arm ⒝'s population, cut at `PIN`: the rows whose verdict there was not REPAIR-OWED.

    Returned with each row's span length in characters, which is what the terciles are cut on.
    ** No presence test is run here: membership is decided at the pin, the outcome at HEAD, and the
    outcome belongs to the counting revision. **
    """
    return [(c[0], c[1][1:-1], c[2], len(c[1]) - 2)
            for c in _ledger(PIN) if c[5] != 'REPAIR-OWED']


def terciles(lengths):
    """the population's own length terciles, cut at the pin -- the strata, fixed before the count"""
    s = sorted(lengths)
    if not s:
        return (0, 0)
    return (s[len(s) // 3], s[2 * len(s) // 3])


def outcome():
    """filled by the counting revision.  ** Registered as unfilled: a design that can report a
    number before its own counting commit is a design that could have chosen the number. **"""
    raise NotImplementedError('arm ⒜ and arm ⒝ are counted in a later revision, not here')


if __name__ == '__main__':
    _s = sides()
    _pop = population()
    _lens = [p[3] for p in _pop]
    _t = terciles(_lens)
    print()
    print('  r7336+60 -- THE SPAN-LENGTH EXPERIMENT, REGISTERED BEFORE ANY COUNT')
    print()
    print(f'    arm (a), prospective, window N = {N_REVISIONS} revision ids from {TRUNK_FRONT}:')
    print(f'      70-side spans on the five receipts: {len(_s["70"])};  '
          f'60-side spans for the same rows: {len(_s["60"])}')
    print(f'      prediction: {A_PREDICTION}')
    print(f'      the symmetric negative: {A_NEGATIVE}')
    print(f'      power, stated in advance: P(no span touched on either side) = '
          f'{zero_zero(min(len(_s["70"]), len(_s["60"]))):.3f} at an assumed hazard of '
          f'{A_HAZARD_ASSUMED}')
    print()
    print(f'    arm (b), retrospective, population cut at {PIN}:')
    print(f'      rows in the population: {len(_pop)};  span length terciles (chars): '
          f'<= {_t[0]} | <= {_t[1]} | >')
    print(f'      quantity: the share of the STALE set in the LONGEST tercile;  null {B_NULL:.3f}, '
          f'central {B_CENTRAL}, band {B_BAND[0]}-{B_BAND[1]}')
    for _n in (B_MIN_READABLE, 40, 60):
        print(f'      decisive at n={_n}: {decisive_share(_n, B_CENTRAL, B_BAND):.3f}')
    print(f'      below {B_MIN_READABLE} stale rows the arm is declared UNDERPOWERED and not read')
    print()
