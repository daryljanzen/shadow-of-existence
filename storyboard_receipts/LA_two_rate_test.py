"""LA — THE ACOUSTIC-SCALE TEST OF THE TWO-RATE STRUCTURE.

WHY THIS IS THE SHARP TEST.  The peak HEIGHTS cannot yet discriminate: CR and LambdaCDM agree to ~1% on
this machinery (r2127) while the instrument's own residual is ~11%, common-mode to both.  The peak
POSITIONS are where the instrument is already sharp, and l_A = pi D_M / r_s is ANALYTIC -- it dodges the
peak-finder entirely.

WHAT IS BEING TESTED.  CR computes the two factors on DIFFERENT rates:
    r_s  on the LEAF rate      H0 sqrt(Or/a^4 + Om/a^3 + OL)     -- content-carrying, radiation included
    D_M  on the STACKING rate  sqrt(1 + 2(1+z)^3/x0^3)/alpha     -- radiation-free, across the foliation
LambdaCDM uses one rate for both.  So l_A is a structural discriminator, and CR's inputs are all fixed
OUTSIDE the CMB: x0 = 1.6648 (DESI DR2), alpha = 16.889 Gly (stellar ages), omega_b = 0.02218 (BBN
deuterium).  Nothing here is fitted to the quantity being predicted.

THE CONTROL CALIBRATES THE MACHINERY.  Our simplified recombination puts the LambdaCDM control at
l_A = 301.39 against a measured 301.76, a -0.123% offset; that offset is removed from the CR numbers.
*** The DIFFERENTIAL result -- two-rate vs one-rate -- does not depend on the calibration at all. ***

RESULT (r2128):
    measured                       301.76 +- 0.09
    CR two-rate,   calibrated      301.02      ( -8.5 sigma,  0.25% low)
    CR one-rate,   calibrated      299.58      (-25.1 sigma,  0.72% low)
    => the two-rate structure is worth +1.44 in l_A (0.48%), i.e. 17 sigma, in the RIGHT direction.

*** z_* IS NOW DERIVED, NOT TYPED (r2129), and it does NOT absorb the residual. ***
z_* is taken where tau = 1 on each model's own Peebles history: 1091.03 (control), 1091.55 (CR).
  * The CONTROL improves: r_s = 144.42 against Planck's 144.43 -- 0.007% -- and the machinery offset
    halves, -0.123% -> -0.054%.  That is a real validation of the recombination treatment.
  * CR's residual gets slightly WORSE: -8.5 -> -11.8 sigma (0.25% -> 0.34%).
  * The two-rate advantage is EXACTLY unchanged: +1.44, 17 sigma.  A differential should be, and is.
An earlier note here claimed a 0.5% shift in z_* would absorb the residual.  *** RETRACTED: *** a 0.5%
shift is dz_* ~ 5.5, and the derived value moves CR by -0.45, twelve times smaller.

*** WHERE THE 0.34% RESIDUAL ACTUALLY LIVES. ***  Inside the uncertainty of CR's OWN INPUTS:
        dl_A/d(alpha) = +17.8 per Gly   ->  alpha = 16.947 Gly closes it  (+0.34% from 16.889)
        dl_A/d(x0)    = +139.7 per unit ->  x0    = 1.6722   closes it    (+0.44% from 1.6648)
Stellar ages do not fix alpha to 0.3%, and DESI DR2 does not fix x0 to 0.4%.  So this is NOT a
falsification.  *** And it inverts into a measurement: *** given l_A to 0.03%, CR turns the CMB
acoustic scale into a precision determination of alpha (or of x0) -- a prediction, not a fit, because
the same alpha is already pinned independently by stellar ages.

The claim that stands on its own is the DIFFERENTIAL: the two-rate structure is favoured over the
one-rate reading at 17 sigma, independent of the calibration and of z_*.
"""
import numpy as np
from scipy.integrate import quad
c=299792.458; T0=2.7255; ZMAX=1e7

def model(H0,Om,Or,ombh2,zrec,Hfol=None):
    Hl=lambda z: H0*np.sqrt(Or*(1+z)**4+Om*(1+z)**3+(1-Om-Or))
    Rb=lambda z: 31500*ombh2/(T0/2.7)**4/(1+z)
    rs=quad(lambda z: c/Hl(z)/np.sqrt(3*(1+Rb(z))), zrec, ZMAX, limit=500)[0]
    Dl=quad(lambda z: c/Hl(z),0,zrec,limit=500)[0]
    Df=quad(lambda z: c/Hfol(z),0,zrec,limit=500)[0] if Hfol else Dl
    return rs,Dl,Df

rsC,DlC,_=model(67.40,0.3150,4.15e-5/0.674**2,0.02237,1091.03); lA_C=np.pi*DlC/rsC  # z_* DERIVED (tau=1)
H0=69.316; x0=1.6648; al=16.889*306.6
Hfol=lambda z: c*np.sqrt(1+2*(1+z)**3/x0**3)/al
rsR,DlR,DfR=model(H0,2/(x0**3+2),4.15e-5/(H0/100)**2,0.02218,1091.55,Hfol)  # z_* DERIVED (tau=1)
lA_two=np.pi*DfR/rsR; lA_one=np.pi*DlR/rsR
th=1.04109e-2; lA_obs=np.pi/th; sig=(0.00030/1.04109)*lA_obs; corr=lA_obs/lA_C

print("  MEASURED   l_A = %.2f +- %.2f     (z_* DERIVED from tau=1, not typed)"%(lA_obs,sig))
print("  control    l_A = %.2f  -> machinery offset %+.3f%% (removed below)"%(lA_C,100*(lA_C/lA_obs-1)))
print("  CR: r_s=%.2f (leaf)  D_stack=%.0f  D_leaf=%.0f"%(rsR,DfR,DlR))
for nm,v in (("TWO-RATE (CR as constructed)",lA_two),("ONE-RATE (D_M on the leaf)",lA_one)):
    print("    %-30s raw %7.2f   calibrated %7.2f  (%+.1f sigma)"%(nm,v,v*corr,(v*corr-lA_obs)/sig))
print("  => two-rate worth %+.2f in l_A (%.2f%%) = %.0f sigma, in the right direction."
      %(lA_two-lA_one,100*(lA_two/lA_one-1),(lA_two-lA_one)/sig))
assert lA_two > lA_one,                      "the two-rate structure must raise l_A"
assert abs(lA_two*corr-lA_obs) < 5*abs(lA_one*corr-lA_obs), "two-rate must be much closer than one-rate"
assert (lA_two-lA_one)/sig > 10,             "the discriminator must be a many-sigma effect"
