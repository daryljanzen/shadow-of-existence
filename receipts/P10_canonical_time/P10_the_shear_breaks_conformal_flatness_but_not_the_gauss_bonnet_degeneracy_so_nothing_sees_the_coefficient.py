"""
P10_the_shear_breaks_conformal_flatness_but_not_the_gauss_bonnet_degeneracy_so_nothing_sees_the_coefficient
=========================================================================================================

LEVEL: exact symbolic (sympy) for the four-dimensional identity on two closed-form families;
30-digit numerics after symbolic differentiation for the Lanczos identity on the shear
configuration; one CONTROL that must and does break the instrument before it is believed.

OBJECT UNDER TEST -- `PO-52`'s SECOND HALF, which `r6897` made the whole row.  The order, verbatim:

    "The entry has a domain --- you established that against the row's own hope.  So: **does
     anything observe the coefficient?**  The degeneracy that made a subtraction-point change
     harmless was conformal flatness, and at second order in the shear it is gone; a separate
     Weyl-squared coefficient then exists. => What is wanted is whether any quantity this
     construction computes moves with it --- and if the honest answer is that the admitted
     second-order shear configurations are not ones anything observes, **that closes the row and
     is the result**, not a failure to find an effect.  Do not import a value for the
     coefficient."

-------------------------------------------------------------------------------
** THE ROW CLOSES, AND NOT BY THE ROUTE THE ORDER OFFERED. **

The order allowed one way to close: that nothing observes the second-order shear configurations.
That is not what this finds.  ** The configurations are observed in the only sense that matters ---
they are on the construction's own admitted list, and r6894 computed a non-vanishing invariant on
one.  What fails is the step from a non-vanishing INVARIANT to a moved OBSERVABLE, and it fails
because conformal flatness was never the only degeneracy in play. **

  ⓵ ** THERE IS A SECOND DEGENERACY AND IT IS NOT A PROPERTY OF THE FAMILY. **  In four dimensions

        C^2  =  E_4  +  2 ( R_ab R^ab  -  R^2/3 ),     E_4 = Riem^2 - 4 Ric^2 + R^2

      is an ALGEBRAIC identity on any metric -- not a feature of conformal flatness, not a feature
      of maximal symmetry, and therefore ** nothing that second order in the shear can break. **
      Verified here on closed FLRW with a(t) left free (where C^2 = 0 and both remainders are
      non-zero, so the identity is carrying weight rather than reading 0 = 0) and on
      Schwarzschild--de Sitter (where C^2 = 48 M^2/r^6 is non-zero).

  ⓶ ** AND THE GAUSS--BONNET HALF CANNOT REACH A FIELD EQUATION, ON THE SHEAR CONFIGURATION
      ITSELF. **  The Lanczos identity -- the variation of int sqrt(-g) E_4 vanishing identically
      in four dimensions -- is checked ON the confined wave, at the same amplitudes where r6894
      found C^2 non-vanishing at second order.  ** It holds to 1e-30 at 30 digits, at eps = 0 and
      at eps != 0 alike. **  So a change of subtraction point for the Weyl-squared log moves the
      equations of motion only through the Ricci-squared remainder.

  ⓷ ** AND THE RICCI REMAINDER IS NOT A GEOMETRIC CONSTANT: THE FIELD EQUATIONS SPEND IT. **
      R_ab is fixed algebraically by the stress tensor, so 2(R_ab R^ab - R^2/3) is a matter
      expression whose counterterm is of a type the ledger already carries.  On the substrate,
      which is an exact vacuum-Lambda space, it is a pure number times the volume:

        R_ab = Lambda g_ab   =>   C^2 = E_4 - 8 Lambda^2/3   EXACTLY

      -- verified symbolically on SdS -- ** so the subtraction-point change is a renormalisation
      of the cosmological term.  Which is PO-51's conclusion, reached WITHOUT conformal flatness,
      and therefore surviving exactly the order of the shear that broke PO-51's version of it. **

  ⇒ ** SO THE COEFFICIENT EXISTS, IS NON-VANISHING POINTWISE, AND MOVES NOTHING.  r6894 IS NOT
      WITHDRAWN -- IT IS THE PREMISE.  What it established (the entry has a domain) is true and
      is not sufficient, because a non-vanishing invariant is not a moved observable. **

⌗ AND THE ONE THING THAT DOES MOVE IS SHEAR-INDEPENDENT, WHICH IS WHY IT IS NOT THIS ROW'S.
  int sqrt(-g) E_4 is a topological invariant up to boundary terms, so a subtraction-point change
  shifts the on-shell action by a constant fixed by the topology.  ** That constant is there with
  or without the shear **, at eps = 0 as at eps != 0, so it is not something the broken degeneracy
  produces and it cannot be what the row was asking about.  Stated because it is the honest
  remainder, not because it reopens anything.

COMPUTES: scope -- what this settles and what it must not be read as.
  * ** ON-SHELL ONLY. **  The reduction of the Weyl-squared counterterm to topological-plus-matter
    uses the field equations to eliminate R_ab.  Off-shell -- inside a path integral over metrics
    that do not solve them -- C^2 is an independent invariant and nothing here bounds it.  ** That
    is a real restriction and it is the whole restriction. **
  * ** A MATTER-SOURCED SHEAR CONFIGURATION IS NOT THE SAME STATEMENT AS THE VACUUM ONE. **  There
    the Ricci remainder is a stress-tensor integral rather than a constant times the volume, so it
    is still not a new geometric constant but it is no longer a pure cosmological-term shift.  The
    sharp form of ⓷ is the vacuum-Lambda one and it is labelled as such.
  * ** THE VALUE 1/60 IS NOT USED, NOT NEEDED, AND NOT TESTED HERE **, as the order required.  The
    argument is coefficient-independent: it says where the coefficient's contribution goes, not
    how big it is.  The frontier table's entry is untouched.
  * ** THE LINEARISED WAVE IS EINSTEIN THROUGH FIRST ORDER ONLY. **  Its Ricci residue is measured
    and scales as eps^2 exactly -- the backreaction an exact solution carries in its own
    second-order metric correction.  ⓶ does not depend on the wave being an exact solution (the
    Lanczos identity is an identity); ⓷'s sharp form does, and is stated for exact vacuum-Lambda
    spaces with SdS as the witness rather than for the linearised wave.
  * ** Nothing here bears on PO-51 (closed), on PO-48's undetermined, on A_s, or on the tower's
    zeta(0) = 10 and log coefficient 39/4 **, which are the DEGENERATE combination's and not this
    counterterm's -- the distinction CR_synthesis sec:frontier already draws.

rc=0 on success.  Run: python3 P10_the_shear_breaks_conformal_flatness_but_not_the_gauss_bonnet_degeneracy_so_nothing_sees_the_coefficient.py
"""
import sys

