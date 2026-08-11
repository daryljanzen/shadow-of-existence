#!/usr/bin/env python3
"""
L-128c — `L-128`'s LAST OWED ITEM, DISCHARGED BY READING P3 RATHER THAN BY COMPUTING.
And the discharge is better than the computation would have been, because ** P3 states the
needed fact in general, M-independently, and states it TWICE -- while I argued it from the
M = 0 embedding and carried an M-dependence caveat through five revisions for no reason. **

  PART 1  What was owed.
  PART 2  ** WHAT P3 ACTUALLY SAYS, IN ITS OWN INTRODUCTION AND AGAIN IN ITS OVERVIEW. **
  PART 3  ** AND IT EXPLAINS WHY BOTH READINGS WERE IN THE CORPUS -- which `L-128` recorded as
          an inconsistency and which is not one. **
  PART 4  What this costs me, stated plainly.

Run: python3 L128c_p3_already_said_it.py
"""
print(__doc__.split("Run:")[0])

# =====================================================================
print("=" * 78)
print("PART 1 — WHAT WAS OWED")
print("=" * 78)
for s in [
 "`L-128` settled the one-radius/three-radii fork by computing r_j = alpha sin(phi - theta_j) on",
 "the throat circle and evaluating it at all three walls.  ** It carried two caveats: the",
 "vantage-rotation step was a READING of P14's sentence, and the evaluation was the M = 0",
 "member. **  `L-128b` removed the fork's dependence on both by a combinatorial argument, and",
 "the register kept 'r on P3's slicing curve at M != 0' as the remaining constructive debt.",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — WHAT P3 ACTUALLY SAYS")
print("=" * 78)
for s in [
 "** P3's ABSTRACT: ** 'That this is a statement about the VACUUM construction and not about",
 "every structure built on the substrate is worth marking at the outset: the matter",
 "construction, which must PLACE its slicing planes at loci rather than merely chart the family,",
 "places one on EACH of the three hinges -- ** three throat walls at DISTINCT POINTS of the",
 "throat circle **, a one-hinge truncation being excluded as carrying an unfixed arbitrary",
 "modulus.'",
 "",
 "** P3 sec:overview, the same statement with one more word in it: ** 'the matter sector puts a",
 "plane on each, giving ** three throat walls at distinct points of the throat circle WITH",
 "DISJOINT SUPPORT **, a one-hinge truncation being excluded as carrying an unfixed arbitrary",
 "modulus.  The distinction is between ONE DOOR SWUNG THROUGH A FAMILY and THREE DOORS STANDING",
 "AT ONCE.'",
 "",
 "⇒ ** 'WITH DISJOINT SUPPORT' IS EXACTLY THE PREMISE `L-128` NEEDED AND COULD NOT COMPUTE. **",
 "   Disjoint support means each wall's structure is supported away from the others, so vantage",
 "   j's radial function does not vanish at wall k.  ** Reading (i) -- one radius vanishing at",
 "   all three walls -- is excluded by P3's own text, in general, with no M anywhere in it. **",
 "",
 "⌗ ** AND 'a one-hinge truncation being excluded as carrying an unfixed arbitrary modulus' is a",
 "   SECOND, INDEPENDENT argument against reading (i), of a kind neither `L-128` nor `L-128b`",
 "   used: not that one radius is geometrically wrong, but that truncating to one hinge leaves a",
 "   free parameter the construction cannot fix. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — AND IT EXPLAINS THE 'INCONSISTENCY', WHICH IS NOT ONE")
print("=" * 78)
for s in [
 "`L-128` recorded that 'the corpus contains two incompatible readings and has never noticed'.",
 "** P3 noticed, said so at the outset, and gave the rule. **",
 "",
 "   * for the VACUUM construction the three hinges are EQUIVALENT VANTAGES -- 'the root-exchange",
 "     is the hop from one to the next, and one swing charts the whole family, so a single door",
 "     suffices'.  ** Reading (i) is correct there. **",
 "   * for the MATTER construction the planes are PLACED, one per hinge, three walls at distinct",
 "     points with disjoint support.  ** Reading (ii) is correct there. **",
 "",
 "⇒ ** SO THE TWO READINGS ARE NOT INCOMPATIBLE, THEY ARE TWO CONSTRUCTIONS, AND P3 MARKS THE",
 "   DISTINCTION 'AT THE OUTSET' IN THOSE WORDS. **  What actually happened is narrower and",
 "   worse: ** `L-74` and `L-78` are MATTER computations that used the VACUUM convention. **",
 "   That is a real defect and `L-128`'s correction of it stands -- but the corpus was not",
 "   inconsistent, and saying it was is a claim against P3 that P3 does not deserve.",
 "",
 "⌗ *And the vacuum reading's correctness in its own domain is why the mistake was invisible: a",
 "single door genuinely does chart the whole vacuum family, so nothing in the vacuum sector ever",
 "objected.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — WHAT THIS COSTS ME")
print("=" * 78)
for s in [
 "① ** I ARGUED FROM AN EMBEDDING COMPUTATION AT M = 0 FOR A FACT P3 STATES IN GENERAL. **  The",
 "   computation is not wrong and its consistency test was worth running -- it returned P14's own",
 "   'the back, X_1 = -alpha' rather than being fitted to it.  ** But it was the weaker argument,",
 "   it carried an M-dependence caveat into P14's text, and that caveat was never necessary. **",
 "",
 "② ** AND I CALLED THE CORPUS INCONSISTENT ON A POINT ITS OWN PAPER MARKS 'AT THE OUTSET'. **",
 "   That is the same failure mode as c54.50's false alarm about the lap orientation, one level",
 "   up: ** finding a disagreement and recording it before reading far enough to see whether the",
 "   corpus had already resolved it. **  Twice in eight revisions, both times against P3, both",
 "   times resolved by reading rather than computing.",
 "",
 "③ ⇒ ** THE RULE THAT FOLLOWS, AND IT IS NARROWER AND MORE USEFUL THAN 'READ MORE': BEFORE",
 "   RECORDING A CONFLICT BETWEEN TWO PARTS OF THE CORPUS, READ THE ABSTRACT AND OVERVIEW OF THE",
 "   PAPER THAT OWNS THE OBJECT. **  Both of these were in an abstract.  Recorded to",
 "   `THE_BASE_RATE.md` beside the c54.50 entry, since they are one pattern.",
 "",
 "④ ** WHAT IS OWED AFTER THIS: nothing on `L-128`.  The constructive M != 0 exhibit would still",
 "   be nice to have and is no longer load-bearing for anything -- three independent arguments",
 "   now carry the fork, and one of them is the corpus's own general statement. **  `L-128` is",
 "   struck.",
]:
    print("  " + s)

# --- r2376+c54.161 : pin the claim, so the receipt can fail -------------------------------
# This receipt's whole content is a QUOTATION, hand-transcribed above.  So the assertion that
# tests its claim is the one that OPENS THE SLICING PAPER and finds the sentences there --
# in the abstract AND in the overview, "stated twice", with the overview carrying the one
# further word ("with disjoint support") on which the argument turns.  If P3's text is edited
# or the transcription drifts, this fires.
import os
_p3 = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "..", "corpus", "SdS-slicing-curve_v2.tex")
_tex = open(_p3, encoding="utf-8", errors="replace").read()

