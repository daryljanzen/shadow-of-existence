"""VALID2 — does the hierarchy reproduce the EXACT radiation-era potential decay?

Damping is validated and the peak positions are right, and the decomposition shows the third peak is
91% monopole -- so a 64% power deficit at P3 means the monopole amplitude at high k is too small.  The
natural origin is RADIATION DRIVING: modes entering the horizon before equality see Phi decay, and that
decay is what boosts the acoustic amplitude.

THE BENCHMARK IS ANALYTIC.  For a single radiation fluid, adiabatic, the exact super/sub-horizon
solution is
        Phi(eta) / Phi(0) = 3 [ sin x - x cos x ] / x^3 ,      x = k eta / sqrt(3),
valid while radiation dominates (eta << eta_eq ~ 110 Mpc here).  Neutrino free-streaming modifies this
at the ~10% level, so agreement is expected to be good but not exact; a LARGE discrepancy would be a
bug, and a small one would eliminate driving as the cause.
"""
import os, numpy as np
os.environ.setdefault('NS1','4000'); os.environ.setdefault('NS2','800')
os.environ['ESTORE']='0.5'; os.environ['STRIDE']='1'
import HIER_photon_hierarchy as H

kk=np.array([0.0159,0.0386,0.0586,0.12])
E,Y,esw=H.evolve(kk)
Ph=Y[:,:,6]/(-1.0)
def exact(x): return 3.0*(np.sin(x)-x*np.cos(x))/x**3

print("="*80)
print("RADIATION-ERA POTENTIAL DECAY   (eta_eq ~ 110 Mpc; benchmark valid for eta << that)")
print("="*80)
print("   eta    | mode k    x=k*eta/sqrt3 |  hierarchy   exact    ratio")
for et in (3.,6.,12.,25.,50.,80.):
    j=int(np.argmin(abs(E-et)))
    for i,k in enumerate(kk):
        x=k*E[j]/np.sqrt(3)
        if x<0.25: continue
        print("  %6.1f  | %7.4f   %8.3f      | %+8.4f  %+8.4f   %6.3f"
              %(E[j],k,x,Ph[j,i],exact(x),Ph[j,i]/exact(x) if abs(exact(x))>1e-3 else float('nan')))
    print()
