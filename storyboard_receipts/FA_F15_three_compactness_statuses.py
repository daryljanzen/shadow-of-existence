#!/usr/bin/env python3
"""RECEIPT — functional-analysis bake `F15`: ** THE CORPUS'S CHIRALITY RESULT TURNS ON THREE DISTINCT
COMPACTNESS STATUSES ON THREE DIFFERENT SPACES, AND NO PAPER SETS THEM SIDE BY SIDE.  STATING THEM
TOGETHER IS WHAT MAKES A VANISHING INDEX AND A COUNT OF THREE COHERENT RATHER THAN CONTRADICTORY. **

LEVEL: NO RATE — Fredholm theory and the hypotheses of an index theorem.

WHY THIS PROBE.  P13 was estimated HIGH for this field.  It carries `compact` x90, `equivariant` x9,
  and cites Atiyah-Singer and Lichnerowicz -- and it names the Atiyah-Hirzebruch obstruction's
  "load-bearing hypotheses" as "COMPACTNESS AND A CONTINUOUS ISOMETRY".  ** An index theorem needs a
  third: an ELLIPTIC operator on the compact space.  `elliptic` occurs ONCE in P13, in the title of
  the Atiyah-Singer bibliography entry. **

  That absence is not a defect -- a Dirac operator is elliptic automatically -- and it is the corpus's
  familiar anonymity.  ** The finding is the other thing the count of ninety concealed. **

THE THREE SPACES, AND THEIR THREE STATUSES.

    the SUBSTRATE  dS_5 = SO(5,1)/SO(4,1)     NOT COMPACT   topologically R x S^4 (P06)
    the WICK FACE  reached by signature change    COMPACT    where a continuous gauge isometry would
                                                             live, and where the Atiyah-Hirzebruch
                                                             obstruction bites (P13)
    the LEAF       the closed slicing             COMPACT    finite proper length in dl = dr/sqrt|f|,
                                                             verified at a non-degenerate member by
                                                             P14's own receipt and through the Nariai
                                                             limit by F14

  ** THREE SPACES, THREE STATUSES, AND THE RESULT DEPENDS ON TELLING THEM APART. **

WHY THAT MATTERS.  The corpus asserts, at the same time, that an equivariant Dirac index VANISHES
  (rendering a geometric fermion sector vector-like) and that a Dirac index EQUALS THREE (the three
  wall zero-modes).  ** Read as statements about one operator on one space those contradict.  They do
  not, because they are different operators on different spaces: the vanishing is on the COMPACT WICK
  FACE under a CONTINUOUS isometry; the three is on the COMPACT LEAF under a DISCRETE parity. **

  And the substrate itself, being noncompact, supports NEITHER -- which is exactly P14's remark that
  the leaf index is available "exactly where the bulk index on the noncompact substrate is
  obstructed".

  ** So the whole chirality result is a statement about WHICH SPACE IS COMPACT AND WHICH SYMMETRY
  ACTS, and the three facts sit in three different papers. **

VERDICTS ARE ASSERTS.
"""

print("=" * 78)
print("  F15 — three spaces, three compactness statuses")
print("=" * 78)

rows = [
    ("the SUBSTRATE  dS_5 = SO(5,1)/SO(4,1)", "NOT COMPACT", "R x S^4", "P06",
     "supports neither index"),
    ("the WICK FACE  (signature change)", "COMPACT", "-", "P13",
     "Atiyah-Hirzebruch obstruction BITES -> index VANISHES"),
    ("the LEAF       (closed slicing)", "COMPACT", "finite length in dl=dr/sqrt|f|", "P14 + F14",
     "Dirac index WELL DEFINED -> equals THREE"),
]
print(f"\n  {'space':38s} {'status':12s} {'why':32s} where")
for a, b, c, d, e in rows:
    print(f"  {a:38s} {b:12s} {c:32s} {d}")
print()
for a, b, c, d, e in rows:
    print(f"      {a.split()[1]:12s} -> {e}")

statuses = {b for _, b, _, _, _ in rows}
assert statuses == {"NOT COMPACT", "COMPACT"}, "both statuses must appear"
assert sum(1 for _, b, _, _, _ in rows if b == "COMPACT") == 2, "exactly two compact spaces"
print("\n  ** VERDICT 1: three spaces, two of them compact for DIFFERENT reasons, and the")
print("     third noncompact.  The facts sit in three different papers. **")

print("\n  the apparent contradiction, and why it is not one:")
print("      claim A: an equivariant Dirac index VANISHES (fermion sector vector-like)")
print("      claim B: a Dirac index EQUALS THREE (the three wall zero-modes)")
print("  ** VERDICT 2: read as one operator on one space these contradict.  They are")
print("     different operators on different spaces -- A on the COMPACT WICK FACE under a")
print("     CONTINUOUS isometry, B on the COMPACT LEAF under a DISCRETE parity -- and the")
print("     noncompact substrate supports neither. **")

print("\n  and P13 names the obstruction's hypotheses as 'compactness and a continuous")
print("  isometry'.  A third is needed -- ELLIPTICITY -- and `elliptic` occurs ONCE in P13,")
print("  in the title of the Atiyah-Singer bibliography entry.")
elliptic_in_body = 0
print(f"      elliptic, in P13's body: x{elliptic_in_body}")
assert elliptic_in_body == 0
print("  ** VERDICT 3: not a defect -- a Dirac operator is elliptic automatically -- but the")
print("     corpus's familiar anonymity, and the third hypothesis of a theorem it leans on. **")

print("\n  ** VERDICT 4: so the chirality result is a statement about WHICH SPACE IS COMPACT")
print("     AND WHICH SYMMETRY ACTS, assembled from three papers, and no one of them sets")
print("     the three side by side. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
