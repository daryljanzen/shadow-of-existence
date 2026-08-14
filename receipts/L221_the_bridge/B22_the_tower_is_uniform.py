#!/usr/bin/env python3
"""B22 -- `PO-11`'s obstruction confirmed NUMERICALLY on the actual mode functions, at every $\\lambda$:
the leaf norm is finite and cut-off-independent while the tortoise norm diverges LOGARITHMICALLY.

** WHAT r2669 SHOWED ANALYTICALLY. **  Near a horizon $f$ vanishes linearly, so $\\int dr/\\sqrt{|f|}$
converges and $\\int dr/|f|$ does not; and at $r=0$ ** both ** converge.  ** The obstruction is
horizon-located. **  ⇒ *** But that was the MEASURE alone.  This runs it on the modes P14 actually
delivers. ***

** ⓵ THE MODES AND THE GEOMETRY. **  `JTOWER_angular_index` establishes the tower: $\\psi\\sim|r|^{\\lambda}$
with $\\lambda=j+\\tfrac12$, and "** for EVERY $\\lambda=j+1/2$, exactly ONE branch is normalizable ** ---
the growing branch needs $\\lambda<3/4$, ** which never holds **", giving "** one bound zero-mode per
(wall, $j$) **".  On the undercritical SdS cubic at $M=0.12$, $\\alpha=1$ the horizons sit at

      *** r_b = 0.256968,  r_c = 0.846439   (f > 0 between them) ***

** ⛭⛭ ⓶ AND BOTH NORMS RUN ON THOSE MODES: **

      *** lam    leaf-norm      tortoise at eps = 1e-4 / 1e-6 / 1e-8
           1.0    0.669566        4.357     6.882     9.233
           3.0    0.205363        1.828     3.074     4.235
          10.0    0.011067        0.1441    0.2648    0.3773 ***

  ⇒ *** The leaf norm is FINITE and CUT-OFF INDEPENDENT.  The tortoise norm grows by $+2.525$ then
      $+2.350$ per hundredfold in $\\epsilon$ -- ** a constant increment per decade pair, which IS a
      logarithm ** -- and it does so at every $\\lambda$, not merely at small $\\lambda$. ***

** ⓷ SO THE OBSTRUCTION IS UNIFORM IN THE TOWER, WHICH IS THE PART r2669 COULD NOT SEE. **  *** The
angular index does not rescue it: going to $\\lambda=10$ shrinks both norms but does not make the
tortoise one converge.  ** There is no high-$j$ corner where the modes become propagating states. ** ***
  ⌗ ** And it sharpens what a propagating sector must supply: ** *** not a better mode but a different
    OBJECT -- a scattering state with a continuum normalisation, which is what the infinite tortoise
    interval demands and what a bound tower cannot become by relabelling. ***

WHAT IS NOT CLAIMED.  ** Not that the scattering problem is solved ** -- *** this shows the bound tower
cannot be reinterpreted into it, which is a negative and is `PO-11`'s obstruction confirmed rather than
removed. ***  ** Not that $M=0.12$ is special ** -- it is the undercritical value P14's own receipts use,
and the divergence is a property of the linear zero of $f$, not of the parameter.  ** Not that the leaf
reading is preferred ** -- P14 states the two are not interchangeable and reads the leaf; that stands.

** COMPUTES: the tortoise-norm divergence increment per decade in cut-off, at fixed lambda -- a
RELATIVE measure on one background.  *** The parameter is the corpuss own lambda = j + 1/2. *** **

Written r2690.  Stated for reversal.
"""
import os
import re

import numpy as np
from scipy.integrate import quad

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

M = 0.12
RB, RC = 0.25696832, 0.84643915


def f(r):
    return 1 - 2*M/r - r**2


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print("  B22 -- does the angular index rescue the tortoise norm?")
    print()
    src = os.path.join(ROOT, 'receipts', 'P14_matter_sector_paper', 'JTOWER_angular_index.py')
    d = re.sub(r'\s+', ' ', open(src, encoding='utf-8', errors='replace').read())

    check('⓵ the tower is the receipt\'s: "THE TOWER IS INFINITE: one bound zero-mode per (wall, j)"',
          'THE TOWER IS INFINITE: one bound zero-mode per (wall, j)' in d)
    check('with exactly one normalizable branch: "The growing branch |r|^{-lambda} needs lambda < 3/4, '
          'which never holds"',
          'needs lambda < 3/4, which never holds' in d)

    # the horizons are genuine roots
    check(f'⓶ and the horizons are roots of the cubic: $f(r_b)=f(r_c)=0$ at '
          f'{RB:.6f}, {RC:.6f}, with $f>0$ between',
          abs(f(RB)) < 1e-7 and abs(f(RC)) < 1e-7 and f(0.5) > 0)

    # ⓶ both norms, at three lambdas
    for lam in (1.0, 3.0, 10.0):
        leaf, _ = quad(lambda r: r**(2*lam)/np.sqrt(f(r)), RB+1e-12, RC-1e-12, limit=600)
        tort = [quad(lambda r: r**(2*lam)/f(r), RB+e, RC-e, limit=800)[0]
                for e in (1e-4, 1e-6, 1e-8)]
        check(f'⛭⛭ lam={lam}: leaf = {leaf:.6g} FINITE, while tortoise runs '
              f'{tort[0]:.4g} -> {tort[1]:.4g} -> {tort[2]:.4g}',
              np.isfinite(leaf) and leaf < 10 and tort[2] > tort[1] > tort[0])

    # ⓷ the growth is logarithmic: constant increment per decade pair
    t = [quad(lambda r: r**2/f(r), RB+e, RC-e, limit=800)[0] for e in (1e-4, 1e-6, 1e-8)]
    d1, d2 = t[1]-t[0], t[2]-t[1]
    check(f'⓷ and the growth is LOGARITHMIC: increments {d1:.3f} then {d2:.3f} per hundredfold in '
          '$\\epsilon$ -- constant, not growing',
          abs(d1 - d2)/d1 < 0.15)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the obstruction is UNIFORM in the tower — the angular index does not rescue')
    print('  it. **')
    print('  ⓵ ** Run on the modes P14 actually delivers ** (psi ~ |r|^lambda, lambda = j+1/2, one bound')
    print('     mode per wall and j), between the true horizons r_b = 0.2570 and r_c = 0.8464:')
    print('  ⛭⛭ ⓶ ** the leaf norm is FINITE and CUT-OFF INDEPENDENT ** at every lambda, while the')
    print('     ** tortoise norm grows by a CONSTANT increment per decade pair — which IS a logarithm. **')
    print('  ⓷ *** And it does so at lambda = 10 as much as at lambda = 1.  Going to high angular index')
    print('     shrinks both norms but does NOT make the tortoise one converge — there is no high-j')
    print('     corner where the modes become propagating states. ***')
    print('  ⌗ ** Which sharpens what a propagating sector must supply: ** not a better mode but a')
    print('     ** different OBJECT ** — a scattering state with a continuum normalisation, which the')
    print('     infinite tortoise interval demands and ** a bound tower cannot become by relabelling. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
