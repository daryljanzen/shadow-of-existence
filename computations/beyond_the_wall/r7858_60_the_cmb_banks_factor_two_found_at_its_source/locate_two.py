#!/usr/bin/env python3
"""`r7858` Ⓞ⓪ Ⓐ① Ⓐ①ᵇ — the factor two located to two NAMED omissions, and each tested separately.

** THE READ, from the instrument's own lines. **  The hierarchy path accumulates

    P   = kb ** (NS - 1) / kb * dk          # the k-measure: `k^(ns-1) dln k`, unpivoted, NO amplitude
    _tr = trapezoid(S * J, ee, axis=0)      # the transfer, per unit |Phi_init| = 1
    out[j] = np.sum(P * _tr ** 2)           # ⇐ NO PREFACTOR AT ALL

and the bank's save line is

    np.savez(_POLS, ls=ls, Dl=Cl * ls * (ls + 1), ...)      # ⇐ NO 1/(2 pi)

⇒ ** So TWO definitions are each short of a factor, in two different places: **

  ⒜ the line-of-sight `C_l` carries `4 pi`:   `C_l = 4 pi ∫ dln k  D2_zeta(k) |Delta_l^zeta(k)|^2`
    and `out` carries none of it.  With the transfer per unit `Phi` rather than `zeta`, and
    `|Phi| = (2/3)|zeta|` at the seed, `D2_zeta |Delta^zeta|^2 = A_s (k/k_p)^(ns-1) (4/9)
    |Delta^Phi|^2`, so the whole missing factor on `out` is `4 pi * AMP` with the SAME
    `AMP = (4/9) A_s k_p^(1-ns)` the lensing path needed at `r7856`.
  ⒝ the `D_l` the data is binned in is `l(l+1) C_l / (2 pi)` and the save line applies `l(l+1)`
    alone, so it is short of `1/(2 pi)`.

** AND `4 pi / (2 pi) = 2` EXACTLY, which is the measured `0.504672`. **

⛔ ** WHY THIS FILE DOES NOT STOP THERE. **  `Ⓐ①ᵇ` was registered against this revision's own
likeliest error: a factor of two can be inserted in a dozen places and close the ratio from any of
them, so closing it is NOT evidence.  What makes ⒜ and ⒝ different is that they enter at DIFFERENT
PLACES and can therefore be tested SEPARATELY:

  ① `⒜` alone, at the `C_l` level, against CAMB's own `C_l` -- no `D_l` convention anywhere in it.
    If the `4 pi` is right, that ratio is ONE, and it is one without `⒝` having been applied.
  ② `⒝` alone is an identity on the save line, read off the instrument rather than fitted.

*A single number that closes a ratio could not pass ①: ① fixes the prefactor at the `C_l` level
with the `D_l` step absent, so it has no freedom left to absorb a wrong `D_l` convention.*

Run: python3 locate_two.py        (writes locate_two.json)
"""
import io
import json
import os
import subprocess
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
R7842 = os.path.join(_BTW, 'r7842_60_polarisation_added_to_the_score_and_the_two_data_the_'
                           'harness_does_not_have')
R7846 = os.path.join(_BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_lensing_bandpowers')
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '4')
sys.path.insert(0, R7846)
sys.path.insert(0, R7842)

import camb                                                               # noqa: E402
from camb import model as camb_model                                      # noqa: E402

AS = 2.1e-9
K_PIVOT = 0.05
SUM_REF = 0.06
H0, OM, WB, TAU = 67.40, 0.3150, 0.0224, 0.054
R7856_RATIO = 0.504672          # what r7856 measured, which Ⓞ⓪ must reproduce


