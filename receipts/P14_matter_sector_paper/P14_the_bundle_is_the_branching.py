"""
P14_the_bundle_is_the_branching.py -- P14 sec:openquestions ("what does the operator act on,
and what fixes it?"): every bundle on P14's own candidate list is eliminated, and the object
that meets the requirement is not a bundle of the substrate at all but the PUSHFORWARD of the
mode bundle from the wall's three-sheeted cover.

THE QUESTION, IN P14's WORDS.  "The substrate is not short of bundles: the tangent bundle of
the five-dimensional embedding space, the spinor bundles it carries, the normal bundle of the
wall itself, and the two ruling bundles."  Three of the sector's standing gaps turned out to be
this one question -- an algebra with no module, a quantised label with no connection, a mode
with no rank.

WHAT IS ESTABLISHED.
  1. THE OBSTRUCTION THAT DECIDES THE LIST, and it was never written down.  su(3) requires a
     COMPLEX rank-3 module.  A REAL bundle's complexification carries a parallel conjugation,
     so its holonomy commutes with conjugation and lands in the real form: for rank 3 that is
     SO(3), of dimension 3, and there is no room for su(3)'s eight.  Verified by imposing
     conj(X) = X on a general element of su(3): five of the eight parameters die and what
     survives is exactly the real antisymmetric matrices.
  2. ** THE CANDIDATE LIST IS ELIMINATED ENTIRELY, each member by a computed reason. **  The
     embedding tangent bundle is real of signature (5,1) and admits NO compatible complex
     structure, since an eta-compatible J splits the space into definite eta-orthogonal planes
     span{x, Jx} and therefore forces both signature blocks EVEN -- 5 and 1 are odd.  The
     spinor bundle has rank 4.  The ruling bundles are LINES, rank 1.  The wall's normal bundle
     has the right rank and is killed by (1).
  3. ** AND (2) CORRECTS L-115, WHICH ELIMINATED THE SAME NORMAL BUNDLE FOR A REASON THAT DOES
     NOT HOLD. **  L-115 argued it "splits 2+1, both summands gradings the operator already
     uses".  That split is only SO(2)-covariant: under the FULL transverse SO(3) whose
     fixed-point set the equatorial section is, the normal bundle is the vector representation
     and is IRREDUCIBLE.  The conclusion stands; the argument is replaced by reality, which is
     group-independent.  ** A right answer resting on a wrong argument is a defect, because the
     argument is what gets reused. **
  4. THE PATTERN IS THE FINDING.  Every object on the list is built from the substrate's
     AMBIENT geometry, and ambient geometry is real.  ** The list could not have contained the
     answer, and the question was never "which real bundle" but "where is the complex
     structure". **
  5. ** WHERE IT IS: THE BRANCH POINT. **  Near the wall r^3 = (9/2) M l^2, so r is a cube root
     and a crossing sends r -> omega r; the corpus's own turnaround figure is drawn on a plane
     of COMPLEX values.  The candidate is E = pi_*(mode bundle), the pushforward from the
     three-sheeted cover to the base: complex because the cover is, of rank the order of the
     deck group, and flat with holonomy the sheet monodromy P.
  6. THE BUNDLE, COMPUTED.  P^3 = I, det P = +1 (so P lies in SU(3)), P unitary.  Rank 3,
     complex, FLAT, holonomy Z_3.  ** Its eigenlines ARE the triality grading, and not up to a
     convention: the deck map is fixed by r -> omega r, the action on sections is PULLBACK, so
     the direction of the shift is forced, and the monodromy eigenvalue on psi ~ r^(-lambda)
     reproduces P14_mode_monodromy_at_the_wall's omega^(-lambda) for every lambda -- asserted
     column by column, so the run fails rather than prints if they part. **
     ** lambda = 0 mod 3 is the deck-INVARIANT line (1,1,1): a colourless state is the trivial
     summand of the regular representation, which is L-72's single-valuedness and L-74's
     point-labelling read as a SUBSPACE. **
  7. ** THE GAP IS EXACTLY ONE GENERATOR WIDE, AND THE COMPUTATION SAYS SO PRECISELY. **  With
     the clock Q = diag(1, omega, omega^2) adjoined, QP = omega PQ, the commutant of <P,Q> is
     the scalars (so it acts IRREDUCIBLY on C^3), and <P,Q> preserves NO symmetric bilinear
     form (the only solution is B = 0), so it is not conjugate into SO(3) -- the only proper
     connected irreducible subgroup of SU(3).  ** Hence the smallest connected group containing
     both P and Q is SU(3) itself. **

** WHAT IS NOT ESTABLISHED, AND THE CIRCULARITY IS REFUSED EXPLICITLY.  The geometry does not
supply Q.  Q is a relative phase BETWEEN sheets that is not a deck transformation, and the
mode's own sheet phases do not supply it -- those are what make the mode a P-eigenvector, which
is P's eigenbasis restated, not a second operator.  Any claim that su(3) is entailed by the
branching alone would be that circularity. **

THE LEDGER.  SUPPLIED: rank 3, complex, flat, Z_3 holonomy, the triality grading, the singlet
line.  NOT SUPPLIED: the second generator, hence the enlargement Z_3 -> SU(3), hence curvature,
hence STRENGTH -- which is what P14_quantisation_not_strength found independently for electric
charge.  ** Two routes now say the geometry quantises and does not couple. **

** A CORRECTION TO THIS RECEIPT'S OWN FIRST VERSION, RECORDED RATHER THAN QUIETLY FIXED.  At
c54.50 this file used the shift in the wrong direction -- pushing the sheet index instead of
pulling it -- got omega^(+lambda), found that it disagreed with the corpus's triality, and
reported the DISAGREEMENT as an unfixed lap-orientation convention and a bookkeeping hazard for
the winding sums.  The derivation (P14_the_lap_orientation_is_derived) shows there was no
convention: the monodromy of a section is pullback along the deck map, the direction is forced,
and the established result was right.  The alarm is withdrawn.  Every conclusion above is
untouched, because both shifts generate the same Z_3 with the same eigenlines. **

ORIGIN: computations/baryon_edge/L127_the_bundle.py -- built r2376 (c54.50), corrected c54.51;
edit the origin, not this copy."""
import sympy as sp

