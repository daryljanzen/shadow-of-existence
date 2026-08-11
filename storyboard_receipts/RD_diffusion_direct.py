"""RD — THE DIFFUSION LENGTH, COMPUTED DIRECTLY, WITH A REAL IONISATION HISTORY.

WHY THIS EXISTS (r2120).  `LEAF_spectrum_first_principles.py` obtains r_D by ANCHORING to LambdaCDM,
  rD = (D_LCDM/1362) sqrt(I/I_LCDM),
because its integral I = int da [R^2/(1+R) + 8/9] / [6(1+R)] / H carries NO Thomson opacity.  The
anchoring supplies the missing n_e sigma_T a -- and in doing so it imposes LambdaCDM's own damping
multipole (the 1362).  The ledger's A.154 reports a direct value r_D = 7.987 Mpc which reproduces its
headline exactly, but that derivation is in no file in the bundle.  This receipt writes it.

WHAT IS COMPUTED.  The standard photon diffusion length,
    1/k_D^2 = int_0^eta  d eta' / [6(1+R) tau']  *  [ R^2/(1+R) + 8/9 ],     r_D = 1/k_D,
with the Thomson opacity tau' = n_e sigma_T a carried explicitly, n_e = x_e n_H, and x_e from a
Peebles effective three-level atom (Saha-initialised, case-B recombination, Lyman-alpha escape and
2s-1s two-photon decay).  Nothing is anchored.

THE CONTROL COMES FIRST.  The same machinery is run on LambdaCDM, where l_D is known independently:
if it does not land near the standard value the CR number means nothing.
"""
import numpy as np
from scipy.integrate import quad, solve_ivp

# --- constants (SI) ---
c_km   = 299792.458          # km/s
sigT   = 6.6524587e-29       # m^2
m_H    = 1.6737e-27          # kg
m_e    = 9.1093837e-31       # kg
k_B    = 1.380649e-23        # J/K
hbar   = 1.054571817e-34     # J s
eV     = 1.602176634e-19     # J
Mpc_m  = 3.0856775814913673e22
rho_c100 = 1.878347e-26      # kg/m^3, critical density for h=1
T0     = 2.7255              # K
B1     = 13.605693*eV        # H ground-state binding
B2     = B1/4.0              # n=2
lam_a  = 121.5682e-9         # m, Lyman-alpha
Lam2s  = 8.2245809           # s^-1, 2s->1s two-photon

def n_H0_of(ombh2, Yp):
    """Present-day hydrogen number density, m^-3."""
    return (1.0-Yp)*ombh2*rho_c100/m_H

# ---- helium: He II -> He I by Saha.  n_e = n_H (x_H + f_He x_HeII), f_He = Yp/(4(1-Yp)).
# He III is already gone by z ~ 3000 where the hydrogen history starts, so only the FIRST
# helium ionisation matters here.  Omitting it makes n_e low by ~8% between He II and H
# recombination, hence tau' low, hence 1/k_D^2 too LARGE -- too much damping (r2133).
chi_HeI = 24.58741*eV
def f_He(Yp): return Yp/(4.0*(1.0-Yp))
def x_HeII_of(z, xH, nH0, Yp):
    """Fraction of helium that is singly ionised, from Saha with the electrons hydrogen supplies."""
    T = T0*(1+z); nH = nH0*(1+z)**3; fHe = f_He(Yp)
    K = 4.0*(m_e*k_B*T/(2*np.pi*hbar**2))**1.5 * np.exp(-chi_HeI/(k_B*T))
    if K <= 0.0: return 0.0
    # x/(1-x) = K/n_e with n_e = nH (xH + fHe x)  ->  fHe nH x^2 + (xH nH + K) x - K = 0
    a = fHe*nH; b = xH*nH + K; c_ = -K
    x = (-b + np.sqrt(b*b - 4*a*c_))/(2*a) if a > 0 else -c_/b
    return float(min(max(x, 0.0), 1.0))
def xe_total(z, xH, nH0, Yp, helium=True):
    """n_e / n_H  -- the quantity the opacity actually needs."""
    if not helium: return xH
    return xH + f_He(Yp)*x_HeII_of(z, xH, nH0, Yp)

def alpha_B(T):
    """Case-B recombination coefficient, m^3/s (Pequignot fit, RECFAST fudge F=1.14)."""
    t = T/1e4
    return 1.14 * 1e-6 * 1.14e-13 * t**(-0.8) * 4.309 / (1.0 + 0.6166*t**0.5300) * t**(-0.1052)

def _alpha_B_simple(T):
    """Simpler standard fit, m^3/s: 2.6e-13 (T/1e4)^-0.8 cm^3/s with the 1.14 fudge."""
    return 1.14 * 2.6e-19 * (T/1e4)**(-0.8)