_ABSTRACT = ("the matter construction, which must place its slicing planes at loci "
             "rather than merely chart the family, places one on \\emph{each} of the three "
             "hinges---three throat walls at distinct points of the throat circle, a one-hinge "
             "truncation being excluded as carrying an unfixed arbitrary modulus")
_OVERVIEW = ("the matter sector puts a plane on each, giving three throat walls at distinct "
             "points of the throat circle with disjoint support, a one-hinge truncation being "
             "excluded as carrying an unfixed arbitrary modulus")
_DOORS = "The distinction is between one door swung through a family and three doors standing at once."
assert _ABSTRACT in _tex, "P3's abstract must contain the passage quoted in PART 2"
assert _OVERVIEW in _tex, "P3 sec:overview must contain the passage quoted in PART 2"
assert _DOORS in _tex, "P3 must contain 'one door swung through a family and three doors standing at once'"
# "stated twice": the one-hinge-truncation clause appears in exactly two places
assert _tex.count("a one-hinge truncation being excluded as carrying an unfixed arbitrary modulus") == 2, \
    "the premise is stated TWICE in P3 -- abstract and overview"
# and the ONE FURTHER WORD is the overview's alone -- that asymmetry is the receipt's point
assert _tex.count("with disjoint support") == 1, \
    "'with disjoint support' is the overview's one further word, and occurs once"
assert _tex.index(_ABSTRACT) < _tex.index(_OVERVIEW), \
    "the abstract statement must precede the overview statement"
# stated 'at the outset' and IN GENERAL: no mass parameter anywhere in either sentence
assert "at the outset" in _tex, "P3 marks the vacuum/matter distinction 'at the outset'"
assert "$M$" not in _ABSTRACT and "$M$" not in _OVERVIEW and "2M" not in _OVERVIEW, \
    "both statements are general -- no mass dependence, which is the whole cost recorded in PART 4"
# and the abstract's own vacuum half, which is why the one-radius reading was correct there
assert "for the vacuum geometry they are equivalent vantages" in _tex, \
    "P3's abstract states the VACUUM half: the three hinges are equivalent vantages"
