import sympy as sp
t,r,th,ph=sp.symbols('t r theta phi',real=True)
a,M,lam=sp.symbols('a M lambda',positive=True)   # lam = Lambda/3
X=[t,r,th,ph]
c,s=sp.cos(th),sp.sin(th)
Sig=r**2+a**2*c**2; Dth=1+lam*a**2*c**2; Xi=1+lam*a**2
# de Sitter background in spheroidal coords (Gibbons-Lu-Page-Pope 2004 form, Lambda>0)
gb=sp.diag(-(1-lam*r**2)*Dth/Xi, Sig/((r**2+a**2)*(1-lam*r**2)), Sig/Dth, (r**2+a**2)*s**2/Xi)
k=sp.Matrix([Dth/Xi, Sig/((r**2+a**2)*(1-lam*r**2)), 0, -a*s**2/Xi])   # covector k_mu
H=2*M*r/Sig
g=gb+H*k*k.T
def ricci(g):
    gi=sp.simplify(g.inv())
    G=[[[sum(gi[i,l]*(sp.diff(g[l,j],X[kk])+sp.diff(g[l,kk],X[j])-sp.diff(g[j,kk],X[l])) for l in range(4))/2 for kk in range(4)] for j in range(4)] for i in range(4)]
    R=sp.zeros(4)
    for i in range(4):
        for j in range(4):
            R[i,j]=sum(sp.diff(G[l][i][j],X[l]) - sp.diff(G[l][i][l],X[j]) + sum(G[l][l][m]*G[m][i][j]-G[l][j][m]*G[m][i][l] for m in range(4)) for l in range(4))
    return R,gi,G
# 1. background is de Sitter: R_ab = 3 lam g_ab (Lambda = 3 lam)
Rb,gbi,Gb=ricci(gb)
print('background Einstein:', all(sp.simplify(Rb[i,j]-3*lam*gb[i,j])==0 for i in range(4) for j in range(4)))
# 2. k null and geodesic in background, and independent of M (explicit)
ku=gbi*k
print('k null in background:', sp.simplify((k.T*ku)[0])==0)
cov=lambda kk: sp.Matrix(4,4,lambda i,j: sp.diff(kk[j],X[i])-sum(Gb[l][i][j]*kk[l] for l in range(4)))   # nabla_i k_j
Dk=cov(k)
acc=sp.simplify(Dk.T*ku)  # k^i nabla_i k_j
print('k geodesic (affine) in background:', all(sp.simplify(x)==0 for x in acc))
# 3. optical scalars in background: theta, twist^2, |shear|^2
up=lambda A: gbi*A*gbi
Du=up(Dk)
divk=sp.simplify(sum(gbi[i,j]*Dk[i,j] for i in range(4) for j in range(4)))
thet=divk/2
sym=(Dk+Dk.T)/2; asym=(Dk-Dk.T)/2
symsq=sp.simplify(sum(sym[i,j]*up(sym)[i,j] for i in range(4) for j in range(4)))
asq=sp.simplify(sum(asym[i,j]*up(asym)[i,j] for i in range(4) for j in range(4)))
shear2=sp.simplify(symsq/2-thet**2)
print('expansion theta =', sp.simplify(thet))
print('twist^2 =', sp.simplify(asq/2))
print('shear^2 in background =', shear2)
# 4. full metric: Einstein with the same Lambda
R,gi,G=ricci(g)
print('full metric Einstein:', all(sp.simplify(R[i,j]-3*lam*g[i,j])==0 for i in range(4) for j in range(4)))
