import sympy as sp
r,th,M,al = sp.symbols('r theta M alpha', positive=True)
f = 1 - 2*M/r - r**2/al**2
# SdS spatial 3-slice (t=const):  ds^2_3 = dr^2/f + r^2(dth^2 + sin^2 th dphi^2)
g = sp.diag(1/f, r**2, r**2*sp.sin(th)**2)
gi = g.inv()
co = [r,th,sp.symbols('phi')]
n=3
# Christoffels
Ga=[[[sp.simplify(sum(gi[i,l]*(sp.diff(g[l,j],co[k])+sp.diff(g[l,k],co[j])-sp.diff(g[j,k],co[l])) for l in range(n))/2) for k in range(n)] for j in range(n)] for i in range(n)]
def Ric(i,j):
    return sp.simplify(sum(sp.diff(Ga[k][i][j],co[k]) for k in range(n))
        - sum(sp.diff(Ga[k][i][k],co[j]) for k in range(n))
        + sum(Ga[k][k][l]*Ga[l][i][j] for k in range(n) for l in range(n))
        - sum(Ga[k][j][l]*Ga[l][i][k] for k in range(n) for l in range(n)))
R = sp.Matrix(n,n, lambda i,j: Ric(i,j))
Rscalar = sp.simplify(sum(gi[i,j]*R[i,j] for i in range(n) for j in range(n)))
print("3-Ricci scalar  ^3R =", Rscalar, "   (claim: 6/alpha^2 = 2*Lambda, M-INDEPENDENT)")
# Ricci-squared invariant R_ab R^ab (diffeo-invariant; M-dependence => non-isometric)
Rup = sp.simplify(gi*R*gi)
R2 = sp.simplify(sum(R[i,j]*Rup[i,j] for i in range(n) for j in range(n)))
R2 = sp.simplify(R2)
print("R_ab R^ab =", R2)
print("  dependence on M:", "M-DEPENDENT" if sp.simplify(sp.diff(R2,M))!=0 else "M-independent")
print("  -> different-M cuts are", "NON-ISOMETRIC (M transverse to so(5,1)-orbits)" if sp.simplify(sp.diff(R2,M))!=0 else "possibly isometric")
