#!/usr/bin/env python3
"""
RECEIPT -- P15: ** P1/P3 TRACKS THE LEAF EQUALITY AND NOT THE ROUTE TO IT.  MOVING z_eq THROUGH THE
RADIATION AND MOVING IT THROUGH Omega_m GIVE 2.299 vs 2.294 AT z_eq = 3447 AND 2.474 vs 2.460 AT
3000 -- 0.2% AND 0.6% APART, ACROSS A 12% CHANGE IN Omega_m AND THEREFORE IN D_M AND THE WHOLE
PROJECTION.  ** SO THE THIRD-PEAK DEFICIT IS RADIATION DRIVING. **

** ⇒ AND THE ARM'S OWN EQUALITY IS THE RESIDUAL. **  At the crossing handover with z_eq moved to
LCDM's 3447 the four peaks land at 220/536/816/1132 against the sky's 220.4/537.7/817.3/1123.9, the
fitted comb at 298.0 against 298.4, and the acoustic phase at -0.2416 pi against the sky's
-0.2405 pi -- `sec:intro`'s own headline number, on an arm that spends no fitted parameter on it.
** chi^2 falls 4723.2 -> 645.8 over 133 bins and the 700-1000 band that the crossing handover did
NOT fix falls 85.9 -> 6.4 per bin. **

⛔ ** THAT IS A DIAGNOSIS AND NOT A FIT. **  z_eq = 3447 is LCDM's value, not a freedom this arm
has: `ORFAC` = 1.1418 is 14.2% more radiation than the arm's parameters give.  What the scan
establishes is WHERE the residual lives, and at 3447 the arm is still 4.86 per bin against the
control's 2.10 -- a factor 2.3, where the coded arm was a factor 56.

Built r6760+cc66.4 (node 66, code seat), on `PO-13`, at node 66 (chat seat)'s work order (run 2)
and its amendment 1 (the second route).

===================================================================================================
** WHY TWO ROUTES, AND WHY THE ANSWER IS ONLY MEANINGFUL FROM BOTH **
===================================================================================================

z_eq = Omega_m/Omega_r - 1 on the leaf background.  It can be moved either way:

  `ORFAC`  scales Omega_r at fixed Omega_m.  ** At fixed T_CMB that is a Delta N_eff **, and it is
           NOT how this arm's equality arises.  It leaves D_M and r_s untouched -- the stacking
           rate carries no radiation term -- so ONLY the driving moves.
  `CROM`   sets Omega_m at fixed Omega_r.  ** That IS how this arm's equality arises **: z_eq = 3936
           here is omega_m = 0.1634 (H0 = 73 at Omega_m = 0.3066) against LCDM's 0.1431.  But
           Omega_m cannot move without Omega_Lambda = 1 - Omega_m and therefore D_M moving with it.

*** Each route has a confound the other does not.  A quantity that tracks z_eq on BOTH is tracking
the equality; one that tracks on ONE is tracking that route's confound.  That is the whole design,
and it is why the run was worth doing twice. ***

  PART 1  ** THE ROWS. **  Peaks, comb, phase, ratios and chi^2 on both routes at both points.
  PART 2  ** THE TEST. **  P1/P3 across the routes.
  PART 3  ** AND WHAT DOES NOT TRACK, ** which is as much of the result as what does.
  PART 4  ** THE SKY, AT z_eq = 3447. **

** COMPUTES: nothing.  *** It reads spectra already produced and scores them.  Every parameter is
   baked into the .npz it reads -- ARM=cr at H0 = 73.00, ZSTART = 3e7 (the crossing), LMAXL = 1300,
   KFAC = 2, the polarisation path -- and the one knob each row varies is in its filename.  The comb
   fit has no parameter. *** **

rc=0 on success.  Run: python3 <this file>   (numpy, scipy; ~10 s; reads spectra/cc66_*.npz)
"""
import os
import sys

import numpy as np
from scipy.signal import argrelextrema
import scipy.linalg

print(__doc__.split("rc=0")[0])
fail = []
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

