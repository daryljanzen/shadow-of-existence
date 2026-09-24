#!/usr/bin/env python3
"""
RECEIPT -- P15: ** NODE 66 (CHAT SEAT) RULED ONE CLOCK, THE LEAF CLOCK, FOR r_s AND r_D BOTH.  THIS
IS WHAT THAT COSTS THE DESI DR2 RESULT.  ** THE H0-DISSOLUTION SURVIVES -- 0.88 PER dof, FLAT TO
TWO DECIMALS FROM H0 = 70 TO 80 -- BUT NOT BY THE DERIVATION THE PAPER GIVES, AND THE PRICE IS THE
ONSET: ITS rho_r/rho_m FALLS FROM 51.0 TO 5.8 ACROSS THAT SAME H0 RANGE, AGAINST THE 1.7 THE
STACKING RULER PUTS IT AT, SO "THE ONSET IS WHERE RADIATION STOPS MATTERING" NO LONGER NAMES ONE
PLACE. **

** ⇒ OUTCOME (a) OF THE THREE THE ORDER NAMED, WITH A PRICE -- not (b), not (c). **

Built r6760+cc66.4 (node 66, code seat), on `PO-13`, at node 66 (chat seat)'s work order:
"redo the DESI DR2 confrontation and the acoustic angle with r_s as the LEAF accumulation, on the
control and on the crossing arm, scanning H0, and report chi^2/dof and the preferred H0 on each
ruler".

===================================================================================================
** WHY THE TWO RULERS ARE TWO RULERS, AND WHY THIS WAS NOT A CHOICE ANYONE MADE ON PURPOSE **
===================================================================================================

`ACOUSTIC_two_arm.py` has carried two sound horizons since it was written.  `rs_from` integrates
c_s/(a^2 H) on the ** STACKING rate ** (L1, radiation-free) and is the comoving ruler that
l_A = pi D_M / r_s reports; `sound_phase` integrates on the ** LEAF rate ** (L2, radiation
included) and is what the oscillator's phase actually runs on.  At the physical onset the two
differ by 1.286.  ** Nothing in the code was wrong: the two objects are two different integrals
with two different jobs. **  What was wrong was the corpus's account of which is which --
`sec:tensions` and `sec:coherence` put r_s and r_D on the stacking rate, `sec:properframe`'s
rate-rule remark puts "the plasma's sound horizon, its diffusion length" on the leaf.

Node 66 (chat) adjudicated it to ** ONE object on the LEAF clock ** and asked what that costs.
`LEAFSCALES=1` is the switch that does it in the instrument; this receipt does the cosmology side,
where the stacking ruler is what the published DESI result rests on.

  PART 1  ** THE STACKING RULER, REPRODUCED. **  The banked receipt's own numbers, recomputed
          here: Om = 0.3066, z_onset = 6764, chi^2 = 12.01 on 12 dof -- and flat in H0 to every
          digit printed, which IS the dissolution as the paper derives it.
  PART 2  ** THE LEAF RULER WITH NO ONSET. **  r_s accumulated from the deep radiation era on the
          leaf rate, which is what "the plasma's sound horizon" means if the onset is not a locus
          of it.  This is the case that would have been outcome (c).
  PART 3  ** THE LEAF RULER WITH THE ONSET RETAINED. **  z_onset re-solved from theta_*(leaf) at
          each H0, then BAO.  ** This is the case that decides, and it is (a). **
  PART 4  ** THE ACOUSTIC ANGLE ON ITS OWN, ** independent of BAO, as a second determination.
  PART 5  ** WHAT IT COSTS, stated as a number and not as a caveat. **

** COMPUTES: the DESI DR2 BAO likelihood (arXiv:2503.14738 Table IV, 13 measurements), at
   THETA_OBS = 0.0104085, z_rec = 1090.0, z_drag = 1059.94, wb = 0.02237, wg = 2.47e-5,
   wr = 4.15e-5 -- every one of them the value `hubble_build/desi_dr2_confrontation.py` already
   uses, so PART 1 is a reproduction and not a re-derivation.  *** Om is FITTED at each H0 and on
   each ruler; it is not pinned.  The LEAF rate's radiation density is wr/h^2, so it moves with H0
   -- which is the whole reason the leaf ruler is not H0-free the way the stacking ruler is. *** **

rc=0 on success.  Run: python3 <this file>   (numpy, scipy; ~90 s)
"""
import sys

