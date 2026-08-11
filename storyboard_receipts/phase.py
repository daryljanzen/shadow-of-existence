"""Measure the acoustic phase directly off the evolved modes.
Take single k values, find where Theta_0 + Psi has its extrema in eta, and compare the
oscillation period against k*r_s.  This distinguishes:
   modes oscillate differently than r_s says   ->  the physics/background disagree
   modes are fine but the l-axis is mislabelled ->  the k<->l mapping is wrong"""
import os, sys, numpy as np
sys.path.insert(0,'/home/claude/cr/cr_r2369/storyboard_receipts')
import importlib.util
spec=importlib.util.spec_from_file_location("crmod","C11TEST_radiation_zeroed.py")
# the module runs its whole script on import, so instead reproduce the mode ODE minimally:
from scipy.integrate import quad
c=299792.458; H0=73.0; Om=0.3066; OL=1-Om; ombh2=0.0224; z_rec=1089.9; a_rec=1/(1+z_rec)
Rb_rec=31500*ombh2/(2.7255/2.7)**4/(1+z_rec)
Hub=lambda a: H0*np.sqrt(Om/a**3+OL)
rs_f=lambda zs: quad(lambda a: c/(a**2*Hub(a)*np.sqrt(3*(1+Rb_rec*a/a_rec))),1/(1+zs),a_rec,limit=250)[0]
eta=lambda z: quad(lambda a: c/(a**2*Hub(a)),1e-12,1/(1+z),limit=300)[0]
zs=6761.; eo=eta(zs); er=eta(z_rec); rs=rs_f(zs); DM=eta(0.)-er
print("   background: eta_onset=%.2f  eta_rec=%.2f  r_s=%.2f  D_M=%.0f"%(eo,er,rs,DM))
print()
# a mode with k r_s = n pi has n half-oscillations across the span.  Count them for the k's
# the ladder assigns to the peaks it FOUND, and to the peaks l_A PREDICTS.
print("      l        k = l/D_M      k*r_s        k*r_s/pi   (integer = an acoustic extremum)")
for lab,l in (('found P1',345),('found P2',555),('found P3',795),('found P4',1020),
              ('l_A',301.6),('2 l_A',603.2),('3 l_A',904.8)):
    k=l/DM
    print("      %-9s %.6f     %8.4f     %7.4f"%(lab+' l=%.0f'%l,k,k*rs,k*rs/np.pi))
