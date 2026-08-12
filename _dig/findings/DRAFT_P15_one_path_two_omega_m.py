"""
DRAFT_P15_one_path_two_omega_m.py -- P15 sec:tensions:
** THE SAME CR DETERMINATION, RUN UNDER EACH OMEGA_M THE P15 RECEIPT SET CARRIES, REPRODUCES BOTH
   OF THE PAPER'S TWO VALUES FOR ONE QUANTITY. **

P15 quotes rho_r/rho_m at the angle-fixed onset, at the directly measured H_0, twice:
  * sec:tensions, the inherited-datum paragraph:  "1.71 at H_0 = 73"
    (citing P15_the_ratio_is_the_onset_in_imported_units, which runs Om = 0.3066)
  * ~40 lines later, the withdrawal paragraph:    "1.69 rather than 2.0"
    (the value P15_zonset_determinations prints, which runs Om = 0.3150)

Both are correctly receipted.  ** The receipts disagree on Omega_m, and neither passage says which
it is at. **  This file runs ONE code path -- the CR radiation-free rate pinned to the measured
100 theta_* = 1.04109 -- under each set of constants, so the difference cannot be an artefact of
two different implementations.

⌗ *Most of the Omega_m spread across the P15 set is legitimate and must not be "fixed":
   BUILD_camb_store, P15_camb_reference, P15_damping_ratio_clean and P15_full_transfer_verdict run
   Planck's LambdaCDM at Om ~ 0.315 as the REFERENCE the CR result is measured against.  The one
   that bites is P15_zonset_determinations, which uses the reference value while computing CR's
   OWN quantity.*

NOT CLAIMED: that either receipt is wrong, that either Omega_m is the right one, or anything about
the rate, the H_0-independence of z_onset (verified in both, with zero spread), or the acoustic
scale -- which is RESOLVED and banked and is not reopened here.
"""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
c=299792.458; z_rec=1089.9; a_rec=1/(1+z_rec); ombh2=0.02237
MEAS_TH=1.04109; MEAS_L=np.pi/(MEAS_TH/100)
def run(Om,wr,label):
    Rb=lambda a: 31500*ombh2/(2.7255/2.7)**4*a
    H=lambda H0:(lambda a: H0*np.sqrt(Om/a**3+(1-Om)))
    rs=lambda Hf,zf: quad(lambda a: c/(a**2*Hf(a)*np.sqrt(3*(1+Rb(a)))),1/(1+zf),a_rec,limit=300)[0]
    DM=lambda Hf: quad(lambda a: c/(a**2*Hf(a)),a_rec,1.0,limit=400)[0]
    lstar=lambda zf,H0: np.pi*DM(H(H0))/rs(H(H0),zf)
    z=brentq(lambda z: lstar(z,67.4)-MEAS_L,4000,12000,xtol=0.5)
    out=[]
    for h0 in (67.4,70.0,73.0):
        om_m=Om*(h0/100)**2
        out.append((h0, om_m, wr*(1+z)/om_m))
    print(f"  {label:<34} Om={Om:.4f} wr={wr:.5g}  -> z_onset={z:.1f}")
    for h0,om,rat in out:
        print(f"       H0={h0:5.1f}  omega_m={om:.5f}  rho_r/rho_m at onset = {rat:.4f}")
    return z
print("the SAME determination -- the CR radiation-free rate pinned to the measured angle -- run")
print("with each of the Omega_m the P15 receipt set carries:\n")
run(0.3150,4.1833e-5,"P15_zonset_determinations")
run(0.3066,4.15e-5,"P15_the_ratio_is_the_onset...")
run(0.3070,4.15e-5,"(the paper's DESI value 0.307)")
run(0.3066,4.1833e-5,"cross: 0.3066 with the other wr")
