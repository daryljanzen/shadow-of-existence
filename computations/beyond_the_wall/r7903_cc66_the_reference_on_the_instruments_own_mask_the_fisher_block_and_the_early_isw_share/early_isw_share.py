# -*- coding: utf-8 -*-
"""r7903+cc66 item ⑲③: THE EARLY-ISW SHARE, BIN BY BIN, ON ONE STATED DEFINITION.

=============================== THE DEFINITION, FIXED BEFORE THE RUN ===============================
    share(bin) = (full - no_ISW) / full
  per plik_lite TT bin with 100 <= ell <= 207, on UNLENSED scalar TT, on the reference's own
  parameters, at Sigma = 0, 0.06, 0.30 and 0.60 eV.
====================================================================================================

`no_ISW` removes CAMB's own ISW source term, which `r7895+cc66.2` established is the **TOTAL** ISW.
In this band the late half is at most `2.82e-04` relative, so the total is the early ISW to within
that, which is what makes this the EARLY-ISW share.  Registered at `b7ade4b6d` before this file
existed: band-aggregate `0.44 ± 0.05`; positive in every bin and FALLING with `ell`; per-bin spread
under `0.02` across the four sums.

** THE BINNING IS THE LIKELIHOOD'S OWN. **  `score_ttteee._bin_one(ls, D, 'TT')` carries plik_lite's
`bin_w_TT` weights.  A flat average over each bin's `ell` range would be a different quantity, and
the thing asked for here is a per-bin RATIO, where the weighting does not cancel.  ⌗ *The legs come
back as `raw_cl=True`, i.e. `C_ell`, so they are converted to `D_ell = ell(ell+1)C/2pi` BEFORE
binning, because that is the convention the bin weights were built for.*

`60` computes the same on the instrument as its own ②, and neither side reads the other's before both
are banked.

    python3 <this file>
"""
import glob
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)
R7842 = glob.glob(os.path.join(BW, 'r7842_60_*'))[0]
R7895 = glob.glob(os.path.join(BW, 'r7895_cc66_*'))[0]
sys.path.insert(0, R7842)

import score_ttteee as SC                                                    # noqa: E402

#: r7895's own leg builder, imported rather than copied -- same sources, same two-pass build
_spec = __import__('importlib.util', fromlist=['util']).spec_from_file_location(
    'cc66_r7895_isw', os.path.join(R7895, 'late_isw_split.py'))
_isw = __import__('importlib.util', fromlist=['util']).module_from_spec(_spec)
_spec.loader.exec_module(_isw)

SUMS = (0.0, 0.06, 0.30, 0.60)
L_LO, L_HI = 100, 207
SPREAD_BAR = 0.02
AGG_LO, AGG_HI = 0.39, 0.49


def to_D(cl):
    """C_ell -> D_ell = ell(ell+1)C/2pi, the convention plik_lite's bin weights were built for"""
    ls = np.arange(len(cl), dtype=float)
    return ls * (ls + 1.0) * np.asarray(cl, float) / (2.0 * np.pi)


def tt_bins(cl):
    """the TT block binned with the likelihood's OWN weights"""
    ls = np.arange(len(cl), dtype=float)
    return np.asarray(SC._bin_one(ls, to_D(cl), 'TT'), float)


