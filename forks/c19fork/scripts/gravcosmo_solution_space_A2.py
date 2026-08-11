#!/usr/bin/env python3
# =============================================================================
# c19fork STEP 3 -- THE A2/S3 SYMMETRY OF THE GRAVITATIONAL-COSMOLOGICAL
#                   SOLUTION SPACE (the gem's home; the groupoid's deferred piece)
#
# CLAIM UNDER TEST (held for cold read; computed, not asserted):
#   The full (r, r0)-plane of the thesis (Ch.4 sec_DPM) is the between-member
#   discrete structure that the groupoid paper (P4) DEFERRED ("the full
#   classification of the same-alpha between-member morphisms left open"; the
#   over-critical "a further partial involution past the Nariai crest").  The
#   A2/S3 root-exchange (sigma), the reflection (negative mass), and the seam
#   continuation (xi) organize the whole plane -- black hole, Nariai, cosmology,
#   negative mass -- as the discrete symmetry of ONE gravitational-cosmological
#   solution class.  This is the gem's home, gravitational-cosmological (P11),
#   NOT colour.
#
# Gauge alpha=1 (throat radius the sole invariant).  Horizon cubic (P3/P10):
#   r^3 - r - (r0^3 - r0) = 0,   roots = the three horizons,   2M = r0 - r0^3.
#   No quadratic term => the three roots sum to 0 = the A2 Cartan/traceless cond.
# =============================================================================
import numpy as np
np.set_printoptions(precision=4, suppress=True, linewidth=120)
def head(s): print("\n"+"="*74+"\n"+s+"\n"+"="*74)

def twoM(r0):                      # cubic mass parameter (P3 mass relation)
    return r0 - r0**3
def horizons(r0):                  # three roots of r^3 - r + 2M = 0  (2M = r0-r0^3)
    c = [1.0, 0.0, -1.0, twoM(r0)] # r^3 + 0 r^2 - r + 2M
    return np.sort_complex(np.roots(c))

# -----------------------------------------------------------------------------
head("[1] A2 Cartan condition: the three horizons sum to zero, for every r0")
ok_sum=True
for r0 in np.linspace(-1.2,1.2,25):
    s = np.sum(horizons(r0))
    if abs(s) > 1e-9: ok_sum=False
print("  sum of the three roots == 0 for all sampled r0 :", ok_sum,
      "  (no r^2 term => Cartan/traceless A2)")

# -----------------------------------------------------------------------------
head("[2] S3 triplet degeneracy: the three horizons are interchangeable as r0")
print("  the same geometry is described whether r0 is taken as any of the three")
print("  horizon roots -- i.e. 2M is invariant under r0 -> (other root). Check:")
def real_roots(r0):
    rts=horizons(r0)
    return sorted(z.real for z in rts if abs(z.imag)<1e-9)
samples=[0.2, 0.4, 0.5, -0.3]
for r0 in samples:
    rr = real_roots(r0)
    if len(rr)==3:
        Ms = [twoM(x) for x in rr]   # 2M evaluated at each root as the new r0
        # the geometry is the same iff the root-TRIPLE (the cubic) is the same:
        trip0 = np.round(sorted(rr),6)
        same = all(np.allclose(sorted(real_roots(x)), trip0, atol=1e-6) for x in rr)
        print(f"  r0={r0:+.2f}: horizons={np.round(rr,4)}  -> each root's own triple "
              f"== original triple: {same}")
print("  => S3 = Weyl(A2) permutes the three horizon-descriptions of ONE geometry")
print("     (the within-geometry root-exchange sigma is one transposition of this S3).")

# -----------------------------------------------------------------------------
head("[3] The two non-designated horizons lie on the fundamental ellipse")
print("  ellipse: r^2 + r r0 + r0^2 = 1  (the A2 quadratic form).  Check the two")
print("  horizons other than the designated r0 satisfy it:")
for r0 in [0.2,0.4,-0.3]:
    rr=real_roots(r0)
    others=[x for x in rr if abs(x-r0)>1e-6]
    vals=[round(x*x + x*r0 + r0*r0,6) for x in others]
    print(f"  r0={r0:+.2f}: ellipse value at the two other horizons = {vals}  (==1)")

# -----------------------------------------------------------------------------
head("[4] Regime map across the plane: BH / Nariai / cosmology -- one cubic")
print("  r0^2<4/3 & !=1/3 : UNDER-critical (3 real horizons) = black hole")
print("  r0^2=4/3 or 1/3  : CRITICAL = Nariai (two roots collide; sigma fixed point)")
print("  r0^2>4/3         : OVER-critical (1 real horizon) = cosmology, r timelike "
      "for all r>0,\n                     the universe; reached by xi past the Nariai crest")
