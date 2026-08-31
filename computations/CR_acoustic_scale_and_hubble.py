#!/usr/bin/env python3
# =============================================================================
# CR acoustic scale + Hubble-tension dissolution  -- validated computation
# For c25's corpus-wide consolidation.  Slots into P9 (CR_flatLCDM) §687-689.
# =============================================================================
#
# WHAT THIS COMPUTES (and what it does NOT)
# -----------------------------------------
# The CMB acoustic angular scale, ell_A = pi * D_M / r_s, in two models:
#   (1) standard LambdaCDM  -- radiation IN the expansion rate; the sound horizon
#       r_s integrates to the beginning a->0, so r_s is PINNED (~144.6 Mpc).
#   (2) CR  -- radiation carries NO term in the rate (H = sinh^{2/3} law, dust+Lambda);
#       the beginning is the onset (r488), not a->0, so the lower
#       integration limit is a finite plasma-onset redshift z_onset: ONE early-universe
#       parameter rather than a pinned value.
# The sound speed in BOTH is the ordinary baryon-loaded fluid value
#       c_s = c / sqrt(3(1+R)),  R = 3 rho_b/4 rho_gamma  (NOT a geometric sqrt3;
#       that path was tested and closed -- the onset metric does not set c_s).
#
# SCOPE -- read before using:
#   * This is the sound-horizon / acoustic-scale leg, which is exactly where the
#     Hubble tension is diagnosed. It is NOT a full CMB power-spectrum fit.
#   * z_onset is CALIBRATED here (pinned by matching the measured ell_A), not yet
#     DERIVED. Its physical target (see RESULT 3) is the open research direction,
#     not a deficiency: a normal model parameter measured, then explained.
#
# THE INVARIANT IS Omega_m, NOT omega_m (reconciliation r959; see hubble_build/
# hubble_expansion_confrontation_v2.py and P15 sec:tensions). Radiation carries no term in the CR
# rate, so H0 factors out of both r_s and D_M and theta_*=r_s/D_M is fixed by Omega_m ALONE,
# independent of H0. The DIMENSIONLESS Omega_m is therefore the CR CMB-fixed quantity -- NOT the
# physical omega_m=Omega_m*h^2 (that is LCDM's invariant, radiation making the peaks sensitive to
# physical densities). Below, models() sets Om=wm/h^2 and the code re-matches z_onset per H0, so it
# still lands theta_* correctly at each H0 (the cancellation guarantees it); but this parametrization
# reports an H0-dependent Om (0.315 at 67.4, 0.268 at 73) and MUST NOT be extended to the low-z BAO,
# where holding omega_m fixed imports the LCDM reading and manufactures a spurious tension. The clean
# statement, and the BAO/distance-ladder confrontation, fix Omega_m~0.31 (z_onset~6774, rho_r/rho_m~2)
# H0-independent: then D_M/r_d and D_H/r_d are H0-independent too and CR fits BAO at the local H0=73
# where LCDM cannot -- the Hubble resolution across the whole expansion history, not just this angle.
#
# RESULTS (printed below; validated against Planck):
#   1. VALIDATION: standard LambdaCDM, H0=67.4 -> r_s=144.6 Mpc, ell_A=301.4
#      (Planck 2018: r_s=144.4 Mpc, ell_A~301). Pipeline trusted.
#   2. TENSION (LambdaCDM): r_s is pinned by radiation; matching ell_A forces
#      H0=67.4. Forcing the local H0=73 misses the measured acoustic scale.
#   3. DISSOLUTION (CR): on the geometric stacking rate, ell_A is matched at the
#      LOCAL H0=73 by the single onset parameter z_onset. There is no second H0.
#      The pinned onset lands at rho_r/rho_m ~ 2 (near twice matter-radiation
#      equality), stable (1.90-1.99) across H0 -- a robust physical epoch.
# =============================================================================

import numpy as np
from scipy.optimize import brentq

