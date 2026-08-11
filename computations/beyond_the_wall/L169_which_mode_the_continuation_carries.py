#!/usr/bin/env python3
"""
`L-169`.  ** WHICH MODE DOES THE ANALYTIC CONTINUATION CARRY? **  The falsifier on c54.122.

c54.122 showed the collapse leg is a matter-dominated contraction, hence scale-invariant.  In the
contraction literature that result is shadowed by one difficulty: the scale-invariant spectrum sits
in the mode that DOMINATES during contraction, and whether that is the mode that SURVIVES depends on
the matching.  ** Here the matching is not a junction condition between two real branches.  It is an
ANALYTIC CONTINUATION through a branch point, and that makes the question sharper and different. **

  PART 1  ** THE TWO MODES, AND WHICH SURVIVES ON EACH SIDE. **
  PART 2  ** THEIR SPECTRA FROM VACUUM DATA: the dominant one is flat, the surviving one is BLUE. **
  PART 3  ** THE CONTINUATION: in the corpus's own variable the conformal time rotates by
          $\\pi/3$, not $\\pi$ — and a rotation cannot mix two powers.  Is there a LOG? **
  PART 4  ** THE VERDICT, AND IT IS A NEGATIVE. **

Run: python3 L169_which_mode_the_continuation_carries.py      (sympy, numpy, scipy)
"""
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

print(__doc__.split("Run:")[0])

# =====================================================================
print("=" * 78)
print("PART 1 — THE TWO MODES")
print("=" * 78)
eta = sp.symbols('eta')
s = sp.symbols('s')
ind = sp.solve(sp.Eq(s * (s - 1), 2), s)
print("  Near the branch point a ∝ eta^2, so the mode equation is v'' - (2/eta^2) v = 0.")
print(f"  Indicial equation s(s-1) = 2  ⇒  s = {sorted(ind)}   -- two POWERS, no log at this order.")
assert sorted(ind) == [-1, 2]
print()
print(f"  {'v behaves as':>16} {'zeta = v/a ∝':>16} {'on CONTRACTION (eta->0-)':>26} {'on EXPANSION':>18}")
for a, b, c, d in [("eta^-1", "eta^-3", "DOMINANT (diverges)", "decaying"),
                   ("eta^2", "constant", "subdominant", "SURVIVES")]:
    print(f"  {a:>16} {b:>16} {c:>26} {d:>18}")
print()
for x in [
 "⌗ ** THE ASYMMETRY IS THE WHOLE PROBLEM: the mode that dominates the contraction is the mode that",
 "   DECAYS on expansion, and the mode that survives expansion is the one that was subdominant. **",
]:
    print("  " + x)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THEIR SPECTRA FROM VACUUM DATA")
print("=" * 78)
print("  The exact solution with vacuum data v = e^{-ik eta}/sqrt(2k) on a ∝ eta^2 is")
print("     v = (1 - i/(k eta)) e^{-ik eta} / sqrt(2k) ,")
print("  and its expansion about eta = 0 gives the two coefficients directly:")
k = sp.symbols('k', positive=True)
v_exact = (1 - sp.I / (k * eta)) * sp.exp(-sp.I * k * eta) / sp.sqrt(2 * k)
ser = sp.series(v_exact, eta, 0, 3).removeO().expand()
cm = sp.simplify(ser.coeff(eta, -1))
cp = sp.simplify(ser.coeff(eta, 2))
print(f"     coefficient of eta^-1 :  c- = {cm}      |c-| ∝ k^(-3/2)")
print(f"     coefficient of eta^2  :  c+ = {cp}      |c+| ∝ k^(+3/2)")
pm = sp.simplify(sp.log(sp.Abs(cm)).diff(k) * k)
pp = sp.simplify(sp.log(sp.Abs(cp)).diff(k) * k)
print(f"     d ln|c-| / d ln k = {pm}      d ln|c+| / d ln k = {pp}")
assert sp.simplify(pm + sp.Rational(3, 2)) == 0
assert sp.simplify(pp - sp.Rational(3, 2)) == 0
print()
print(f"  P_zeta = k^3 |zeta|^2, and zeta = c- eta^-3 or zeta = c+ :")
print(f"  {'mode':>26} {'P(k) ∝':>10} {'n_s - 1':>10} {'':>6}")
for nm, pw, ns in [("dominant  (scale-invariant)", "k^0", 0), ("constant  (the survivor)", "k^6", 6)]:
    print(f"  {nm:>26} {pw:>10} {ns:>10}")
