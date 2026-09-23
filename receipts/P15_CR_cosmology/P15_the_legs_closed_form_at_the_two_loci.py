#!/usr/bin/env python3
"""
RECEIPT -- P15: ** THE LEG'S CLOSED FORM READ AT THE TWO LOCI.  AT THE CROSSING IT IS THE ORDINARY
FROZEN ADIABATIC STATE EXACTLY -- Theta_hat = Psi_i/2, Psi = Psi_i -- AND THE HANDOVER AMPLITUDE THE
INSTRUMENT CODES, 0.4835 Psi_i, IS Psi(entry)/2 AT NEITHER LOCUS. **

Built r6760+cc66.1 (node 66, code seat), on `PO-13`.

===================================================================================================
** WHAT WAS ASKED, AND WHY IT IS ANSWERABLE IN CLOSED FORM **
===================================================================================================

`sec:envelope` gives the collapse leg's potential in closed form -- Psi'' + (4/eta)Psi' + (k^2/3)Psi
= 0, regular solution Psi = 3 Psi_i (sin x - x cos x)/x^3 = Psi_i T(x), x = k eta/sqrt3 -- and shows
that Theta_hat = Theta_0 + Psi obeys Theta_hat'' + (k^2/3) Theta_hat = 0 exactly.  ** So both
quantities are elementary functions of x at every point of the leg, and the two loci the handover
could sit at can be compared by evaluation rather than by argument. **

  PART 1  ** THE MAP, taken from `C4_driving_envelope` verbatim rather than rebuilt. **
  PART 2  ** THE TWO LOCI. **  At the CROSSING (r -> 0, x -> 0) the regular solution is anchored:
          Psi = Psi_i exactly, and the adiabatic super-horizon relation Theta_0 = -Psi/2 gives
          Theta_hat = Psi_i/2 exactly.  At the SEAM (r = alpha/sqrt3) both are k-dependent:
          x_seam = 0.7638 (k/k_s), Psi has decayed below half a per cent for k >= 10 k_s, and
          Theta_hat is at an arbitrary point of a free oscillation whose ENVELOPE is Psi_i/2.
  PART 3  ** AND THE CODED HANDOVER AMPLITUDE IS NEITHER. **  `CRAMP=flat` sets Theta_hat =
          -T(1/sqrt3)/2 = 0.48356 Psi_i, which is Psi at HORIZON ENTRY halved -- `C4` STEP 3's
          "Theta_hat(entry) = Psi(entry)/2".  ** The exact free solution gives Theta_hat(entry) =
          (Psi_i/2) cos(1/sqrt3) = 0.41896 Psi_i and an envelope of 0.5 Psi_i. **  The three differ:
          0.48356 is the potential at entry, 0.41896 is the temperature at entry, 0.5 is the
          envelope and the value at the crossing.
  PART 4  ** THE INDEPENDENT CHECK. **  Theta_0's own driven equation integrated directly, with no
          Theta_hat substitution, reproduces (Psi_i/2) cos x.

** WHAT THIS IS NOT. **  Not a claim that the instrument's 0.4835 is wrong for the locus it is
imposed at -- that is a separate question about the ONSET, and this receipt does not touch it.  Not
a claim about the spectrum.  ** What is established is arithmetic: the three candidate amplitudes and
where each comes from. **

** COMPUTES: the leg's closed form at alpha = 1, M = 1/(3 sqrt3), r_seam = 1/sqrt3, A = 4 M r_seam --
   the map C4_driving_envelope uses -- over k/k_s = 1 to 300.  *** The construction has one scale and
   these are its pure numbers, so there is no parameter to have chosen otherwise; the k-ladder is the
   only input and it is stated. *** **

rc=0 on success.  Run: python3 <this file>   (numpy, scipy; ~3 s)
"""
import sys

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

print(__doc__.split("rc=0")[0])
fail = []

# ---- PART 1: the map, from C4_driving_envelope ---------------------------------------------------
M = 1.0 / (3 * np.sqrt(3))          # the Nariai mass parameter in alpha = 1 units
RS = 1.0 / np.sqrt(3)               # the seam, r = alpha/sqrt3
A = 4 * M * RS                      # the leg's radiation constant
rH = lambda r: np.sqrt(A / r ** 2 + 2 * M / r + r ** 2)
KS = rH(RS)                         # the seam's own comoving Hubble scale


