"""
P03_winding_and_closure.py -- P3 sec:lap / sec:tour: charge as winding on the equator, the
closure rule against the hadron spectrum, and the three involutions against the Standard
Model's three discrete structures.

THE ARITHMETIC, EXACT.  Q(u) = +2/3, Q(d) = -1/3, and Q(u) - Q(d) = 1 EXACTLY.  Split into
fractional and integer parts:
    u, d       -> fractional part 2/3 BOTH; integer parts 0 and -1
    ubar, dbar -> fractional part 1/3 BOTH; integer parts -1 and 0
    e-, nu     -> fractional part 0 BOTH
** So the fractional part does NOT distinguish u from d.  It distinguishes QUARK from
ANTIQUARK, as 2/3 one way round against 1/3 the other -- and 2/3 + 1/3 = 1.  The INTEGER
part is what distinguishes u from d, and it is exactly ONE LAP. **

That is the three hinges cutting the equator into arcs of 120 and 240 degrees, which are
ONE arc read the two ways round.  (Daryl: "the 1/3 vs 2/3 of the equator, i.e. 120 vs 240
... they're even the opposite direction".)

THE CLOSURE RULE, TESTED.  Assign fractional part 2/3 to a quark and 1/3 to an antiquark;
admit a composite only if the total closes, sum = 0 mod 1.  Checked against eleven contents:
closes AND observed -- meson, baryon, antibaryon, tetraquark, pentaquark, dibaryon; does NOT
close AND not observed -- free quark, diquark, qq-qbar, qqqq, qqq-qbar.  ** 11 of 11 agree. **
This is QCD's triality selection rule; the point is that THE CORPUS ALREADY OWNS THE Z_3 --
P3 sec:temporal-threeness derives r -> e^{2 pi i/3} r from cosmic time's imaginary period
2 pi i alpha / 3, for its own reasons.  And an isolated quark does not close, which makes
confinement a candidate statement about FAILURE TO CLOSE THE LAP rather than about a force.

THE THREE INVOLUTIONS.  sigma (root exchange, the Weyl S_3 on three hinges) -> COLOUR, with
a bound triple forced one-per-hinge by the causal trichotomy.  T (horn swap) -> WEAK ISOSPIN,
and the horn swap costing exactly one lap of charge is the same sentence as the W carrying
one unit.  R (offset parity; mass-odd, charge-even; = gamma^5) -> CHIRALITY and SPECIES at
once, which is REQUIRED for a Weyl field rather than a conflation.

** WHAT IS NOT ESTABLISHED. **  That a constituent's fractional charge IS its equatorial arc
rather than merely sharing its arithmetic -- the one load-bearing identification, stated as a
proof obligation and not made.  That the hinge three can be colour while the corpus welds
roots = hinges = walls = GENERATIONS into one 3 (COMBINATORICS L8.1-a): the weld must split
or be argued to carry both, and that reaches the dimension result's fold step.  That the axis
carries two lepton states.  Registered term by term, each with a refutation clause, in
THE_FERMION_SECTOR_GEOMETRY.md.

ORIGIN: computations/baryon_edge/L65_the_winding_and_the_whole_sector.py -- built r2376
(c54.21); edit the origin, not this copy."""

import itertools
from fractions import Fraction as F
import sympy as sp

print(__doc__.split("Run:")[0])

# =====================================================================
print("=" * 78)
print("PART 1 — THE ARITHMETIC OF THE THIRDS, AND WHAT EACH PART ACTUALLY CARRIES")
print("=" * 78)
u, d = F(2, 3), F(-1, 3)
print(f"    Q(u) = {u}    Q(d) = {d}    Q(u) - Q(d) = {u - d}   <-- EXACTLY ONE")
print()
print("  So take them apart into a fractional part (mod 1) and an integer part:")
print()
print(f"  {'field':>8} {'Q':>7} {'Q mod 1':>9} {'integer part':>14}")
for nm, q in (('u', u), ('d', d), ('ubar', -u), ('dbar', -d),
              ('e-', F(-1)), ('nu', F(0))):
    print(f"  {nm:>8} {str(q):>7} {str(q % 1):>9} {str(q - (q % 1)):>14}")