print(__doc__.split("Run:")[0])

I3 = sp.eye(3)
w = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2          # omega = exp(2 pi i / 3), exact
assert sp.simplify(w**3 - 1) == 0 and sp.simplify(w - 1) != 0

# =====================================================================
print("=" * 78)
print("PART 1 — THE OBSTRUCTION NOBODY WROTE DOWN")
print("=" * 78)

# (a)  the real elements of su(3) form so(3), dim 3, not 8.
a, b, c, d, e, f, g, h = sp.symbols('a b c d e f g h', real=True)
X = sp.Matrix([[sp.I * a, b + sp.I * c, d + sp.I * e],
               [-b + sp.I * c, sp.I * f, g + sp.I * h],
               [-d + sp.I * e, -g + sp.I * h, -sp.I * (a + f)]])
assert sp.simplify(X.H + X) == sp.zeros(3), "X must be anti-hermitian"
assert sp.simplify(sp.trace(X)) == 0, "X must be traceless"
# impose reality  conj(X) = X  ->  every imaginary part vanishes
real_conds = sp.solve([sp.simplify(sp.im(X[i, j])) for i in range(3) for j in range(3)],
                      [a, c, e, f, h], dict=True)
Xr = sp.simplify(X.subs(real_conds[0]))
free = sorted({s for s in Xr.free_symbols}, key=str)
print(f"  su(3) has dimension 8.  Imposing conj(X) = X leaves {len(free)} free parameters: "
      f"{[str(s) for s in free]}")
print(f"  and the surviving matrices are exactly the real ANTISYMMETRIC ones:  "
      f"X^T + X = 0 is {sp.simplify(Xr.T + Xr) == sp.zeros(3)}")
print("  ⇒ { X in su(3) : conj(X) = X } = so(3),  dimension 3.")
print()
for s in [
 "** SO A REAL RANK-3 BUNDLE CANNOT CARRY su(3), AND THE REASON IS STRUCTURAL, NOT ACCIDENTAL. **",
 "If E is a REAL bundle, its complexification E⊗C carries a conjugation c (the real structure),",
 "parallel for any connection induced from E.  Holonomy must commute with c, so it lands in the",
 "real form -- SO(3) for rank 3, dimension 3.  ** There is no room for su(3)'s eight. **",
 "",
 "⌗ AND THE GENERAL FORM OF THE STATEMENT IS THE USEFUL ONE.  A real bundle carries su(3) if and",
 "only if it admits an INVARIANT COMPLEX STRUCTURE and is therefore secretly a complex bundle of",
 "half the rank.  ** So 'which real bundle of the substrate' was the wrong question from the",
 "start.  The question is WHERE THE COMPLEX STRUCTURE IS. **",
]:
    print("  " + s)

