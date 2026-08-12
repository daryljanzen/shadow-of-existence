#!/usr/bin/env python3
"""
L-59 + L-52 — WHAT EXCHANGES uud AND udd, AND IS IT SEATED IN CHARGE?

THESE ARE ONE QUESTION AND ARE WORKED TOGETHER.  L-52 was restated by Daryl at c54.19: not
"what distinguishes the two readings" -- the geometry provably cannot distinguish them, the
symmetry group being transitive -- but ** what RELATION EXCHANGES them, and where is it
seated? **  L-59 is unseated proposed seat: "I'd be surprised if there wasn't a connection
THERE between charge and uud vs udd", together with the observation that drove it --

    "I've already told you about the 2/3 vs 1/3 asymmetry ... THEY'RE EVEN THE OPPOSITE
     DIRECTION!"

** THE OPPOSITE-DIRECTION REMARK IS THE WHOLE OF THE ANSWER AND THIS COMPUTATION IS MOSTLY
   THE WORK OF NOTICING THAT.  A reflection reverses direction; a translation does not. **

  PART 1  The corpus's own winding variables, and the two candidate exchanges.
  PART 2  ** Charge conjugation ALONE CANNOT DO IT. **  A clean negative, computed.
  PART 3  ** The unique involution that does: an AFFINE REFLECTION, and it is not in D_6. **
  PART 4  Where its two pieces are seated -- and BOTH are the corpus's own.
  PART 4b ** CORRECTED c54.37 -- THE INVOLUTION IS T, THE HORN SWAP, AND THE CORPUS
           ALREADY HAD IT.  My 'it must be adjoined from outside D_6' was wrong. **
  PART 5  ** The offset is 1/(number of walls), and that is a falsifiable correspondence. **
  PART 6  The winding charge against the Maxwell charge -- REWRITTEN c54.37 against P9.

Run: python3 L59_the_exchange_is_an_affine_reflection.py     (sympy)
"""
import itertools
import sympy as sp

print(__doc__.split("Run:")[0])
third = sp.Rational(1, 3)

# =====================================================================
print("=" * 78)
print("PART 1 — THE CORPUS'S OWN VARIABLES, AND WHAT AN EXCHANGE HAS TO DO")
print("=" * 78)
print("  L-65/L-73 derived charge as a WINDING: the signed count of graze-point crossings.")
print("  Two routes between punctures cross 1 and 2 of the 3 graze points, so they differ by")
print("  exactly ONE LAP; imposing that difference and closure of both horn-families gives")
print("  3x in Z, with exactly THREE solution classes.  In the corpus's own numbers:")
print()
u, d = sp.Rational(2, 3), sp.Rational(-1, 3)
print(f"  {'class':>12} {'winding w':>12} {'3w':>5} {'reads as':>12}")
for nm, w in (("quark (u)", u), ("quark (d)", d), ("antiquark", -u), ("lepton", sp.Integer(0))):
    print(f"  {nm:>12} {str(w):>12} {str(3*w):>5} {('integer' if (3*w).is_Integer else '?'):>12}")
print()
print(f"  ** AND THE TWO QUARK WINDINGS DIFFER BY EXACTLY ONE LAP: u - d = {u - d}. **")
print("  That is not an input; it is the x - y = 1 the closure derivation imposes.")
print()
print("  ⌗ SO THE QUESTION IS EXACT: what involution of the winding line exchanges")
print(f"  w = {u} and w = {d}?  ** And uud <-> udd is exactly that involution applied")
print("  to a triple, which swaps which of the two windings is doubled. **")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — CHARGE CONJUGATION ALONE CANNOT DO IT.  A negative, and a sharp one.")
print("=" * 78)
print("  P3 sec:charge establishes the charge involution geometrically: f carries Q only as")
print("  Q^2, so Q -> -Q fixes every horizon root and adjoins a Z_2 INDEPENDENT of")
print("  Aut(A_2) = D_6 'rather than sitting within it'.  On the winding line that is w -> -w.")
print("  ** Apply it: **")
print()
print(f"  {'map':>16} {'u = 2/3 ->':>12} {'d = -1/3 ->':>13} {'exchanges u,d?':>16}")
def show(nm, fmap):
    ok = (sp.simplify(fmap(u) - d) == 0) and (sp.simplify(fmap(d) - u) == 0)
    print(f"  {nm:>16} {str(fmap(u)):>12} {str(fmap(d)):>13} {str(ok):>16}")
    return ok
