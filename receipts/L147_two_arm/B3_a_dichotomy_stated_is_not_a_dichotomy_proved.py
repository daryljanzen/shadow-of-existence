#!/usr/bin/env python3
"""B3 -- B1's verdict corrected: ruling out one horn established the other only if the pair was
exhaustive, and it was not.

** WHAT B1 (r2462) ESTABLISHED, AND IT STANDS: ** a shared upstream constant would corrupt both arms
identically; it does not; the LambdaCDM arm through the same code, grid, peak-finder and bins returns
l_1/l_A = 0.7300 against the sky's 0.7312.  ** That argument is correct and c54.187 credits it: "two
arms at essentially equal l_A with first peaks 21.8% apart still rules out l_1 = c*l_A." **

** WHAT L-235's ROW CLAIMED, AND IT DID NOT FOLLOW: ** "the alternative is decided."  The alternative
was the fork's own pair -- ** "evidence either of a ROBUST PREDICTION or of a SHARED UPSTREAM CONSTANT"
** -- and ruling out the second was read as establishing the first.

  ⇒ *** IT WAS A THIRD THING.  c54.187: Z_START is solved so that pi*D_M/r_s = 301.6, the first-peak
      modes are ALREADY SUB-HORIZON when integration begins, and their phase there is ASSIGNED rather
      than derived.  Scanning that one freedom moves l_1/l_A from 0.5703 to 1.2599 -- a 2.21x
      spread. ***

  ** So 0.5703 is a statement about the SEAM DATUM, and the datum is neither shared machinery nor a
  prediction. **

** AND THE FORK NAMES WHY B1 COULD NOT REACH IT, precisely: "the control never exercises the
ARM-SPECIFIC datum." **  The control is LambdaCDM, which carries its own datum; comparing the two arms
tests the SHARED machinery and nothing else.  ** B1 was correctly scoped and the row's disposition line
was not. **

*** THE RULE: RULING OUT ONE HORN OF A DICHOTOMY ESTABLISHES THE OTHER ONLY IF THE DICHOTOMY IS
    EXHAUSTIVE -- AND A DICHOTOMY SOMEONE STATED IN PASSING IS NOT A PROOF OF EXHAUSTIVENESS. ***

  ⌗ The fork wrote "either ... or" as an honest statement of what it could not separate, not as a
  theorem that those were the only two.  ** This line read a candid framing as a partition. **

** ⛭⛭ AND WHAT SURVIVES IS BETTER THAN WHAT FELL, which is the fork's own finding and is verified here
from its spectra: **

      phi      l_1    l_1/l_A   spacing/l_A
      0.0      172     0.5703      0.8046
      0.3927   172     0.5703      0.7913
      0.7854   184     0.6101      0.7692
      1.1781   380     1.2599      0.8090
      1.5708   380     1.2599      0.8090
      1.9635   204     0.6764      0.7339
      2.3562   188     0.6233      0.7737
      2.7489   188     0.6233      0.8046
      3.1416   188     0.6233      0.8179

  ** the first-peak ratio spreads 2.21x and is a datum artefact.
     THE SPACING SPREADS 1.11x, sits at 0.79 +/- 0.04 of l_A, AND IS NEVER 1.0. **

  ⇒ *** A ~21% SPACING DEFICIT SURVIVING EVERY PHASE IS A BETTER NUMBER THAN THE 22% POSITION DEFICIT
      THE PAPER CARRIED, AND THE FORK LANDED IT AND WITHDREW THE WEIGHT THE TEXT PUT ON 0.5703. ***

WHAT IS NOT CLAIMED.  Not that B1 was wrong -- it was right and remains cited.  Not that the spacing
deficit is a framework verdict: F5 is unsoftened, PO-7 protected, the conversion Daryl's.  ** Only that
this line's ROW overstated what B1's argument reached, and that the overstatement had a nameable shape:
treating a candid "either/or" as a partition. **

Written r2470.  Stated for reversal.
"""
import os, glob
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


