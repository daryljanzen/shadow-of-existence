#!/usr/bin/env python3
"""
L-96 — WHAT SUPPLIES THE ADJOINT OF SU(3), GIVEN THE CENTRE IS ALREADY SUPPLIED?

WHY IT MATTERS, IN THE CORPUS'S OWN TERMS.  THE_BASE_RATE, written one turn ago, found that
least-arbitrariness arguments which DELETE an exception succeed and ones which ADD machinery
to explain a number fail, and it scored CR's colour reading as currently ADDING -- "on the
unfavourable side, and should be watched."  It then named the one move that would change
that: "showing the adjoint is ALREADY THERE and was being discarded, rather than supplying
it.  That is not a stylistic preference; it is what the base rate says."

  ** SO THIS IS NOT A FISHING EXPEDITION.  THE CORPUS SET ITSELF A TEST AND THIS IS IT. **

  PART 1  What the corpus actually has, listed before anything is claimed about it.
  PART 2  ** The corpus's own ellipse IS the Killing form on the Cartan.  Computed, not read. **
  PART 3  The four root-system axioms, tested.  Integrality is the one that can fail.
  PART 4  ** THE ANSWER: nothing supplies the adjoint, because the root system ENTAILS it. **
  PART 5  ** AND THE QUESTION WAS MIS-POSED: the centre and the adjoint are ONE datum. **
  PART 6  What is therefore NOT established, stated as sharply as what is.
  PART 7  The base-rate re-score, and the two open questions that turn out to be one.

Run: python3 L96_what_supplies_the_adjoint.py     (sympy)
"""
import itertools
import sympy as sp

print(__doc__.split("Run:")[0])

# =====================================================================
print("=" * 78)
print("PART 1 — WHAT THE CORPUS HAS.  Listed first, so nothing is smuggled in later.")
print("=" * 78)
for s in [
 "① ** THREE HORIZON ROOTS SUMMING TO ZERO. **  The horizon cubic in the construction gauge",
 "   is r^3 - r + 2M = 0 (alpha = 1): no quadratic term, so by Vieta the three roots sum to",
 "   zero.  P02_ring_lambda_limit and P03_cubic_factor_ellipse_locus both record this, and",
 "   both record it as BOOKKEEPING -- a property of a depressed cubic.",
 "② ** THE ROOT-EXCHANGE INVOLUTION sigma, generating S_3. **  P3 sec:cubic: sigma swaps which",
 "   root a hinge designates as its own hole; the three-cycle is the tour of the three hinges;",
 "   the Weyl group S_3 'is the relation among the three vantages'.",
 "③ ** THE OFFSET PARITY R : r_0 -> -r_0. **  The A_2 diagram automorphism, carrying 3 to 3bar,",
 "   mass-odd and charge-even, and gamma^5 on the cut (P14).",
 "④ ** A HEXAD, TWICE OVER. **  The six Nariai members exchanged as 3 + 3bar by R; and the six",
 "   hinge-ends closing into one skew hexagon (P3 fig:skewhex, fig:U3).  P3 calls the relation",
 "   between the two hexads 'a genuine RESONANCE and not an identity' and stops there.",
 "⑤ ** AND A QUADRATIC FORM THE CORPUS DERIVED FOR ITS OWN REASONS. **  P3 prop:factor: the",
 "   cubic factors on the ellipse  r^2 + r r_0 + r_0^2 = 1,  which the corpus already calls",
 "   'the A_2 norm form' -- and whose eigenstructure it computes (eigenvalues 1/2 and 3/2,",
 "   semi-axes sqrt2 and sqrt(2/3), at 45 degrees) without asking what the form IS.",
]:
    print("  " + s)
