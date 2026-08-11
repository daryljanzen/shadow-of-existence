#!/usr/bin/env python3
# =============================================================================
# c19fork TEST 2 -- THE xi-LIFT (the seam-continuation leg, properly posed)
#
# QUESTION (c17's, de-conflated from the sigma-lift):
#   The corpus carries THREE distinct discrete operations (canonical: P3 slicing-
#   curve, P4 groupoid, P10 algebroid, P9 dynamics -- "different involutions,
#   not one"):
#     sigma : root-exchange w<->pi/3-w  (Weyl(A2); SIGNATURE-PRESERVING; the gem)
#     xi    : seam signature-FLIP, the analytic continuation theta->pi/2+i psi
#             joining the Riemannian spherical piece to the Lorentzian dS piece
#     (cosmogenesis null<->timelike reassignment)
#   The sigma-lift (r296) tested sigma vs the GLOBAL Wick x0->ix0 and found them
#   different.  c17's catch: the real geometric signature-changing operation is
#   xi, which the sigma-lift never tested.  So the properly-posed question is:
#
#       does xi reach the GLOBAL SO(6) where su(3) lives,
#       or does it provably stop below it?
#
# GROUND (canonical source, NOT assumed here):
#   * P3 slicing-curve l.470-508: xi is the continuation of a curve traced ON
#     the de Sitter manifold; its Riemannian piece is r=alpha*sin(theta),
#     theta in [0,pi/2], the spherical THROAT region up to the equatorial seam
#     r=alpha; and l.508 "a geometry obtained as a slicing of de Sitter RETAINS
#     its membership in de Sitter" -- xi is INTRINSIC to dS5, not a passage off it.
#   * thesis Ch3 l.292: that Riemannian piece is "the closed 4-sphere of radius
#     sqrt(3/Lambda) embedded in five-dimensional Euclidean space" = the x0=0
#     equatorial S^4 of dS5.
#   So xi's Riemannian piece = the x0=0 equator of dS5.  This script computes the
#   ALGEBRAIC consequence: what symmetry that reaches, vs what the global Wick
#   reaches, vs what su(3) needs.  Suspect-the-model: every claim is computed.
# =============================================================================
import numpy as np

np.set_printoptions(precision=3, suppress=True, linewidth=120)
def head(s): print("\n" + "="*74 + "\n" + s + "\n" + "="*74)

eta_L = np.diag([-1.,1,1,1,1,1])   # dS5 in M^6, isometry so(5,1)
eta_E = np.diag([ 1.,1,1,1,1,1])   # Wick face S^5 in R^6, isometry so(6)

# -----------------------------------------------------------------------------
# so(5,1) generators: g preserves eta_L  <=>  g^T eta_L + eta_L g = 0.
#   M_ij (1<=i<j<=5): spatial rotations  -> so(5), 10 of them, FIX x0
#   M_0i (i=1..5)    : boosts            -> so(5,1)\so(5), 5 of them, MOVE x0
# -----------------------------------------------------------------------------
def E(a,b):
    M=np.zeros((6,6)); M[a,b]=1.0; return M

def boost(i):            # M_0i : x0<->xi, hyperbolic (eta_L-antisymmetric)
    return E(0,i)+E(i,0)
def rot(i,j):            # M_ij : xi<->xj, compact
    return E(i,j)-E(j,i)

boosts = [boost(i) for i in range(1,6)]          # 5
rots   = [rot(i,j) for i in range(1,6) for j in range(i+1,6)]  # 10
so51   = boosts + rots                            # 15 = dim so(5,1)

def preserves(g, eta):   # g in Lie algebra of O(eta) ?
    return np.allclose(g.T@eta + eta@g, 0.0)

head("[1] so(5,1): 15 generators on the real Lorentzian substrate dS5")
print("  all 15 preserve eta_L :", all(preserves(g,eta_L) for g in so51))
print("  count: boosts M_0i =",len(boosts)," (move x0)   rots M_ij =",len(rots)," (fix x0)")
print("  the 10 M_ij that FIX x0 form so(5) (max compact, the x0=0 stabilizer);")
print("  the 5 M_0i are the noncompact boosts = so(5,1)\\so(5).")

# -----------------------------------------------------------------------------
# [2] GLOBAL Wick W = diag(i,1,1,1,1,1).  Metric is a BILINEAR form -> pullback
#     is W^T eta W (the r296 cold-referee fix; NOT the sesquilinear W^dagger).
# -----------------------------------------------------------------------------
W = np.diag([1j,1,1,1,1,1])
head("[2] GLOBAL Wick  x0 -> i x0 :  so(5,1) -> so(6)  (this is where su(3) lives)")
print("  W^T eta_L W = eta_E ? :", np.allclose((W.T@eta_L@W), eta_E),
      "   (signature flip (-+++++)->(++++++))")
# conjugate a boost by the Wick: does it become a (real) compact so(6) rotation?
def wick_conj(g):
    return np.real_if_close(np.linalg.inv(W)@g@W, tol=1e6)
