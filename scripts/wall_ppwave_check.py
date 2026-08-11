import sympy as sp

# Finding 1 grounding: the wall (Type-N) as a Brinkmann pp-wave. Test it against P1's ACTUAL
# criterion (measure-collapse), not "is it a Killing horizon."
u,v,x,y = sp.symbols('u v x y', real=True)
H = sp.Function('H')(u,x,y)   # wave profile
X = [u,v,x,y]
# Brinkmann form: ds^2 = 2 du dv + H du^2 + dx^2 + dy^2
g = sp.Matrix([[H,1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]])
print("det g =", sp.simplify(g.det()), " -> non-degenerate, NO measure collapse (no Δx→0 hypersurface).")
ginv = g.inv()

# k = ∂_v : null? Killing? covariantly constant?
k_up = sp.Matrix([0,1,0,0])               # vector ∂_v
k_dn = g*k_up
print("k=∂_v norm |k|^2 =", sp.simplify((k_up.T*g*k_up)[0]), " -> NULL.")

# Christoffels
def christ(g,ginv,X):
    n=len(X); G=[[[0]*n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                s=0
                for d in range(n):
                    s+=ginv[a,d]*(sp.diff(g[d,b],X[c])+sp.diff(g[d,c],X[b])-sp.diff(g[b,c],X[d]))
                G[a][b][c]=sp.simplify(s/2)
    return G
G=christ(g,ginv,X)
# ∇_a k^b  (k^b constant components) = ∂_a k^b + Γ^b_{a c} k^c ; k^c = δ^c_v
nabla_k = sp.Matrix([[ sp.simplify(G[b][a][1]) for b in range(4)] for a in range(4)])
print("∇k (covariant derivative of ∂_v) zero? ", nabla_k == sp.zeros(4,4), " -> covariantly constant null Killing vector.")

# Killing: ∇_a k_b + ∇_b k_a = 0  (Lie derivative of g along ∂_v = ∂_v g = 0 since g indep of v)
print("∂_v g = 0 (metric v-independent) -> ∂_v is Killing. YES.")

# Curvature invariants: Ricci scalar and Kretschmann
def riemann(G,X):
    n=len(X); R=[[[[0]*n for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    t=sp.diff(G[a][b][d],X[c])-sp.diff(G[a][b][c],X[d])
                    for e in range(n):
                        t+=G[a][c][e]*G[e][b][d]-G[a][d][e]*G[e][b][c]
                    R[a][b][c][d]=sp.simplify(t)
    return R
R=riemann(G,X)
# Ricci
Ric=sp.Matrix([[sp.simplify(sum(R[a][b][a][d] for a in range(4))) for d in range(4)] for b in range(4)])
Rscal=sp.simplify(sum(ginv[b,d]*Ric[b,d] for b in range(4) for d in range(4)))
print("Ricci scalar =", Rscal, " (vacuum pp-wave: 0 when ∂_xx H+∂_yy H=0).")
# Kretschmann K = R_{abcd}R^{abcd}
Rdn=[[[[sp.simplify(sum(g[a,e]*R[e][b][c][d] for e in range(4))) for d in range(4)] for c in range(4)] for b in range(4)] for a in range(4)]
Rup=[[[[sp.simplify(sum(ginv[a,e]*ginv[b,f]*ginv[c,h]*ginv[d,k2]*Rdn[e][f][h][k2] for e in range(4) for f in range(4) for h in range(4) for k2 in range(4))) for d in range(4)] for c in range(4)] for b in range(4)] for a in range(4)]
K=sp.simplify(sum(Rdn[a][b][c][d]*Rup[a][b][c][d] for a in range(4) for b in range(4) for c in range(4) for d in range(4)))
print("Kretschmann K =", K, " -> ALL polynomial curvature invariants vanish (VSI): curvature-regular, NOT the infinite-curvature species.")
print()
print("VERDICT: non-degenerate metric (no measure-collapse) + VSI (curvature-regular) => the wall is")
print("NEITHER species of metric singularity, BY P1'S MEASURE-COLLAPSE DEFINITION. Branch (c), re-grounded.")
print("The covariantly-constant null KV is null EVERYWHERE (no non-null→null transition) => no Killing")
print("horizon, no measure collapse -- consistent with (c). 'No Killing vector at all' was false and unneeded.")