import sympy as sp

print(__doc__.split("\n", 1)[1].split("COMPUTES:")[0].rstrip())
print("COMPUTES:" + __doc__.split("COMPUTES:")[1].split("rc=0")[0].rstrip())

FAILED = []


def check(ok, msg):
    print(f"    {'OK  ' if ok else 'FAIL'}  {msg}")
    if not ok:
        FAILED.append(msg)


def head(title):
    print()
    print("=" * 94)
    print(title)
    print("=" * 94)


N = 4


def _riemann(g, xs, simp):
    """Christoffels and the (1,3) Riemann tensor, from the definition."""
    gi = g.inv()
    Gam = [[[simp(sum(gi[a, d] * (sp.diff(g[d, b], xs[c]) + sp.diff(g[d, c], xs[b])
                                  - sp.diff(g[b, c], xs[d])) for d in range(N)) / 2)
             for c in range(N)] for b in range(N)] for a in range(N)]
    R = [[[[simp(sp.diff(Gam[a][b][d], xs[c]) - sp.diff(Gam[a][b][c], xs[d])
                 + sum(Gam[a][c][e] * Gam[e][b][d] - Gam[a][d][e] * Gam[e][b][c]
                       for e in range(N)))
            for d in range(N)] for c in range(N)] for b in range(N)] for a in range(N)]
    return gi, R


