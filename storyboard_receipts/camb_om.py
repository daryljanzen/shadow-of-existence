import numpy as np, camb, os
OMF=float(os.environ.get('OMF','1.0')); Om=0.3150*OMF
pars=camb.CAMBparams()
pars.set_cosmology(H0=67.40, ombh2=0.02237, omch2=Om*0.674**2-0.02237, mnu=0.0, tau=0.0)
pars.InitPower.set_params(As=2.1e-9, ns=0.965)
pars.set_for_lmax(1300, lens_potential_accuracy=0); pars.Accuracy.AccuracyBoost=1.5
r=camb.get_results(pars); td=r.get_cmb_transfer_data()
np.savez('/tmp/camb_tr_om.npz', d=td.delta_p_l_k, L=td.L, q=td.q)
d=r.get_derived_params()
print("   OMF=%.2f  Om=%.4f  r_s=%.2f Mpc  z*=%.1f   (OMF=1: r_s=144.26)"%(OMF,Om,d['rstar'],d['zstar']))
