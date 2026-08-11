import os, sys, numpy as np
sys.path.insert(0,'/home/claude/cr/cr_r2352/storyboard_receipts')
os.environ.setdefault('ESTORE','0.5'); os.environ.setdefault('STRIDE','2'); os.environ.setdefault('ETAEND','760')
import HIER_photon_hierarchy as H
kk=np.array([0.0159,0.0387,0.0588])
E,Y,esw=H.evolve(kk)
er=H.eta_rec
np.savez(os.environ['OUTF'],
         th0=np.array([float(np.interp(er,E,Y[:,j,0])) for j in range(3)]),
         ph =np.array([float(np.interp(er,E,Y[:,j,2])) for j in range(3)]))
print("OK")