show("C:  w -> -w", lambda w: -w)
show("one lap: w-1", lambda w: w - 1)
show("one lap: w+1", lambda w: w + 1)
show("R (sign flip)", lambda w: -w)
print()
print("  ** CHARGE CONJUGATION SENDS THE QUARK CLASS TO THE ANTIQUARK CLASS, NOT u TO d. **")
print("  u -> -2/3 is ubar and d -> +1/3 is dbar; uud -> ubar ubar dbar, the ANTIBARYON.")
print("  ⇒ ** So L-59's proposal is NOT right as stated: charge conjugation alone is not the")
print("     uud/udd exchange, and no single lap shift is either. **  And the reason is visible")
print("     in the table: C is a reflection through the ORIGIN, and the u,d pair is not")
print("     centred on the origin.")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE UNIQUE INVOLUTION THAT DOES IT, AND IT IS AFFINE")
print("=" * 78)
print("  An involution of a line exchanging two given points is either the translation by")
print("  their difference (not an involution unless the difference is zero) or the REFLECTION")
print("  in their midpoint.  So there is exactly one candidate and it is forced:")
print()
c = sp.symbols('c')
sol = sp.solve([sp.Eq(c - u, d), sp.Eq(c - d, u)], c, dict=True)
cval = sol[0][c]
print(f"      w -> c - w   with   c = u + d = {u} + ({d}) = {cval}")
print(f"      midpoint = {sp.Rational(1,2)*(u+d)} = c/2")
ok = show("w -> 1/3 - w", lambda w: third - w)
print()
print(f"  ** SO THE EXCHANGE IS  w -> 1/3 - w :  UNIQUE, INVOLUTIVE, AND AFFINE. **  ({ok})")
print(f"     involution check: applying it twice returns w?  "
      f"{sp.simplify(third - (third - sp.Symbol('w'))) == sp.Symbol('w')}")
print()
print("  ⌗ ** AND THIS IS WHERE DARYL'S 'THEY'RE EVEN THE OPPOSITE DIRECTION' IS THE PROOF.**")
print("  The map has a MINUS SIGN on w.  A pair related by a reflection runs in opposite")
print("  directions from the fixed point; a pair related by a translation runs the same way.")
print(f"  u and d sit at {u - cval/2} and {d - cval/2} about the fixed point c/2 = {cval/2}:")
print("  ** equal and opposite.  The observation that the two charges point opposite ways is")
print("     exactly the statement that the exchange is a REFLECTION and not a shift, and it")
print("     is what rules out every translation in PART 2 at a glance. **")
print()
print("  ⌗ AND IT IS THE STANDARD MODEL'S OWN MAP, WHICH IS THE CHECK THAT IT IS RIGHT:")
print("  with Q = I_3 + Y/2, the isospin Weyl reflection I_3 -> -I_3 at fixed Y is")
print("  Q -> Y - Q.  For the quark doublet Y = 1/3 and that is  Q -> 1/3 - Q, identically.")
Y = third
print(f"      Y - Q at Q = 2/3, Y = 1/3:  {Y - u}   and at Q = -1/3:  {Y - d}")
print("  ** The corpus's winding-line involution IS the isospin Weyl element.  Nothing was")
print("     fitted: c was solved for, and it came out equal to the doublet's hypercharge. **")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — WHERE ITS TWO PIECES SIT.  Both are the corpus's, and NEITHER is in D_6.")
print("=" * 78)
print("  Factor the involution:      w -> 1/3 - w   =   (w -> -w)  followed by  (w -> w + 1/3)")
print()
print(f"  {'piece':>22} {'what it is in the corpus':>44}")
for a, b in [
    ("w -> -w", "CHARGE CONJUGATION -- P3 sec:charge's independent Z_2"),
    ("w -> w + 1/3", "ONE THIRD OF A LAP = ONE GRAZE-POINT CROSSING = ONE WALL"),
]:
    print(f"  {a:>22} {b:>44}")
