#!/usr/bin/env python3
"""
`L-150`.  ** THE CORPUS SAYS IT HAS NO SCALE-INVARIANT ATTRACTOR.  ITS OWN COLLAPSE LEG IS ONE. **

P15 `sec:predictions` lists as an established signature: *"the branch point carries the progenitor
tilt and does not drive $n_s\\to1$; CR has no inflationary scale-invariant attractor."*  The
adjective is doing more work than the sentence admits.  ** There are TWO backgrounds that produce a
scale-invariant spectrum, they are the two roots of one quadratic, and only one of them is
inflation.  The other is a MATTER-DOMINATED CONTRACTION — and the corpus's collapse leg near the
branch point is exactly that, by its own solution. **

  PART 1  ** THE CONDITION, AND ITS TWO ROOTS: $\\beta(\\beta-1)=2$ gives $\\beta=-1$ (de Sitter
          inflation) and $\\beta=+2$ (matter contraction).  Dual, and both scale-invariant. **
  PART 2  ** THE CORPUS'S COLLAPSE LEG IS $\\beta=2$ EXACTLY, derived from its own $r^3=(9/2)M\\tau^2$. **
  PART 3  ** THE SPECTRUM, INTEGRATED: $n_s=1$ at leading order, checked numerically. **
  PART 4  ** THE CORRECTION, AND ITS SIGN: the exact $\\sinh^{2/3}$ solution departs from $\\beta=2$,
          different wavenumbers exit at different epochs, and the departure TILTS the spectrum. **
  PART 5  What this does and does not settle.

Run: python3 L150a_the_collapse_leg_is_the_scale_invariant_one.py      (sympy, numpy, scipy)
"""
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

print(__doc__.split("Run:")[0])

# =====================================================================
print("=" * 78)
print("PART 1 — THE CONDITION AND ITS TWO ROOTS")
print("=" * 78)
eta, beta, k = sp.symbols('eta beta k', real=True)
a_pow = (-eta)**beta
zz = sp.simplify(sp.diff(a_pow, eta, 2) / a_pow)
print(f"  For a background a ∝ (-eta)^beta with z ∝ a, the Mukhanov--Sasaki potential is")
print(f"     z''/z = a''/a = {sp.simplify(zz)}")
print(f"  Scale invariance needs this to be 2/eta^2 -- the de Sitter value -- so:")
roots = sorted(sp.solve(sp.Eq(beta * (beta - 1), 2), beta))
print(f"     ** beta(beta-1) = 2   ⇒   beta = {roots} **")
assert roots == [-1, 2]
print()
print(f"  {'beta':>6} {'background':>34} {'a ∝':>16} {'scale-invariant?':>18}")
for b, nm, sc, si in [(-1, "de Sitter inflation (expanding)", "1/(-eta)", "yes"),
                      (2, "matter-dominated CONTRACTION", "(-eta)^2", "yes")]:
    print(f"  {b:>6} {nm:>34} {sc:>16} {si:>18}")
print()
for s in [
 "⌗ ** THIS IS A KNOWN DUALITY IN THE LITERATURE (Wands 1999; Finelli--Brandenberger 2002) AND THE",
 "   CORPUS DOES NOT CITE IT ANYWHERE. **  *It is stated here as what it is — a standard result",
 "   about a standard equation — and the work below is checking whether THIS construction's",
 "   collapse leg satisfies its hypothesis.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE CORPUS'S COLLAPSE LEG IS beta = 2")
print("=" * 78)
tau, M, al = sp.symbols('tau M alpha', positive=True)
print("  P14 `P14_mode_monodromy_at_the_wall` and P8 `prop:cosmo`, both already banked:")
print("     r^3 = (9/2) M tau^2 + O(tau^4)      and the scale factor IS the areal radius, a = |r|.")
a_of_tau = (sp.Rational(9, 2) * M * tau**2)**sp.Rational(1, 3)
print(f"     so a(tau) = {sp.simplify(a_of_tau)}  ∝ tau^(2/3)   -- the matter-dominated law")
p = sp.simplify(sp.log(a_of_tau).diff(tau) * tau)
print(f"     check: d ln a / d ln tau = {p}   (= 2/3 exactly)")
assert sp.simplify(p - sp.Rational(2, 3)) == 0
print()
print("  Conformal time: d eta = d tau / a  ⇒")
eta_of_tau = sp.simplify(sp.integrate(1 / a_of_tau, tau))
print(f"     eta(tau) = {eta_of_tau}   ∝ tau^(1/3)")
q = sp.simplify(sp.log(eta_of_tau).diff(tau) * tau)
assert sp.simplify(q - sp.Rational(1, 3)) == 0
print(f"     so tau ∝ eta^3 and a ∝ tau^(2/3) ∝ ** eta^2 **")
print()
for s in [
 "⇒⇒ ** THE COLLAPSE LEG IS beta = 2 EXACTLY, WHICH IS THE SECOND ROOT. **  *And it is forced, not",
 "   fitted: near the branch point $f\\to-2M/r$, the MASS term dominates and the $\\Lambda$ term",
 "   vanishes, so the leg is pressureless there — **which is the same fact `A·4` used at c54.112**",
 "   *when it found that a pressureless component has $c_s=0$ and crosses exactly.*",
 "",
 "⌗⌗ ** SO THE TWO RESULTS THE CORPUS ALREADY HAS ARE THE TWO HALVES OF ONE MECHANISM: the crossing",
 "   transmits what is frozen (c54.121/P15), and what is frozen was frozen by a matter-dominated",
 "   contraction — which is the one non-inflationary background that freezes a SCALE-INVARIANT",
 "   spectrum. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE SPECTRUM, INTEGRATED")
