#!/usr/bin/env python3
"""RECEIPT — P15: ** WITHDRAWN r3424.  THE SHAPE THIS RECEIPT REPORTED IS AN ARTEFACT OF AN INITIAL
CONDITION I CHOSE RATHER THAN DERIVED, AND IT REVERSES WITH THAT DATUM'S SIGN. **

WHAT WAS CLAIMED: that Q(k), the accumulated sound phase at first turnover, runs to its
  free-oscillator value from above on this rate while a background carrying a radiation era holds
  it flat and below -- offered as a second, normalisation-independent observable and written into
  P15 and P07 at r3412.

WHAT IS TRUE: the frozen effective temperature the modes carry at onset, T-hat, is NOT determined
  by the construction, and Q depends on it strongly at low k.  Measured:

      T-hat     k=5     k=10    k=20    k=40    k=160
      -0.500  1.2763  1.1661  1.0828  1.0374  1.0076   <- what this receipt used
      +0.488  0.2416  0.0997  0.0470  1.0556  1.0122   <- the ADIABATIC value, +Phi/2

  For T-hat <= 0 the phase runs to 1 from above; for T-hat > 0 it collapses at low k.  The
  "rising toward 1" shape is the sign, not the physics.

HOW IT WAS FOUND, since the route matters: the comprehensive comb (589) swept for a RETIRED TERM
  and surfaced PHASE7_BUILD_LEDGER using it in live physics prose -- whose measurement A.139 says
  the opposite of this receipt, "CR's shift is LARGER, by a factor of four", and records that its
  own earlier mechanism "had the sign backwards".  A terminology sweep found a physics
  contradiction, and the contradiction was mine.

WHAT SURVIVES AND IS UNAFFECTED: the comb result itself -- that this comb's spacings do not
  alternate where the sky's do -- is an INSTRUMENT measurement and does not depend on any of this.
  So is the crossing-during-plasma mechanism and its calibration curve.  What falls is only the
  claim that the mechanism can be read directly in the phase.

THE PART OF THE MACHINERY THAT STANDS: the undriven calibration gates at 1.0000 on both arms, the
  potential is closed by the energy constraint and not evolved, and the turnover is the photon
  velocity's reversal.  Those three were right and are kept.  The IC was never checked against the
  adiabatic relation delta_gamma = -2 Phi, which gives T-hat = +Phi/2, and that is the whole error.
"""
import numpy as np
from scipy.integrate import solve_ivp, trapezoid
from scipy.optimize import brentq

# ---------------------------------------------------------------- background, DERIVED
# rho_r ~ a^-4, rho_m ~ a^-3, y = a/a_eq.  H^2 = C (1+y)/y^2; with C=1,
#   Hc(y) = sqrt(1+y)/y      and      d eta / dy = 1/sqrt(1+y).
Hc = lambda y: np.sqrt(1 + y) / y
Og = lambda y: 1.0 / (1.0 + y)          # radiation fraction of the total
Om = lambda y: y / (1.0 + y)
Req = 0.199                             # R = 0.62 at y_rec = 3.12
R = lambda y: Req * y


def rs(y, y0, n=4000):
    """comoving sound horizon from the start of oscillation, c_s = 1/sqrt(3(1+R))."""
    yy = np.linspace(y0, y, n)
    return trapezoid(1 / np.sqrt(3 * (1 + R(yy))) / np.sqrt(1 + yy), yy)


def Q(k, y0, ic, drive=1.0):
    """accumulated sound phase at first turnover, in half-periods.  1.0 for a free oscillator."""
    def rhs(y, u):
        dg, tg, dc, tc, Ph = u
        H, Rv = Hc(y), R(y)
        dPh = -H * Ph - k * k * Ph / (3 * H) - (H / 2) * (Og(y) * dg + Om(y) * dc)   # CONSTRAINT
        dtg = -(H * Rv / (1 + Rv)) * tg + (k * k / (1 + Rv)) * (dg / 4) + k * k * Ph * drive
        return np.array([-(4 / 3) * tg + 4 * dPh * drive, dtg,
                         -tc + 3 * dPh, -H * tc + k * k * Ph, dPh]) / np.sqrt(1 + y)
    s = solve_ivp(rhs, [y0, 60], ic, rtol=1e-10, atol=1e-14, dense_output=True, method='Radau')
    ys = np.linspace(y0 + 1e-6, 50, 60000)
    tg = s.sol(ys)[1]
    idx = [i for i in np.where(np.diff(np.sign(tg)) != 0)[0] if ys[i] > y0 * 1.02 + 1e-4]
    if not idx:
        return np.nan
    yz = brentq(lambda yy: s.sol(yy)[1], ys[idx[0]], ys[idx[0] + 1])
    return k * rs(yz, y0) / np.pi


