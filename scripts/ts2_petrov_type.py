#!/usr/bin/env python3
"""
C2 — the rotating type-I corner (P9 range_paper §202), closed by direct computation.

P9 computes Type-I reachability at 3 Killing vectors (Bianchi I) and in the STATIC
axisymmetric class (Zipoy-Voorhees, gamma!=1).  The rotating type-I members -- the
Ernst class, the Tomimatsu-Sato metrics -- are ARGUED reachable (static type-I leaf +
the independent shift) but not computed.  P9: "A direct computation of a Tomimatsu-Sato
member's algebraic type and its realization as a cut would close this corner."

The sharp question: does turning the SHIFT on a Type-I static leaf keep it Type I, or
collapse it to Type D the way rotating the SPHERICAL (Schwarzschild, Type-D) leaf gives
Type-D Kerr?  We answer it by running ONE pipeline on the Kerr-TS family
(Bambi-Yoshida form, arXiv:1004.3149) at:
    delta=1  -> Kerr        [CONTROL: must return Type D  (repeated Weyl eigenvalue)]
    delta=2  -> TS2         [must return Type I           (three distinct eigenvalues)]
Both are stationary axisymmetric vacuum (Lambda=0); the substrate realization is the
Lambda->0 (alpha->inf) edge of the operator's rotating axisymmetric class (2 Killing
vectors t,phi -> a sweep-subgroup of so(5,1); class-filling by leaf+lapse+shift+vantage,
P9 Thm bound/range).  Vacuum (Ricci=0) is the self-validating check on the transcription.

Method: metric in prolate spheroidal (t,x,y,phi); 4th-order finite-difference d g, dd g
(x,y only; metric is t,phi independent); Riemann via the dd-g formula; Ricci (vacuum
check); Weyl; orthonormal tetrad; complex Weyl operator Q = E + iB (3x3, symmetric,
traceless); eigenvalues -> Petrov type (3 distinct = I; a repeated pair = D).
"""
import numpy as np

# ---------- Kerr-TS metric functions (Bambi-Yoshida arXiv:1004.3149, eqs 2,5,6,7) ----
def ABC(delta, x, y, p, q):
    x2, y2 = x*x, y*y
    X, Y = x2 - 1.0, 1.0 - y2      # (x^2-1), (1-y^2)
    if delta == 1:                 # Kerr
        A = p*p*X - q*q*Y
        B = (p*x + 1.0)**2 + q*q*y2
        C = -(p*x + 1.0)
    elif delta == 2:               # Tomimatsu-Sato delta=2
        A = (p**4)*X**4 + (q**4)*Y**4 \
            - 2.0*p*p*q*q*X*Y*(2.0*X*X + 2.0*Y*Y + 3.0*X*Y)
        B = (p*p*(x2+1.0)*X - q*q*(1.0+y2)*Y + 2.0*p*x*X)**2 \
            + 4.0*q*q*y2*(p*x*X + (p*x+1.0)*Y)**2
        C = -(p**3)*x*X*(2.0*(x2+1.0)*X + (x2+3.0)*Y) \
            - p*p*X*(4.0*x2*X + (3.0*x2+1.0)*Y) \
            + q*q*(p*x+1.0)*Y**3
    else:
        raise ValueError("delta in {1,2}")
    return A, B, C

def metric(delta, x, y, p, q, M):
    """4x4 metric g_{mu nu} in coords (t,x,y,phi); depends only on (x,y)."""
    sigma = M*p/delta
    A, B, C = ABC(delta, x, y, p, q)
    x2, y2 = x*x, y*y
    f   = A / B
    fw  = 2.0*M*q*(1.0 - y2)*C / B        # f*omega = 2Mq(1-y^2)C/B  (=(A/B)*w)
    w   = fw / f
    rho2 = sigma*sigma*(x2 - 1.0)*(1.0 - y2)
    # e^{2gamma}/f = B / (p^{2 delta} (x^2-y^2)^{delta^2})
    e2g_over_f = B / ( p**(2*delta) * (x2 - y2)**(delta*delta) )
    gxx = e2g_over_f * sigma*sigma*(x2 - y2)/(x2 - 1.0)
    gyy = e2g_over_f * sigma*sigma*(x2 - y2)/(1.0 - y2)
    g = np.zeros((4,4))
    g[0,0] = -f
    g[0,3] = g[3,0] = f*w                 # = fw
    g[3,3] = -f*w*w + rho2/f
    g[1,1] = gxx
    g[2,2] = gyy
    return g

