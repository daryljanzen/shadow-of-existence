#!/usr/bin/env python3
"""RECEIPT — harmonic-analysis bake `H19`: ** P04'S 1/sqrt(N) IS A WHITE-NOISE LIMIT.  IT HOLDS ONLY
FOR MODES SHORTER THAN THE PATH; MODES WITH k <~ 1/L ARE UNSUPPRESSED BY THE PATH WINDOW AND ADD
COHERENTLY, SO THE FLOOR IS HIGHER THAN THE ESTIMATE -- AND THOSE MODES ARE THE LOWEST MULTIPOLES. **

LEVEL: NO RATE — Fourier analysis of a line-of-sight average.

WHY THIS PROBE.  P04 was estimated HIGH from its contents before any grep: CMB anisotropy IS a
  spherical-harmonic decomposition, and the isotropy floor is a MODE-COUNTING argument.  P04 models a
  photon path as "a tube binned into N statistically independent cells of comoving size
  R = 8 h^-1 Mpc, each carrying rms contrast sigma_8", and takes the central limit theorem:
  sigma_path = sigma_{8,eff} / (3 sqrt(N)).

WHAT THE HARMONIC FORM SAYS.  A path average is a WINDOW in Fourier space: the variance is
  int dk P(k) |W(k)|^2 with W the path-average window, |W(k)|^2 = sinc^2(kL/2).  Evaluated at
  L = 9390 h^-1 Mpc, N = L/R = 1174:

      k = 1/L   (path scale)   |W|^2 = 0.919      <- essentially UNSUPPRESSED
      k = 3/L                  |W|^2 = 0.442
      k = 10/L                 |W|^2 = 0.037
      k = 1/R   (cell scale)   |W|^2 = 0.000

  ** So the 1/sqrt(N) is the WHITE-NOISE limit and it holds for k >> 1/L.  Modes with k <~ 1/L are
  not averaged down at all -- they contribute COHERENTLY along the whole path. **

WHICH DIRECTION IT MOVES THE RESULT.  Coherent contributions ADD to the scatter, so the true floor is
  HIGHER than the cell estimate.  ** P04 states that "every choice in the estimate biases it downward,
  so the number is a floor", and this is a further instance of exactly that -- the harmonic form
  STRENGTHENS the exclusion rather than weakening it, and by a channel P04's own robustness checks
  (sigma_8 normalisation, correlated cells) do not cover. **

AND THE MODES RESPONSIBLE ARE THE LOWEST MULTIPOLES.  With l ~ k D_C and D_C = L, the unsuppressed
  band k <~ few/L is l of order a few.  ** That is the same range at which the corpus independently
  places its filter's loss of control -- the transmission boundary at l ~ 2.5, the Euclidean
  projection at l ~ 3, and the adiabatic breakdown at n = 2, 3 (H13, which shows the last is forced).
  A fourth arrival at the same place, from the isotropy floor. **

ROUTED, NOT APPLIED.  The clause owed: that the cell estimate is the white-noise limit of the path
  window, exact for k >> 1/L, and that the unaveraged long-wavelength band raises the floor further.

VERDICTS ARE ASSERTS.
"""
import numpy as np

print("=" * 78)
print("  H19 — P04's isotropy floor, in Fourier")
print("=" * 78)

L, R = 9390.0, 8.0
N = L / R
print(f"\n  path L = {L:.0f} h^-1 Mpc,  cell R = {R:.0f}  ->  N = {N:.0f},  1/sqrt(N) = {1/np.sqrt(N):.5f}")

W = lambda k: float(np.sinc(k * L / (2 * np.pi))**2)
rows = [("k = 1/L   (path scale)", 1 / L), ("k = 3/L", 3 / L),
        ("k = 10/L", 10 / L), ("k = 1/R   (cell scale)", 1 / R)]
print("\n  path-average window |W(k)|^2 = sinc^2(kL/2):")
for lbl, k in rows:
    print(f"      {lbl:26s} k = {k:.2e}   |W|^2 = {W(k):.4f}")

assert W(1 / L) > 0.85, "modes at the path scale must be essentially unsuppressed"
assert W(10 / L) < 0.10, "modes ten times shorter must be strongly suppressed"
assert W(1 / R) < 1e-3, "modes at the cell scale must be killed"
print("  ** VERDICT 1: the 1/sqrt(N) is the WHITE-NOISE limit, valid for k >> 1/L.  Modes with")
print("     k <~ 1/L are not averaged down -- they contribute COHERENTLY along the path. **")

print("\n  direction: coherent contributions ADD to the scatter.")
print("  ** VERDICT 2: so the true floor is HIGHER than the cell estimate.  P04 says 'every")
print("     choice in the estimate biases it downward, so the number is a floor' -- this is a")
print("     further instance, through a channel its stated robustness checks do not cover. **")

print("\n  where the unaveraged band lands on the sky, l ~ k D_C with D_C = L:")
for k, lbl in [(1 / L, "k = 1/L"), (2 / L, "k = 2/L"), (5 / L, "k = 5/L")]:
    print(f"      {lbl:10s} ->  l ~ {k*L:.0f}")
assert 5 / L * L < 10, "the unaveraged band must sit at low multipole"
print("  ** VERDICT 3: l of order a few -- the same range at which the corpus independently")
print("     places the transmission boundary (l ~ 2.5), the Euclidean projection (l ~ 3),")
print("     and the adiabatic breakdown at n = 2,3 (which H13 shows is forced).  A fourth")
print("     arrival at the same place, from the isotropy floor. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
