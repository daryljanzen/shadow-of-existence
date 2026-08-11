#!/usr/bin/env python3
"""
L-64w — ATTACKING THE PROVENANCE TABLE, WHICH IS A CHECK ON MY OWN WORK AND WAS REGISTERED AS
ONE.  `THE_FERMION_SECTOR_GEOMETRY` Part Three asserts that every geometric input was fixed for
a reason internal to the construction BEFORE any Standard Model reading was attached, and
returns ** ten rows, ten yeses. **  `L-64`: "a table that comes out 10/10 for its author is the
table to attack", and no node had.

** THE ATTACK FINDS TWO THINGS, AND THE SECOND IS THE SERIOUS ONE. **

  PART 1  The method: what would actually falsify a row, stated before looking.
  PART 2  ⚠ ** FINDING 1 — THE TABLE OMITS THE INPUT THAT TURNED OUT TO MATTER MOST. **
  PART 3  ⚠⚠ ** FINDING 2 — AND THAT INPUT MOVED DURING THIS SESSION, AFTER THE PHYSICS NEED
          FOR IT HAD BEEN STATED.  That is the exact pattern the table exists to rule out. **
  PART 4  The defence, weighed honestly rather than asserted.
  PART 5  The verdict, and what the table should say instead of 10/10.

Run: python3 L064w_attack_the_provenance_table.py
"""
print(__doc__.split("Run:")[0])

# =====================================================================
print("=" * 78)
print("PART 1 — THE METHOD, FIXED BEFORE LOOKING")
print("=" * 78)
for s in [
 "`L-64`'s own prescription: ** 'take each row and hunt for a revision where the input MOVED",
 "AFTER a physics reading existed.' **  So a row falsifies if:",
 "",
 "   (a) the input's VALUE or CONTENT changed at some revision, AND",
 "   (b) at that revision a Standard Model reading depending on it was already in play, AND",
 "   (c) the change went in the direction that reading needed.",
 "",
 "⌗ ** AND ONE MORE FAILURE MODE THE PRESCRIPTION DOES NOT NAME, WHICH I AM ADDING BECAUSE A",
 "   TABLE CAN ALSO FAIL BY OMISSION: an input that is load-bearing for the reading and is NOT",
 "   IN THE TABLE AT ALL. **  A 10/10 over the rows one chose to list is not a 10/10 over the",
 "   inputs the result actually rests on.  ** That is the sharper attack and it is the one that",
 "   lands. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — FINDING 1: THE TABLE OMITS THE LOAD-BEARING INPUT")
print("=" * 78)
rows = [
    "alpha the only scale", "the hinge at 2 alpha", "three hinges, 120 deg",
    "the hinge is a LINE", "null <=> tangent", "sin w = 1/2 => Nariai",
    "R = gamma^5", "charge R-even, mass R-odd", "the lap closes through r=0",
    "the Z_3 deck action",
]
print(f"  the ten rows, as listed:")
for i, r in enumerate(rows, 1):
    print(f"     {i:>2}. {r}")
