# Nonlinear Lambda>0 Gowdy-dS, second bite (c17, r274): the graviton's back-reaction on the
# de Sitter background, HOMOGENEOUS (non-propagating) sector. The graviton = anisotropic departure
# from the isotropic background (r273). Question: does the nonlinear back-reaction force structure,
# or admit clean classical dynamics? Result rests on an EXACT analytic first integral (below),
# NOT numerics: free numerical evolution of this constrained system is stiff and constraint-violating
# in the de Sitter blow-up (a naive solve_ivp drove the ENERGY constraint and C0 to ~1e40), so it is
# not used as evidence — the first integral is exact on shell. Built on gowdy_ds_canonical_1.py.
import sympy as sp
t,Lam = sp.symbols('t Lambda', real=True, positive=True)
psi=sp.Function('psi')(t); gam=sp.Function('gamma')(t); R=sp.Function('R')(t)
src = R*sp.exp(2*(gam-psi))
AREA   = sp.diff(R,t,t) - 2*Lam*src                                  # R_tt - 2 Lam R e^{2(g-p)}
WAVE   = sp.diff(R*sp.diff(psi,t),t) - Lam*src                        # (R psi_t)_t - Lam R e^{2(g-p)}
ENERGY = 2*sp.diff(R,t)*sp.diff(gam,t) - sp.diff(R,t,t) - 2*R*sp.diff(psi,t)**2   # constraint

# --- The exact first integral: in AREA - 2*WAVE the Lambda source cancels identically ---
diff_eq = sp.simplify(AREA - 2*WAVE)
print("AREA - 2*WAVE =", diff_eq)
print("  = R_tt - 2(R psi_t)_t   (the 2*Lam*src cancels exactly)  =>  R_tt = 2 (R psi_t)_t")
C0 = sp.diff(R,t) - 2*R*sp.diff(psi,t)
print("d/dt[ R_t - 2 R psi_t ] =", sp.simplify(sp.diff(C0,t) - (AREA - 2*WAVE)), "+ (AREA-2WAVE)")
print("  => on shell d/dt[R_t - 2 R psi_t] = 0:  FIRST INTEGRAL  C0 := R_t - 2 R psi_t = const.\n")

# --- The shape (graviton) s = psi - (1/2)ln R ;  a_x/a_y = e^{2s} (s=0 = isotropic background) ---
print("Shape s = psi - (1/2)ln R ;  a_x/a_y = e^{2s};  s=0 on the isotropic de Sitter background (r273).")
print("  2 R s_t = 2 R psi_t - R_t = -C0   =>   ds/dt = -C0/(2R).")
print("  Lapse N = e^{gam-psi};  spatial volume V = sqrt(g_xx g_yy g_zz) = R e^{gam-psi} = R N.")
print("  => COSMIC-TIME shear  ds/dtau = (ds/dt)/N = -C0/(2 R N) = -C0/(2V).")
print()
print("RESULT (exact, on shell):")
print("  * C0 = R_t - 2 R psi_t is a CONSERVED shear charge of the homogeneous Lambda>0 system")
print("    (= -(p_gamma + p_psi)/2 in the canonical variables p_gamma=-2R_t, p_psi=4R psi_t... ")
print("     -(p_gamma+p_psi)/2 = -(-2R_t + 4R psi_t)/2 = R_t - 2R psi_t = C0). ")
print("  * the graviton shear ds/dtau = -C0/(2V) DECAYS AS 1/VOLUME as de Sitter expands (V->inf):")
print("    cosmic no-hair. The isotropic de Sitter background is an ATTRACTOR.")
print("  => the homogeneous nonlinear Lambda>0 back-reaction ADMITS clean classical dynamics")
print("     (a conserved charge + a monotone decay law); nothing forces structure here.")
print("     Forcing, if real, is pushed to the PROPAGATING (inhomogeneous) sector or the")
print("     discrete S3/A2 skeleton (Move 13, do-not-assert) -- per spine s6.")

# sanity: verify the canonical-momentum identity C0 = -(p_gamma+p_psi)/2 symbolically
pg = -2*sp.diff(R,t); pp = 4*R*sp.diff(psi,t)
print("\ncheck  C0 - (-(p_gamma+p_psi)/2) =", sp.simplify(C0 - (-(pg+pp)/2)), " (0 confirms the identity)")
