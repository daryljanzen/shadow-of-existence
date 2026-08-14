#!/usr/bin/env python3
"""Q1 -- `PO-6`'s dark half HAS an object, and the answer separates ONE claim into TWO degeneracies
that r2677 stated as one.  The one with a CHOICE in it survives back-reaction completely; the one
that was an accident of constant curvature does not; and the real limit is the SHEAR.

** WHAT THE ROW SAYS, r2713. **  *** "A counterterm basis is a statement about a class of FIXED
backgrounds, and in the coupled sector there is no such class to state it on -- which is a statement
about what the question can MEAN, not a calculation waiting to be run." ***
  ⌗ ** That reading follows from r2677's stated REASON, and the reason is not what carries the
    result. **  r2677 (and this fork's own c54.210, and `S50`) attributed the collapse to MAXIMAL
    SYMMETRY -- "the counterterm basis is one-dimensional because the admitted background family is."
    *** If the degeneracy needs a one-parameter family of fixed backgrounds, then quantizing the
    scale factor does remove the class, and the question does lose its object.  It does not need
    one. ***

** ⛭⛭⛭ ⓵ THE DEFICIT IS EXACTLY $C^{2}$, AND EVERY FRW IS CONFORMALLY FLAT FOR EVERY $a(T)$. **
In four dimensions $C_{\\mu\\nu\\rho\\sigma}C^{\\mu\\nu\\rho\\sigma}=\\mathrm{Riem}^{2}-2\\,\\mathrm{Ric}^{2}
+\\tfrac13R^{2}$.  Computed here from the metric, with $a$ a FREE FUNCTION and no assumption on it:

      *** Riem^2 - (2 Ric^2 - R^2/3) = 0   identically,  at k = +1, 0 and -1 ***

** ⓶ AND THE GAUSS--BONNET COMBINATION IS AN EXACT TOTAL DERIVATIVE THERE, ALSO FOR EVERY $a(T)$. **

      *** sqrt(g) (R^2 - 4 Ric^2 + Riem^2)  =  d/dT [ 24 ( a'^3/3 + a' ) ]   exactly ***

⇒⇒ *** ⓵ AND ⓶ TOGETHER FIX $\\int\\!\\sqrt g\\,\\mathrm{Ric}^{2}$ AND $\\int\\!\\sqrt g\\,
\\mathrm{Riem}^{2}$ FROM $\\int\\!\\sqrt g\\,R^{2}$ UP TO A BOUNDARY TERM, ON EVERY FRW WHATEVER.  The
three quadratic invariants -- the ONLY place in the basis where a CHOICE exists, three functionals at
one dimension -- span a ONE-DIMENSIONAL space for every scale factor. ***
  ⌗ ** And the relation is POINTWISE in $a(\\cdot)$: an identity on each geometry separately, not an
    evaluation on a chosen class. **  *** An identity that holds on every member of a set survives
    superposition.  So it descends to the sector where $a$ is quantized as an operator relation, and
    the coupled sector does not need "a class of fixed backgrounds" for the statement to be made --
    because the statement was never made by evaluating on a class. ***

** ⛔ ⓷ AND THE OTHER HALF OF r2677's CLAIM REALLY DOES FAIL, WHICH IS WHAT THE ROW WAS TRACKING. **
On a maximally symmetric background $R$ is constant, so $\\int\\!\\sqrt g$, $\\int\\!\\sqrt g\\,R$ and
$\\int\\!\\sqrt g\\,R^{2}$ -- terms of DIFFERENT dimension -- are proportional too, and the basis is
one-dimensional at every order.  *That is the part maximal symmetry buys, and it is lost the moment
$a$ is not the de Sitter $\\cosh$.*  Shown on P15's own radiation-free layer $a=\\sinh^{2/3}(3Ht/2)$:
$R$ RUNS from $\\infty$ to $12H^{2}$, so $R^{2}$ is $t$-dependent and the different-dimension terms
part company -- *** while the quadratic identity holds on that same running layer EXACTLY (symbolic
zero). ***
⇒⇒ *** SO r2677's PREMISE FAILS AND ITS CONCLUSION SURVIVES, AND SEPARATING THE TWO IS THE WHOLE OF
IT.  r2713 read the premise's failure as the conclusion's, which is why the dark half looked like a
question about what a question can mean. ***
  ⌗ ** And withdrawn `L-543` asked a real question after all. **  It asked whether the one-dimensional
    basis survives on a background whose curvature RUNS.  *** For the sector where a basis choice
    exists, the answer is YES, and it is computed here on the very layer r2677 named.  The withdrawal's
    OCCASION was right -- the free tower's own background is constant-curvature -- and its REASON,
    "the question has no object", was not. ***

** ⛭⛭ ⓸ AND THE REAL LIMIT IS DETERMINATE, AND IT IS NOT THE SCALE FACTOR. **  The deficit IS $C^{2}$,
so the degeneracy ends exactly where conformal flatness does -- at the SHEAR.  On an axisymmetric
Bianchi~I shear of amplitude $\\sigma$ over an isotropic expansion:

      *** C^2 = sigma^2 ( 4 + 16 sigma^2 / 3 )  =  4 sigma^2 + O(sigma^4) ***

zero at $\\sigma=0$ and entering at SECOND order in the shear amplitude.
⇒⇒ *** AND THE TOWER IS THE TRANSVERSE-TRACELESS SHEAR -- P10's own words for what propagates.  So
what ends the one-dimensional quadratic basis is the TOWER'S OWN TENSOR CONTENT at second order in the
mode amplitude, and not the scale factor at any order.  `PO-6`'s dark half is that calculation, and it
is a calculation. ***

WHAT IS NOT CLAIMED.  ** Not that the coupled sector is renormalizable ** -- this says which functionals
a divergence can need, not that the divergences are absorbable.  ** Not a heat-kernel computation ** --
no coefficient is computed here; the claim is about the SPAN of the admitted counterterms.
** Not that the basis is one-dimensional at every order under back-reaction ** -- ⓷ shows exactly the
opposite, and that half of r2677 is withdrawn here.  ** Not a second-order tower calculation ** --
Bianchi~I is a HOMOGENEOUS shear and fixes the order at which conformal flatness fails; the mode-by-mode
statement on P10's tower is what the row now owes.  ** And not a closure ** -- `PO-6` stays open; this
narrows it and the re-verdict is 56's.

Written c54.215, `L-549`.  Stated for reversal.
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


def flat(path):
    return re.sub(r'\s+', ' ', open(path, encoding='utf-8', errors='replace').read())


# ---------------------------------------------------------------- curvature, from the metric
def invariants(g, x):
    """R, Ric^2, Riem^2 for a diagonal 4-metric -- computed from g, nothing hard-coded."""
    n = 4
    gi = g.inv()
    Gam = [[[sp.simplify(sum(gi[i, l]*(sp.diff(g[l, j], x[k]) + sp.diff(g[l, k], x[j])
                                       - sp.diff(g[j, k], x[l])) for l in range(n))/2)
             for k in range(n)] for j in range(n)] for i in range(n)]

    def Rm(i, j, k, l):
        e = sp.diff(Gam[i][j][l], x[k]) - sp.diff(Gam[i][j][k], x[l])
        e += sum(Gam[i][k][m]*Gam[m][j][l] - Gam[i][l][m]*Gam[m][j][k] for m in range(n))
        return sp.simplify(e)

    R4 = [[[[Rm(i, j, k, l) for l in range(n)] for k in range(n)] for j in range(n)]
          for i in range(n)]
    Ric = sp.Matrix(n, n, lambda j, l: sp.simplify(sum(R4[i][j][i][l] for i in range(n))))
    Rs = sp.simplify(sum(gi[j, l]*Ric[j, l] for j in range(n) for l in range(n)))
    Rd = [[[[sp.simplify(sum(g[i, m]*R4[m][j][k][l] for m in range(n))) for l in range(n)]
            for k in range(n)] for j in range(n)] for i in range(n)]
    riem2 = sp.simplify(sum(Rd[A][B][C][D]**2*gi[A, A]*gi[B, B]*gi[C, C]*gi[D, D]
                            for A in range(n) for B in range(n)
                            for C in range(n) for D in range(n)))
    ric2 = sp.simplify(sum(gi[i, i]*gi[j, j]*Ric[i, j]**2 for i in range(n) for j in range(n)))
    return Rs, ric2, riem2


def weyl_sq(Rs, ric2, riem2):
    """In 4D: C^2 = Riem^2 - 2 Ric^2 + R^2/3.** COMPUTES: the Weyl-squared combination Riem^2 - 2 Ric^2 + R^2/3 on FRW at k = +1, 0, -1 for a
