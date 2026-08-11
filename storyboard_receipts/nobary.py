"""Does dropping the baryon source account for the 332 vs 150 gap?
HIER carries Obv*db in the constraint; the CR receipt structurally cannot.  Rather than rebuild
the receipt, remove the term FROM HIER and see how far the peaks move.  If they head toward 150,
the omission is the cause; if they barely move, it is not."""
import os, sys, numpy as np
sys.path.insert(0,'/home/claude/cr/cr_r2375/storyboard_receipts')
os.environ.update(ARM='cr', ZS='6761', ESTORE='0.5', STRIDE='2', ETAEND='760',
                  NOBARYGRAV=os.environ.get('NOBARYGRAV','0'))
import HIER_photon_hierarchy as H
from scipy.special import spherical_jn
NS_=0.965
kk=np.linspace(0.004,0.12,650)
E,Y,esw=H.evolve(kk)
m=E>max(esw,H.eta_rec-160.); ee=E[m]; Yv=Y[m]
g=np.array([float(H.g_of(e)) for e in ee]); tau=np.array([float(H.tau_of(e)) for e in ee])
Sm,Sd,Si,Sq=H.source_terms(ee,Yv,kk,g,tau)
eta0=H.eg[-1]
out=[]
for l in (60,80,100,120,140,160,180,200,240,280,320,360,400,450,500,560,620,700,800):
    x=kk[None,:]*(eta0-ee)[:,None]
    jl=spherical_jn(int(l),x); jlp=spherical_jn(int(l),x,derivative=True)
    xs=np.maximum(x,1e-8)
    Kq=2.0*(-3.0*jlp/xs+(3.0*l*(l+1)/(2.0*xs**2)-1.0)*jl)
    D=np.trapezoid(Sm*jl+Si*jl+Sd*jlp+(Sq*Kq if Sq is not None else 0.0),ee,axis=0)
    B=float(np.trapezoid(kk**(NS_-2.0)*D**2,kk))*l*(l+1)
    out.append((l,B))
print("   NOBARYGRAV=%s   D_l-like band power vs l:"%os.environ.get('NOBARYGRAV','0'))
for l,B in out: print("     l=%4d   %.5e"%(l,B))
b=np.array([x[1] for x in out]); ls=np.array([x[0] for x in out])
i=int(np.argmax(b)); print("   peak of this coarse scan near l = %d"%ls[i])
