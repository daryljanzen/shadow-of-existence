import sympy as sp
r, th, M, al = sp.symbols('r theta M alpha', positive=True)
f = 1 - 2*M/r - r**2/al**2
g = sp.diag(1/f, r**2, r**2*sp.sin(th)**2)
gi = g.inv()
x = [r, th, sp.Symbol('phi')]
n = 3

# Christoffel (independent index handling)
def Gamma(a,b,c):
    return sp.Rational(1,2)*sum(gi[a,d]*(sp.diff(g[d,b],x[c])+sp.diff(g[d,c],x[b])-sp.diff(g[b,c],x[d])) for d in range(n))
G = [[[sp.simplify(Gamma(a,b,c)) for c in range(n)] for b in range(n)] for a in range(n)]

# Full Riemann R^a_{bcd} (independent route), then Ricci as contraction R_{bd}=R^a_{bad}
def Riem(a,b,c,d):
    t = sp.diff(G[a][b][d],x[c]) - sp.diff(G[a][b][c],x[d])
    t += sum(G[a][c][e]*G[e][b][d] - G[a][d][e]*G[e][b][c] for e in range(n))
    return sp.simplify(t)
Ric = sp.Matrix(n,n, lambda b,d: sp.simplify(sum(Riem(a,b,a,d) for a in range(n))))
Rs_from_riem = sp.simplify(sum(gi[b,d]*Ric[b,d] for b in range(n) for d in range(n)))

# Ricci scalar a second, independent way: trace of mixed Ricci R^a_a
Ric_mixed = sp.simplify(gi*Ric)
Rs_trace = sp.simplify(sum(Ric_mixed[a,a] for a in range(n)))

# Ricci-squared
Ric_up = sp.simplify(gi*Ric*gi)
R2 = sp.simplify(sum(Ric[i,j]*Ric_up[i,j] for i in range(n) for j in range(n)))

Lam = 3/al**2  # Lambda for dS radius alpha (so 2*Lambda = 6/alpha^2)
print("3R via Riemann-contraction :", Rs_from_riem)
print("3R via mixed-Ricci trace   :", Rs_trace, " (must match the line above)")
print("3R - 2*Lambda              :", sp.simplify(Rs_from_riem - 2*Lam), " (Hamiltonian constraint, K=0 vacuum: must be 0)")
print("dependence of 3R on M      :", "M-DEP" if sp.simplify(sp.diff(Rs_from_riem,M))!=0 else "M-INDEPENDENT")
print()
print("R_ab R^ab                  :", R2)
print("  M=0 limit                :", sp.simplify(R2.subs(M,0)), " (constant-curvature 3-space expects 12/alpha^4)")
print("  3*(2/alpha^2)^2           :", sp.simplify(3*(2/al**2)**2), " (= R_ab R^ab for a 3-space with R_ab=(2/alpha^2)g_ab)")
print("  dependence on M           :", "M-DEP -> different-M slices NON-ISOMETRIC" if sp.simplify(sp.diff(R2,M))!=0 else "M-indep")
