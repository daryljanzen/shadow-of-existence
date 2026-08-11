#!/usr/bin/env python3
"""
RECEIPT — P16 (the collapse excursion): ** IN THE PROGENITOR INTERIOR THE DUST CONTENT IS THE EVEN
PART OF THE BACKGROUND AND THE RADIATION CONTENT IS EXACTLY THE ODD PART — AND RADIATION DOMINATES
AT THE BRANCH POINT. **

The interior this paper's excursion requires (it runs BBN there, so it has radiation) is a closed
FRW ball.  Its exact solution splits by species into the two parities, which matters because the
mode-mixing question at the branch point turns precisely on whether an odd part exists.

  PART 1  the exact closed dust+radiation solution, verified against its own Friedmann equation
  PART 2  ** dust -> even, radiation -> ODD, exactly and with no cross terms **
  PART 3  ** and radiation is the LEADING behaviour as a -> 0, since rho_r/rho_m ~ 1/a **

rc=0 on success.  Run: python3 P16_radiation_is_the_odd_part.py     (sympy)
"""
import sys

import sympy as sp

print(__doc__.split("rc=0")[0])
eta, A, B = sp.symbols('eta A B', positive=True)

print("=" * 78)
print("PART 1 — THE EXACT SOLUTION")
print("=" * 78)
a = (A / 2) * (1 - sp.cos(eta)) + sp.sqrt(B) * sp.sin(eta)
res = sp.simplify(sp.diff(a, eta)**2 - (A * a + B - a**2))
print("  closed FRW, dust + radiation, conformal time:  (da/deta)^2 = A a + B - a^2")
print(f"  a(eta) = (A/2)(1 - cos eta) + sqrt(B) sin eta      residual = {res}")
assert res == 0

print()
print("=" * 78)
print("PART 2 — THE PARITY SPLIT IS BY SPECIES")
print("=" * 78)
even = sp.simplify((a + a.subs(eta, -eta)) / 2)
odd = sp.simplify((a - a.subs(eta, -eta)) / 2)
print(f"  even part : {even}      <- the DUST term, entire")
print(f"  odd  part : {odd}      <- the RADIATION term, entire")
assert sp.simplify(even - (A / 2) * (1 - sp.cos(eta))) == 0
assert sp.simplify(odd - sp.sqrt(B) * sp.sin(eta)) == 0
print("  ** exact, with no cross terms: the dust content has no odd piece and the radiation")
print("     content has no even piece. **")

print()
print("=" * 78)
print("PART 3 — RADIATION LEADS AT THE BRANCH POINT")
print("=" * 78)
ser = sp.expand(sp.series(a, eta, 0, 4).removeO())
print(f"  a(eta) = {ser}")
print(f"     linear coefficient    = {sp.simplify(ser.coeff(eta, 1))}   (radiation)")
print(f"     quadratic coefficient = {sp.simplify(ser.coeff(eta, 2))}   (dust)")
assert sp.simplify(ser.coeff(eta, 1) - sp.sqrt(B)) == 0
assert sp.simplify(ser.coeff(eta, 2) - A / 4) == 0
print("  and independently of any expansion, rho_r/rho_m ~ a^-4 / a^-3 = 1/a -> infinity as a -> 0.")
print()
print("  ** SO AN INTERIOR WITH ANY RADIATION AT ALL IS RADIATION-DOMINATED IN ITS LAST MOMENTS,")
print("     AND ITS BACKGROUND IS ODD THERE AT LEADING ORDER. **")
print()
print("  BOUND: this is the interior at LEADING ORDER -- closed FRW, dust plus radiation, no")
print("  anisotropy, no dissipation.  What it establishes is the PARITY STRUCTURE and its species")
print("  assignment, which follows from the exact solution's form.  The SIZE of any resulting mode")
print("  mixing is not computed here.  ** And it does not overturn the vacuum-leg results: those")
print("  are exact statements about the marginally-bound geodesic, which is the dust law. **")
print()
print("ALL PASS")
sys.exit(0)
