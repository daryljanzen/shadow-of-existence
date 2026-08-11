"""
P14_a_labelling_not_a_gauging.py -- P14 sec:whichthree / sec:openquestions: the two-bit match
between the turnaround's four colourless characters and the lepton content of a sixteen-fermion
generation is a LABELLING result, not a GAUGE result -- and saying so is forced by an arithmetic
fact about $SU(2)_L$ that the corpus had not put beside it.

WHAT PROMPTED IT.  A standing discharge condition for the sector asks for "an isospin grading: a
doublet plus a singlet", and an earlier turn withdrew that clause on the ground that "against the
sixteen the gradings agree", exhibiting chirality and species.  Both of those split the four
leptons $2+2$; $SU(2)_L$ does not.

WHAT IS ESTABLISHED.
  1. ** SPECIES AND ISOSPIN ARE DIFFERENT PARTITIONS OF THE SAME FOUR STATES. **  Chirality and
     species each give $2+2$ (asserted); $SU(2)_L$ decomposes the four as doublet plus two
     inequivalent singlets, $2+1+1$ (asserted), because it does not distinguish $\\nu_R$ from
     $e_R$ at all -- both are singlets with $T_3=0$ -- while the species bit does.
  2. ** SO NO $\\mathbb{Z}_2$ GRADING CAN REPRODUCE $SU(2)_L$'s DECOMPOSITION. **  A grading by a
     one-dimensional character is a function to $\\{+1,-1\\}$ and its blocks are its fibres, so it
     has at most two; $2+1+1$ has three (asserted).  A clause demanding that shape from a
     character count asks for something no character count on a finite group can deliver -- not
     from a deficiency of this construction but from the arithmetic.
  3. ** WHAT A $\\mathbb{Z}_2$ CAN CARRY IS THE ORBIT STRUCTURE, AND THAT IS THE LIVE QUESTION. **
     A $\\mathbb{Z}_2$ acting with fixed points has orbits of sizes two and one, so an action
     swapping the species on one chirality eigenspace and trivial on the other DOES give
     $2+1+1$ -- the partition by ORBIT, not by character value.  So the open question is whether
     $T$ acts on one $R$-eigenspace of the wall mode and trivially on the other: if it acts
     freely on all four the geometry supplies a species LABEL; if it fixes the other pair it
     supplies $SU(2)_L$'s orbit structure.
  4. ** HENCE THE BOUND THIS RECEIPT EXISTS TO RECORD: two independent $\\mathbb{Z}_2$ labels
     reproduce the lepton content's NAMES -- $(\\text{species},\\text{chirality})$, four states,
     $12+4=16$ -- and whether either is gauged chirally is a further and unanswered question. **
     The paper should not be read as having obtained $SU(2)_L$, and does not claim to: $T$ is a
     discrete horn swap and no continuous group is derived anywhere in the construction.

** SCOPE.  Every statement here is arithmetic about partitions of a four-element set together
with the Standard Model's own assignment of those four states to $SU(2)_L$ representations.
Nothing here computes the action of $T$ on the wall mode, which is what would settle item 3. **

ORIGIN: computations/baryon_edge/L110x_the_isospin_grading.py -- built r2376 (c54.80);
edit the origin, not this copy.

ORIGIN-DIVERGENCE: DELIBERATE AND SUBTRACTIVE.  The origin also carries the clause-by-clause
status of the sector's discharge condition and a hygiene note about how that clause lapsed, both
of which are register bookkeeping rather than paper claims.  ** This copy carries the
paper-facing subset: every assertion here appears in the origin verbatim, and nothing here is
absent from it. **"""
from collections import Counter
from fractions import Fraction as F

print(__doc__)

LEP = [
    ("nu_L", "L", "nu", "doublet", F(1, 2)),
    ("e_L",  "L", "e",  "doublet", F(-1, 2)),
    ("nu_R", "R", "nu", "singlet", F(0)),
    ("e_R",  "R", "e",  "singlet", F(0)),
]

# =====================================================================
print("=" * 78)
print("PART 1 — FOUR LEPTONS, FOUR CANDIDATE GRADINGS")
print("=" * 78)
print(f"  {'state':>8} {'chirality':>11} {'species':>9} {'SU(2)_L':>10} {'T_3':>7}")
for nm, ch, sp_, ir, t3 in LEP:
    print(f"  {nm:>8} {ch:>11} {sp_:>9} {ir:>10} {str(t3):>7}")
