#!/usr/bin/env python3
"""
L-15 — THE QUARK/LEPTON FRONTIER.  Not a table of what is known: a push on what is not.

Daryl: "The corpus doesn't have anything on leptons and quarks yet because we've not found a
way yet to land that ... incompleteness and underdevelopment are only there because we have
not managed to do them yet and that is what I need your help with."

The word `lepton` appears once in the corpus and that once is in a bibliography title.  What
follows is an attempt to land it, with the conflicts named where they arise rather than
smoothed.

  PART 1  WHERE DO BOUND MODES ACTUALLY LIVE?  ** The answer kills my own earlier reading. **
  PART 2  So what distinguishes a quark from a lepton here?
  PART 3  ** THE CONSEQUENCE: they are partial waves of ONE field. **
  PART 4  And that explains something P14 observed and could not explain.
  PART 5  The counting, stated with its conflict rather than around it.
  PART 6  What would falsify the whole reading.

Run: python3 L15_the_quark_lepton_frontier.py     (sympy)
"""
import itertools
from collections import defaultdict
import sympy as sp

print(__doc__.split("Run:")[0])

# =====================================================================
print("=" * 78)
print("PART 1 — WHERE DO BOUND MODES ACTUALLY LIVE?")
print("=" * 78)
print("  Two candidate readings have been in play, and they cannot both be right:")
print()
print("   (A) 'quarks are the T-ORBIT (the six punctures) and leptons the T-FIXED locus (the")
print("       three walls)' -- L-80's consequence, recorded at c54.28")
print("   (B) 'every bound mode is a WALL mode' -- P14 prop:wall, which binds one chiral")
print("       zero-mode per wall and nowhere else")
print()
print("  ** (B) IS THE CORPUS'S AND (A) IS MINE.  P14's superpotential W = lambda sqrt(f)/r")
print("     changes sign at r = 0 and nowhere else, so the ONLY place a mode binds is a wall.")
print("     The punctures are where the HINGES meet the substrate; no field binds there. **")
print()
print("  ⇒ ** SO (A) IS WRONG AS A STATEMENT ABOUT FIELDS, AND I RETRACT IT. **  What L-80")
print("     established is true of SEATS -- the punctures are the T-orbit and the walls the")
print("     T-fixed locus -- and I read a geometric fact about seats as a fact about states.")
print("  ⇒ ** AND THE T-FIXED LOCUS IS BIGGER THAN THE WALLS ANYWAY: T fixes the whole")
print("     equatorial plane X0 = 0, hence the entire throat circle.  The three walls are")
print("     three MARKED POINTS on a fixed CIRCLE, not the fixed set. **")
print()
print("  ⌗ SO THE FRONTIER QUESTION IS NOT 'WHERE DOES A LEPTON SIT'.  Every mode sits at a")
print("  wall.  ** The question is what distinguishes them THERE. **")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — WHAT DISTINGUISHES A QUARK FROM A LEPTON AT A WALL")
print("=" * 78)
print("  The corpus supplies exactly two gradings on a wall-bound mode, both computed from")
print("  one number (receipt P14_mode_monodromy_at_the_wall, P14_lambda_spectrum):")
print()
print("     triality  = -lambda mod 3      [Z_3 -- and Z_3 IS the centre of SU(3)]")
print("     chirality = sign(lambda)       [Z_2 -- which branch normalizes at the wall]")
print()
print("  ** AND TRIALITY IS EXACTLY THE STANDARD MODEL'S OWN QUARK/LEPTON DISCRIMINANT. **")
print("  In the Standard Model a field is coloured iff it carries non-trivial triality, i.e.")
print("  iff it transforms non-trivially under Z(SU(3)).  Leptons are the triality-zero")
print("  fields.  So:")
print()
w = sp.exp(2*sp.pi*sp.I/3)
print(f"  {'lambda mod 3':>14} {'triality':>10} {'centre charge':>16} {'the corpus says':>22} {'the SM says':>16}")
for m in (1, 2, 0):
    tri = (-m) % 3
    print(f"  {m:>14} {tri:>10} {str(sp.nsimplify(w**tri)):>16} "
          f"{('coloured' if tri else 'colourless'):>22} "
          f"{('quark' if tri else 'lepton'):>16}")