print()
print("  ** AND HERE IS WHAT I HAD BACKWARDS. **")
print("     Q(u) mod 1 = 2/3   and   Q(d) mod 1 = 2/3.   ** THEY ARE EQUAL. **")
print("     Q(ubar) mod 1 = 1/3 and Q(dbar) mod 1 = 1/3.  ** ALSO EQUAL. **")
qmod = {nm: q % 1 for nm, q in (('u', u), ('d', d), ('ubar', -u), ('dbar', -d))}
same_q = qmod['u'] == qmod['d']
same_a = qmod['ubar'] == qmod['dbar']
opp = qmod['u'] + qmod['ubar'] == 1
print(f"       quarks share a fractional part:      {same_q}   (= {qmod['u']})")
print(f"       antiquarks share a fractional part:  {same_a}   (= {qmod['ubar']})")
print(f"       and the two are the two ways round:  {opp}   (2/3 + 1/3 = 1)")
print()
# --- r2376+c54.159 -----------------------------------------------------------------
# PART 1's CLAIM, ASSERTED.  Three verdict flags were computed and only printed.  With the
# exact arithmetic pinned (INDEX: "u and d BOTH have fractional part 2/3; ubar and dbar
# BOTH have 1/3; 2/3 + 1/3 = 1"):  Q(u) - Q(d) = 1 exactly; the fractional part is 2/3 for
# BOTH quarks and 1/3 for BOTH antiquarks, so it separates quark from antiquark and NOT
# u from d; and the integer parts of u and d are 0 and -1, one lap apart.
assert u - d == 1, "Q(u) - Q(d) must be exactly 1"
assert qmod['u'] == F(2, 3) and qmod['d'] == F(2, 3) and same_q, \
    "both quarks must have fractional part 2/3"
assert qmod['ubar'] == F(1, 3) and qmod['dbar'] == F(1, 3) and same_a, \
    "both antiquarks must have fractional part 1/3"
assert opp, "the quark and antiquark fractional parts must be the two ways round, 2/3 + 1/3 = 1"
assert (u - u % 1, d - d % 1) == (F(0), F(-1)), \
    "the INTEGER parts of u and d must be 0 and -1 -- exactly one lap"
# -----------------------------------------------------------------------------------
print("  ⇒ ** THE FRACTIONAL PART DOES NOT DISTINGUISH u FROM d.  IT DISTINGUISHES QUARK")
print("       FROM ANTIQUARK -- and it does so as 2/3 ONE WAY ROUND against 1/3 THE OTHER. **")
print("  ⇒ ** THE INTEGER PART IS WHAT DISTINGUISHES u FROM d, AND IT IS EXACTLY ONE LAP. **")
print()
print("  Which is Daryl's sentence, term for term: the 2/3 vs 1/3 of the equator IS the")
print("  charge distinction, and 'they're even the opposite direction'.  The equator is cut")
print("  by the three hinges into arcs of 120 and 240 degrees -- 1/3 and 2/3 -- and those")
print("  are ONE arc read the two ways round, differing by a full lap.")
print()
print("  ** SO THE TRANSITIVITY OBJECTION I RAISED IS EMPTY. **  Transitivity forbids an")
print("  absolute label ON a puncture.  An arc is a relation BETWEEN two punctures with a")
print("  direction on it; the group acts on those consistently and averages nothing away.")
print("  ** I had turned the corpus's own relativity into an obstacle to using it. **")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE CLOSURE RULE, AGAINST EVERY HADRON TYPE")
print("=" * 78)
print("  Proposed rule, and it is the corpus's own lap made into a selection rule:")
print("    · every quark carries fractional part 2/3 (one direction round the equator)")
print("    · every antiquark carries 1/3 (the other)")
print("    · ** a composite exists only if the total fractional part CLOSES: sum = 0 mod 1 **")
print("  i.e. the walk round the equator must come back to where it started.")
print()
def closes(nq, nqbar):
    tot = F(2, 3) * nq + F(1, 3) * nqbar
    return tot % 1 == 0, tot

