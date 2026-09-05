"""
P14_p3_already_said_it.py -- P14 sec:chirality: the premise the vantage reading of the wall
needed is stated in the slicing paper's own abstract and overview, in general and with no mass
dependence, and stated twice.  ** The two readings are therefore not an inconsistency in the
corpus but two constructions, which that paper distinguishes "at the outset". **

WHAT WAS OWED.  P14_the_wall_is_a_wall_of_a_hinge settled the one-radius/three-radii fork by an
embedding computation on the throat circle, carrying two caveats: the vantage-rotation step was
a reading, and the evaluation was the M = 0 member.  The constructive debt left standing was the
areal radius on the slicing curve at M != 0.

WHAT THE SLICING PAPER SAYS.  Abstract: "the matter construction, which must PLACE its slicing
planes at loci rather than merely chart the family, places one on EACH of the three hinges --
three throat walls at DISTINCT POINTS of the throat circle, a one-hinge truncation being
excluded as carrying an unfixed arbitrary modulus."  Overview, with one further word: "three
throat walls at distinct points of the throat circle WITH DISJOINT SUPPORT ... The distinction
is between one door swung through a family and three doors standing at once."

WHAT IS ESTABLISHED.
  1. ** "WITH DISJOINT SUPPORT" IS EXACTLY THE PREMISE THAT COULD NOT BE COMPUTED. **  Disjoint
     support means each wall's structure is supported away from the others, so one vantage's
     radial function does not vanish at another's wall.  The one-radius reading is excluded by
     the slicing paper's own text, in general, with no mass parameter anywhere in it.
  2. ** AND "a one-hinge truncation being excluded as carrying an unfixed arbitrary modulus" is
     a SECOND, INDEPENDENT argument of a kind neither earlier receipt used: not that one radius
     is geometrically wrong, but that truncating to one hinge leaves a free parameter the
     construction cannot fix. **
  3. ** SO THE "INCONSISTENCY" IS NOT ONE.  For the VACUUM construction the three hinges are
     equivalent vantages and one swing charts the whole family, so the single-radius reading is
     correct there; for the MATTER construction the planes are placed, one per hinge, and the
     three-radii reading is correct.  The slicing paper marks the distinction at the outset in
     those words. **  What actually happened is narrower and worse: the winding computations are
     MATTER computations that used the VACUUM convention.  That defect is real and its
     correction stands -- but the corpus was not inconsistent, and the earlier receipt's claim
     that it was is withdrawn.
  4. The vacuum reading's correctness in its own domain is why the error was invisible: a single
     door genuinely does chart the whole vacuum family, so nothing in the vacuum sector objected.

** WHAT THIS COSTS, STATED PLAINLY.  The M = 0 embedding computation is not wrong and its
consistency test was worth running -- it returned this paper's own "the back, X_1 = -alpha"
rather than being fitted to it -- but it was the weaker argument, and it carried an
M-dependence caveat into this paper's text that was never necessary.  Worse, a conflict was
recorded against a paper that marks the distinction in its abstract.  That is the same failure
mode as the lap-orientation false alarm one level up: recording a disagreement before reading
far enough to see whether it had already been resolved.  Twice in eight revisions, both times
against the same paper, both times resolved by reading rather than computing.  The rule that
follows is narrower than "read more": BEFORE RECORDING A CONFLICT BETWEEN TWO PARTS OF THE
CORPUS, READ THE ABSTRACT AND OVERVIEW OF THE PAPER THAT OWNS THE OBJECT.  Both of these were in
an abstract. **

ORIGIN: computations/baryon_edge/L128c_p3_already_said_it.py -- built r2376 (c54.58); edit the
origin, not this copy."""
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

# ⛔⛭⛭ r4070 (node 60): ** THE QUOTATION THIS RECEIPT PINS WAS DELETED FROM P3, AND THE
#   RECEIPT WAS RIGHT TO GO RED.  **  61's r4029/r4035 cut P3's abstract and "brought the
#   introduction and closing inside its own vocabulary".  Checked at source, every trace of the
#   premise is GONE from P3 -- not relocated into the body:
#       "with disjoint support"                 P3: 0   (was the ONE FURTHER WORD the argument turns on)
#       "a one-hinge truncation being excluded" P3: 0
#       "one-hinge" / "truncation"              P3: 0 / 0
#       "three throat walls" / "three planes"   P3: 0 / 0
#   *and r4035's diff on P3 is 4 insertions against 5 deletions -- an edit, not a move.*
#
# ⇒ ** THE CORPUS HAS NOT LOST THE PREMISE.  P14 CARRIES IT, four times, in its own voice. **
#   *What is lost is the INDEPENDENT SUPPORT, which is this receipt's entire thesis: "the two
#   readings are therefore not an inconsistency in the corpus but two constructions, which THAT
#   PAPER distinguishes at the outset."*  ⇒ *** P3 no longer distinguishes them at the outset, so
#   P14's premise now rests on P14 alone. ***
#
# ⌗ ** THE PINS ARE NOT RE-ANCHORED TO TEXT THAT WAS DELETED ON PURPOSE, AND THE FINDING IS NOT
#   ERASED BY MAKING THIS RECEIPT GREEN. **  It now asserts WHAT IS TRUE -- P14 carries it, P3 does
#   not -- so the receipt runs; and it REGISTERS the loss below so the signal survives the repair.
#   *A receipt repaired into silence is worse than a receipt that fails.*
import os
_p3 = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "..", "corpus", "SdS-slicing-curve_v2.tex")
_p14 = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    "..", "..", "corpus", "matter_sector_paper.tex")
_tex = open(_p3, encoding="utf-8", errors="replace").read()
_m14 = open(_p14, encoding="utf-8", errors="replace").read()

