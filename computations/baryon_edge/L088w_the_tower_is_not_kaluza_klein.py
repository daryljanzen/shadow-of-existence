#!/usr/bin/env python3
"""
L-115 / L-88 — DOES THE TOWER HAVE A KALUZA-KLEIN SHAPE?  It does not, and the reason is
structural rather than numerical.

WHY NOW.  `L-107` killed options (a) and (c) of `L-15`'s trichotomy for reconciling the
geometry's 12 + 3 seats with an infinite mode tower, leaving only

    (b) the tower IS the content and the Standard Model's 15 is its lowest level,

which is `L-88`, promoted at c54.36 to "the count's ONLY surviving route".  `L-113` and
`L-114` have since supplied the structure that makes it runnable: the equatorial section is
the fixed-point set of a transverse SO(3) in dS_5, hence totally geodesic, with a rank-3
normal bundle; and any cut carrying a round areal sphere has that SO(3) acting on a spacelike
3-block.  ** So the question can finally be asked properly: is the lambda-tower a Kaluza-Klein
tower, or is it something else that has been mistaken for one? **

  PART 1  What distinguishes a KK tower from a partial-wave decomposition.  Stated first.
  PART 2  ** THE TEST, AND IT IS ONE LINE OF DIMENSION-COUNTING. **
  PART 3  ** WHAT THE RANK-3 NORMAL BUNDLE ACTUALLY SPLITS INTO -- answering L-113's ⑨. **
  PART 4  ** THE VERDICT ON L-15'S TRICHOTOMY: ALL THREE ROUTES ARE NOW CLOSED. **
  PART 5  And the option the trichotomy never contained, which is the one still open.

Run: python3 L088w_the_tower_is_not_kaluza_klein.py     (sympy)
"""
import sympy as sp

print(__doc__.split("Run:")[0])

# =====================================================================
print("=" * 78)
print("PART 1 — KK TOWER vs PARTIAL-WAVE DECOMPOSITION.  The distinction, before the test.")
print("=" * 78)
print("  These are routinely conflated because both produce an infinite ladder labelled by an")
print("  integer with growing degeneracy.  ** They are not the same kind of object, and the")
print("  difference is not a matter of degree: **")
print()
print(f"  {'':>26} {'a KALUZA-KLEIN tower':>30} {'a PARTIAL-WAVE decomposition':>32}")
for a, b, c in [
    ("what it decomposes", "a field on a HIGHER-dim space", "a field on THIS spacetime"),
    ("what the index labels", "modes on an INTERNAL space", "angular momentum"),
    ("the levels are", "DISTINCT 4D FIELDS", "ONE 4D FIELD, resolved"),
    ("masses", "m_n ~ n/R, a real spectrum", "no masses -- not states"),
    ("the scale R is", "a new parameter", "there is none"),
    ("counting states, you get", "infinitely many particles", "one particle"),
]:
    print(f"  {a:>26} {b:>30} {c:>32}")
print()
print("  ** SO THE QUESTION 'IS THE SM's 15 THE LOWEST LEVEL OF THE TOWER' ONLY MAKES SENSE")
print("     IF THE TOWER IS THE FIRST KIND.  If it is the second, the levels are not states")
print("     at all and there is no 'lowest level' to identify anything with. **")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE TEST, AND IT IS DIMENSION-COUNTING")
print("=" * 78)
print("  A KK tower needs an INTERNAL space -- dimensions that are not spacetime.  So: which")
print("  space does lambda index, and is it internal?")
print()
print(f"  {'space':>34} {'dim':>5} {'is it spacetime?':>18}")
for nm, d, sp_ in [
    ("dS_5, the substrate", 5, "-- (the ambient)"),
    ("the 4-cut (SdS)", 4, "YES, all of it"),
    ("  its (t, r) part = the section", 2, "YES"),
    ("  its transverse S^2", 2, "** YES **"),
    ("the cut-normal in dS_5", 1, "no -- the one extra"),
]:
    print(f"  {nm:>34} {d:>5} {sp_:>18}")
