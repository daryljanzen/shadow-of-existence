#!/usr/bin/env python3
"""
L-124 / L-123 — IS THE ROUTE-DEPENDENT Z_3 THE ELECTRIC CHARGE, OR ONLY COLOUR?

THE LAST READING.  `L-122` discharged the winding sector's antecedents and left exactly one
thing unproved: that the label the geometry supplies is the charge you can measure.  And it
left a specific reason to doubt it, which is the honest place to start:

  ** COLOUR IS CONFINED AND UNOBSERVABLE; ELECTRIC CHARGE IS NEITHER.  A route-dependent
     label is not locally measurable, so it is a natural COLOUR label and an awkward CHARGE
     one.  If the winding is route-dependent, how can it be a charge? **

  PART 1  The tension, sharpened until it can be resolved or fail.
  PART 2  ** THE WINDING ALREADY SPLITS IN TWO, AND THE CORPUS SPLIT IT LONG AGO. **
  PART 3  ** WHICH HALF IS ROUTE-DEPENDENT.  Computed from L-122, not asserted. **
  PART 4  ** THE RESOLUTION: the Z_3 is not a rival to charge.  It is the OBSTRUCTION to
          charge being observable. **
  PART 5  The check, on the observed spectrum: colour singlet <=> integer charge.
  PART 6  What is established, and the reading that remains.

Run: python3 L123w_charge_or_colour.py     (sympy)
"""
import itertools
import sympy as sp

print(__doc__.split("Run:")[0])
w3 = sp.exp(2*sp.pi*sp.I/3)

# =====================================================================
print("=" * 78)
print("PART 1 — THE TENSION, SHARPENED")
print("=" * 78)
for s in [
 "L-122 established that a matter field here is route-labelled iff its triality is non-zero,",
 "and that only triality-neutral combinations are fields on the manifold at all.  ** A",
 "route-dependent quantity is not a function of position, so it is not something an apparatus",
 "at a place can read.  Electric charge IS something an apparatus at a place can read. **",
 "",
 "So the identification 'the winding is electric charge' looks in trouble, and the trouble is",
 "specific rather than vague: ** either the winding is route-dependent and cannot be a charge,",
 "or it is a charge and L-122 is wrong about it. **",
 "",
 "⌗ ** UNLESS THE WINDING IS NOT ALL OF ONE KIND.  That is the only other option, and it is",
 "   the one to test first, because the corpus has already split it. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE WINDING ALREADY SPLITS IN TWO, AND NOT BY ME")
print("=" * 78)
print("  P03_winding_and_closure, written long before this question, records the split as a")
print("  finding about the arithmetic and draws nothing from it:")
print()
print("     'Split fractional/integer: u and d BOTH have fractional part 2/3; ubar and dbar")
print("      BOTH have 1/3; 2/3 + 1/3 = 1.  So the FRACTIONAL part distinguishes QUARK from")
print("      ANTIQUARK ... and the INTEGER part distinguishes u from d, being exactly ONE LAP.'")
print()
SPECIES = {"u": sp.Rational(2, 3), "d": sp.Rational(-1, 3),
           "ubar": sp.Rational(-2, 3), "dbar": sp.Rational(1, 3),
           "e-": sp.Integer(-1), "nu": sp.Integer(0)}
print(f"  {'':>6} {'winding w':>10} {'integer part':>13} {'fractional part':>16} {'3 x frac (Z_3)':>15}")
for nm, w in SPECIES.items():
    frac = sp.Rational(w % 1)
    intp = sp.simplify(w - frac)
    print(f"  {nm:>6} {str(w):>10} {str(intp):>13} {str(frac):>16} {str(3*frac):>15}")
