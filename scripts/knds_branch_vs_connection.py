import numpy as np, itertools
# ---- P10's exact grading test (from f1_per_stratum_subalgebra_id.py) ----
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
def grade(hkeys):
    h=[gens[k] for k in hkeys]; m=[gens[p] for p in pairs if p not in hkeys]
    if not is_subalg(h): return f"dim {len(hkeys)}: NOT a subalgebra"
    mm_in_h=all(span_ok(comm(X,Y),h) for X in m for Y in m)
    return f"dim {len(hkeys)}: SUBALGEBRA, [m,m]<=h ? {'SYMMETRIC (connection ZERO)' if mm_in_h else 'NON-symmetric (connection NONZERO)'}"

print("CANDIDATE ISOTROPIES (cut-fixing subalgebra of so(5,1)) and the connection (grading) test:")
cands = {
 "Type O   dS vacuum         so(4,1)            ": [(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)],
 "SdS generic  R_t x SO(3)                      ": [(0,1),(3,4),(3,5),(4,5)],
 "SdS NARIAI   SO(2,1)x SO(3)  [branch+spherical]": [(0,1),(0,2),(1,2),(3,4),(3,5),(4,5)],
 "KdS generic  R_t x SO(2)                      ": [(0,1),(3,4)],
 "KdS EXTREMAL SO(2,1)x SO(2)  [branch+rotating]": [(0,1),(0,2),(1,2),(3,4)],
}
for name,h in cands.items():
    print(f"  {name}: {grade(h)}")

# ---- enumerate ALL block-symmetric pairs of so(5,1): which dims are SYMMETRIC? ----
print("\nSYMMETRIC-PAIR DIMENSIONS of so(5,1) (block involutions split R^{5,1}=V+ + V-):")
sym_dims=set()
idx=list(range(6))
seen=set()
for k in range(0,7):
    for V in itertools.combinations(idx,k):
        Vp=set(V); 
        key=frozenset(Vp)
        # H = so(V+) + so(V-): generators L_ab with {a,b}⊂V+ or {a,b}⊂Vm
        Vm=set(idx)-Vp
        hk=[p for p in pairs if (p[0] in Vp and p[1] in Vp) or (p[0] in Vm and p[1] in Vm)]
        h=[gens[p] for p in hk]
        if not is_subalg(h): continue
        m=[gens[p] for p in pairs if p not in hk]
        if all(span_ok(comm(X,Y),h) for X in m for Y in m):
            sym_dims.add(len(hk))
print("   symmetric isotropy dimensions =", sorted(sym_dims), "  (P10 reports {6,7,10})")
print("   dim of SO(2,1)xSO(3) (SdS Nariai) = 6  in set ->", 6 in sym_dims)
print("   dim of SO(2,1)xSO(2) (KdS extremal)= 4  in set ->", 4 in sym_dims)

# ---- Kerr-dS horizon function: does it have degenerate-horizon (double-root) branch points? ----
import sympy as sp
r,Ma,a,al = sp.symbols('r M a alpha', positive=True)
Delta_r = (r**2+a**2)*(1-r**2/al**2) - 2*Ma*r      # KdS radial horizon function (Lambda=3/al^2)
print("\nKerr-dS Delta_r =", sp.expand(Delta_r), " (quartic in r; horizons at Delta_r=0)")
disc = sp.discriminant(sp.expand(Delta_r*(-al**2)), r)   # discriminant -> branch (double-root) locus
print("Delta_r discriminant in r factorizes (branch locus = where two horizons coincide):")
print("   ", sp.factor(disc))