def T(x):
    x = float(x)
    return 1 - x * x / 10 + x ** 4 / 280 if x < 0.05 else \
        3 * (np.sin(x) - x * np.cos(x)) / x ** 3


def Tp(x):
    x = float(x)
    return -x / 5 + x ** 3 / 70 if x < 0.05 else \
        3 * (x * x * np.sin(x) - 3 * (np.sin(x) - x * np.cos(x))) / x ** 4


print("=" * 78)
print("PART 1 — THE MAP (alpha = 1), from C4_driving_envelope")
print("=" * 78)
print(f"  M = {M:.6f}   r_seam = {RS:.6f}   A_leg = 4 M r_seam = {A:.6f}")
print(f"  k_s = rH(r_seam) = {KS:.6f}   eta = r/sqrt(A)   x = k eta/sqrt3")
print(f"  ** x_seam = {RS/np.sqrt(A)/np.sqrt(3):.6f} k = {RS/np.sqrt(A)/np.sqrt(3)*KS:.6f} (k/k_s) **")
if abs(RS / np.sqrt(A) / np.sqrt(3) - 0.5) > 1e-12:
    fail.append("x_seam is not exactly k/2 in these units")

# ---- PART 2: the two loci ------------------------------------------------------------------------
print()
print("=" * 78)
print("PART 2 — THE TWO LOCI")
print("=" * 78)
print("  ** THE CROSSING, r -> 0, x -> 0 — where the regular solution is anchored: **")
print(f"     Psi/Psi_i       = T(0)                 = {T(0.0):.6f}")
print(f"     Theta_hat/Psi_i = 1/2 (Theta_0 = -Psi/2) = {0.5:.6f}")
if abs(T(0.0) - 1.0) > 1e-12:
    fail.append("T(0) != 1 -- the regular solution is not anchored at the crossing")
print()
print("  ** THE SEAM, r = alpha/sqrt3 — both k-dependent: **")
hdr = (f"     {'k/k_s':>7} {'x_entry':>9} {'x_seam':>10} {'Psi(seam)/Psi_i':>16} "
       f"{'Theta^(seam)':>13} {'envelope':>9}")
print(hdr)
print("     " + "-" * (len(hdr) - 5))
for kk in (1, 2, 5, 10, 30, 100, 300):
    k = kk * KS
    r_e = brentq(lambda z: rH(z) - k, 1e-12, RS)
    x_e = k * (r_e / np.sqrt(A)) / np.sqrt(3)
    x_s = k * (RS / np.sqrt(A)) / np.sqrt(3)
    print(f"     {kk:>7} {x_e:>9.5f} {x_s:>10.4f} {T(x_s):>16.6f} {0.5*np.cos(x_s):>+13.6f} "
          f"{0.5:>9.6f}")
    if kk >= 10 and abs(T(x_s)) > 0.005:
        fail.append(f"Psi at the seam is {T(x_s):.4f} at k = {kk} k_s -- sec:envelope says below a per cent")
    if kk >= 30 and abs(x_e - 1 / np.sqrt(3)) > 0.005:
        fail.append(f"x_entry is {x_e:.5f} at k = {kk} k_s -- sec:envelope's limit is 1/sqrt3")

# ---- PART 3: the three candidate amplitudes ------------------------------------------------------
xe = 1.0 / np.sqrt(3)
A_coded, A_exact_entry, A_env = T(xe) / 2, 0.5 * np.cos(xe), 0.5
print()
print("=" * 78)
print("PART 3 — THE THREE CANDIDATE AMPLITUDES, AND WHERE EACH COMES FROM")
print("=" * 78)
print(f"  Psi(entry)/2        = T(1/sqrt3)/2       = {A_coded:.6f}   <- CRAMP=flat, the coded handover")
print(f"  Theta_hat(entry)    = (1/2) cos(1/sqrt3) = {A_exact_entry:.6f}   <- the exact free solution AT entry")
print(f"  Theta_hat envelope  = 1/2                = {A_env:.6f}   <- the crossing value, and the envelope")
print(f"\n  ** the coded value sits {100*(A_coded-A_env)/A_env:+.2f}% from the envelope and "
      f"{100*(A_coded-A_exact_entry)/A_exact_entry:+.2f}% from the temperature at entry. **")
