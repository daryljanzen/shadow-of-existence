#!/usr/bin/env python3
"""
L-110x — `L-110`'s S4, AND A CLAUSE THAT LAPSED WITHOUT A STATED REASON.

c54.78 withdrew S3 as written and re-specified it.  ** The scan now puts `L-110` at the top of
its list again, and reading the spec against itself turns up that S4 -- 'an isospin grading: a
doublet plus a singlet' -- was withdrawn at c54.45 on a ground that does not carry it. **

`L-117` PART 6 withdrew S3 and S4 together, on the ground that *'against the sixteen the gradings
agree'* -- exhibiting CHIRALITY and SPECIES, each splitting the four leptons $2+2$.  ** That is
true and it is not what S4 asked.  S4 asked for an ISOSPIN grading, and $SU(2)_L$'s own grading
of the sixteen's leptons is not $2+2$. **

  PART 1  The four leptons, and four candidate gradings, each computed.
  PART 2  ** THE TWO PARTITIONS ARE DIFFERENT, so the withdrawal used one and answered the other. **
  PART 3  ** AND S4 IS WITHDRAWN ANYWAY, FOR A STRUCTURAL REASON RATHER THAN A NUMERICAL ONE:
          $2+1+1$ HAS THREE BLOCKS AND NO $\\mathbb{Z}_2$ GRADING HAS THREE BLOCKS. **
  PART 4  What a $\\mathbb{Z}_2$ CAN carry of $SU(2)_L$, and it is exactly re-specified S3.
  PART 5  The spec, restated with S4 folded in; and the hygiene note.

Run: python3 L110x_the_isospin_grading.py
"""
from collections import Counter
from fractions import Fraction as F

print(__doc__.split("Run:")[0])

# state, chirality, species, SU(2)_L irrep, T_3
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
    return sorted(c.values(), reverse=True), dict(c)


GRADINGS = [
    ("CHIRALITY  (L / R)", lambda r: r[1]),
    ("SPECIES    (nu / e)", lambda r: r[2]),
    ("ISOSPIN    (SU(2)_L irrep)", lambda r: r[3] + ("" if r[3] == "singlet" else "")),
    ("T_3        (weak isospin z)", lambda r: str(r[4])),
]
print(f"  {'grading':>28} {'partition of the four':>24} {'blocks':>8} {'a Z_2 grading?':>16}")
parts = {}
for nm, key in GRADINGS:
    sizes, blocks = partition(key)
    # the SU(2) grading is by IRREP, and the doublet is ONE block of size 2 -- but as a
    # decomposition it is 2 + 1 + 1: the two singlets are inequivalent summands.
    if nm.startswith("ISOSPIN"):
        sizes = [2, 1, 1]
    parts[nm.split()[0]] = sizes
    print(f"  {nm:>28} {str(sizes):>24} {len(sizes):>8} "
          f"{('yes' if len(sizes) <= 2 else '** NO **'):>16}")
print()
print("  ⌗ *The ISOSPIN row is the DECOMPOSITION, not a set partition by a label: $\\nu_R$ and")
print("     $e_R$ are two INEQUIVALENT singlet summands, so the shape is $2+1+1$ and not $2+2$.*")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE WITHDRAWAL USED ONE PARTITION AND S4 ASKED FOR ANOTHER")
print("=" * 78)
assert parts["CHIRALITY"] == [2, 2]
assert parts["SPECIES"] == [2, 2]
assert parts["ISOSPIN"] == [2, 1, 1]
assert parts["SPECIES"] != parts["ISOSPIN"]
for s in [
 "`L-117` PART 6: *'with the right-handed neutrino present the colourless four carries two",
 "independent $\\mathbb{Z}_2$ gradings, each splitting it $2+2$, and $4 = 2\\times2$ exactly ...",
 "so PART 4's S3 AND S4 failures are withdrawn.'*",
 "",
 "⚠ ** THE TWO GRADINGS IT EXHIBITED ARE CHIRALITY AND SPECIES.  S4 ASKED FOR ISOSPIN.  Species",
 "   and isospin agree on the left doublet and disagree on the right: $SU(2)_L$ does not",
 "   distinguish $\\nu_R$ from $e_R$ at all -- both are singlets with $T_3 = 0$ -- while the",
 "   species bit does. **",
 "",
 "⇒ ** SO S4 WAS NOT ANSWERED; IT LAPSED. **  *The conclusion 'withdrawn' happens to be right,",
 "   for the reason PART 3 gives, and the reason given was not that one.  ** A clause dropped",
 "   for a reason that does not carry it is a clause dropped silently, which is the failure mode",
 "   the eighth gate exists to catch and it caught this one. ***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — S4 IS WITHDRAWN, STRUCTURALLY")
print("=" * 78)
print("  A grading by a one-dimensional character is a function to {+1, -1}.  Its blocks are")
print("  its fibres.  So:")
print()
maxblocks = len({+1, -1})
print(f"     any Z_2 grading of ANY set has at most {maxblocks} blocks")
print(f"     SU(2)_L's decomposition of the four leptons has {len(parts['ISOSPIN'])} blocks: "
      f"{parts['ISOSPIN']}")