# ⓵ WHAT IS STILL TRUE: P14 states the premise itself, and the load-bearing clause is there.
assert _m14.count("disjoint support") >= 1, \
    "P14 must still carry 'disjoint support' -- if this fires the premise is lost from the corpus"
assert "unfixed arbitrary modulus" in _m14, \
    "P14 must still carry the one-hinge exclusion in its own voice"

# ⓶ WHAT WAS LOST, asserted as a FACT so the loss is checkable and cannot be quietly reversed
#    without this receipt noticing in the other direction.
assert "disjoint support" not in _tex, \
    ("P3 has regained 'disjoint support'.  That is GOOD NEWS and this receipt must be rewritten "
     "to its original form: the cross-paper support is back.")
assert "one-hinge" not in _tex, \
    "P3 has regained the one-hinge clause -- rewrite this receipt to its original form"

# ⓷ WHAT SURVIVES, AND THE FORM IT SURVIVES IN -- which is the precise finding.
#   ** P3 did not simply delete the reading.  It CONDITIONALISED it. **  The sentence now reads:
#       "A construction that must \emph{place} its slicing planes at loci, rather than chart a
#        family with one of them, WOULD read the three hinges differently---the distinction is
#        between one door swung through a family and three doors standing at once."
#   ⇒ *So P3 keeps the DISTINCTION and drops the ASSERTION.  It no longer says that the matter
#     construction places one plane on each hinge with disjoint support; it says what such a
#     construction WOULD look like.*  ⌗ *That is r4035's stated purpose -- "brought inside its own
#     vocabulary" -- carried out correctly: a slicing paper should not speak for the matter
#     paper's construction.*  ** The cost is that P14's premise lost its independent statement,
#     and THAT is what this receipt now records rather than certifies. **
_DOORS = "the distinction is between one door swung through a family and three doors standing at once"
assert _DOORS in _tex, \
    "P3 must still contain the doors distinction -- if this goes too, P3 retains nothing of the reading"
_CONDITIONAL = "would read the three hinges differently"
assert _CONDITIONAL in _tex, \
    ("P3's surviving statement must be the CONDITIONAL one.  If this fires, P3 has either "
     "re-asserted the reading or dropped it entirely -- both change this receipt's verdict.")
# ⓸ THE VACUUM HALF SURVIVES, AND IT WAS SHARPENED RATHER THAN CUT.
#   *Old wording: "for the vacuum geometry they are equivalent vantages" -- gone.
#    Current:     "for the \\emph{vacuum} construction OF THIS PAPER they are equivalent
#                  vantages---the root-exchange $\\sigma$ is the hop from one to the next, and one
#                  swing charts the whole family".*
#   ⇒ ** The added words "of this paper" are the same move as ⓷: P3 scoping its claim to itself. **
#     *So the vacuum half is intact and BETTER bounded, while the matter half is no longer P3's to
#     state.  Both halves changed in the same direction, which is what makes r4035 a coherent pass
#     rather than an accident.*
_VACUUM = "construction of this paper they are equivalent vantages"
assert _VACUUM in _tex, \
    "P3 must still state the VACUUM half -- the three hinges as equivalent vantages"
assert "the root-exchange $\\sigma$ is the hop from one to the next" in _tex, \
    "P3's vacuum half must still carry the root-exchange as the hop between vantages"

# ⓹ AND THE SURVIVING STATEMENTS ARE STILL GENERAL -- no mass parameter in either, which was the
#    whole cost recorded in PART 4 and is unchanged by the rewording.
_span_start = _tex.index(_CONDITIONAL)
_span = _tex[max(0, _span_start - 400):_span_start + 400]
assert "$M$" not in _span and "2M" not in _span, \
    "P3's surviving statement of the reading must remain mass-free"

# ⛔ ⓺ THE PHRASE THE RECEIPT'S PROSE QUOTES -- "at the outset" -- IS GONE FROM P3.
#    *PART 2 above says the two readings are "not an inconsistency in the corpus but two
#    constructions, which that paper distinguishes AT THE OUTSET".  P3 no longer uses that phrase,
#    and no longer distinguishes them at the outset: the matter reading now appears only as a
#    conditional aside.*  ⇒ ** Asserted as an absence so the receipt's own prose cannot drift back
#    into claiming a marker the paper does not carry. **
assert "at the outset" not in _tex, \
    ("P3 has regained 'at the outset'.  If so the distinction may be marked again -- re-read the "
     "paper and restore this receipt's original thesis rather than leaving this inverted check.")
