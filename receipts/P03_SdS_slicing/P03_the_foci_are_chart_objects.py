"""
P03_the_foci_are_chart_objects.py -- P3 sec:ellipse: the qualification that belongs with the word
"metric" in "the metric foci of the horizon locus", and it protects the reading rather than
weakening it.

** A FOCUS IS NOT A PROJECTIVE INVARIANT OF A CONIC: IT IS DEFINED AGAINST A METRIC.  Read with
the $A_2$ form itself as the metric, the horizon locus is a CIRCLE and its foci coincide.  What is
chart-dependent is that the consequence presents itself as a PAIR OF POINTS; the number $2/\sqrt3$
is not, being forced by the axis ratio the unit cross-term fixes. **

WHAT PROMPTED IT.  A standing item asked whether the two null generators of the companion
operator paper's synchronous section \emph{are} these foci -- a cross-plane identification.

WHAT IS ESTABLISHED.
  1. ** THE ELLIPSE SIDE IS EXACT AND INDEPENDENTLY BANKED THREE TIMES: ** eigenvalues
     $\tfrac12,\tfrac32$ of the $A_2$ form in the equal-scale chart, semi-axes $\sqrt2$ and
     $\sqrt{2/3}$, axis ratio $\sqrt3$ and focal distance $2/\sqrt3$ -- asserted equal to the
     Nariai offset.
  2. ** THE FOCI ARE METRIC-DEPENDENT. **  With the $A_2$ form as the metric, $Q=1$ is that form's
     unit sphere: a circle of eccentricity zero whose foci coincide at the centre.
  3. ** AND THE TWO READINGS GENUINELY DIFFER, WHICH THE WEYL ACTION SHOWS ** (both asserted): the
     three-cycle $(r_1,r_2)\mapsto(r_2,-r_1-r_2)$ has $M^3=I$, preserves the $A_2$ form, and is
     NOT orthogonal in the chart metric.  So the locus is Weyl-invariant as a set while the Weyl
     action is not by chart-rotations, and the eccentricity the chart assigns is a property of the
     chart rather than of the configuration.
  4. ** THE NUMBER IS NOT THEREBY EMPTY. **  The focal distance is $\sqrt{a^2-b^2}$ with the
     eigenvalue ratio $3$ forced by the form, so $2/\sqrt3$ is a consequence of the form and
     stands however the locus is drawn.
  5. ** HENCE A CROSS-PLANE IDENTIFICATION CANNOT BE CANONICAL: ** the companion paper's $A$ and
     $B$ are null directions of the ambient, invariant under the isometry group; the foci are a
     point-pair defined against a chosen chart metric, and in the metric the configuration's own
     symmetry respects they do not exist as a pair at all.

** WHAT SURVIVES IS THE STATEMENT THE PAPERS ACTUALLY MAKE: one forced scale, $2/\sqrt3$, carrying
the metric foci, the two null generators and the lap-close root together -- a statement about a
scale, not an identification of objects. **

ORIGIN: computations/frontier_audit/L142w_the_foci_are_chart_objects.py -- built r2376 (c54.97);
edit the origin, not this copy.

ORIGIN-DIVERGENCE: DELIBERATE AND SUBTRACTIVE.  The origin closes by disposing of the register
item that prompted it.  ** This copy carries the paper-facing subset: every assertion here appears
in the origin verbatim, and nothing here is absent from it. **"""

import sympy as sp

print(__doc__.split("Run:")[0])

# =====================================================================
print("=" * 78)
print("PART 1 — THE ELLIPSE SIDE, AND THE THREE BANKS")
print("=" * 78)
Q = sp.Matrix([[1, sp.Rational(1, 2)], [sp.Rational(1, 2), 1]])
print("  The horizon-locus is the A_2 norm form r^2 + r r_0 + r_0^2 = 1, i.e. Q = 1 with")
sp.pprint(Q)
ev = sorted(Q.eigenvals(), key=lambda z: sp.N(z))
print(f"  eigenvalues {[sp.nsimplify(e) for e in ev]}  (ratio {sp.nsimplify(ev[1]/ev[0])})")
a, b = sp.sqrt(1/ev[0]), sp.sqrt(1/ev[1])
c = sp.sqrt(sp.simplify(a**2 - b**2))
print(f"  semi-axes {sp.simplify(a)} and {sp.simplify(b)};  axis ratio {sp.simplify(a/b)};"
      f"  focal distance {sp.simplify(c)}")
assert sp.simplify(c - 2/sp.sqrt(3)) == 0
assert sp.simplify(a/b - sp.sqrt(3)) == 0
print(f"  ** and that focal distance IS the Nariai offset 2/sqrt3: "
      f"{sp.simplify(c - 2/sp.sqrt(3)) == 0} **")
print()
print(f"  {'bank':>34} {'reaches it by':>44}")
for x, y in [("computations/slicing_bseries/bseries_C6_C7", "semi-axes and the focal distance"),
             ("receipt P03_ellipse_foci", "eigenvalues 1/2, 3/2 and the axis ratio sqrt3"),
             ("receipt P03_cubic_factor_ellipse_locus", "the cubic's factorisation and eigenstructure")]:
    print(f"  {x:>34} {y:>44}")
