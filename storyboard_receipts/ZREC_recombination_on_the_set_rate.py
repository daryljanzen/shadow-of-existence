"""ZREC — THE RECOMBINATION REDSHIFT ON THE CONSTRUCTION'S OWN RATE.
The last inherited number in the chain.  z_rec = 1089.9 came from CAMB, whose ionisation evolution
runs on LambdaCDM's expansion.  Recompute it here, same shape as everything else in A.0: the atomic
physics outside the integral, the rate inside.
DEFINITION USED: last scattering is where the optical depth reaches unity,
     tau(z) = INT_0^z n_e sigma_T c dz'/((1+z') H(z'))  =  1.
The IONISATION FRACTION x_e(z) from Saha is pure atomic physics and is the SAME for both cosmologies;
*** THE WHOLE COSMOLOGY-DEPENDENCE IS THE 1/H IN THE MEASURE. ***"""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
# constants (SI-ish, but only ratios matter for the comparison)
sigT=6.6524587e-29          # m^2
mp=1.67262192e-27; me=9.1093837e-31; kB=1.380649e-23; hbar=1.054571817e-34; cc=2.99792458e8
T0=2.7255; B=13.605693*1.602176634e-19
G=6.67430e-11; Mpc=3.0856775814913673e22
def n_b0(ombh2):   # baryons per m^3 today
    rho_c = 3*(100e3/Mpc)**2/(8*np.pi*G)     # h^-2 kg/m^3
    return ombh2*rho_c/mp
def saha_xe(z, ombh2):
    T=T0*(1+z); nb=n_b0(ombh2)*(1+z)**3
    rhs=(me*kB*T/(2*np.pi*hbar**2))**1.5*np.exp(-B/(kB*T))/nb
    # x^2/(1-x) = rhs
    return (-rhs+np.sqrt(rhs**2+4*rhs))/2
print("="*80); print("ZREC — LAST SCATTERING ON THE SET RATE"); print("="*80)
ombh2=0.0224
print(f"\n  Saha check (pure atomic, cosmology-free):")
for z in [1400,1200,1100,1000,900]:
    print(f"     z={z:5d}:  x_e = {saha_xe(z,ombh2):.4f}")
def H_of(z, kind, H0, Om):
    if kind=='CR': return H0*1e3/Mpc*np.sqrt(Om*(1+z)**3+1-Om)
    Or=Om/(1+3403.6)
    return H0*1e3/Mpc*np.sqrt(Or*(1+z)**4+Om*(1+z)**3+1-Om)
def tau_of(z, kind, H0, Om):
    f=lambda zp: saha_xe(zp,ombh2)*n_b0(ombh2)*(1+zp)**3*sigT*cc/((1+zp)*H_of(zp,kind,H0,Om))
    v,_=quad(f, 0, z, limit=300); return v
print(f"\n  {'cosmology':28s} {'H0':>6s} {'Om':>7s} {'z(tau=1)':>10s}")
out={}
for lab,kind,H0,Om in [("LambdaCDM (rad-included)","L",67.4,0.307),
                       ("CR (radiation-free)","CR",73.0,0.3066),
                       ("CR at H0=67.4 (control)","CR",67.4,0.3066)]:
    z=brentq(lambda zz: tau_of(zz,kind,H0,Om)-1.0, 700., 2000.)
    out[lab]=z
    print(f"  {lab:28s} {H0:>6.1f} {Om:>7.4f} {z:>10.1f}")
print(f"""
  *** AND THE COMPARISON THAT MATTERS: ***
     LambdaCDM here      : z = {out['LambdaCDM (rad-included)']:.1f}   (CAMB's full treatment gives 1089.9)
     CR                  : z = {out['CR (radiation-free)']:.1f}
     shift               : {out['CR (radiation-free)']-out['LambdaCDM (rad-included)']:+.1f}  ({100*(out['CR (radiation-free)']/out['LambdaCDM (rad-included)']-1):+.2f}%)
  The Saha-only treatment sits high of CAMB's 1089.9 -- Peebles' departure from equilibrium delays
  recombination and CAMB includes it -- but *** THE SHIFT BETWEEN THE TWO COSMOLOGIES IS THE THING
  BEING COMPUTED, AND IT IS COMMON-MODE IN THAT APPROXIMATION. ***
""")
