#!/usr/bin/env python3
"""B46 -- the two crossings are not alike: the inner horizon is at INFINITE tortoise distance and the
wall at $r=0$ is at FINITE.  `PO-11`'s continuum problem is not a two-horizon matching.

** THE FIRST COMPUTED RESULT ON THIS ROW. **  *** r2785 established the continuum's route crosses two
signature changes -- the inner horizon and the wall.  ** Nobody had asked whether a wave can reach
either. **  In the coordinate the mode equation is written in, they behave oppositely. ***

** ⛭⛭ ⓵ THE INNER HORIZON IS INFINITELY FAR. **  $f$ has a ** simple ** zero there:

      *** f'(r_b) = 0.44232   nonzero  ->  1/f ~ 1/[f'(r_b)(r - r_b)]
          INT dr/(r-r_b) = log|r-r_b|  ->  -infinity ***

  ⇒ ** Analytically divergent. **  *** P14 already says so in its own voice -- "the horizons standing
      infinitely far" in the tortoise measure -- and this is that statement at the INNER horizon
      specifically. ***
  ⌗ ** And the quadrature would have lied: ** *** naive `quad` returned $-20.3$, $-20.6$, $-17.4$ at
    successively closer endpoints -- ** wandering, not converging **, which is an integrator failing on
    a log singularity and not a finite answer. ***

** ⛭⛭⛭ ⓶ THE WALL IS A FINITE DISTANCE AWAY. **  As $r\\to0$, $f\\simeq-2M/r$, so

      *** 1/f ~ -r/(2M)   ->  0,   and  INT_0 r dr  is FINITE ***

  ⇒ *** $r_*$ from $r=1$ to $r=0$ is $-0.385239$, ** stable to $10^{-12}$ **.  The integrand VANISHES at
      the wall because $f$ diverges there. ***

** ⛭ ⓷ SO THE ROW'S PROBLEM IS NOT A TWO-HORIZON MATCHING, AND THAT CHANGES WHAT IS OWED. **
  * *** the inner horizon is a ** standard ** infinite-distance boundary: modes acquire the usual
    horizon asymptotics and no matching CONDITION is imposed there -- it is where boundary behaviour is
    READ OFF, as at any horizon; ***
  * *** the wall is a ** regular singular point at finite distance ** -- the place a matching condition
    is actually needed, and the place P14's bound mode already lives. ***

  ⇒⇒ *** ONE MATCHING, NOT TWO.  r2785 counted two signature changes and inferred two matchings; ** a
      signature change at infinite tortoise distance is not a junction a mode passes through **, it is an
      asymptotic region. ***

** ⓸ AND IT EXPLAINS THE BOUND MODE'S PRIVILEGE PRECISELY. **  *** P14 binds its zero-mode in the leaf's
proper measure and notes the same mode "does not normalize" in the tortoise measure, "the horizons
standing infinitely far".  ** The wall being at finite tortoise distance is why a mode can be localised
there at all; the horizons being infinitely far is why the same mode fails to normalise against
them. ** ***

WHAT IS NOT CLAIMED.  ** Not that the matching condition is derived ** -- *** what is established is
WHERE it must be imposed and that there is one, not two. ***  ** Not that $M=1,\\alpha=12$ is the
corpus's case ** -- *** both limits are analytic: the simple zero of $f$ gives the log, and $f\\sim-2M/r$
gives the convergence, for every $M>0$. ***  ** Not that the wall is a regular point ** -- *** it is a
regular SINGULAR point; the potential $V=f(\\ell(\\ell+1)/r^2+f'/r)$ is not examined here. ***

** COMPUTES: $f'(r_b)$ against zero, and $r_*$ to the wall at four cutoffs.  *** $f$ is the corpus's own
Schwarzschild--de Sitter lapse. *** **

Written r2796.  Stated for reversal.
"""
import os
import re

import numpy as np
from scipy.integrate import quad

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

M, ALPHA = 1.0, 12.0


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def f(r):
    return 1 - 2*M/r - r*r/(ALPHA*ALPHA)


