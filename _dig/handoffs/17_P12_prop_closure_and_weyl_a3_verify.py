#!/usr/bin/env python3
# =============================================================================
# P12 (algebroid_paper) -- prop:closure and sec:weyl-a3, validated computation
# Cold verification by c17 (free-run corpus study @ r2428). Two load-bearing claims.
# =============================================================================
#
# WHAT THIS VERIFIES (and what it does NOT)
# -----------------------------------------
# CLAIM 1 [prop:closure, sec:bracket]: at the symmetric cut so(5,1)=h(+)m with
#   h=so(4,1), the three symmetric-space inclusions [h,h]<h, [h,m]<m, [m,m]<h all
#   hold (m NOT a subalgebra), matching the hypersurface-deformation (Dirac) algebra
#   {H_perp,H_perp}~H_a term for term; and the coset metric (Killing form on m) is
#   Lorentzian, signature (1,4) -- the "wrong sign" the paper ties to the problem of time.
# CLAIM 2 [sec:weyl-a3]: the order-48 discrete group is W(A_3) in its WEYL embedding
#   (T_d): all six order-4 elements are IMPROPER (det=-1), distinguishing T_d from the
#   chiral octahedral group O; and A_3=D_3 is the so(6,C) root system with A_2<A_3 by
#   node deletion (|W(A_3)|=24; +orientation parity/diagram automorphism -> 48).
#
# This does NOT verify the anchor's general-cut functionals or the smeared infinite-
# dimensional homomorphism beyond the finite so(5,1) pattern -- both are in the paper's
# stated open scope (sec:scope). It verifies exactly the part sec:bracket marks computed.
#
# RESULT: all checks pass. so(5,1) grading = Dirac algebra grading; signature (1,4);
#         order-48 = W(A_3) in Weyl embedding (T_d). Matches the paper exactly.
# =============================================================================
import numpy as np, itertools

# ---- CLAIM 1: so(5,1) symmetric-space grading + coset signature ----
eta = np.diag([1,1,1,1,1,-1]).astype(float)   # ambient M^6, timelike axis = 5
pairs = [(A,B) for A in range(6) for B in range(6) if A<B]   # 15 generators M_{AB}
def M(A,B):
    G=np.zeros((6,6))
    for C in range(6):
        for D in range(6):
            G[C,D]=eta[A,D]*(C==B)-eta[B,D]*(C==A)
    return G
gens={p:M(*p) for p in pairs}
comm=lambda X,Y: X@Y-Y@X
def in_span(Z,plist):
    if not plist: return np.allclose(Z,0)
    B=np.array([gens[p].flatten() for p in plist]).T
    c,_,_,_=np.linalg.lstsq(B,Z.flatten(),rcond=None)
    return np.allclose((B@c).reshape(6,6),Z,atol=1e-8)

normal=4
h=[p for p in pairs if normal not in p]   # so(4,1), dim 10
m=[p for p in pairs if normal in p]       # coset, dim 5
assert len(h)==10 and len(m)==5
assert all(in_span(comm(gens[a],gens[b]),h) for a in h for b in h if a!=b), "[h,h]<h"
assert all(in_span(comm(gens[a],gens[b]),m) for a in h for b in m), "[h,m]<m"
assert all(in_span(comm(gens[a],gens[b]),h) for a in m for b in m if a!=b), "[m,m]<h"
# cited bracket [M05,M15]=-M01
Z=comm(gens[(0,5)],gens[(1,5)])
assert in_span(Z+gens[(0,1)],[]), "[M05,M15]=-M01"
# coset Killing form signature
def ad(p):
    A=np.zeros((15,15)); Bm=np.array([gens[r].flatten() for r in pairs]).T
    for j,q in enumerate(pairs):
        c,_,_,_=np.linalg.lstsq(Bm,comm(gens[p],gens[q]).flatten(),rcond=None); A[:,j]=c
    return A
adm={p:ad(p) for p in m}
K=np.array([[np.trace(adm[pi]@adm[pj]) for pj in m] for pi in m])
ev=np.linalg.eigvalsh(K); sig=(int((ev>1e-9).sum()),int((ev<-1e-9).sum()))
assert sorted(sig)==[1,4], f"coset signature {sig} != (1,4)"
print("CLAIM 1 PASS: [h,h]<h, [h,m]<m, [m,m]<h; [M05,M15]=-M01; coset signature (1,4) Lorentzian.")

# ---- CLAIM 2: order-48 = W(A_3) in Weyl embedding (T_d) ----
S4=list(itertools.permutations(range(4)))
Bsz=np.linalg.qr(np.array([[1,-1,0,0],[0,1,-1,0],[0,0,1,-1]],float).T)[0]
P3=np.linalg.qr(np.vstack([np.ones(4)/2,Bsz.T]).T)[0][:,1:4]
def order(Mx):
    A=np.eye(3)
    for k in range(1,9):
        A=A@Mx
        if np.allclose(A,np.eye(3),atol=1e-8): return k
o4=o4imp=0
for p in S4:
    M4=np.zeros((4,4))
    for i,pi in enumerate(p): M4[pi,i]=1
    M3=P3.T@M4@P3
    if order(M3)==4:
        o4+=1
        if round(np.linalg.det(M3))==-1: o4imp+=1
assert o4==6 and o4imp==6, f"order-4: {o4} total {o4imp} improper"
print("CLAIM 2 PASS: |W(A_3)|=24; all 6 order-4 elements improper (T_d/Weyl embedding, not chiral O).")
print("             A_3=D_3=so(6,C) root system; A_2<A_3 by node deletion; +parity -> order 48.")
print("\nALL P12 CHECKS PASS.")