# ---------- finite-difference derivatives (x=index1, y=index2 only) ----------
def dmetric(delta, x, y, p, q, M, h=1e-4):
    """returns dg[a][mu][nu] = d_a g_{mu nu}, a in {1(x),2(y)}; a=0,3 -> 0."""
    dg = np.zeros((4,4,4))
    for a, (dx,dy) in [(1,(h,0.0)), (2,(0.0,h))]:
        gm2 = metric(delta, x-2*dx, y-2*dy, p,q,M)
        gm1 = metric(delta, x-dx,   y-dy,   p,q,M)
        gp1 = metric(delta, x+dx,   y+dy,   p,q,M)
        gp2 = metric(delta, x+2*dx, y+2*dy, p,q,M)
        dg[a] = (-gp2 + 8*gp1 - 8*gm1 + gm2)/(12*h)      # 4th-order 1st deriv
    return dg

def ddmetric(delta, x, y, p, q, M, h=1e-4):
    """ddg[a][b][mu][nu] = d_a d_b g_{mu nu}, a,b in {1,2}."""
    ddg = np.zeros((4,4,4,4))
    # pure second derivatives (4th-order)
    for a, (dx,dy) in [(1,(h,0.0)), (2,(0.0,h))]:
        gm2 = metric(delta, x-2*dx, y-2*dy, p,q,M)
        gm1 = metric(delta, x-dx,   y-dy,   p,q,M)
        g0  = metric(delta, x,      y,      p,q,M)
        gp1 = metric(delta, x+dx,   y+dy,   p,q,M)
        gp2 = metric(delta, x+2*dx, y+2*dy, p,q,M)
        ddg[a,a] = (-gp2 + 16*gp1 - 30*g0 + 16*gm1 - gm2)/(12*h*h)
    # mixed d_x d_y (2nd-order cross stencil)
    gpp = metric(delta, x+h, y+h, p,q,M); gpm = metric(delta, x+h, y-h, p,q,M)
    gmp = metric(delta, x-h, y+h, p,q,M); gmm = metric(delta, x-h, y-h, p,q,M)
    mixed = (gpp - gpm - gmp + gmm)/(4*h*h)
    ddg[1,2] = ddg[2,1] = mixed
    return ddg

# ---------- curvature ----------
def christoffel(ginv, dg):
    G = np.zeros((4,4,4))     # G[a][b][c] = Gamma^a_{bc}
    for a in range(4):
        for b in range(4):
            for c in range(4):
                s = 0.0
                for d in range(4):
                    s += ginv[a,d]*(dg[b][d,c] + dg[c][d,b] - dg[d][b,c])
                G[a,b,c] = 0.5*s
    return G

def riemann_lower(g, ginv, dg, ddg, G):
    """R_{abcd} via R_{abcd}=1/2(dd g terms)+g_ef(G^e_ad G^f_bc - G^e_ac G^f_bd)."""
    R = np.zeros((4,4,4,4))
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    lin = 0.5*(ddg[b,c][a,d] + ddg[a,d][b,c]
                               - ddg[a,c][b,d] - ddg[b,d][a,c])
                    quad = 0.0
                    for e in range(4):
                        for ff in range(4):
                            quad += g[e,ff]*(G[e,a,d]*G[ff,b,c] - G[e,a,c]*G[ff,b,d])
                    R[a,b,c,d] = lin + quad
    return R

def ricci(R, ginv):
    Ric = np.zeros((4,4))
    for b in range(4):
        for d in range(4):
            s = 0.0
            for a in range(4):
                for c in range(4):
                    s += ginv[a,c]*R[a,b,c,d]
            Ric[b,d] = s
    return Ric

def weyl(R, g, Ric, Rs):
    C = np.zeros((4,4,4,4))
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    term = R[a,b,c,d]
                    term -= 0.5*(g[a,c]*Ric[b,d] - g[a,d]*Ric[b,c]
                                 - g[b,c]*Ric[a,d] + g[b,d]*Ric[a,c])
                    term += (Rs/6.0)*(g[a,c]*g[b,d] - g[a,d]*g[b,c])
                    C[a,b,c,d] = term
    return C

# ---------- Petrov type via complex Weyl operator Q = E + iB ----------
def tetrad(g):
    """orthonormal tetrad e[mu][A]: g = eta_{AB} e^A e^B, eta=diag(-1,1,1,1).
    Returns E[:,A] frame vectors (contravariant components e_A^mu)."""
    w, V = np.linalg.eigh(g)                      # g symmetric
    order = np.argsort(w)                         # most negative first (timelike)
    w = w[order]; V = V[:, order]
    e = np.zeros((4,4))
    for A in range(4):
        norm = np.sqrt(abs(w[A]))
        e[:,A] = V[:,A]/norm                      # e[:,0] timelike, e[:,1:] spacelike
    return e

def levicivita_lower(g):
    """eps_{abcd} = sqrt(-det g) * [abcd], with [0123]=+1."""
    detg = np.linalg.det(g)
    s = np.sqrt(abs(detg))
    eps = np.zeros((4,4,4,4))
    from itertools import permutations
    base = (0,1,2,3)
    def sign(perm):
        perm=list(perm); sgn=1
        for i in range(len(perm)):
            for j in range(i+1,len(perm)):
                if perm[i]>perm[j]: sgn=-sgn
        return sgn
    for perm in permutations(base):
        eps[perm] = s*sign(perm)
    return eps

