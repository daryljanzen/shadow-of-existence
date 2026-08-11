import os, numpy as np
os.environ['ESTORE']='0.5'; os.environ['STRIDE']='1'; os.environ['ETAEND']='500'
import HIER_photon_hierarchy as H
Z=np.load('/tmp/camb_ev.npz'); ev=Z['ev']; ets=Z['ets']; K=Z['K']
E,Y,esw=H.evolve(K)
print("  PHOTON ANISOTROPIC STRESS  sigma_gamma  (gauge-invariant at this order)")
print("  CAMB's pi_photon = 2 sigma_gamma in MB convention; compare the RATIO's constancy in eta.")
for i,k in enumerate(K):
    print("   k=%.3f"%k)
    rr=[]
    for j,e in enumerate(ets):
        q=int(np.argmin(abs(E-e)))
        if abs(E[q]-e)>6: continue
        ours=Y[q,i,4]                      # sigma_gamma from the compact store
        camb_sig=ev[i,j,4]/2.0             # pi_photon/2
        r=ours/camb_sig if abs(camb_sig)>1e-9 else np.nan
        rr.append(r)
        print("      eta=%6.0f   ours sigma=%+11.5f   CAMB sigma=%+11.5f   ratio %+9.3f"%(E[q],ours,camb_sig,r))
    a=np.array([x for x in rr if np.isfinite(x)])
    if len(a)>1: print("        -> ratio spread over eta: %.3f to %.3f  (%.0f%%)"%(a.min(),a.max(),100*(a.max()-a.min())/abs(np.mean(a))))
