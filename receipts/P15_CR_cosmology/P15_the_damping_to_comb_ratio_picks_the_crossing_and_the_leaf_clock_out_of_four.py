#!/usr/bin/env python3
"""
RECEIPT -- P15: ** theta_D/theta_* SEPARATES THE FOUR (HANDOVER LOCUS x CLOCK) COMBINATIONS AND
PICKS EXACTLY ONE: THE CROSSING ON THE LEAF CLOCK, AT 1.022 OF THE CONTROL'S RATIO.  THE OTHER
THREE ARE 1.135, 1.353 AND 0.652. **

** ⇒ AND NEITHER CHOICE WAS MADE TO FIX THIS QUANTITY. **  The crossing was adopted because it is
where aH diverges and every mode is super-horizon, the leaf clock because node 66 (chat seat) ruled
ONE object for r_s and r_D both.  theta_D/theta_* is the ratio of the damping angle to the acoustic
angle -- it is not the comb, it is not the heights, and nothing in either decision was aimed at it.
** A 2.2% agreement from a quantity that was not consulted is evidence; a 2.2% agreement from a
quantity that was fitted is bookkeeping.  This is the first kind. **

Built r6760+cc66.5 (node 66, code seat), on `PO-13`, at node 66 (chat seat)'s work order
(message A item 3, narrowed by message B item 3 to "the crossing arm on the leaf clock only").

===================================================================================================
** WHAT IS BEING MEASURED, AND WHY IT IS A RATIO **
===================================================================================================

theta_* = r_s/D_M and theta_D = r_D/D_M, so ** theta_D/theta_* = r_D/r_s and D_M drops out. **
That matters: the CR arm's D_M is 13005 Mpc against the control's 13865, and a comparison of
theta_D alone would be reporting that difference rather than the damping.  The ratio is the
dimensionless thing the sky measures as "how far into the tail the peaks survive", and it is the
one quantity in this family that ** no configuration here was tuned on. **

  r_s = int c_s C/(a^2 H) da  from the handover to recombination
  r_D = sqrt( int [ (R^2/(1+R) + 8/9) / (6 (1+R) tau') ] C/(a^2 H) da )     -- the standard
        Silk integrand, with the opacity tau'(a) taken from `storyboard_receipts/RD_diffusion_direct.py`
        so the ionisation history is the corpus's own and not a fresh assumption.

** The four rows are (handover locus) x (clock), nothing else changed. **  The locus is either the
ONSET (z = 6761, the redshift solved so l_A hits LATARG) or the CROSSING (a -> 0, the branch point,
where aH diverges).  The clock is either L1, the radiation-free stacking rate that `sec:coherence`
assigns r_s AND r_D to and calls forced, or L2, the leaf rate that `sec:properframe`'s rate-rule
remark assigns "the plasma's sound horizon, its diffusion length" to.  ** Those two sentences are
the corpus contradicting itself, and this is the measurement that says which one the sky prefers. **

** COMPUTES: control at H0 = 67.40, Om = 0.3150, radiation IN the rate; CR arm at H0 = 73.00,
   Om = 0.3066, radiation OUT of the stacking rate and IN the leaf rate -- the instrument's own
   two-arm parameters, not new ones.  z_rec = 1089.9, Ombh2 = 0.0224, Yp = 0.2454,
   RB_REC = 31500 Ombh2 (2.7255/2.7)^-4 / (1+z_rec), onset z = 6761, crossing a0 = 1/(1+3e7) --
   every one of them read off `ACOUSTIC_two_arm.py`.  *** r_D here is integrated to A_REC, NOT to
   the visibility peak, so it is NOT the 7.64 Mpc the instrument's header prints; the two
   definitions differ and only one of them is used, in all four rows alike. *** **

rc=0 on success.  Run: python3 <this file>   (numpy, scipy; ~60 s)
"""
import os
import sys

import numpy as np

print(__doc__.split("rc=0")[0])
fail = []
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'storyboard_receipts'))
from RD_diffusion_direct import xe_history, n_H0_of, sigT, Mpc_m, xe_total   # noqa: E402

C = 299792.458
Z_REC = 1089.9
A_REC = 1.0 / (1.0 + Z_REC)
OMBH2 = 0.0224
YP = 0.2454
RB_REC = 31500 * OMBH2 / (2.7255 / 2.7) ** 4 / (1 + Z_REC)
WR = 4.15e-5