print()
for s in [
 "⇒ ** SO L-59'S ANSWER IS 'HALF YES', AND THE HALF IS PRECISE: the exchange is SEATED IN",
 "   CHARGE FOR ITS REFLECTION AND IN THE WALL COUNT FOR ITS OFFSET.  Charge supplies the",
 "   minus sign Daryl noticed; the three walls supply the 1/3. **",
 "",
 "⇒ ** AND L-52 IS ANSWERED, IN THE FORM DARYL RESTATED IT.  The relation exchanging the two",
 "   readings is an AFFINE reflection.  Aut(A_2) = D_6 acts LINEARLY on the root space -- every",
 "   element fixes the origin -- so a map with a nonzero offset CANNOT lie in it, whatever it",
 "   is.  The exchange therefore REQUIRES a symmetry adjoined from outside D_6. **",
 "",
 "⌗ AND P3 SAID SO, ABOUT THIS EXACT Z_2, BEFORE ANY OF THIS WAS ASKED.  sec:charge:",
 "   'because it is a symmetry of the charge and not of the mass roots the A_2 system",
 "    realises -- Q absent from the horizon cubic, so Q -> -Q fixes every root -- it adjoins",
 "    an INDEPENDENT Z_2 to the solution space's Aut(A_2) = D_6 RATHER THAN SITTING WITHIN IT.'",
 "** That sentence was written as a bookkeeping remark about where charge lives.  It is the",
 "   structural precondition for the uud/udd exchange to exist at all. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4b — CORRECTION.  THE INVOLUTION IS T, AND THE CORPUS ALREADY HAD IT.")
print("=" * 78)
print("  ** PART 4 ABOVE IS WRONG WHERE IT MATTERS AND IS LEFT STANDING SO THE ERROR IS")
print("     VISIBLE.  It concluded that the exchange 'REQUIRES a symmetry adjoined from")
print("     outside D_6', on the argument that D_6 acts LINEARLY and an affine map cannot")
print("     lie in it.  ** The argument compares objects in two different spaces. **  D_6")
print("     acts on the ROOT SPACE; w lives on the WINDING LINE, which is an affine line with")
print("     no canonical origin -- its zero is the lepton class, which is a CHOICE.  An offset")
print("     on that line says nothing about membership in a group acting somewhere else. **")
print()
print("  ⌗ AND THE CORPUS ALREADY IDENTIFIED THE EXCHANGE, AT THE LEVEL OF THE TRIPLE.")
print("  P03_winding_and_closure and THE_FERMION_SECTOR_GEOMETRY both record:")
print()
print("     'the upper-headed triple (u,d,d) totals 0 and the lower-headed (d,u,u) totals +1,")
print("      so THE HORN SWAP COSTS EXACTLY ONE LAP -- the nucleon doublet'")
print("     'INVOLUTIONS: sigma -> COLOUR, T -> WEAK ISOSPIN, R -> CHIRALITY AND SPECIES'")
print()
print("  ** T IS THE HORN SWAP X_0 -> -X_0, AN ACTUAL SUBSTRATE ISOMETRY, and it exchanges")
print("     the head and partner roles of a triple.  Check that my constituent-wise map does")
print("     exactly that: **")
print()
head, part = u, d
up_triple = (head, part, part)          # (u,d,d), the upper-headed one
lo_triple = (part, head, head)          # (d,u,u), the lower-headed one
img = tuple(third - w for w in up_triple)
print(f"  {'triple':>26} {'total':>7} {'reads as':>12}")
print(f"  {str(up_triple):>26} {str(sum(up_triple)):>7} {'the neutron':>12}")
print(f"  {str(lo_triple):>26} {str(sum(lo_triple)):>7} {'the proton':>12}")
print(f"  {'image under w -> 1/3 - w':>26} {str(sum(img)):>7} "
      f"{('= the lower triple: ' + str(img == lo_triple)):>12}")
