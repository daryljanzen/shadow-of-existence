#!/usr/bin/env python3
"""
RECEIPT — P7 / P16: ** EVERY MODE IS SUPER-HORIZON AT THE BRANCH POINT, FOR EVERY WAVENUMBER THE
SKY CONTAINS — SO THE CROSSING'S SPECIES FILTER HAS NOTHING TO ACT ON, AND THE PASSAGE IS LOSSLESS
FOR EVERY SPECIES RATHER THAN FOR COLD ONES ALONE. **

Built r2376+c54.162, settling front #1 — the construction's recursion — which had headed the
programme's list for twelve revisions.

** THE TENSION THIS CLOSES. **  P7 gives two accounts of what the Euclidean segment does to a
perturbation, and they are not compatible as written:

  sec:lift-quantum  the kernel e^{-H|Delta eta|} "acts on OSCILLATORY content only: a frozen,
                    zero-frequency mode is a fixed point of the kernel.  And at the crossing no
                    mode is oscillating -- on the contracting leg aH grows without bound as
                    r -> 0, so the comoving horizon shrinks to zero and every mode exits it and
                    freezes first."
  sec:frontiers     the selection rule e^{-k c_s |Delta eta|} read at fixed k "makes it a
                    criterion on SPECIES: a pressureless component has c_s = 0 identically ... so
                    its crossing is exact ... while at the acoustic peak the exponent runs
                    ~1.6e2 c_s/c and the crossing can inherit perturbations from a cold species
                    and from NO OTHER."

** If every mode is already frozen, the second has nothing to bite on. **  The first account's
premise -- that every mode exits the comoving horizon before the branch point -- was asserted and
cited sideways, never computed.  It is computed here, on the progenitor's own exact interior.

  PART 1  ** THE MECHANISM, AND IT IS ONE LINE OF ASYMPTOTICS: |aH| = |a'/a| diverges as 1/x at
          the crunch while c_s SATURATES at 1/sqrt3, so c_s k/|aH| -> c_s k x -> 0 for EVERY k. **
  PART 2  ** THE FREEZE-OUT EPOCH x_f for each observed multipole: strictly positive throughout,
          so every mode freezes with conformal room to spare. **
  PART 3  ** THE CONSEQUENCE: the species criterion is vacuous at the crossing, and what the
          corpus advertised as a selection rule is not one. **

** SCOPE, STATED. **  This settles what the segment ACTS ON.  It does not compute the segment's
action on a frozen mode beyond P7's own fixed-point statement, and it says nothing about the
harmonic-basis question -- that is answered by reading rather than by arithmetic (P7's
correspondence is null-boundary to null-boundary "with no spacelike slice entering the map", so
there is no spacelike datum for a basis identification to be about).

rc=0 on success.  Run: python3 P16_every_mode_is_frozen_at_the_crossing.py   (numpy sympy scipy)
"""
import sys

import numpy as np
import sympy as sp
from scipy.optimize import brentq

print(__doc__.split("rc=0")[0])
fail = []

# the progenitor's exact interior at the determined composition
A, RHO = 2.0, 0.0539
B = RHO ** 2 * A ** 2 / 4
e = sp.symbols('e')
a_s = (A / 2) * (1 - sp.cos(e)) + sp.sqrt(B) * sp.sin(e)
a_n = sp.lambdify(e, a_s, 'numpy')
ap_n = sp.lambdify(e, sp.diff(a_s, e), 'numpy')
cs_n = sp.lambdify(e, sp.sqrt(sp.Rational(4, 3) * B / (3 * A * a_s + 4 * B)), 'numpy')
ETA_C = float(2 * np.pi - 2 * np.arctan(RHO))
ETA_T = float(np.pi - np.arctan(RHO))
SMAP = 2.750                                   # interior mode L -> observed multipole


def ratio(x, k):
    """c_s k / |aH| at conformal distance x before the crunch -- above 1 the mode oscillates"""
    eta = ETA_C - x
    return float(cs_n(eta)) * k / abs(ap_n(eta) / a_n(eta))


# =====================================================================
print("=" * 78)
print("PART 1 — THE MECHANISM: |aH| DIVERGES, c_s SATURATES")
print("=" * 78)
print(f"  the collapsing leg runs from turnaround eta = {ETA_T:.4f} to the crunch at "
      f"eta = {ETA_C:.4f}")
print(f"  near the crunch a -> (A rho/2) x, so |aH| = |a'/a| -> 1/x, while c_s -> 1/sqrt3 = "
      f"{1/np.sqrt(3):.5f}\n")
print(f"  {'x = eta_c - eta':>17} {'c_s':>9} {'|aH|':>12} {'|aH| . x':>10} "
      f"{'c_s k/|aH| at k=200':>21} {'state':>20}")
for x in (1.0, 0.3, 0.1, 0.03, 0.01, 3e-3, 1e-3, 1e-4, 1e-5):
    eta = ETA_C - x
    aH = abs(ap_n(eta) / a_n(eta))
    r = ratio(x, 200.0)
    print(f"  {x:>17.4g} {float(cs_n(eta)):>9.5f} {aH:>12.4g} {aH*x:>10.5f} {r:>21.4g} "
          f"{'SUB (oscillating)' if r > 1 else 'super (FROZEN)':>20}")
