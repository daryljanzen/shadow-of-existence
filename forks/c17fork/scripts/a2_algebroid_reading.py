import sympy as sp
print("="*70); print("c17fork_4 / bite (D): S3 in the algebroid (P10 at source)"); print("="*70)
r, M, alpha, Lam = sp.symbols('r M alpha Lambda', positive=True)

# [D1] P10's horizon cubic (general alpha) and its discriminant vs fork_2's Delta (alpha=1)
cubicP10 = r**3 - alpha**2*r + 2*M*alpha**2
disc_general = sp.discriminant(cubicP10, r)
print("\n[D1] P10 cubic r^3 - alpha^2 r + 2 M alpha^2 ; discriminant =", sp.factor(disc_general))
print("     at alpha=1:", sp.expand(disc_general.subs(alpha,1)), " == fork_2's Delta=4-108M^2 :",
      sp.simplify(disc_general.subs(alpha,1)-(4-108*M**2))==0)
# vanishes at the Nariai locus
nariai = sp.solve(sp.Eq(disc_general,0), M)
print("     discriminant=0 at M=", nariai, " ; with alpha^2=3/Lambda this is Lambda M^2=1/9 (Nariai):",
      sp.simplify((sp.Rational(1,27)*alpha**2).subs(alpha**2,3/Lam)*Lam - sp.Rational(1,9))==0)

print("""
[D2] GROUNDED reading off P10 (sec:discrete + sec:strata), consistent with fork_1-3:
 - P10 already places the fork's object: S3 ~= D3 is the discrete skeleton INSIDE so(5,1),
   permuting the three horizon roots (the A2 root configuration, roots sum to zero); the
   root-permutation transposition's FIXED POINT is the Nariai seam (two roots collide,
   discriminant 0). That is EXACTLY fork_1 (A2 triplet) + fork_2 (Delta=0 = Nariai) +
   fork_3 (the involution f(r0) on the cut, fixed at Nariai). The fork ADDS the explicit
   slicing-operator realization (the sky-angle cover, triple-angle, deck group); P10 states
   it abstractly. Agreement and sharpening, not a new claim.
 - THE TIE (new, grounded): P10 sec:strata computes the algebroid CONNECTION (the structure-
   function leak [m,m]->m) to vanish at exactly TWO symmetric strata: Type O (de Sitter,
   so(4,1)) and Nariai (SO(2,1)xSO(3)). The S3 root-permutation's fixed point is Nariai.
   => the discrete S3-cover's BRANCH POINT coincides with a symmetric stratum where the
   continuous algebroid connection VANISHES. The discrete and continuous faces of the
   algebroid meet at Nariai: branch point of the deck group = zero of the connection.
""")
print("="*70)
print("THE BOUNDARY P10 SETS (do-not-assert, honored): P10 lists THREE DISTINCT discrete")
print("involutions, 'different involutions, not one,' each anchored at a stratum --")
print("  (1) root-permutation  (fixed pt Nariai)        [= the fork's S3]")
print("  (2) null<->timelike reassignment (cosmogenesis horizon)")
print("  (3) Riemannian<->Lorentzian signature flip (the seam)")
print("-- and states: 'We make no claim that these unify into a single discrete action.'")
print("The fork's S3 is ONLY (1). Whether (1),(2),(3) assemble into one discrete structure")
print("is P10's explicit do-not-assert AND the face-19 flavor-match spot (fusing distinct")
print("involutions by their shared signature-flip flavor = the exact C7 trap). NOT forced here.")
print("="*70)