print("=" * 78)
print("  Solve v'' + (k^2 - a''/a) v = 0 on a ∝ (-eta)^2 from deep inside the horizon (|k eta| >> 1)")
print("  with vacuum data v = e^{-ik eta}/sqrt(2k), and read P(k) = k^3 |v/a|^2 at |k eta| << 1.")


def spectrum(beta_val, kk, eta_i=-4000.0, eta_f=-1e-3):
    """integrate the real and imaginary parts of the mode function"""
    def rhs(e, y):
        pot = beta_val * (beta_val - 1) / e**2
        return [y[1], -(kk**2 - pot) * y[0], y[3], -(kk**2 - pot) * y[2]]
    ei = min(eta_i, -200.0 / kk)          # start each k well inside its own horizon
    y0 = [np.cos(kk * ei) / np.sqrt(2 * kk), kk * np.sin(kk * ei) / np.sqrt(2 * kk),
          -np.sin(kk * ei) / np.sqrt(2 * kk), kk * np.cos(kk * ei) / np.sqrt(2 * kk)]
    sol = solve_ivp(rhs, [ei, eta_f], y0, rtol=1e-10, atol=1e-14, dense_output=True)
    v2 = sol.y[0, -1]**2 + sol.y[2, -1]**2
    a_f = abs(eta_f)**beta_val
    return kk**3 * v2 / a_f**2


KS = np.array([0.05, 0.1, 0.2, 0.5, 1.0, 2.0])
print(f"\n  {'k':>10} {'P(k), beta=2 (contraction)':>28} {'P(k), beta=-1 (de Sitter)':>28}")
P2 = np.array([spectrum(2.0, kk) for kk in KS])
Pm = np.array([spectrum(-1.0, kk) for kk in KS])
for kk, p2, pm in zip(KS, P2, Pm):
    print(f"  {kk:>10.3g} {p2:>28.6g} {pm:>28.6g}")
n2 = np.polyfit(np.log(KS), np.log(P2), 1)[0]
nm = np.polyfit(np.log(KS), np.log(Pm), 1)[0]
print(f"\n  ** d ln P / d ln k :  contraction {n2:+.4f}   de Sitter {nm:+.4f} **")
print(f"  ** so n_s = 1 + dlnP/dlnk :  contraction {1+n2:.4f}   de Sitter {1+nm:.4f} **")
assert abs(n2) < 1e-3, n2
assert abs(nm) < 1e-3, nm
print()
for s in [
 "✔✔ ** BOTH FLAT TO A PART IN A THOUSAND.  The matter-dominated CONTRACTION freezes a",
 "   scale-invariant spectrum exactly as de Sitter inflation does, and the corpus's collapse leg",
 "   is the contraction. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE CORRECTION, AND ITS SIGN")
