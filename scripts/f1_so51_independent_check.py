import numpy as np
import itertools

# ===== Independent build of so(5,1) from scratch (matrix/vector rep) =====
# Metric: index 0 timelike, 1..5 spacelike.  eta = diag(-1,+1,+1,+1,+1,+1)
eta = np.diag([-1.,1.,1.,1.,1.,1.])
N = 6

def L(a,b):
    """Generator L_{ab} of so(eta): (L_ab)^i_j = d^i_a eta_{bj} - d^i_b eta_{aj}."""
    M = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            M[i,j] = (1.0 if i==a else 0.0)*eta[b,j] - (1.0 if i==b else 0.0)*eta[a,j]
    return M

# basis: all a<b  (15 generators)
pairs = [(a,b) for a in range(N) for b in range(a+1,N)]
gens = {p: L(*p) for p in pairs}
print("dim so(5,1) =", len(pairs), "(expect 15)")

# sanity: each generator is in so(eta):  L^T eta + eta L = 0
ok = all(np.allclose(g.T@eta + eta@g, 0) for g in gens.values())
print("all generators satisfy so(eta) condition:", ok)

def comm(X,Y): return X@Y - Y@X

# ===== block involution theta_S : conjugation by D_S = diag(signs) =====
def D(S):
    s = np.array([-1.0 if i in S else 1.0 for i in range(N)])
    return np.diag(s)

def split_h_m(S):
    """Return index-lists of basis generators in h (theta=+1) and m (theta=-1)."""
    Ds = D(S)
    h, m = [], []
    for p,g in gens.items():
        th = Ds@g@Ds          # D^{-1}=D
        if np.allclose(th, g):      h.append(p)
        elif np.allclose(th,-g):    m.append(p)
        else: raise RuntimeError("not an involution eigenvector?!")
    return h, m

def is_subalgebra(idxset):
    B=[gens[p] for p in idxset]
    basis=B
    # check each commutator lies in span of basis (over reals) -> solve least squares residual
    M = np.column_stack([g.flatten() for g in basis])
    for X in B:
        for Y in B:
            c = comm(X,Y).flatten()
            coef,res,rk,sv = np.linalg.lstsq(M,c,rcond=None)
            if np.linalg.norm(M@coef - c) > 1e-9:
                return False
    return True

def in_span(vec, idxset):
    if not idxset: return np.linalg.norm(vec)<1e-9
    M=np.column_stack([gens[p].flatten() for p in idxset])
    coef,_,_,_=np.linalg.lstsq(M,vec.flatten(),rcond=None)
    return np.linalg.norm(M@coef-vec.flatten())<1e-9

def symmetric_pair_check(S):
    h,m = split_h_m(S)
    # [h,h] in h, [h,m] in m, [m,m] in h
    hh = all(in_span(comm(gens[p],gens[q]), h) for p in h for q in h)
    hm = all(in_span(comm(gens[p],gens[q]), m) for p in h for q in m)
    mm = all(in_span(comm(gens[p],gens[q]), h) for p in m for q in m)
    return len(h), len(m), hh, hm, mm

print("\n=== Symmetric subalgebra dims from block involutions |S|=k ===")
dims=set()
for k in range(0,N+1):
    for S in itertools.combinations(range(N),k):
        h,m=split_h_m(set(S))
        # proper subalgebra (exclude trivial whole-algebra k=0/k=6 giving m empty)
        if len(m)>0:
            dims.add(len(h))
print("proper symmetric-subalgebra dims found:", sorted(dims), " (claim: {6,7,10})")

print("\n=== The three named strata ===")
# Type O isotropy = so(4,1): flip one SPACELIKE coord, S={5}
hO,mO,*ckO = symmetric_pair_check({5})
print(f"Type O   S={{5}} -> dim h={hO}, dim m={mO}, [hh]in h,[hm]in m,[mm]in h = {tuple(ckO)}  (expect so(4,1) dim10, all True)")
# Nariai isotropy = so(2,1)+so(3): split {0,1,2}|{3,4,5} -> flip S={3,4,5}
hNa,mNa,*ckNa = symmetric_pair_check({3,4,5})
print(f"Nariai   S={{3,4,5}} -> dim h={hNa}, dim m={mNa}, grading = {tuple(ckNa)}  (expect dim6, all True)")

# SdS static isotropy: R_t x SO(3) = <boost M_03> + so(3) on {1,2,4}, dim 4. NOT a block-involution fixed set.
sds = [(0,3),(1,2),(1,4),(2,4)]   # <M_03> + so(3) among {1,2,4}
print("\nSdS isotropy <M_03>+so(3){1,2,4}: dim", len(sds), "is_subalgebra:", is_subalgebra(sds))
# coset = everything else
sds_coset=[p for p in pairs if p not in sds]
mm_into_h = all(in_span(comm(gens[p],gens[q]), sds) for p in sds_coset for q in sds_coset)
print("  [m,m] subset h (symmetric)?:", mm_into_h, " (claim: NO -> grading fails)")

print("\n=== Coset Killing-form signature (Type O coset, the de Sitter tangent) ===")
# Killing form ~ (N-2)*Tr(XY) in vector rep; signature of Tr(XY) on coset m_O
mvecs=[gens[(i,5)] for i in range(5)]   # coset so(5,1)/so(4,1) = M_{i5}, i=0..4 (mO above is the dim, not the pair list)
G=np.array([[np.trace(X@Y) for Y in mvecs] for X in mvecs])
evals=np.linalg.eigvalsh(G)
pos=int(np.sum(evals>1e-9)); neg=int(np.sum(evals<-1e-9))
print("coset gram (Tr XY) eigenvalues:", np.round(evals,3))
print(f"signature: ({pos} of one sign, {neg} of the other)  (claim: (1,4) Lorentzian)")
