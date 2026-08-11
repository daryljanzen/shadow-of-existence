import sympy as sp
r,t,th,al=sp.symbols('r t theta alpha',positive=True)
Lam=3/al**2  # de Sitter substrate, Lambda=3/alpha^2

print("VACUUM de Sitter substrate (M=0), f = 1 - r^2/alpha^2.  Hamiltonian constraint H = R3 + K^2 - KabKab - 2*Lambda  (=0 in vacuum)\n")

# ---------- EXTERIOR vantage: r spacelike, t timelike. Foliate by t=const. ----------
f=1-r**2/al**2   # >0 for r<alpha
# spatial 3-metric h(t-slice)=diag(1/f, r^2, r^2 sin^2 th); static => K=0
def ricci3(h,xs):
    n=3; hi=h.inv()
    G=[[[sp.simplify(sum(hi[a,e]*(sp.diff(h[e,b],xs[c])+sp.diff(h[e,c],xs[b])-sp.diff(h[b,c],xs[e])) for e in range(n))/2) for c in range(n)] for b in range(n)] for a in range(n)]
    Ric=sp.zeros(n,n)
    for b in range(n):
        for c in range(n):
            s=sum(sp.diff(G[a][b][c],xs[a])-sp.diff(G[a][b][a],xs[c]) for a in range(n))
            s+=sum(G[a][a][e]*G[e][b][c]-G[a][c][e]*G[e][b][a] for a in range(n) for e in range(n))
            Ric[b,c]=sp.simplify(s)
    return sp.simplify(sum(hi[i,j]*Ric[i,j] for i in range(n) for j in range(n)))
hE=sp.diag(1/f, r**2, r**2*sp.sin(th)**2)
R3E=ricci3(hE,[r,th,sp.Symbol('ph')])
HE=sp.simplify(R3E + 0 - 0 - 2*Lam)   # K=0
print("EXTERIOR (t-foliation, K=0):")
print("   R3 =", sp.simplify(R3E), "  (= 2*Lambda =",sp.simplify(2*Lam),")")
print("   H  = R3 - 2Lambda =", HE, "  -> all of 2Lambda sits in spatial curvature R3")

# ---------- INTERIOR vantage: r timelike, t spacelike. Foliate by r=const. ----------
# induced 3-metric on r=const (coords t,th,ph): gamma=diag(|f|, r^2, r^2 sin^2 th), |f|=r^2/al^2-1
F=r**2/al**2-1   # |f|, >0 for r>alpha
gam=sp.diag(F, r**2, r**2*sp.sin(th)**2)
xs=[t,th,sp.Symbol('ph')]
R3I=ricci3(gam,xs)   # spatial curvature of the r=const slice (t is now spatial)
# r is "time"; lapse N=1/sqrt|f|=1/sqrt(F); extrinsic curvature K_ab=(1/(2N)) d_r gamma_ab = (sqrt(F)/2) d_r gamma_ab
N=1/sp.sqrt(F)
Kab=sp.zeros(3,3)
for a in range(3): Kab[a,a]=sp.simplify((1/(2*N))*sp.diff(gam[a,a],r))
gi=gam.inv()
Kmix=sp.simplify(gi*Kab)          # K^a_b
Ktr=sp.simplify(sp.trace(Kmix))   # K
KabKab=sp.simplify(sum(Kmix[a,b]*Kmix[b,a] for a in range(3) for b in range(3)))
HI=sp.simplify(R3I + Ktr**2 - KabKab - 2*Lam)
print("\nINTERIOR (r-foliation, r is time):")
print("   R3(t,th,ph slice) =", sp.simplify(R3I))
print("   K   =", sp.simplify(Ktr))
print("   K^2 - KabKab      =", sp.simplify(Ktr**2-KabKab))
print("   R3 + (K^2-KabKab) =", sp.simplify(R3I+Ktr**2-KabKab), "  (should be 2*Lambda =",sp.simplify(2*Lam),")")
print("   H = R3 + K^2 - KabKab - 2Lambda =", HI)
print("\n=> sigma (vantage flip) redistributes the SAME 2*Lambda:")
print("   exterior: 2Lambda all in R3, K=0.   interior: R3 =",sp.simplify(R3I),", and (K^2-KabKab) carries the rest.")