print()
print("  ⌗ ** THE QUESTION L-96 ASKS IS WHETHER THAT LIST ALREADY CONTAINS AN ADJOINT. **")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE CORPUS'S OWN ELLIPSE IS THE KILLING FORM ON THE CARTAN")
print("=" * 78)
print("  Item ① puts the root triple in the plane  V = { x in R^3 : x1 + x2 + x3 = 0 },")
print("  which is exactly the Cartan subalgebra of su(3) in its standard realisation --")
print("  diagonal traceless matrices.  Parametrise V by the first two entries:")
print()
a, b = sp.symbols('a b', real=True)
x = sp.Matrix([a, b, -a - b])
print(f"      x = {tuple(x)},   sum = {sp.simplify(sum(x))}")
euclid = sp.expand(sum(c**2 for c in x))
corpus = sp.expand(a**2 + a*b + b**2)
print(f"      induced Euclidean norm  |x|^2 = {euclid}")
print(f"      the corpus's A_2 norm form      = {corpus}   (P3 prop:factor, with (r, r_0) = (a, b))")
print(f"      ratio                            = {sp.simplify(euclid/corpus)}")
print()
print("  ** SO THE ELLIPSE P3 FACTORS THE CUBIC ON IS THE UNIT CIRCLE OF THE KILLING FORM")
print("     RESTRICTED TO THE CARTAN SUBALGEBRA OF su(3), UP TO THE FACTOR 2. **")
print("  ⌗ This is an identity, not a resemblance, and the corpus already had both halves:")
print("  it named the form 'the A_2 norm form' and it computed the sum-to-zero by Vieta.")
print("  ** It never multiplied them together. **")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE FOUR AXIOMS, TESTED.  A hexagon is not a root system until it is.")
print("=" * 78)
print("  Items ② and ④ give six objects in V: the differences e_i - e_j (i != j), which are")
print("  the DESIGNATION TRANSITIONS -- 'the step to a neighbouring hinge' -- and whose")
print("  reflections are exactly the corpus's sigma.  Do they form a REDUCED CRYSTALLOGRAPHIC")
print("  ROOT SYSTEM?  ** Integrality is the axiom that can fail, and it is the whole test. **")
print()
E = [sp.Matrix([1 if t == i else (-1 if t == j else 0) for t in range(3)])
     for i in range(3) for j in range(3) if i != j]
def ip(u, v):  # the Killing form on V, i.e. TWICE the corpus's own norm form
    return sp.simplify((u.T*v)[0, 0])
print(f"  {'root':>12} {'in V?':>7} {'(a,a)':>7} {'a as (r,r_0)':>14} {'corpus norm':>12}")
for u in E:
    aa, bb = u[0], u[1]
    print(f"  {str(tuple(u)):>12} {str(sp.simplify(sum(u)) == 0):>7} {str(ip(u, u)):>7} "
          f"{str((aa, bb)):>14} {str(sp.expand(aa**2 + aa*bb + bb**2)):>12}")
print()
lengths = {ip(u, u) for u in E}
print(f"  AXIOM (i)  finite, spans V, excludes 0:  {len(E)} roots, "
      f"rank {sp.Matrix.hstack(*E).rank()}, 0 excluded: {all(any(c != 0 for c in u) for u in E)}")
prop = [(i, j) for i in range(6) for j in range(6)
        if i < j and sp.Matrix.hstack(E[i], E[j]).rank() == 1]
print(f"  AXIOM (ii) REDUCED -- only +-alpha proportional: "
      f"{len(prop)} proportional pairs, all negatives: "
      f"{all(E[i] == -E[j] for i, j in prop)}")
def refl(u, v):   # s_v(u) = u - 2(u,v)/(v,v) v
    return sp.simplify(u - 2*ip(u, v)/ip(v, v)*v)
closed = all(any(refl(u, v) == w for w in E) for u in E for v in E)
print(f"  AXIOM (iii) closed under its own reflections:  {closed}")
cartan_ints = sorted({sp.nsimplify(2*ip(u, v)/ip(v, v)) for u in E for v in E})
allint = all(t.is_Integer for t in cartan_ints)
print(f"  AXIOM (iv) ** INTEGRALITY ** -- <alpha, beta^vee> in Z:  values {cartan_ints}, "
      f"all integers: {allint}")
print()
angs = sorted({sp.nsimplify(sp.deg(sp.acos(ip(u, v)/sp.sqrt(ip(u, u)*ip(v, v)))))
               for u in E for v in E})
print(f"  and the pairwise angles are {angs} degrees -- equal lengths, and NO 90, which is what separates A_2 from A_1 x A_1 and B_2.")
# the Weyl group by CLOSURE, not by two-letter words -- a first pass took products of
# exactly TWO reflections and got 3, which is the rotation subgroup, not the group.
gen = sp.Matrix([1, 2, -3])
W, frontier = {tuple(gen)}, [gen]
while frontier:
    nxt = []
    for pt in frontier:
        for rt in E:
            im = sp.simplify(refl(pt, rt)); key = tuple(im)
            if key not in W:
                W.add(key); nxt.append(im)
    frontier = nxt
print(f"  the reflection group's orbit of a generic point has {len(W)} elements "
      f"(|W(A_2)| = |S_3| = 6): {len(W) == 6}")
