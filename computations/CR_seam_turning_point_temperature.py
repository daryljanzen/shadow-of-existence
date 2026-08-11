#!/usr/bin/env python3
# =============================================================================
# CR seam turning-point temperature -- does complete collapse reset to primordial?
# Companion to CR_acoustic_scale_and_hubble.py; feeds P9 (CR_flatLCDM) sec.691.
# =============================================================================
#
# THE QUESTION (the horn that decides piece (i) of the acoustic remark):
#   In CR the expanding cosmos begins at the finite-curvature equatorial seam
#   (r=alpha), where the contracting and expanding Lorentzian halves of one C0
#   slice meet -- the turning point of the cycle, hence its hottest moment.
#   Does complete collapse through it reach the ~MeV scale of primordial
#   nucleosynthesis (resetting the composition to primordial), or stay cold
#   (so the light elements must be inherited)?
#
# TWO INDEPENDENT ESTIMATES OF THE SEAM TEMPERATURE -- both come out COLD:
#
#   (A) GEOMETRIC (the seam's own curvature scale).
#       Kretschmann at r=alpha:  K = 24/alpha^4 + 48 M^2/alpha^6.
#       External universe = Nariai member, alpha=1 gauge: 2M = 2/(3 sqrt3) ~ 0.385,
#       so the mass part 48 M^2 ~ 1.8 is ~13x below the de Sitter part 24.
#       Curvature length L_K = K^{-1/4} ~ 0.44 alpha ~ de Sitter (Hubble) radius
#       => no compression; the crossing sits at the Gibbons-Hawking temperature
#          T_GH = hbar c /(2 pi kB alpha) ~ 1e-30 K  (tens of orders below MeV).
#
#   (B) COMPRESSION (the matter's turning-point temperature).
#       The seam is the turning point a_min, the hottest moment (T ~ 1/a).
#       The acoustic calibration (companion script) pins z_onset ~ 6797, hence
#          T_seam = T0 (1+z_onset) ~ 1.6 eV   (~6 orders below MeV).
#
# THE INCOMPATIBILITY (why this is a definite tension, not an open temperature):
#       A turning point hot enough for BBN (T~1 MeV, z~4e9) would, through the
#       same radiation-free rate, send the sound-horizon lower limit deep and
#       give ell_A ~ 172, not the observed 301.  Acoustic scale and a
#       nucleosynthesis-capable beginning demand OPPOSITE turning-point temps.
#
# VERDICT: complete collapse through the seam does NOT reset to primordial.
#   The light elements must be inherited (processed composition -- resisted by
#   observed primordiality -- or a prior state), OR the matter sector must
#   decouple the nucleosynthesis epoch from the sound-horizon onset (unbuilt).
#   This constrains the matter sector only; the gravitational core (P1
#   no-horizons) is untouched.
# =============================================================================

import math, importlib.util
from scipy.optimize import brentq

# physical constants (SI for T_GH; eV/K for the rest)
hbar = 1.054571817e-34      # J s
cc   = 2.99792458e8         # m/s
kB_J = 1.380649e-23         # J/K
kB   = 8.617333e-5          # eV/K
T0   = 2.725                # K  (CMB today)
MeV  = 1e6                  # eV

# ---- (A) geometric: seam curvature and Gibbons-Hawking temperature ----------
twoM = 2/(3*math.sqrt(3)); M = twoM/2
K_dS, K_mass = 24.0, 48*M**2                       # units 1/alpha^4 (alpha=1 gauge)
L_K_over_alpha = (K_dS + K_mass)**-0.25
alpha = cc/ (67.4*1e3/3.086e22)                    # de Sitter radius ~ c/H0  (m)
T_GH_K = hbar*cc/(2*math.pi*kB_J*alpha)            # Gibbons-Hawking temperature (K)

print("(A) GEOMETRIC seam temperature:")
print(f"    K(seam) = 24/a^4 + 48M^2/a^6 ;  de Sitter {K_dS:.0f} vs mass {K_mass:.2f}  (~{K_dS/K_mass:.0f}x)")
print(f"    curvature length L_K ~ {L_K_over_alpha:.2f} alpha ~ de Sitter radius")
print(f"    alpha ~ c/H0 ~ {alpha:.2e} m  ->  T_GH ~ {T_GH_K:.1e} K = {T_GH_K*kB_J/1.602e-19:.1e} eV")
print(f"    -> ~{math.log10(MeV/(T_GH_K*kB)):.0f} orders below the MeV nucleosynthesis scale. No compression.\n")

# ---- (B) compression: turning-point temperature from the acoustic onset ------
spec = importlib.util.spec_from_file_location("cr", "CR_acoustic_scale_and_hubble.py")
cr = importlib.util.module_from_spec(spec); spec.loader.exec_module(cr)
_, Hcr = cr.models(67.4)
z_onset = brentq(lambda z: cr.ell_A(Hcr, z) - 301.0, 1300, 1e8)
T_seam = T0*(1+z_onset)*kB
print("(B) COMPRESSION (turning-point) temperature:")
print(f"    seam = turning point a_min (hottest moment); acoustic calibration: z_onset={z_onset:.0f}")
print(f"    T_seam = T0(1+z_onset) = {T_seam:.2f} eV  (~{MeV/T_seam:.0e} below MeV)\n")

# ---- the incompatibility -----------------------------------------------------
z_BBN = MeV/(T0*kB) - 1
print("INCOMPATIBILITY:")
for zt, lab in [(z_onset, "cold seam (acoustic-calibrated)"), (z_BBN, "BBN-hot turning point (T~1 MeV)")]:
    print(f"    z_turn={zt:>10.2e}:  ell_A = {cr.ell_A(Hcr, zt):6.1f}   ({lab})")
print("    -> a BBN-hot beginning gives ell_A~172, not 301: opposite demands. The seam does not reset.")