import numpy as np
from scipy.optimize import brentq, minimize_scalar

print(__doc__.split("rc=0")[0])
fail = []
trapz = np.trapezoid
c = 299792.458

# ---- DESI DR2 BAO, Table IV (arXiv:2503.14738), verbatim from hubble_build/desi_dr2_confrontation.py
DESI_ANISO = [(0.510, 13.588, 0.167, 21.863, 0.425, -0.459),
              (0.706, 17.351, 0.177, 19.455, 0.330, -0.404),
              (0.934, 21.576, 0.152, 17.641, 0.193, -0.416),
              (1.321, 27.601, 0.318, 14.176, 0.221, -0.434),
              (1.484, 30.512, 0.760, 12.817, 0.516, -0.500),
              (2.330, 38.988, 0.531, 8.632, 0.101, -0.431)]
DESI_ISO = [(0.295, 7.942, 0.075)]
NDATA = 2 * len(DESI_ANISO) + len(DESI_ISO)            # 13
NDOF = NDATA - 1                                       # one fitted Om

WB, WG, WR = 0.02237, 2.47e-5, 4.15e-5
R0 = 3 * WB / (4 * WG)
ZREC, ZDRAG = 1090.0, 1059.94
THETA_OBS = 0.0104085


def cs(z):
    return c / np.sqrt(3 * (1 + R0 / (1 + z)))


def E_stack(z, Om, h):
    """L1, the foliation-stacking rate: RADIATION-FREE by construction, so h does not enter."""
    return np.sqrt(Om * (1 + z) ** 3 + (1 - Om))


def E_leaf(z, Om, h):
    """L2, the leaf rate: the same background WITH its radiation, at w_r = 4.15e-5."""
    return np.sqrt(Om * (1 + z) ** 3 + (WR / h ** 2) * (1 + z) ** 4 + (1 - Om))


def D_M(z, H0, Om, E, n=4000):
    zz = np.linspace(0, z, n)
    return trapz(c / (H0 * E(zz, Om, H0 / 100)), zz)


def D_H(z, H0, Om, E):
    return c / (H0 * E(z, Om, H0 / 100))


def D_V(z, H0, Om, E):
    return (z * D_M(z, H0, Om, E) ** 2 * D_H(z, H0, Om, E)) ** (1 / 3)


def r_snd(H0, Om, z_hi, z_lo, E, n=60000):
    u = np.linspace(np.log(1 + z_lo), np.log(1 + z_hi), n)
    z = np.exp(u) - 1
    return trapz(cs(z) / (H0 * E(z, Om, H0 / 100)) * (1 + z), u)


def chi2_bao(H0, Om, rd, E):
    x2 = 0.0
    for z, dm, sdm, dh, sdh, rho in DESI_ANISO:
        r = np.array([D_M(z, H0, Om, E) / rd - dm, D_H(z, H0, Om, E) / rd - dh])
        cov = np.array([[sdm ** 2, rho * sdm * sdh], [rho * sdm * sdh, sdh ** 2]])
        x2 += r @ np.linalg.solve(cov, r)
    for z, dv, sdv in DESI_ISO:
        x2 += ((D_V(z, H0, Om, E) / rd - dv) / sdv) ** 2
    return float(x2)


def z_onset_of(H0, Om, E):
    """theta_*(z_onset) = THETA_OBS.  ** BRACKET (1500, 5e6), r6760+cc66.3. **  On the stacking
    ruler the root is 6764 and the old 5e4 ceiling was never near it; on the LEAF ruler it is
    6.16e4 at H0 = 73 and runs to ~5e6 at H0 = 67.4, so the old bracket turned a reachable root
    into 'f(a) and f(b) must have different signs'.  theta_* is monotone in z_onset, so widening
    cannot find a different root."""
    return brentq(lambda zo: r_snd(H0, Om, zo, ZREC, E) / D_M(ZREC, H0, Om, E) - THETA_OBS,
                  1500., 5.0e6)


