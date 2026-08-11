import sympy as sp
r,th=sp.symbols('r theta',positive=True)
f=sp.Function('f')(r)
# ---- 3+1 split of construction gauge ds^2 = -f dt^2 + dr^2/f + r^2 dOmega^2 ----
# lapse N=sqrt(f), shift=0, spatial 3-metric:
h=sp.diag(1/f, r**2, r**2*sp.sin(th)**2)
xs=[r,th,sp.Symbol('phi')]
hi=h.inv(); n=3
# 3-Christoffel
G=[[[sp.S(0)]*n for _ in range(n)] for _ in range(n)]
for a in range(n):
 for b in range(n):
  for c in range(n):
   G[a][b][c]=sp.simplify(sum(hi[a,e]*(sp.diff(h[e,b],xs[c])+sp.diff(h[e,c],xs[b])-sp.diff(h[b,c],xs[e])) for e in range(n))/2)
# 3-Ricci
Ric=sp.zeros(n,n)
for b in range(n):
 for c in range(n):
  s=sum(sp.diff(G[a][b][c],xs[a])-sp.diff(G[a][b][a],xs[c]) for a in range(n))
  s+=sum(G[a][a][e]*G[e][b][c]-G[a][c][e]*G[e][b][a] for a in range(n) for e in range(n))
  Ric[b,c]=sp.simplify(s)
R3=sp.simplify(sum(hi[i,j]*Ric[i,j] for i in range(n) for j in range(n)))
print("3-Ricci scalar R^(3) =", R3)
print("check R^(3) == (2/r^2)(1 - f - r f') :", sp.simplify(R3-(2/r**2)*(1-f-r*sp.diff(f,r)))==0)

# ---- Hamiltonian constraint with K_ij=0 (static slice): R^(3) - 2*Lambda = 16*pi*rho ----
Lam,m=sp.symbols('Lambda',positive=True), sp.Function('m')(r)
Lam=sp.Symbol('Lambda',positive=True)
fSdS=1-2*m/r-Lam*r**2/3
R3_sds=sp.simplify(R3.subs(f,fSdS).doit())
rho=sp.simplify((R3_sds-2*Lam)/(16*sp.pi))
print("\nWith f = 1 - 2m(r)/r - Lambda r^2/3:")
print("  R^(3) =", sp.simplify(R3_sds))
print("  Hamiltonian constraint  rho = (R^(3)-2Lambda)/16pi =", rho)
print("  => rho == m'(r)/(4 pi r^2) :", sp.simplify(rho - sp.diff(m,r)/(4*sp.pi*r**2))==0)
