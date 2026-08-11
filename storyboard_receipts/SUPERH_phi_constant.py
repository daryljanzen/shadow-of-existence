"""INTERNAL TEST, no CAMB: is OUR Phi constant super-horizon, as it must be in radiation domination?
A mode with k*eta << 1 in a radiation-dominated universe has Phi = const (the growing mode).
Any drift is ours to explain."""
import os, sys, numpy as np
sys.path.insert(0,'/home/claude/cr/cr_r2346/storyboard_receipts')
os.environ.setdefault('ESTORE','0.02'); os.environ.setdefault('STRIDE','1'); os.environ.setdefault('ETAEND','760')
import HIER_photon_hierarchy as H
kk=np.array([0.0005,0.001,0.002,0.010])       # very small k: k*eta << 1 for a long while
E,Y,esw=H.evolve(kk)
Phi=Y[:,:,2]
print("   our Phi(eta)/Phi(eta_0), for modes far outside the horizon (k*eta << 1):")
print("      eta     " + "".join("   k=%.4f (k*eta=%.3f)"%(k,k*10) for k in kk))
e0=0.6
p0=np.array([np.interp(e0,E,Phi[:,j]) for j in range(len(kk))])
for et in (1.,2.,5.,10.,20.,50.,100.):
    print("    %6.1f    "%et + "".join("%22.5f"%(np.interp(et,E,Phi[:,j])/p0[j]) for j in range(len(kk))))
print()
print("   k*eta at each eta, for the smallest mode k=0.0005:")
for et in (1.,10.,100.): print("      eta=%5.0f -> k*eta = %.4f"%(et, 0.0005*et))
print()
print("   -> for k=0.0005 the mode is FAR outside the horizon at every eta shown.")
print("      Phi must be CONSTANT there in radiation domination.  Any drift is a bug or a")
print("      real feature of the background (matter is present too, which lifts Phi by 9/10 -> 1).")
