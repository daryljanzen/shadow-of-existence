"""lambda_carries_the_threeness.py (r1707) -- A4.9, restated after understanding WHY P3 forbids
the limit. The prohibition is not the premise; sec:mass's reasoning is.

WHY alpha->oo IS UNINTELLIGIBLE (P3 sec:mass, which the prohibition rests on and does not state):
  2M = alpha * [(r0/alpha) - (r0/alpha)^3] = alpha * sin(u) cos^2(u).
  alpha is the construction's ONLY dimensionful object -- invariant under the reading-swap, fixed
  across the whole slicing family, invariant under the projection. Everything else is a PURE NUMBER
  of the slicing. So M is not independent of alpha: "M is not an intrinsic coefficient of a
  spacetime; it is the throat radius alpha projected through a turning of the slicing."
  Therefore "alpha -> oo at fixed M" holds fixed a quantity DEFINED as alpha x profile, forcing
  profile -> 0, i.e. w -> 0. That is not a limit of the geometry. It is a CHOICE OF SLICING.
  => Schwarzschild is not a limit of this construction; it is this substrate read at small sky
     angle. There is no Lambda=0 member because mass is a READING OF alpha.

WHAT THAT CHANGES about the earlier (r1706) statement: the three-foldness is NOT "a term of f that
could be removed". It is an IDENTITY OF THE PROJECTION. Correcting the frame is the result.

VERDICTS ARE ASSERTS, WRITTEN AFTER THE OUTPUT WAS READ.
"""
import sympy as sp
u, w, al, r0, M = sp.symbols('u w alpha r_0 M', positive=True)

print("(1) MASS IS A READING OF alpha -- the whole basis")
prof = sp.sin(u)*sp.cos(u)**2
twoM = al*prof
print("    2M = alpha * sin(u) cos^2(u);  the second factor is dimensionless and slicing-dependent.")
assert sp.simplify(sp.diff(twoM, al) - prof) == 0, "M is not linear in alpha"
print("    ASSERTED: 2M is exactly LINEAR in alpha with the profile as coefficient.")
print("    So M cannot be held fixed while alpha varies without varying the slicing:")
print("    holding 2M fixed as alpha->oo forces profile->0, i.e. u->0. A dial turn, not a limit.")

print()
print("(2) THE THREE-FOLDNESS IS THE PROJECTION'S OWN IDENTITY")
tri = sp.simplify(sp.expand_trig(prof.subs(u, sp.asin(2*sp.sin(w)/sp.sqrt(3)))))
assert sp.simplify(tri - 2*sp.sin(3*w)/(3*sp.sqrt(3))) == 0, "profile is not (2/3sqrt3) sin 3w"
print("    in the sky angle:  profile = (2/3sqrt3) sin(3w).   ASSERTED.")
print("    The cubic is the sin^3 of sin(3w) = 3 sin w - 4 sin^3 w -- an identity of the ANGLE,")
print("    not a coefficient anyone could delete. The map w -> 3w is three-to-one BECAUSE the")
print("    observation geometry is gnomonic (prop:gnomonic) and mass is read off it.")

print()
print("(3) NARIAI IS THE PROFILE'S MAXIMUM -- which is WHY the discriminant vanishes there")
d = sp.simplify(sp.diff(prof, u))
# factor the derivative rather than trusting solve()'s nested-radical branch forms
assert sp.simplify(d - sp.cos(u)*(1 - 3*sp.sin(u)**2)) == 0, "derivative is not cos u (1-3 sin^2 u)"
# so the interior critical point is exactly sin u = 1/sqrt3
assert sp.simplify((1 - 3*sp.sin(u)**2).subs(sp.sin(u), 1/sp.sqrt(3))) == 0, "sin u = 1/sqrt3 is not a root"
mx = sp.simplify(prof.subs(u, sp.asin(1/sp.sqrt(3))))
assert sp.simplify(mx - 2/(3*sp.sqrt(3))) == 0, "max is not 2/(3 sqrt3)"
print("    d/du (sin u cos^2 u) = 0 at sin u = 1/sqrt3;  max profile = 2/(3 sqrt3).  ASSERTED.")
print("    So 2M_max = 2 alpha/(3 sqrt3) -- the Nariai value -- and P3 states the consequence:")
print("    THE LARGEST MASS ANY SLICING OF A GIVEN DE SITTER MANIFOLD CAN CARRY IS SET BY alpha.")
disc = sp.factor(sp.discriminant(sp.Poly(r0**3/al**2 - r0 + 2*M, r0)))
assert sp.simplify(disc - (-4*(27*M**2 - al**2)/al**4)) == 0
print("    disc =", disc, " -> zero at 27 M^2 = alpha^2, the same member.")
print("    A double root IS a critical point of the mass map. Nariai is not a separate fact about")
print("    a discriminant; it is the profile's maximum, seen the other way round.")

print()
print("(4) SO THE CORRECT STATEMENT OF THE Lambda-DEPENDENCE")
print("    NOT: 'delete the Lambda term and the three-ness goes' -- there is no such deletion,")
print("    because -r^2/alpha^2 is not a term added to a background. It IS the substrate.")
print("    BUT: the three-foldness, the Nariai bound and the hexad are all readings of alpha,")
print("    because MASS ITSELF is a reading of alpha. No substrate, nothing to read, no triple.")
print("    'No Lambda, no third' is not a counterfactual. It is the observation that the count")
print("    belongs to the substrate and not to the matter.")

print()
print("BOUND, do-not-assert:")
print("  * No limit is taken and none is needed; the r1706 phrasing 'one term carries four things'")
print("    is superseded -- it framed the substrate as a deletable term.")
print("  * The GENERATIONS reading is P14's, from the three hinges. Untouched here.")
print("    World-correspondence, and whether MASSES realise the splitting, stay open.")
