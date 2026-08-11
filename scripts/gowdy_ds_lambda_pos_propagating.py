# Nonlinear Lambda>0 Gowdy-dS, third bite (c17, r275): the PROPAGATING (inhomogeneous, psi_z!=0)
# graviton on the de Sitter background (r273) -- the sector where any FORCE must live (r274 closed
# the homogeneous sector as ADMIT). FIRST sub-step: the LINEARIZED propagating graviton, fixed
# background (TT truncation delta-gamma=delta-R=0). Built on the source WAVE eq (gowdy_ds_canonical_1.py).
import sympy as sp
t,z,Lam,H,k = sp.symbols('t z Lambda H k', real=True, positive=True)

# --- Background (r273): psi0(t), gam0=2 psi0, R0=e^{2 psi0};  e^{2(gam0-psi0)}=e^{2psi0}=R0 ---
psi0=sp.Function('psi0')(t); R0=sp.exp(2*psi0)
# background WAVE: (R0 psi0')' = Lam R0 e^{2(gam0-psi0)} = Lam R0^2  (sanity, r273)
bg_wave = sp.simplify(sp.diff(R0*sp.diff(psi0,t),t) - Lam*R0*sp.exp(2*((2*psi0)-psi0)))
print("background WAVE residual form (must vanish on the r273 background):")
print("  (R0 psi0')' - Lam R0 e^{2psi0} =", sp.simplify(bg_wave/R0), "* R0   [the r273 bg eq]\n")

# --- Linearize WAVE on the propagating graviton, fixed background (delta-gam=delta-R=0) ---
# WAVE = (R psi_t)_t - (R psi_z)_z - Lam R e^{2(gam-psi)} ;  psi=psi0+eps*dp(t,z), gam=2psi0, R=R0
eps=sp.symbols('epsilon'); dp=sp.Function('dp')(t,z)
psi=psi0+eps*dp; gam=2*psi0; R=R0
WAVE = sp.diff(R*sp.diff(psi,t),t) - sp.diff(R*sp.diff(psi,z),z) - Lam*R*sp.exp(2*(gam-psi))
lin = sp.simplify(sp.diff(WAVE,eps).subs(eps,0))   # O(eps) part
lin_over_R0 = sp.simplify(lin/R0)
print("Linearized WAVE / R0  (fixed background) = 0:")
print("  ", lin_over_R0, "= 0")
# expected:  dp_tt + 2 psi0' dp_t - dp_zz + 2 Lam e^{2psi0} dp = 0
expected = sp.diff(dp,t,t) + 2*sp.diff(psi0,t)*sp.diff(dp,t) - sp.diff(dp,z,z) + 2*Lam*sp.exp(2*psi0)*dp
print("  matches  dp_tt + 2 psi0' dp_t - dp_zz + 2 Lam e^{2psi0} dp ? ->", sp.simplify(lin_over_R0-expected),"\n")

# --- Convert to cosmic time tau (dtau = N dt, N=e^{gam0-psi0}=e^{psi0}=a; a=e^{psi0}, a_tau/a=H) ---
# Verify by back-conversion: take the proposed cosmic-time eq and convert d/dtau=(1/a)d/dt; must match.
a=sp.Function('a')(t)
DP=sp.Function('DP')   # dp as fn of tau; we test via operators
# proposed cosmic-time eq:  dp_tautau + 3H dp_tau + (k^2/a^2) dp + 2 Lam dp = 0   (dp_zz -> -k^2 dp)
# back-convert: d/dtau=(1/a)d/dt ; dp_tau=(1/a)dp_t ; dp_tautau=(1/a^2)dp_tt-(a_t/a^3)dp_t
dpt,dptt=sp.symbols('dp_t dp_tt')
at=sp.Symbol('a_t'); aa=sp.Symbol('a')
dp_tau=dpt/aa
dp_tautau=dptt/aa**2 - at*dpt/aa**3
cosmic = dp_tautau + 3*H*dp_tau + (k**2/aa**2)*sp.Symbol('dp') + 2*Lam*sp.Symbol('dp')
cosmic_times_a2 = sp.expand(cosmic*aa**2)
# use a_t/a = psi0' = H a  =>  a_t = H a^2 ;  and k^2 dp -> -dp_zz
cosmic_in_t = cosmic_times_a2.subs(at, H*aa**2)
print("Cosmic-time eq  dp_tautau+3H dp_tau+(k^2/a^2)dp+2Lam dp=0, back-converted to t (x a^2):")
print("  ", sp.simplify(cosmic_in_t))
print("  = dp_tt + 2H a dp_t + k^2 dp + 2 Lam a^2 dp   ; with psi0'=Ha and k^2 dp->-dp_zz, a^2=e^{2psi0}:")
print("  = dp_tt + 2 psi0' dp_t - dp_zz + 2 Lam e^{2psi0} dp   == the linearized t-equation above. VERIFIED.\n")

print("RESULT (r275): the linearized propagating graviton on the de Sitter background satisfies")
print("  dp_tautau + 3H dp_tau + (k^2/a^2) dp + 2Lam dp = 0   (cosmic time, a=e^{H tau}, H^2=Lam/3),")
print("  a de Sitter wave equation: Hubble friction 3H, redshifting gradient k^2/a^2, effective")
print("  mass^2 = 2Lam = 6H^2 (>0, principal series). This ADMITS a clean unitary (Bunch-Davies)")
print("  quantization -- so the PROPAGATING sector's linearized part ADMITS, explicitly, in the")
print("  CR cosmic-time foliation. [honest scope: fixed-background TT truncation (dgam=dR=0); the")
print("  constraint back-reaction may shift the mass; the FULL NONLINEAR back-reaction = the open")
print("  FORCE question, the next bite.]")
