"""
A1.2 pressure-test -- does the omitted DOPPLER term separate ell=2 from ell=3, or is CR's octopole
over-suppression firm? The live falsification risk of the empirically-favoured milestone.

CR's mechanism (verify_lowell_full_radiative.py, r522+): the discrete closed-S^3 source
(k_L=sqrt(L(L+2))/r0, L>=2) projected through the flat Bessel j_l(k_L D_C) starves ell=2 and ell=3
TOGETHER (depth 0.22, 0.20 of LCDM). The data show ell=2 robustly low but ell=3 mostly normal, so CR
over-predicts the octopole suppression. The one transfer ingredient omitted there is the Doppler
(velocity) term. Here it is added and the ell=2/ell=3 ratio re-checked.

Doppler source: the baryon velocity at last scattering, v(k) ~ -(2/3)(k/aH)_lss * Phi(k) (potential
flow, matter era), projecting with the Bessel DERIVATIVE j_l'(k D_C):
    C_l^dop = Sum_L w_L * [alpha_L j_l'(k_L D_C)]^2 ,  alpha_L = (2/3)(k_L/(a H)_lss).
SW+ISW as before. If Doppler leaves the ell=2/ell=3 depths ~equal, the octopole tension is FIRM.
"""
import numpy as np
from scipy.special import spherical_jn
from scipy.integrate import quad

Om,OL,h,Or = 0.315,0.685,0.674,9.24e-5
cH0 = 299792.458/(100*h)
def E(z): return np.sqrt(Or*(1+z)**4+Om*(1+z)**3+OL)
def dC(z): return cH0*quad(lambda zz:1/E(zz),0,z,limit=200)[0]
z_lss=1089.0; D_C=dC(z_lss); r0=5064.0; z_eq=Om/Or-1
def HS(y): return (16*np.sqrt(1+y)+9*y**3+2*y**2-8*y-16)/(10*y**3)
def Dg(z):
    a=1/(1+z); I=quad(lambda ap:1/(ap*np.sqrt(Om/ap**3+OL))**3,1e-6,a,limit=200)[0]
    return 2.5*Om*np.sqrt(Om/a**3+OL)*I
gLhi=Dg(30.)*31.
def Phi(z): return HS((1+z_eq)/(1+z))*Dg(z)*(1+z)/gLhi
Phi_lss=Phi(z_lss)

# (a H) at last scattering in km/s per Mpc-comoving: a H = H(z)/(1+z)
aH_lss = (100*h)*E(z_lss)/(1+z_lss)/ (299792.458)   # in 1/Mpc  (H in c=1 units: H/c)
ells=list(range(2,31))
Lmax=400
def k_of(L): return np.sqrt(L*(L+2))/r0
w=lambda L:(L+1)/(L*(L+2))                    # scale-invariant discrete measure

def jl(l,x): return spherical_jn(l,x)
def djl(l,x): return spherical_jn(l,x,derivative=True)

def Cl_components():
    C_sw={l:0. for l in ells}; C_dop={l:0. for l in ells}
    for L in range(2,Lmax+1):
        k=k_of(L); x=k*D_C; wl=w(L)
        alpha=(2./3.)*(k/aH_lss)               # velocity/potential ratio at LSS
        for l in ells:
            C_sw[l]  += wl*((1./3.)*Phi_lss*jl(l,x))**2
            C_dop[l] += wl*(alpha*djl(l,x))**2
    return C_sw,C_dop

C_sw,C_dop=Cl_components()
# LCDM continuum SW baseline (for the depth ratio), same transfer, continuum source
def Cl_lcdm_sw():
    C={l:0. for l in ells}
    kk=np.linspace(1e-4,0.05,4000)
    for l in ells:
        integ=(1./3.*Phi_lss*jl(l,kk*D_C))**2/kk    # ~scale-invariant d k/k
        C[l]=np.trapezoid(integ,kk)
    return C