print(f"     and the total moves by {sum(lo_triple) - sum(up_triple)} -- EXACTLY ONE LAP, "
      f"which is what the corpus says T costs.")
print()
for s2 in [
 "⇒ ** SO THE CORRECTED ANSWER, AND IT IS BETTER THAN THE ONE I GAVE: the uud/udd exchange",
 "   IS T, THE HORN SWAP.  Nothing needs adjoining.  It is a substrate isometry, it is inside",
 "   the configuration's own symmetry group (P3: 'the dihedral symmetry of the three stations",
 "   together with the horn swap T, of order twelve'), and the corpus had already read it as",
 "   WEAK ISOSPIN. **",
 "",
 "⌗ WHAT IS ACTUALLY NEW HERE IS THEREFORE NOT THE EXCHANGE BUT ITS ACTION ON A SINGLE",
 "CONSTITUENT.  The corpus had T at the level of the TRIPLE (a total moving by one lap).",
 "** Constituent-wise T is the affine reflection w -> 1/3 - w, whose FIXED POINT is 1/6 --",
 "and 1/6 = Y/2 for the quark doublet.  So T's fixed point on the winding line IS the",
 "hypercharge. **  That is new and it is what PART 5 then tests.",
 "",
 "⇒ ** AND L-59's QUESTION GETS A CLEANER ANSWER THAN 'HALF YES'.  The exchange is NOT",
 "   seated in charge: it is seated in T.  What charge does is fix the ORIGIN against which",
 "   T is read. **  On the winding line C is w -> -w (reflection at 0) and T is w -> 1/3 - w",
 "   (reflection at 1/6), and two reflections of a line compose to a TRANSLATION:",
 f"      T o C : w -> {sp.simplify(third - (-sp.Symbol('w')))}   -- a shift by 1/3,",
 "   ** which is ONE GRAZE-POINT CROSSING: one wall, one colour step. **",
 "",
 "⌗ ** SO C, T AND THE COLOUR STEP CLOSE A TRIANGLE ON THE WINDING LINE: T o C = sigma. **",
 "   The corpus's three involution-readings -- sigma -> colour, T -> isospin, R -> chirality",
 "   and species -- are NOT independent there: any two of {C, T, one colour step} give the",
 "   third.  ** That is a relation among the three assignments, and it is the thing L-59 was",
 "   actually pointing at.  Daryl's 'I'd be surprised if there wasn't a connection THERE",
 "   between charge and uud vs udd' is right, and the connection is this composition law",
 "   rather than an identification. **",
]:
    print("  " + s2)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — THE OFFSET IS 1/(NUMBER OF WALLS), WHICH IS A FALSIFIABLE CORRESPONDENCE")
print("=" * 78)
print("  The 1/3 is not decoration: it is one crossing out of the THREE graze points, and the")
print("  three graze points are the three walls, which are the corpus's colour three.  So the")
print("  reflection's offset is 1/N with N the wall count.  Run the counterfactual:")
print()
print(f"  {'N walls':>8} {'offset 1/N':>11} {'the doublet Q values':>26} {'baryon of 3':>12}")
integral = []
for N in (1, 2, 3, 4, 5, 6):
    off = sp.Rational(1, N)
    # the pair straddles the fixed point off/2 at +-1/2 (one lap apart, by the closure rule)
    qu, qd = off/2 + sp.Rational(1, 2), off/2 - sp.Rational(1, 2)
    B = 2*qu + qd
    if B.is_Integer: integral.append(N)
    print(f"  {N:>8} {str(off):>11} {str((qu, qd)):>26} {str(B):>12}"
          + ("   <- integer" if B.is_Integer else ""))
