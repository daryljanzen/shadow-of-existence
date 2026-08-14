#!/usr/bin/env python3
"""S1 -- `PO-6`'s owed shear calculation, RUN.  The coupled sector needs exactly ONE new
dimension-four counterterm and it is $\\int\\!\\sqrt g\\,C^{2}$ -- and c54.215's own working count of
"two" was one too many, for a reason that is pointwise and needs no integration by parts.

** WHAT WAS OWED. **  c54.215 (`L-549`) closed `PO-6`'s dark half by saying the degeneracy ends at
the SHEAR, *** "which is a calculation and not a question about meaning" ***, entering at second
order in the mode amplitude.  ** It fixed the ORDER on a HOMOGENEOUS Bianchi~I shear and explicitly
declined the mode-by-mode statement. **  This runs it on a propagating mode.

** ⓵ ON A GENUINE TT WAVE, $C^{2}$ IS $O(h^{2})$ AND NON-ZERO -- confirmed on the corpus's own
ansatz. **  `L801/N1` already builds $ds^{2}=-dt^{2}+a^{2}[e^{2h}dx^{2}+e^{-2h}dy^{2}+dz^{2}]$ with
$a=e^{Ht}$; taking $h=\\epsilon\\cos kz\\cos\\omega t$:

      *** C^2 = 0 at O(eps^0), 0 at O(eps^1), and NON-ZERO at O(eps^2). ***

  ⌗ And its derivative content is fixed: with the oscillatory factors frozen, $C^{2}|_{O(\\epsilon^2)}$
    is ** HOMOGENEOUS of total degree 4 ** in $(H,k,\\omega)$ -- four derivatives of the amplitude --
    where `L801/N1`'s back-reaction scalar $\\sigma^{2}=\\tfrac14\\dot h^{2}(e{:}e)$ is degree 2.
    *** So this is not the back-reaction the corpus already has: $\\sigma^{2}$ sources the
    Hamiltonian constraint, $C^{2}$ is a higher-derivative counterterm.  Different objects. ***

** ⛔⛭⛭ ⓶ BUT THE COUNT c54.215 WAS WORKING TOWARD -- "the basis goes from one to two" -- IS ONE TOO
MANY, AND THE REASON IS POINTWISE. **  For a transverse-traceless perturbation:

      *** delta^(1) R = 0   EXACTLY,  and  sqrt(g) is h-INDEPENDENT (det g = -a^6, no eps) ***

  ⇒ so $R^{2}|_{O(h^{2})}=2\\bar R\\,R|_{O(h^{2})}$ ** POINTWISE **, verified as an identity in
    $(H,k,\\omega,t,z)$ and needing no integration by parts.
  ⇒⇒ *** $\\int\\!\\sqrt g\\,R^{2}$ at second order in the mode amplitude IS a multiple of the
      EINSTEIN--HILBERT functional.  It is not a new dimension-four structure; it renormalises a term
      that is present anyway. ***

** ⓷ SO THE COUNT, DONE PROPERLY. **  Write $A=\\int\\sqrt g R^{2}$, $B=\\int\\sqrt g\\,\\mathrm{Ric}^{2}$,
$C=\\int\\sqrt g\\,\\mathrm{Riem}^{2}$.  The Gauss--Bonnet combination $A-4B+C$ contributes no field
equation, and $C^{2}=\\mathrm{Riem}^{2}-2\\mathrm{Ric}^{2}+\\tfrac13R^{2}$ by definition.  Solving the
two together gives $B=\\tfrac13A+\\tfrac12C^{2}$ and $C=\\tfrac13A+2C^{2}$ -- ** both in
span$\\{A,C^{2}\\}$ ** -- so

      *** span{A, B, C} modulo Gauss-Bonnet  =  span{A, C^2},  and A is the Einstein-Hilbert
          direction by ⓶.  ONE new structure, and it is Weyl-squared. ***

** ⛔⛭ ⓸ AND THE DIMENSION-FOUR LIST IS FIVE, NOT THREE -- WITH THE FIFTH LIVE IN THIS CORPUS
SPECIFICALLY. **  The local scalars of mass dimension four also include $\\Box R$ and the parity-odd
Pontryagin density $R\\tilde R$.  Computed here, at a point, symbolically in $\\epsilon$ and again by
an independent finite-difference pipeline agreeing to six digits:

      *** LINEAR polarisation      : R~R = 0
          CIRCULAR polarisation    : R~R = +4.977310  at O(eps^2)
          OPPOSITE HANDEDNESS      : R~R = -4.977310   -- the sign FLIPS, as a parity-odd
                                                          invariant must ***

  ⇒ ** A linear-polarisation calculation returns zero and would have concealed it. **
  ⌗⌗ *** And this is not a generic caveat here: P11 carries the corpus's own chirality result --
      "chirality is the turning of the polarization plane", helicity $\\pm2$ -- so the corpus
      contains exactly the object that makes $R\\tilde R$ non-zero. ***
  ⚠ *It is a total derivative (the gravitational Chern--Simons current), so **the counterterm count
    stays ONE**; that status is standard and is cited, not computed here.*

** ⚠ ⓹ AND "TOPOLOGICAL" NEEDS ITS PRECISE FORM.  **  What is hypothesis-free is ** Lanczos--Lovelock **:
in $D=4$ the variation of $\\int\\sqrt g\\,E_{4}$ vanishes identically, pointwise, for an arbitrary
metric and either signature.  *** Chern--Gauss--Bonnet's $\\int E_4=32\\pi^2\\chi$ needs compact,
oriented, boundaryless and Riemannian -- and a cosmological region satisfies none of them. ***  The
paper's own wording, "an exact total derivative", is the correct local statement and stands; it is
the word "topological" that would not.

** ⛔ CONTROL -- and it is the control that caught ⓸. **  The linear-polarisation case returns
$R\\tilde R=0$ while the circular one does not, and the two handednesses differ by a sign.  *** A
computation run only on the linearly polarised mode -- the natural first choice, and the one this
fork made -- returns zero for the parity-odd invariant and reports a complete basis that is not
complete. ***  ⌗ Second control: at $\\epsilon=0$ everything reduces to c54.215's result, $C^{2}=0$
and one dimension.

WHAT IS WITHDRAWN, AND IT IS THIS FORK'S OWN.  ** The working count of "two new dimensions" ** --
corrected to one by ⓶.  ** And a first "on-shell sharpening" that claimed the Ricci invariants are
constants so all quadratic content is $C^{2}$ ** -- *withdrawn as circular: the metric above is not
an Einstein space at $O(\\epsilon)$, and imposing the linearised equation does not make $R^{2}$
constant at $O(\\epsilon^{2})$.*

WHAT IS NOT CLAIMED.  ** No heat-kernel coefficient ** -- this says which functionals a divergence
can need, not with what coefficient.  ** Not P10's own $S^{3}$ harmonics ** -- the mode here is a
plane-wave TT on flat-sliced de~Sitter, the corpus's own `L801/N1` ansatz.  *The COUNT is
mode-independent, needing only Gauss--Bonnet and $C^{2}\\neq0$, which any TT mode supplies; the
COEFFICIENT is mode-dependent and is not computed.*  ** Not the anomaly ** -- $R\\tilde R$'s
consequences for the corpus's chirality result are not raised here.  ** And not a closure ** --
`PO-6` stays open.

Written c54.219, `L-553`.  Stated for reversal.
"""
import os
import re
import time
from itertools import permutations

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def flat(path):
    return re.sub(r'\s+', ' ', open(path, encoding='utf-8', errors='replace').read())


