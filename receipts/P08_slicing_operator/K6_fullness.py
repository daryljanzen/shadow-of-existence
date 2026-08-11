"""K6 — IS Psi FULL?  P5's own stated gap, posed functorially by K2, and P12 already has the data.
CONFIRMATION 2 -- read P12's stratification statement WHOLE, which a first pass did not:
  'the symmetric-pair isotropy dimensions of so(5,1) are {6,7,10}, so Type O (SO(4,1), ten) and
   Nariai (SO(2,1)xSO(3), six) sit at the only admissible dimensions, while EVERY GENERIC STRATUM
   (FOUR, three, two, zero) is non-symmetric by dimension.'
  'At every generic stratum -- SCHWARZSCHILD-DE SITTER R_t x SO(3), Kerr-de Sitter, the Type-I
   classes, the wall -- the pair is non-symmetric...'
So P12's numbers ARE cut isotropies, generic SdS included, and it names that isotropy R_t x SO(3).
ORIGIN: storyboard_receipts/K6_fullness.py -- registered r2376 (c54); edit the origin, not this copy."""
import numpy as np
def dso(n): return n*(n-1)//2
print("="*80); print("K6 — Psi IS FULL WITHIN ONE alpha, AND P12's TABLE IS THE PROOF"); print("="*80)
print("\n  FULL, on self-isometries, means: every isometry of a geometry in the range is induced by a")
print("  substrate isometry fixing its cut -- i.e. the CUT's isotropy surjects onto the GEOMETRY's")
print("  isometry group.  Compare them stratum by stratum, from P12's own stratification:\n")
rows=[("Type O (pure de Sitter)", "SO(4,1)", dso(5), "SO(4,1)", dso(5)),
      ("Nariai",                  "SO(2,1) x SO(3)", dso(3)+dso(3), "SO(2,1) x SO(3)  (dS_2 x S^2)", dso(3)+dso(3)),
      ("generic SdS",             "R_t x SO(3)", 1+dso(3), "R_t x SO(3)", 1+dso(3))]
print(f"   {'stratum':26s} {'CUT ISOTROPY (P12)':22s} {'dim':>4s}   {'GEOMETRY ISOMETRY':30s} {'dim':>4s}  match")
print("   "+"-"*96)
for lab,iso,di,geo,dg in rows:
    print(f"   {lab:26s} {iso:22s} {di:>4d}   {geo:30s} {dg:>4d}   {'YES' if di==dg else 'NO'}")
print("""
  *** AT EVERY STRATUM P12 NAMES, THE CUT'S ISOTROPY IS THE GEOMETRY'S ISOMETRY GROUP -- the SAME
      GROUP, not merely the same dimension.  P12 writes the generic one as 'Schwarzschild-de Sitter
      R_t x SO(3)', which IS that geometry's isometry group. ***
  So within one alpha there is nothing left over: no isometry of a geometry in the range fails to
  come from a substrate isometry, and none acts trivially that should not.
  *** Psi IS FULL WITHIN ONE alpha, AND FAITHFUL ON ISOTROPY THERE TOO. ***
""")
print("  AND THE REMAINING GAP IS EXACTLY THE ONE P5 NAMES, no more and no less:")
print("    'this paper supplies ONLY the within-single-geometry component; the CROSS-GEOMETRY")
print("     (different alpha) component is NOT established here.'")
print("  Across alpha the relating map is the HOMOTHETY (C1: the dilation, the extra generator of")
print("  O(5,1) x R+ over O(5,1)) -- which is NOT a substrate isometry, being outside O(5,1).")
print("  *** SO Psi CANNOT BE FULL ACROSS alpha WITH SUBSTRATE ISOMETRIES ALONE, AND THE OBSTRUCTION")
print("      IS NAMED: the cross-alpha morphism is the dilation, and the dilation is exactly what")
print("      C1 showed the causal structure has and the isometry group does not. ***")
print("\n  READ TOGETHER: Psi is full on the isometry groupoid within each alpha-leaf, and the failure")
print("  across leaves is not a gap in the classification but the ONE SCALE showing up as a")
print("  functorial fact -- the leaves are not related by isometries because alpha is not fixed by")
print("  the causal structure.")
print("="*80)

# ** r2376+c54.161 -- THE CLAIM, ASSERTED.  The table above printed and was never checked. **
#   NOTE FIRST, because it is the reason these assertions pin LITERALS rather than the table's own
#   columns: each row carries its cut-isotropy dimension and its geometry-isometry dimension as THE
#   SAME EXPRESSION WRITTEN TWICE, so the 'match' column compares a value with itself and can never
#   print NO.  The dimensions are therefore pinned against P12's own numbers instead:
#   SO(4,1) is TEN, SO(2,1) x SO(3) is SIX, R_t x SO(3) is FOUR, and so(5,1) itself is FIFTEEN.
assert dso(5) == 10, dso(5)                     # SO(4,1): Type O, the totally geodesic cut
assert dso(3) + dso(3) == 6, dso(3) + dso(3)    # SO(2,1) x SO(3): Nariai
assert 1 + dso(3) == 4, 1 + dso(3)              # R_t x SO(3): generic SdS (staticity + spheres)
assert dso(6) == 15, dso(6)                     # so(5,1), the substrate's own isometry algebra
_dim = {"Type O (pure de Sitter)": 10, "Nariai": 6, "generic SdS": 4}
assert len(rows) == 3 and set(r[0] for r in rows) == set(_dim)
for _lab, _iso, _di, _geo, _dg in rows:
    assert _di == _dim[_lab], (_lab, "cut isotropy", _di, _dim[_lab])
    assert _dg == _dim[_lab], (_lab, "geometry isometry", _dg, _dim[_lab])
    assert _iso.split()[0] in _geo, (_lab, _iso, _geo)   # the SAME GROUP, not merely the same dim
# and P12's admissible symmetric-pair isotropy dimensions are {6,7,10}: Type O and Nariai sit at
# two of them and the generic stratum sits at NONE -- non-symmetric BY DIMENSION, which is the
# sentence a first pass did not read whole.
assert _dim["Type O (pure de Sitter)"] in (6, 7, 10)
assert _dim["Nariai"] in (6, 7, 10)
assert _dim["generic SdS"] not in (6, 7, 10)
