"""r_s on the LEAF rate for both arms -- the same assignment the diffusion length just took.
P7's rule names the sound horizon FIRST in its list of content processes, so it takes the leaf rate.
The question this settles: does the acoustic angle still work on that assignment?"""
import numpy as np
from scipy.integrate import quad
c=299792.458; z_rec=1089.9; a_rec=1/(1+z_rec)
def rs(H0, Om, ombh2, z_from):
    h=H0/100; Or=4.1833e-5/h**2; OL=1-Om
    Hub=lambda a: H0*np.sqrt(Or/a**4+Om/a**3+OL)              # LEAF rate
    Rb=lambda a: 31500*ombh2/(2.7255/2.7)**4*a
    return quad(lambda a: c/(a**2*Hub(a)*np.sqrt(3*(1+Rb(a)))), 1/(1+z_from), a_rec, limit=300)[0]
def DM(H0, Om):                                                # STACKING rate, radiation-free
    Hub=lambda a: H0*np.sqrt(Om/a**3+(1-Om))
    return quad(lambda a: c/(a**2*Hub(a)), a_rec, 1.0, limit=400)[0]
print("   BOTH content quantities on the LEAF rate; D_M on the stacking rate (P7's assignment).")
print()
print("      H0     Om      r_s(leaf, z->1e7)   D_M(stack)   100*theta_*   l_* = pi D_M/r_s")
for H0 in (67.4, 70.0, 73.0):
    r=rs(H0,0.3150,0.02237,1e7); d=DM(H0,0.3150)
    print("     %5.1f  %.4f      %8.2f          %8.1f      %.5f       %6.1f"%(H0,0.3150,r,d,100*r/d,np.pi*d/r))
print()
print("   measured: 100 theta_* = 1.04109 +- 0.00030 ;  l_* ~ 301.8")
