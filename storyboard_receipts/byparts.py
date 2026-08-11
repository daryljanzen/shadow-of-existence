"""Our source integrated BY PARTS into the j_l-only form, so it is structurally the same object as
CAMB's T_source.  No CAMB convention needed: we build the comparable object ourselves.
   Sd j_l' dη  with x=k(eta0-eta) => j_l' = -(1/k) dj_l/deta => by parts => (1/k) dSd/deta * j_l
   and Sd = g theta_b/k, so the j_l coefficient is (1/k^2) d(g theta_b)/deta.
   S_jl = g(Theta_0+Psi) + e^{-tau}(Phi'+Psi') + (1/k^2)(g theta_b)'      [+ quadrupole, omitted both sides]"""
import os, numpy as np
os.environ['ESTORE']='0.5'; os.environ['STRIDE']='1'; os.environ['ETAEND']='500'
import HIER_photon_hierarchy as H
Z=np.load('/tmp/camb_tsrc.npz'); ev=Z['ev']; ets=Z['ets']; K=Z['K']
E,Y,esw=H.evolve(K)
m=(E>170)&(E<430); ee=E[m]; Yv=Y[m]
g=np.array([float(H.g_of(e)) for e in ee]); tau=np.array([float(H.tau_of(e)) for e in ee])
Ph=Yv[:,:,2]; sgn=Yv[:,:,3]; sgg=Yv[:,:,4]
Hcv=np.array([H.Hc_of(e) for e in ee])[:,None]
Onv=np.array([H.On_of(e) for e in ee])[:,None]; Ogv=np.array([H.Og_of(e) for e in ee])[:,None]
Ps=Ph-6*Hcv**2*(Onv*sgn+Ogv*sgg)/K[None,:]**2
S_mono = g[:,None]*(Yv[:,:,0]+Ps)
S_isw  = np.exp(-tau)[:,None]*(np.gradient(Ph,ee,axis=0)+np.gradient(Ps,ee,axis=0))
S_dopp = np.gradient(g[:,None]*Yv[:,:,1], ee, axis=0)/K[None,:]**2
S = S_mono + S_isw + S_dopp
print("  OURS (by parts, j_l-only) vs CAMB T_source -- each normalised to its own peak |value|")
print("     eta       k=0.015              k=0.030")
print("              ours    CAMB         ours    CAMB")
no=[np.max(np.abs(S[:,i])) for i in range(2)]; nc=[np.max(np.abs(ev[i,:,0])) for i in range(2)]
for e in (240.,255.,265.,277.,290.,305.,330.,370.):
    q=int(np.argmin(abs(ee-e))); j=int(np.argmin(abs(ets-e)))
    print("   %6.0f   %+7.3f %+7.3f     %+7.3f %+7.3f"%(e,S[q,0]/no[0],ev[0,j,0]/nc[0],S[q,1]/no[1],ev[1,j,0]/nc[1]))
print()
print("   zero crossing (k=0.015): ours near eta=%.0f, CAMB near eta=%.0f"
      %(ee[m2][0] if len((m2:=np.where(np.diff(np.sign(S[:,0])))[0]))>0 else -1,
        ets[c2][0] if len((c2:=np.where(np.diff(np.sign(ev[0,:,0])))[0]))>0 else -1))
print("   peak eta:  ours %.0f / %.0f    CAMB %.0f / %.0f"
      %(ee[np.argmax(abs(S[:,0]))],ee[np.argmax(abs(S[:,1]))],ets[np.argmax(abs(ev[0,:,0]))],ets[np.argmax(abs(ev[1,:,0]))]))