FREE a(T), and the Gauss-Bonnet total-derivative identity.  *** The scale factor and the spatial
curvature are the corpus's own; nothing is imported. ***  ⌗ Scope added r2738 by 56 on merge --
check_computes fires on this receipt and the band is 54's, but a one-line declaration that
blocks the whole gate is a repair, not an edit to their finding. **

"""
    return sp.simplify(riem2 - 2*ric2 + Rs**2/3)


def main():
    print()
    print('  Q1 -- PO-6: does back-reaction remove the object of the counterterm question?')
    print()

    # ------------------------------------------------- (1) what the row and the receipt say
    po = flat(os.path.join(ROOT, 'PROTECTED_OPEN.md'))
    check('⓵ the row states the dark half as a question about MEANING: "a counterterm basis is a '
          'statement about a class of FIXED backgrounds, and in the coupled sector there is no such '
          'class to state it on"',
          '**A counterterm basis is a statement about a class of FIXED backgrounds, and in the '
          'coupled sector there is no such class to state it on** — which is a statement about what '
          'the question can MEAN, not a calculation waiting to be run' in po)
    s50 = flat(os.path.join(ROOT, 'receipts', 'L165_defining_the_sum',
                            'S50_the_counterterm_basis_is_one_dimensional_because_the_background_'
                            'family_is.py'))
    check('   and the claim it descends from names MAXIMAL SYMMETRY as the reason: "THE INVARIANT '
          'BASIS ON A MAXIMALLY SYMMETRIC BACKGROUND"',
          'THE INVARIANT BASIS ON A MAXIMALLY SYMMETRIC BACKGROUND' in s50)

    # ------------------------------------------------- (2) the identity, general a(T), all k
    T = sp.Symbol('T', real=True)
    a = sp.Function('a', positive=True)(T)
    chi, th, ph = sp.symbols('chi theta varphi', real=True)
    for kk, S in ((1, sp.sin(chi)), (0, chi), (-1, sp.sinh(chi))):
        g = sp.diag(-1, a**2, a**2*S**2, a**2*S**2*sp.sin(th)**2)
        Rs, ric2, riem2 = invariants(g, [T, chi, th, ph])
        C2 = weyl_sq(Rs, ric2, riem2)
        check(f'⓶ k={kk:+d}: Weyl^2 = Riem^2 - 2 Ric^2 + R^2/3 = {C2} for a FREE a(T) -- '
              'CONFORMALLY FLAT, with no assumption on the scale factor',
              C2 == 0)
        if kk == 1:
            R_k1, ric2_k1, riem2_k1 = Rs, ric2, riem2

    # ------------------------------------------------- (3) Gauss-Bonnet is an exact total derivative
    ad = sp.diff(a, T)
    GBdens = sp.simplify(a**3*(R_k1**2 - 4*ric2_k1 + riem2_k1))
    F = 24*(ad**3/3 + ad)
    check(f'⓷ and sqrt(g)(R^2 - 4 Ric^2 + Riem^2) = d/dT[24(a\'^3/3 + a\')] EXACTLY, for every a(T) '
          f'-- the Gauss-Bonnet term is a boundary term on FRW, not a functional in the basis',
          sp.simplify(sp.diff(F, T) - GBdens) == 0)
    # ⓶ + ⓷ solved explicitly: with C^2 = 0 and GB = boundary, both Ric^2 and Riem^2 are fixed by
    # R^2.  Solve the two linear relations and check the coefficients rather than asserting them.
    A_, B_, C_, chi_ = sp.symbols('A B C chieuler')
    sol = sp.solve([A_ - 4*B_ + C_ - chi_, C_ - 2*B_ + A_/3], [B_, C_], dict=True)[0]
    check(f'   ⇒ ⓶ + ⓷ SOLVE: int Ric^2 = {sp.simplify(sol[B_])} and int Riem^2 = '
          f'{sp.simplify(sol[C_])} -- both fixed by int R^2 up to the boundary term, on EVERY FRW, '
          'so the three quadratic invariants span ONE dimension for every scale factor',
          sp.simplify(sol[B_] - (A_/3 - chi_/2)) == 0
          and sp.simplify(sol[C_] - (A_/3 - chi_)) == 0)

    # ------------------------------------------------- (4) r2677's own background reproduced
    al = sp.Symbol('alpha', positive=True)
    ds = al*sp.cosh(T/al)
    sub = {sp.diff(a, T, 2): sp.diff(ds, T, 2), sp.diff(a, T): sp.diff(ds, T), a: ds}
    vals = [sp.simplify(e.subs(sub)) for e in (R_k1, R_k1**2, ric2_k1, riem2_k1)]
    check(f'⓸ at P10\'s own slicing a = alpha cosh(T/alpha): R = {vals[0]}, R^2 = {vals[1]}, '
          f'Ric^2 = {vals[2]}, Riem^2 = {vals[3]} -- S50\'s D=4 row, reproduced from the metric',
          vals[0] == 12/al**2 and vals[1] == 144/al**4
          and vals[2] == 36/al**4 and vals[3] == 24/al**4)
    # ** r2738, 56 on merge, per cc54's own c54.213 principle: *** an absence receipt that FAILS
    # because its finding was ACTED ON is a SUCCESS.  The misquote cc54 found was real -- 80 is
    # S50's D=5 entry, and dS_4 gives 144/36/24, verified here by direct computation.  The
    # register was corrected at r2738, so this converts to a REGRESSION GUARD on the filling. ***
    check('✔ ⛭ AND THE REGISTER MISQUOTE cc54 FOUND IS FIXED (r2738): PROTECTED_OPEN carried '
          '"144/80/24" where dS_4 gives 144/36/24 -- 80 was S50\'s D=5 entry.  The guard is now '
          'on the correction holding',
          '144/36/24' in po and '144/80/24' not in po)

    # ------------------------------------------------- (5) the RUNNING layer
    # ⚠ HONESTY ABOUT WHAT THIS ADDS.  (2) proved the identity for a FREE a(T), so substituting a
    #   particular a into that expression is trivially zero and proves nothing.  What is done here
    #   instead is an INDEPENDENT second path: the invariants are recomputed from the layer's own
    #   metric, and the deficit is rationalised in u = exp(3Ht/2) -- a different variable, a
    #   different simplification route.  What the layer genuinely ADDS is (5b) and (6): that its
    #   curvature RUNS, and that the different-dimension degeneracy fails on it.
    t, H = sp.symbols('t H', positive=True)
    u = sp.Symbol('u', positive=True)
    aL = sp.sinh(sp.Rational(3, 2)*H*t)**sp.Rational(2, 3)
    gL = sp.diag(-1, aL**2, aL**2*chi**2, aL**2*chi**2*sp.sin(th)**2)
    RsL, ric2L, riem2L = invariants(gL, [t, chi, th, ph])
    C2L = weyl_sq(RsL, ric2L, riem2L)
    # rationalise: sinh/cosh(3Ht/2) -> (u -/+ 1/u)/2, which makes the whole thing a rational function
    rat = {sp.sinh(sp.Rational(3, 2)*H*t): (u - 1/u)/2, sp.cosh(sp.Rational(3, 2)*H*t): (u + 1/u)/2}
    C2u = sp.simplify(sp.radsimp(sp.together(
        sp.expand(C2L.rewrite(sp.exp).subs(t, 2*sp.log(u)/(3*H)))
        if C2L != 0 else sp.Integer(0))))
    early, late = sp.limit(RsL, t, 0, '+'), sp.limit(RsL, t, sp.oo)
    check(f'⓹ on P15\'s OWN running layer a = sinh^(2/3)(3Ht/2), recomputed from ITS metric: R runs '
          f'{early} -> {late}, so the curvature genuinely RUNS',
          early == sp.oo and late == 12*H**2)
    check(f'   and the deficit vanishes on it by a SECOND route -- rationalised in u = exp(3Ht/2), '
          f'Weyl^2 = {C2u}',
          C2u == 0)
    # and numerically, to guard the symbolic route.
    # ⚠ A THRESHOLD HERE WOULD BE A GUESS FITTED TO THE ANSWER.  The metric-derived expression has
    #   catastrophic cancellation, so the residual is set by working precision, not by the physics
    #   -- at 40 digits it sits at 1e-12, which no honest threshold could have been picked for in
    #   advance.  The signature of an EXACT zero is not "small" but "shrinks with precision", so
    #   the test is a SCALING one: double the precision and the residual must fall by tens of
    #   orders.  A genuinely non-zero deficit would sit still.
    import mpmath as mp
    # the invariants are scalars, so they cannot depend on chi or theta; freeze them at generic
    # values (and the freeze is itself a check -- a leftover angular dependence would show up)
    ang = {chi: sp.Rational(7, 10), th: sp.pi/3}
    fnum = sp.lambdify((t, H), C2L.subs(ang), 'mpmath')
    scale = sp.lambdify((t, H), riem2L.subs(ang), 'mpmath')

    def worst_at(dps):
        mp.mp.dps = dps
        one = mp.mpf(1)
        return max(abs(fnum(mp.mpf(x)/10, one))/abs(scale(mp.mpf(x)/10, one))
                   for x in (3, 10, 20, 50))

    w40, w80 = worst_at(40), worst_at(80)
    check(f'   and independently the residual SCALES WITH PRECISION: |Weyl^2|/|Riem^2| goes '
          f'{mp.nstr(w40, 3)} at 40 digits to {mp.nstr(w80, 3)} at 80 -- which an exact zero does '
          'and a real deficit does not',
          w80 < w40*mp.mpf('1e-20'))
    check('   ⇒ withdrawn L-543 asked a real question -- "does the one-dimensional basis survive on a '
          'background whose curvature runs?" -- and for the sector where a CHOICE exists the answer '
          'is YES, on the layer r2677 named',
          C2u == 0 and early == sp.oo)

    # ------------------------------------------------- (6) the OTHER half really does fail
    R2run = sp.simplify(RsL**2)
    ratio = sp.simplify(R2run.subs(t, 1/H)/R2run.subs(t, 3/H))
    check(f'⛔ ⓺ AND THE DIFFERENT-DIMENSION HALF FAILS, WHICH IS WHAT THE ROW WAS TRACKING: R^2 is '
          f't-dependent on the layer (ratio {sp.N(ratio, 8)} between t=1/H and t=3/H), so int sqrt(g) '
          f'and int sqrt(g) R^2 are NOT proportional once a is not the de Sitter cosh',
          sp.simplify(ratio - 1) != 0 and abs(float(sp.N(ratio)) - 1) > 1e-3)
    check('   ⇒ *** r2677\'s PREMISE fails and its CONCLUSION survives. r2713 read the first as the '
          'second, which is why the dark half looked like a question about meaning. ***',
          C2u == 0 and abs(float(sp.N(ratio)) - 1) > 1e-3)

    # ------------------------------------------------- (7) CONTROL: SdS, the corpus's own background
    r, M, La = sp.symbols('r M Lambda', positive=True)
    RsS, ric2S, riem2S = 4*La, 4*La**2, sp.Rational(8, 3)*La**2 + 48*M**2/r**6
    C2S = sp.simplify(weyl_sq(RsS, ric2S, riem2S))
    check(f'⛔ CONTROL -- the identity is NOT vacuous, and the corpus\'s own SdS is what breaks it: '
          f'Weyl^2 = {C2S}, zero iff M = 0',
          sp.simplify(C2S - 48*M**2/r**6) == 0 and sp.simplify(C2S.subs(M, 0)) == 0)

    # ------------------------------------------------- (8) SCOPE: shear is the real limit
    x = [t] + list(sp.symbols('x y z', real=True))
    sig = sp.Symbol('sigma', real=True)
    gB = sp.diag(-1, sp.exp(2*t), sp.exp(2*(t + sig*t)), sp.exp(2*(t - sig*t)))
    RsB, ric2B, riem2B = invariants(gB, x)
    C2B = sp.simplify(sp.expand(weyl_sq(RsB, ric2B, riem2B)))
    lead = sp.simplify(sp.series(C2B, sig, 0, 4).removeO())
    check(f'⛭ SCOPE -- and the real limit is the SHEAR, not the scale factor: on an axisymmetric '
          f'Bianchi I shear of amplitude sigma over an isotropic expansion, Weyl^2 = {C2B}',
          sp.simplify(C2B - sig**2*(4 + 16*sig**2/3)) == 0)
    check(f'   zero at sigma = 0 and entering at SECOND order: {lead}',
          sp.simplify(C2B.subs(sig, 0)) == 0 and sp.simplify(lead - 4*sig**2) == 0)
    p10 = flat(os.path.join(ROOT, 'corpus', 'canonical_time.tex'))
    check('   ⇒ AND THE TOWER IS THAT SHEAR, in P10\'s own words: "The propagating degree of '
          'freedom is the transverse-traceless shear of the evolving layer"',
          'The propagating degree of freedom is the transverse-traceless shear of the evolving '
          'layer' in p10)

    # ------------------------------------------------- (9) banked in P10, and declining the closure
    check('⛭ and the result is BANKED in P10, not only here: "no scale factor breaks it, because no '
          'scale factor can make an FRW geometry anything but conformally flat"',
          'no scale factor breaks it, because no scale factor can make an FRW geometry anything '
          'but conformally flat' in p10)
    check('   ⚠ and P10 DECLINES the closure in the same passage: "what remains is the tower\'s own '
          'shear, which is a calculation and not a question about meaning"',
          "what remains is the tower's own shear, which is a calculation and not a question about "
          'meaning' in p10)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** PO-6\'s dark half HAS an object, and r2677 stated TWO degeneracies as one. **')
    print('  ⓵ ** The one with a CHOICE in it — three quadratic invariants at one dimension — is')
    print('     one-dimensional on EVERY FRW, for EVERY a(T): the deficit is exactly Weyl^2, FRW is')
    print('     conformally flat whatever the scale factor, and Gauss-Bonnet is an exact total')
    print('     derivative there.  ** No scale factor can break it, so back-reaction cannot. **')
    print('  ⛭⛭ ⓶ *** And the relation is POINTWISE in a(·) — an identity on each geometry, not an')
    print('     evaluation on a class.  An identity true of every member of a set survives')
    print('     superposition, so it descends to the quantized sector as an operator relation: the')
    print('     coupled sector never needed "a class of fixed backgrounds" to state it on. ***')
    print('  ⛔ ⓷ ** The one that was an ACCIDENT of constant curvature does fail ** — different-')
    print('     dimension terms stop being proportional the moment a is not the de Sitter cosh.')
    print('     *** So r2677\'s premise fails and its conclusion survives, and r2713 read the first')
    print('     as the second. ***')
    print('  ⛭ ⓸ *** And the real limit is determinate: the deficit IS Weyl^2, so the degeneracy')
    print('     ends at the SHEAR — 4 sigma^2 + O(sigma^4) on Bianchi I — and the tower IS the')
    print('     transverse-traceless shear.  PO-6\'s dark half is that calculation. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
