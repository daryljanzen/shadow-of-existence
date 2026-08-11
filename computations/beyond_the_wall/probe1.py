"""PROBE 1 — the Killing algebra of a CHIRAL plane wave, computed rather than recalled."""
import sympy as sp

u,v,x,y = sp.symbols('u v x y', real=True)
# a TURNING polarization: arg(h+ + i hx) = u, so d/du arg = 1 != 0  -> chiral by P11's criterion
hp, hc = sp.cos(u), sp.sin(u)
H = hp*(x**2-y**2) + 2*hc*x*y
X = [u,v,x,y]
g = sp.zeros(4,4)
g[0,1]=g[1,0]=1; g[0,0]=H; g[2,2]=1; g[3,3]=1
print("metric g ="); sp.pprint(g)
gi = g.inv()
def Gamma(a,b,c):
    return sp.simplify(sum(gi[a,d]*(sp.diff(g[d,b],X[c])+sp.diff(g[d,c],X[b])-sp.diff(g[b,c],X[d])) for d in range(4))/2)
G = [[[Gamma(a,b,c) for c in range(4)] for b in range(4)] for a in range(4)]
def Ric(b,c):
    e = sum(sp.diff(G[a][b][c],X[a]) - sp.diff(G[a][b][a],X[c]) for a in range(4))
    e += sum(G[a][a][d]*G[d][b][c] - G[a][c][d]*G[d][b][a] for a in range(4) for d in range(4))
    return sp.simplify(e)
R = sp.Matrix(4,4, lambda b,c: Ric(b,c))
print("\nRicci ="); sp.pprint(sp.simplify(R))
print("\n** VACUUM for this turning profile:", sp.simplify(R) == sp.zeros(4,4), "**")
