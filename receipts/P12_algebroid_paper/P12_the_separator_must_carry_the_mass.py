#!/usr/bin/env python3
"""P12_the_separator_must_carry_the_mass.py -- the stratification's invariant, corrected.

** THE ERROR, and it was worse than a wrong number. **  P12 sec:strata argued the so(5,1)-action on the
space of cuts is NON-TRANSITIVE because "the diffeomorphism invariant R_ab R^ab = 6M^2/r^6 + 12/alpha^4
separates different-mass cuts".

  ** Schwarzschild--de Sitter is an EINSTEIN space: R_ab = Lambda g_ab.  So R_ab R^ab = 4 Lambda^2 =
     36/alpha^4 -- M-INDEPENDENT.  The stated separator cannot separate anything at all, and it does
     not equal the expression given. **

⇒ The conclusion (non-transitivity; the mass a modulus transverse to the orbits) is CORRECT and
unchanged.  What was wrong is the witness: ** a true claim was resting on an invariant that carries no
mass. **

THE FIX, and it is the corpus's own recurring invariant rather than an import: the Kretschmann scalar

    R_abcd R^abcd = 48 M^2 / r^6 + 24 / alpha^4,      d/dM = 96 M / r^6 != 0

which appears throughout P9 and the constant-ledger receipt as 48 G^2 M^2 / c^4 r^6.

PROVENANCE.  Found by node 23 in a full-corpus study pass at r501 -- ** the single physics error in
thirteen papers ** -- and re-verified by that node as still live on the current tree before it was
routed.  This receipt derives BOTH quantities from the metric rather than trusting either party:
node 23's manifest was ~2000 revisions behind, and ** its Group B was obsolete for exactly that reason,
so the Group A claim could not be taken on the manifest's authority. **  It survived the check.

Written r2439.  Stated for reversal.
"""
import sympy as sp

FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def curvature():
    t, r, th, ph = sp.symbols('t r theta phi')
    M, a = sp.symbols('M alpha', positive=True)
    f = 1 - 2*M/r - r**2/a**2
    g = sp.diag(-f, 1/f, r**2, r**2*sp.sin(th)**2)
    x = [t, r, th, ph]
    gi = g.inv()

    def Gam(i, j, k):
        return sp.simplify(sum(gi[i, l]*(sp.diff(g[l, j], x[k]) + sp.diff(g[l, k], x[j])
                                         - sp.diff(g[j, k], x[l])) for l in range(4))/2)
    G = [[[Gam(i, j, k) for k in range(4)] for j in range(4)] for i in range(4)]

    def Riem(i, j, k, l):
        e = sp.diff(G[i][j][l], x[k]) - sp.diff(G[i][j][k], x[l])
        e += sum(G[i][k][m]*G[m][j][l] - G[i][l][m]*G[m][j][k] for m in range(4))
        return sp.simplify(e)
    Rud = [[[[Riem(i, j, k, l) for l in range(4)] for k in range(4)]
            for j in range(4)] for i in range(4)]
    Ric = sp.Matrix(4, 4, lambda j, l: sp.simplify(sum(Rud[i][j][i][l] for i in range(4))))
    Rdn = [[[[sp.simplify(sum(g[i, m]*Rud[m][j][k][l] for m in range(4)))
              for l in range(4)] for k in range(4)] for j in range(4)] for i in range(4)]
    Rup = [[[[sp.simplify(sum(gi[i, p]*gi[j, q]*gi[k, s]*gi[l, u]*Rdn[p][q][s][u]
                              for p in range(4) for q in range(4)
                              for s in range(4) for u in range(4)))
              for l in range(4)] for k in range(4)] for j in range(4)] for i in range(4)]
    RicUp = sp.simplify(gi*Ric)
    RabRab = sp.simplify(sum(RicUp[i, j]*RicUp[j, i] for i in range(4) for j in range(4)))
    K = sp.simplify(sp.expand(sum(Rdn[i][j][k][l]*Rup[i][j][k][l]
                                  for i in range(4) for j in range(4)
                                  for k in range(4) for l in range(4))))
    return g, Ric, RabRab, K, M, a, r


def main():
    print()
    print('  P12 -- can R_ab R^ab separate different-mass SdS cuts?')
    print()
    g, Ric, RabRab, K, M, a, r = curvature()
    Lam = 3/a**2

    check('SdS is an EINSTEIN space: R_ab = Lambda g_ab with Lambda = 3/alpha^2',
          all(sp.simplify(Ric[i, i] - Lam*g[i, i]) == 0 for i in range(4)))
    check('therefore R_ab R^ab = 4 Lambda^2 = 36/alpha^4',
          sp.simplify(RabRab - 36/a**4) == 0)
    check('⇒ it is M-INDEPENDENT, so it cannot separate different-mass cuts',
          sp.simplify(sp.diff(RabRab, M)) == 0)
    check('and it does NOT equal the 6M^2/r^6 + 12/alpha^4 the paper stated',
          sp.simplify(RabRab - (6*M**2/r**6 + 12/a**4)) != 0)

    check('the Kretschmann scalar IS 48 M^2/r^6 + 24/alpha^4',
          sp.simplify(K - (48*M**2/r**6 + 24/a**4)) == 0)
    check('and it DOES carry the mass: d/dM = 96 M / r^6, nonzero',
          sp.simplify(sp.diff(K, M) - 96*M/r**6) == 0)
    check('so different-mass cuts are non-isometric, which is the paper\'s conclusion, unchanged',
          sp.simplify(sp.diff(K, M)) != 0)

    # the conclusion rests on the mass being a modulus TRANSVERSE to the orbits: the 3-curvature does not see it
    check('CONTROL: the scalar curvature R = 4 Lambda is also M-independent, as the paper says',
          sp.simplify(sp.diff(sp.simplify(sum(g.inv()[i, j]*Ric[i, j]
                                              for i in range(4) for j in range(4))), M)) == 0)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** SdS is Einstein, so R_ab R^ab = 36/alpha^4 and carries no mass at all. **')
    print('  The paper\'s stated separator separated nothing, and did not equal the expression given.')
    print('  ⇒ The NON-TRANSITIVITY CONCLUSION IS UNCHANGED AND CORRECT; what was wrong was its witness.')
    print('  ** The Kretschmann scalar 48 M^2/r^6 + 24/alpha^4 -- the corpus\'s own recurring invariant --')
    print('     carries the mass and does the work the sentence claimed. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
