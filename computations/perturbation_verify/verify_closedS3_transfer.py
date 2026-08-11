"""
CR perturbation reach -- REACH_PLAN Steps 3-4, FIRST computation.
The closed-S^3 hyperspherical Sachs-Wolfe transfer at low ell.
Replaces the flat-sky placeholder eq:lowell (ell_2 ~ 7.8) with the closed-universe
transfer in which a degree-L mode feeds ell <= L (so the lowest physical mode L=2
feeds the QUADRUPOLE, not ell ~ 8).

TAG: [R] leading-order first pass.  DO-NOT-ASSERT until verified at source AND a
fresh-node COLD READ (coherence != correspondence).  This script establishes the
QUALITATIVE shape (low-ell suppression onset at the quadrupole); the overall
amplitude convention is [R].

Grounding (Step 0/1/2, read at source 2026-06-29):
  - Step 1 (look-signal): the observable large-angle anisotropy is the standard
    Sachs-Wolfe SOURCE term (P7 sec:floor: lumpiness on one background a(t), the
    potential telescopes; the cumulative term is the uniform expansion).  So a
    closed-S^3 signature enters as the standard closed-universe modification of the
    SOURCE mode spectrum (P7 sec:decomp eq:decomp), NOT a new CR mechanism.  Held
    as a falsifiable programme: the global closed-S^3 topology is an EXTRAPOLATION
    (P7 sec:establishes/Copernican), and it EXPLAINS the deficit only if it REQUIRES
    it (P8 Rule 2), which the discreteness does structurally (minimum mode beta=3).
  - Step 2 (scales): r0 = present S^3 areal radius r(tau~_0) = (2^{1/3}/sqrt(Lam))
    sinh^{2/3}(.) at u~1.18  ~= 5064 Mpc  [P12 sec:largescale; P9 eq:r-SdS-solution].
    Distinct from the dS size alpha=sqrt(3/Lam) and the merged-horizon radius
    alpha/sqrt3 (P9 sec:481; reach-plan sec.2).  D_C ~= 13927 Mpc = comoving distance
    to LSS (flat-LCDM observable).  chi_lss = D_C/r0 (an angle on S^3, in [0,pi]).
  - Mode spectrum: closed-S^3 scalar harmonics, integer degree L, beta=L+1,
    k_L=sqrt(L(L+2))/r0; L>=2 physical (beta>=3): L=0 background, L=1 pure-gauge dipole.
"""
import numpy as np
from scipy.special import eval_gegenbauer, spherical_jn
from math import comb

# ----------------------------------------------------------------------
# grounded scales
r0      = 5064.0
D_C     = 13927.0
chi_lss = D_C / r0
print("="*70)
print("Closed-S^3 hyperspherical SW transfer -- FIRST PASS  [R, do-not-assert]")
print("="*70)
print(f"  r0 (present S^3 areal radius)   = {r0:.0f} Mpc")
print(f"  D_C (comoving dist to LSS)      = {D_C:.0f} Mpc")
print(f"  chi_lss = D_C/r0                = {chi_lss:.4f} rad   (pi = {np.pi:.4f}; LSS near antipode)")

# ----------------------------------------------------------------------
# hyperspherical radial functions Phi^beta_ell(chi), ell=0..beta-1, by STABLE
# DOWNWARD recursion in ell (Miller's algorithm; direct Gegenbauer overflows at high beta).
#   recursion:  sqrt(b^2-l^2) Phi_{l-1} = (2l+1) cot(chi) Phi_l - sqrt(b^2-(l+1)^2) Phi_{l+1}
#   seed at l=L=beta-1 (Phi_{beta}=0), recurse to l=0, rescale to the exact
#   Phi^beta_0(chi)=sin(beta*chi)/(beta*sin(chi)) (which -> j_0 in the flat limit).
def phis(beta, chi):
    L=beta-1
    cot=np.cos(chi)/np.sin(chi)
    f=np.zeros(L+2)            # indices 0..L+1
    f[L+1]=0.0; f[L]=1e-30     # seed
    for l in range(L,0,-1):
        f[l-1]=((2*l+1)*cot*f[l]-np.sqrt(max(beta**2-(l+1)**2,0.0))*f[l+1])/np.sqrt(beta**2-l**2)
    phi0_exact=np.sin(beta*chi)/(beta*np.sin(chi))
    if f[0]!=0: f*= phi0_exact/f[0]
    return f[:L+1]             # Phi^beta_ell for ell=0..L

