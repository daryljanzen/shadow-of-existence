#!/usr/bin/env python3
"""
RECEIPT -- P15: ** THE k-DEPENDENCE LIVES IN THE POTENTIAL'S GRADIENT, NOT IN ITS DECAY.  SPLIT INTO
ITS TWO COUPLINGS, THE DRIVING SEPARATES: THE 4 Phi' IN CONTINUITY GIVES A NEARLY k-INDEPENDENT SHIFT
(k^-0.17) AND THE k^2 Psi IN EULER GIVES k^-1.04.  ** AND IN FLAT LambdaCDM BOTH ARE FLAT AND THEY
PARTLY CANCEL -- ONE DELAYS THE TURNOVER, THE OTHER ADVANCES IT -- WHILE ON THE RADIATION-FREE RATE
BOTH ADVANCE IT AND THEY ADD. **

Built r2376+c54.170, front #5, on the c54.168 instrument and against its 1.000 calibration.

** WHY THIS IS THE RIGHT NEXT CUT. **  c54.169 measured the driving shift model-free and found CR's
Q(k) scaling at k^-0.62 against a flat LambdaCDM -- reproducing the acoustic fold's PHENOMENON and
not its EXPONENT of -2.  The fold's mechanism attributes the k-dependence to a seam transient
relaxing on 3H/k^2, which is a statement about how the potential DECAYS.  ** Decay feeds the density
through the 4 Phi' term in continuity.  So the mechanism is checkable by switching the two couplings
independently, and that is what this does. **

  DRC   the 4 Phi' in the photon, neutrino and CDM CONTINUITY equations -- the potential's RATE OF
        CHANGE feeding the density.  ** This is the decay channel, and it is the one the fold's
        mechanism points at. **
  DRE   the k^2 Psi in the photon/baryon and neutrino EULER equations -- the potential's GRADIENT
        driving the velocity, the restoring force the oscillator swings against.

Phi's own evolution is never switched: that is the potential's dynamics, not a coupling into the
fluid, and removing it would change the background rather than the driving.

  PART 1  ** FLAT LambdaCDM: BOTH COUPLINGS ARE FLAT IN k, AND THEY OPPOSE. **  Continuity alone
          gives Q = 1.23-1.28 -- ABOVE one, so it DELAYS the turnover past a free half-period --
          while Euler alone gives 0.73-0.87, BELOW one, advancing it.  Together, 0.77-0.86.
          ** The universality of the standard driving shift is a cancellation, not a single term. **
  PART 2  ** ON THE RADIATION-FREE RATE THEY BOTH ADVANCE, SO THEY ADD. **  Continuity 0.11-0.18,
          Euler 0.06-0.57, driven 0.12-0.46 -- all far below one.  There is no cancellation left.
  PART 3  ** AND THE k-DEPENDENCE IS IN THE EULER TERM. **  Continuity alone varies by 1.6x across
          the band (k^-0.17, nearly flat); Euler alone by 8.9x (k^-1.04).  ** The decay channel --
          the one the fold's mechanism names -- is the FLAT one. **
  PART 4  ** AND NEITHER TERM ALONE IS THE ANSWER. **  The driven exponent, -0.62, lies BETWEEN the
          two, so the observed scaling is their interference and not either coupling's signature.
          *A mechanism naming one term has to explain why the other does not cancel it.*

** WHAT THIS DOES AND DOES NOT SETTLE. **  It localises the k-dependence to a specific coupling and
shows the standard shift's universality is a cancellation that this rate does not have.  ** It does
not name the process that makes the Euler coupling run as k^-1 here, and it does not compute a peak
position. **  It closes the fold's stated mechanism as an explanation of THIS measurement: a
relaxation on 3H/k^2 acts through the decay channel, and the decay channel is measured flat.

rc=0 on success.  Run: python3 P15_which_coupling_carries_the_k_dependence.py   (numpy, ~2 s)
"""
import sys

import numpy as np

print(__doc__.split("rc=0")[0])
fail = []

# ---- measured by ACOUSTIC_two_arm.py, QSCAN=1, at r2376+c54.170 ---------------------------------
K = np.array([0.0120, 0.0200, 0.0300, 0.0450, 0.0650, 0.0900, 0.1200, 0.1600])
N = np.nan
LC = {'undriven':   np.array([N, N, 0.9979, 0.9991, 0.9999, 1.0001, 0.9994, 1.0003]),
      'continuity': np.array([N, N, 1.2320, 1.2488, 1.2611, 1.2692, 1.2758, 1.2807]),
      'Euler':      np.array([N, 0.8727, 0.8050, 0.7716, 0.7542, 0.7439, 0.7366, 0.7319]),
      'driven':     np.array([N, 0.8641, 0.8118, 0.7909, 0.7821, 0.7775, 0.7743, 0.7744])}
CR = {'undriven':   np.array([N, N, 0.9968, 0.9981, 0.9987, 0.9992, 0.9997, 0.9999]),
      'continuity': np.array([0.1675, 0.1753, 0.1761, 0.1686, 0.1555, 0.1395, 0.1241, 0.1091]),
      'Euler':      np.array([N, 0.5668, 0.3572, 0.2334, 0.1601, 0.1153, 0.0861, 0.0640]),
      'driven':     np.array([N, 0.4566, 0.2955, 0.2266, 0.1874, 0.1596, 0.1368, 0.1167])}


def fit(q):
    m = np.isfinite(q)
    return float(np.polyfit(np.log(K[m]), np.log(q[m]), 1)[0]), q[m].min(), q[m].max()


