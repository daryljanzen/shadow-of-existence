#!/usr/bin/env python3
"""r7336+60 -- THE CHEAP TAIL: the arithmetic of the registration, written and pushed BEFORE the
first repair of this revision.

** WHAT THIS PRICES. **  `r7333` ④ ordered the single-row tail next rather than another dense block,
because the per-receipt cost is measured on the expensive end alone and the cheap end is unmeasured.
The figure to report again is RECEIPTS A REVISION, with its band and its decisive fraction registered
first -- and it is what the re-stated trigger reads, which is now the pooled rate's DIRECTION over
two further revisions rather than a boundary at `8`.

⚠ ** AND THE CHEAP END CANNOT BE MEASURED TO COMPLETION IN ONE REVISION, WHICH IS REGISTERED HERE
RATHER THAN DISCOVERED AFTER. **  The tail this seat holds is `15` receipts of exactly one owed row,
of which `1` is on the do-not-edit list and is routed as a patch, so `14` can close.  *** A rate
whose population is `14` cannot report a number above `14`: if every one of them closes the outcome
is CENSORED and the measurement supports only `>= 14`, never an equality. ***  That is stated before
the draw because a censored result read as a point estimate would understate the cheap end exactly
when it is cheapest.

** COMPUTES: ** the two registered bands, their decisive fractions under an exact binomial on the
tail's own size, and the census of the tail read at a pinned commit.  No paper quantity.
"""
import collections
import io
import os
import subprocess
from math import comb

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    '..', '..', '..'))

# ── the census commit: the tail is read HERE, before the registration commit itself ──────────────
CENSUS = '23cecc99'

# ── arm ⒜: receipts of the single-row tail CLOSED in this revision ───────────────────────────────
#   A receipt counts as closed only when its one owed row is repaired or withdrawn WITH ITS CASE
#   WRITTEN DOWN, its minted key is adjudicated in the same push, and the receipt re-runs green.
A_SPACE = 14                    # the editable tail: 15 receipts less the one on the do-not-edit list
A_CENTRAL = 11
A_BAND = (10, 14)               # right-censored at the population's own size

# ── arm ⒝: how many of the tail's rows need something OTHER than a plain widening ────────────────
#   A withdrawal with its case, a reader normalisation, or a routed patch -- anything the named
#   repair form alone does not close.  In the dense blocks it was `1` withdrawal in `39` rows.
B_SPACE = 14
B_CENTRAL = 2
B_BAND = (1, 4)                 # two-sided: ZERO fails it as surely as five does

BARRED = 1                      # `L259/D1`, routed as a patch and not edited

RESULT = {}                     # filled by the result block appended after the stride


def decisive(space, central, band):
    """P(outcome outside the band | the registration's own central), exact binomial.

    ** The number that says whether a band could have failed at the size it will be scored at. **
    `r7325`'s standing rule; `70`'s weighted form, credited there.
    """
    p = central / space
    return sum(comb(space, k) * p ** k * (1 - p) ** (space - k)
               for k in range(space + 1) if k < band[0] or k > band[1])


def _ledger(sha=CENSUS):
    text = (subprocess.run(['git', '-C', ROOT, 'show', f'{sha}:corpus/quote_pin_baseline.tsv'],
                           capture_output=True, text=True, errors='replace').stdout if sha
            else io.open(os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv'),
                         encoding='utf-8').read())
    return [l.split('\t') for l in text.split('\n') if l.startswith('receipts/')]


def _my_prefixes(sha=CENSUS):
    text = subprocess.run(['git', '-C', ROOT, 'show', f'{sha}:THE_REPAIR_STRIDE.tsv'],
                          capture_output=True, text=True, errors='replace').stdout
    return {l.split('\t')[1] for l in text.split('\n')
            if l and not l.startswith('#') and l.split('\t')[0] == '60'}


def tail(sha=CENSUS):
    """the receipts of this seat's stride holding EXACTLY ONE owed row, read at the census commit"""
    pref = _my_prefixes(sha)
    owed = collections.Counter(c[0] for c in _ledger(sha)
                               if c[5] == 'REPAIR-OWED' and c[0].split('/')[1] in pref)
    return sorted(r for r, n in owed.items() if n == 1)