print()
print(f"  ** THE TRIPLE IS INTEGRAL AT N = {integral} AND NOWHERE ELSE. **  Solving it: the")
print("     baryon charge is 2q_u + q_d = 3/(2N) + 1/2, integral iff 3/(2N) is a half-odd")
print("     integer, iff N = 1 or N = 3.  ** SO THE FORCING IS TO A PAIR, NOT TO A POINT, and")
print("     saying otherwise would be the exact kind of overstatement the base rate punishes. **")
print()
print("  ⌗ AND CR EXCLUDES N = 1 BY A PRINCIPLE IT ALREADY ARGUES ELSEWHERE, not by taste.")
print("  P14: 'a one-hinge truncation is excluded NOT AS DISFAVOURED but as carrying an")
print("  unfixed arbitrary modulus, which the principle forbids' -- Rule 2, the corpus's own")
print("  least-arbitrariness criterion, whose favourable-side credentials THE_BASE_RATE")
print("  scores as a DELETE (it removes an arbitrary choice among three Z_3-equivalent")
print("  options).  ** So N = 3 is forced by integrality PLUS a criterion already in force")
print("  for independent reasons, rather than by integrality alone. **  That is a weaker")
print("  claim than the table alone suggests and a better-founded one.")
print()
for s in [
 "⌗ WHAT N ACTUALLY CONTROLS IS WORTH SAYING SEPARATELY.  The pair SPREAD is 1 at every N,",
 "   fixed by the closure rule; what N sets is where the pair SITS on the line.  ** So the",
 "   wall count does not create the doublet -- the closure rule does -- it POSITIONS it, and",
 "   the position is what makes a triple of them integral. **",
 "",
 "⌗ AND THE STANDARD MODEL AGREES BY A ROUTE THAT MENTIONS NONE OF THIS.  Y_Q = 1/3 for the",
 "quark doublet, and it is tied to N_c = 3 by ANOMALY CANCELLATION -- which is exactly the",
 "condition P14 already carries: 'given the colour and isospin assignments, that same",
 "condition fixes the hypercharges uniquely up to normalisation'.  ** So the corpus reaches",
 "Y = 1/N_c from the wall count and the SM reaches it from anomaly cancellation, and the two",
 "meet at 1/3. **  ⚠ Recorded as a MATCH and not a derivation: nothing here computes an",
 "anomaly, and the winding variable's identification with electric charge is L-65's reading",
 "rather than a theorem.  ** But it is a NUMBER the construction did not get to choose. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 6 — THE WINDING CHARGE AGAINST THE MAXWELL CHARGE.  Rewritten c54.37.")
