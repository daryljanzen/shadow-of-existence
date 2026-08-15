"""C10 — THE HIGH-ELL RATIO, ASSEMBLED FROM DERIVED PIECES ONLY.
Inputs, all derived in C4/C7a/C8/C9 except H0 and Omega_m, which are observations:
  * driving envelope flat above ~10 k_s, turning over at the inherited datum's own equality;
  * r_s matched (+0.76%);  r_D +8.97%;  theta_D/theta_* +8.16%.
** CORRECTED c54.223 (`L-557`).  This file read theta_D/theta_* = +9.26% and the paper printed the
** rounded r = 1.093 -- both inherited the x_e non-cancellation r2753 found.  r2755 corrected the
** PAPER's sentence (9.4% -> 8.2%) and stopped there: `sec:envelope-consequence`'s r, one paragraph
** later, is the SAME quantity and still read 1.093, as did this file and twelve other receipts.
**   ⇒ *** A correction that stops at the sentence leaves the number the sentence DEFINES. ***
** The value here is now P15_damping_ratio_clean's direct computation, 1.0816, which is what the
** corrected paper prints and what C46 brackets at +7.65%..+8.24%.
l_D = D_M/r_D, so D_M is needed for an ABSOLUTE multipole -- and D_M is the same integral again.
ORIGIN: storyboard_receipts/C10_highl_ratio.py -- registered r2376 (c54); edit the origin, not this copy."""
import numpy as np
from scipy.integrate import quad
print("="*80); print("C10 — THE RATIO, AND WHERE IT SITS IN MULTIPOLE"); print("="*80)
Om,OL,H0,c = 0.307,0.693,67.4,299792.458
z_rec,z_onset = 1100.0,6797.0
a_rec,a_onset = 1/(1+z_rec), 1/(1+z_onset)
ratio_rec=2.0*(1+z_rec)/(1+z_onset); Or=Om*ratio_rec*a_rec; Rb_rec=0.6
def Rb_of(a): return Rb_rec*(a/a_rec)
def H_CR(a): return H0*np.sqrt(Om/a**3+OL)
def H_LC(a): return H0*np.sqrt(Or/a**4+Om/a**3+OL)
print("\nSTEP 1 — D_M, the comoving distance to last scattering.  SAME integral, run outward.")
def DM(H):
    f=lambda a: c/(a**2*H(a))
    v,_=quad(f, a_rec, 1.0, limit=400); return v
DM_CR, DM_LC = DM(H_CR), DM(H_LC)
print(f"   D_M(CR)   = {DM_CR:8.1f} Mpc")
print(f"   D_M(LCDM) = {DM_LC:8.1f} Mpc      (they differ only by the radiation term, tiny after z_rec)")
print(f"   ratio = {DM_CR/DM_LC:.6f}  -- *** effectively identical, as P15 says: D_M is the COMMON map ***")
print("\nSTEP 2 — l_* AND l_D, ABSOLUTE, FROM DERIVED r_s AND r_D.")
def rs(H, lo):
    f=lambda a: c/(a**2*H(a)*np.sqrt(3*(1+Rb_of(a))))
    v,_=quad(f, lo, a_rec, limit=400); return v
rs_CR, rs_LC = rs(H_CR,a_onset), rs(H_LC,1e-9)
print(f"   l_* = pi D_M / r_s :   CR {np.pi*DM_CR/rs_CR:7.1f}    LCDM {np.pi*DM_LC/rs_LC:7.1f}"
      f"    (observed ~ 301)")
# r_D absolute needs the Thomson constant; take l_D from the DERIVED ratio anchored on LCDM's observed value
lD_LC_obs = 1400.0    # an OBSERVED damping multipole for LCDM, used only as an anchor
th_ratio = 1.0816     # ** CORRECTED c54.223: P15_damping_ratio_clean's direct r_D/r_s, and what
                     # ** the corrected paper prints.  Was 1.0926 (an r_D that did not cancel x_e).
lD_CR = lD_LC_obs/th_ratio
print(f"\n   theta_D/theta_* is {100*(th_ratio-1):+.2f}% larger (DERIVED, C9), and theta_* is matched,")
print(f"   so l_D(CR) = l_D(LCDM)/{th_ratio:.4f} = {lD_CR:.0f}  against LCDM's {lD_LC_obs:.0f}.")
print("   (l_D(LCDM) is taken from observation as an anchor -- the RATIO is what is derived.)")
print("\nSTEP 3 — THE POWER RATIO.  Parameter-free in units of l_D.")
print(f"   C_l(CR)/C_l(LCDM) = exp[ -(l/l_D)^2 (r^2 - 1) ],  r = {th_ratio:.4f},  r^2-1 = {th_ratio**2-1:.4f}")
print(f"   {'l/l_D':>7s} {'ratio':>9s} {'  l (if l_D=1400)':>18s}")
for x in [0.25,0.5,0.75,1.0,1.25,1.5,1.75]:
    print(f"   {x:>7.2f} {np.exp(-x**2*(th_ratio**2-1)):>9.4f} {x*lD_LC_obs:>18.0f}")
