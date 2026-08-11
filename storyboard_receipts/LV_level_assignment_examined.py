"""LV — EXAMINING THE LEVEL ASSIGNMENT.  Not the number: the argument.
The commitment: 'recombination is observable cosmology FROM THE SEAM OUTWARD', so r_s and r_D are
both L1 and both run from the seam.  THREE PLACES IT COULD BEND, each checked."""
import numpy as np
from scipy.integrate import quad
print("="*80); print("LV — THE LEVEL ASSIGNMENT, EXAMINED"); print("="*80)
print("""
PLACE 1 — SHOULD r_s AND r_D SHARE A LOWER LIMIT AT ALL?
  r_s is set by the PHASE: it is how far sound travelled since the mode's phase was fixed.  P15 says
  the null boundary sets one phase per mode, so r_s counting FROM THE SEAM is exactly right, and C9's
  result -- r_s = 146.8 Mpc, and the seam redshift that matches the acoustic scale being the one the
  corpus uses -- is the check that it is right.
  *** BUT r_D IS NOT A PHASE QUANTITY.  It is CUMULATIVE DAMAGE. ***
  Photons random-walk out of overdensities and the damping is the integrated mean-square displacement.
  A PHASE RESET AT THE SEAM DOES NOT UNDO DIFFUSION THAT ALREADY HAPPENED.
  So the two do NOT obviously share a lower limit, and the corpus's rule -- 'r_s AND r_D are both
  L1' -- puts them on the same LEVEL, which is a different claim from the same LIMIT.
""")
print("  CONSEQUENCE, computed: if diffusion accumulates across the seam too, r_D grows further.")
c=299792.458; H0=67.4; Om=0.307; OL=0.693
z_rec=1089.9; a_rec=1/(1+z_rec); z_eq=3403.6; Or=Om/(1+z_eq)
Rb_rec=0.6230
def Rb_of(a): return Rb_rec*(a/a_rec)
def g(a):
    Rb=Rb_of(a); return (Rb**2/(1+Rb)+8/9)/(6*(1+Rb))
def H(a,rad): return H0*np.sqrt(Or/a**4*rad+Om/a**3+OL)
a_s=1/(1+6797.0)
IL,_=quad(lambda a:g(a)/H(a,1.0),1e-9,a_rec,limit=200)                 # LCDM, all the way
IC_seam,_=quad(lambda a:g(a)/H(a,0.0),a_s,a_rec,limit=200)             # CR, from the seam, L1
IC_pre,_=quad(lambda a:g(a)/H(a,1.0),1e-9,a_s,limit=200)               # collapse leg, L2 (rad gravitates)
print(f"    r_D^2 pieces (arbitrary common units):")
print(f"      LCDM total                       {IL:.6e}")
print(f"      CR, seam->rec on L1              {IC_seam:.6e}")
print(f"      CR, pre-seam leg on L2           {IC_pre:.6e}   <- the piece the rule drops")
print(f"      CR total if diffusion accumulates {IC_seam+IC_pre:.6e}")
rs_L,_=quad(lambda a: c/(a**2*H(a,1.0)*np.sqrt(3*(1+Rb_of(a)))),1e-9,a_rec,limit=200)
rs_C,_=quad(lambda a: c/(a**2*H(a,0.0)*np.sqrt(3*(1+Rb_of(a)))),a_s,a_rec,limit=200)
for lab,I in [("seam only (the corpus's rule)",IC_seam),("seam + collapse leg",IC_seam+IC_pre)]:
    r=(np.sqrt(I/IL))/(rs_C/rs_L)
    print(f"    theta_D/theta_* ratio, {lab:32s} = {r:.4f}  ({100*(r-1):+.2f}%)")
print("""
  *** SO INCLUDING THE PRE-SEAM DIFFUSION MAKES IT WORSE, NOT BETTER. ***
  The rule's choice is the CONSERVATIVE one, and dropping it is not an escape.
""")
print("""
PLACE 2 — IS THE COMPARISON ITSELF FAIR?  The corpus has a standing objection to the pipeline.
  section 1-SHADOW: 'every Boltzmann code, every r_s / r_D / BBN pipeline' is built on
  hypersurface-orthogonality, which P6 EXCLUDES.  So one might say the CAMB comparison is rigged.
  *** BUT THAT OBJECTION DOES NOT SAVE THIS, AND IT IS IMPORTANT TO SAY WHY. ***
  The corpus does NOT reject the observable.  It PREDICTS A VALUE FOR IT: theta_D/theta_* larger by
  ~9%.  A framework that predicts a specific value for a quantity cannot then decline the measurement
  of that quantity on the grounds that the measuring apparatus embodies a different ontology --
  not while using the same apparatus's r_s to calibrate its own seam redshift, which C9 does.
  *** YOU MAY NOT CALIBRATE ON A PIPELINE AND THEN DISOWN IT WHEN IT DISAGREES. ***
""")
print("""
PLACE 3 — WHAT THE TEST ACTUALLY TESTED, and this is the real limitation.
  My 'CR spectrum' is CAMB's LambdaCDM spectrum times a derived suppression.  C4 licenses the
  ACOUSTIC part of that -- the peaks match, derived not assumed.  It does NOT license the rest:
  lensing, reionisation, the recombination history, the projection.
  *** SO WHAT WAS TESTED IS A HYBRID: LambdaCDM's everything with CR's damping. ***
  That is informative -- it says the damping alone breaks the fit -- but it is NOT 'CR's spectrum',
  and no honest verdict on the framework can rest on it alone.
""")
print("="*80)
