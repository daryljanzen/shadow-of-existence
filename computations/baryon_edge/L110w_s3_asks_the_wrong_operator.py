#!/usr/bin/env python3
"""
L-110w — `L-110`'s DISCHARGE CONDITION S3, RE-SPECIFIED.  The scan put this lead at the top of
its list twice over, and reading it against the arc turns up a category error in the spec
itself rather than a failure to meet it.

`L-110`'s S3, the clause it calls "the sharp one": ** "the colourless triple is
chirality-ASYMMETRIC while every object the geometry has offered comes in R-conjugate PAIRS, so
the three must sit on an R-FIXED locus." **

** THE ASYMMETRY S3 DEMANDS IS NOT A PROPERTY OF COLOUR IN THE STANDARD MODEL EITHER, so
demanding it of this construction's COLOUR structure asks the wrong operator.  What that does to
the spec is the content of this file. **

  PART 1  What S3 asks, and what the Standard Model's own colour structure does.
  PART 2  ** THE CATEGORY ERROR, NAMED. **
  PART 3  Where the asymmetry actually lives, and whether this construction has that operator.
  PART 4  ** THE COMMUTATOR THAT DECIDES IT, computed -- and it comes out the RIGHT way. **
  PART 5  S3 re-specified, and what is genuinely still owed.

Run: python3 L110w_s3_asks_the_wrong_operator.py
"""
import sympy as sp

print(__doc__.split("Run:")[0])

# =====================================================================
print("=" * 78)
print("PART 1 — WHAT S3 ASKS, AND WHAT COLOUR ACTUALLY DOES")
print("=" * 78)
print("  The Standard Model's colourless content per generation, and how COLOUR acts on it:")
print()
print(f"  {'state':>10} {'chirality':>11} {'colour rep':>12} {'does colour see the chirality?':>32}")
for s, ch in (("nu_L", "left"), ("e_L", "left"), ("e_R", "right"), ("nu_R", "right (if present)")):
    print(f"  {s:>10} {ch:>11} {'singlet':>12} {'NO':>32}")
