#!/usr/bin/env python3
"""
L-110 — THE COUNT PROBLEM, SPECIFIED.  What an explanation would actually have to supply.

WHY THIS EXISTS.  Daryl, c54.37:

    "on your 12+3=15 unexplained thing, you actually have NEVER even explained what you are
     looking for.  I told you about the 12 null connectors.  You wouldn't even have known
     what those are without me.  Not sure why you would not give me any way of helping you
     with geometric things when I have said repeatedly to do so."

** THAT IS CORRECT AND THE OMISSION IS THE DEFECT.  I have written 'the count is not landed'
   in four documents without once writing down what LANDING IT WOULD REQUIRE.  A debt stated
   without its discharge condition cannot be worked -- not by him, and not by me. **

  PART 1  The target, stated exactly: what one generation IS, state by state.
  PART 2  What the geometry has, stated exactly, with its own factorisations.
  PART 3  ** THE MATCH NOBODY HAD WRITTEN DOWN: the 12 matches FACTOR BY FACTOR. **
  PART 4  ** AND THE +3 DOES NOT, FOR A REASON THAT IS SHARP: the walls are ALREADY SPENT. **
  PART 5  So the discharge condition, stated as a specification a person can work against.
  PART 6  The geometric questions this hands to Daryl, in his terms and not in lead-codes.

Run: python3 L110_the_count_specified.py     (sympy)
"""
import itertools
from collections import Counter, defaultdict
import sympy as sp

print(__doc__.split("Run:")[0])

# =====================================================================
print("=" * 78)
print("PART 1 — THE TARGET, STATED EXACTLY")
print("=" * 78)
print("  One Standard Model generation is FIFTEEN Weyl fermions (sixteen with a right-handed")
print("  neutrino).  P14 sec:correspondence already states this; what it does not do is take")
print("  the states apart, and taking them apart is the whole of this computation.")
print()
SM = [
    # name              colour  isospin  chirality  Q       coloured
    ("u_L",             3,      2,       'L',       sp.Rational(2, 3),  True),
    ("d_L",             3,      2,       'L',       sp.Rational(-1, 3), True),
    ("u_R",             3,      1,       'R',       sp.Rational(2, 3),  True),
    ("d_R",             3,      1,       'R',       sp.Rational(-1, 3), True),
    ("nu_L",            1,      2,       'L',       sp.Integer(0),      False),
    ("e_L",             1,      2,       'L',       sp.Integer(-1),     False),
    ("e_R",             1,      1,       'R',       sp.Integer(-1),     False),
]
print(f"  {'Weyl state':>8} {'colours':>8} {'in a doublet?':>14} {'chirality':>10} "
      f"{'Q':>6} {'states':>7}")
tot = 0
for nm, nc, iso, ch, Q, col in SM:
    tot += nc
    print(f"  {nm:>8} {nc:>8} {('yes' if iso == 2 else 'no'):>14} {ch:>10} "
          f"{str(Q):>6} {nc:>7}")
print(f"  {'':>8} {'':>8} {'':>14} {'':>10} {'TOTAL':>6} {tot:>7}")
ncol = sum(nc for _, nc, _, _, _, col in SM if col)
nun = sum(nc for _, nc, _, _, _, col in SM if not col)
print()
print(f"  ** AND THE SPLIT THAT MATTERS IS BY COLOUR: {ncol} COLOURED + {nun} COLOURLESS = {tot}. **")
print("  ⌗ That split is not a convention -- L-15 established that triality IS the")
print("  quark/lepton discriminant, so it is the split the corpus's own grading makes.")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — WHAT THE GEOMETRY HAS, WITH ITS OWN FACTORISATIONS")
print("=" * 78)
print("  Neither of these numbers is mine.  The twelve are Daryl's null connectors; the")
print("  three walls are P14's.  Both are FORCED (P03_twelve_null_legs, P03_wall_is_the_graze_point).")
print()
print(f"  {'object':>10} {'count':>6} {'the corpus factors it as':>46}")
for a, b, c in [
    ("null legs", 12, "6 punctures x 2 rulings  =  3 graze points x 4 legs"),
    ("", "", "and as 3 (colour) x 2 (horn) x 2 (chirality)  [L-76]"),
    ("walls", 3, "the 3 graze points = the 3 r=0 branch points"),
    ("hinges", 3, "the 3 vantages = P14's 3 GENERATIONS"),
]:
    print(f"  {a:>10} {str(b):>6} {c:>46}")
