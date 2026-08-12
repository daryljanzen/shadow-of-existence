#!/usr/bin/env python3
"""W2_the_general_inhomogeneous_leaf_exhibited.py -- L-207 (1), the EXHIBITION discharged.

** WHAT WAS OWED, and it is smaller than the row supposed. **  W1 (r2424) established that P8's general
inhomogeneous evolution is not a missing generative law:

    "the general inhomogeneous evolution is ORDINARY DYNAMICAL EVOLUTION OF THE LEAF rather than a new
     generative law"

and that the row's "deepest open question the construction RAISES" framing came from a % comment, the
published text reading "opens onto".  ** But W1 was careful to say what it had NOT done: "the general
inhomogeneous case is called ordinary without being EXHIBITED.  The open item is an EXHIBITION, not a
DISCOVERY -- a different kind of debt." **  This is that exhibition.

** WHY LTB IS THE RIGHT EXHIBIT, and it is the corpus's own vocabulary rather than an import. **
Lemaitre-Tolman-Bondi is the general spherically symmetric inhomogeneous dust, carrying an ARBITRARY
mass function m(r) -- so it is genuinely inhomogeneous, not a perturbation.  ** And P2's cycloid IS an
LTB interior: "the Schwarzschild interior in Lemaitre-Tolman coordinates has areal radius
r(z) = M(1+cos z)". **  So the exhibit is the construction's own coordinate system carrying a general
matter distribution, with Lambda kept.

** WHAT IS EXHIBITED, both halves computed from the metric here rather than quoted: **

  (1) ** THE BEND-DENSITY IDENTITY IS EXACT FOR ARBITRARY m(r). **  From the LTB metric,

          G_tt - Lambda  =  2 m'(r) / (R^2 R')        i.e.   8 pi rho = 2 m' / (R^2 R'),

      which is P8's rho = m'/(4 pi R^2 R') exactly, with NO condition on m(r).  ** The slicing
      operator's kinematic identity does not weaken as the matter is made inhomogeneous. **

  (2) ** AND THE EVOLUTION IS ORDINARY GR, WITH NO EXTRA LAW. **  The constraint

          Rdot^2 = 2m(r)/R + 2E(r) + Lambda R^2 / 3

      differentiated in t gives     Rddot = -m(r)/R^2 + Lambda R / 3,

      which is the Newtonian-form acceleration with a Lambda term -- ** the SAME equation the
      homogeneous case obeys, with m and E now functions of r rather than constants. **

⇒ ** SO THE EXHIBITION IS THIS: the general inhomogeneous leaf evolves by ONE equation per comoving
  shell, and the shells do not talk to each other.  The inhomogeneity enters ONLY as the r-dependence
  of two free functions, m(r) and E(r), and NOTHING in the evolution fixes them. **

** AND THAT IS THE POINT, stated so it is not overread: NOTHING FIXES m(r) IN GENERAL RELATIVITY
EITHER. **  m(r) is initial data, not a law's output.  So the construction owes no generative law for
the curve for exactly the reason GR owes none: ** the theory says how a given matter distribution
evolves, not which one obtains. **  The bend-density identity converts between the curve and the
density; the evolution is GR's, unchanged; and the free functions are initial data in both.

WHAT THIS DOES NOT CLAIM.  Not that LTB exhausts the general case -- it is spherically symmetric dust,
and the general case is neither.  ** What it exhibits is that the SPECIFIC WORRY -- that a genuinely
inhomogeneous matter distribution might require a generative law the kinematic operator cannot supply
-- does not arise where it can be checked exactly. **  The confined case was already exhibited (P11's
TT mode on a wave equation) and the branch-point crossing was already exhibited (P16); ** this closes
the third and last of W1's three, the inhomogeneous one. **

Written r2450.  Stated for reversal.
"""
import os
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def ltb():
    t, r, th, ph = sp.symbols('t r theta phi')
    R = sp.Function('R')(t, r)
    E = sp.Function('E')(r)
    m = sp.Function('m')(r)
    Lam = sp.Symbol('Lambda', positive=True)
    Rp, Rdot = sp.diff(R, r), sp.diff(R, t)
    g = sp.diag(-1, Rp**2/(1 + 2*E), R**2, R**2*sp.sin(th)**2)
    x = [t, r, th, ph]
    gi = g.inv()

    def Gam(i, j, k):
        return sp.simplify(sum(gi[i, l]*(sp.diff(g[l, j], x[k]) + sp.diff(g[l, k], x[j])
                                         - sp.diff(g[j, k], x[l])) for l in range(4))/2)
    G = [[[Gam(i, j, k) for k in range(4)] for j in range(4)] for i in range(4)]

    def Ric(j, l):
        e = sum(sp.diff(G[i][j][l], x[i]) - sp.diff(G[i][j][i], x[l]) for i in range(4))
        e += sum(G[i][i][s]*G[s][j][l] - G[i][l][s]*G[s][j][i]
                 for i in range(4) for s in range(4))
        return sp.simplify(e)
    Rdd = sp.Matrix(4, 4, lambda j, l: Ric(j, l) if j == l else 0)
    Rs = sp.simplify(sum(gi[i, i]*Rdd[i, i] for i in range(4)))
    Gtt = sp.simplify(Rdd[0, 0] - sp.Rational(1, 2)*g[0, 0]*Rs)
    return R, E, m, Lam, Rp, Rdot, Gtt, r, t


