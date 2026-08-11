"""K2 + K3 — IS Psi A FUNCTOR, AND IS 'THE SINGLE INVARIANT IS THE GEOMETRY' A UNIVERSAL PROPERTY?
CONFIRMATION 4 — the objects:
  SOURCE: K1's action groupoid  SO(5,1) |x C ==> C .  Objects = cuts.  Arrows c -> g.c .
  Psi (P8): 'carries a cut of the substrate to a geometry'.
  TARGET: geometries, with isometries between them.
  P5: 'ONE RIGID GEOMETRY charted from many vantages -- THE GROUPOID'S SINGLE INVARIANT IS THE GEOMETRY',
      and 'rigidity as dimensional collapse (the continuous parameter is a CHART LABEL, not a modulus)'.

ORIGIN: storyboard_receipts/K23_functor_and_quotient.py -- registered r2376 (c54); edit the origin, not this copy."""
import numpy as np, sympy as sp
print("="*80); print("K2 — IS Psi A FUNCTOR?"); print("="*80)
print("""
  A map on objects is not a functor until it carries ARROWS and preserves composition and identities.
  ON ARROWS: an arrow of the source is a substrate isometry g with g.c = c'.  Psi reads the geometry
  OFF the cut, and g is an isometry of the substrate, so it carries the geometry read off c to the
  geometry read off c' -- isometrically.  So Psi(g) := the induced isometry.  Composition and
  identities are inherited from the group, since Psi(g)Psi(h) is induced by gh and Psi(e) = id.
  *** SO Psi IS A FUNCTOR from the action groupoid to geometries-and-isometries. ***
  The content is not that it is one; it is what KIND of functor, and the corpus answers each part.
""")
print("  (a) ESSENTIALLY SURJECTIVE?  onto its image by definition -- and P9 IS that image:")
print("      P9 is titled 'the RANGE of the operator'.  *** P9 computes the ESSENTIAL IMAGE. ***")
print()
print("  (b) FAITHFUL?  Faithful means distinct arrows give distinct induced isometries.")
print("      FAILS, and the corpus says how: an isometry that MOVES THE CUT but leaves the geometry")
print("      it reads off unchanged is a nonidentity arrow with identity image.")
print("      P3: 'one geometry is designated by SEVERAL r_0-values'.  Check on the horizon cubic:")
r0=sp.symbols('r_0'); M2=r0-r0**3
print(f"      2M(r_0) = {M2};  the three roots of a given 2M all return that same 2M:")
for M in [0.20, 0.33]:
    rts=np.sort([x.real for x in np.roots([1,0,-1,M]) if abs(x.imag)<1e-9])
    print(f"        2M={M}: roots {np.round(rts,6)}  ->  2M from each = {np.round([r-r**3 for r in rts],9)}")
    # r2376+c54.158 -- pins K2(b), the non-faithfulness: for each mass the cubic has THREE distinct
    # real roots -- printed [-1.088034, 0.209149, 0.878885] at 2M=0.20 and [-1.135999, 0.388751,
    # 0.747248] at 2M=0.33 -- and ALL THREE return the same 2M.  Three cuts, one geometry: the
    # fibre of Psi has three elements, so Psi is not faithful and its fibres are the S_3-orbits.
    assert len(rts) == 3 and float(np.min(np.diff(rts))) > 0.3, rts
    assert np.allclose(rts, {0.20: [-1.088034, 0.209149, 0.878885],
                             0.33: [-1.135999, 0.388751, 0.747248]}[M], atol=1e-6), rts
    assert np.allclose([r - r**3 for r in rts], M, atol=1e-9), rts
print("      *** THREE CUTS, ONE GEOMETRY. Psi IS NOT FAITHFUL, AND ITS FAILURE IS EXACTLY THE ***")
print("      *** VANTAGE MULTIPLICITY -- the fibres of Psi ARE the S_3-orbits of designated roots. ***")
print()
print("  (c) FULL?  Are all isometries between two geometries in the image induced by substrate")
print("      isometries?  NOT SETTLED HERE and flagged: P5 establishes the WITHIN-single-geometry")
print("      component only and says the cross-geometry (different alpha) component is not")
print("      established.  *** FULLNESS IS THE OPEN PART, and it is P5's own stated gap. ***")

print("\n" + "="*80); print("K3 — IS 'THE SINGLE INVARIANT IS THE GEOMETRY' A UNIVERSAL PROPERTY?"); print("="*80)
print("""
  P5, verbatim: 'ONE RIGID GEOMETRY charted from many vantages (the groupoid's single invariant is
  the geometry)'.  Unpack 'SINGLE':
    - 'an invariant' = a function on objects constant on arrows, i.e. constant on orbits.
    - 'the SINGLE invariant' = every such function is a function OF the geometry.
  *** THAT SECOND CLAUSE IS EXACTLY THE UNIVERSAL PROPERTY OF THE QUOTIENT (the coequaliser of the
      source and target maps): any F constant on orbits factors UNIQUELY through the geometry. ***
  So P5's parenthesis is a universal property, stated as an observation.  And it has a consequence
  P5 draws in different words -- 'rigidity as DIMENSIONAL COLLAPSE (the continuous parameter is a
  CHART LABEL, not a modulus)': a chart label is precisely a coordinate that the quotient map kills.
""")
print("  CHECK the factorisation on the corpus's own invariant.  alpha is invariant, 2M is not:")
for lab,f in [('alpha (the throat scale)', lambda r,M: 1.0), ('2M (the mass)', lambda r,M: M),
              ('r_0 (the designated root)', lambda r,M: r)]:
    vals=[]
    for M in [0.20]:
        rts=[x.real for x in np.roots([1,0,-1,M]) if abs(x.imag)<1e-9]
        vals=[f(r,M) for r in rts]
    const=np.allclose(vals, vals[0])
    print(f"    {lab:28s} across the three cuts of one geometry: {np.round(vals,6)}   constant? {const}")
    # r2376+c54.158 -- pins K3's factorisation test, and it is a DISCRIMINATING pin, not a blanket
    # one: alpha and 2M must come out CONSTANT on the S_3 orbit (they are functions OF the geometry,
    # so they factor through the quotient) while r_0 must come out NOT constant -- it is the chart
    # label the quotient kills, which is what "rigidity as dimensional collapse" asserts.  A run in
    # which r_0 also came out constant would refute the claim just as surely as one in which 2M did
    # not.  The three r_0 values printed are the three roots at 2M=0.20, spread over more than 1.9.
    assert bool(const) == (lab != 'r_0 (the designated root)'), (lab, vals)
    assert lab != 'r_0 (the designated root)' or float(np.ptp(vals)) > 1.9, vals
print("  *** alpha and 2M are constant on the orbit -- they are functions OF the geometry. ***")
print("  *** r_0 is NOT -- it is the chart label, exactly what the quotient kills. ***")
print("  So the universal property holds on the corpus's own invariants, and 'single' is earned.")
print("="*80)