CASES = [
    ("q            (a free quark)", 1, 0, False),
    ("q qbar       (meson)",        1, 1, True),
    ("q q          (diquark)",      2, 0, False),
    ("q q q        (baryon)",       3, 0, True),
    ("q q q q      ",               4, 0, False),
    ("q q qbar     ",               2, 1, False),
    ("q q q qbar   ",              3, 1, False),
    ("q q qbar qbar(tetraquark)",   2, 2, True),
    ("q q q q qbar (pentaquark)",   4, 1, True),
    ("q q q q q q  (dibaryon)",     6, 0, True),
    ("qbar qbar qbar (antibaryon)", 0, 3, True),
]
print(f"  {'content':>28} {'total frac':>11} {'closes?':>8} {'observed in nature?':>21} {'agree?':>7}")
allagree = True
for label, nq, nqb, observed in CASES:
    ok, tot = closes(nq, nqb)
    agree = (ok == observed)
    allagree &= agree
    print(f"  {label:>28} {str(tot):>11} {str(ok):>8} {str(observed):>21} {str(agree):>7}")
print()
print(f"  ** THE RULE AGREES WITH THE OBSERVED HADRON SPECTRUM ON EVERY CASE: {allagree} **")
# --- r2376+c54.159 -----------------------------------------------------------------
# PART 2's CLAIM, ASSERTED.  The file computed the verdict flag `allagree` and only printed
# it.  INDEX: "tested against eleven contents and agrees 11 of 11 with the observed hadron
# spectrum".  Pinned: there are ELEVEN cases, all agree, and the discriminating pair is
# named explicitly -- the free quark totals 2/3 and does NOT close, the baryon totals 2 and
# DOES; the antibaryon (0 quarks, 3 antiquarks) totals 1 and closes.
assert len(CASES) == 11, "the closure rule must be tested against eleven contents"
assert allagree, "the closure rule must agree with the observed spectrum on every case"
assert closes(1, 0) == (False, F(2, 3)), "a free quark totals 2/3 and must NOT close"
assert closes(3, 0) == (True, F(2)), "a baryon totals 2 and must close"
assert closes(0, 3) == (True, F(1)), "an antibaryon totals 1 and must close"
assert closes(2, 0)[0] is False and closes(1, 1)[0] is True, \
    "a diquark must not close and a meson must"
