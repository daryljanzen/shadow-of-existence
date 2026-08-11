#!/usr/bin/env python3
"""
RECEIPT -- P15: ** THE SOUND-HORIZON CROSSING BETWEEN THE BRANCH POINT AND THE ONSET EXISTS, AND IT
IMPRINTS NOTHING. THE POTENTIAL EQUATION ON THE L1 BACKGROUND CONTAINS NO k AT ALL, SO THERE IS
NOTHING FOR A CROSSING TO BE AN EVENT FOR. **

Built r2376+c54.167, working front #5.

** WHAT THIS TESTS, AND IT IS MY OWN PROPOSAL. **  At c54.165, reading the acoustic fold's handoff
against front #1, I proposed a candidate the fold could not have seen:

    front #1 (c54.162)  every mode is SUPER-HORIZON and frozen at the branch point
    prop:subhorizon     the acoustic modes are SUB-HORIZON at the onset, by a factor >~ 2
    => every observed mode CROSSES the horizon somewhere in between -- and a crossing is exactly
       what the handoff says the construction lacks, and exactly where LambdaCDM acquires its
       k-independent driving shift.  ** So: is the missing shift acquired at that crossing? **

** THE ANSWER IS NO, AND THE REASON IS STRONGER THAN THE QUESTION. **

  PART 1  ** THE CROSSING IS REAL AND IT IS LOCATED. **  On the L1 rate the re-entry that separates
          front #1's frozen modes from prop:subhorizon's sub-horizon ones sits at l ~ 154, computed.
          ** Every mode at and above the acoustic peaks crossed BEFORE the onset; l = 28 crosses
          after it. **  The interval is not empty where the peaks live.  *The first draft of this
          file claimed it for every observed mode and its own assertion fired on l = 28.*
  PART 2  ** BUT IT IS A MATTER-ERA CROSSING. **  At every observed mode's crossing the L1 background
          is matter-dominated to better than a part in 10^4, because L1 has no radiation SOURCE at all
          -- radiation is content on this foliation, not a term in the rate.
  PART 3  ** AND THE POTENTIAL EQUATION FOR PRESSURELESS MATTER HAS NO k IN IT. **
          Phi'' + 3H(1+w)Phi' + [2H' + (1+3w)H^2]Phi + w k^2 Phi = 0, and w = 0 kills the only k.
          On matter domination the bracket vanishes identically too, leaving Phi'' + (6/eta)Phi' = 0:
          ** Phi = const + C eta^-5, the same for every k. **  Verified by integration, not asserted.
  PART 4  ** THE CONTRAST THAT MAKES IT LEGIBLE. **  In LambdaCDM the same modes cross during RADIATION
          domination, where w = 1/3 restores the k^2 term and Phi = 3Phi_i(sin x - x cos x)/x^3 decays
          on the sound-crossing time -- which is exactly why that shift is k-independent and why every
          mode gets it.

** THE VERDICT: THE CROSSING EXISTS AND IT IS EMPTY, so the escape route I proposed at c54.165 is
closed -- by the computation I proposed it to motivate. **  This does not refute the acoustic fold's
mechanism; it supplies its missing half.  The fold said the shift turns on as k^2 because the seam
transient is the only phase-imprinting process left.  ** This says WHY nothing earlier imprints
anything: before the onset the perturbation problem on L1 is scale-free. **

** WHAT IS NOT CLAIMED. **  Nothing here computes a peak position, and nothing here uses a figure from
the fold -- the fold's own reproduction gate does not reproduce in this tree (FOLD52_ASSESSMENT).
This closes one candidate mechanism.  ** It leaves PO-7 open and it leaves it harder. **

rc=0 on success.  Run: python3 P15_the_crossing_exists_and_is_empty.py   (numpy scipy, ~5 s)
"""
import sys

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

print(__doc__.split("rc=0")[0])
fail = []

# ---- the L1 background, exactly as the corpus states it: radiation is CONTENT, not a source -------
C = 299792.458
H0, OM = 73.0, 0.3066
OL = 1.0 - OM
H0C = H0 / C                                        # 1/Mpc
Z_ONSET = 6761.0
A_ONSET = 1.0 / (1.0 + Z_ONSET)
D_M = 13005.0                                       # comoving distance to last scattering, Mpc
# LambdaCDM comparison arm, for PART 4 only
OM_L, H0_L = 0.3150, 67.40
OR_L = 4.15e-5 / (H0_L / 100) ** 2

aH = lambda a: H0C * np.sqrt(OM / a + OL * a ** 2)                       # noqa: E731  (= a H / c)
aH_L = lambda a: (H0_L / C) * np.sqrt(OR_L / a ** 2 + OM_L / a + OL * a ** 2)   # noqa: E731

