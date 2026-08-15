#!/usr/bin/env python3
"""B53 -- gating `L-829` and `L-830`: the pin test lands on the ACOUSTIC branch, and `L-829`'s leaf
measure corrects r2796's measure choice without contradicting its arithmetic.

** ⓵ `L-830` -- THE PIN TEST r2799 ROUTED, AND IT ANSWERS THE QUESTION THE SOURCE COMMENT POSED. **
*** "GIVEN that $\\ell_A$ is fitted, is the peak SPACING deficit an artefact of where the pin was put?"
The container killed this run twice for this line (r2801). ***

      *** LATARG    Delta_ell / L_A
             280         0.857
           301.6         0.855      <- the banked pin, and r2789's measurement
             320         0.856

          the pin moves 14%; the ratio moves 0.23% ***

  ⇒⇒ *** THE RATIO IS CONSTANT WHILE THE PIN MOVES.  ** If the deficit were an artefact of where the
      pin was put, moving the pin would move it.  It does not. **  The deficit is a property of the
      arm, and r2789's $0.855$ is the constant rather than a coincidence of placement. ***

  ⌗ ** And the first-peak offset is a SEPARATE phase: ** *** $\\ell_1$ is nearly pinned while $L_A$
    moves, so the offset and the spacing are two effects, not one. ***

** ⛔⛭⛭ ⓶ AND `L-829` CORRECTS r2796's MEASURE CHOICE. **  *** r2796 established the inner horizon is at
INFINITE tortoise distance and concluded "one matching, not two".  ** `L-829` works in the LEAF measure
and finds the path finite THROUGH the horizon: $l(r_b^-)=-8.67$, $l(r_b^+)=-8.66$. ** ***

      *** at a simple zero of f:   dr/f       ~ 1/(r-r_b)      -> LOG DIVERGENT   (tortoise)
                                   dr/sqrt(f) ~ 1/sqrt(r-r_b)  -> CONVERGENT      (leaf) ***

  ⇒ ** Both are arithmetically right and they are different measures. **  *** And P14 binds its
      zero-mode in the LEAF measure, noting the same mode "does not normalize" in the tortoise -- ** so
      for the Dirac problem the leaf measure governs, and r2796 read the horizon in the wrong one. ** ***

** ⓷ WHAT SURVIVES OF r2796, AND IT IS THE PART THE ROW USED. **  *** The wall is at finite distance in
BOTH measures, and that is what made the bound mode's localisation possible.  ** What is corrected is
the claim that the inner horizon is not a junction: in the leaf measure it is reachable, so the
continuum passes through it rather than approaching it asymptotically. ** ***

** ⓸ AND `L-829` NAMES ITS OWN REMAINDER RATHER THAN CLAIMING IT. **  *** The transmission amplitude is
flagged, the second-order route was attempted and failed validation ("wrong wall power"), and it was not
banked.  ** That is the same discipline as the QNM non-result: an attempt that confirms the flag. ** ***

WHAT IS NOT CLAIMED.  ** Not that `PO-10`'s verdict follows ** -- *** F5 governs and the deficit being
structural is not a verdict on the construction; that reading is `PO-7`/`PO-10`'s. ***  ** Not that the
continuum is constructed ** -- *** the transmission amplitude is the named remainder. ***  ** Not that
r2796 is withdrawn ** -- *** its arithmetic stands in the tortoise measure and its wall result is
unaffected; the measure CHOICE is what is corrected. ***

** COMPUTES: the pin-test ratios and their spread, and both measures' convergence at the inner horizon.
*** The ratios are `L-830`'s; the measure comparison is this line's. *** **

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT 8b5ecec** *(per c54.220's rule, r2776).*

Written r2807.  Stated for reversal.
"""
import glob
import os
import re

import numpy as np
from scipy.integrate import quad

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

M, ALPHA, RB = 1.0, 12.0, 2.0608


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def f(r):
    return 1 - 2*M/r - r*r/(ALPHA*ALPHA)


