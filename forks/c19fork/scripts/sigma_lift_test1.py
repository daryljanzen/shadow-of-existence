import numpy as np
np.set_printoptions(suppress=True, linewidth=140, precision=4)

print("="*78)
print("TEST 1 — THE sigma-LIFT, computed in the M^6 embedding coordinates")
print("Question: is sigma (the A2 skeleton's root-exchange) the SAME operation as")
print("the Wick rotation x0 -> i x0 (the SO(5,1)->SO(6) bridge to where su(3) lives)?")
print("Decide IN COORDINATES, not by shared 'A2 flip' flavor.")
print("="*78)

# ---------------------------------------------------------------------------
# THE EMBEDDING (thesis Ch.3, source-read): substrate = one-sheet hyperboloid
#   -x0^2 + sum_{i=1}^5 x_i^2 = 3/Lambda  in  M^6,  metric eta=diag(-1,1,1,1,1,1)
# isometry SO(5,1).  Wick x0 -> i x0  =>  +x0^2+...  = sphere S^5, isometry SO(6).
eta_L = np.diag([-1.,1,1,1,1,1])      # Lorentzian ambient (real substrate)
eta_E = np.diag([ 1.,1,1,1,1,1])      # Euclidean ambient (Wick face)

# ---------------------------------------------------------------------------
# OBJECT B — the Wick rotation, as an explicit operation on the embedding.
# x0 -> i x0 : W = diag(i,1,1,1,1,1).  The metric is a BILINEAR form, so the Wick
# pullback is W^T eta W (NOT the sesquilinear W^dagger eta W -- with the conjugate
# transpose the i and -i cancel, |i|^2=1, and eta_L would come back unchanged;
# that one-character slip was caught on the cold-referee read and is fixed here):
W = np.diag([1j,1,1,1,1,1])
pulled = (W.T @ eta_L @ W).real
print("\n[B] Wick rotation W = diag(i,1,1,1,1,1)  (complexifies the TIME axis x0)")
print("    W^T eta_L W =\n", pulled)
print("    -> turns eta_L into eta_E :", np.allclose(pulled, eta_E), " i.e. SO(5,1)->SO(6).")
print("    CHARACTER: imaginary (has i); acts on the x0 (timelike) axis;")
print("    CHANGES the geometry (Lorentzian dS  ->  Euclidean S^5).")

# ---------------------------------------------------------------------------
# OBJECT A — sigma, the root-exchange involution (SdS-slicing-curve, source-read):
#   the reflection w <-> pi/3 - w of the REAL sky angle, equivalently the
#   diagonal reflection (r0,r)->(r,r0) of the fundamental ellipse r^2+r r0+r0^2=1.
#
# GROUND (where sigma-fixes-x0 actually comes from -- NOT from the matrix below):
#   sigma is a genuine Weyl(A2) reflection of the SPATIAL sky/root plane, a
#   rigidity-fixing groupoid morphism that permutes observer-vantages while FIXING
#   the one rigid SdS geometry (C6 + the genericity check; SdS-slicing-curve
#   sec:two-descriptions; framework_paper sigma,tau as derived coord-independent
#   morphisms).  The Weyl group is a SIGNATURE-INDEPENDENT combinatorial object,
#   so sigma is realized IDENTICALLY in both real forms SO(5,1) and SO(6) -- which
#   is *why* it is an isometry of both eta_L and eta_E and *why* it fixes x0.
#   The matrix below ILLUSTRATES that established character in coordinates; it does
#   not derive it (building S in a spatial plane makes touches_time==False by
#   construction).  [sharpening banked from the different-node read.]
S = np.eye(6)
S[1,1]=0; S[2,2]=0; S[1,2]=1; S[2,1]=1          # real reflection (r0,r)->(r,r0)
print("\n[A] sigma (root-exchange) -- a signature-independent Weyl(A2) reflection of the")
print("    spatial sky/root plane (C6); shown here in coordinates (ILLUSTRATES, see GROUND):")
print(S.real)
print("    real:", np.isrealobj(S), " | involution sigma^2=I:", np.allclose(S@S,np.eye(6)),
      " | det:", round(np.linalg.det(S),3))
