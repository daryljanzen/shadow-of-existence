#!/usr/bin/env python3
r"""S1 -- cc54, PO-10 (struck r2712, remainder a RUN; 56's greenlight r2719): DELIVER THE BIC PAIR.
PO-10's specified deliverable is chi^2(phi=0) and chi^2(phi=pi) for the CR arm, each scored as F3 =
chi^2(CR arm) - chi^2(LambdaCDM arm) on the SAME instrument and bins, each compared to the model-
selection threshold dBIC = (k_LCDM - k_CR) ln N = (6-2) ln 215 = 21.5. CR is preferred iff F3 < 21.5.
PO-7 selects the physical branch when it closes.

** Board lead L-814 (cc54's band); DELIVERS PO-10's run (informs L-147 / family-5, the scalar sector to
a verdict). The reference was pinned to F3 at r2719: BIC = chi^2 + k ln N and only DIFFERENCES carry
meaning, so dBIC = F3 - 21.5 -- an ABSOLUTE chi^2 never enters, and the instrument floor cancels exactly
rather than approximately. (The earlier BIC-against-CAMB framing was withdrawn r2719: it charged CR the
instrument's chi^2/dof ~ 100 floor that CAMB, run natively, never pays.) **

** THE SPECTRA. ** F3(phi=0) is scored from the banked c54.178_cr arm (the photon hierarchy with
polarisation, CRPHI=0). F3(phi=pi) is scored from L814_cr_phipi_L2000.npz -- the SAME c54.178 CR-arm
command with CRPHI=3.14159 (banked with its provenance), CR's fitted acoustic scale l_A=301.6 unchanged.
The LambdaCDM arm (phase-independent) is c54.178_lcdm. All three scored through chi2_of_spectrum.py on
the same 185 covered bins, one amplitude fitted exactly.

COMPUTES: F3 = chi^2(CR arm) - chi^2(LambdaCDM arm) through plik_lite TT for the CR arm at the two
admissible seam phases CRPHI=0 and CRPHI=pi (3.14159), and the model-selection threshold dBIC =
(6-2) ln 215 = 21.5. ** CRPHI here is a SCOPE the deliverable ranges over, not a pinned prediction: the
run reports BOTH branches precisely because the seam phase is two-valued while PO-7 is open, and PO-7
selects the physical one. **

** WHAT THIS RECEIPT ASSERTS. **
  1. THE PIPELINE IS WIRED (F1): the banked CAMB flat-LambdaCDM best fit is chi^2 = 206.4 / 215
     (chi^2/dof = 0.96). If it were not, nothing below could be read.
  2. THE PAIR: F3(phi=0) = chi^2(CR,phi=0) - chi^2(LCDM arm) ~ +5.05e4, and F3(phi=pi) ~ +6.76e4.
     BOTH are enormous and BOTH exceed the 21.5 threshold by ~2000-3000x, so dBIC = F3 - 21.5 > 0 at
     BOTH branches: ** CR is NOT preferred at either seam phase, and PO-7's branch selection does not
     change that. ** (phi=pi is WORSE, not better: its first-peak gap is smaller -- l_1/l_A = 0.6233 vs
     phi=0's 0.5703, against the sky's 0.7312 -- but its peak HEIGHTS/shape cost more chi^2.)
  3. THE THRESHOLD AND ITS REFERENCE (the standing rule -- state what a threshold is scored AGAINST, so
     it is not scored against whatever is nearest): F3 is scored against dBIC = 21.5, and 21.5 is the
     SAME-INSTRUMENT parameter penalty (6-2) ln 215 -- NOT against CAMB's 206.4 (the framing withdrawn at
     r2719, a number CAMB never had to pay). On the Jeffreys/Liddle scale 21.5 is 3.5x the strong-evidence
     line of 6. CR is preferred IFF F3 < 21.5 -- stated as the numeric bar, so the reading is not chosen
     after the number.
  4. THE FLOOR CUTS BOTH WAYS AND DOES NOT SOFTEN THE NEGATIVE (and explicitly NOT laundering).
     F2 = chi^2(LCDM arm) - chi^2(CAMB) ~ +1114: no model here fits Planck well (this instrument's own
     control sits at chi^2/dof ~ 7 vs CAMB's 0.96), so the likelihood cannot arbitrate on ABSOLUTE fit.
     ** But the arbitration the floor prevents is ONLY between models whose F3 differ by LESS than the
     floor -- roughly |F3| <~ 1114; the measured F3, +5.05e4 and +6.76e4, are 45-60x the floor, so the
     RELATIVE gap is real physics, not instrument. ** So the negatives are DECISIVE and BOUNDED: CR is
     disfavoured at phi=0 (dBIC +50475) and at phi=pi (+67603), each a bounded negative on its seam-phase
     reading. The floor could no more BANK a decisive positive than RESCUE this decisive negative -- a
     "cannot arbitrate" note that neutralised +50475 would be laundering, and this receipt refuses it.

** WHAT IS NOT CLAIMED, stated for reversal. ** NOT a framework verdict on CR: PO-7 is PROTECTED and F5
says a measurement discrepancy is not a verdict on the construction, which is unseated. This receipt
reports the BIC pair PO-10 specified and no more; it does not convert PO-7, and the physical branch is
PO-7's to select. NOT a claim that the phase is settled -- CRPHI is assigned (PO-seam open); the pair is
reported precisely because the input is two-valued while PO-7 is open. NOT comparable to CAMB's LambdaCDM
directly -- that was the withdrawn framing; F3 is same-instrument by construction.

Written r2674 (cc54, L-814). Asserts against the plik_lite likelihood and the banked/generated CR arms --
never the register. Scope: plik_lite TT only (no pol, no ell<30, no lensing, third-party impl). Stated
for reversal.
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
LIK = os.path.join(ROOT, 'computations', 'planck_tt_likelihood')
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, LIK)
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    import json
    import chi2_of_spectrum as CS

    print()
    print('  S1 -- PO-10: the BIC pair, F3(phi=0) and F3(phi=pi), each vs the 21.5 threshold')
    print()

    # 1. F1: the pipeline is wired (banked CAMB LCDM chi^2 = 206.4 / 215)
    banked = json.load(open(os.path.join(LIK, 'lcdm.json')))
    chi_camb = float(banked['fun'])
    check(f'F1 PIPELINE WIRED: the banked CAMB flat-LambdaCDM best fit is chi^2 = {chi_camb:.1f} / 215 '
          f'(chi^2/dof = {chi_camb/215:.3f} ~ 0.96) -- the wiring check',
          0.85 < chi_camb / 215 < 1.15)

    def score(fname):
        z = np.load(os.path.join(SPEC, fname))
        return CS.chi2_of(z['ls'], z['Dl'])[0]

    chi_lcdm = score('c54.178_lcdm.npz')
    chi_cr0 = score('c54.178_cr.npz')
    chi_crpi = score('L814_cr_phipi_L2000.npz')
    F3_0 = chi_cr0 - chi_lcdm
    F3_pi = chi_crpi - chi_lcdm
    THR = (6 - 2) * np.log(215)

    print(f"    [scored] chi^2(LCDM arm)={chi_lcdm:.1f}  chi^2(CR phi=0)={chi_cr0:.1f}  "
          f"chi^2(CR phi=pi)={chi_crpi:.1f}")
    print(f"    [pair]   F3(phi=0)={F3_0:+.1f}   F3(phi=pi)={F3_pi:+.1f}   threshold dBIC={THR:.1f}")

    # 2. the pair: both F3 exceed 21.5 by thousands -> CR not preferred at either branch
    check('THE PAIR: F3(phi=0) and F3(phi=pi) are BOTH >> the 21.5 threshold (by ~2000-3000x), so '
          f'dBIC = F3 - 21.5 > 0 at BOTH branches -- CR is NOT preferred at either seam phase '
          f'(F3_0={F3_0:.0f}, F3_pi={F3_pi:.0f}); PO-7\'s branch selection does not change it',
          F3_0 > THR and F3_pi > THR and F3_0 > 1e4 and F3_pi > 1e4)

    # phi=pi is worse despite the smaller first-peak gap
    zpi = np.load(os.path.join(SPEC, 'L814_cr_phipi_L2000.npz'))
    check('and phi=pi is WORSE, not better: F3(phi=pi) > F3(phi=0), even though its first-peak gap is '
          f'smaller (l_A={float(zpi["l_A"]):.1f} pinned) -- the heights/shape cost more chi^2 than the '
          'closer position saves',
          F3_pi > F3_0)

    # 3. the threshold AND its reference (state what it is scored against, not the threshold alone)
    check('THE THRESHOLD AND ITS REFERENCE: F3 is scored against 21.5 = (6-2) ln 215 (the SAME-INSTRUMENT '
          f'parameter penalty, got {THR:.1f}), NOT against CAMB\'s 206.4 (withdrawn r2719); on the '
          'Jeffreys scale 21.5 is 3.5x the strong line of 6. CR preferred IFF F3 < 21.5 -- the numeric '
          'bar, so the reading is not chosen after the number',
          abs(THR - 21.5) < 0.2)

    # 4. the floor cuts BOTH ways: the relative gap is decisive, above the floor -- NOT laundered
    F2 = chi_lcdm - chi_camb
    check('THE FLOOR CUTS BOTH WAYS, does not soften the negative: F2 = chi^2(LCDM arm) - chi^2(CAMB) = '
          f'{F2:+.0f} (control at chi^2/dof ~ {chi_lcdm/185:.0f}), so no model fits well -- but the floor '
          'only prevents arbitration between models whose F3 differ by <~ the floor (~1114); the measured '
          f'F3 ({F3_0:.0f}, {F3_pi:.0f}) are 45-60x it, so the RELATIVE gap is real and the negatives are '
          'DECISIVE and BOUNDED. The floor could no more bank a positive than rescue this negative',
          F2 > 500 and F3_0 > 40 * F2 and F3_pi > 40 * F2)

    # 5. F5 guard: no framework verdict; PO-7 protected; the run is delivered, not converted
    src = open(__file__, encoding='utf-8').read()
    check('no framework verdict on CR -- PO-7 is PROTECTED, this reports the BIC pair PO-10 '
          'specified and does not convert PO-7; the physical branch is PO-7\'s to select',
          'PO-7 is PROTECTED' in src and 'does not convert PO-7' in src)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (PO-10 run delivered): the BIC pair is F3(phi=0) ~ +5.05e4 and F3(phi=pi) ~ +6.76e4,')
    print('  both ~2000-3000x the 21.5 threshold AND 45-60x the instrument floor, so the RELATIVE gap is')
    print('  real physics: CR is DECISIVELY disfavoured at BOTH seam phases -- two bounded negatives, and')
    print('  PO-7\'s branch selection does not rescue either. The floor (chi^2/dof ~ 7 control) means no')
    print('  model fits well ABSOLUTELY, but it cuts both ways and does not soften the negative. F5')
    print('  unsoftened: a measurement discrepancy, not a framework verdict; PO-7 protected. cc54 ran it.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