# the asymptotic statement, asserted rather than eyeballed
for x in (1e-3, 1e-4, 1e-5):
    prod = abs(ap_n(ETA_C - x) / a_n(ETA_C - x)) * x
    if abs(prod - 1.0) > 2e-2:
        fail.append(f"|aH| x -> 1 fails at x={x}: {prod:.4f}")
if abs(float(cs_n(ETA_C - 1e-5)) - 1 / np.sqrt(3)) > 1e-3:
    fail.append("c_s does not saturate at 1/sqrt3")
print("\n  ** |aH| x -> 1 and c_s -> 1/sqrt3, so c_s k/|aH| -> c_s k x -> 0 for EVERY k. **")
print("     *The comoving sound horizon shrinks to nothing at the branch point, and every mode,")
print("     however deep inside it began, is outside it by the time the crossing happens.*")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE FREEZE-OUT EPOCH, ACROSS THE WHOLE OBSERVED RANGE")
print("=" * 78)
print(f"  {'k':>8} {'ell = 2.75 k':>13} {'x_freeze':>12} {'as a fraction of the leg':>25}")
LEG = ETA_C - ETA_T
xs = []
for k in (10.0, 30.0, 80.0, 200.0, 500.0, 900.0):
    f = lambda x: ratio(x, k) - 1.0                                   # noqa: E731
    xf = brentq(f, 1e-12, LEG - 1e-9)
    xs.append((k, xf))
    print(f"  {k:>8.0f} {SMAP*k:>13.0f} {xf:>12.5g} {xf/LEG:>24.3%}")
    if not (0 < xf < LEG):
        fail.append(f"k={k} does not freeze on the leg")
    if ratio(xf / 10.0, k) >= 1.0:
        fail.append(f"k={k} is still oscillating a decade past its freeze-out")
print("\n  ** EVERY MODE IN THE OBSERVED RANGE FREEZES STRICTLY BEFORE THE CRUNCH, and stays")
print("     frozen: the ratio falls monotonically to zero once it has crossed. **")
# ** r3124: this gloss read "a fifth of a per cent" -- 0.2% -- against its OWN table two lines above,
#    which computes 0.065% of the leg remaining at ell = 2475.  Threefold out, and in the LESS
#    conservative direction, since a smaller margin is the harder case for the claim being made.  P7
#    quoted the gloss rather than the table and carried the error into a paper (corrected r3095). **
print("     *The highest mode tested, ell = 2475, still freezes with 0.065% of the leg to spare --")
print("      the figure the table above computes -- and the margin only grows as x -> 0.*")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — SO THE SPECIES CRITERION IS VACUOUS AT THE CROSSING")
print("=" * 78)
ALPHA_MPC = 5338.0
DETA = 3.32 * ALPHA_MPC
print(f"  P7's segment has conformal length |Delta eta| = 3.32 alpha = {DETA:.0f} Mpc, and its")
print(f"  selection rule is exp(-k c_s |Delta eta|).  At the first acoustic peak that exponent is")
K_PEAK = 0.02                                                          # 1/Mpc, first peak
for lbl, c in (("radiation, c_s = 1/sqrt3", 1 / np.sqrt(3)), ("dust, c_s = 0", 0.0)):
    print(f"     {lbl:>26}:  k c_s |Delta eta| = {K_PEAK*c*DETA:>8.1f}"
          f"   -> exp(-.) = {np.exp(-K_PEAK*c*DETA):.2e}")
print()
print("  ** BUT THE KERNEL ACTS ON OSCILLATORY CONTENT, AND PART 2 SHOWS THAT NO CONTENT ARRIVES")
print("     OSCILLATING.  P7's own sec:lift-quantum says a frozen zero-frequency mode is a FIXED")
print("     POINT of the kernel; PART 2 supplies the premise that sentence needed and never had. **")
print()
print("  ⇒ ** THE CROSSING IS LOSSLESS FOR EVERY SPECIES, NOT FOR COLD ONES ALONE, and P7's")
print("     'can inherit perturbations from a cold species and from no other' does not hold. **")
print("     *That REMOVES a selection rule the corpus advertised.  It is a loss of a claimed")
print("     prediction, not a gain, and it is recorded as one.*")
# the two halves of the criterion, pinned as computed here.  ** P7 quotes the exponent as
# ~1.6e2 c_s/c at the acoustic peak and does not state the k it used; at k = 0.02/Mpc and
# |Delta eta| = 3.32 alpha this file gets 204.6, i.e. the same order and not the same number.
# Pinning what IS computed rather than reverse-engineering P7's input. **
_warm = K_PEAK * (1 / np.sqrt(3)) * DETA
assert abs(_warm - 204.6) < 0.5, f"the warm exponent is {_warm:.1f}, not 204.6"
assert _warm > 50.0, "the warm exponent must be large enough for the filter to be a filter at all"
assert K_PEAK * 0.0 * DETA == 0.0, "a pressureless species must have a vanishing exponent"
print(f"  *P7 quotes ~1.6e2 c_s/c for this exponent without stating its k; at k = "
      f"{K_PEAK}/Mpc it is {_warm:.1f}.  Same order, different number, and the conclusion")
print("   below does not turn on which.*")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — every mode is frozen at the crossing, so the segment's species filter")
print("has nothing to act on and the passage is lossless for every species.")
print("=" * 78)
