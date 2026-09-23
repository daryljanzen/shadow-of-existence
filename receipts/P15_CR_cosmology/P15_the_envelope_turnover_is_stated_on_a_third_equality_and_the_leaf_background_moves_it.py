#!/usr/bin/env python3
"""
RECEIPT -- P15: ** `sec:envelope` PLACES THE DRIVING ENVELOPE'S TURNOVER AT EQUALITY AND THEN PUTS
EQUALITY AT 1+z_eq = (1+z_onset)/2 = 3399, "essentially flat LCDM's".  ** THE LEAF BACKGROUND THE
PERTURBATIONS ACTUALLY RUN ON PUTS IT AT 3936. **  THOSE ARE TWO DIFFERENT NUMBERS AND THE PAPER
USES THE FIRST TO ARGUE THAT THE TURNOVER WAVENUMBER MATCHES LCDM's. **

** ⇒ ON THE LEAF BACKGROUND IT DOES NOT MATCH: k_eq IS 14.1% ABOVE THE CONTROL'S, AND PROJECTED,
ell_eq IS 7.0% ABOVE. **  The 3399 is not wrong as arithmetic -- it is the inherited datum's own
equality, (1+z_onset)/2 -- but it is not the equality of the background whose driving the envelope
argument is about, and `sec:envelope`'s "for a structural reason and not by assumption" is carried
by whichever of the two is meant.

** ⇒ AND AT THE SELF-CONSISTENT POINT THE DISAGREEMENT LARGELY GOES AWAY ON ITS OWN. **  At the
H0 = 68.60, Om = 0.2973 the leaf ruler itself prefers (r6760+cc66.2), the leaf equality is 3370 --
2.2% from the control's 3447 rather than 14.2% -- and k_eq lands within 4.0% of the control's.
*Nothing was fitted to make that happen; it follows from the H0 the BAO and the acoustic angle
both pick.*

Built r6760+cc66.5 (node 66, code seat), on `PO-13`, at node 66 (chat seat)'s work order
(message B, item 3: "k_eq and the envelope turnover wavenumber on the leaf background against the
control's 3447").

===================================================================================================
** THE THREE EQUALITIES, AND WHY THE CORPUS HAS THREE **
===================================================================================================

  3447  ** the control's **, Omega_m/Omega_r - 1 on flat LCDM at H0 = 67.40, Om = 0.3150.
  3399  ** `sec:envelope`'s **, (1+z_onset)/2 from the inherited datum -- a statement about what the
        handover DELIVERS, and the paper's own words for it are "the inherited datum places
        equality at".
  3936  ** the leaf background's **, Omega_m/Omega_r - 1 at the arm's own H0 = 73.00, Om = 0.3066 --
        which is what `ACOUSTIC_two_arm.py` integrates the perturbations on, printed in its header
        since r6760+cc66.2.

*The first two agree to 1.4% and the paper's sentence rests on that agreement.  ** The third is
14.2% from the control and 15.8% from `sec:envelope`'s own figure. **  Which one the turnover sits
at is not a matter of preference: the envelope is the DRIVING, the driving is integrated on the
leaf rate (`LEAFPERT`, the instrument's default), and the leaf rate's equality is 3936.*

  PART 1  ** THE THREE EQUALITIES AND THEIR k_eq. **
  PART 2  ** PROJECTED, ** because a wavenumber is not observable and a multipole is.
  PART 3  ** THE SELF-CONSISTENT POINT. **
  PART 4  ** WHAT IS AND IS NOT BEING SAID. **

** COMPUTES: control H0 = 67.40, Om = 0.3150; arm H0 = 73.00, Om = 0.3066; the self-consistent
   point H0 = 68.60, Om = 0.2973 (the joint DESI/theta_* fit of r6760+cc66.2); wr = 4.15e-5,
   z_rec = 1089.9, z_onset = 6797 -- the last BACKED OUT of `sec:envelope`'s own 3399 rather than
   assumed, and noted as 0.5% off the 6761 the instrument solves.  *** k_eq is computed from the background directly,
   a_eq H(a_eq)/c, and NOT from the closed form sqrt(2 Om) H0 sqrt(1+z_eq)/c, which is a
   matter-domination approximation and is 30% wrong AT equality. *** **

rc=0 on success.  Run: python3 <this file>   (numpy, scipy; ~5 s)
"""
import sys

import numpy as np
from scipy.optimize import brentq

print(__doc__.split("rc=0")[0])
fail = []
C = 299792.458
WR = 4.15e-5
Z_REC = 1089.9
A_REC = 1.0 / (1.0 + Z_REC)


