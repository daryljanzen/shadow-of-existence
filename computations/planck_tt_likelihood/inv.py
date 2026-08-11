"""What damping-ratio r does Planck TT ALLOW?  Invert the question."""
import sys, numpy as np, camb, warnings, json
warnings.filterwarnings('ignore'); sys.path.insert(0,'/tmp/planckdata')
from planck_lite_py import PlanckLitePy
lik=PlanckLitePy(data_directory='/tmp/planckdata/data', year=2018, spectra='TT', use_low_ell_bins=False)
lmax=2508
x=json.load(open('lcdm.json'))['x']
H0,ombh2,omch2,As9,ns=x
p=camb.CAMBparams(); p.set_cosmology(H0=H0,ombh2=ombh2,omch2=omch2,tau=0.054)
p.InitPower.set_params(As=As9*1e-9,ns=ns); p.set_for_lmax(2600,lens_potential_accuracy=0)
res=camb.get_results(p); d=res.get_cmb_power_spectra(p,CMB_unit='muK')['total']
full=np.arange(d.shape[0]); sel=(full>1400)&(full<2400)
co=np.polyfit(full[sel].astype(float)**2, np.log(np.maximum(d[sel,0],1e-12)),1); lD=np.sqrt(-1/co[0])
ell=np.arange(2,lmax+1)
Dltt=d[2:lmax+1,0]; Dlte=d[2:lmax+1,3]; Dlee=d[2:lmax+1,1]
print("="*78); print("M6 — WHAT r DOES PLANCK TT ALLOW, at LCDM's best fit?"); print("="*78)
print(f"  l_D = {lD:.0f};  suppression = exp[-(l/l_D)^2 (r^2-1)]")
base=-2*lik.loglike(Dltt,Dlte,Dlee,ellmin=2)
print(f"  chi^2 at r=1 (no modification): {base:.1f}\n")
print(f"  {'r':>7s} {'% shift':>9s} {'chi^2':>9s} {'Delta chi^2':>12s}")
for r in [1.000,1.005,1.010,1.015,1.020,1.030,1.050,1.0904]:
    s=np.exp(-(ell/lD)**2*(r**2-1))
    ch=-2*lik.loglike(Dltt*s,Dlte,Dlee,ellmin=2)
    print(f"  {r:>7.4f} {100*(r-1):>8.2f}% {ch:>9.1f} {ch-base:>12.1f}")
print("""
  *** READ IT: at fixed LambdaCDM parameters, Planck TT admits only a FRACTION OF A PER CENT in r
      before chi^2 moves by a few.  The derived +9.04% is far outside that. ***
  (The refit relieves it substantially -- 3002 -> 397 -- but only at omega_b 14% above BBN, n_s=1.095
   and H0=78, and it still leaves Delta chi^2 ~ 191 against LambdaCDM's 206 over 215 bins.)
""")
