import sympy as sp
# F3 grounding: the coset metric of dS_5 = SO(5,1)/SO(4,1) is Lorentzian 5-dim,
# distinct from the Riemannian 3-metric h^{ab}. Compute the Killing form on the coset m.
# so(5,1): generators M_{AB}, A,B=0..5, ambient metric eta = diag(-1,1,1,1,1,1) (signature (5,1)).
eta = sp.diag(-1,1,1,1,1,1)
n=6
def M(a,b):
    # generator M_{ab}: (M_{ab})^i_j = eta_{a j} delta^i_b - eta_{b j} delta^i_a  (acts on R^6)
    G=sp.zeros(n,n)
    for i in range(n):
        for j in range(n):
            G[i,j]=eta[a,j]*(1 if i==b else 0) - eta[b,j]*(1 if i==a else 0)
    return G
# basis of so(5,1): M_{ab}, a<b
basis=[(a,b) for a in range(n) for b in range(a+1,n)]   # 15 generators
mats=[M(a,b) for (a,b) in basis]
# coset m = boosts/rotations mixing the 5th index (point stabilizer SO(4,1) fixes X_5 axis):
# h = so(4,1) = M_{ab} with a,b in {0,1,2,3,4}; m = M_{a5}, a in {0..4}  (5 generators)
m_idx=[k for k,(a,b) in enumerate(basis) if b==5]
h_idx=[k for k,(a,b) in enumerate(basis) if b!=5]
print("dim m =",len(m_idx)," dim h =",len(h_idx))
# Killing form B(X,Y)=tr(ad_X ad_Y). Build structure constants via commutators in this rep,
# but Killing form is rep-independent up to scale; use B(X,Y)=tr(ad_X ad_Y).
def comm(A,B): return A*B-B*A
N=len(mats)
# express [mats[i],mats[j]] in the basis -> structure constants f[i][j][k]
def coords(X):
    # solve X = sum c_k mats[k]; basis is linearly independent, match entries
    cs=[]
    used=X.copy()
    for k,(a,b) in enumerate(basis):
        # coefficient of M_{ab}: entry (b,a) of generator M_{ab} is eta[a,a]; read off
        # simpler: M_{ab} has (i,j) with i=b,j=a term eta[a,a]; use that slot
        c=used[b,a]/ (eta[a,a]) if eta[a,a]!=0 else used[b,a]
        cs.append(sp.simplify(c))
    return cs
# structure constants
f=[[None]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        f[i][j]=coords(comm(mats[i],mats[j]))
# ad_X matrix in basis: (ad_i)_{k j} = f[i][j][k]
def ad(i):
    A=sp.zeros(N,N)
    for j in range(N):
        for k in range(N):
            A[k,j]=f[i][j][k]
    return A
ads=[ad(i) for i in range(N)]
def B(i,j): return sp.simplify((ads[i]*ads[j]).trace())
# Killing form on m
Bm=sp.Matrix([[B(m_idx[i],m_idx[j]) for j in range(len(m_idx))] for i in range(len(m_idx))])
print("Killing form on coset m:")
sp.pprint(Bm)
eigs=Bm.eigenvals()
print("eigenvalues (value:multiplicity):",eigs)
vals=[]
for v,mult in eigs.items():
    vals += [sp.sign(v)]*mult
pos=sum(1 for s in vals if s==1); neg=sum(1 for s in vals if s==-1)
print(f"signature of coset metric: ({pos} positive, {neg} negative)  -> Lorentzian 5-dim" if (pos==4 and neg==1) or (pos==1 and neg==4) else f"signature ({pos},{neg})")
print("vs the HDA structure function h^{ab}: Riemannian inverse spatial 3-metric, signature (3,0).")