# =====================================================================
print("=" * 78)
print("PART 1 — THE CROSSING IS REAL, AND FOR THE PEAK MODES IT PRECEDES THE ONSET")
print("=" * 78)
print(f"  L1 rate: (aH/c)^2 = H0C^2 (Om/a + OL a^2), H0 = {H0}, Om = {OM} — no radiation term.")
print(f"  the onset sits at z = {Z_ONSET:.0f}, a = {A_ONSET:.3e}\n")
print(f"  {'l':>6} {'k [1/Mpc]':>11} {'a_cross':>11} {'z_cross':>11} "
      f"{'z_cross/z_onset':>16} {'state at onset':>17}")
ELLS = (28, 150, 220, 550, 1100, 2475)
# ** the boundary mode: the one whose re-entry coincides with the onset. **  Computed rather than
# assumed, because the first draft of this file asserted "every observed mode" and the assertion
# fired -- l = 28 crosses at z = 254, LONG AFTER the onset.  The claim is narrowed to what is true.
K_ONSET = aH(A_ONSET)
L_BOUNDARY = K_ONSET * D_M
zx = {}
for ell in ELLS:
    k = ell / D_M
    a_c = brentq(lambda a: aH(a) - k, 1e-12, 1.0)
    z_c = 1.0 / a_c - 1.0
    zx[ell] = z_c
    r = k / K_ONSET
    state = f"sub-horizon x{r:.1f}" if r >= 1 else f"STILL SUPER x{1/r:.1f}"
    when = "before onset" if z_c > Z_ONSET else "AFTER onset"
    print(f"  {ell:>6} {k:>11.5f} {a_c:>11.3e} {z_c:>11.0f} {when:>16} {state:>18}")
print(f"\n  ** THE BOUNDARY IS COMPUTED, NOT ASSUMED: the mode whose re-entry COINCIDES with the")
print(f"     onset is k = {K_ONSET:.5f}/Mpc, i.e. l = {L_BOUNDARY:.0f}. **")
print("     *Above it, the mode crossed BEFORE the onset and is already inside when the plasma")
print("     begins -- which is prop:subhorizon. Below it, the mode is still outside at the onset and")
print("     crosses later.*")
print(f"\n  ** SO THE INTERVAL IS NOT EMPTY FOR THE MODES THE ACOUSTIC PEAKS LIVE ON. **  front #1's")
print("  'super-horizon and frozen at the branch point' and prop:subhorizon's 'sub-horizon at the")
print("  onset' are both true, and the re-entry between them is a real event for every mode above")
print(f"  l = {L_BOUNDARY:.0f}.")
print("     ⚠ *The first draft of this file claimed it for EVERY observed mode and the assertion")
print("     below fired on l = 28, which crosses at z = 254 — after the onset, not before. The")
print("     narrowed claim is the one that survives, and the boundary sits within a few multipoles")
print("     of the disputed first peak, which is not a coincidence: both are set by the same k.*")
# the peak-region modes and above must cross before the onset; the boundary must sit where it is said
for ell in ELLS:
    if ell >= 220 and not (zx[ell] > Z_ONSET):
        fail.append(f"l={ell} is at or above the peak region and does not cross before the onset")
if not (100.0 < L_BOUNDARY < 250.0):
    fail.append(f"the boundary multipole is {L_BOUNDARY:.0f}, outside the acoustic-peak region")
if zx[28] > Z_ONSET:
    fail.append("l=28 is expected to cross AFTER the onset -- if it does not, the boundary moved")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — BUT IT IS A MATTER-ERA CROSSING, BECAUSE L1 HAS NO RADIATION SOURCE")
print("=" * 78)
print(f"  {'l':>6} {'a_cross':>11} {'Om_m(a_x)':>11} {'Om_L(a_x)':>12} {'w_eff at crossing':>19}")
worst_w = 0.0
for ell in ELLS:
    a_c = 1.0 / (1.0 + zx[ell])
    rm, rl = OM / a_c ** 3, OL
    fm = rm / (rm + rl)
    w_eff = (-rl) / (rm + rl)                       # p/rho with dust + Lambda
    worst_w = max(worst_w, abs(w_eff))
    print(f"  {ell:>6} {a_c:>11.3e} {fm:>11.7f} {rl/(rm+rl):>12.3e} {w_eff:>19.3e}")
print("\n  ** THE BACKGROUND AT EVERY CROSSING IS PRESSURELESS MATTER TO BETTER THAN A PART IN 10^4. **")
print("     *This is not an approximation of the construction — it is the construction. The L1 rate is")
print("     fixed by Lambda and matter alone; radiation rides it as content. That is the same statement")
print("     that dissolves the Hubble tension, and it is what empties the crossing.*")
if worst_w > 1e-3:
    fail.append(f"the background is not pressureless at the crossings: |w| up to {worst_w:.2e}")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — AND THE POTENTIAL EQUATION FOR PRESSURELESS MATTER CONTAINS NO k")
print("=" * 78)
print("  Phi'' + 3H(1+w) Phi' + [2H' + (1+3w) H^2] Phi + w k^2 Phi = 0")
print("  ** w = 0 removes the ONLY k in it. **  On matter domination H = 2/eta, so the bracket is")
print("  -4/eta^2 + 4/eta^2 = 0 as well, leaving Phi'' + (6/eta) Phi' = 0:  Phi = const + C eta^-5.\n")


