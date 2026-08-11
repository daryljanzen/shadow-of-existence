#!/usr/bin/env python3
"""
L-76 — WHAT TRANSFORMS AS A CROSSING COUNT; AND FIRST, THE CRITERION I FAILED TO STATE.

Daryl:

  "Please note that walls and hinges are related to each other but are decidedly NOT the
   same thing.  And please ask in what way they need to be actually completely divorced
   from one another before you would allow that two different things like a wall and a
   hinge could be called separate things.  And please also clarify the greater scope of the
   problem.  What you really need, both ways."

** THE BAD INFERENCE, NAMED FIRST. **  At c54.23 I wrote: "wall <-> hinge is a bijection, so
walls and hinges are the same three; walls cannot be both colour and generation any more
than hinges can."  ** That is invalid, and the Standard Model is the counterexample sitting
in plain sight: colour and generation are BOTH threes, both permuted, and completely
independent. **  A bijection between two three-element sets says nothing whatever about
whether they carry the same physical label.  If it did, the Standard Model could not exist.

  PART 1  THE CRITERION.  What would actually make two things separate?  Stated as tests,
          and then run on wall vs hinge.
  PART 2  THE GREATER SCOPE, both ways.  What the geometry must supply; what the reading
          must supply back.  ** The requirement is INDEPENDENCE, not divorce. **
  PART 3  The twelve legs FACTORISE, and the third factor is provably chirality.
  PART 4  Two competing assignments, and what discriminates them.
  PART 5  ** L-76 PROPER: what transforms as a crossing count. **
  PART 6  15 = 12 + 3, registered with its refutation and not asserted.
  PART 7  What is owed.

Run: python3 L76_the_label_and_the_criterion.py     (sympy)
"""

import itertools
import sympy as sp
from fractions import Fraction as F

print(__doc__.split("Run:")[0])
HINGE = {k: 120 * k for k in (0, 1, 2)}
WALL = {k: (HINGE[k] + 180) % 360 for k in HINGE}
TOUCH = {k: sorted({(HINGE[k] - 60) % 360, (HINGE[k] + 60) % 360}) for k in HINGE}

# =====================================================================
print("=" * 78)
print("PART 1 — THE CRITERION.  When are two things in bijection SEPARATE things?")
print("=" * 78)
print("  I never stated one, which is how a bijection got used as an identity.  Stated now,")
print("  as five tests.  ** Two objects are the SAME thing only if they pass ALL five. **")
print()
tests = [
 ("LOCUS", "do they sit at the same place?"),
 ("TYPE", "are they the same kind of object -- same dimension, same category?"),
 ("DEFINITION", "is one definable from the other with no further data?"),
 ("EQUIVARIANCE", "is the bijection natural -- does it commute with the whole group?"),
 ("SEPARABILITY", "can a quantity take different values on the two?"),
]
print(f"  {'test':>16}  what it asks")
for a, b in tests:
    print(f"  {a:>16}  {b}")
print()
print("  Run on WALL vs HINGE:")
print()
rows = [
 ("LOCUS", "hinge: a line at transverse 2a, off the throat entirely",
           "wall: a point ON the throat, radius a", "DIFFER"),
 ("TYPE", "hinge: a LINE (timelike, 1-dimensional, in the ambient)",
          "wall: a POINT of the throat circle -- in the full geometry, the swept r=0 locus",
          "DIFFER"),
 ("DEFINITION", "hinge: the axis the slicing plane SWINGS about",
                "wall: where the SIGNED RADIUS FLIPS, r = 0", "DIFFER"),
 ("EQUIVARIANCE", "the antipodal map carries hinge k to wall k and commutes with D_3 x Z_2",
                  "-- so they ARE isomorphic as G-sets", "AGREE"),
 ("SEPARABILITY", "a hinge has 2 punctures on it; a wall has none",
                  "4 null legs meet a wall; 0 meet a hinge away from its punctures", "DIFFER"),
]
print(f"  {'test':>15} {'verdict':>9}   what it comes to")
for a, b, c, v in rows:
    print(f"  {a:>15} {v:>9}   {b}")
    print(f"  {'':>15} {'':>9}   {c}")
