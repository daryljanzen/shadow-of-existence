"""r7813+70 ①: the control's P1/P2 at Planck 2018's point, at KFAC 2 and 3, against CAMB there.

Reads the summed banks this directory's `bank.py` writes (`out/control_planck2018_kfac{2,3}.npz`),
locates peaks through P15's own matched locator -- `_sweep` of `P15_at_its_own_preferred_H0_...`,
IMPORTED from that receipt, not copied -- and runs CAMB at the same point through the same locator.
Registered in PREDICTION.md before any run.  Writes out/SUMMARY.json.

Run: python3 measure.py      (numpy, scipy, camb; about a minute)
"""
import contextlib
import io
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(BW))
OUT = os.path.join(HERE, 'out')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import camb                                                                    # noqa: E402
import chi2_of_spectrum as CS                                                  # noqa: E402

COMB = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                    'P15_at_its_own_preferred_H0_the_crossing_arm_predicts_the_acoustic_comb_'
                    'with_no_fitted_number.py')
_ns = {'__name__': '__r7813_locator__', '__file__': COMB}
with contextlib.redirect_stdout(io.StringIO()):
    try:
        exec(compile(open(COMB, encoding='utf-8').read(), COMB, 'exec'), _ns)
    except SystemExit:
        pass
_sweep, _FACB, _WS = _ns['_sweep'], _ns['_FACB'], _ns['_WS']

H0, WB, WC, NS, TAU = 67.36, 0.02237, 0.1200, 0.9649, 0.0544


def camb_tt(mnu):
    kw = dict(H0=H0, ombh2=WB, omch2=WC, ns=NS, tau=TAU, As=2.1e-9, omk=0, lmax=3000)
    if mnu > 0:
        p = camb.set_params(mnu=mnu, **kw)
    else:
        p = camb.set_params(mnu=0.0, num_massive_neutrinos=0, **kw)
    cl = camb.get_results(p).get_cmb_power_spectra(p, CMB_unit='muK', lmax=3000)
    return cl['total'][:, 0], cl['unlensed_scalar'][:, 0]


def located(ls, Dl):
    s = _sweep(CS.bin_spectrum(ls, Dl) * _FACB)
    return dict(pk=[float(x) for x in s['pk']], p12=s['p12'], p13=s['p13'], nW=s['nW'])


LEN06, UNL06 = camb_tt(0.06)
LEN00, UNL00 = camb_tt(0.0)
LG = np.arange(len(LEN06), dtype=float)
RATIO = np.ones_like(LEN06)
RATIO[UNL06 > 0] = LEN06[UNL06 > 0] / UNL06[UNL06 > 0]
LC = np.arange(2, 2501, dtype=float)

R = {'locator': f'_sweep of {os.path.basename(COMB)}, windows {list(_WS)}',
     'point': dict(H0=H0, ombh2=WB, omch2=WC, ns=NS, tau=TAU)}
R['camb'] = {
    'lensed_mnu0.06': located(LC, LEN06[2:2501]),
    'unlensed_mnu0.06': located(LC, UNL06[2:2501]),
    'lensed_mnu0': located(LC, LEN00[2:2501]),
    'unlensed_mnu0': located(LC, UNL00[2:2501]),
}
for kf in (2, 3):
    fn = os.path.join(OUT, f'control_planck2018_kfac{kf}.npz')
    with np.load(fn) as z:
        ls, Dl = np.asarray(z['ls'], float), np.asarray(z['Dl'], float)
    R[f'kfac{kf}'] = {'lensed': located(ls, Dl * np.interp(ls, LG, RATIO)),
                      'unlensed': located(ls, Dl)}

# the r7807 bank, through the same locator, for prediction (1)
P7807 = os.path.join(BW, 'r7807_cc66_the_23_items_and_the_repointed_control', 'out',
                     'r7807_control_planck2018_L2000.npz')
with np.load(P7807) as z:
    l7, D7 = np.asarray(z['ls'], float), np.asarray(z['Dl'], float)
with np.load(os.path.join(OUT, 'control_planck2018_kfac2.npz')) as z:
    l2, D2 = np.asarray(z['ls'], float), np.asarray(z['Dl'], float)
same = np.array_equal(l7, l2)
R['reproduces_r7807'] = dict(same_ls=bool(same),
                             max_rel=float(np.max(np.abs(D2 / D7 - 1))) if same else None)

c = R['camb']['lensed_mnu0.06']['p12']
for kf in (2, 3):
    for mode, cref in (('lensed', 'lensed_mnu0.06'), ('unlensed', 'unlensed_mnu0.06')):
        R[f'kfac{kf}'][mode]['agree_pct_vs_camb'] = \
            100 * (R[f'kfac{kf}'][mode]['p12'] / R['camb'][cref]['p12'] - 1)
R['kfac_move_pct'] = {m: 100 * (R['kfac3'][m]['p12'] / R['kfac2'][m]['p12'] - 1)
                      for m in ('lensed', 'unlensed')}
R['camb_mnu_move_pct'] = 100 * (R['camb']['lensed_mnu0']['p12'] / c - 1)

print(json.dumps(R, indent=1))
with open(os.path.join(OUT, 'SUMMARY.json'), 'w') as f:
    json.dump(R, f, indent=1)