def xe_history(Hub_SI, ombh2, Yp, z_hi=3000.0, z_lo=100.0, n=4000):
    """Peebles three-level atom.  Hub_SI(z) returns H in s^-1.  Returns (z, x_e) descending in z."""
    nH0 = n_H0_of(ombh2, Yp)
    def saha(z):
        T = T0*(1+z); nH = nH0*(1+z)**3
        S = (m_e*k_B*T/(2*np.pi*hbar**2))**1.5 * np.exp(-B1/(k_B*T)) / nH
        return 2.0/(1.0+np.sqrt(1.0+4.0/S)) if S > 0 else 0.0
    def rhs(z, y):
        xe = min(max(y[0], 1e-12), 1.0)
        T = T0*(1+z); nH = nH0*(1+z)**3; H = Hub_SI(z)
        aB = _alpha_B_simple(T)
        bB = aB * (m_e*k_B*T/(2*np.pi*hbar**2))**1.5 * np.exp(-B2/(k_B*T))
        K  = lam_a**3/(8*np.pi*H)                       # Lyman-alpha escape, m^3 s
        C  = (1.0 + K*Lam2s*nH*(1-xe)) / (1.0 + K*(Lam2s+bB)*nH*(1-xe))
        return [C*(aB*nH*xe**2 - bB*(1-xe)*np.exp(-(B1-B2)/(k_B*T))) / (H*(1+z))]
    zs = np.linspace(z_hi, z_lo, n)
    s = solve_ivp(rhs, (z_hi, z_lo), [saha(z_hi)], t_eval=zs, rtol=1e-8, atol=1e-12, method='Radau')
    return s.t, np.clip(s.y[0], 1e-12, 1.0)

def r_D(Hub_kms, ombh2, Yp, z_rec, Rb_rec, label):
    """Direct diffusion length in Mpc.  Hub_kms(z) in km/s/Mpc."""
    Hub_SI = lambda z: Hub_kms(z)*1e3/Mpc_m
    zg, xeg = xe_history(Hub_SI, ombh2, Yp)
    xe_of = lambda z: float(np.interp(z, zg[::-1], xeg[::-1]))
    nH0 = n_H0_of(ombh2, Yp)
    def integrand(z):
        a  = 1.0/(1+z)
        R  = Rb_rec*a*(1+z_rec)                                  # R = 3 rho_b/4 rho_g, prop to a
        ne = xe_of(z)*nH0*(1+z)**3                               # m^-3
        tp = ne*sigT*a*Mpc_m                                     # tau' in Mpc^-1
        deta_dz = c_km/Hub_kms(z)                                # d eta/dz in Mpc
        return deta_dz * (R*R/(1+R) + 8.0/9.0) / (6.0*(1+R)*tp)
    val, err = quad(integrand, z_rec, 1e5, limit=400)
    kD = 1.0/np.sqrt(val)
    print(f"  {label:22s} x_e(z_rec)={xe_of(z_rec):.4f}   1/k_D^2={val:8.3f} Mpc^2   "
          f"r_D={1/kD if False else np.sqrt(val):7.3f} Mpc")
    return np.sqrt(val)

if __name__ == "__main__":
    print("="*84); print("RD — THE DIFFUSION LENGTH, DIRECT.  Control first."); print("="*84)

    # ---------- CONTROL: LambdaCDM (Planck 2018) ----------
    h_l, Om_l, ombh2_l, Yp_l, z_rec = 0.674, 0.315, 0.02237, 0.2454, 1089.9
    Or_l = 4.15e-5/h_l**2
    Hl = lambda z: 100*h_l*np.sqrt(Or_l*(1+z)**4 + Om_l*(1+z)**3 + (1-Om_l-Or_l))
    Rb_rec_l = 31500*ombh2_l/(T0/2.7)**4/(1+z_rec)
    rD_l = r_D(Hl, ombh2_l, Yp_l, z_rec, Rb_rec_l, "LambdaCDM control")
    DM_l = quad(lambda z: c_km/Hl(z), 0, z_rec, limit=300)[0]
    print(f"      -> l_D = D_M/r_D = {DM_l/rD_l:.0f}     (standard LambdaCDM value ~1350;"
          f" D_M={DM_l:.0f} Mpc)")

    # ---------- CR: the LEAF rate ----------
    print()
    H0_cr, x0, ombh2_cr, Yp_cr, z_rec_cr = 69.316, 1.6648, 0.02218, 0.2470, 1092.0
    Om_cr = 2/(x0**3+2); Or_cr = 4.15e-5/(H0_cr/100)**2; OL_cr = 1-Om_cr
    Hleaf = lambda z: H0_cr*np.sqrt(Or_cr*(1+z)**4 + Om_cr*(1+z)**3 + OL_cr)   # CONTENT-CARRYING
    Rb_rec_c = 31500*ombh2_cr/(T0/2.7)**4/(1+z_rec_cr)
    rD_c = r_D(Hleaf, ombh2_cr, Yp_cr, z_rec_cr, Rb_rec_c, "CR, leaf rate")

    # D_M is measured ACROSS the foliation -> the STACKING rate (radiation-free)
    al_Mpc = 16.889*306.6
    Hfol = lambda z: c_km*np.sqrt(1+2*(1+z)**3/x0**3)/al_Mpc
    DM_c = quad(lambda z: c_km/Hfol(z), 0, z_rec_cr, limit=400)[0]
    print(f"      -> l_D = D_M/r_D = {DM_c/rD_c:.0f}     (D_M={DM_c:.0f} Mpc, stacking rate)")

    print()
    print("="*84)
    print(f"  ANCHORED value in LEAF_spectrum_first_principles.py : 10.200 Mpc  (l_D=1350)")
    print(f"  LEDGER A.154's direct value                         :  7.987 Mpc")
    print(f"  THIS RECEIPT, computed with explicit opacity        : {rD_c:6.3f} Mpc")
    print("="*84)
