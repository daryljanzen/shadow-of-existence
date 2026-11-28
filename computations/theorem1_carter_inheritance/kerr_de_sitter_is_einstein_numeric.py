import sympy as sp, random
t,r,th,ph=sp.symbols('t r theta phi',real=True); X=[t,r,th,ph]
a,M,lam=sp.Rational(3,7),sp.Rational(2,5),sp.Rational(1,11)
c,s=sp.cos(th),sp.sin(th)
Sig=r**2+a**2*c**2; Dth=1+lam*a**2*c**2; Xi=1+lam*a**2
gb=sp.diag(-(1-lam*r**2)*Dth/Xi, Sig/((r**2+a**2)*(1-lam*r**2)), Sig/Dth, (r**2+a**2)*s**2/Xi)
k=sp.Matrix([Dth/Xi, Sig/((r**2+a**2)*(1-lam*r**2)), 0, -a*s**2/Xi])
g=gb+(2*M*r/Sig)*k*k.T
gi=g.inv()
G=[[[sum(gi[i,l]*(sp.diff(g[l,j],X[kk])+sp.diff(g[l,kk],X[j])-sp.diff(g[j,kk],X[l])) for l in range(4))/2 for kk in range(4)] for j in range(4)] for i in range(4)]
worst=0
for trial in range(4):
    pt={r:sp.Rational(random.randint(11,29),10), th:sp.Rational(random.randint(2,13),10)}
    for i in range(4):
        for j in range(i,4):
            Rij=sum(sp.diff(G[l][i][j],X[l]) - sp.diff(G[l][i][l],X[j]) + sum(G[l][l][m]*G[m][i][j]-G[l][j][m]*G[m][i][l] for m in range(4)) for l in range(4))
            v=abs(sp.N((Rij-3*lam*g[i,j]).subs(pt),30)); worst=max(worst,v)
print('max |R_ab - Lambda g_ab| over 4 points, all components:', worst)
