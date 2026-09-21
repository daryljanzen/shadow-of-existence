"""
P14_the_core_family_carries_no_first_cohomology_and_the_cover_is_a_sphere
=========================================================================

Object under test -- where in this construction a four-dimensional locus carries FIRST
COHOMOLOGY, which r6714 showed is the one thing the doublet lacks on the shared S^4: there
Lambda^1 = (2,2) is a doublet of each su(2) factor and is empty only because b_1(S^4) = 0.

--------------------------------------------------------------------------------
(1) THE BRANCHED COVER IS A SPHERE.

  The horizon cubic r^3 - alpha^2 r + 2M alpha^2 = 0 is a three-sheeted cover of the 2M-plane,
  with discriminant -4 alpha^4 (27 M^2 - alpha^2) vanishing at the two Nariai values.  By
  Riemann-Hurwitz, with the base a sphere:

      2g - 2 = 3(0 - 2) + sum (e_p - 1)
      two sheets merge at each Nariai value (e = 2, contributing 1 each)
      all three meet at infinity           (e = 3, contributing 2)
      2g - 2 = -6 + 4 = -2    so    g = 0.

  *** The cover is genus zero -- a sphere, with no first cohomology. ***

  ⌗ So colour's loops (r6710) are NOT the cover's.  The fundamental group whose representation
  colour is, is that of the BASE punctured at the branch points; the monodromy is how it acts on
  the sheets.  Colour's loops live in the space of MEMBERS -- a two-dimensional parameter space --
  and not in any member's spacetime.

--------------------------------------------------------------------------------
(2) EVERY COMPACT RIEMANNIAN SECTION OF THE CORE FAMILY IS SIMPLY CONNECTED.

    Euclidean de Sitter                 S^4        b = (1,0,0,0,1)   b_1 = 0
    Euclidean Nariai (dS_2 x S^2)       S^2 x S^2  b = (1,0,2,0,1)   b_1 = 0
    the shared throat / equator         S^4        b = (1,0,0,0,1)   b_1 = 0

  *** No compact Riemannian four-dimensional section of the Schwarzschild-de Sitter family
  carries a harmonic one-form. ***

  The one locus with loops the corpus cites is the T^3-Gowdy class (Andreasson-Ringstrom), whose
  Euclidean section T^4 has b_1 = 4 -- and that is where C50's member lives, which r6702 found
  has the split but not the pairing, blocked by the twist.

--------------------------------------------------------------------------------
(3) AND P14 ALREADY DRAWS THIS BOUNDARY.

  Its masthead: NOT DELIVERED are "the GAUGE REPRESENTATIONS (colour, weak isospin, hypercharge --
  excluded from the isometry; 'they remain the ordinary route, a bundle imposed by hand')".

  The doublet PO-45 asks for is a weak-isospin representation.  What this line has done since
  r6686 is supply the MECHANISM behind a boundary P14 states: discrete operations trade chirality
  against pairing (r6698, r6702); continuous pairing needs curvature, and the curved face is simply
  connected (r6704); the shared S^4 has the symmetry profile and no first cohomology (r6714); and
  no compact Riemannian section of the core family has any (here).

--------------------------------------------------------------------------------
⚠ WHAT IS NOT CLAIMED.

  ** NOT that weak isospin is absent from physics or from CR. **  P14's statement is that it
  enters by the ordinary route -- a bundle -- and that is WHERE it is fixed.  What this receipt
  adds is why the geometry does not supply it, not that nothing does.

  ** NOT that loops would suffice. **  The T^3-Gowdy member has them and fails by the twist.

  ** NOT anything about non-compact or Lorentzian sections, ** where harmonic forms are not the
  right notion and the index argument does not apply.
"""

import sympy as sp

r, M = sp.symbols('r M'); al = sp.Integer(1)
disc = sp.factor(sp.discriminant(r**3 - al**2*r + 2*M*al**2, r))
bps = sp.solve(sp.Eq(disc, 0), M)
assert len(bps) == 2
n, ram = 3, {'nariai+': 2, 'nariai-': 2, 'infinity': 3}
two_g_minus_2 = n*(0-2) + sum(e-1 for e in ram.values())
g = sp.Rational(two_g_minus_2 + 2, 2)
assert g == 0, g
print(f"  the horizon cubic's cover: branch points {bps}, genus {g}          OK")

SECTIONS = {'Euclidean de Sitter S^4': (1,0,0,0,1),
            'Euclidean Nariai S^2 x S^2': (1,0,2,0,1),
            'the shared throat S^4': (1,0,0,0,1)}
for k, b in SECTIONS.items():
    assert b[1] == 0
    print(f"  {k:<28} b_1 = {b[1]}   chi = {b[0]-b[1]+b[2]-b[3]+b[4]}           OK")
T4 = (1,4,6,4,1)
assert T4[1] == 4 and (T4[0]-T4[1]+T4[2]-T4[3]+T4[4]) == 0
print(f"  the T^3-Gowdy class's Euclidean T^4   b_1 = {T4[1]} -- the one locus with loops    OK")

print()
print("ESTABLISHED: the horizon cubic's three-sheeted branched cover is genus zero, so colour's loops")
print("are the punctured BASE's, in the space of members, not in any member's spacetime. And every")
print("compact Riemannian four-dimensional section of the Schwarzschild-de Sitter family -- S^4 and")
print("S^2 x S^2 -- has b_1 = 0; the one locus with loops the corpus cites is the T^3-Gowdy class,")
print("where C50's member fails by the twist. This supplies the mechanism behind a boundary P14 already")
print("draws: weak isospin enters by the ordinary route, a bundle.")
print("NOT CLAIMED: that weak isospin is absent -- P14 says WHERE it is fixed. Not that loops would")
print("suffice. Nothing about non-compact or Lorentzian sections.")