# Illustration (guaranteed by the spatial construction; the derivation is the C6 ground above):
touches_time = (not np.allclose(S[0,1:],0)) or (not np.allclose(S[1:,0],0))
print("    acts on x0 (time)?", touches_time, " -> consistent with sigma FIXING x0 (C6 ground).")
# The load-bearing fact: sigma is an isometry of BOTH eta_L and eta_E (realized identically
# in both real forms) -- the signature-independence that IS the reason it fixes x0:
print("    sigma preserves eta_L:", np.allclose(S.T@eta_L@S, eta_L),
      " and eta_E:", np.allclose(S.T@eta_E@S, eta_E),
      " -> same reflection in both real forms; NOT a signature flip.")

print("\n[A vs B] same operation in coordinates?", np.allclose(S.astype(complex), W),
      "  -> sigma != Wick.")
print("   - kind:    real discrete reflection      vs   imaginary continuation")
print("   - acts on: spatial root plane (fixes x0) vs   the timelike axis x0")
print("   - effect:  FIXES the geometry            vs   CHANGES it (Lorentzian<->Euclidean)")

# ---------------------------------------------------------------------------
# THE SECTOR OBSTRUCTION (re-derive C2 at source): where can su(3) live?
# so(5) = spatial rotations of (x1..x5), the max compact of so(5,1); it FIXES x0.
# Wick turns the so(5,1) boosts M_{0i} into so(6) rotations M_{0i} mixing x0<->x_i:
#   these are exactly so(6)\so(5).  su(3) (8-dim) needs a faithful REAL rep;
#   its smallest is 6-dim (3 complex = R^6) -> su(3) ⊂ so(6), su(3) ⊄ so(5).
# Smallest faithful real su(3) rep dimension (decisive number):
#   real(3)=6, real(8 adjoint)=8 has kernel Z3 (not faithful as SU(3)) -> min faithful real = 6.
dims = {"so(5)=max compact of so(5,1), fixes x0":10,
        "so(6)=isometry of the Wick face":15,
        "su(3)":8, "min faithful REAL rep of su(3)":6, "R^5 (so(5) acts here)":5}
for k,v in dims.items(): print(f"    dim {k:42s} = {v}")
print("    => su(3) needs a 6-dim real carrier; so(5) only gives R^5 ->  su(3) ⊄ so(5).")
print("    => su(3) MUST use so(6)\\so(5) = the x0-mixing generators the Wick rotation makes.")
print("    => the sector su(3) needs is the one sigma FIXES (x0); the one Wick REACHES.")

print("\n"+"="*78)
print("VERDICT (test 1): FORMAL COINCIDENCE.")
print(" sigma (root-exchange) and the Wick rotation are DIFFERENT operations in")
print(" coordinates: a real discrete reflection of the spatial sky/root plane that")
print(" FIXES the geometry and FIXES x0, vs an imaginary continuation of the timelike")
print(" axis x0 that CHANGES the geometry and produces the so(6)\\so(5) generators")
print(" su(3) requires. They share A2 root-system FLAVOR (both relate to the horizon-")
print(" root A2 / su(3)'s Cartan-Weyl is A2), but sigma is real-form bookkeeping of the")
print(" real-substrate horizon roots in the description groupoid; it is NOT the Wick")
print(" bridge and does NOT carry the discrete A2 skeleton to the Wick-face su(3).")
print(" => closes colour-from-geometry-via-the-sigma-lift AS STRUCTURE; core + A2 gem intact.")
print(" => the UNIVERSAL 'colour-from-geometry foreclosed' stays do-not-assert (face 18).")
print("="*78)
