import os, sys
import numpy as np, scipy.linalg
from scipy.optimize import minimize
from scipy.interpolate import PchipInterpolator
ROOT='/home/user/shadow-of-existence'
sys.path.insert(0, os.path.join(ROOT,'computations','planck_tt_likelihood'))
import chi2_of_spectrum as CS
R, LD = 1.0926, 1489.5783; K=R**2-1
SP=os.path.join(ROOT,'computations','beyond_the_wall','spectra')
z=np.load(os.path.join(SP,'L820_lcdm_L2512_nk800.npz'))
LS,RAW=z['ls'].astype(float),z['Dl'].astype(float)
def fish(keep):
    cov=CS.COV_TT[np.ix_(keep,keep)]
    F=scipy.linalg.cho_solve(scipy.linalg.cho_factor(cov),np.identity(int(keep.sum())))
    return 0.5*(F+F.T)
k0=np.isfinite(CS.bin_spectrum(LS,RAW)); F0=fish(k0); m0=CS.bin_spectrum(LS,RAW)[k0]
DL=RAW*float((m0@F0@CS.X_DATA[k0])/(m0@F0@m0))
WZ=np.load(os.path.join(SP,'r6897_wb_response_lcdm.npz'),allow_pickle=True)
WBS=np.array(sorted({float(k.split('__')[1]) for k in WZ.files if k.startswith('Dl__')})); WB0=WBS[len(WBS)//2]
key=lambda p,w: next(k for k in WZ.files if k.startswith(p+'__') and abs(float(k.split('__')[1])-w)<1e-12)
WL=WZ[key('ls',WB0)].astype(float); WD=np.array([WZ[key('Dl',w)].astype(float) for w in WBS])
RAT=PchipInterpolator(WBS,WD/WD[len(WBS)//2],axis=0)
def ratio(wb):
    rb=np.asarray(RAT(float(wb))); return np.interp(LS,WL,rb,left=rb[0],right=rb[-1])
keep=np.isfinite(CS.bin_spectrum(LS,DL))&(CS.BIN_LO>=100)&(CS.BIN_HI<=1758)
F=fish(keep); tgt=CS.bin_spectrum(LS,DL*np.exp(-K*(LS/LD)**2))[keep]
def at(p):
    m=CS.bin_spectrum(LS,DL*(LS/1000.0)**float(p[0])*ratio(p[1]))[keep]
    A=float((m@F@tgt)/(m@F@m)); r=tgt-A*m; return float(r@F@r)
rows=[]
for dn0 in (-0.30,-0.10,0.0,0.10):
    for wb0 in (WBS[1],WB0,WBS[3]):
        o=minimize(at,x0=[dn0,wb0],method='L-BFGS-B',bounds=[(-3.0,3.0),(WBS[0],WBS[-1])],
                   options={'ftol':1e-14,'gtol':1e-12})
        rows.append((dn0,wb0,float(o.fun),float(o.x[0]),float(o.x[1])))
print(f"{'dn0':>7}{'wb0':>12}{'fun':>22}{'dn':>14}{'wb':>14}")
for dn0,wb0,fun,dn,wb in rows:
    print(f"{dn0:>7.2f}{wb0:>12.8f}{fun:>22.12f}{dn:>14.8f}{wb:>14.8f}")
funs=[r[2] for r in rows]; dns=[r[3] for r in rows]; wbs=[r[4] for r in rows]
print()
print(f"  fun: spread {max(funs)-min(funs):.3e}  relative {(max(funs)-min(funs))/min(funs):.3e}")
print(f"  dn : min {min(dns):.8f}  max {max(dns):.8f}  spread {max(dns)-min(dns):.3e}")
print(f"  wb : min {min(wbs):.8f}  max {max(wbs):.8f}  spread {max(wbs)-min(wbs):.3e}"
      f"  = {(max(wbs)-min(wbs))/WB0*100:.4f} per cent of omega_b")
best=min(rows,key=lambda r:r[2]); print(f"  the argmin start: dn0={best[0]} wb0={best[1]:.8f} -> dn={best[3]:.8f} wb={best[4]:.8f}")
print(f"  ⇒ does the WINNER's dn/wb depend on which start wins?  dn spread {max(dns)-min(dns):.2e}, wb spread {max(wbs)-min(wbs):.2e}")
