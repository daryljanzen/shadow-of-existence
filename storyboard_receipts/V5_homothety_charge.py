"""V5 — THE DILATION AS A SYMMETRY WITH NO CONSERVED CHARGE.
CONFIRMATION 4 — the object: C1 established that the group preserving the substrate's ABSOLUTE is
O(5,1) x R+, one generator larger than the isometry group O(5,1), and that the extra generator is the
DILATION carrying alpha -> lambda.alpha.  A dilation is a HOMOTHETY: L_xi g = 2c g with c constant.
The variational question: what conserved quantity, if any, does a homothety carry?"""
import sympy as sp
print("="*80); print("V5 — A HOMOTHETY CONSERVES ITS CHARGE ON THE NULL CONE AND NOWHERE ELSE"); print("="*80)
print("""
STEP 1 — THE IDENTITY, derived rather than quoted.
  For any vector field xi and any geodesic with tangent p (affinely parametrised, p^b nabla_b p^a = 0):
        d/dtau ( xi_a p^a ) = p^b nabla_b ( xi_a p^a ) = p^a p^b nabla_(b xi_a)
                            = (1/2) p^a p^b ( L_xi g )_{ab} .
  So the charge xi.p is conserved exactly when (L_xi g)_{ab} p^a p^b = 0.
    * KILLING:   L_xi g = 0            -> conserved on EVERY geodesic.
    * HOMOTHETY: L_xi g = 2c g, c != 0 -> d/dtau (xi.p) = c (p.p).
""")
tau,c,m=sp.symbols('tau c m', real=True)
print("STEP 2 — EVALUATE c (p.p) BY CAUSAL CHARACTER:")
for lab,pp,note in [("NULL geodesic (light)", 0, "-> d/dtau (xi.p) = 0 : CONSERVED"),
                    ("TIMELIKE geodesic (matter)", -m**2, "-> d/dtau (xi.p) = -c m^2 : NOT conserved"),
                    ("SPACELIKE", sp.Symbol('s')**2, "-> nonzero : NOT conserved")]:
    print(f"   {lab:28s} p.p = {str(pp):8s} {note}")
    # r2376+c54.158 -- pins V5's whole result against the verdict each row PRINTS.  STEP 1's
    # identity gives d/dtau(xi.p) = c (p.p) for a homothety, so the charge is conserved exactly
    # where c*(p.p) vanishes identically.  Check that symbolically, row by row, and require it to
    # agree with the row's own CONSERVED / NOT-conserved label: it must vanish on the NULL row
    # and on NEITHER of the other two.  A blanket "it vanishes" would be the wrong assertion here
    # -- the content is that it vanishes on exactly ONE of the three causal characters.
    assert (sp.simplify(c*pp) == 0) == ("CONSERVED" in note), (lab, sp.simplify(c*pp))
    if lab.startswith("TIMELIKE"):
        # and the obstruction on the timelike row is exactly -c m^2: *** MASS is what breaks it. ***
        assert sp.simplify(c*pp + c*m**2) == 0, sp.simplify(c*pp)
        assert sp.simplify(c*pp).has(m)
print("""
  *** SO THE DILATION'S CHARGE IS CONSERVED ON NULL GEODESICS AND ON NOTHING ELSE. ***

STEP 3 — AND THAT IS EXACTLY C1's STATEMENT, MET FROM THE CONSERVATION SIDE.
  C1: the dilation is the generator by which the group preserving the CAUSAL STRUCTURE exceeds the
  ISOMETRY group -- 'the null cone determines the geometry up to the scale, and the scale is the one
  thing it leaves'.
  The causal structure IS the null cone.  And the homothety's charge is conserved precisely on the
  null cone.
  *** A SYMMETRY CONSERVES A CHARGE EXACTLY ON THE STRUCTURE IT PRESERVES. The dilation preserves the
      null cone and not the metric; correspondingly its charge is conserved on null geodesics and not
      on timelike ones. ***
""")
print("STEP 4 — AND WHAT THAT SAYS ABOUT THE ONE SCALE, stated at the altitude the identity supports.")
print("   The failure is proportional to p.p = -m^2: *** IT IS MASS THAT BREAKS IT. ***")
print("   A massless world would carry a conserved dilation charge and no way to fix alpha from")
print("   dynamics; a massive one has no such charge, and mass is the corpus's own perspectival,")
print("   R-odd quantity.  We state the identity and its two cases and mark the reading as a reading:")
print("   the identity is a theorem, 'mass is what breaks the scale symmetry' is its gloss.")
print("="*80)