def scan():
    """** TWO REQUIREMENTS, TWO FILTERS -- and the first draft used one for both. **
    The first-peak ratio needs ONE peak; the mean spacing needs FOUR.  Requiring four for both
    dropped exactly the states where the series starts at 380 -- ** the states carrying the
    MAXIMUM of the very spread being claimed. **  A filter that makes one quantity computable
    must not silently decide which data the OTHER quantity sees."""
    ratios, spacings = [], []
    for f in sorted(glob.glob(os.path.join(SP, 'c54.187_cr_phi*.npz'))):
        z = np.load(f)
        ls, Dl, lA = z['ls'], z['Dl'], float(z['l_A'])
        pk = ls[argrelextrema(Dl, np.greater, order=3)[0]]
        if len(pk) >= 1:
            ratios.append(float(pk[0])/lA)
        if len(pk) >= 4:
            spacings.append(float(np.mean(np.diff(pk[:4])))/lA)
    return ratios, spacings


def main():
    print()
    print('  B3 -- did B1 establish that 0.5703 is a robust prediction?')
    print()
    r, sp = scan()
    check(f'the phase scan carries nine states, all giving a first peak (found {len(r)})',
          len(r) == 9)
    check(f'and {len(sp)} of them carry four peaks in range, which is what a mean spacing needs',
          len(sp) >= 7)
    check(f'the first-peak ratio spreads from {min(r):.4f} to {max(r):.4f}',
          abs(min(r) - 0.5703) < 5e-4 and max(r) > 1.2)
    check(f'a spread of {max(r)/min(r):.2f}x -- so 0.5703 is ONE VALUE OF A FREE DATUM, not a '
          'prediction', max(r)/min(r) > 2.0)
    check('and at one phase the peak at 172 is absent entirely; the series starts at 380',
          max(r) > 1.25)

    check(f'⛭ THE SPACING spreads only {max(sp)/min(sp):.2f}x, from {min(sp):.3f} to {max(sp):.3f}',
          max(sp)/min(sp) < 1.2)
    check('and sits at 0.79 +/- 0.04 of l_A across every phase that has four peaks',
          abs(float(np.mean(sp)) - 0.79) < 0.02 and float(np.std(sp)) < 0.04)
    check('⇒⇒ AND IS NEVER 1.0 -- a ~21% spacing deficit surviving every reading',
          max(sp) < 0.9)
    check('which is a better number than the 22% position deficit the paper carried',
          (1 - float(np.mean(sp))) > 0.15 and max(sp)/min(sp) < max(r)/min(r))

    # B1 stands
    arc = open(os.path.join(ROOT, 'THE_LIVE_ARC.md'), encoding='utf-8', errors='replace').read()
    check("B1's argument stands and is credited by the fork: two arms at equal l_A with first "
          'peaks 21.8% apart rules out l_1 = c*l_A',
          '21.8%' in arc or '0.7300' in arc)
    check("but the row's disposition said 'the alternative is decided', which did not follow",
          'the alternative is decided' in arc)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** B1 stands; L-235\'s DISPOSITION did not follow from it. **')
    print('  The fork\'s pair was "a robust prediction OR a shared upstream constant", and ruling out')
    print('  the second was read as establishing the first.  ** It was a THIRD thing: the first-peak')
    print('  modes are already sub-horizon at Z_START, so their phase is ASSIGNED, and scanning that')
    print('  one freedom moves l_1/l_A by 2.21x. **')
    print('  ⇒ ** RULING OUT ONE HORN OF A DICHOTOMY ESTABLISHES THE OTHER ONLY IF THE DICHOTOMY IS')
    print('     EXHAUSTIVE -- and a dichotomy someone stated in passing is not a proof of')
    print('     exhaustiveness. **  The fork wrote a candid "either/or"; this line read a partition.')
    print('  ⛭ AND WHAT SURVIVES IS BETTER: ** the SPACING spreads only 1.11x, sits at 0.79 +/- 0.04')
    print('     of l_A, and is NEVER 1.0 -- a ~21% deficit surviving every phase. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
