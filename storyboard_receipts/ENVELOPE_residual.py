"""RE-MEASURE the residual by the ENVELOPE method, across the full k range and several l.
No bins, no interpolation of CAMB onto our grid beyond the extremum itself, ratio taken where
|Delta| is at a maximum so it is well-conditioned."""
import os, numpy as np
from scipy.special import spherical_jn
from scipy.signal import argrelextrema as ar
os.environ['ESTORE']='0.5'; os.environ['STRIDE']='2'; os.environ['ETAEND']='760'
import HIER_photon_hierarchy as H
Z=np.load('/tmp/camb_tr.npz'); dC=Z['d'][0]; LC=Z['L']; qC=Z['q']
kk=np.array([q for q in qC if 0.004<=q<=0.095])
E,Y,esw=H.evolve(kk)
m=E>max(esw,H.eta_rec-160.); ee=E[m]; Yv=Y[m]
g=np.array([float(H.g_of(e)) for e in ee]); tau=np.array([float(H.tau_of(e)) for e in ee])
Sm,Sd,Si,Sq=H.source_terms(ee,Yv,kk,g,tau)
if Sq is None: Sq=np.zeros_like(Sm)
bins=np.array([0.010,0.018,0.026,0.038,0.055,0.080,0.095])
print("   ENVELOPE ratio ours/CAMB (median over extrema in each k range), calibrated at the lowest")
print("      l    " + "".join("%12s"%("%.3f-%.3f"%(a,b)) for a,b in zip(bins[:-1],bins[1:])))
for L in [int(v) for v in LC if v in (90,150,250,350,500,700)]:
    iL=int(np.argmin(abs(LC-L))); Dc=np.interp(kk,qC,dC[iL])
    X=kk[None,:]*(H.eta_0-ee)[:,None]
    jl=spherical_jn(L,X); jlp=spherical_jn(L,X,derivative=True); Xs=np.maximum(X,1e-8)
    Kq=-3.0*jlp/Xs+(3.0*L*(L+1)/(2.0*Xs**2)-1.0)*jl
    Do=np.trapezoid(Sm*jl+Si*jl+Sd*jlp+Sq*Kq,ee,axis=0)
    ao=np.abs(Do); ac=np.abs(Dc)
    ext=np.array([i for i in ar(ac,np.greater,order=3)[0] if ac[i]>0.02*ac.max()])
    if len(ext)<4: continue
    rat=ao[ext]/ac[ext]; kx=kk[ext]
    vals=[np.median(rat[(kx>=a)&(kx<b)]) if ((kx>=a)&(kx<b)).sum()>=2 else np.nan
          for a,b in zip(bins[:-1],bins[1:])]
    v=np.array(vals); base=v[~np.isnan(v)][0]
    print("   %4d   "%LC[iL] + "".join("%12.4f"%(x/base) for x in v))
