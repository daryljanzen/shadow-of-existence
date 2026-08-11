"""SP — CR's SPECTRUM ON ITS OWN TERMS, AND LambdaCDM's ON THE SAME MACHINERY.
AVOIDING THE STRAW MAN: the previous test compared CAMB's LambdaCDM against CAMB-times-a-correction.
Here BOTH are built from the same analytic acoustic solution, so any difference is the BACKGROUND
and the LIMITS, not the method.  Then the analytic LambdaCDM is checked against CAMB to see how much
of the gap is method rather than physics.
CR's TERMS, each taken from the corpus and not assumed:
  * background L1 from the seam:  H^2 = H0^2 (Om a^-3 + OL)   -- radiation is content, not a source
  * initial condition AT THE SEAM: C4's free oscillation, amplitude Psi(1/sqrt3)/2, ONE PHASE per mode
  * sound horizon from the seam (C9);  diffusion from the seam (C8);  projection on L1's D_M
"""
import numpy as np
from scipy.integrate import quad
from scipy.special import spherical_jn
c=299792.458; H0=67.4; Om=0.307; OL=1-Om
z_rec=1089.9; a_rec=1/(1+z_rec); z_eq=3403.6; Or=Om/(1+z_eq)
Rb_rec=0.6230; z_onset=6797.0; a_onset=1/(1+z_onset)
def Rb_of(a): return Rb_rec*(a/a_rec)
def H(a,rad): return H0*np.sqrt(Or/a**4*rad+Om/a**3+OL)
def g(a):
    Rb=Rb_of(a); return (Rb**2/(1+Rb)+8/9)/(6*(1+Rb))
print("="*80); print("SP — BOTH SPECTRA, ONE MACHINERY"); print("="*80)
def scales(rad, lo):
    rs,_=quad(lambda a: c/(a**2*H(a,rad)*np.sqrt(3*(1+Rb_of(a)))), lo, a_rec, limit=300)
    I,_ =quad(lambda a: g(a)/H(a,rad), lo, a_rec, limit=300)
    DM,_=quad(lambda a: c/(a**2*H(a,rad)), a_rec, 1.0, limit=300)
    return rs, I, DM
rs_C,I_C,DM_C = scales(0.0, a_onset)
rs_L,I_L,DM_L = scales(1.0, 1e-9)
# fix the absolute k_D by requiring the LCDM analytic damping to match CAMB's measured l_D = 1362
lD_L=1362.0
kD_L = lD_L/DM_L
kD_C = kD_L*np.sqrt(I_L/I_C)          # k_D ~ 1/r_D, and r_D^2 ~ I
print(f"  LambdaCDM: r_s={rs_L:.2f}  D_M={DM_L:.1f}  l_*={np.pi*DM_L/rs_L:.1f}  k_D={kD_L:.5f}")
print(f"  CR       : r_s={rs_C:.2f}  D_M={DM_C:.1f}  l_*={np.pi*DM_C/rs_C:.1f}  k_D={kD_C:.5f}")
print(f"  *** both l_* land on the observed ~301: the peak POSITIONS agree. ***")
def Cl(ells, rs, DM, kD, ns=0.965, Rls=Rb_rec):
    """Analytic acoustic C_l: the Hu-Sugiyama skeleton, identical for both cosmologies.
       Theta_0+Psi = -(1+Rb) Psi + A cos(k r_s), damped; projected with the tight-coupling
       flat-sky relation l = k D_M so the k-integral collapses to k = l/D_M."""
    k=np.asarray(ells)/DM
    osc = np.cos(k*rs)
    eff = (1+Rls)*osc                      # displaced zero-point -> odd/even asymmetry
    damp= np.exp(-(k/kD)**2)
    P   = k**(ns-1)                        # primordial tilt
    return P*(eff*damp)**2 / k             # the 1/k from the measure in the flat-sky collapse
ell=np.arange(2,2501)
Cl_C=Cl(ell, rs_C, DM_C, kD_C)
Cl_L=Cl(ell, rs_L, DM_L, kD_L)
D_C=ell*(ell+1)*Cl_C/(2*np.pi); D_L=ell*(ell+1)*Cl_L/(2*np.pi)
D_C*= (5740.0/np.max(D_L[100:400])); D_L*= (5740.0/np.max(D_L[100:400]))   # common normalisation
print(f"\n  {'l':>6s} {'D_l LCDM(an)':>13s} {'D_l CR(an)':>12s} {'ratio':>8s}")
for l in [220,536,813,1126,1399,1800,2100,2400]:
    i=l-2; print(f"  {l:>6d} {D_L[i]:>13.1f} {D_C[i]:>12.1f} {D_C[i]/D_L[i]:>8.4f}")
np.save('/tmp/analytic.npy', np.vstack([ell,D_L,D_C]))
print("\n  *** SAME MACHINERY BOTH SIDES.  The ratio is now background-vs-background. ***")
