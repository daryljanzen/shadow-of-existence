#!/usr/bin/env python3
"""
L-44w — THE THREE LEADS `check_supersession` POINTED AT ON ITS FIRST CLEAN RUN, worked together
because the scan grouped them and because each is answered by banked work rather than by new.

  `L-44`  what IS the ellipse pair, physically, as against the designated root?
  `L-57`  is a generation seated on the HINGE or on an END -- the line or the piercing?
  `L-108` the winding charge against the Maxwell charge (blocked on `L-74`, since discharged)

** ALL THREE STRIKE, AND THE INSTRUMENT FOUND THEM RATHER THAN I DID -- which is the first
evidence that the eighth gate does the job it was built for. **

  PART 1  ** `L-44`: the pair characterised, and its own "generally" made exact. **
  PART 2  ** `L-57`: the question DISSOLVES -- a generation sits on neither. **
  PART 3  `L-108`: unblocked, and answered while it was blocked.
  PART 4  What the scan's hit-rate says, stated at its honest weight.

Run: python3 L044w_the_scan_cluster.py
"""
import sympy as sp

print(__doc__.split("Run:")[0])
r0 = sp.Symbol('r_0', real=True)
pair = [(-r0 + sp.sqrt(4 - 3*r0**2))/2, (-r0 - sp.sqrt(4 - 3*r0**2))/2]

# =====================================================================
print("=" * 78)
print("PART 1 — `L-44`: THE ELLIPSE PAIR, CHARACTERISED")
print("=" * 78)
for s in [
 "`L-44`: *'the designation $2{+}1$ is now named as an object and **its two sides have never",
 "been characterised**.  One is \"my horizon\"; the other is a conic pair holding, generally, one",
 "positive and one negative root -- **one of each species**.'*",
 "",
 "** ITS OWN 'GENERALLY' IS THE THING TO MAKE EXACT, AND `L-12`'s COMPUTATION ALREADY DOES. **",
]:
    print("  " + s)
print()
print(f"  the pair are the roots of $r^2 + r r_0 + r_0^2 - 1$:")
print(f"     sum     = {sp.simplify(sum(pair))}")
print(f"     product = {sp.simplify(sp.expand(pair[0]*pair[1]))}")
print()
print(f"  {'r_0':>10} {'pair':>28} {'signs':>12} {'one of each species?':>21}")
for v in ("0", "1/2", "1/sqrt(3)", "0.9", "1", "1.1", "2/sqrt(3)"):
    a = sp.nsimplify(v)
    vals = sorted([sp.simplify(x.subs(r0, a)) for x in pair], key=lambda z: sp.N(z))
    sg = [int(sp.sign(sp.N(x))) if sp.N(x) != 0 else 0 for x in vals]
    each = (1 in sg and -1 in sg)
    print(f"  {v:>10} {str([str(sp.N(x,5)) for x in vals]):>28} {str(sg):>12} {str(each):>21}")
print()
for s in [
 "⇒ ** THE PAIR HOLDS ONE OF EACH SPECIES EXACTLY WHEN $|r_0| < 1$, and both of one species when",
 "   $|r_0| > 1$ -- because the pair's PRODUCT is $r_0^2 - 1$. **  `L-44`'s 'generally' is",
 "   therefore precise and its boundary is the $M=0$ member, since $2M = r_0 - r_0^3$.",
 "",
 "⌗ ** SO THE TWO SIDES OF THE DESIGNATION SPLIT ARE: 'my horizon' (the designated root, one",
 "   object, always present) against a CONIC PAIR whose species content CHANGES ACROSS THE",
 "   de~Sitter member. **  The designated side is species-stable; the pair side is not.  ** That",
 "   asymmetry is the physical characterisation `L-44` asked for, and it was computed at c54.73",
 "   for a different lead. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — `L-57`: THE LINE OR THE PIERCING?")