def main():
    ref = _isw._reference()
    ntt = int((SC.BLOCK == 0).sum())
    lo, hi = SC.BIN_LO[:ntt], SC.BIN_HI[:ntt]
    inband = np.where((lo >= L_LO) & (hi <= L_HI))[0]
    print('=' * 100)
    print('  ⑲③ THE EARLY-ISW SHARE, BIN BY BIN')
    print('=' * 100)
    print('  definition: (full - no_ISW)/full per plik_lite TT bin, %d <= ell <= %d, UNLENSED, '
          'reference parameters' % (L_LO, L_HI))
    print('  reference : %s' % ref)
    print('  TT bins fully inside the band: %d   (ell %d..%d)'
          % (len(inband), lo[inband].min(), hi[inband].max()))
    #: ⌗ TWELVE, and `r7892`/`r7895+cc66.2` counted THIRTEEN sub-peak TT bins.  Those are DIFFERENT
    #  POPULATIONS, not a discrepancy: `r7892`'s band is everything below the first peak at
    #  `ell = 220`, which is wider than this order's `100..207`.  Stated here because the two counts
    #  sit beside each other in this seat's own record and would otherwise read as a contradiction.
    print('  ⌗ r7892 counted 13 sub-peak TT bins on a WIDER band (below the first peak at ell=220);')
    print('    this order\'s band is 100..207, which holds %d. Different populations, not a '
          'discrepancy.' % len(inband))
    if len(inband) < 3:
        print('  ⛔ REFUSING: fewer than three TT bins lie inside the band.')
        return 1

    out = {'definition': '(full - no_ISW)/full per plik_lite TT bin, %d<=ell<=%d, unlensed scalar '
                         'TT, reference parameters' % (L_LO, L_HI),
           'no_ISW_is': 'CAMB\'s own ISW source term removed = the TOTAL ISW; the late half is at '
                        'most 2.82e-04 relative here (r7895+cc66.2), so this is the early ISW',
           'binning': 'score_ttteee._bin_one(..., "TT") -- plik_lite\'s own bin_w_TT weights, on '
                      'D_ell = ell(ell+1)C/2pi',
           'reference': ref, 'sums_eV': list(SUMS), 'band': [L_LO, L_HI],
           'subpeak_count_note': 'r7892 counted 13 TT bins below the first peak at ell=220; this band (100..207) holds %d -- different populations' % len(inband),
           'bin_ell_lo': [int(x) for x in lo[inband]], 'bin_ell_hi': [int(x) for x in hi[inband]],
           'per_sum': {}}

    shares = {}
    for s in SUMS:
        L = _isw.legs(ref['H0'], ref['OM'], ref['WB'], ref['NS'], s)
        bf, bn = tt_bins(L['T'])[inband], tt_bins(L['Tno'])[inband]
        sh = (bf - bn) / bf
        shares[s] = sh
        agg = float((bf.sum() - bn.sum()) / bf.sum())
        out['per_sum']['%.2f' % s] = dict(
            share_per_bin=[float(x) for x in sh], aggregate=agg,
            min=float(sh.min()), max=float(sh.max()),
            falling=bool(np.all(np.diff(sh) < 0)),
            all_positive=bool(np.all(sh > 0)),
            spearman_sign=int(np.sign(np.corrcoef(np.arange(len(sh)), sh)[0, 1])))
        print('  Sum=%.2f  aggregate %.4f   per-bin %.4f..%.4f   all positive %s   '
              'monotone falling %s' % (s, agg, sh.min(), sh.max(),
                                       out['per_sum']['%.2f' % s]['all_positive'],
                                       out['per_sum']['%.2f' % s]['falling']), flush=True)

    M = np.vstack([shares[s] for s in SUMS])
    spread = M.max(axis=0) - M.min(axis=0)
    out['per_bin_spread_across_sums'] = [float(x) for x in spread]
    out['worst_spread'] = float(spread.max())
    aggs = [out['per_sum']['%.2f' % s]['aggregate'] for s in SUMS]

    print()
    print('  ' + '-' * 96)
    print('  THE THREE REGISTERED CLAIMS, SCORED')
    print('  ' + '-' * 96)
    c1 = all(AGG_LO <= a <= AGG_HI for a in aggs)
    c2a = all(out['per_sum']['%.2f' % s]['all_positive'] for s in SUMS)
    c2b = all(out['per_sum']['%.2f' % s]['falling'] for s in SUMS)
    c3 = bool(spread.max() < SPREAD_BAR)
    out['claims'] = {'Ⓒ①_aggregate_0.44_pm_0.05': bool(c1),
                     'Ⓒ②_positive_every_bin': bool(c2a),
                     'Ⓒ②_falling_with_ell': bool(c2b),
                     'Ⓒ③_spread_under_0.02': c3}
    print('  Ⓒ① aggregate 0.44 ± 0.05 at every sum          : %s   (%s)'
          % ('HOLDS' if c1 else 'REFUTED', ', '.join('%.4f' % a for a in aggs)))
    print('  Ⓒ② positive in every bin                       : %s' % ('HOLDS' if c2a else 'REFUTED'))
    print('  Ⓒ② FALLING with ell across the band            : %s' % ('HOLDS' if c2b else 'REFUTED'))
    print('  Ⓒ③ per-bin spread across sums under %.2f        : %s   (worst %.4f)'
          % (SPREAD_BAR, 'HOLDS' if c3 else 'REFUTED', spread.max()))
    print()
    json.dump(out, open(os.path.join(HERE, 'early_isw_share.json'), 'w'), indent=1)
    print('  banked: early_isw_share.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