def fit_Om(H0, E, onset=True, z_hi_fixed=1.0e8):
    """Best-fit Om at this H0 on this ruler, and everything that goes with it."""
    def f(Om):
        try:
            if onset:
                zo = z_onset_of(H0, Om, E)
                return chi2_bao(H0, Om, r_snd(H0, Om, zo, ZDRAG, E), E)
            return chi2_bao(H0, Om, r_snd(H0, Om, z_hi_fixed, ZDRAG, E), E)
        except Exception:
            return 1.0e9
    r = minimize_scalar(f, bounds=(0.22, 0.42), method='bounded')
    if r.fun > 1.0e8:
        return None
    Om = float(r.x)
    zo = z_onset_of(H0, Om, E) if onset else float('nan')
    rd = r_snd(H0, Om, zo if onset else z_hi_fixed, ZDRAG, E)
    zeq = Om / (WR / (H0 / 100) ** 2) - 1.0
    return dict(H0=H0, Om=Om, z_onset=zo, r_d=float(rd), chi2=float(r.fun),
                rho_ratio=(1 + zo) / (1 + zeq) if onset else float('nan'), z_eq=zeq)


H0S = (63.0, 67.4, 70.0, 73.0, 76.0, 80.0)
HDR = (f"  {'H0':>6} {'Om fit':>8} {'z_onset':>10} {'rho_r/rho_m':>12} {'r_d Mpc':>9} "
       f"{'chi2':>8} {'/12 dof':>8}")


def row(r):
    if r is None:
        return "   theta_* is unreachable on this ruler at this H0"
    zo = f"{r['z_onset']:>10.0f}" if np.isfinite(r['z_onset']) else f"{'--':>10}"
    rr = f"{r['rho_ratio']:>12.2f}" if np.isfinite(r['rho_ratio']) else f"{'--':>12}"
    return (f"  {r['H0']:>6.1f} {r['Om']:>8.4f} {zo} {rr} {r['r_d']:>9.2f} "
            f"{r['chi2']:>8.2f} {r['chi2'] / NDOF:>8.2f}")


print("=" * 99)
print("  PART 1 -- ** THE STACKING RULER: THE PUBLISHED RESULT, RECOMPUTED HERE **")
print("=" * 99)
print("  The radiation-free rate factors H0 out of D_M, D_H and r_d alike, so the BAO ratios")
print("  depend on the dimensionless Om ALONE.  ** That is the dissolution: the SAME fit at every")
print("  H0, the local 73 included. **")
print(HDR)
stack = [fit_Om(H0, E_stack) for H0 in H0S]
for r in stack:
    print(row(r))
s73 = [r for r in stack if r['H0'] == 73.0][0]
if abs(s73['Om'] - 0.3066) > 0.002:
    fail.append(f"stacking Om = {s73['Om']:.4f}, banked 0.3066")
if abs(s73['z_onset'] - 6764) > 30:
    fail.append(f"stacking z_onset = {s73['z_onset']:.0f}, banked 6764")
if abs(s73['chi2'] - 12.01) > 0.35:
    fail.append(f"stacking chi2 = {s73['chi2']:.2f}, banked 12.01")
spread = max(r['chi2'] for r in stack) - min(r['chi2'] for r in stack)
print(f"\n  ⌗ chi^2 spread across H0 = 63 to 80:  {spread:.4f}   "
      f"(the dissolution: H0 is not a parameter of this fit)")
if spread > 0.05:
    fail.append(f"the stacking ruler's chi2 moved by {spread:.4f} across H0 -- it must not move")