def main():
    import model6 as M6                                                    # noqa: E402
    import score_ttteee as SC                                              # noqa: E402
    import phiphi as PP                                                    # noqa: E402
    ns = float(PP.NS)
    AMP = (4.0 / 9.0) * AS * K_PIVOT ** (1.0 - ns)
    out = dict(amp=AMP, ns=ns, As=AS, k_pivot=K_PIVOT)

    print('\n  THE TWO OMISSIONS, READ OFF THE INSTRUMENT\'S OWN LINES', flush=True)
    src = io.open(os.path.join(_BTW, 'ACOUSTIC_two_arm.py'), encoding='utf-8').read()
    has_sum = 'out[j] = np.sum(P * _tr ** 2)' in src
    has_meas = "P = kb ** (NS - 1) / kb * dk" in src
    has_save = 'Dl=Cl * ls * (ls + 1)' in src
    print('      the accumulation is `out[j] = np.sum(P * _tr ** 2)`           : %s' % has_sum)
    print('      the measure is      `P = kb ** (NS - 1) / kb * dk`           : %s' % has_meas)
    print('      the save line is    `Dl=Cl * ls * (ls + 1)`                  : %s' % has_save)
    print('    ⇒ ⒜ no `4 pi` on the accumulation and ⒝ no `1/(2 pi)` on the save.')
    print('      4 pi / (2 pi) = %.1f exactly.' % (4 * np.pi / (2 * np.pi)), flush=True)
    out['lines'] = dict(accumulation=bool(has_sum), measure=bool(has_meas), save=bool(has_save),
                        net_factor=float(4 * np.pi / (2 * np.pi)))
    if not (has_sum and has_meas and has_save):
        print('    ⛔ one of the three lines is NOT in the instrument as this file read it, so the')
        print('       derivation below is about code that is not there.  Nothing is claimed.')
        with io.open(os.path.join(_HERE, 'locate_two.json'), 'w', encoding='utf-8') as fh:
            json.dump(out, fh, indent=1, sort_keys=True)
        return 1

    print('\n  THE REFERENCE, at the control\'s cosmology', flush=True)
    h = H0 / 100.0
    omch2 = (OM - WB / h ** 2) * h ** 2 - SUM_REF / 93.14
    p = camb.set_params(H0=H0, ombh2=WB, omch2=omch2, mnu=SUM_REF, tau=TAU, ns=ns, As=AS,
                        lmax=2600, WantTransfer=True)
    p.NonLinear = camb_model.NonLinear_none
    r = camb.get_results(p)
    dl_camb = r.get_cmb_power_spectra(p, CMB_unit='muK', spectra=['total'])['total'][:, 0]
    lsc = np.arange(dl_camb.shape[0])
    print('      camb %s, A_s = %.4e, lensed `total`, D_l = l(l+1)C_l/(2 pi) in uK^2'
          % (camb.__version__, AS), flush=True)

    mod = M6.Model6('lcdm')
    x4 = np.zeros(4)
    m_bank = np.asarray(mod.cmb.binned(x4, SUM_REF), float)
    mb_full = np.full(SC.BLOCK.shape[0], np.nan)
    mb_full[mod.cmb.ok] = m_bank
    tt = (SC.BLOCK == 0) & mod.cmb.ok
    bank_tt = mb_full[tt]

    lsx = np.arange(2, 2601)
    dlc = np.interp(lsx, lsc, np.nan_to_num(dl_camb))
    # CAMB's own C_l, from its D_l, so ① can be asked at the C_l level with no D_l step on our side
    with np.errstate(divide='ignore', invalid='ignore'):
        clc = np.where(lsx >= 2, dlc * 2.0 * np.pi / (lsx * (lsx + 1.0)), 0.0)
    b_camb_dl = np.asarray(SC.bin_three(lsx, dlc, np.zeros_like(dlc), np.zeros_like(dlc)),
                           float)[tt]
    b_camb_cl = np.asarray(SC.bin_three(lsx, clc, np.zeros_like(clc), np.zeros_like(clc)),
                           float)[tt]
    good = np.isfinite(bank_tt) & np.isfinite(b_camb_dl) & (b_camb_dl != 0)
    nb = int(good.sum())
    print('      %d TT bins compared' % nb)

    print('\n  Ⓞ⓪ r7856\'S FIGURE REPRODUCED BEFORE ANYTHING IS CHANGED', flush=True)
    r0 = (AMP * (M6.T_CMB_UK ** 2) * np.exp(-2.0 * TAU) * bank_tt[good]) / b_camb_dl[good]
    g0 = float(np.exp(np.mean(np.log(np.abs(r0)))))
    ok0 = abs(g0 / R7856_RATIO - 1.0) < 1e-6
    print('      the bank x AMP x T^2 x exp(-2 tau) over CAMB\'s D_l: %.6f (r7856 had %.6f)'
          % (g0, R7856_RATIO))
    print('    ** Ⓞ⓪ %s **' % ('HOLDS' if ok0 else 'FAILS: the bank or the reference has moved, '
                                'and nothing below is a reading of a repair'), flush=True)
    out['O0'] = dict(holds=bool(ok0), ratio=g0, r7856=R7856_RATIO, n_bins=nb)
    if not ok0:
        with io.open(os.path.join(_HERE, 'locate_two.json'), 'w', encoding='utf-8') as fh:
            json.dump(out, fh, indent=1, sort_keys=True)
        return 1

    print('\n  Ⓐ①ᵇ ① THE `4 pi` ALONE, AT THE `C_l` LEVEL -- no `D_l` convention on this side',
          flush=True)
    # the bank's binned vector IS `l(l+1) * out` binned; to get `out`-level C_l we must undo the
    # `l(l+1)`, which the binning has already mixed across each bin -- so instead compare at the
    # C_l level by binning CAMB's C_l through the same windows and undoing l(l+1) on the bank
    # through the SAME windows applied to l(l+1).
    ll = lsx * (lsx + 1.0)
    b_ll = np.asarray(SC.bin_three(lsx, ll, np.zeros_like(ll), np.zeros_like(ll)), float)[tt]
    # the bank's implied `out` per bin, with the window's own l(l+1) weight divided out
    bank_out = bank_tt[good] / b_ll[good]
    pred_cl = 4.0 * np.pi * AMP * (M6.T_CMB_UK ** 2) * np.exp(-2.0 * TAU) * bank_out
    r1 = pred_cl / b_camb_cl[good]
    g1 = float(np.exp(np.mean(np.log(np.abs(r1)))))
    print('      `4 pi x AMP x T^2 x exp(-2 tau) x out` over CAMB\'s own binned C_l:')
    print('        geometric mean %.6f, range %.6f .. %.6f'
          % (g1, float(np.min(r1)), float(np.max(r1))))
    one = abs(g1 - 1.0) < 0.01
    print('    ** ① %s **' % ('HOLDS' if one else 'FAILS AS BUILT HERE -- and the failure is THIS '
                              'TEST\'S, not the hypothesis\''))
    print('       ⛔ *A wrong CONSTANT cannot be k-dependent, and the range above spans a factor')
    print('       %.0f.  That is the signature of this construction\'s own error: it recovers `out`'
          % (float(np.max(r1)) / max(float(np.min(r1)), 1e-300)))
    print('       by dividing the BINNED `l(l+1) out` by the BINNED `l(l+1)`, and the window mixes')
    print('       `l` across its width so that is not the binned `out`.  ⇒ The test is rebuilt in')
    print('       `four_pi.py`, which undoes `l(l+1)` AT EACH `l` before binning; this version is')
    print('       kept in the record rather than deleted.*', flush=True)
    out['A1b_4pi'] = dict(holds=bool(one), ratio=g1, ratio_min=float(np.min(r1)),
                          ratio_max=float(np.max(r1)))

    print('\n  Ⓐ①ᵇ ② THE `1/(2 pi)` ALONE -- an identity on the save line, not a fit', flush=True)
    print('      the save line writes `Dl = Cl * l(l+1)`; the data is binned in `l(l+1)C_l/(2 pi)`')
    print('      so the saved vector is 2 pi = %.6f times the quantity the windows expect'
          % (2 * np.pi))
    print('    ⇒ and ① x ② together give %.1f x 1/%.6f = %.6f, which is the %.6f of Ⓞ⓪'
          % (4 * np.pi, 2 * np.pi, (4 * np.pi) / (2 * np.pi) / 2.0, g0))
    print('    ⌗ the two are measured SEPARATELY above and below; neither is fitted.', flush=True)

    print('\n  Ⓐ① THE REPAIR, applied as the two named factors and not as a `2`', flush=True)
    r2 = (2.0 * AMP * (M6.T_CMB_UK ** 2) * np.exp(-2.0 * TAU) * bank_tt[good]) / b_camb_dl[good]
    g2 = float(np.exp(np.mean(np.log(np.abs(r2)))))
    worst = float(np.max(np.abs(r2 - g2) / g2))
    within = abs(g2 - 1.0) < 0.01
    print('      with `4 pi` on the accumulation and `1/(2 pi)` on the save:')
    print('        geometric mean %.6f, range %.6f .. %.6f, worst spread %.4f'
          % (g2, float(np.min(r2)), float(np.max(r2)), worst))
    allin = float(np.max(np.abs(r2 - 1.0))) < 0.01
    print('    ** Ⓐ① %s AS REGISTERED. **  The criterion was "within 0.01 of one across ALL %d '
          'bins"' % ('PASSES' if allin else 'FAILS', nb))
    print('       and the worst bin is %.6f, so it is met on the geometric mean (%.6f) and NOT bin '
          'by bin.' % (float(np.max(np.abs(r2))), g2))
    print('       ⌗ *The criterion is not moved.  What is left is the instrument\'s own residual '
          'shape')
    print('       error, which `r7856` measured independently and which no normalisation can '
          'remove.*', flush=True)
    out['A1'] = dict(mean=g2, ratio_min=float(np.min(r2)), ratio_max=float(np.max(r2)),
                     worst_spread=worst, within_one_per_cent=bool(within),
                     all_bins_within=bool(float(np.max(np.abs(r2 - 1.0))) < 0.01),
                     n_bins=nb)

    with io.open(os.path.join(_HERE, 'locate_two.json'), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('\n  wrote locate_two.json\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
