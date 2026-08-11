import sympy as sp

print("="*78)
print("F1 explicit restriction (signature level): the (1,4) coset metric -> the HDA")
print("structure function data (the ε and h^{ab}). The HDA carries ε h^{ab}: an indefinite")
print("SIGN ε (the problem-of-time / vantage) times a Riemannian spatial metric h^{ab}.")
print("Claim (C12-F3, reduced identification): BOTH are read off the one (1,4) coset metric")
print("of dS5 = SO(5,1)/SO(4,1) -- ε is its timelike (vantage) direction's sign, h^{ab} its")
print("spacelike (Riemannian) block. Compute the per-direction Killing form to show it.")
print("="*78)

eta = sp.diag(-1,1,1,1,1,1)   # ambient (5,1): index 0 timelike, 1..5 spacelike
n=6
def gen(a,b):
    G=sp.zeros(n,n)
    for i in range(n):
        for j in range(n):
            G[i,j]=eta[a,j]*(1 if i==b else 0) - eta[b,j]*(1 if i==a else 0)
    return G
basis=[(a,b) for a in range(n) for b in range(a+1,n)]
mats=[gen(a,b) for (a,b) in basis]
def comm(A,B): return A*B-B*A
def coords(X):
    cs=[]
    for (a,b) in basis:
        c = X[b,a]/eta[a,a] if eta[a,a]!=0 else X[b,a]
        cs.append(sp.simplify(c))
    return cs
N=len(mats)
f=[[coords(comm(mats[i],mats[j])) for j in range(N)] for i in range(N)]
def ad(i):
    A=sp.zeros(N,N)
    for j in range(N):
        for k in range(N):
            A[k,j]=f[i][j][k]
    return A
ads=[ad(i) for i in range(N)]
def B(i,j): return sp.simplify((ads[i]*ads[j]).trace())

# coset m = M_{a5}, a=0..4 (point stabilizer SO(4,1) fixes the 5-axis)
m_keys=[k for k,(a,b) in enumerate(basis) if b==5]
m_labels=[f"M_{basis[k][0]}5" for k in m_keys]
Bm=sp.Matrix([[B(m_keys[i],m_keys[j]) for j in range(len(m_keys))] for i in range(len(m_keys))])
print("\n[1] Killing form on the coset m (basis M_05,M_15,M_25,M_35,M_45):")
sp.pprint(Bm)

# per-direction sign (diagonal) -> identify timelike vs spacelike coset directions
print("\n[2] per-direction signs (diagonal of the coset Killing form):")
for i,k in enumerate(m_keys):
    s = int(sp.sign(Bm[i,i]))
    a = basis[k][0]
    kind = "BOOST (mixes time index 0)" if a==0 else "rotation (spacelike-spacelike)"
    print(f"    {m_labels[i]:6s}: B = {Bm[i,i]}   sign {s:+d}   <- {kind}")
print("    => the lone opposite-sign direction is M_05, the BOOST = the de Sitter time /")
print("       vantage direction (sigma's signature axis). The other four are spacelike.")

# the reduced identification: split m = <timelike vantage> (+) <spacelike block>
tl = [i for i in range(len(m_keys)) if sp.sign(Bm[i,i])==sp.sign(Bm[0,0])]  # same sign as M_05
sl = [i for i in range(len(m_keys)) if i not in tl]
print(f"\n[3] decomposition of the (1,4) coset metric:")
print(f"    timelike/vantage sector (the ε): directions {[m_labels[i] for i in tl]}  (dim {len(tl)})")
print(f"    spacelike/Riemannian sector (the h^ab role): {[m_labels[i] for i in sl]}  (dim {len(sl)})")
Bsl = Bm[sl, sl]
eig = Bsl.eigenvals()
allpos = all(sp.sign(v)==sp.sign(Bsl[0,0]) for v in eig)
print(f"    spacelike block eigenvalues: {eig}  -> definite (Riemannian): {allpos}")

print("\n" + "="*78)
print("READING:")
print("="*78)
print("""
 [computed] The (1,4) coset metric splits cleanly into ONE timelike direction -- M_05, the
 boost = the de Sitter time / vantage axis (sigma's signature axis, adm3/P3) -- and a
 definite (Riemannian) spacelike block. So the HDA's structure function ε h^{ab} is the one
 coset metric decomposed: ε = the SIGN of its timelike/vantage direction (the problem-of-time
 obstruction), h^{ab} = its spacelike Riemannian block. This is exactly C12-F3's 'reduced
 (not naive-tensor) identification': not (3-metric) = (5-metric), but the 5-dim Lorentzian
 coset metric SUPPLYING both the ε and the spatial h^{ab} of the HDA. The vantage flip
 sigma (ε -> -ε) is the timelike direction's sign flip = exterior(hole)/interior(cosmos).

 [grounded via Move 4 -- the layering READ, not modelled] The spacelike block is 4-dim (M_15..M_45);
 the physical structure function is the 3-metric of the S^3 the universe lives on. The dS5(5D)->4D->3D
 layering is read off the geometry/background-geometry/substrate distinction (algebroid_base_and_substrate
 Move 4): SUBSTRATE dS5 -> [SLICING, codim-1, dimension-reducing] -> BACKGROUND GEOMETRY dS4 -> [ADM] -> S^3.
 So the (1,4) coset = ε (M_05 timelike, the vantage, sign set by REASSIGNMENT) (+) lift (ONE spacelike = the
 codim-1 SLICING normal, the substrate's extra dim, removed dS5->dS4) (+) h^{ab} (the 3 spacelike = the S^3,
 signature (3,0)). The two non-spatial pieces ARE the two construction operations; h^{ab} is the residue.
 The restriction (1,4) -> ε (+) h^{ab}(3,0) holds AT THE SYMMETRIC CUT, forced by the operations split.
 F1's across-C identification (h^{ab}(x) = the coset metric, all cuts) is GROUNDED AS A READING (P5/P6:
 every cut's 3-metric is the induced substrate metric) -- NOT closed/[computed] across the base. The
 symmetric-cut signature here is [computed]; the OUTSTANDING objective step is the generic-cut verification
 (is the base-varying h^{ab}(x) the cut's induced 3-metric where the isotropy is broken -- the four
 spacelike are isotropic ONLY at the symmetric cut; off {O,Nariai} the grading fails,
 f1_strata_homomorphism.py, so the identification needs the explicit induced-metric comparison, not the
 grading). That generic-cut computation is objective and does NOT depend on the open 5th-dimension geometric
 identity (Move 4, Daryl's flagged call) -- the two are distinct; conflating them was the r223 over-claim
 (corrected r224).
""")
