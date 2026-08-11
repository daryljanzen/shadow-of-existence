"""PK2 — THE PEAK HEIGHTS, WITH THE PIECE PK MISSED.
The fault in PK was treating Psi at recombination as a single number.  C11 supplies the correction:
*** ON L1 THE BACKGROUND IS MATTER-DOMINATED, SO Psi IS CONSTANT FROM THE SEAM TO RECOMBINATION. ***
So Psi at last scattering is whatever the collapse leg LEFT -- and C1/C4 give that in closed form,
and it is k-DEPENDENT: Psi(k) = Psi_i . 3(sin x - x cos x)/x^3 evaluated at the seam.
High-k modes arrive with Psi ~ 0; low-k modes arrive with Psi ~ Psi_i.  The baryon zero point is
-Rb Psi(k), so THE ODD/EVEN ASYMMETRY IS STRONG AT LOW ell AND WASHES OUT AT HIGH ell -- which is what
the sky shows and what PK's constant-Psi model could not produce."""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.signal import argrelextrema
c=299792.458
H0=73.0; Om=0.3066; OL=1-Om; ombh2=0.0224
z_rec=1089.9; a_rec=1/(1+z_rec)
Rb_rec=31500*ombh2/(2.7255/2.7)**4/(1+z_rec)
Rbf=lambda a: Rb_rec*(a/a_rec)
H=lambda a: H0*np.sqrt(Om/a**3+OL)
def rs(zs):
    v,_=quad(lambda a: c/(a**2*H(a)*np.sqrt(3*(1+Rbf(a)))), 1/(1+zs), a_rec, limit=300); return v
DM,_=quad(lambda a: c/(a**2*H(a)), a_rec, 1.0, limit=300)
zs=brentq(lambda z: np.pi*DM/rs(z)-301.6, 1500., 60000.); RS=rs(zs)
print("="*80); print("PK2 — PEAK HEIGHTS WITH Psi(k) FROM THE COLLAPSE LEG"); print("="*80)
print(f"\n  z_onset={zs:.0f}  r_s={RS:.2f}  D_M={DM:.0f}  Rb_rec={Rb_rec:.4f}")
# conformal time at the seam on the radiation leg (C3's elementary map): eta_onset = 1/k at entry, but
# what we need is the phase x_s = k eta_s/sqrt3 with eta_s the conformal time ELAPSED on the leg.
# C2/C3: entry is at x=1/sqrt3 for every mode; the leg then runs to the seam.  The elapsed phase to
# the seam is x_s = k eta_onset/sqrt3, and eta_onset = r_seam/sqrt(A) in C3's units.  In observable
# terms the same statement is: x_s = k . (the comoving sound horizon accumulated ON THE LEG) . sqrt3
# Take the leg's contribution as the corpus's own: the modes are sub-horizon at the seam, entry at
# k eta = 1, so x_s/x_entry = eta_onset/eta_entry = k eta_onset.  Parametrise by the ONE number that
# fixes it: the comoving horizon at the seam, DM/l_seam with l_seam the multipole entering there.
eta_s_over = 1.0   # k eta_entry = 1 by C4
def Psi_at_seam(k, k_s):
    x = (k/k_s)/np.sqrt(3)          # phase accumulated on the leg, in units of the seam's own k
    return np.where(x<1e-8, 1.0, 3*(np.sin(x)-x*np.cos(x))/np.maximum(x,1e-12)**3)
# k_s = the wavenumber entering the horizon AT the seam
k_s = 1/ (RS/ (np.pi))   # crude: set by r_s; refine below by matching the first peak's l
ell=np.arange(2,2600); k=ell/DM
print("\n  scan the one free scale (the seam's horizon wavenumber) and read the first-peak position:")
for ks in [0.002,0.004,0.006,0.010,0.020]:
    Ps=Psi_at_seam(k, ks); Psi=-Ps
    A=(-0.5*Psi + (1+Rb_rec)*Psi)*(1+Rb_rec)**-0.25
    osc=A*np.cos(k*RS) - Rb_rec*Psi
    D=(osc*np.exp(-(k*12.9)**2))**2*ell**(0.965-1)
    idx=[i for i in argrelextrema(D,np.greater,order=10)[0] if ell[i]>120]
    pk=[ell[i] for i in idx[:3]]
    hi=[D[i] for i in idx[:3]]
    r12 = hi[0]/hi[1] if len(hi)>1 else np.nan
    print(f"   k_s={ks:.4f}:  peaks {pk}   P1/P2 = {r12:.2f}")
print(f"\n  measured: peaks 220, 536, 813 ; P1/P2 = {5741/2595:.2f}")