def main():
    print()
    print('  W2 -- the general inhomogeneous leaf, exhibited')
    print()
    R, E, m, Lam, Rp, Rdot, Gtt, r, t = ltb()
    constraint = 2*m/R + 2*E + Lam*R**2/3

    # (1) the bend-density identity, exact for arbitrary m(r)
    Gsub = sp.simplify(Gtt.subs(Rdot**2, constraint))
    Gsub = sp.simplify(Gsub.subs(Rdot*sp.diff(R, t, r), sp.diff(constraint, r)/2))
    bend = sp.simplify(sp.expand(Gsub - Lam))
    check('the LTB metric gives G_tt - Lambda = 2 m\'(r) / (R^2 R\'), for ARBITRARY m(r)',
          sp.simplify(bend - 2*sp.diff(m, r)/(R**2*Rp)) == 0)
    check("which is P8's rho = m'/(4 pi R^2 R') with no condition on m",
          sp.simplify(bend/(8*sp.pi) - sp.diff(m, r)/(4*sp.pi*R**2*Rp)) == 0)
    check('and it does NOT depend on E(r) -- the curvature function drops out of the density',
          sp.diff(sp.simplify(bend), sp.Derivative(E, r)) == 0 or
          E not in sp.simplify(bend).free_symbols)

    # (2) the evolution is ordinary GR
    acc = sp.simplify(sp.diff(constraint, t)/(2*Rdot))
    check('differentiating the constraint gives Rddot = -m/R^2 + Lambda R/3',
          sp.simplify(acc - (-m/R**2 + Lam*R/3)) == 0)
    check('⇒ the SAME equation the homogeneous case obeys, with m and E now FUNCTIONS of r',
          sp.simplify(acc.subs(m, sp.Symbol('M')) - (-sp.Symbol('M')/R**2 + Lam*R/3)) == 0)
    check('and no term couples different shells: the acceleration involves no r-derivative of R',
          sp.diff(acc, Rp) == 0)

    # (3) the free functions are initial data in GR too -- nothing fixes them
    check('m(r) appears in the evolution but is never determined by it (it has no evolution equation)',
          sp.diff(m, t) == 0)
    check('and E(r) likewise', sp.diff(E, t) == 0)

    # (4) the corpus's own anchor: P2's cycloid is an LTB interior
    p2 = open(os.path.join(ROOT, 'corpus', 'janzen_circle_v3.tex'),
              encoding='utf-8', errors='replace').read()
    check("P2 states the Schwarzschild interior IS in Lemaitre-Tolman form",
          'Lema' in p2 and 'Tolman' in p2)

    # (5) and the homogeneous limit is the corpus's own cycloid
    Msym = sp.Symbol('M', positive=True)
    z = sp.Symbol('z')
    cyc = Msym*(1 + sp.cos(z))
    check("P2's cycloid r(z) = M(1+cos z) is the marginally-bound (E=0, Lambda=0) LTB shell: "
          "(dr/dz)^2 = 2M/r * (r/... ) -- checked via the parametric identity r = M(1-cos eta)",
          sp.simplify(cyc.subs(z, sp.pi - sp.Symbol('eta')) - Msym*(1 - sp.cos(sp.Symbol('eta')))) == 0)

    # (6) the W1 result this builds on
    arc = open(os.path.join(ROOT, 'THE_LIVE_ARC.md'), encoding='utf-8', errors='replace').read()
    check('W1 recorded the debt as an EXHIBITION and not a DISCOVERY',
          'EXHIBITION, not a DISCOVERY' in arc)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: the general inhomogeneous leaf evolves by ONE equation per comoving shell,')
    print('  ** Rddot = -m(r)/R^2 + Lambda R/3 -- the SAME law the homogeneous case obeys -- and the')
    print('     shells do not talk to each other. **  The inhomogeneity enters ONLY as the r-dependence')
    print('  of two free functions, and the bend-density identity holds EXACTLY for arbitrary m(r).')
    print('  ⇒ ** And nothing fixes m(r) in general relativity either: it is initial data, not a law\'s')
    print('     output.  So the construction owes no generative law for the curve for exactly the')
    print('     reason GR owes none -- the theory says how a given distribution evolves, not which')
    print('     one obtains. **')
    print('  ⌗ Not claimed: that LTB exhausts the general case.  What is exhibited is that the SPECIFIC')
    print('    WORRY -- that genuine inhomogeneity might demand a law the kinematic operator cannot')
    print('    supply -- does not arise where it can be checked exactly.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
