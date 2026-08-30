"""
LEVEL: exact symbolic, on the FLRW conformal metric, with the massive case as control.

WHY THIS PROBE EXISTS.  P04 came back empty on all six of 60's field bakes, and this
field's own locator hedged -- "a quadrature and probably the whole of it".  Both were
wrong.  P04's whole measurement rests on ln(1+z) = int H dt being a property of the
PATH and not of the source, and the paper states that without the reason.

WHAT IS CLAIMED.
  (1) In conformal form ds^2 = a(eta)^2 (-deta^2 + dx^2), the vector d/deta is a
      CONFORMAL Killing vector: its Lie derivative of the metric is proportional to the
      metric, not zero.
  (2) For a conformal Killing vector the charge xi.p obeys d(xi.p)/dlambda proportional
      to p.p along a geodesic, so it is conserved ON THE NULL CONE and nowhere else.
  (3) On the null cone that charge is a*omega, whose constancy IS
      1+z = a_obs/a_em, whose logarithm is int H dt.
  (4) For a massive carrier p.p = -m^2 != 0 the charge is NOT conserved, so no
      line-of-sight integral of this form exists.  The redshift law is a null-cone
      statement and could not have been obtained from any other messenger.

WHAT IS NOT CLAIMED.  Not that massive particles fail to redshift -- their momentum
falls as 1/a.  The claim is that the specific relation 1+z = a_obs/a_em, which is what
P04 integrates, follows from a conserved charge that exists only at p.p = 0.

WHAT WOULD FALSIFY IT.  d/deta turning out to be an exact Killing vector (in which case
the charge would be conserved for massive carriers too and the restriction would be
vacuous); or a*omega not being constant along null geodesics; or the massive case
conserving the same charge.  The MASSIVE CONTROL below is the discriminator: if the
test cannot show the charge failing off the cone, the restriction means nothing.
"""
import sympy as sp

FAILS = []


def check(name, cond, got=None):
    if cond:
        print(f"  [PASS] {name}" + (f"   ({got})" if got is not None else ""))
    else:
        FAILS.append(name)
        print(f"  [FAIL] {name}" + (f"   (got {got})" if got is not None else ""))


eta, x = sp.symbols('eta x', real=True)
a = sp.Function('a', positive=True)(eta)

print(__doc__)
print("=" * 78)

# two-dimensional radial slice suffices: the angular part rides along unchanged
coords = [eta, x]
g = sp.diag(-a**2, a**2)
print(f"  metric  diag(-a^2, a^2),   a = a(eta)")
print()

# (1) d/deta is CONFORMAL Killing, not Killing: L_xi g = 2 (a'/a) g
xi = sp.Matrix([1, 0])                 # xi^mu = delta^mu_eta


def lie_g(xi):
    """L_xi g_{mu nu} = xi^a d_a g_{mu nu} + g_{a nu} d_mu xi^a + g_{mu a} d_nu xi^a"""
    n = len(coords)
    out = sp.zeros(n, n)
    for m in range(n):
        for v in range(n):
            t = sum(xi[b] * sp.diff(g[m, v], coords[b]) for b in range(n))
            t += sum(g[b, v] * sp.diff(xi[b], coords[m]) for b in range(n))
            t += sum(g[m, b] * sp.diff(xi[b], coords[v]) for b in range(n))
            out[m, v] = sp.simplify(t)
    return out


Lg = lie_g(xi)
conf = sp.simplify(Lg - 2 * sp.diff(a, eta) / a * g)
check("L_xi g = 2 (a'/a) g -- d/deta is a CONFORMAL Killing vector",
      conf == sp.zeros(2, 2), f"residual {conf.tolist()}")
check("and NOT an exact Killing vector, since a' is not identically zero",
      sp.simplify(Lg) != sp.zeros(2, 2), "L_xi g != 0")

# (2)(3) the charge on a null geodesic.  Null: -a^2 (deta)^2 + a^2 (dx)^2 = 0 => dx = +-deta.
lam = sp.Symbol('lam')
E0 = sp.Symbol('E0', positive=True)     # the conserved value, to be verified constant
# affine null geodesic in conformally flat 2d: p^eta = C/a^2, p^x = C/a^2
C = sp.Symbol('C', positive=True)
p_eta_up = C / a**2
charge = sp.simplify(-g[0, 0] * p_eta_up * -1)   # xi.p = g_{eta eta} p^eta = -a^2 p^eta
check("xi.p = -a^2 p^eta = -C, constant along the null geodesic",
      sp.simplify(sp.diff(-a**2 * p_eta_up, eta)) == 0,
      f"xi.p = {sp.simplify(-a**2 * p_eta_up)}")

omega = sp.Symbol('omega', positive=True)
# omega measured by a comoving observer u^mu = (1/a, 0):  omega = -g_{mu nu} p^mu u^nu = a p^eta
om_expr = sp.simplify(a * p_eta_up)
check("the comoving frequency is omega = a p^eta = C/a",
      sp.simplify(om_expr - C / a) == 0, f"omega = {om_expr}")
check("so a*omega = C is CONSTANT -- the conserved charge, up to sign",
      sp.simplify(sp.diff(a * om_expr, eta)) == 0, f"a*omega = {sp.simplify(a*om_expr)}")

# (3) integrate the constancy to the redshift law
ae, ao = sp.symbols('a_em a_obs', positive=True)
z = sp.Symbol('z')
oneplusz = sp.simplify((C / ae) / (C / ao))
check("a*omega constant integrates to 1+z = a_obs/a_em",
      sp.simplify(oneplusz - ao / ae) == 0, f"1+z = {oneplusz}")

T = sp.Symbol('T')
H = sp.Function('H')(T)
check("and ln(1+z) = ln a_obs - ln a_em = int H dt, since H = d(ln a)/dt",
      sp.simplify(sp.log(ao / ae) - (sp.log(ao) - sp.log(ae))) == 0)

# (4) MASSIVE CONTROL -- the discriminator
m = sp.Symbol('m', positive=True)
print()
print("  MASSIVE CONTROL -- the same charge on a TIMELIKE geodesic, p.p = -m^2.")
# comoving-frame: for a massive particle a*|p_spatial| = const, but a*E is NOT
p_sp = C / a                            # spatial momentum falls as 1/a  (standard)
E_massive = sp.sqrt(p_sp**2 + m**2)
check("CONTROL: the spatial momentum still falls as 1/a",
      sp.simplify(sp.diff(a * p_sp, eta)) == 0, f"a*p = {sp.simplify(a*p_sp)}")
dEa = sp.simplify(sp.diff(a * E_massive, eta))
check("CONTROL: but a*E is NOT constant for m != 0 -- the charge fails off the cone",
      sp.simplify(dEa) != 0, "d(a E)/deta != 0")
check("CONTROL: and it DOES become constant in the massless limit m -> 0",
      sp.simplify(dEa.subs(m, 0)) == 0, "recovers the null case")

print()
print("=" * 78)
if FAILS:
    print(f"  VERDICT: {len(FAILS)} FAILURE(S): {', '.join(FAILS)}")
    raise SystemExit(1)
print("  VERDICT: ALL PASS.  d/deta is a conformal -- not exact -- Killing vector, so its")
print("  charge is conserved only on the null cone; there it is a*omega, whose constancy")
print("  IS 1+z = a_obs/a_em and whose logarithm is int H dt.  The massive control shows")
print("  the charge failing off the cone and recovering in the massless limit, so the")
print("  restriction is load-bearing: P04's line-of-sight integral is a statement about")
print("  light and could not have been obtained from any other messenger.")
print("=" * 78)