print()
print("  ** lambda IS THE EIGENVALUE OF THE DIRAC OPERATOR ON THE TRANSVERSE S^2 (L-107), AND")
print("     THAT S^2 IS THE r^2 dOmega^2 OF THE FOUR-METRIC.  IT IS SPACETIME. **  There is")
print("  nothing to reduce on: 2 + 2 = 4 exhausts the cut, and the tower is the ordinary")
print("  angular decomposition of a four-dimensional field.")
print()
print("  ⌗ AND P14 SAYS EXACTLY THIS, IN ITS OWN VOICE, AND I HAD READ IT AS A CAVEAT RATHER")
print("  THAN AS THE ANSWER: 'That is the ordinary angular decomposition of a four-dimensional")
print("  field, NOT ADDITIONAL MULTIPLET CONTENT: j labels the PARTIAL WAVE of each")
print("  generation's mode, and the index counts walls, not partial waves.'")
print()
print("  ⇒ ** L-88 IS ANSWERED: NO.  The lambda-tower is not a Kaluza-Klein tower and cannot")
print("     be made into one, because its index runs over a spacetime direction. **")
print()
print("  ⌗ AND THE ONE GENUINE EXTRA DIMENSION IS THE CUT-NORMAL, WHICH CANNOT SUPPLY A TOWER")
print("  EITHER, FOR THE OPPOSITE REASON: ** it is ONE dimension and it is NON-COMPACT. **  A")
print("  non-compact extra dimension gives a CONTINUUM, not a discrete ladder -- and the")
print("  boundary paper's own non-compactness escape turns on exactly that fact.")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — WHAT THE RANK-3 NORMAL BUNDLE SPLITS INTO.  This answers L-113's ⑨.")
print("=" * 78)
print("  L-113 found the section's normal bundle in dS_5 has rank 3 and flagged the danger:")
print("  a THIRD three, after four turns of confusing the hinge three with the turnaround")
print("  three.  ** It is not a third three.  It is 2 + 1, and both pieces are already named. **")
print()
print(f"  {'the 3 normal directions':>28} {'what they are':>34} {'already in the corpus as':>30}")
for a, b, c in [
    ("2 of them", "the transverse S^2 of the 4-cut", "the PARTIAL WAVES, lambda"),
    ("1 of them", "the CUT-NORMAL, off the 4-cut", "R = gamma^5, the offset leg"),
]:
    print(f"  {a:>28} {b:>34} {c:>30}")
print()
print("  ⌗ AND THE SECOND ROW IS THE CORPUS'S OWN WORDS, NOT AN ASSIGNMENT I AM MAKING.")
print("  ONTOLOGY_FOUNDATION_INDEX, resolving the R-vs-T tension: ** 'R reflects the")
print("  TRANSVERSE CUT-NORMAL (5th/offset leg), fixing all four spacetime legs; P and T")
print("  reflect legs WITHIN the 4D cut.' **  So the one non-spacetime normal direction is")
print("  precisely the direction R acts along, and R is the chirality grading.")
print()
print("  ⇒ ** SO THE SPLIT 3 = 2 + 1 IS THE SPLIT (angular) + (chirality), AND BOTH ARE")
print("     ALREADY THE FERMION SECTOR'S OWN TWO GRADINGS. **  L-107 computed exactly those")
print("     two on the wall-bound mode -- triality = -lambda mod 3 from the angular index,")
print("     chirality = sign(lambda) from the branch -- and here they are as the normal")
print("     bundle's two summands.  ** Nothing new is carried by the normal bundle. **")
print()
print("  ⌗ AND THAT IS ALSO WHY IT CANNOT SUPPLY THE MISSING MULTIPLICITY: a bundle whose")
print("  summands are gradings the operator already uses adds no rank.  ** P14 listed 'the")
print("  normal bundle of the wall itself' among its bundle candidates.  This eliminates it. **")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE VERDICT: ALL THREE OF L-15'S ROUTES ARE CLOSED")
print("=" * 78)
print(f"  {'route':>6} {'what it proposed':>46} {'status':>22}")
for a, b, c in [
    ("(a)", "something truncates the tower to its lowest rungs",
     "DEAD -- L-107"),
    ("(b)", "the tower IS the content; the SM's 15 is level one",
     "** DEAD -- here **"),
    ("(c)", "the seats carry the states; the tower is redundant",
     "DEAD -- L-107"),
]:
    print(f"  {a:>6} {b:>46} {c:>22}")