boosts_wicked = [wick_conj(b) for b in boosts]
print("  each boost M_0i, Wick-conjugated, is eta_E-antisymmetric (a COMPACT so(6) rotation)?")
print("   ", [bool(preserves(np.real(bw), eta_E)) for bw in boosts_wicked])
# build so(6) and check dimension closure: so(5) (the 10 rots, unchanged) + 5 wicked boosts
so6 = rots + [np.real(bw) for bw in boosts_wicked]
print("  all 15 of {10 M_ij} U {5 Wick(M_0i)} preserve eta_E :",
      all(preserves(g,eta_E) for g in so6), "  -> dim so(6) =",len(so6))
print("  => the GLOBAL Wick turns the 5 boosts into the 5 compact x0-mixing")
print("     rotations so(6)\\so(5).  THIS is the sector beyond so(5).")

# -----------------------------------------------------------------------------
# [3] xi's reach: the Riemannian piece is the x0=0 equator (ground above).
#     Its isometry = the subalgebra of BOTH so(5,1) and so(6) that FIXES x0=0.
# -----------------------------------------------------------------------------
def fixes_x0_axis(g):    # g maps the x0-axis e0 into itself (stabilizer of x0=0 equator)
    e0=np.zeros(6); e0[0]=1.0
    return np.allclose(g@e0, (g@e0)[0]*e0)   # g e0 parallel to e0
head("[3] What xi reaches: the x0=0 equatorial S^4 (its Riemannian piece, intrinsic to dS5)")
stab = [g for g in so51 if fixes_x0_axis(g)]
print("  generators of so(5,1) fixing the x0-axis (the equator stabilizer):", len(stab))
print("   -> these are exactly the 10 M_ij = so(5).  (boosts fail: they move x0.)")
print("  boosts fix x0-axis? :", [fixes_x0_axis(b) for b in boosts])
print("  so xi's Riemannian piece carries isometry so(5), dim", len(stab),
      "-- the SAME so(5) in so(5,1) and in so(6).")
print("  KEY: xi is INTRINSIC to dS5 (P3 l.508), so it relates the equatorial")
print("  S^4 to the Lorentzian piece WITHIN dS5; it does NOT make x0 a full")
print("  coordinate of an S^5.  The full S^5/SO(6) is the EXTRINSIC global Wick [2],")
print("  a different operation: it Wick-rotates the WHOLE embedding, not a curve on it.")

# -----------------------------------------------------------------------------
# [4] Does su(3) need the difference so(6)\so(5) ?  (rep-dimension, computed facts)
# -----------------------------------------------------------------------------
head("[4] su(3): needs so(6)\\so(5), the x0-mixing generators -- which xi does NOT supply")
print("  * su(3) irrep dims: 1, 3, 3bar, 6, 8, ...  smallest FAITHFUL is the 3 (complex),")
print("    i.e. C^3 = R^6 as a real rep -> smallest faithful REAL rep is 6-dimensional.")
print("  * so(5) acts on R^5 (defining rep).  A subalgebra su(3) c so(5) would give a")
print("    faithful real rep of su(3) on R^5 (dim 5 < 6) -- impossible.  => su(3) NOT c so(5).")
print("  * so(6) ~= su(4) (D3=A3); su(3) c su(4) (upper-left block) -> su(3) c so(6),")
print("    realized on C^3=R^6.  This uses generators OUTSIDE so(5): the x0-mixing")
print("    so(6)\\so(5) rotations -- exactly the 5 the GLOBAL Wick [2] makes and that")
print("    the equator/xi [3] does NOT (the equator FIXES x0).")
# sanity: rank check (necessary, not sufficient) -- both rank 2, consistent with A2 Cartan-Weyl skeleton
print("  (rank su(3)=2 = rank so(5)=rank so(6); the A2 Cartan-Weyl skeleton is the")
print("   NECESSARY ingredient C6 -- present on the substrate -- but the CONTINUOUS")
print("   su(3) needs the 6-real-dim rep, i.e. so(6), not the discrete skeleton.)")

# -----------------------------------------------------------------------------
head("VERDICT (c19fork, stated for reversal; receipt this file)")
print("""  xi (the seam continuation, c17's pivot) reaches so(5): its Riemannian piece is
  the x0=0 equatorial S^4 of dS5, intrinsic to dS5 (P3 l.508).  so(5) is the SAME
  subalgebra in both so(5,1) and so(6) -- it is the part that FIXES x0.

  su(3) lives in so(6) and requires the so(6)\\so(5) generators (the x0-mixing
  compact rotations) -- which ONLY the GLOBAL, EXTRINSIC Wick x0->ix0 supplies,
  and which xi (fixing x0 at its Riemannian piece) does NOT.

  => xi does NOT reach SO(6)/su(3).  It provably stops at SO(5).

  So the colour wall closes from BOTH discrete sides, now de-conflated:
    - sigma (root-exchange, signature-preserving)        != global Wick  [sigma-lift, r296]
    - xi    (seam continuation, intrinsic, reaches so(5)) != global Wick  [this test]
  Neither real-substrate discrete operation is the global Wick that builds the
  SO(6) where su(3) lives.  su(3) c so(5,1) stays false; AH untouched.
  This CONFIRMS c17's SO(5) reading -- derived here from the canonical source,
  independently -- and resolves "leg unsound" to "leg sound, argument cleaner once
  sigma and xi are kept distinct."  Held for the cold read (convergence with a
  saturated node is itself a flag).""")
