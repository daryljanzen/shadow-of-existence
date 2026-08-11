"""Does T(k) depend on LN (the neutrino truncation)?  One variable, convergence test -- cannot be
confounded by conventions, windows or backgrounds.  Compare Phi(k)/Phi(k->0) at settled eta."""
import os, numpy as np
os.environ['ESTORE']='0.5'; os.environ['STRIDE']='4'; os.environ['ETAEND']='1400'
import HIER_photon_hierarchy as H
kk=np.array([0.003,0.012,0.026,0.048,0.080])
E,Y,esw=H.evolve(kk); q=int(np.argmin(abs(E-1200.)))
Hc=float(H.Hc_of(E[q])); On=H.On_of(E[q]); Og=H.Og_of(E[q])
Ph=Y[q,:,2]; Ps=Ph-6*Hc**2*(On*Y[q,:,3]+Og*Y[q,:,4])/kk**2
w=0.5*(Ph+Ps); w=w/w[0]
print("   LN=%-4s LG=%-4s  T(k)/T(k=0.003): "%(H.LN,H.LG)+"".join("%9.5f"%x for x in w[1:]))