print("""
  *** THE SHAPE OF THE PREDICTION, stated as what it is. ***
  A smooth, monotonic suppression that is negligible below l ~ l_D/2 and reaches tens of percent
  beyond it.  It has NO free parameter: the exponent is fixed by theta_D/theta_*, which was derived
  from the inherited datum and the level assignment alone.
""")
print("  AND WHAT IT IS NOT:")
print("   - it is NOT a peak-height change: the envelope tracks (C4) and the positions match (C9);")
print("   - it is NOT reabsorbable by omega_b: r_D ~ omega_b^-0.31, and the corpus checked that;")
print("   - it is NOT the l_D=1400 number: that is only the anchor turning l/l_D into a multipole.")
print("="*80)

# ============================================================================================
# GATE — r2376+c54.160.  This receipt printed the paper's headline high-ell numbers and asserted
# nothing.  It is one of the files whose figures the c54.155 audit corrected in
# CR_cosmology.tex, so the paper's CURRENT sentence is pinned alongside the receipt's own output.
#
# CR_cosmology.tex sec:envelope-consequence, as it reads NOW: "... and ell_* = pi D_M/r_s = 302.2
# against the measured ~301", and "C_l(CR)/C_l(LCDM) = exp[-(l/l_D)^2 (r^2-1)] with
# r = theta_D/theta_* = 1.082 ... so the ratio is 0.84 at l_D and 0.68 at 1.5 l_D."
#
# NOTE, recorded r2376+c54.160 and NOW RESOLVED: th_ratio was HARDCODED 1.0926 with the comment
# "DERIVED in C9", while C9 itself produced 1.0941 -- and the note said the discrepancy was
# "recorded and not re-litigated here".
#   ⇒ ** BOTH were wrong in the same direction and for the same reason: they divide an r_D that
#     carries the x_e non-cancellation r2753 found. **  r2755 corrected the PAPER's preceding
#     sentence and this number, one paragraph later, is the same quantity and was left behind.
# *** AND THE GATE DID NOT NOTICE, BECAUSE THE GATE IS WHAT HELD THEM TOGETHER. ***  It pinned this
# file's th_ratio against the paper's printed r, so the two "could not drift apart" -- and they did
# not.  They were consistent with each other and both wrong, while the sentence eight lines earlier
# in the same paper said otherwise.  ** A consistency check binds two things to each other and says
# nothing about either. **
# ============================================================================================
_l_star_CR = np.pi*DM_CR/rs_CR
_l_star_LC = np.pi*DM_LC/rs_LC
assert abs(DM_CR - 14079.9) < 0.1, f"D_M(CR) = {DM_CR:.1f} Mpc, expected 14079.9"
assert abs(DM_LC - 14010.2) < 0.1, f"D_M(LCDM) = {DM_LC:.1f} Mpc, expected 14010.2"
assert abs(DM_CR/DM_LC - 1.004976) < 1.0e-6, \
    f"D_M is no longer the common map: ratio {DM_CR/DM_LC:.6f}, expected 1.004976"
# ell_*: the paper's 302.2, and the observed ~301 it is held against.
assert abs(_l_star_CR - 302.2) < 0.05, \
    f"ell_*(CR) = {_l_star_CR:.2f}; CR_cosmology.tex sec:envelope-consequence says 302.2"
assert abs(_l_star_LC - 302.8) < 0.05, f"ell_*(LCDM) = {_l_star_LC:.2f}, expected 302.8"
assert abs(_l_star_CR - 301.0) < 2.0, \
    f"ell_*(CR) = {_l_star_CR:.2f} is no longer within 2 of the measured ~301"
assert abs(rs_CR - 146.36) < 0.01, f"r_s(CR) = {rs_CR:.2f} Mpc, expected 146.36"
assert abs(rs_LC - 145.38) < 0.01, f"r_s(LCDM) = {rs_LC:.2f} Mpc, expected 145.38"
# the ratio the whole prediction hangs on, and the paper's rounded r = 1.093.
assert abs(th_ratio - 1.082) < 0.001, \
    (f"this receipt's theta_D/theta_* is {th_ratio:.4f} but CR_cosmology.tex "
     f"sec:envelope-consequence prints r = 1.082")
assert abs(th_ratio**2 - 1 - 0.169859) < 1.0e-6, \
    f"the damping exponent r^2-1 = {th_ratio**2-1:.6f}, expected 0.169859"
assert abs(lD_CR - 1294.38) < 0.01, f"l_D(CR) = {lD_CR:.3f}, expected 1294.38 (= 1400/{th_ratio:.4f})"
# the two suppression figures the paper quotes.
assert abs(np.exp(-1.0**2*(th_ratio**2-1)) - 0.8438) < 1.0e-4, \
    (f"C_l ratio at l_D is {np.exp(-(th_ratio**2-1)):.4f}; CR_cosmology.tex says 0.84")
assert abs(np.exp(-1.5**2*(th_ratio**2-1)) - 0.6824) < 1.0e-4, \
    (f"C_l ratio at 1.5 l_D is {np.exp(-2.25*(th_ratio**2-1)):.4f}; CR_cosmology.tex says 0.68")
print(f"GATE C10 (r2376+c54.160): ell_*(CR) = {_l_star_CR:.2f}, r_s(CR) = {rs_CR:.2f} Mpc, "
      f"r = {th_ratio:.4f}, C_l ratio {np.exp(-(th_ratio**2-1)):.4f} at l_D and "
      f"{np.exp(-2.25*(th_ratio**2-1)):.4f} at 1.5 l_D -- pinned against CR_cosmology.tex.")
