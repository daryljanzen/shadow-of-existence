"""L-163 build, step 1: the field equations of the UNPOLARIZED Gowdy-de Sitter cut."""
import sympy as sp
t,z,x,y = sp.symbols('t z x y', real=True)
X=[t,z,x,y]
psi=sp.Function('psi')(t,z); gam=sp.Function('gamma')(t,z)
om =sp.Function('omega')(t,z); R  =sp.Function('R')(t,z)
Lam=sp.Symbol('Lambda', positive=True)
E=sp.exp
g=sp.zeros(4,4)
g[0,0]=-E(2*(gam-psi)); g[1,1]=E(2*(gam-psi))
g[2,2]=E(2*psi); g[2,3]=g[3,2]=E(2*psi)*om
g[3,3]=E(2*psi)*om**2 + R**2*E(-2*psi)
gi=sp.simplify(g.inv())
def d(e,i): return sp.diff(e,X[i])
Gam=[[[sp.together(sp.expand(sum(gi[a,dd]*(d(g[dd,b],c)+d(g[dd,c],b)-d(g[b,c],dd)) for dd in range(4))/2))
       for c in range(4)] for b in range(4)] for a in range(4)]
def Ric(b,c):
    e=sum(d(Gam[a][b][c],a)-d(Gam[a][b][a],c) for a in range(4))
    e+=sum(Gam[a][a][dd]*Gam[dd][b][c]-Gam[a][c][dd]*Gam[dd][b][a] for a in range(4) for dd in range(4))
    return sp.simplify(sp.expand(e))
Rt=sp.Matrix(4,4,lambda b,c: Ric(b,c))
Rs=sp.simplify(sum(gi[a,b]*Rt[a,b] for a in range(4) for b in range(4)))
G=sp.Matrix(4,4,lambda a,b: sp.simplify(Rt[a,b]-g[a,b]*Rs/2))
EQ=sp.Matrix(4,4,lambda a,b: sp.simplify(G[a,b]+Lam*g[a,b]))
import pickle
pickle.dump({'EQ':EQ,'g':g,'Rt':Rt,'Rs':Rs}, open('eqs.pkl','wb'))
print("nonzero components of G_ab + Lambda g_ab:")
for a in range(4):
    for b in range(a,4):
        if sp.simplify(EQ[a,b])!=0: print("  (%d,%d)"%(a,b))
