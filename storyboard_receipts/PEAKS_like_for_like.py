"""Like-for-like peak ratios: CAMB UNLENSED at the instrument's own parameters, tau matched.
The instrument's control is unlensed and has no reionisation, so that is the reference."""
import numpy as np, camb
from scipy.signal import argrelextrema
def peaks(cl, lo=100, hi=1300, order=12):
    ell=np.arange(len(cl))
    idx=argrelextrema(cl[lo:hi],np.greater,order=order)[0]+lo
    return [(int(l), float(cl[l])) for l in idx][:4]
for tau,lab in ((0.0,'tau=0 (matched to the instrument)'),(0.0544,'tau=0.0544')):
    p=camb.CAMBparams()
    p.set_cosmology(H0=67.40, ombh2=0.02237, omch2=0.3150*0.674**2-0.02237, mnu=0.0, omk=0, tau=tau)
    p.InitPower.set_params(As=2.1e-9, ns=0.965)
    p.set_for_lmax(1600, lens_potential_accuracy=0)
    r=camb.get_results(p)
    for kind in ('unlensed_scalar','total'):
        try: cl=r.get_cmb_power_spectra(p, CMB_unit='muK', raw_cl=False)[kind][:,0]
        except Exception: continue
        pk=peaks(cl)
        if len(pk)<3: continue
        print("   CAMB %-34s %-16s peaks %s"%(lab,kind,[p_[0] for p_ in pk]))
        print("        P1/P2 = %.3f   P1/P3 = %.3f"%(pk[0][1]/pk[1][1], pk[0][1]/pk[2][1]))
print()
print("   OURS (instrument, unlensed, no reionisation):")
print("        peaks 218.9 / 527.5 / 793.7      P1/P2 = 2.431   P1/P3 = 3.263")
print()
print("   PLANCK 2018 (lensed, observed):")
print("        peaks 220.6 / 538.1 / 809.8      P1/P2 = 2.217   P1/P3 = 2.277")