print()
print("  ⇒ ** THE PROPOSAL, AND IT IS THE WHOLE OF L-15's LANDING ATTEMPT:")
print("       A LEPTON IS A WALL-BOUND MODE WHOSE ANGULAR EIGENVALUE IS DIVISIBLE BY THREE.")
print("       A QUARK IS ONE WHOSE IS NOT. **")
print()
print("  This is not a placement and not an extra structure.  ** It says the quark/lepton")
print("  distinction is a property of the PARTIAL WAVE, and the corpus computed that")
print("  property before anyone asked it to mean anything. **")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE CONSEQUENCE: THEY ARE PARTIAL WAVES OF ONE FIELD")
print("=" * 78)
print("  P14 puts ONE Dirac spinor on the slicing structure.  Its radial problem separates")
print("  by angular eigenvalue, and every lambda gives a bound wall mode.  If triality")
print("  distinguishes quark from lepton, then:")
print()
print("  ** QUARKS AND LEPTONS ARE NOT TWO FIELDS.  THEY ARE THE SAME FIELD IN DIFFERENT")
print("     PARTIAL WAVES, SORTED BY lambda mod 3. **")
print()
print(f"  {'|lambda|':>9} {'lambda':>8} {'triality':>10} {'chirality':>11} {'reads as':>12} {'mult 2|lambda|':>15}")
tally = defaultdict(int)
for n in range(1, 8):
    for lv in (n, -n):
        tri = (-lv) % 3
        tally['lepton' if tri == 0 else 'quark'] += 2*abs(lv)
        if n <= 4:
            print(f"  {n:>9} {lv:>8} {tri:>10} {('+' if lv < 0 else '-'):>11} "
                  f"{('LEPTON' if tri == 0 else 'quark'):>12} {2*abs(lv):>15}")
print("      ...")
print()
print("  ** THE PATTERN IS EXACT AND PERIODIC: two coloured partial waves, then one")
print("     colourless one, forever.  Two-to-one, quark to lepton, BY PARTIAL WAVE. **")
print()
print("  ⌗ AND THAT RATIO IS THE STANDARD MODEL'S OWN, at the level of MULTIPLETS:")
print("     one generation has TWO quark multiplets by isospin (u-type, d-type) carrying")
print("     colour, and ONE lepton doublet not carrying it.  ** Two coloured, one not. **")
print("  ⚠ Stated as a resonance, not an identification: the corpus's two-to-one is over")
print("  PARTIAL WAVES and the Standard Model's is over MULTIPLETS, and nothing here shows")
print("  those are the same counting.  ** But they are the same ratio and it is not put in. **")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — AND IT EXPLAINS SOMETHING P14 OBSERVED AND COULD NOT EXPLAIN")
print("=" * 78)
print("  P14, on anomaly cancellation, in its own words:")
print()
print("     'the wall structure requires each generation's content to be anomaly-free on its")
print("      own -- there being no bulk gauge field for inflow to come from -- and the")
print("      observed content meets that condition on every count AND ONLY AS A COMPLETE SET'")
print()
print("  ** P14 records the 'only as a complete set' as a fact about the Standard Model.  It")
print("     has no account of WHY the set should be complete. **")
print()
print("  ⇒ ** ON THIS READING IT IS FORCED: if quarks and leptons are partial waves of ONE")
print("     field, they are not a set that could have been assembled differently.  You")
print("     cannot take the coloured waves without the colourless ones -- they are the same")
print("     field's tower, sorted by lambda mod 3.  ** Anomaly-freedom 'only as a complete")
print("     set' is then not a coincidence of the spectrum but a statement that the spectrum")
print("     is ONE OBJECT. **")
print()
print("  ⌗ THIS IS THE STRONGEST THING L-15 PRODUCES, and it is an EXPLANATION of an")
print("  existing observation rather than a new claim: P14 already noticed the fact and")
print("  called it striking.  ** The reading supplies the reason. **")

# =====================================================================
print()
print("=" * 78)
print("PART 5 — THE COUNTING, WITH ITS CONFLICT NAMED")
print("=" * 78)
print("  Two countings are on the table and they do NOT agree, and pretending otherwise is")
print("  what F-11 did:")
print()
print(f"  {'':>22} {'counts':>12} {'what it counts':>44}")
for a, b, c in (("SEATS (the geometry)", "12 + 3",
                 "12 null legs (3 colour x 2 horn x 2 chirality) + 3 walls"),
                ("MODES (the field)", "infinite",
                 "one per lambda, multiplicity 2|lambda|, graded 2:1 quark:lepton")):
    print(f"  {a:>22} {b:>12} {c:>44}")
print()
print("  ** THE SEAT COUNT MATCHES THE STANDARD MODEL'S 15 AND THE MODE COUNT DOES NOT")
print("     TERMINATE.  Both are computed; neither is wrong; they answer different questions.")
print("     ** And L-15 cannot be landed until one of three things is true: **")
print("       (a) something truncates the tower to its lowest rungs;")
print("       (b) the tower IS the content and the SM's 15 is its lowest level (L-88);")
print("       (c) the seats carry the states and the tower is a redundancy of the")
print("           description -- which would need the modes at one seat to be identified.")
print()
print("  ⌗ AND (c) IS NEW HERE AND IS THE ONE I WOULD BET ON, for a reason: the geometry has")
print("  ** exactly 3 walls and exactly 12 legs, and both numbers are forced **, while the")
print("  tower's degeneracy 2|lambda| is the round sphere's and is not forced by anything in")
print("  CR.  ** If the transverse space is not the round S^2 at the wall -- and L-90 records")
print("  that the round choice is a CHOICE -- the degeneracy changes and the tower may")
print("  truncate. **  That is a computation, and it is the next one.  (L-107.)")