sup = lambda P: [-2 * P, 0, -1.5 * P, 0, P]          # adiabatic super-horizon (control)
frz = lambda P, T: [4 * (T - P), 0, -1.5, 0, P]      # frozen at onset, velocities zero (CR)
KS = (5, 10, 20, 40, 80, 160)
Y_ON = 0.5      # rho_r/rho_m = 2 at the onset  =>  y = a/a_eq = 1/2.  THE DATUM, not a choice.
PHI_ON = 0.9767  # Meszaros Phi(y=1/2)/Phi(0)

print("=" * 78)
print("  THE DRIVING SHIFT, DERIVED — coupled photon/matter/potential on Meszaros")
print("=" * 78)

print("\n  [gate] UNDRIVEN CALIBRATION — a free oscillator must turn at k r_s = pi, i.e. Q = 1")
for k in KS:
    qa, qb = Q(k, 1e-4, sup(1.0), 0.0), Q(k, Y_ON, frz(PHI_ON, -0.5), 0.0)
    print(f"      k={k:4d}   control {qa:.4f}   onset-start {qb:.4f}")
    assert abs(qa - 1) < 0.01 and abs(qb - 1) < 0.01, "undriven calibration failed"
print("      ** both arms return 1.0000 — the machinery is gated before anything is read **")

print("\n  [result] DRIVEN")
print(f"      {'k':>5} {'Q control':>11} {'Q onset-start':>15} {'difference':>12}")
qc, qo = [], []
for k in KS:
    a, b = Q(k, 1e-4, sup(1.0)), Q(k, Y_ON, frz(PHI_ON, -0.5))
    qc.append(a); qo.append(b)
    print(f"      {k:5d} {a:11.4f} {b:15.4f} {b - a:+12.4f}")

print("\n  [verdict 1] the control is DRIVEN and FLAT in k")
assert all(q < 0.85 for q in qc), "control should sit well below 1"
assert max(qc) - min(qc) < 0.10, "control should be flat in k"
print(f"      Q_control spans {min(qc):.3f}..{max(qc):.3f} — driven, and flat to {max(qc)-min(qc):.3f}")

print("\n  [verdict 2] the onset-start arm RISES TOWARD 1: it inherits the UNDRIVEN phase")
assert qo[-1] < qo[0], "Q should fall toward 1 from above as k rises"
assert abs(qo[-1] - 1) < 0.02, "Q should reach the free-oscillator value at large k"
print(f"      Q_onset spans {qo[0]:.3f} down to {qo[-1]:.4f} — reaching the free-oscillator value")
print("      ** a uniform comb IS an undriven comb, and Q -> 1 is what undriven means **")

print("\n  [verdict 3] FLAT versus RISING is independent of normalisation")
print("      which is why the magnitude gap (no neutrinos here) does not touch the prediction")
assert (max(qc) - min(qc)) < (qo[0] - qo[-1]) / 2, "the shapes must be qualitatively distinct"

print("\n  [robustness] the onset position is the ONLY channel a radiation-budget change acts through")
print(f"      {'y_on':>6} {'rho_r/rho_m':>12} {'Q(k=40)':>10} {'Q(k=160)':>10}")
for yon in (0.35, 0.50, 0.75):
    print(f"      {yon:6.2f} {1/yon:12.2f} {Q(40,yon,frz(PHI_ON,-0.5)):10.4f} {Q(160,yon,frz(PHI_ON,-0.5)):10.4f}")
print("      ** a factor of two in the radiation budget barely moves it: the shape survives **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
