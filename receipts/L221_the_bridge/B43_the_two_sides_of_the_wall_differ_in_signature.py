#!/usr/bin/env python3
"""B43 -- the two sides of the wall are in DIFFERENT CAUSAL REGIONS: $f\\to-\\infty$ as $r\\to0^+$ and
$f\\to+\\infty$ as $r\\to0^-$, which corrects r2744 and reshapes `PO-11`'s remaining question.

** WHAT r2744 SAID. **  *** "$r=0$ sits deep inside the inner horizon ($f(0.010)=-23.0$), so the
continuum ($f>0$) and the wall ($r=0$) sit in different regions."  ** The observation was right and the
conclusion drawn from ONE SIDE. ** ***

** ⛭⛭ ⓵ $f$ IS NOT EVEN IN $r$, AND THE ODD TERM DOMINATES AT THE ORIGIN. **
$f = 1 - 2M/r - r^2/\\alpha^2$, and $2M/r$ is ** ODD **:

      *** f(+0.001) = -1999      -> INSIDE the inner horizon, r is TIMELIKE
          f(-0.001) = +2001      -> STATIC, r is SPACELIKE ***

  ⇒ *** THE WALL SITS ON THE BOUNDARY BETWEEN A STATIC REGION AND A NON-STATIC ONE, not deep inside
      one. ** r2744 sampled $r>0$ only. ** ***

** ⓶ AND THE CONJUGATE BRANCH IS A FULL STATIC REGION WITH ITS OWN HORIZON. **  *** The real roots of
$f$ are $\\{-12.897,\\ 2.061,\\ 10.836\\}$ at $M=1,\\alpha=12$: ** a reflected de Sitter horizon at
$r=-12.897$ **, with $f>0$ throughout $-12.897<r<0$.  ** The $r<0$ branch is not a thin sliver -- it is
a static region of the same kind as $r_b<r<r_c$. ** ***

** ⛭⛭⛭ ⓷ WHICH RESHAPES `PO-11`'s QUESTION RATHER THAN ANSWERING IT. **  *** r2767 narrowed the row to:
does the static region's continuum continue through $r=0$?  ** That question presupposed the wall was
interior to one region. **  It is not: ***

      *** the continuum on r_b < r < r_c        f > 0, r spacelike
          ...crosses the inner horizon...       (r2744's finding, unchanged)
          ...reaches r -> 0+                    f < 0, r TIMELIKE
          ...and emerges at r -> 0-             f > 0, r SPACELIKE again ***

  ⇒⇒ *** SO THE CROSSING IS NOT ONE MATCHING BUT A ** SIGNATURE ROUND TRIP **: spacelike to timelike
      and back.  ** The mode equation changes character twice, and the wall is where the second change
      happens. ** ***

** ⓸ AND IT EXPLAINS WHY THE BOUND MODE IS THE EASY CASE. **  *** P14's zero-mode is bound AT the wall
-- it lives where the superpotential $W=\\sqrt f/r$ changes sign, and $W$ is odd precisely because
$\\sqrt f$ is even in the dominant term and $1/r$ is odd.  ** A bound state at the sign change never has
to propagate through the timelike stretch; a continuum mode does. ** ***

WHAT IS NOT CLAIMED.  ** Not that the continuum fails to continue ** -- *** the round trip is the shape
of the question, not a verdict; `janzen_circle` continues the METRIC through $r=0$ as a theorem, and
nothing here contradicts that. ***  ** Not that $M=1,\\alpha=12$ is the corpus's case ** -- *** the sign
structure at the origin follows from $2M/r$ being odd and holds for every $M>0$; the horizon LOCATIONS
are illustrative. ***  ** Not that r2744 was wrong ** -- its $f(0.010)=-23.0$ is correct and its
inner-horizon crossing stands; what is corrected is the inference that both sides are interior.

** COMPUTES: $f$ at six radii spanning the origin, and its real roots.  *** $f$ is the corpus's own
Schwarzschild--de Sitter lapse. *** **

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT 499a4be** *(per c54.220's rule, r2776).*

Written r2785.  Stated for reversal.
"""
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

M, ALPHA = 1.0, 12.0


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def f(r):
    return 1 - 2*M/r - r*r/(ALPHA*ALPHA)


def main():
    print()
    print("  B43 -- are the two sides of the wall in the same causal region?")
    print()

    check(f'⛭⛭ ⓵ $f\\to-\\infty$ as $r\\to0^+$: $f(+0.001)={f(0.001):.0f}$ -- INSIDE the inner horizon, '
          '$r$ TIMELIKE', f(0.001) < -100)
    check(f'and $f\\to+\\infty$ as $r\\to0^-$: $f(-0.001)={f(-0.001):.0f}$ -- STATIC, $r$ SPACELIKE',
          f(-0.001) > 100)
    check('⇒ because $2M/r$ is ODD and dominates at the origin -- so the wall sits ON the boundary '
          'between a static region and a non-static one, not deep inside one',
          f(0.001)*f(-0.001) < 0)

    # ⓶ the conjugate branch has its own horizon
    roots = np.roots([-1/(ALPHA*ALPHA), 0, 1, -2*M])
    real = sorted(np.real(roots[np.abs(np.imag(roots)) < 1e-9]))
    check(f'⓶ and the conjugate branch has its own horizon: the real roots of $f$ are '
          f'{[round(x, 3) for x in real]} -- ** a reflected de Sitter horizon at {real[0]:.3f} **',
          real[0] < -1)
    check(f'with $f>0$ throughout {real[0]:.2f} $<r<0$ -- ** a static region of the same kind as '
          '$r_b<r<r_c$, not a thin sliver **',
          f(real[0]/2) > 0 and f(-0.5) > 0)

    # ⓷ r2744's own value stands
    check('⓷ while r2744\'s own sample stands: $f(0.010)$ is negative, so its inner-horizon crossing '
          'is unaffected -- ** what is corrected is the inference that BOTH sides are interior **',
          f(0.010) < 0)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the two sides of the wall are in different causal regions. **')
    print(f'  ⛭⛭ ⓵ ** f(+0.001) = {f(0.001):.0f} ** (inside the inner horizon, r timelike) against')
    print(f'     ** f(-0.001) = {f(-0.001):.0f} ** (static, r spacelike) — because 2M/r is ODD and')
    print('     dominates at the origin.  ** r2744 sampled r > 0 only. **')
    print(f'  ⓶ ** And the conjugate branch is a full static region ** — roots at')
    print(f'     {[round(x, 3) for x in real]}, a reflected de Sitter horizon at {real[0]:.3f}, with')
    print('     f > 0 throughout.  ** Not a sliver: the same kind of region as r_b < r < r_c. **')
    print('  ⛭⛭⛭ ⓷ ** Which reshapes PO-11 rather than answering it: **')
    print('       continuum on r_b<r<r_c      f > 0, r spacelike')
    print('       ...crosses the inner horizon (r2744, unchanged)')
    print('       ...reaches r → 0+           f < 0, r TIMELIKE')
    print('       ...emerges at r → 0-        f > 0, r SPACELIKE again')
    print('     *** So the crossing is a SIGNATURE ROUND TRIP, not one matching.  The mode equation')
    print('     changes character twice, and the wall is where the second change happens. ***')
    print('  ⓸ ** And it explains why the bound mode is the easy case: ** it lives AT the sign change')
    print('     of W = √f/r.  ** A bound state never has to propagate through the timelike stretch;')
    print('     a continuum mode does. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
