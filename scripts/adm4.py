import sympy as sp
print("="*78)
print("ADM-4: deparametrization in the E=1 / Nariai clock (sigma's fixed point)")
print("="*78)

t,r,th,ph,al,M=sp.symbols('t r theta phi alpha M',positive=True)
Lam=3/al**2
f=1-2*M/r-r**2/al**2
v=sp.sqrt(1-f)   # = sqrt(2M/r + r^2/alpha^2), the PG infall/expansion velocity

# ---- (1) the PG / E=1 foliation: lapse, shift, flat slice ----
# ds^2 = -f dtau^2 + 2 v dtau dr + dr^2 + r^2 dOmega^2
g=sp.Matrix([[-f, v,0,0],[v,1,0,0],[0,0,r**2,0],[0,0,0,r**2*sp.sin(th)**2]])
gi=sp.simplify(g.inv())
print("\n(1) PG/E=1 foliation of SdS:")
print("   det g =", sp.simplify(g.det()), " (=-1 => N=1 exactly)")
print("   lapse N = 1/sqrt(-g^tautau):  g^tautau =", sp.simplify(gi[0,0]), "-> N =", sp.simplify(1/sp.sqrt(-gi[0,0])))
print("   shift N^r = g^{tau r}/(-g^{tau tau}) =", sp.simplify(gi[0,1]/(-gi[0,0])), " (= v)")
# spatial slice tau=const: h = diag(1, r^2, r^2 sin^2) = FLAT
print("   spatial slice tau=const: h=diag(1,r^2,r^2 sin^2 th) -> flat, R^(3)=0 by construction")

# ---- comoving normal congruence: geodesic? irrotational? (Brown-Kuchar dust conditions) ----
coords=[t,r,th,ph]; n=4
Gam=[[[sp.simplify(sum(gi[a,e]*(sp.diff(g[e,b],coords[c])+sp.diff(g[e,c],coords[b])-sp.diff(g[b,c],coords[e])) for e in range(n))/2) for c in range(n)] for b in range(n)] for a in range(n)]
nlow=sp.Matrix([-1,0,0,0])               # n_mu = -N d_mu tau, N=1
nup=sp.simplify(gi*nlow)                 # n^mu
print("\n   unit normal n^mu =", [sp.simplify(x) for x in nup], " (timelike norm n.n =", sp.simplify((nlow.T*nup)[0]),")")
# acceleration a^mu = n^nu nabla_nu n^mu
a_up=[]
for mu in range(n):
    expr=sum(nup[nu]*(sp.diff(nup[mu],coords[nu])+sum(Gam[mu][nu][la]*nup[la] for la in range(n))) for nu in range(n))
    a_up.append(sp.simplify(expr))
print("   acceleration a^mu =", a_up, " -> GEODESIC (E=1 free-fallers) iff all zero")

# ---- (2) Hamiltonian constraint on the flat PG slice: K^2 - K_ij K^ij ----
# K_ij = -(1/2)(D_i N_j + D_j N_i), flat 3-metric, N_r=v, N_theta=N_phi=0
h3=sp.diag(1,r**2,r**2*sp.sin(th)**2); x3=[r,th,ph]; h3i=h3.inv()
G3=[[[sp.simplify(sum(h3i[a,e]*(sp.diff(h3[e,b],x3[c])+sp.diff(h3[e,c],x3[b])-sp.diff(h3[b,c],x3[e])) for e in range(3))/2) for c in range(3)] for b in range(3)] for a in range(3)]
Nlow=[v,0,0]
def covD(i,j):  # D_i N_j
    return sp.diff(Nlow[j],x3[i]) - sum(G3[k][i][j]*Nlow[k] for k in range(3))
K=sp.zeros(3,3)
for i in range(3):
    for j in range(3):
        K[i,j]=sp.simplify(-sp.Rational(1,2)*(covD(i,j)+covD(j,i)))
Kmix=sp.simplify(h3i*K); Ktr=sp.simplify(sp.trace(Kmix))
KK=sp.simplify(sum(Kmix[i,j]*Kmix[j,i] for i in range(3) for j in range(3)))
H=sp.simplify(0 + Ktr**2 - KK - 2*Lam)   # R3=0
print("\n(2) Hamiltonian constraint on the flat PG slice (R3=0):")
print("   K (expansion) =", sp.simplify(Ktr))
print("   K^2 - K_ijK^ij =", sp.simplify(Ktr**2-KK))
print("   H = R3 + K^2 - K_ijK^ij - 2Lambda =", H, " => vacuum (rho=0) for r>0; M is the point source at r=0")
print("   (the comoving reading reads M as homogeneous dust: this is the Friedmann content, evolving in tau)")

# ---- (3) the clock = sigma's fixed point; the cubic degeneracy ----
print("\n(3) the clock is sigma's fixed point, and the cubic degenerates there:")
Msym=sp.Symbol('M',positive=True)
cubic=r**3-r+2*Msym                       # gauge alpha=1, horizon cubic
disc=sp.discriminant(cubic,r)
print("   horizon cubic r^3 - r + 2M ; discriminant =", sp.simplify(disc))
Mnariai=sp.solve(sp.Eq(disc,0),Msym)
print("   discriminant = 0 at M =", Mnariai, " -> 2M =", [sp.nsimplify(2*m) for m in Mnariai if m>0])
print("   Nariai 2M = 2/(3 sqrt3) =", sp.nsimplify(2/(3*sp.sqrt(3))))
# double root at Nariai
cub_n=cubic.subs(Msym,1/(3*sp.sqrt(3)))
print("   at Nariai the cubic factors:", sp.factor(sp.nsimplify(cub_n)))
print("   double root r0 = 1/sqrt3 =", sp.nsimplify(1/sp.sqrt(3)), " = sigma's fixed point (w=pi/6).")
print("   => the standard-2d S3 irrep's carrier (the two sigma-swapped roots) MERGES exactly at the clock.")