print()
print("  ** FOUR OF FIVE SAY THEY ARE DIFFERENT OBJECTS.  The one that says 'same' is")
print("     EQUIVARIANCE -- and equivariance of a bijection is exactly the property that")
print("     does NOT force identity of labels. **")
print()
print("  ⇒ ** AND HERE IS THE ANSWER TO DARYL'S QUESTION, WHICH IS SHARPER THAN 'DIVORCED'.")
print("     Two structures do NOT need to be unrelated to carry independent labels.  They")
print("     need to be independent AS FACTORS: the labels must be able to vary separately.")
print("     A canonical bijection between the INDEX SETS does not tie the labels together;")
print("     only a constraint on the PAIRS does. **")
print()
print("  The Standard Model is the proof that this is the right criterion: colour and")
print("  generation are both threes, both permuted by an S_3-like action, and no physicist")
print("  concludes from that that a red quark is a first-generation quark.")
print("  ** My c54.23 inference is RETRACTED. **")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE GREATER SCOPE, BOTH WAYS")
print("=" * 78)
print("  ⌗ WHAT THE GEOMETRY MUST SUPPLY (the forward direction).")
print("  A fermion state is not labelled by ONE index; it is labelled by a TUPLE:")
print("     (colour, isospin, chirality, generation)  -- and for quarks that is 3.2.2.3")
print("  ** So the question is never 'which three is colour'.  It is: WHICH GEOMETRIC")
print("     OBJECTS SUPPLY INDEPENDENT FACTORS, and is the set of realised tuples the FULL")
print("     PRODUCT or a constrained subset? **  A constrained subset is not a failure --")
print("     it is a prediction, and it is where a geometry can say more than a bundle can.")
print()
print("  ⌗ WHAT THE READING MUST SUPPLY BACK (the reverse direction, and it is the half I")
print("  have been neglecting).  If the geometry is right, the Standard Model's structure")
print("  is DATA ABOUT THE GEOMETRY:")
print("     · 15 Weyl states per generation, splitting 12 quark + 3 lepton")
print("     · quarks carry colour and leptons do not -- so the colour factor must be")
print("       ABSENT from the lepton sector, not merely trivial on it")
print("     · anomaly cancellation holds per generation and ONLY as a complete set (P14)")
print("     · exactly one of the two chiralities carries isospin")
print("  ** Each of those is a constraint the geometry must MEET, and a geometry that meets")
print("     them for a reason has said something.  I have been running this arrow in one")
print("     direction only. **")
print()
print("  ⌗ AND THE INCIDENCE THE GEOMETRY ACTUALLY HAS.  Not the free product:")
print()
print(f"  {'hinge':>6} {'its wall':>9} {'walls its legs cross':>22} {'own wall crossed?':>18}")
pairs = []
for k in HINGE:
    owners = sorted(w for w in HINGE if WALL[w] in TOUCH[k])
    for o in owners:
        pairs.append((k, o))
    print(f"  {k:>6} {WALL[k]:>7} d {str([WALL[o] for o in owners]):>22} "
          f"{str(k in owners):>18}")
print()
print(f"  ** REALISED (hinge, wall) INCIDENCES: {len(pairs)} of the 9 in the full product. **")
print("     The three missing are exactly the diagonal -- a hinge never crosses its own wall.")
print("  ** So the geometry supplies 3 x 3 MINUS A PERFECT MATCHING = 6, not a free 3 x 3. **")
print("     That is a constraint, hence a prediction, and it is the sort of thing a bundle")
print("     imposed by hand cannot produce.")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE TWELVE LEGS FACTORISE, AND THE THIRD FACTOR IS PROVABLY CHIRALITY")
print("=" * 78)
print("  A leg is (puncture, ruling) = (hinge, horn, which-of-the-other-two-walls).")
print()
legs = [(k, h, w) for k in HINGE for h in ('U', 'D')
        for w in sorted(o for o in HINGE if WALL[o] in TOUCH[k])]
print(f"  {'count':>8} = 3 hinges x 2 horns x 2 walls = {len(legs)}")
assert len(legs) == 12
print()
print("  ** AND THE THIRD FACTOR IS NOT A FREE LABEL -- IT IS THE HANDEDNESS, AND THE")
print("     HANDEDNESS IS ALREADY IDENTIFIED. **  L-61, verified: a hinge's two legs graze")
print("     at exactly -60 and +60 from its own azimuth, and each tangent is a Nariai cut")
print("     with r0 = (2/sqrt3) sin w at w = -30 and w = +30, so:")
for s, w in (('+', 30), ('-', -30)):
    r0 = sp.nsimplify(2/sp.sqrt(3) * sp.sin(sp.rad(w)))
    print(f"       the {s}60 leg  ->  w = {w:+3d} deg  ->  r0 = {r0}")
