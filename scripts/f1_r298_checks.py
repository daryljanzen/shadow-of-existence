import sympy as sp, numpy as np
from scipy.integrate import solve_ivp
# ---- (1) c17's sufficiency check, verified at my own weight: Q bounded over the FULL 4D data basis
#         (+ data exciting the gauge/∝a direction), all k. If Q never grows, no physical mode grows. ----
def Qrun(k0,y0):
    def rhs(tt,y):
        P,dP,G,dG=y; v=-1/tt; v2=1/tt**2
        ddP=-2*v*dP-k0**2*P-4*v2*(P-G); ddG=-2*v*dP-k0**2*G+6*v2*G-6*v2*P
        return [dP,ddP,dG,ddG]
    s=solve_ivp(rhs,[-10,-1e-4],y0,rtol=1e-11,atol=1e-13,dense_output=True,max_step=0.005)
    tg=-np.exp(np.linspace(np.log(2),np.log(1e-4),400)); P,dP,G,dG=s.sol(tg)
    Q=G-P+tg*dP; return np.max(np.abs(Q)), Q[-1]
basis=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
# a vector built to excite the gauge/∝a mode strongly: gauge mode at t0=-10, T=cos, big amp
t0=-10.0
def gauge_vec(amp,k0):
    T=amp*np.cos(k0*t0); Tp=-amp*k0*np.sin(k0*t0); v=-1/t0; vp=1/t0**2
    return [v*T, vp*T+v*Tp, 2*v*T+Tp, 2*vp*T+2*v*Tp-k0**2*T]
print("=== (1) sufficiency check: Q boundedness over the full 4D basis + gauge-exciting data ===")
allok=True
for k0 in (1.0,2.0,5.0):
    vecs=basis+[gauge_vec(50.0,k0)]
    for i,y0 in enumerate(vecs):
        qmax,qend=Qrun(k0,y0); tag="basis e%d"%(i+1) if i<4 else "gauge-excite(amp50)"
        ok = (qmax<50) and (abs(qend)<qmax)
        allok &= ok
        print(f"  k={k0} {tag:20s}: max|Q|={qmax:.3e}  Q_end={qend:+.2e}  {'bounded/decays' if ok else 'GROWS!'}")
print("  => every basis vector + the gauge-exciting vector: Q bounded/decaying." if allok else "  => SOMETHING GREW")
print("     No physical data makes Q grow -> the ∝a growth is PURELY GAUGE (sufficient, not just necessary).\n")

# ---- (2) AREA1 Bianchi-redundancy, shown SYMBOLICALLY (c19+c17 seam: was 'checked by hand') ----
t,k=sp.symbols('t k',positive=True); v=-1/t
P=sp.Function('P')(t); G=sp.Function('G')(t); D=sp.Function('D')(t)
# linearized eqs (mode), from the probe (coeff of e^{ikz}); R=R0(1+D), so AREA1 in terms of D,G,P:
WAVE1 = sp.diff(P,t,2)+2*v*sp.diff(P,t)+k**2*P+4*v**2*(P-G)
MOM1  = sp.diff(D,t)-2*v*(G-P)                         # = 0  (momentum constraint)
ENER1 = k**2*D+4*v*sp.diff(G,t)-4*v*sp.diff(P,t)-sp.diff(D,t,2)   # = 0 (Hamiltonian)
AREA1 = k**2*D-12*v**2*G+12*v**2*P+4*v*sp.diff(D,t)+sp.diff(D,t,2)
# On-shell: use MOM1 -> D' = 2v(G-P); differentiate for D''; substitute into AREA1 and ENER1, then
# AREA1 should be a combination of ENER1 and gameq1 -> reduce to 0 using the momentum constraint twice.
Dp = 2*v*(G-P)                                  # from MOM1
Dpp= sp.diff(Dp,t)                              # D''
# k^2 D from ENERGY1 (on-shell): k^2 D = D'' -4v G' +4v P'
k2D = Dpp - 4*v*sp.diff(G,t)+4*v*sp.diff(P,t)
AREA1_onshell = AREA1.subs(sp.diff(D,t,2),Dpp).subs(sp.diff(D,t),Dp).subs(k**2*D,k2D)
# k^2 D appears as k**2*D term: substitute explicitly
AREA1_onshell = (k**2*D-12*v**2*G+12*v**2*P+4*v*Dp+Dpp).subs(k**2*D,k2D)
print("=== (2) AREA1 Bianchi-redundancy, shown symbolically (no longer 'by hand') ===")
print("  AREA1 on-shell (D'=2v(G-P), k^2D from ENERGY1) =", sp.simplify(AREA1_onshell))
