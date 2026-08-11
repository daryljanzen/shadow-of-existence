"""PROBE 3 — the unpolarized Gowdy cut: two spacelike Killing vectors, and no transverse reflection."""
import sympy as sp
t,th,x,y = sp.symbols('t theta x y', real=True, positive=False)
P = sp.Function('P')(t,th); Q = sp.Function('Q')(t,th); L = sp.Function('lam')(t,th)
T = sp.Symbol('t', positive=True)
X=[t,th,x,y]
# Gowdy T^3 form (unpolarized when Q != 0)
g = sp.zeros(4,4)
g[0,0] = -sp.exp(L); g[1,1] = sp.exp(L)
g[2,2] = t*sp.exp(P); g[2,3] = g[3,2] = t*sp.exp(P)*Q
g[3,3] = t*(sp.exp(P)*Q**2 + sp.exp(-P))
def lie(xi):
    R=sp.zeros(4,4)
    for a in range(4):
        for b in range(4):
            e = sum(xi[c]*sp.diff(g[a,b],X[c]) for c in range(4))
            e += sum(g[c,b]*sp.diff(xi[c],X[a]) for c in range(4))
            e += sum(g[a,c]*sp.diff(xi[c],X[b]) for c in range(4))
            R[a,b]=sp.simplify(e)
    return R
print("d_x Killing:", lie([0,0,1,0])==sp.zeros(4,4))
print("d_y Killing:", lie([0,0,0,1])==sp.zeros(4,4))
print("g(d_x,d_x) =", sp.simplify(g[2,2]), " (spacelike for t>0, P real)")
print("g(d_y,d_y) =", sp.simplify(g[3,3]))
print()
# the transverse reflection x -> -x  (P11's helicity-flipping parity)
gr = g.copy()
S = sp.diag(1,1,-1,1)          # x -> -x
gpull = sp.simplify(S.T*g*S)
print("under x -> -x the metric maps to itself iff the off-diagonal g_xy flips sign and matches:")
print("   g_xy      =", sp.simplify(g[2,3]))
print("   (pullback)=", sp.simplify(gpull[2,3]))
print("   ** reflection is an isometry iff g_xy = 0, i.e. iff Q == 0 (POLARIZED) **",
      sp.simplify(gpull[2,3]+g[2,3])==0)