def invariants(g, xs, simp=sp.simplify, want_lanczos=False):
    """Riem^2, Ric^2, R, C^2, E_4 and (optionally) the Lanczos tensor -- all from the definition.

    Every index is carried DOWN and raised only through the inverse metric, explicitly.  The first
    version of the Lanczos block here raised one index of one factor and not of the other, giving a
    tensor that failed at eps = 0 where de Sitter forces it to vanish; the control below is what
    caught it, and it is kept for that reason.
    """
    gi, Rm = _riemann(g, xs, simp)
    Rl = [[[[simp(sum(g[a, e] * Rm[e][b][c][d] for e in range(N)))
             for d in range(N)] for c in range(N)] for b in range(N)] for a in range(N)]
    Ric = sp.Matrix(N, N, lambda b, d: simp(sum(Rm[a][b][a][d] for a in range(N))))
    Rs = simp(sum(gi[b, d] * Ric[b, d] for b in range(N) for d in range(N)))

    def up4(T):
        return [[[[simp(sum(gi[a, p] * gi[b, q] * gi[c, r] * gi[d, s] * T[p][q][r][s]
                            for p in range(N) for q in range(N)
                            for r in range(N) for s in range(N)))
                   for d in range(N)] for c in range(N)] for b in range(N)] for a in range(N)]

    Ru = up4(Rl)
    Riem2 = simp(sum(Rl[a][b][c][d] * Ru[a][b][c][d]
                     for a in range(N) for b in range(N) for c in range(N) for d in range(N)))
    Ricu = sp.Matrix(N, N, lambda a, b: simp(sum(gi[a, c] * gi[b, d] * Ric[c, d]
                                                 for c in range(N) for d in range(N))))
    Ric2 = simp(sum(Ric[a, b] * Ricu[a, b] for a in range(N) for b in range(N)))
    Cl = [[[[simp(Rl[a][b][c][d]
                  - (g[a, c] * Ric[b, d] - g[a, d] * Ric[b, c]
                     - g[b, c] * Ric[a, d] + g[b, d] * Ric[a, c]) / (N - 2)
                  + Rs * (g[a, c] * g[b, d] - g[a, d] * g[b, c]) / ((N - 1) * (N - 2)))
             for d in range(N)] for c in range(N)] for b in range(N)] for a in range(N)]
    Cu = up4(Cl)
    C2 = simp(sum(Cl[a][b][c][d] * Cu[a][b][c][d]
                  for a in range(N) for b in range(N) for c in range(N) for d in range(N)))
    E4 = simp(Riem2 - 4 * Ric2 + Rs**2)
    out = dict(g=g, Ric=Ric, Rs=Rs, Riem2=Riem2, Ric2=Ric2, C2=C2, E4=E4)
    if want_lanczos:
        rng = range(N)
        H = sp.zeros(N, N)
        for a in rng:
            for b in rng:
                t1 = Rs * Ric[a, b]
                t2 = -2 * sum(Rl[a][c][b][d] * Ricu[c, d] for c in rng for d in rng)
                t3 = -2 * sum(Ric[a, c] * gi[c, d] * Ric[d, b] for c in rng for d in rng)
                t4 = sum(Rl[a][c][d][e] * gi[c, cp] * gi[d, dp] * gi[e, ep] * Rl[b][cp][dp][ep]
                         for c in rng for d in rng for e in rng
                         for cp in rng for dp in rng for ep in rng)
                H[a, b] = simp(2 * (t1 + t2 + t3 + t4) - g[a, b] * E4 / 2)
        out['H'] = H
    return out


# =============================================================================================
head("PART 1 (C1) -- THE FOUR-DIMENSIONAL IDENTITY, ON TWO CLOSED-FORM FAMILIES")

t, r, th, ph = sp.symbols('t r theta phi', real=True)
chi = sp.symbols('chi', positive=True)
a_t = sp.Function('a')(t)
g_flrw = sp.diag(-1, a_t**2, a_t**2 * sp.sin(chi)**2,
                 a_t**2 * sp.sin(chi)**2 * sp.sin(th)**2)
d1 = invariants(g_flrw, [t, chi, th, ph])
print("  closed FLRW, a(t) left FREE -- the admitted background family:")
print(f"    R      = {sp.simplify(d1['Rs'])}")
print(f"    C^2    = {d1['C2']}")
print(f"    E_4    = {sp.simplify(d1['E4'])}")
check(sp.simplify(d1['C2']) == 0,
      "C^2 vanishes identically on the admitted family (conformal flatness -- r6894's calibration)")