print("=" * 78)
for s in [
 "`L-57`, restated at c54.19: *'is a generation seated on the HINGE or on an END?  The line or",
 "the piercing?  P14's own wall-binding language must decide, and the two answers differ in what",
 "the horn then is.'*",
 "",
 "⇒⇒ ** THE QUESTION DISSOLVES: A GENERATION IS SEATED ON NEITHER. **  P14 `sec:whichthree`",
 "   (c54.31) withdrew the generations-as-hinges reading outright -- the hinge $S_3$ is the",
 "   WITHIN-STATE index and the generations' threeness is the turnaround's deck $\\mathbb{Z}_3$,",
 "   which is not on the hinge figure at all.  ** So neither the line nor the piercing seats a",
 "   generation, and the disjunction the lead poses has no true branch. **",
 "",
 "⌗ ** AND THE DISTINCTION THE LEAD DREW IS STILL THE RIGHT ONE -- IT JUST INDEXES SOMETHING",
 "   ELSE, AND BOTH BRANCHES ARE NOW OCCUPIED: **",
 "",
 "     the LINE (which hinge)      ⇒  ** COLOUR **   -- each hinge owns one wall; the vantage",
 "                                    index is what the monodromy is diagonal in",
 "     the PIERCING (which horn)   ⇒  ** WEAK ISOSPIN ** -- $T$, the horn swap, which is also",
 "                                    what supplies the turnaround's transpositions",
 "",
 "⌗ *`L-57` worried that 'the two answers differ in what the horn then is'.  ** They do, and the",
 "   corpus has since answered what the horn is on independent grounds -- so the worry was",
 "   well-placed and is now spent. ***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — `L-108`: UNBLOCKED, AND ANSWERED WHILE BLOCKED")
print("=" * 78)
for s in [
 "`L-108` was re-triaged off `HOT` as ** BLOCKED on `L-74`'s antecedent ** -- is a matter field",
 "labelled by a ROUTE rather than a point? -- with the note that working it first 'would be",
 "building on an unshown premise'.",
 "",
 "✔ ** `L-74` WAS DISCHARGED AT c54.46: a matter field is route-labelled IF AND ONLY IF it is",
 "   coloured, shown from the field equation rather than assumed.  So the block is lifted. **",
 "",
 "⌗ ** AND THE QUESTION IT WAS BLOCKED ON WAS ANSWERED IN THE MEANTIME, TWICE. **",
 "     `L-123` (c54.47): ** the $\\mathbb{Z}_3$ is the OBSTRUCTION TO CHARGE BEING OBSERVABLE, not",
 "       a rival to it ** -- verified on ten contents.  The winding charge and the Maxwell charge",
 "       were never competing for the same job.",
 "     `L-125` (c54.48): ** charge = QUANTISATION (the geometry) + SIGN (the field) + STRENGTH",
 "       (the field, not supplied) ** -- a topological label quantises and cannot scale.",
 "",
 "⇒ ** SO `L-108`'s framing -- winding charge AGAINST Maxwell charge -- is the one thing the",
 "   answer removes.  They are not alternatives; they are different parts of one decomposition,",
 "   and the geometry supplies the smallest of the three. **",
 "",
 "⚠ *And the caution that produced this lead stands and is worth keeping in the strike: the",
 "c54.37 version of it was written without having read P9 and the CPT material, and had to be",
 "rewritten.  ** The lead's value was in refusing to be answered quickly, and it was right to",
 "wait. ***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — WHAT THE SCAN'S HIT-RATE SAYS")
print("=" * 78)
for s in [
 "** THE INSTRUMENT NAMED THESE THREE AND I HAD NOT LOOKED AT ANY OF THEM. **  On its first",
 "clean run `check_supersession` put `L-110`, `L-108`, `L-44`, `L-57` and `L-91` at the top; of",
 "the four checked here, ** three strike outright and one (`L-110`) is the sector's own standing",
 "spec rather than a supersedable item. **",
 "",
 "⌗ ** AT HONEST WEIGHT, THOUGH: the scan matches WORDS, and these leads and receipts share a",
 "   vocabulary because they are about the same objects. **  It cannot distinguish 'this receipt",
 "   answers this lead' from 'these two discuss the same thing', and it never will.  ** What it",
 "   buys is an ordering of where to look, and the ordering was good. **",
 "",
 "⌗ *One run is not a hit-rate.  Recorded as a first result, not as a validation.*",
]:
    print("  " + s)