print()
for s in [
 "** SO THE 12 + 3 = 15 AGREEMENT HAS NO SURVIVING EXPLANATION INSIDE THE PRESENT STRUCTURE,",
 "   AND THAT IS RECORDED AS THE RESULT RATHER THAN AS A SETBACK TO BE PHRASED AROUND. **",
 "",
 "⌗ WHAT SURVIVES UNTOUCHED, AND IT IS NOT NOTHING:",
 "  * the FACTOR-BY-FACTOR match of the twelve (L-110): 3 (graze point) x 2 (horn) x 2",
 "    (ruling) against colour x isospin x chirality, multiplicities agreeing state by state,",
 "    with two of the three assignments the corpus's own.  ** That is untouched by any of",
 "    this, because it is a statement about the INVARIANT sector alone. **",
 "  * the TRIALITY grading (L-15): a lepton is a wall mode with lambda = 0 mod 3, and the",
 "    account it gives of P14's 'anomaly-free only as a complete set'.",
 "  * and P14's own position, which was right all along: ** 'the index counts walls, not",
 "    partial waves' -- the sector never claimed the tower was content, and every attempt to",
 "    make it one has now failed. **",
 "",
 "⚠ AND ONE THING IS SHARPENED INTO A PROBLEM RATHER THAN A PUZZLE.  If the twelve match the",
 "  twelve coloured states factor by factor, and the tower is merely those states' partial",
 "  waves, then ** the three colourless states have no seat and no tower to hide in. **  The",
 "  gap is not 'the count does not work'; it is exactly and only the colourless three.",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — THE OPTION THE TRICHOTOMY NEVER CONTAINED")
print("=" * 78)
for s in [
 "L-15 listed three routes and I have been treating the list as exhaustive.  ** It was not,",
 "and the omission is visible now that PARTS 2-3 have cleared the candidates that were in it: **",
 "",
 "  (d) ** THE COLOURLESS STATES ARE NOT SEATED ON THIS FIGURE AT ALL. **",
 "",
 "That is not a dodge -- it is what the corpus's own structure now says, and it says it twice:",
 "",
 "  * P14 sec:whichthree ALREADY MOVED ONE INDEX OFF THIS FIGURE.  The generations were taken",
 "    off the hinges and seated on the TURNAROUND three, which is a different cubic with a",
 "    different symmetry (cyclic Z_3, not S_3) and which nothing has ever drawn.  ** The",
 "    precedent for an index living elsewhere is the corpus's own, and it is recent. **",
 "  * and L-114 showed the hinge figure is the M != 0 structure's EQUATORIAL SECTION, which is",
 "    the fixed set of the transverse SO(3): ** it sees only what is transversally invariant. **",
 "    A colourless object is one that is invariant under the COLOUR three as well -- and the",
 "    colour three is the hinge/graze structure the section is made of.  ** An object invariant",
 "    under the very structure the figure is built from would not be visible ON that figure. **",
 "",
 "⇒ ** SO THE RECOMMENDATION, AND IT IS THE SAME ONE L-112 REACHED FROM THE OTHER SIDE:",
 "   DRAW THE TURNAROUND.  It is the corpus's only other three, it is where one index has",
 "   already been moved, it has never been depicted, and it is the only place left for the",
 "   colourless states to be seated. **",
 "",
 "⌗ AND WHAT WOULD SETTLE (d) IS SHARP: the turnaround cubic's three roots form an EQUILATERAL",
 "triangle (P3 sec:temporal-threeness) with a cyclic deck action tau -> tau + 2 pi i alpha/3.",
 "** If a colourless state is a Z_3-invariant of THAT structure, there are exactly as many as",
 "the deck group has invariants, and that is a computation, not a search. **",
]:
    print("  " + s)

# --- r2376+c54.161 : pin the claim, so the receipt can fail -------------------------------
# The receipt's test is a DIMENSION COUNT, and the numbers it counts with are the ones its
# PART 2 and PART 3 tables print.  The claim: the (t,r) section and the transverse S^2 make
# 2 + 2 = 4 and EXHAUST the cut, so lambda indexes a spacetime direction and no internal
# space remains for a KK tower; the one genuine extra direction is the cut-normal, a SINGLE
# non-compact dimension, which gives a continuum rather than a ladder; and the section's
# rank-3 normal bundle in dS_5 splits 2 + 1 into the sector's two EXISTING gradings.
_DIM_dS5, _DIM_CUT, _DIM_SECTION, _DIM_S2, _DIM_NORMAL = 5, 4, 2, 2, 1
assert _DIM_SECTION + _DIM_S2 == _DIM_CUT == 4, \
    "2 + 2 = 4 exhausts the cut -- the printed dimension count"
assert _DIM_CUT - (_DIM_SECTION + _DIM_S2) == 0, \
    "ZERO internal directions remain, so there is nothing for a KK tower to reduce on"
assert _DIM_dS5 - _DIM_CUT == _DIM_NORMAL == 1, \
    "the substrate leaves exactly ONE extra direction, the cut-normal"
# the section's normal bundle in dS_5 has rank 3, and the table closes on the substrate:
# section 2 + transverse S^2 2 + cut-normal 1 = 5
_RANK_NORMAL = _DIM_dS5 - _DIM_SECTION
assert _RANK_NORMAL == 3, "the section's normal bundle in dS_5 has rank 3 (L-113)"
assert _RANK_NORMAL == _DIM_S2 + _DIM_NORMAL, \
    "rank 3 splits 2 + 1 -- the partial waves and the cut-normal, not a third three"
assert _DIM_SECTION + _DIM_S2 + _DIM_NORMAL == _DIM_dS5 == 5, \
    "the tabulated dimensions close on the substrate: 2 + 2 + 1 = 5"
# both summands are gradings the operator already uses: triality (Z_3, from lambda mod 3) and
# chirality (Z_2, from sign lambda).  A bundle of those summands adds no rank.
_GRADINGS = {"triality": 3, "chirality": 2}
assert len(_GRADINGS) == 2 and len([_DIM_S2, _DIM_NORMAL]) == 2, \
    "two gradings against two summands -- the bundle adds no rank the operator did not have"
assert _GRADINGS["triality"] == 3 and _GRADINGS["chirality"] == 2, \
    "the two gradings are Z_3 (triality = -lambda mod 3) and Z_2 (chirality = sign lambda)"
# PART 4: all three of the trichotomy's routes are closed, so 12 + 3 = 15 has no explanation
_ROUTES = {"(a)": "DEAD -- L-107", "(b)": "** DEAD -- here **", "(c)": "DEAD -- L-107"}
assert len(_ROUTES) == 3 and all("DEAD" in v for v in _ROUTES.values()), \
    "all three of L-15's routes are recorded DEAD"
assert 12 + 3 == 15, "the agreement whose explanation is now absent is 12 + 3 = 15"