SKY = np.array([220.4, 537.7, 817.3, 1123.9])          # sec:intro's parabolic fit on plik_lite
BAND = (700.0, 1000.0)


def fit_comb(pk, n=3):
    """l_n = l_A (n + phi/pi) on the first n peaks -- sec:intro's own procedure."""
    nn = np.arange(1, n + 1, dtype=float)
    A = np.vstack([nn, np.ones_like(nn)]).T
    lA, b = np.linalg.lstsq(A, np.asarray(pk[:n], float), rcond=None)[0]
    return float(lA), float(np.pi * b / lA)


def _fisher(keep):
    cov = CS.COV_TT[np.ix_(keep, keep)]
    F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(cov), np.identity(int(keep.sum())))
    return 0.5 * (F + F.T)


def score(tag):
    z = np.load(os.path.join(SPEC, f'cc66_{tag}.npz'))
    ls, Dl = np.asarray(z['ls'], float), np.asarray(z['Dl'], float)
    q = argrelextrema(Dl, np.greater, order=3)[0][:4]
    P = [float(ls[i]) for i in q]
    H = [float(Dl[i]) for i in q]
    lA, phi = fit_comb(P)
    mb = CS.bin_spectrum(ls, Dl)
    ok = np.isfinite(mb)
    # ** THE BAND chi^2 IS EVALUATED AT THE GLOBALLY FITTED AMPLITUDE, not one refitted inside the
    # band: this instrument has ONE amplitude and scoring a band on its own would be answering a
    # question the model does not ask.  And the restriction is done on the COVARIANCE and
    # re-inverted, never on the Fisher matrix -- dropping Fisher rows would CONDITION on the bins
    # outside the band instead of marginalising over them (chi2_of_spectrum.py's choice 1). **
    Fg = _fisher(ok)
    m, d = mb[ok], CS.X_DATA[ok]
    A = float((m @ Fg @ d) / (m @ Fg @ m))
    chi2_all = float((d - A * m) @ Fg @ (d - A * m))
    inb = ok & (CS.BIN_LO >= BAND[0]) & (CS.BIN_HI <= BAND[1])
    Fb = _fisher(inb)
    r = CS.X_DATA[inb] - A * mb[inb]
    return dict(peaks=P, heights=H, lA=lA, phi=phi, p12=H[0] / H[1], p13=H[0] / H[2],
                chi2=chi2_all, nall=int(ok.sum()),
                band=float(r @ Fb @ r), nband=int(inb.sum()),
                r_s=float(z['r_s']), D_M=float(z['D_M']))


ROWS = [
    ('as coded', 3936, '-', 0.3066, 'cr_crossing'),
    ('radiation (ORFAC)', 3447, 'Omega_r x 1.1418', 0.3066, 'cr_x_zeq3447'),
    ('matter (CROM)', 3447, 'Omega_m = 0.2685', 0.2685, 'cr_x_crom3447'),
    ('radiation (ORFAC)', 3000, 'Omega_r x 1.3119', 0.3066, 'cr_x_zeq3000'),
    ('matter (CROM)', 3000, 'Omega_m = 0.2337', 0.2337, 'cr_x_crom3000'),
]
CTL = score('lcdm')
R = {}
print("=" * 108)
print("  PART 1 -- ** THE ROWS.  The crossing handover throughout; only the equality moves. **")
print("=" * 108)
print(f"  {'route':>19} {'z_eq':>5} {'Om':>7} {'peaks':>26} {'comb':>7} {'phi/pi':>8} "
      f"{'P1/P2':>7} {'P1/P3':>7} {'chi2':>8} {'band/bin':>9}")
for route, zeq, how, Om, tag in ROWS:
    try:
        s = score(tag)
    except FileNotFoundError:
        fail.append(f"spectrum cc66_{tag}.npz is missing")
        continue
    R[(route.split()[0], zeq)] = s
    print(f"  {route:>19} {zeq:>5d} {Om:>7.4f} {str([int(v) for v in s['peaks']]):>26} "
          f"{s['lA']:>7.1f} {s['phi'] / np.pi:>8.4f} {s['p12']:>7.3f} {s['p13']:>7.3f} "
          f"{s['chi2']:>8.1f} {s['band'] / s['nband']:>9.2f}")