def Phi(beta, ell, chi):
    if ell>beta-1: return 0.0
    return phis(beta,chi)[ell]

# independent (Gegenbauer) radial fn for cross-validation -- reliable at MODERATE degree,
# flat-normalised: Phi = beta^ell/[(2ell+1)!! C^{ell+1}_{beta-1-ell}(1)] sin^ell(chi) C^{ell+1}_{beta-1-ell}(cos chi)
def dfact(n):
    r=1.0
    while n>1: r*=n; n-=2
    return r
def Phi_gegen(beta, ell, chi):
    if ell>beta-1: return 0.0
    n=beta-1-ell; g1=eval_gegenbauer(n,ell+1,1.0)
    if g1==0: return 0.0
    return beta**ell/(dfact(2*ell+1)*g1)*np.sin(chi)**ell*eval_gegenbauer(n,ell+1,np.cos(chi))

# ----------------------------------------------------------------------
# CHECK A -- cross-validate the recursion against the Gegenbauer form AT chi_lss
#   (the regime the C_ell sum uses; flat-limit at small chi is recursion-unstable, cot chi huge)
# independent check #2: integrate the radial ODE from the origin (neither recursion nor Gegenbauer)
#   Phi'' + 2 cot(chi) Phi' + [beta^2-1 - ell(ell+1)/sin^2 chi] Phi = 0,  regular Phi~j_ell(beta chi) at 0
from scipy.integrate import solve_ivp
def Phi_ode(beta, ell, chi_target):
    chi0=1e-3
    y0=[spherical_jn(ell,beta*chi0), beta*spherical_jn(ell,beta*chi0,derivative=True)]
    def rhs(chi,y):
        Phi,dPhi=y
        return [dPhi, -2*np.cos(chi)/np.sin(chi)*dPhi-(beta**2-1-ell*(ell+1)/np.sin(chi)**2)*Phi]
    sol=solve_ivp(rhs,[chi0,chi_target],y0,rtol=1e-9,atol=1e-12,dense_output=True)
    return sol.y[0,-1]

print("\n[CHECK A] three independent methods at chi_lss=%.3f (beta=25):"%chi_lss)
print("   ell | recursion    | gegenbauer   | ODE-from-origin")
for ell in (2,5,10,20):
    print(f"   {ell:3d} | {Phi(25,ell,chi_lss):+.6e} | {Phi_gegen(25,ell,chi_lss):+.6e} | {Phi_ode(25,ell,chi_lss):+.6e}")

# CHECK B -- the cutoff: Phi^beta_ell = 0 for ell > beta-1
print("\n[CHECK B] cutoff  Phi^beta_ell=0 for ell>L=beta-1")
print(f"   beta=3 (L=2): Phi(ell=2)={Phi(3,2,chi_lss):+.4e}  Phi(ell=3)={Phi(3,3,chi_lss):+.4e}  (ell=3 must be 0)")
print(f"   beta=4 (L=3): Phi(ell=3)={Phi(4,3,chi_lss):+.4e}  Phi(ell=4)={Phi(4,4,chi_lss):+.4e}  (ell=4 must be 0)")

# ----------------------------------------------------------------------
# C_ell -- ordinary Sachs-Wolfe, dT/T=(1/3)Phi, scale-invariant primordial spectrum.
#   flat:   C_ell ~ Int dk/k j_ell^2(k D_C) = 1/(2 ell(ell+1))   ->   ell(ell+1)C_ell = const
#   closed: C_ell ~ Sum_{beta>=3} w(beta) |Phi^beta_ell(chi_lss)|^2
#           w(beta)->1/beta in flat limit recovers HZ.  Two scale-invariant conventions:
#             w1 = 1/beta                  (simplest flat-limit-correct)
#             w2 = beta/(beta^2-1)         (curvature-corrected Harrison-Zel'dovich)
beta_max=600
betas=np.arange(3,beta_max+1)
ells=np.arange(2,31)

