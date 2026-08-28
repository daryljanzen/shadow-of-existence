#!/usr/bin/env python3
"""RECEIPT — harmonic-analysis bake `H14`: ** P16 FLAGS AN IDENTIFICATION AS UNESTABLISHED AND P15
CARRIES A MAP OF EXACTLY THAT KIND — WHICH IS NOT THE IDENTITY, AND DEVIATES MOST AT THE LOW
MULTIPOLES WHERE THE BOUND IS USED. **

LEVEL: NO RATE — the S^3-to-sky projection.

WHY THIS PROBE.  The fourth of the reach owed after r3453.  P16 carries this field's vocabulary x40
  and the bake had never read it.  P16 bounds the progenitor's radiation fraction,
  rho_r/rho_m <~ 1e-5, and then states its own assumption plainly: the bound rests "on the
  identification of the interior's harmonic index with the observed multipole -- AN IDENTIFICATION
  THIS PAPER DOES NOT ESTABLISH, so the figure is an order of magnitude with a stated assumption
  rather than a measurement."

  ** A paper naming its own unestablished assumption is the best kind of probe, and this field owns
  the object: index-to-multipole IS the S^3-to-sky projection. **

  ⛔ CORRECTED r3496, by the SPECTRAL-THEORY bake reading P16.  ** THIS PROBE QUOTED THE CLAUSE AND
  STOPPED AT THE FULL STOP.  The VERY NEXT SENTENCE supplies the map: "And the identification it
  rested on can be replaced by a map, both halves of which the corpus already carried ... the spatial
  section is S^3 throughout and the mode equation is diagonal in the harmonic index, so that index
  passes the branch point unchanged -- an integer eigenvalue label has nothing to rescale -- while on
  this side the companion paper's closed-S^3 projection sends mode L to l = sqrt(L(L+2)) D_C / r_0",
  with its own receipt P16_the_interior_to_observed_mode_map. **

  ** So the corpus does NOT lack the map, and this probe's framing was wrong.  What survives is a
  REFINEMENT: P16's map is l = k_L D_C exactly, and the computation below shows the actual projection
  peaks BELOW that -- 0.600 of it at l = 3, rising to 0.991 by l ~ 1000.  The map is right
  asymptotically and forty per cent off at the lowest multipoles, which is where the bound is used. **

WHAT IS SHOWN.  P15 carries a map of exactly that kind -- the closed-S^3 source projected through the
  flat spherical Bessel functions -- and it is NOT the identity.  A single mode at wavenumber k
  projects with weight (2l+1) j_l(k D_C)^2, which peaks at

      k D_C =    5   ->  l =   3    l/(k D_C) = 0.600
      k D_C =   10   ->  l =   8                0.800
      k D_C =   50   ->  l =  47                0.940
      k D_C =  200   ->  l = 195                0.975
      k D_C = 1000   ->  l = 991                0.991

  ** So the map is l ~ k D_C approached from BELOW, and the identification k <-> l is the identity
  only if D_C = 1 in the units used.  And the deviation is WORST AT LOW MULTIPOLE -- forty per cent at
  l = 3 -- which is exactly the range the corpus's low-multipole story occupies and where P16's bound
  is meant to bite. **

SO THE ASSUMPTION IS NOT MERELY UNESTABLISHED.  The corpus contains a map of the required kind, and
  that map says the simplest form of the identification is wrong, by a factor that is largest where
  the bound is used.  ** P16's caution is warranted, and it can be made specific rather than left
  general. **

ROUTED, NOT APPLIED.  P16's sentence can name where the map lives and what it costs, instead of
  leaving the identification unattributed.

VERDICTS ARE ASSERTS.
"""
import numpy as np
from scipy.special import spherical_jn

print("=" * 78)
print("  H14 — the index-to-multipole map P16 declines and P15 carries")
print("=" * 78)

print(f"\n  a single S^3 mode at k projects with weight (2l+1) j_l(k D_C)^2:")
print(f"  {'k D_C':>8}   {'peak l':>7}   {'ratio':>8}")
rows = []
for kD in (5.0, 10.0, 50.0, 200.0, 1000.0):
    ls = np.arange(1, int(3 * kD) + 40)
    lpk = int(ls[np.argmax((2 * ls + 1) * spherical_jn(ls, kD)**2)])
    rows.append((kD, lpk, lpk / kD))
    print(f"  {kD:8.0f}   {lpk:7d}   {lpk/kD:8.3f}")

assert all(r[2] < 1.0 for r in rows), "the peak must sit BELOW k D_C"
assert rows[0][2] < 0.7, "and the deviation must be large at low multipole"
assert rows[-1][2] > 0.98, "and small at high multipole"
print("  ** VERDICT 1: the map is l ~ k D_C approached from BELOW.  The identification")
print("     k <-> l is the identity only if D_C = 1 in the units used. **")

ratios = [r[2] for r in rows]
assert ratios == sorted(ratios), "the ratio must increase monotonically with k D_C"
print(f"\n  ** VERDICT 2: the deviation is WORST AT LOW MULTIPOLE -- {100*(1-rows[0][2]):.0f} per cent at")
print(f"     l = {rows[0][1]} -- which is exactly the range the corpus's low-multipole story")
print("     occupies and where P16's bound is meant to bite. **")

print("\n  ** VERDICT 3 (CORRECTED r3496): P16 SUPPLIES the map in its very next sentence --")
print("     l = sqrt(L(L+2)) D_C/r_0, with its own receipt.  This probe quoted the caveat")
print("     and stopped at the full stop.  What survives is a REFINEMENT: that map is")
print("     l = k_L D_C exactly, and the actual projection peaks BELOW it -- 0.600 of it")
print("     at l = 3 -- so it is right asymptotically and 40 per cent off at the lowest")
print("     multipoles, which is where the bound is used. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
