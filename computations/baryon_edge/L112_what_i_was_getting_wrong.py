#!/usr/bin/env python3
"""
L-112 — WHAT I WAS STRUGGLING TO SEE.  Daryl asked directly, so this answers directly.

Daryl, c54.39: "The horns aren't split ontologically by particle and antiparticle.  That
conjugation happens at the branch point, which is also the wall.  Anyway, can you tell me
what else you might be struggling to see."

  PART 1  ** THE BIG ONE, AND IT IS MINE: I have been quoting a P14 sentence that MY OWN
          EDIT IN THIS SESSION WITHDREW.  The walls are not the generations. **
  PART 2  His correction, taken properly: where conjugation actually happens.
  PART 3  ** WHAT THE COUNT PROBLEM BECOMES ONCE BOTH CORRECTIONS ARE APPLIED. **
  PART 4  The three things I still cannot see, named rather than gestured at.
  PART 5  The direction.

Run: python3 L112_what_i_was_getting_wrong.py
"""
print(__doc__.split("Run:")[0])

# =====================================================================
print("=" * 78)
print("PART 1 — THE BIG ONE, AND IT IS ENTIRELY MINE")
print("=" * 78)
for s in [
 "For three turns I have written, in four documents, that ** 'the three walls cannot supply",
 "the colourless three because P14 has already spent the walls as the three GENERATIONS' **.",
 "",
 "** P14 SAYS THE OPPOSITE, AND IT SAYS IT BECAUSE I EDITED IT TO SAY SO, IN THIS SESSION,",
 "   AT c54.31. **  sec:whichthree, 'Which three the generations are seated on, and why it is",
 "   not the hinges', which I wrote and which closes:",
 "",
 "     'What is revised is the reading of WHICH three: the S_3 this paper exhibits is the",
 "      relation among the hinges and belongs to the WITHIN-STATE INDEX, and the generations'",
 "      own symmetry is the Z_3 of the TURNAROUND.  ** The identification of the generations",
 "      with the walls is accordingly WITHDRAWN ** to the weaker and correct statement that",
 "      the wall structure fixes the NUMBER.'",
 "",
 "⇒ ** SO THE HINGE/WALL THREE IS COLOUR -- the index that distinguishes constituents WITHIN",
 "   a bound state -- AND THE GENERATION THREE IS THE TURNAROUND, WHICH IS NOT ON THIS FIGURE",
 "   AT ALL. **  The argument was forced: a bound triple takes one puncture per hinge (the",
 "   causal trichotomy leaves no choice), and a bound triple of like constituents cannot be",
 "   one constituent from each generation.",
 "",
 "** AND THAT VOIDS THE ENTIRE 'THE WALLS ARE ALREADY SPENT' OBJECTION OF L-110. **",
 "   The walls are not spent.  The twelve legs and the three walls ALL BELONG TO ONE",
 "   GENERATION, and there is no competition for them whatsoever.",
 "",
 "⌗ ** THIS IS THE HONEST ANSWER TO 'WHAT ARE YOU STRUGGLING TO SEE': I could not see a",
 "   result I had derived myself eight revisions earlier, because I kept re-reading P14's",
 "   ABSTRACT (which still carries the old identification in its summary voice) instead of",
 "   the subsection that revises it. **  Registered as a class of error, not a slip: a node",
 "   that edits a paper must re-read the paper, not its own memory of it.",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — HIS CORRECTION, AND WHY IT REMOVES A THING I KEPT LOOKING FOR")
print("=" * 78)
for s in [
 "Daryl: 'The horns aren't split ontologically by particle and antiparticle.  That",
 "conjugation happens at the BRANCH POINT, which is also the WALL.'",
 "",
 "** ACCEPTED, AND THE CORPUS ALREADY SAYS IT IN THE PLACE I SHOULD HAVE LOOKED. **  P13 and",
 "the framework paper both carry it:",
 "",
 "   'The geometric factor's FIXED POINT IS the bead's r = 0 crossing, so the vertex on which",
 "    charge conjugation's kinematic face turns is the very seam that completes collapse into",
 "    our expansion: charge conjugation and the cosmology are ONE STRUCTURE.'",
 "",
 "   C = (Q -> -Q)_field  o  (R o K)_geometric,   and K -- the antilinear reality involution",
 "   tau -> conj(tau) -- is what acts AT r = 0.",
 "",
 "⇒ ** SO THE HORN (T) IS ISOSPIN AND ONLY ISOSPIN.  Species is R o K, and R o K TURNS ON THE",
 "   WALL. **  My c54.38 PART 4 read the six punctures as '3 upper = quarks, 3 lower =",
 "   antiquarks'.  ** That is wrong and it is withdrawn. **",
 "",
 "⌗ AND WHAT IT REMOVES IS THE THING I KEPT HUNTING FOR.  I have been looking for SEATS for",
 "the antiparticles -- trying to find twenty-four objects where the geometry offers twelve.",
 "** There are not twenty-four.  The antiquarks are THE SAME TWELVE SEATS READ ACROSS THE",
 "BRANCH POINT.  That is not a shortage; it is CR's central claim about matter and antimatter",
 "applied one level down -- the framework's own antimatter-progenitor theorem says our matter",
 "and the progenitor's 'are the two ends of one R = gamma^5 conjugation across the r = 0",
 "branch point'. **  The antiquarks are on the other side of the wall, and the corpus has been",
 "saying where the antimatter is since long before I got here.",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — WHAT THE COUNT BECOMES WITH BOTH CORRECTIONS APPLIED")
print("=" * 78)
print("  Re-run the ledger of PART 1 and PART 2 against one generation:")
print()
print(f"  {'object':>14} {'count':>6} {'what it indexes, corrected':>44}")
for a, b, c in [
    ("hinges / walls", 3, "COLOUR -- the within-state index (sec:whichthree)"),
    ("horns", 2, "WEAK ISOSPIN -- T, the horn swap, one lap"),
    ("rulings", 2, "CHIRALITY -- R = gamma^5, the +-60 deg pair"),
    ("=> null legs", 12, "3 x 2 x 2 = the coloured content of ONE generation"),
    ("the branch point", "-", "WHERE CONJUGATION HAPPENS -- not a seat, an operation"),
    ("the turnaround", 3, "GENERATION -- deck Z_3, and NOT ON THIS FIGURE"),
]:
    print(f"  {a:>14} {str(b):>6} {c:>44}")
print()
for s in [
 "** SO THE TWELVE IS ONE GENERATION'S COLOURED CONTENT, ITS ANTIPARTICLES ARE THE SAME",
 "   TWELVE ACROSS THE WALL, AND THE GENERATION INDEX LIVES SOMEWHERE ELSE ENTIRELY. **",
 "   Every one of those three sentences is the corpus's, and I had all three and used none.",
 "",
 "⌗ ** AND THE COLOURLESS STATES ARE NOW UNOBSTRUCTED, WHICH IS THE WHOLE POINT. **  There is",
 "no longer anything competing for the walls.  Daryl's reading -- leptons at the Nariai",
 "points -- is not blocked by the generations, because the generations were never there.",
 "** The objection I raised against his proposal last turn was made of my own error. **",
 "",
 "⌗ AND ONE THING FALLS OUT THAT I COULD NOT SAY BEFORE.  A lepton must be COLOURLESS, and",
 "colour is now explicitly the hinge/wall index.  ** So a colourless object is one that is the",
 "SAME AT ALL THREE WALLS -- a Z_3-invariant of the wall structure, not an object sitting at",
 "one wall. **  That is a sharp criterion and it was unavailable while the walls were being",
 "read as generations, because a generation index is precisely NOT something you average over.",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE THREE THINGS I STILL CANNOT SEE")
print("=" * 78)
for s in [
 "① ** WHAT A STATE IS. **  Daryl settled the puncture: it is the VANTAGE, where an observer",
 "   stands and looks out along the slicing plane both ways.  ** A vantage is not obviously a",
 "   state. **  So of {puncture, leg, wall} I now know one is not a seat and I do not know",
 "   about the other two.  This is L-74's antecedent and it has been the hinge of everything",
 "   for four turns.  ** Every count I produce is conditional on it and I keep not saying so. **",
 "",
 "② ** WHETHER THE TURNAROUND THREE HAS ITS OWN FIGURE, AND WHAT IS ON IT. **  The generations",
 "   moved to the turnaround at c54.31 and ** nothing has ever been drawn there. **  If the",
 "   generation index lives on a structure nobody has depicted, then the question 'where are",
 "   the other two generations' has no picture to be answered in.  ** That is a gap of the",
 "   same kind as U3 was, and it is now the more important one. **",
 "",
 "③ ** WHETHER A LEPTON IS A Z_3-INVARIANT OR AN OBJECT AT A SINGLE WALL. **  PART 3 gives the",
 "   criterion -- colourless means same at all three walls -- but Daryl's reading puts leptons",
 "   AT Nariai points, which are the colour sites.  ** Those pull opposite ways, and the",
 "   resolution is probably the winding: a leg CROSSES a graze point (winding +-1/3, coloured)",
 "   and a state AT one has crossed nothing (winding 0, colourless). **  If that is right then",
 "   'at a wall' and 'Z_3-invariant' are the same condition and the tension is only apparent.",
 "   ** I can compute that once someone tells me whether a state at a graze point is at winding",
 "   zero or is undefined there. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — THE DIRECTION")
print("=" * 78)
for s in [
 "** DRAW THE TURNAROUND. **  That is the recommendation and it is not a small one.",
 "",
 "The reasoning: the corpus now has TWO threes doing different jobs -- the hinge three",
 "(colour, within-state) and the turnaround three (generation, deck Z_3) -- and it has drawn",
 "one of them and never the other.  Every confusion of the last four turns has been a",
 "collision between those two threes: the walls-as-generations error, the 12+3 arithmetic, the",
 "'walls already spent' objection, the horn asked to be both isospin and species.  ** They are",
 "all one mistake, which is reading a single figure as though it carried both threes. **",
 "",
 "And the turnaround is not short of structure to draw: the cubic whose roots form an",
 "EQUILATERAL triangle (P3 sec:temporal-threeness), the deck action tau -> tau + 2 pi i alpha/3",
 "permuting three cube-root sheets, the half-period carrying sinh^2 to -cosh^2, the wings at",
 "Im tau = +- pi alpha/3, and R reaching it exactly when D is even (P03_R_reaches_the_turnaround).",
 "** A figure of that is buildable today, from receipts that already exist. **",
 "",
 "⌗ AND THE PAYOFF IS DIRECT, not aesthetic: if the generation index is the turnaround's Z_3",
 "and the colour index is the hinge's S_3, then ** the question 'what are the colourless",
 "states' should be asked on the object where colour is DEFINED and generations are ABSENT --",
 "which is the hinge figure alone, with three walls free and nothing competing for them. **",
 "Daryl's Nariai-point reading is a proposal about exactly that object, and with the",
 "generations removed from it there is now room for the proposal to be true.",
 "",
 "** SO: draw the turnaround; then re-run the count on the hinge figure with the walls free;",
 "   then test Daryl's leptons against the Z_3-invariance criterion of PART 3. **  In that",
 "   order, because the first is what stops the two threes colliding again.",
]:
    print("  " + s)