print()
print("=" * 99)
print("  PART 2 -- ** THE LEAF RULER WITH NO ONSET: r_s ACCUMULATED FROM THE DEEP RADIATION ERA **")
print("=" * 99)
print("  This is the reading on which the onset is not a locus of the sound horizon at all.  ** It")
print("  is ordinary LCDM sound-horizon bookkeeping on a CR background, and it re-pins H0. **")
print(HDR)
leaf_noonset = [fit_Om(H0, E_leaf, onset=False) for H0 in H0S]
for r in leaf_noonset:
    print(row(r))
best_no = min(leaf_noonset, key=lambda r: r['chi2'])
fine = [fit_Om(H0, E_leaf, onset=False) for H0 in np.arange(66.0, 72.01, 0.5)]
best_fine = min(fine, key=lambda r: r['chi2'])
print(f"\n  ⌗ preferred H0 on this ruler = {best_fine['H0']:.2f}  "
      f"(chi^2/dof = {best_fine['chi2'] / NDOF:.2f}),  against H0 = 73 at "
      f"{[r for r in leaf_noonset if r['H0'] == 73.0][0]['chi2'] / NDOF:.2f} per dof")
if best_fine['H0'] > 71.0:
    fail.append("the onset-free leaf ruler was supposed to re-pin H0 low; it did not")
if [r for r in leaf_noonset if r['H0'] == 73.0][0]['chi2'] / NDOF < 3.0:
    fail.append("the onset-free leaf ruler does not break at H0 = 73, so PART 2 says nothing")

print()
print("=" * 99)
print("  PART 3 -- ** THE LEAF RULER WITH THE ONSET RETAINED.  THIS IS THE CASE THAT DECIDES. **")
print("=" * 99)
print("  z_onset is re-solved from theta_*(leaf) = observed at each H0, exactly as the corpus")
print("  solves it on the stacking ruler, and only then is BAO scored.")
print(HDR)
leaf_onset = [fit_Om(H0, E_leaf, onset=True) for H0 in H0S]
for r in leaf_onset:
    print(row(r))
band = [r for r in leaf_onset if 70.0 <= r['H0'] <= 80.0]
worst = max(r['chi2'] for r in band) / NDOF
best = min(r['chi2'] for r in band) / NDOF
print(f"\n  ⌗ over H0 = 70 to 80 the fit runs {best:.2f} to {worst:.2f} per dof.  "
      f"** The dissolution SURVIVES. **")
if worst > 1.20:
    fail.append(f"the leaf ruler with the onset does NOT hold across 70-80 ({worst:.2f}/dof)")
rho_hi = max(r['rho_ratio'] for r in band)
rho_lo = min(r['rho_ratio'] for r in band)
zo_hi = max(r['z_onset'] for r in band)
zo_lo = min(r['z_onset'] for r in band)
srho_hi = max((1 + r['z_onset']) / (1 + r['z_eq']) for r in stack)
srho_lo = min((1 + r['z_onset']) / (1 + r['z_eq']) for r in stack)
print(f"  ⌗ and across that same band rho_r/rho_m at the onset runs {rho_hi:.1f} down to "
      f"{rho_lo:.1f}.  ** THAT is the price. **")
if rho_hi / rho_lo < 3.0:
    fail.append("the onset's rho_r/rho_m was supposed to run by an order of magnitude; it did not")

print()
print("=" * 99)
print("  PART 4 -- ** THE ACOUSTIC ANGLE ALONE, as a second and independent determination **")
print("=" * 99)
print("  theta_* on the leaf ruler with no onset, against the observed 0.0104085, with Om held at")
print("  each ruler's own BAO best fit.  ** BAO and the angle are not the same measurement and")
print("  agreeing is a result, not bookkeeping. **")


def theta_noonset(H0):
    r = fit_Om(H0, E_leaf, onset=False)
    return r_snd(H0, r['Om'], 1.0e8, ZREC, E_leaf) / D_M(ZREC, H0, r['Om'], E_leaf)


