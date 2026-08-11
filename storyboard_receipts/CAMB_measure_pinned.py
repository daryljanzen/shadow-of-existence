"""Reconstruct CAMB's C_l from CAMB's OWN transfer array.  Entirely internal to CAMB: if this
reproduces its reported spectrum, the measure and normalisation are PINNED and our k-band
comparison is sound.  If not, the same wrong measure sits in our comparison."""
import numpy as np, camb
pars=camb.CAMBparams()
pars.set_cosmology(H0=67.40, ombh2=0.02237, omch2=0.3150*0.674**2-0.02237, mnu=0.0, tau=0.0)
pars.InitPower.set_params(As=2.1e-9, ns=0.965)
pars.set_for_lmax(1300, lens_potential_accuracy=0); pars.Accuracy.AccuracyBoost=1.5
r=camb.get_results(pars)
td=r.get_cmb_transfer_data(); d=td.delta_p_l_k[0]; L=td.L; q=td.q
cl=r.get_cmb_power_spectra(pars, CMB_unit='muK', raw_cl=True)['unlensed_scalar'][:,0]
As=2.1e-9; ns=0.965; kpiv=0.05
PR = As*(q/kpiv)**(ns-1)                        # Delta^2_R(k)
T0 = 2.7255e6                                   # uK
print("   L      CAMB C_l          reconstructed      ratio")
for i,l in enumerate(L):
    if l<2 or l>1200 or l%1: continue
    if int(l) not in (10,50,100,200,400,600,800,1000): continue
    integ = 4*np.pi*PR*d[i]**2/q
    C = np.trapezoid(integ, q)*T0**2
    print("  %5d   %.6e   %.6e   %7.4f"%(l,cl[int(l)],C,C/cl[int(l)] if cl[int(l)]!=0 else np.nan))
