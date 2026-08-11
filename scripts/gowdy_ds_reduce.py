import sympy as sp
t,z,Lam=sp.symbols('t z Lambda',real=True,positive=True)
PSI=sp.Function('psi'); GAM=sp.Function('gamma'); RR=sp.Function('R')
psi=PSI(t,z); gam=GAM(t,z); R=RR(t,z)

# --- Lambda=0 : area-time gauge R=t is consistent (R harmonic) ---
print("=== Lambda=0, area-time R=t ===")
# AREA with Lam=0: R_tt - R_zz = 0.  R=t -> 0-0=0  OK (consistent)
print("AREA(Lam=0) with R=t :", sp.simplify(sp.diff(t,t,t)-sp.diff(t,z,z)), " (0 = consistent)")
# Constraints fix gamma:  ENERGY -> gamma_t,  MOMENTUM -> gamma_z   (R=t)
pt,pz=sp.symbols('psi_t psi_z',real=True)
# ENERGY (Lam irrelevant here): 2(R_t g_t + R_z g_z) - (R_tt+R_zz) = 2R(pt^2+pz^2); R=t
gam_t_sol = sp.solve(sp.Eq(2*(1*sp.Symbol('g_t')+0) - 0, 2*t*(pt**2+pz**2)), sp.Symbol('g_t'))[0]
gam_z_sol = sp.solve(sp.Eq(1*sp.Symbol('g_z')+0 - 0, 2*t*pt*pz), sp.Symbol('g_z'))[0]
print("gamma_t =", gam_t_sol, "   gamma_z =", gam_z_sol, "  (gamma determined by psi)")

# Reduced physical Hamiltonian on (psi,p_psi):  H = int [ p_psi^2/(8 R) + 2 R psi_z^2 ], R=t
# Hamilton -> Gowdy wave eqn?
psi2=PSI(t,z); ppsi=4*t*sp.diff(psi2,t)   # p_psi = 4R psi_t, R=t
# p_psi_t = -dH/dpsi = +d/dz(4 t psi_z)
lhs=sp.diff(ppsi,t); rhs=sp.diff(4*t*sp.diff(psi2,z),z)
gowdy_wave = sp.simplify((lhs-rhs)/(4*t))
print("Hamilton(H_phys) -> ", sp.simplify(gowdy_wave), " = 0  i.e.  psi_tt + psi_t/t - psi_zz = 0 (Gowdy/Bessel)")
print("  check vs psi_tt+psi_t/t-psi_zz:", sp.simplify(gowdy_wave-(sp.diff(psi2,t,t)+sp.diff(psi2,t)/t-sp.diff(psi2,z,z))))

print("\n=== Lambda>0 : area-time R=t is INCONSISTENT ===")
# AREA: R_tt - R_zz = 2 Lam R e^{2(gam-psi)}.  Put R=t:  0 = 2 Lam t e^{...}  -> contradiction
area_with_Rt = sp.simplify(sp.diff(t,t,t)-sp.diff(t,z,z) - 2*Lam*t*sp.exp(2*(gam-psi)))
print("AREA with R=t  =>  0 - 2*Lam*t*e^{2(gam-psi)} =", area_with_Rt, " != 0  (R not harmonic; area-time fails)")