lA_sky, phi_sky = fit_comb(SKY)
print(f"  {'sky':>19} {'':>5} {'':>7} {str([float(v) for v in SKY]):>26} {lA_sky:>7.1f} "
      f"{phi_sky / np.pi:>8.4f} {2.217:>7.3f} {2.277:>7.3f} {'--':>8} {'--':>9}")
print(f"  {'control (LCDM)':>19} {3447:>5d} {0.3150:>7.4f} "
      f"{str([int(v) for v in CTL['peaks']]):>26} {CTL['lA']:>7.1f} "
      f"{CTL['phi'] / np.pi:>8.4f} {CTL['p12']:>7.3f} {CTL['p13']:>7.3f} {CTL['chi2']:>8.1f} "
      f"{CTL['band'] / CTL['nband']:>9.2f}")

print()
print("=" * 108)
print("  PART 2 -- ** THE TEST: DOES P1/P3 TRACK THE EQUALITY OR THE ROUTE? **")
print("=" * 108)
print(f"  {'z_eq':>6} {'radiation':>11} {'matter':>9} {'apart':>8}   "
      f"{'d(Omega_m) between the two routes':>34}")
for zeq in (3447, 3000):
    a, b = R[('radiation', zeq)]['p13'], R[('matter', zeq)]['p13']
    dOm = abs(0.3066 - dict(((3447, 0.2685), (3000, 0.2337)))[zeq]) / 0.3066
    print(f"  {zeq:>6d} {a:>11.3f} {b:>9.3f} {abs(a - b) / a * 100:>7.2f}%   {dOm * 100:>33.1f}%")
    if abs(a - b) / a > 0.02:
        fail.append(f"P1/P3 differs by {abs(a - b) / a * 100:.1f}% between routes at z_eq = {zeq}")
base = R[('as', 3936)]['p13']
print(f"\n  ⌗ and it MOVES with z_eq on both: {base:.3f} at 3936, "
      f"{R[('radiation', 3447)]['p13']:.3f}/{R[('matter', 3447)]['p13']:.3f} at 3447, "
      f"{R[('radiation', 3000)]['p13']:.3f}/{R[('matter', 3000)]['p13']:.3f} at 3000")
if R[('radiation', 3000)]['p13'] - base < 0.15:
    fail.append("P1/P3 barely moves across the scan -- the test has no lever")
print("\n  ** A quantity that agrees to 0.2-0.6% across a 12-24% change in Omega_m, D_M and the")
print("  whole projection is tracking the EQUALITY.  So the third-peak deficit is radiation")
print("  driving, and the route by which the equality is reached is irrelevant to it. **")

print()
print("=" * 108)
print("  PART 3 -- ** AND WHAT DOES NOT TRACK **")
print("=" * 108)
print(f"  {'z_eq':>6} {'':>12} {'peaks':>26} {'comb':>7} {'r_s':>8} {'D_M':>9} {'band/bin':>9}")
for zeq in (3447, 3000):
    for route in ('radiation', 'matter'):
        s = R[(route, zeq)]
        print(f"  {zeq:>6d} {route:>12} {str([int(v) for v in s['peaks']]):>26} {s['lA']:>7.1f} "
              f"{s['r_s']:>8.2f} {s['D_M']:>9.1f} {s['band'] / s['nband']:>9.2f}")
print(f"""
  ** THE RADIATION ROUTE MOVES NEITHER RULER: ** r_s = {R[('radiation', 3447)]['r_s']:.2f} Mpc and
  D_M = {R[('radiation', 3447)]['D_M']:.1f} Mpc are IDENTICAL at every ORFAC, because the stacking
  rate has no radiation term in it.  ** The matter route moves both. **  So the two routes'
  positions and their 700-1000 bands part company -- {R[('radiation', 3447)]['band'] / 33:.1f} per bin
  at 3447 on radiation against {R[('matter', 3447)]['band'] / 33:.1f} on matter, and the band's
  minimum lands at a DIFFERENT z_eq on the two.
  ⇒ *** That is the Omega_m/D_M confound made visible, not a contradiction, and it is exactly why
  P1/P3 -- a ratio at fixed ell, blind to D_M -- is the quantity that carries the verdict. ***""")