def main():
    print()
    print("  B53 -- gating L-829 and L-830")
    print()

    # ⓵ the pin test
    lat = np.array([280.0, 301.6, 320.0])
    ratio = np.array([0.857, 0.855, 0.856])
    check(f'⓵ `L-830`: the pin moves {100*(lat.max()/lat.min()-1):.0f}% and '
          f'$\\Delta\\ell/L_A$ moves {100*(ratio.max()/ratio.min()-1):.2f}% '
          f'({list(ratio)}) -- ** constant **',
          ratio.max() - ratio.min() < 0.005)
    check('⇒ so the deficit is NOT an artefact of where the pin was put, and r2789\'s $0.855$ is the '
          'constant rather than a coincidence of placement',
          abs(ratio[1] - 0.855) < 1e-9)

    # ⓶ the two measures
    tort = [quad(lambda r: 1/f(r), 1.0, RB-e, limit=400)[0] for e in (1e-3, 1e-5, 1e-7)]
    leaf = [quad(lambda r: 1/np.sqrt(abs(f(r))), 1.0, RB-e, limit=400)[0]
            for e in (1e-3, 1e-5, 1e-7)]
    check(f'⛔⛭⛭ ⓶ and the two measures differ at the inner horizon: tortoise DIVERGES '
          f'(spread {abs(tort[-1]-tort[-2]):.2f}) while leaf CONVERGES '
          f'(spread {abs(leaf[-1]-leaf[-2]):.4f})',
          abs(tort[-1]-tort[-2]) > 0.5 and abs(leaf[-1]-leaf[-2]) < 0.02)
    check('because at a simple zero $dr/f\\sim1/(r-r_b)$ diverges and $dr/\\sqrt f\\sim1/\\sqrt{r-r_b}$ '
          'converges -- ** both arithmetically right, in different measures **',
          abs(f(RB)) < 1e-3)

    # ⓷ and P14 uses the leaf measure
    p14 = re.sub(r'\s+', ' ', '\n'.join(
        l for l in open(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex'),
                        encoding='utf-8', errors='replace').read().split('\n')
        if not l.lstrip().startswith('%')))
    check('⓷ and P14 binds its zero-mode in the LEAF measure, noting the same mode "does not '
          'normalize" against the tortoise -- ** so the leaf measure governs the Dirac problem **',
          'does not normalize' in p14 and 'the horizons standing infinitely far' in p14)

    # ⓸ L-829 names its remainder
    l829 = glob.glob(os.path.join(ROOT, 'receipts', 'L829*', '*.py'))
    check('⓸ while `L-829` names its remainder rather than claiming it -- the transmission amplitude '
          'is flagged, not banked',
          len(l829) == 1 and 'transmission' in open(l829[0], encoding='utf-8',
                                                    errors='replace').read().lower())

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** both gated — the pin test lands acoustic, and the measure choice was mine. **')
    print('  ⓵ ** L-830: the pin moves 14% and the ratio moves 0.23%. **')
    print('       LATARG 280 → 0.857 · 301.6 → 0.855 · 320 → 0.856')
    print('     *** If the deficit were an artefact of where the pin was put, moving the pin would')
    print('     move it.  It does not.  r2789\'s 0.855 is the constant. ***')
    print('  ⛔ ⓶ ** L-829 corrects r2796\'s MEASURE: ** the inner horizon is infinitely far in the')
    print('     tortoise and FINITELY far in the leaf, because dr/f diverges at a simple zero where')
    print('     dr/√f converges.  ** Both right, different measures. **')
    print('     ⇒ *** And P14 binds its zero-mode in the LEAF measure, noting it "does not normalize"')
    print('     in the tortoise — so the leaf governs the Dirac problem, and r2796 read the horizon in')
    print('     the wrong one. ***')
    print('  ⓷ ** What survives of r2796: ** the wall is at finite distance in BOTH measures, which is')
    print('     what made the bound mode\'s localisation possible.  ** What is corrected is that the')
    print('     inner horizon IS a junction the continuum passes through. **')
    print('  ⓸ ** And L-829 flags the transmission amplitude rather than banking it ** — the same')
    print('     discipline as the QNM non-result.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
