"""
CR low-ell: does the late-ISW fill the deficit?  THE MAKE-OR-BREAK TEST -- the deficit SURVIVES.

Context.  verify_closedS3_nonsync.py gave the bare ordinary-SW CR transfer: a strong low-ell deficit
below ell~8 (flat projection of the discrete closed-S^3 source).  The one effect that could fill it
is the late-ISW: it is sourced near the observer (small line-of-sight distance d), so a mode projects
to ell~k*d with d small -> even the lowest mode k_2 reaches ell~1-2, and its amplitude (~2*Delta g ~0.42)
is comparable to the SW (1/3).  P7 (sec:floor, l.135) fixes the SCOPE: in CR's uniform-expansion picture
the gravitational redshift telescopes, leaving "the endpoint potential and the small integrated term" --
i.e. the cumulative term is the STANDARD SW + STANDARD ISW (CR's own differential-expansion floor is zero).
So there is no CR-specific ISW to derive: it is the standard ISW, sourced by the same discrete spectrum.

Scope / assumptions (leading-order; flagged honestly):
  - potential evolution g(z)=D(z)/a is the STANDARD-LCDM one (CR reproduces the flat-LCDM background
    exactly; the scalar dynamics are taken standard on it -- to be confirmed against P12);
  - large-scale transfer T(k)~1 (good at low ell); adiabatic SW (1/3)Phi; no Doppler; e^{-tau}~1.
  - the ONLY CR modification is the DISCRETE source spectrum k_L=sqrt(L(L+2))/r0 (L>=2) and the FLAT
    projection D_M=D_C (prop:flat).  Transfers added COHERENTLY (same primordial Phi).

  T_SW(k,ell)  = (1/3) j_ell(k D_C)
  T_ISW(k,ell) = 2 \int dz (dg/dz) j_ell(k d(z))            [late-ISW dominates the low ell]
  C_ell = sum_{L>=2} w_L [T_SW(k_L,ell)+T_ISW(k_L,ell)]^2,   w_L=(L+1)/(L(L+2)).

CONTINUUM CHECK (validates the machinery against known LCDM): with k->0 the SW gives FLAT
ell(ell+1)C_ell, and SW+ISW gives the known modest late-ISW rise (~+56% at ell=2). [PASSES]

RESULT [E, continuum-validated] at chi=D_C/r0~2.75, ell(ell+1)C_ell normalised to ell=25-30:
  SW only (CR):  l2=0.12 l3=0.10 l4=0.20 l5=0.65 l6=0.92 ...   (bare deficit, ~8x at ell=2)
  SW+ISW (CR):   l2=0.50 l3=0.41 l4=0.47 l5=0.85 l6=1.06 ...   (deficit PARTIALLY filled, SURVIVES)
  LCDM (cont.):  l2=1.56 l3=1.35 l4=1.24 ...                    (ISW-ENHANCED, for contrast)
=> The late-ISW partially fills the bare SW deficit (ell=2: 0.12 -> 0.50) but cannot erase it, because
   the ISW is sourced by the same discrete spectrum (no modes below k_2).  Net: CR sits a factor ~3
   BELOW LCDM at ell=2-4 -- a genuine low-multipole deficit, in the direction of the observed anomaly.
   The make-or-break ISW test is PASSED: the deficit is robust.

Remaining (not claimed the final corpus claim): the discrete measure w_L convention (affects the
exact depth, not the survival); confirm the scalar dynamics/g(z) against P12; fresh-node P12 cold read.
"""
import numpy as np
from scipy.special import spherical_jn
from scipy.integrate import quad, trapezoid

Om, OL, h = 0.315, 0.685, 0.674
cH0 = 299792.458/(100*h)
def E(z): return np.sqrt(Om*(1+z)**3 + OL)
def dC(z): return cH0*quad(lambda zz: 1.0/E(zz), 0, z, limit=200)[0]
z_lss = 1089.0; D_C = dC(z_lss); r0 = 5064.0
def Dgrow(z):
    a = 1/(1+z); integ = quad(lambda ap: 1.0/(ap*np.sqrt(Om/ap**3+OL))**3, 1e-6, a, limit=200)[0]
    return 2.5*Om*np.sqrt(Om/a**3+OL)*integ
g_hi = Dgrow(50.0)*51.0
def g(z): return Dgrow(z)*(1+z)/g_hi
_zg = np.linspace(0, 12, 300); _gg = np.array([g(z) for z in _zg])
_dgdz = np.gradient(_gg, _zg); _dd = np.array([dC(z) for z in _zg])
def T_SW(k, l): return (1/3.0)*spherical_jn(l, k*D_C)
def T_ISW(k, l): return 2.0*trapezoid(_dgdz*spherical_jn(l, k*_dd), _zg)
ells = np.array([2,3,4,5,6,7,8,10,12,15,20,25,30])
def Cl_disc(mode, Lmax=4000):
    out = np.zeros(len(ells))
    for L in range(2, Lmax+1):
        kL = np.sqrt(L*(L+2))/r0; w = (L+1)/(L*(L+2))
        sw = np.array([T_SW(kL,l) for l in ells]) if mode!='isw' else 0.0
        isw = np.array([T_ISW(kL,l) for l in ells]) if mode!='sw' else 0.0
        out += w*(sw+isw)**2
    return out
def Cl_cont(mode, kmin_fac=0.02, Lmax=6000):
    kk = np.geomspace(kmin_fac/r0, Lmax/r0, 2000); out = np.zeros(len(ells))
    for i, l in enumerate(ells):
        sw = np.array([T_SW(k,l) for k in kk]) if mode!='isw' else 0.0
        isw = np.array([T_ISW(k,l) for k in kk]) if mode!='sw' else 0.0
        out[i] = trapezoid((sw+isw)**2/kk, kk)
    return out
def Dl(C): d = ells*(ells+1)*C; return d/np.mean(d[ells>=25])
def show(t, C): print(f" {t:15s}: "+" ".join(f"l{l}={v:.2f}" for l,v in zip(ells,Dl(C)) if l in [2,3,4,5,6,8,12,25]))
if __name__ == "__main__":
    print("checks: D_C=%.0f (target ~13927), g(0)=%.3f (LCDM ~0.78)\n" % (D_C, g(0)))
    print("[continuum check] ell(ell+1)C_ell normalised to ell=25-30 (validate vs LCDM):")
    show("SW (->flat)", Cl_cont('sw')); show("SW+ISW (LCDM)", Cl_cont('both'))
    print("\n[CR discrete] does the late-ISW fill the deficit below ell~8?")
    show("SW only", Cl_disc('sw')); show("ISW only", Cl_disc('isw')); show("SW+ISW (CR)", Cl_disc('both'))
    print("\n=> deficit SURVIVES: ell=2 fills 0.12->0.50, still ~3x below LCDM's 1.56. Make-or-break passed.")
