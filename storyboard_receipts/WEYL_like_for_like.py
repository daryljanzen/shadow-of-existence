import os, sys, numpy as np
sys.path.insert(0,'/home/claude/cr/cr_r2345/storyboard_receipts')
os.environ.setdefault('ESTORE','0.5'); os.environ.setdefault('STRIDE','2'); os.environ.setdefault('ETAEND','760')
import HIER_photon_hierarchy as H
import camb
kk=np.array([0.010,0.035,0.080])
E,Y,esw=H.evolve(kk)
Phi=Y[:,:,2]; sgn=Y[:,:,3]; sgg=Y[:,:,4]        # cols: 2=Phi, 3=nu sigma, 4=photon sigma
Hc=np.array([float(H.Hc_of(e)) for e in E])
Onv=np.array([float(H.On_of(e)) for e in E]); Ogv=np.array([float(H.Og_of(e)) for e in E])
stress=6*(Hc**2)[:,None]*(Onv[:,None]*sgn + Ogv[:,None]*sgg)/kk[None,:]**2
Psi = Phi - stress
Weyl_ours = 0.5*(Phi+Psi)
p=camb.CAMBparams()
p.set_cosmology(H0=67.40, ombh2=0.02237, omch2=0.3150*0.674**2-0.02237, mnu=0.0, omk=0, tau=0.0544)
p.InitPower.set_params(As=2.1e-9, ns=0.965); p.set_for_lmax(1500, lens_potential_accuracy=0)
r=camb.get_results(p)
etas=np.linspace(1.,300.,300); ev=r.get_time_evolution(kk, etas, ['Weyl'])
print("   like-for-like: OUR (Phi+Psi)/2 vs CAMB's Weyl, normalised at eta=1")
print("      eta      k=0.010        k=0.035        k=0.080")
print("               ours  CAMB     ours  CAMB     ours  CAMB      ratio 0.010 / 0.035 / 0.080")
o0=np.array([np.interp(1.,E,Weyl_ours[:,j]) for j in range(3)]); c0=ev[:,0,0]
for et in (20.,50.,100.,200.,300.):
    ro=[np.interp(et,E,Weyl_ours[:,j])/o0[j] for j in range(3)]
    rc=[np.interp(et,etas,ev[j,:,0])/c0[j] for j in range(3)]
    print("    %6.1f  "%et + " ".join("%6.3f%6.3f "%(ro[j],rc[j]) for j in range(3))
          + "   " + " ".join("%7.4f"%(ro[j]/rc[j]) for j in range(3)))
print()
print("   (compare: with our PHI against CAMB's WEYL the ratios were 0.973/0.932/0.803 at eta=50)")