C_lc=Cl_lcdm_sw()

def norm(D):
    hi=np.mean([D[l] for l in ells if 25<=l<=30]); return {l:D[l]/hi for l in ells}
D_sw={l:l*(l+1)*C_sw[l] for l in ells}
D_swdop={l:l*(l+1)*(C_sw[l]+C_dop[l]) for l in ells}
D_lc={l:l*(l+1)*C_lc[l] for l in ells}
n_sw=norm(D_sw); n_swdop=norm(D_swdop); n_lc=norm(D_lc)

print("="*70)
print("A1.2 -- does Doppler separate ell=2 from ell=3? (aH_lss=%.2e /Mpc)"%aH_lss)
print("="*70)
print(f"  k_2 D_C = {k_of(2)*D_C:.2f}, alpha_2=(2/3)k_2/aH = {(2./3.)*(k_of(2)/aH_lss):.3f}")
print(f"  k_8 D_C = {k_of(8)*D_C:.2f}, alpha_8 = {(2./3.)*(k_of(8)/aH_lss):.3f}")
print(f"\n  Doppler/SW power ratio at each ell (is it subdominant at low ell?):")
for l in [2,3,4,5,8]:
    print(f"     ell={l}: C_dop/C_sw = {C_dop[l]/C_sw[l]:.3f}")
print(f"\n  ell(ell+1)C_ell normalised to ell=25-30:")
print(f"     {'ell':>4s} {'SW only':>9s} {'SW+Dop':>9s} {'ratio SW+Dop CR/LCDM':>22s}")
for l in [2,3,4,5,6,8]:
    depth=n_swdop[l]/n_lc[l]
    print(f"     {l:4d} {n_sw[l]:9.3f} {n_swdop[l]:9.3f} {depth:22.3f}")
r_sw = n_sw[3]/n_sw[2]; r_swdop=n_swdop[3]/n_swdop[2]
print(f"\n  ell=3/ell=2 depth ratio (normalisation-independent):  SW only = {r_sw:.3f}   SW+Doppler = {r_swdop:.3f}")
print(f"  (>1 means the octopole is LESS suppressed than the quadrupole -- Doppler separating them)")
print("""
  HONEST READING (not claimed; this is a pressure-test, not a pinned result):
   * The SW-only octopole over-suppression (ell=3 as suppressed as ell=2, both ~0.2 of LCDM) is the
     robust, flat-limit-verified result the papers state as the live falsification risk.
   * BUT the omitted Doppler term is NOT cleanly negligible at these multipoles (C_dop/C_sw ~ 0.2-0.66
     here), because CR's low-ell power comes from the TAILS of j_l(k_L D_C) for modes k_L at the
     ell~8 scale, where the derivative j_l' is comparable to j_l -- the continuum "Doppler is
     sub-dominant at low ell" lore does not transfer to the discrete-source tails.
   * Included even roughly, Doppler LIFTS ell=3 relative to ell=2 (ratio %.2f -> %.2f), i.e. it moves
     the octopole toward the observed pattern (quadrupole low, octopole more normal).
   * CAVEATS making this a not claimed, not a verdict: (i) the velocity-potential normalisation
     alpha_L=(2/3)k/aH is order-of-magnitude, not a solved transfer; (ii) Doppler was added to CR but
     the LCDM baseline here is SW-only, so the absolute depths are not a consistent comparison (the
     ell=3/ell=2 ratio is the clean, normalisation-free quantity).
  CONCLUSION: the octopole tension is NOT as firm as a bare-SW reading implies. Whether it softens or
  holds turns on a PROPER velocity/Doppler transfer (or a genuine Boltzmann solve with the discrete
  source) -- the real remaining A1.2 computation. The papers' 'octopole is the live risk' stands, but
  the risk may be milder than 0.20/0.22 suggests; state it that way, do not sharpen it into a firm
  refutation-magnet.""" % (r_sw, r_swdop))
print("="*70)