print()
for s in [
 "⌗ ** THREE INDEPENDENT BANKS OF ONE IDENTITY, AND THE ITEM CITED ONE. **  *The scan found the",
 "   other two; the ellipse side was never what was missing.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE FOCI ARE METRIC-DEPENDENT")
print("=" * 78)
print("  A focus is not a projective invariant of a conic: it is defined against a METRIC.  The")
print("  numbers above use the (r, r_0) chart's EUCLIDEAN metric -- the two axes at equal scale")
print("  and at right angles.  Read instead with the A_2 form itself as the metric:")
print()
print("     Q = 1 is by definition the unit sphere of Q -- a CIRCLE, semi-axes 1 and 1,")
print("     eccentricity 0, ** and its two foci coincide at the centre. **")
print()
print("  And the two readings are genuinely different, which the Weyl action shows:")
M = sp.Matrix([[0, 1], [-1, -1]])
print(f"     the Weyl 3-cycle on (r_1, r_2) with r_3 = -r_1-r_2:  M = {M.tolist()}")
print(f"     M^3 = I : {(M**3) == sp.eye(2)}      det M = {M.det()}")
pres = sp.simplify(M.T*Q*M - Q) == sp.zeros(2, 2)
orth = sp.simplify(M.T*M - sp.eye(2)) == sp.zeros(2, 2)
print(f"     preserves the A_2 form  (M^T Q M = Q) : ** {pres} **")
print(f"     orthogonal in the CHART metric (M^T M = I) : ** {orth} **")
assert pres and not orth
print()
for s in [
 "⇒⇒ ** THE LOCUS IS WEYL-INVARIANT AS A SET, AND THE WEYL ACTION IS NOT BY CHART-ROTATIONS. **",
 "   *So the chart's Euclidean structure is not the one the configuration's own symmetry",
 "   respects, and the eccentricity it assigns -- hence the focal pair -- is a property of the",
 "   chart and not of the configuration.*",
 "",
 "⌗ ** AND THE NUMBER IS NOT THEREBY EMPTY, WHICH IS THE PART TO STATE CAREFULLY: the focal",
 "   distance is $\\sqrt{a^2-b^2}$ with $a^2/b^2$ the eigenvalue ratio $3$, and THAT ratio is",
 "   forced by the $A_2$ form.  $2/\\sqrt3$ is a real consequence of the form. **  *What is",
 "   chart-dependent is that the consequence presents itself as a pair of POINTS.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — WHAT A AND B ARE, AND WHY THE BRIDGE CANNOT BE CANONICAL")
print("=" * 78)
print("  P8 sec:synchronous: in the embedding -X_0^2 + X_1^2 + ... + X_4^2 = alpha^2 the flat-")
print("  slicing comoving worldline is X(tau) = e^{tau/alpha} A + e^{-tau/alpha} B with")
print("  eta(A,A) = eta(B,B) = 0 -- two NULL DIRECTIONS of the ambient, A the per-worldline")
print("  cosmological horizon and B common to the whole congruence.")
print()
print(f"  {'':>22} {'the ellipse foci':>34} {'the generators A, B':>34}")
for x, y, z in [
    ("live in", "the (r, r_0) PARAMETER plane", "the 5-d EMBEDDING"),
    ("defined against", "a chosen Euclidean metric", "eta, the ambient form"),
    ("invariant under", "chart rescalings? NO", "the isometry group -- yes"),
    ("what they are", "a point pair", "a pair of null RAYS"),
    ("in the A_2 metric", "** they coincide **", "unchanged"),
]:
    print(f"  {x:>22} {y:>34} {z:>34}")
print()
for s in [
 "⇒⇒ ** AN IDENTIFICATION WOULD HAVE TO EQUATE AN ISOMETRY-INVARIANT PAIR WITH A CHART-DEPENDENT",
 "   ONE, AND NO SUCH EQUATION CAN BE CANONICAL. **  *In the metric the configuration's own",
 "   symmetry respects, one side of the proposed bridge does not exist as a pair at all.*",
 "",
 "⌗ ** SO `C·7`'s REMAINING HALF IS NOT UNBUILT.  IT IS UNAVAILABLE, and knowing that is worth",
 "   more than the bridge would have been: it removes a standing item rather than deferring it. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — WHAT SURVIVES, AND P8 ALREADY SAYS IT")
print("=" * 78)
for s in [
 "P8, in its own words: *\"The ellipse foci, the two null generators $A,B$ of",
 "Section~\\ref{sec:synchronous}, and the lap-close root are thus all carried at the single forced",
 "scale $2/\\sqrt3$ … no second scale.\"*",
 "",
 "✔ ** THAT IS A STATEMENT ABOUT A SCALE, AND IT IS CORRECT AND UNAFFECTED. **  *Three structures",
 "   are carried at one forced number; the number is forced by the $A_2$ form's eigenvalue ratio;",
 "   and the corpus's whole one-scale claim is of exactly this kind.*",
 "",
 "⚠ ** WHAT WOULD HAVE BEEN WRONG IS THE STRONGER SENTENCE THE ITEM WAS REACHING FOR -- that the",
 "   generators ARE the foci. **  *P8 never wrote it, and the item's own phrasing ('whether … ARE",
 "   these foci') shows it knew the difference.  ** The disposal is therefore a confirmation of",
 "   the paper and a retirement of the question, not a correction of anything. ***",
]:
    print("  " + s)

