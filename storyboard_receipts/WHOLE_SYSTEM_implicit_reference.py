"""WHOLE-SYSTEM implicit reference (r2179): from a full-state snapshot inside tight coupling,
integrate the SAME equations with Radau -- NO switch, NO seeding, NO freeze -- straight through
recombination.  Our conventions throughout.  Compare the source terms."""
import os, numpy as np
os.environ['ESTORE']='0.5'; os.environ['STRIDE']='1'; os.environ['ETAEND']='400'; os.environ['SNAPETA']='170'
import HIER_photon_hierarchy as H
from scipy.integrate import solve_ivp
K=np.array([0.030])
E,Y,esw=H.evolve(K)
S=H.SNAPSHOT; y0=S['y'][0]; e0=S['eta']
print("   start eta=%.2f (tight=%s), NV=%d ; integrating implicitly to 340 with NO switch"%(e0,S['tight'],len(y0)))
rhs=lambda e,y: H._rhs(e, y.reshape(1,-1), K, False).ravel()   # FULL hierarchy, tight=False throughout
sol=solve_ivp(rhs,[e0,340.],y0,method='Radau',rtol=1e-8,atol=1e-14,dense_output=True)
print("   implicit run: success=%s, nfev=%d"%(sol.success,sol.nfev))
if sol.success:
    print("      eta      explicit Theta0   implicit Theta0   ratio |  explicit tb   implicit tb   ratio")
    for e in (240.,265.,277.,290.,305.):
        q=int(np.argmin(abs(E-e))); yv=sol.sol(e)
        te,ti=Y[q,0,0], yv[2]/4.0
        be,bi=Y[q,0,1], yv[7]
        print("    %6.0f   %+13.6f %+15.6f %7.4f | %+11.5f %+11.5f %7.4f"
              %(e,te,ti,te/ti if abs(ti)>1e-30 else np.nan,be,bi,be/bi if abs(bi)>1e-30 else np.nan))