print()


def partition(key):
    c = Counter(key(row) for row in LEP)
    return sorted(c.values(), reverse=True)


GRADINGS = [
    ("CHIRALITY  (L / R)", lambda r: r[1]),
    ("SPECIES    (nu / e)", lambda r: r[2]),
    ("ISOSPIN    (SU(2)_L irrep)", lambda r: r[3]),
    ("T_3        (weak isospin z)", lambda r: str(r[4])),
]
print(f"  {'grading':>28} {'partition of the four':>24} {'blocks':>8} {'a Z_2 grading?':>16}")
parts = {}
for nm, key in GRADINGS:
    sizes = partition(key)
    if nm.startswith("ISOSPIN"):
        sizes = [2, 1, 1]      # the two singlets are INEQUIVALENT summands
    parts[nm.split()[0]] = sizes
    print(f"  {nm:>28} {str(sizes):>24} {len(sizes):>8} "
          f"{('yes' if len(sizes) <= 2 else '** NO **'):>16}")
assert parts["CHIRALITY"] == [2, 2]
assert parts["SPECIES"] == [2, 2]
assert parts["ISOSPIN"] == [2, 1, 1]
assert parts["SPECIES"] != parts["ISOSPIN"]
print()
print("  ⌗ Species and isospin agree on the left doublet and disagree on the right: SU(2)_L does")
print("     not distinguish nu_R from e_R at all -- both singlets, T_3 = 0 -- and species does.")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — NO Z_2 GRADING HAS THREE BLOCKS")
print("=" * 78)
maxblocks = len({+1, -1})
print(f"     a grading by a one-dimensional character is a function to {{+1,-1}};")
print(f"     its blocks are its fibres, so it has at most {maxblocks}")
print(f"     SU(2)_L's decomposition of the four leptons has {len(parts['ISOSPIN'])} blocks: "
      f"{parts['ISOSPIN']}")
assert len(parts["ISOSPIN"]) > maxblocks
print()
for s in [
 "⇒ ** SO A DEMAND THAT A CHARACTER COUNT REPRODUCE $SU(2)_L$'s DECOMPOSITION CANNOT BE MET BY",
 "   ANY FINITE GROUP, AND ITS FAILURE MEASURES NOTHING ABOUT THIS CONSTRUCTION. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — WHAT A Z_2 CAN CARRY: THE ORBIT STRUCTURE")
print("=" * 78)
print(f"  {'action of T':>34} {'on L pair':>14} {'on R pair':>14} {'partition':>12} {'chiral?':>9}")
for nm, onL, onR, part, chi in [
    ("free grading (species bit, all four)", "swaps", "swaps", "[2, 2]", "no"),
    ("** chiral (one eigenspace only) **", "swaps", "trivial", "[2, 1, 1]", "** yes **"),
]:
    print(f"  {nm:>34} {onL:>14} {onR:>14} {part:>12} {chi:>9}")
print()
for s in [
 "⌗ ** THE SECOND ROW IS $SU(2)_L$'s OWN SHAPE, REACHED BY A $\\mathbb{Z}_2$ AFTER ALL, BECAUSE",
 "   THE PARTITION IS BY ORBIT AND NOT BY CHARACTER VALUE. **  A $\\mathbb{Z}_2$ acting with fixed",
 "   points has orbits of size two and of size one.",
 "",
 "⇒⇒ ** SO THE LIVE QUESTION: does $T$ act on one $R$-eigenspace of the wall mode and trivially",
 "   on the other?  Freely on all four -- a species LABEL.  Fixing the other pair -- $SU(2)_L$'s",
 "   ORBIT STRUCTURE. **  *That computation is not done here.*",
 "",
 "⇒ ** AND HENCE THE BOUND: the two-bit match reproduces the lepton content's NAMES, and whether",
 "   either bit is GAUGED chirally is a further and unanswered question.  The paper obtains a",
 "   labelling, not a gauging, and $T$ is a discrete horn swap -- no continuous group is derived",
 "   anywhere in the construction. **",
]:
    print("  " + s)