# (b) an eta-compatible complex structure forces both signature blocks EVEN
print()
print("  The signature test, which is what decides the ambient candidates:")
x0, x1 = sp.symbols('x0 x1', real=True)
print("    If J^2 = -1 and eta(Jx,Jy) = eta(x,y), then on the plane span{x, Jx}")
print("      eta(Jx,Jx) = eta(x,x)   and   eta(x,Jx) = eta(Jx,J(Jx)) = -eta(Jx,x) = 0,")
print("    so that plane is eta-orthogonal and DEFINITE, of signature (2,0) or (0,2).")
print("    V decomposes into such planes  ⇒  ** both signature blocks are EVEN. **")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE CANDIDATE LIST, ELIMINATED ENTIRELY")
print("=" * 78)
print(f"  {'P14 candidate':>30} {'field':>6} {'rank':>5}  {'verdict'}")
rows = [
    ("embedding tangent bundle", "real", 6,
     "signature (5,1): 5 and 1 are ODD, so NO compatible J.  ELIMINATED."),
    ("substrate spinor bundle", "cplx", 4,
     "rank 4, not 3; and it is the rank the operator already uses.  ELIMINATED (P14)."),
    ("wall's normal bundle", "real", 3,
     "** real rank 3 ⇒ complexified holonomy ⊂ SO(3).  ELIMINATED, and BY REALITY. **"),
    ("the two ruling bundles", "real", 1,
     "a ruling is a LINE: rank 1 each, 2 together.  Below 3.  ELIMINATED on rank."),
]
for nm, fld, rk, v in rows:
    print(f"  {nm:>30} {fld:>6} {rk:>5}  {v}")
print()
for s in [
 "⚠ ** AND THE THIRD ROW IS A CORRECTION TO `L-115`, WHICH ELIMINATED THE SAME BUNDLE FOR A",
 "   REASON THAT DOES NOT HOLD. **  `L-115` argued the rank-3 normal bundle 'splits 2+1 --",
 "   the transverse S^2 and the cut-normal -- both gradings the operator already uses'.",
 "   ** That split is only SO(2)-covariant. **  Under the FULL transverse SO(3), whose fixed-point",
 "   set the equatorial section is, the normal bundle is the vector representation and is",
 "   IRREDUCIBLE; the 2+1 appears only after a cut direction is chosen, which is a choice and not",
 "   a property of the bundle.  ** So `L-115` eliminated the one candidate whose rank was right,",
 "   using an argument that depends on breaking the symmetry that defines the bundle. **",
 "",
 "⌗ The conclusion survives -- the bundle is still eliminated -- but by REALITY, which is",
 "   group-independent and holds whether or not a cut is chosen.  ** A right answer resting on a",
 "   wrong argument is a bug even when the answer stands, because the argument is what gets",
 "   reused. **  Recorded as such.",
 "",
 "⌗ AND THE PATTERN IN THE COLUMN IS THE FINDING.  Three of the four are REAL bundles and one has",
 "the wrong rank.  ** Every object on P14's list is built from the substrate's ambient geometry,",
 "and ambient geometry is real.  The list could not have contained the answer. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — WHERE THE COMPLEX STRUCTURE IS")
print("=" * 78)
for s in [
 "The corpus has exactly one place where a complex structure is not imported but FORCED, and it",
 "has been staring at it since `L-78`: ** the branch point. **  Near the wall the bead's law is",
 "r^3 = (9/2) M l^2, so r is a CUBE ROOT, the base is branched, and a crossing sends r -> omega r.",
 "That is not a real structure with a complex structure laid on top; the cube root is complex or",
 "it is nothing.  ** `fig:turnaround` panel (b) is literally a plane of complex values. **",
 "",
 "⇒ ** THE CANDIDATE: E = pi_*(mode bundle), the PUSHFORWARD of the mode line bundle from the",
 "   three-sheeted cover down to the base. **  Its fibre over a base point is the space of values",
 "   on the three preimages.  It is complex because the cover is; its rank is the order of the",
 "   deck group; and its flat structure is the sheet monodromy.  ** Not on P14's list, and could",
 "   not have been: it is not a bundle OF the substrate, it is a bundle of the BRANCHING. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE BUNDLE, COMPUTED")
print("=" * 78)

# The monodromy of a SECTION is PULLBACK along the deck map D : sheet k -> sheet k+1, so in
# components (D* s)_k = s_{k+1}.  Derived, not chosen -- see L127b_fix_the_orientation.py, which
# corrects c54.50's first version of this file: it used the inverse shift, mislabelled two of the
# three eigenlines, and then reported the resulting disagreement with L-78 as a corpus convention
# gap rather than as its own bug.
P = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])            # sheet shift = pullback along D
print(f"  monodromy of one lap about the branch point = the sheet 3-cycle P:")
print(f"     P^3 = I : {sp.simplify(P**3) == I3}      det P = {sp.det(P)}      "
      f"P unitary : {sp.simplify(P.H * P) == I3}")