print()
for s in [
 "** AND THE INPUT THE WHOLE COLOUR RESULT RESTS ON IS NOT AMONG THEM: **",
 "",
 "     ⇒ ** HOW MANY SIGNED AREAL RADII THERE ARE -- one shared, or one per vantage. **",
 "",
 "Everything `L-128`-`L-130` established turns on it.  With ONE radius the branched cover is",
 "cyclic, the monodromy is ABELIAN, the group is Z_3 and there is no colour.  With THREE the",
 "monodromy is diagonal in the vantage basis, the hinge cycle does not commute with it, and the",
 "smallest connected group containing the pair is SU(3).  ** The entire result is the difference",
 "between those two readings, and the provenance table has no row for it. **",
 "",
 "⌗ ** SO THE TABLE'S SCORE IS NOT 10/10.  IT IS 10 OF AT LEAST 11, WITH THE ELEVENTH -- THE",
 "   DECISIVE ONE -- UNLISTED AND THEREFORE UNTESTED AT THE TIME IT WAS WRITTEN. **  That is not",
 "   a defect of any row; it is a defect of the table's CLOSURE, and it is the kind of gap a",
 "   10/10 makes harder to see rather than easier.",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — FINDING 2: AND THAT INPUT MOVED, AFTER THE NEED FOR IT WAS STATED")
print("=" * 78)
print("  The revision history of this session, stated in order and without gloss:")
print()
print(f"  {'revision':>10}  {'what happened'}")
for a, b in [
    ("c54.50", "`L-127` computes the bundle, finds only Z_3, and NAMES WHAT IT NEEDS:"),
    ("",       "  'there are THREE walls ... a relative phase between the sheets of one wall,"),
    ("",       "   induced by transport around another, is exactly the shape Q has.'"),
    ("c54.52", "`L-128` examines the one-radius/three-radii fork and ADOPTS THREE RADII --"),
    ("",       "  which supplies exactly the generator named two revisions earlier."),
    ("c54.53", "a second, combinatorial argument for three radii is found."),
    ("c54.58", "P3's abstract is read; it states the three-radii reading in general."),
]:
    print(f"  {a:>10}  {b}")
print()
for s in [
 "⚠⚠ ** ON THE FACE OF IT THIS IS EXACTLY CONDITION (a)+(b)+(c) OF PART 1.  The input moved; a",
 "   physics reading depending on it was in play; and it moved in the direction that reading",
 "   needed. **  I am not going to write that up as anything else.",
 "",
 "⚠ ** AND THERE IS AN AGGRAVATING DETAIL I MUST RECORD BECAUSE IT IS MINE. **  At c54.52 I wrote",
 "   the fork up as ** 'the corpus contains two incompatible readings and has never noticed' **",
 "   -- a framing under which adopting the reading I needed looks like REPAIRING A DEFECT rather",
 "   than CHOOSING.  ** c54.58 found that framing false: P3 had noticed, and says so at the",
 "   outset. **  The false framing was in the direction that made the adoption look disinterested.",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE DEFENCE, WEIGHED RATHER THAN ASSERTED")
print("=" * 78)
print(f"  {'defence':>46}  {'weight'}")
for d, w in [
    ("the three-radii reading was ALREADY the corpus's written",
     "STRONG -- P3 abstract + P14 header +"),
    ("  position; the computations had drifted from the papers",
     "  `L-75`'s verification all predate"),
    ("the premise 'with disjoint support' is in P3's ABSTRACT",
     "STRONG -- dated long before, and general"),
    ("`L-128` tested (ii) against four ESTABLISHED results BEFORE",
     "STRONG -- and it found an unsought"),
    ("  using it, and found it also repairs `L-74`'s confinement",
     "  benefit, which motivated reasoning"),
    ("  sentence, which (i) could not support",
     "  does not usually produce"),
    ("the search was MOTIVATED by the need for Q",
     "AGAINST -- motivated search is the"),
    ("",
     "  condition under which motivated"),
    ("",
     "  conclusions happen"),
    ("the c54.52 framing overstated the corpus's confusion",
     "AGAINST -- and in the flattering direction"),
]:
    print(f"  {d:>46}  {w}")
print()
for s in [
 "⌗ ** THE DISTINCTION THAT DECIDES IT, AND IT IS NOT A COMFORTABLE ONE: the reading predates the",
 "   physics need IN THE PAPERS.  It does not predate it IN MY ADOPTION OF IT. **  Those are",
 "   different claims and the table's column heading -- 'fixed before any SM reading?' -- is",
 "   ambiguous between them.  ** For the ten listed rows the two coincide, which is why nobody",
 "   noticed the ambiguity.  For the eleventh they come apart. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — THE VERDICT")
print("=" * 78)
for s in [
 "① ** NO LISTED ROW FALSIFIES. **  I found no revision at which any of the ten inputs changed",
 "   value after a reading depending on it existed.  ** The rows survive the attack they were",
 "   written to invite. **",
 "",
 "② ** BUT THE TABLE DOES NOT SURVIVE AS A 10/10, AND SHOULD STOP BEING WRITTEN AS ONE. **  It",
 "   omits the input the colour result rests on, and that input's provenance is DOCUMENTARY (the",
 "   papers said it first) rather than TEMPORAL (I adopted it after needing it).  ** Documentary",
 "   provenance is real evidence and it is weaker evidence, and the table should say which kind",
 "   each row has. **",
 "",
 "③ ** THE COLUMN HEADING IS THE ACTUAL DEFECT. **  'Fixed before any SM reading?' does not",
 "   distinguish *the corpus fixed it before* from *this node adopted it before*.  ** Split the",
 "   column and the table becomes an instrument instead of a score. **",
 "",
 "④ ⌗ *And the general lesson is the one `L-64` was reaching for when it registered itself:*",
 "   ** a provenance table protects against ad-hoc INPUTS and does nothing about ad-hoc",
 "   SELECTION AMONG EXISTING inputs. **  The corpus is large enough that a node needing a",
 "   structure can usually FIND one already written down.  *That is a real and different hazard,",
 "   it is not what the table tests, and this session is an instance of it -- one where the",
 "   independent evidence happens to be strong.*",
]:
    print("  " + s)