if abs(R[('radiation', 3447)]['r_s'] - R[('radiation', 3000)]['r_s']) > 1e-6:
    fail.append("the radiation route moved r_s -- it must not")
if abs(R[('radiation', 3447)]['D_M'] - R[('radiation', 3000)]['D_M']) > 1e-6:
    fail.append("the radiation route moved D_M -- it must not")
if abs(R[('matter', 3447)]['D_M'] - R[('radiation', 3447)]['D_M']) < 100:
    fail.append("the matter route did NOT move D_M -- PART 3's premise is wrong")

print()
print("=" * 108)
print("  PART 4 -- ** THE SKY, AT z_eq = 3447 **")
print("=" * 108)
s = R[('radiation', 3447)]
print(f"  {'':>14} {'peak 1':>9} {'peak 2':>9} {'peak 3':>9} {'peak 4':>9} {'comb':>8} {'phi/pi':>9}")
print(f"  {'arm at 3447':>14} {s['peaks'][0]:>9.0f} {s['peaks'][1]:>9.0f} {s['peaks'][2]:>9.0f} "
      f"{s['peaks'][3]:>9.0f} {s['lA']:>8.1f} {s['phi'] / np.pi:>9.4f}")
print(f"  {'sky':>14} {SKY[0]:>9.1f} {SKY[1]:>9.1f} {SKY[2]:>9.1f} {SKY[3]:>9.1f} "
      f"{lA_sky:>8.1f} {phi_sky / np.pi:>9.4f}")
print(f"  {'control':>14} {CTL['peaks'][0]:>9.0f} {CTL['peaks'][1]:>9.0f} {CTL['peaks'][2]:>9.0f} "
      f"{CTL['peaks'][3]:>9.0f} {CTL['lA']:>8.1f} {CTL['phi'] / np.pi:>9.4f}")
for i in range(3):
    d = abs(s['peaks'][i] - SKY[i]) / SKY[i]
    if d > 0.01:
        fail.append(f"peak {i + 1} is {d * 100:.1f}% off the sky at z_eq = 3447, not sub-per-cent")
if abs(s['phi'] - phi_sky) / abs(phi_sky) > 0.02:
    fail.append(f"the phase at 3447 is {s['phi'] / np.pi:.4f} pi against the sky's "
                f"{phi_sky / np.pi:.4f} pi")
if s['chi2'] > 0.25 * R[('as', 3936)]['chi2']:
    fail.append("chi^2 at 3447 is not the large improvement claimed")
print(f"""
  ⛔ ** AND IT IS STILL REJECTED. **  {s['chi2'] / s['nall']:.2f} per bin against the control's
  {CTL['chi2'] / CTL['nall']:.2f} -- a factor {s['chi2'] / CTL['chi2']:.1f}, where the coded arm was a factor
  {15752.0 / CTL['chi2']:.0f}.  ** z_eq = 3447 is not a freedom this arm has, and this row is a
  MEASUREMENT OF WHERE THE RESIDUAL LIVES, not a fit to the sky. **

  ⌗ ** AND THE SCAN IS NOT MONOTONE, ** which is the point: chi^2 runs
  {R[('as', 3936)]['chi2']:.0f} -> {R[('radiation', 3447)]['chi2']:.0f} ->
  {R[('radiation', 3000)]['chi2']:.0f} at 3936/3447/3000.  *The sky sits at a MINIMUM inside the
  scanned range, so this measures where the arm's equality should be; it does not give a direction
  to push it.*""")
if R[('radiation', 3000)]['chi2'] < R[('radiation', 3447)]['chi2']:
    fail.append("chi^2 is monotone in z_eq -- the minimum claim is wrong")

print()
print("=" * 108)
if fail:
    print("  FAILED:")
    for f in fail:
        print(f"    - {f}")
    sys.exit(1)
print("  ✓ ALL CHECKS PASSED")
print("=" * 108)
