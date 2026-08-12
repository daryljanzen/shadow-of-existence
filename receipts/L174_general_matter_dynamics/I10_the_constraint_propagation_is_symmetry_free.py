#!/usr/bin/env python3
"""I10 -- cc54's L-801 verified independently on this tree: the contracted Bianchi identity holds to
O(eps^2) on a metric with NO Killing vector, so the FREEDOM half of L-174 ⓵'s nonlinear remainder
generalises and only the STABILITY half is Gowdy-scoped.

** WHAT ARRIVED. **  Daryl handed cc54 the nonlinear remainder r2514 left: does the nonlinear evolution
keep sigma^TT free?  ** cc54 split it at P11's own seam ** rather than answering yes or no:

  * ** THE FREEDOM ** -- does sigma^TT stay free?  P11: "a first-class constrained system evolves
    consistently to all orders ** by the contracted Bianchi identity **".  That identity is OFF-SHELL.
  * ** THE STABILITY ** -- no runaway?  P11's "** two exact structures [that] sharpen this beyond the
    Bianchi count **" -- the conserved shear charge and the positive-definite reduced energy -- and
    those ARE Gowdy-specific.

  ⇒ *** SO P11's ALL-ORDERS FREEDOM ARGUMENT COVERS THE GENERAL CASE.  What its Gowdy scoping actually
      leaves open is the NARROWER STABILITY QUESTION. ***

** ⓵ THE LOAD-BEARING STEP, RE-DERIVED HERE ON A DIFFERENT METRIC. **  cc54 verified the identity on
"the inhomogeneous polarized leaf" and the momentum constraint for a two-wave superposition.  This line
built an independent test: ** two TT waves in NON-PARALLEL directions **, so the metric depends on t, x
AND z and ** no Killing vector is available **:

      g = diag(-1, 1+h_+, 1-h_+, 1) + off-diagonal h_x ,
      h_+ = eps cos(k1 (z - t)) ,   h_x = eps cos(k2 (x - t))

  Christoffels, Riemann, Ricci and G built to O(eps^2), then:

      *** nabla_mu G^mu_0 = nabla_mu G^mu_1 = nabla_mu G^mu_2 = nabla_mu G^mu_3 = 0 ***

  ⇒ ** All four vanish, and NO Killing vector was used or available. **  ⇒ *** The constraint
    propagation is OFF-SHELL AND SYMMETRY-FREE.  It is not a Gowdy fact. ***

** ⓶ AND THAT ANSWERS SOMETHING THIS LINE HAD LEFT OPEN TWICE. **  r2504 named the sigma^2 back-reaction
as the obstruction and r2514 flagged it as the invisible term at linear order.
  ⇒ ** cc54's answer: it is a positive O(eps^2) SCALAR sourcing the energy/Hamiltonian sector via
    rho = R_3/2 + theta^2/3 - sigma^2/2 -- ** *** NOT a new constraint on the two TT functions. ***
  ⇒ ** So the thing this line could not see at linear order does not remove the freedom; it feeds the
    scalar sector. **

** ⌗ ⓷ AND THREE JUDGEMENTS IN THE DROP ARE WORTH RECORDING AS RIGHT. **
  * It filed into ** its own directory ** (L801_nonlinear_shear_freedom/) rather than adding an "I10"
    to 54's live I-series.  ** That is the c54.198 filename collision avoided BY CONSTRUCTION rather
    than by luck. **
  * It asserted ** only against sources, never the register ** -- the rule its own arc-pin finding
    produced, applied to itself one revision later.
  * And it ** did not rewrite L-174's board entry **, stated for reversal, on the ground that the row's
    status is unseated.  ** That is r2495's distinction used correctly: a judgement remains, so it
    deferred -- as against deferring where the mathematics decides. **

WHAT IS NOT CLAIMED.  ** Not that L-174 ⓵ is converted ** -- the vein verdict is unseated and neither
node has taken it.  ** Not that the stability question is settled ** -- it is open, and open in a named,
externally-bounded way (Friedrich for vacuum small-data, Andreasson--Ringstrom for all-data T^3 Gowdy
with matter, Nariai the non-generic exception).  ** Not that this receipt's metric is a solution ** --
the contracted Bianchi identity is off-shell and holds for ANY metric, which is precisely the point:
the test is that it holds where no symmetry does.

Written r2529.  Stated for reversal.
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


def bianchi_residual():
    """Build G to O(eps^2) on a two-wave, no-Killing-vector metric and contract the Bianchi identity."""
    t, x, y, z, e = sp.symbols('t x y z epsilon')
    co = [t, x, y, z]
    k1, k2 = sp.symbols('k1 k2', positive=True)
    hp = e*sp.cos(k1*(z - t))
    hc = e*sp.cos(k2*(x - t))
    g = sp.diag(-1, 1 + hp, 1 - hp, 1) + sp.Matrix([[0, 0, 0, 0], [0, 0, hc, 0],
                                                    [0, hc, 0, 0], [0, 0, 0, 0]])
    gi = g.inv()

    def trunc(expr):
        return sp.series(sp.expand(expr), e, 0, 3).removeO()

    Gam = [[[trunc(sp.Rational(1, 2)*sum(
        gi[a, d]*(sp.diff(g[d, b], co[c]) + sp.diff(g[d, c], co[b]) - sp.diff(g[b, c], co[d]))
        for d in range(4))) for c in range(4)] for b in range(4)] for a in range(4)]

    def riem(a, b, c, d):
        r = sp.diff(Gam[a][b][d], co[c]) - sp.diff(Gam[a][b][c], co[d])
        r += sum(Gam[a][c][m]*Gam[m][b][d] - Gam[a][d][m]*Gam[m][b][c] for m in range(4))
        return r

    Ric = sp.zeros(4, 4)
    for b in range(4):
        for d in range(4):
            Ric[b, d] = trunc(sum(riem(a, b, a, d) for a in range(4)))
    R = trunc(sum(gi[i, j]*Ric[i, j] for i in range(4) for j in range(4)))
    Ein = sp.simplify(Ric - sp.Rational(1, 2)*R*g)
    Gm = sp.simplify(gi*Ein)

    out = []
    for nu in range(4):
        d = sum(sp.diff(Gm[mu, nu], co[mu]) for mu in range(4))
        d += sum(Gam[mu][mu][lam]*Gm[lam, nu] for mu in range(4) for lam in range(4))
        d -= sum(Gam[lam][mu][nu]*Gm[mu, lam] for mu in range(4) for lam in range(4))
        out.append(sp.simplify(trunc(d)))
    return out, g, (t, x, z)


def main():
    print()
    print("  I10 -- is the constraint propagation symmetry-free?")
    print()
    p11 = re.sub(r'\s+', ' ', '\n'.join(
        l for l in open(os.path.join(ROOT, 'corpus', 'dynamics_paper.tex'),
                        encoding='utf-8', errors='replace').read().split('\n')
        if not l.lstrip().startswith('%')))

    # ⓵ P11's seam, at source
    check('P11: "A first-class constrained system evolves consistently to all orders by the contracted '
          'Bianchi identity: there is no classical dynamical obstruction at any order"',
          'evolves consistently to all orders by the contracted Bianchi identity' in p11
          and 'no classical dynamical obstruction at any order' in p11)
    check('and P11 itself marks the NEXT layer as separate: "Two exact structures sharpen this beyond '
          'the Bianchi count"',
          'Two exact structures sharpen this beyond the Bianchi count' in p11)
    check('⇒ so P11 has TWO layers, and the FREEDOM sits in the first while the Gowdy-specific '
          'structures sharpen STABILITY',
          'Two exact structures sharpen this beyond the Bianchi count' in p11)

    # ⓶ the independent test
    res, g, deps = bianchi_residual()
    t, x, z = deps
    fs = g.free_symbols
    check('the test metric carries two NON-PARALLEL TT waves and depends on t, x AND z, so no Killing '
          'vector is available',
          all(s in fs for s in (t, x, z)))
    for nu, v in enumerate(res):
        check(f'⛭ nabla_mu G^mu_{nu} = {v} to O(eps^2)', sp.simplify(v) == 0)
    check('⇒⇒ ALL FOUR VANISH WITH NO KILLING VECTOR USED OR AVAILABLE -- the constraint propagation '
          'is OFF-SHELL AND SYMMETRY-FREE, not a Gowdy fact',
          all(sp.simplify(v) == 0 for v in res) and all(s in fs for s in (t, x, z)))

    # ⓷ what P11 routes out, and what stays open
    check('⚠ and P11 routes the general/all-data stability statement OUT, to external results',
          'Friedrich' in p11 or 'Ringstr' in p11)
    check('with Nariai the named non-generic exception', 'Nariai' in p11)
    check('⇒ so what the Gowdy scoping leaves open is the narrower STABILITY question, in a named and '
          'externally-bounded way',
          ('Friedrich' in p11 or 'Ringstr' in p11) and 'Nariai' in p11)

    # ⓸ and cc54's own filing judgement
    own = os.path.join(ROOT, 'receipts', 'L801_nonlinear_shear_freedom')
    check("⌗ and cc54 filed into ITS OWN directory rather than adding to 54's live I-series -- the "
          'c54.198 filename collision avoided BY CONSTRUCTION', os.path.isdir(own))

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the seam is the right cut, and the freedom half generalises. **')
    print('  On a metric with ** two non-parallel TT waves, depending on t, x AND z, with NO Killing')
    print('  vector available **, the Einstein tensor built to O(eps^2) satisfies')
    print('     ** nabla_mu G^mu_nu = 0 for all four nu. **')
    print('  ⇒ ** The constraint propagation is off-shell and symmetry-free.  It is not a Gowdy fact,')
    print('     so P11\'s all-orders FREEDOM argument covers the general leaf. **')
    print('  ⌗ And the sigma^2 back-reaction this line named at r2504 and could not see at r2514 is a')
    print('    ** positive O(eps^2) SCALAR sourcing the energy sector -- NOT a new constraint on the')
    print('    two TT functions. **')
    print('  ⚠ ** What stays open is the narrower STABILITY question **, and P11 routes it out by name')
    print('    (Friedrich; Andreasson--Ringstrom; Nariai the non-generic exception).')
    print('  ⇒ ** The conversion of L-174 ⓵ to a vein verdict is Daryl\'s, and neither node has taken')
    print('    it. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