def build(H0, OM, radiation_in_stacking_rate):
    OR = WR / (H0 / 100) ** 2
    OL = 1.0 - OM
    def Hs(a):
        return H0 * np.sqrt(OM / a ** 3 + OL + (OR / a ** 4 if radiation_in_stacking_rate else 0.0))
    def Hl(a):
        return H0 * np.sqrt(OM / a ** 3 + OL + OR / a ** 4)
    zg, xeg = xe_history(lambda z: Hs(1 / (1 + z)) * 1e3 / Mpc_m, OMBH2, YP,
                         z_hi=3000., z_lo=80., n=6000)
    nH0 = n_H0_of(OMBH2, YP)

    def taup(a):
        """dtau/deta in 1/Mpc, from the corpus's own ionisation history."""
        z = 1.0 / a - 1.0
        xH = (float(np.interp(z, zg[::-1], xeg[::-1])) if (zg[-1] <= z <= zg[0])
              else (1.0 if z > zg[0] else float(xeg[-1])))
        return xe_total(z, xH, nH0, YP, helium=True) * nH0 / a ** 3 * sigT * a * Mpc_m

    def R(a):
        return RB_REC * a / A_REC

    # ** THE INTEGRALS ARE DONE ON A LOG-a GRID AND NOT WITH quad. **  quad on [a0, a_rec] with
    # a0 = 1/(1+3e7) spends its subdivisions on thirteen e-folds where the integrand is flat and
    # then runs out of them at recombination, where it is not -- it returns a roundoff warning and
    # a maximum-subdivisions warning on exactly the two rows that start at the crossing.  In log a
    # the integrand is smooth across the whole range and Simpson converges; the convergence is
    # CHECKED below rather than asserted.
    def integrate(f, a0, n):
        u = np.linspace(np.log(a0), np.log(A_REC), n)
        a = np.exp(u)
        return float(np.trapezoid(np.array([f(x) for x in a]) * a, u))

    def r_s(H, a0, n=6001):
        return integrate(lambda a: C / (a ** 2 * H(a) * np.sqrt(3 * (1 + R(a)))), a0, n)

    def r_D(H, a0, n=6001):
        def g(a):
            return ((R(a) ** 2 / (1 + R(a)) + 8.0 / 9.0)
                    / (6 * (1 + R(a)) * taup(a))) * C / (a ** 2 * H(a))
        return float(np.sqrt(integrate(g, a0, n)))

    # ** D_M IS DELIBERATELY NOT COMPUTED. **  theta_D/theta_* = r_D/r_s exactly, so D_M cancels;
    # computing it and dividing twice would only add its quadrature error to both sides.
    return dict(Hs=Hs, Hl=Hl, r_s=r_s, r_D=r_D)


CTL = build(67.40, 0.3150, True)
CR = build(73.00, 0.3066, False)
A_CROSS = 1.0 / (1.0 + 3.0e7)
A_ONSET = 1.0 / (1.0 + 6761.0)

ROWS = [
    ('control (LCDM; one rate, start a->0)',        CTL, 'Hs', A_CROSS),
    ('CR, ONSET handover   -- STACKING clock',      CR, 'Hs', A_ONSET),
    ('CR, ONSET handover   -- LEAF clock',          CR, 'Hl', A_ONSET),
    ('CR, CROSSING handover -- STACKING clock',     CR, 'Hs', A_CROSS),
    ('CR, CROSSING handover -- LEAF clock',         CR, 'Hl', A_CROSS),
]

print("=" * 99)
print("  theta_D / theta_* = r_D / r_s, EVERY COMBINATION OF HANDOVER LOCUS AND CLOCK")
print("=" * 99)
print(f"  {'case':>42} {'r_s Mpc':>9} {'r_D Mpc':>8} {'r_D/r_s':>9} {'vs control':>11}")
vals = {}
base = None
for nm, M, hk, a0 in ROWS:
    H = M[hk]
    rs_, rD_ = M['r_s'](H, a0), M['r_D'](H, a0)
    t = rD_ / rs_
    if base is None:
        base = t
    vals[nm] = (rs_, rD_, t, t / base)
    print(f"  {nm:>42} {rs_:>9.2f} {rD_:>8.3f} {t:>9.5f} {t / base:>10.4f}x")

print()
print("  ⌗ CONVERGENCE OF THE LOG-a QUADRATURE, on the row that starts deepest (the crossing)")
for n in (1501, 3001, 6001, 12001):
    t = CR['r_D'](CR['Hl'], A_CROSS, n) / CR['r_s'](CR['Hl'], A_CROSS, n)
    print(f"      n = {n:>6d}   r_D/r_s = {t:.6f}")
t_lo = CR['r_D'](CR['Hl'], A_CROSS, 3001) / CR['r_s'](CR['Hl'], A_CROSS, 3001)
t_hi = CR['r_D'](CR['Hl'], A_CROSS, 12001) / CR['r_s'](CR['Hl'], A_CROSS, 12001)
print(f"      ⇒ moved {abs(t_hi - t_lo) / t_hi * 100:.4f}% from n = 3001 to n = 12001")
if abs(t_hi - t_lo) / t_hi > 1e-3:
    fail.append("the log-a quadrature has not converged to 0.1% on the crossing row")

