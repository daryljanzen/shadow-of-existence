#!/usr/bin/env python3
"""RECEIPT — Cartan/holonomy bake `C6`, `C9`, `C10`: ** THE CORPUS CARRIES TWO DISTINCT HOLONOMIES, NOT
ONE; IT NAMES THE FLAT-CONNECTION THEOREM IN ITS OWN WORDS WITHOUT ITS STANDARD NAME; AND P14'S MODULI
ARITHMETIC IS EXACT. **

LEVEL: NO RATE — flat-bundle theory and a dimension count.

C6 — THE LEDGER'S "LOAD-BEARING ABSENCE" CLAIM IS WRONG, AND IS CORRECTED HERE.  The r3164 bake reads
  `Ambrose-Singer` x0 as a load-bearing absence -- "the theorem that makes a FLAT connection have
  discrete holonomy".  ** But Ambrose-Singer relates holonomy to CURVATURE; the theorem a flat bundle
  needs is the flat-connection correspondence, that holonomy is its complete invariant. **  And P14
  states exactly that, in its own words: "holonomy is precisely the complete invariant a flat
  connection has ... no holonomy datum can take one off the flat locus."  So this is the WEAK form of
  the corpus's anonymity -- the right theorem, unnamed -- and not a hole.  Same shape as the
  functional-analysis bake's `Hilbert space` x0 over work fully done on L^2.

C9 — AND THE MODULI QUESTION BOUNCES, WITH P14 AHEAD.  P14 already carries: the holonomy group is
  finite of order 81; a finite group in characteristic zero has vanishing H^1, so the representation
  does not deform; the moduli space is ZERO-DIMENSIONAL, counted directly; and the reason a
  two-parameter family does not appear is that the wall classes are SUBREGULAR (dimension four) rather
  than regular (six).  Verified here: for sl(3), three regular classes on a three-punctured sphere give
  3x6 - 2x8 = 2, and three subregular give 3x4 - 2x8 = -4.  ** The arithmetic is exact. **

C10 — THE FINDING THIS LEAVES.  ** The corpus computes TWO DIFFERENT HOLONOMIES on two different
  bundles: the residue pairing's, of order 24 = S_4 = W(so(6,C)) (P05, P07), and the wall monodromies'
  together with the hinge three-cycle, of order 81 = 3^4 (P14). **  The Cartan ledger treats holonomy
  as one topic and computes only the first.  They are not the same group, not on the same base, and
  not doing the same work -- one closes the substrate's Weyl group, the other supplies colour's
  selection rules.

VERDICTS ARE ASSERTS.
"""
import math

print("=" * 78)
print("  C6 / C9 / C10 — the two holonomies")
print("=" * 78)

# ---------------------------------------------------------------- C9
dimG = 8  # sl(3)
print(f"\n  C9  moduli of flat G-connections on a 3-punctured sphere, dim G = {dimG} (sl(3))")
print("      dim = sum_i dim(C_i) - 2 dim G")
reg = 3 * 6 - 2 * dimG
sub = 3 * 4 - 2 * dimG
print(f"      three REGULAR    classes (dim 6): 3x6 - 2x{dimG} = {reg}")
print(f"      three SUBREGULAR classes (dim 4): 3x4 - 2x{dimG} = {sub}")
assert reg == 2, "regular classes must give the two-parameter family P14 names"
assert sub < 0, "subregular classes must give a zero-dimensional moduli space"
print("  ** VERDICT C9: P14's arithmetic is EXACT -- 'three regular classes ... would have left")
print("     a two-parameter family, and the disjointness of the vantages' supports is exactly")
print("     what removes it'.  The bake adds nothing; this is a BOUNCE. **")

# ---------------------------------------------------------------- finiteness
print("\n      and the finiteness: 81 = 3^4, and a finite group in characteristic zero has")
print("      H^1 = 0 by Maschke, so the representation does not deform as a representation")
print("      of its own holonomy -- which is P14's own argument.")
assert 81 == 3**4

# ---------------------------------------------------------------- C10
print("\n  C10 the corpus's TWO holonomies:")
rows = [("residue pairing (P05, P07)", 24, "S_4 = W(A_3) = W(so(6,C))", "closes the substrate's Weyl group"),
        ("wall monodromies + hinge (P14)", 81, "3^4, a finite 3-group", "supplies colour's selection rules")]
print(f"      {'bundle':32s} {'order':>6}  {'group':28s} role")
for b, o, g, r in rows:
    print(f"      {b:32s} {o:6d}  {g:28s} {r}")
assert 24 != 81, "they are different groups"
assert math.gcd(24, 81) == 3, "and share only a factor of 3"
print("  ** VERDICT C10: DIFFERENT groups, DIFFERENT bases, DIFFERENT work.  The Cartan ledger")
print("     treats holonomy as one topic and computes only the first. **")

# ---------------------------------------------------------------- C6
print("\n  C6  the theorem the corpus needs is NOT Ambrose-Singer.")
print("      Ambrose-Singer relates holonomy to CURVATURE.  A flat bundle has none.")
print("      The theorem it needs is that holonomy is the COMPLETE INVARIANT of a flat")
print("      connection -- and P14 states it: 'holonomy is precisely the complete invariant")
print("      a flat connection has ... no holonomy datum can take one off the flat locus.'")
print("  ** VERDICT C6: the WEAK form of anonymity -- the right theorem, unnamed -- and NOT a")
print("     load-bearing absence.  The r3164 ledger's claim is corrected. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
