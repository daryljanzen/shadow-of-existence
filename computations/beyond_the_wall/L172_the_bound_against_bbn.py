#!/usr/bin/env python3
"""
`L-172`.  ** IS c54.133's BOUND CONSISTENT WITH RUNNING NUCLEOSYNTHESIS ON THE SAME LEG?  YES — AND
THE CHECK ARRIVES INDEPENDENTLY AT THE CORPUS'S NARIAI THRESHOLD. **

c54.133 bounds the parent: $\\rho_r/\\rho_m\\lesssim3.6\\times10^{-5}$ at maximum expansion.  P16 runs
BBN on that same collapse.  The two constrain the same object and have never been compared.

  PART 1  ** THE PROGENITOR MUST RECOLLAPSE AT ALL — and the condition is $2M\\le2\\alpha/3\\sqrt3$,
          which is the NARIAI THRESHOLD, reached here from the closed interior rather than from the
          horizon cubic. **
  PART 2  ** WHAT THE BOUND THEN FIXES: the maximum radius, and the curvature radius at equality. **
  PART 3  ** THE BBN CHECK: is curvature relevant where nucleosynthesis runs? **
  PART 4  The verdict.

Run: python3 L172_the_bound_against_bbn.py      (sympy, numpy)
"""
import numpy as np
import sympy as sp

print(__doc__.split("Run:")[0])
a_, A_, al_ = sp.symbols('a A alpha', positive=True)

# =====================================================================
print("=" * 78)
print("PART 1 — THE PROGENITOR MUST RECOLLAPSE AT ALL")
print("=" * 78)
print("  The closed interior with dust and Lambda has, in units where the curvature term is 1/a^2,")
print("     (da/dtau)^2 = A/a + a^2/alpha^2 - 1      (Lambda = 3/alpha^2)")
print("  and a turnaround exists iff f(a) = A/a + a^2/alpha^2 reaches 1, i.e. iff its MINIMUM is")
print("  at most 1.  Minimising:")
f = A_ / a_ + a_**2 / al_**2
astar = sp.solve(sp.diff(f, a_), a_)[0]
fmin = sp.simplify(f.subs(a_, astar))
print(f"     a* = {sp.simplify(astar)}")
print(f"     f(a*) = {sp.simplify(fmin)}")
cond = sp.solve(sp.Eq(fmin, 1), A_)
print(f"\n  ** recollapse  <=>  f(a*) <= 1  <=>  A <= {sp.simplify(cond[0])} **")
A_max_expr = sp.simplify(cond[0])
# compare with the Nariai value 2 M_N = 2 alpha / (3 sqrt 3)
nariai = 2 * al_ / (3 * sp.sqrt(3))
print(f"  and the corpus's Nariai mass parameter is 2 M_N = {sp.simplify(nariai)}")
print(f"     difference: {sp.simplify(A_max_expr - nariai)}")
assert sp.simplify(A_max_expr - nariai) == 0
print()
for s in [
 "⇒⇒⇒ ** THE RECOLLAPSE THRESHOLD *IS* THE NARIAI THRESHOLD, EXACTLY. **  *And it is reached here",
 "   from a completely different direction: the corpus derives Nariai from the HORIZON CUBIC's",
 "   double root, and this derives it from whether a closed dust ball with $\\Lambda$ turns around.",
 "   **Same number, two constructions, no shared step.***",
 "",
 "⌗ ** SO THE COSMOGENESIS PICTURE IS SELF-CONSISTENT IN A WAY NOBODY CHECKED: a progenitor that",
 "   could seed a universe must be SUB-NARIAI, which is exactly the regime the slicing construction",
 "   requires for three horizons.  A super-Nariai ball does not recollapse and so never reaches a",
 "   branch point at all. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — WHAT THE BOUND THEN FIXES")
print("=" * 78)
LAM = 1.1056e-52
MPC = 3.0857e22
alpha_m = np.sqrt(3.0 / LAM)
alpha_Mpc = alpha_m / MPC
A_max = 2 * alpha_Mpc / (3 * np.sqrt(3))
ratio_bound = 3.6e-5                       # rho_r/rho_m at a_max, from c54.133
a_eq_max = A_max * ratio_bound
print(f"  {'quantity':>44} {'value':>18}")
for nm, v, u in [("alpha", alpha_Mpc, "Mpc"),
                 ("A_max = 2 alpha / (3 sqrt 3)  (recollapse cap)", A_max, "Mpc"),
                 ("a_max ~ A (turnaround, A << alpha)", A_max, "Mpc"),
                 ("a_eq = a_max * (rho_r/rho_m)|_max", a_eq_max, "Mpc")]:
    print(f"  {nm:>44} {v:>18.4g} {u}")
