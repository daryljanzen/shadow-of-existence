"""LET THE DATA CHOOSE.  Two candidate rates for the plasma's diffusion.  The observable is
theta_D/theta_* -- the damping scale in units of the acoustic scale, projection-independent.
It is MEASURED.  So: compute it both ways and see which the sky picks.

Measured damping scale: Planck gives the damping tail; the standard parametrisation is
theta_D/theta_* ~ 0.1615 (i.e. l_D/l_* with l_D ~ 1400 and l_* ~ 301.8 -> 4.64 ... conventions vary)
so we work in a convention-free way: form theta_D/theta_* for BOTH candidates and for LambdaCDM,
and ask which pair is closer.  LambdaCDM is known to fit the tail, so LambdaCDM's value IS the
measured one to the accuracy that matters here."""
import numpy as np
from scipy.integrate import quad
c=299792.458; z_rec=1089.9; a_rec=1/(1+z_rec); ombh2=0.02237; wr=4.1833e-5; Om=0.3150
Rb=lambda a: 31500*ombh2/(2.7255/2.7)**4*a
def rates(H0):
    Hs=lambda a: H0*np.sqrt(Om/a**3+(1-Om))
    Hl=lambda a: np.sqrt(Hs(a)**2+(100**2)*wr/a**4)
    return Hs,Hl
def rD(H,zf,H0):
    tp=lambda a: 2.3e-5*ombh2/(H0/100)*a**-2
    f=lambda a: (c/(a**2*H(a)))/(6*(1+Rb(a))*tp(a))*(Rb(a)**2/(1+Rb(a))+16./15.)
    return np.sqrt(quad(f,1/(1+zf),a_rec,limit=300)[0])
def rs(H,zf): return quad(lambda a: c/(a**2*H(a)*np.sqrt(3*(1+Rb(a)))), 1/(1+zf), a_rec, limit=300)[0]
print("   theta_D/theta_* = r_D/r_s -- projection-independent, so D_M drops out entirely.")
print("   (LambdaCDM fits the observed tail, so its value is the target.)")
print()
print("      account                                        r_D      r_s     r_D/r_s   vs LCDM")
Hs,Hl=rates(67.40)
b_rD=rD(Hl,1e7,67.40); b_rs=rs(Hl,1e7); base=b_rD/b_rs
print("      LambdaCDM (radiation in, from zero)          %.4f  %7.2f  %.5f   ---"%(b_rD,b_rs,base))
for zo in (6797.,):
    for H,lab in ((Hs,'STACKING rate (radiation out)'),(Hl,'LEAF rate (radiation in)')):
        r=rD(H,zo,67.40); sfun=rs(H,zo)
        print("      CR, %-28s     %.4f  %7.2f  %.5f   %+6.1f%%"%(lab,r,sfun,r/sfun,100*((r/sfun)/base-1)))
print()
print("   NOTE r_s must use the SAME rate as r_D for the ratio to be a coherent observable --")
print("   both are lengths laid down in the same plasma over the same interval.")
