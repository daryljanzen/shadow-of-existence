#!/usr/bin/env python3
"""
RECEIPT -- P15: ** THE DRIVING SHIFT, MEASURED MODEL-FREE BY SUBTRACTION AGAINST AN UNDRIVEN
REFERENCE THAT CALIBRATES AT 1.000.  LambdaCDM's ACOUSTIC PHASE AT FIRST TURNOVER IS FLAT IN k TO
2.1%; CR's VARIES BY A FACTOR OF 3.9 ACROSS THE SAME BAND.  ** AND THE SCALING IS k^-0.62, NOT THE
k^-2 THE ABANDONED FORK REPORTS -- SO THE PHENOMENON REPRODUCES HERE AND THE EXPONENT DOES NOT. **

Built r2376+c54.169, front #5.  Instrument: `computations/beyond_the_wall/ACOUSTIC_two_arm.py`
(QSCAN=1), whose control and undriven guard were established at c54.168.

** THE METHOD, AND ITS WHOLE POINT IS THAT NOTHING IS MODELLED. **  For each k the same equations
are integrated TWICE -- driven and undriven -- differing in one multiplicative switch and in nothing
else.  Q(k) is the accumulated sound phase in half-periods at the first acoustic turnover of
Theta_0 = delta_gamma/4:

        Q(k) = k INT c_s d(eta) / pi,   from eta_start to that turnover.

** Undriven, a free oscillator must give Q = 1 exactly.  That column is the CALIBRATION and it is
MEASURED, not assumed: it comes out 0.9968-1.0003 on both arms. **  Then

        Delta(k) = Q_undriven(k) - Q_driven(k)

is the driving shift, with no model of the driving anywhere in it.

  PART 1  ** THE CALIBRATION, FIRST, because everything else is read against it. **
  PART 2  ** LambdaCDM: Q_driven flat in k. **  0.791 -> 0.774 over k = 0.045-0.16, a 2.1% spread.
          A mode starts super-horizon, enters, and turns over half a period later minus a constant
          driving shift -- constant because every mode crosses during radiation domination, where
          the potential decays on the sound-crossing time by construction.
  PART 3  ** CR: Q_driven varies by 3.9x over the same band. **  0.457 -> 0.117.  There is no
          radiation era to cross, so the shift is not acquired at crossing (c54.167 showed the
          pre-onset interval is scale-free), and what is left is k-dependent.
  PART 4  ** THE SCALING, AND IT IS WHERE THIS FORK PARTS FROM THE ABANDONED ONE. **  A power-law
          fit gives Q ~ k^-0.62, collapsing the data to a factor of 1.2 where k^-2 spans a factor
          of 16.  ** The acoustic fold reports Q_1 k^2 constant -- an exponent of -2 -- which its
          mechanism (a seam transient relaxing on 3H/k^2) requires. **  This
          instrument does not see that exponent.  The phenomenon is independently reproduced; the
          mechanism's signature is not.

** TWO CORRECTIONS THIS FILE'S OWN CALIBRATION FORCED, both recorded because each would have been a
false result. **  (i) Q was first read on Theta-hat = Theta_0 + Psi; DR switches the couplings INTO
the fluid but not Psi's own evolution, so the undriven column carried a non-oscillating piece and
calibrated at 0.0003.  (ii) With Theta_0, the DRIVEN LambdaCDM column then calibrated at 0.001 -- a
decaying-mode transient in the initial data, two grid points from the start.  ** The acoustic
turnover is by definition after horizon entry, so extrema at k eta < 1 are excluded; that is the
definition of the quantity and not a tuned threshold, and it removes nothing on the CR arm, whose
modes are already sub-horizon at the onset. **

rc=0 on success.  Run: python3 P15_the_driving_shift_by_subtraction.py   (numpy, ~2 s)
"""
import sys

import numpy as np

print(__doc__.split("rc=0")[0])
fail = []

# ---- measured by ACOUSTIC_two_arm.py, QSCAN=1, at r2376+c54.169 ---------------------------------
K = np.array([0.0120, 0.0200, 0.0300, 0.0450, 0.0650, 0.0900, 0.1200, 0.1600])
LC_UND = np.array([np.nan, np.nan, 0.9979, 0.9991, 0.9999, 1.0001, 0.9994, 1.0003])
LC_DRV = np.array([np.nan, 0.8641, 0.8118, 0.7909, 0.7821, 0.7775, 0.7743, 0.7744])
CR_UND = np.array([np.nan, np.nan, 0.9968, 0.9981, 0.9987, 0.9992, 0.9997, 0.9999])
CR_DRV = np.array([np.nan, 0.4566, 0.2955, 0.2266, 0.1874, 0.1596, 0.1368, 0.1167])

# =====================================================================
print("=" * 78)
print("PART 1 — THE CALIBRATION, MEASURED AND NOT ASSUMED")
print("=" * 78)
print("  Undriven, a free oscillator must turn over at Q = 1 exactly.\n")
print(f"  {'arm':>12} {'Q undriven, min':>17} {'max':>10} {'worst departure from 1':>25}")
worst = 0.0
for nm, u in (('LambdaCDM', LC_UND), ('CR', CR_UND)):
    f = u[np.isfinite(u)]
    d = max(abs(f.min() - 1.0), abs(f.max() - 1.0))
    worst = max(worst, d)
    print(f"  {nm:>12} {f.min():>17.4f} {f.max():>10.4f} {d:>25.4f}")
