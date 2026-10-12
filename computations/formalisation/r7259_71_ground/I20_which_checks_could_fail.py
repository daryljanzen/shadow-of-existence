"""r7259+71.4 -- which of I20's ten checks could have failed?

The receipt (receipts/P04_modern_parallax/I20_the_redshift_is_a_conformal_killing_charge_
on_the_null_cone.py, owned by another seat, NOT edited here) prints VERDICT: ALL PASS.
This probe does not dispute its claims.  It asks a narrower question, the one a formal
statement would force: for each check, is there an input change that turns it red?  A
check no mutation can turn red is satisfied by construction.

Three things are tested, each by running the receipt's own expressions:
  (1) the geodesic input p^eta = C/a^2 is ASSERTED in the receipt; here it is DERIVED
      from the geodesic equation of diag(-a^2, a^2), so the claim is shown true and the
      receipt's check of it is shown to rest on an input rather than a derivation;
  (2) the "ln(1+z) = int H dt" check never uses H; it passes for any H whatever;
  (3) the three "!= 0" checks pass whenever sympy fails to REDUCE an expression to zero,
      which is not a proof of non-vanishing; here each is evaluated exactly at a concrete
      a(eta), showing the claims true by a test that could have failed.
"""
import sympy as sp

FAILS = []


def check(name, cond, got=None):
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"   ({got})" if got is not None else ""))
    if not cond:
        FAILS.append(name)


eta, x, lam = sp.symbols('eta x lam', real=True)
a = sp.Function('a', positive=True)

# ---------------------------------------------------------------- (1) derive the null geodesic
print("(1) the null geodesic of diag(-a^2, a^2), derived rather than asserted")
coords = [eta, x]
g = sp.diag(-a(eta)**2, a(eta)**2)
ginv = g.inv()
Gam = [[[sp.simplify(sum(ginv[i, l] * (sp.diff(g[l, j], coords[k]) + sp.diff(g[l, k], coords[j])
                                       - sp.diff(g[j, k], coords[l])) for l in range(2)) / 2)
         for k in range(2)] for j in range(2)] for i in range(2)]
# eta-component of the geodesic equation, written for p^mu = dx^mu/dlam along a null curve
# (p^x = +- p^eta).  With p^eta = P(eta): dP/dlam = P dP/deta = -Gam^eta_{ab} p^a p^b
P = sp.Function('P')
peta, px = P(eta), P(eta)
rhs = -sum(Gam[0][j][k] * [peta, px][j] * [peta, px][k] for j in range(2) for k in range(2))
ode = sp.Eq(peta * sp.diff(peta, eta), rhs)
sol = sp.dsolve(ode, P(eta))
sols = sol if isinstance(sol, list) else [sol]
C1 = sp.Symbol('C1')
derived = [s.rhs for s in sols if s.rhs != 0]
ok = any(sp.simplify(d * a(eta)**2).free_symbols <= {C1} | {sp.Symbol('C1')} and
         sp.simplify(sp.diff(d * a(eta)**2, eta)) == 0 for d in derived)
check("the geodesic equation gives p^eta proportional to 1/a^2 -- the receipt's input is TRUE",
      ok, f"solutions {derived}")
print("      ... and the receipt states it as an assumption ('p^eta = C/a^2'), so its check")
print("      'xi.p = -a^2 p^eta constant' reads back the input it was given: -a^2 * C/a^2 = -C.")
C = sp.Symbol('C', positive=True)
for wrong in (C / a(eta), C / a(eta)**3):
    xi_p = -a(eta)**2 * wrong
    check(f"MUTATION p^eta = {wrong}: the receipt's 'xi.p constant' check would turn red",
          sp.simplify(sp.diff(xi_p, eta)) != 0)
print("      So that check DISCRIMINATES its input -- but nothing in the receipt fixes the")
print("      input except the comment; the geodesic equation is never written.")

# ---------------------------------------------------------------- (2) the ln / int H check
print()
print("(2) 'ln(1+z) = ln a_obs - ln a_em = int H dt'")
ae, ao = sp.symbols('a_em a_obs', positive=True)
T = sp.Symbol('T')
for Hmut in (sp.Function('H')(T), sp.Integer(0), sp.exp(T), sp.Symbol('anything')):
    expr = sp.simplify(sp.log(ao / ae) - (sp.log(ao) - sp.log(ae)))   # the receipt's own test
    check(f"with H = {Hmut}: the receipt's test still passes (H does not appear in it)",
          expr == 0 and Hmut not in expr.atoms(sp.Function, sp.Symbol))
print("      CANNOT FAIL: the test is the identity log(u/v) = log u - log v; the integral")
print("      of H named in the check's title is not computed anywhere in the receipt.")

# ---------------------------------------------------------------- (3) the != 0 checks, exactly
print()
print("(3) the three '!= 0' checks, re-run exactly at a concrete a(eta) = exp(eta)")
m = sp.Symbol('m', positive=True)
conc = {a(eta): sp.exp(eta)}
Lg_eta_eta = sp.diff(-a(eta)**2, eta)            # L_xi g_{eta eta} for xi = d/deta
v = sp.simplify(Lg_eta_eta.subs(conc).doit())
check("NOT exact Killing: L_xi g_{eta eta} at a = e^eta is nonzero", v != 0 and v.equals(0) is False, v)
p_sp = C / a(eta)
E = sp.sqrt(p_sp**2 + m**2)
dEa = sp.diff(a(eta) * E, eta)
val = sp.simplify(dEa.subs(conc).doit().subs({C: 1, m: 1, eta: 0}))
check("massive control: d(aE)/deta at a = e^eta, C = m = 1, eta = 0 is nonzero", val != 0, val)
val0 = sp.simplify(dEa.subs(m, 0).subs(conc).doit())
check("massless limit: d(aE)/deta vanishes identically at a = e^eta", val0 == 0, val0)
print("      The claims hold; the receipt's own form of the first two tests passes whenever")
print("      simplify does not reach 0, so a red was not reachable through them.")

print()
print("=" * 78)
if FAILS:
    print(f"VERDICT: {len(FAILS)} FAILURE(S): {', '.join(FAILS)}")
    raise SystemExit(1)
print("VERDICT: I20's CLAIMS HOLD, AND OF ITS TEN CHECKS ONE CANNOT FAIL (the ln/int-H check,")
print("H unused), ONE READS BACK AN ASSERTED INPUT (the geodesic, derived here and true), AND")
print("TWO ARE FAIL-OPEN '!= 0' TESTS (re-run exactly here and true).  The one computation in")
print("the receipt that a formal statement would carry unchanged is the Lie-derivative identity.")
print("=" * 78)
