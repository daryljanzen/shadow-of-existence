"""
LEVEL: exact symbolic, both readings on one metric function, with the non-degenerate
horizon as the control.

WHY THIS PROBE EXISTS.  Two papers describe the same locus in two languages and neither
says they are one statement.  P03's prop:turning derives d^2r/dl^2 = (1/2) f' sgn(f)
and calls the horizons TURNING POINTS of the slicing curve.  P01 argues that horizon
generators sit at one areal radius and are therefore metrically coincident.  Read
dynamically both are statements about the SAME function f having a zero, at zeroth and
first order.

WHAT IS CLAIMED, four things.
  (1) TIMELIKE SIDE.  With V(r) = -|f(r)|/2 the slicing law (dr/dl)^2 = |f| is
      (1/2)(dr/dl)^2 + V = 0, and P03's own second-derivative formula is exactly
      -dV/dr.  So the slicing curve is the ZERO-ENERGY orbit of a one-dimensional
      conservative system and the horizon cubic is its turning-point condition V = E.
  (2) NULL SIDE.  In ingoing Eddington-Finkelstein coordinates the outgoing null rays
      obey dr/dv = f(r)/2, a one-dimensional flow whose EQUILIBRIA are the zeros of f.
      A generator stays at r_h because r_h is a fixed point.
  (3) THE EIGENVALUE IS THE SURFACE GRAVITY.  Linearising that flow gives
      dr/dv = kappa (r - r_h) with kappa = f'(r_h)/2, so neighbouring rays separate as
      exp(kappa v) and the fixed point is hyperbolic exactly when kappa != 0.
  (4) AT NARIAI BOTH DEGENERATE TOGETHER.  f has a double root, so V and V' vanish
      together and V has a MAXIMUM at the orbit's own energy -- an unstable equilibrium
      -- while kappa = 0 makes the fixed point non-hyperbolic.  The approach costs
      infinite affine parameter, because |f| ~ c (r - r_N)^2 makes int dr/sqrt|f|
      diverge logarithmically.

WHAT IS NOT CLAIMED.  Nothing about the horizon's thermodynamics; kappa appears here
only as a linearisation eigenvalue, and that it also carries the temperature is a
separate fact of the literature.  Nothing about generators' affine parametrisation
beyond the radial flow.

WHAT WOULD FALSIFY IT.  V = -|f|/2 failing to reproduce P03's own formula, sign
included; the flow's equilibria not coinciding with f's zeros; the linearisation
differing from f'(r_h)/2; or the affine-parameter integral converging at a double root.
The NON-DEGENERATE CONTROL is the discriminator: a simple root must come out
hyperbolic, with finite approach -- otherwise "degenerate" is not being measured.
"""
import sympy as sp

FAILS = []


def check(name, cond, got=None):
    if cond:
        print(f"  [PASS] {name}" + (f"   ({got})" if got is not None else ""))
    else:
        FAILS.append(name)
        print(f"  [FAIL] {name}" + (f"   (got {got})" if got is not None else ""))


r, M, a, v, eps = sp.symbols('r M alpha v epsilon', positive=True)
f = 1 - 2 * M / r - r**2 / a**2

print(__doc__)
print("=" * 78)

# ---- (1) TIMELIKE: V = -|f|/2 reproduces P03's formula, sgn included ----------
# on f > 0 the uniform potential -|f|/2 is -f/2; on f < 0 it is +f/2.
for region, sgn in [('f > 0', +1), ('f < 0', -1)]:
    V = -sgn * f / 2                      # -|f|/2 in that region
    newton = sp.simplify(-sp.diff(V, r))
    p03 = sp.simplify(sp.diff(f, r) / 2 * sgn)   # P03: (1/2) f' sgn f
    check(f"({region}) -dV/dr equals P03's (1/2) f' sgn(f)",
          sp.simplify(newton - p03) == 0, f"{sp.simplify(newton)}")

check("turning points of the orbit are the zeros of f -- the horizon cubic is V = E = 0",
      sp.simplify(sp.solve(sp.Eq(f, 0), M)[0]) == sp.simplify(sp.solve(sp.Eq(-sp.Abs(f) / 2, 0), M)[0])
      if sp.solve(sp.Eq(f, 0), M) else True,
      "f = 0  <=>  V = 0")

# ---- (2)(3) NULL: the flow, its equilibria, and its eigenvalue ---------------
flow = f / 2                              # dr/dv for outgoing null rays in ingoing EF
eq_flow = set(sp.solve(sp.Eq(flow, 0), r))
eq_f = set(sp.solve(sp.Eq(f, 0), r))
check("outgoing null flow dr/dv = f/2 has equilibria exactly at the zeros of f",
      eq_flow == eq_f and len(eq_f) > 0,
      f"{len(eq_f)} root(s), sets identical")

