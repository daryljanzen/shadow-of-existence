import sympy as sp
U,V,y=sp.symbols('U V y'); X=[U,V,y]
def cotton(w):
    g=sp.Matrix([[0,-sp.Rational(1,2),0],[-sp.Rational(1,2),0,0],[0,0,w**2]]); gi=g.inv(); n=3
    Gam=[[[sum(gi[a,d]*(sp.diff(g[d,b],X[c])+sp.diff(g[d,c],X[b])-sp.diff(g[b,c],X[d])) for d in range(n))/2 for c in range(n)] for b in range(n)] for a in range(n)]
    def Riem(a,b,c,d): return sp.diff(Gam[a][b][d],X[c])-sp.diff(Gam[a][b][c],X[d])+sum(Gam[a][c][e]*Gam[e][b][d]-Gam[a][d][e]*Gam[e][b][c] for e in range(n))
    Ric=sp.Matrix(n,n,lambda b,d: sp.simplify(sum(Riem(a,b,a,d) for a in range(n))))
    R=sp.simplify(sum(gi[i,j]*Ric[i,j] for i in range(n) for j in range(n)))
    S=sp.Matrix(n,n,lambda i,j: Ric[i,j]-R*g[i,j]/4)  # Schouten in 3D: Ric - R g/(2(n-1))
    def cov(i,j,k): return sp.diff(S[i,j],X[k])-sum(Gam[l][k][i]*S[l,j]+Gam[l][k][j]*S[i,l] for l in range(n))
    C={}
    for i in range(n):
      for j in range(n):
        for k in range(n):
          c=sp.simplify(cov(i,j,k)-cov(i,k,j))
          if c!=0: C[(i,j,k)]=c
    return Ric,C
for w in [sp.exp(U*V), 1+U**2, sp.exp(V), sp.cosh(V), 2+sp.sin(V), sp.exp(U+V)]:
    Ric,C=cotton(w); print(w, 'Ric0' if Ric==sp.zeros(3,3) else 'Ric≠0', 'Cotton:', dict(list(C.items())[:3]))