def table(name, D):
    print(f"  {name}")
    print(f"  {'configuration':>14} {'Q range':>19} {'variation':>11} {'exponent':>11} "
          f"{'vs a free half-period':>23}")
    out = {}
    for tag in ('undriven', 'continuity', 'Euler', 'driven'):
        sl, lo, hi = fit(D[tag])
        out[tag] = (sl, lo, hi)
        side = 'delays it' if lo > 1.0 else ('advances it' if hi < 1.0 else 'straddles 1')
        print(f"  {tag:>14} {('%.4f - %.4f' % (lo, hi)):>19} {hi/lo:>10.2f}x "
              f"{('k^%+.2f' % sl):>11} {side:>23}")
    return out


# =====================================================================
print("=" * 78)
print("PART 1 — FLAT LambdaCDM: BOTH COUPLINGS FLAT, AND THEY OPPOSE")
print("=" * 78)
L = table("flat LambdaCDM, radiation-included rate", LC)
print()
print("  ** THE STANDARD DRIVING SHIFT'S UNIVERSALITY IS A CANCELLATION. **")
print("     *Continuity alone puts the turnover LATE — Q above one — and Euler alone puts it EARLY.")
print("     Each is flat in k on its own, and the residue after they oppose is flat too.*")
if not (L['continuity'][1] > 1.0 and L['Euler'][2] < 1.0):
    fail.append("in LambdaCDM the two couplings do not oppose across a free half-period")
for tag in ('continuity', 'Euler', 'driven'):
    if abs(L[tag][0]) > 0.15:
        fail.append(f"LambdaCDM's {tag} is not flat: exponent {L[tag][0]:+.2f}")

# =====================================================================
print()
print("=" * 78)
print("PART 2/3 — THE RADIATION-FREE RATE: THEY ADD, AND THE EULER TERM CARRIES THE k-DEPENDENCE")
print("=" * 78)
R = table("CR, geometric stacking (L1) rate", CR)
print()
print(f"  ** BOTH COUPLINGS NOW ADVANCE THE TURNOVER — continuity to {R['continuity'][2]:.2f} and")
print(f"     Euler to {R['Euler'][2]:.2f}, both below one — so there is no cancellation left. **")
print(f"  ** AND THE k-DEPENDENCE IS IN THE EULER TERM: continuity varies "
      f"{R['continuity'][2]/R['continuity'][1]:.1f}x at k^{R['continuity'][0]:+.2f}, "
      f"Euler {R['Euler'][2]/R['Euler'][1]:.1f}x at k^{R['Euler'][0]:+.2f}. **")
print("     ⇒ ***The DECAY channel — the potential's rate of change feeding the density, which is")
print("     what a relaxation timescale acts through — is the NEARLY FLAT one.***")
if abs(R['continuity'][0]) > 0.35:
    fail.append(f"CR's continuity term is not nearly flat: exponent {R['continuity'][0]:+.2f}")
if abs(R['Euler'][0]) < 0.8:
    fail.append(f"CR's Euler term is not steep: exponent {R['Euler'][0]:+.2f}")
if not (R['continuity'][2] < 1.0 and R['Euler'][2] < 1.0):
    fail.append("on the CR arm the two couplings do not both advance the turnover")
if abs(R['Euler'][0]) <= abs(R['continuity'][0]):
    fail.append("the Euler term is not the steeper one -- PART 3's whole claim would be reversed")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — AND NEITHER TERM ALONE IS THE ANSWER")
print("=" * 78)
c, e, d = R['continuity'][0], R['Euler'][0], R['driven'][0]
print(f"  CR exponents:   continuity {c:+.2f}     Euler {e:+.2f}     driven {d:+.2f}")
print(f"\n  ** The driven exponent lies BETWEEN the two ({e:+.2f} < {d:+.2f} < {c:+.2f}), so the")
print("     observed scaling is their INTERFERENCE and not either coupling's own signature. **")
print("     *A mechanism that names one term has to say why the other does not cancel it — which is")
print("     exactly what flat LambdaCDM does and this rate does not.*")
print()
print("  ⌗ **WHAT THIS DOES TO THE ABANDONED FORK'S MECHANISM.** *It attributes the k-dependence to")
print("     a seam transient relaxing on 3H/k^2. **A relaxation timescale acts through the decay")
print("     channel, and the decay channel is measured flat here at k^-0.17.** So that mechanism does")
print("     not explain THIS measurement.* ⇒ *Recorded as what it is: the fold's phenomenon is")
print("     reproduced (c54.169), its exponent is not, and now its channel is not either. **No")
print("     replacement mechanism is named, because the measurement does not supply one.***")
if not (e < d < c):
    fail.append(f"the driven exponent {d:+.2f} is not between {e:+.2f} and {c:+.2f} -- no interference")
assert abs(d - e) > 0.2 and abs(d - c) > 0.2, \
    "the driven exponent must be clearly distinct from BOTH single-term exponents"
# the calibration is the file's own gate, on both arms
for nm, D in (('LambdaCDM', LC), ('CR', CR)):
    u = D['undriven'][np.isfinite(D['undriven'])]
    if max(abs(u.min() - 1.0), abs(u.max() - 1.0)) > 0.01:
        fail.append(f"{nm}'s undriven calibration is off -- nothing above is readable")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — in flat LambdaCDM both couplings are flat in k and oppose, so the standard")
print("shift's universality is a cancellation; on the geometric stacking rate both advance and add, the")
print("k-dependence sits in the Euler coupling at k^-1.04 while the decay channel is flat at k^-0.17,")
print("and the driven exponent lies between the two.")
print("=" * 78)
