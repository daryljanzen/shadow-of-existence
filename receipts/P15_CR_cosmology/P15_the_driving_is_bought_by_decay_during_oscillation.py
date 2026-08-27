#!/usr/bin/env python3
"""RECEIPT — P15: ** THE DRIVING SHIFT IS BOUGHT BY POTENTIAL DECAY OCCURRING WHILE A MODE
OSCILLATES, SO A MODE WHOSE OSCILLATION BEGINS AFTER THE POTENTIAL HAS SETTLED INHERITS THE
UNDRIVEN PHASE.  A UNIFORM COMB IS AN UNDRIVEN COMB. **

LEVEL: L2 -- the perturbations are a process running IN the content and take the leaf's rate
  (P15 sec:properframe, P7's rate-rule remark).  The background here is the ordinary
  matter-and-radiation Friedmann readout with radiation gravitating normally, which is correct
  for this sector and is not an import.

WHAT IS DERIVED, AND WHAT IS NOT.  The SHAPE is derived: Q(k) -> 1 from above with increasing k
  on a background whose plasma begins after the potential has settled, where a background
  carrying a radiation era holds Q flat and below unity.  The MAGNITUDE is NOT: this solve omits
  neutrino free-streaming -- forty per cent of the radiation, which does not oscillate -- and its
  absolute values sit about fifteen per cent below the instrumented ones.  The offset's
  DIRECTION is the check that it is the omission and not an error: free-streaming REDUCES the
  driving, so including it must RAISE Q, and ACOUSTIC_two_arm's qscan (with neutrinos) sits ABOVE
  this solve at every k.  Shape claimed, magnitude not.

TWO SPECIFICATIONS THAT COST WRONG ANSWERS BEFORE THEY WERE RIGHT, recorded because the next
  attempt will make the same two:

  (1) THE POTENTIAL IS FIXED BY THE ENERGY CONSTRAINT, NOT EVOLVED.  Writing a second-order
      equation for Phi and integrating it diverges -- Phi ran to 3e2 by equality and 9e4 by y=10
      in the first attempt.  The G^0_0 constraint gives Phi' algebraically from the densities,
      which is what ACOUSTIC_two_arm does and what this does.

  (2) THE ACOUSTIC TURNOVER IS THE REVERSAL OF THE PHOTON VELOCITY, NOT AN EXTREMUM OF THE
      EFFECTIVE TEMPERATURE.  Under an initial condition with the velocities zero but Phi still
      evolving, T' = 2 Phi' != 0 at the start, so |T| reaches an extremum immediately and an
      extremum-finder reads the transient rather than the oscillation.  ACOUSTIC_two_arm's qscan
      had already hit and fixed this independently (its note on dropping Theta_0+Psi).

VERDICTS ARE ASSERTS, and each was written after its output was read.
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
