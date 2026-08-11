#!/usr/bin/env python3
"""
RECEIPT — P15 `sec:predictions` / `sec:amplitude`:
** THE DIAGONALITY OF THE CONTINUATION IS THE CONSTRUCTION'S TIME-REVERSAL SYMMETRY, AND THE SAME
INVARIANCE THAT FIXES THE PEAK HEIGHTS IS WHAT STOPS THE SCALE-INVARIANT SPECTRUM CROSSING. **

The falsifier left open by `P15_the_continuation_is_diagonal`: mixing would need a background
correction ODD in tau, with the Z_3 monodromy the named candidate.  It fires negative.

  PART 1  ** the exact factorisation r = A u^(2/3) g(u): all branching in u^(2/3), g EVEN **
  PART 2  ** the three sheets differ by a CONSTANT, so none has an odd part **
  PART 3  ** the conjugate branch is even too, and has no branch point at all **
  PART 4  ** the evenness IS r(-tau) = r(tau): time symmetry about the branch point **

rc=0 on success.  Run: python3 P15_the_evenness_is_the_time_symmetry.py    (sympy)
"""
import sys

import sympy as sp

print(__doc__.split("rc=0")[0])
u = sp.symbols('u')
w = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2

print("=" * 78)
print("PART 1 — THE FACTORISATION")
print("=" * 78)
h = sp.series(sp.sinh(u) / u, u, 0, 13).removeO()
assert not [n for n in range(1, 13, 2) if sp.simplify(h.coeff(u, n)) != 0]
assert sp.limit(sp.sinh(u) / u, u, 0) == 1
g = sp.expand(sp.series((sp.sinh(u) / u)**sp.Rational(2, 3), u, 0, 13).removeO())
odd_g = [n for n in range(1, 13, 2) if sp.simplify(g.coeff(u, n)) != 0]
print("  r^3 = A^3 sinh^2(u)  =>  r = A u^(2/3) g(u),  g = [sinh(u)/u]^(2/3)")
print(f"  sinh(u)/u is EVEN and equals 1 at u=0 (both asserted), so g is a power series in u^2:")
print(f"  ** odd powers in g through u^12: {odd_g} -- none **")
assert not odd_g
print("  and this is exact, not a truncation: log(sinh u/u) is analytic in u^2 near 0, two thirds")
print("  of it likewise, and the exponential of a series in u^2 is a series in u^2.")

print()
print("=" * 78)
print("PART 2 — THE THREE SHEETS")
print("=" * 78)
for j in range(3):
    prod = sp.expand(sp.simplify(w**j) * g)
    odd_j = [n for n in range(1, 11, 2) if sp.simplify(prod.coeff(u, n)) != 0]
    print(f"  sheet {j}: r = omega^{j} A u^(2/3) g(u);  odd powers in the correction: {odd_j}")
    assert not odd_j
print("  ** the sheet label is a CONSTANT multiplier and cannot change a parity. **")
print("     So the Z_3 monodromy -- the only route the previous receipt left -- is closed.")

print()
print("=" * 78)
print("PART 3 — THE CONJUGATE BRANCH")
print("=" * 78)
sh = sp.simplify(sp.sinh(u - sp.I * sp.pi / 2))
print(f"  half-period shift u -> u - i pi/2 :  sinh -> {sh},  so r ∝ -cosh^(2/3)(u)")
ch = sp.expand(sp.series(sp.cosh(u)**sp.Rational(2, 3), u, 0, 9).removeO())
odd_c = [n for n in range(1, 9, 2) if sp.simplify(ch.coeff(u, n)) != 0]
print(f"  ** odd powers in cosh^(2/3): {odd_c} -- none, and cosh^(2/3) is NON-ZERO at u=0, **")
print("     so the conjugate branch has no branch point: |r| has a smooth minimum, not a zero.")
assert not odd_c

print()
print("=" * 78)
print("PART 4 — THE EVENNESS IS THE TIME SYMMETRY")
print("=" * 78)
assert sp.simplify(sp.sinh(-u)**2 - sp.sinh(u)**2) == 0
print("  sinh^2(-u) = sinh^2(u), asserted.  As geometry: ** r(-tau) = r(tau). **")
print("  The cosmogenesis is TIME-SYMMETRIC about the branch point, and a time-symmetric background")
print("  cannot mix a growing mode with a decaying one, because mixing would distinguish a")
print("  direction of time that the background does not.")
print()
print("  ** AND P15 sec:amplitude ALREADY LEANS ON THIS INVARIANCE, one observable over: the peak")
print("     HEIGHTS follow from a driving amplitude 'exactly invariant under time reversal' and may")
print("     therefore be evaluated on the contracting side. **")
print("  => ONE SYMMETRY, TWO CONSEQUENCES, and the corpus had banked only the welcome one.")
print()
print("  BOUND: the leg is exactly even because it is the marginally-bound E=1 geodesic of an")
print("  exactly VACUUM SdS exterior.  A progenitor with real matter content -- pressure,")
print("  dissipation, anything carrying an arrow -- would not be, and that is where a mixing term")
print("  would have to come from.  ** This receipt does not exclude that; it locates it. **")
print()
print("ALL PASS")
sys.exit(0)