print(f"\n  ** THE DIAGNOSTIC IS CALIBRATED TO {worst:.4f} ON BOTH ARMS. **")
print("     *Everything below is read against this, and both corrections in the header were caught")
print("     by it rather than by inspection — which is the entire reason for measuring it.*")
print("     ⌗ *The two lowest modes return no undriven turnover before recombination and are")
print("     carried as blanks rather than filled in.*")
if worst > 0.01:
    fail.append(f"the undriven calibration is off by {worst:.4f} -- the diagnostic is not calibrated")

# =====================================================================
print()
print("=" * 78)
print("PART 2/3 — THE TWO ARMS, ON ONE SET OF EQUATIONS")
print("=" * 78)
print(f"  {'k [1/Mpc]':>11} {'LCDM Q_drv':>12} {'CR Q_drv':>11} {'LCDM Delta':>12} {'CR Delta':>10}")
for i, k in enumerate(K):
    f = lambda x: ('%.4f' % x) if np.isfinite(x) else '—'                     # noqa: E731
    print(f"  {k:>11.4f} {f(LC_DRV[i]):>12} {f(CR_DRV[i]):>11} "
          f"{f(LC_UND[i]-LC_DRV[i]):>12} {f(CR_UND[i]-CR_DRV[i]):>10}")
band = K >= 0.045
lc_b, cr_b = LC_DRV[band], CR_DRV[band]
lc_spread = (lc_b.max() - lc_b.min()) / lc_b.mean()
cr_ratio = CR_DRV[1] / CR_DRV[-1]
print(f"\n  ** LambdaCDM's Q_driven is FLAT: {lc_spread:.1%} spread over k = 0.045-0.16. **")
print("     *A mode starts super-horizon, enters, and turns over half a period later minus a")
print("     CONSTANT driving shift — constant because every mode crosses during radiation")
print("     domination, where the potential decays on the sound-crossing time by construction.*")
print(f"  ** CR's varies by a factor of {cr_ratio:.1f} across the band, {CR_DRV[1]:.4f} to "
      f"{CR_DRV[-1]:.4f}. **")
print("     *There is no radiation era to cross. c54.167 showed the whole pre-onset interval is")
print("     scale-free, so the shift is not acquired at crossing, and what is left is k-dependent.*")
if lc_spread > 0.06:
    fail.append(f"the control's Q is not flat: {lc_spread:.1%} spread")
if cr_ratio < 2.0:
    fail.append(f"CR's Q varies by only {cr_ratio:.1f}x -- the effect is not present")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE SCALING, AND WHERE THIS FORK PARTS FROM THE ABANDONED ONE")
print("=" * 78)
m = np.isfinite(CR_DRV)
p = np.polyfit(np.log(K[m]), np.log(CR_DRV[m]), 1)
slope = p[0]
resid = np.log(CR_DRV[m]) - np.polyval(p, np.log(K[m]))
print(f"  power-law fit to CR's Q_driven over the whole band: Q ~ k^{slope:.3f}   "
      f"(rms residual {np.std(resid):.4f} in ln Q)")
print(f"\n  {'k':>10} {'Q_driven':>10} {'Q k^2':>12} {'Q k^(-fit)':>12}")
for i in np.where(m)[0]:
    print(f"  {K[i]:>10.4f} {CR_DRV[i]:>10.4f} {CR_DRV[i]*K[i]**2:>12.3e} "
          f"{CR_DRV[i]*K[i]**(-slope):>12.4f}")
qk2 = CR_DRV[m] * K[m] ** 2
qkp = CR_DRV[m] * K[m] ** (-slope)
print(f"\n  Q k^2      spans {qk2.min():.3e} to {qk2.max():.3e}  — a factor of {qk2.max()/qk2.min():.0f}")
print(f"  Q k^{-slope:.2f}   spans {qkp.min():.4f} to {qkp.max():.4f}  — a factor of "
      f"{qkp.max()/qkp.min():.2f}")
print()
print(f"  ** SO THE SCALING IS k^{slope:.2f}, NOT k^-2. **")
print("     *The abandoned acoustic fork reports Q_1 k^2 constant across its range, and its stated")
print("     mechanism — a seam transient relaxing on 3H/k^2 — REQUIRES that exponent.* ")
print(f"     ⇒ ***This instrument reproduces the PHENOMENON independently — LambdaCDM flat, CR")
print(f"     falling steeply, same direction and comparable magnitude — and does NOT reproduce the")
print("     EXPONENT its mechanism turns on.***")
print("     *Recorded as a disagreement between instruments, not resolved. The fold's own")
print("     reproduction gate fails in this tree, and no figure of its is used here; this file's")
print("     own gate is the 1.000 calibration in PART 1.*")
if not (-1.2 < slope < -0.3):
    fail.append(f"CR's fitted exponent is {slope:.2f}, outside the measured -0.66 by too much")
if qk2.max() / qk2.min() < 4.0:
    fail.append("Q k^2 IS nearly constant after all -- PART 4's whole claim would be wrong")
assert qkp.max() / qkp.min() < qk2.max() / qk2.min(), \
    "the fitted exponent must collapse the data better than k^-2, or the fit means nothing"

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — the diagnostic calibrates at 1.000 on both arms; LambdaCDM's acoustic")
print("phase is flat in k to 2.1% and CR's varies by 3.9x; and the CR scaling is k^-0.62, which is")
print("not the k^-2 the abandoned fork's mechanism requires.")
print("=" * 78)
