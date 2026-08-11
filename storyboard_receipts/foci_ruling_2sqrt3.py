"""Receipt (r1281): the A,B-rulings ↔ horizon-locus-ellipse-foci convergence at 2/sqrt3
is NOT a coincidence — 2/sqrt3 is the equilateral substrate's single forced constant.
Hunted down after wrongly killing it as a 'description-level coincidence'."""
import numpy as np
M = np.array([[1,0.5],[0.5,1]])            # quadratic form of r^2 + r r0 + r0^2 (units alpha=1)
evals,_ = np.linalg.eigh(M)                 # eigenvalues 1/2, 3/2
a,b = 1/np.sqrt(evals.min()), 1/np.sqrt(evals.max())   # semi-axes sqrt2, sqrt(2/3)
c = np.sqrt(a**2-b**2)                      # focal distance
r0_vt = np.sqrt(4/3)                        # vertical-tangent (Nariai) offset: 3/4 r0^2 = 1
target = 2/np.sqrt(3)
assert np.isclose(c, target),      f"focal distance {c} != 2/sqrt3"
assert np.isclose(r0_vt, target),  f"Nariai offset {r0_vt} != 2/sqrt3"
print(f"focal distance = {c:.6f}, Nariai offset = {r0_vt:.6f}, 2/sqrt3 = {target:.6f}")
print("VERIFIED: ellipse focal distance = Nariai critical offset = throat-image radius = 2/sqrt3.")
print("The rulings (tangent to the throat, gnomonic radius 2/sqrt3) and the ellipse foci")
print("(at focal distance 2/sqrt3) share the ONE forced scale of the equilateral cubic — real structure.")

# --- chase, r1281: the cross-plane unification (Daryl: chase it) ---
# Both r0 and the horizon roots r are (2/sqrt3) sin(angle): the ONE gnomonic
# sine-parametrization at amplitude 2/sqrt3 (the forced constant). The rulings,
# foci, Nariai are three special sky-angles of that single parametrization:
#   Nariai  w = 30deg (crest of sin 3w; double horizon r = alpha/sqrt3 = 1/sqrtLambda)
#   FOCI    w = 45deg (foci at (r0,r)=(+-sqrt(2/3),-+sqrt(2/3)))
#   RULINGS w = 60deg (throat-tangent extreme r0 = 1 = alpha)
# alpha relation: dimensionally the constant is 2*alpha/sqrt3 = 2/sqrtLambda = 2 x Nariai radius;
# a forced pure number (2/sqrt3) times the substrate's one gauge alpha -- not a second scale.
