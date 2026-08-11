"""THE SLIP, tested at recombination.  theta_g - theta_b is GAUGE-INVARIANT (both shift alike),
so CAMB's synchronous-gauge pair v_photon and v_baryon_cdm (v_cdm=0 in synchronous) gives a
directly comparable slip.  Ours: theta_g from EXACT photon continuity, theta_b from the store."""
import os, numpy as np, camb
os.environ['ESTORE']='0.5'; os.environ['STRIDE']='1'; os.environ['ETAEND']='500'
import HIER_photon_hierarchy as H
K=np.array([0.015,0.030])
pars=camb.CAMBparams()
pars.set_cosmology(H0=67.40, ombh2=0.02237, omch2=0.3150*0.674**2-0.02237, mnu=0.0, tau=0.0)
pars.InitPower.set_params(As=2.1e-9, ns=0.965); pars.set_for_lmax(1300, lens_potential_accuracy=0)
r=camb.get_results(pars)
ets=np.array([240.,255.,265.,277.,290.,305.])
ev=r.get_time_evolution(K, ets, ['v_photon','v_baryon_cdm'], lAccuracyBoost=2)
E,Y,esw=H.evolve(K)
print("  SLIP  v_gamma - v_baryon  (gauge-invariant).  ours from exact photon continuity.")
print("     eta      k=0.015                          k=0.030")
print("            ours       CAMB      ratio       ours       CAMB      ratio")
for j,e in enumerate(ets):
    q=int(np.argmin(abs(E-e)))
    row=""
    for i,k in enumerate(K):
        dTh=(Y[q+1,i,0]-Y[q-1,i,0])/(E[q+1]-E[q-1]); dPh=(Y[q+1,i,2]-Y[q-1,i,2])/(E[q+1]-E[q-1])
        thg=-3.0*dTh+3.0*dPh                       # exact continuity
        s_ours=(thg-Y[q,i,1])/k                    # as a velocity
        s_camb=ev[i,j,0]-ev[i,j,1]
        row+="  %+9.5f %+9.5f %7.3f"%(s_ours,s_camb,s_ours/s_camb if abs(s_camb)>1e-12 else np.nan)
    print("   %6.0f %s"%(e,row))
