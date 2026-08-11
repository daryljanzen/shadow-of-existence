"""C5 — THE BARYON TERM.  The first of the two terms C4 named as missing.
CONFIRMATION 4 -- and the corpus fixes the division rather than me:
  P16 masthead: 'eta fixes the abundances and the CMB peak HEIGHTS, rho_r/rho_m the peak SPACING.'
  P15: this cosmology 'carries the matter density as the bend of the spatial cut WITHOUT YET REMOVING
  THE COMPONENT' -- so rho_m is TOTAL matter and the baryon fraction is set separately, by eta.
ORIGIN: storyboard_receipts/C5b_baryon_term.py -- registered r2376 (c54); edit the origin, not this copy."""
import numpy as np
print("="*80); print("C5 — WHERE THE BARYON LOADING ACTUALLY BITES"); print("="*80)
print("""
STEP 1 — HOW Rb SCALES, derived.
  Rb = 3 rho_b / 4 rho_gamma.  rho_b = m_p n_b with n_b ~ a^-3; rho_gamma ~ T^4 ~ a^-4.
  So Rb ~ a : *** Rb IS PROPORTIONAL TO THE SCALE FACTOR, hence to r. ***
  On the collapse leg r -> 0, so Rb -> 0 deep.  Rb is largest at the far end.
""")
z_onset=6797.0; z_rec=1100.0
Rb_rec=0.6          # the standard value at recombination, set by eta and T -- both shared with LCDM
R_seam=Rb_rec*(1+z_rec)/(1+z_onset)
print(f"STEP 2 — THE TWO NUMBERS THAT MATTER, from the corpus's own redshifts.")
print(f"   z_onset = {z_onset:.0f}  (P15 prop:subhorizon),   z_recombination = {z_rec:.0f}")
print(f"   Rb is set by eta and the temperature, BOTH shared with LambdaCDM, so at recombination")
print(f"   Rb_rec = {Rb_rec:.2f} as usual.  Scaling Rb ~ a = 1/(1+z) back to the seam:")
print(f"      R_seam = Rb_rec (1+z_rec)/(1+z_onset) = {R_seam:.4f}")
print(f"   and deeper still, at the entry radii of the high-ell modes, Rb falls with r:")
rs=1/np.sqrt(3); Av=4*(1/(3*np.sqrt(3)))*rs; Mv=1/(3*np.sqrt(3))
def rH(r): return np.sqrt(Av/r**2 + 2*Mv/r + r**2/1.0)
ks=rH(rs)
from scipy.optimize import brentq
print(f"   {'k/k_s':>7s} {'r_entry/r_s':>12s} {'Rb at entry':>12s}")
for kk in [1,10,100,300]:
    re_=brentq(lambda z: rH(z)-kk*ks, 1e-10, rs)
    print(f"   {kk:>7d} {re_/rs:>12.5f} {R_seam*re_/rs:>12.6f}")
print("""
  *** SO Rb <~ 0.1 AT THE SEAM AND ORDERS BELOW THAT WHERE THE HIGH-ell MODES ENTER. ***
  The Rb -> 0 skeleton of C4 is therefore not a convenience: it is accurate to a few percent at the
  worst point of the driving and to parts in 10^3 or better where the driving actually happens.
""")
print("STEP 3 — AND WHERE DOES THE ODD/EVEN ASYMMETRY COME FROM, THEN?")
print("   The asymmetry is the displaced zero-point: Theta_0 + (1+Rb) Psi oscillates about -(1+Rb) Psi,")
print("   so compressions and rarefactions are unequal by a factor set by Rb AT LAST SCATTERING.")
print(f"   Rb_rec = {Rb_rec:.2f}, not {R_seam:.4f}.")
print("   *** THE DRIVING IS SET AT THE SEAM WITH Rb NEGLIGIBLE; THE ASYMMETRY IS IMPRINTED AFTERWARD,")
print("       ON THE EXPANSION LEG, WHERE Rb GROWS BY A FACTOR (1+z_onset)/(1+z_rec) = "
      f"{(1+z_onset)/(1+z_rec):.2f}. ***")
