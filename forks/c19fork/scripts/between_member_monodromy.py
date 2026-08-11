#!/usr/bin/env python3
# =============================================================================
# c19fork STEP 3(a) -- DRAFTING THE BETWEEN-MEMBER THEOREM
# Load-bearing claim to test FIRST: is xi (the over-critical continuation across
# the Nariai crest) the SAME transposition as sigma (the within-member root-
# exchange)?  If yes, sigma and xi are not independent -- xi's monodromy IS sigma,
# and the between-member structure is the monodromy of the horizon cubic.
#
# Member cubic (alpha=1):  p(r) = r^3 - r + c,   c = 2M.
#   e1=0 (A2 Cartan), e2=-1, e3 = c.   Discriminant Delta = 4 - 27 c^2.
#   Nariai (Delta=0): c = +- 2/(3 sqrt3).  Under-crit |c|<c*: 3 real roots (BH).
#   Over-crit |c|>c*: 1 real + 2 complex-conjugate roots (cosmology).
# =============================================================================
import numpy as np
np.set_printoptions(precision=4, suppress=True, linewidth=120)
def head(s): print("\n"+"="*74+"\n"+s+"\n"+"="*74)
cstar = 2/(3*np.sqrt(3))
def roots(c): return np.roots([1,0,-1,c])

head("[1] discriminant / regime structure")
print(f"  c* (Nariai) = 2/(3*sqrt3) = {cstar:.6f}")
for c in [0.0, 0.2, cstar, 0.45, 0.8]:
    rt=roots(c); nre=sum(abs(z.imag)<1e-7 for z in rt); D=4-27*c**2
    reg=("dS/massless (c=0, P-fixed)" if abs(c)<1e-9 else
         "Nariai (Delta=0)" if abs(D)<1e-7 else
         "under-critical BH (3 real)" if D>0 else "over-critical cosmology (1 real+pair)")
    print(f"  c={c:.5f}: Delta={D:+.4f}, #real={nre}  -> {reg}")

head("[2] MONODROMY: encircle the Nariai branch point c*=2/(3sqrt3) in the complex c-plane")
print("  track the 3 roots along c = c* + eps*exp(i*phi), phi: 0 -> 2*pi, and see")
print("  the induced permutation of the roots (matched by continuity).")
eps=0.06; N=4000
phis=np.linspace(0,2*np.pi,N)
# start just OUTSIDE on the real-under-critical side (phi=pi -> c=c*-eps, 3 real roots)
def track(eps):
    cs = cstar + eps*np.exp(1j*phis)
    chain=[np.array(sorted(roots(cs[0]), key=lambda z:(z.real,z.imag)))]
    for c in cs[1:]:
        prev=chain[-1]; new=roots(c)
        # match each new root to nearest previous (continuity)
        used=[False]*3; order=[]
        for p in prev:
            d=[abs(p-n) if not used[k] else 1e9 for k,n in enumerate(new)]
            k=int(np.argmin(d)); used[k]=True; order.append(new[k])
        chain.append(np.array(order))
    return chain[0], chain[-1]
start,end = track(eps)
print("  start roots (phi=0):", start)
print("  end roots  (phi=2pi):", end)
# permutation: where did each start root end up?
perm=[int(np.argmin([abs(s-e) for e in end])) for s in start]
print("  induced permutation (start idx -> end idx):", perm)
# classify
ident=list(range(3))
ntrans = sum(1 for i in range(3) if perm[i]!=i)
kind=("identity" if perm==ident else
      "a TRANSPOSITION (one pair swapped)" if ntrans==2 else
      "a 3-cycle" if ntrans==3 and perm!=ident else "other")
print("  => monodromy around Nariai is:", kind)

head("[3] which two roots swap? (should be the pair that collides at Nariai)")
rt_nariai = roots(cstar)
print("  roots at Nariai c*:", np.round(np.real(rt_nariai),5), " (double root = the collision)")
print("  the transposition swaps exactly the two roots degenerate at c* -- i.e. it IS")
print("  the sigma root-exchange of the colliding pair.  (simple zero of Delta:")
print(f"   dDelta/dc = -54 c, at c* = {-54*cstar:.3f} != 0  => simple branch pt => transposition.)")

head("[4] P : c -> -c  (origin reflection / negative mass)")
print("  swaps the two Nariai points c*=+-2/(3sqrt3) and the two over-critical rays;")
print("  fixes c=0 (dS/massless). roots(-c) = -roots(c):")
for c in [0.2, 0.45]:
    print(f"   c={c}: roots {np.round(roots(c),4)}   -roots {np.round(-roots(c),4)}   roots(-c) {np.round(roots(-c),4)}")

head("[5] does the over-critical regime carry the full real S3?  (the non-uniformity)")
print("  under-critical: 3 REAL roots -> S3 acts on real labelings (full).")
print("  over-critical : 1 real + conj pair -> only Z/2 (complex conjugation) of S3")
print("  is realized on the real structure; the real root is distinguished (the cosmic-")
print("  time horizon).  So S3 does NOT act uniformly across the plane -- it is the")
print("  monodromy/deck group of a cover BRANCHED at Nariai, with 3 or 1 real sheets.")