# -----------------------------------------------------------------------------------
print("  Every combination nature shows closes; every combination nature forbids does not.")
print("  ** This is the standard TRIALITY / Z_3 selection rule of QCD -- and the point is")
print("     not that it is new physics but that THE CORPUS ALREADY OWNS THE Z_3. **")
print()
print("  P3 sec:temporal-threeness, established there for its own reasons:  the shift")
print("  tau -> tau + 2 pi i alpha / 3 leaves r^3 invariant and permutes the three cube-root")
print("  sheets cyclically, r -> e^{2 pi i/3} r: ** the turnaround cubic's Z_3 and cosmic")
print("  time's own imaginary period are ONE OBJECT. **")
print("  ⇒ ** so the triality that selects the hadron spectrum is a candidate for the SAME")
print("     Z_3 the corpus derives from the deck action of cosmic time's period. **")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — WHAT THAT MAKES CONFINEMENT")
print("=" * 78)
print("  A single quark has total fractional part 2/3, which is not 0 mod 1.")
print("  ** So the walk does not return.  The lap does not close. **")
print()
print("  And P3 sec:lap is not silent about unclosed laps -- closure is the whole point:")
print("  'run inward to the seam, around the throat through r = 0 ... and out onto the real")
print("  conjugate branch, the curve CLOSES on the backward-radial root.  This LAP makes")
print("  the slicing ONE CLOSED OBJECT ON ONE MANIFOLD.'")
print()
print("  ⇒ ** CONFINEMENT AS A CANDIDATE STRUCTURAL STATEMENT: an isolated quark is not")
print("     forbidden by a force law but by FAILURE TO CLOSE -- it is not a slicing of the")
print("     manifold at all, because the object CR admits is the closed lap. **")
print("  ⇒ and the composites that DO close are exactly the ones nature shows (PART 2).")
print()
print("  ⚠ WHAT IS NOT SHOWN.  That the fractional part of a constituent's charge IS its")
print("  equatorial arc, rather than merely sharing its arithmetic.  ** That is the load-")
print("  bearing identification and it is stated as a proof obligation, not made here. **")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE THREE INVOLUTIONS AGAINST THE THREE DISCRETE SM STRUCTURES")
print("=" * 78)
print("  The corpus establishes three distinct involutions and has never put them beside")
print("  the Standard Model's three discrete structures.  Laid side by side:")
print()
rows = [
 ("sigma", "root exchange; the Weyl S_3 permuting the THREE HINGES",
  "COLOUR", "3 hinges = 3 colours; a triple takes one per hinge = a colour singlet"),
 ("T", "horn swap X0 -> -X0; exchanges the two ends of EVERY hinge",
  "WEAK ISOSPIN", "u <-> d; and PART 1 says that costs exactly ONE LAP of charge"),
 ("R", "offset parity r0 -> -r0; mass-odd, charge-even; = gamma^5 in P14",
  "CHIRALITY / SPECIES", "left vs right, and 3 vs 3bar -- one operator, as it must be for a Weyl field"),
]
print(f"  {'involution':>10}  {'what it is in the corpus':>52}")
for a, b, c, dsc in rows:
    print(f"  {a:>10}  {b:>52}")
    print(f"  {'':>10}  -> {c:<20} {dsc}")
print()
print("  ** THE FIT THAT MAKES THIS MORE THAN A TABLE: the charge cost. **")
print("  T is the horn swap.  PART 1 found u and d differ by exactly one lap of charge.")
print("  In the Standard Model the operator taking u to d is weak isospin, and it costs")
print("  exactly one unit of charge (the W).  ** So 'T changes the integer part by one' and")
print("  'the W carries one unit' are the same sentence if the identification holds. **")
print()
print("  And R doing chirality AND matter/antimatter is not a clash but a requirement: for")
print("  a Weyl field, charge conjugation flips handedness.  ** One operator is CORRECT. **")
print()
print("  ⚠ AND THE COST OF THIS TABLE, WHICH IS REAL AND MUST BE PAID.  If sigma's three")
print("  hinges are COLOUR, then they are not also the three GENERATIONS -- and P14 plus")
print("  COMBINATORICS L8.1-a weld roots = hinges = walls = generations into 'one 3'.")
print("  ** THE WELD MUST EITHER SPLIT OR BE ARGUED TO CARRY BOTH.  That is a first-rank")
print("     structural question and no node has ever put it. **  (Registered L-67.)")
print("  And the corpus has a SECOND three already proved DISTINCT from the hinge three")
print("  (lem:twoturnings, L-07: the bead/turnaround roots).  ** If one three is colour,")
print("  the other is the natural seat of generation -- and L-07 has been sitting in the")
print("  register asking why there are two threes with one cause. **")

# =====================================================================
print()
print("=" * 78)
print("PART 5 — THE WHOLE FERMION SECTOR: AXIAL AGAINST AZIMUTHAL")
print("=" * 78)
print("  The geometry has exactly two kinds of place: ON the hole's axis (no azimuth at")
print("  all) and OFF it at an azimuth (the hinges, at 0/120/240).  One statement:")
print()
print("  ** A CONSTITUENT'S FRACTIONAL CHARGE IS ITS AZIMUTHAL POSITION.  SO: **")
print()
print(f"  {'':>10} {'has an azimuth?':>17} {'fractional charge?':>20} {'colour?':>9} {'is':>10}")
for nm, azi in (('quark', True), ('lepton', False)):
    print(f"  {nm:>10} {str(azi):>17} {str(azi):>20} {str(azi):>9} "
          f"{'at a hinge' if azi else 'on the axis':>12}")
