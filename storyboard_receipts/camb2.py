import numpy as np, camb, os
OBF=float(os.environ.get('OBF','1.0')); ob=0.02237*OBF
pars=camb.CAMBparams()
pars.set_cosmology(H0=67.40, ombh2=ob, omch2=0.3150*0.674**2-ob, mnu=0.0, tau=0.0)
pars.InitPower.set_params(As=2.1e-9, ns=0.965)
pars.set_for_lmax(1300, lens_potential_accuracy=0); pars.Accuracy.AccuracyBoost=1.5
r=camb.get_results(pars); td=r.get_cmb_transfer_data()
np.savez('/tmp/camb_tr_obf.npz', d=td.delta_p_l_k, L=td.L, q=td.q)
print("  CAMB rerun at ombh2=%.5f (OBF=%.1f);  r_s(z*) = %.2f Mpc  (was %.2f at OBF=1)"
      %(ob,OBF,r.get_derived_params()['rstar'], 144.4))
print("  => k_s = pi/r_s = %.5f /Mpc   (OBF=1 gives %.5f)"%(np.pi/r.get_derived_params()['rstar'], np.pi/144.4))
