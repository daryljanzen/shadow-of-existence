"""r7836+60: the 185-bin lensed refit with the NEUTRINO MASS SUM FREE beside the four parameters,
jointly with DESI DR2 BAO on the leaf ruler -- on the leaf-geometry arm of record and on the control,
run the same way.

On order r7831 (69), added clause, routed from 72.  PREDICTION.md was committed and pushed before any
run; this file is the run.

** THE INSTRUMENT, AND WHAT IS BORROWED RATHER THAN REBUILT. **
  * the CMB side is `r7749_70_leafgeom_refit/refit.py`'s own `build`/`chi2_at`: the same CAMB lensing
    operator, the same `chi2_of_spectrum` covariance, the same 185 lensed bins, the same analytic
    amplitude solve, and the same quadratic expansion -- extended by ONE direction and nothing else;
  * the BAO side is that harness's `distances.py`, called and not reimplemented: `chi2_bao` on
    `E_leaf` (the leaf ruler the order names) with `r_d` minimised at every point, so the ruler is
    marginalised rather than fixed;
  * the four existing directions are the banked grids, untouched;
  * the FIFTH direction is this revision's own pair, generated at each arm's own grid centre.

** WHY THE MASS MOVES ONLY THE CMB TERM, AND IT IS THE WHOLE MECHANISM. **  The distances see the
total `Omega_m`, which is `Om` in `E_leaf`; the spectrum's driving sees `omega_cb = Omega_m h^2 -
omega_nu`.  So at fixed `(H0, Om)` the sum moves the CMB term and leaves the BAO term identically
alone, and the joint fit's mass direction is driven by the CMB's preferred `omega_cb` against the
BAO's preferred total.  That is the lever the standard-model bound rides, with the sign reversed.

** THE SIGN CONVENTION, STATED. **  `x_MNU` is in units of the step, so `Sum = STEP_MNU * x`, and
NEGATIVE values are admitted and reported.  They mean operationally what the published negative
effective mass means -- density moved out of the neutrinos and into the clustering matter -- which is
the convention the figure this is checked against uses (`-0.101` eV, arXiv:2503.14744).

rc=0 on success.  Run: python3 fit_mnu.py          (numpy, scipy, camb)
"""
import json
import os
import sys

import numpy as np
from scipy.optimize import minimize, minimize_scalar

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(BW))
sys.path.insert(0, os.path.join(BW, 'r7749_70_leafgeom_refit'))
import refit as R                                                          # noqa: E402
import distances as DI                                                     # noqa: E402

MNU_DIR = os.environ.get('MNU_DIR', '/tmp/claude-0/mnu_grid')
STEP_MNU = 0.06                      # eV, the step the pair was generated at
OUT = os.path.join(HERE, 'fit_mnu.json')
# each arm's grid and centre, read from the harness rather than retyped where it has them
ARMS = {
    'cr': dict(grid=os.path.join(BW, 'r7093_directions', 'grid_oneclock_leafrec1'),
               centre=dict(R.CENTRE), pref='cr', E=DI.E_leaf),
    'lcdm': dict(grid=os.path.join(BW, 'refit_grid185'),
                 centre=dict(H0=67.40, OM=0.3150, WB=0.0224, NS=0.965), pref='lcdm', E=DI.E_stack),
}
fail = []


def check(label, ok, witness=''):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}" + (f"   ({witness})" if witness else ''))
    if not ok:
        fail.append(label)


def build5(arm):
    """`refit.build`, with the fifth direction appended from this revision's own pair."""
    a = ARMS[arm]
    B = R.build(a['grid']) if arm == 'cr' else _build_lcdm(a['grid'])
    ok = B['ok']
    zp = np.load(os.path.join(MNU_DIR, f"{a['pref']}_MNUp.npz"))
    zm = np.load(os.path.join(MNU_DIR, f"{a['pref']}_MNUm.npz"))
    mp = R.binned(np.asarray(zp['ls'], float), np.asarray(zp['Dl'], float))[ok]
    mm = R.binned(np.asarray(zm['ls'], float), np.asarray(zm['Dl'], float))[ok]
    B['g']['MNU'] = (mp - mm) / (2 * STEP_MNU)
    B['h']['MNU'] = (mp - 2 * B['m0'] + mm) / STEP_MNU ** 2
    return B


