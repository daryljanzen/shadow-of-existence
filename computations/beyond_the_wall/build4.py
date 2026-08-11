"""L-163 build, step 4: identify the structure the equations actually have."""
import sympy as sp, pickle
t,z = sp.symbols('t z', real=True)
psi=sp.Function('psi')(t,z); gam=sp.Function('gamma')(t,z)
om =sp.Function('omega')(t,z); R  =sp.Function('R')(t,z)
Lam=sp.Symbol('Lambda', positive=True); E=sp.exp
s=pickle.load(open('sol.pkl','rb'))
dt=lambda e: sp.diff(e,t); dz=lambda e: sp.diff(e,z)
sub={sp.Derivative(psi,(t,2)): s[sp.Derivative(psi,(t,2))],
     sp.Derivative(om ,(t,2)): s[sp.Derivative(om ,(t,2))],
     sp.Derivative(R  ,(t,2)): s[sp.Derivative(R  ,(t,2))],
     sp.Derivative(gam,(t,2)): s[sp.Derivative(gam,(t,2))]}
def onshell(e): return sp.simplify(sp.expand(sp.expand(e).subs(sub)))

# (1) the omega equation:  d_t( R e^{4psi} om_t ) - d_z( R e^{4psi} om_z ) = 0
W = R*E(4*psi)
OMEQ = dt(W*dt(om)) - dz(W*dz(om))
print("(1) d_t(R e^{4psi} om_t) - d_z(R e^{4psi} om_z) on shell =", onshell(OMEQ))

# (2) the psi equation: wave-map partner with the Lambda source
PSIEQ = dt(R*dt(psi)) - dz(R*dz(psi)) - sp.Rational(1,2)*R*E(4*psi)*(dt(om)**2 - dz(om)**2) \
        - Lam*R*E(2*(gam-psi))
print("(2) [d_t(R psi_t) - d_z(R psi_z)] - (R/2)e^{4psi}(om_t^2-om_z^2) - Lam R e^{2(gam-psi)}"
      " on shell =", onshell(PSIEQ))

# (3) the area equation, unchanged from the polarized case
AREA = dt(dt(R)) - dz(dz(R)) - 2*Lam*R*E(2*(gam-psi))
print("(3) R_tt - R_zz - 2 Lam R e^{2(gam-psi)} on shell =", onshell(AREA))

# (4) the constraints
EN  = 2*(dt(R)*dt(gam) + dz(R)*dz(gam)) - (s[sp.Derivative(R,(t,2))] + dz(dz(R))) \
      - 2*R*(dt(psi)**2 + dz(psi)**2) - sp.Rational(1,2)*R*E(4*psi)*(dt(om)**2 + dz(om)**2)
print("(4) ENERGY residual on shell =", sp.simplify(sp.expand(EN.subs(sub))))
MO  = dt(R)*dz(gam) + dz(R)*dt(gam) - dt(dz(R)) - 2*R*dt(psi)*dz(psi) \
      - sp.Rational(1,2)*R*E(4*psi)*dt(om)*dz(om)
print("(5) MOMENTUM residual on shell =", sp.simplify(sp.expand(MO.subs(sub))))