trapz = np.trapezoid            # (numpy>=2.0; was np.trapz)
c     = 299792.458              # km/s

# --- physical densities Omega_i h^2  (CMB-robust, independent of H0) ----------
wm = 0.1430                     # matter  (Planck)
wb = 0.02237                    # baryon
wr = 4.15e-5                    # radiation (photons + 3 neutrino species)
wg = 2.47e-5                    # photons only (for the baryon loading R)
zrec = 1090.0                   # recombination
zeq  = wm/wr - 1.0              # matter-radiation equality (H0-independent)
R0   = 3*wb/(4*wg)              # baryon loading: R(z) = R0/(1+z)

def cs(z):                                  # baryon-loaded sound speed
    return c/np.sqrt(3*(1+R0/(1+z)))

def models(H0):
    """Return (H_standard, H_CR) for a given H0, with Omega_i fixed by the
    H0-independent physical densities."""
    h = H0/100.0
    Om, Or, OL = wm/h**2, wr/h**2, 1 - wm/h**2
    H_std = lambda z: H0*np.sqrt(Om*(1+z)**3 + Or*(1+z)**4 + OL)   # radiation in rate
    H_cr  = lambda z: H0*np.sqrt(Om*(1+z)**3 + OL)                 # radiation NOT in rate
    return H_std, H_cr

def D_M(Hf, n=400000):                       # comoving distance to last scattering
    z = np.linspace(0, zrec, n)
    return trapz(c/Hf(z), z)

def r_s(Hf, z_onset, n=300000):              # comoving sound horizon; beginning=z_onset
    u = np.linspace(np.log(1+zrec), np.log(1+z_onset), n)
    z = np.exp(u) - 1
    return trapz(cs(z)/Hf(z)*(1+z), u)       # integrate in u=ln(1+z): dz=(1+z)du

def ell_A(Hf, z_onset):
    return np.pi*D_M(Hf)/r_s(Hf, z_onset)

ELL_A_OBS = 301.0                            # measured acoustic-scale multipole

# =============================================================================
if __name__ == "__main__":
    print(f"matter-radiation equality z_eq = {zeq:.0f}  (H0-independent)\n")

    # ---- 1. VALIDATION + 2. TENSION : standard LambdaCDM, r_s pinned (a->0) ----
    print("STANDARD LambdaCDM  (radiation in the rate; r_s integrated to a->0, PINNED):")
    for H0 in (67.4, 73.0):
        Hs, _ = models(H0)
        print(f"   H0={H0:>5} :  r_s={r_s(Hs,1e8):6.1f} Mpc   D_M={D_M(Hs):6.0f} Mpc   ell_A={ell_A(Hs,1e8):6.1f}")
    print("   -> r_s is the same ~144.6 Mpc either way; matching the measured ell_A=301")
    print("      FORCES H0=67.4.  The local H0=73 misses it.  That pinning is the tension.\n")

    # ---- 3. DISSOLUTION : CR, geometric stacking rate, z_onset the one parameter ----
    print("CR  (geometric stacking rate; beginning = onset; onset z_onset free):")
    for H0 in (67.4, 73.0):
        _, Hcr = models(H0)
        z_onset = brentq(lambda z: ell_A(Hcr, z) - ELL_A_OBS, 1300, 1e8)
        rr = (1+z_onset)/(1+zeq)              # rho_r/rho_m at the onset
        print(f"   H0={H0:>5} :  ell_A=301 pinned by z_onset={z_onset:6.0f}   "
              f"r_s={r_s(Hcr,z_onset):6.1f} Mpc   rho_r/rho_m@onset={rr:.2f}")
    print("   -> CR matches the measured acoustic scale at the LOCAL H0=73 with one")
    print("      onset parameter.  ONE H0, no second value to reconcile.")
    print("      The onset sits at rho_r/rho_m ~ 2 (near 2x equality), stable across H0:")
    print("      a measured parameter with a robust physical target for its cause")
    print("      (the post-collapse thermalization onset -- the open derivation).")
