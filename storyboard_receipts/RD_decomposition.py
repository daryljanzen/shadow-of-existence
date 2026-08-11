"""WHY does one computation give 10% and the other 0.4%?  Decompose it: the two differ in TWO
things at once -- the RATE (radiation in or out) and the LOWER LIMIT (onset or zero).  Vary them
one at a time and see which carries the difference."""
import numpy as np
from scipy.integrate import quad
c=299792.458; z_rec=1089.9; a_rec=1/(1+z_rec); ombh2=0.02237; wr=4.1833e-5; Om=0.3150; H0=67.40
Rb=lambda a: 31500*ombh2/(2.7255/2.7)**4*a
taup=lambda a: 2.3e-5*ombh2/(H0/100)*a**-2
def rD(zf, radiation):
    Hs=lambda a: H0*np.sqrt(Om/a**3+(1-Om))
    H=(lambda a: np.sqrt(Hs(a)**2+(100**2)*wr/a**4)) if radiation else Hs
    f=lambda a: (c/(a**2*H(a)))/(6*(1+Rb(a))*taup(a))*(Rb(a)**2/(1+Rb(a))+16./15.)
    return np.sqrt(quad(f,1/(1+zf),a_rec,limit=300)[0])
base=rD(1e7,True)                         # LambdaCDM: radiation in, from zero
print("   LambdaCDM reference (radiation in the rate, from z->1e7):  r_D = %.4f Mpc"%base)
print()
print("      configuration                                    r_D      vs LCDM")
for zf,rad,lab in ((1e7,True,'radiation IN, from zero        (= LCDM)'),
                   (6797.,True,'radiation IN, cut at onset     (LIMIT only)'),
                   (1e7,False,'radiation OUT, from zero       (RATE only)'),
                   (6797.,False,'radiation OUT, cut at onset    (BOTH = CR)')):
    r=rD(zf,rad); print("      %-46s %.4f   %+6.1f%%"%(lab,r,100*(r/base-1)))
print()
print("   => the LIMIT alone is worth a fraction of a per cent; the RATE alone carries essentially")
print("      all of the difference.  The 0.4% computation held the rate fixed, so it was measuring")
print("      the LIMIT and nothing else -- it never asked the question the 10% answers.")
