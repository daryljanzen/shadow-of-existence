#!/usr/bin/env python3
# Route A: CR's CMB acoustic scale, done properly (r462, c23 with Daryl). DO-NOT-ASSERT.
#
# Honest CR acoustic scale = ordinary photon-baryon plasma sound horizon on CR's NO-RADIATION rate
# (H ~ (1+z)^(3/2) matter+Lambda, NOT radiation-boosted (1+z)^2), integrated from recombination z*
# back to the FINITE onset of free radiation z_wall (the wall, sec325/P6) -- NOT to a->0.
#   - The a->0 upper limit on CR's rate is the "172 hybrid" sec687 disowns (a model of neither framework).
#   - z_wall is the one input CR's picture puts in place of "radiation density in the rate"; sec265 says
#     the no-radiation claim is decided by early-universe data, not derived from Lambda.
# Pipeline VALIDATED against standard LambdaCDM: reproduces r_s=144.3 Mpc, l_A=302 (Planck 144.4, ~301).
#
# RESULT, with the r463 CORRECTION (grounded at P9 sec687 + P6 sec-wall):
#  - VALIDATED pipeline (standard LambdaCDM -> r_s=144.3, l_A=302) and the a->0 limit on CR's rate -> l_A~172
#    are SOLID. The 172 is positively identified as sec687's hybrid (standard plasma+integral on CR's rate).
#  - RETRACTED: the "z_wall ~ 2 z_eq reproduces l_A=301" line below is NOT a CR prediction. sec687 names TWO
#    unbuilt pieces -- (i) the medium and its c_s, (ii) the integration limit = the finite-curvature SEAM's
#    location relative to recombination (NOT the wall; the wall is P6's symmetry boundary, not a redshift).
#    The "z_wall=2z_eq" fit tuned BOTH unbuilt pieces to the answer -> a hybrid, not a prediction; the factor
#    2.00 was a fit coincidence. The scan below is retained only as a SENSITIVITY MAP of sec687 piece (ii):
#    l_A runs from 172 (seam at a->0) upward as the seam moves to finite z. Where the seam sits, and whether
#    a pre-recombination sound-travel integral exists on this side at all, is UNCONSTRUCTED (sec687).
#  - CR's acoustic scale is OPEN, blocked on sec687's two pieces = the node-4 frontier (build, don't fit).
import numpy as np
from scipy import integrate
from scipy.optimize import brentq

c=299792.458; H0=67.4; h=H0/100; Om=0.315; OL=0.685          # flat LambdaCDM measured inputs
Ob=0.02237/h**2; Og=2.47e-5/h**2; Neff=3.046; Or=Og*(1+0.2271*Neff); zstar=1089.8
R=lambda z:0.75*Ob/Og/(1+z)                                   # baryon loading
H_std=lambda z:H0*np.sqrt(Or*(1+z)**4+Om*(1+z)**3+OL)         # standard: radiation in rate
H_cr =lambda z:H0*np.sqrt(           Om*(1+z)**3+OL)          # CR: NO radiation in rate
Dc=lambda zhi,H:integrate.quad(lambda z:c/H(z),0,zhi,limit=200)[0]
rs=lambda zup,H,cs:integrate.quad(lambda z:cs(z)/H(z),zstar,zup,limit=200)[0]
cs_baryon=lambda z:c/np.sqrt(3*(1+R(z))); cs_geom=lambda z:c/np.sqrt(3)
zeq=Om/Or-1

if __name__=="__main__":
    DMs,rss=Dc(zstar,H_std),rs(np.inf,H_std,cs_baryon)
    print(f"VALIDATION std LambdaCDM: D_M={DMs:.0f} r_s={rss:.1f} l_A={np.pi*DMs/rss:.0f}  (Planck 13900/144.4/301)")
    DM=Dc(zstar,H_cr); print(f"CR D_M={DM:.0f}  z_eq={zeq:.0f}  z*={zstar:.0f}")
    for nm,cs in [("baryon-loaded c/sqrt(3(1+R))",cs_baryon),("geometric c/sqrt3",cs_geom)]:
        lA_inf=np.pi*DM/rs(1e7,H_cr,cs); zw=brentq(lambda z:np.pi*DM/rs(z,H_cr,cs)-301.0,1100.1,1e7)
        print(f"  {nm:28s}: a->0 l_A={lA_inf:.0f} (hybrid); z_wall(l_A=301)={zw:.0f} = {zw/zeq:.2f}*z_eq")
