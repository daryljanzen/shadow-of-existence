import sympy as sp
r,t,th,ph = sp.symbols('r t theta phi', positive=True)
A=sp.Function('A')(r); f=sp.Function('f')(r)
# Paper's two-function metric: ds^2 = -A dt^2 + dr^2/f + r^2 dOmega^2
g=sp.diag(-A, 1/f, r**2, r**2*sp.sin(th)**2)
coords=[t,r,th,ph]; gi=g.inv(); n=4
Gam=[[[sp.S(0)]*n for _ in range(n)] for _ in range(n)]
for a in range(n):
 for b in range(n):
  for c in range(n):
   Gam[a][b][c]=sp.simplify(sum(gi[a,e]*(sp.diff(g[e,b],coords[c])+sp.diff(g[e,c],coords[b])-sp.diff(g[b,c],coords[e])) for e in range(n))/2)
Ric=sp.zeros(n,n)
for b in range(n):
 for c in range(n):
  s=sum(sp.diff(Gam[a][b][c],coords[a])-sp.diff(Gam[a][b][a],coords[c]) for a in range(n))
  s+=sum(Gam[a][a][e]*Gam[e][b][c]-Gam[a][c][e]*Gam[e][b][a] for a in range(n) for e in range(n))
  Ric[b,c]=sp.simplify(s)
Rs=sp.simplify(sum(gi[i,j]*Ric[i,j] for i in range(n) for j in range(n)))
G=sp.simplify(Ric-Rs*g/2)
Gmix=sp.simplify(gi*G)  # G^mu_nu
Gtt=sp.simplify(Gmix[0,0]); Grr=sp.simplify(Gmix[1,1])
print("G^t_t =", Gtt)
print()
print("G^r_r =", Grr)
print()
# 8pi T^t_t = G^t_t = -8pi rho ; with rho-B form expect -(r f' + f -1)/r^2  (+Lambda absorbed in f)
print("G^t_t simplified (should depend on f only):", sp.simplify(Gtt))
print()
diff = sp.simplify(Grr-Gtt)   # = 8pi(p_r + rho)
print("G^r_r - G^t_t =", diff)
print()
# show it's (f/r) d/dr ln(A/f):
target = sp.simplify((f/r)*sp.diff(sp.log(A/f),r))
print("(f/r) d_r ln(A/f) =", target)
print()
print("difference (Grr-Gtt) - (f/r)d_r ln(A/f) =", sp.simplify(diff-target))