print()
onell = [u for u in E if sp.expand(u[0]**2 + u[0]*u[1] + u[1]**2) == 1]
print(f"  ** AND THE 'corpus norm' COLUMN IS THE RESULT, NOT A CHECK: all {len(onell)} roots have")
print("     corpus-norm EXACTLY 1, so ** the six roots of A_2 LIE ON P3's FACTORISATION")
print("     ELLIPSE r^2 + r r_0 + r_0^2 = 1 **.  P3 factors its horizon cubic on a curve")
print("     which is the unit circle of the Killing form, and whose lattice points at unit")
print("     norm ARE the root hexagon.  ** The corpus drew the roots and called the drawing")
print("     a factorisation identity. **")
print()
print("  ⇒ ** ALL FOUR AXIOMS HOLD.  The corpus's hexad, in the corpus's own quadratic form,")
print("     IS A REDUCED IRREDUCIBLE CRYSTALLOGRAPHIC ROOT SYSTEM OF RANK TWO WITH SIX ROOTS. **")
print("  ⌗ And the reduced rank-two systems are classified exhaustively -- A_1 x A_1 (4 roots),")
print("  A_2 (6), B_2 (8), G_2 (12).  ** Six roots leaves exactly one option. **")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE ANSWER.  NOTHING SUPPLIES THE ADJOINT, BECAUSE A_2 ENTAILS IT.")
print("=" * 78)
print("  By the isomorphism and existence theorems for semisimple Lie algebras (Serre), a")
print("  reduced irreducible root system determines a complex simple Lie algebra UNIQUELY up")
print("  to isomorphism, and every such algebra arises this way.  For A_2 that algebra is")
print("  sl(3,C), whose compact real form is su(3).  Its dimension is not an extra datum:")
print()
rank, nroots = 2, len(E)
print(f"      dim g = |Phi| + rank = {nroots} + {rank} = {nroots + rank}")
print("      ** = 8 = the dimension of the ADJOINT of SU(3). **")
print()
print("  ⌗ AND THE TWO SUMMANDS ARE THE CORPUS'S OWN TWO ITEMS, NEITHER OF THEM NEW:")
print("      the 6 root spaces  <-  the HEXAD (item ④), the six designation transitions")
print("      the 2 Cartan dims  <-  the SUM-TO-ZERO PLANE (item ①), which the corpus")
print("                             computes by Vieta and records as bookkeeping")
print()
print("  ** SO THE ADJOINT IS NOT ADDED.  It is what the corpus already wrote down, counted. **")
print("  ⌗ What was being DISCARDED is precisely the two-dimensional piece: the corpus treats")
print("  'the three roots sum to zero' as an accident of a depressed cubic.  It is the Cartan.")

# =====================================================================
print()
print("=" * 78)
print("PART 5 — AND THE QUESTION WAS MIS-POSED: THE CENTRE AND THE ADJOINT ARE ONE DATUM")
print("=" * 78)
print("  L-96 asks what supplies the adjoint GIVEN the centre is already supplied.  That")
print("  phrasing treats them as two gifts.  ** They are computed from the same object. **")
print("  The centre of the simply connected group is the weight lattice modulo the root")
print("  lattice, P/Q, whose order is the determinant of the Cartan matrix:")
print()
al1, al2 = E[0], sp.Matrix([0, 1, -1])
Cmat = sp.Matrix([[sp.nsimplify(2*ip(ai, aj)/ip(aj, aj)) for aj in (al1, al2)]
                  for ai in (al1, al2)])
print("      Cartan matrix =", Cmat.tolist(), "  det =", Cmat.det())
print("      |Z(SU(3))| = |P/Q| = det(Cartan) =", Cmat.det(), "  ** = 3 **")
print()
print("  ** SO THE Z_3 THE CORPUS SUPPLIES FOUR TIMES OVER IS NOT AN INDEPENDENT GIFT: IT IS")
print("     A FUNCTION OF THE ROOT SYSTEM, AND SO IS THE ADJOINT.  You cannot have the centre")
print("     of A_2 without having A_2, and having A_2 you have the eight. **")
print()
print("  ⇒ ** L-96 ANSWERS ITSELF, AND ANSWERS IN THE DELETE DIRECTION. **  The corpus was")
print("  holding two facts -- 'we have a Z_3' and 'we have a hexagon, but only as a")
print("  resonance' -- and treating the adjoint as a third thing still owed.  There is no")
print("  third thing.  ** There is one root system, stated twice and counted once. **")