def background(H0, Om, radiation_in_projection_rate):
    """The LEAF rate (radiation included) always; the PROJECTION rate is the arm's own."""
    Or = WR / (H0 / 100) ** 2
    Ol = 1.0 - Om

    def H_leaf(a):
        return H0 * np.sqrt(Om / a ** 3 + Ol + Or / a ** 4)

    def H_proj(a):
        return H0 * np.sqrt(Om / a ** 3 + Ol + (Or / a ** 4 if radiation_in_projection_rate else 0))

    z_eq = Om / Or - 1.0
    a_eq = 1.0 / (1.0 + z_eq)
    # ** k_eq FROM THE BACKGROUND, NOT FROM THE CLOSED FORM. **  a H(a)/c at a_eq, in 1/Mpc.
    k_eq = a_eq * H_leaf(a_eq) / C
    # the projection distance, on whichever rate this arm projects with
    ag = np.exp(np.linspace(np.log(A_REC), 0.0, 20001))
    D_M = float(np.trapezoid(C / (ag ** 2 * H_proj(ag)) * ag, np.log(ag)))
    return dict(Or=Or, z_eq=z_eq, k_eq=k_eq, D_M=D_M, ell_eq=k_eq * D_M, H_leaf=H_leaf)


CTL = background(67.40, 0.3150, True)
ARM = background(73.00, 0.3066, False)
SELF = background(68.60, 0.2973, False)

# sec:envelope's own figure, from its own arithmetic and not assumed
Z_ONSET_ENV = 6797.0
# The paper writes 1 + z_eq = (1 + z_onset)/2 = 3399, so z_eq = 3398.  Z_ONSET_ENV is BACKED OUT
# of that, 2*3399 - 1 = 6797, and is NOT the 6761 the instrument solves -- a 0.5% difference that
# is noted and not chased, since the sentence being weighed quotes 3399 directly.
Z_EQ_ENV = (1.0 + Z_ONSET_ENV) / 2.0 - 1.0
print("=" * 99)
print("  PART 1 -- ** THE THREE EQUALITIES AND THEIR k_eq **")
print("=" * 99)
print(f"  sec:envelope's arithmetic: 1 + z_eq = (1 + z_onset)/2 = (1 + {Z_ONSET_ENV:.0f})/2 = "
      f"{(1 + Z_ONSET_ENV) / 2:.0f},  so z_eq = {Z_EQ_ENV:.0f}")
if abs((1 + Z_ONSET_ENV) / 2 - 3399) > 1:
    fail.append(f"sec:envelope's 3399 does not reproduce from (1+{Z_ONSET_ENV:.0f})/2")
print()
print(f"  {'background':>38} {'H0':>6} {'Om':>7} {'z_eq':>7} {'k_eq 1/Mpc':>11} {'vs control':>11}")


def row(nm, d):
    print(f"  {nm:>38} {'':>6} {'':>7} {d['z_eq']:>7.1f} {d['k_eq']:>11.6f} "
          f"{d['k_eq'] / CTL['k_eq']:>10.4f}x")


print(f"  {'control (LCDM, one rate)':>38} {67.40:>6.2f} {0.3150:>7.4f} {CTL['z_eq']:>7.1f} "
      f"{CTL['k_eq']:>11.6f} {1.0:>10.4f}x")
print(f"  {'the arm, LEAF background as coded':>38} {73.00:>6.2f} {0.3066:>7.4f} "
      f"{ARM['z_eq']:>7.1f} {ARM['k_eq']:>11.6f} {ARM['k_eq'] / CTL['k_eq']:>10.4f}x")
print(f"  {'sec:envelope (inherited datum)':>38} {'--':>6} {'--':>7} {Z_EQ_ENV:>7.1f} "
      f"{'--':>11} {'--':>11}")
d_eq = ARM['z_eq'] / CTL['z_eq'] - 1
d_k = ARM['k_eq'] / CTL['k_eq'] - 1
print(f"\n  ⌗ the leaf equality is {d_eq * 100:+.1f}% on the control and "
      f"{(ARM['z_eq'] / Z_EQ_ENV - 1) * 100:+.1f}% on sec:envelope's own 3399")
print(f"  ⌗ and k_eq with it: {d_k * 100:+.1f}%")
if abs(Z_EQ_ENV / CTL['z_eq'] - 1) > 0.03:
    fail.append("sec:envelope's 3399 is NOT within 3% of the control -- its premise fails")
if abs(d_eq) < 0.10:
    fail.append(f"the leaf equality is only {d_eq * 100:.1f}% from the control -- no disagreement")

print()
print("=" * 99)
print("  PART 2 -- ** PROJECTED, because a wavenumber is not observable and a multipole is **")
print("=" * 99)
print(f"  {'background':>38} {'D_M Mpc':>9} {'ell_eq = k_eq D_M':>18} {'vs control':>11}")
for nm, d in (('control', CTL), ('the arm, as coded', ARM)):
    print(f"  {nm:>38} {d['D_M']:>9.1f} {d['ell_eq']:>18.1f} "
          f"{d['ell_eq'] / CTL['ell_eq']:>10.4f}x")
