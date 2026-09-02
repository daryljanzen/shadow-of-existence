"""hubble_eddington_is_the_merged_horizon.py (r1629) -- the Hubble-Eddington radius lies ON
a horizon if and only if the configuration is Nariai, and then it IS the merged horizon.

WHERE IT CAME FROM. Reading c49's transcript: its r1426 derivative work put the bead's front
seam at r = (2 M alpha^2)^(1/3) * 2^(-1/3) with dr/ds = 1 exactly (the bead's unique
inflection). That is the SAME expression as r_star = (M alpha^2)^(1/3), the Hubble-Eddington
radius of P3/P8 -- which the r1608 identity had already related to the amplitude by 2^(1/3).
Two quantities defined by unrelated conditions, in different papers, at one radius.

THE TAXONOMY TEST (GEOMETRY_PHYSICS_TAXONOMY: a bare number-match is numerology; a structural
mechanism that forces the number AND a further consequence has teeth). Applied below, and the
mechanism is exhibited rather than asserted:

  K_G = 1/alpha^2 - M/r^3 = 0  <=>  2M/r = 2 r^2/alpha^2
  f   = 1 - 2M/r - r^2/alpha^2, so ON that locus  f = 1 - 3 r^2/alpha^2
  -- the pure de Sitter form at scale alpha/sqrt3, with the mass term absorbed.

  Hence f(r_star) = 0  <=>  r_star = alpha/sqrt3  <=>  27 M^2 = alpha^2  <=>  NARIAI.

So it is not that two numbers agree at one mass; it is that the vanishing of the slicing
surface's Gaussian curvature converts the SdS potential into a de Sitter potential whose own
horizon is alpha/sqrt3 -- and the configuration for which that horizon is where the curvature
vanishes is precisely the double-root one.

FURTHER CONSEQUENCE (what the test demands beyond a mechanism): r_star is a horizon for
exactly one member of the family, and it is the member the cosmology selects. On every other
member r_star is strictly inside the static region (f(r_star) > 0) or beyond it, and the
receipt exhibits the sign both ways.
"""
import sympy as sp

r, M, al = sp.symbols('r M alpha', positive=True)

f   = 1 - 2*M/r - r**2/al**2                 # the SdS potential
K_G = 1/al**2 - M/r**3                       # P3's slicing-surface Gaussian curvature
r_st = (M*al**2)**sp.Rational(1,3)           # Hubble-Eddington radius: K_G = 0

print("1. r_star is the K_G zero, symbolically")
assert sp.simplify(K_G.subs(r, r_st)) == 0
print("   K_G(r_star) = 0  ->  verified.  r_star =", r_st)

print()
print("2. THE MECHANISM: on the locus K_G = 0 the potential becomes the de Sitter form")
# on K_G = 0 we have M = r^3/alpha^2; substitute into f
f_on_locus = sp.simplify(f.subs(M, r**3/al**2))
print("   f | (K_G=0)  =", f_on_locus)
assert sp.simplify(f_on_locus - (1 - 3*r**2/al**2)) == 0
print("   = 1 - 3 r^2/alpha^2  -- pure de Sitter at scale alpha/sqrt3, the mass term absorbed.")
print("   *The vanishing of the surface curvature is exactly the condition that removes the")
print("    mass from the potential.* That is the mechanism, and it is an identity.")

print()
print("3. THE CONSEQUENCE: f(r_star) = 0 iff Nariai")
f_at_rst = sp.simplify(f.subs(r, r_st))
print("   f(r_star) =", f_at_rst)
sols = sp.solve(sp.Eq(f_at_rst, 0), M)
print("   f(r_star) = 0  =>  M =", sols)
M_N = al/(3*sp.sqrt(3))
assert any(sp.simplify(s - M_N) == 0 for s in sols), "the root is not the Nariai mass"
disc = sp.factor(sp.discriminant(r**3 - al**2*r + 2*M*al**2, r))
print("   the Nariai mass, independently, from disc = 0:", sp.solve(sp.Eq(disc,0), M))
print("   -> the SAME mass. So r_star is a horizon for exactly ONE member, and it is the")
print("      double-root member the cosmological reassignment selects.")

print()
print("4. AND THERE IT IS THE MERGED HORIZON, not some other root")
rho = al/sp.sqrt(3)
assert sp.simplify(r_st.subs(M, M_N) - rho) == 0
H_N = sp.expand((r**3 - al**2*r + 2*M*al**2).subs(M, M_N))
assert sp.simplify(H_N - sp.expand((r-rho)**2*(r+2*rho))) == 0
print("   r_star | Nariai =", sp.simplify(r_st.subs(M, M_N)), "= rho = alpha/sqrt3")
print("   and H | Nariai factors as (r-rho)^2 (r+2rho): rho is the DOUBLE root.")

print()
print("5. THE SIGN BOTH WAYS (so the 'exactly one member' claim is exhibited, not asserted)")
for lab, Mval in [("sub-Nariai  M = alpha/6   ", al/6),
                  ("Nariai      M = alpha/3sqrt3", M_N),
                  ("over-Nariai M = alpha/4   ", al/4)]:
    v = sp.simplify(f_at_rst.subs(M, Mval))
    print(f"   {lab}: f(r_star) = {v} = {float(v.subs(al,1)):+.6f}")

print()
print("6. AND c49's THIRD FACE, from its r1426 derivative work")
A = (2*M*al**2)**sp.Rational(1,3)
front = sp.simplify(A*2**sp.Rational(-1,3))
assert sp.simplify(front - r_st) == 0
print("   the bead's front seam sits at A * 2^(-1/3), and A*2^(-1/3) = r_star identically:")
print("   so the front seam -- the bead's UNIQUE inflection, where dr/ds = 1 exactly and")
print("   d^2r/ds^2 = 0 -- is the Hubble-Eddington radius, for every M.")

print()
print("="*78)
print("VERDICT vs the taxonomy: TEETH, not numerology.")
print("  MECHANISM: K_G = 0 is the condition that absorbs the mass from f, leaving the")
print("             de Sitter potential at scale alpha/sqrt3 -- an identity, not a fit.")
print("  CONSEQUENCE: r_star lies on a horizon for exactly one member of the family, the")
print("             double-root member, and there it IS the merged horizon; plus the front")
print("             seam identification, which holds for every M.")
print()
print("HELD, not claimed: no claim that this explains WHY the cosmology selects Nariai --")
print("  the selection is P7's trichotomy and stands on its own. This says that the member")
print("  so selected is the one whose structure-formation boundary is its own merged horizon.")
print("="*78)
