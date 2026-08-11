"""ABSOLUTE calibration: fix the one constant relating our (Phi_i=-1, P=k^{ns-2}dk) normalisation
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
Sm,Sd,Si,Sq = H.source_terms(ee, Yv, kk, g, tau)   # r2196: the MODULE's assembly, knobs honoured
if Sq is None: Sq=np.zeros_like(Sm)
x0m=H.eta_0-ee
QF=float(os.environ.get('QKF','1.0'))
def ours(L):
    X=kk[None,:]*x0m[:,None]
    jl=spherical_jn(L,X); jlp=spherical_jn(L,X,derivative=True); Xs=np.maximum(X,1e-8)
    K=QF*(-3.0*jlp/Xs+(3.0*L*(L+1)/(2.0*Xs**2)-1.0)*jl)
    return np.trapezoid(Sm*jl+Si*jl+Sd*jlp+Sq*K,ee,axis=0)
# calibration: ratio of the BAND POWER at low l, low k (the validated SW regime)
Lc=int([x for x in LC if x>=90][0]); iC=int(np.argmin(abs(LC-Lc))); Dc=np.interp(kk,qC,dC[iC]); Do=ours(Lc)
sel=(kk>=0.004)&(kk<=0.014)
w=kk**(0.965-1)/kk
cal=np.sqrt(np.trapezoid((w*Do**2)[sel],kk[sel])/np.trapezoid((w*Dc**2)[sel],kk[sel]))
print("  calibration constant (ours/CAMB in Delta) from l=%d, k=0.004-0.014 : %.5f"%(LC[iC],cal))
print()
print("  ABSOLUTE band powers, ours/CAMB (calibrated once, NO per-row renormalisation)")
edges=np.linspace(0.016,0.046,16)
print("      l   " + "".join("%8s"%("%.3f"%e) for e in edges[:-1]))
avail=[int(x) for x in LC if 80<=x<=900]
for L in avail[::max(1,len(avail)//4)]:
    iL=int(np.argmin(abs(LC-L))); assert abs(LC[iL]-L)<=1
    Dcl=np.interp(kk,qC,dC[iL]); Dol=ours(L)/cal
    po=w*Dol**2; pc=w*Dcl**2
    row=""
    for a,b in zip(edges[:-1],edges[1:]):
        s=(kk>=a)&(kk<b)
        o=np.trapezoid(po[s],kk[s]); c=np.trapezoid(pc[s],kk[s])
        row+="%8.3f"%(o/c if c>1e-40 else np.nan)
    print("   %5d  "%L+row)
