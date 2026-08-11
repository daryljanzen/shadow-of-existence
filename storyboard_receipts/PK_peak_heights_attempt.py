"""PK — THE PEAK HEIGHTS FROM THE CONSTRUCTION'S OWN PHYSICS.
No Boltzmann code.  Inputs, each derived or measured here:
  * the entry amplitude, C4: every mode leaves the collapse leg with Psi(1/sqrt3)/2 = 0.4835 Psi_i,
    k-INDEPENDENT -- so the envelope is flat and the peak PATTERN comes from the oscillator alone;
  * Rb at recombination, from the corpus's own BBN omega_b and the measured T_CMB;
  * r_s and D_M, FP, at the construction's own H0 and its BAO-fit Omega_m;
  * the damping, C8 + PR (diffusion and thickness in quadrature).
The observable RATIOS of peak heights are independent of A_s, so nothing inherited enters them."""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
c=299792.458
H0=73.0; Om=0.3066; OL=1-Om; ombh2=0.0224
z_rec=1089.9; a_rec=1/(1+z_rec)
Rb_rec=31500*ombh2/(2.7255/2.7)**4/(1+z_rec)
Rbf=lambda a: Rb_rec*(a/a_rec)
H=lambda a: H0*np.sqrt(Om/a**3+OL)
print("="*80); print("PK — PEAK HEIGHTS, FROM FIRST PRINCIPLES"); print("="*80)
def rs(zs):
    v,_=quad(lambda a: c/(a**2*H(a)*np.sqrt(3*(1+Rbf(a)))), 1/(1+zs), a_rec, limit=300); return v
DM,_=quad(lambda a: c/(a**2*H(a)), a_rec, 1.0, limit=300)
zs=brentq(lambda z: np.pi*DM/rs(z)-301.6, 1500., 60000.)
RS=rs(zs)
print(f"\n  z_onset={zs:.0f}  r_s={RS:.2f} Mpc  D_M={DM:.0f} Mpc  Rb_rec={Rb_rec:.4f}")
# damping scales, absolute, on this rate
def g(a):
    Rb=Rbf(a); return (Rb**2/(1+Rb)+8/9)/(6*(1+Rb))
I,_=quad(lambda a: g(a)/H(a), 1/(1+zs), a_rec, limit=300)
# anchor the Thomson normalisation the same way for both: r_D^2 = K * I, K fixed by LCDM's l_D=1362
def lcdm_I():
    Oml=0.307; H0l=67.4; z_eq=3403.6; Orl=Oml/(1+z_eq); OLl=1-Oml
    Hl=lambda a: H0l*np.sqrt(Orl/a**4+Oml/a**3+OLl)
    Il,_=quad(lambda a: g(a)/Hl(a), 1e-9, a_rec, limit=300)
    Dl,_=quad(lambda a: c/(a**2*Hl(a)), a_rec, 1.0, limit=300)
    return Il, Dl
Il, DMl = lcdm_I()
rD_L = DMl/1362.0                 # LCDM's diffusion length in Mpc from its measured l_D
K = rD_L**2/Il
rD = np.sqrt(K*I)
# thickness
def comov(dz):
    v,_=quad(lambda z: c/(H(1/(1+z))), z_rec-dz/2, z_rec+dz/2, limit=200); return v
sig = comov(80.0)/2.355
tot = np.sqrt(rD**2+sig**2)
print(f"  r_D={rD:.2f} Mpc   sigma={sig:.2f} Mpc   quadrature={tot:.2f} Mpc")
print(f"  -> l_damp = D_M/total = {DM/tot:.0f}")
print("""
  THE OSCILLATOR AT LAST SCATTERING.  With baryons the zero point is displaced:
     Theta_0 + Psi = A cos(k r_s) - Rb Psi     (constant-Rb form)
  C4 fixes A: the free oscillation carries Psi(1/sqrt3)/2 per unit Psi_i, k-independent.
  Take Psi = -1 (a potential well, sign conventional) and A = 0.4835.
""")
A=0.4835; Psi=-1.0
ell=np.arange(2,2600)
k=ell/DM
osc=A*np.cos(k*RS) - Rb_rec*Psi
damp=np.exp(-(k*tot)**2)
D_l = (osc*damp)**2 * ell**(0.965-1)     # x the primordial tilt; A_s drops out of RATIOS
# find the peaks
from scipy.signal import argrelextrema
idx=argrelextrema(D_l, np.greater, order=12)[0]
pk=[(ell[i], D_l[i]) for i in idx if ell[i]>120][:6]
print(f"  {'peak':>6s} {'l (CR)':>9s} {'l (measured)':>14s}   {'height (arb)':>14s}")
meas=[220,536,813,1126,1399,1750]
for n,(l,v) in enumerate(pk):
    m = meas[n] if n<len(meas) else None
    print(f"  {n+1:>6d} {l:>9d} {str(m):>14s}   {v:>14.4e}")
if len(pk)>=3:
    print(f"\n  RATIOS (A_s-independent):")
    print(f"     P1/P2 = {pk[0][1]/pk[1][1]:.3f}     measured ~ {5741/2595:.3f}")
    print(f"     P1/P3 = {pk[0][1]/pk[2][1]:.3f}     measured ~ {5741/2544:.3f}")
    print(f"     P2/P3 = {pk[1][1]/pk[2][1]:.3f}     measured ~ {2595/2544:.3f}")
