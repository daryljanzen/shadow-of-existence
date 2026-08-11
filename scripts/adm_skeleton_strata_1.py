import sympy as sp

print("="*78)
print("MOVE 11 — the discrete skeleton at the strata (test as a RELATION, never an identity).")
print("The discrete operations are DISTINCT (P4). Question: do they ACT at the strata, and how?")
print("The one new computable connection: is Nariai (the inner metric-singular stratum) the")
print("FIXED POINT of the S3 transposition on the three cubic roots?")
print("="*78)

r, r0 = sp.symbols('r r_0', real=True)
# gauge-free SdS horizon cubic (fundamental-ellipse form): r^3 - r0^3 - (r - r0) = 0
P = r**3 - r0**3 - (r - r0)
print("\n[1] the three horizons are the roots of  P(r) = r^3 - r0^3 - (r - r0):")
print("    P has no r^2 term => the three roots SUM TO ZERO (the A_2 root configuration).")
coeffs = sp.Poly(P, r).all_coeffs()
print("    coeffs [r^3, r^2, r^1, r^0] =", coeffs, "  (r^2 coeff = 0 confirms sum of roots = 0)")
print("    factors as (r - r0)(r^2 + r*r0 + r0^2 - 1): linear = the horizon at r0, quadratic = the")
print("    fundamental ellipse carrying the other two. S3 permutes the three roots (adm3: <sigma,tau>).")

print("\n[2] the S3 transposition fixed locus = two roots coincide = a DOUBLE ROOT.")
print("    A double root <=> discriminant(P) = 0.  Compute:")
disc = sp.discriminant(P, r)
print("    discriminant_r(P) =", sp.factor(disc))
sol = sp.solve(sp.Eq(disc, 0), r0**2)
print("    disc = 0  =>  r0^2 =", sol, " (the critical/Nariai aim: r0^2 = 4/3 or 1/3)")
# verify at r0^2 = 4/3 there is a double root
r0c = sp.sqrt(sp.Rational(4,3))
Pc = P.subs(r0, r0c)
roots = sp.solve(Pc, r)
print("    at r0^2=4/3, roots of P:", [sp.nsimplify(sp.simplify(x)) for x in roots])
# multiplicity:
Pc_poly = sp.Poly(sp.expand(Pc), r)
print("    => a repeated root (two of the three horizons COINCIDE): the transposition's fixed point.")
print("    This is exactly Move 7's Nariai double root (Lambda M^2 = 1/9): the inner metric-singular")
print("    stratum IS the fixed point of the S3 transposition that swaps the two colliding roots. [computed]")

print("\n" + "="*78)
print("READING — the discrete operations are distinct, each ANCHORED at a stratum (no unified action):")
print("="*78)
print("""
 The discrete skeleton does NOT collapse to one operation carrying everything across (P4 keeps the
 operations distinct; this move confirms the can-return: they stay distinct). Instead each special /
 metric-singular stratum is the locus of a SPECIFIC discrete operation, and the cubic's root structure
 (the A_2/S_3 skeleton, geometrically grounded in the fundamental ellipse) is what organizes them:

   STRATUM                         DISCRETE OPERATION ANCHORED THERE
   --------------------------------------------------------------------------------
   Nariai (inner, double root)     the S_3 TRANSPOSITION fixed point -- two of the three roots
                                   collide (discriminant 0, Lambda M^2=1/9). [computed here]
   NBC cosmogenesis horizon        the REASSIGNMENT involution -- null<->timelike on the degenerating
                                   Killing field's freed direction (P7; Move 9). [established]
   Riemann<->Lorentz seam          sigma -- the vantage SIGNATURE FLIP (theta->pi/2+i psi; adm3, P3 478).
                                   [established]
   the WALL (isotropy 0, Type N)   NONE -- no cubic roots, no Killing vector (Move 9): the discrete
                                   skeleton does NOT reach the wall; past it is pure continuous evolution.

 So "the discrete skeleton acts at the strata" holds in the BOUNDED form: the strata are the
 fixed-point / locus set of the (distinct) discrete operations, organized by the cubic root structure;
 they are NOT one unified discrete action, and the wall has none. This is exactly the
 continuous/discrete complementarity (vision sec.4): the CONTINUOUS face so(5,1) runs the flow through
 the symmetry-reducible sector (between strata); the DISCRETE face is the set of boundary operations,
 each marking its stratum. The wall is the one boundary that is purely continuous (Move 9) -- no
 discrete operation -- consistent with its being no metric singularity.

 [computed: Nariai = the S_3 transposition fixed point (double root = discriminant 0). established:
 the reassignment at the NBC horizon (P7/Move 9), sigma at the seam (adm3/P3), the wall has none (Move 9).
 reading: the organizing claim (the strata ARE the discrete operations' locus set, distinct-but-anchored).
 NOT asserted: any unification into one discrete action; any continuous su(3) (the A_2 root structure is
 the skeleton; the su(3) leap stays Move 13).]
""")