def petrov_Q(C, g):
    """Build Q_{ij}=E_{ij}+i B_{ij} (i,j=1,2,3 spatial frame), return eigenvalues."""
    e = tetrad(g)                    # e[:,A], A=0 timelike
    ginv = np.linalg.inv(g)
    eps = levicivita_lower(g)
    # dual Weyl *C_{abcd} = 1/2 eps_{ab}^{ef} C_{efcd} = 1/2 eps_{abpq} g^{pe} g^{qf} C_{efcd}
    Cstar = np.zeros((4,4,4,4))
    # raise last two indices of eps: eps_{ab}{}^{ef}
    epsUp = np.einsum('abpq,pe,qf->abef', eps, ginv, ginv)
    Cstar = 0.5*np.einsum('abef,efcd->abcd', epsUp, C)
    E = np.zeros((3,3)); B = np.zeros((3,3))
    e0 = e[:,0]
    for i in range(1,4):
        for j in range(1,4):
            ei, ej = e[:,i], e[:,j]
            E[i-1,j-1] = np.einsum('abcd,a,b,c,d->', C,     e0, ei, e0, ej)
            B[i-1,j-1] = np.einsum('abcd,a,b,c,d->', Cstar, e0, ei, e0, ej)
    Q = E + 1j*B
    Q = 0.5*(Q + Q.T)                # symmetrize (numerical)
    evals = np.linalg.eigvals(Q)
    return evals, Q

def analyze(delta, name, p, q, M, pts):
    print(f"\n===== {name}  (delta={delta}, p={p:.4f}, q={q:.4f}, M={M}) =====")
    for (x,y) in pts:
        g   = metric(delta, x,y,p,q,M)
        ginv= np.linalg.inv(g)
        dg  = dmetric(delta, x,y,p,q,M)
        ddg = ddmetric(delta, x,y,p,q,M)
        G   = christoffel(ginv, dg)
        R   = riemann_lower(g, ginv, dg, ddg, G)
        Ric = ricci(R, ginv)
        Rs  = np.einsum('bd,bd->', ginv, Ric)
        C   = weyl(R, g, Ric, Rs)
        # scale-free vacuum residual: |Ric| vs |Riemann|
        rnorm = np.sqrt(np.sum(R*R)); ricnorm = np.sqrt(np.sum(Ric*Ric))
        vac = ricnorm/max(rnorm,1e-30)
        evals, Q = petrov_Q(C, g)
        ev = evals[np.argsort(-np.abs(evals))]
        # speciality: sort, measure minimal pairwise separation (normalized)
        seps = [abs(ev[i]-ev[j]) for i in range(3) for j in range(i+1,3)]
        scale = np.mean(np.abs(ev)) + 1e-30
        min_sep = min(seps)/scale
        # invariants I=-(l1l2+l2l3+l3l1), J=l1l2l3 ; speciality S=27 J^2 / I^3
        l1,l2,l3 = ev
        Iinv = -(l1*l2 + l2*l3 + l3*l1)
        Jinv = l1*l2*l3
        S = 27*Jinv**2 / Iinv**3 if abs(Iinv)>1e-30 else np.nan
        typ = "TYPE D/special (repeated eigenvalue)" if min_sep < 1e-3 \
              else "TYPE I (three distinct eigenvalues)"
        print(f"  (x,y)=({x},{y}): vacuum |Ric|/|Riem|={vac:.2e} | "
              f"eig sep(min,norm)={min_sep:.3e} | Sr=27J^2/I^3={S.real:.5f} -> {typ}")
        print(f"        Weyl eigenvalues: "
              + ", ".join(f"{z.real:+.4f}{z.imag:+.4f}i" for z in ev)
              + f"  (sum={sum(ev):.1e})")

if __name__ == "__main__":
    np.set_printoptions(precision=4, suppress=True)
    M = 1.0
    p, q = 0.8, 0.6          # p^2+q^2=1, generic rotation
    pts = [(2.0,0.3),(2.5,-0.4),(3.0,0.6),(1.8,0.1)]
    # CONTROL: Kerr (delta=1) -- rotating the SPHERICAL leaf -> must be TYPE D
    analyze(1, "KERR  [control: rotating spherical (Type-D) leaf]", p,q,M, pts)
    # TARGET: TS2 (delta=2) -- rotating the TYPE-I (Zipoy-Voorhees) leaf
    analyze(2, "TOMIMATSU-SATO delta=2  [rotating Type-I leaf]",    p,q,M, pts)
    # STATIC LIMIT sanity: TS2 with q->0 recovers ZV delta=2 (static, Type I)
    analyze(2, "TS2 static limit q->0+  [Zipoy-Voorhees delta=2]",  0.999999, 1e-6, M, pts)
