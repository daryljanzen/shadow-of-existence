"""Contribution to C_l per k-band: dC_l/dlnk ~ k^{ns} Delta_l(k)^2.  Positive-definite, so it can be
binned and compared without the zero-crossing pathology of a pointwise transfer ratio."""
import os, numpy as np
from scipy.special import spherical_jn
os.environ['ETAEND']='1400'; os.environ['STRIDE']='10'
import HIER_photon_hierarchy as H
Z=np.load('/tmp/camb_tr.npz'); dC=Z['d'][0]; LC=Z['L']; qC=Z['q']
kk=np.array([q for q in qC if 1e-3<=q<=0.12])[::2]
E,Y,esw=H.evolve(kk)
m=E>max(esw,H.eta_rec-160.); ee=E[m]; Yv=Y[m]
g=np.array([float(H.g_of(e)) for e in ee]); tau=np.array([float(H.tau_of(e)) for e in ee])
Ph=Yv[:,:,2]; sgn=Yv[:,:,3]; sgg=Yv[:,:,4]; Pi=Yv[:,:,5]
Hcv=np.array([H.Hc_of(e) for e in ee])[:,None]
Onv=np.array([H.On_of(e) for e in ee])[:,None]; Ogv=np.array([H.Og_of(e) for e in ee])[:,None]
Ps=Ph-6*Hcv**2*(Onv*sgn+Ogv*sgg)/kk[None,:]**2
Sm=g[:,None]*(Yv[:,:,0]+Ps+Pi/16.); Sd=g[:,None]*(Yv[:,:,1]/kk[None,:])
Si=np.exp(-tau)[:,None]*(np.gradient(Ph,ee,axis=0)+np.gradient(Ps,ee,axis=0))
x0m=H.eta_0-ee
edges=np.array([0.002,0.006,0.012,0.020,0.030,0.042,0.056,0.072,0.090,0.120])
print("  CONTRIBUTION TO C_l PER k-BAND, ours/CAMB (each row renormalised to its own total)")
print("      l   " + "".join("%9s"%("%.3f"%e) for e in edges[:-1]))
for L in (200,400,550,700,800,1000):
    X=kk[None,:]*x0m[:,None]
    jl=spherical_jn(L,X); jlp=spherical_jn(L,X,derivative=True)
    Do=np.trapezoid(Sm*jl,ee,axis=0)+np.trapezoid(Si*jl,ee,axis=0)+np.trapezoid(Sd*jlp,ee,axis=0)
    iL=int(np.argmin(abs(LC-L)));
    assert abs(LC[iL]-L)<=1, "l mismatch %d vs %d"%(LC[iL],L)
    Dc=np.interp(kk,qC,dC[iL])
    w=kk**(0.965-1)/kk
    po=w*Do**2; pc=w*Dc**2
    bo=np.array([np.trapezoid(po[(kk>=a)&(kk<b)],kk[(kk>=a)&(kk<b)]) for a,b in zip(edges[:-1],edges[1:])])
    bc=np.array([np.trapezoid(pc[(kk>=a)&(kk<b)],kk[(kk>=a)&(kk<b)]) for a,b in zip(edges[:-1],edges[1:])])
    bo/=bo.sum(); bc/=bc.sum()
    print("   %5d  "%L + "".join("%9.3f"%(o/c if c>1e-12 else np.nan) for o,c in zip(bo,bc)) + "   (CAMB l=%d)"%LC[iL])
