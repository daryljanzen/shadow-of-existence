"""WHEN is the potential deficit laid down?  Weyl is gauge-invariant and both codes report it,
so this needs no convention matching.  Map ours/CAMB finely in conformal time, with redshift."""
import os, sys, numpy as np
sys.path.insert(0,'/home/claude/cr/cr_r2346/storyboard_receipts')
os.environ.setdefault('ESTORE','0.5'); os.environ.setdefault('STRIDE','2'); os.environ.setdefault('ETAEND','760')
import HIER_photon_hierarchy as H
import camb
kk=np.array([0.010,0.020,0.035,0.055,0.080])
E,Y,esw=H.evolve(kk)
Hc=np.array([float(H.Hc_of(e)) for e in E])
Onv=np.array([float(H.On_of(e)) for e in E]); Ogv=np.array([float(H.Og_of(e)) for e in E])
stress=6*(Hc**2)[:,None]*(Onv[:,None]*Y[:,:,3]+Ogv[:,None]*Y[:,:,4])/kk[None,:]**2
W=Y[:,:,2]-0.5*stress
p=camb.CAMBparams()
p.set_cosmology(H0=67.40, ombh2=0.02237, omch2=0.3150*0.674**2-0.02237, mnu=0.0, omk=0, tau=0.0544)
p.InitPower.set_params(As=2.1e-9, ns=0.965); p.set_for_lmax(1500, lens_potential_accuracy=0)
r=camb.get_results(p)
etas=np.linspace(1.,400.,400); ev=r.get_time_evolution(kk, etas, ['Weyl','a'])
o0=np.array([np.interp(1.,E,W[:,j]) for j in range(len(kk))]); c0=ev[:,0,0]
print("   ratio (ours/CAMB) of Weyl, each normalised at eta=1  --  gauge-invariant, no conventions")
print("      eta      z        " + "".join("%10.3f"%k for k in kk))
for et in (10.,25.,50.,75.,100.,150.,200.,250.,275.,300.,350.,400.):
    a=np.interp(et,etas,ev[0,:,1]); z=1/a-1
    rr=[(np.interp(et,E,W[:,j])/o0[j])/(np.interp(et,etas,ev[j,:,0])/c0[j]) for j in range(len(kk))]
    print("    %6.0f  %7.0f    "%(et,z) + "".join("%10.4f"%x for x in rr))
print()
print("   eta_rec = 275.5 ; the deficit's final value is what survives to late times.")
