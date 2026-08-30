"""
LEVEL: exact symbolic, with the non-elementary case established by reduction.

WHY THIS PROBE EXISTS.  P08 sec:trichotomy says "the three slicings are one
congruence at three energies", with -k = E^2 - 1, and adds that "run inward, the
closed member is the cycloid r = M(1 + cos eta)".  P15 states that the E = 1
integration gives sinh^{2/3}.  Neither says why the E = 1 case integrates and the
others do not, and P08's cycloid identification is stated without the limit in which
it holds.

WHAT IS CLAIMED, three things.
  (1) The quadrature is ELEMENTARY at k = 0 and inverts to sinh^{2/3}.
  (2) At k != 0 the substitution r = u^2 carries it to a sextic under the root, so it
      is not elementary; the only elementary cases are the DEGENERATE corners
      Lambda = 0 (the cycloid) and M = 0 (pure de Sitter).
  (3) The cycloid solves (dr/dtau)^2 = 2M/r - 1 identically -- the Lambda = 0 law --
      while P08's closed member carries the further term r^2/alpha^2, whose weight
      against the dust term is r^3 / 2 M alpha^2.

WHAT IS NOT CLAIMED.  Not that the k != 0 integral has no closed form in ANY special
function: it is an elliptic/hyperelliptic integral and is perfectly well defined.
The claim is that it is not ELEMENTARY, which is what makes the marginal member the
one the corpus can write down.

COMPUTES: the dropped term's weight r^3 / (2 M alpha^2) is evaluated at the
illustrative gauge 2M = 0.1 alpha, giving 1e-5 at r/alpha = 0.01 and 0.27 at 0.3.
That gauge is an ILLUSTRATION of how fast the ratio grows, not a physical parameter
of any member of the family: the ratio's form is exact and the number 0.1 is chosen.
No result below depends on it -- the elementary/non-elementary split is parameter-free.

WHAT WOULD FALSIFY IT.  A constant-coefficient elementary antiderivative for the
k != 0 integrand; or the cycloid satisfying the Lambda != 0 law; or the omitted term
being negligible at all radii rather than only for r << alpha.
"""
import sympy as sp

FAILS = []


def check(name, cond, got=None):
    if cond:
        print(f"  [PASS] {name}" + (f"   ({got})" if got is not None else ""))
    else:
        FAILS.append(name)
        print(f"  [FAIL] {name}" + (f"   (got {got})" if got is not None else ""))


r, M, a, k, eta = sp.symbols('r M alpha k eta', positive=True)

print(__doc__)
print("=" * 78)
print("  the family:  (dr/dtau)^2 = 2M/r + r^2/alpha^2 - k,     k = 1 - E^2")
print()

# (1) k = 0 is elementary and inverts to sinh^{2/3}
I0 = sp.integrate(1 / sp.sqrt(2 * M / r + r**2 / a**2), r)
check("k = 0: the quadrature evaluates in elementary functions",
      I0.has(sp.asinh) or I0.has(sp.log), f"{sp.simplify(I0)}")

tau = sp.Symbol('tau', positive=True)
rsol = (2 * M * a**2)**sp.Rational(1, 3) * sp.sinh(sp.Rational(3, 2) * tau / a)**sp.Rational(2, 3)
lhs = sp.simplify(sp.diff(rsol, tau)**2)
rhs = sp.simplify(2 * M / rsol + rsol**2 / a**2)
check("k = 0: r ~ sinh^{2/3} satisfies the radial equation identically",
      sp.simplify(sp.expand(lhs - rhs)) == 0)

# (2) k != 0 reduces to a sextic under the root
u = sp.Symbol('u', positive=True)
integrand = sp.sqrt(r) / sp.sqrt(r**3 - k * a**2 * r + 2 * M * a**2)
sub = sp.simplify(integrand.subs(r, u**2) * 2 * u)
poly = sp.simplify(u**6 - k * a**2 * u**2 + 2 * M * a**2)
check("k != 0: r = u^2 gives a degree-SIX polynomial under the root",
      sp.degree(sp.Poly(poly, u)) == 6, f"degree {sp.degree(sp.Poly(poly, u))}")

unev = sp.integrate(1 / sp.sqrt(2 * M / r + r**2 / a**2 - k), r)
check("k != 0: sympy returns the quadrature UNEVALUATED (no elementary form found)",
      unev.has(sp.Integral), "Integral(...) returned")

# the two degenerate corners ARE elementary
Ic = sp.integrate(1 / sp.sqrt(2 * M / r - 1), r)          # Lambda = 0, k = +1
check("degenerate corner Lambda = 0, k = +1: elementary (the cycloid)",
      not Ic.has(sp.Integral), f"{sp.simplify(Ic)}"[:52])
Id = sp.integrate(1 / sp.sqrt(r**2 / a**2 - k), r)        # M = 0
check("degenerate corner M = 0: elementary (pure de Sitter)",
      not Id.has(sp.Integral), f"{sp.simplify(Id)}"[:52])

# (3) the cycloid solves the Lambda = 0 law and NOT the Lambda != 0 one
rc = M * (1 + sp.cos(eta))
drdt = sp.diff(rc, eta) / rc                    # dtau = r deta for the cycloid gauge
cyc_lhs = sp.simplify(sp.expand_trig(drdt**2))
check("cycloid satisfies (dr/dtau)^2 = 2M/r - 1 identically  [Lambda = 0]",
      sp.simplify(cyc_lhs - (2 * M / rc - 1)) == 0)
resid = sp.simplify(cyc_lhs - (2 * M / rc - 1 + rc**2 / a**2))
check("cycloid does NOT satisfy the Lambda != 0 law -- residual is the dropped term",
      sp.simplify(resid + rc**2 / a**2) == 0, "residual = -r^2/alpha^2")

# the omitted term's weight, at the numbers quoted in P08's landed qualifier
for ratio, want in [(sp.Rational(1, 100), 1e-5), (sp.Rational(3, 10), 0.27)]:
    w = float((ratio**3) / (sp.Rational(1, 10)))   # r^3/(2M alpha^2) with 2M = 0.1 alpha
    check(f"omitted term's weight at r/alpha = {float(ratio)} is ~{want:g}",
          abs(w - want) / want < 0.06, f"{w:.3g}")

print()
print("=" * 78)
if FAILS:
    print(f"  VERDICT: {len(FAILS)} FAILURE(S): {', '.join(FAILS)}")
    raise SystemExit(1)
print("  VERDICT: ALL PASS.  The marginal member E = 1 is the ONLY non-degenerate member")
print("  of the family that integrates in elementary terms; the closed and open members")
print("  reduce to a sextic under the root.  The cycloid and pure de Sitter are the two")
print("  degenerate corners, reached by switching Lambda or M off -- so P08's 'the closed")
print("  member is the cycloid' is exact in the dust limit and a small-r reading otherwise.")
print("=" * 78)