print()
print("  ** THREE FACTS COLLAPSE INTO ONE. **  Leptons have integer charge, leptons carry")
print("  no colour, and leptons do not confine -- and on this reading those are not three")
print("  facts but one: ** the axis has no azimuth, so there is no third to carry, no hinge")
print("  to label, and the lap closes on its own. **  A structure that explains three")
print("  things with one statement is the shape a forced relationship has.")
print()
print("  Checked against the assignments:")
print(f"    e-   Q = -1     -> fractional part {F(-1) % 1}, integer part {F(-1)}   axial, closes alone")
print(f"    nu   Q =  0     -> fractional part {F(0) % 1}, integer part {F(0)}   axial, closes alone")
print(f"    u    Q =  2/3   -> fractional part {u % 1}, ** does not close alone **")
print(f"    d    Q = -1/3   -> fractional part {d % 1}, ** does not close alone **")
print()
print("  ** AND r = 0 IS THE AXIS. **  P3 sec:lap: r = 0 is 'a BRANCH POINT and not a")
print("  barrier, the substrate being smooth across the locus the chart labels r = 0'.")
print("  Daryl: 'at r=0 we have charge conjugation'.  ** So the lepton's home and the seat")
print("  of C are the same locus, and the integer unit of charge and the lap through r = 0")
print("  are candidates for the same object. **")

# =====================================================================
print()
print("=" * 78)
print("PART 6 — THE DEGREE-OF-FREEDOM COUNT, HONESTLY")
print("=" * 78)
print("  What the geometry supplies per generation, and what the Standard Model wants:")
print()
print(f"  {'object':>26} {'geometry':>10} {'SM, one generation':>20} {'lands?':>8}")
checks = [
 ("colours", 3, 3, True),
 ("isospin states (horn)", 2, 2, True),
 ("quark punctures", 6, 6, True),
 ("chirality states (R)", 2, 2, True),
 ("null legs", 12, None, None),
 ("lepton states", None, 2, None),
]
for nm, g, s, ok in checks:
    print(f"  {nm:>26} {str(g) if g is not None else '-':>10} "
          f"{str(s) if s is not None else '-':>20} "
          f"{('YES' if ok else ('-' if ok is None else 'no')):>8}")
print()
print("  ** WHAT LANDS: 3 colours x 2 isospin = 6 = the six punctures, exactly, with the")
print("     chirality carried by R on top of them. **  That is the quark content of one")
print("     generation up to chirality, and it lands with nothing left over.")
print()
# --- r2376+c54.159 -----------------------------------------------------------------
# PART 6's CLAIM, ASSERTED.  The ledger's stated arithmetic: 3 colours x 2 isospin (horn)
# states = 6, and the geometry supplies exactly 6 quark punctures -- so the row lands with
# nothing over; and the leg count is 12 = 6 x 2, the row the receipt leaves UNMATCHED to
# any SM number (its geometry entry is 12 and its SM entry is None, deliberately).
_geo = {nm: g for nm, g, s, ok in checks}
_sm = {nm: s for nm, g, s, ok in checks}
assert _geo['colours'] * _geo['isospin states (horn)'] == _geo['quark punctures'] == 6, \
    "3 colours x 2 horn states must be the 6 quark punctures"
assert _sm['quark punctures'] == 6 and _geo['null legs'] == 12, \
    "the SM's six and the geometry's twelve legs must be as tabulated"
assert _sm['null legs'] is None and _geo['lepton states'] is None, \
    "the leg count and the lepton seat must be left UNMATCHED, not quietly claimed"