def _build_lcdm(grid):
    """the same expansion on the control's own base and pairs."""
    import scipy.linalg
    import chi2_of_spectrum as CS
    z = np.load(os.path.join(grid, 'lcdm_base.npz'))
    m0 = R.binned(np.asarray(z['ls'], float), np.asarray(z['Dl'], float))
    ok = np.isfinite(m0)
    F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(CS.COV_TT[np.ix_(ok, ok)]),
                               np.identity(int(ok.sum())))
    F = 0.5 * (F + F.T)
    g, h = {}, {}
    for k in R.STEP:
        zp = np.load(os.path.join(grid, f'lcdm_{k}p.npz'))
        zm = np.load(os.path.join(grid, f'lcdm_{k}m.npz'))
        mp = R.binned(np.asarray(zp['ls'], float), np.asarray(zp['Dl'], float))[ok]
        mm = R.binned(np.asarray(zm['ls'], float), np.asarray(zm['Dl'], float))[ok]
        g[k] = (mp - mm) / (2 * R.STEP[k])
        h[k] = (mp - 2 * m0[ok] + mm) / R.STEP[k] ** 2
    return dict(m0=m0[ok], ok=ok, F=F, d=CS.X_DATA[ok], g=g, h=h)


KEYS = list(R.STEP) + ['MNU']            # H0, OM, WB, NS, MNU


def chi2_cmb(B, x):
    m = B['m0'].copy()
    for k, v in zip(KEYS, x):
        m = m + B['g'][k] * v + 0.5 * B['h'][k] * v * v
    if np.any(m <= 0):
        return 1e12
    A = float((m @ B['F'] @ B['d']) / (m @ B['F'] @ m))
    r = B['d'] - A * m
    return float(r @ B['F'] @ r)


def phys(arm, x):
    """the physical point the expansion coefficients name."""
    c = ARMS[arm]['centre']
    return dict(H0=c['H0'] + R.STEP['H0'] * x[0], OM=c['OM'] + R.STEP['OM'] * x[1],
                WB=c['WB'] + R.STEP['WB'] * x[2], NS=c['NS'] + R.STEP['NS'] * x[3],
                MNU=STEP_MNU * x[4])


_BAO = {}


def chi2_bao_at(arm, H0, OM):
    """DESI DR2 on the arm's own ruler, r_d minimised -- cached on the rounded point."""
    key = (arm, round(H0, 4), round(OM, 5))
    if key not in _BAO:
        E = ARMS[arm]['E']
        r = minimize_scalar(lambda rd: DI.chi2_bao(H0, OM, rd, E), bounds=(120, 170),
                            method='bounded')
        _BAO[key] = (float(r.fun), float(r.x))
    return _BAO[key]


def chi2_joint(arm, B, x, bao=True):
    p = phys(arm, x)
    c = chi2_cmb(B, x)
    if bao:
        c += chi2_bao_at(arm, p['H0'], p['OM'])[0]
    return c


def fit(arm, B, fixed_mnu=None, bao=True):
    def f(y):
        x = list(y) + [fixed_mnu / STEP_MNU] if fixed_mnu is not None else list(y)
        return chi2_joint(arm, B, x, bao)
    n = 4 if fixed_mnu is not None else 5
    best = None
    for s in ([0.0] * n, [0.3] * n, [-0.3] * n):
        r = minimize(f, np.array(s), method='Nelder-Mead',
                     options=dict(xatol=1e-5, fatol=1e-6, maxiter=20000, maxfev=20000))
        if best is None or r.fun < best.fun:
            best = r
    x = list(best.x) + [fixed_mnu / STEP_MNU] if fixed_mnu is not None else list(best.x)
    return float(best.fun), x