def mine(sha=CENSUS):
    """the whole of this seat's stride at the census commit: {receipt: owed rows}"""
    pref = _my_prefixes(sha)
    return collections.Counter(c[0] for c in _ledger(sha)
                               if c[5] == 'REPAIR-OWED' and c[0].split('/')[1] in pref)


def scored():
    """the two arms against their registered bands, from the result block"""
    out = {}
    for nm, got, space, central, band in (
            ('a', RESULT.get('A_CLOSED'), A_SPACE, A_CENTRAL, A_BAND),
            ('b', RESULT.get('B_OTHER'), B_SPACE, B_CENTRAL, B_BAND)):
        if got is None:
            out[nm] = (None, band, None, decisive(space, central, band))
            continue
        out[nm] = (got, band, band[0] <= got <= band[1], decisive(space, central, band))
    return out


if __name__ == '__main__':
    _t = tail()
    _m = mine()
    print()
    print('  r7336+60 -- THE CHEAP TAIL, REGISTERED BEFORE THE STRIDE')
    print()
    print(f'    this seat\'s stride at {CENSUS}: {sum(_m.values())} rows in {len(_m)} receipts')
    print(f'    the single-row tail: {len(_t)} receipts, {BARRED} of them on the do-not-edit list '
          f'and routed, so {len(_t) - BARRED} can close')
    print(f'    rows in the rest: {sum(n for n in _m.values() if n > 1)} in '
          f'{sum(1 for n in _m.values() if n > 1)} receipts, '
          f'{sum(n for n in _m.values() if n > 1) / max(1, sum(1 for n in _m.values() if n > 1)):.2f}'
          f' a receipt against 1.00 here')
    print()
    for nm, space, central, band in (('a', A_SPACE, A_CENTRAL, A_BAND),
                                     ('b', B_SPACE, B_CENTRAL, B_BAND)):
        print(f'    arm ({nm}): central {central} of {space}, band {band[0]}-{band[1]}, '
              f'decisive {decisive(space, central, band):.3f}')
    print()
    for r in _t:
        print(f'      {"[routed]" if "/L259" in r else "        "} {r}')
    print()

# ══════════════════════════════════════════════════════════════════════════════════════════════════
# THE RESULT, appended after the stride and read by the receipt.  ** The registration above is
# untouched: nothing here moves a band, a central or a decisive fraction. **
# ══════════════════════════════════════════════════════════════════════════════════════════════════
RESULT.update({
    # arm ⒜ -- receipts of the tail closed.  ⚠ CENSORED AT THE CEILING, as registered: the tail is
    #   14 receipts long, so 14 supports `>= 14` and not an equality.
    'A_CLOSED': 14,
    # arm ⒝ -- rows needing something other than a plain widening.  ** OUTSIDE THE BAND, HIGH **,
    #   which is one of the two failures the registration named in advance.
    'B_OTHER': 9,
    #   its composition: 7 needed the markup normaliser the gate layer compares with (one of them a
    #   MARKDOWN carrier the gate layer's own normaliser does not reach), and 2 had no span to
    #   widen at all -- proxies on LIVE CODE, repaired by parsing the gate's syntax tree.
    'B_NORMALISED': 7,
    'B_STRUCTURAL': 2,
    'B_PLAIN': 5,
    # ** TWO distinct rule cases, carried on THREE rows: ** the markdown carrier, and -- found by
    #   the ledger instrument on the repair itself -- that the gate layer's normaliser cannot be
    #   reached from inside a receipt's reader without making the pin invisible to the instrument.
    'CASES': 2,
    'CASE_ROWS': 3,
    'ROUTED': 1,                # the row on the do-not-edit list, routed as a patch
    # why ⒝ failed, measured rather than asserted: the tail's rows are composed differently from
    # the dense blocks the band was priced on.
    'TAIL_MARKUP': 4, 'TAIL_ROWS': 15, 'BLOCK_MARKUP': 1, 'BLOCK_ROWS': 39,
    'TAIL_TOKEN': 7, 'BLOCK_TOKEN': 7,
})
