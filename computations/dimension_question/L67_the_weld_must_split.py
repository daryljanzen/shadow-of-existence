#!/usr/bin/env python3
"""
L-67 — THE WELD.  ** FIRST-RANK, AND IT REACHES A LANDED RESULT. **

The conflict, stated at c54.21 and forced at c54.24:

  COMBINATORICS L8.1-a welds  roots = hinges = walls = GENERATIONS  into "one 3", and P14
  seats a generation at each hinge wall.  ** But the causal trichotomy forces a bound triple
  to take ONE PUNCTURE PER HINGE, so a proton is one of each COLOUR -- three generations in
  one proton is wrong.  The hinge three must be colour, so it is not also generation. **

  And the corpus already has a SECOND three, PROVED DISTINCT (lem:twoturnings): the
  bead/turnaround roots.  ** If one three is colour, that is the natural seat of generation. **

  ⚠ AND THE COST THAT MAKES THIS FIRST-RANK: the D = 4 result runs through "the fold is D-1"
  and "the fold IS the generation count", VIA THIS WELD.  ** If the weld splits, that step
  must be re-examined at generation's new seat.  Not obviously damaged.  Not automatically
  fine. **

  PART 1  The turnaround law at general D, derived rather than quoted.
  PART 2  ** Its deck group.  Is the turnaround three also D-1? **
  PART 3  Why BOTH threes are D-1 -- and this answers L-07 as well.
  PART 4  So does the dimension result's fold step survive the split?
  PART 5  What the split COSTS: S_3 against Z_3, and what P14 would have to change.
  PART 6  The verdict, and what is still owed.

Run: python3 L67_the_weld_must_split.py     (sympy)
"""

import sympy as sp

print(__doc__.split("Run:")[0])
r, M, al, tau, D = sp.symbols('r M alpha tau D', positive=True)
Dv_s = sp.Symbol('D', integer=True, positive=True)

# =====================================================================
print("=" * 78)
print("PART 1 — THE TURNAROUND LAW AT GENERAL D, DERIVED")
print("=" * 78)
print("  P8 prop:cosmo, at D = 4: the marginally-bound (E = 1) radial geodesic integrates to")
print("     r^3 = 2 M alpha^2 sinh^2(3 tau / 2 alpha)")
print("  and P3 sec:temporal-threeness reads its Z_3 off the cube root.")
print()
print("  ** With (A1) discharged (L-01), f = 1 - 2M/r^(D-3) - r^2/alpha^2 at every D, so the")
print("     E = 1 condition (dr/dtau)^2 = 1 - f generalises with no further input: **")
print()
print("     (dr/dtau)^2 = 2M/r^(D-3) + r^2/alpha^2")
print()
print("  Ansatz, the obvious one:  r^(D-1) = 2 M alpha^2 sinh^2( (D-1) tau / (2 alpha) )")
print("  Verified by substitution at each D:")
print()
print(f"  {'D':>3} {'the proposed law':>44} {'(dr/dtau)^2 - (2M/r^(D-3) + r^2/a^2)':>40}")
allok = True
for Dv in (4, 5, 6, 7, 8):
    n = Dv - 1
    rr = (2*M*al**2*sp.sinh(n*tau/(2*al))**2)**sp.Rational(1, 1)  # r^(D-1)
    r_of_tau = (2*M*al**2*sp.sinh(n*tau/(2*al))**2)**sp.Rational(1, n)
    lhs = sp.simplify(sp.diff(r_of_tau, tau)**2)
    rhs = sp.simplify(2*M/r_of_tau**(Dv-3) + r_of_tau**2/al**2)
    d = sp.simplify(sp.expand(sp.simplify(lhs - rhs)))
    allok &= (d == 0)
    print(f"  {Dv:>3} {'r^'+str(n)+' = 2 M a^2 sinh^2('+str(n)+' t/2a)':>44} {str(d):>40}")
print()
print(f"  ** THE MARGINALLY-BOUND LAW AT EVERY D IS r^(D-1) = 2 M alpha^2 sinh^2((D-1) tau/2 alpha)"
      f": {allok} **")
print("     and at D = 4 it is P8's own r^3 = 2 M alpha^2 sinh^2(3 tau/2 alpha).")