print("     *All three are readings of sec:envelope; they are not the same number and the paper's")
print("      'the same driving amplitude Psi(1/sqrt3)/2' names the first.*")
if abs(A_coded - 0.48356) > 1e-4:
    fail.append(f"T(1/sqrt3)/2 = {A_coded:.6f}, not the instrument's 0.4835")

# ---- PART 4: the independent check ---------------------------------------------------------------
print()
print("=" * 78)
print("PART 4 — Theta_0's OWN DRIVEN EQUATION, INTEGRATED DIRECTLY")
print("=" * 78)
print("  Psi'' + (4/x)Psi' + Psi = 0  =>  Theta_0'' + Theta_0 = -Psi - Psi'' = (4/x) Psi'")
x0 = 0.02
s = solve_ivp(lambda x, y: [y[1], -y[0] + 4.0 * Tp(x) / x], [x0, 23.5],
              [-0.5 * T(x0), -0.5 * Tp(x0)], rtol=1e-9, atol=1e-12, dense_output=True)
print(f"  {'x':>10} {'Theta_0':>12} {'Psi':>12} {'Theta_hat':>12} {'(1/2)cos x':>12} {'|diff|':>10}")
worst = 0.0
for x in (xe, 0.7638, 1.5275, 3.8188, 7.6376, 22.9129):
    th0 = float(s.sol(x)[0]); ps = T(x); d = abs(th0 + ps - 0.5 * np.cos(x))
    worst = max(worst, d)
    print(f"  {x:>10.4f} {th0:>+12.6f} {ps:>+12.6f} {th0+ps:>+12.6f} {0.5*np.cos(x):>+12.6f} {d:>10.2e}")
print(f"\n  ** agreement to {worst:.1e} — and the residual is NOT round-off: it is a homogeneous")
print("     mode excited by the FIRST-ORDER error in the starting velocity, and it is measured. **")
print("     *The adiabatic relation Theta_0 = -Psi/2 differentiates to -Psi'/2, while the exact")
print("      Theta_0' = -(1/2)sin x - Psi' ; the difference at x0 is 0.4 x0 to leading order.*")
print(f"     {'x0':>8} {'worst |diff|':>14} {'diff / x0':>11}")
_sc = []
for _x0 in (0.04, 0.02, 0.01, 0.005):
    _s = solve_ivp(lambda x, y: [y[1], -y[0] + 4.0 * Tp(x) / x], [_x0, 23.5],
                   [-0.5 * T(_x0), -0.5 * Tp(_x0)], rtol=1e-10, atol=1e-13, dense_output=True)
    _w = max(abs(float(_s.sol(x)[0]) + T(x) - 0.5 * np.cos(x))
             for x in (xe, 1.5275, 7.6376, 22.9129))
    _sc.append(_w / _x0)
    print(f"     {_x0:>8} {_w:>14.3e} {_w/_x0:>11.4f}")
print(f"  ** the ratio is {np.mean(_sc):.4f} at every step and the residual vanishes with x0 — so the")
print("     identity Theta_hat = (Psi_i/2) cos x is exact and the departure is the starting data. **")
if max(_sc) - min(_sc) > 0.01:
    fail.append("the residual does not scale linearly in x0 -- it is not the starting-velocity error")
if abs(np.mean(_sc) - 0.4) > 0.02:
    fail.append(f"the residual/x0 is {np.mean(_sc):.4f}, not the predicted 0.4")

print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — the crossing carries Psi = Psi_i and Theta_hat = Psi_i/2 exactly; the seam")
print("carries a decayed potential and a free oscillation of envelope Psi_i/2; and the coded 0.4835")
print("is Psi at horizon entry halved, which is neither locus.")
print("=" * 78)