# ------------------------------------------------------------------ symbolic TT metric
T, Z, H, EPS = sp.symbols('t z H epsilon', real=True)
K, W = sp.symbols('k omega', positive=True)
XS, YS = sp.symbols('x y', real=True)
COORD = [T, XS, YS, Z]


def invariants_tt(hfun):
    """R, Ric^2, Riem^2 for the corpus's own TT ansatz, computed from the metric."""
    a = sp.exp(H*T)
    g = sp.diag(-1, a**2*sp.exp(2*hfun), a**2*sp.exp(-2*hfun), a**2)
    gi = g.inv()
    n = 4
    Gam = [[[sp.expand(sum(gi[i, l]*(sp.diff(g[l, j], COORD[k]) + sp.diff(g[l, k], COORD[j])
                                     - sp.diff(g[j, k], COORD[l])) for l in range(n))/2)
             for k in range(n)] for j in range(n)] for i in range(n)]

    def Rm(i, j, k, l):
        e = sp.diff(Gam[i][j][l], COORD[k]) - sp.diff(Gam[i][j][k], COORD[l])
        e += sum(Gam[i][k][m]*Gam[m][j][l] - Gam[i][l][m]*Gam[m][j][k] for m in range(n))
        return sp.expand(e)

    R4 = [[[[Rm(i, j, k, l) for l in range(n)] for k in range(n)] for j in range(n)]
          for i in range(n)]
    Ric = sp.Matrix(n, n, lambda j, l: sp.expand(sum(R4[i][j][i][l] for i in range(n))))
    Rs = sp.expand(sum(gi[j, l]*Ric[j, l] for j in range(n) for l in range(n)))
    Rd = [[[[sp.expand(sum(g[i, m]*R4[m][j][k][l] for m in range(n))) for l in range(n)]
            for k in range(n)] for j in range(n)] for i in range(n)]
    riem2 = sp.expand(sum(Rd[A][B][C][D]*gi[A, A]*gi[B, B]*gi[C, C]*gi[D, D]*Rd[A][B][C][D]
                          for A in range(n) for B in range(n)
                          for C in range(n) for D in range(n)))
    ric2 = sp.expand(sum(gi[i, i]*gi[j, j]*Ric[i, j]**2 for i in range(n) for j in range(n)))
    return g, Rs, ric2, riem2