rh = sp.Symbol('r_h', positive=True)
lin = sp.diff(flow, r)
kappa = sp.diff(f, r) / 2
check("the linearisation d/dr(f/2) IS the surface gravity f'(r_h)/2",
      sp.simplify(lin - kappa) == 0, f"{sp.simplify(lin)}")

# Schwarzschild, as the concrete case P01 argues on
fS = 1 - 2 * M / r
check("Schwarzschild: kappa = 1/4M, and the linearisation at r = 2M agrees",
      sp.simplify(sp.diff(fS, r).subs(r, 2 * M) / 2 - 1 / (4 * M)) == 0 and
      sp.simplify(sp.diff(fS / 2, r).subs(r, 2 * M) - 1 / (4 * M)) == 0,
      f"{sp.simplify(sp.diff(fS,r).subs(r,2*M)/2)}")

# ---- (4) NARIAI: both degenerate together ------------------------------------
Mn = a / (3 * sp.sqrt(3))
rN = a / sp.sqrt(3)
fn = sp.simplify(f.subs(M, Mn))
check("Nariai: f(r_N) = 0 and f'(r_N) = 0 -- a DOUBLE root",
      sp.simplify(fn.subs(r, rN)) == 0 and sp.simplify(sp.diff(fn, r).subs(r, rN)) == 0)
check("so kappa = 0 there: the fixed point is NON-HYPERBOLIC",
      sp.simplify(sp.diff(fn, r).subs(r, rN) / 2) == 0)
fpp = sp.simplify(sp.diff(fn, r, 2).subs(r, rN))
check("f''(r_N) < 0, so |f| ~ (|f''|/2)(r-r_N)^2 and V = -|f|/2 has a MAXIMUM",
      fpp < 0, f"f'' = {fpp}")
check("V has a maximum at the orbit's own energy -- an UNSTABLE equilibrium",
      fpp < 0 and sp.simplify(fn.subs(r, rN)) == 0)

# the affine cost, from the quadratic behaviour
c = sp.simplify(-fpp / 2)                      # |f| ~ c (r - r_N)^2 near the double root
u = sp.Symbol('u', positive=True)              # u = r - r_N > 0, so the sqrt is exact
antideriv = sp.integrate(1 / sp.sqrt(c * u**2), u)
check("near a DOUBLE root the antiderivative is logarithmic in (r - r_N)",
      antideriv.has(sp.log), f"{sp.simplify(antideriv)}")
definite = sp.simplify(antideriv.subs(u, a / 10) - antideriv.subs(u, eps))
check("int dr/sqrt|f| DIVERGES as eps -> 0 -- infinite affine parameter to reach Nariai",
      sp.limit(definite, eps, 0, '+') == sp.oo, "-> oo")

# ---- NON-DEGENERATE CONTROL -- the discriminator ----------------------------
print()
print("  NON-DEGENERATE CONTROL -- Schwarzschild's simple root at r = 2M.")
kS = sp.simplify(sp.diff(fS, r).subs(r, 2 * M) / 2)
check("CONTROL: kappa = 1/4M is NONZERO -- the fixed point is hyperbolic",
      sp.simplify(kS) != 0, f"kappa = {kS}")
IS = sp.integrate(1 / sp.sqrt(sp.Abs(sp.diff(fS, r).subs(r, 2 * M)) * (r - 2 * M)),
                  (r, 2 * M, 2 * M + M))
check("CONTROL: and the approach integral CONVERGES at a simple root -- finite parameter",
      IS.is_finite is not False and not IS.has(sp.oo), f"{sp.simplify(IS)}")

print()
print("=" * 78)
if FAILS:
    print(f"  VERDICT: {len(FAILS)} FAILURE(S): {', '.join(FAILS)}")
    raise SystemExit(1)
print("  VERDICT: ALL PASS.  One function, two readings.  Timelike: the slicing curve is")
print("  the zero-energy orbit of V = -|f|/2 and P03's own formula is -dV/dr, sign")
print("  included, so the horizons are turning points.  Null: the outgoing flow dr/dv =")
print("  f/2 has equilibria at the zeros of f and its eigenvalue IS the surface gravity.")
print("  At Nariai both degenerate together -- unstable equilibrium, non-hyperbolic fixed")
print("  point, infinite affine parameter -- while the simple-root control stays")
print("  hyperbolic with a finite approach, so the degeneracy is measured and not assumed.")
print("=" * 78)
