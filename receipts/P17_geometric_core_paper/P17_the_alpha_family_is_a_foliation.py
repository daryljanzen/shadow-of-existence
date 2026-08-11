"""
P17_the_alpha_family_is_a_foliation.py -- p0 (geometric core), the substrate ontology and the
c--Lambda null-ruling gauge: the alpha-family is a foliation of the ambient by the level sets of
one quadratic form, with the LIGHT CONE as its singular member -- and the confocal orthogonality
theorem, which a standing lead expected to apply, is VACUOUS here for a structural reason.

WHAT PROMPTED IT.  A lead observed that the alpha-dilation is a CONFOCAL family and that confocal
quadrics meet ORTHOGONALLY, and registered that the corpus has never used the theorem.

WHAT IS ESTABLISHED.
  1. THE PREMISE IS CORRECT.  In the EQUILATERAL case -- which is what this substrate is, "the
     equilateral pseudo-sphere of sole scale alpha" -- the confocal family IS the dilation
     family: the members are the level sets of one quadratic form, indexed by the constant.
  2. ** BUT THE CLASSICAL THEOREM IS NOT "CONFOCAL QUADRICS ARE ORTHOGONAL" FULL STOP. **  It is:
     through a generic point pass THREE members of a confocal family, one of each type, and
     those meet pairwise orthogonally.  Clearing denominators, the confocal equation is CUBIC in
     the parameter generically and LINEAR in the equilateral case -- asserted -- so ** exactly
     one member passes through any point of the alpha-family, and there is no second member for
     it to be orthogonal TO.  The hypothesis fails, not the conclusion. **
  3. The same fact without machinery: a point assigns ONE value to the quadratic form, so
     distinct-alpha substrates are DISJOINT and cannot meet at any angle.
  4. ** THE DEGENERATION, NAMED: equilateral is exactly the confocal family's degenerate case.
     As the semi-axes come together the cubic loses two roots, the three types collapse, and the
     triply-orthogonal coordinate system collapses with them.  So the theorem went unused for
     the best possible reason -- this substrate sits at the one point of the confocal moduli
     space where it has no content. **
  5. ** WHAT SURVIVES IS BETTER THAN THE THEOREM WOULD HAVE BEEN.  The family is a foliation of
     the ambient by level sets of one function: de Sitter above zero, THE LIGHT CONE at zero,
     the two-sheet hyperboloid below.  Different-alpha substrates NEST, do not meet, and share
     ONE asymptote -- which is the family's own degenerate member. **
  6. ** AND THAT IS A REASON FOR THE c--Lambda NULL-RULING GAUGE'S alpha-INDEPENDENCE, from the
     family rather than from the gauge: the null structure is carried by the one leaf common to
     the whole family, so it cannot depend on which leaf one stands on. **  This paper already
     calls the cone "the locked asymptote of the equilateral pseudo-sphere of sole scale alpha"
     without connecting it to the family it belongs to.

** AND ONE ROUTING THE LEAD DID NOT ASK FOR: the map between members is a DILATION, which is
conformal and not an isometry, so the alpha-family is a CONFORMAL ORBIT and belongs in the
conformal ledger rather than in the quadric-geometry file where it was left.  An item filed
under the machinery someone first reached for rather than the machinery that fits it. **

ORIGIN: computations/baryon_edge/L099w_confocal_orthogonality.py -- built r2376 (c54.72); edit
the origin, not this copy."""
import sympy as sp

print(__doc__.split("Run:")[0])

al, lam = sp.symbols('alpha lambda', real=True)
a1, a2, a3 = sp.symbols('a_1 a_2 a_3', positive=True)
x, y, z = sp.symbols('x y z', real=True)

# =====================================================================
print("=" * 78)
print("PART 1 — IS THE ALPHA-FAMILY CONFOCAL?")
print("=" * 78)
print("  The general confocal family of central quadrics, in three dimensions for legibility:")
print()
conf = x**2/(a1 + lam) + y**2/(a2 + lam) + z**2/(a3 + lam) - 1
print(f"     {sp.simplify(conf)} = 0,  one member per lambda")
print()
print("  Set all the semi-axis parameters equal -- the EQUILATERAL case, which is what the")
print("  substrate is (P3: 'the equilateral pseudo-sphere of sole scale alpha'):")
eq = conf.subs({a2: a1, a3: a1})
print(f"     {sp.simplify(eq)} = 0")
R2 = sp.Symbol("R2")
sol = sp.solve(sp.Eq(sp.numer(sp.together(eq)).subs(x**2 + y**2 + z**2, R2), 0), R2)
print(f"     ⇒ x^2 + y^2 + z^2 = {sol[0]}   -- a sphere of squared radius a_1 + lambda")
print()
for s in [
 "** SO `L-24`'s PREMISE IS CORRECT: in the equilateral case the confocal family IS the",
 "   dilation family -- the members are the level sets of one quadratic form, indexed by the",
 "   constant. **  Nothing is wrong with the observation.",
 "",
 "⌗ *And in Lorentzian signature the same holds with the constant taking either sign, so the",
 "family is $-X_0^2+\\sum X_i^2 = c$ for $c \\in \\mathbb{R}$: de Sitter above zero, the light cone",
 "at zero, the two-sheet hyperboloid below.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — HOW MANY MEMBERS PASS THROUGH A POINT?")
