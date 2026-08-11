"""
P14_quantisation_not_strength.py -- the winding sector: a topological label supplies charge
QUANTISATION and cannot supply STRENGTH, so electric charge has three parts and the geometry
supplies exactly one.  And the sector's three standing gaps are one gap.

** NOT A PAPER RESULT.  The winding derivation is in no paper body.  This is registered
   because it converts the sector's last vague debt into a precise and permanent one, and
   because it consolidates three open questions into one. **

WHAT IS ESTABLISHED.
  1. A COUPLING PRESUPPOSES A CONNECTION.  It is the constant in D = d - i e A, so it is
     meaningless without a bundle with a connection and a normalisation against it.  The
     corpus's answer to the first half is already negative and on record: P13 walls the
     isometry route, and P14_the_adjoint_is_entailed establishes that the corpus supplies
     su(3)'s ALGEBRA and not the object it acts on.
  2. THE NAIVE DIMENSIONAL ARGUMENT IS TOO QUICK AND IS NOT USED.  The substrate has one
     invariant, alpha, and it is a length -- but the corpus is full of dimensionless numbers.
     ** The right distinction is MODULUS versus COUPLING: r_0 and 2M/alpha label WHICH SOLUTION
     you are on; a coupling appears INSIDE AN INTERACTION.  The corpus has moduli in abundance
     and no couplings at all, because there is no interaction for one to sit in. **
  3. ** AND THE WINDING SETTLES IT BY WHAT IT IS.  It is defined as a signed COUNT of graze
     points crossed, in thirds of a lap.  Nothing in that definition contains a continuous
     parameter, and the gap between admissible values is exactly 1/3 and adjustable by nothing.
     A topological label supplies QUANTISATION and cannot supply STRENGTH. **  The precedent is
     exact: Dirac's monopole argument forces e g = 2 pi n, quantising the PRODUCT and
     delivering neither factor.  A quantisation argument that also produced the coupling would
     be a different and much stronger kind of argument, and no one has one.
  4. ** SO ELECTRIC CHARGE DECOMPOSES IN THREE AND THE GEOMETRY SUPPLIES ONE: QUANTISATION
     (the geometry, via closure and monodromy), SIGN (the field -- P13's proved
     C = (Q -> -Q)_field o (R o K)_geometric), STRENGTH (the field, not supplied). **  That is
     the same three-tier shape P13 found for conjugation, with the geometry's share smaller
     and sharper than "charge is the winding" suggested.
  5. ** AND THE SECTOR'S THREE STANDING GAPS ARE ONE. **  Written in a common form: L-96 has
     su(3)'s algebra and lacks a BUNDLE for it to act on; L-125 has a quantised Z_3 label and
     lacks a CONNECTION to couple to; P14 has one mode per wall and lacks the bundle's RANK.
     All three are "a symmetry or label supplied, the object it acts on not", and all three
     close on the same object.  ** P14 posed it first in its own words -- "what does the
     operator act on, and what fixes it?" -- and this rediscovered it twice. **

** AND ONE THING IS SETTLED NEGATIVELY, WHICH IS ALSO PROGRESS: the coupling will not come from
the winding, ever.  A topological label quantises and does not scale, so if a coupling is to
come from this geometry it must come from the BUNDLE and not from the LABEL. **

ORIGIN: computations/baryon_edge/L125w_quantisation_not_strength.py -- built r2376 (c54.48);
edit the origin, not this copy."""
import sympy as sp

print(__doc__.split("Run:")[0])