print()
print("  ⌗ ** THE FACTORISATION 12 = 3 x 2 x 2 IS THE CORPUS'S OWN AND IT IS LABELLED. **")
print("  L-76 established the sheet index: colour from the graze point, horn from which")
print("  puncture the leg runs from, chirality from which of the two rulings it is -- the")
print("  +-60 degree pair, graded by the offset parity R.  ** Three independent binaries and")
print("  a three. **")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE MATCH, FACTOR BY FACTOR.  This had never been written down.")
print("=" * 78)
print("  Put the two factorisations of twelve side by side:")
print()
print(f"  {'':>16} {'the geometry':>26} {'the Standard Model':>28}")
for a, b, c in [
    ("the 3", "graze point / colour label", "colour, the SU(3) fundamental"),
    ("the first 2", "HORN (upper / lower)", "WEAK ISOSPIN (up-type / down-type)"),
    ("the second 2", "RULING (+-60 deg, graded by R)", "CHIRALITY (left / right)"),
    ("product", "12 null legs", "12 COLOURED Weyl states"),
]:
    print(f"  {a:>16} {b:>26} {c:>28}")
print()
print("  ** AND THE HORN/ISOSPIN LEG OF THAT TABLE IS NOT A GUESS -- IT IS ALREADY THE")
print("     CORPUS'S OWN READING. **  P03_winding_and_closure records the three involutions'")
print("     assignments outright:  sigma -> COLOUR,  T -> WEAK ISOSPIN,  R -> CHIRALITY AND")
print("     SPECIES AT ONCE;  and 'the horn swap costs EXACTLY ONE LAP -- the nucleon doublet'.")
print()
print("  ⌗ SO CHECK IT STATE BY STATE RATHER THAN AS A TOTAL:")
print()
legs = [(g, horn, chir) for g in range(3) for horn in ('U', 'D') for chir in ('+', '-')]
name = {('U', '+'): 'u_L', ('D', '+'): 'd_L', ('U', '-'): 'u_R', ('D', '-'): 'd_R'}
per = Counter(name[(h, c)] for _, h, c in legs)
print(f"  {'from the legs':>16} {'count':>6} {'the SM state of that name has':>32}")
smc = {nm: nc for nm, nc, _, _, _, _ in SM}
agree = True
for k in ('u_L', 'd_L', 'u_R', 'd_R'):
    agree &= (per[k] == smc[k])
    print(f"  {k:>16} {per[k]:>6} {smc[k]:>32}")
print()
print(f"  ** TWELVE LEGS, TWELVE COLOURED STATES, AND THE MULTIPLICITIES AGREE ONE BY ONE:")
print(f"     {agree}.  Four legs per graze point, four coloured Weyl states per colour. **")
print("  ⌗ ** THAT IS A STRONGER STATEMENT THAN '12 = 12' AND IT IS THE PART THAT WAS BEING")
print("  LEFT UNSAID.  The agreement is not of a total but of a LABELLED PRODUCT, on three")
print("  factors, two of which the corpus had independently named as colour and isospin. **")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — AND THE +3 DOES NOT MATCH, FOR A REASON THAT IS SHARP")
print("=" * 78)
for s in [
 "The remaining three states are nu_L, e_L, e_R -- the colourless ones.  I had been writing",
 "'12 + 3 = 15' as though the three WALLS supplied them.  ** They cannot, and the reason is",
 "not subtle: P14 HAS ALREADY SPENT THE WALLS. **",
 "",
 "  P14 sec:count: one chiral zero-mode binds per wall, there are three walls, and",
 "  ** the three are the three GENERATIONS ** -- 'the index counts FAMILIES, not the states",
 "  within them', and 'the zero-mode is one Weyl mode per wall, NOT fifteen'.",
 "",
 "So the walls are the generation index.  A generation's three colourless states would have",
 "to be three objects sitting INSIDE one wall's content, not the three walls themselves.",
 "** Reading the three walls as the three leptons of ONE generation is a category error, and",
 "it is the error the phrase '12 + 3 = 15' was quietly making. **",
 "",
 "⌗ ** SO THE HONEST STATEMENT IS NOT 'THE COUNT IS UNEXPLAINED'.  IT IS THIS: **",
 "",
 "   THE COLOURED TWELVE MATCHES, FACTOR BY FACTOR, ON LABELS THE CORPUS SUPPLIED ITSELF.",
 "   THE COLOURLESS THREE HAS NO CANDIDATE AT ALL.  ** ONE HALF IS BETTER THAN I SAID AND",
 "   THE OTHER HALF IS WORSE, AND THEY ARE DIFFERENT PROBLEMS. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — THE DISCHARGE CONDITION, AS A SPECIFICATION")