ours_eq = 5064.0 / 3400.0
print(f"\n  {'our own curvature radius at equality':>44} {ours_eq:>18.4g} Mpc")
print(f"  ** so the parent's is at most {a_eq_max/ours_eq:.2f} of ours -- a smaller closed universe,")
print(f"     not an impossible one. **")
assert 0.01 < a_eq_max / ours_eq < 1.0

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE BBN CHECK")
print("=" * 78)
print("  Nucleosynthesis runs on the cooling leg at T ~ 0.1-1 MeV.  Two things could spoil it:")
print("  a wrong expansion RATE there, or a curvature term that is not negligible.")
print()
print("  (i) THE RATE.  In radiation domination H^2 = (8 pi G/3) rho_r, fixed by T and the")
print("      relativistic degrees of freedom ALONE.  It does not know the universe's size.")
print("      ** So at fixed eta the yields are insensitive to a_eq. **")
print()
print("  (ii) THE CURVATURE TERM.  Its ratio to the radiation term is")
print("       (1/a^2) / (B/a^4) = a^2 / B , and with B = A a_eq this is (a/a_eq)(a/A):")
T_eq_eV = 0.8
for T_MeV in [1.0, 0.1, 0.07]:
    a_over_aeq = T_eq_eV / (T_MeV * 1e6)
    a_bbn = a_eq_max * a_over_aeq
    ratio = (a_bbn / a_eq_max) * (a_bbn / A_max)
    print(f"     T = {T_MeV:>5} MeV :  a/a_eq = {a_over_aeq:.3g},  "
          f"curvature/radiation = {ratio:.3g}")
    assert ratio < 1e-10
print()
for s in [
 "⇒⇒ ** THE CURVATURE TERM SITS SOME FIFTEEN ORDERS BELOW THE RADIATION TERM THROUGHOUT",
 "   NUCLEOSYNTHESIS, EVEN AT THE TIGHTEST END OF THE BOUND. **  *A closed universe small enough to",
 "   satisfy c54.133 is still, at MeV temperatures, indistinguishable from a flat one.*",
 "",
 "⌗ *Which is not a surprise once stated — curvature scales as $a^{-2}$ and radiation as $a^{-4}$,",
 "   so the gap widens by four orders per decade of cooling — **but 'not a surprise once stated' is",
 "   exactly the class of thing this corpus has learned to check rather than assume.***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE VERDICT")
print("=" * 78)
print(f"  {'constraint':>46} {'on what':>26} {'verdict':>12}")
for a, b, c in [("recollapse at all", "2M <= 2 alpha/3 sqrt 3", "= NARIAI"),
                ("c54.133's spectral bound", "a_max / a_eq >~ 2.8e4", "compatible"),
                ("BBN yields on the cooling leg", "eta, and the rate at MeV", "untouched")]:
    print(f"  {a:>46} {b:>26} {c:>12}")
print()
for s in [
 "✔✔ ** THE CHECK PASSES, AND IT PASSES BECAUSE THE THREE CONSTRAINTS TURN OUT TO ACT ON NEARLY",
 "   INDEPENDENT QUANTITIES: recollapse constrains the MASS against $\\alpha$; the spectral bound",
 "   constrains the total EXPANSION past equality; BBN constrains $\\eta$ and the rate at MeV",
 "   temperatures.  ** I registered this row expecting three constraints on two numbers; there are",
 "   three constraints on three. ** *The row's own framing was the thing that needed checking.*",
 "",
 "✔✔✔ ** AND THE REAL YIELD IS PART 1, WHICH WAS NOT WHAT THE ROW ASKED FOR: the condition that a",
 "   progenitor recollapse at all is EXACTLY the Nariai threshold, derived here from a closed dust",
 "   ball with $\\Lambda$ and in the corpus from a horizon cubic's double root — two constructions,",
 "   no shared step, same number. **",
 "   *So a progenitor that can seed a universe is necessarily sub-Nariai, which is precisely the",
 "   regime the slicing construction requires for three horizons.  **A super-Nariai ball never",
 "   reaches a branch point at all, because it never turns around.***",
 "",
 "⚠ *Bound: the recollapse condition is computed for dust plus $\\Lambda$; radiation makes the ball",
 "   marginally easier to collapse and does not move the threshold at the bound's radiation",
 "   fractions.  And the BBN comparison uses standard thermodynamics with our own $T_{\\rm eq}$,",
 "   which the corpus's own BBN account already assumes.*",
]:
    print("  " + s)
