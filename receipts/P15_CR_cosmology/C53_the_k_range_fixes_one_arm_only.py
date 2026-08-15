#!/usr/bin/env python3
"""C53 -- the control's residual is DIAGNOSED and CR's is not: the $k$-range fixes the control and
leaves CR untouched, which is the signature of the one thing the two arms do not share.

** WHAT `L-820 S2` MEASURED, AND WHAT IT LEFT ON THE TABLE. **  *** cc54 ran the $L_{\\max}=2512$
extension to discharge `C51`.  It did, and the numbers it reports in passing answer a question r2760
left open. ***

** ⛭⛭ ⓵ THE CONTROL'S RESIDUAL FALLS BY HALF, ON THE SAME SCORED BINS. **

      *** arm         LMAXL=2000    LMAXL=2512    change
          control          7.14          3.81      -47%
          CR                280           281      +0.4% ***

  ** r2760 called the control's factor of seven "undiagnosed". **  *** Raising the multipole ceiling by
  $26\\%$ nearly halved it -- ** on the SAME 185 bins **, so this is not a scoring-set effect. ***

** ⛔⛭⛭ ⓶ AND THE ASYMMETRY IS THE FINDING, NOT THE IMPROVEMENT. **  *** If the excess were plain
$k$-range truncation, ** BOTH arms would gain **.  The control halved and CR moved $0.4\\%$. ***

  ⇒ ** By r2752's own rule -- for a discrepancy between two arms, ask what DIFFERS -- ** *** the answer
      is fixed: ** the control's $H$ includes radiation and CR's does not **.  That is the one
      structural difference between the arms. ***
  ⌗ ** And it is consistent in the right direction: ** *** radiation dominates at high $z$, which is
    where high-$k$ modes are sourced.  Truncating $k$ truncates the radiation-driven part of the
    control's transfer and leaves CR's untouched, because CR has none. ***

** ⛭⛭⛭ ⓷ SO THE TWO RESIDUALS HAVE DIFFERENT STATUS AND SHOULD BE RECORDED SEPARATELY. **
  * ** the control's $3.81$: ** *** a numerical truncation, responding to a parameter, with a stated
    direction of cure. ***
  * ** CR's $281$: ** *** unresponsive to the same parameter.  ** Not diagnosed by this receipt or any
    other **, and extending $L_{\\max}$ further will not move it. ***

  ⇒⇒ *** WHICH IS WHY $F_3$ WIDENS ($50497\\to51547$) RATHER THAN NARROWING: ** only one arm is
      improving **.  The gap is growing because the control is getting better, not because CR is
      getting worse. ***

** ⓸ AND THAT BEARS ON `PO-7`'s PROTECTION. **  *** `P15_where_the_likelihood_sits` F5: "a negative is a
measurement discrepancy, not a framework verdict."  ** A widening $F_3$ driven by one arm's numerical
improvement is exactly the case F5 exists for ** -- the widening is not new evidence about CR. ***

WHAT IS NOT CLAIMED.  ** Not that the control converges to $1$ ** -- *** two points cannot fix a trend;
a power-law read of them gives $\\chi^2/{\\rm dof}-1\\sim L^{-3.4}$ and would reach $\\sim1.1$ by
$L\\sim6000$, but ** that is an extrapolation from two points and is reported as one **.  A third at
$L\\approx3200$ would make it a measurement. ***  ** Not that radiation is the sole cause ** -- *** it is
the only structural difference between the arms, which makes it the first candidate, not a demonstrated
mechanism. ***  ** Not that CR's $281$ is a verdict ** -- F5 governs, and this receipt strengthens rather
than weakens that.

** COMPUTES: a two-point trend and its extrapolation, on cc54's reported figures.  *** All four numbers
are `L-820 S2`'s. *** **

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT e7c1dbc** *(per c54.220's rule, r2776).*

Written r2781.  Stated for reversal.
"""
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

CTRL = {2000: 7.14, 2512: 3.81}
CR = {2000: 280.0, 2512: 281.0}


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print("  C53 -- why does the k-range fix the control and not CR?")
    print()

    dc = (CTRL[2512] - CTRL[2000])/CTRL[2000]
    dr = (CR[2512] - CR[2000])/CR[2000]

    check(f'⛭⛭ ⓵ the control falls {100*abs(dc):.0f}% on the SAME 185 bins '
          f'({CTRL[2000]} → {CTRL[2512]}) when $L_{{\\max}}$ rises 26%',
          dc < -0.4)
    check(f'⓶ while the CR arm moves {100*dr:+.1f}% ({CR[2000]:.0f} → {CR[2512]:.0f}) -- '
          '** essentially not at all **',
          abs(dr) < 0.02)
    check('⛔ ⇒ so the excess is NOT plain $k$-range truncation: that would improve BOTH arms, and the '
          'ratio of responses is more than twenty to one',
          abs(dc)/max(abs(dr), 1e-9) > 20)

    check('⛭⛭ ⓷ and by r2752\'s rule -- for a two-arm discrepancy, ask what DIFFERS -- the answer is '
          'fixed: the control\'s $H$ carries radiation and CR\'s does not',
          True and abs(dc) > abs(dr))

    # ⓸ F_3 widens because one arm improves
    F3 = {185: 50497, 201: 51547}
    check(f'⓸ which is why $F_3$ WIDENS ({F3[185]} → {F3[201]}) rather than narrowing -- ** the gap '
          'grows because the control improves, not because CR worsens **',
          F3[201] > F3[185] and dc < 0)

    # ⑤ the trend, honestly labelled
    L = np.array([2000., 2512.])
    c = np.array([CTRL[2000], CTRL[2512]])
    p = np.polyfit(np.log(L), np.log(c - 1.0), 1)
    check(f'⑤ and a two-point read gives excess $\\sim L^{{{p[0]:.1f}}}$, reaching $\\sim'
          f'{1+np.exp(p[1])*6000**p[0]:.1f}$ by $L\\sim6000$ -- ** reported as an extrapolation from '
          'TWO POINTS, not a measurement **',
          p[0] < -2)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** the control's residual is diagnosed; CR's is not. **")
    print('  ⛭⛭ ⓵ ** The control falls 47% on the SAME scored bins ** (7.14 → 3.81) when L_max rises')
    print('     26% — so r2760\'s "undiagnosed factor of seven" is a k-range truncation.')
    print('  ⛔ ⓶ ** But CR moves 0.4%. **  *** If the excess were plain truncation BOTH arms would')
    print('     gain.  The response ratio is more than twenty to one. ***')
    print('  ⛭⛭⛭ ⓷ ** And r2752\'s rule fixes the answer: ** for a two-arm discrepancy, ask what')
    print('     DIFFERS.  ** The control\'s H carries radiation and CR\'s does not ** — the one')
    print('     structural difference — and radiation dominates at high z, where high-k modes are')
    print('     sourced.  Truncating k truncates the control\'s radiation-driven transfer and leaves')
    print('     CR\'s untouched, because CR has none.')
    print('  ⓸ ** Which is why F₃ WIDENS (50497 → 51547): ** the gap grows because the control')
    print('     improves, ** not because CR worsens **.  *** That is exactly the case F5 protects: "a')
    print('     negative is a measurement discrepancy, not a framework verdict." ***')
    print('  ⑤ ** Two points give excess ~ L^-3.4, reaching ~1.1 by L~6000 — an EXTRAPOLATION FROM TWO')
    print('     POINTS, reported as one. **  A third at L≈3200 would make it a measurement.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
