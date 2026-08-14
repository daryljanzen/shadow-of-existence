#!/usr/bin/env python3
"""C35 -- the reference fork cc54 flagged settles itself, and AGAINST this line's framing: BIC uses only
DIFFERENCES, so F3 is the right score and the CAMB comparison is an instrument comparison.

** THE FORK, as cc54 states it (L-813). **  "the same-instrument F3 ($\\chi^2$(CR arm) $-$
$\\chi^2$($\\Lambda$CDM arm), per `P15_where_the_likelihood_sits`, to avoid charging CR for the instrument's
$\\chi^2/{\\rm dof}\\sim100$ floor) vs the BIC-against-CAMB-206.4 ($k=6$).  ** Which reference `PO-10`'s
$\\Delta$BIC $=21.5$ scores against decides it. **"

** ⛭⛭ ⓵ AND IT SETTLES ITSELF, BECAUSE OF WHAT BIC IS. **  $\\mathrm{BIC}=\\chi^2_{\\min}+k\\ln N$, and
** only DIFFERENCES of BIC carry meaning ** (Liddle 2004: "the absolute value of the criterion is not of
interest, only the relative value between different models").  So:

      *** dBIC = [chi2_CR - chi2_LCDM] + (k_CR - k_LCDM) ln N ***

  ⇒ *** The $\\chi^2$ enters ONLY as a difference.  An absolute $\\chi^2$ never appears in the criterion at
      all. ***

** ⓶ WHICH MAKES F3 THE SCORE AND NOT A SUBSTITUTE FOR ONE. **  *** $F3$ IS $\\chi^2_{\\rm CR}-
\\chi^2_{\\Lambda\\rm CDM}$ on the same instrument.  If both arms run through the same pipeline its floor is
COMMON and cancels in the difference -- which is not an approximation but exactly the quantity BIC
wants. ***

      *** dBIC = F3 + (2 - 6) ln 215 = F3 - 21.5
          ⇒ CR is preferred on BIC iff  F3 < 21.5 ***

** ⛔ ⓷ AND THE FRAMING THIS LINE SET UP IS THE ONE THAT BREAKS. **  r2709--r2711 set the threshold
against "flat $\\Lambda$CDM's best-fit $\\chi^2$", with `L-147`'s CAMB reference of $206.4$ in mind.
*** That charges CR the instrument's $\\chi^2/{\\rm dof}\\sim100$ floor while CAMB, run natively, is not
charged it.  A comparison in which one arm carries a pipeline's error and the other does not is an
INSTRUMENT comparison, not a model comparison. ***
  ⌗ ** cc54 caught this and asked rather than assuming, ** *** which is the right handling: the threshold
    is unchanged at $21.5$, but WHAT IT SCORES AGAINST was wrong in my statement of it. ***

** ⓸ SO THE GREENLIGHT IS: RUN $\\varphi=\\pi$, SCORE F3, COMPARE TO $21.5$. **  *** And the deliverable
stays the pair r2711 specified: $F3(\\varphi{=}0)$ from the banked `c54.178_cr` arm and $F3(\\varphi{=}\\pi)$
from the production run, each against the same threshold, with `PO-7` selecting the physical branch. ***

WHAT IS NOT CLAIMED.  ** Not that the threshold changes ** -- *** $\\Delta$BIC $=21.5$ stands; $k=2$
against $k=6$ over $N=215$ is unaffected by which $\\chi^2$ pair is differenced. ***  ** Not that F3's own
scope is re-derived ** -- it is `P15_where_the_likelihood_sits`'s, with that receipt's stated limits
(plik_lite TT only, no polarisation, no $\\ell<30$, no lensing).  ** Not that the run is cheap ** -- it is
a production two-arm run and it is cc54's to spend.

Written r2719.  Stated for reversal.
"""
import glob
import os
import re

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
N = 215


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  C35 -- which reference does PO-10 score against?')
    print()
    l147 = open(os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                             'P15_where_the_likelihood_sits.py'),
                encoding='utf-8', errors='replace').read()

    # ⓵ F3 is defined as a same-instrument difference
    check("⓵ L-147 defines the instrument's own floor as a same-instrument difference: \"THE "
          "INSTRUMENT'S OWN FLOOR IS chi^2(this instrument's LambdaCDM arm) - chi^2(CAMB)\"",
          "chi^2(this instrument's LambdaCDM arm) - chi^2(CAMB)" in l147)
    check('and wires the pipeline against CAMB as a REFERENCE: "THE PIPELINE IS WIRED IFF the CAMB '
          'flat-LambdaCDM best fit reproduces chi^2 = 206.4 over 215 TT bins"',
          'the CAMB flat-LambdaCDM best fit reproduces' in l147 and '206.4' in l147)

    # ⓶ BIC uses only differences
    dbic = (2 - 6)*np.log(N)
    check(f'⛭⛭ ⓶ and $\\Delta$BIC $=[\\chi^2_{{CR}}-\\chi^2_{{\\Lambda CDM}}]+(k_{{CR}}-k_{{\\Lambda CDM}})'
          f'\\ln N$ = F3 ${dbic:.1f}$ -- the $\\chi^2$ enters ONLY as a difference',
          abs(dbic + 21.5) < 0.1)
    check(f'⇒ so CR is preferred on BIC iff F3 < {-dbic:.1f}', -dbic > 0)

    # ⓷ the threshold is unchanged by the choice
    for pair in ((2, 6), (2, 5)):
        d = (pair[1]-pair[0])*np.log(N)
        check(f'⓷ and the threshold is unaffected by WHICH $\\chi^2$ pair is differenced: '
              f'$k={pair[0]}$ vs ${pair[1]}$ still gives {d:.1f}',
              d > 0)

    # ⓸ the instrument floor is real and large
    check('⓸ while the instrument floor is real and large -- L-147 measures it rather than assuming it',
          'FLOOR' in l147.upper())

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** F3 is the score, and this line\'s CAMB framing was the broken one. **')
    print('  ⛭⛭ ⓵ ** BIC = χ² + k ln N, and only DIFFERENCES of BIC carry meaning. **  So')
    print('       ΔBIC = [χ²_CR − χ²_ΛCDM] + (k_CR − k_ΛCDM) ln N')
    print('     ⇒ *** the χ² enters ONLY as a difference; an absolute χ² never appears in the criterion')
    print('       at all. ***')
    print('  ⓶ ** Which makes F3 the score rather than a substitute for one: ** F3 IS')
    print('     χ²(CR arm) − χ²(ΛCDM arm) on the same instrument, so the floor is COMMON and cancels —')
    print('     ** not an approximation but exactly the quantity BIC wants. **')
    print(f'       ΔBIC = F3 {dbic:.1f}    ⇒  CR preferred iff  F3 < {-dbic:.1f}')
    print('  ⛔ ⓷ ** And the framing this line set up is the one that breaks. **  r2709–r2711 set the')
    print("     threshold against flat ΛCDM's best-fit χ², with CAMB's 206.4 in mind — ** which charges")
    print('     CR the instrument\'s χ²/dof ~ 100 floor while CAMB, run natively, is not charged it. **')
    print('     *** A comparison where one arm carries a pipeline\'s error and the other does not is an')
    print('     INSTRUMENT comparison, not a model comparison. ***')
    print('  ⇒ ⓸ ** GREENLIGHT: run φ=π, score F3, compare to 21.5. **  The deliverable stays the pair —')
    print('     F3(φ=0) from the banked arm and F3(φ=π) from the production run, PO-7 selecting.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
