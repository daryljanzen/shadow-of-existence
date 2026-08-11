"""PK9 — THE PEAK HEIGHTS, WITH THE DOUBLE-COUNT REMOVED AND READ AT THE EXTREMA.
The two errors, both mine, both now fixed:
  (1) PK7/PK8 used C4's SATURATED amplitude 0.4835 alongside an UNSATURATED Psi_s -- the same mode at
      two stages of its life.  The datum to carry is the INSTANTANEOUS Theta_hat = A_leg cos(dphi).
  (2) PK4-PK6 read the peaks with an extremum finder on a damped product, which shifts the maxima.
      Read at the oscillator's own extrema, k r_s = n pi.
CHARACTERISTIC MATCHING STANDS (P15 sec:coherence): one datum per mode, so no independent sin term."""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
c=299792.458
H0=73.0; Om=0.3066; OL=1-Om; ombh2=0.0224; z_rec=1086.4
a_rec=1/(1+z_rec); Rb_rec=31500*ombh2/(2.7255/2.7)**4/(1+z_rec)
Rbf=lambda a: Rb_rec*(a/a_rec); H=lambda a: H0*np.sqrt(Om/a**3+OL)
rs=lambda zs: quad(lambda a: c/(a**2*H(a)*np.sqrt(3*(1+Rbf(a)))), 1/(1+zs), a_rec, limit=300)[0]
DM=quad(lambda a: c/(a**2*H(a)), a_rec, 1.0, limit=300)[0]
zs=brentq(lambda z: np.pi*DM/rs(z)-301.6, 1500., 60000.)
RS=rs(zs); a_s=1/(1+zs); Rb_s=Rbf(a_s); k_s=a_s*H(a_s)/c
g=lambda a:(Rbf(a)**2/(1+Rbf(a))+8/9)/(6*(1+Rbf(a)))
I=quad(lambda a: g(a)/H(a), a_s, a_rec, limit=300)[0]
Oml=0.307;H0l=67.4;Orl=Oml/(1+3403.6);Hl=lambda a:H0l*np.sqrt(Orl/a**4+Oml/a**3+1-Oml)
Il=quad(lambda a: g(a)/Hl(a),1e-9,a_rec,limit=300)[0]
Dl=quad(lambda a: c/(a**2*Hl(a)),a_rec,1.0,limit=300)[0]
rD=np.sqrt((Dl/1362.)**2/Il*I)
print("="*80); print("PK9 — DOUBLE-COUNT REMOVED, READ AT THE EXTREMA"); print("="*80)
print(f"\n  z_onset={zs:.0f}  r_s={RS:.2f}  D_M={DM:.0f}  Rb_s={Rb_s:.4f}  Rb_rec={Rb_rec:.4f}  r_D={rD:.2f}")
x_e=1/np.sqrt(3)
Psi_exact=lambda x: np.where(np.abs(x)<1e-6,1.0,3*(np.sin(x)-x*np.cos(x))/np.maximum(np.abs(x),1e-12)**3)
A_leg=-Psi_exact(x_e)/2                       # C4, and Psi is a WELL
print(f"  A_leg (entry amplitude, C4) = {A_leg:.4f}\n")
print(f"  {'n':>3s} {'l_n':>8s} {'l meas':>8s} {'x_seam':>8s} {'Psi_s':>8s} {'D_l':>12s}")
hs=[]
for n in range(1,6):
    l=n*np.pi*DM/RS; k=l/DM
    x_s=(k/k_s)/np.sqrt(3)
    Psi=-Psi_exact(x_s)                        # exact leg residual, well
    That=A_leg*np.cos(x_s-x_e)                 # INSTANTANEOUS, one datum
    A=(That + Rb_s*Psi)*(1+Rb_s)**0.25
    osc=-Rb_rec*Psi + (1+Rb_rec)**-0.25*A*np.cos(n*np.pi)
    D=(osc*np.exp(-(k*rD)**2))**2*l**(0.965-1)
    hs.append(D)
    meas=[220,536,813,1126,1399][n-1]
    print(f"  {n:>3d} {l:>8.1f} {meas:>8d} {x_s:>8.2f} {float(Psi):>8.3f} {D:>12.4e}")
print(f"\n  RATIOS (A_s-free):")
print(f"     P1/P2 = {hs[0]/hs[1]:7.3f}   measured {5741/2595:.3f}")
print(f"     P1/P3 = {hs[0]/hs[2]:7.3f}   measured {5741/2544:.3f}")
print(f"     P2/P3 = {hs[1]/hs[2]:7.3f}   measured {2595/2544:.3f}")