print("=" * 78)
print("  ** THE FIRST VERSION OF THIS SECTION WAS WRITTEN OFF ONE SENTENCE OF P3 AND SAID")
print("     'A NONZERO MAXWELL CHARGE DESTROYS THE r = 0 BRANCH POINT', AS THOUGH THAT WERE")
print("     A TENSION I HAD FOUND.  IT IS NOT.  IT IS A RESULT THE CORPUS ALREADY OWNS, ALREADY")
print("     LOCATES, AND ALREADY HANDS SOMEWHERE.  What follows is that, read properly. **")
print()
for s2 in [
 "① ** THE FACT IS P3's AND IT IS EXACT, NOT ALARMING. **  P3 sec:charge, scope paragraph:",
 "   with Q != 0 the Q^2/r^2 term dominates as r -> 0, so f -> +infinity, an inner (Cauchy)",
 "   turning point appears, and r = 0 becomes a timelike RN singularity rather than the branch",
 "   point.  Computed symbolically in P03_charge_parity with the Q = 0 control.  ** And P3",
 "   states in the same breath where it goes: 'the charged CLOSED LOOP through r = 0,",
 "   obstructed by the inner horizon the charge raises, IS AN INTERIOR REASSIGNMENT TIED TO",
 "   THE MATTER SIDE'. **",
 "",
 "② ** AND P9 ALREADY CARRIES THAT AS ITS ONE NAMED OPEN REMAINDER. **  range_paper:",
 "   'the one genuinely open remainder is THE IRREDUCIBLE INTERIOR REASSIGNMENTS (Kerr-inner,",
 "    Reissner-Nordstroem-interior) -- the vantage-axis complement, tied to the matter sector.'",
 "   ** So this is not a new tension.  It is an instance of a frontier the range paper named",
 "   and scoped, and P3's charged loop is exactly the RN-interior case of it. **",
 "",
 "③ ** WHAT P9 DOES SAY ABOUT CHARGE IS THE THING THAT ACTUALLY BEARS, AND I HAD NOT READ IT:",
 "   CHARGE IS THE BEND. **  rem:charge: the kernel of P9's classification theorem is the",
 "   VACUUM-Lambda family; the charged solutions are ELECTROVAC, with m(r) = M - Q^2/2r, the",
 "   bend m'(r) = Q^2/2r^2 sourced by A = -(Q/r)dt.  ** Charge is on the MATTER side of P9's",
 "   own primary axis, and the vacuum kernel is unchanged by it. **",
 "",
 "⇒ ** SO THE RELATION BETWEEN THE TWO CHARGES IS STATABLE IN THE CORPUS'S OWN PRIMARY",
 "   DIVISION, AND THAT IS THE INFORMED VERSION OF L-108: **",
 "",
 "      the WINDING charge  lives on the VACUUM KERNEL -- it is defined by crossings of the",
 "                          three graze points of the vacuum lap, and the thirds are forced by",
 "                          closure of that lap;",
 "      the MAXWELL charge  is the BEND -- matter on the cut, electrovac not vacuum, entering",
 "                          f only through Q^2 and leaving the vacuum kernel untouched.",
 "",
 "   ** THEY SIT ON OPPOSITE SIDES OF THE AXIS P9's WHOLE CLASSIFICATION IS BUILT ON. **  A",
 "   claim that the winding IS electric charge is therefore a claim that a vacuum-kernel datum",
 "   equals a matter-bend datum -- which is precisely the distinction P9 exists to draw.",
 "   ** That is a much sharper statement of the debt than 'Q kills the wall', and it is the",
 "   corpus's own language rather than my alarm. **",
 "",
 "④ ** AND ONE MORE THING I HAD WRONG BY OMISSION.  The corpus does NOT claim the winding is",
 "   electric charge. **  The winding derivation appears in no paper body -- it is receipted",
 "   and ledgered only -- and its own receipt marks the antecedent unshown: 'CONDITIONAL, and",
 "   the antecedent is NOT shown ... whether a matter field here is labelled by a ROUTE rather",
 "   than a point is L-74'.  ** So there is no live over-claim to defend against.  What is owed",
 "   is a POSITIVE account, not a repair. **",
 "",
 "⌗ AND THE SHAPE OF THAT ACCOUNT IS NOW CONSTRAINED, WHICH IS THE USEFUL OUTPUT:",
 "  * it cannot be a Q -> 0 LIMIT of the charged geometry, because the graze points are",
 "    features of the lap and the lap does not exist at Q != 0 -- there is nothing to take a",
 "    limit OF;",
 "  * it cannot be an identification, for ③;",
 "  * ** so it must be a CORRESPONDENCE between a vacuum-kernel index and a matter-bend",
 "    parameter -- which is structurally the same kind of statement as P13's charge-conjugation",
 "    FACTORISATION, where the substrate supplies every kinematic datum and only the charge",
 "    SIGN closes from the field. **  P13: 'C = (Q -> -Q)_field o (R o K)_geometric'.",
 "  ⇒ ** THE CANDIDATE SHAPE, REGISTERED AS SUCH: the winding supplies the QUANTISATION (the",
 "    thirds, from closure) and the Maxwell field supplies the SIGN and the SCALE (the coupling).",
 "    That is P13's factorisation pattern applied one level down, and it is testable against",
 "    P13's own machinery rather than being a new hope. **",
]:
    print("  " + s2)