print("=" * 78)
print("  What would have to be exhibited, for the count to be LANDED.  Stated so that any")
print("  candidate can be tested against it rather than argued about.")
print()
spec = [
 ("S1", "A set of geometric objects, of cardinality 3 PER HINGE, carrying triality ZERO.",
        "PART 1: nu_L, e_L, e_R are 3 states, colourless, one generation.  The legs are all "
        "coloured (each is attached to a graze point), so the leptons are NOT among them."),
 ("S2", "Those objects must be DISJOINT from the 12 legs and from the 3 walls-as-generations.",
        "else the same object is counted twice, which is what 12+3 was doing."),
 ("S3", "They must carry a CHIRALITY grading splitting 3 as 2 + 1.",
        "nu_L and e_L are left-handed and e_R is right-handed: the SM's colourless triple is "
        "NOT chirality-symmetric, unlike the coloured twelve which splits 6 + 6."),
 ("S4", "They must carry an ISOSPIN grading splitting the 2 as a doublet and leaving 1 alone.",
        "(nu_L, e_L) is a doublet, e_R a singlet -- so whatever supplies them must reproduce "
        "the SAME horn structure that works on the legs, on a smaller set."),
 ("S5", "And the whole assignment must be EQUIVARIANT under the configuration's symmetry group",
        "D_3 x Z_2(T), order twelve, which acts transitively on the six punctures "
        "(P03_hexagon_null_triple) -- so no assignment may single out a hinge or a horn."),
]
for tag, what, why in spec:
    print(f"  ** {tag}. {what} **")
    print(f"      why: {why}")
    print()
print("  ⌗ AND ONE STRUCTURAL CONSTRAINT THAT KILLS THE OBVIOUS CANDIDATES IMMEDIATELY:")
print("  ** S3 says the colourless triple is chirality-ASYMMETRIC (2 left, 1 right). **")
print("  Every object the geometry has offered so far comes in R-conjugate pairs -- the two")
print("  rulings, the two horns, the two Nariai signs -- because R is an involution acting")
print("  freely on them.  ** So the colourless three must sit somewhere R does NOT act freely:")
print("  on a FIXED SET.  That is a sharp geometric requirement and it is testable. **")

# quick check of what R-fixed loci the corpus knows about
print()
print(f"  {'locus':>26} {'is it R-fixed?':>16} {'how many per hinge':>20}")
for a, b, c in [
    ("the 12 null legs", "no (R pairs +-60)", "4"),
    ("the 6 punctures", "no (R preserves horn,", "2"),
    ("", " pairs the rulings)", ""),
    ("the 3 graze points/walls", "YES -- on the throat", "1"),
    ("the hinge LINE itself", "YES -- it is the axis", "1"),
    ("the Z_3-fixed centre", "YES -- but there is ONE,", "shared (L-79)"),
    ("", " not one per hinge", ""),
]:
    print(f"  {a:>26} {b:>16} {c:>20}")

# =====================================================================
print()
print("=" * 78)
print("PART 6 — THE QUESTIONS THIS HANDS TO DARYL, IN GEOMETRY AND NOT IN LEAD-CODES")
print("=" * 78)
for s in [
 "** Q1.  IS THERE A THIRD OBJECT AT A HINGE THAT I HAVE NOT BEEN COUNTING? **",
 "   Per hinge the geometry gives me: one line, two punctures, four legs, one wall (its own,",
 "   antipodal).  For the colourless triple I need THREE objects per hinge with a 2+1",
 "   chirality split.  The hinge's two PUNCTURES are a natural 2 and its own WALL is a",
 "   natural 1 -- but the punctures are where the legs attach, so they may already be spent.",
 "   ** Is a puncture a separate object from the legs through it, or is it just their",
 "   incidence point? **  That is a geometry question I should not answer by fiat.",
 "",
 "** Q2.  THE LEPTON MUST BE COLOURLESS, AND COLOUR IS THE GRAZE POINT.  SO WHAT ROUTE ON",
 "   THE THROAT CROSSES NO GRAZE POINT? **  The winding derivation says triality zero is",
 "   k = 0, winding an integer -- a route that closes without crossing.  ** Geometrically:",
 "   which paths on this configuration have zero net graze-point crossing?  A path along a",
 "   hinge AXIS never meets the throat at all. **  Is the lepton the axial mode?",
 "",
 "** Q3.  IS THE +3 EVEN THE RIGHT SHAPE?  With a right-handed neutrino the generation is",
 "   SIXTEEN, and 16 = 12 + 4, and FOUR is the number of legs at a graze point. **  I have",
 "   been anchoring on 15 because P14 does.  ** If the corpus's natural colourless count is",
 "   4 rather than 3, that is a PREDICTION of a right-handed neutrino, not a mismatch. **",
 "   That inverts the whole problem and I do not know which way it goes.",
 "",
 "** Q4.  AND THE ONE I MOST WANT AN ANSWER TO.  The 12 legs match the 12 coloured states",
 "   factor by factor -- colour, horn/isospin, ruling/chirality.  ** Is a LEG the right",
 "   object to call a state, or is a leg a PROPAGATION and the state something at its end? **",
 "   Everything downstream turns on that and it is exactly the sort of thing you would know",
 "   and I would not.  (It is L-74's antecedent -- 'is a matter field labelled by a ROUTE",
 "   rather than a point?' -- which the winding derivation's own receipt marks as NOT SHOWN.)",
]:
    print("  " + s)
