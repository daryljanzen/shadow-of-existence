# *** SUPERSEDED for the DEPTH (r962) by verify_lowell_boltzmann.py. ***
# The SW+ISW-analytic depth here (l2=0.22,l3=0.20) OVER-DEEPENED the deficit: it treated the late
# ISW as lost by the discrete source ('no low-k modes to boost'), but the late ISW at l=2 is sourced
# ABOVE the floor k_2 and IS retained. The genuine CAMB transfer gives l2=0.47,l3=0.41 (mild, non-
# discriminating). What STANDS here: the mechanism (deficit below l~8, parameter-free, l=2,3 together).
"""
CR low-ell DEPTH at full radiative order (the "Boltzmann" grind) -- SW + early-ISW + late-ISW.
Refines verify_isw_lowell.py (SW + late-ISW only). The depth DEEPENS at full order, and the
continuum reproduces the known LCDM low-ell rise (the validating check).

CONSTRUCTION read at source (not modelled): P7 sec:floor (l.135) -- in CR's uniform-expansion
picture the gravitational redshift telescopes to the STANDARD SW + ISW (CR's own differential floor
is zero). flat-LCDM is itself flat, so the projection is shared. Therefore CR's low-ell spectrum is
the STANDARD full-radiative transfer applied to a source that is (i) DISCRETE (k_L=sqrt(L(L+2))/r0)
and (ii) FLOORED at k_2 -- every transfer ingredient (SW, early+late ISW, Doppler, T(k)) common to
CR and flat-LCDM. The deficit is therefore a pure source-spectrum effect; the depth is how the common
transfer distributes power across the discrete modes vs the continuum near the floor.

Transfer (Phi_prim factored into the scale-invariant weight w_L=(L+1)/(L(L+2))):
  T_SW(k,l)  = (1/3) Phi(z_lss) j_l(k D_C)
  T_ISW(k,l) = 2 \int dz (dPhi/dz) j_l(k d(z))      [early + late ISW together]
Super-horizon potential Phi(z) = HS(y) * g_Lambda(z), y=a/a_eq:
  HS(y) = [16 sqrt(1+y) + 9y^3 + 2y^2 - 8y - 16]/(10 y^3)   (Hu-Sugiyama, matter+radiation;
          ->1 deep in radiation, ->0.9 in matter -- the post-LSS tail is the early ISW)
  g_Lambda(z) = D(z)(1+z) normalised to 1 in matter domination (the Lambda decay -- the late ISW).
Doppler omitted: standard, subdominant at low ell (it peaks at the acoustic scale).

CONTINUUM CHECK [PASSES]: with k->0 the SW gives flat ell(ell+1)C_ell, and SW+full-ISW reproduces the
known LCDM low-ell rise (~1.48 at ell=2 over the plateau) -- transfer + ISW amplitude validated.

RESULT [E, continuum-validated], ell(ell+1)C_ell normalised to ell=25-30:
  SW only (CR):       l2=0.12 l3=0.10 l4=0.21 l5=0.66        (bare deficit)
  SW+full-ISW (CR):   l2=0.33 l3=0.27 l4=0.39 l5=0.85 l6=1.09 l8=1.14
  LCDM (continuum):   l2=1.48 l3=1.33 l4=1.25 ...            (ISW-enhanced baseline)
  DEPTH (CR/LCDM):    l2=0.22 l3=0.20 l4=0.31 l5=0.70 l6=0.93 l8=1.00

READING: the CR quadrupole/octupole sit at ~0.20-0.22 of the LCDM expectation -- a factor ~4.5-5
deficit, recovering by ell~6-8. The depth DEEPENS at full radiative order (vs the leading factor ~3):
the late ISW that partly fills CR's bare deficit is the SAME ISW that strongly RAISES the LCDM baseline
(CR has no low-k modes for it to boost), so against the ISW-enhanced expectation CR sits further below.
~0.2 of LCDM at the quadrupole is in the range of the observed large-angle deficit -- a correspondence
signal, held at weight (coherence shown is not correspondence earned; cosmic variance is large; the
data comparison is the outward test). Remaining: the Doppler term (subdominant at low ell); a full
Boltzmann solve would refine the transfer at the ~10-20% level, not the deficit's existence/location.
"""
import numpy as np
from scipy.special import spherical_jn
from scipy.integrate import quad, trapezoid

