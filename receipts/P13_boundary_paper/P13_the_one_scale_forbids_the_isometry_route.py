"""
P13_the_one_scale_forbids_the_isometry_route
============================================

Object under test -- PO-26, "the compact-face fermion sector -- CAN IT BE BUILT",
registered as a floor estimate with no route known.

THE BASE, fixed from the corpus rather than chosen:
  p0 sec:ledger  --  the Wick face is "S^5 of the SAME RADIUS", and "every curvature
                     invariant on either face is a pure power of 1/alpha^2"
  P13 sec:synthesis -- the face is S^5 = SO(6)/SO(5), "the round sphere its
                     Euclidean section"
  p0             --  alpha = sqrt(3/Lambda), the substrate's only scale

So the face is the ROUND S^5 of radius alpha, and alpha is fixed by Lambda alone.

THE OPERATOR.  "Isometry-realised" means gauge group = isometry group: there is no
extra twisting bundle, the gauge field is the internal metric's own structure, the
fermion's gauge charge is its isotropy label, and the four-dimensional mass of a
mode IS the internal Dirac eigenvalue.  The operator is therefore the ordinary
Dirac operator on the face.

TWO CONSEQUENCES, and the second is the sharp one.

  (A) NO MASSLESS MODES.  Round S^5 has positive scalar curvature, so by
      Lichnerowicz there are no zero modes: the spectrum is +/-(5/2 + k)/alpha.
      This is the standard reason Kaluza-Klein on a positively curved internal
      space yields no massless fermions, and it is why the literature's escapes are
      flux or Ricci-flatness (Calabi-Yau).  P13 lists exactly those escapes.

  (B) AND EVERY SCALE THE FACE CAN SUPPLY IS COSMOLOGICAL.  Not a Kaluza-Klein
      tower: P13 states that the substrate is "a single irreducible Lorentzian
      manifold, not a product M_4 x K of a spacetime with a compact internal
      space -- so the ordinary Kaluza-Klein route is not merely unbuilt here, it
      is unavailable", so there is no reduction over an internal space to take and
      no tower to compute.  What survives without that premise is weaker and needs
      none of it: the face carries ONE scale, alpha, and every curvature invariant
      on it is a pure power of 1/alpha^2 (p0 sec:ledger).  So any mass read off the
      face's own geometry is a multiple of hbar c / alpha, computed below.

  ==> That is a JOIN and not a second obstruction, and it is worth having as one:
      it is why P14's "the zero-modes are massless, and their splitting is
      electroweak physics, external to the geometry" is not a concession but a
      requirement.  With one scale and that scale cosmological, the geometry could
      not have supplied a fermion mass even in principle.

WHAT THIS DOES NOT TOUCH, stated so the negative stays bounded:
  colour placed by hand (P13 sec:open says it is untouched and not the subject);
  flux or boundary-condition routes, which abandon gauge-group-equals-isometry and
  are outside what PO-26 asks; the universal claim, which P13 declines and so does
  this; and P14's built sector, which lives on the DISCRETE component, carries a
  wall-localised leaf index, and is not a mode of this operator at all.

The receipt could have returned otherwise: if the corpus had left the face's radius
free, (B) would say nothing; if the face had been Ricci-flat or negatively curved,
(A) would fail.
"""

import sympy as sp

# ---- the base, from the corpus ------------------------------------------------
Lam = sp.Symbol('Lambda', positive=True)
alpha = sp.sqrt(3/Lam)
n = 5

R = sp.simplify(n*(n-1)/alpha**2)
assert sp.simplify(R - sp.Rational(20, 3)*Lam) == 0
print(f"face: round S^{n}, radius alpha = sqrt(3/Lambda)")
print(f"scalar curvature R = {sp.simplify(R)}   (= 20/alpha^2, set by Lambda alone)")

# ---- (A) no zero modes ---------------------------------------------------------
k = sp.Symbol('k', nonnegative=True, integer=True)
lam = (sp.Rational(n, 2) + k)/alpha
lam_min = sp.simplify(lam.subs(k, 0))
assert sp.simplify(lam_min) == sp.Rational(5, 2)*sp.sqrt(Lam)/sp.sqrt(3)
print(f"(A) Dirac spectrum +/-({n}/2 + k)/alpha, least |lambda| = 5/(2 alpha) > 0")
print("    -> no zero modes: NO massless fermions from this route        OK")

# ---- (B) the tower's scale, in physical units ----------------------------------
# alpha = c / (H0 sqrt(Omega_Lambda)); the corpus's own H0 = 73 km/s/Mpc
c = 2.99792458e8                 # m/s
Mpc = 3.0856775814913673e22      # m
hbar_c = 1.973269804e-7          # eV m
H0 = 73.0 * 1e3 / Mpc            # s^-1
Om_L = 0.7
H_L = H0 * Om_L**0.5
alpha_m = c / H_L
m_min_eV = 2.5 * hbar_c / alpha_m

m_e = 5.10998950e5               # eV, electron
m_nu = 5.0e-2                    # eV, an upper-bound-scale neutrino mass

print()
print(f"(B) alpha            = {alpha_m:.4g} m")
print(f"    hbar c / alpha    = {hbar_c/alpha_m:.4g} eV")
print(f"    5/(2 alpha)      = {m_min_eV:.4g} eV")
print(f"    vs electron      = {m_e/m_min_eV:.3g}x too light")
print(f"    vs a ~0.05 eV nu = {m_nu/m_min_eV:.3g}x too light")

assert m_min_eV < 1e-30, "the face's only scale is cosmological"
assert m_e / m_min_eV > 1e30, "the shortfall must be tens of orders"
print("    -> every scale the face supplies is cosmological              OK")

print()
print("ESTABLISHED (A), bounded to the isometry-realised route on the corpus's own")
print("face: it yields NO massless fermions at all -- empty, not vector-like.")
print()
print("JOINED (B): the face's one scale is cosmological, so the geometry could not")
print("have supplied a fermion mass in principle. P14's external mass spectrum is a")
print("REQUIREMENT of the one-scale ledger, not a concession.")
print()
print("WITHDRAWN: an earlier draft read (B) as a Kaluza-Klein tower at the wrong")
print("scale. P13 states the product structure that argument needs is unavailable.")