print("  and r0 -> -r0 is R, which P14 establishes IS gamma^5.")
print()
print("  ⇒ ** 12 legs = 3 (hinge) x 2 (horn) x 2 (chirality), with the last factor NOT")
print("     assigned but DERIVED. **  Two of the three factors are therefore already")
print("     pinned by earlier results, and only the first is in dispute.")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — TWO COMPETING ASSIGNMENTS, AND WHAT DISCRIMINATES THEM")
print("=" * 78)
print(f"  {'':>26} {'READING A':>26} {'READING B (P14 as it stands)':>30}")
for a, b, c in (("the hinge three is", "COLOUR", "GENERATION"),
                ("the horn two is", "weak isospin", "weak isospin"),
                ("the leg pair is", "chirality", "chirality"),
                ("so 12 legs are", "one generation's 12 quarks", "3 generations x 4 states"),
                ("generation comes from", "the OTHER three (turnaround)", "the hinges"),
                ("colour comes from", "the hinges", "NOWHERE -- still walled")):
    print(f"  {a:>26} {b:>26} {c:>30}")
print()
print("  ** THE DISCRIMINATOR, and it is not a preference. **")
print("  The causal trichotomy (receipt P03_hexagon_null_triple) forces a bound triple to")
print("  take ONE PUNCTURE PER HINGE: two on one hinge are timelike-separated, two on one")
print("  horn are spacelike, and only the cross pairs are null.  A baryon is three bound")
print("  constituents.  ** Under READING B a proton would be one quark from each of three")
print("  GENERATIONS, which is wrong.  Under READING A it is one of each colour, which is")
print("  right and is the definition of a colour singlet. **")
print()
print("  ⇒ ** READING A is forced by the binding structure, and it does NOT require walls")
print("     and hinges to be the same thing -- it requires them to be independent factors,")
print("     which PART 1 says they are. **")
print("  ⇒ AND THE COST IS PRECISE, not vague: P14's 'three walls = three generations' must")
print("     become 'three walls = something else', and the generation index must be sought")
print("     on the corpus's OTHER three (lem:twoturnings, the turnaround roots).  ** That is")
print("     L-67, and it is now forced rather than merely available. **")

# =====================================================================
print()
print("=" * 78)
print("PART 5 — L-76 PROPER: WHAT TRANSFORMS AS A CROSSING COUNT")
print("=" * 78)
print("  The question: L-73 defines a winding as a count of wall crossings.  ** Is there")
print("  anything in the corpus that ACTUALLY TRANSFORMS that way? **  Not by assignment.")
print()
print("  ⌗ THE PIECES, all established elsewhere and none of them introduced here:")
print("   (1) a wall IS the r = 0 locus, relative to its hinge          [P14 header; L-75]")
print("   (2) r = 0 is a BRANCH POINT, not a barrier, and the slicing")
print("       passes THROUGH it onto the conjugate branch                [P3 sec:lap]")
print("   (3) the turnaround law r^3 = 2M a^2 sinh^2(3 tau/2a) has a Z_3 deck action:")
print("       tau -> tau + 2 pi i a/3 leaves r^3 INVARIANT and sends r -> e^{2 pi i/3} r")
print("                                                       [P3 sec:temporal-threeness]")
print()
w3 = sp.exp(2 * sp.pi * sp.I / 3)
print("  ⌗ THE CUBE-ROOT SHEET INDEX.  r is a cube root of an invariant, so it carries a")
print("  sheet label in Z_3, and the deck action advances it:")
print()
print(f"  {'sheet n':>9} {'r on that sheet':>22} {'r^3':>8} {'label in thirds':>16}")
for n in range(4):
    val = sp.simplify(w3**n)
    print(f"  {n:>9} {str(val)+' . r0':>22} {'r0^3':>8} {str(F(n % 3, 3)):>16}")
print()
print("  ** THE SHEET INDEX IS A Z_3-VALUED LABEL THAT ADVANCES BY ONE PER PASSAGE THROUGH")
print("     THE BRANCH POINT, AND RETURNS TO ITSELF AFTER THREE.  That is precisely the")
print("     transformation law a crossing count must have -- and it was in the corpus")
print("     before any of this, derived from cosmic time's own imaginary period. **")
print()
print("  ⇒ ** SO L-76's ANSWER: the label that transforms as a wall-crossing count is the")
print("     CUBE-ROOT SHEET INDEX of the signed radius.  A wall crossing is a passage")
print("     through r = 0; r = 0 is the branch point of r^3; the deck action advances the")
print("     sheet by one third; three crossings close the orbit and return the label. **")
print()
print("  ⇒ AND IT MAKES THE CLOSURE RULE MEAN SOMETHING RATHER THAN STIPULATE IT.  A")
print("     composite is admissible iff its total sheet advance vanishes in Z_3 -- i.e. iff")
print("     the configuration returns to the SAME BRANCH it started on.  ** An object that")
print("     does not close is not a slicing of one manifold; it is a path that ends on a")
print("     different sheet from the one it began on. **  That is confinement stated in the")
print("     corpus's own analytic structure rather than as a selection rule.")
print()
print("  ⚠ WHAT IS STILL NOT DONE, AND IT IS ONE STEP, NOT A PROGRAMME.  prop:wall's mode")
print("  is exp(-int W) chi_+ with W = lambda sqrt(f)/r, odd in the signed radius.  ** The")
print("  step owed is to carry that solution through r = 0 on the branched bead and read")
print("  off the sheet advance it picks up. **  P14 already establishes the crossing is")
print("  through a branch point rather than a single-valued loop -- which is exactly the")
print("  condition under which a sheet advance is possible at all -- but the advance itself")
print("  has not been computed.  (L-78.)")