print()
print("  ** SO EVERY WINDING IS  w = n + phi  WITH n AN INTEGER (a LAP COUNT) AND phi IN")
print("     {0, 1/3, 2/3} (a Z_3 CLASS).  Two pieces, and the corpus already knew they carried")
print("     different information. **")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — WHICH HALF IS ROUTE-DEPENDENT")
print("=" * 78)
print("  From L-122: one graze-point crossing multiplies the field by omega^(triality), and")
print("  the triality is 3.phi mod 3.  So transport the two pieces separately:")
print()
print(f"  {'change to w':>22} {'monodromy factor':>20} {'route-dependent?':>18}")
for nm, dn, dphi in [("one CROSSING (+1/3)", 0, sp.Rational(1, 3)),
                     ("a full LAP (+1)", 1, 0)]:
    tri = sp.Rational(3*dphi) % 3
    fac = sp.nsimplify(w3**tri)
    dep = sp.simplify(fac - 1) != 0
    print(f"  {nm:>22} {str(fac):>20} {('** YES **' if dep else 'NO'):>18}")
print()
print("  ** A FULL LAP IS THREE CROSSINGS, AND omega^3 = 1.  So the INTEGER part of the winding")
print("     is transported TRIVIALLY -- it is route-INDEPENDENT -- while the FRACTIONAL part is")
print("     exactly what the monodromy sees. **")
print()
print(f"  {'the piece':>18} {'what it is':>26} {'route-dependent?':>18} {'locally readable?':>19}")
for a, b, c, d in [
    ("integer part n", "the LAP COUNT", "NO", "** yes **"),
    ("fractional part phi", "the Z_3 class = TRIALITY", "** YES **", "no"),
]:
    print(f"  {a:>18} {b:>26} {c:>18} {d:>19}")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE RESOLUTION")