check(sp.simplify(d1['E4']) != 0 and sp.simplify(d1['Ric2']) != 0,
      "and BOTH remainders are non-zero there, so the identity below is carrying weight")
check(sp.simplify(d1['C2'] - (d1['E4'] + 2 * (d1['Ric2'] - d1['Rs']**2 / 3))) == 0,
      "C^2 = E_4 + 2(Ric^2 - R^2/3) on closed FLRW with a(t) arbitrary")

Mv, al = sp.symbols('M alpha', positive=True)
f_sds = 1 - 2 * Mv / r - r**2 / al**2
g_sds = sp.diag(-f_sds, 1 / f_sds, r**2, r**2 * sp.sin(th)**2)
d2 = invariants(g_sds, [t, r, th, ph])
Lam = 3 / al**2
print()
print("  Schwarzschild--de Sitter -- an EXACT vacuum-Lambda space, where C^2 does NOT vanish:")
print(f"    R      = {sp.simplify(d2['Rs'])}        (= 4 Lambda, Lambda = 3/alpha^2)")
print(f"    C^2    = {sp.simplify(d2['C2'])}")
print(f"    E_4    = {sp.simplify(d2['E4'])}")
check(sp.simplify(d2['C2'] - 48 * Mv**2 / r**6) == 0, "C^2 = 48 M^2/r^6, non-vanishing")
check(sp.simplify(d2['C2'] - (d2['E4'] + 2 * (d2['Ric2'] - d2['Rs']**2 / 3))) == 0,
      "the SAME identity holds where C^2 is non-zero -- it is algebraic, not a family property")
check(sp.simplify((d2['Ric'] - Lam * g_sds).norm()) == 0,
      "R_ab = Lambda g_ab exactly: the substrate family is an Einstein space")
check(sp.simplify(d2['C2'] - (d2['E4'] - 8 * Lam**2 / 3)) == 0,
      "and there C^2 = E_4 - 8 Lambda^2/3 EXACTLY -- the remainder is a constant")
print("    ** so on a vacuum-Lambda space the Ricci remainder integrates to a pure number times")
print("       the volume: a renormalisation of the cosmological term the ledger already carries. **")

# =============================================================================================
head("PART 2 -- THE DECIDING ONE: THE LANCZOS IDENTITY, ON THE SHEAR CONFIGURATION ITSELF")

eta, zz, eps = sp.symbols('eta z varepsilon', real=True)
xs_w = [eta, sp.Symbol('x'), sp.Symbol('y'), zz]
scale = -1 / eta                                    # de Sitter, flat slicing, H = 1
prof = (sp.sin(eta) - eta * sp.cos(eta)) * sp.cos(zz)
on_shell = sp.simplify(sp.diff(prof, eta, 2) - (2 / eta) * sp.diff(prof, eta)
                       - sp.diff(prof, zz, 2))
check(on_shell == 0,
      "the profile solves the de Sitter transverse-traceless wave equation on the nose (r6894's witness)")
psi = eps * prof
g_wave = sp.diag(-scale**2, scale**2 * sp.exp(2 * psi), scale**2 * sp.exp(-2 * psi), scale**2)

# symbolic differentiation first, numbers only afterwards
gi_w, Rm_w = _riemann(g_wave, xs_w, sp.together)


