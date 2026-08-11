"""Apply OUR peak-extraction method to CAMB's OWN spectrum.
If subsampling a known-good C_l at DL=15 and refining with three points reproduces our biased
ratios, the extraction is the whole story -- no Boltzmann run needed to find out."""
import numpy as np, camb
from scipy.signal import argrelextrema
p=camb.CAMBparams()
p.set_cosmology(H0=67.40, ombh2=0.02237, omch2=0.3150*0.674**2-0.02237, mnu=0.0, omk=0, tau=0.0)
p.InitPower.set_params(As=2.1e-9, ns=0.965); p.set_for_lmax(1600, lens_potential_accuracy=0)
r=camb.get_results(p)
cl=r.get_cmb_power_spectra(p, CMB_unit='muK', raw_cl=False)['unlensed_scalar'][:,0]
def our_extraction(ls, Dl, order=2):
    """exactly the instrument's method: argrelextrema(order=2) then 3-point parabolic refine"""
    idx=[q for q in argrelextrema(Dl,np.greater,order=order)[0]]
    def refine(q):
        if q<1 or q>=len(ls)-1: return float(ls[q]),float(Dl[q])
        y0,y1,y2=Dl[q-1],Dl[q],Dl[q+1]; d=y0-2*y1+y2
        if d==0: return float(ls[q]),float(y1)
        t=0.5*(y0-y2)/d; h=float(ls[1]-ls[0])
        return float(ls[q]+t*h), float(y1-0.25*(y0-y2)*t)
    return [refine(q) for q in idx[:4]]
print("   CAMB's own spectrum, extracted three ways:")
print()
# truth: dense sampling
pk=our_extraction(np.arange(len(cl))[100:1400].astype(float), cl[100:1400], order=12)
print("     DENSE (every l, order=12)      peaks %s"%[round(x[0],1) for x in pk[:3]])
print("        P1/P2 = %.3f   P1/P3 = %.3f"%(pk[0][1]/pk[1][1], pk[0][1]/pk[2][1]))
print()
for DL,LMIN in ((15,120),(5,120),(30,120)):
    ls=np.arange(LMIN,1250,DL).astype(float)
    Dl=np.interp(ls, np.arange(len(cl)), cl)
    pk=our_extraction(ls,Dl,order=2)
    if len(pk)>=3:
        print("     DL=%-3d (our method)            peaks %s"%(DL,[round(x[0],1) for x in pk[:3]]))
        print("        P1/P2 = %.3f   P1/P3 = %.3f"%(pk[0][1]/pk[1][1], pk[0][1]/pk[2][1]))
print()
print("   OUR INSTRUMENT at DL=15 gave: peaks 218.9/527.5/793.7  P1/P2=2.431  P1/P3=3.263")