print(f"  ⇒ ** rank 3, complex, FLAT, holonomy <P> = Z_3, and P lies in SU(3) (det = +1). **")
print()

ev = P.eigenvects()
print("  eigenstructure — the triality grading:")
for val, mult, vecs in sorted(ev, key=lambda t: sp.arg(sp.N(t[0]))):
    v = sp.simplify(vecs[0].T)
    lab = ("colourless (deck-INVARIANT)" if sp.simplify(val - 1) == 0 else "coloured")
    print(f"     eigenvalue {sp.nsimplify(sp.simplify(val)) !s:>28}   eigenvector {str(v.tolist()[0]):<28} {lab}")

# the mode's own sheet vector: psi ~ r^(-lambda), sheet k sits at omega^k r
lam = sp.symbols('lambda', integer=True)
def omega_power(z):
    """exact discrete log base omega, for z a cube root of unity"""
    for k in range(3):
        if sp.simplify(z - w**k) == 0:
            return k
    raise ValueError("not a cube root of unity")

print(f"     {'lambda':>7} {'sheet vector of psi ~ r^(-lambda)':>44} {'monodromy eig':>14} "
      f"{'L-78 phase':>11} {'triality -L mod 3':>18}")
for L in range(6):
    sheet = sp.Matrix([sp.simplify((w**k)**(-L)) for k in range(3)])
    img = sp.simplify(P * sheet)
    eig = sp.simplify(img[0] / sheet[0])
    assert sp.simplify(img - eig * sheet) == sp.zeros(3, 1), "mode must be a P-eigenvector"
    kP = omega_power(eig)
    tri = (-L) % 3
    # L-78, derived twenty revisions earlier: the mode picks up omega^(-lambda) per crossing
    assert sp.simplify(eig - w**(-L)) == 0, "monodromy must reproduce L-78's phase"
    assert kP == tri, "the monodromy eigenvalue IS the triality"
    print(f"     {L:>7} {str([sp.nsimplify(x) for x in sheet]):>44} "
          f"{'w^' + str(kP):>14} {'w^' + str((-L) % 3):>11} {tri:>18}")
print()
print("  ** AND THE EIGENVALUE IS THE TRIALITY ON THE NOSE, WITH NO CONVENTION INTERPOSED. **")
print("     omega^(-lambda) per crossing is `L-78`'s, derived twenty revisions before this lead, and")
print("     the pushforward's monodromy REPRODUCES IT for every lambda -- asserted above, column by")
print("     column, so the run fails rather than prints if they part.  ** The lap orientation is not")
print("     a free convention: the deck map is fixed by r -> omega r and the action on sections is")
print("     pullback, so the direction of the shift is FORCED. **")
print("  ⚠ (c54.50's first version of this file wrote the shift the other way, disagreed with `L-78`,")
print("     and recorded the ESTABLISHED result as the doubtful one.  Corrected and the false alarm")
print("     withdrawn at c54.51 -- `L127b_fix_the_orientation.py`.)")

