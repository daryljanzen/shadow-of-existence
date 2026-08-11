"""M3 — THE CR SPECTRUM ON A REAL BOLTZMANN BASE.
WHY THIS IS LICENSED AND THE r965 SHORTCUT WAS NOT: the trap says 'assuming the high-ell peaks equal
LambdaCDM's is precisely the unbuilt part.'  C4 DERIVED that they match -- flat envelope, turnover at
the inherited datum's own equality -- so using LambdaCDM's peaks is now a RESULT, not an assumption.
The damping is derived too (C8/C9).  Both halves come from the same place, which is the rule r1923
extracted from the trap."""
import camb, numpy as np
from scipy.integrate import quad
pars=camb.CAMBparams()
pars.set_cosmology(H0=67.4, ombh2=0.0224, omch2=0.120, tau=0.054)
pars.InitPower.set_params(As=2.1e-9, ns=0.965)
pars.set_for_lmax(2500, lens_potential_accuracy=0)
res=camb.get_results(pars); dp=res.get_derived_params()
TT=res.get_cmb_power_spectra(pars, CMB_unit='muK')['total'][:,0]; ell=np.arange(TT.size)
c=299792.458; H0=67.4; Om=(0.0224+0.120)/(H0/100)**2; OL=1-Om
z_rec=dp['zstar']; a_rec=1/(1+z_rec); Or=Om/(1+dp['zeq'])
Rb_rec=31500*0.0224/(2.7255/2.7)**4/(1+z_rec)
def Rb_of(a): return Rb_rec*(a/a_rec)
def g(a):
    Rb=Rb_of(a); return (Rb**2/(1+Rb)+8/9)/(6*(1+Rb))
def H_of(a,rad): return H0*np.sqrt(Or/a**4*rad + Om/a**3 + OL)
a_onset=1/(1+6797.0)
I_L,_=quad(lambda a: g(a)/H_of(a,1.0), 1e-9, a_rec, limit=300)
I_C,_=quad(lambda a: g(a)/H_of(a,0.0), a_onset, a_rec, limit=300)
rs_L,_=quad(lambda a: c/(a**2*H_of(a,1.0)*np.sqrt(3*(1+Rb_of(a)))), 1e-9, a_rec, limit=300)
rs_C,_=quad(lambda a: c/(a**2*H_of(a,0.0)*np.sqrt(3*(1+Rb_of(a)))), a_onset, a_rec, limit=300)
r=(np.sqrt(I_C/I_L))/(rs_C/rs_L)
print("="*78); print("M3 — THE SPECTRUM"); print("="*78)
print(f"  CAMB: z_*={z_rec:.1f}  z_eq={dp['zeq']:.1f}  r_*={dp['rstar']:.2f} Mpc  l_*={np.pi/(dp['thetastar']/100):.2f}")
print(f"  my r_s on CAMB's own background: LCDM {rs_L:.2f} (CAMB {dp['rstar']:.2f})  CR {rs_C:.2f}")
print(f"  *** theta_D/theta_* ratio = {r:.4f}  ->  {100*(r-1):+.2f}% ***")
sel=(ell>1400)&(ell<2400)
co=np.polyfit(ell[sel].astype(float)**2, np.log(np.maximum(TT[sel],1e-12)), 1)
lD=np.sqrt(-1/co[0])
print(f"  l_D read off CAMB's OWN damping envelope: {lD:.0f}   (not typed in)")
TT_CR=TT*np.exp(-(ell/lD)**2*(r**2-1))
print(f"\n  {'l':>6s} {'D_l LCDM':>11s} {'D_l CR':>11s} {'ratio':>8s}")
for l in [220,536,813,1126,1399,1800,2100,2400]:
    print(f"  {l:>6d} {TT[l]:>11.2f} {TT_CR[l]:>11.2f} {TT_CR[l]/TT[l]:>8.4f}")
print("""
*** WHAT THIS IS: a real Boltzmann LambdaCDM spectrum with a DERIVED modification applied. ***
*** WHAT IT IS NOT: a likelihood.  The Planck data are not reachable here -- cobaya installs but its
    likelihood files come from hosts outside the allowed domains -- so no chi^2 is computed and no
    verdict is drawn.  With M2 it says: the difference is large and it does not reabsorb within
    priors.  It does not say the framework is excluded, because that is a statement about data. ***
""")
print("="*78)
