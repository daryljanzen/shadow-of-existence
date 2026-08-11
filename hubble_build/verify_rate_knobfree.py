"""
E4 -- radiation-free rate: the KNOB-FREE-NESS test (Entry 17). Corrected presentation.
Finding: the seam datum z_onset is H0-INDEPENDENT, because the radiation-free rate makes
theta*=r_s/D_M have H0 cancel (both ~1/H0 at fixed Om). So the single datum reproduces the
observed acoustic scale at EVERY H0 -- it cannot be a knob absorbing the Hubble tension.
Contrast: LCDM's radiation term (physical omega_r, h-fixed) ties theta* to H0, pinning H0~67.
"""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
c=299792.458; zstar=1089.92; theta_obs=0.0104110
wm,wb,wr,wg = 0.1431,0.02237,4.15e-5,2.47e-5      # MEASURED physical densities (omega_i=Omega_i h^2)
def cs(z): R=3*wb/(4*wg)/(1+z); return c/np.sqrt(3*(1+R))   # baryon-loaded, depends on omega's (h-free)

# ---- CR: radiation-free rate, late-time Om fixed ----
OmCR=0.3153; OLCR=1-OmCR
def Hcr(z,H0): return H0*np.sqrt(OmCR*(1+z)**3+OLCR)
def thetaCR(zo,H0): return quad(lambda z:cs(z)/Hcr(z,H0),zstar,zo,limit=400)[0]/quad(lambda z:c/Hcr(z,H0),0,zstar,limit=200)[0]
print("CR (radiation-free rate): does the seam datum z_onset move with H0?")
print(f"{'H0':>7} {'z_onset(theta_obs)':>18} {'100theta*@fixed z_onset=6801':>30}")
zos=[]
for H0 in [67.0,69.0,71.0,73.0,73.04,74.0]:
    zo=brentq(lambda z:thetaCR(z,H0)-theta_obs, zstar+1, 5e5); zos.append(zo)
    print(f"{H0:>7.2f} {zo:>18.1f} {100*thetaCR(6801,H0):>30.5f}")
zos=np.array(zos)
zeq=wm/wr-1; rho=(1+zos.mean())/(1+zeq)
print(f"\n  z_onset spread across H0: [{zos.min():.1f},{zos.max():.1f}]  -> H0-INDEPENDENT (cancels in theta*)")
print(f"  measured z_eq = wm/wr-1 = {zeq:.0f};  rho_r/rho_m at z_onset = (1+{zos.mean():.0f})/(1+{zeq:.0f}) = {rho:.2f}  (~twice equality)")

# ---- LCDM: radiation in the rate, physical densities ----
print("\nLCDM (radiation in rate): theta* vs H0 at fixed measured omega_m,omega_b,omega_r:")
def Hstd(z,H0):
    h=H0/100; Om=wm/h**2; Or=wr/h**2; OL=1-Om-Or
    return H0*np.sqrt(Om*(1+z)**3+Or*(1+z)**4+OL)
def thetaStd(H0): return quad(lambda z:cs(z)/Hstd(z,H0),zstar,1e6,limit=500)[0]/quad(lambda z:c/Hstd(z,H0),0,zstar,limit=200)[0]
for H0 in [67.0,70.0,73.0]:
    print(f"   H0={H0:.1f}: 100theta*={100*thetaStd(H0):.5f}")
H0_lcdm=brentq(lambda H:thetaStd(H)-theta_obs,60,75)
print(f"   -> LCDM reproduces theta_obs only at H0={H0_lcdm:.2f}  (theta* DEPENDS on H0 -> pins it; the tension)")
print(f"\nVERDICT: CR's seam datum is H0-independent (same z_onst~6801 at H0=67 and 73) and O(1)~2 (twice")
print(f"  equality) -- a MEASURED datum like eta, not a knob. The radiation-free rate decouples theta*")
print(f"  from H0, so the acoustic scale is met at the DIRECTLY-measured H0 with no second H0 to reconcile.")
