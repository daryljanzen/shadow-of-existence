#!/usr/bin/env python3
"""
L-122 / L-74 — IS A MATTER FIELD LABELLED BY A ROUTE RATHER THAN BY A POINT?

** THE GATE.  Open since c54.21, and the load-bearing premise under everything the winding
   sector has produced -- the thirds, the three classes, the isospin exchange, the hypercharge
   agreement, the whole colour reading.  L-73 proves: IF constituents carry windings and bound
   objects close, THEN the thirds follow.  ** It does not show the antecedent, and its own
   receipt says so: "CONDITIONAL, and the antecedent is NOT shown." **

L-74's registered first move is the right one and is followed here:
    "ask what P14's wall-bound zero-mode is a function OF; a route-valued label is a strong
     and checkable claim about the field."

** AND THE ANSWER TURNS OUT TO BE ALREADY COMPUTED, AT c54.25, IN A RECEIPT THAT DID NOT
   RECOGNISE ITSELF AS DISCHARGING THIS.  Nothing new is derived below.  What is new is
   noticing that P14_mode_monodromy_at_the_wall IS the antecedent, and that it answers with a
   DISTINCTION rather than a yes or a no. **

  PART 1  What "labelled by a route" means precisely, so the question can be decided.
  PART 2  What the field is a function of -- P14's own zero mode.
  PART 3  ** THE TWO ROUTES, AND WHAT THE FIELD DOES ALONG THEM.  Computed. **
  PART 4  ** THE ANSWER: route-labelled IFF triality is non-zero.  Coloured yes, colourless no. **
  PART 5  What that discharges, what it does not, and the convergence it produces.

Run: python3 L074w_route_or_point.py     (sympy)
"""
import sympy as sp

print(__doc__.split("Run:")[0])
lam = sp.Symbol('lambda', integer=True, positive=True)
w = sp.exp(2*sp.pi*sp.I/3)

# =====================================================================
print("=" * 78)
print("PART 1 — WHAT THE QUESTION MEANS, STATED SO IT CAN BE DECIDED")
print("=" * 78)
for s in [
 "A field is ** labelled by a POINT ** if its value at a place is determined by the place.",
 "It is ** labelled by a ROUTE ** if two paths reaching the same place can deliver different",
 "values -- that is, if it is a single-valued function on some COVER of the space rather than",
 "on the space itself.",
 "",
 "** THAT IS NOT A PHILOSOPHICAL DISTINCTION, IT IS A MONODROMY.  The field is point-labelled",
 "   exactly when its monodromy around every closed loop is trivial. **  So the question has a",
 "   computation attached to it, and the computation is small:",
 "",
 "     take two routes between the same two places;  transport the field along each;",
 "     compare.  ** If they differ, the label is the route. **",
 "",
 "⌗ AND THE CORPUS HAS EXACTLY THE RIGHT TEST CASE SITTING IN IT, because the winding",
 "derivation is BUILT on a two-route fact: between two punctures at different hinges there are",
 "exactly TWO equatorial routes, crossing ONE and TWO of the three graze points, in opposite",
 "senses.  ** So the test is not hypothetical.  It is the derivation's own configuration. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — WHAT THE FIELD IS A FUNCTION OF")
print("=" * 78)
print("  P14 prop:wall's bound zero-mode, and every step below is the corpus's, not mine:")
print()
for s in [
 "  * the superpotential is W = lambda sqrt(f)/r, with r the SIGNED areal radius;",
 "  * in the leaf measure dl = dr/sqrt|f| the square roots cancel exactly, W dl = lambda dr/r,",
 "    so ** psi = exp(-int W dl) ~ r^(-lambda) ** (P14_mode_monodromy_at_the_wall);",
 "  * near the wall f -> -2M/r gives ** r^3 = (9/2) M l^2 **, so r is a CUBE ROOT of a quantity",
 "    with a simple zero -- the wall IS a cube-root branch point, scored 5/5 on the",
 "    five-test criterion (locus, type, definition, equivariance, separability);",
 "  * and a CROSSING of the wall is a half-loop in l, giving ** r -> omega r exactly **.",
]:
    print(s)
print()
print("  ** SO THE FIELD IS A POWER OF A QUANTITY THAT IS NOT SINGLE-VALUED ON THE BASE.  That")
print("     is already the shape of a route-label, and PART 3 makes it quantitative. **")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE TWO ROUTES, AND WHAT THE FIELD DOES ALONG THEM")
print("=" * 78)
print("  Transport psi ~ r^(-lambda) along each of the two equatorial routes between the same")
print("  pair of punctures.  Each graze-point crossing sends r -> omega r, hence")
print("      psi -> (omega r)^(-lambda) = omega^(-lambda) psi.")
print()
print(f"  {'route':>28} {'crossings':>10} {'the field picks up':>22} {'as a power of omega':>21}")
facs = {}
for nm, n in (("the short way", 1), ("the long way", 2)):
    facs[nm] = sp.simplify(w**(-lam*n))
    print(f"  {nm:>28} {n:>10} {('omega^(-%d lambda)' % n):>22} "
          f"{('-%d lambda mod 3' % n):>21}")