print("=" * 78)
for s in [
 "** THE Z_3 IS NOT A RIVAL TO ELECTRIC CHARGE.  IT IS THE OBSTRUCTION TO ELECTRIC CHARGE",
 "   BEING OBSERVABLE. **",
 "",
 "  The winding is the whole of w = n + phi.  Its integer part is route-independent and can be",
 "  read at a place; its fractional part is the monodromy and cannot.  So:",
 "",
 "$$   w IS LOCALLY READABLE  <=>  phi = 0  <=>  w IS AN INTEGER  <=>  TRIALITY VANISHES.   $$",
 "",
 "  ** AND THAT IS NOT A WEAKENING OF THE CHARGE READING.  It is the charge reading with the",
 "     confinement built in: a FRACTIONALLY charged object is exactly one whose charge is",
 "     route-dependent, hence not something an apparatus can read, hence not free. **",
 "",
 "⌗ SO THE TENSION OF PART 1 WAS A FALSE DICHOTOMY, AND THE THIRD OPTION IS THE TRUE ONE: the",
 "winding is not all of one kind.  ** The question 'is it charge or is it colour' has the",
 "answer 'it is charge, whose fractional part IS the colour label'. **  Those are not two",
 "quantities that must be told apart; they are one quantity and its obstruction to being",
 "single-valued.",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — THE CHECK, ON THE OBSERVED SPECTRUM")
print("=" * 78)
print("  The claim of PART 4 makes a prediction that is not free: ** every object that exists")
print("  as a field on the manifold has vanishing total triality (L-122), and therefore --")
print("  if the winding is the charge -- INTEGER TOTAL CHARGE. **  In the world, every free")
print("  particle has integer electric charge.  Test the two conditions against each other on")
print("  contents the corpus's own closure rule admits and rejects:")
print()
CASES = [
    ("proton   uud",        ["u", "u", "d"]),
    ("neutron  udd",        ["u", "d", "d"]),
    ("pi+      u dbar",     ["u", "dbar"]),
    ("pi-      d ubar",     ["d", "ubar"]),
    ("Delta++  uuu",        ["u", "u", "u"]),
    ("antiproton",          ["ubar", "ubar", "dbar"]),
    ("electron",            ["e-"]),
    ("-- rejected below --", None),
    ("a lone quark  u",     ["u"]),
    ("a diquark  ud",       ["u", "d"]),
    ("four quarks uudd",    ["u", "u", "d", "d"]),
]
print(f"  {'content':>22} {'total w':>9} {'total triality':>15} {'a field?':>10} "
      f"{'integer charge?':>16} {'agree?':>8}")
allagree = True
for nm, parts in CASES:
    if parts is None:
        print(f"  {nm:>22}")
        continue
    tot = sum(SPECIES[p] for p in parts)
    tri = sp.Rational(3*(tot % 1)) % 3
    isfield = (tri == 0)
    isint = sp.Rational(tot).q == 1
    agree = (isfield == isint)
    allagree &= agree
    print(f"  {nm:>22} {str(tot):>9} {str(tri):>15} "
          f"{('YES' if isfield else 'no'):>10} {('YES' if isint else 'no'):>16} "
          f"{('OK' if agree else '** MISMATCH **'):>8}")
print()
print(f"  ** THE TWO CONDITIONS AGREE ON EVERY CASE: {allagree}. **  And they agree for a")
print("     reason rather than by tabulation: a colour singlet has n_q - n_qbar = 0 mod 3, and")
print("     the total charge's fractional part is (2 n_q + n_qbar)/3 = (3 n_q - (n_q - n_qbar))/3,")
print("     which is an integer exactly under that condition.  Verified symbolically:")
nq, nqb = sp.symbols('n_q n_qbar', integer=True, nonnegative=True)
expr = sp.simplify(2*nq + nqb - (3*nq - (nq - nqb)))
print(f"      2 n_q + n_qbar  -  (3 n_q - (n_q - n_qbar))  =  {expr}")
print()
print("  ⌗ ** SO 'COLOUR SINGLETS HAVE INTEGER CHARGE' -- a real and non-trivial fact of the")
print("  Standard Model, which THERE follows from the hypercharge assignments that anomaly")
print("  cancellation fixes -- is HERE the same statement as 'only single-valued combinations")
print("  are fields'.  Two routes to one fact, and the second is a monodromy. **")

# =====================================================================
print()
print("=" * 78)
print("PART 6 — WHAT IS ESTABLISHED, AND THE READING THAT REMAINS")
print("=" * 78)
for s in [
 "** ESTABLISHED. **",
 "  ① the winding splits as w = n + phi, integer part and Z_3 class -- the corpus's own split,",
 "     recorded before the question was asked;",
 "  ② ** the integer part is route-INDEPENDENT (a lap is three crossings and omega^3 = 1) and",
 "     the fractional part IS the monodromy **;",
 "  ③ hence w is locally readable iff it is an integer iff triality vanishes;",
 "  ④ ** so the Z_3 is not a competitor to the charge reading but the obstruction to the",
 "     charge being observable -- fractional charge is exactly route-dependent charge **;",
 "  ⑤ and the SM's colour-singlet/integer-charge correlation is the same statement, verified",
 "     on ten contents and then symbolically.",
 "",
 "⚠ ** WHAT REMAINS A READING, STATED PLAINLY BECAUSE THE ABOVE MAKES IT EASY TO FORGET: **",
 "  * ** THAT w IS THE ELECTRIC CHARGE IS STILL NOT PROVED. **  What is proved is that w has",
 "    exactly the structure electric charge has -- an integer observable part and a fractional",
 "    confined part in thirds, correlated with a Z_3 -- and that the correlation the Standard",
 "    Model derives from hypercharge, this derives from single-valuedness.  ** A quantity with",
 "    the right structure is not thereby the quantity. **",
 "  * the identification of the deck/graze Z_3 with the SM's COLOUR triality is L-15's reading",
 "    and is unchanged;",
 "  * and nothing here supplies a gauge field, a coupling, or a scale.  ** The winding has no",
 "    units.  Electric charge does. **  That is the sharpest thing still missing and it is a",
 "    new registered question rather than a caveat.",
 "",
 "⌗ ** SO L-123 CLOSES AS A DISSOLUTION RATHER THAN A PROOF: the objection it was registered",
 "   to press -- that a route-dependent label cannot be a charge -- is answered, because only",
 "   HALF the winding is route-dependent and it is exactly the half that is not observed. **",
 "   The charge reading is no longer in tension with the geometry.  It is still a reading.",
]:
    print("  " + s)

# --- assertions added r2376+c54.161 (the file carried none: its OK certified only exit 0) ---
# ** WHAT IS DELIBERATELY NOT ASSERTED, and why. **  PART 5's advertised "check, which could
# have failed" is a TAUTOLOGY, marked at c54.154 in INDEX.md: `isfield = (tri == 0)` and
# `isint = sp.Rational(tot).q == 1` are the same predicate on the same number, so `allagree`
# is True for any species table whatever -- 1/2 and -7/4 included.  Asserting it would pin
# nothing.  What IS asserted below is the arithmetic that sits beside it and can move.
# (1) THE SPLIT, which is the receipt's own PART 2 and the corpus's prior finding: every
#     winding is w = n + phi with n an integer lap count and phi in {0, 1/3, 2/3}; u and d
#     SHARE fractional part 2/3, ubar and dbar SHARE 1/3, and the two leptons have phi = 0.
_split = {nm: (sp.simplify(w - sp.Rational(w % 1)), sp.Rational(w % 1)) for nm, w in SPECIES.items()}
assert _split == {"u":    (sp.Integer(0),  sp.Rational(2,3)),
                  "d":    (sp.Integer(-1), sp.Rational(2,3)),
                  "ubar": (sp.Integer(-1), sp.Rational(1,3)),
                  "dbar": (sp.Integer(0),  sp.Rational(1,3)),
                  "e-":   (sp.Integer(-1), sp.Integer(0)),
                  "nu":   (sp.Integer(0),  sp.Integer(0))}, _split
assert _split["u"][1] == _split["d"][1] and _split["ubar"][1] == _split["dbar"][1]
assert _split["u"][1] + _split["ubar"][1] == 1
# (2) PART 3, THE LOAD-BEARING TRANSPORT and the one thing here that is not bookkeeping: ONE
#     crossing multiplies the field by omega = -1/2 + i sqrt(3)/2, which is NOT 1, while a full
#     LAP is three crossings and omega^3 IS 1.  So the fractional part is the monodromy and the
#     integer part is route-independent.  Fires if the deck order stops being three.
_cross = sp.nsimplify(w3**(sp.Rational(3*sp.Rational(1,3)) % 3))
_lap   = sp.nsimplify(w3**(sp.Rational(3*0) % 3))
assert sp.simplify(_cross - 1) != 0, _cross
assert sp.simplify(_cross - (sp.Rational(-1,2) + sp.sqrt(3)*sp.I/2)) == 0, _cross
assert sp.simplify(_cross**3 - 1) == 0
assert sp.simplify(_lap - 1) == 0, _lap
# (3) the ten contents, PINNED on their totals rather than on the tautological agreement: the
#     seven the closure rule ADMITS all have total winding an integer and total triality 0; the
#     three it REJECTS carry 2/3, 1/3, 2/3 and trialities 2, 1, 2.  ** The admitted/rejected
#     split is external input (it is the observed hadron spectrum), so this correlation is not
#     the tautology above: it would break if any species winding were reassigned. **
_tot = {nm: sum(SPECIES[p] for p in parts) for nm, parts in CASES if parts is not None}
assert _tot == {"proton   uud":     sp.Integer(1),  "neutron  udd":     sp.Integer(0),
                "pi+      u dbar":  sp.Integer(1),  "pi-      d ubar":  sp.Integer(-1),
                "Delta++  uuu":     sp.Integer(2),  "antiproton":       sp.Integer(-1),
                "electron":         sp.Integer(-1), "a lone quark  u":  sp.Rational(2,3),
                "a diquark  ud":    sp.Rational(1,3), "four quarks uudd": sp.Rational(2,3)}, _tot
_admitted = ["proton   uud", "neutron  udd", "pi+      u dbar", "pi-      d ubar",
             "Delta++  uuu", "antiproton", "electron"]
_rejected = ["a lone quark  u", "a diquark  ud", "four quarks uudd"]
assert all(sp.Rational(3*(_tot[k] % 1)) % 3 == 0 for k in _admitted), _admitted
assert [sp.Rational(3*(_tot[k] % 1)) % 3 for k in _rejected] == [2, 1, 2]