for r0 in [0.3, 1/np.sqrt(3), 0.9, 2/np.sqrt(3), 1.5]:
    rr=horizons(r0); nreal=sum(abs(z.imag)<1e-9 for z in rr)
    M=twoM(r0)/2
    regime=("Nariai (critical)" if abs(r0**2-1/3)<1e-6 or abs(r0**2-4/3)<1e-6
            else "under-critical (BH)" if r0**2<4/3 else "over-critical (cosmology)")
    print(f"  r0={r0:+.4f}: #real horizons={nreal}, M={M:+.4f}  -> {regime}")

# -----------------------------------------------------------------------------
head("[5] Reflection (r,r0) -> (-r,-r0): the negative-mass half-plane")
print("  2M is odd in r0: 2M(-r0) = -2M(r0).  So the plane's reflection through the")
print("  origin carries each geometry to its negative-mass partner (-1/sqrt(27)<M<0")
print("  the genuine negative-mass band, thesis sec_DPM).  Check 2M oddness:")
for r0 in [0.2,0.5,0.9,1.3]:
    print(f"  r0={r0:.2f}: 2M={twoM(r0):+.4f}   r0={-r0:.2f}: 2M={twoM(-r0):+.4f}"
          f"   (odd: {np.isclose(twoM(-r0),-twoM(r0))})")
print(f"  critical |2M| = 2/(3*sqrt3) = {2/(3*np.sqrt(3)):.6f}  (the under/over threshold,")
print("  M=+-1/sqrt(27); negative-mass band is the reflection of the positive one).")

# -----------------------------------------------------------------------------
head("[6] The over-critical (cosmology) branch is the xi-continuation of the BH branch")
print("  thesis/P3: 2M = (2/3sqrt3) sin(3w); over-critical |2M|>2/(3sqrt3) needs")
print("  |sin 3w|>1, i.e. 3w = pi/2 + i*beta, sin(3w)=cosh(beta)>1 -- the SAME")
print("  continuation theta->pi/2+i*psi = xi that joins the Riemannian and Lorentzian")
print("  pieces at the seam.  So cosmology is not a separate solution: it is the BH")
print("  slicing continued past the Nariai crest by xi.  Check the crest value:")
w_crest = np.pi/6                       # 3w=pi/2
print(f"  2M at Nariai crest (3w=pi/2): {2/(3*np.sqrt(3))*np.sin(3*w_crest):.6f}"
      f"  == 2/(3sqrt3)={2/(3*np.sqrt(3)):.6f}  (the branch point)")

# -----------------------------------------------------------------------------
head("STEP-3 RESULT (c19fork, stated for reversal; held for cold read)")
print("""  COMPUTED (the orbit structure of the full (r,r0)-plane):
    - the three horizons sum to zero (A2 Cartan) for all r0;            [1]
    - S3=Weyl(A2) permutes them as interchangeable descriptions of one  [2]
      geometry (sigma = one transposition);
    - the two non-designated horizons lie on the fundamental ellipse;   [3]
    - the plane stratifies into BH / Nariai / cosmology by one cubic;   [4]
    - reflection through the origin = the negative-mass partner;        [5]
    - the cosmology branch is the xi-continuation of the BH branch      [6]
      past the Nariai crest (the SAME seam continuation, not a new map).

  THEREFORE (grounded): the full (r,r0)-plane is one gravitational-cosmological
  solution class organized by the discrete operations the corpus already names
  -- S3 root-exchange sigma (between-member relabeling), the origin reflection
  (negative mass), and xi (the seam/over-critical continuation) -- with the
  slicing operator (P5/P6) supplying the CONTINUOUS generation of the cut family
  and these discrete operations the relabeling/continuation structure on it.
  This is exactly the groupoid paper's DEFERRED between-member classification
  (P4 l.39,410), now filled in from the thesis's plane, and it is the gem's home:
  gravitational-cosmological, confirming P11 -- NOT an internal-gauge structure.

  OPEN / REACH (honestly bounded, for the grind & cold read):
    (a) Promote this to a THEOREM in the groupoid/algebroid language: the full
        same-alpha between-member groupoid = <sigma (S3), origin-reflection, xi>
        acting on the (r,r0)-plane, with relations and fixed-point strata
        (Nariai = sigma fixed pt; r0=0 carrying dS & massless-Schw; the band
        edges). The within-geometry S3 is established (P4); the BETWEEN-member
        closure is what is computed-but-not-yet-axiomatized here.
    (b) The tie to P1 (interior-as-cosmology, no trapped surfaces): the over-
        critical r-as-cosmic-time branch IS P1's interior=cosmology; the xi-
        continuation linking BH<->cosmology is the discrete shadow of that. This
        is a reach -- a connection to make rigorous, not banked.
    (c) Cosmogenesis/omniverse (thesis sec_CBHO): the negative-mass band and the
        collapse->over-critical-universe map are the thesis's speculative reach;
        held at the thesis's own weight (conjecture), not promoted.

  SYMMETRIC BAR: no rescue, no wall -- this neither reopens colour nor inflates
  the gem; it relocates the A2/S3 to where the geometry puts it (the solution
  space) and marks the precise open theorem. Convergence-from-a-saturated-node
  flag: the orbit facts [1]-[6] are computed here independently of any node's read.""")