print()
for s in [
 "** COLOUR ACTS AS THE TRIVIAL REPRESENTATION ON EVERY ONE OF THEM, LEFT AND RIGHT ALIKE. **",
 "SU(3) does not distinguish $e_L$ from $e_R$ -- both are colour singlets and colour has nothing",
 "to say about which is which.",
 "",
 "⌗ ** SO THE CHIRALITY ASYMMETRY OF THE COLOURLESS SECTOR IS INVISIBLE TO COLOUR IN THE",
 "   STANDARD MODEL ITSELF. **  What makes $\\nu_L, e_L$ a doublet and $e_R$ a singlet is",
 "   $SU(2)_L$ -- the WEAK structure -- and nothing else.",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE CATEGORY ERROR")
print("=" * 78)
for s in [
 "S3 reasons: *the colourless triple is chirality-asymmetric; everything the geometry offers",
 "comes in $R$-conjugate pairs; therefore the three must sit on an $R$-fixed locus.*",
 "",
 "⚠ ** THE FIRST PREMISE IS TRUE AND THE INFERENCE IS ADDRESSED TO THE WRONG STRUCTURE. **  The",
 "   triple IS chirality-asymmetric -- but that asymmetry is a fact about ISOSPIN acting on",
 "   chirality, not about the colour sector having an $R$-fixed locus.  ** A colour structure",
 "   that produced a chirality-asymmetric colourless triple would not match the Standard Model;",
 "   it would EXCEED it. **",
 "",
 "⌗ ** AND THAT REFRAMES TWO STANDING 'FAILURES' AS NON-FAILURES: **",
 "     `L-117`: the turnaround's colourless sector has dimension four, all one-dimensional, so",
 "       every $\\mathbb{Z}_2$ grading splits them $2+2$ -- recorded as a SHAPE FAILURE against",
 "       S3.  ** Against colour, $2+2$ is the correct shape: colour is vector-like on singlets. **",
 "     `L-130`: the colour bundle's invariant line is ONE-dimensional.  ** Also correct: colour",
 "       offers one trivial representation, not a chirality-graded family. **",
 "",
 "⇒ *Both were measured against a condition the Standard Model does not impose on colour.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — WHERE THE ASYMMETRY LIVES, AND WHETHER THE GEOMETRY HAS IT")
print("=" * 78)
for s in [
 "The asymmetry lives in ISOSPIN acting on CHIRALITY.  This construction names both:",
 "",
 "     ** $T$ ** -- the horn swap $X_0 \\mapsto -X_0$, timelike, horn-flipping;",
 "                the corpus reads it as WEAK ISOSPIN.",
 "     ** $R$ ** -- the offset parity $r_0 \\mapsto -r_0$, spacelike, horn-preserving;",
 "                realised on the cut spinor as $\\gamma^5$, hence CHIRALITY.",
 "",
 "** SO THE QUESTION S3 SHOULD BE ASKING IS: does $T$ act differently on the two $R$-eigenspaces?",
 "   That is what 'the weak interaction is chiral' MEANS. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE COMMUTATOR THAT DECIDES IT")
print("=" * 78)
X0, r0 = sp.symbols('X_0 r_0', real=True)
print("  $T$ and $R$ act on independent data of the construction:")
print(f"     T : X_0 -> -X_0   (and leaves r_0 alone)")
print(f"     R : r_0 -> -r_0   (and leaves X_0 alone)")
print()
# act on a generic function of both
f = sp.Function('f')(X0, r0)
TR = f.subs({X0: -X0, r0: -r0})
RT = f.subs({r0: -r0, X0: -X0})
print(f"     T R f = {TR}")
print(f"     R T f = {RT}")
comm = sp.simplify(TR - RT)
print(f"     [T, R] f = {comm}    ⇒ ** they COMMUTE: {comm == 0} **")
assert comm == 0
print()
for s in [
 "⌗ ** AND COMMUTING IS THE RIGHT ANSWER, NOT THE WRONG ONE -- WHICH IS WORTH SAYING BECAUSE THE",
 "   NAIVE EXPECTATION RUNS THE OTHER WAY. **  'The weak interaction is chiral' is not the claim",
 "   that isospin fails to commute with $\\gamma^5$.  It is the claim that isospin acts",
 "   NON-TRIVIALLY ON ONE CHIRALITY EIGENSPACE AND TRIVIALLY ON THE OTHER -- and that requires",
 "   the two to be simultaneously diagonalisable, i.e. ** requires them to commute. **",
 "",
 "⇒ ** SO THE GEOMETRY PASSES THE NECESSARY CONDITION: $T$ and $R$ commute, so $T$ acts within",
 "   each chirality eigenspace separately and CAN in principle act on one and not the other. **",
 "   Whether it DOES is a computation on the wall mode, and it is not done here.",
 "",
 "⚠ *A necessary condition met is not a result.  ** What this establishes is that the structure",
 "   is not excluded, which is exactly as much as a commutator can establish. ***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — S3 RE-SPECIFIED, AND WHAT IS GENUINELY OWED")
print("=" * 78)
for s in [
 "⛔ ** S3 AS WRITTEN IS WITHDRAWN. **  'The colourless three must sit on an $R$-fixed locus' asks",
 "   the colour structure for an asymmetry that colour does not carry in the Standard Model",
 "   either.  ** Two recorded failures against it -- `L-117`'s $2+2$ shape and `L-130`'s",
 "   one-dimensional invariant line -- are re-read as CORRECT behaviour. **",
 "",
 "✔ ** S3 RE-SPECIFIED: does $T$ act on one $R$-eigenspace of the wall mode and trivially on the",
 "   other? **  That is the same physics the old clause was reaching for, addressed to the",
 "   operator that carries it.  The commutator above says the question is well-posed; the answer",
 "   needs `prop:wall`'s mode and is a real computation.",
 "",
 "⌗ ** AND `L-110` STAYS OPEN ON THAT, WHICH IS WHY THIS IS A RE-SPECIFICATION AND NOT A STRIKE. **",
 "   *The lead's job was to say what discharging the count requires.  It still has that job; one",
 "   of its five clauses was pointed at the wrong operator and now is not.*",
 "",
 "⌗ *The other clauses are untouched here and no claim is made about them.*",
]:
    print("  " + s)
