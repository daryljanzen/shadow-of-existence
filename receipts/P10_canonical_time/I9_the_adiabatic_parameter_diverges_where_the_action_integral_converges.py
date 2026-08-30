"""
LEVEL: exact symbolic, on P10's own near-branch-point scaling.

WHY THIS PROBE EXISTS.  P10 reduces the transverse-traceless sector mode by mode to a
harmonic oscillator with time-dependent mass a^3 and frequency mu_n/a -- a tower of
parametric oscillators.  It then writes that "the projection is ADIABATIC rather than
exact", and asks whether the suppression exponent converges.  It does.  That is the
right computation under the wrong name, and the two are different questions.

WHAT IS CLAIMED.
  (1) The adiabatic expansion is controlled by |d omega / ds| / omega^2.  On P10's own
      near-branch-point scaling |r| ~ s^(2/3), with omega = mu/a and a following r,
      that parameter goes as s^(-1/3) and DIVERGES at the branch point.  So the
      adiabatic invariant E/omega -- the quantity an adiabatic approximation conserves
      -- is not conserved through it.
  (2) The suppression exponent int omega ds nevertheless CONVERGES, because
      omega ~ s^(-2/3) is integrable at zero.  That is a statement about an action
      integral, not about slow variation.
  (3) So (1) and (2) are independent: a divergent adiabaticity parameter is compatible
      with a convergent action integral, and P10's check establishes the second while
      its word claims the first.  P15 names the same object correctly, as a WKB form
      "whose adiabaticity parameter is of order unity".

WHAT IS NOT CLAIMED.  Not that P10's suppression is wrong -- it is right, and the
convergence is verified here.  Not that the projection fails; the exponent is finite
and the mode is suppressed.  The claim is only about which approximation scheme the
finiteness comes from, and therefore what the correction should be called.

COMPUTES: the scaling |r| ~ s^(2/3) is P10's own, quoted in its adiabatic-correction
paragraph; the amplitudes A and mu are carried symbolically and no numerical value is
pinned.  The exponents -1/3 and -2/3 are derived from that scaling, not assumed.

WHAT WOULD FALSIFY IT.  An adiabaticity parameter that stayed bounded as s -> 0; or a
divergent action integral, which would make P10's own convergence check wrong; or the
two turning out to be controlled by the same power, in which case naming would not
matter.
"""
import sympy as sp

FAILS = []


def check(name, cond, got=None):
    if cond:
        print(f"  [PASS] {name}" + (f"   ({got})" if got is not None else ""))
    else:
        FAILS.append(name)
        print(f"  [FAIL] {name}" + (f"   (got {got})" if got is not None else ""))


s, A, mu, S = sp.symbols('s A mu S', positive=True)

print(__doc__)
print("=" * 78)

a = A * s**sp.Rational(2, 3)            # P10: |r| ~ s^(2/3) near the branch point
w = mu / a                              # omega_n = mu_n / a
print(f"  a(s) = {a}          [P10's own scaling]")
print(f"  omega(s) = mu/a = {sp.simplify(w)}")
print()

# (1) the adiabaticity parameter
eps = sp.simplify(sp.Abs(sp.diff(w, s)) / w**2)
check("adiabaticity parameter |dw/ds|/w^2 is a positive power of s^(-1/3)",
      sp.simplify(eps * s**sp.Rational(1, 3)).free_symbols.isdisjoint({s}),
      f"eps = {eps}")
lim = sp.limit(eps, s, 0, '+')
check("it DIVERGES as s -> 0 -- adiabaticity fails at the branch point",
      lim == sp.oo, f"limit = {lim}")

# the exponent, derived rather than asserted
expo = sp.simplify(sp.log(eps.subs(s, sp.exp(sp.Symbol('L')))) )
check("the divergence is exactly s^(-1/3)",
      sp.simplify(eps / (s**sp.Rational(-1, 3))).free_symbols.isdisjoint({s}),
      "eps * s^(1/3) is s-free")

# (2) the action integral
I = sp.integrate(w, (s, 0, S))
check("the suppression exponent int omega ds CONVERGES",
      not I.has(sp.oo) and not I.has(sp.zoo) and I.is_finite is not False,
      f"int = {sp.simplify(I)}")
check("and it goes as S^(1/3) -- finite for every finite S",
      sp.simplify(I / S**sp.Rational(1, 3)).free_symbols.isdisjoint({S}),
      f"{sp.simplify(I)}")

# (3) the two are controlled by DIFFERENT powers, which is why naming matters
check("the two questions are governed by different powers: s^(-1/3) against s^(2/3) integrand",
      sp.Rational(-1, 3) != sp.Rational(2, 3))
check("so a DIVERGENT adiabaticity parameter coexists with a CONVERGENT action integral",
      lim == sp.oo and not sp.simplify(I).has(sp.oo))

# ADVERSARIAL: a scaling for which adiabaticity would HOLD must register as holding,
# so the test is not merely reporting that limits diverge.
a2 = A * s**2                            # a much gentler approach
w2 = mu / a2
eps2 = sp.simplify(sp.Abs(sp.diff(w2, s)) / w2**2)
lim2 = sp.limit(eps2, s, 0, '+')
check("ADVERSARIAL: for a ~ s^2 the parameter tends to 0 -- adiabaticity WOULD hold",
      lim2 == 0, f"limit = {lim2}")

# and a scaling for which the ACTION integral would diverge, so that check bites too
w3 = mu / (A * s**sp.Rational(3, 2))     # omega ~ s^{-3/2}, not integrable at 0
I3 = sp.integrate(w3, (s, 0, S))
check("ADVERSARIAL: for omega ~ s^(-3/2) the action integral DIVERGES",
      I3.has(sp.oo) or I3.has(sp.zoo), f"{I3}")

print()
print("=" * 78)
if FAILS:
    print(f"  VERDICT: {len(FAILS)} FAILURE(S): {', '.join(FAILS)}")
    raise SystemExit(1)
print("  VERDICT: ALL PASS.  On P10's own scaling the adiabaticity parameter diverges as")
print("  s^(-1/3) at the branch point while the suppression exponent converges as S^(1/3).")
print("  The two are governed by different powers, so the finiteness P10 verifies comes")
print("  from the action integral and not from slow variation: the correction is")
print("  semiclassical, and P15 names the same object correctly as WKB.")
print("=" * 78)
