import numpy as np
from scipy import integrate, optimize

# Constants / cosmology (Planck-ish)
c = 299792.458          # km/s
H0 = 67.4               # km/s/Mpc  (CMB/Planck normalization for the calibration & the "=standard" check)
Om = 0.3150
OL = 0.6850
Or = 9.10e-5            # photons+neutrinos, for the STANDARD calibration only
z_rec = 1089.80
# baryon loading for c_s (standard): R = 3 rho_b/(4 rho_gamma) = (3 Ob/4 Og)/(1+z)
Ob = 0.0493
Og = 5.5e-5             # photons only
def Rbar(z): return (3*Ob/(4*Og))/(1+z)
def cs_loaded(z): return c/np.sqrt(3*(1+Rbar(z)))   # km/s
cs_rel = c/np.sqrt(3)                                # clean relativistic plasma

def H_std(z):  return H0*np.sqrt(Om*(1+z)**3 + OL + Or*(1+z)**4)   # WITH radiation
def H_CR(z):   return H0*np.sqrt(Om*(1+z)**3 + OL)                 # NO radiation (CR rate)

def r_s(Hfunc, csfunc, ztop, zbot=z_rec):
    f = lambda z: csfunc(z)/Hfunc(z)
    val,_ = integrate.quad(f, zbot, ztop, limit=200)
    return val   # Mpc

print("=== CALIBRATION (machinery sanity) ===")
print(f"standard LCDM, radiation in H, baryon-loaded c_s, ztop=1e5: r_s = {r_s(H_std, cs_loaded, 1e5):7.2f} Mpc  (obs ~144-147)")
print(f"standard LCDM, radiation in H, c_s=c/sqrt3,    ztop=1e5: r_s = {r_s(H_std, lambda z: cs_rel, 1e5):7.2f} Mpc")
print()
print("=== CR rate (NO radiation), c_s=c/sqrt3 — the chimera and the z_onset map ===")
print(f"CR rate, c_s=c/sqrt3, ztop=1e6 (to beginning a->0):   r_s = {r_s(H_CR, lambda z: cs_rel, 1e6):7.2f} Mpc  <- the +74% balloon")
print(f"CR rate, c_s=c/sqrt3, ztop=z_rec (seam=recomb):       r_s = {r_s(H_CR, lambda z: cs_rel, z_rec+1e-6):7.4f} Mpc  <- ~0, must inherit from collapse side")
print()
# the observed acoustic scale fixes r_s once D_M is set. D_M robust flat-LCDM.
# target band: 144 (H0=67.4, =Planck) ... 133 (H0=73, tension dissolved)
for target in (147.0, 144.0, 133.0):
    g = lambda z_onset: r_s(H_CR, lambda z: cs_rel, z_onset) - target
    try:
        zs = optimize.brentq(g, z_rec+1.0, 5e5)
        print(f"  to hit r_s={target:6.1f} Mpc (c_s=c/sqrt3, CR rate): z_onset = {zs:8.0f}")
    except Exception as e:
        print(f"  target {target}: {e}")
print()
# show the curve
print("  r_s(z_onset), CR rate, c_s=c/sqrt3:")
for zs in (1200, 1500, 2000, 3000, 3400, 4000, 4700, 6000, 1e4, 1e5):
    print(f"    z_onset={zs:8.0f}:  r_s={r_s(H_CR, lambda z: cs_rel, zs):7.2f} Mpc")