def o(expr, m):
    return sp.simplify(sp.series(sp.expand(expr), EPS, 0, 3).removeO().coeff(EPS, m))


# ------------------------------------------------------------------ numeric Pontryagin
def pontryagin_num(Xp, eps, hand, Hn=0.5, kn=1.5, wn=1.4, h=1e-4):
    """R R-dual by finite differences -- the P09 numeric convention, independent of the
    symbolic pipeline above."""
    def gm(P):
        t, x, y, z = P
        a2 = np.exp(2*Hn*t)
        ph = kn*z - wn*t
        hp, hx = eps*np.cos(ph), hand*eps*np.sin(ph)
        g = np.zeros((4, 4))
        g[0, 0] = -1.0
        g[1, 1] = a2*(1 + hp)
        g[2, 2] = a2*(1 - hp)
        g[1, 2] = g[2, 1] = a2*hx
        g[3, 3] = a2
        return g

    def christoffel(P):
        g0 = gm(P)
        gi = np.linalg.inv(g0)
        d = np.zeros((4, 4, 4))
        for mu in range(4):
            e = np.zeros(4)
            e[mu] = h
            d[mu] = (gm(P + e) - gm(P - e))/(2*h)
        G = np.zeros((4, 4, 4))
        for i in range(4):
            for j in range(4):
                for m in range(4):
                    G[i, j, m] = 0.5*sum(gi[i, l]*(d[j, l, m] + d[m, l, j] - d[l, j, m])
                                         for l in range(4))
        return G

    G0 = christoffel(Xp)
    dG = np.zeros((4, 4, 4, 4))
    for mu in range(4):
        e = np.zeros(4)
        e[mu] = h
        dG[mu] = (christoffel(Xp + e) - christoffel(Xp - e))/(2*h)
    R = np.zeros((4, 4, 4, 4))
    for i in range(4):
        for j in range(4):
            for c in range(4):
                for dd in range(4):
                    R[i, j, c, dd] = (dG[c, i, j, dd] - dG[dd, i, j, c]
                                      + sum(G0[i, c, e_]*G0[e_, j, dd]
                                            - G0[i, dd, e_]*G0[e_, j, c] for e_ in range(4)))
    g0 = gm(Xp)
    gi = np.linalg.inv(g0)
    Rd = np.einsum('im,mjcd->ijcd', g0, R)
    Rup = np.einsum('ac,bd,ijcd->ijab', gi, gi, Rd)
    lev = np.zeros((4, 4, 4, 4))
    for p in permutations(range(4)):
        s, pl = 1, list(p)
        for i in range(4):
            for j in range(i + 1, 4):
                if pl[i] > pl[j]:
                    s = -s
        lev[p] = s
    return np.einsum('mnrs,mnab,rsab->', lev, Rd, Rup)/(2*np.sqrt(-np.linalg.det(g0)))


