"""P9 rem:carter-chain -- THE MASS RIDES A TWISTING, SHEAR-FREE CONGRUENCE OF THE SUBSTRATE'S RULINGS.

The chain in P9 runs: the substrate's null rulings are shear-free; a cut that takes one ruling congruence
as its principal congruence is algebraically special (Goldberg--Sachs); hence Type D; hence a Killing
tensor (Walker--Penrose) and Carter's constant.  This receipt computes the link that takes the ruling
congruence: it exhibits P9's own Kerr--NUT--de Sitter family, in the Plebanski form of thm:pd, as

    g = g0 + (2 M r / Sigma) k k + (2 N p / Sigma) l l,        Sigma = r^2 + p^2,

with g0 the maximally symmetric member (curvature Lambda/3) and k, l null, affinely geodesic and
shear-free congruences OF g0.  A null geodesic of de Sitter space is a straight null line of the
embedding, a ruling, so k and l are congruences of substrate rulings.  k is real: with N = 0 (Kerr--de
Sitter) every step is real Lorentzian.  l is complex in Lorentzian signature, being reached through a
continuation of the polar coordinate (real in (2,2) signature, Chong--Gibbons--Lu--Pope 2005, Chen--Lu
2008).  The Killing tensor K = p^2 g^(r) - r^2 g^(p) satisfies the Killing equation for every M, N; at
M = N = 0 it is a Killing tensor of a constant-curvature space, hence a sum of symmetrised products of
its Killing vectors (Thompson 1986).
"""
import sympy as sp, random
random.seed(7)
tau,sig,t,s,r,p=sp.symbols('tau sigma t s r p'); I=sp.I
lam,c0,c2,M,N=sp.Rational(1,11),sp.Rational(3,5),sp.Rational(7,9),sp.Rational(2,5),sp.Rational(1,3)
Sig=r**2+p**2
Dr0=c0+c2*r**2-lam*r**4; Dp0=c0-c2*p**2-lam*p**4
sym=lambda u,v:(u*v.T+v*u.T)/2
def christoffel(g,X):
    gi=g.inv()
    return gi,[[[sum(gi[i,l]*(sp.diff(g[l,j],X[k])+sp.diff(g[l,k],X[j])-sp.diff(g[j,k],X[l])) for l in range(4))/2 for k in range(4)] for j in range(4)] for i in range(4)]
def max_sym_residual(g,X,pts):
    gi,G=christoffel(g,X); worst=0
    R=lambda i,j,k,l: sp.diff(G[i][j][l],X[k])-sp.diff(G[i][j][k],X[l])+sum(G[i][k][m]*G[m][j][l]-G[i][l][m]*G[m][j][k] for m in range(4))
    for pt in pts:
        g0=g.subs(pt)
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for l in range(k+1,4):
                        v=sum(g0[i,m]*R(m,j,k,l).subs(pt) for m in range(4))-lam*(g0[i,k]*g0[j,l]-g0[i,l]*g0[j,k])
                        worst=max(worst,abs(sp.N(v,40)))
    return worst
def optics(g,X,k):
    gi,G=christoffel(g,X); ku=gi*k
    Dk=sp.Matrix(4,4,lambda i,j: sp.diff(k[j],X[i])-sum(G[l][i][j]*k[l] for l in range(4)))
    up=lambda T: gi*T*gi
    th=sp.simplify(sum(gi[i,j]*Dk[i,j] for i in range(4) for j in range(4))/2)
    S=(Dk+Dk.T)/2; A_=(Dk-Dk.T)/2
    return (sp.simplify((k.T*ku)[0]), [sp.simplify(x) for x in Dk.T*ku], th,
            sp.simplify(sum(A_[i,j]*up(A_)[i,j] for i in range(4) for j in range(4))/2),
            sp.simplify(sum(S[i,j]*up(S)[i,j] for i in range(4) for j in range(4))/2-th**2))
pts=[{r:sp.Rational(random.randint(3,19),10),p:sp.Rational(random.randint(1,9),10)} for _ in range(2)]
X=[t,s,r,p]
A=sp.Matrix([1,p**2,0,0]); B=sp.Matrix([1,-r**2,0,0]); dr=sp.Matrix([0,0,1,0]); dp=sp.Matrix([0,0,0,1])

# (1) KERR--DE SITTER (N = 0), REAL: ingoing coordinates dtau = dt + r^2/Dr dr, dsigma = ds + dr/Dr
gK=lambda Dr: -Dr/Sig*A*A.T - 2*sym(A,dr) + Dp0/Sig*B*B.T + Sig/Dp0*dp*dp.T
g0=gK(Dr0)
assert sp.simplify(gK(Dr0-2*M*r)-g0-(2*M*r/Sig)*A*A.T)==sp.zeros(4)
w=max_sym_residual(g0,X,pts); assert w<1e-30, w
nul,acc,th,tw,sh=optics(g0,X,A)
assert nul==0 and all(x==0 for x in acc) and sh==0
assert sp.simplify(th+r/Sig)==0 and sp.simplify(tw-p**2/Sig**2)==0
print("Kerr--de Sitter, real: g = g0 + (2Mr/Sigma) k k with g0 de Sitter (residual %.1e);"%w)
print("  k null, affinely geodesic, shear 0, expansion -r/Sigma, twist^2 p^2/Sigma^2, no M in k")

# (2) KERR--NUT--DE SITTER: the NUT charge along l, reached through the polar continuation
gC=lambda Dr,Dp: -Dr/Sig*A*A.T - 2*sym(A,dr) + Dp/Sig*B*B.T + 2*I*sym(B,dp)
g00=gC(Dr0,Dp0)
assert sp.simplify(gC(Dr0-2*M*r,Dp0+2*N*p)-g00-(2*M*r/Sig)*A*A.T-(2*N*p/Sig)*B*B.T)==sp.zeros(4)
w2=max_sym_residual(g00,X,pts); assert w2<1e-30, w2
for name,k in (('k',A),('l',B)):
    nul,acc,th,tw,sh=optics(g00,X,k)
    assert nul==0 and all(x==0 for x in acc) and sh==0, name
print("Kerr--NUT--de Sitter: g = g00 + (2Mr/Sigma) k k + (2Np/Sigma) l l, g00 maximally symmetric (residual %.1e);"%w2)
print("  k and l null, geodesic, shear-free; l complex in Lorentzian signature (the polar continuation)")

# (3) THE KILLING TENSOR, for the full family in Plebanski coordinates
Xp=[tau,sig,r,p]
Dr=Dr0-2*M*r; Dp=Dp0+2*N*p
g=-Dr/Sig*A*A.T+Sig/Dr*dr*dr.T+Sig/Dp*dp*dp.T+Dp/Sig*B*B.T
K=p**2*(-Dr/Sig*A*A.T+Sig/Dr*dr*dr.T)-r**2*(Sig/Dp*dp*dp.T+Dp/Sig*B*B.T)
gi,G=christoffel(g,Xp)
DK=lambda a,b,c: sp.diff(K[b,c],Xp[a])-sum(G[l][a][b]*K[l,c]+G[l][a][c]*K[b,l] for l in range(4))
worst=0
for pt in pts:
    for a in range(4):
        for b in range(a,4):
            for c in range(b,4):
                worst=max(worst,abs(sp.N((DK(a,b,c)+DK(b,c,a)+DK(c,a,b)).subs(pt),40)))
assert worst<1e-30, worst
print("Killing tensor K = p^2 g^(r) - r^2 g^(p): Killing equation residual %.1e for M, N != 0"%worst)
print("ALL PASS")
