import numpy as np, itertools
# so(5,1): generators M_{AB}, A<B, on R^{5,1} with metric eta=diag(-,+,+,+,+,+)? Convention: the
# ambient M^6 for dS_5 has signature (5,1): five spacelike (0..4) + one timelike (5)? The paper writes
# so(5,1). Take eta = diag(+,+,+,+,+,-) with indices 0,1,2,3,4,5 and the TIMELIKE direction = 5.
# (dS_5 hyperboloid X.X=+alpha^2 in this signature.) M_{AB} generate so(5,1).
eta = np.diag([1,1,1,1,1,-1]).astype(float)
idx = list(range(6))
pairs = [(A,B) for A in idx for B in idx if A<B]   # 15 generators
def M(A,B):
    # (M_{AB})^C_D = eta_{A D} delta^C_B - eta_{B D} delta^C_A  (so(p,q) generator, mixed form)
    G = np.zeros((6,6))
    for C in range(6):
        for D in range(6):
            G[C,D] = eta[A,D]*(1 if C==B else 0) - eta[B,D]*(1 if C==A else 0)
    return G
gens = {p:M(*p) for p in pairs}
def comm(X,Y): return X@Y - Y@X
def as_combo(Z):
    # express Z in the M_{AB} basis: coeff_{AB} = something; solve least-squares over the 15 basis mats
    B = np.array([gens[p].flatten() for p in pairs]).T
    c,_,_,_ = np.linalg.lstsq(B, Z.flatten(), rcond=None)
    return {pairs[i]:round(c[i],6) for i in range(len(pairs)) if abs(c[i])>1e-9}

# check the specific bracket the paper cites: [M_{05},M_{15}] = -M_{01}
c = as_combo(comm(gens[(0,5)], gens[(1,5)]))
print("[M_05, M_15] =", c, "  (paper: = -M_01)")

# symmetric-space split so(5,1)=h+m, h=so(4,1) fixing the leaf.
# The leaf-fixing subalgebra at a symmetric cut: so(4,1) = rotations/boosts among {0,1,2,3,5} say,
# and m = the 5 coset directions M_{A4}, A in {0,1,2,3,5} (the '4' direction = the normal carrying leaf to leaf).
# (Any choice of the split index works; pick the normal = axis 4.)
normal = 4
h_pairs = [p for p in pairs if normal not in p]      # so(4,1): the 10 gens not touching axis 4
m_pairs = [p for p in pairs if normal in p]           # 5 coset gens M_{A4}
print(f"\ndim h = {len(h_pairs)} (want 10, so(4,1)); dim m = {len(m_pairs)} (want 5, coset)")

def in_span(Z, plist):
    if not plist: return np.allclose(Z,0)
    B = np.array([gens[p].flatten() for p in plist]).T
    c,res,rk,_ = np.linalg.lstsq(B, Z.flatten(), rcond=None)
    recon = (B@c).reshape(6,6)
    return np.allclose(recon, Z, atol=1e-8)

# test the three symmetric-space inclusions
def test(plistX, plistY, target, label):
    ok=True; examples=[]
    for px in plistX:
        for py in plistY:
            if px==py: continue
            Z = comm(gens[px], gens[py])
            if not in_span(Z, target):
                ok=False; examples.append((px,py))
    print(f"  [{label}] closes into target: {ok}", ("" if ok else f" FAIL e.g. {examples[:2]}"))
    return ok

print("\nSymmetric-space grading tests:")
test(h_pairs, h_pairs, h_pairs, "h,h] ⊂ h")
test(h_pairs, m_pairs, m_pairs, "h,m] ⊂ m")
test(m_pairs, m_pairs, h_pairs, "m,m] ⊂ h")   # <-- the key one: two coset dirs bracket into isotropy

# m is NOT a subalgebra: show [m,m] has nonzero h-component (generic)
Z = comm(gens[m_pairs[0]], gens[m_pairs[1]])
print("\n  sample [m,m] element", m_pairs[0], m_pairs[1], "=", as_combo(Z), "-> lands in h (not m), so m not a subalgebra ✓")

# coset metric signature: Killing form restricted to m. B(X,Y)=tr(ad_X ad_Y). Compute on m basis.
allp = pairs
def ad(p):
    A = np.zeros((15,15))
    for j,q in enumerate(allp):
        Z = comm(gens[p], gens[q])
        # coords of Z in basis
        Bm = np.array([gens[r].flatten() for r in allp]).T
        c,_,_,_ = np.linalg.lstsq(Bm, Z.flatten(), rcond=None)
        A[:,j] = c
    return A
adm = {p:ad(p) for p in m_pairs}
K = np.zeros((5,5))
for i,pi in enumerate(m_pairs):
    for j,pj in enumerate(m_pairs):
        K[i,j] = np.trace(adm[pi]@adm[pj])
evals = np.linalg.eigvalsh(K)
sig = (int(np.sum(evals>1e-9)), int(np.sum(evals<-1e-9)))
print(f"\n  Killing form on coset m: eigenvalue signs -> ({sig[0]} positive, {sig[1]} negative)")
print(f"  => coset metric signature (1,4) or (4,1) [Lorentzian]:", sorted(sig)==[1,4])
