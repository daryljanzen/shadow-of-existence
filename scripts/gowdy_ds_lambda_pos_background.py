# Nonlinear Lambda>0 Gowdy-dS, first bite (c17, charting the field-DOF frontier).
# Established at source (gowdy_ds_canonical_1.py, gowdy_ds_reduce.py): area-time R=t is
# INCONSISTENT at Lambda>0 (AREA: R_tt-R_zz=2*Lam*R*e^{2(gam-psi)} != 0 with R=t). So the
# substrate cosmic-time foliation must replace it. FIRST PROBE: does the Lambda>0 system have a
# consistent isotropic de Sitter background, and what is its cosmic-time clock? The graviton is
# the anisotropic departure from it; this grounds the foliation the nonlinear evolution uses.
import sympy as sp
t,Lam = sp.symbols('t Lambda', real=True, positive=True)
psi=sp.Function('psi'); gam=sp.Function('gamma'); R=sp.Function('R')
ps=psi(t); gm=gam(t); Rr=R(t)

# Homogeneous (d_z=0) field equations, from source (gowdy_ds_canonical_1.py lines 42-46):
src = Rr*sp.exp(2*(gm-ps))
AREA   = sp.diff(Rr,t,t) - 2*Lam*src
WAVE   = sp.diff(Rr*sp.diff(ps,t),t) - Lam*src
ENERGY = 2*sp.diff(Rr,t)*sp.diff(gm,t) - sp.diff(Rr,t,t) - 2*Rr*sp.diff(ps,t)**2   # constraint
GAMEQ  = sp.diff(gm,t,t) + sp.diff(ps,t)**2 - Lam*sp.exp(2*(gm-ps))
print("MOMENTUM is trivial (d_z=0).  Four homogeneous eqs: AREA, WAVE, ENERGY(constraint), GAMEQ.\n")

# --- Isotropic ansatz: all three spatial scale factors equal ---
# spatial metric diag pieces: z: e^{2(gam-psi)},  x: e^{2psi},  y: R^2 e^{-2psi}
# isotropy  e^{2(gam-psi)} = e^{2psi} = R^2 e^{-2psi}  =>  gam=2psi,  R=e^{2psi}
f = sp.Function('f')  # let psi=f(t) be free; gam=2f, R=e^{2f}
subs_iso = {gm: 2*f(t), Rr: sp.exp(2*f(t)), ps: f(t)}
def apply(expr):
    e = expr
    # substitute functions and their derivatives by rewriting in terms of f
    e = e.subs(sp.diff(ps,t,t), sp.diff(f(t),t,t)).subs(sp.diff(ps,t), sp.diff(f(t),t)).subs(ps, f(t))
    e = e.subs(sp.diff(gm,t,t), 2*sp.diff(f(t),t,t)).subs(sp.diff(gm,t), 2*sp.diff(f(t),t)).subs(gm, 2*f(t))
    Rexpr = sp.exp(2*f(t))
    e = e.subs(sp.diff(Rr,t,t), sp.diff(Rexpr,t,t)).subs(sp.diff(Rr,t), sp.diff(Rexpr,t)).subs(Rr, Rexpr)
    return sp.simplify(e)

ft, ftt = sp.diff(f(t),t), sp.diff(f(t),t,t)
print("Under the isotropic ansatz gam=2psi, R=e^{2psi}  (psi=f(t)):")
for name,E in [("AREA",AREA),("WAVE",WAVE),("ENERGY(constraint)",ENERGY),("GAMEQ",GAMEQ)]:
    red = apply(E)
    # divide out e^{2f} to read the bracket
    red_over = sp.simplify(red/sp.exp(2*f(t)))
    print(f"  {name:18s}/e^2psi = {red_over}  = 0")

# So: ENERGY -> psi_tt = psi_t^2 ;  AREA/WAVE/GAMEQ -> 3 psi_t^2 = Lam e^{2psi}
print("\n=> constraint ENERGY: psi_tt = psi_t^2 ;  dynamics: 3 psi_t^2 = Lam e^{2psi}")

# --- The de Sitter solution: psi_t = sqrt(Lam/3) e^{psi} ---
H = sp.sqrt(Lam/3)
psidot_sol = H*sp.exp(f(t))
# check it satisfies BOTH 3 psi_t^2 = Lam e^{2psi}  AND  psi_tt = psi_t^2
chk_dyn = sp.simplify(3*psidot_sol**2 - Lam*sp.exp(2*f(t)))
# psi_tt = d/dt[sqrt(Lam/3) e^{f}] = sqrt(Lam/3) e^{f} f_t = psidot_sol * psidot_sol = psi_t^2
chk_con = sp.simplify(psidot_sol*sp.diff(f(t),t).subs(sp.diff(f(t),t), psidot_sol) - psidot_sol**2)
print(f"\nde Sitter sol psi_t = sqrt(Lam/3) e^psi:")
print(f"  dynamics residual  3 psi_t^2 - Lam e^2psi = {chk_dyn}")
print(f"  constraint psi_tt - psi_t^2 = {chk_con}   (psi_tt=psi_t*d psi_t/dpsi *psi_t = psi_t^2, since dpsi_t/dpsi=psi_t)")

# scale factor a=e^{psi}, lapse N=e^{gam-psi}=e^{psi}, cosmic time dtau=N dt=e^psi dt
# a(tau): da/dtau = (da/dt)/(dtau/dt) = (e^psi psi_t)/(e^psi) = psi_t = sqrt(Lam/3) e^psi = sqrt(Lam/3) a
print("\nLapse N=e^{gam-psi}=e^{psi}=a (scale factor).  Cosmic time dtau=N dt=a dt.")
print("  da/dtau = psi_t = sqrt(Lam/3) e^psi = sqrt(Lam/3) a   =>   a(tau)=a0 e^{H tau},  H=sqrt(Lam/3).")
print("  => isotropic background is exact de Sitter, H^2 = Lam/3. COSMIC-TIME CLOCK ESTABLISHED.")
