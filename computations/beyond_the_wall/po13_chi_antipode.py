import numpy as np
from scipy.integrate import quad

# ---- CR / LCDM background (CR shares LCDM's geometric expansion; control byte-identical) ----
c   = 299792.458            # km/s
# Planck 2018 base-LCDM (TT,TE,EE+lowE+lensing)
H0  = 67.36
Om  = 0.3153
OL  = 1.0 - Om             # flat background for the *rate*; curvature is CR's S^3 substrate, not in H(z)
# radiation (photons+neutrinos) so the LSS integral is honest
h   = H0/100.0
Ogam= 2.469e-5/h**2
Onu = Ogam*3.046*(7/8)*(4/11)**(4/3)
Or  = Ogam+Onu
Om_c= Om - Or if Om>Or else Om
zst = 1089.80              # Planck z_*

def Hz(z):
    return H0*np.sqrt(Om*(1+z)**3 + Or*(1+z)**4 + OL)   # Om already includes small Or; fine at 1e-3

# comoving distance to last scattering
D_C,_ = quad(lambda z: c/Hz(z), 0, zst, limit=200)

# ---- CR present areal radius of the S^3 from Lambda ----
# r0 = 2^(1/3) Lambda^{-1/2} sinh^{2/3}(u), u = arcsinh sqrt(OL/Om)  (corpus derived form)
Lam = 3*OL*(H0/c)**2       # 1/Mpc^2
u   = np.arcsinh(np.sqrt(OL/Om))
r0  = 2**(1/3) * Lam**(-0.5) * np.sinh(u)**(2/3)

chi = D_C/r0
print(f"H0={H0}  Om={Om}  OL={OL:.4f}  z*={zst}")
print(f"D_C (comoving dist to LSS) = {D_C:8.1f} Mpc   [corpus hardcode 13927]")
print(f"r0  (S^3 areal radius)     = {r0:8.1f} Mpc   [corpus hardcode 5064]")
print(f"chi = D_C/r0               = {chi:.4f} rad   [corpus 2.75]")
print(f"  pole  pi/2 = {np.pi/2:.4f}   antipode pi = {np.pi:.4f}")
print(f"  chi past the pole? {chi> np.pi/2}   ; rad short of antipode: {np.pi-chi:.4f}")
print()
sinchi = np.sin(chi)
mag = sinchi/chi
print(f"sin(chi) = {sinchi:.4f}   sin(chi)/chi = {mag:.4f}   magnification 1/(that) = {1/mag:.3f}x")
print()
# peak relocation: corpus flat map l = sqrt(L(L+2))*chi  vs  angular (closed) l = sqrt(L(L+2))*sin(chi)
for L in (2,):
    lflat = np.sqrt(L*(L+2))*chi
    lang  = np.sqrt(L*(L+2))*sinchi
    print(f"L={L}: corpus flat l={lflat:.3f}   angular(D_M) l={lang:.3f}")
# acoustic first peak: LCDM lands l1~220 using D_C. Under D_M it moves to:
l1_flat = 220.0
print(f"acoustic l1: flat/D_C = {l1_flat:.0f}  ->  angular/D_M = {l1_flat*mag:.1f}  (peaks move DOWN)")
print(f"first three: {220*mag:.0f}, {538*mag:.0f}, {810*mag:.0f}  (cf measured hyperspherical comb l~27-93)")