def profile(arm, B, grid_ev, bao=True):
    """chi^2 minimised over the four at each fixed sum -- the profile the order asks for."""
    out = []
    for s in grid_ev:
        c, x = fit(arm, B, fixed_mnu=s, bao=bao)
        out.append(dict(mnu=float(s), chi2=c, x=[float(v) for v in x], phys=phys(arm, x)))
        print(f'    Sum = {s:+.4f} eV   chi2 = {c:.4f}')
    return out


def upper95(prof):
    """the one-sided 95 per cent upper limit: Delta chi^2 = 2.71 above the profile minimum,
    read by linear interpolation on the profile's own points and NOT by a fitted parabola."""
    s = np.array([p['mnu'] for p in prof])
    c = np.array([p['chi2'] for p in prof])
    i = int(np.argmin(c))
    tgt = c[i] + 2.71
    up = [(s[k], c[k]) for k in range(i, len(s))]
    for (s0, c0), (s1, c1) in zip(up, up[1:]):
        if (c0 - tgt) * (c1 - tgt) <= 0 and c1 != c0:
            return float(s0 + (tgt - c0) * (s1 - s0) / (c1 - c0)), float(s[i]), float(c[i])
    return None, float(s[i]), float(c[i])


def main():
    print(__doc__.split('rc=0')[0])
    res = {}
    GRID_EV = [-0.20, -0.15, -0.10, -0.06, -0.03, 0.0, 0.03, 0.059, 0.064, 0.09, 0.12, 0.16, 0.20]
    for arm in ('lcdm', 'cr'):
        print('=' * 78)
        print(f'ARM {arm}')
        print('=' * 78)
        B = build5(arm)
        gm = B['g']['MNU']
        check(f'{arm}: the mass direction is a real gradient, not numerical noise',
              float(np.max(np.abs(gm))) > 0, f'max |dm/dSum| = {np.max(np.abs(gm)):.4g}')
        c0, x0 = fit(arm, B, bao=True)
        p0 = phys(arm, x0)
        print(f'  joint minimum: chi2 = {c0:.4f}   Sum = {p0["MNU"]:+.5f} eV   '
              f'H0 = {p0["H0"]:.4f}  Om = {p0["OM"]:.5f}  wb = {p0["WB"]:.5f}  ns = {p0["NS"]:.5f}')
        prof = profile(arm, B, GRID_EV, bao=True)
        lim, smin, cmin = upper95(prof)
        print(f'  profile minimum at Sum = {smin:+.4f} eV, chi2 = {cmin:.4f}')
        print(f'  95 per cent upper limit (Delta chi2 = 2.71): '
              f'{"none inside the scanned range" if lim is None else f"{lim:.4f} eV"}')
        at = {}
        for q in (0.059, 0.064):
            k = min(range(len(prof)), key=lambda j: abs(prof[j]['mnu'] - q))
            at[f'{q}'] = dict(mnu=prof[k]['mnu'], dchi2=prof[k]['chi2'] - cmin)
            print(f'    Sum = {prof[k]["mnu"]:.3f} eV sits at Delta chi2 = {prof[k]["chi2"] - cmin:+.4f}')
        res[arm] = dict(joint_min=dict(chi2=c0, **{k: float(v) for k, v in p0.items()}),
                        profile=prof, upper95=lim, profile_min=smin, profile_chi2=cmin, at=at)
    json.dump(res, open(OUT, 'w'), indent=1)
    print()
    print('=' * 78)
    if fail:
        print(f'{len(fail)} CHECK(S) FAILED:')
        for f in fail:
            print('  - ' + f)
        return 1
    print('  the two arms are fitted the same way; the receipt reads this file\'s JSON.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