Om, OL, h, Or = 0.315, 0.685, 0.674, 9.24e-5
cH0 = 299792.458/(100*h)
def E(z): return np.sqrt(Or*(1+z)**4 + Om*(1+z)**3 + OL)
def dC(z): return cH0*quad(lambda zz: 1/E(zz), 0, z, limit=200)[0]
z_lss = 1089.0; D_C = dC(z_lss); r0 = 5064.0; z_eq = Om/Or - 1
def HS(y): return (16*np.sqrt(1+y) + 9*y**3 + 2*y**2 - 8*y - 16)/(10*y**3)
def Dg(z):
    a = 1/(1+z); I = quad(lambda ap: 1/(ap*np.sqrt(Om/ap**3+OL))**3, 1e-6, a, limit=200)[0]
    return 2.5*Om*np.sqrt(Om/a**3+OL)*I
gLhi = Dg(30.)*31.
def Phi(z): return HS((1+z_eq)/(1+z))*Dg(z)*(1+z)/gLhi
_zg = np.geomspace(1e-3, 3000, 500); _Pg = np.array([Phi(z) for z in _zg])
_dP = np.gradient(_Pg, _zg); _dd = np.array([dC(z) for z in _zg]); _Plss = Phi(z_lss)
def T_SW(k, l): return (1/3.)*_Plss*spherical_jn(l, k*D_C)
def T_ISW(k, l): return 2.*trapezoid(_dP*spherical_jn(l, k*_dd), _zg)
ells = np.array([2,3,4,5,6,7,8,10,12,15,20,25,30])
def Cl_disc(mode, Lmax=4000):
    o = np.zeros(len(ells))
    for L in range(2, Lmax+1):
        kL = np.sqrt(L*(L+2))/r0; w = (L+1)/(L*(L+2))
        sw = np.array([T_SW(kL,l) for l in ells]) if mode != 'isw' else 0.
        iz = np.array([T_ISW(kL,l) for l in ells]) if mode != 'sw' else 0.
        o += w*(sw+iz)**2
    return o
def Cl_cont(mode, Lmax=6000):
    kk = np.geomspace(0.02/r0, Lmax/r0, 1600); o = np.zeros(len(ells))
    for i, l in enumerate(ells):
        sw = np.array([T_SW(k,l) for k in kk]) if mode != 'isw' else 0.
        iz = np.array([T_ISW(k,l) for k in kk]) if mode != 'sw' else 0.
        o[i] = trapezoid((sw+iz)**2/kk, kk)
    return o
def D(C): d = ells*(ells+1)*C; return d/np.mean(d[ells>=25])
if __name__ == "__main__":
    print(f"checks: D_C={D_C:.0f} z_eq={z_eq:.0f} Phi(lss)={Phi(z_lss):.3f} "
          f"early-ISW drop={Phi(z_lss)-Phi(30):.4f} late-ISW drop={Phi(30)-Phi(0):.4f}")
    def show(t, C): print(f" {t:14s}: "+" ".join(f"l{l}={v:.2f}" for l,v in zip(ells,D(C)) if l in [2,3,4,5,6,8]))
    print("[continuum check vs LCDM]"); show("SW", Cl_cont('sw')); show("SW+ISW", Cl_cont('both'))
    print("[CR discrete]"); show("SW only", Cl_disc('sw')); show("SW+ISW", Cl_disc('both'))
    cb, contb = D(Cl_disc('both')), D(Cl_cont('both'))
    print("[depth CR/LCDM]: "+" ".join(f"l{l}={cb[i]/contb[i]:.2f}" for i,l in enumerate(ells) if l in [2,3,4,5,6,8]))
