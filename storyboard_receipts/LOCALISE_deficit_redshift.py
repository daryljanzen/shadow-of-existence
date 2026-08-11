"""LOCALISE the deficit in redshift, now that Transfer_cdm is pinned.
Question: the T(k) shortfall at k~0.08 -- does it arise early (transfer era) or late (growth)?
Method: read delta_c(k,z) in the pinned convention at a ladder of redshifts and track the
CR-vs-LCDM ratio's k-dependence as a function of z."""
import numpy as np, camb
from camb import model
def run(H0,omch2,zs):
    p=camb.CAMBparams()
    p.set_cosmology(H0=H0, ombh2=0.02237, omch2=omch2, mnu=0.0, omk=0, tau=0.0544)
    p.InitPower.set_params(As=2.1e-9, ns=0.965)
    p.set_matter_power(redshifts=zs, kmax=2.0)
    p.NonLinear=model.NonLinear_none
    r=camb.get_results(p); tr=r.get_matter_transfer_data(); h=H0/100
    return tr.q/h, tr.transfer_data[model.Transfer_cdm-1,:,:], h
zs=[0.,0.5,1.,2.,5.,10.,30.,100.,300.,1000.]
zs=sorted(zs, reverse=True)
kh,T,h=run(67.4,0.1200,zs)
print("   delta_c ~ k^2 T ; ratio to the z=0 shape, normalised at k/h=0.01")
print("   (a pure growth factor cancels in this normalised shape; only SHAPE change shows)")
print()
print("      z      shape(k=0.05)/shape(k=0.01)   shape(0.08)/shape(0.01)   shape(0.3)/shape(0.01)")
kref=0.01
for i,zz in enumerate(zs):
    d=(kh*h)**2*T[:,i]
    f=lambda x: np.interp(x,kh,d)/np.interp(kref,kh,d)
    print("   %7.1f        %10.5f                %10.5f              %10.5f"%(zz,f(0.05),f(0.08),f(0.3)))
print()
print("   if the SHAPE is frozen after some z, the transfer era is over there and any deficit")
print("   arising later must be a growth/late effect; if it still moves, it is transfer-era.")