# =====================================================================
print()
print("=" * 78)
print("PART 6 — WHAT IS *NOT* ESTABLISHED, AT THE SAME VOLUME")
print("=" * 78)
for s in [
 "** A LIE ALGEBRA BEING PRESENT IS NOT A GAUGE SYMMETRY BEING PRESENT, AND NOTHING ABOVE",
 "   CLOSES THAT GAP. **  What PARTS 3-5 establish is that the corpus's own hexad, in the",
 "   corpus's own quadratic form, satisfies the axioms of A_2, and that A_2 determines su(3)",
 "   with its 8 and its Z_3.  That is a statement about a ROOT SYSTEM SITTING IN A PLANE OF",
 "   HORIZON-ROOT TRIPLES.  It is not a statement that anything transforms under it.",
 "",
 "Three things would be needed and none is delivered here:",
 "  (i)   a BUNDLE for the algebra to act on, of the right rank;",
 "  (ii)  a CONNECTION on it, so that the action is gauged rather than global;",
 "  (iii) a reason the fermion content sits in the FUNDAMENTAL rather than anywhere else.",
 "",
 "And the corpus's existing walls stand untouched: su(3) is NOT a subalgebra of so(5,1), so",
 "the isometry route remains closed (P13), and the su(3) the boundary and geometric-core",
 "papers place on the conjugate real form S^5 = SO(6)/SO(5) is reached by the GLOBAL WICK,",
 "a continuation the slicing never performs (P3 sec:seam).  ** Nothing here reopens either. **",
 "",
 "⌗ ONE THING IS SHARPENED RATHER THAN CLOSED, AND IT IS THE USEFUL PART.  P14 states its",
 "own open question in exactly these terms: 'the question the undelivered content amounts to",
 "is a question about the BUNDLE: what does the operator act on, and what fixes it?' -- and",
 "lists the substrate's candidates (the embedding tangent bundle, the spinor bundles, the",
 "wall's normal bundle, the two ruling bundles).  ** That is the same question as (i)-(iii). **",
 "So L-96 and P14's bundle question are ONE QUESTION, and L-96's contribution is to have",
 "removed the OTHER half of what was thought to be owed.",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 7 — THE BASE-RATE RE-SCORE, DONE HONESTLY RATHER THAN FAVOURABLY")
print("=" * 78)
print("  THE_BASE_RATE scored 'colour as the centre' as ONE argument, ADDING.  The right")
print("  correction is not to flip that row but to SPLIT it, because it was two claims:")
print()
print(f"  {'the claim':>34} {'kind':>12} {'status after L-96':>28}")
for c, kind, st in [
    ("the ALGEBRA is present (su(3))", "** DELETES **", "** established here **"),
    ("the algebra ACTS (colour is gauged)", "still ADDS", "open -- the bundle question"),
]:
    print(f"  {c:>34} {kind:>12} {st:>28}")
print()
for s in [
 "** THE FIRST ROW MOVES TO THE FAVOURABLE SIDE OF THE DISCRIMINANT AND THE SECOND DOES NOT. **",
 "The first deletes: it removes the supposition that an adjoint must be supplied, by showing",
 "the corpus had already written it down in two pieces and counted neither.  The second still",
 "adds: it proposes a structure -- a bundle with a connection -- to account for observed",
 "colour, and nothing here supplies one.",
 "",
 "⌗ SO THE HONEST HEADLINE IS NARROWER THAN THE RESULT FEELS, AND IT IS STILL A RESULT:",
 "** the corpus does not owe the adjoint of su(3); it owes the object su(3) acts on. **",
 "That is a smaller debt than the one the base rate flagged, it is a DIFFERENT KIND of debt",
 "(a bundle, not a number), and it is one P14 had already isolated on its own side of the",
 "programme without knowing it was the same debt.",
]:
    print("  " + s)

# --- r2376+c54.159 -----------------------------------------------------------------
# Every axiom test here produced a boolean that was only PRINTED.  Assert them, and pin
# the root-system data the entailment turns on: the Killing form is exactly TWICE the
# corpus's own norm form; six roots of rank two, all of corpus-norm 1 (so they lie ON
# P3's factorisation ellipse); Cartan integers {-2,-1,1,2}; angles 0/60/120/180 with no
# 90; |W| = 6; dim g = 6 + 2 = 8; and det(Cartan) = |Z(SU(3))| = 3.
assert sp.simplify(euclid/corpus - 2) == 0, "the ellipse is NOT the Killing form up to 2"
assert len(E) == 6 and sp.Matrix.hstack(*E).rank() == 2
assert len(prop) == 3 and all(E[i] == -E[j] for i, j in prop)      # reduced
assert closed, "AXIOM (iii): not closed under its own reflections"
assert allint and cartan_ints == [-2, -1, 1, 2], "AXIOM (iv): INTEGRALITY fails"
assert angs == [0, 60, 120, 180], "an angle of 90 would put this in A_1 x A_1 or B_2"
assert len(W) == 6, "the reflection group is not S_3"
assert len(onell) == 6, "not all six roots lie on P3's factorisation ellipse"
assert {ip(u, u) for u in E} == {2}                                # one root length
assert nroots + rank == 8                                          # dim su(3)
assert Cmat.det() == 3                                             # |Z(SU(3))| = |P/Q|