# --- r2376+c54.159 -----------------------------------------------------------------
# PART 1's CLAIM, ASSERTED.  The file computed the verdict flag `allok` and only printed it.
# INDEX: "the marginally-bound condition (dr/dtau)^2 = 1 - f ... is verified by substitution
# at D=4..8 to integrate to r^(D-1) = 2 M alpha^2 sinh^2((D-1) tau/2 alpha) -- P8 prop:cosmo's
# own law at D=4."  Pinned at the loop's last row, D = 8: the exponent is n = D-1 = 7 and the
# residual (dr/dtau)^2 - (2M/r^(D-3) + r^2/a^2) is EXACTLY zero there.
assert allok, "the turnaround law must hold at every D from 4 to 8"
assert (Dv, n) == (8, 7), "the last D tested must be 8, with exponent D-1 = 7"
assert d == 0, "the residual at D = 8 must be exactly zero"
# -----------------------------------------------------------------------------------

# =====================================================================
print()
print("=" * 78)
print("PART 2 — ITS DECK GROUP.  IS THE TURNAROUND THREE ALSO D-1?")
print("=" * 78)
print("  P3's argument at four: sinh^2 has period i pi in its argument, so the shift")
print("  tau -> tau + 2 pi i alpha/3 leaves r^3 INVARIANT and permutes the three cube-root")
print("  sheets, r -> e^{2 pi i/3} r.  ** Run the same argument on r^(D-1): **")
print()
print(f"  {'D':>3} {'period in tau leaving r^(D-1) fixed':>38} {'r -> ? r':>18} {'deck group':>14}")
for Dv in (4, 5, 6, 7, 8):
    n = Dv - 1
    period = sp.simplify(2*sp.pi*sp.I*al/n)
    # check invariance of sinh^2 under tau -> tau + period
    arg = n*tau/(2*al)
    shifted = sp.simplify(sp.expand_trig(sp.sinh(n*(tau + period)/(2*al))**2)
                          - sp.sinh(arg)**2)
    inv = sp.simplify(shifted) == 0
    w = sp.exp(2*sp.pi*sp.I/n)
    print(f"  {Dv:>3} {'2 pi i alpha/'+str(n)+'   (invariant: '+str(inv)+')':>38} "
          f"{'e^{2 pi i/'+str(n)+'}':>18} {'Z_'+str(n):>14}")
print()
print("  ** SO THE TURNAROUND'S DECK GROUP IS Z_{D-1} AT EVERY D. **")
print("     At D = 4 it is Z_3 -- the corpus's own.  At D = 5 it is Z_4.")
print()
# --- r2376+c54.159 -----------------------------------------------------------------
# PART 2's CLAIM, ASSERTED.  INDEX: "sinh^2 has period i pi, so tau -> tau + 2 pi i
# alpha/(D-1) leaves r^(D-1) invariant ... (invariance verified at each D), so THE TURNAROUND
# FOLD IS Z_{D-1}."  The loop only printed `inv`.  Pinned at its last row, D = 8: the period
# is 2 pi i alpha/7, the shift leaves sinh^2 invariant, and the deck generator is the
# PRIMITIVE 7th root of unity -- w^7 = 1 with w != 1, i.e. the group is Z_7 = Z_{D-1}.
assert inv, "the shift by 2 pi i alpha/(D-1) must leave sinh^2 invariant at D = 8"
assert sp.simplify(period - 2*sp.pi*sp.I*al/7) == 0, "the D = 8 period must be 2 pi i alpha/7"
assert sp.simplify(w**7 - 1) == 0 and sp.simplify(w - 1) != 0, \
    "the deck generator at D = 8 must be a primitive 7th root of unity"
# -----------------------------------------------------------------------------------
print("  ⇒ ** THE TURNAROUND FOLD IS D-1, EXACTLY AS THE HORIZON FOLD IS. **")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — WHY BOTH THREES ARE D-1.  ** AND THIS ANSWERS L-07. **")
print("=" * 78)
print("  L-07 has been in the register since c54.16: 'two distinct threes with ONE CAUSE --")
print("  the horizon-root three and the bead/turnaround three are PROVED DISTINCT")
print("  (lem:twoturnings) and are BOTH D-1.  Why do two distinct objects share the cause?'")
print()
print("  ** THE ANSWER IS ONE LINE, AND (A1)'s DISCHARGE IS WHAT MAKES IT SAYABLE. **")
print("  Clear the denominators in f = 1 - 2M/r^(D-3) - r^2/alpha^2:")
print()
for Dv in (4, 5, 6):
    num = sp.simplify(sp.expand((1 - 2*M/r**(Dv-3) - r**2/al**2)*r**(Dv-3)))
    deg = sp.degree(sp.Poly(sp.expand(num*al**2), r), r)
    print(f"     D = {Dv}:  f = 0  <=>  {sp.simplify(num*al**2)} = 0   -- degree {deg} in r")