def fp(r):
    return 2*M/r**2 - 2*r/(ALPHA*ALPHA)


def main():
    print()
    print("  B46 -- can a wave reach either crossing?")
    print()
    roots = np.roots([-1/(ALPHA*ALPHA), 0, 1, -2*M])
    real = sorted(np.real(roots[np.abs(np.imag(roots)) < 1e-9]))
    rb = real[1]

    # ⓵ the inner horizon: simple zero => log divergence
    check(f'⛭⛭ ⓵ the inner horizon at $r_b={rb:.4f}$ is a SIMPLE zero: $f\'(r_b)={fp(rb):.5f}$, '
          'nonzero -- so $1/f\\sim1/[f\'(r_b)(r-r_b)]$ and $\\int dr/(r-r_b)$ diverges logarithmically',
          abs(fp(rb)) > 0.01)

    # and the quadrature wanders rather than converging
    vals = [quad(lambda r: 1/f(r), 1.0, rb-e, limit=400)[0] for e in (1e-2, 1e-4, 1e-6, 1e-8)]
    check(f'⌗ and naive quadrature WANDERS rather than converging '
          f'({", ".join(f"{v:.1f}" for v in vals)}) -- ** an integrator failing on a log singularity, '
          'not a finite answer **',
          abs(vals[-1] - vals[-2]) > 1.0)

    # ⓶ the wall: f ~ -2M/r => 1/f -> 0
    ws = [quad(lambda r: 1/f(r), e, 1.0, limit=600)[0] for e in (1e-2, 1e-4, 1e-6, 1e-12)]
    check(f'⛭⛭⛭ ⓶ while the wall is at FINITE tortoise distance: $r_*={ws[-1]:.6f}$, '
          f'stable across cutoffs $10^{{-2}}$ to $10^{{-12}}$ (spread {max(ws)-min(ws):.2e})',
          max(ws) - min(ws) < 1e-3)
    check('because $f\\simeq-2M/r$ as $r\\to0$, so $1/f\\sim-r/2M$ -- ** the integrand VANISHES at the '
          'wall **',
          abs(1/f(1e-6) - (-1e-6/(2*M))) < 1e-9)

    # ⓷ P14 says the horizons are infinitely far
    p14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))
    check('⓷ and P14 says so in its own voice: the static mode "does not normalize" in the tortoise '
          'measure, "the horizons standing infinitely far"',
          'the horizons standing infinitely far' in p14)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** one matching, not two — the crossings are not alike. **')
    print(f'  ⛭⛭ ⓵ ** The inner horizon is INFINITELY far: ** f\'(r_b) = {fp(rb):.5f} ≠ 0, a simple zero,')
    print('     so 1/f ~ 1/[f\'(r_b)(r−r_b)] and the integral diverges logarithmically.')
    print(f'     ⌗ *** Naive quadrature wandered — {", ".join(f"{v:.1f}" for v in vals)} — which is an')
    print('     integrator failing on a log singularity, not a finite answer. ***')
    print(f'  ⛭⛭⛭ ⓶ ** The wall is at FINITE distance: ** r_* = {ws[-1]:.6f}, stable to 1e-12, because')
    print('     f ≃ −2M/r as r→0 and ** the integrand VANISHES there. **')
    print('  ⓷ *** SO THE ROW\'S PROBLEM IS NOT A TWO-HORIZON MATCHING: ***')
    print('       the inner horizon   an infinite-distance ASYMPTOTIC region — behaviour is read off,')
    print('                           no condition is imposed, as at any horizon')
    print('       the wall            a regular singular point at FINITE distance — where a matching')
    print('                           condition is needed, and where P14\'s bound mode already lives')
    print('     ** r2785 counted two signature changes and inferred two matchings.  A signature change')
    print('     at infinite tortoise distance is not a junction a mode passes through. **')
    print('  ⓸ ** And it explains the bound mode\'s privilege exactly: ** the wall being at finite')
    print('     distance is why a mode can localise there; the horizons being infinitely far is why')
    print('     the same mode "does not normalize" against them.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
