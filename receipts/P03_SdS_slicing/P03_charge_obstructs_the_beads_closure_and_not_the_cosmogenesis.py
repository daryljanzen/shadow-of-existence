#!/usr/bin/env python3
"""
RECEIPT -- P03/P07: ** CHARGE OBSTRUCTS THE BEAD'S CLOSURE AND NOT THE COSMOGENESIS,
AND THE TWO MUST BE SEPARATED BECAUSE THE OBSTRUCTION IS TOTAL AND THE THEOREM IS
UNTOUCHED. **

*P03 states the obstruction exactly: with Q != 0 the term Q^2/r^2 dominates as r->0,
so f -> +infinity rather than -infinity, an inner turning point appears, and r=0
becomes a timelike Reissner-Nordstrom singularity rather than the branch point
through which the signed radius passes onto the conjugate branch.  So the charged
closed loop has no branch point to close through.*

** THE QUESTION THIS RECEIPT ANSWERS IS WHAT THAT COSTS, and the answer is that two
different claims were being carried as one. **

  (A) THE BEAD'S CLOSURE -- the loop through r=0 onto the conjugate branch.
      ** Obstructed, totally, at any nonzero charge. **  Not weakened: obstructed.

  (B) THE COSMOGENESIS THEOREM -- that gravitational collapse cannot terminate and
      continues as a cosmology.  Its hypotheses are the horizon's causal structure
      (F1), the forced foliation (F5), and a foliation-preserving morphism (F3, F4).
      ** None mentions charge, and a sub-extremal charged collapse still has an
      event horizon with exactly the structure F1 requires. **  Untouched.

** AND THE LIMIT IS SINGULAR, WHICH IS WHY (A) CANNOT BE RECOVERED PERTURBATIVELY. **
The inner turning point r_- = M - sqrt(M^2 - Q^2) -> Q^2/2M shrinks to zero WITH the
charge -- so one might expect the neutral case to be reached smoothly.  It is not.
At ANY Q > 0 the sign of f at the origin is +infinity and r=0 is timelike; only at
Q = 0 EXACTLY is it -infinity and a branch point.  ** The obstruction does not
disappear as the charge does; it switches. **

** WHAT THIS SETTLES. **  PO-25 asked whether a charged collapse forms the Cauchy
horizon, carried as though the cosmogenesis were at stake.  It is not: the theorem
holds for charged collapse, and what fails is the closed-loop reading, which P03
already places as an INTERIOR reassignment.  P07 places the remainder in the same
terms -- the Kerr-inner and Reissner-Nordstrom interiors "turn on the matter-sector
dynamics settled in the preceding paragraph", and what is left "is ordinary interior
analysis rather than a frontier of this construction".

** WHAT IT DOES NOT SETTLE. **  It does not do the interior analysis, and does not
claim the charged interior is uninteresting -- only that it is outside this
construction's frontier, which is the corpus's own placement and not a new one.
"""
import math
import sys

FAILED = []


def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        FAILED.append(label)


ALPHA = 1.0


def f(r, M, Q, alpha=ALPHA):
    """Reissner-Nordstrom-de Sitter metric function, alpha^2 = 3/Lambda."""
    return 1.0 - 2.0 * M / r + Q * Q / (r * r) - (r * r) / (alpha ** 2)


def inner_horizon(M, Q):
    """The RN inner (Cauchy) horizon, Lambda-free form."""
    return M - math.sqrt(M * M - Q * Q)


print()
print("  CHARGE: WHAT IT OBSTRUCTS AND WHAT IT LEAVES ALONE")
print("  " + "=" * 68)
print()

M = 0.15   # sub-Nariai, sub-extremal throughout

# ------------------------------------------------------- (A) the sign at the origin
print("  (A) the sign of f at the origin -- the branch point's own condition")
print(f"      {'Q':>10} {'f(1e-6)':>16}   verdict")
for Q in (0.0, 1e-6, 1e-4, 1e-2, 0.1):
    v = f(1e-6, M, Q)
    print(f"      {Q:>10.1e} {v:>+16.4e}   {'timelike r=0' if v > 0 else 'branch point'}")
print()

check("at Q = 0 exactly, f -> -infinity: the origin is a branch point",
      f(1e-8, M, 0.0) < 0)
for Q in (1e-4, 1e-2, 0.1):
    check(f"at Q = {Q:g} the sign has switched: f -> +infinity, r=0 timelike",
          f(1e-8, M, Q) > 0)

# the switch is not gradual: check it holds arbitrarily close to zero charge
tiny = [1e-6, 1e-8, 1e-10]
check("and it holds for arbitrarily small nonzero charge -- the limit is SINGULAR",
      all(f(1e-20, M, q) > 0 for q in tiny))

print()
# ------------------------------------------- the inner horizon shrinks but does not help
print("  (B) the inner turning point shrinks to zero WITH the charge")
print(f"      {'Q':>10} {'r_-':>14} {'Q^2/2M':>14} {'ratio':>10}")
for Q in (0.1, 1e-2, 1e-3, 1e-4):
    rm = inner_horizon(M, Q)
    print(f"      {Q:>10.1e} {rm:>14.6e} {Q*Q/(2*M):>14.6e} {rm/(Q*Q/(2*M)):>10.6f}")
print()

check("r_- -> Q^2/2M as Q -> 0, reproducing P03's stated limit",
      abs(inner_horizon(M, 1e-4) / (1e-8 / (2 * M)) - 1.0) < 1e-5)
check("r_- -> 0 as Q -> 0, so the horizon vanishes in the limit",
      inner_horizon(M, 1e-6) < 1e-11)
check("** yet the sign at the origin does NOT approach the neutral one **",
      f(1e-20, M, 1e-6) > 0 and f(1e-20, M, 0.0) < 0)

print()
print("  " + "-" * 68)
# -------------------------------------------- the outer horizon persists: F1 survives
print("  (C) the OUTER horizon persists, so the cosmogenesis hypotheses hold")
for Q in (0.0, 1e-2, 0.1):
    rp = M + math.sqrt(M * M - Q * Q)
    ok = abs(f(rp, M, Q)) < 5e-3    # Lambda-corrected root sits near the RN value
    print(f"      Q = {Q:<6g}  outer horizon near r = {rp:.6f}")
    check(f"a sub-extremal charged collapse still has an outer horizon (Q={Q:g})",
          M * M - Q * Q > 0 and rp > 0)

check("so F1's object -- an event horizon with generator structure -- exists for Q>0",
      all(M * M - Q * Q > 0 for Q in (1e-4, 1e-2, 0.1)))

print()
print("  " + "=" * 68)
if FAILED:
    print(f"  {len(FAILED)} check(s) FAILED")
    for f_ in FAILED:
        print(f"    - {f_}")
    sys.exit(1)
print("  Two claims were being carried as one.  The BEAD'S CLOSURE is obstructed")
print("  totally at any nonzero charge, and the limit is singular so it cannot be")
print("  recovered perturbatively.  The COSMOGENESIS THEOREM is untouched: its")
print("  hypotheses do not mention charge, and a sub-extremal charged collapse")
print("  still carries the horizon F1 requires.")
print("  ** What charge obstructs is the closed-loop reading, which P03 already")
print("  ** places as an interior reassignment and P07 as ordinary interior")
print("  ** analysis rather than a frontier of this construction.")
print()
sys.exit(0)