print()
# --- r2376+c54.159 -----------------------------------------------------------------
# PART 3's CLAIM, ASSERTED -- the one that answers L-07.  Clearing denominators in
# f = 1 - 2M/r^(D-3) - r^2/alpha^2 leaves a polynomial of degree D-1 in r.  Pinned at the
# loop's last row, D = 6: the degree is 5 = D-1, and the numerator is exactly
# alpha^2 r^3 - 2 M alpha^2 - r^5 -- so BOTH threes descend from one degree-(D-1) object.
assert (Dv, deg) == (6, 5), "f's numerator must have degree D-1 = 5 at D = 6"
assert sp.simplify(num*al**2 - (al**2*r**3 - 2*M*al**2 - r**5)) == 0, \
    "the cleared numerator at D = 6 must be alpha^2 r^3 - 2 M alpha^2 - r^5"
# -----------------------------------------------------------------------------------
print("  ** f's NUMERATOR IS A POLYNOMIAL OF DEGREE D-1 IN r, AT EVERY D. **")
print()
print("  And the two threes are the two things one does with that one polynomial:")
print(f"  {'the three':>26} {'is':>34} {'D-1 because':>34}")
for a, b, c in (("the HORIZON three", "the ZERO SET of f",
                 "the numerator has degree D-1"),
                ("the TURNAROUND three", "the DECK ACTION of the integral of 1-f",
                 "1 - f = 2M/r^(D-3) + r^2/a^2, whose\n"
                 "                                                                     "
                 "integral gives r^(D-1) = 2Ma^2 sinh^2")):
    print(f"  {a:>26} {b:>34} {c:>34}")
print()
print("  ⇒ ** L-07 ANSWERED: the two threes are distinct because one is f's ZEROS and the")
print("     other is the deck action of the integral of 1 - f -- and they share the cause")
print("     because BOTH descend from the SAME degree-(D-1) numerator. **")
print("     lem:twoturnings proves no affine map identifies the root sets; that is exactly")
print("     right and is not in tension with this -- ** a common cause is not an identity,")
print("     which is the criterion this session has had to learn four times. **")
print()
print("  ⇒ AND THE THIRD THING L-07 ASKED: 'is there a THIRD?'  Any construction reading a")
print("     fold off f is reading off a degree-(D-1) object.  ** The prediction is that every")
print("     such three in the corpus is D-1 and that there is no independent one. **  Not")
print("     proved here; stated as the shape L-07's third clause now has.")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — DOES THE DIMENSION RESULT'S FOLD STEP SURVIVE THE SPLIT?")
print("=" * 78)
print("  The step at risk: 'the fold the count reads is D-1 in a D-dimensional cut', with")
print("  the fold IDENTIFIED as the generation count through L8.1-a's weld.")
print()
print(f"  {'seat of GENERATION':>28} {'its fold':>12} {'is it D-1?':>12} {'at D=4':>8} {'at D=5':>8}")
for nm, fold in (("the HINGE three (weld, as was)", "D-1"),
                 ("the TURNAROUND three (split)", "D-1")):
    print(f"  {nm:>28} {fold:>12} {'YES':>12} {'3':>8} {'4':>8}")
print()
print("  ** THE FOLD IS D-1 AT EITHER SEAT.  THE DIMENSION RESULT'S FOLD STEP SURVIVES THE")
print("     SPLIT UNCHANGED. **")
print()
print("  And it survives for a better reason than luck: PART 3 shows both threes are D-1")
print("  because both descend from f's degree-(D-1) numerator, so ** the fold is a property")
print("  of f rather than of which structure one reads it on. **  Moving generation from one")
print("  D-1 object to another D-1 object cannot change a count that is D-1 either way.")
print()
print("  ⇒ AND THE D = 5 STATEMENT IS UNCHANGED TOO: four generations there, now read off")
print("     the turnaround's Z_4 rather than the horizon quartic, and the same number.")