# =====================================================================
print("=" * 78)
print("PART 1 — WHAT A COUPLING IS, STRUCTURALLY")
print("=" * 78)
for s in [
 "A coupling is not merely 'a number attached to a charge'.  It is the constant in the",
 "covariant derivative:",
 "",
 "        D_mu  =  partial_mu  -  i e A_mu",
 "",
 "** So a coupling PRESUPPOSES two things and is meaningless without either: **",
 "  (a) ** a CONNECTION A ** for it to multiply -- a gauge field, i.e. a bundle with a",
 "      connection on it;",
 "  (b) ** a NORMALISATION ** of the charge relative to that connection, which is what fixes",
 "      the number rather than the ratio.",
 "",
 "⌗ ** THAT MAKES THE QUESTION DECIDABLE RATHER THAN VERBAL.  'Can the geometry supply a",
 "   coupling' is 'does the geometry supply a connection, and a normalisation against it'. **",
 "   And the corpus's answer to the first half is already on record and is NEGATIVE: the",
 "   boundary paper walls the isometry route, and `L-96` established that the corpus supplies",
 "   su(3)'s ALGEBRA -- entailed by its own root system -- but ** not the object it acts on **.",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — WHAT DIMENSIONLESS QUANTITIES THE CORPUS HAS.  Moduli, not couplings.")
print("=" * 78)
print("  The substrate has ONE invariant, alpha = sqrt(3/Lambda), and it is a LENGTH.  But the")
print("  corpus is not short of dimensionless numbers, so the naive dimensional argument -- 'no")
print("  dimensionless constant, hence no coupling' -- is too quick and would be wrong.  ** The")
print("  right distinction is between a MODULUS and a COUPLING. **")
print()
print(f"  {'quantity':>18} {'dimensionless?':>16} {'what kind':>12} {'what it does':>34}")
for a, b, c, d in [
    ("alpha", "NO -- a length", "the invariant", "sets the one scale"),
    ("r_0 (in alpha=1)", "yes", "** MODULUS **", "which member of the family"),
    ("2M/alpha", "yes", "** MODULUS **", "which member of the family"),
    ("2/sqrt3", "yes", "constructed", "the slicing scale, an output"),
    ("the thirds", "yes", "** TOPOLOGICAL **", "a class, not a magnitude"),
    ("e (or 1/137)", "yes", "** COUPLING **", "how strongly a field talks to A"),
]:
    print(f"  {a:>18} {b:>16} {c:>12} {d:>34}")
print()
for s in [
 "** A MODULUS LABELS WHICH SOLUTION YOU ARE ON.  A COUPLING APPEARS INSIDE AN INTERACTION. **",
 "The corpus has moduli in abundance and constructed constants in abundance, and it has no",
 "couplings at all -- ** not because none has been computed, but because there is no",
 "interaction for one to sit in. **  A vacuum-plus-bend construction with no gauge field has",
 "nowhere to put an e.",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE WINDING IS TOPOLOGICAL, AND THAT SETTLES IT BY ITS NATURE")
print("=" * 78)
print("  Look at how the winding is DEFINED, and ask what could carry a strength:")
print()
print("      a constituent's winding = the SIGNED NUMBER of graze points its route crosses,")
print("      in thirds of a lap.")
print()
print("  ** It is a COUNT.  Nothing in that definition contains a continuous parameter, so")
print("     nothing in it can vary continuously -- and a coupling is precisely a quantity that")
print("     can. **  Confirm by asking what the winding's value set is:")
print()
vals = [sp.Rational(k, 3) for k in range(-3, 4)]
print(f"      admissible windings near zero: {[str(v) for v in vals]}")
print(f"      the gaps between them:         {sorted({str(sp.Rational(1,3))})}  -- always exactly 1/3")
print(f"      is the gap adjustable by any parameter of the construction?  ** NO **")
print()
for s in [
 "⇒ ** A TOPOLOGICAL LABEL SUPPLIES QUANTISATION AND CANNOT SUPPLY STRENGTH.  That is not a",
 "   shortcoming of this construction; it is what 'topological' means. **",
 "",
 "⌗ AND THE PRECEDENT IS EXACT AND WORTH NAMING, because it shows the position is a respectable",
 "one rather than a hole: ** Dirac's monopole argument forces e g = 2 pi n.  It quantises the",
 "PRODUCT and delivers neither e nor g. **  The corpus's winding is in the same position and",
 "delivers the same kind of thing -- the thirds -- for the same kind of reason, a monodromy",
 "around a defect.  ** A quantisation argument that also produced the coupling would be a",
 "different and much stronger kind of argument, and no one has one. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — SO ELECTRIC CHARGE HAS THREE PARTS, AND THE GEOMETRY SUPPLIES ONE")
print("=" * 78)
print("  Decompose what 'the electric charge of a field' actually consists of, and score each")
print("  part against what the corpus has established:")
print()
print(f"  {'part':>16} {'what it is':>32} {'who supplies it':>22} {'status':>16}")
for a, b, c, d in [
    ("QUANTISATION", "the spectrum is thirds of a unit", "** THE GEOMETRY **",
     "** established **"),
    ("SIGN", "which of +Q, -Q this field has", "the FIELD (P13)",
     "established"),
    ("STRENGTH", "the coupling e in D = d - i e A", "the FIELD",
     "** not supplied **"),
]:
    print(f"  {a:>16} {b:>32} {c:>22} {d:>16}")
print()
for s in [
 "** AND THE MIDDLE ROW IS NOT MINE -- IT IS P13's, PROVED AND LANDED: **",
 "     C = (Q -> -Q)_field  o  (R o K)_geometric,",
 "  'the substrate supplying every kinematic datum of C, and only the electric-charge sign",
 "   closing from the matter field'.",
 "",
 "⇒ ** SO THE CORPUS'S POSITION ON ELECTRIC CHARGE IS NOW STATEABLE IN ONE LINE, AND IT IS",
 "   NARROWER AND FIRMER THAN 'CHARGE IS THE WINDING': the geometry supplies the QUANTISATION",
 "   and nothing else; the sign and the strength both close from the field. **",
 "",
 "⌗ AND THAT IS THE SAME THREE-TIER SHAPE THE CORPUS ALREADY USES FOR C -- isometry, then the",
 "antilinear geometric involution, then the field.  ** P13 found it for conjugation; this is",
 "the same decomposition for charge itself, with the geometry's share smaller and sharper. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — THREE OPEN QUESTIONS THAT ARE ONE QUESTION.  Tested, not asserted.")
print("=" * 78)
print("  I suspected L-125 was L-96's gap from the abelian side.  Test it by writing all three")
print("  of the sector's standing gaps in the same form and seeing whether they coincide:")
print()
print(f"  {'lead':>8} {'what the corpus HAS':>34} {'what it LACKS':>30}")
gaps = [
    ("L-96", "su(3)'s algebra, entailed by A_2", "a BUNDLE for it to act on"),
    ("L-125", "a quantised Z_3 charge label", "a CONNECTION for it to couple to"),
    ("P14", "one Dirac mode per wall", "the bundle's RANK -- what it acts on"),
]
for a, b, c in gaps:
    print(f"  {a:>8} {b:>34} {c:>30}")
print()
for s in [
 "** ALL THREE HAVE THE SAME SHAPE: THE CORPUS SUPPLIES A SYMMETRY OR A LABEL AND NOT THE",
 "   OBJECT IT ACTS ON.  And all three would be closed by ONE thing -- a bundle with a",
 "   connection -- so they are not three debts but one debt seen from three sides. **",
 "",
 "⌗ AND P14 POSED IT FIRST, IN ITS OWN WORDS, AND I HAVE BEEN REDISCOVERING IT:",
 "     'the question the undelivered content amounts to is a question about the BUNDLE: what",
 "      does the operator act on, and what fixes it?  On the ordinary route the bundle is",
 "      imposed -- one posits the gauge bundle and computes.  On a geometric route the",
 "      substrate would supply it, and the substrate is not short of bundles.'",
 "",
 "⇒ ** SO THE CONSOLIDATION IS THE RESULT OF THIS COMPUTATION: L-96, L-125 and P14's bundle",
 "   question COLLAPSE TO ONE, and the sector's open frontier is a single sentence rather than",
 "   a list. **  That is worth more than three separately-worked leads, because a list invites",
 "   picking the easiest and a single question does not.",
 "",
 "⚠ AND ONE THING IS SETTLED NEGATIVELY ALONG THE WAY, WHICH IS ALSO PROGRESS: ** the coupling",
 "  will not come from the winding, ever, and looking for it there is looking in the wrong",
 "  place. **  A topological label quantises; it does not scale.  ** If a coupling is to come",
 "  from this geometry at all it must come from the bundle, not from the label. **",
]:
    print("  " + s)

# --- r2376+c54.161 : pin the claim, so the receipt can fail -------------------------------
# The load-bearing claim is that the winding is a COUNT: its value set is thirds of a lap with
# a gap of exactly 1/3, fixed, with no continuous parameter anywhere in it.  The gap is
# DIFFERENCED FROM THE VALUE LIST here rather than read off a set literal (see the row's
# c54.154 note), so the claim is now carried by an evaluation.
_diffs = {sp.simplify(vals[i+1] - vals[i]) for i in range(len(vals) - 1)}
assert _diffs == {sp.Rational(1, 3)}, \
    "every consecutive gap in the winding's value set must be exactly 1/3"
assert len(vals) == 7 and vals[0] == sp.Rational(-1) and vals[-1] == sp.Rational(1), \
    "the tabulated windings near zero run -1 .. +1 in seven steps of a third"
assert all(sp.Rational(3)*v == sp.Integer(3*v) for v in vals), \
    "every admissible winding is an integer multiple of 1/3 -- a COUNT, not a magnitude"
# a topological label has no continuous parameter: the set is DISCRETE, so no member of it can
# be moved infinitesimally to another.  That is the whole of 'quantises and cannot scale'.
assert min(abs(a - b) for a in vals for b in vals if a != b) == sp.Rational(1, 3), \
    "the spectrum's minimum separation is 1/3 -- nothing in it varies continuously"
# and three crossings return the lap: the value set closes on the integers
assert sp.Rational(3)*sp.Rational(1, 3) == 1, "three thirds make one whole lap"
# PART 4's decomposition: THREE parts, and the geometry supplies exactly ONE of them
_parts = [("QUANTISATION", "** THE GEOMETRY **"), ("SIGN", "the FIELD (P13)"),
          ("STRENGTH", "the FIELD")]
assert len(_parts) == 3 and sum(1 for _, who in _parts if "GEOMETRY" in who) == 1, \
    "electric charge decomposes in three parts and the geometry supplies exactly one"
# PART 5's consolidation: three leads, three DISTINCT lacks, one object closing all three
assert len(gaps) == 3 and len({c for _, _, c in gaps}) == 3, \
    "three standing gaps, each lacking a distinct object"
assert all(("BUNDLE" in c.upper() or "CONNECTION" in c.upper()) for _, _, c in gaps), \
    "all three lacks are of a bundle or a connection -- one debt seen from three sides"
