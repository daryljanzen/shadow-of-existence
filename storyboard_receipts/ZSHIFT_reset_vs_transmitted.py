"""ZSHIFT — the transmitted-phase reading is excluded by the diffusion scale.

A.128 established that carrying the leg phase across is exactly a rescaling of the sound horizon,
r_eff = r_s + eta_leg/sqrt3, so the COMB cannot discriminate: a scale factor on r_s is degenerate
with z_onset, which sec:refit-bound fixes from the acoustic angle.  The discriminant must be a
quantity that does NOT take the same factor, and r_D is one.

  *** r_D IS COMPUTED THE WAY THE PERTURBATION RUN COMPUTES IT: ratio-anchored to LambdaCDM's
      l_D = 1362, so the Thomson microphysics cancels identically (C8's own construction). ***
      An earlier pass computed it from absolute n_b0 and got 5.18 instead of 10.88; the ratio was
      unaffected (2.016 against 2.020) but the absolute value was wrong."""
import numpy as np
from scipy.integrate import quad
c=299792.458; H0=73.; Om=0.3066; ombh2=0.0224; z_rec=1089.9; a_rec=1/(1+z_rec)
Rb_rec=31500*ombh2/(2.7255/2.7)**4/(1+z_rec)
Hub=lambda a: H0*np.sqrt(Om/a**3+(1-Om))
Hl =lambda a: 67.4*np.sqrt(0.307/(1+3403.6)/a**4+0.307/a**3+0.693)
kern=lambda a,H: ((Rb_rec*a/a_rec)**2/(1+Rb_rec*a/a_rec)+8/9)/(6*(1+Rb_rec*a/a_rec))/H(a)
Il=quad(lambda a: kern(a,Hl),1e-9,a_rec,limit=250)[0]
Dl_=quad(lambda a: c/(a**2*Hl(a)),a_rec,1.,limit=250)[0]
DM=quad(lambda a: c/(a**2*Hub(a)),a_rec,1.,limit=250)[0]
rs=lambda zs: quad(lambda a: c/(a**2*Hub(a)*np.sqrt(3*(1+Rb_rec*a/a_rec))),1/(1+zs),a_rec,limit=300)[0]
rD=lambda zs: (Dl_/1362.)*np.sqrt(quad(lambda a: kern(a,Hub),1/(1+zs),a_rec,limit=250)[0]/Il)
wr=4.15e-5
def leg(zs):
    a=1/(1+zs); Hc=a*Hub(a)/c
    return 1.0/(Hc*np.sqrt(1+(wr*(1+zs)**4/(H0/100)**2)/(Om*(1+zs)**3)))
from scipy.optimize import brentq
tgt=np.pi*DM/301.6
z_reset=brentq(lambda z: rs(z)-tgt, 1500., 60000.)
z_trans=brentq(lambda z: rs(z)+leg(z)/np.sqrt(3)-tgt, 1500., 200000.)
print("="*74); print("ZSHIFT — reset versus transmitted, judged on the diffusion scale"); print("="*74)
print(f"\n  l_* = 301.6 requires r_eff = {tgt:.2f} Mpc\n")
print(f"  {'reading':14s} {'z_onset':>8s} {'r_s':>9s} {'r_D':>8s} {'l_D':>7s} {'r_D/r_s':>9s}")
o={}
for lab,z in [('reset',z_reset),('transmitted',z_trans)]:
    a,b=rs(z),rD(z); o[lab]=b/a
    print(f"  {lab:14s} {z:>8.0f} {a:>9.2f} {b:>8.3f} {DM/b:>7.0f} {b/a:>9.5f}")
assert abs(rD(z_reset)-10.88)<0.05, f"r_D at the reset seam must reproduce the run's 10.88, got {rD(z_reset)}"
Rb=o['transmitted']/o['reset']
print(f"\n  ASSERT PASSED: r_D at the reset seam = {rD(z_reset):.3f}, matching the perturbation run.")
print(f"\n  ratio of r_D/r_s = {Rb:.4f}  ->  theta_D/theta_* would be {100*(1.1396*Rb-1):+.1f}% instead of +13.96%")
assert Rb>1.5, "the transmitted reading must give a substantially larger damping excess"
print(f"""
  *** SO THE TRANSMITTED READING PREDICTS A DAMPING EXCESS OF ORDER +130% AGAINST AN OBSERVED
      ~+14%, AND IS EXCLUDED. ***
  Note the direction: z_onset FALLS to {z_trans:.0f} rather than rising, because a later seam shortens
  r_s but lengthens eta_leg and the two trade off.
  Scope: r_D is ratio-anchored, so this is a comparison of readings and not an absolute prediction;
  and z_rec is held at {z_rec} rather than recomputed on the shifted seam.""")
