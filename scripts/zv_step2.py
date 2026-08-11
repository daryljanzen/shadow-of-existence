import sympy as sp, numpy as np

t,x,y,ph = sp.symbols('t x y phi', real=True)
coords=[t,x,y,ph]
def metric(dval):
    H=((x+1)/(x-1))**dval
    return sp.diag(-((x-1)/(x+1))**dval,
                   H*(x**2-1)**(dval**2-1)*(x**2-y**2)**(1-dval**2),
                   H*(x**2-1)**(dval**2)*(x**2-y**2)**(1-dval**2)/(1-y**2),
                   H*(x**2-1)*(1-y**2))

def riemann_lower(g):
    n=4; gi=g.inv()
    Gam=[[[sp.S(0)]*n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                s=sum(gi[a,e]*(sp.diff(g[e,b],coords[c])+sp.diff(g[e,c],coords[b])-sp.diff(g[b,c],coords[e])) for e in range(n))
                Gam[a][b][c]=s/2
    # R^a_{bcd}
    R=[[[[sp.S(0)]*n for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for dd in range(n):
                    term=sp.diff(Gam[a][b][dd],coords[c])-sp.diff(Gam[a][b][c],coords[dd])
                    term+=sum(Gam[a][c][e]*Gam[e][b][dd]-Gam[a][dd][e]*Gam[e][b][c] for e in range(n))
                    R[a][b][c][dd]=term
    # lower: R_{abcd}=g_{ae}R^e_{bcd}
    Rl=[[[[sp.S(0)]*n for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for dd in range(n):
                    Rl[a][b][c][dd]=sum(g[a,e]*R[e][b][c][dd] for e in range(n))
    return Rl,gi

def Qmatrix(dval, xv, yv):
    g=metric(sp.Integer(dval) if float(dval)==int(dval) else sp.Rational(dval).limit_denominator(1000))
    Rl,gi=riemann_lower(g)
    subs={x:sp.Rational(xv).limit_denominator(10**6), y:sp.Rational(yv).limit_denominator(10**6)}
    gN=np.array(g.subs(subs)).astype(float)
    # In vacuum Weyl=Riemann. Evaluate R_{abcd} numerically.
    Rn=np.zeros((4,4,4,4))
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for ddi in range(4):
                    Rn[a,b,c,ddi]=float(sp.N(Rl[a][b][c][ddi].subs(subs)))
    # Orthonormal tetrad (diagonal metric), signature (-,+,+,+)
    e=np.zeros((4,4))   # e[A][mu]: frame index A, coord index mu
    e[0,0]=1/np.sqrt(-gN[0,0]); 
    for i in range(1,4): e[i,i]=1/np.sqrt(gN[i,i])
    # Weyl in ON frame C_{ABCD}
    C=np.einsum('am,bn,cp,dq,mnpq->abcd', e,e,e,e, Rn)
    # 3x3 complex Q: electric E_ij=C_{0i0j}; magnetic B_ij = (1/2) eps_{ikl} C_{0jkl} (spatial Levi-Civita)
    eps=np.zeros((3,3,3))
    for (i,j,kk),s in zip([(0,1,2),(1,2,0),(2,0,1),(2,1,0),(0,2,1),(1,0,2)],[1,1,1,-1,-1,-1]):
        eps[i,j,kk]=s
    E=np.zeros((3,3)); B=np.zeros((3,3))
    for i in range(3):
        for j in range(3):
            E[i,j]=C[0,i+1,0,j+1]
            B[i,j]=0.5*sum(eps[i,kk,ll]*C[0+0,j+1,kk+1,ll+1] for kk in range(3) for ll in range(3))
    Q=E+1j*B
    Q=0.5*(Q+Q.T)  # symmetrize numerical noise
    w=np.linalg.eigvals(Q)
    w=np.array(sorted(w,key=lambda z:(z.real,z.imag)))
    Iinv=np.sum(w**2)
    Jinv=np.prod(w)
    return w,Iinv,Jinv

for dval in [1, 2, 0.5, 3]:
    w,Iinv,Jinv=Qmatrix(dval, 2.0, 0.3)
    ratio=27*Jinv**2/Iinv**3
    print(f"\ndelta={dval}  at (x,y)=(2.0,0.3)")
    print("  Q eigenvalues:", np.round(w,6))
    print("  trace(Q)=",np.round(np.sum(w),8)," (should be ~0)")
    print("  I=Σλ²=",np.round(Iinv,8),"  J=Πλ=",np.round(Jinv,8))
    print("  27J²/I³ =",np.round(ratio,6),"   I³/27J² =",np.round(1/ratio,6))
    diffs=[abs(w[i]-w[j]) for i in range(3) for j in range(i+1,3)]
    print("  pairwise |λi-λj|:",np.round(diffs,6), "-> Type", "D/special (two equal)" if min(diffs)<1e-6 else "I (all distinct)")

print("\n\n===== POSITION-DEPENDENCE TEST (Type D constant vs Type I varying) =====")
pts=[(2.0,0.3),(3.0,-0.5),(1.6,0.8)]
for dval in [1,2,0.5,3]:
    vals=[]
    for (xv,yv) in pts:
        w,Iinv,Jinv=Qmatrix(dval,xv,yv)
        r=27*Jinv**2/Iinv**3
        vals.append(complex(r).real)
    spread=max(vals)-min(vals)
    print(f"delta={dval}: 27J²/I³ at 3 points = {np.round(vals,6)}  spread={spread:.2e}  -> "
          + ("CONSTANT (Type D)" if spread<1e-6 else "POSITION-DEPENDENT (Type I)"))
