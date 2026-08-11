"""Direct variable-by-variable comparison against CAMB at fixed k, through recombination.
The most direct diagnostic available: no projection, no k-integral, no normalisation anchor."""
import os, numpy as np, camb
K=[0.015,0.030]
pars=camb.CAMBparams()
pars.set_cosmology(H0=67.40, ombh2=0.02237, omch2=0.3150*0.674**2-0.02237, mnu=0.0, tau=0.0)
pars.InitPower.set_params(As=2.1e-9, ns=0.965)
pars.set_for_lmax(1300, lens_potential_accuracy=0)
r=camb.get_results(pars)
ets=np.array([150.,200.,240.,277.,320.,400.])
ev=r.get_time_evolution(np.array(K), ets, ['delta_photon','v_newtonian_baryon','Weyl','v_photon','pi_photon'], lAccuracyBoost=2)
print("  CAMB  (Newtonian-ish outputs; delta_photon, v_baryon, Weyl)")
for i,k in enumerate(K):
    print("   k=%.3f"%k)
    for j,e in enumerate(ets):
        print("      eta=%6.0f   d_g=%+9.4f v_b=%+9.4f Weyl=%+9.5f v_g=%+9.4f pi_g=%+9.5f"%(e,ev[i,j,0],ev[i,j,1],ev[i,j,2],ev[i,j,3],ev[i,j,4]))
np.savez('/tmp/camb_ev.npz', ev=ev, ets=ets, K=np.array(K))
