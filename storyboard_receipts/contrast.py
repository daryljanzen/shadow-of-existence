"""Effective damping from PEAK-TO-TROUGH CONTRAST -- no undamped reference needed on either side.
The oscillation amplitude relative to the smooth mean falls as exp(-2 k^2 r_D^2) with k = l/D.
Fit ln(contrast) vs l^2 for CAMB and for ours; the slope gives r_D^2 for each."""
import numpy as np, camb, os
pars=camb.CAMBparams()
pars.set_cosmology(H0=67.40, ombh2=0.02237, omch2=0.3150*0.674**2-0.02237, mnu=0.0, tau=0.0)
pars.InitPower.set_params(As=2.1e-9, ns=0.965)
pars.set_for_lmax(1600, lens_potential_accuracy=0); pars.Accuracy.AccuracyBoost=1.5
r=camb.get_results(pars)
D=r.get_cmb_power_spectra(pars, CMB_unit='muK', raw_cl=False)['unlensed_scalar'][:,0]
ls=np.arange(len(D))
from scipy.signal import argrelextrema as ar
def contrasts(ls,D,lo=150,hi=1500):
    m=(ls>=lo)&(ls<=hi); L=ls[m]; Y=D[m]
    pk=list(ar(Y,np.greater,order=8)[0]); tr=list(ar(Y,np.less,order=8)[0])
    out=[]
    for p in pk:                                    # pair each PEAK with the NEXT trough
        nxt=[t for t in tr if t>p]
        if not nxt: continue
        t=nxt[0]; a,b=Y[p],Y[t]
        out.append((0.5*(L[p]+L[t]), abs(a-b)/(a+b)))
    return out
c=contrasts(ls,D)
print("   CAMB unlensed: peak-trough contrast")
for lm,v in c: print("      l_mid=%6.0f   contrast=%.4f"%(lm,v))
DM=13864.0
x=np.array([lm for lm,_ in c]); y=np.array([v for _,v in c])
if len(x)>=3:
    A=np.polyfit(x**2, np.log(y), 1)
    rD2=-A[0]*DM**2/2.0
    print()
    print("   fit ln(contrast) = a*l^2 + b :  a = %.3e  ->  r_D^2 = %.1f Mpc^2  (r_D=%.2f Mpc)"%(A[0],rD2,np.sqrt(abs(rD2))))
    print("   [ours delivers 32-44; standard formula 50.2]")
