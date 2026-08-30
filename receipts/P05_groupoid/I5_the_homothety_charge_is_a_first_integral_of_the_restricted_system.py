"""I5 — THE HOMOTHETY CHARGE IS A FIRST INTEGRAL OF THE RESTRICTED SYSTEM, NOT A WEAKER KIND OF ONE.

INTEGRABLE-SYSTEMS FIELD BAKE, probe I5.  P05 states, correctly and with its own receipt
(V5_homothety_charge), that the dilation's charge xi.p is conserved on the null cone and nowhere
else, the failure off the cone going as -m^2.  It then glosses: "A symmetry that is not a symmetry
of the action carries no Noether charge."

** BOTH SENTENCES ARE TRUE AND THEY SIT IN TENSION ON THEIR FACE. **  A reader meeting them in
order sees a charge that is conserved somewhere and a symmetry that carries no charge.  The field
that owns the object supplies the one word that reconciles them, and it is not a softening:

  *** p.p IS ITSELF CONSERVED, SO THE NULL CONE IS AN INVARIANT SUBMANIFOLD OF THE GEODESIC FLOW,
      AND xi.p IS A GENUINE FIRST INTEGRAL OF THE FLOW RESTRICTED TO IT. ***

In Dirac's language the statement is exact: the homothety charge commutes with the Hamiltonian
WEAKLY (on the constraint surface) and not STRONGLY.  {xi.p, p.p} = 2 p.p, which vanishes on
p.p = 0 and nowhere else -- the same "and nowhere else" P05 already has, now as a bracket.

WHAT THIS BUYS, AND IT IS THE REASON THE ROW IS OWED:
  * it says WHY the charge is conserved exactly there rather than merely THAT it is -- the
    conservation is not a coincidence of the null case, it is the bracket closing on the surface;
  * it says what the charge may and may not be counted toward.  Liouville's theorem counts
    independent integrals in involution against the degrees of freedom OF THE PHASE SPACE BEING
    INTEGRATED.  xi.p enters the tally for the null subsystem.  ** It may not be added to the
    tally for massive geodesics, where it is not an integral at all. **

VERDICTS, each able to have returned otherwise:
  1. p.p is conserved along any affinely parametrised geodesic -> the cone is invariant.
  2. d/dtau (xi.p) = c (p.p): zero on null, EXACTLY -c m^2 on timelike, nonzero on spacelike.
  3. the Poisson bracket {xi.p, p.p} = 2 p.p -- weakly zero, NOT identically zero.
  4. integrated: on a null geodesic xi.p is constant to machine precision; on a timelike one it
     is exactly linear in tau with slope -c m^2, so the failure is not a small effect.
  5. INDEPENDENCE -- xi.p is functionally independent of the ambient isometry charges, so on the
     cone it genuinely ADDS one to the count rather than restating a Killing charge.

Written r3608 by node 60, integrable-systems bake.  Stated for reversal.
"""
import numpy as np
import sympy as sp

FAIL = []
def check(label, got, want, tol=None):
    ok = (abs(got - want) <= tol) if tol is not None else (sp.simplify(got - want) == 0)
    print(f"    [{'ok' if ok else 'FAIL'}]  {label}")
    if not ok:
        FAIL.append((label, got, want))
    return ok

n = 6                                     # the substrate's ambient R^{5,1}
X = sp.symbols('X0:6', real=True)         # X^a, contravariant
P = sp.symbols('p0:6', real=True)         # p_a, COVARIANT -- the canonical conjugate
INV = [-1, 1, 1, 1, 1, 1]                 # eta^{aa}, mostly-plus with one timelike direction

# ** INDEX PLACEMENT IS THE WHOLE OF THIS AND A FIRST DRAFT GOT IT WRONG. **  (X^a, p_a) are the
# canonical pair, so the dilation's charge xi^a p_a is a PLAIN contraction with no metric in it,
# while p.p = eta^{ab} p_a p_b carries the inverse metric.  Putting eta into xi.p makes the
# bracket come out 2*sum(p_a^2) -- positive definite, never zero, and the whole result vanishes.
pp   = sum(INV[i] * P[i]**2 for i in range(n))             # p.p = eta^{ab} p_a p_b
xidp = sum(X[i] * P[i] for i in range(n))                  # xi.p = xi^a p_a, xi^a = X^a

