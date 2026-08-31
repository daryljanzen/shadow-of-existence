"""
Size the CR-specific Silk-damping deviation. Diffusion scale r_D = 1/k_D from
  1/k_D^2 = INT deta /(6(1+R) a n_e sigT) [16/15 + R^2/(1+R)]
computed with the SAME recombination x_e(z) (from CAMB) but two expansion rates:
  LCDM  H = H0 sqrt(Om(1+z)^3 + OL + Or(1+z)^4)   (radiation in rate)
  CR    H = H0 sqrt(Om(1+z)^3 + OL)               (geometric stacking, every epoch)
Validate the LCDM integral against CAMB's own theta_D, then read the CR/LCDM damping difference.
"""
import numpy as np, camb
from scipy.integrate import simpson
c=299792.458; sigT=6.6524587e-25*1e-4  # m^2 ->  (we'll keep cgs-consistent below)
# --- CAMB LCDM ---
pars=camb.CAMBparams(); pars.set_cosmology(H0=67.36,ombh2=0.02237,omch2=0.1200,mnu=0.06,tau=0.0544)
pars.InitPower.set_params(As=2.1e-9,ns=0.9649); pars.set_for_lmax(2700)
res=camb.get_results(pars); dp=res.get_derived_params()
H0=67.36; h=H0/100; Om=(0.02237+0.1200+0.06/93.14)/h**2; Or=res.get_Omega('photon')+res.get_Omega('neutrino'); OL=1-Om-Or
print(f"Om={Om:.4f} Or={Or:.3e} OL={OL:.4f};  CAMB: 100*theta*={dp['thetastar']:.4f} 100*theta_D={dp['thetad']:.4f} zstar={dp['zstar']:.1f} rstar={dp['rstar']:.2f} r_D~{dp['rstar']*dp['thetad']/dp['thetastar']:.2f} Mpc")

# ionization history x_e(z) from CAMB thermodynamics
zs=np.linspace(700,1700,2000)
bg=res.get_background_redshift_evolution(zs, ['x_e'], format='array')  # x_e(z)
xe=bg[:,0]
# baryon number density today (m^-3): n_b0 = ombh2 * rho_crit100 / m_p ; use n_e = xe * n_b0 (1-Yp) (1+z)^3
Yp=0.2454; m_p=1.67262e-27; rho_crit100=1.87847e-26  # kg/m^3 * h^2
n_b0=(0.02237)*rho_crit100/m_p   # m^-3 (ombh2 already includes h^2)
def integrand(z, rad):
    H=H0*np.sqrt(Om*(1+z)**3+OL+(Or*(1+z)**4 if rad else 0.0))  # km/s/Mpc
    H_si=H*1000/(3.0857e22)      # 1/s
    a=1/(1+z); R=3*0.02237/(4*2.47e-5)/(1+z)*(h**2)  # 3 rho_b/4 rho_gamma ; ombh2/ogh2
    n_e=xe*n_b0*(1-Yp)*(1+z)**3  # m^-3
    dtau=1/(a*n_e*sigT)          # m ... photon mfp * a  (conformal)
    fac=(16/15+R**2/(1+R))/(6*(1+R))
    # deta = c dz / H ; keep comoving Mpc: c[km/s]/H[km/s/Mpc]=Mpc; convert dtau (m) to Mpc
    deta_dz=c/H                   # Mpc per unit z
    dtau_Mpc=dtau/3.0857e22
    return deta_dz*fac*dtau_Mpc*1/((1+z))  # 1/k_D^2 integrand in Mpc^2 per z  (a factor 1/(1+z) from a in dtau? handled)
# integrate 1/k_D^2 from zstar to high z (diffusion accumulates to recomb)
zstar=dp['zstar']; mask=zs>=zstar
zint=zs[mask]
for rad,lab in [(True,'LCDM'),(False,'CR  ')]:
    integ=np.array([integrand(z,rad) for z in zint])
    invkD2=simpson(integ, x=zint)
    kD=1/np.sqrt(invkD2); rD=kD  # r_D = 1/k_D (comoving Mpc)
    print(f"  {lab}: r_D = 1/k_D = {rD:7.2f} Mpc")