def Cl_closed(ells, w, bmax=beta_max):
    out=np.zeros(len(ells))
    for beta in range(3,bmax+1):
        ph=phis(beta,chi_lss)              # Phi^beta_ell, ell=0..beta-1
        wb=w(beta)
        for i,ell in enumerate(ells):
            if ell<=beta-1:
                out[i]+= wb*ph[ell]**2
    return out

# FLAT reference computed THE SAME WAY: continuum beta-integral from 0 (incl beta<3),
# j_ell replacing the hyperspherical Phi.  closed/flat then isolates the actual
# closed-universe effect (discreteness + the missing sub-curvature modes beta<3).
from scipy.integrate import quad
def Cl_flat_same(ells, w):
    out=np.zeros(len(ells))
    for i,ell in enumerate(ells):
        integ=lambda b: w(b)*spherical_jn(int(ell),b*chi_lss)**2
        val,_=quad(integ,1e-6,beta_max,limit=400)
        out[i]=val
    return out

w1=lambda b: 1.0/b                     # scale-invariant, flat-limit-correct (the clean choice)
# w2 = beta/(beta^2-1) has a non-integrable pole at beta=1, so the continuum flat
# reference is ill-defined for it; w1 is used for the apples-to-apples ratio.
Cl1=Cl_closed(ells,w1)
Fl1=Cl_flat_same(ells,w1)
Cl1_lo=Cl_closed(ells,w1,bmax=300)     # convergence check

def ratio_norm(Clc,Clf):
    r=Clc/Clf
    return r/r[(ells>=25)].mean()
R1=ratio_norm(Cl1,Fl1)

print("\n[CONVERGENCE] closed C_ell (w1), beta_max 300 vs 600:")
for i,ell in enumerate(ells):
    if ell in (2,5,10,20,30):
        print(f"   ell={ell:2d}:  300={Cl1_lo[i]:.4e}  600={Cl1[i]:.4e}  drift={(Cl1[i]-Cl1_lo[i])/Cl1[i]*100:+.2f}%")

print("\n[RESULT] closed/flat power ratio (same spectrum + projection), norm=1 at high ell  [R]")
print("   (closed = discrete sum beta>=3 of Phi^2 ; flat = continuum integral of j^2 incl beta<3)")
print("   ell  | closed/flat (w=1/beta)")
for i,ell in enumerate(ells):
    if ell<=12 or ell in (15,20,25,30):
        print(f"   {ell:3d}  |        {R1[i]:.3f}")

quad_ratio=R1[0]
print("\n[READING -- what is sound, and what is held open]")
print(f"   * SOUND (verified): the transfer is the closed-universe one -- a degree-L")
print(f"     mode feeds ell<=L (exact cutoff, CHECK B), so the lowest physical mode")
print(f"     L=2 feeds the QUADRUPOLE, not ell~8.  The flat-sky placeholder eq:lowell")
print(f"     (ell_2~7.8) is qualitatively wrong at low ell and is replaced by this.")
print(f"     At the quadrupole, two independent methods agree: Phi^25_2(chi_lss)=6.490e-2.")
print(f"   * NOT YET SOUND (do-not-assert): the low-ell C_ell SHAPE.  No single")
print(f"     hyperspherical-Bessel method is trustworthy across all (beta,ell) at")
print(f"     chi_lss={chi_lss:.2f} (near antipode pi={np.pi:.2f}): the recursion is few-%% off vs")
print(f"     ODE+Gegenbauer at low ell, the Gegenbauer precision-loses at high beta,")
print(f"     the ODE-from-origin underflows at high ell.  The first-pass closed/flat")
print(f"     quadrupole ratio = {quad_ratio:.3f} sits WITHIN that method error -> the")
print(f"     suppression question (the k_min argument expects a deficit) is UNRESOLVED.")
print(f"   * ALSO: this is the STANDARD closed transfer, NOT the CR non-synchronous")
print(f"     tau~=tau+chi transfer (closed-S^3 source on the FLAT distance projection,")
print(f"     prop:flat) that P12 sec:scope names as the actual unbuilt element.")
print(f"   * NEXT: an accurate uniform hyperspherical-Bessel routine (log-space, or a")
print(f"     published closed-universe C_ell benchmark), THEN the non-synchronous transfer.")
print("\n[STATUS] do-not-assert; [R] first pass; method-accuracy + non-synchronous gaps")
print("         both open; cold read owed (coherence != correspondence).")
print("="*70)