# =====================================================================
print()
print("=" * 78)
print("PART 5 — WHAT THE SPLIT COSTS.  S_3 AGAINST Z_3.")
print("=" * 78)
print("  ** THE SPLIT IS NOT FREE, AND THIS IS THE PART P14 WOULD HAVE TO CHANGE. **")
print()
print(f"  {'the three':>24} {'its symmetry':>34} {'source':>26}")
rows = [
 ("the HORIZON three", "S_3 -- the WEYL group / monodromy of the",
  "P5 rem:monodromy-group"),
 ("", "cubic over the mass plane, generated by", ""),
 ("", "transpositions", ""),
 ("the TURNAROUND three", "Z_3 -- the CYCLIC deck action of cosmic",
  "P3 sec:temporal-threeness"),
 ("", "time's imaginary period", ""),
]
for a, b, c in rows:
    print(f"  {a:>24} {b:>34} {c:>26}")
print()
print("  ** Z_3 IS A SUBGROUP OF S_3, AND THEY ARE NOT THE SAME GROUP. **")
print()
print("  P14 currently reads the family symmetry as the WEYL S_3: 'a transposition of roots")
print("  is a hop to a neighbouring hinge and the Weyl S_3 IS the relation among the three")
print("  hinges'.  ** On the split that sentence is about COLOUR, not flavour. **")
print()
print("  ⇒ ** SO THE SPLIT PREDICTS: colour carries the full S_3 (the transpositions ARE the")
print("     hops between hinges, which is what the causal trichotomy needs for a singlet),")
print("     and FLAVOUR carries only the cyclic Z_3. **")
print("  ⇒ and that is a CONSEQUENCE with content rather than a repair: an S_3 family")
print("     symmetry and a Z_3 family symmetry are different physics, and the Standard")
print("     Model's flavour literature treats both as candidates.  ** The corpus would be")
print("     saying Z_3, and saying it for a reason. **  (L-91.)")
print()
print("  ⚠ AND THE SECOND COST, WHICH IS NOT YET PAID: P14's chirality is R = gamma^5, the")
print("  OFFSET parity r0 -> -r0, which acts on the horizon/offset structure.  ** Whether R")
print("  acts on the TURNAROUND three at all is not shown here, and P14 needs the generations")
print("  chiral.  If R does not reach the new seat, the split costs the chirality grading and")
print("  that would be serious. **  (L-92 -- and it is the split's real falsifier.)")

# =====================================================================
print()
print("=" * 78)
print("PART 6 — THE VERDICT")
print("=" * 78)
for s in [
 "⌗ THE SPLIT IS ADMISSIBLE, AND THE DIMENSION RESULT IS NOT DAMAGED BY IT.",
 "   · the turnaround law at general D is r^(D-1) = 2 M alpha^2 sinh^2((D-1) tau/2 alpha),",
 "     derived here from f rather than assumed, with (A1) discharged behind it",
 "   · its deck group is Z_{D-1}, so ** the turnaround fold is D-1 **",
 "   · BOTH threes are D-1 because both descend from f's degree-(D-1) numerator, which",
 "     ** answers L-07's 'one cause' after thirteen revisions **",
 "   · so the fold step survives the split, and survives it structurally rather than by",
 "     luck: the fold is a property of f, not of which structure reads it",
 "",
 "⌗ WHAT THE SPLIT COSTS, AND IT IS REAL:",
 "   · flavour's symmetry becomes Z_3 (cyclic) where P14 has S_3 (Weyl).  ** Content, not",
 "     damage -- but P14's sentence about the family symmetry becomes a sentence about",
 "     COLOUR, and that is a substantive revision. **  (L-91.)",
 "   · ** whether R = gamma^5 reaches the turnaround three is NOT shown, and P14 needs the",
 "     generations chiral.  This is the split's falsifier and it is unrun. **  (L-92.)",
 "",
 "⌗ WHAT IS NOT DONE HERE: the revision to P14 itself.  ** The weld is shown SPLITTABLE",
 "   without cost to the dimension result; it is not yet SPLIT in the papers, and it should",
 "   not be until L-92 is run. **  A split that costs the chirality would be worse than the",
 "   conflict it resolves.",
]:
    print("  " + s)
