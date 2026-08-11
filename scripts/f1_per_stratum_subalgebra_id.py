import numpy as np, itertools
eta=np.diag([-1.,1.,1.,1.,1.,1.]); N=6
def L(a,b):
    M=np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            M[i,j]=(1.0 if i==a else 0)*eta[b,j]-(1.0 if i==b else 0)*eta[a,j]
    return M
pairs=[(a,b) for a in range(N) for b in range(a+1,N)]
gens={p:L(*p) for p in pairs}
def comm(X,Y): return X@Y-Y@X
def span_ok(vec,B):
    if not B: return np.linalg.norm(vec)<1e-9
    Mx=np.column_stack([g.flatten() for g in B]); c,*_=np.linalg.lstsq(Mx,vec.flatten(),rcond=None)
    return np.linalg.norm(Mx@c-vec.flatten())<1e-9
def is_subalg(B): return all(span_ok(comm(X,Y),B) for X in B for Y in B)
def grading(hkeys):
    h=[gens[k] for k in hkeys]; m=[gens[p] for p in pairs if p not in hkeys]
    if not is_subalg(h): return "NOT a subalgebra"
    mm_in_h=all(span_ok(comm(X,Y),h) for X in m for Y in m)  # [m,m] subset h ?
    return "SYMMETRIC (grading holds)" if mm_in_h else "non-symmetric (grading fails)"

# P6 sweep-subgroups realized in so(5,1) (X0 timelike; X1..X5 spacelike), read from P6 sec.51/65/97/159:
strata = {
 "Type O   dS/FLRW vacuum   so(4,1)":        [(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)],  # block S={5}
 "Type D   SdS   R_t x SO(3)":               [(0,1),(3,4),(3,5),(4,5)],            # boost M01 (+) so(3)_345
 "Type D   Nariai   SO(2,1) x SO(3)":        [(0,1),(0,2),(1,2),(3,4),(3,5),(4,5)],# so(2,1)_012 (+) so(3)_345  (block S={3,4,5})
 "Type D   Kerr-dS   R x SO(2)":             [(0,1),(3,4)],                        # boost (+) so(2)_34
 "Type I   Bianchi I   3 KV (abelian)":      None,  # handled specially (translations, not so(N) rotations)
 "Type I   Zipoy/Weyl   R x SO(2)":          [(0,1),(3,4)],
 "wall     Type N":                          [],
}
print(f"{'stratum':<40}{'dim':<5}{'subalgebra?':<14}grading")
for name,keys in strata.items():
    if keys is None:
        # Bianchi I: 3 commuting spacelike translations. In so(5,1) the abelian translations of an E(3)-type
        # subgroup are null-rotation generators N_i = M_{0i}+M_{1i} (i=2,3,4): nilpotent, mutually commuting.
        Nn=[gens[(0,i)]+gens[(1,i)] for i in (2,3,4)]
        sub=is_subalg(Nn)
        mm=all(span_ok(comm(X,Y),Nn) for X in Nn for Y in Nn)
        # symmetric needs an involution with these as h and complement m closing back; abelian dim3 not in {6,7,10}
        print(f"{name:<40}{3:<5}{('yes' if sub else 'NO'):<14}{'abelian; dim 3 not in {6,7,10} -> non-symmetric' if sub else '—'}")
        continue
    d=len(keys)
    print(f"{name:<40}{d:<5}{('yes' if is_subalg([gens[k] for k in keys]) else 'NO'):<14}{grading(set(keys))}")
print("\nSummary: clean symmetric-space grading survives at {Type O, Nariai} only;")
print("generic D/I/wall non-symmetric -> structure function genuinely varies (the algebroid connection).")
