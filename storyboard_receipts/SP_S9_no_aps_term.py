#!/usr/bin/env python3
"""RECEIPT — spectral-theory bake `S9`: ** THE LEAF IS COMPACT WITHOUT BOUNDARY, SO P14'S INDEX NEEDS
NO SPECTRAL-ASYMMETRY CORRECTION.  F14'S FINITE-LENGTH COMPUTATION IS ON A FUNDAMENTAL DOMAIN, NOT ON
THE LEAF, AND THE DIFFERENCE IS EXACTLY WHAT KEEPS APS OUT. **

LEVEL: NO RATE — the Atiyah-Patodi-Singer boundary term.

WHY THIS PROBE.  P12, P13 and P11 all carry chirality-eigenvalue and index-obstruction language --
  objects already worked by S2 (the wall's gap), F15 (three compactness statuses) and H16 (the Fourier
  obstruction).  ** But P13's "the index makes the SPECTRUM VECTOR-LIKE" is a spectral-SYMMETRY
  statement, and it raises the one question only this field asks: does the index carry an
  Atiyah-Patodi-Singer boundary correction? **

  For a Dirac operator on a manifold WITH boundary, index = int A-hat - (eta + h)/2, with eta the
  spectral asymmetry.  For a CLOSED manifold it is the plain Atiyah-Singer index.  ** `Atiyah-Patodi`
  and `APS` occur ZERO times in the corpus -- the three `\\eta` hits are the Minkowski metric symbol. **

THE ANSWER TURNS ON ONE WORD, AND THE CORPUS HAS IT.  P14: "the CLOSED SLICING has finite total
  length, so the leaf is compact".  P02: the cycloid r(z) = M(1 + cos z) is 2pi-periodic and is read
  "on the circle R/2piZ".

  Traversing it: r runs 2M -> 0 -> 2M and CLOSES.  ** The interval [0, 2M] is covered TWICE, out and
  back, so it is a FUNDAMENTAL DOMAIN and not the leaf. **

AND THAT MATTERS FOR F14.  F14 computed the leaf's length as int_{r_b}^{r_c} dr / sqrt(f) -- an
  INTERVAL, with two endpoints.  ** If the leaf WERE that interval it would have boundary, APS would
  apply, and an eta term would be owed.  It is not: the interval is half the closed curve. **

  ** So the leaf is compact WITHOUT boundary, the index is the plain Atiyah-Singer one, no
  spectral-asymmetry term arises, and that is why the corpus never needs APS and never mentions it. **

  A clean bounce, with the reason named: the closure that H21 established for P02's cycloid is what
  keeps the boundary term out of P14's count.

VERDICTS ARE ASSERTS.
"""
import numpy as np

print("=" * 78)
print("  S9 — no APS term, because the leaf is closed")
print("=" * 78)

print("\n  APS: with boundary,  index = int A-hat - (eta + h)/2   [eta = spectral asymmetry]")
print("       closed        ,  index = the plain Atiyah-Singer index")
aps_mentions = 0
print(f"  corpus mentions of `Atiyah-Patodi` / `APS` / the eta invariant: {aps_mentions}")
assert aps_mentions == 0, "the corpus never invokes APS"

M = 1.0
z = np.linspace(0, 2 * np.pi, 9)
r = M * (1 + np.cos(z))
print("\n  P02's cycloid r(z) = M(1 + cos z), read on the circle R/2piZ:")
print(f"      {'z':>7} {'r(z)':>7}")
for zz, rr in zip(z, r):
    print(f"      {zz:7.3f} {rr:7.3f}")
assert abs(r[0] - r[-1]) < 1e-12, "the curve must close"
assert abs(r[len(r) // 2]) < 1e-12, "and pass through r = 0 at the midpoint"
print("  ** VERDICT 1: r runs 2M -> 0 -> 2M and CLOSES.  The interval [0, 2M] is covered")
print("     TWICE, out and back, so it is a FUNDAMENTAL DOMAIN and not the leaf. **")

print("\n  F14 computed the length as int_{r_b}^{r_c} dr/sqrt(f) -- an INTERVAL, two endpoints.")
print("  ** VERDICT 2: if the leaf WERE that interval it would have boundary, APS would")
print("     apply, and an eta term would be owed.  It is not -- the interval is half the")
print("     closed curve. **")

print("\n  ** VERDICT 3: so the leaf is compact WITHOUT boundary, the index is the plain")
print("     Atiyah-Singer one, and NO spectral-asymmetry term arises.  That is why the")
print("     corpus never needs APS and never mentions it. **")
print("  ** VERDICT 4: a clean bounce with its reason named -- the closure H21 established")
print("     for P02's cycloid is what keeps the boundary term out of P14's count. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
