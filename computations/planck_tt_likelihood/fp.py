"""FP — THE PREDICTION FROM THE CONSTRUCTION'S OWN PARAMETERS.  No inherited ΛCDM values.
INPUTS, each measured or fit by the construction itself:
  H0 = 73.0        the DIRECTLY MEASURED rate (the corpus: 'the geometry read at the present epoch')
  Om = 0.31        the corpus's OWN BAO fit, DESI DR2, chi^2/dof ~ 1 at the measured H0
  T_CMB           measured, fixing omega_r = 4.15e-5
  omega_b = 0.0224 from the corpus's OWN BBN network (P16), not from a CMB fit
  l_* = 301.6      the measured acoustic angle -- the one CMB observable used, and it FIXES z_onset
NOTHING ELSE IS TAKEN FROM ΛCDM.  rho_r/rho_m at the seam is then an OUTPUT, not a target."""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
c=299792.458
H0=73.0; Om=0.31; OL=1-Om; ombh2=0.0224; omr=4.15e-5
omm=Om*(H0/100)**2
z_rec=1089.9; a_rec=1/(1+z_rec)
R_rec=31500*ombh2/(2.7255/2.7)**4/(1+z_rec)
Rf=lambda a: R_rec*(a/a_rec)
H=lambda a: H0*np.sqrt(Om/a**3+OL)
print("="*80); print("FP — THE PREDICTION, FROM THE CONSTRUCTION'S OWN NUMBERS"); print("="*80)
print(f"\n  inputs:  H0={H0}  Om={Om} (own BAO fit)  omega_m={omm:.4f}  omega_b={ombh2} (own BBN)")
print(f"           omega_r={omr:.3e} (measured T_CMB)   R_rec={R_rec:.4f}")
def rs(zs):
    v,_=quad(lambda a: c/(a**2*H(a)*np.sqrt(3*(1+Rf(a)))), 1/(1+zs), a_rec, limit=300); return v
DM,_=quad(lambda a: c/(a**2*H(a)), a_rec, 1.0, limit=300)
zs=brentq(lambda z: np.pi*DM/rs(z)-301.6, 1500., 60000.)
print(f"\n  the measured acoustic angle fixes the seam:  z_onset = {zs:.0f}")
print(f"     r_s = {rs(zs):.2f} Mpc,  D_M = {DM:.0f} Mpc,  l_* = {np.pi*DM/rs(zs):.1f}")
print(f"\n  AND THE SEAM RADIATION AMPLITUDE IS THEN AN OUTPUT:")
print(f"     rho_r/rho_m at the seam = omega_r(1+z)/omega_m = {omr*(1+zs)/omm:.3f}")
print(f"     (the corpus says 'approximately 2'; the construction's own numbers give {omr*(1+zs)/omm:.2f})")
def g(a):
    R=Rf(a); return (R**2/(1+R)+8/9)/(6*(1+R))
I,_=quad(lambda a: g(a)/H(a), 1/(1+zs), a_rec, limit=300)
# the LambdaCDM comparison object, at ITS OWN best-fit -- not at CR's parameters
def lcdm():
    Oml=0.307; H0l=67.4; OLl=1-Oml; z_eq=3403.6; Orl=Oml/(1+z_eq)
    Hl=lambda a: H0l*np.sqrt(Orl/a**4+Oml/a**3+OLl)
    s,_=quad(lambda a: c/(a**2*Hl(a)*np.sqrt(3*(1+Rf(a)))), 1e-9, a_rec, limit=300)
    Il,_=quad(lambda a: g(a)/Hl(a), 1e-9, a_rec, limit=300)
    D,_=quad(lambda a: c/(a**2*Hl(a)), a_rec, 1.0, limit=300)
    return s, np.sqrt(Il), D
rsL, rDL, DML = lcdm()
rD = np.sqrt(I)
print(f"\n  {'':22s} {'CR (own params)':>18s} {'LCDM (own best fit)':>22s}")
print(f"  {'r_s (Mpc)':22s} {rs(zs):>18.2f} {rsL:>22.2f}")
print(f"  {'D_M (Mpc)':22s} {DM:>18.0f} {DML:>22.0f}")
print(f"  {'l_*':22s} {np.pi*DM/rs(zs):>18.1f} {np.pi*DML/rsL:>22.1f}")
r=(rD/rs(zs))/(rDL/rsL)
print(f"\n  *** theta_D/theta_* :  CR/LCDM = {r:.4f}   ->  {100*(r-1):+.2f}% ***")
print(f"  and l_D scales inversely: if LCDM's is 1362, CR's is {1362/r:.0f}")
print("""
  *** THIS IS THE PREDICTION FROM THE CONSTRUCTION'S OWN INPUTS.  Nothing here is tuned to ΛCDM:
      H0 is the local measurement, Om is the corpus's BAO fit, omega_b is the corpus's BBN, T_CMB is
      measured, and the ONE CMB number used is the acoustic angle -- which is spent fixing the seam. ***
""")

print("="*80); print("AND WHAT THE CMB INFERENCE RETURNS IF THIS IS THE TRUTH"); print("="*80)
rsC=rs(zs)
print(f"""
  Planck infers H0 from the measured theta_* by assuming LambdaCDM's sound horizon.  If the truth is
  the construction's, that assumption is wrong by the ratio of the two sound horizons:
     H0_inferred = H0_true x (r_s^CR / r_s^LCDM) = {H0:.1f} x ({rsC:.2f}/{rsL:.2f}) = {H0*rsC/rsL:.2f}
  *** AND PLANCK REPORTS 67.4. ***
""")
print("""  ⚠ AND THE HONEST READING OF THAT, WHICH IS NOT 'WE DERIVED 67.4'.
  I solved z_onset by IMPOSING l_* = 301.6 at H0 = 73.  Once that is imposed, D_M/r_s is matched by
  construction, and since D_M ~ 1/H0 the relation H0_inf = H0_true (r_s^CR/r_s^L) follows
  automatically.  *** SO THE 67.4 IS NOT AN INDEPENDENT PREDICTION; IT IS THE RESTATEMENT OF THE
  IMPOSED MATCH. ***  What IS non-trivial is the SEAM REDSHIFT that match demands:
""")
print(f"     z_onset required = {zs:.0f}")
print(f"     the corpus states, independently, ~6797   ->  agreement to {100*abs(zs-6797)/6797:.1f}%")
print("""
  *** THAT is the real content: the construction, run at its own H0 and its own BAO-fit Omega_m,
      needs its seam at a redshift within one per cent of the one the corpus states on other
      grounds.  The Hubble 'prediction' is a consistency, and the seam redshift is the check. ***
""")
print(f"""AND THE ONE THING HERE THAT IS NOT IMPOSED AT ALL:
     theta_D/theta_* = {100*(r-1):+.2f}%  and  l_D = {1362/r:.0f} against LambdaCDM's 1362.
  Nothing was tuned to produce it.  The acoustic angle was spent on the seam; the damping followed.
  *** IT IS THE SECTOR'S ONE FREE-STANDING PREDICTION. ***
""")
