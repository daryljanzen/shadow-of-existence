"""Does the z_onset cutoff make the rate assignment moot for r_s?
The two rates differ by H0^2 Or (1+z)^4 = 100^2 omega_r (1+z)^4 -- an H0-INDEPENDENT term that
dominates only at high z.  The sound-horizon integral is cut at z_onset.  So: compute r_s from
z_onset on BOTH rates, at several H0, and see."""
import numpy as np
from scipy.integrate import quad
c=299792.458; z_rec=1089.9; a_rec=1/(1+z_rec); ombh2=0.02237
wr=4.1833e-5                      # omega_r, fixed by T_CMB
def rs(H0,Om,zf,leaf):
    h=H0/100
    Hs=lambda a: H0*np.sqrt(Om/a**3+(1-Om))                    # stacking
    H=(lambda a: np.sqrt(Hs(a)**2 + (100**2)*wr/a**4)) if leaf else Hs
    Rb=lambda a: 31500*ombh2/(2.7255/2.7)**4*a
    return quad(lambda a: c/(a**2*H(a)*np.sqrt(3*(1+Rb(a)))), 1/(1+zf), a_rec, limit=300)[0]
def DM(H0,Om):
    Hs=lambda a: H0*np.sqrt(Om/a**3+(1-Om))
    return quad(lambda a: c/(a**2*Hs(a)), a_rec, 1.0, limit=400)[0]
print("   r_s FROM z_onset=6797, both rates, and the resulting acoustic angle")
print()
print("      H0     r_s(stack)  r_s(leaf)   diff     100theta_*(stack)  100theta_*(leaf)")
for H0 in (67.4,70.0,73.0):
    a_=rs(H0,0.3150,6797.,False); b_=rs(H0,0.3150,6797.,True); d=DM(H0,0.3150)
    print("     %5.1f   %8.2f   %8.2f   %+.2f%%      %.5f          %.5f"%(
        H0,a_,b_,100*(b_/a_-1),100*a_/d,100*b_/d))
print()
print("   measured 100 theta_* = 1.04109 +- 0.00030")