print()
for x in [
 "⇒⇒ ** SO THE TWO MODES CARRY OPPOSITE SPECTRA, AND THE SURVIVOR IS VIOLENTLY BLUE. **  *If the",
 "   continuation carries only the constant mode, the observable spectrum is $n_s-1=6$ and the",
 "   construction is dead on the sky.  **This is not a small correction to c54.122; it decides",
 "   whether c54.122 says anything about the observed universe at all.***",
]:
    print("  " + x)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE CONTINUATION")
print("=" * 78)
print("  In the corpus's own time variable the branch point sits at tau = 0 with r ∝ tau^(2/3),")
print("  so the conformal time is eta ∝ tau^(1/3).  Going from the contracting leg (tau < 0) to the")
print("  expanding leg (tau > 0) through the upper half plane is tau: |tau|e^{i pi} -> |tau|e^{i 0},")
print("  and therefore")
print("     ** eta rotates by pi/3, NOT by pi.  The corpus's cube root is acting here. **")
print()
print("  A rotation acts DIAGONALLY on two power solutions -- it multiplies eta^2 and eta^-1 by")
print("  phases and cannot mix them.  Mixing requires a LOGARITHM, and a log can appear precisely")
print("  because the exponents differ by an INTEGER (2 - (-1) = 3, a resonance).  So the question")
print("  is whether the exact background produces one.")
print()
u = sp.symbols('u', positive=True)
# exact a(tau) ∝ sinh^(2/3)(u), u ∝ tau: get a''/a in eta to the resonant order
a_ser = sp.series(sp.sinh(u)**sp.Rational(2, 3), u, 0, 6).removeO()
corr = sp.simplify(sp.expand(a_ser / u**sp.Rational(2, 3)))
print(f"  a(tau) ∝ tau^(2/3) * [{corr}]   -- the correction is EVEN in u and starts at u^2")
c_u2 = sp.simplify(corr.coeff(u, 2))
c_u4 = sp.simplify(corr.coeff(u, 4))
print(f"     u^2 coefficient = {c_u2} ,  u^4 coefficient = {c_u4}")
assert c_u2 == sp.Rational(1, 9)
print()
print("  In eta the correction enters at eta^6 (since u ∝ tau ∝ eta^3), so the potential is")
print("     a''/a = 2/eta^2 * [1 + O(eta^6)] ,")
print("  and the Frobenius recursion about eta = 0 steps in SIXES from each root while the")
print("  resonance sits at a step of THREE.")
print()
# demonstrate: the recursion for v = sum a_n eta^(s+6n) never reaches s = 2 from s = -1
steps = [(-1) + 6 * n for n in range(4)]
print(f"     from the root s = -1 the series visits exponents {steps}")
print(f"     the other root is s = 2 :  reachable?  ** {2 in steps} **")
assert 2 not in steps
print()
for x in [
 "⇒⇒ ** NO LOGARITHM, AND THE REASON IS THE PARITY OF THE BACKGROUND: the $\\sinh^{2/3}$ correction",
 "   is EVEN in $\\tau$, so in conformal time it enters at $\\eta^{6}$ and the Frobenius series steps",
 "   in sixes.  The resonance is at a step of three, and a series stepping in sixes never lands on",
 "   an odd step. **  *The two solutions stay pure powers, and the continuation stays diagonal.*",
]:
    print("  " + x)

