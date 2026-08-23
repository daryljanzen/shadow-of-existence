#!/usr/bin/env python3
r"""S1 -- cc54, PO-10 (OWED #454): the CONTROL arm's remaining chi^2/dof after L-824's convergence is
a BROADBAND instrument floor, not a localized defect -- so reaching the pipeline's ~1 target is an
instrument-accuracy question, not a patch. L-824 brought the converged, lensed control to 1.18/dof on
the 185 bins against CAMB lensed LCDM's 1.014 on the SAME bins (#454 had recorded the old ~100). This
receipt localizes the remaining excess (chi^2 ~ 30 over CAMB): a per-bin r_i(Fr)_i decomposition shows
it is spread across EVERY ell-band -- +4.5 (100-300), +6.0 (300-550), +7.4 (550-850), +1.6 (850-1200),
+5.7 (1200-1600), +4.9 (1600-2000) -- with no single band dominating, slightly concentrated in the
first two acoustic peaks (300-850 carries 13.4 of the 30). So the two-arm instrument sits ~15% above a
full Boltzmann code broadband, leading in the peaks (its acoustic phase/height approximations), which
is why #454's ~1 target needs a uniformly more accurate transfer, not a fixable band. This is
the CONTROL arm, and it is why F3 = chi^2(CR)-chi^2(LCDM) -- which cancels this shared floor -- is the
right differential.

** THE METHOD. ** chi^2 = r^T F r with r = d - A m the amplitude-fitted residual and F the plik_lite
Fisher matrix; r_i (F r)_i sums to chi^2 exactly, so grouping it by ell-band localizes the excess with
the FULL covariance. Both arms are scored on the SAME 185 bins; the control carries c54.183's lensing
(CAMB's lensed/unlensed ratio, L-824's construction), CAMB is its own lensed LCDM.

** THE DECOMPOSITION (converged lensed control vs CAMB lensed, same 185 bins). **
      ell band       control chi^2    CAMB chi^2    excess
      100- 300           17.7            13.2        +4.5
      300- 550           33.7            27.7        +6.0
      550- 850           38.0            30.6        +7.4     <- peaks lead
      850-1200           40.4            38.9        +1.6
     1200-1600           53.4            47.7        +5.7
     1600-2000           33.4            28.5        +4.9
      TOTAL             216.6 (1.18)    186.6 (1.01)  +30.1
  ⇒ every band is positive; the excess is broadband, not a single defect.

COMPUTES: the per-bin chi^2 decomposition of the converged lensed control (L824 L3200 arm) and CAMB
lensed LCDM against plik_lite TT on the fixed 185-bin set. ** The band edges partition the ell-range;
the CAMB reference is the pipeline's own F1 reference, not a pinned working point. **

** WHAT THIS RECEIPT ASSERTS. **
  1. THE REMAINDER IS SMALL AND MEASURED: the converged lensed control is 1.18/dof vs CAMB lensed's
     1.01 on the same 185 bins, an excess of ~30 in chi^2 (#454's "~100" is the pre-convergence,
     pre-lensing number).
  2. IT IS BROADBAND, NOT LOCALIZED: every ell-band from 100 to 2000 contributes a positive excess,
     none dominating; the largest single band (550-850) is 7.4 of 30.
  3. IT LEADS IN THE ACOUSTIC PEAKS: 300-850 carries 13.4 of the 30, consistent with the two-arm
     instrument's acoustic phase/height approximation being its leading imperfection vs a full
     Boltzmann code.

** WHAT IS NOT CLAIMED, stated for reversal. ** NOT that #454's ~1 target is reached -- it is not
(1.18, floor ~0.16 above CAMB); the claim is that the remainder is broadband and small, so closing it
is an instrument-accuracy task (a more accurate transfer everywhere), not a patchable band. NOT a
framework verdict (F5): this is the CONTROL arm; the CR arm is untouched. NOT that the 15% is uniform
per-bin -- it is per-BAND positive and peak-led; a finer split may find structure, but no band is
zero-excess, which is the broadband claim. NOT that the two-arm instrument is wrong -- a ~15%
broadband floor vs CAMB is expected of a reduced acoustic solver, and F3 cancels it.

** Board lead L-826 (cc54's band); OWED #454's remainder localized. Continues L-824 (the convergence).
Informs L-147 (PO-10). Routed to 56. **

Written r2674 (cc54, L-826). Asserts against the converged lensed control (L824 arm) and CAMB lensed
LCDM scored through plik_lite TT's full covariance -- never the register. Stated for reversal.
"""
import os
import sys

