"""Compare the two CR implementations' source at recombination, mode by mode.
Same background, same ladder -- so if the sources agree the divergence is downstream, and if they
differ the initial data is where to look.  Prints Phi_0, Psi_0 and the neutrino seed from each,
since that is the specific place the transplant could differ."""
import os, sys, numpy as np
sys.path.insert(0,'/home/claude/cr/cr_r2375/storyboard_receipts')
os.environ.update(ARM='cr', ZS='6761', ESTORE='0.5', STRIDE='2', ETAEND='760')
import HIER_photon_hierarchy as H
kk=np.array([0.0116,0.0154,0.0277,0.0387,0.0588])   # l ~ 150, 200, 360, 500, 765 at D_M=13005
E,Y,esw=H.evolve(kk)
er=H.eta_rec
Hcs=float(H.Hc_of(H.eta_onset)); Ons=float(H.On_of(H.eta_onset))
# HIER-CR's initial data, recomputed the same way evolve() does
xs=(kk/Hcs)/np.sqrt(3.0); Pl=1.0/(1.0+xs**2/3.0); Ph0=-Pl; Ps0=Ph0
seed=2.0*(Ph0-Ps0)*kk**2/(6.0*Hcs**2*Ons)
print("   HIER-CR initial data at eta_onset = %.2f  (Hc = %.6f)"%(H.eta_onset,Hcs))
print("      k        Phi_0      Psi_0     F_nu2 seed")
for j,k in enumerate(kk):
    print("     %.4f   %+.5f   %+.5f   %+.3e"%(k,Ph0[j],Ps0[j],seed[j]))
print()
# the source at recombination, HIER-CR
sgn=np.interp(er,E,Y[:,0,3])  # placeholder to force the interp path
Hcr=float(H.Hc_of(er)); Onr=float(H.On_of(er)); Ogr=float(H.Og_of(er))
print("   HIER-CR source at recombination (Theta_0 + Psi), by mode:")
print("      k        Theta_0      Psi         SW = Theta_0+Psi")
for j,k in enumerate(kk):
    th0=float(np.interp(er,E,Y[:,j,0]))          # col 0 = Theta_0 = delta_g/4
    ph =float(np.interp(er,E,Y[:,j,2]))          # col 2 = Phi
    sg =float(np.interp(er,E,Y[:,j,3]))          # col 3 = nu sigma
    sgg=float(np.interp(er,E,Y[:,j,4]))          # col 4 = photon sigma
    ps = ph - 6*Hcr**2*(Onr*sg + Ogr*sgg)/k**2
    print("     %.4f   %+.6f   %+.6f   %+.6f"%(k,th0,ps,th0+ps))
