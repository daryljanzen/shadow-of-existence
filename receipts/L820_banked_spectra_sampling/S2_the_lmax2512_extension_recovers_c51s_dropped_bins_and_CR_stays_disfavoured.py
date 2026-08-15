#!/usr/bin/env python3
r"""S2 -- cc54: the LMAXL=2512 extension (C51's real point) is delivered. It recovers the 30 damping-tail
bins the LMAXL=2000 arm drops (ell 1759-2508), and including them does NOT rescue the CR arm -- it makes CR
MORE clearly disfavoured, because opening the wavenumber range improves the CONTROL while the CR arm barely
moves. Two effects, isolated: (i) the wider k-range improves the control's overlap fit 7.14 -> 3.81 on the
SAME 185 bins (the truncation effect c54.186 already found on LMAXL=2000->3000); (ii) the added damping-tail
bins barely change either arm. F3 = chi^2(CR)-chi^2(LCDM) goes 50497 (185 bins) -> 51547 (201 bins) -- the
gap WIDENS. So C51's blocker is discharged: the dropped region is not a hidden regime where CR does better.

** WHY THE TWO EFFECTS MUST BE SEPARATED. ** Opening LMAXL widens the projection's k-grid for ALL modes
(kk = linspace(12, LMAXL, 3*NK)/D_M), so an LMAXL=2512 run is not "the LMAXL=2000 spectrum plus 16 bins" --
it recomputes the overlap at a wider k-range too. Scoring the extension BOTH on the overlap (ell<=1996, the
banked 185 bins) and on the full range (201 bins) separates the k-range effect from the damping-tail
addition.

** THE MEASUREMENT (plik_lite TT, one fitted amplitude, chi2_of_spectrum). **
  LCDM:  banked L2000 (185 bins)            chi^2/dof = 7.14
         ext   L2512, overlap ell<=1996     chi^2/dof = 3.81   <- the k-range effect (c54.186's truncation)
         ext   L2512, full (201 bins)       chi^2/dof = 3.68   <- adding the damping tail barely moves it
  CR:    banked L2000 (185 bins)            chi^2/dof = 280.1
         ext   L2512, overlap ell<=1996     chi^2/dof = 281.1  <- the CR arm does NOT gain from wider k
         ext   L2512, full (201 bins)       chi^2/dof = 260.1  <- still overwhelmingly disfavoured
  F3 = chi^2(CR) - chi^2(LCDM):  185 bins 50497  ->  201 bins 51547   (the gap WIDENS)

COMPUTES: the chi^2 of the LMAXL=2512 lcdm (NK=800) and CR (ladder) extensions, scored on the overlap
(ell<=1996) and full (ell<=2508) bin sets, against the banked LMAXL=2000 pair. ** LMAXL=2512 NK=800 is the
extension's configuration (6.0 pts/period, clears the guard) and LMAXL=2000 is the banked baseline, not a
single pinned point. **

** WHAT THIS RECEIPT ASSERTS. **
  1. THE EXTENSION COVERS THE DROPPED REGION: the LMAXL=2512 spectra carry ell up to 2508 and score 201
     bins (vs the banked 185), recovering C51's damping-tail bins (ell 1759-2508).
  2. THE CONTROL'S GAIN IS THE K-RANGE, NOT THE TAIL: on the SAME 185 bins the control goes 7.14 -> 3.81
     when LMAXL opens 2000 -> 2512 (the truncation effect c54.186 found), and the added damping-tail bins
     move it only 3.81 -> 3.68.
  3. THE CR ARM DOES NOT GAIN AND STAYS DISFAVOURED: on the overlap CR barely moves (280.1 -> 281.1), and
     with the damping tail it is 260.1/dof -- overwhelmingly disfavoured either way.
  4. INCLUDING THE DROPPED BINS DOES NOT RESCUE CR: F3 = chi^2(CR)-chi^2(LCDM) goes 50497 -> 51547 across
     the extension, so the gap WIDENS; the dropped region is not a hidden regime where CR discriminates in
     its own favour. C51's blocker is discharged.

** WHAT IS NOT CLAIMED, stated for reversal. ** NOT that the control now fits well -- 3.68/dof is still
large against a true LCDM fit's ~1.0; part of the residual is the truncation c54.186 named and part is
physics, and this receipt does not separate those further. NOT that F3's growth is a new disfavouring of
CR -- both F3 values are ~2400x the 21.5 threshold, so the verdict (CR not preferred) is unchanged; what is
new is only that the dropped bins do not reverse it. NOT that the LMAXL=2512 CR ladder is a continuum check
-- it is the physical ladder (guard-waived, as c54.186's KCONT already validated for L2000); the lcdm arm
is the continuum. NOT a claim about polarisation or ell<30 -- plik_lite TT only, as the whole arm is.

** Board lead L-820 (cc54's band), receipt S2; the C51 (damping-tail) half of 56's resampling route, the
companion to S1's C52 (sampling) half. Informs L-147 (PO-10). With S1 and S2, both halves of the routed
task are discharged: the sampling premise was a misread (S1) and the dropped bins do not rescue CR (S2). **

Written r2674 (cc54, L-820 S2). Asserts against the banked c54.178 pair and cc54's LMAXL=2512 extensions
(L820_lcdm_L2512_nk800.npz, L820_cr_L2512.npz) through the same plik_lite scorer -- never the register.
Stated for reversal.
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS  # noqa: E402
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def chi2(path, ell_cut=None):
    z = np.load(os.path.join(SPEC, path))
    ls, Dl = z['ls'], z['Dl']
    if ell_cut is not None:
        m = ls <= ell_cut
        ls, Dl = ls[m], Dl[m]
    c, n, _A, _lo, _hi = CS.chi2_of(ls, Dl)
    return c, n


def main():
    print()
    print('  S2 -- LMAXL=2512 extension: does recovering C51\'s dropped bins rescue the CR arm?')
    print()

    lc_b, nb_l = chi2('c54.178_lcdm.npz')                       # banked L2000, 185 bins
    lc_ov, nb_ov = chi2('L820_lcdm_L2512_nk800.npz', 1996)      # extension, overlap 185 bins
    lc_f, n_f = chi2('L820_lcdm_L2512_nk800.npz')               # extension, full 201 bins
    cr_b, _ = chi2('c54.178_cr.npz')
    cr_ov, _ = chi2('L820_cr_L2512.npz', 1996)
    cr_f, ncr_f = chi2('L820_cr_L2512.npz')

    # 1. the extension covers the dropped region
    check(f'THE EXTENSION COVERS THE DROPPED REGION: LMAXL=2512 scores {n_f} bins to ell=2508 (vs the '
          f'banked {nb_l} to ell=1996), recovering C51\'s damping-tail bins (ell 1759-2508)',
          n_f > nb_l and n_f >= 200)

    # 2. the control's gain is the k-range, not the tail
    check(f'THE CONTROL\'S GAIN IS THE K-RANGE: on the SAME {nb_ov} bins the control goes '
          f'{lc_b/nb_l:.2f} -> {lc_ov/nb_ov:.2f}/dof when LMAXL opens 2000->2512 (c54.186\'s truncation '
          f'effect), and the added damping tail moves it only {lc_ov/nb_ov:.2f} -> {lc_f/n_f:.2f}',
          lc_ov / nb_ov < 0.6 * (lc_b / nb_l) and abs(lc_f / n_f - lc_ov / nb_ov) < 0.5)

    # 3. the CR arm does not gain and stays disfavoured
    check(f'THE CR ARM DOES NOT GAIN AND STAYS DISFAVOURED: on the overlap CR barely moves '
          f'({cr_b/nb_l:.1f} -> {cr_ov/nb_ov:.1f}/dof), and with the damping tail it is {cr_f/ncr_f:.1f}'
          '/dof -- overwhelmingly disfavoured either way',
          abs(cr_ov / nb_ov - cr_b / nb_l) / (cr_b / nb_l) < 0.02 and cr_f / ncr_f > 100)

    # 4. including the dropped bins does not rescue CR -- F3 widens
    f3_185 = cr_b - lc_b
    f3_201 = cr_f - lc_f
    check(f'INCLUDING THE DROPPED BINS DOES NOT RESCUE CR: F3 = chi^2(CR)-chi^2(LCDM) goes {f3_185:.0f} '
          f'(185 bins) -> {f3_201:.0f} (201 bins) -- the gap WIDENS, both ~2400x the 21.5 threshold; the '
          'dropped region is not a hidden regime where CR does better. C51\'s blocker is discharged',
          f3_201 > f3_185 and f3_185 > 21.5 and f3_201 > 21.5)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (C51 discharged): the LMAXL=2512 extension recovers the 30 damping-tail bins the arm')
    print('  drops. Opening the wavenumber range improves the CONTROL (7.14 -> 3.81/dof on the same 185')
    print('  bins -- c54.186\'s truncation effect), while the CR arm barely moves (280 -> 281); adding the')
    print('  damping tail leaves CR at 260/dof. F3 widens 50497 -> 51547, so including the dropped bins')
    print('  makes CR MORE clearly disfavoured, not less. With S1 (the sampling premise was a misread),')
    print('  both halves of 56\'s resampling route are discharged: the banked numbers hold and the dropped')
    print('  region does not reverse the CR verdict.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