print("=" * 78)
print("  ** The classical theorem is not 'confocal quadrics are orthogonal' full stop.  It is:")
print("     through a generic point pass THREE members of a confocal family, one of each TYPE,")
print("     and THOSE meet pairwise orthogonally. **  So the count matters.")
print()
print("  GENERIC CASE -- distinct semi-axes.  Clearing denominators at a fixed point gives a")
print("  polynomial in lambda; its degree is the number of members through that point:")
num = sp.simplify(sp.numer(sp.together(conf)))
deg = sp.degree(sp.expand(num), lam)
print(f"     degree in lambda = {deg}   ⇒ ** {deg} members through a generic point ** (the classical three)")
assert deg == 3
print()
print("  EQUILATERAL CASE -- all semi-axes equal:")
num_e = sp.simplify(sp.numer(sp.together(eq)))
deg_e = sp.degree(sp.expand(num_e), lam)
print(f"     degree in lambda = {deg_e}   ⇒ ** {deg_e} member through ANY point **")
assert deg_e == 1
print()
for s in [
 "⇒ ** THROUGH EACH POINT PASSES EXACTLY ONE MEMBER OF THE ALPHA-FAMILY.  There is no second",
 "   member for it to be orthogonal TO. **  The theorem's hypothesis fails, not its conclusion.",
 "",
 "⌗ ** AND THE SAME FACT SEEN WITHOUT ANY MACHINERY: distinct members are disjoint. **  A point",
 "   assigns ONE value to the quadratic form, so it lies on the level set of that value and on",
 "   no other.  ** Two substrates of different $\\alpha$ never meet, so they cannot meet at any",
 "   angle. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE DEGENERATION, NAMED")
print("=" * 78)
for s in [
 "** THE EQUILATERAL CASE IS EXACTLY THE DEGENERATE CASE OF THE CONFOCAL FAMILY. **  As the",
 "semi-axes are brought together the cubic in $\\lambda$ loses two roots -- the three types",
 "(ellipsoid, one-sheet, two-sheet) collapse -- and the triply-orthogonal coordinate system the",
 "theorem describes collapses with them.",
 "",
 "⌗ ** SO THE CORPUS HAS NOT USED THE THEOREM FOR THE BEST POSSIBLE REASON: its substrate sits at",
 "   the one point of the confocal moduli space where the theorem has no content. **  `L-99`",
 "   asked what the orthogonality means for the $\\alpha$-family.  ** It means nothing, and that",
 "   it means nothing is forced by the same equilateral property the whole construction rests",
 "   on. **",
 "",
 "⚠ *This is a genuine negative and should not be dressed up.  ** But it is a negative with a",
 "   reason attached, and the reason is the substrate's defining property rather than an",
 "   accident -- which is the difference between 'we never got to it' and 'there is nothing",
 "   there'. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — WHAT SURVIVES: A FOLIATION WITH A SINGULAR LEAF")
print("=" * 78)
Q = -sp.Symbol('X_0')**2 + sum(sp.Symbol(f'X_{i}')**2 for i in range(1, 6))
print(f"  The family is the level sets of one function on R^(5,1):")
print(f"     Q = {Q}")
print()
print(f"  {'value of Q':>14} {'the member':>34} {'normal':>12}")
for v, nm, nrm in [("> 0", "de Sitter, one-sheet (the substrate)", "spacelike"),
                   ("= 0", "THE LIGHT CONE -- the singular leaf", "null"),
                   ("< 0", "two-sheet hyperboloid", "timelike")]:
    print(f"  {v:>14} {nm:>34} {nrm:>12}")
print()
for s in [
 "⇒ ** THE ANSWER TO 'HOW DO DIFFERENT-$\\alpha$ SUBSTRATES SIT AGAINST EACH OTHER' IS: THEY NEST,",
 "   THEY DO NOT MEET, AND THEY SHARE ONE ASYMPTOTE -- THE LIGHT CONE, WHICH IS THE FAMILY'S OWN",
 "   DEGENERATE MEMBER. **",
 "",
 "⌗ *And P3 already says the second half of that without connecting it to the family: 'its light",
 "cone the **locked asymptote** of the equilateral pseudo-sphere of sole scale $\\alpha$.'*",
 "** The cone is not merely an asymptote of the substrate; it is the $Q=0$ member of the very",
 "family the substrate belongs to, and it is the ONLY member every other one approaches. **",
 "",
 "⌗ ** THAT IS WHY THE $c$--$\\Lambda$ NULL-RULING GAUGE IS $\\alpha$-INDEPENDENT: the null structure",
 "   is carried by the one leaf that is common to the whole family, so it cannot depend on which",
 "   leaf you are standing on. **  The corpus asserts the gauge's $\\alpha$-independence; this is",
 "   a reason for it, from the family rather than from the gauge.",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — ONE THING THE SURVEY TURNS UP THAT THE LEAD DID NOT ASK FOR")
print("=" * 78)
for s in [
 "** THE MAP BETWEEN MEMBERS IS A DILATION, AND A DILATION IS NOT AN ISOMETRY OF $\\eta$ -- IT IS",
 "   A CONFORMAL MAP. **  So the $\\alpha$-family is a conformal orbit, and 'how different-$\\alpha$",
 "   substrates sit against each other' is a conformal-geometry question rather than a metric one.",
 "",
 "⌗ ** THE CORPUS HAS A LEDGER FOR EXACTLY THAT (`CONFORMAL_GEOMETRY_LEDGER`, `L-100`) AND THIS",
 "   ITEM WAS NEVER ROUTED TO IT. **  Registered as the routing rather than worked here: the",
 "   $\\alpha$-family belongs in the conformal ledger, where the dilation is one of the generators,",
 "   and not in the quadric-geometry file where `L-24` left it.",
 "",
 "⌗ *That is a small finding and it is the kind this sweep keeps producing: an item filed under",
 "the machinery someone first reached for, rather than under the machinery that fits it.*",
]:
    print("  " + s)