print()
for s in [
 "** THE MODE IS AN EIGENVECTOR OF THE MONODROMY AND ITS EIGENVALUE IS ITS TRIALITY. **  Nothing",
 "was fitted: psi ~ r^(-lambda) is c54.25's, the omega-per-crossing is `L-78`'s, triality =",
 "-lambda mod 3 is `L-78`'s, and the eigenvalue falls out of the 3-cycle.",
 "",
 "⌗ ** AND lambda = 0 mod 3 IS THE INVARIANT DIRECTION (1,1,1). **  A colourless mode is the",
 "deck-invariant vector -- the trivial summand of the regular representation -- which is `L-72`'s",
 "single-valuedness and `L-74`'s point-labelling READ AS A SUBSPACE.  ** 'Colour singlet-ness is",
 "single-valuedness' is now a statement about a specific line in a specific rank-3 bundle. **",
 "",
 "⌗ AND THE THREE ASKS OF `L-127` ARE MET IN ONE OBJECT: `L-96` wanted a module for the algebra",
 "(rank 3, complex — here it is); `L-125` wanted a connection for the Z_3 label (flat, holonomy",
 "Z_3 — quantisation with NO strength, which is exactly what `L-125` concluded and could not",
 "derive); P14 wanted the operator's rank (3).",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — THE LEDGER, AND THE GAP IS NOW ONE GENERATOR WIDE")
print("=" * 78)

Q = sp.diag(1, w, w**2)
print(f"  What su(3) would additionally require is a second, NON-COMMUTING unitary on the fibre.")
print(f"  The canonical partner of the shift P is the clock Q = diag(1, w, w^2):")
kQP = next(j for j in range(3) if sp.simplify(Q * P - (w**j) * P * Q) == sp.zeros(3))
print(f"     det Q = {sp.simplify(sp.det(Q))}    Q^3 = I : {sp.simplify(Q**3) == I3}    "
      f"Q P = w^{kQP} P Q : {sp.simplify(Q*P - (w**kQP)*P*Q) == sp.zeros(3)}   "
      f"(non-trivial: w^{kQP} != 1 is {sp.simplify(w**kQP - 1) != 0})")
comm = sp.simplify(P * Q - Q * P)
print(f"     [P,Q] = 0 ? {comm == sp.zeros(3)}   — so <P,Q> is the order-27 Heisenberg group.")

# irreducibility of <P,Q>: only scalars commute with both
m = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'm{i}{j}'))
sol = sp.solve(list(sp.simplify(m * P - P * m)) + list(sp.simplify(m * Q - Q * m)),
               list(m), dict=True)[0]
Mred = sp.simplify(m.subs(sol))
print(f"     commutant of <P,Q> = {Mred.tolist()}  ⇒ SCALARS ⇒ ** <P,Q> acts IRREDUCIBLY on C^3. **")

# does <P,Q> preserve a symmetric bilinear form?  (would put it inside SO(3) < SU(3))
B = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'b{min(i,j)}{max(i,j)}'))
eqs = list(sp.simplify(P.T * B * P - B)) + list(sp.simplify(Q.T * B * Q - B))
bsol = sp.solve(eqs, sorted(B.free_symbols, key=str), dict=True)
Bred = sp.simplify(B.subs(bsol[0])) if bsol else B
print(f"     invariant symmetric bilinear form: {Bred.tolist()}  ⇒ only B = 0,")
print(f"     so <P,Q> is NOT conjugate into SO(3) — and SO(3) is the only proper connected")
print(f"     irreducible subgroup of SU(3).  ** Hence the smallest connected group containing")
print(f"     BOTH P and Q is SU(3) itself. **")
print()
for s in [
 "⌗ ** SO THE WHOLE OF su(3) IS ONE GENERATOR AWAY, AND THE GENERATOR IS NAMED. **  P alone gives",
 "Z_3 and a reducible bundle.  P together with any Q of that kind gives SU(3) with nothing else",
 "added.  ** The gap between 'the corpus has colour's Z_3' and 'the corpus has colour' is exactly",
 "one non-commuting phase, and the computation above says so precisely rather than approximately. **",
 "",
 "⚠ ** AND WHAT THE GEOMETRY DOES NOT YET SUPPLY IS Q, AND I WILL NOT PRETEND OTHERWISE. **  Q is a",
 "RELATIVE PHASE BETWEEN SHEETS that is not itself a deck transformation.  The mode's own sheet",
 "phases do NOT supply it: those make the mode a P-eigenvector (PART 4), which is P's own",
 "eigenbasis restated, not a new operator.  ** Any claim that su(3) is entailed by the branching",
 "alone would be that circularity, and it is refused here. **",
 "",
 "⇒ ** WHERE TO LOOK, AND IT IS SPECIFIC. **  There is not ONE branched cover: there are THREE",
 "walls, each with its own Z_3, and the hinge S_3 PERMUTES them (`lem:twoturnings` keeps this S_3",
 "apart from the turnaround's Z_3, so no collision).  ** A relative phase between the sheets of one",
 "wall, induced by transport around another wall, is exactly the shape Q has -- and it exists only",
 "because there are three walls rather than one. **  That is the next computation and it is well",
 "posed: transport a mode about wall B and read its action on wall A's sheet basis.",
 "",
 "⌗ THE LEDGER, HONESTLY:",
 "     SUPPLIED   rank 3 · complex · flat · Z_3 holonomy · the triality grading · the singlet line",
 "     NOT YET    the second generator, hence the structure group's enlargement Z_3 -> SU(3),",
 "                hence the curvature, hence the STRENGTH -- which is the same thing `L-125` found",
 "                the geometry does not supply for electric charge.  ** Two independent routes now",
 "                say the geometry quantises and does not couple. **",
]:
    print("  " + s)
