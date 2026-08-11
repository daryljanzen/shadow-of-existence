"""Switch the neutrino sector OFF on BOTH sides and re-run the k-band comparison.
If the deficit vanishes, it is the neutrino sector; if it persists, it is not."""
import numpy as np, camb, os
NEFF=float(os.environ.get('NEFF','3.046'))
pars=camb.CAMBparams()
pars.set_cosmology(H0=67.40, ombh2=0.02237, omch2=0.3150*0.674**2-0.02237, mnu=0.0, tau=0.0,
                   nnu=NEFF, num_massive_neutrinos=0)
pars.InitPower.set_params(As=2.1e-9, ns=0.965)
pars.set_for_lmax(1300, lens_potential_accuracy=0); pars.Accuracy.AccuracyBoost=1.5
r=camb.get_results(pars); td=r.get_cmb_transfer_data()
np.savez('/tmp/camb_tr_nu.npz', d=td.delta_p_l_k, L=td.L, q=td.q)
print("   CAMB rerun with N_eff=%.3f ; saved."%NEFF)