print(f"""
  ** THE PROJECTION PARTLY CANCELS IT AND DOES NOT REMOVE IT. **  k_eq is
  {d_k * 100:+.1f}% but D_M is {(ARM['D_M'] / CTL['D_M'] - 1) * 100:+.1f}% -- the arm projects on the
  radiation-free rate at a higher H0 -- so ell_eq comes out {(ARM['ell_eq'] / CTL['ell_eq'] - 1) * 100:+.1f}%.
  *A cancellation of roughly half, which is worth knowing precisely because it means the
  disagreement is smaller in the observable than in the wavenumber and is not zero in either.*""")
if abs(ARM['ell_eq'] / CTL['ell_eq'] - 1) < 0.02:
    fail.append("ell_eq agrees to 2% -- the projected statement has no content")

print()
print("=" * 99)
print("  PART 3 -- ** THE SELF-CONSISTENT POINT, AND NOTHING WAS FITTED TO REACH IT **")
print("=" * 99)
print(f"  {'background':>38} {'H0':>6} {'Om':>7} {'z_eq':>7} {'k_eq':>10} {'vs ctl':>8} "
      f"{'ell_eq':>8} {'vs ctl':>8}")
print(f"  {'control':>38} {67.40:>6.2f} {0.3150:>7.4f} {CTL['z_eq']:>7.1f} {CTL['k_eq']:>10.6f} "
      f"{1.0:>7.4f}x {CTL['ell_eq']:>8.1f} {1.0:>7.4f}x")
print(f"  {'the arm as coded (73.0, 0.3066)':>38} {73.00:>6.2f} {0.3066:>7.4f} {ARM['z_eq']:>7.1f} "
      f"{ARM['k_eq']:>10.6f} {ARM['k_eq'] / CTL['k_eq']:>7.4f}x {ARM['ell_eq']:>8.1f} "
      f"{ARM['ell_eq'] / CTL['ell_eq']:>7.4f}x")
print(f"  {'self-consistent (68.6, 0.2973)':>38} {68.60:>6.2f} {0.2973:>7.4f} "
      f"{SELF['z_eq']:>7.1f} {SELF['k_eq']:>10.6f} {SELF['k_eq'] / CTL['k_eq']:>7.4f}x "
      f"{SELF['ell_eq']:>8.1f} {SELF['ell_eq'] / CTL['ell_eq']:>7.4f}x")
print(f"""
  ** THE EQUALITY IS {SELF['z_eq']:.0f} THERE, {abs(SELF['z_eq'] / CTL['z_eq'] - 1) * 100:.1f}% FROM THE
  CONTROL INSTEAD OF {abs(d_eq) * 100:.1f}%. **  (H0, Om) = (68.60, 0.2973) is the pair the leaf ruler's
  own joint fit returns from DESI BAO, and theta_* alone returns 68.55 independently.  *So the
  equality residual that r6760+cc66.4 measured as the arm's dominant error is, on that branch,
  mostly an artefact of running the arm at an H0 its own ruler does not prefer.*
  ⚠ *Mostly, not entirely: {abs(SELF['z_eq'] / CTL['z_eq'] - 1) * 100:.1f}% is not zero, and whether the
  remainder matters is a spectrum question and not this receipt's.*""")
if abs(SELF['z_eq'] / CTL['z_eq'] - 1) > abs(d_eq):
    fail.append("the self-consistent point does NOT reduce the equality gap")

print(f"""
=================================================================================================
  PART 4 -- ** WHAT IS AND IS NOT BEING SAID **
=================================================================================================

  ⇒ ** `sec:envelope`'s sentence is arithmetically correct and rests on the equality of the
  INHERITED DATUM, {Z_EQ_ENV:.0f}.  The background the driving is integrated on has equality
  {ARM['z_eq']:.0f}.  The sentence does not say which it means, and the two differ by
  {abs(ARM['z_eq'] / Z_EQ_ENV - 1) * 100:.0f}%. **

  ⚠ ** NOT CLAIMED: that the envelope's turnover is at equality. **  That is `sec:envelope`'s
  premise and it is taken here as given; what is measured is where equality IS on each background.
  ** NOT CLAIMED: that the envelope argument fails. **  Its conclusion -- a flat envelope from the
  collapse leg's scale invariance -- rests on the closed form and not on this number.  What moves
  is the claim that the turnover WAVENUMBER matches LCDM's, which is stated on 3399 and is
  {abs(d_k) * 100:.0f}% out on 3936.
  ** NOT a spectrum result. **  The routing is to the chat seat, whose file `CR_cosmology.tex` is.
""")

print("=" * 99)
if fail:
    print("  FAILED:")
    for f in fail:
        print(f"    - {f}")
    sys.exit(1)
print("  ✓ ALL CHECKS PASSED")
print("=" * 99)
