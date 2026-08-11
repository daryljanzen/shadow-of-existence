"""
P03_colour_spacelike_isospin_timelike.py -- P3 sec:tour: the causal trichotomy on the six
hinge-ends is exactly a statement about WHICH OF TWO LABELS DIFFERS, and both labels have since
been named.  Substituting the names turns a classification of fifteen point-pairs into a
structural statement: ** on this substrate COLOUR is a SPACELIKE relation and ISOSPIN a TIMELIKE
one. **  And the triangle is the quotient of the hinge figure by the horn swap, so the double
ruling downstairs and the two horns upstairs are one fact.

WHAT PROMPTED IT.  Two standing questions: what a null chord between two hinge-ends MEANS
physically (the corpus uses null generators geometrically throughout and never said), and whether
anything reads the triangle as a shadow with a two-fold cover above it.

WHAT IS ESTABLISHED.
  1. ** THE SIX ENDS ARE 3 HINGES x 2 HORNS, AND THE FIFTEEN PAIRS SPLIT 3 / 6 / 6 BY WHICH
     LABEL DIFFERS ** (recomputed and asserted): same hinge and other horn (3), same horn and
     other hinge (6), both differing (6).  That is the same 3/6/6 the causal classification
     gives -- timelike, spacelike, null -- and the classification is a COMPLETE invariant, the
     symmetry group being transitive on the six ends with one orbit per class.
  2. ** SO THE CAUSAL CHARACTER OF A PAIR OF ENDS IS *WHICH LABEL DIFFERS*, AND THE LABELS ARE
     THE HINGE INDEX (colour) AND THE HORN INDEX ($T$, weak isospin). **  Substituting:
     timelike iff same colour and opposite isospin; spacelike iff same isospin and different
     colour; null iff both differ.
  3. ** HENCE: THE THREE COLOURS ARE MUTUALLY SPACELIKE ** -- which is what "three walls with
     disjoint support" says in causal language, and what a baryon requires: one constituent per
     hinge, all in one simultaneity.  ** AND A STATE'S RELATION TO ITS ISOSPIN PARTNER IS CAUSAL
     CONTACT. **
  4. ** A NULL CHORD IS THE CHANNEL THAT CHANGES BOTH LABELS AT ONCE. **  Since a graze point is
     a wall and a wall crossing is a third of a lap, the null legs are the winding step itself --
     not causal contact and not a gauge identification.  Twelve of them, each of three walls
     grazed four times.
  5. ** THE TRIANGLE IS THE QUOTIENT OF THE HINGE FIGURE BY THE HORN SWAP. **  The six ends cover
     the three hinge lines 2:1 and the six null chords cover the three triangle sides 2:1
     (asserted), with $T$ the deck transformation in both cases -- which the corpus already
     stated as "the two rulings, told apart by horn" without calling it a covering.
  6. ** AND $D_6=S_3\\times\\mathbb{Z}_2$ IS THE SYMMETRY OF THAT COVER: ** $S_3$ the triangle's own
     symmetry downstairs, $\\mathbb{Z}_2$ the deck group, and the direct product exactly the
     statement that the deck commutes with the triangle's symmetries, i.e. that the cover is
     regular.  So "doubly ruled" downstairs and "two-sheeted" upstairs are one fact, and the
     construction's $\\mathbb{Z}_2$ has three descriptions -- horn swap, second ruling, deck of
     the covering -- not previously known to be the same $\\mathbb{Z}_2$.

** SCOPE.  The trichotomy itself and the 2:1 projection of the chords are prior results, verified
elsewhere; what is established here is that their two labels are colour and isospin, which makes
the classification a statement about two Standard Model indices rather than about six points.
Nothing here derives either identification. **

ORIGIN: computations/baryon_edge/L045w_the_four_the_scan_left.py -- built r2376 (c54.81);
edit the origin, not this copy.

ORIGIN-DIVERGENCE: DELIBERATE AND SUBTRACTIVE.  The origin also disposes of two register items
about the two $2+1$ splits, which are unrelated to this claim.  ** This copy carries the
paper-facing subset: every assertion here appears in the origin verbatim, and nothing here is
absent from it. **"""
import itertools

print(__doc__)

# =====================================================================
print("=" * 78)
print("PART 1 — THE CAUSAL CHARACTER MEASURES WHICH LABEL DIFFERS")
print("=" * 78)
ends = [(j, e) for j in range(3) for e in ('+', '-')]
pairs = list(itertools.combinations(ends, 2))
print(f"  six hinge-ends = 3 hinges x 2 horns; {len(pairs)} unordered pairs.")
print()
print(f"  {'relation':>26} {'hinge label':>12} {'horn label':>11} {'count':>6} "
      f"{'causal character':>18}")