def at_point(pt):
    num = lambda e: sp.N(sp.sympify(e).subs(pt), 30)
    gN = sp.Matrix(N, N, lambda a, b: num(g_wave[a, b]))
    giN = sp.Matrix(N, N, lambda a, b: num(gi_w[a, b]))
    Rmx = [[[[num(Rm_w[a][b][c][d]) for d in range(N)] for c in range(N)]
            for b in range(N)] for a in range(N)]
    Rl = [[[[sum(gN[a, e] * Rmx[e][b][c][d] for e in range(N))
             for d in range(N)] for c in range(N)] for b in range(N)] for a in range(N)]
    Ric = sp.Matrix(N, N, lambda b, d: sum(Rmx[a][b][a][d] for a in range(N)))
    Rs = sum(giN[b, d] * Ric[b, d] for b in range(N) for d in range(N))
    up = lambda T: [[[[sum(giN[a, p] * giN[b, q] * giN[c, rr] * giN[d, s] * T[p][q][rr][s]
                           for p in range(N) for q in range(N) for rr in range(N) for s in range(N))
                       for d in range(N)] for c in range(N)] for b in range(N)] for a in range(N)]
    Ru = up(Rl)
    Riem2 = sum(Rl[a][b][c][d] * Ru[a][b][c][d]
                for a in range(N) for b in range(N) for c in range(N) for d in range(N))
    Ricu = sp.Matrix(N, N, lambda a, b: sum(giN[a, c] * giN[b, d] * Ric[c, d]
                                            for c in range(N) for d in range(N)))
    Ric2 = sum(Ric[a, b] * Ricu[a, b] for a in range(N) for b in range(N))
    Cl = [[[[Rl[a][b][c][d]
             - (gN[a, c] * Ric[b, d] - gN[a, d] * Ric[b, c]
                - gN[b, c] * Ric[a, d] + gN[b, d] * Ric[a, c]) / 2
             + Rs * (gN[a, c] * gN[b, d] - gN[a, d] * gN[b, c]) / 6
             for d in range(N)] for c in range(N)] for b in range(N)] for a in range(N)]
    Cu = up(Cl)
    C2 = sum(Cl[a][b][c][d] * Cu[a][b][c][d]
             for a in range(N) for b in range(N) for c in range(N) for d in range(N))
    E4 = Riem2 - 4 * Ric2 + Rs**2
    rng = range(N)
    H = sp.zeros(N, N)
    for a in rng:
        for b in rng:
            t1 = Rs * Ric[a, b]
            t2 = -2 * sum(Rl[a][c][b][d] * Ricu[c, d] for c in rng for d in rng)
            t3 = -2 * sum(Ric[a, c] * giN[c, d] * Ric[d, b] for c in rng for d in rng)
            t4 = sum(Rl[a][c][d][e] * giN[c, cp] * giN[d, dp] * giN[e, ep_] * Rl[b][cp][dp][ep_]
                     for c in rng for d in rng for e in rng
                     for cp in rng for dp in rng for ep_ in rng)
            H[a, b] = 2 * (t1 + t2 + t3 + t4) - gN[a, b] * E4 / 2
    return dict(C2=C2, E4=E4, Ric=Ric, g=gN, H=H, Riem2=Riem2)


print("  H_ab = 2( R R_ab - 2 R_acbd R^cd - 2 R_ac R^c_b + R_a^cde R_bcde ) - g_ab E_4/2")
print("  -- the variation of int sqrt(-g) E_4.  In four dimensions it must vanish IDENTICALLY.")
print()
print(f"  {'eta':>7} {'z':>6} {'eps':>7} {'C^2':>16} {'E_4':>15} {'max|H_ab| / Riem^2':>20}")
worst = 0.0
rows = [(sp.Rational(-13, 10), sp.Rational(2, 5), sp.Rational(1, 10)),
        (sp.Rational(-27, 10), sp.Rational(11, 10), sp.Rational(1, 5)),
        (sp.Rational(-3, 5), sp.Rational(2, 1), sp.Rational(1, 20)),
        (sp.Rational(-13, 10), sp.Rational(2, 5), sp.Integer(0))]      # the CONTROL: eps = 0
c2_at_zero = None
for e0, z0, ep in rows:
    d = at_point({eta: e0, zz: z0, eps: ep})
    rel = float(abs(max(abs(d['H'][a, b]) for a in range(N) for b in range(N))) / abs(d['Riem2']))
    worst = max(worst, rel)
    if ep == 0:
        c2_at_zero = float(d['C2'])
    print(f"  {float(e0):>7.2f} {float(z0):>6.2f} {float(ep):>7.3f} "
          f"{float(d['C2']):>16.8f} {float(d['E4']):>15.8f} {rel:>20.2e}")
check(worst < 1e-24,
      f"the Lanczos identity holds on the shear configuration -- worst |H_ab|/Riem^2 = {worst:.1e}")
check(abs(c2_at_zero) < 1e-24,
      "and the CONTROL fires: at eps = 0 the metric is de Sitter and C^2 vanishes there")