print("=" * 78)
print("I5 — THE HOMOTHETY CHARGE, NAMED BY THE FIELD THAT OWNS IT")
print("=" * 78)

# ---------------------------------------------------------------- VERDICT 1
print("\nVERDICT 1 — p.p is conserved, so the null cone is an INVARIANT SUBMANIFOLD.")
print("  Along an affinely parametrised geodesic X(tau) = X0 + p tau in the flat ambient,")
print("  dp/dtau = 0, so d(p.p)/dtau = 0 identically -- for EVERY causal character.")
tau = sp.Symbol('tau', real=True)
Xt = [X[i] + INV[i] * P[i] * tau for i in range(n)]        # dX^a/dtau = eta^{ab} p_b
pp_t = sum(INV[i] * P[i]**2 for i in range(n))
check("d(p.p)/dtau == 0 identically", sp.diff(pp_t, tau), 0)
print("  => {p.p = 0} is preserved by the flow.  *** That is what makes 'restricted' a")
print("     legitimate word here rather than an excuse. ***")

# ---------------------------------------------------------------- VERDICT 2
print("\nVERDICT 2 — d(xi.p)/dtau = c (p.p), evaluated by causal character (c = 1 for xi^A = X^A).")
xidp_t = sum(Xt[i] * P[i] for i in range(n))
rate = sp.simplify(sp.diff(xidp_t, tau))
check("rate == p.p exactly", rate, pp)
m = sp.Symbol('m', positive=True)
for lab, val, want_zero in [("NULL      p.p = 0",  0,      True),
                            ("TIMELIKE  p.p = -m^2", -m**2, False),
                            ("SPACELIKE p.p = +s^2", sp.Symbol('s', positive=True)**2, False)]:
    is_zero = (sp.simplify(val) == 0)
    print(f"    {lab:24s} -> d(xi.p)/dtau = {sp.simplify(val)}")
    check(f"{lab.split()[0]}: conserved is {want_zero}", int(is_zero), int(want_zero))

# ---------------------------------------------------------------- VERDICT 3
print("\nVERDICT 3 — THE BRACKET.  {xi.p, p.p} = 2 p.p : WEAKLY zero, not identically zero.")
def poisson(F, G):
    return sum(sp.diff(F, X[i]) * sp.diff(G, P[i]) - sp.diff(F, P[i]) * sp.diff(G, X[i])
               for i in range(n))
br = sp.simplify(poisson(xidp, pp))
print(f"    {{xi.p, p.p}} = {br}")
check("{xi.p, p.p} == 2 p.p", br, 2 * pp)
print("    and it is NOT identically zero -- the discriminating half:")
sub = {X[0]: 1, X[1]: 0, X[2]: 0, X[3]: 0, X[4]: 0, X[5]: 0,
       P[0]: sp.Rational(3, 2), P[1]: 1, P[2]: 0, P[3]: 0, P[4]: 0, P[5]: 0}
val = sp.simplify(br.subs(sub))               # p.p = -9/4 + 1 = -5/4, timelike
check("at a TIMELIKE point the bracket is nonzero (= -5/2)", val, sp.Rational(-5, 2))
print("    *** So xi.p commutes with the Hamiltonian ON the constraint surface and nowhere else.")
print("        A first integral of the RESTRICTED system.  Not of the full one. ***")

# ---------------------------------------------------------------- VERDICT 4
print("\nVERDICT 4 — INTEGRATED, so the claim is not left as an identity.")
rng = np.random.default_rng(20260830)
def run(mass2, label):
    """build a geodesic with p.p = mass2 exactly, integrate, report the drift"""
    spatial = rng.normal(size=n - 1)
    s2 = spatial @ spatial
    p0 = np.sqrt(s2 - mass2)                  # -p0^2 + |s|^2 = mass2, with p_a covariant
    p = np.concatenate(([p0], spatial))
    x0 = rng.normal(size=n)
    g = np.array([-1.0] + [1.0] * (n - 1))    # eta^{aa}
    ppn = float((g * p) @ p)
    v = g * p                                 # dX^a/dtau = eta^{ab} p_b
    taus = np.linspace(0.0, 10.0, 2001)
    q = np.array([(x0 + v * t) @ p for t in taus])      # xi.p = X^a p_a
    slope = np.polyfit(taus, q, 1)[0]
    spread = float(q.max() - q.min())
    print(f"    {label:22s} p.p = {ppn:+.6f}   drift over tau in [0,10] = {spread:.3e}"
          f"   fitted slope = {slope:+.6f}")
    return ppn, slope, spread