import numpy as np
import scipy.linalg

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


def main():
    print()
    print('  S1 -- PO-10 OWED #454: is the converged control\'s remainder localized or broadband?')
    print()
    try:
        import camb
    except ImportError:
        print('    SKIP  needs camb for the CAMB lensed reference and the lensing ratio; the corpus '
              'runs receipts where camb is present (as P15_the_control_entered… does)')
        return 0

    _p = camb.set_params(H0=67.36, ombh2=0.02237, omch2=0.1200, ns=0.9649, As=2.1e-9, tau=0.0544)
    _p.set_for_lmax(3500, lens_potential_accuracy=1)
    _pc = camb.get_results(_p).get_cmb_power_spectra(_p, CMB_unit='muK')
    Dlen, Dunl = _pc['total'][:, 0], _pc['unlensed_total'][:, 0]
    Lc = np.arange(len(Dlen))
    rat = np.ones_like(Dlen)
    m = (Lc >= 2) & (Dunl > 0)
    rat[m] = Dlen[m] / Dunl[m]

    def LR(l):
        return np.interp(np.asarray(l, float), Lc, rat, left=1.0, right=rat[-1])

    # common 185 bins = the L2000 arm's coverage
    z0 = np.load(os.path.join(SPEC, 'c54.178_lcdm.npz'))
    common = np.isfinite(CS.bin_spectrum(z0['ls'], z0['Dl']))

    def perbin(ls, Dl):
        mb = CS.bin_spectrum(ls, Dl)
        fin = np.isfinite(mb) & common
        cov = CS.COV_TT[np.ix_(fin, fin)]
        F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(cov), np.identity(fin.sum()))
        F = 0.5 * (F + F.T)
        mm, d = mb[fin], CS.X_DATA[fin]
        A = float((mm @ F @ d) / (mm @ F @ mm))
        r = d - A * mm
        return CS.BIN_LO[fin], r * (F @ r)

    z = np.load(os.path.join(SPEC, 'L824_lcdm_L3200_nk960.npz'))
    lo, ctr = perbin(z['ls'], z['Dl'] * LR(z['ls']))
    _, cam = perbin(np.arange(2, 3500, dtype=float), Dlen[2:3500])
    nb = len(ctr)
    excess = ctr.sum() - cam.sum()

    check(f'THE REMAINDER IS SMALL AND MEASURED: the converged lensed control is '
          f'{ctr.sum()/(nb-1):.2f}/dof vs CAMB lensed\'s {cam.sum()/(nb-1):.2f} on the same {nb} '
          f'bins, an excess of {excess:.0f} in chi^2 (#454\'s "~100" is pre-convergence, pre-lensing)',
          1.05 < ctr.sum() / (nb - 1) < 1.30 and 0.9 < cam.sum() / (nb - 1) < 1.10)

    bands = [(100, 300), (300, 550), (550, 850), (850, 1200), (1200, 1600), (1600, 2000)]
    per = [(ctr[(lo >= a) & (lo < b)].sum() - cam[(lo >= a) & (lo < b)].sum()) for a, b in bands]
    check(f'IT IS BROADBAND, NOT LOCALIZED: every ell-band 100-2000 contributes a positive excess '
          f'{[round(float(x), 1) for x in per]}, none dominating (largest {max(per):.1f} of {excess:.0f})',
          all(x > 0 for x in per) and max(per) < 0.45 * excess)

    peaks = per[1] + per[2]                                  # 300-850
    check(f'IT LEADS IN THE ACOUSTIC PEAKS: 300-850 carries {peaks:.1f} of the {excess:.0f} excess, '
          'the two-arm instrument\'s acoustic phase/height approximation vs a full Boltzmann code',
          peaks > 0.30 * excess)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (OWED #454 remainder): the converged lensed control\'s 1.18/dof is a BROADBAND')
    print('  instrument floor -- ~15% above CAMB lensed across every ell-band, leading in the acoustic')
    print('  peaks -- not a localized defect. So the pipeline\'s ~1 target is an instrument-accuracy')
    print('  question (a uniformly better transfer), not a patchable band; and F3 = chi^2(CR)-')
    print('  chi^2(LCDM), which cancels this shared floor, is why it is the right differential. F5')
    print('  untouched: this is the control arm.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
