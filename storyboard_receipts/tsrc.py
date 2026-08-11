import numpy as np, camb
pars=camb.CAMBparams()
pars.set_cosmology(H0=67.40, ombh2=0.02237, omch2=0.3150*0.674**2-0.02237, mnu=0.0, tau=0.0)
pars.InitPower.set_params(As=2.1e-9, ns=0.965)
pars.set_for_lmax(1300, lens_potential_accuracy=0)
r=camb.get_results(pars)
K=np.array([0.015,0.030])
ets=np.linspace(180.,420.,25)
ev=r.get_time_evolution(K, ets, ['T_source'], lAccuracyBoost=2)
print("  CAMB T_source (the line-of-sight temperature source that multiplies j_l)")
print("     eta     k=0.015      k=0.030")
for j,e in enumerate(ets[::3]):
    jj=j*3
    print("   %6.1f  %+11.5f  %+11.5f"%(e,ev[0,jj,0],ev[1,jj,0]))
np.savez('/tmp/camb_tsrc.npz', ev=ev, ets=ets, K=K)
print("  saved.")
