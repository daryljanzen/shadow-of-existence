"""PK3 — THE PEAK HEIGHTS, INTEGRATED.  On the ground of A.0: one integral over the set rate.
NOTHING SPLICED, NOTHING GUESSED.  The chain, each link derived:

L1 EQUATION.  Theta_0'' + (Rb'/(1+Rb))Theta_0' + k^2 c_s^2 Theta_0 = -(k^2/3)Psi - Psi'' - (Rb'/(1+Rb))Psi'
  and C11 gives Psi' = Psi'' = 0 on L1 (matter-dominated, growing mode constant).  So the drive is
  CONSTANT and the particular solution is exact:
       Theta_0^part = -(k^2/3)Psi / (k^2 c_s^2) = -(1+Rb) Psi     [since c_s^2 = 1/(3(1+Rb))]
  *** SO Theta_0 + Psi = -Rb Psi + (homogeneous).  THE DISPLACED ZERO POINT IS DERIVED, NOT ASSUMED. ***
HOMOGENEOUS.  WKB for slowly varying Rb: (1+Rb)^{-1/4} {cos, sin}(k r_s), r_s = INT c_s d eta from the seam.
MATCHING.  At the seam, Theta_0+Psi and its derivative are whatever the leg left -- C4 gives both in
  closed form, because on the leg Theta_hat oscillates FREELY from entry at k eta = 1.
"""
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
def rs_of(zs):
    v,_=quad(lambda a: c/(a**2*H(a)*np.sqrt(3*(1+Rbf(a)))), 1/(1+zs), a_rec, limit=300); return v
DM,_=quad(lambda a: c/(a**2*H(a)), a_rec, 1.0, limit=300)
zs=brentq(lambda z: np.pi*DM/rs_of(z)-301.6, 1500., 60000.)
a_s=1/(1+zs); RS=rs_of(zs); Rb_s=Rbf(a_s)
print("="*80); print("PK3 — INTEGRATED, NOT SPLICED"); print("="*80)
print(f"\n  z_onset={zs:.0f}  r_s(seam->rec)={RS:.2f} Mpc  D_M={DM:.0f}  R_seam={Rb_s:.4f}  Rb_rec={Rb_rec:.4f}")
# the comoving wavenumber entering the horizon AT the seam
k_s = a_s*H(a_s)/c
print(f"  k_seam = a_s H(a_s)/c = {k_s:.6f} /Mpc   ->  l_seam = k_s D_M = {k_s*DM:.0f}")
# --- the leg (C1/C4): Psi elementary; Theta_hat free from entry at k eta = 1 ---
def Psi_leg(x): 
    x=np.asarray(x,float); return np.where(x<1e-6,1.0,3*(np.sin(x)-x*np.cos(x))/np.maximum(x,1e-12)**3)
x_e=1/np.sqrt(3)                       # C4: entry phase, same for every mode
def leg_state(k):
    """Theta_hat and its eta-derivative at the seam, and Psi at the seam, per unit Psi_i."""
    x_s = (k/k_s)/np.sqrt(3)           # phase at the seam: k eta_s/sqrt3 with k eta_s = k/k_s
    A_leg = Psi_leg(x_e)/2             # C4: Theta_hat(entry) = Psi(entry)/2
    dphi  = x_s - x_e                  # phase advanced since entry
    That  = A_leg*np.cos(dphi)
    dThat = -A_leg*np.sin(dphi)*(k/np.sqrt(3))     # d/d eta
    return That, dThat, Psi_leg(x_s)
ell=np.arange(2,2600); k=ell/DM
That_s, dThat_s, Psi_s = leg_state(k)
Psi_s = -Psi_s                          # potential well, sign convention
# --- match onto L1 ---
# Theta_0+Psi = -Rb Psi_s + (1+Rb)^{-1/4}[A cos(k r) + B sin(k r)],  r measured from the seam
A = (That_s + Rb_s*Psi_s)*(1+Rb_s)**0.25
# derivative at r=0:  d/d eta = c_s d/dr ; c_s(seam) = c/sqrt(3(1+Rb_s))
cs_s = 1/np.sqrt(3*(1+Rb_s))
B = (dThat_s/(k*cs_s))*(1+Rb_s)**0.25
# --- evaluate at recombination ---
phase = k*RS
osc = -Rb_rec*Psi_s + (1+Rb_rec)**-0.25*(A*np.cos(phase)+B*np.sin(phase))
# damping, from C8+PR in quadrature (absolute, anchored as in TOT)
def g(a):
    Rb=Rbf(a); return (Rb**2/(1+Rb)+8/9)/(6*(1+Rb))
I,_=quad(lambda a: g(a)/H(a), a_s, a_rec, limit=300)
Oml=0.307; H0l=67.4; Orl=Oml/(1+3403.6); Hl=lambda a: H0l*np.sqrt(Orl/a**4+Oml/a**3+1-Oml)
Il,_=quad(lambda a: g(a)/Hl(a), 1e-9, a_rec, limit=300)
Dl,_=quad(lambda a: c/(a**2*Hl(a)), a_rec, 1.0, limit=300)
K=(Dl/1362.0)**2/Il; rD=np.sqrt(K*I)
sg,_=quad(lambda z: c/H(1/(1+z)), z_rec-40, z_rec+40, limit=200); sg/=2.355
tot=np.sqrt(rD**2+sg**2)
D_l = (osc*np.exp(-(k*tot)**2))**2 * ell**(0.965-1)
idx=[i for i in argrelextrema(D_l,np.greater,order=8)[0] if ell[i]>120]
print(f"\n  r_D={rD:.2f}  sigma={sg:.2f}  quadrature={tot:.2f} Mpc")
print(f"\n  {'n':>3s} {'l (PK3)':>9s} {'l (measured)':>13s}   {'height':>12s}")
meas=[220,536,813,1126,1399]
for n,i in enumerate(idx[:5]):
    m=str(meas[n]) if n<len(meas) else '-'
    print(f"  {n+1:>3d} {ell[i]:>9d} {m:>13s}   {D_l[i]:>12.4e}")
if len(idx)>=3:
    h=[D_l[i] for i in idx[:3]]
    print(f"\n  P1/P2 = {h[0]/h[1]:.3f}   (measured {5741/2595:.3f})")
    print(f"  P1/P3 = {h[0]/h[2]:.3f}   (measured {5741/2544:.3f})")