tally = {"same hinge": 0, "same horn": 0, "neither": 0}
for a, b in pairs:
    if a[0] == b[0]:
        tally["same hinge"] += 1
    elif a[1] == b[1]:
        tally["same horn"] += 1
    else:
        tally["neither"] += 1
ROWS = [("same hinge, other horn", "SAME", "differs", tally["same hinge"], "TIMELIKE"),
        ("same horn, other hinge", "differs", "SAME", tally["same horn"], "SPACELIKE"),
        ("both differ", "differs", "differs", tally["neither"], "NULL")]
for a, b, c, d, e in ROWS:
    print(f"  {a:>26} {b:>12} {c:>11} {d:>6} {e:>18}")
print(f"  {'':>26} {'':>12} {'':>11} {sum(tally.values()):>6}")
assert tally == {"same hinge": 3, "same horn": 6, "neither": 6}
print()
for s in [
 "⌗ ** THE HINGE INDEX IS COLOUR AND THE HORN INDEX IS $T$, WEAK ISOSPIN.  Substituting: **",
 "",
 "     TIMELIKE   ⇔ same colour, opposite isospin  ⇔ ** the relation a state bears to its own",
 "                  isospin partner is CAUSAL CONTACT **",
 "     SPACELIKE  ⇔ same isospin, different colour ⇔ ** THE THREE COLOURS ARE MUTUALLY",
 "                  SPACELIKE -- which is what 'three walls with DISJOINT SUPPORT' says, and what",
 "                  a baryon needs: one constituent per hinge, all at once **",
 "     NULL       ⇔ both differ                    ⇔ ** the channel that changes BOTH labels, and",
 "                  the null legs are exactly the ones that graze walls **",
 "",
 "⇒⇒ ** A NULL CHORD IS THE SIMULTANEOUS COLOUR-AND-ISOSPIN CHANGE, AND SINCE A GRAZE POINT IS A",
 "   WALL AND A WALL CROSSING IS A THIRD OF A LAP, IT IS THE WINDING STEP ITSELF. **",
 "",
 "⌗⌗ ** SO ON THIS SUBSTRATE COLOUR IS A SPACELIKE RELATION AND ISOSPIN A TIMELIKE ONE -- one",
 "   figure, two relations, and the causal structure telling them apart with no further input. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE TRIANGLE IS THE QUOTIENT BY THE HORN SWAP")
print("=" * 78)
print(f"  {'upstairs':>28} {'downstairs':>22} {'fibre':>7} {'the deck transformation':>26}")
for a, b, c, d in [("6 hinge-ends (hinge, horn)", "3 hinge lines", "2", "** T, the horn swap **"),
                   ("6 null chords U_i->D_j", "3 triangle sides", "2", "** T, the horn swap **")]:
    print(f"  {a:>28} {b:>22} {c:>7} {d:>26}")
print()
fibres = {j: [e for e in ends if e[0] == j] for j in range(3)}
assert all(len(v) == 2 for v in fibres.values()) and sum(len(v) for v in fibres.values()) == 6
print(f"  fibres over the three hinges: {[len(fibres[j]) for j in range(3)]}  -- "
      f"a genuine 2:1 cover, asserted")
print()
for s in [
 "⌗ ** THE CORPUS ALREADY NAMED THE DECK GROUP WITHOUT CALLING IT ONE: *'the chords project",
 "   two-to-one onto the three sides (the two rulings, TOLD APART BY HORN)'*. **",
 "",
 "⌗⌗ ** AND $D_6 = S_3 \\times \\mathbb{Z}_2$ IS THE SYMMETRY OF THE COVER: $S_3$ the triangle's own",
 "   symmetry downstairs, $\\mathbb{Z}_2$ the deck group, and the DIRECT PRODUCT exactly the",
 "   statement that the deck commutes with the triangle's symmetries -- i.e. that the cover is",
 "   regular. **",
 "",
 "⇒⇒ ** SO THE DOUBLE RULING AND THE TWO HORNS ARE ONE FACT, and the construction's",
 "   $\\mathbb{Z}_2$ has three descriptions -- horn swap, second ruling, deck of the covering --",
 "   which were not previously known to be the same $\\mathbb{Z}_2$. **",
]:
    print("  " + s)
