"""Our transfer against CAMB's Transfer_cdm -- an INDEPENDENT output from Weyl, with its
normalisation verified (flat at low k).  In MD, Phi ~ delta_m/k^2, so ours*k^2 is the analogue.
CAMB's grid is k/h, so k = q*h."""
import os, numpy as np, camb
os.environ['ESTORE']='0.5'; os.environ['STRIDE']='4'; os.environ['ETAEND']='1600'
import HIER_photon_hierarchy as H
h=0.674
pars=camb.CAMBparams()
pars.set_cosmology(H0=67.40, ombh2=0.02237, omch2=0.3150*0.674**2-0.02237, mnu=0.0, tau=0.0)
pars.InitPower.set_params(As=2.1e-9, ns=0.965)
pars.set_matter_power(redshifts=[0.], kmax=2.0)
r=camb.get_results(pars); mt=r.get_matter_transfer_data()
q=mt.transfer_data[0,:,0]*h                       # -> 1/Mpc
Tc=mt.transfer_data[camb.model.Transfer_cdm-1,:,0]; Tc=Tc/Tc[0]
kk=np.array([0.003,0.006,0.010,0.016,0.024,0.034,0.048,0.068,0.090])
E,Y,esw=H.evolve(kk); qi=int(np.argmin(abs(E-1200.)))
Hc=float(H.Hc_of(E[qi])); On=H.On_of(E[qi]); Og=H.Og_of(E[qi])
Ph=Y[qi,:,2]; Ps=Ph-6*Hc**2*(On*Y[qi,:,3]+Og*Y[qi,:,4])/kk**2
w=0.5*(Ph+Ps); w=w/w[0]
Tci=np.interp(kk,q,Tc); Tci=Tci/Tci[0]
print("   transfer, ours vs CAMB's Transfer_cdm (independent of Weyl), both normalised at k=0.003")
print("        k        ours      CAMB      ratio")
for i,k in enumerate(kk):
    print("   %8.4f  %8.4f  %8.4f   %7.4f"%(k,w[i],Tci[i],w[i]/Tci[i]))
