"""CAMB_absolute_kband — the anchor-free comparison (r2165).

ABSOLUTE calibration: fix the one constant relating our (Phi_i=-1, P=k^{ns-2}dk) normalisation
to CAMB's (A_s, curvature R).  Measured where both are the validated SW limit: low k, low l.
Then every comparison is ANCHOR-FREE -- no l=50 reference to move under the ISW."""
import os, numpy as np
from scipy.special import spherical_jn
os.environ['ETAEND']='3000'; os.environ['STRIDE']='8'
import HIER_photon_hierarchy as H
Z=np.load('/tmp/camb_tr.npz'); dC=Z['d'][0]; LC=Z['L']; qC=Z['q']
kk=np.array([q for q in qC if 1.5e-3<=q<=0.11])[::2]
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
def ours(L):
    X=kk[None,:]*x0m[:,None]
    jl=spherical_jn(L,X); jlp=spherical_jn(L,X,derivative=True)
    return np.trapezoid(Sm*jl,ee,axis=0)+np.trapezoid(Si*jl,ee,axis=0)+np.trapezoid(Sd*jlp,ee,axis=0)
# calibration: ratio of the BAND POWER at low l, low k (the validated SW regime)
Lc=int([x for x in LC if x>=90][0]); iC=int(np.argmin(abs(LC-Lc))); Dc=np.interp(kk,qC,dC[iC]); Do=ours(Lc)
sel=(kk>=0.004)&(kk<=0.014)
w=kk**(0.965-1)/kk
cal=np.sqrt(np.trapezoid((w*Do**2)[sel],kk[sel])/np.trapezoid((w*Dc**2)[sel],kk[sel]))
print("  calibration constant (ours/CAMB in Delta) from l=%d, k=0.004-0.014 : %.5f"%(LC[iC],cal))
print()
print("  ABSOLUTE band powers, ours/CAMB (calibrated once, NO per-row renormalisation)")
edges=np.array([0.004,0.014,0.026,0.040,0.056,0.075,0.095])
print("      l   " + "".join("%9s"%("%.3f"%e) for e in edges[:-1]))
avail=[int(x) for x in LC if 80<=x<=1100]
    for L in avail[::max(1,len(avail)//8)]:
    iL=int(np.argmin(abs(LC-L))); assert abs(LC[iL]-L)<=1
    Dcl=np.interp(kk,qC,dC[iL]); Dol=ours(L)/cal
    po=w*Dol**2; pc=w*Dcl**2
    row=""
    for a,b in zip(edges[:-1],edges[1:]):
        s=(kk>=a)&(kk<b)
        o=np.trapezoid(po[s],kk[s]); c=np.trapezoid(pc[s],kk[s])
        row+="%9.3f"%(o/c if c>1e-40 else np.nan)
    print("   %5d  "%L+row)
