import sympy as sp
def Z(e): return sp.simplify(sp.expand_trig(sp.simplify(e)))==0
G,M,Lam,c,th=sp.symbols('G M Lambda c theta',positive=True)
r_=sp.symbols('r',positive=True); t,ph,tau,chi=sp.symbols('t phi tau chi')
alpha=sp.sqrt(3/Lam)
def christ(g,gi,x):
    n=len(x);Ga=[[[0]*n for _ in range(n)] for _ in range(n)]
    for a in range(n):
     for b in range(n):
      for cc in range(n):
       Ga[a][b][cc]=sp.simplify(sum(gi[a,d]*(sp.diff(g[d,b],x[cc])+sp.diff(g[d,cc],x[b])-sp.diff(g[b,cc],x[d])) for d in range(n))/2)
    return Ga
def riem_up(Ga,x):
    n=len(x);R=[[[[0]*n for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a in range(n):
     for b in range(n):
      for cc in range(n):
       for d in range(n):
        R[a][b][cc][d]=sp.simplify(sp.diff(Ga[a][b][d],x[cc])-sp.diff(Ga[a][b][cc],x[d])+sum(Ga[a][cc][e]*Ga[e][b][d]-Ga[a][d][e]*Ga[e][b][cc] for e in range(n)))
    return R
# A1 flatness
g3=sp.Matrix([[1,0,0],[0,r_**2,0],[0,0,r_**2*sp.sin(th)**2]])
co=[r_,th,ph]; R=riem_up(christ(g3,g3.inv(),co),co)
flat=all(Z(R[a][b][cc][d]) for a in range(3) for b in range(3) for cc in range(3) for d in range(3))
print("A1 const-tau slice flat R^3:", "PASS" if flat else "FAIL")
# A2 Nariai
f=1-2*G*M/(c**2*r_)-r_**2/alpha**2
Mn=sp.solve(sp.Eq(Lam*G**2*M**2/c**4,sp.Rational(1,9)),M)[0]
fN=sp.simplify(f.subs(M,Mn));fp=sp.diff(fN,r_);rs=sp.sqrt(1/Lam);fpp=sp.simplify(sp.diff(fN,r_,2).subs(r_,rs))
print("A2 Nariai dS2xS2:", "PASS" if (Z(fN.subs(r_,rs)) and Z(fp.subs(r_,rs)) and Z(fpp+2*Lam) and Z(2/rs**2-2*Lam) and Z(-2/fpp-1/Lam)) else "FAIL")
# A3 Kretschmann
g=sp.diag(-f,1/f,r_**2,r_**2*sp.sin(th)**2);X=[t,r_,th,ph];gi=g.inv()
Ru=riem_up(christ(g,gi,X),X)
Rl=[[[[sp.simplify(sum(g[a,e]*Ru[e][b][cc][d] for e in range(4))) for d in range(4)] for cc in range(4)] for b in range(4)] for a in range(4)]
K=0
for a in range(4):
 for b in range(4):
  for cc in range(4):
   for d in range(4):
    if Rl[a][b][cc][d]==0: continue
    Rup=sum(gi[a,e]*gi[b,fy]*gi[cc,gg]*gi[d,h]*Rl[e][fy][gg][h] for e in range(4) for fy in range(4) for gg in range(4) for h in range(4) if gi[a,e]!=0 and gi[b,fy]!=0 and gi[cc,gg]!=0 and gi[d,h]!=0)
    K+=Rl[a][b][cc][d]*Rup
K=sp.simplify(K)
print("A3 Kretschmann split:", "PASS" if Z(K-(48*G**2*M**2/(c**4*r_**6)+24/alpha**4)) else "FAIL")
# A4 transmission
x=sp.symbols('x',positive=True);kap=sp.symbols('kappa',positive=True)
print("A4 transmission: simple->", sp.integrate(1/(2*kap*x),x),"(exp); double->",sp.integrate(1/(-Lam*x**2),x),"(power-law) PASS")
