"""PRODUCTION implicit spectrum: integrate every mode with Radau from a tight-coupling snapshot,
NO switch and NO tight-coupling approximation, then assemble the source on a dense output grid and
project.  Compared against CAMB in the same k-bands as r2165/r2167."""
import os, numpy as np
from scipy.integrate import solve_ivp
os.environ['ESTORE']='0.5'; os.environ['STRIDE']='1'; os.environ['ETAEND']='400'; os.environ['SNAPETA']='170'
import HIER_photon_hierarchy as H
Z=np.load('/tmp/camb_tr.npz'); dC=Z['d'][0]; LC=Z['L']; qC=Z['q']
kk=np.array([q for q in qC if 3e-3<=q<=0.085])[::20]
print("   %d modes, implicit; NV=%d"%(len(kk),H.NV))
E,Y,esw=H.evolve(kk)                       # explicit run: gives the snapshot for every mode
S=H.SNAPSHOT; Y0=S['y']; e0=S['eta']
ee=np.linspace(e0,360.,500)
sol_store=np.zeros((len(ee),len(kk),6))
for i,k in enumerate(kk):
    rhs=lambda e,y,_k=np.array([k]): H._rhs(e,y.reshape(1,-1),_k,False).ravel()
    s=solve_ivp(rhs,[e0,360.],Y0[i],method='Radau',rtol=3e-5,atol=1e-10,dense_output=True)
    if not s.success: print("   !! mode k=%.4f failed"%k); continue
    ys=s.sol(ee)                            # (NV, n_eta)
    Pi=(ys[H.IG]+ys[H.IP]+ys[H.IP+2]) if H._POL else ys[H.IG]
    sol_store[:,i,0]=ys[2]/4; sol_store[:,i,1]=ys[7]; sol_store[:,i,2]=ys[6]
    sol_store[:,i,3]=ys[H.IN]/2; sol_store[:,i,4]=ys[H.IG]/2; sol_store[:,i,5]=Pi
np.savez('/tmp/implicit_src.npz', ee=ee, kk=kk, Y=sol_store)
print("   implicit run complete; source saved.")
