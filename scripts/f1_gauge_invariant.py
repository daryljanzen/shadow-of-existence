import sympy as sp
t,k = sp.symbols('t k', real=True, positive=True)   # conformal time t<0; use -|t|, a=-1/(H t)
# Concrete dS background in conformal time: psi0'=-1/t, psi0''=1/t^2=psi0'^2 (verified).
v  = -1/t          # psi0' = -1/t
vp = 1/t**2        # psi0'' = 1/t^2 = v^2  (check: v^2=1/t^2 OK)
P=sp.Function('P')(t); G=sp.Function('G')(t)
def WAVE1(P,G): return sp.diff(P,t,2) + 2*v*sp.diff(P,t) + k**2*P + 4*v**2*(P-G)
def GAMEQ1(P,G): return sp.diff(G,t,2) + 2*v*sp.diff(P,t) + k**2*G - 6*v**2*G + 6*v**2*P

print("=== 1. does the pure-gauge mode (P_g,G_g)=(v T, 2 v T + T'),  T''=-k^2 T,  solve the homogeneous system? ===")
T=sp.Function('T')(t)
Pg = v*T
Gg = 2*v*T + sp.diff(T,t)
def reduceT(e):  # impose conformal-Killing T''=-k^2 T (and its derivatives)
    e=sp.expand(sp.simplify(e))
    e=e.subs(sp.diff(T,t,3), -k**2*sp.diff(T,t))
    e=e.subs(sp.diff(T,t,2), -k**2*T)
    return sp.simplify(e)
print("  WAVE1[P_g,G_g]  =", reduceT(WAVE1(Pg,Gg)))
print("  GAMEQ1[P_g,G_g] =", reduceT(GAMEQ1(Pg,Gg)))

print("\n=== 2. gauge-invariant Q = G - P - P'/psi0' = G - P + t P' :  check delta_gauge Q = 0 ===")
dP=Pg; dG=Gg
Q_of=lambda P,G: G - P + t*sp.diff(P,t)
dQ = Q_of(P+sp.Symbol('e')*dP, G+sp.Symbol('e')*dG)
dQ = sp.diff(dQ, sp.Symbol('e'))   # the O(e) gauge shift of Q
print("  delta_gauge Q =", reduceT(sp.simplify(dQ)))

print("\n=== 3. numerical: integrate the coupled system, form Q(t), test (a) bounded as t->0^- (a->inf), (b) gauge-invariance ===")
import numpy as np
from scipy.integrate import solve_ivp
kk=2.0
def rhs2(tt,y):
    Pr,dPr,Gr,dGr=y; vv=-1.0/tt; v2=1.0/tt**2
    ddPr=-2*vv*dPr - kk**2*Pr - 4*v2*(Pr-Gr)
    ddGr=-2*vv*dPr - kk**2*Gr + 6*v2*Gr - 6*v2*Pr
    return [dPr,ddPr,dGr,ddGr]
t0,tf=-10.0,-1e-3
# generic physical initial data
y0=[0.7,0.2,-0.3,0.5]
s=solve_ivp(rhs2,[t0,tf],y0,rtol=1e-10,atol=1e-12,dense_output=True,max_step=0.01)
tg=np.linspace(t0,tf,4000)
Pr,dPr,Gr,dGr=s.sol(tg)
Q=Gr-Pr+tg*dPr
print("  |Q| over the run:  min=%.4e  max=%.4e  final(t->0^-)=%.4e"%(np.min(np.abs(Q)),np.max(np.abs(Q)),Q[-1]))
print("  |P| final=%.4e  |G| final=%.4e"%(abs(Pr[-1]),abs(Gr[-1])))
# gauge-invariance: add a gauge mode T=cos(k t)+... with T''=-k^2 T => T=cos(kt),sin(kt)
amp=3.0
def add_gauge(y0,t0):
    T=amp*np.cos(kk*t0); Tp=-amp*kk*np.sin(kk*t0)
    vv=-1.0/t0
    # P->P+vT, P'->P'+(vT)'=v'T+vT' ; G->G+2vT+T', G'->...
    vpp=1.0/t0**2
    dP_=vv*T; dPp_=vpp*T+vv*Tp
    dG_=2*vv*T+Tp; dGp_=2*vpp*T+2*vv*Tp + (-kk**2*T)  # T''=-k^2T
    return [y0[0]+dP_, y0[1]+dPp_, y0[2]+dG_, y0[3]+dGp_]
y0g=add_gauge(y0,t0)
s2=solve_ivp(rhs2,[t0,tf],y0g,rtol=1e-10,atol=1e-12,dense_output=True,max_step=0.01)
Pr2,dPr2,Gr2,dGr2=s2.sol(tg)
Q2=Gr2-Pr2+tg*dPr2
print("  after adding a gauge mode (amp=%.1f):  max|Q2-Q| = %.3e   (0 => Q is gauge-invariant)"%(amp,np.max(np.abs(Q2-Q))))
print("    (note |P2-P| max=%.3e -- the gauge mode DID move P,G; Q is unmoved)"%np.max(np.abs(Pr2-Pr)))
