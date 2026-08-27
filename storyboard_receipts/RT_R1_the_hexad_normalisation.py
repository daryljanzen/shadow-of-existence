#!/usr/bin/env python3
"""RECEIPT — representation-theory bake `R1`: ** P03'S NARIAI TRIPLE IS A GENUINE FUNDAMENTAL WEIGHT
SYSTEM IN ITS DIRECTIONS AND AN A_2 ROOT IN ITS LENGTH.  THE TWO DIFFER BY EXACTLY sqrt(3). **

LEVEL: NO RATE — finite-dimensional representation theory and the horizon cubic's roots.

P03 sec:cubic states: "The six Nariai marks are the A_2 hexad.  The three at 2M = +2/(3 sqrt3)
  (w = 30, 150, 270 deg) carry the root triple (-2,1,1)/sqrt3 -- THE THREE WEIGHTS OF A FUNDAMENTAL 3."

WHAT IS CONFIRMED.  The three marks carry the three CYCLIC PERMUTATIONS, which are three distinct
  vectors summing to zero and permuted by S_3.  That is a genuine fundamental weight system, and the
  identification is right in its directions and its symmetry.

WHAT IS OFF, AND IT IS EXACT.  The vectors have |v|^2 = 2, which is the A_2 ROOT length.  The true
  weights of the fundamental have |v|^2 = 2/3.  The ratio is sqrt(3).  So P03's triple lies along the
  weight directions at ROOT scale -- and it is not itself a root either, since the A_2 roots in this
  realisation are the differences e_i - e_j.

  ** THREE DISTINCT OBJECTS, ONE WORD.  The corpus's own receipt P03_the_adjoint_is_entailed
  establishes the hexad as the six DIFFERENCES e_i - e_j, which are the roots.  P03's prose calls the
  six NARIAI MARKS the A_2 hexad and reads them as 3 + 3bar, which are weights.  Roots and weights of
  A_2 are different hexagons: same centre, rotated 30 degrees, scaled by sqrt(3). **

A WORRY RAISED AND WITHDRAWN, recorded because it cost a step: at Nariai the cubic has a DOUBLE root,
  (-1.1547, 0.5774, 0.5774), so the multiset is degenerate while a fundamental's weights are always
  distinct.  That is not a contradiction -- the three MARKS carry three distinct ORDERED triples, the
  cyclic permutations, and the degeneracy is of the multiset and not of the weight system.

VERDICTS ARE ASSERTS.
"""
import numpy as np
import sympy as sp

print("=" * 78)
print("  R1 — the Nariai triple: weight directions, root length")
print("=" * 78)

sq3 = np.sqrt(3)
marks = [np.array(v) / sq3 for v in [(-2, 1, 1), (1, -2, 1), (1, 1, -2)]]
weights = [np.array(v) / 3.0 for v in [(-2, 1, 1), (1, -2, 1), (1, 1, -2)]]
n = lambda v: float(np.dot(v, v))

print("\n  the three Nariai marks at 2M = +2/(3 sqrt3), w = 30, 150, 270 deg:")
for m in marks:
    print(f"      {np.round(m, 4)}   |v|^2 = {n(m):.4f}")
assert np.allclose(sum(marks), 0), "a weight system must sum to zero"
print(f"  sum = {np.round(sum(marks), 12)}  -> sums to zero")

seen = {tuple(np.round(np.sort(m), 6)) for m in marks}
assert len(seen) == 1, "the three marks must be permutations of one triple"
assert len({tuple(np.round(m, 6)) for m in marks}) == 3, "and must be three DISTINCT vectors"
print("  ** VERDICT 1: three distinct vectors, one S_3 orbit, summing to zero --")
print("     a genuine fundamental weight system.  P03's directions and symmetry are right. **")

print(f"\n  |mark|^2            = {n(marks[0]):.4f}")
print(f"  |true 3 weight|^2   = {n(weights[0]):.4f}   (= 2/3)")
ratio = np.sqrt(n(marks[0]) / n(weights[0]))
assert abs(ratio - sq3) < 1e-12, "the discrepancy must be exactly sqrt(3)"
print(f"  ratio of lengths    = {ratio:.6f}  = sqrt(3)")

roots = [np.array(v) for v in [(1, -1, 0), (-1, 1, 0), (1, 0, -1), (-1, 0, 1), (0, 1, -1), (0, -1, 1)]]
assert abs(n(roots[0]) - n(marks[0])) < 1e-12, "the marks must carry ROOT length"
assert not any(np.allclose(marks[0], r) for r in roots), "but must not BE roots"
print("  ** VERDICT 2: the marks carry the A_2 ROOT length exactly, and are not roots --")
print("     they lie along the WEIGHT directions at ROOT scale, off by sqrt(3). **")

rh = sorted(tuple(np.round(r, 6)) for r in roots)
wh = sorted(tuple(np.round(w, 6)) for w in weights + [-w for w in weights])
assert rh != wh, "root hexad and weight hexad must be distinct figures"
print("  ** VERDICT 3: the root hexad and the 3+3bar weight hexad are DIFFERENT hexagons --")
print("     same centre, rotated 30 degrees, scaled by sqrt(3).  The corpus calls both 'the")
print("     A_2 hexad', and its own receipt P03_the_adjoint_is_entailed uses the root one. **")

r = sp.symbols('r')
M2 = 2 / (3 * sp.sqrt(3))
rts = sorted(complex(x).real for x in sp.Poly(r**3 - r + M2, r).nroots())
print(f"\n  the withdrawn worry: at Nariai the cubic's roots are {[round(x,4) for x in rts]}")
assert abs(rts[1] - rts[2]) < 1e-9, "Nariai is a double root"
assert len({tuple(np.round(m, 6)) for m in marks}) == 3
print("     -- a DOUBLE root, so the multiset is degenerate.  Not a contradiction: the three")
print("     MARKS carry three distinct ORDERED triples.  Raised, checked, withdrawn.")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