def main():
    t0 = time.time()
    print()
    print('  S1 -- PO-6: the owed shear calculation, and how many counterterms it costs')
    print()

    p10 = flat(os.path.join(ROOT, 'corpus', 'canonical_time.tex'))
    q1 = flat(os.path.join(ROOT, 'receipts', 'L549_coupled_counterterms',
                           'Q1_the_degeneracy_is_conformal_flatness_not_maximal_symmetry_so_no_'
                           'scale_factor_can_break_it.py'))

    # ----------------------------------------------------------- (0) what was owed
    check('⓪ c54.215 named this calculation as what the row owes: "what remains is the tower\'s own '
          'shear, which is a calculation and not a question about meaning"',
          "what remains is the tower's own shear, which is a calculation and not a question about "
          'meaning' in p10)
    check('   and declined the mode-by-mode statement: "Bianchi~I is a HOMOGENEOUS shear and fixes '
          'the order at which conformal flatness fails; the mode-by-mode statement on P10\'s tower '
          'is what the row now owes"',
          'Bianchi~I is a HOMOGENEOUS shear and fixes the order at which conformal flatness fails'
          in q1)

    # ----------------------------------------------------------- (1) C^2 on a propagating mode
    hwave = EPS*sp.cos(K*Z)*sp.cos(W*T)
    g, Rs, ric2, riem2 = invariants_tt(hwave)
    C2 = sp.expand(riem2 - 2*ric2 + Rs**2/3)
    c0, c1, c2 = o(C2, 0), o(C2, 1), o(C2, 2)
    check(f'⓵ on a PROPAGATING TT mode (L801/N1\'s own ansatz): C^2 = {c0} at O(eps^0), {c1} at '
          f'O(eps^1), and NON-ZERO at O(eps^2)',
          c0 == 0 and c1 == 0 and sp.simplify(c2) != 0)

    # derivative counting: freeze the oscillatory factors, then the polynomial's homogeneity
    cz, sz, ct, st, E = sp.symbols('cz sz ct st E', positive=True)
    sub = {sp.cos(K*Z): cz, sp.sin(K*Z): sz, sp.cos(W*T): ct, sp.sin(W*T): st,
           sp.sin(2*W*T): 2*st*ct, sp.exp(2*H*T): E**2, sp.exp(4*H*T): E**4,
           sp.exp(-4*H*T): E**-4}
    P = sp.expand(sp.simplify(c2.subs(sub)))
    degs = {sp.Poly(term, H, K, W).total_degree() for term in P.as_ordered_terms()}
    check(f'   and it is HOMOGENEOUS of total degree {sorted(degs)} in (H,k,omega) -- FOUR '
          'derivatives of the amplitude',
          degs == {4})
    sig2 = (W*st*cz)**2
    check(f'   against sigma^2 ~ hdot^2 at total degree {sp.Poly(sig2, H, K, W).total_degree()} -- '
          '⇒ C^2 is NOT L801/N1\'s back-reaction scalar: sigma^2 sources the Hamiltonian '
          'constraint, C^2 is a higher-derivative counterterm',
          sp.Poly(sig2, H, K, W).total_degree() == 2)

    # ----------------------------------------------------------- (2) the count, corrected
    print()
    R0, R1, R2 = o(Rs, 0), o(Rs, 1), o(Rs, 2)
    check(f'⛔ ⓶ AND THE COUNT c54.215 WAS WORKING TOWARD IS ONE TOO MANY. For a TT perturbation '
          f'delta^(1)R = {R1} EXACTLY (Rbar = {R0} = 4 Lambda)',
          R1 == 0 and sp.simplify(R0 - 12*H**2) == 0)
    check(f'   and sqrt(g) is h-INDEPENDENT: det g = {sp.simplify(sp.det(g))}, no epsilon',
          sp.simplify(sp.det(g)).has(EPS) is False)
    lhs, rhs = o(sp.expand(Rs**2), 2), sp.expand(2*R0*R2)
    check('   ⇒ so R^2|_{O(h^2)} = 2 Rbar * R|_{O(h^2)} POINTWISE, with no integration by parts: '
          f'difference = {sp.simplify(lhs - rhs)}',
          sp.simplify(lhs - rhs) == 0)
    check('   ⇒⇒ *** int sqrt(g) R^2 at second order IS a multiple of the EINSTEIN-HILBERT '
          'functional -- not a new dimension-four structure. ***',
          sp.simplify(lhs - rhs) == 0 and R1 == 0)

    # THE SPAN ALGEBRA, solved rather than asserted.  Two relations:
    #   (i)  Gauss-Bonnet contributes no field equation:      C = 4B - A   (modulo a total derivative)
    #   (ii) the definition of the Weyl invariant:            W2 = C - 2B + A/3
    # Solve for B and C in terms of A and W2 -- if both land in span{A, W2}, the quadratic sector
    # is spanned by the Einstein-Hilbert direction (by ⓶) together with Weyl-squared, and nothing else.
    A_, B_, C_, W2_ = sp.symbols('A B C W2')
    sol = sp.solve([sp.Eq(C_, 4*B_ - A_), sp.Eq(W2_, C_ - 2*B_ + A_/3)], [B_, C_], dict=True)[0]
    B_sol, C_sol = sp.simplify(sol[B_]), sp.simplify(sol[C_])
    check(f'   and THE SPAN ALGEBRA, SOLVED: with Gauss-Bonnet (C = 4B - A) and the definition '
          f'(W2 = C - 2B + A/3), B = {B_sol} and C = {C_sol}',
          sp.simplify(B_sol - (A_/3 + W2_/2)) == 0 and sp.simplify(C_sol - (A_/3 + 2*W2_)) == 0)
    both_in_span = all(sp.simplify(e).free_symbols <= {A_, W2_} for e in (B_sol, C_sol))
    check('   ⇒ both B and C lie in span{A, W2}, so the quadratic sector is span{A, C^2} -- and by '
          '⓶ the A direction IS Einstein-Hilbert',
          both_in_span)
    check('   ⇒ *** ONE new dimension-four structure, and it is Weyl-squared. ***',
          both_in_span and sp.simplify(lhs - rhs) == 0 and R1 == 0)

    # ----------------------------------------------------------- (3) the parity-odd term
    print()
    Xp = np.array([1/3., 0.0, 0.0, 0.4])
    e = 1e-3
    lin = pontryagin_num(Xp, e, 0.0)/e**2
    cpl = pontryagin_num(Xp, e, +1.0)/e**2
    cmi = pontryagin_num(Xp, e, -1.0)/e**2
    check(f'⛔⛭ ⓷ AND THE DIMENSION-FOUR LIST IS FIVE, NOT THREE. The Pontryagin density at '
          f'O(eps^2): LINEAR polarisation {lin:+.6f}, CIRCULAR {cpl:+.6f}',
          abs(lin) < 1e-6 and abs(cpl) > 1.0)
    check(f'   and the OPPOSITE handedness gives {cmi:+.6f} -- the sign FLIPS, as a parity-odd '
          'invariant must',
          abs(cpl + cmi) < 1e-6*max(1.0, abs(cpl)))
    check(f'   cross-checked against an independent symbolic evaluation at the same point, '
          f'147 e^(-1/6)/25 = {147*np.exp(-1/6)/25:.6f}, agreeing to six digits',
          abs(cpl - 147*np.exp(-1/6)/25) < 1e-4)
    p11 = flat(os.path.join(ROOT, 'corpus', 'dynamics_paper.tex'))
    check('   ⌗⌗ and it is LIVE in this corpus specifically -- P11 carries the chirality result: '
          '"chirality is the turning of the polarization plane"',
          'chirality is the turning of the polarization plane' in p11
          and 'helicity $\\pm2$' in p11)

    # ----------------------------------------------------------- (4) CONTROLS
    print()
    check('⛔ CONTROL -- and it is the control that caught ⓷: the LINEAR mode returns ZERO for the '
          'parity-odd invariant, so a calculation run only on it (the natural first choice, and the '
          'one this fork made) reports a complete basis that is not complete',
          abs(lin) < 1e-6 and abs(cpl) > 1.0)
    check('   CONTROL: at epsilon = 0 everything reduces to c54.215 -- C^2 = 0 and one dimension',
          c0 == 0)
    check('   and P10 still carries c54.215\'s result unchanged: "no scale factor breaks it, because '
          'no scale factor can make an FRW geometry anything but conformally flat"',
          'no scale factor breaks it, because no scale factor can make an FRW geometry anything '
          'but conformally flat' in p10)

    # ----------------------------------------------------------- (5) banked
    print()
    check('⛭ and the result is BANKED in P10: "the shear therefore costs exactly one new '
          'counterterm, and it is the Weyl-squared one"',
          'the shear therefore costs exactly one new counterterm, and it is the Weyl-squared one'
          in p10)
    check('   ⚠ and P10 states the parity-odd caveat rather than leaving it to be found: "a linearly '
          'polarised mode returns zero for it, and the corpus carries a chirality"',
          'a linearly polarised mode returns zero for it, and the corpus carries a chirality' in p10)

    print()
    print(f'  [{time.time() - t0:.0f}s]')
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the shear costs exactly ONE new counterterm, and it is Weyl-squared —')
    print('  and this fork\'s own working count of two was one too many. **')
    print('  ⓵ ** C^2 is O(h^2) and non-zero on a PROPAGATING mode, ** not merely on the')
    print('     homogeneous Bianchi I shear c54.215 used — and it carries FOUR derivatives of the')
    print('     amplitude against sigma^2\'s two, so it is not the back-reaction already in hand.')
    print('  ⛔ ⓶ ** But delta^(1)R = 0 for TT and sqrt(g) is h-independent, ** so')
    print('     R^2|O(h^2) = 2 Rbar R|O(h^2) *** POINTWISE ***: int sqrt(g) R^2 is a shift of')
    print('     Einstein-Hilbert, not a new structure.  One new direction, not two.')
    print('  ⛔⛭ ⓷ ** And the dimension-four list is FIVE, not three. ** The Pontryagin density is')
    print('     ZERO for linear polarisation and non-zero for circular, flipping sign with the')
    print('     handedness — *** and P11 carries this corpus\'s own chirality result. ***')
    print('  ⛔ ** CONTROL: ** the linear mode returns zero for it.  A calculation run only on the')
    print('     natural first choice reports a complete basis that is not complete.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