# --- the diagonality TESTED, not asserted -------------------------------------------------
# ** A FIRST VERSION OF THIS BLOCK WAS DECORATION AND IS RECORDED AS SUCH: it started from
# (v, v') = (1,0) and (0,1) -- which are NOT the two pure modes -- continued them, and reported
# that the connection determinant was nonzero.  A nonzero determinant says the map is INVERTIBLE,
# which every connection map is.  It does not say the map is DIAGONAL, which is the entire claim.
# ** A check that cannot fail is not a check. **  What follows starts from the ASYMPTOTIC pure
# modes and measures the OFF-DIAGONAL entries, which is the thing in question.
print()
print("  THE DIAGONALITY, MEASURED.  Near the branch point the two solutions are v ∝ tau^(2/3)")
print("  (the constant-zeta mode) and v ∝ tau^(-1/3) (the dominant one).  Start from each as pure")
print("  asymptotic data on the contracting side at tau = delta e^{i pi}, continue the semicircle")
print("  to tau = delta, and project onto the same basis there.")
A_ = 1.0
KK = 1.0


def a_exact(tau):
    # ** THE BRANCH MATTERS AND A FIRST VERSION GOT IT WRONG.  Writing a = (sinh^2)^(1/3) squares
    # FIRST, which throws away the phase: on the contracting side sinh(1.5 tau) is negative real,
    # its square is positive real, and the principal cube root returns a REAL a -- when the correct
    # continuation carries e^{2 pi i/3}.  (z^2)^(1/3) is not z^(2/3).  The test below rose instead
    # of falling until this was fixed, which is the test doing its job on the code. **
    return A_ * np.power(np.sinh(1.5 * tau), 2.0 / 3.0)


def coeffs(tau, v, vp):
    """decompose (v, v') in the basis {tau^(2/3), tau^(-1/3)} at the point tau"""
    b1, b1p = tau ** (2 / 3), (2 / 3) * tau ** (-1 / 3)
    b2, b2p = tau ** (-1 / 3), (-1 / 3) * tau ** (-4 / 3)
    det = b1 * b2p - b2 * b1p
    return ((v * b2p - vp * b2) / det, (vp * b1 - v * b1p) / det)


def continue_mode(which, delta):
    th0 = np.pi - 1e-9      # start just inside the principal branch cut
    tau0 = delta * np.exp(1j * th0)
    if which == 1:
        v0, vp0 = tau0 ** (2 / 3), (2 / 3) * tau0 ** (-1 / 3)
    else:
        v0, vp0 = tau0 ** (-1 / 3), (-1 / 3) * tau0 ** (-4 / 3)

    def rhs(th, y):
        # ** ANALYTIC derivatives, not finite differences: a finite difference of a branched power
        # near its branch point is dominated by the branch, not by the derivative. **
        tau = delta * np.exp(1j * th)
        dtau = 1j * tau
        b = 1.5
        S, C = np.sinh(b * tau), np.cosh(b * tau)
        a0 = A_ * np.power(S, 2.0 / 3.0)
        a1 = A_ * (2.0 / 3.0) * b * np.power(S, -1.0 / 3.0) * C
        a2 = A_ * b * b * ((2.0 / 3.0) * np.power(S, 2.0 / 3.0)
                           - (2.0 / 9.0) * np.power(S, -4.0 / 3.0) * C * C)
        v, vp = y
        vpp = -(a0 * a1 * vp + (KK ** 2 - a0 * a2 - a1 ** 2) * v) / a0 ** 2
        return [vp * dtau, vpp * dtau]

    sol = solve_ivp(rhs, [th0, 0.0], [v0, vp0], rtol=1e-11, atol=1e-14)
    return coeffs(delta + 0j, sol.y[0, -1], sol.y[1, -1])


print()
print("  ** delta must be small enough that the mode is FROZEN there: eta ~ 3 tau^(1/3)/A, so")
print("     k eta << 1 needs tau << (A/3k)^3.  A first run used delta ~ 0.1, where k eta ~ 1.4 --")
print("     the k^2 term fully active and mixing the modes by ORDINARY EVOLUTION rather than by the")
print("     connection.  That is not a refutation of diagonality; it is a test run outside its own")
print("     hypothesis. **")
print()
print("  ** AND THE DIAGNOSTIC MUST BE BASIS-AWARE, which a second run got wrong: the two basis")
print("     functions scale oppositely (tau^(2/3) vanishes, tau^(-1/3) diverges), so the COEFFICIENT")
print("     ratio c1/c2 grows even when the physical admixture goes to zero.  The leakage is the")
print("     contribution to v ITSELF: eps = (c1 tau^(2/3)) / (c2 tau^(-1/3)) = (c1/c2) * delta. **")
print()
print(f"  {'delta':>10} {'k eta':>9} {'mode2->mode2':>14} {'c1/c2':>11} "
      f"{'LEAKAGE eps':>13} {'eps ratio':>10}")