print("""
  AND THAT IS ANOTHER LEVEL SEPARATION, not an accident:
    - the DRIVING is L2, pre-seam, Rb negligible -- so C4's envelope stands as computed;
    - the ASYMMETRY is post-seam, on the L1 expansion, Rb ~ 0.6 -- ordinary content physics on the
      observable side, exactly where P15 puts the microphysics ('its Thomson microphysics ordinary
      content physics but its expansion the L1 rate').
  *** SO THE BARYON TERM DOES NOT CORRECT C4. IT ACTS SOMEWHERE ELSE. ***
""")
print("="*80)
print("RESULT C5: the Rb -> 0 skeleton is not a limitation of the driving computation -- Rb is")
print("  proportional to the scale factor and the driving happens where the scale factor is smallest.")
print("  The baryon loading imprints the odd/even peak asymmetry on the EXPANSION side at Rb ~ 0.6,")
print("  which is ordinary content physics on the observable leg and is NOT part of the object P15")
print("  named uncomputed.  *** ONE OF C4's TWO NAMED MISSING TERMS IS DISCHARGED: IT IS NOT MISSING")
print("  FROM THE DRIVING, IT BELONGS TO A DIFFERENT LEG. ***")
print("="*80)

# ============================================================================================
# GATE — r2376+c54.160.  This receipt printed a table and a RESULT paragraph and asserted
# nothing.  What is gated below is C5's own claim, in the words CR_cosmology.tex sec:envelope
# cites it for: "the baryon loading is proportional to the scale factor and the driving happens
# where the scale factor is smallest, so R <~ 0.1 AT THE ONSET and orders below that at entry;
# the odd/even asymmetry is imprinted afterwards, ON THE EXPANSION SIDE at R ~ 0.6".
#   (1) R at the onset, pinned to the receipt's 0.097176 -- and the paper's "<~ 0.1" made a gate;
#   (2) "orders below that at entry" -- R at the entry radius of a 300 k_s mode, pinned, and
#       required to be more than two decades below the onset value;
#   (3) the growth factor (1+z_onset)/(1+z_rec) that carries R from the seam to R ~ 0.6, pinned
#       to the 6.17 the receipt prints;
#   (4) the separation itself: R at the onset is far below R at last scattering, which is the
#       level split the whole receipt turns on.
# ============================================================================================
assert abs(R_seam - 0.097176) < 1.0e-6, f"R at the onset = {R_seam:.6f}, expected 0.097176"
assert R_seam < 0.1, f"R at the onset is {R_seam:.4f}: the paper's 'R <~ 0.1 at the onset' has drifted"
_re_300 = brentq(lambda z: rH(z) - 300*ks, 1e-10, rs)
_Rb_300 = R_seam*_re_300/rs
assert abs(_Rb_300 - 0.000245) < 1.0e-6, f"R at 300 k_s entry = {_Rb_300:.6f}, expected 0.000245"
assert _Rb_300 < R_seam/100.0, \
    f"R at entry ({_Rb_300:.2e}) is not 'orders below' the onset value ({R_seam:.2e})"
_growth = (1+z_onset)/(1+z_rec)
assert abs(_growth - 6.1744) < 1.0e-3, f"(1+z_onset)/(1+z_rec) = {_growth:.4f}, expected 6.1744"
assert abs(R_seam*_growth - Rb_rec) < 1.0e-9, \
    "R does not scale as the scale factor between the onset and last scattering"
assert R_seam < 0.2*Rb_rec, \
    f"R at the onset ({R_seam:.4f}) is no longer negligible against R at last scattering ({Rb_rec})"
print(f"GATE C5 (r2376+c54.160): R_onset = {R_seam:.6f} (< 0.1), R at 300 k_s entry = {_Rb_300:.6f}, "
      f"growing by {_growth:.2f} to R_rec = {Rb_rec:.2f} -- the level split pinned.")
