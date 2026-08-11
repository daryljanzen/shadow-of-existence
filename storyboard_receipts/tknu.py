"""T(k) shape with neutrinos removed from BOTH sides, backgrounds matched.
If the 4.4% deficit vanishes -> our neutrino treatment.  If it survives -> not the neutrinos."""
import os, numpy as np, camb
os.environ['ESTORE']='0.5'; os.environ['STRIDE']='2'; os.environ['ETAEND']='500'
import HIER_photon_hierarchy as H
kk=np.array([0.003,0.008,0.012,0.018,0.026,0.038,0.055,0.080])
NEFF=float(os.environ.get('NEFF','3.046'))
pars=camb.CAMBparams()
pars.set_cosmology(H0=67.40, ombh2=0.02237, omch2=0.3150*0.674**2-0.02237, mnu=0.0, tau=0.0,
                   nnu=NEFF, num_massive_neutrinos=0)
pars.InitPower.set_params(As=2.1e-9, ns=0.965); pars.set_for_lmax(1300, lens_potential_accuracy=0)
r=camb.get_results(pars)
ev=r.get_time_evolution(kk, np.array([277.0]), ['Weyl'], lAccuracyBoost=2)[:,0,0]
E,Y,esw=H.evolve(kk); q=int(np.argmin(abs(E-277.0)))
Hc=float(H.Hc_of(E[q])); On=H.On_of(E[q]); Og=H.Og_of(E[q])
Ph=Y[q,:,2]; Ps=Ph-6*Hc**2*(On*Y[q,:,3]+Og*Y[q,:,4])/kk**2
w=0.5*(Ph+Ps); rr=w*kk**2/ev; rr=rr/rr[0]
print("   N_eff=%.4f   ours*k^2/CAMB, normalised at k=0.003"%NEFF)
for a,b in zip(kk,rr): print("      k=%.4f   %.4f"%(a,b))
print("   spread: %.1f%%"%(100*(rr.max()-rr.min())/rr.mean()))
