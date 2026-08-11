#!/usr/bin/env python3
"""
RECEIPT — P10 `sec:lock`, the coupled sector.

** CLAIM: THE DIRECT-INTEGRAL DECOMPOSITION OF THE COUPLED BOUNDARY OPERATOR NEEDS ONLY THAT THE
SPECTRUM OF $\\hat\\Gamma$ MEET BOTH SIDES OF $3/4$.  IT DOES NOT NEED A LOWER BOUND. **

The paper's paragraph asserted $\\hat\\Gamma$ 'bounded below by $\\gamma$' where it sets up the
straddle, and listed 'whether it is bounded below' among what is OPEN four hundred characters
later.  Both statements are correct of DIFFERENT operators -- the first of the leading-order
$\\hat\\Gamma=\\gamma+c\\sum_n\\hat\\pi_n^{2}$, the second of the complete one with the cubic and
higher self-interactions included -- and the qualification was missing.  ** This receipt shows the
repair costs the argument nothing, which is why it is a qualification and not a retraction. **

  PART 1  the leading-order operator: a sum of squares, so bounded below by gamma, unbounded above.
  PART 2  ** a complete operator that is UNBOUNDED BELOW and still straddles 3/4. **
  PART 3  ** the two spectral subspaces, both non-trivial in both cases -- which is all the
          decomposition uses. **

rc=0 on success.  Run: python3 P10_the_straddle_does_not_need_a_floor.py      (numpy)
"""
import sys

import numpy as np

print(__doc__.split("rc=0")[0])
GAMMA, C, THR = 0.25, 1.0, 0.75          # gamma <= 1/4 is the free scale factor's; 3/4 the threshold
K = np.linspace(0.0, 2.0, 4001)          # one mode's momentum, the representation in which pi^2 is
                                         # diagonal with eigenvalues k^2 >= 0

# ---------------------------------------------------------------- PART 1
print("=" * 78)
print("PART 1 — THE LEADING-ORDER OPERATOR")
print("=" * 78)
lead = GAMMA + C * K**2
print(f"  Gamma-hat_lead = gamma + c * pi^2      gamma = {GAMMA},  c = {C}")
print(f"  {'inf spec':>26} {lead.min():.12f}")
print(f"  {'sup spec on this grid':>26} {lead.max():.12f}")
assert abs(lead.min() - GAMMA) < 1e-12, "the infimum of a sum of squares over gamma is gamma"
assert lead.max() > THR
print(f"  ** bounded below by gamma:  {bool(lead.min() >= GAMMA - 1e-12)} **")
print(f"  ** unbounded above (grows as k^2):  {bool(np.all(np.diff(lead) >= -1e-15))} **")
print("  ⇒ the paper's clause is CORRECT of this operator, and it is proved by the form itself:")
print("    a sum of squares over a positive coefficient has spectrum in [gamma, oo).")

# ---------------------------------------------------------------- PART 2
print()
print("=" * 78)
print("PART 2 — A COMPLETE OPERATOR THAT IS UNBOUNDED BELOW")
print("=" * 78)
print("  The cubic and higher self-interactions enter at the same inverse-square order at the")
print("  origin and are not sign-definite, and they do not act alike on every channel.  Model the")
print("  worst case honestly: TWO channels, one the quadratic keeps and one the cubic takes over.")
LAM = 0.6
chA = GAMMA + C * K**2
chB = GAMMA + C * K**2 - LAM * K**3
full = np.concatenate([chA, chB])
print(f"    channel A:  gamma + c pi^2                   spec ⊂ [{chA.min():+.4f}, {chA.max():+.4f}]")
print(f"    channel B:  gamma + c pi^2 - lambda pi^3     spec ⊂ [{chB.min():+.4f}, {chB.max():+.4f}]"
      f"   (lambda = {LAM})")
print(f"  {'inf of the union':>26} {full.min():+.12f}")
print(f"  {'sup of the union':>26} {full.max():+.12f}")
assert full.min() < GAMMA - 1e-9, "the model must actually break the floor, or it shows nothing"
assert chB[-1] < chB[0], "channel B must be driven DOWN by the cubic at large momentum"
print(f"  ** bounded below by gamma:  {bool(full.min() >= GAMMA - 1e-12)}   (the floor is gone) **")
print("  *And it is gone unboundedly: -lambda k^3 beats +c k^2 for every lambda > 0 at large k, so")
print("   the model is not a tuned counterexample but the generic behaviour of a cubic term.*")

# ---------------------------------------------------------------- PART 3
print()
print("=" * 78)
print("PART 3 — THE TWO SPECTRAL SUBSPACES")
print("=" * 78)
print(f"  {'operator':>34} {'below 3/4':>12} {'at or above':>12} {'floor?':>8}")
rows = []
for name, spec in [("leading order", lead), ("complete (unbounded below)", full)]:
    sub, sup = int((spec < THR).sum()), int((spec >= THR).sum())
    rows.append((name, sub, sup, bool(spec.min() >= GAMMA - 1e-12)))
    print(f"  {name:>34} {sub:>12} {sup:>12} {str(rows[-1][3]):>8}")
for name, sub, sup, _ in rows:
    assert sub > 0, f"{name}: the limit-circle subspace must be non-trivial"
    assert sup > 0, f"{name}: the limit-point subspace must be non-trivial"
print()
print("  ** BOTH SUBSPACES ARE NON-TRIVIAL IN BOTH CASES. **")
print("  The decomposition -partial_x^2 + Gamma-hat/x^2 over the spectrum of Gamma-hat asks for")
print("  exactly this: essential self-adjointness on the fibres with Gamma-hat >= 3/4 (limit point),")
print("  a boundary condition on the fibres below (limit circle).  A spectral projection onto")
print("  {Gamma-hat < 3/4} exists whether or not the spectrum has a floor.")
print()
print("  ⇒⇒ ** SO THE REPAIR IS A QUALIFICATION: 'bounded below by gamma' belongs to the")
print("     leading-order operator, and the straddle stands on the two subspaces being occupied. **")
print("  ⌗ *What the floor WOULD bear on is the interacting theory's own definition -- whether the")
print("   tower has a ground state -- which is the frontier the same paragraph names, and which this")
print("   receipt does not touch.*")
print()
print("ALL PASS")
sys.exit(0)
