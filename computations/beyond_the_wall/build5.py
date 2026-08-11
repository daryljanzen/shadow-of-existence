"""L-163 build, step 5: the correct wave-map identification."""
import sympy as sp, pickle
t,z = sp.symbols('t z', real=True)
psi=sp.Function('psi')(t,z); gam=sp.Function('gamma')(t,z)
om =sp.Function('omega')(t,z); R  =sp.Function('R')(t,z)
Lam=sp.Symbol('Lambda', positive=True); E=sp.exp
s=pickle.load(open('sol.pkl','rb'))
dt=lambda e: sp.diff(e,t); dz=lambda e: sp.diff(e,z)
sub={k:v for k,v in s.items()}
def onshell(e):
    e=sp.expand(e).subs(sub)
    return sp.simplify(sp.expand(sp.powsimp(sp.expand(e),force=True)))

P = 2*psi - sp.log(R); Q = om
print("wave-map coordinates:  P = 2 psi - ln R ,  Q = omega")
print("target metric        :  dP^2 + e^{2P} dQ^2   (Gaussian curvature -1)")
print()
WQ = dt(R*E(2*P)*dt(Q)) - dz(R*E(2*P)*dz(Q))
print("(Q)  d_t(R e^{2P} Q_t) - d_z(R e^{2P} Q_z)          on shell =", onshell(WQ))
WP = dt(R*dt(P)) - dz(R*dz(P)) - R*E(2*P)*(dt(Q)**2 - dz(Q)**2)
print("(P)  d_t(R P_t) - d_z(R P_z) - R e^{2P}(Q_t^2-Q_z^2) on shell =", onshell(WP))
AR = onshell(dt(dt(R)) - dz(dz(R)))
print("\n(AREA) R_tt - R_zz on shell =", AR)
print("       compare 2 Lam R e^{2(gam-psi)} :", sp.simplify(AR - 2*Lam*R*E(2*(gam-psi))))