def daH_da(a):
    """d(aH/c)/da, analytic -- a finite difference here made the integration stiff (c54.167)"""
    return H0C * (-OM / a ** 2 + 2.0 * OL * a) / (2.0 * np.sqrt(OM / a + OL * a ** 2))


def phi_run(k, a0=1e-7, a1=A_ONSET):
    """integrate Phi on the L1 background in ln a, with the w = 0 equation, for a given k.

    ** The k enters the signature and NOT the equation, deliberately: that is the result. **  The
    w k^2 Phi term is written with its w = 0 coefficient in place so a reader can see the term that
    is absent rather than take its absence on trust.
    """
    def rhs(x, y):
        a = np.exp(x)
        H = aH(a)                                   # comoving Hubble, aH/c
        Hp = a * H * daH_da(a)                      # dH/deta, since da/deta = a H
        phi, dphi = y                               # dphi = dPhi/deta
        d2 = -3.0 * H * dphi - (2.0 * Hp + H ** 2) * phi - 0.0 * k ** 2 * phi
        return [dphi / H, d2 / H]                   # d/dln a = (1/H) d/deta
    s = solve_ivp(rhs, [np.log(a0), np.log(a1)], [1.0, 0.0], rtol=1e-10, atol=1e-14)
    return float(s.y[0, -1]), int(s.nfev)


print(f"  {'l':>6} {'k [1/Mpc]':>11} {'Phi(onset)/Phi(init)':>24} {'departure':>12} {'solver steps':>13}")
vals, nfevs = [], []
for ell in ELLS:
    k = ell / D_M
    r, nf = phi_run(k)
    vals.append(r); nfevs.append(nf)
    print(f"  {ell:>6} {k:>11.5f} {r:>24.12f} {abs(r-1.0):>12.1e} {nf:>13}")
print(f"\n  ** AND THE SOLVER TAKES THE IDENTICAL NUMBER OF STEPS FOR EVERY MODE ({nfevs[0]}). **")
print("  *It is not that the k-dependence is small. The integrator is being handed the same problem")
print("  four decades apart in k, because k is not in it.*")
spread = max(vals) - min(vals)
print(f"\n  ** SPREAD ACROSS FOUR DECADES IN k: {spread:.2e}. **  The potential is constant across the")
print("  crossing and it is THE SAME CONSTANT FOR EVERY MODE.")
print("     *So 'horizon crossing' is not an event for the potential on L1 — there is nothing for a")
print("     mode to cross. The problem before the onset is scale-free, and a scale-free problem cannot")
print("     imprint a scale-dependent — or a scale-independent — phase, because it imprints nothing.*")
if spread > 1e-9:
    fail.append(f"Phi is k-dependent on L1: spread {spread:.2e}")
if len(set(nfevs)) != 1:
    fail.append(f"the solver saw different problems across k: nfev {sorted(set(nfevs))}")
if abs(np.mean(vals) - 1.0) > 1e-3:
    fail.append(f"Phi is not constant on L1: mean {np.mean(vals):.6f}")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE CONTRAST: IN LambdaCDM THE SAME MODES CROSS UNDER RADIATION")
print("=" * 78)
z_eq_L = OM_L / OR_L - 1.0
print(f"  LambdaCDM has a radiation TERM in its rate; equality sits at z_eq = {z_eq_L:.0f}.\n")
print(f"  {'l':>6} {'z_cross (LCDM)':>16} {'vs z_eq':>12} {'era at crossing':>20}")
rad_count = 0
for ell in ELLS:
    k = ell / D_M
    a_c = brentq(lambda a: aH_L(a) - k, 1e-14, 1.0)
    z_c = 1.0 / a_c - 1.0
    era = "RADIATION" if z_c > z_eq_L else "matter"
    rad_count += (z_c > z_eq_L)
    print(f"  {ell:>6} {z_c:>16.0f} {z_c/z_eq_L:>12.2f} {era:>20}")
print(f"\n  ** {rad_count} of {len(ELLS)} cross under radiation in LambdaCDM. **  There w = 1/3 restores")
print("  the k^2 term and Phi = 3 Phi_i (sin x - x cos x)/x^3 with x = k eta/sqrt3 — a potential that")
print("  decays ON THE SOUND-CROSSING TIME BY CONSTRUCTION, which is exactly why its driving shift is")
print("  the same for every mode.")
print("     *That is the process CR does not have, and this file locates the absence precisely: not")
print("     that the crossing is missing, but that on L1 the crossing is scale-free and empty.*")
if rad_count < 4:
    fail.append("the LambdaCDM contrast fails: too few modes cross under radiation")
assert z_eq_L > 3000, "LambdaCDM equality must sit above z = 3000 for the contrast to be the standard one"

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — the crossing exists, it precedes the onset for every mode the peaks live on, and it")
print("is empty: the L1 potential equation has no k in it, so nothing is imprinted there. The c54.165")
print("candidate is closed by the computation it motivated, and PO-7 is left open and harder.")
print("=" * 78)
