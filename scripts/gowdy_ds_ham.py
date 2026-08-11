import sympy as sp
t,z,Lam=sp.symbols('t z Lambda',real=True)
psi=sp.Function('psi')(t,z); gam=sp.Function('gamma')(t,z); R=sp.Function('R')(t,z)
pt,pz=sp.diff(psi,t),sp.diff(psi,z); gt,gz=sp.diff(gam,t),sp.diff(gam,z); Rt,Rz=sp.diff(R,t),sp.diff(R,z)

# Reduced first-order Lagrangian density (derived by IBP from the raw L):
Lred = 2*R*(pt**2-pz**2) - 2*(Rt*gt - Rz*gz) - 2*Lam*R*sp.exp(2*(gam-psi))

def EL(field):
    ft,fz=sp.diff(field,t),sp.diff(field,z)
    return sp.simplify(sp.diff(sp.diff(Lred,ft),t)+sp.diff(sp.diff(Lred,fz),z)-sp.diff(Lred,field))

src=R*sp.exp(2*(gam-psi))
WAVE=sp.diff(R*pt,t)-sp.diff(R*pz,z)-Lam*src
AREA=sp.diff(R,t,t)-sp.diff(R,z,z)-2*Lam*src
gameq=sp.diff(gam,t,t)-sp.diff(gam,z,z)+pt**2-pz**2-Lam*sp.exp(2*(gam-psi))

print("EL_psi / 4  - WAVE  =", sp.simplify(EL(psi)/4-WAVE))     # psi eom = WAVE
print("EL_gam /-2  - AREA  =", sp.simplify(EL(gam)/(-2) - AREA))      # gamma eom = AREA
print("EL_R   gives gamma-eq:", sp.simplify(EL(R)/2 + gameq))      # R eom = gamma-eq (constraint-ish)

# Canonical momenta (t = time)
p_psi=sp.simplify(sp.diff(Lred,pt))
p_gam=sp.simplify(sp.diff(Lred,gt))
p_R  =sp.simplify(sp.diff(Lred,Rt))
print("\np_psi =",p_psi,"   p_gam =",p_gam,"   p_R =",p_R)

# Legendre transform -> Hamiltonian density, expressed in momenta
Ppsi,Pgam,PR=sp.symbols('P_psi P_gamma P_R',real=True)
# invert velocities
psit=Ppsi/(4*R); gamt=-PR/2; Rt_=-Pgam/2
H = Ppsi*psit + Pgam*gamt + PR*Rt_ - Lred.subs({pt:psit, gt:gamt, Rt:Rt_})
H = sp.simplify(sp.expand(H))
print("\n=== Hamiltonian density H (in momenta; z-derivatives are gradients) ===")
print(sp.simplify(H))