prev = None
for delta in [1e-3, 1e-4, 1e-5, 1e-6]:
    c1, c2 = continue_mode(2, delta)
    keta = KK * 3.0 * delta ** (1.0 / 3.0) / A_
    ratio = abs(c1) / abs(c2)
    eps = ratio * delta
    rr = (eps / prev) if prev else float('nan')
    print(f"  {delta:>10.0e} {keta:>9.4f} {abs(c2):>14.6f} {ratio:>11.4g} "
          f"{eps:>13.4e} {rr:>10.4f}")
    if prev is not None:
        assert eps < prev, (delta, eps, prev)
        # a clean power law and NOT a logarithm: each decade multiplies eps by 10^(-2/3)
        assert abs(rr - 10 ** (-2 / 3)) < 0.02, (delta, rr)
    prev = eps
assert abs(abs(c2) - 1.0) < 1e-2, abs(c2)
print()
print("  ** THE LEAKAGE FALLS AS delta^(2/3), A CLEAN POWER LAW, WHILE THE DIAGONAL ENTRY GOES TO")
print("     EXACTLY 1. **  The admixture is a finite-delta effect of the k^2 term, not a connection")
print("     coefficient -- and the power law is itself the evidence AGAINST a logarithm, since a")
print("     log would leave a residual that no power of delta removes.")
print("     ⇒ ** the continuation is DIAGONAL in the limit, exactly as the Frobenius parity")
print("       argument requires, and the two arguments are independent. **")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE VERDICT")
print("=" * 78)
for x in [
 "⛔⛔ ** THE FALSIFIER FIRES.  The continuation is DIAGONAL on the two modes, so the",
 "   scale-invariant spectrum stays in the mode that decays on the expanding side, and the mode",
 "   that survives carries $n_s-1=6$. **",
 "",
 "⇒ ** SO c54.122's RESULT IS CONFINED TO THE CONTRACTING SIDE AS IT STANDS, and P15 must say so. **",
 "   *What was shown there is true and remains true: the leg is the second root of",
 "   $\\beta(\\beta-1)=2$ and freezes a scale-invariant spectrum.  **What is NOT shown, and what this",
 "   revision removes, is that the spectrum reaches the observer.***",
 "",
 "⌗⌗ ** AND THE REASON IS WORTH MORE THAN THE VERDICT, because it is a fact about THIS geometry and",
 "   not an imported caveat: the $\\sinh^{2/3}$ correction is EVEN in $\\tau$. **  *So in conformal",
 "   time it enters at $\\eta^{6}$, the Frobenius series steps in sixes, the resonance at step three",
 "   is never reached, no logarithm is generated, and the two solutions stay pure powers through the",
 "   continuation.  **The evenness of the background is what forbids the mixing.***",
 "",
 "✔ ** WHAT SURVIVES, AND IT IS NOT NOTHING: the corpus's claim that it has no scale-invariant",
 "   ATTRACTOR was wrong as stated and is now right for a better reason. **  *It has a",
 "   scale-invariant background; the spectrum that background freezes does not reach the observer;",
 "   and the obstruction is a parity property of its own solution rather than a missing mechanism.*",
 "",
 "⚑ ** AND THE ROUTE THAT REMAINS IS NAMED, NOT LEFT VAGUE: mixing needs a background correction",
 "   ODD in $\\tau$. **  *The corpus has exactly one candidate — the $\\mathbb{Z}_3$ monodromy sends",
 "   $\\tau$ around zero rather than through it, and an odd-order term is what a genuinely",
 "   three-sheeted continuation could supply that a two-sided matching cannot.  **That is the next",
 "   question and it is sharp: is there a determination of the continuation under which the",
 "   correction acquires an odd part?***",
]:
    print("  " + x)
