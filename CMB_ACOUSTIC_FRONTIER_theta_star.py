#!/usr/bin/env python3
# CMB acoustic-scale decomposition for CR (r368, c21).
#
# WHAT IS VALID HERE:  the D_M comparison. Standard-LCDM calibration reproduces 100*theta*=1.040
#   (~observed 1.041), and CR's radiation-free D_M differs from standard by only 0.5% -- the comoving
#   distance is low-z dominated and is the flat-LCDM observable (P7 550/696). So D_M is robust, and the
#   CR-vs-LCDM acoustic-scale question localizes entirely to r_s.
#
# WHAT IS NOT A CR RESULT:  the r_s and theta* this script prints. The r_s integral below keeps the
#   STANDARD photon-baryon plasma sound speed and integrates to z->inf while only removing radiation
#   from the expansion RATE. That grafts the standard early-universe structure (a radiation plasma,
#   the standard sound horizon, the integral to infinity) onto a radiation-free rate -- exactly the
#   structure P7 679 says CR does NOT have. It is the WRONG calculation for CR: a chimera of neither
#   model. The number it prints (100*theta* ~ 1.76) is NOT a CR prediction, NOT a tension, NOT to be
#   reported as a result. CR's acoustic scale is UNCOMPUTED -- the rigorous r_s (sound-horizon
#   evolution in the 3-sphere ontology, projected to the observable frame; P7 679) is unperformed.
#   The r_s/theta* lines are kept ONLY so the wrong-method number is recognized on sight and discarded,
#   not re-derived as if new.

import numpy as np
from scipy.integrate import quad

# Planck 2018 (stated for reversal)
c = 299792.458; H0 = 67.36; Om = 0.3153; OL = 0.6847
h = H0/100; Ob = 0.02237/h**2
Og = 2.47e-5/h**2; Or = 4.15e-5/h**2      # photons; photons+neutrinos
zstar = 1089.92

def Hstd(z): return H0*np.sqrt(Om*(1+z)**3 + Or*(1+z)**4 + OL)   # standard: radiation in the rate
def Hcr(z):  return H0*np.sqrt(Om*(1+z)**3 + OL)                 # CR: radiation NOT in the rate (P7 679)
def cs(z):
    R = (3*Ob)/(4*Og)/(1+z)
    return c/np.sqrt(3*(1+R))                                   # standard photon-baryon plasma c_s
def DM(H, zmax): return quad(lambda z: c/H(z), 0, zmax, limit=200)[0]
def rs(H, zmax): return quad(lambda z: cs(z)/H(z), zstar, zmax, limit=400)[0]

if __name__ == "__main__":
    rs_s, DM_s = rs(Hstd, 1e6), DM(Hstd, zstar)
    rs_c, DM_c = rs(Hcr, 1e6),  DM(Hcr, zstar)
    print(f"standard LCDM : r_s={rs_s:7.2f}  D_M={DM_s:8.1f}  100theta*={100*rs_s/DM_s:6.4f}  (obs ~1.041)")
    print(f"CR rad-free   : r_s={rs_c:7.2f}  D_M={DM_c:8.1f}  100theta*={100*rs_c/DM_c:6.4f}")
    print(f"ratios CR/std : D_M x{DM_c/DM_s:.4f} (robust)   r_s x{rs_c/rs_s:.4f} (the whole difference)")
