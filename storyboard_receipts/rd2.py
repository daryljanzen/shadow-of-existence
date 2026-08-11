"""r_D on the WORKING assignment: one geometric rate (stacking) with the onset cutoff for CR,
against LambdaCDM's own rate from zero.  Same recombination treatment both sides."""
import numpy as np
from scipy.integrate import quad
c=299792.458; z_rec=1089.9; a_rec=1/(1+z_rec); ombh2=0.02237; wr=4.1833e-5; Om=0.3150
Rb=lambda a: 31500*ombh2/(2.7255/2.7)**4*a
taup=lambda a,h: 2.3e-5*ombh2/h*a**-2
def rD(H0, zf, radiation):
    h=H0/100
    Hs=lambda a: H0*np.sqrt(Om/a**3+(1-Om))
    H=(lambda a: np.sqrt(Hs(a)**2+(100**2)*wr/a**4)) if radiation else Hs
    f=lambda a: (c/(a**2*H(a)))/(6*(1+Rb(a))*taup(a,h))*(Rb(a)**2/(1+Rb(a))+16./15.)
    return np.sqrt(quad(f,1/(1+zf),a_rec,limit=300)[0])
print("   LambdaCDM: its own rate (radiation in), from z->1e7")
rl=rD(67.40,1e7,True); print("      r_D = %.4f Mpc"%rl)
print()
print("   CR: the ONE geometric rate (stacking, radiation-free), cut at the onset")
for zo in (6797.,6850.):
    rc=rD(67.40,zo,False)
    print("      z_onset=%.0f :  r_D = %.4f Mpc   ratio = %.4f  (%+.1f%%)"%(zo,rc,rc/rl,100*(rc/rl-1)))
print()
print("   and the observable, in which D_M cancels:  theta_D/theta_* = r_D/r_s")
rs=lambda H0,zf,rad: quad(lambda a: c/(a**2*((lambda A: np.sqrt((H0*np.sqrt(Om/A**3+(1-Om)))**2+(100**2)*wr/A**4))(a) if rad else H0*np.sqrt(Om/a**3+(1-Om)))*np.sqrt(3*(1+Rb(a)))),1/(1+zf),a_rec,limit=300)[0]
sl=rs(67.40,1e7,True); print("      LCDM  r_D/r_s = %.5f"%(rl/sl))
for zo in (6797.,6850.):
    sc=rs(67.40,zo,False); rc=rD(67.40,zo,False)
    print("      CR (z_onset=%.0f)  r_D/r_s = %.5f   excess = %+.1f%%"%(zo,rc/sc,100*((rc/sc)/(rl/sl)-1)))
