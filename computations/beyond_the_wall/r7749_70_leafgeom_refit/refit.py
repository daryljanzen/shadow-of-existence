"""r7749+70: the leaf-rate-distance arm (arm of record + LEAFGEOM=1), scored exactly as the arm of record is.

Usage:  python3 refit.py A <nofit.npz>          score the no-fit run at the distances' point (Ⓐ, with K1/K2)
        python3 refit.py B                       linearised minimum on the one-clock leafrec1 grid (Ⓑ)
        python3 refit.py V <verify.npz>          score the verify run at Ⓑ's minimum

Scoring is `r7643_70_distances_point/measure.py`'s: P15's CAMB lensing operator on both arms,
`chi2_of_spectrum.chi2_of`, 185 lensed bins.  The fit is `r7641_cc66_grid_readers/full_range_refit_on_the_arm_of_record.py`'s
`build` / `chi2_at` / `fit` (copied verbatim in substance: same STEP, same lensing, same amplitude solve,
same Nelder-Mead), pointed at `r7093_directions/grid_oneclock_leafrec1`.
"""
import json
import os
import sys

import numpy as np
import scipy.linalg
from scipy.optimize import minimize

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(BW))
SP = os.path.join(BW, 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import camb                                                                # noqa: E402
import chi2_of_spectrum as CS                                              # noqa: E402

_p = camb.set_params(H0=67.40, ombh2=0.02237, omch2=0.3150 * 0.674 ** 2 - 0.02237,
                     mnu=0.06, omk=0, tau=0.054, As=2.1e-9, ns=0.965, lmax=3000)
_cl = camb.get_results(_p).get_cmb_power_spectra(_p, CMB_unit='muK', lmax=3000)
_le, _un = _cl['total'][:, 0], _cl['unlensed_scalar'][:, 0]
LG = np.arange(len(_le), dtype=float)
RATIO = np.ones_like(_le)
RATIO[_un > 0] = _le[_un > 0] / _un[_un > 0]
STEP = dict(H0=2.0, OM=0.0150, WB=0.0008, NS=0.020)
CENTRE = dict(H0=68.570730, OM=0.291246, WB=0.021643, NS=1.015066)
GRID = os.path.join(BW, 'r7093_directions', 'grid_oneclock_leafrec1')
OUT = os.path.join(HERE, 'figures.json')


def score(path):
    z = np.load(path)
    ls, Dl = np.asarray(z['ls'], float), np.asarray(z['Dl'], float)
    c, nb = CS.chi2_of(ls, Dl * np.interp(ls, LG, RATIO))[:2]
    return float(c), int(nb)


def binned(ls, Dl):
    return CS.bin_spectrum(ls, Dl * np.interp(ls, LG, RATIO))


def build():
    z = np.load(os.path.join(GRID, 'cr_base.npz'))
    m0 = binned(np.asarray(z['ls'], float), np.asarray(z['Dl'], float))
    ok = np.isfinite(m0)
    F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(CS.COV_TT[np.ix_(ok, ok)]), np.identity(int(ok.sum())))
    F = 0.5 * (F + F.T)
    mb = m0[ok]
    g, h = {}, {}
    for k in STEP:
        zp, zm = np.load(os.path.join(GRID, f'cr_{k}p.npz')), np.load(os.path.join(GRID, f'cr_{k}m.npz'))
        mp = binned(np.asarray(zp['ls'], float), np.asarray(zp['Dl'], float))[ok]
        mm = binned(np.asarray(zm['ls'], float), np.asarray(zm['Dl'], float))[ok]
        g[k] = (mp - mm) / (2 * STEP[k])
        h[k] = (mp - 2 * mb + mm) / STEP[k] ** 2
    return dict(m0=mb, ok=ok, F=F, d=CS.X_DATA[ok], g=g, h=h)


def chi2_at(B, x):
    m = B['m0'].copy()
    for k, v in zip(STEP, x):
        m = m + B['g'][k] * v + 0.5 * B['h'][k] * v * v
    if np.any(m <= 0):
        return 1e12
    A = float((m @ B['F'] @ B['d']) / (m @ B['F'] @ m))
    r = B['d'] - A * m
    return float(r @ B['F'] @ r)


def load():
    return json.load(open(OUT)) if os.path.exists(OUT) else {}


def save(d):
    json.dump(d, open(OUT, 'w'), indent=1)


def main():
    mode = sys.argv[1]
    F = load()
    ctl_nofit = score(os.path.join(SP, 'cc66_lcdm_L2000.npz'))
    ctl_refit = score(os.path.join(SP, 'cc66_r185_verify_lcdm.npz'))
    aor_nofit = score(os.path.join(SP, 'cc66_cr_x_h686_L2000_leafrec1_distances.npz'))
    aor_refit = score(os.path.join(SP, 'cc66_r185_verify_cr_leafrec1.npz'))
    K1 = abs(ctl_nofit[0] - 214.1) < 0.05 and abs(ctl_refit[0] - 186.5) < 0.05
    K2 = abs(aor_nofit[0] - 502.1) < 0.05
    print(f'K1 control 214.1/186.5 -> {ctl_nofit[0]:.2f}/{ctl_refit[0]:.2f}: {K1}')
    print(f'K2 arm of record no-fit 502.1 -> {aor_nofit[0]:.2f}: {K2}')
    if not (K1 and K2):
        raise SystemExit('a closure failed -- REFUSING')
    F.update(control_nofit=ctl_nofit[0], control_refit=ctl_refit[0], aor_nofit=aor_nofit[0], aor_refit=aor_refit[0])
    if mode == 'A':
        c, nb = score(sys.argv[2])
        assert nb == 185
        F['A'] = dict(chi2=c, per_bin=c / nb, ratio=c / ctl_nofit[0])
        print(f'A no-fit LEAFGEOM=1: chi2 {c:.1f}  /bin {c / nb:.2f}  x control {c / ctl_nofit[0]:.3f}  '
              f'(arm of record {aor_nofit[0]:.1f}, {aor_nofit[0] / 185:.2f}/bin, {aor_nofit[0] / ctl_nofit[0]:.3f}x)')
    elif mode == 'B':
        B = build()
        c0 = chi2_at(B, np.zeros(4))
        r = minimize(lambda x: chi2_at(B, x), np.zeros(4), method='Nelder-Mead',
                     options=dict(xatol=1e-4, fatol=1e-3, maxiter=4000))
        pt = {k: CENTRE[k] + v for k, v in zip(STEP, r.x)}
        steps = {k: float(v / STEP[k]) for k, v in zip(STEP, r.x)}
        F['B'] = dict(chi2_base=c0, chi2_model_min=float(r.fun), point=pt, offset_in_steps=steps)
        print(f'B grid base chi2 {c0:.2f};  linearised minimum {r.fun:.2f} at {pt}')
        print(f'  offsets in grid steps: {steps}  (|offset| <= 1 is inside the grid)')
    elif mode == 'V':
        c, nb = score(sys.argv[2])
        F['V'] = dict(chi2=c, per_bin=c / nb, ratio=c / ctl_refit[0],
                      model_minus_run=F['B']['chi2_model_min'] - c)
        print(f'V verify run: chi2 {c:.2f}  /bin {c / nb:.2f}  x control {c / ctl_refit[0]:.3f}  '
              f'(model said {F["B"]["chi2_model_min"]:.2f}; arm of record refit {aor_refit[0]:.1f}, '
              f'{aor_refit[0] / ctl_refit[0]:.3f}x)')
    save(F)


if __name__ == '__main__':
    main()