# --- r2376+c54.161 : pin the claim, so the receipt can fail -------------------------------
# WHAT IS PINNED is the clean negative, the solved-for involution, PART 4b's corrected group
# identification, and PART 5's counterfactual.  ** PART 4's conclusion (that the exchange
# requires a symmetry adjoined from OUTSIDE D_6) is NOT pinned: PART 4b withdraws it, and the
# receipt leaves it standing only so the error is visible. **
# PART 1: the two quark windings differ by exactly one lap, and both are thirds
assert u - d == 1, "the printed lap difference is u - d = 1"
assert u == sp.Rational(2, 3) and d == sp.Rational(-1, 3), "the winding classes are 2/3 and -1/3"
assert all((3*wv).is_Integer for wv in (u, d, -u, sp.Integer(0))), \
    "3w is an integer on every class -- the thirds of the closure derivation"
# PART 2, THE CLEAN NEGATIVE: C carries the quark class to the ANTIQUARK class, and no lap
# shift exchanges the pair either.  If any of these ever became an exchange, PART 3 collapses.
assert sp.simplify(-u - d) != 0, "C: w -> -w does NOT send u to d -- it sends u to the antiquark -2/3"
assert -u == sp.Rational(-2, 3) and -d == sp.Rational(1, 3), "C returns the antiquark pair -2/3, 1/3"
for _shift in (-1, 1):
    assert not (sp.simplify(u + _shift - d) == 0 and sp.simplify(d + _shift - u) == 0), \
        f"the lap shift w -> w + {_shift} does not exchange u and d either"
# PART 3: the involution SOLVED FOR, not posited -- c came out equal to the doublet hypercharge
assert cval == sp.Rational(1, 3), "solving c - u = d and c - d = u gives c = 1/3"
assert ok, "w -> 1/3 - w must actually exchange u and d (the printed True)"
_w = sp.Symbol('w')
assert sp.simplify(third - (third - _w) - _w) == 0, "the map is an INVOLUTION: applying it twice returns w"
assert cval/2 == sp.Rational(1, 6), "the fixed point is the midpoint 1/6"
assert (u - cval/2, d - cval/2) == (sp.Rational(1, 2), sp.Rational(-1, 2)), \
    "u and d sit at +1/2 and -1/2 about the fixed point -- equal and OPPOSITE, hence a reflection"
# and it is the SM's own map: the isospin Weyl reflection Q -> Y - Q at the doublet's Y = 1/3
assert Y == sp.Rational(1, 3) and Y - u == d and Y - d == u, \
    "Q -> Y - Q with Y = 1/3 is identically the solved-for involution -- nothing fitted"
# PART 4b: the corrected identification.  T is the horn swap, and constituent-wise it carries
# the neutron triple to the proton triple, the TOTAL moving by exactly one lap.
assert img == lo_triple, "the image of (u,d,d) under w -> 1/3 - w is exactly (d,u,u)"
assert sum(up_triple) == 0 and sum(lo_triple) == 1, "the printed triple totals are 0 and +1"
assert sum(lo_triple) - sum(up_triple) == 1, "the horn swap costs EXACTLY ONE LAP"
assert sp.simplify((third - (-_w)) - (_w + third)) == 0, \
    "T o C is the TRANSLATION w -> w + 1/3 -- one graze-point crossing, one colour step"
# PART 5: the counterfactual, and it forces a PAIR not a point
assert integral == [1, 3], "the baryon charge is integral at N = 1 and N = 3 and nowhere else"
assert 3 in integral and len(integral) == 2, \
    "N = 3 is not forced by integrality alone -- N = 1 survives it and is excluded elsewhere"
assert sp.Rational(3, 2*3) + sp.Rational(1, 2) == 1, \
    "at N = 3 the baryon charge 3/(2N) + 1/2 is exactly 1 -- the printed proton charge"
assert sp.Rational(3, 2*2) + sp.Rational(1, 2) == sp.Rational(5, 4), \
    "at N = 2 it is 5/4, the printed non-integer"
assert sp.Rational(1, 3)/2 == sp.Rational(1, 6) == Y/2, \
    "the offset 1/N at N = 3 puts the fixed point at Y/2 for the quark doublet"
