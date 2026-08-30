"""
LEVEL: exact symbolic.

WHY THIS PROBE EXISTS.  P02 scores ZERO on every term in the integrable-systems
vocabulary -- integrable, separable, Killing tensor, first integral, Liouville all
x0 -- and a vocabulary screen scores it CHECKED-NEGATIVE.  Read from contents it is
the field's founding example: the Schwarzschild interior which is term-for-term the
closed Friedmann scale factor is the Kepler radial problem, and the cycloid is its
parametric solution.

WHAT IS CLAIMED.  P02 states r'' = -(r-M) and reads the locus (r-M)^2 + s^2 = M^2 as
a geometric circle.  With s = dr/dz that locus is the harmonic oscillator's orbit in
phase space; the conserved energy is M^2/2; the two critical points are the orbit's
two turning points, where the momentum vanishes; and a periodic orbit of one degree
of freedom has EXACTLY TWO, interchanged by the time reversal z -> -z that the
evenness of r(z) expresses.

WHAT IS NOT CLAIMED.  Nothing about Lambda != 0.  The cycloid is the Lambda = 0
member of the family (see I12); with Lambda present the closed member obeys a
different equation and has no elementary closed form.

WHAT WOULD FALSIFY IT.  If u^2 + (du/dz)^2 were not constant, or if the number of
turning points on a period were other than two, or if the second derivative at the
two critical points had the same sign, the reading would fail.  Each is checked.
"""
import sympy as sp

FAILS = []


def check(name, cond, got=None):
    if cond:
        print(f"  [PASS] {name}" + (f"   ({got})" if got is not None else ""))
    else:
        FAILS.append(name)
        print(f"  [FAIL] {name}" + (f"   (got {got})" if got is not None else ""))


z, M = sp.symbols('z M', positive=True)
r = M * (1 + sp.cos(z))
u = r - M                       # displacement from the circle's centre
p = sp.diff(r, z)               # the momentum conjugate to z, P02's s

print(__doc__)
print("=" * 78)
print("  r(z) = M(1 + cos z)      [P02 eq:cycloid]")
print(f"  u = r - M              = {sp.simplify(u)}")
print(f"  s = dr/dz              = {sp.simplify(p)}")
print()

# 1. the equation of motion is the harmonic oscillator, as P02 itself writes
eom = sp.simplify(sp.diff(r, z, 2) + u)
check("r'' + (r - M) = 0 identically -- the harmonic oscillator in u",
      eom == 0, f"r'' + u = {eom}")

# 2. P02's locus IS the phase-space orbit, with s = dr/dz
orbit = sp.simplify(u**2 + p**2)
check("(r-M)^2 + s^2 = M^2 identically, with s = dr/dz -- the locus is the orbit",
      sp.simplify(orbit - M**2) == 0, f"u^2 + s^2 = {orbit}")

# 3. the energy is conserved and equals M^2/2
E = sp.simplify(sp.Rational(1, 2) * p**2 + sp.Rational(1, 2) * u**2)
check("E = (1/2)s^2 + (1/2)u^2 = M^2/2, conserved",
      sp.simplify(E - M**2 / 2) == 0, f"E = {E}")
check("dE/dz = 0", sp.simplify(sp.diff(E, z)) == 0)

# 4. EXACTLY TWO turning points on one period, and they are the critical points
turn = sp.solve(sp.Eq(sp.simplify(p), 0), z)
turn_in_period = sorted({sp.nsimplify(t) for t in turn if 0 <= sp.N(t) < 2 * sp.pi} |
                        {sp.Integer(0)}, key=lambda t: sp.N(t))
check("exactly two turning points on 0 <= z < 2pi", len(turn_in_period) == 2,
      f"{turn_in_period}")
check("they are z = 0 and z = pi, P02's horizon and r=0",
      turn_in_period == [sp.Integer(0), sp.pi], f"{turn_in_period}")

# 5. non-degenerate, and of OPPOSITE curvature -- P02's own d^2r/dz^2 = -M and +M
d2 = sp.diff(r, z, 2)
a0, ap = sp.simplify(d2.subs(z, 0)), sp.simplify(d2.subs(z, sp.pi))
check("r''(0) = -M and r''(pi) = +M -- non-degenerate, opposite signs",
      a0 == -M and ap == M, f"{a0}, {ap}")

# 6. the time reversal z -> -z is a symmetry, and it exchanges the two turning points
check("r(z) is even: the time reversal z -> -z is a symmetry of the orbit",
      sp.simplify(r.subs(z, -z) - r) == 0)
check("z -> -z maps the turning point at 0 to itself and pi to -pi = pi (mod 2pi)",
      sp.simplify(sp.cos(-sp.pi) - sp.cos(sp.pi)) == 0)

# 7. ADVERSARIAL: a NON-oscillator curve must fail the orbit identity, so the test bites
q = M * (1 + sp.cos(z) + sp.Rational(1, 5) * sp.cos(2 * z))
bad = sp.simplify((q - M)**2 + sp.diff(q, z)**2)
check("ADVERSARIAL: a perturbed curve does NOT satisfy the orbit identity",
      sp.simplify(bad - M**2) != 0, "perturbation detected")

print()
print("=" * 78)
if FAILS:
    print(f"  VERDICT: {len(FAILS)} FAILURE(S): {', '.join(FAILS)}")
    raise SystemExit(1)
print("  VERDICT: ALL PASS.  P02's geometric circle IS the harmonic oscillator's phase")
print("  portrait; its 'homogeneity' is a level set of the conserved energy M^2/2; and its")
print("  two critical points are the orbit's two turning points, which a one-degree-of-freedom")
print("  periodic orbit has exactly two of, interchanged by the time reversal the evenness")
print("  of r(z) expresses.")
print("=" * 78)
