"""PK7 — THE PEAK HEIGHTS, READ AT THE EXTREMA.  The epoch matching, assembled.
A.21 established the pieces; A.21 also found that my EXTREMUM FINDER, not the physics, put the peaks
in the wrong place.  So: evaluate at the oscillator's own extrema, k r_s = n pi.
THE CHAIN, each link derived and none guessed:
  L1 solution (derived, C11 -> constant drive):  Theta_0+Psi = -Rb Psi_s + (1+Rb)^{-1/4} A cos(k r_s)
  MATCHING (characteristic, P15 sec:coherence -- ONE datum per mode, so no independent sin term):
      A = (Theta_hat_seam + Rb_s Psi_s)(1+Rb_s)^{1/4}
  Theta_hat_seam = Psi(x_entry)/2 = 0.4835 Psi_i, THE SAME FOR EVERY k  (C4's flat envelope)
  Psi_s(k)       = the leg's residual potential ENVELOPE at the seam (one datum: amplitude, no phase)
"""
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
print("="*80); print("PK8 — HEIGHTS AT THE EXTREMA, SIGN CORRECTED"); print("="*80)
print(f"\n  z_onset={zs:.0f}  r_s={RS:.2f}  D_M={DM:.0f}  Rb_s={Rb_s:.4f}  Rb_rec={Rb_rec:.4f}  k_s={k_s:.5f}")
A_leg=-0.4835                      # C4: Theta_hat(entry) = Psi(entry)/2, and Psi is a WELL (negative)
def Psi_env(k):                    # the leg's residual: envelope, one datum, no phase
    x=(k/k_s)/np.sqrt(3); return 1.0/(1.0+x**2/3.0)
# damping (C8 + A.22: thickness cancels, so r_D alone)
g=lambda a:(Rbf(a)**2/(1+Rbf(a))+8/9)/(6*(1+Rbf(a)))
I=quad(lambda a: g(a)/H(a), a_s, a_rec, limit=300)[0]
Oml=0.307;H0l=67.4;Orl=Oml/(1+3403.6);Hl=lambda a:H0l*np.sqrt(Orl/a**4+Oml/a**3+1-Oml)
Il=quad(lambda a: g(a)/Hl(a),1e-9,a_rec,limit=300)[0]
Dl=quad(lambda a: c/(a**2*Hl(a)),a_rec,1.0,limit=300)[0]
rD=np.sqrt((Dl/1362.)**2/Il*I)
print(f"  r_D = {rD:.2f} Mpc   ->  l_D = D_M/r_D = {DM/rD:.0f}")
print(f"\n  {'n':>3s} {'l_n = n pi D_M/r_s':>19s} {'l measured':>11s} {'D_l (arb)':>12s}")
hs=[]
for n in range(1,6):
    l=n*np.pi*DM/RS; k=l/DM
    Psi=-Psi_env(k)                                  # potential well
    A=(A_leg + Rb_s*Psi)*(1+Rb_s)**0.25
    osc=-Rb_rec*Psi + (1+Rb_rec)**-0.25*A*np.cos(n*np.pi)
    D=(osc*np.exp(-(k*rD)**2))**2*l**(0.965-1)
    hs.append(D)
    meas=[220,536,813,1126,1399][n-1]
    print(f"  {n:>3d} {l:>19.1f} {meas:>11d} {D:>12.4e}")
print(f"\n  RATIOS (A_s-free):   P1/P2 = {hs[0]/hs[1]:.3f}   measured {5741/2595:.3f}")
print(f"                       P1/P3 = {hs[0]/hs[2]:.3f}   measured {5741/2544:.3f}")
print(f"                       P2/P3 = {hs[1]/hs[2]:.3f}   measured {2595/2544:.3f}")
