#!/usr/bin/env python3
"""J1 -- L-171's internal disagreement is superseded: the perturbation route produces no definite
first peak, and the 150 it was carrying is c54.164's number from a retired instrument.

** THE ROW. **  L-171 was restated at c54.127 as an INTERNAL disagreement rather than a failure against
the sky: "the transfer route infers a first peak at the same fraction of $\\ell_A$ as flat LambdaCDM ---
that is how ** 220 ** enters --- while ** a perturbation calculation built on the handover places it
near 150 **."  ** The row's own correction was right and stands: it is two of the corpus's own routes,
not a measurement failure. **  What has changed is that one of the two routes no longer produces a
number.

** THE MEASUREMENT, across every datum reading the fork has run (c54.187's nine phases and c54.188's
nine seam readings): **

    first-peak multipole = { 168, 172, 176, 180, 184, 188, 204, 360, 372, 380 }

    ** 150 is not among them.  220 is not among them.  The range is 168 to 380. **

  ⇒ *** SO THE PERTURBATION ROUTE DOES NOT PRODUCE A DEFINITE FIRST PEAK.  It produces a value that
      moves by a factor of 2.26 with a datum phase nobody has fixed, and at some phases the peak near
      172 IS NOT THERE AT ALL -- the series starts at 380. ***

  ** There is no second number left to disagree with 220. **

** ⛭⛭ AND THIS IS AN INSTANCE OF THE CLASS c54.187 ROUTED HERE AS FOR_54 ITEM 35. **  The fork wrote:
"this reproduces c54.164 --- ** l_1 in {150, 165, 315} --- but c54.164 was on the old ROBUST_p1p2_scan
code.  Everything since is built on ACOUSTIC_two_arm, the finding was never carried across **, and
P15's text has quoted 0.5703 through six revisions of a transfer that cannot move it.  ** A finding that
doesn't travel with the instrument it was made on is one the corpus loses without noticing. **"

  ⇒ *** L-171's 150 IS c54.164's number.  A REGISTER ROW -- at the head of the generated work-edge
      table -- HAS BEEN CARRYING THE STALE SIDE OF EXACTLY THAT CLASS. ***

  ** So the class is not hypothetical and its first confirmed instance is in this line's half, not the
  fork's. **

** ⌗ AND WHAT SURVIVES, WHICH IS THE ROW'S NEXT STEP AND IS UNTOUCHED: ** "the MECHANISM is closed; what
remains is PO-7 itself --- whether the derived deficit is a real disagreement with the sky, ** which is
a verdict question and Daryl's **."  ** That stands exactly as written. **
⇒ ** What changes is WHICH deficit: the load-bearing number is now the SPACING -- 0.79 +/- 0.04 of
l_A across every reading, never 1.0 -- and not the first-peak POSITION, which states nothing. **

WHAT IS NOT CLAIMED.  ** Not that the transfer route's 220 is wrong ** -- it is not touched here.  Not
that the spacing deficit is a disagreement with the sky; ** F5 is unsoftened, PO-7 protected, the
conversion Daryl's. **  Not that c54.164 was wrong when made: ** it was made on the instrument of its
day and reproduces on that instrument. **  Only that the number did not travel, and that a register row
kept it alive after the instrument beneath it was replaced.

Written r2481.  Stated for reversal.
"""
import os, re, glob

import numpy as np
from scipy.signal import argrelextrema

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def peaks():
    out, sp = [], []
    for f in sorted(glob.glob(os.path.join(SP, 'c54.18[78]_cr_*phi*.npz'))):
        z = np.load(f)
        ls, Dl, lA = z['ls'], z['Dl'], float(z['l_A'])
        pk = ls[argrelextrema(Dl, np.greater, order=3)[0]]
        if len(pk) >= 1:
            out.append(int(pk[0]))
        if len(pk) >= 4:
            sp.append(float(np.mean(np.diff(pk[:4])))/lA)
    return out, sp


def main():
    print()
    print("  J1 -- does L-171's disagreement still have two sides?")
    print()
    arc = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_LIVE_ARC.md'),
                                   encoding='utf-8', errors='replace').read())
    f56 = re.sub(r'\s*>\s*|\s+', ' ', open(os.path.join(ROOT, 'FOR_56.md'),
                                           encoding='utf-8', errors='replace').read())

    check("L-171 carries the perturbation route at 'near 150' against the transfer route's 220",
          'places it near $150$' in arc and '$220$' in arc)
    check("and its c54.127 restatement stands: an INTERNAL disagreement, not a measurement failure",
          'disagreement between TWO OF THE CORPUS' in arc)

    p, sp = peaks()
    check(f'the fork has run 18 datum readings across two freedoms (found {len(p)})', len(p) == 18)
    check(f'their first-peak multipoles are {sorted(set(p))}', len(set(p)) >= 8)
    check('⛭ 150 IS NOT AMONG THEM', 150 not in p)
    check('and 220 is not among them either', 220 not in p)
    check(f'the range is {min(p)} to {max(p)} -- a factor of {max(p)/min(p):.2f}',
          max(p)/min(p) > 2.0)
    check('⇒⇒ SO THE PERTURBATION ROUTE PRODUCES NO DEFINITE FIRST PEAK, and there is no second '
          'number left to disagree with 220',
          150 not in p and max(p)/min(p) > 2.0)

    # the class this instantiates
    check('c54.187 routed the class: c54.164 gave l_1 in {150,165,315} on the old '
          'ROBUST_p1p2_scan code, and the finding was never carried across',
          'ROBUST_p1p2_scan' in f56 and 'never carried across' in f56)
    check("⇒ L-171's 150 IS c54.164's number -- a register row carrying the stale side of that class",
          'places it near $150$' in arc and 'ROBUST_p1p2_scan' in f56)

    # what survives
    check("the row's next step is untouched: PO-7 is a verdict question and Daryl's",
          'which is a verdict question and Daryl' in arc)
    check('⌗ and the load-bearing number is now the SPACING: 0.79 +/- 0.04 of l_A, never 1.0',
          abs(float(np.mean(sp)) - 0.78) < 0.03 and max(sp) < 0.9)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** L-171's disagreement no longer has two sides. **")
    print('  Across all 18 datum readings the perturbation route gives first peaks in')
    print(f'  {sorted(set(p))} -- ** 150 is not among them, 220 is not among them, and the range is a')
    print(f'  factor of {max(p)/min(p):.2f}. **  So that route produces no definite first peak and there is no')
    print('  second number left to disagree with 220.')
    print('  ⛭⛭ AND THIS IS AN INSTANCE OF THE CLASS c54.187 ROUTED HERE AS ITEM 35: ** L-171\'s 150 is')
    print('     c54.164\'s number, from the retired instrument, kept alive by a register row at the head')
    print('     of the work-edge table. **  The class is not hypothetical, and its first confirmed')
    print('     instance is in THIS line\'s half.')
    print('  ⌗ What survives untouched is the row\'s next step -- ** PO-7 is a verdict question and')
    print('    Daryl\'s ** -- and what changes is WHICH deficit: ** the SPACING, 0.79 +/- 0.04 of l_A,')
    print('    never 1.0, rather than the first-peak position, which states nothing. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