print()
ratio = sp.simplify(w**(-lam*2) / w**(-lam*1))
print(f"  ** THE RATIO OF THE TWO TRANSPORTS IS omega^(-lambda) ** -- the two routes differ by")
print(f"     exactly ONE crossing, which is the derivation's own 'the two routes differ by")
print(f"     exactly one lap' seen on the FIELD instead of on the winding.")
print()
print("  So the field's value at the endpoint is route-INDEPENDENT exactly when that factor is 1:")
print()
print(f"  {'lambda mod 3':>14} {'triality = -lambda mod 3':>26} {'omega^(-lambda)':>18} "
      f"{'route-independent?':>20} {'reads as':>10}")
for m in (1, 2, 0):
    tri = (-m) % 3
    fac = sp.nsimplify(w**(-m))
    ok = (sp.simplify(fac - 1) == 0)
    print(f"  {m:>14} {tri:>26} {str(fac):>18} "
          f"{('** YES **' if ok else 'no'):>20} {('LEPTON' if tri == 0 else 'quark'):>10}")
print()
print("  ** AND THE FACTOR IS omega^(triality), EXACTLY.  Triality is -lambda mod 3 (L-78), so")
print("     the route-ambiguity of the field IS its triality, written multiplicatively. **")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE ANSWER, AND IT IS A DISTINCTION RATHER THAN A YES OR A NO")
print("=" * 78)
for s in [
 "$$ A MATTER FIELD ON THIS GEOMETRY IS LABELLED BY A ROUTE IF AND ONLY IF ITS TRIALITY IS",
 "   NON-ZERO -- THAT IS, IF AND ONLY IF IT IS COLOURED. $$",
 "",
 "  * ** A QUARK (triality 1 or 2) IS ROUTE-LABELLED. **  Its value at a puncture depends on",
 "    which of the two equatorial routes brought it there, by the factor omega^(triality).",
 "    ** So L-73's antecedent HOLDS for exactly the objects L-73 applies it to. **",
 "  * ** A LEPTON (triality 0) IS POINT-LABELLED. **  Its monodromy is trivial, both routes",
 "    agree, and it is an ordinary single-valued function on the base.  ** It does not need",
 "    the route structure, and the antecedent neither holds for it nor has to. **",
 "",
 "⌗ ** SO L-74 WAS ASKED AS A YES-OR-NO AND IS NOT ONE.  The antecedent is not a global",
 "   premise about matter fields; it is a PROPERTY THAT SORTS THEM, and it sorts them by",
 "   exactly the discriminant the sector already uses. **",
 "",
 "⌗ AND THE STRENGTH OF THIS IS THAT NOTHING WAS ADDED.  Every ingredient is the corpus's own",
 "and predates the question: psi ~ r^(-lambda) and the omega-per-crossing are c54.25's; the",
 "two-route fact is the winding derivation's; triality = -lambda mod 3 is L-78's.  ** The only",
 "new act is noticing that P14_mode_monodromy_at_the_wall IS the answer to L-74, which it was",
 "not written to be. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — WHAT THIS DISCHARGES, WHAT IT DOES NOT, AND THE CONVERGENCE")