# -----------------------------------------------------------------------------------
print("  ** WHAT DOES NOT LAND, STATED AND NOT SMOOTHED: **")
print("   (a) the LEPTONS have no assigned seat yet.  PART 5 argues they are AXIAL, which")
print("       is a place, but the geometry has not been shown to carry TWO axial states")
print("       (e and nu) the way it carries six azimuthal ones.  ** Unworked. **")
print("   (b) the TWELVE legs have no SM counterpart claimed here.  12 = 6 punctures x 2")
print("       rulings; P3 independently carries 'twelve designations'.  ** Whether the")
print("       legs are the quark states doubled by chirality (6 x 2 = 12) is the obvious")
print("       thing to ask and it is NOT ASSERTED. ** (L-63, L-66.)")
print("   (c) GENERATIONS, per PART 4's cost: if the hinges are colour, the generation")
print("       three must come from the corpus's OTHER three.  ** Unworked, and it is the")
print("       biggest single item this file opens. ** (L-67.)")

# =====================================================================
print()
print("=" * 78)
print("PART 7 — WHAT THIS DOES TO THE COLOUR PROBLEM")
print("=" * 78)
print("  The corpus's standing open item (R2, and STATE_matter_sector): su(3) is not an")
print("  isometry of the Lorentzian substrate, su(3) not in so(5,1), the isometry")
print("  exhausted; the conjugate real form S^5 = SO(6)/SO(5) carries a continuous su(3)")
print("  'real by construction but carrying no clock'.  The complaint R2 makes is that")
print("  colour comes out PERMITTED rather than REQUIRED.")
print()
print("  ** WHAT PARTS 2-5 CHANGE ABOUT THAT COMPLAINT. **  They do not find su(3) in the")
print("  isometry -- that wall stands.  What they do is split the question the way the")
print("  corpus ALREADY split the charge question:")
print()
print(f"  {'':>34} {'CHARGE (settled, P3 sec:charge)':>34} {'COLOUR (this file)':>26}")
for a, b, c in (("the discrete structure",
                 "R-parity, mass-odd/charge-even; Q -> -Q fixes every root",
                 "triality Z_3, the singlet rule, confinement as non-closure"),
                ("where it sits",
                 "GEOMETRIC -- in the slicing function",
                 "GEOMETRIC -- candidate, PARTS 2-3"),
                ("the continuous group",
                 "U(1) / full C, ANTILINEAR",
                 "SU(3)"),
                ("where THAT sits",
                 "FIELD-LEVEL, closes from the matter field",
                 "field-level candidate; the S^5 real form")):
    print(f"  {a:>34}")
    print(f"      charge: {b}")
    print(f"      colour: {c}")
print()
print("  ⇒ ** THE PROPOSAL, AND IT IS A REFRAME OF R2 RATHER THAN AN ANSWER TO IT: colour")
print("     may stand in EXACTLY the position charge already stands in -- discrete part")
print("     geometric and forced, continuous part field-level -- in which case R2's")
print("     'permitted not required' is asking the geometry for something the corpus does")
print("     not demand of charge either. **")
print()
print("  ⚠ AND THE PRICE, WHICH R2 IS ENTITLED TO CHARGE.  Charge's discrete part is")
print("  DERIVED in P3 from the eigenspace split of f -- an actual computation.  Colour's")
print("  discrete part is here only a CANDIDATE: the triality arithmetic is exact (PART 2)")
print("  but its identification with the equatorial thirds is not established.")
print("  ** So the parallel is a programme, not a result, and the work it names is exactly")
print("     the work R2 was right to demand. **  (Registered L-68.)")
print()
print("=" * 78)
print("  WHAT THIS FILE ASSERTS: the arithmetic of PARTS 1, 2 and 6, which is exact.")
print("  WHAT IT DOES NOT ASSERT: every identification with a Standard Model object.")
print("  Those are registered term by term, each with a stated refutation, in")
print("  THE_FERMION_SECTOR_GEOMETRY.md -- which is a SPINE document of the live arc and")
print("  not an annex.")
print("=" * 78)