print("  ** the eps = 0 row is the control that caught a wrong H_ab: an earlier version of this")
print("     block raised one index of one Riemann factor and not of the other, and returned")
print("     |H_ab|/Riem^2 ~ 0.8 on pure de Sitter, where the identity is exact.  Recorded because")
print("     the failure was silent everywhere except on the case with a known answer. **")
print()
print("  ⇒ ** THE GAUSS--BONNET HALF OF THE COUNTERTERM REACHES NO FIELD EQUATION, AT THE SAME")
print("       AMPLITUDES WHERE C^2 IS NON-VANISHING.  So a change of subtraction point moves the")
print("       dynamics only through 2(R_ab R^ab - R^2/3), which the field equations spend. **")

# =============================================================================================
head("PART 3 -- AND THE LINEARISED WITNESS IS EINSTEIN THROUGH FIRST ORDER, MEASURED NOT ASSUMED")

print(f"  {'eps':>9} {'max|R_ab - Lambda g_ab|':>26} {'divided by eps^2':>18}")
ratios = []
for ep in [sp.Rational(1, 10), sp.Rational(1, 20), sp.Rational(1, 40)]:
    d = at_point({eta: sp.Rational(-13, 10), zz: sp.Rational(2, 5), eps: ep})
    dev = float(max(abs(d['Ric'][a, b] - 3 * d['g'][a, b]) for a in range(N) for b in range(N)))
    ratios.append(dev / float(ep)**2)
    print(f"  {float(ep):>9.4f} {dev:>26.6e} {dev/float(ep)**2:>18.6f}")
check(max(ratios) / min(ratios) - 1 < 1e-6,
      "the Ricci residue scales as eps^2 EXACTLY -- Einstein through first order, and no further")
print("  ** which is why PART 2 and not PART 3 carries the verdict: the Lanczos identity is an")
print("     IDENTITY and needs no solution, while the sharp vacuum-Lambda form of the Ricci")
print("     remainder is stated on SdS, an exact solution, rather than on this linearised wave. **")

# =============================================================================================
head("VERDICT")

print("""
  ⇒ ** PO-52 CLOSES.  THE COEFFICIENT EXISTS, IS NON-VANISHING POINTWISE, AND MOVES NOTHING THE
       CONSTRUCTION COMPUTES -- BECAUSE THE DEGENERACY THAT SURVIVES SECOND ORDER IN THE SHEAR IS
       NOT CONFORMAL FLATNESS BUT THE FOUR-DIMENSIONAL GAUSS--BONNET IDENTITY. **

  r6894 established that the admitted family reaches second order in the shear and that the Weyl
  invariant is non-vanishing there.  ** That is the premise of this result and not a casualty of
  it. **  What r6894 did not ask, and what the order did ask, is whether a non-vanishing invariant
  is a moved observable.  It is not:

     * C^2 = E_4 + 2(R_ab R^ab - R^2/3) is ALGEBRAIC in four dimensions, so no order in the shear
       can break it -- checked where C^2 = 0 and where C^2 != 0;
     * the E_4 half contributes NOTHING to the field equations, checked on the shear configuration
       at the amplitudes where C^2 != 0;
     * the remainder is Ricci-squared, and the field equations trade R_ab for the stress tensor --
       on the substrate, an exact vacuum-Lambda space, for the constant -8 Lambda^2/3.

  ** So the subtraction-point change is a cosmological-term renormalisation, which is exactly what
     PO-51 concluded -- and it is now concluded from an identity rather than from a property of the
     admitted family, so the shear cannot take it away. **

  ⌗ AND THE REMAINDER IS NAMED RATHER THAN HIDDEN: int sqrt(-g) E_4 shifts the on-shell action by
    a topology-fixed constant.  ** It does so at eps = 0 as much as at eps != 0 **, so the broken
    degeneracy is not what produces it, and it is not what the row asked about.

  ⌗ WHAT THIS DOES NOT DO.  It does not touch the frontier's 1/60 (not used, not needed), does not
    reopen PO-51, does not bear on PO-48's undetermined, and does not extend off-shell -- where
    C^2 is an independent invariant and nothing here bounds it.  ** The one restriction is the
    on-shell one and it is the whole restriction. **
""".rstrip())

print()
if FAILED:
    print("FAIL: " + "; ".join(FAILED))
    sys.exit(1)
print("ALL CHECKS PASS")
sys.exit(0)