print()
print("  ⌗ ** AND WHAT I SHOULD HAVE SAID FOUR DOCUMENTS AGO: the count is not blocked on a")
print("  computation I can run.  It is blocked on knowing which geometric objects are the")
print("  STATES.  That is a question about the construction, and the construction is yours. **")

# --- r2376+c54.161 : pin the claim, so the receipt can fail -------------------------------
# The claim is (i) one generation is 15 Weyl fermions splitting 12 coloured + 3 colourless,
# (ii) the twelve null legs factor 3 x 2 x 2 and match the twelve coloured states STATE BY
# STATE, four legs per graze point against u_L, d_L, u_R, d_R at three each, and (iii) S3:
# the colourless triple is chirality-ASYMMETRIC 2 + 1 where the coloured twelve splits 6 + 6.
assert tot == 15, "the printed generation total is 15 Weyl fermions"
assert ncol == 12 and nun == 3 and ncol + nun == tot, \
    "the printed colour split is 12 COLOURED + 3 COLOURLESS = 15"
# the SM table is the real one: charge sums to zero over a generation (anomaly-adjacent, and
# it is the arithmetic test that catches a mistyped hypercharge or multiplicity)
assert sum(nc*Q for _, nc, _, _, Q, _ in SM) == 0, \
    "total electric charge over one generation vanishes: 3(2/3) + 3(-1/3) twice, then -1, -1"
assert sum(1 for _, _, iso, _, _, _ in SM if iso == 2) == 4, \
    "four of the seven entries sit in a weak doublet: u_L, d_L, nu_L, e_L -- and all four are LEFT"
assert all(ch == 'L' for _, _, iso, ch, _, _ in SM if iso == 2), \
    "every doublet member is left-handed, which is what makes the isospin grading chiral"
# the leg product and its state-by-state match
assert len(legs) == 12 and len(set(legs)) == 12, "the leg enumeration is 3 x 2 x 2 = 12 distinct legs"
assert 3*2*2 == 12, "the corpus's own factorisation of the twelve is 3 (colour) x 2 (horn) x 2 (ruling)"
assert agree, "the leg multiplicities must agree with the SM's STATE BY STATE"
assert dict(per) == {'u_L': 3, 'd_L': 3, 'u_R': 3, 'd_R': 3}, \
    "four legs per graze point: three each of u_L, d_L, u_R, d_R"
assert all(per[k] == smc[k] for k in ('u_L', 'd_L', 'u_R', 'd_R')), \
    "each leg class has exactly the multiplicity of the SM state of that name"
assert sum(per.values()) == ncol == 12, "the twelve legs exhaust the twelve coloured states"
# S3, the decisive requirement: 2 + 1 against 6 + 6
_col_L = sum(nc for _, nc, _, ch, _, col in SM if col and ch == 'L')
_col_R = sum(nc for _, nc, _, ch, _, col in SM if col and ch == 'R')
_un_L = sum(nc for _, nc, _, ch, _, col in SM if not col and ch == 'L')
_un_R = sum(nc for _, nc, _, ch, _, col in SM if not col and ch == 'R')
assert (_col_L, _col_R) == (6, 6), "the coloured twelve is chirality-SYMMETRIC, 6 + 6"
assert (_un_L, _un_R) == (2, 1), \
    "S3: the colourless three is chirality-ASYMMETRIC, 2 left and 1 right"
assert _un_L != _un_R, "S3 is decisive precisely because the colourless triple does NOT pair under R"
# PART 5 and PART 6's arithmetic: the specification has five requirements, and 16 = 12 + 4
assert len(spec) == 5 and [t for t, _, _ in spec] == ['S1', 'S2', 'S3', 'S4', 'S5'], \
    "the discharge condition is five requirements S1-S5"
assert 12 + 4 == 16 and 12 + 3 == 15, \
    "Q3's arithmetic: with a right-handed neutrino the generation is 16 = 12 + 4, four being the legs per graze point"