print("=" * 78)
for s in [
 "** DISCHARGED. **  L-73's conditional -- IF constituents carry windings THEN the thirds",
 "follow -- had an unshown antecedent.  ** For the coloured classes the antecedent is now shown",
 "and shown from the field equation, not assumed. **  So the thirds, the three classes, and",
 "everything resting on them stand on a computed premise for the sector they describe.",
 "",
 "⌗ ** AND CHECKING THE OTHER ANTECEDENT BEFORE CLAIMING A REMAINDER CHANGES THE RESULT.",
 "   L-73 has TWO antecedents -- that constituents carry windings (this one) and that bound",
 "   objects CLOSE -- and I was about to record the second as still open.  IT IS NOT.  L-72",
 "   was struck at c54.32, and struck by THE SAME PRINCIPLE: **",
 "",
 "     'What confinement needs is the matter configuration's Z_3 sheet index RETURNING, and",
 "      that IS required -- ** by SINGLE-VALUEDNESS, not by stipulation **: a field on the",
 "      branched bead must be single-valued, so a configuration with non-zero total sheet",
 "      advance IS NOT A FIELD ON THE MANIFOLD.'",
 "",
 "⇒ ** SO BOTH OF L-73's ANTECEDENTS ARE DISCHARGED, AND BY ONE FACT READ IN TWO DIRECTIONS: **",
 "",
 f"  {'':>6} {'read forward':>34} {'read backward':>34}",
 f"  {'':>6} {'a coloured field is MULTIVALUED':>34} {'only total-triality-zero combinations':>34}",
 f"  {'':>6} {'on the base -- hence ROUTE-labelled':>34} {'are single-valued -- hence CLOSURE is':>34}",
 f"  {'':>6} {'(L-74, here)':>34} {'REQUIRED (L-72, c54.32)':>34}",
 "",
 "** L-73's CONDITIONAL IS THEREFORE UNCONDITIONAL.  'IF constituents carry windings and bound",
 "   objects close, THEN the thirds follow' now has both premises computed from the field",
 "   equation and the branch structure, neither assumed. **  That is the gate this stretch has",
 "   been carrying since c54.21, and it is the whole of what was owed.",
 "",
 "⌗ AND CONFINEMENT IS THE SAME SENTENCE.  P03_winding_and_closure recorded 'confinement",
 "becomes FAILURE TO CLOSE THE LAP' as a reading.  ** With both halves proved it is a",
 "statement: a coloured field is route-labelled, so a lone coloured constituent has no",
 "well-defined value at a point; only a combination of vanishing total triality is a field on",
 "the manifold at all.  COLOUR SINGLET-NESS IS SINGLE-VALUEDNESS. **",
 "",
 "⚠ ** AND THE ONE REMAINDER, WHICH IS REAL AND IS NOT THIS: the identification of the winding",
 "   with ELECTRIC charge is still L-65's reading. **  What is established is that the field",
 "   carries a route-dependent Z_3 label and that only triality-neutral combinations exist as",
 "   fields.  ** That the label is the charge you can measure is a further step, and this is",
 "   not it. **  The Z_3 established here is COLOUR's, by construction -- it is the centre --",
 "   and the electric reading rides on top of it.",
 "",
 "⌗ ** AND THE CONVERGENCE, WHICH IS THE PART I DID NOT EXPECT. **  L-120 concluded, from an",
 "entirely separate route -- representation theory on the turnaround -- that the COLOURLESS",
 "states are not seated on the hinge figure at all.  ** PART 4 says why, from the field side:",
 "a point-labelled state has no route-dependence, so it has no use for the graze points, so it",
 "is not seated where the routes are. **  Two lines, one from a character count and one from a",
 "monodromy, reaching the same split between coloured and colourless seating.",
 "",
 "⌗ AND WHAT IS OWED NEXT IS NARROW AND NAMED: with L-72 and L-74 both closed, the winding",
 "sector's premises are computed and its CONCLUSION -- that this Z_3 is electric charge --",
 "is the single remaining reading.  ** That is a far better position than a stack of results",
 "resting on an unshown antecedent, and it is where the effort should now go. **",
]:
    print("  " + s)

# --- r2376+c54.161 : pin the claim, so the receipt can fail -------------------------------
# The claim is the criterion applied: the two equatorial routes (ONE and TWO graze-point
# crossings) transport psi ~ r^(-lambda) by omega^(-lambda) and omega^(-2 lambda), and their
# RATIO is omega^(-lambda) = omega^(triality) -- so the routes agree IFF triality vanishes,
# i.e. iff the field is colourless.  Every value below is one this receipt prints.
assert sp.simplify(facs["the short way"] - sp.exp(-2*sp.pi*sp.I*lam/3)) == 0, \
    "the one-crossing route transports by omega^(-lambda)"
assert sp.simplify(facs["the long way"] - sp.exp(-4*sp.pi*sp.I*lam/3)) == 0, \
    "the two-crossing route transports by omega^(-2 lambda)"
assert sp.simplify(ratio - w**(-lam)) == 0, \
    "the two routes differ by exactly ONE crossing: the ratio is omega^(-lambda)"
# and that ratio is omega^(triality), which is the identification the receipt turns on
for m in (1, 2, 0):
    assert sp.simplify(w**(-m) - w**((-m) % 3)) == 0, \
        f"the route factor for lambda = {m} mod 3 equals omega^(triality)"
# route-independence sorts EXACTLY the colourless class, and nothing else
_indep = [m for m in (1, 2, 0) if sp.simplify(w**(-m) - 1) == 0]
assert _indep == [0], "only lambda = 0 mod 3 is route-INDEPENDENT -- the lepton class alone"
assert len([m for m in range(3) if sp.simplify(w**(-m) - 1) != 0]) == 2, \
    "exactly two of the three residues are route-labelled -- the two coloured classes"
# the printed table's own values: omega^(-1) and omega^(-2) are the primitive cube roots
assert sp.simplify(sp.expand_complex(w**(-1)) - (sp.Rational(-1, 2) - sp.sqrt(3)*sp.I/2)) == 0, \
    "the printed factor at lambda = 1 mod 3 is -1/2 - sqrt(3) I / 2"
assert sp.simplify(sp.expand_complex(w**(-2)) - (sp.Rational(-1, 2) + sp.sqrt(3)*sp.I/2)) == 0, \
    "the printed factor at lambda = 2 mod 3 is -1/2 + sqrt(3) I / 2"
# CLOSURE, read backward: a combination is single-valued iff its trialities sum to 0 mod 3.
# A lone coloured constituent is not; a triality-neutral triple is -- colour singlet-ness.
assert sp.simplify(w**(-(1 + 2 + 3)) - 1) == 0, \
    "a triality-neutral combination (1 + 2 + 3) is single-valued on the base"
assert sp.simplify(w**(-(1 + 1)) - 1) != 0, \
    "a combination of total triality 2 is NOT a field on the manifold"