print()
print("  ⌗ AND THE STARTING POINT IS NOT DOING THE WORK: the crossing rows are re-run from")
print("    a0 = 1/(1+3e6) and 1/(1+3e8), a hundredfold range in the locus")
for z0 in (3.0e6, 3.0e8):
    a0 = 1.0 / (1.0 + z0)
    t = CR['r_D'](CR['Hl'], a0) / CR['r_s'](CR['Hl'], a0)
    print(f"      z_cross = {z0:>7.1e}   r_D/r_s = {t:.5f}   ({t / base:.4f}x control)")
t3e6 = CR['r_D'](CR['Hl'], 1 / (1 + 3.0e6)) / CR['r_s'](CR['Hl'], 1 / (1 + 3.0e6))
t3e8 = CR['r_D'](CR['Hl'], 1 / (1 + 3.0e8)) / CR['r_s'](CR['Hl'], 1 / (1 + 3.0e8))
if abs(t3e8 - t3e6) / t3e6 > 0.05:
    fail.append(f"r_D/r_s moved {abs(t3e8 - t3e6) / t3e6 * 100:.1f}% over a 100x range in the locus")

WIN = 'CR, CROSSING handover -- LEAF clock'
ratios = {nm: v[3] for nm, v in vals.items() if nm != ROWS[0][0]}
best = min(ratios, key=lambda k: abs(ratios[k] - 1.0))
print()
print("=" * 99)
print("  WHAT THE FOUR ROWS SAY")
print("=" * 99)
print(f"""
  ** THE WINNER IS NOT CLOSE. **  Distance from the control's ratio:

        CROSSING + LEAF      {abs(ratios[WIN] - 1) * 100:>6.1f}%      <- the two choices node 66 made, independently
        ONSET    + STACKING  {abs(ratios['CR, ONSET handover   -- STACKING clock'] - 1) * 100:>6.1f}%      <- the corpus as it stands
        ONSET    + LEAF      {abs(ratios['CR, ONSET handover   -- LEAF clock'] - 1) * 100:>6.1f}%
        CROSSING + STACKING  {abs(ratios['CR, CROSSING handover -- STACKING clock'] - 1) * 100:>6.1f}%

  ** AND THE TWO CHOICES ARE NOT SEPARABLE. **  Reading down the list: the crossing on the WRONG
  clock is worse than the onset on the wrong clock, and the leaf clock at the WRONG locus is the
  worst row of the four.  Neither choice helps on its own.  *** So this is not two improvements
  that happen to land together; it is one configuration, and the corpus's current pair
  (onset + stacking) is the second-best of four rather than the reasonable default it reads as. ***

  ⌗ ** AND THE 2.2% IS ENDPOINT-DEPENDENT, WHICH r6760+cc66.6 MEASURED AFTERWARDS. **  Every row
  here integrates r_D to A_REC.  Integrating instead to the COMPUTED VISIBILITY PEAK (z = 1093.8,
  0.36% away in redshift) moves this row to 0.9911 -- a 3.1-point swing, against a cosmological
  parameter budget of 0.02 points -- because r_D's integrand carries 1/tau' and tau' collapses
  exactly where the range ends.  ** The RANKING above survives that: the crossing on the leaf clock
  is closest on both endpoints and the other three are tens of points away on both, checked in
  `P15_the_damping_signature_error_budget_and_the_convention_dominates_it`.  The VALUE does not
  survive it and must be quoted with its endpoint named. **

  ⌗ ** WHAT THIS DOES NOT SAY. **  r_D/r_s agreeing with the control to 2.2% does not make the
  spectrum agree with the sky -- the crossing arm is still rejected at 35.5 per bin against the
  control's 2.10 (r6760+cc66.1), and the 700-1000 band is where that lives.  This measures ONE
  ratio and it is the ratio the damping tail's position is set by.  A configuration that got this
  wrong could not be right; getting it right is necessary and is not sufficient.
""")

if best != WIN:
    fail.append(f"the closest row is '{best}', not the crossing on the leaf clock")
if abs(ratios[WIN] - 1.0) > 0.05:
    fail.append(f"the crossing on the leaf clock is {abs(ratios[WIN] - 1) * 100:.1f}% off, not ~2%")
for nm in ratios:
    if nm != WIN and abs(ratios[nm] - 1.0) < 0.10:
        fail.append(f"'{nm}' is also within 10% -- the four rows do not separate")

print("=" * 99)
if fail:
    print("  FAILED:")
    for f in fail:
        print(f"    - {f}")
    sys.exit(1)
print("  ✓ ALL CHECKS PASSED")
print("=" * 99)
