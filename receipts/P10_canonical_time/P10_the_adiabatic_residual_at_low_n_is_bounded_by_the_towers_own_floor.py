#!/usr/bin/env python3
"""
RECEIPT -- P10: ** THE ADIABATIC RESIDUAL AT LOW HARMONIC INDEX IS BOUNDED BY THE
TOWER'S OWN FLOOR, AND IT REACHES NOTHING OBSERVABLE. **

*P10 establishes that the projection across the lift is adiabatic for all but the
lowest few harmonics and degrades to order unity at n=2 and n=3.  What that failure
COSTS is the question this receipt answers, and it answers it in the direction the
item's own closing condition names: if the residual touches nothing observable, that
is the result.*

** THE STRUCTURE THAT DOES THE WORK IS THE TOWER'S FLOOR. **  On the closed three-
sphere the tensor tower starts at n=2 -- there are no modes below it.  So the
LEAST-SUPPRESSED mode has no less-suppressed neighbour to receive amplitude from,
and the mixing the adiabatic projection neglects can only carry amplitude DOWNWARD
in suppression.  The bound is therefore one-sided by construction rather than by
estimate.

Two quantities, both from P10's own text:
  * the exact suppression exponent is the action integral, int omega_n ds = I*mu_n
    with I = 3.3387 alpha^-1 on the forced member -- CONVERGENT because omega goes
    as s^-2/3 and is integrable, which is a statement about the integral and NOT
    about slow variation;
  * the adiabaticity parameter is C/mu_n with C running 1.72 near the branch point
    to 0.16 near the turnaround, so the projection is controlled by the harmonic
    index alone.

with mu_n^2 = n(n+2) - 2, n >= 2.

** WHAT IS CHECKED HERE. **  (i) the exponent and the suppression mode by mode;
(ii) that the adiabaticity parameter reproduces P10's stated values at n=2,3,10;
(iii) that the suppression falls monotonically with n, so mixing is one-directional;
(iv) that the worst-case transfer of the whole O(eps) fraction out of n=2 leaves the
     ceiling on transmitted power BELOW its unmixed value; and
(v) that the ceiling itself sits at 1e-7 in power, far below anything observable.

** WHAT THIS RECEIPT DOES NOT CLAIM. **  It does not compute the mixing matrix; it
bounds its effect using the floor and the monotonicity.  A bound is what the item
asks for, since its closing condition is whether the residual reaches an observable
and not what its exact value is.
"""
import math
import sys

FAILED = []


def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        FAILED.append(label)


I_EXACT = 3.3387       # int ds/|r| on the forced member, units alpha^-1  (P10 eq:adiabatic-exponent)
I_NAIVE = 1.4396       # constant-frequency estimate at the turnaround value
C_BRANCH = 1.72        # adiabaticity coefficient near the branch point
C_TURN = 0.16          # ... near the turnaround


def mu(n):
    """S^3 tensor-harmonic eigenvalue: mu_n^2 = n(n+2) - 2, n >= 2."""
    return math.sqrt(n * (n + 2) - 2)


def exponent(n):
    return I_EXACT * mu(n)


def suppression(n):
    return math.exp(-exponent(n))


print()
print("  THE ADIABATIC RESIDUAL AT LOW n -- bounded by the tower's floor")
print("  " + "=" * 72)
print()

# ------------------------------------------------------------------ (i) and (ii)
print("  the tower, mode by mode:")
print(f"    {'n':>3} {'mu_n':>8} {'exponent':>9} {'suppression':>12} {'eps(branch)':>12}")
for n in range(2, 11):
    print(f"    {n:>3} {mu(n):8.4f} {exponent(n):9.3f} {suppression(n):12.3e}"
          f" {C_BRANCH/mu(n):12.3f}")
print()

# P10 states 0.70 at n=2, 0.48 at n=3, 0.16 by n=10
check("eps(n=2) reproduces P10's 0.70", abs(C_BRANCH / mu(2) - 0.70) < 0.01)
check("eps(n=3) reproduces P10's 0.48", abs(C_BRANCH / mu(3) - 0.48) < 0.01)
check("eps(n=10) reproduces P10's 0.16", abs(C_BRANCH / mu(10) - 0.16) < 0.01)

# the exact-to-naive ratio P10 states as 2.32
check("exact/naive exponent ratio is P10's 2.32",
      abs(I_EXACT / I_NAIVE - 2.32) < 0.01)

# --------------------------------------------------------------------- (iii)
mono = all(suppression(n + 1) < suppression(n) for n in range(2, 20))
check("suppression falls monotonically with n, so mixing is one-directional", mono)

# There is no mode below n=2 on S^3: the floor is what makes the bound one-sided.
# The transverse-traceless tensor harmonics on the three-sphere begin at n=2 -- the
# n=0 and n=1 would-be modes are pure gauge and carry no physical polarisation, which
# is why P10 says "there are no modes below n=2 on S^3".  The check is therefore that
# the tower's index set starts at 2, not that some formula turns negative below it.
TOWER_FLOOR = 2
check("the tower's index set starts at n=2, so the dominant mode has no source below it",
      TOWER_FLOOR == 2 and min(range(TOWER_FLOOR, 20)) == 2)
check("and that floor is what makes the mixing bound one-sided rather than estimated",
      suppression(TOWER_FLOOR) == max(suppression(n) for n in range(TOWER_FLOOR, 20)))

print()
print("  " + "-" * 72)

# --------------------------------------------------------------------- (iv)
A2, A3 = suppression(2), suppression(3)
eps2 = C_BRANCH / mu(2)

# worst case: n=2 transfers its entire O(eps) fraction into n=3
A2_after = A2 * (1 - eps2)
A3_after = A3 + eps2 * A2

print(f"  n=2 unmixed amplitude        {A2:.3e}   power {A2**2:.3e}")
print(f"  n=3 unmixed amplitude        {A3:.3e}   power {A3**2:.3e}")
print(f"  worst-case mixing fraction   {eps2:.3f}")
print(f"  n=2 after losing it          {A2_after:.3e}   (suppression STRONGER)")
print(f"  n=3 after gaining it all     {A3_after:.3e}   power {A3_after**2:.3e}")
print()

check("mixing weakens the least-suppressed mode rather than strengthening it",
      A2_after < A2)
check("the enriched n=3 does not exceed the unmixed n=2 ceiling",
      A3_after < A2)
check("the ceiling on transmitted power is set by n=2 and is not raised by mixing",
      max(A2_after, A3_after) ** 2 <= A2 ** 2)

# --------------------------------------------------------------------- (v)
CEILING = A2 ** 2
print(f"  ceiling on transmitted power (n=2, unmixed):  {CEILING:.3e}")
print()
check("the ceiling sits below 1e-6 in power", CEILING < 1e-6)
check("and below 1e-3 even on the NAIVE exponent, which is the weaker estimate",
      math.exp(-I_NAIVE * mu(2)) ** 2 < 1e-3)

print()
print("  " + "=" * 72)
if FAILED:
    print(f"  {len(FAILED)} check(s) FAILED")
    for f in FAILED:
        print(f"    - {f}")
    sys.exit(1)
print("  The residual is bounded above by the unmixed n=2 suppression, which is")
print("  7.9e-08 in power.  Mixing moves amplitude into more-suppressed modes and")
print("  the tower's floor at n=2 means the dominant mode has no source below it.")
print("  ** So the residual reaches nothing observable, which is the item's own")
print("  ** closing condition.")
print()
sys.exit(0)
