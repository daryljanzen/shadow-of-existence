#!/usr/bin/env python3
"""
RECEIPT — P16 (the collapse excursion): ** THE CONDITION THAT A PROGENITOR RECOLLAPSE AT ALL IS
EXACTLY THE NARIAI THRESHOLD — reached from a closed dust ball with Lambda, where the corpus reaches
it from a horizon cubic's double root.  Two constructions, no shared step, same number. **

  PART 1  ** the recollapse condition: A <= 2 alpha/(3 sqrt 3) = 2 M_Nariai, symbolically **
  PART 2  what c54.133's spectral bound then fixes
  PART 3  ** the BBN check: curvature sits ~15 orders below radiation throughout **

rc=0 on success.  Run: python3 P16_recollapse_is_the_nariai_threshold.py    (sympy, numpy)
"""
import sys

import numpy as np
import sympy as sp

print(__doc__.split("rc=0")[0])
a_, A_, al_ = sp.symbols('a A alpha', positive=True)

print("=" * 78)
print("PART 1 — RECOLLAPSE IS NARIAI")
print("=" * 78)
f = A_ / a_ + a_**2 / al_**2
astar = sp.solve(sp.diff(f, a_), a_)[0]
fmin = sp.simplify(f.subs(a_, astar))
cond = sp.simplify(sp.solve(sp.Eq(fmin, 1), A_)[0])
nariai = sp.simplify(2 * al_ / (3 * sp.sqrt(3)))
print("  closed interior, dust + Lambda:  (da/dtau)^2 = A/a + a^2/alpha^2 - 1")
print("  a turnaround exists iff min f <= 1, and")
print(f"     a* = {sp.simplify(astar)},   f(a*) = {fmin}")
print(f"  ** recollapse <=> A <= {cond} **")
print(f"  ** Nariai      2 M_N = {nariai} **")
print(f"     difference = {sp.simplify(cond - nariai)}")
assert sp.simplify(cond - nariai) == 0
print("  ** EXACTLY EQUAL.  The corpus reaches Nariai from the horizon cubic's double root; this")
print("     reaches it from whether a closed dust ball with Lambda turns around.  No shared step. **")
print("  => a progenitor that can seed a universe is necessarily SUB-Nariai, which is precisely the")
print("     regime the slicing construction requires for three horizons.  A super-Nariai ball never")
print("     turns around and so never reaches a branch point at all.")

print()
print("=" * 78)
print("PART 2 — WHAT THE SPECTRAL BOUND THEN FIXES")
print("=" * 78)
alpha_Mpc = np.sqrt(3.0 / 1.1056e-52) / 3.0857e22
A_max = 2 * alpha_Mpc / (3 * np.sqrt(3))
a_eq_max = A_max * 3.6e-5
ours = 5064.0 / 3400.0
print(f"  alpha = {alpha_Mpc:.0f} Mpc,  A_max = {A_max:.0f} Mpc (the recollapse cap)")
print(f"  a_eq = a_max * (rho_r/rho_m)|_max <= {a_eq_max:.5f} Mpc")
print(f"  our own curvature radius at equality = {ours:.3f} Mpc, so the parent's is <= "
      f"{a_eq_max/ours:.3f} of ours")
assert 0.01 < a_eq_max / ours < 1.0

print()
print("=" * 78)
print("PART 3 — THE BBN CHECK")
print("=" * 78)
print("  (i) the RATE: in radiation domination H^2 = (8 pi G/3) rho_r depends on T and the")
print("      relativistic degrees of freedom alone -- not on the universe's size.  At fixed eta the")
print("      yields do not know a_eq.")
print("  (ii) the CURVATURE term, relative to radiation, is (a/a_eq)(a/A):")
for T in [1.0, 0.1, 0.07]:
    x = 0.8 / (T * 1e6)
    ab = a_eq_max * x
    r = (ab / a_eq_max) * (ab / A_max)
    print(f"      T = {T:>5} MeV : ratio = {r:.2g}")
    assert r < 1e-10
print("  ** some fifteen orders below throughout nucleosynthesis, even at the tightest end of the")
print("     bound.  A closed universe small enough to satisfy the spectral bound is still, at MeV")
print("     temperatures, indistinguishable from a flat one. **")
print()
print("  VERDICT: consistent -- and consistent because the three constraints act on nearly")
print("  INDEPENDENT quantities: recollapse on the mass against alpha, the spectral bound on total")
print("  expansion past equality, BBN on eta and the rate at MeV temperatures.")
print()
print("  BOUND: the recollapse condition is computed for dust plus Lambda; radiation makes the ball")
print("  marginally easier to collapse and does not move the threshold at these radiation fractions.")
print("  The BBN comparison uses standard thermodynamics with our own T_eq, which the corpus's own")
print("  BBN account already assumes.")
print()
print("ALL PASS")
sys.exit(0)
