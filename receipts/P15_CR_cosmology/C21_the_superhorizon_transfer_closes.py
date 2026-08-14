#!/usr/bin/env python3
"""C21 -- the super-horizon transfer closes: $\\Phi\\to\\Phi_i$ at the branch point for every $k$, so with
r2661's join the expansion leg inherits $\\tfrac{9}{10}\\Phi_i$ scale-invariantly.

** WHERE THIS STANDS. **  r2661 computed the join ($9/10$, from $\\mathcal R$'s conservation); r2662
removed its caveat (at the branch point ** every ** mode is outside the horizon).  ** What was left was
the collapse leg's own evolution UP TO the branch point. **

** ⓵ AND `sec:envelope`'s CLOSED FORM ANSWERS IT. **  $\\Phi=3\\Phi_i(\\sin x-x\\cos x)/x^3$ with
$x=k\\eta/\\sqrt3$.  At the branch point $\\eta\\to0$, so $x\\to0$:

      *** Phi -> Phi_i   EXACTLY, for every k ***

  ⌗ ** And the approach is quantified by the series: ** $\\Phi/\\Phi_i=1-x^2/10+x^4/280+\\dots$, so the
    departure from $\\Phi_i$ is $O(k^2\\eta^2)$ -- *** vanishing at the branch point for every finite $k$,
    which is the same statement r2662 made geometrically ($k\\ll aH$ there). ***

** ⛭⛭ ⓶ SO THE SUPER-HORIZON TRANSFER CLOSES, AND IT IS SCALE-INVARIANT. **

      *** Phi_expansion(k)  =  (9/10) * Phi_i(k),   every k, no k-dependence in the ratio ***

  ⇒ *** The branch point does not filter: whatever $k$-dependence the expansion leg carries is inherited
      from $\\Phi_i$, not manufactured at the crossing.  Which is the corpus's own word for it -- the
      branch point "TRANSMITS that content rather than imprinting one of its own" -- now computed rather
      than argued from degeneracy. ***

** ⚠ ⓷ AND A NUMERICAL NEAR-MISS WORTH NAMING SO NOBODY LATER CONFLATES THEM. **  *** The join is
$1-\\tfrac1{10}$ and the series' leading correction is $-\\tfrac1{10}x^2$.  SAME NUMBER, DIFFERENT ORIGIN:
the join's $1/10$ comes from $(5+3w)/(3+3w)$ evaluated at $w=1/3$ against $w=0$; the series' comes from
expanding $(\\sin x-x\\cos x)/x^3$.  They are not the same $1/10$ and must not be read as one effect. ***

WHAT IS NOT CLAIMED.  ** Not that the transfer is complete ** -- *** this is the SCALAR super-horizon
transfer.  The acoustic evolution on the expansion leg from the branch point to recombination is the
oscillation the instrument already runs, and joining the two remains unrun as a single calculation. ***
** Not that $\\Phi_i$ itself is derived here ** -- it is the progenitor-supplied content, and P15 routes
$A_s$ and $n_s$ "through the same handover".  ** Not that the crossing DYNAMICS is addressed ** -- P15
defers it for a concrete matter model and that stands.

Written r2663.  Stated for reversal.
"""
import os
import re

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def main():
    print()
    print('  C21 -- does the super-horizon transfer close?')
    print()
    p15 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')))

    x, Phi_i = sp.symbols('x Phi_i', positive=True)
    Phi = 3 * Phi_i * (sp.sin(x) - x * sp.cos(x)) / x**3

    # ⓵ the closed form and its branch-point limit
    check('⓵ the closed form is the paper\'s: "$\\Phi=3\\Phi_{i}(\\sin x-x\\cos x)/x^{3}$ with '
          '$x=k\\eta/\\sqrt3$"',
          'whose regular solution is elementary' in p15 and 'x=k\\eta/\\sqrt' in p15)
    check('and at the branch point $x\\to0$ it gives $\\Phi\\to\\Phi_i$ EXACTLY, for every $k$',
          sp.limit(Phi, x, 0) == Phi_i)

    # the series
    ser = sp.series(Phi / Phi_i, x, 0, 5).removeO()
    c2 = sp.nsimplify(sp.expand(ser).coeff(x, 2))
    c4 = sp.nsimplify(sp.expand(ser).coeff(x, 4))
    check(f'with the approach quantified: $\\Phi/\\Phi_i = 1 {c2}x^2 + {c4}x^4 + \\dots$, so the '
          'departure is $O(k^2\\eta^2)$',
          c2 == sp.Rational(-1, 10) and c4 == sp.Rational(1, 280))

    # ⓶ the join, and the product
    w = sp.symbols('w')
    RoP = (5 + 3*w) / (3 + 3*w)
    join = sp.nsimplify(RoP.subs(w, sp.Rational(1, 3)) / RoP.subs(w, 0))
    check(f'⛭⛭ ⓶ and r2661\'s join is {join}, so $\\Phi_{{\\rm exp}}(k)=\\tfrac9{{10}}\\Phi_i(k)$ for '
          'every $k$ -- no $k$-dependence in the ratio',
          join == sp.Rational(9, 10))
    check('which is the corpus\'s own claim, now computed: the branch point "transmits that content '
          'rather than imprinting one of its own"',
          'transmits that content rather than imprinting one of its own' in p15)

    # ⓷ the near-miss
    check('⚠ ⓷ and the near-miss: the join is $1-1/10$ while the series\' leading correction is '
          '$-x^2/10$ -- SAME NUMBER, DIFFERENT ORIGIN',
          (1 - join) == sp.Rational(1, 10) and -c2 == sp.Rational(1, 10))

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the super-horizon transfer closes, and it is scale-invariant. **')
    print('  ⓵ ** At the branch point x -> 0 and Phi -> Phi_i EXACTLY, for every k. **  The series')
    print('     Phi/Phi_i = 1 - x²/10 + x⁴/280 puts the departure at ** O(k²η²) ** -- vanishing there for')
    print('     every finite k, which is r2662\'s geometric statement (k ≪ aH) in analytic form.')
    print('  ⛭⛭ ⓶ ** So with r2661\'s join: **')
    print('     *** Phi_expansion(k) = (9/10) Phi_i(k),  every k, no k-dependence in the ratio. ***')
    print('     ⇒ ** The branch point does not FILTER. **  Whatever k-dependence the expansion leg')
    print('     carries is ** inherited from Phi_i, not manufactured at the crossing ** -- which is the')
    print('     corpus\'s own "transmits rather than imprints", ** now computed rather than argued from')
    print('     degeneracy. **')
    print('  ⚠ ⓷ ** A near-miss worth naming: ** the join is 1 - 1/10 and the series\' leading correction')
    print('     is -x²/10.  ** SAME NUMBER, DIFFERENT ORIGIN ** -- (5+3w)/(3+3w) at two equations of')
    print('     state, against the expansion of (sin x - x cos x)/x³.  *** Not one effect. ***')
    print('  ⚠ SCALAR super-horizon only.  ** The acoustic evolution from the branch point to')
    print('    recombination is what the instrument already runs; joining the two as a single')
    print('    calculation is unrun. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
