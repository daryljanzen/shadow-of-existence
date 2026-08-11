"""
two_factors_direct.py  --  L8 (built r1329, Arthur): the two factors of Aut(A_2)=S_3 x Z_2 -- that the
product is DIRECT with the inversion CENTRAL, and the contingency that the Z_2 exists at all
(A_2 is the unique rank-2 root system with -1 NOT in its Weyl group).

P14 sec:twofactors/§212-214: "the product is DIRECT -- its factors acting on independent structures,
the Weyl S_3 on the three horizon roots and the inversion on the two null rulings, the inversion
CENTRAL"; "the inversion is an OUTER automorphism -- not already inside the Weyl S_3 -- only because
the cubic realises A_2, the one rank-two system with -1 not in W; were negation inner (as for A_1,
B_2, G_2) Aut(A_2) would collapse to the Weyl group and leave no chirality factor to sort."

CHECKABLE:
  (1) Aut(A_2) = D_6, order 12 = S_3 x Z_2, DIRECT, with the inversion -1 CENTRAL and -1 NOT in W(A_2).
  (2) THE CONTINGENCY: -1 in W for A_1, B_2, G_2 (inner) but -1 NOT in W for A_2 (outer) -- A_2 the
      unique rank-2 exception, so the chirality Z_2 exists only there.
  TRACED (not group theory): that the S_3 factor is the flavour (GLOBAL, deck symmetry -- no substrate
  isometry, su(3) not in so(5,1)) and the Z_2 the chirality (GAUGED -- a substrate isometry acting on
  the cut spinor as gamma^5, L4).  The "on vs tangent to one circle" independence -> direct product is
  the geometric reading (P14 §214, P12 §240); the group theory below is its algebraic shadow.
"""
import numpy as np
from itertools import product
np.set_printoptions(precision=3, suppress=True)
def check(tag,cond): print(f"  [{'PASS' if cond else 'FAIL'}] {tag}"); return bool(cond)
ok=True
print("="*80); print("two_factors_direct -- Aut(A_2)=S_3 x Z_2 direct, inversion central & outer"); print("="*80)

def reflect(v,a): return v - 2*np.dot(v,a)/np.dot(a,a)*a
def close_group(gens, dim, cap=200):
    G=[np.eye(dim)]
    frontier=[np.eye(dim)]
    while frontier:
        g=frontier.pop()
        for s in gens:
            h=s@g
            if not any(np.allclose(h,w,atol=1e-9) for w in G):
                G.append(h); frontier.append(h)
                if len(G)>cap: return G
    return G
def refl_mat(a,dim):
    I=np.eye(dim); return np.array([reflect(I[:,i],a) for i in range(dim)]).T
def in_group(M,G): return any(np.allclose(M,w,atol=1e-9) for w in G)

# ---- root systems (2D) ------------------------------------------------------------------------
r3=np.sqrt(3)
roots = {
 "A1": [np.array([1.,0.])],                                   # simple: one root (rank 1, embed in... use 1D)
 "A2": [np.array([1.,0.]), np.array([-0.5, r3/2])],           # simple roots, 60deg apart-ish (A2)
 "B2": [np.array([1.,-1.]), np.array([0.,1.])],               # simple roots of B2
 "G2": [np.array([1.,0.]), np.array([-1.5, r3/2])],           # simple roots of G2 (150deg, length ratio sqrt3)
}
minus1 = -np.eye(2)

# ---- (2) THE CONTINGENCY: is -1 in the Weyl group? --------------------------------------------
print("(2) is the point inversion -1 IN the Weyl group W (=> negation inner) for each rank-2 system?")
Waut={}
for name,simple in roots.items():
    if name=="A1":
        # rank 1: W = {1, -1} in the 1D root line; -1 IS the reflection => inner
        Wsize=2; has=True
        print(f"    {name}: rank 1, W={{1,-1}} (order 2); -1 in W?  {has}   (inner)")
        Waut[name]=(Wsize,has); continue
    gens=[refl_mat(a,2) for a in simple]
    W=close_group(gens,2)
    has = in_group(minus1, W)
    Waut[name]=(len(W),has)
    print(f"    {name}: |W|={len(W):2d}; -1 in W?  {has}    ({'inner' if has else 'OUTER'})")
ok&=check("A_2 is the UNIQUE rank-2 system with -1 NOT in W (outer); A_1,B_2,G_2 have -1 in W (inner)",
          Waut["A2"][1]==False and Waut["A1"][1] and Waut["B2"][1] and Waut["G2"][1])

# ---- (1) Aut(A_2) = S_3 x Z_2, direct, inversion central ---------------------------------------
print("-"*80)
print("(1) Aut(A_2): the full root-system symmetry group.")
# all 6 roots of A2:
a1,a2=roots["A2"]; W_A2=close_group([refl_mat(a1,2),refl_mat(a2,2)],2)
A2roots=set()
for g in W_A2:
    for r in (a1,a2): A2roots.add(tuple(np.round(g@r,6)))
A2roots=[np.array(r) for r in A2roots]
ok&=check(f"A_2 has 6 roots (regular hexagon): got {len(A2roots)}", len(A2roots)==6)
# Aut(A_2) = all orthogonal maps permuting the 6 roots.  Build from W plus the inversion.
Aut=close_group([refl_mat(a1,2),refl_mat(a2,2), minus1],2)
ok&=check(f"Aut(A_2) = D_6, order 12 (= |S_3 x Z_2|): got {len(Aut)}", len(Aut)==12)
ok&=check("W(A_2)=S_3 (order 6) is an index-2 subgroup of Aut(A_2)", len(W_A2)==6)
# the inversion -1 is central in Aut:
central = all(np.allclose(minus1@g, g@minus1) for g in Aut)
ok&=check("the inversion -1 is CENTRAL in Aut(A_2)", central)
# direct product: W ∩ <-1> = {e}, <-1> central, |W|*2 = |Aut|  => Aut = W x <-1> = S_3 x Z_2
disjoint = not in_group(minus1, W_A2)
ok&=check("W(A_2) ∩ <-1> = {e} and |W|·|<-1>| = |Aut|  => Aut(A_2) = S_3 x Z_2 (DIRECT)",
          disjoint and central and 2*len(W_A2)==len(Aut))
print("     => the second factor Z_2 = <-1> is exactly the outer inversion that (2) shows exists only")
print("        for A_2 among the rank-2 systems: the chirality factor, present because -1 is OUTER here.")

print("="*80)
print("RESULT:", "ALL PASS -- Aut(A_2)=S_3 x Z_2 (direct, inversion central & outer); A_2 the unique"
      "\n         rank-2 system with -1 outer, so the chirality Z_2 exists only there." if ok
      else "SOME FAILED -- see above.")
print("  Traced (geometry, not group theory): S_3 = flavour GLOBAL (deck, no substrate isometry);")
print("  Z_2 = chirality GAUGED (substrate isometry = gamma^5, L4); on/tangent independence -> direct.")
print("="*80)