try:
    H0_theta = brentq(lambda h: theta_noonset(h) - THETA_OBS, 62.0, 78.0, xtol=0.02)
    print(f"\n  theta_*(leaf, no onset) = observed at  H0 = {H0_theta:.2f}")
    print(f"  BAO on the same ruler prefers            H0 = {best_fine['H0']:.2f}")
    print(f"  ⌗ the two agree to {abs(H0_theta - best_fine['H0']):.2f} in H0, from independent data")
    if abs(H0_theta - best_fine['H0']) > 2.0:
        fail.append(f"the angle ({H0_theta:.2f}) and BAO ({best_fine['H0']:.2f}) do not agree")
except ValueError:
    print("\n  ** theta_* does not cross the observed value in 62-78 on this ruler **")
    fail.append("theta_* has no root in 62-78 on the onset-free leaf ruler")

print()
print("=" * 99)
print("  PART 5 -- ** WHAT IT COSTS **")
print("=" * 99)
print(f"""
  ** (a) THE DISSOLUTION SURVIVES, WITH A DIFFERENT DERIVATION. **  On the stacking ruler H0
  cancels ALGEBRAICALLY -- the rate is radiation-free, so H0 leaves D_M, D_H and r_d together and
  the BAO ratios cannot see it; the chi^2 spread measured in PART 1 is {spread:.4f}, which is zero.
  On the leaf ruler H0 does NOT cancel: it enters through w_r/h^2.  ** The fit holds across
  70-80 anyway, at {best:.2f}-{worst:.2f} per dof, because the onset moves to keep theta_* fixed. **
  That is a compensation, not a cancellation, and the two are not the same claim.

  ** THE PRICE IS THE ONSET'S PHYSICAL READING. **  The corpus's onset is "where radiation stops
  mattering".  On the stacking ruler it is ONE redshift, {s73['z_onset']:.0f}, at every H0, and the
  leaf background carries rho_r/rho_m there between {srho_hi:.1f} and {srho_lo:.1f} across
  H0 = 63-80 -- a factor {srho_hi / srho_lo:.1f}, and it moves only because z_eq itself moves with h,
  not because the locus does.  ** On the leaf ruler the LOCUS moves: z_onset runs
  {zo_hi:.3g} down to {zo_lo:.3g} across H0 = 70-80 and rho_r/rho_m with it, {rho_hi:.1f} to
  {rho_lo:.1f}, a factor {rho_hi / rho_lo:.1f}. **  A locus that sits at rho_r/rho_m = 51 at one H0
  and 5.8 at another is not "where radiation stops mattering"; it is a fitted redshift, and PART 3's
  flatness is bought with it.

  ⇒ ** AND THE TWO LEAF BRANCHES NEED TWO DIFFERENT SENTENCES, r6760+cc66.8 at 66 (chat)'s
  reading -- an earlier draft of this receipt gave them one and that was wrong: **

      *leaf ruler, ONSET RETAINED* -- sec:tensions keeps its CONCLUSION and not its ARGUMENT.  The
      fit does hold across H0 = 70-80, so H0 is not FORCED by BAO; but it holds by the onset
      moving, not by H0 cancelling, so "H0 is ABSENT from it" no longer follows.

      *leaf ruler, NO ONSET* -- ** sec:tensions keeps NEITHER. **  This branch re-pins H0 to
      {best_fine['H0']:.2f} and breaks at 73 ({[r for r in leaf_noonset if r['H0'] == 73.0][0]['chi2'] / NDOF:.1f} per dof).
      There is no dissolution here at all: BAO on this ruler forces a low H0 exactly as LCDM's
      does, and the acoustic angle independently agrees with it.

  *Which branch the corpus takes is not this receipt's to choose.  What it may not do is carry one
  sentence for both, and the branch that produces the CR spectrum's best acoustic comb
  (r6760+cc66.7) is the second one -- the branch on which the dissolution does not survive.*
""")

print("=" * 99)
if fail:
    print("  FAILED:")
    for f in fail:
        print(f"    - {f}")
    sys.exit(1)
print("  ✓ ALL CHECKS PASSED")
print("=" * 99)
