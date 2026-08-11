"""WHEN does the T(k) log-slope error develop?  delta_c on BOTH sides -- like for like, valid at
every z (unlike Phi ~ delta_c/k^2, which holds only in matter domination)."""
import os, numpy as np, camb
os.environ['ESTORE']='0.5'; os.environ['STRIDE']='4'; os.environ['ETAEND']='1600'
import HIER_photon_hierarchy as H
h=0.674; zs=[0.,200.,1000.,2000.,4000.,8000.]
pars=camb.CAMBparams()
pars.set_cosmology(H0=67.40, ombh2=0.02237, omch2=0.3150*0.674**2-0.02237, mnu=0.0, tau=0.0)
pars.InitPower.set_params(As=2.1e-9, ns=0.965)
pars.set_matter_power(redshifts=zs, kmax=2.0)
r=camb.get_results(pars); mt=r.get_matter_transfer_data()
q=mt.transfer_data[0,:,0]*h
kk=np.array([0.003,0.010,0.024,0.048,0.090])
E,Y,esw=H.evolve(kk)
print("   delta_c transfer, ours vs CAMB, both normalised at k=0.003")
print("        z    eta     " + "".join("%9s"%("k=%.3f"%k) for k in kk[1:]) + "   log-slope err")
for j,z in enumerate(zs):
    a=1.0/(1+z); e=float(np.interp(a,H.ag,H.eg))
    if e<E[2] or e>E[-2]: continue
    qi=int(np.argmin(abs(E-e)))
    dc=Y[qi,:,6]/kk**2; w=dc/dc[0]
    Tc=mt.transfer_data[camb.model.Transfer_cdm-1,:,len(zs)-1-j]
    Tci=np.interp(kk,q,Tc); Tci=Tci/Tci[0]
    rat=w/Tci
    sl=np.polyfit(np.log(kk[1:]),np.log(np.abs(rat[1:])),1)[0]
    print("   %6.0f %6.0f    "%(z,E[qi]) + "".join("%9.4f"%x for x in rat[1:]) + "   %+8.4f"%sl)
