"""IMPLICIT PRODUCTION SPECTRUM, with a harness built for the job:
  - our OWN dense k-grid, chosen so every band has many modes (not subsampled from CAMB's)
  - CAMB's transfer interpolated onto it
  - source range extended to 700 so the early ISW is included
  - calibration anchored at low k where the SW limit is validated on both sides"""
import os, numpy as np
from scipy.integrate import solve_ivp
from scipy.special import spherical_jn
os.environ['ESTORE']='0.5'; os.environ['STRIDE']='1'; os.environ['ETAEND']='760'; os.environ['SNAPETA']='170'
import HIER_photon_hierarchy as H
Z=np.load('/tmp/camb_tr.npz'); dC=Z['d'][0]; LC=Z['L']; qC=Z['q']
kk=np.exp(np.linspace(np.log(0.004),np.log(0.085),96))     # our own grid, log-spaced, dense
E,Y,esw=H.evolve(kk); S=H.SNAPSHOT; Y0=S['y']; e0=S['eta']
ee=np.linspace(e0,700.,1100)
Yi=np.zeros((len(ee),len(kk),6)); ok=np.ones(len(kk),bool)
for i,k in enumerate(kk):
    rhs=lambda e,y,_k=np.array([k]): H._rhs(e,y.reshape(1,-1),_k,False).ravel()
    s=solve_ivp(rhs,[e0,700.],Y0[i],method='Radau',rtol=3e-5,atol=1e-10,dense_output=True)
    if not s.success: ok[i]=False; continue
    ys=s.sol(ee); Pi=(ys[H.IG]+ys[H.IP]+ys[H.IP+2]) if H._POL else ys[H.IG]
    Yi[:,i,0]=ys[2]/4; Yi[:,i,1]=ys[7]; Yi[:,i,2]=ys[6]
    Yi[:,i,3]=ys[H.IN]/2; Yi[:,i,4]=ys[H.IG]/2; Yi[:,i,5]=Pi
print("   implicit: %d/%d modes ok"%(ok.sum(),len(kk)))
np.savez('/tmp/imp2.npz', ee=ee, kk=kk, Y=Yi, ok=ok)