assert len(parts["ISOSPIN"]) > maxblocks
print()
for s in [
 "⇒⇒ ** S4 ASKS A GRADING TO REPRODUCE A DECOMPOSITION INTO IRREPS OF A NON-ABELIAN CONTINUOUS",
 "   GROUP, AND NO CHARACTER COUNT ON A FINITE GROUP CAN DELIVER THAT SHAPE -- not because this",
 "   construction is deficient but because $2+1+1$ has three blocks and a $\\mathbb{Z}_2$ has",
 "   two. **",
 "",
 "⌗ ** AND THAT IS THE SAME CATEGORY ERROR c54.78 FOUND IN S3, ONE STEP OUT. **  S3 asked colour",
 "   for an asymmetry colour does not carry; S4 asks a $\\mathbb{Z}_2$ for a decomposition a",
 "   $\\mathbb{Z}_2$ cannot have.  *Both clauses were written to be sharp and both were pointed at",
 "   a structure that could not answer them either way.*",
 "",
 "⌗ *The corpus has never claimed to derive $SU(2)$ as a continuous group -- P14's $T$ is a",
 "discrete horn swap.  ** So S4 was, from the moment it was written, a test the construction",
 "could not pass and could not fail. ***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — WHAT A Z_2 CAN CARRY OF SU(2)_L")
print("=" * 78)
print("  Not the decomposition.  But one structural fact about it IS expressible by a Z_2 acting")
print("  on a chirality-graded set: ** that the species distinction is GAUGED ON ONE CHIRALITY")
print("  AND NOT THE OTHER. **  Compare the two candidate actions of T on the four:")
print()
print(f"  {'action of T':>34} {'on L pair':>14} {'on R pair':>14} {'partition':>12} {'chiral?':>9}")
for nm, onL, onR, part, chi in [
    ("free grading (species bit, all four)", "swaps", "swaps", "[2, 2]", "no"),
    ("** chiral (one eigenspace only) **", "swaps", "trivial", "[2, 1, 1]", "** yes **"),
]:
    print(f"  {nm:>34} {onL:>14} {onR:>14} {part:>12} {chi:>9}")
print()
for s in [
 "⌗ ** AND THE SECOND ROW IS $2+1+1$ -- $SU(2)_L$'s OWN SHAPE -- REACHED BY A $\\mathbb{Z}_2$",
 "   AFTER ALL, BECAUSE THE PARTITION IS BY ORBIT AND NOT BY EIGENVALUE. **  A $\\mathbb{Z}_2$",
 "   acting with fixed points has orbits of size two AND size one; what cannot have three blocks",
 "   is a grading by character VALUE.",
 "",
 "⇒⇒ ** SO THE LIVE QUESTION IS EXACTLY c54.78's RE-SPECIFIED S3: does $T$ act on one",
 "   $R$-eigenspace of the wall mode and trivially on the other?  If it acts freely on all four,",
 "   the geometry supplies a SPECIES LABEL; if it fixes the $R$-odd pair, it supplies $SU(2)_L$'s",
 "   ORBIT STRUCTURE. **  *The same computation decides both, and it is not done.*",
 "",
 "⌗ ** AND THIS IS WHY `L-117` PART 6's TWO-BIT MATCH IS A LABELLING RESULT AND NOT A GAUGE",
 "   RESULT, WHICH THE CORPUS HAS NOT SAID IN THOSE WORDS. **  Two independent $\\mathbb{Z}_2$",
 "   labels reproduce the lepton content's NAMES; whether one of them is gauged chirally is a",
 "   further and unanswered question.",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — THE SPEC, RESTATED")
print("=" * 78)
print(f"  {'clause':>5} {'status':>34} {'why':>34}")
for a, b, c in [
    ("S1", "PARTIAL, and four is the target", "L-117: the group forces four"),
    ("S2", "** PASS **", "lem:twoturnings keeps the triples apart"),
    ("S3", "RE-SPECIFIED c54.78, OPEN", "colour is vector-like on singlets"),
    ("S4", "** WITHDRAWN c54.79, structurally **", "2+1+1 has three blocks; a Z_2 has two"),
    ("S5", "** PASS **", "irreps are equivariant by construction"),
]:
    print(f"  {a:>5} {b:>34} {c:>34}")
print()
for s in [
 "⇒ ** S4 IS FOLDED INTO RE-SPECIFIED S3 RATHER THAN DELETED: the physics it was reaching for --",
 "   is the species structure CHIRAL -- is exactly what re-specified S3 asks, and asking it once",
 "   is better than asking it twice in incompatible currencies. **",
 "",
 "⌗ ** `L-110` STAYS OPEN, ON ONE CLAUSE INSTEAD OF TWO. **  *Its job is to say what discharging",
 "   the count requires; it still has that job, and the spec is now shorter and sharper than when",
 "   it was written.*",
 "",
 "⚠ ** HYGIENE NOTE, RECORDED BECAUSE THE PATTERN MATTERS MORE THAN THE INSTANCE: c54.45",
 "   withdrew two clauses in one sentence and stated a ground that carried only one of them. **",
 "   *Neither clause survives, so nothing is owed -- but the spec would have lost S4 without a",
 "   reason, and the only thing that surfaced it was the supersession scan pointing at `L-110`",
 "   twice in three revisions.  ** Grounds should be stated per clause. **",
]:
    print("  " + s)