# =====================================================================
print()
print("=" * 78)
print("PART 6 — WHAT WOULD FALSIFY THIS")
print("=" * 78)
for s in [
 "① ** If triality did NOT track lambda mod 3 ** -- but it does, computed on prop:wall's own",
 "   solution (P14_mode_monodromy_at_the_wall), so this is settled.",
 "② ** If a wall-bound mode with lambda = 0 mod 3 carried a colour label anyway ** -- it",
 "   cannot: triality zero IS trivial centre charge, and colour without centre charge is",
 "   not colour.",
 "③ ** If the SM's quark/lepton split were NOT a triality split ** -- it is, definitionally.",
 "④ ** THE REAL FALSIFIER: if the lambda-tower's quark:lepton ratio came out other than",
 "   2:1. ** It is 2:1 because 3 is prime and two residues are non-zero.  So the reading",
 "   predicts a 2:1 ratio of coloured to colourless PARTIAL WAVES, and if the multiplet",
 "   counting is ever tied to the partial-wave counting, ** a departure from 2:1 kills it. **",
 "⑤ ** And if (c) fails -- if the modes at one seat cannot be identified -- then the seat",
 "   count is decorative and F-11's 12+3 is a coincidence of small integers. **  That is the",
 "   honest risk and L-107 is where it is decided.",
]:
    print("  " + s)
print()
print("  ** WHAT L-15 LANDS: the quark/lepton distinction, as triality, as a property of the")
print("     partial wave, with an explanation of P14's 'only as a complete set'. **")
print("  ** WHAT IT DOES NOT LAND: the count.  That waits on L-107. **")

# --- r2376+c54.161 : pin the claim, so the receipt can fail -------------------------------
# WHAT IS PINNED is the grading, which is what this receipt actually computes: triality
# = -lambda mod 3, the SM's own quark/lepton discriminant, and the resulting UNWEIGHTED
# partial-wave pattern -- two coloured then one colourless, forever.  ** The printed
# 'two-to-one' is that UNWEIGHTED count; the tally the file builds carries the 2|lambda|
# multiplicity and is never printed, so its totals are pinned separately below rather than
# read as the ratio (see the row's c54.154 note). **
# 1. the grading table of PART 2, lambda mod 3 = 1, 2, 0
assert [(-m) % 3 for m in (1, 2, 0)] == [2, 1, 0], "the printed triality column is 2, 1, 0"
assert sp.simplify(w**3 - 1) == 0 and sp.simplify(w - 1) != 0, \
    "the centre charge omega has order exactly 3 -- Z_3 IS the centre of SU(3)"
assert sp.simplify(w**((-0) % 3) - 1) == 0, "lambda = 0 mod 3 carries TRIVIAL centre charge (colourless)"
assert all(sp.simplify(w**((-m) % 3) - 1) != 0 for m in (1, 2)), \
    "lambda != 0 mod 3 carries NON-trivial centre charge (coloured)"
# 2. the periodic pattern, counted BY PARTIAL WAVE (unweighted): 2 coloured : 1 colourless
_period = [(-lv) % 3 for lv in range(1, 4)]
assert sum(1 for t in _period if t != 0) == 2 and sum(1 for t in _period if t == 0) == 1, \
    "over one period of three partial waves, two are coloured and one is not -- the printed 2:1"
assert len([t for t in range(3) if t != 0]) == 2, \
    "the ratio is 2:1 because 3 is PRIME and exactly two residues are non-zero (PART 6 item 4)"
# and it is exactly periodic, so the pattern holds forever and not just at the bottom
assert [(-lv) % 3 for lv in range(1, 13)] == [(-lv) % 3 for lv in range(4, 16)], \
    "the coloured-coloured-colourless pattern is periodic with period 3"
# 3. the MULTIPLICITY-WEIGHTED tally the file builds and does not print.  These are the values
#    it holds after the n = 1..7 loop; they are NOT 2:1, and over the full periods n = 1..6
#    the same weighting gives 48:36 = 4:3.
assert tally['quark'] == 76 and tally['lepton'] == 36, \
    "the unprinted 2|lambda|-weighted tally over n = 1..7 is quark 76, lepton 36"
assert abs(tally['quark']/tally['lepton'] - 2) > 0.1, \
    "the weighted tally is NOT the 2:1 printed above -- the printed ratio is the unweighted one"
# 4. PART 5's conflict, as stated: 12 + 3 = 15 seats against a non-terminating mode count
assert 3*2*2 == 12 and 12 + 3 == 15, \
    "the seat count is 3 colour x 2 horn x 2 chirality = 12 legs, plus 3 walls = 15"