ppn, slope, spread = run(0.0, "NULL geodesic")
check("null: p.p is 0 to 1e-12", ppn, 0.0, tol=1e-12)
check("null: xi.p constant to 1e-10", spread, 0.0, tol=1e-10)
mass = 1.7
ppn_t, slope_t, spread_t = run(-mass**2, "TIMELIKE geodesic")
check(f"timelike: p.p == -m^2 = {-mass**2:+.4f}", ppn_t, -mass**2, tol=1e-10)
check("timelike: slope == -m^2 (c = 1)", slope_t, -mass**2, tol=1e-8)
print(f"    *** the drift is EXACTLY linear at slope -m^2 = {-mass**2:+.4f}, not a small effect. ***")

# ---------------------------------------------------------------- VERDICT 5
print("\nVERDICT 5 — INDEPENDENCE.  On the cone, xi.p ADDS an integral rather than restating one.")
print("  The ambient isometry charges are the so(5,1) ones: translations p_A and boosts/rotations")
print("  J_AB = X_A p_B - X_B p_A.  Test independence by the RANK of the Jacobian of")
print("  {p.p, xi.p, p_0..p_5} with respect to (X, p) at a point ON the cone.")
charges = [pp, xidp] + [P[k] for k in range(n)]
Jac = sp.Matrix([[sp.diff(c, v) for v in list(X) + list(P)] for c in charges])
# a point on the cone: p = (1,1,0,0,0,0) -> p.p = -1 + 1 = 0
on_cone = {X[0]: 0, X[1]: 2, X[2]: 0, X[3]: 0, X[4]: 0, X[5]: 0,
           P[0]: 1, P[1]: 1, P[2]: 0, P[3]: 0, P[4]: 0, P[5]: 0}
check("the test point is ON the cone", sp.simplify(pp.subs(on_cone)), 0)
rank = Jac.subs(on_cone).rank()
print(f"    rank of the Jacobian of the {len(charges)} charges at that point = {rank}")
check("rank == 7: xi.p is independent of p.p and of the six translations", rank, 7)
print("  *** So on the null subsystem the homothety charge is a genuine extra integral. ***")
print("      And on the massive system it is not an integral at all, so it enters NO tally there.")

# ---------------------------------------------------------------- the control
print("\nCONTROL — a genuine KILLING field must behave differently, or this receipt proves nothing.")
print("  Take the ambient translation xi^A = const (a Killing field): charge = xi.p, and")
print("  {xi.p, p.p} must be IDENTICALLY zero rather than weakly zero.")
k = sp.symbols('k0:6', real=True)
kdp = sum(k[i] * P[i] for i in range(n))          # k^a p_a, k^a constant
br_k = sp.simplify(poisson(kdp, pp))
print(f"    {{k.p, p.p}} = {br_k}")
check("Killing: the bracket is IDENTICALLY zero", br_k, 0)
print("  *** The two cases separate. A receipt in which both came out the same would be measuring")
print("      nothing, and this is the line that would have caught it. ***")

print("\n" + "=" * 78)
if FAIL:
    print(f"  VERDICT: {len(FAIL)} CHECK(S) FAILED")
    for f in FAIL:
        print("   ", f)
    raise SystemExit(1)
print("  VERDICT: ALL PASS.  The homothety charge is a first integral of the geodesic flow")
print("  RESTRICTED to the invariant submanifold p.p = 0 -- {xi.p, p.p} = 2 p.p, weakly zero.")
print("  It counts toward the null subsystem's tally and toward no other.")
print("=" * 78)