# =====================================================================
print()
print("=" * 78)
print("PART 6 — 15 = 12 + 3.  REGISTERED, WITH ITS REFUTATION, AND NOT ASSERTED.")
print("=" * 78)
print("  PART 3: the geometry carries 12 legs = 3 x 2 x 2.")
print("  PART 4 READING A: those are one generation's QUARK states -- and in the Standard")
print("  Model one generation's quarks are exactly 3 colours x 2 isospin x 2 chirality = 12.")
print()
print(f"  {'':>28} {'geometry':>12} {'SM, one generation':>20}")
for a, b, c in (("quark Weyl states", 12, 12),
                ("lepton Weyl states", 3, 3),
                ("total", 15, 15)):
    print(f"  {a:>28} {b:>12} {c:>20}")
print()
print("  ** THE 3 ON THE GEOMETRY SIDE IS THE THREE WALLS THEMSELVES -- the objects the")
print("     legs cross rather than the legs.  And leptons are precisely the triality-zero")
print("     sector, which is what 'carries no colour' means in L-73's terms. **")
print()
print("  ⚠ THIS IS THE MOST NUMEROLOGY-EXPOSED CLAIM IN THE WHOLE READING AND IS FLAGGED")
print("  AS SUCH.  Two things keep it from being a coincidence of small integers, and they")
print("  should be weighed and not waved:")
print("   (i) the 12 is not matched but FACTORISED, 3 x 2 x 2, with the SAME three factors")
print("       the Standard Model uses, and two of the three (horn = isospin, leg pair =")
print("       chirality) were fixed for other reasons before this count was taken;")
print("   (ii) the 12/3 SPLIT falls where the SM's does -- the legs carry the hinge label")
print("       and the walls do not, which is 'quarks carry colour and leptons do not'.")
print()
print("  ** REFUTED BY: any assignment on which the 3 walls cannot carry exactly the lepton")
print("     content -- e.g. if the wall states turn out to have a horn label, which would")
print("     make them 6 and not 3.  ** That is checkable and it has not been checked. **")
print()
print("  ⌗ AND ONE FURTHER THING, RECORDED BECAUSE IT IS TOO SHARP TO DROP AND TOO THIN TO")
print("  CLAIM.  With a right-handed neutrino the SM count is 16 = 12 + 4, and the geometry")
print("  would owe a FOURTH lepton state.  ** P14's own header says the Z_3-FIXED CENTRE")
print("  CARRIES NO WALL. **  A fixed point carrying no wall is the natural home of a state")
print("  with no charge of any kind, and a right-handed neutrino is exactly that -- sterile.")
print("  ** Registered as a question, asserted as nothing. **  (L-79.)")

# =====================================================================
print()
print("=" * 78)
print("PART 7 — WHAT IS OWED")
print("=" * 78)
for s in [
 "L-78  carry prop:wall's mode through r = 0 and compute the sheet advance.  ** The one",
 "      remaining step of L-76, and it is a computation on an existing solution. **",
 "L-67  the weld, now FORCED rather than available: generation must move to the",
 "      turnaround three, and P14's 'three walls = three generations' must be revised.",
 "      ** This reaches the dimension result's fold step. **",
 "L-79  does the Z_3-fixed centre carry the fourth lepton state?",
 "L-72  closure as a requirement -- PART 5 gives it an analytic meaning (same branch)",
 "      but not yet the status of a requirement.",
 "L-80  do the three wall states carry a horn label?  ** If they do, PART 6 is refuted. **",
]:
    print("  " + s)
print()
print("  ** AND THE METHODOLOGICAL RESULT, WHICH IS THE ONE I SHOULD KEEP. **  A bijection")
print("  is not an identity.  The test for whether two structures can carry independent")
print("  labels is whether the LABELS can vary independently, not whether the objects are")
print("  unrelated.  ** Wall and hinge are tightly related and completely distinct, and")
print("  that combination is not a tension -- it is what a factorisation looks like. **")