print("=" * 78)
print("  The exact leg is a = (2 M alpha^2)^(1/3) sinh^(2/3)(3 tau / 2 alpha), not a pure power.")
u = sp.symbols('u', positive=True)
ser = sp.series(sp.sinh(u)**sp.Rational(2, 3), u, 0, 4).removeO()
print(f"     sinh^(2/3)(u) = {sp.simplify(ser)}   ⇒ a ∝ tau^(2/3) [1 + (3 tau/2 alpha)^2/9 + ...]")
c2 = sp.simplify(sp.expand(ser / u**sp.Rational(2, 3)).coeff(u, 2))
print(f"     the leading departure from the pure power has coefficient {c2} in u^2, u = 3 tau/2 alpha")
assert sp.simplify(c2 - sp.Rational(1, 9)) == 0
print()
print("  A mode exits the horizon when k = aH.  On the leg aH = sqrt(2M/r + r^2/alpha^2), which is")
print("  MONOTONE in r, so LARGER k exits LATER (at smaller r, deeper into the pure-matter regime)")
print("  and SMALLER k exits EARLIER (at larger r, where the Lambda term is less negligible).")
al_v, M_v = 1.0, 2.0 / (3.0 * np.sqrt(3.0)) / 2.0
rr = np.logspace(-6, -1.2, 400)
aH = np.sqrt(2 * M_v / rr + rr**2 / al_v**2)
frac_lambda = (rr**2 / al_v**2) / (2 * M_v / rr + rr**2 / al_v**2)
print(f"\n  {'k = aH':>12} {'exit radius r/alpha':>20} {'Lambda share of (aH)^2':>24}")
for tgt in [3.0, 10.0, 30.0, 100.0]:
    i = int(np.argmin(abs(aH - tgt)))
    print(f"  {aH[i]:>12.3f} {rr[i]:>20.3e} {frac_lambda[i]:>24.3e}")
print()
for s in [
 "⇒⇒ ** SO THE DEPARTURE FROM SCALE INVARIANCE IS CONTROLLED BY THE $\\Lambda$ SHARE AT HORIZON",
 "   EXIT, AND THAT SHARE FALLS WITH $k$ — every extra decade in $k$ pushes the exit deeper into",
 "   the pure-matter regime, where the spectrum is exactly flat. **  *The long-wavelength end",
 "   carries the contamination; the short-wavelength end is asymptotically flat.*",
 "",
 "⇒ ** A SPECTRUM FLAT AT LARGE $k$ AND DISTURBED AT SMALL $k$ IS A TILT WITH A DEFINITE SIGN",
 "   STRUCTURE, AND IT IS NOT CONSTANT ACROSS THE BAND — a RUNNING, not a single index. **",
 "   ⚠ *Whether it is red or blue, and of what size, is NOT computed here: it needs the mode",
 "   equation integrated on the exact $\\sinh^{2/3}$ background rather than on the pure power, with",
 "   the pressure of the actual progenitor content rather than exact dust.  **That is the next",
 "   step and it is bounded.***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — WHAT THIS SETTLES AND WHAT IT DOES NOT")
print("=" * 78)
print(f"  {'claim':>60} {'status':>16}")
for a, b in [
    ("the collapse leg is beta = 2 (matter-dominated contraction)", "DERIVED"),
    ("beta = 2 freezes a scale-invariant spectrum", "INTEGRATED"),
    ("so n_s = 1 emerges from the construction, not from the progenitor", "FOLLOWS"),
    ("the Lambda term breaks it, and its share falls with k", "COMPUTED"),
    ("the sign and size of the resulting tilt", "NOT YET"),
    ("the amplitude A_s", "NOT TOUCHED"),
]:
    print(f"  {a:>60} {b:>16}")
print()
for s in [
 "⚠⚠ ** AND A CORPUS CLAIM NEEDS CORRECTING: P15 `sec:predictions` lists as ESTABLISHED that 'the",
 "   branch point ... does not drive $n_s\\to1$; CR has no inflationary scale-invariant attractor'.",
 "   The second clause is true and the first is not the same clause. **  *The construction has a",
 "   scale-invariant attractor; it is not inflationary; it is the matter-dominated contraction the",
 "   leg already is.  **The word 'inflationary' was carrying the whole sentence.***",
 "",
 "✔✔ ** AND THE PRIZE, STATED AT ITS HONEST WEIGHT: if this survives, $n_s$ IS NOT AN INHERITED",
 "   DATUM AT ALL.  Its scale-invariant part is a consequence of the leg's own geometry, and only",
 "   its DEPARTURE from unity is inherited — a much smaller thing to owe. **  *The corpus currently",
 "   owes the whole of $n_s$; on this reading it owes $n_s-1\\simeq-0.035$, and has a candidate",
 "   mechanism for that too.*",
 "",
 "⛔ ** NOT CLAIMED, AND THE BOUND IS SHARP: this is the STANDARD matter-contraction result applied",
 "   to a background the corpus derives.  It inherits that literature's known difficulties — the",
 "   growing anisotropy of a contracting phase, and the fact that the DOMINANT mode in contraction",
 "   is not always the one that survives a bounce. **  *The corpus's bounce is a branch point with",
 "   an analytic continuation rather than a smooth bounce, and whether the matching selects the",
 "   scale-invariant mode is exactly the question `A·4` answered for CONTENT and not for MODE",
 "   SELECTION.  That is the falsifier and it is named for the next revision.*",
]:
    print("  " + s)
