#!/usr/bin/env python3
"""The parameter refit on the FULL RANGE -- 185 bins, ell 100-1996 -- built on a measured
response rather than a search.  r6801+cc66.23, at the chat seat's order (1) of r6801.

** WHAT THE FULL RANGE BUYS, AND IT IS THE WHOLE REASON FOR THE SIX HOURS. **  The 132-bin run
stopped at ell 1287, which is BELOW the damping tail -- and the tail is where omega_b and n_s have
their leverage.  *Those were named as the two loosest parameters of that fit; this is the run that
tightens them, and it is also the run that says whether the background still sits where the
distances put it once the tail is in the fit.*

** WHY A RESPONSE MODEL AND NOT A SEARCH. **  Each likelihood call is a full LMAXL=2000 spectrum,
~40-120 min.  A six-parameter search is thousands of those and is not doable.  But the parameters
are not equal:

  A_s    fitted in CLOSED FORM by chi2_of -- free, zero cost.
  tau    EXACTLY degenerate with A_s on ell >= 100 (no reionisation is modelled, so exp(-2 tau) is
         a constant).  Measured at r6760+cc66.14: chi2 identical to 1e-6 over tau = 0 to 0.15.
         ** Not a direction of this fit. **
  n_s, omega_b, Omega_m, H0   real directions; two-sided finite differences give the gradient AND
         the diagonal curvature, so the model is quadratic along each axis.

** THERE IS NO LSTEP SHORTCUT HERE: base and derivatives are BOTH at LSTEP=8, LMAXL=2000, KFAC
at the corpus default 2.0. **  *The binning is what puts them on a common footing -- plik_lite's
bins are weighted sums over every ell, so a strided sample is interpolated onto the full grid
before binning and never compared stride-to-stride.*

** WHAT THIS CANNOT DO: CROSS TERMS. **  Two-sided steps along each axis give no off-diagonal
curvature, so the model is separable.  *That is stated, and it is why the minimum is VERIFIED with
a real run rather than reported from the model.*
"""
import os
import sys

import numpy as np
import scipy.linalg
from scipy.optimize import minimize
from scipy.signal import argrelextrema

sys.path.insert(0, '/home/user/shadow-of-existence/computations/planck_tt_likelihood')
import chi2_of_spectrum as CS

D = '/tmp/n66/refit185'
SPEC = '/home/user/shadow-of-existence/computations/beyond_the_wall/spectra'
SKY = np.array([220.4, 537.7, 817.3, 1123.9])
STEP = dict(H0=2.0, OM=0.0150, WB=0.0008, NS=0.020)
# ** THE BASE IS THE GRID'S OWN, NOT THE BANKED LENSED SPECTRUM -- 66's ruling, r6788. **
# *"The comparison must be like-for-like: the control refitted with the same six parameters on the
# same 132 bins, not the banked lensed control."*  So both arms' m0 come from THIS grid, at the
# same LMAXL, LSTEP and k-reach as the derivatives that act on them.  Using the banked LMAXL=2000
# base would have applied 132-bin derivatives to a 185-bin base -- two different objects.
ARMS = {
    'control (LCDM)': dict(tag='lcdm', base=f'{D}/lcdm_base.npz',
                           th0=dict(H0=67.40, OM=0.3150, WB=0.0224, NS=0.965)),
    'CR, crossing':   dict(tag='cr', base=f'{D}/cr_base.npz',
                           th0=dict(H0=68.60, OM=0.2973, WB=0.0224, NS=0.965)),
}


def lens_ratio():
    lg, r = np.load('/tmp/n66/lens_ratio.npy')
    return lg, r


LG, RATIO = lens_ratio()


def fit_comb(pk, n=3):
    nn = np.arange(1, n + 1, dtype=float)
    A = np.vstack([nn, np.ones_like(nn)]).T
    lA, b = np.linalg.lstsq(A, np.asarray(pk[:n], float), rcond=None)[0]
    return float(lA), float(np.pi * b / lA)


LENS = os.environ.get('LENS', '1') == '1'


def binned(ls, Dl):
    """Bin the spectrum, lensed by default.

    ** BOTH ARE REPORTED. **  Lensing is LCDM's operator imposed on both arms alike, so it cannot
    favour either; but it is a smoothing, and on a range that stops at ell 1287 it does less work
    than on the full one.  *Reporting the refit both ways is cheap and says how much of the answer
    is the operator's.*
    """
    return CS.bin_spectrum(ls, Dl * np.interp(ls, LG, RATIO) if LENS else Dl)


def build(arm):
    z = np.load(arm['base'])
    ls = np.asarray(z['ls'], float)
    m0 = binned(ls, np.asarray(z['Dl'], float))
    ok = np.isfinite(m0)
    F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(CS.COV_TT[np.ix_(ok, ok)]),
                               np.identity(int(ok.sum())))
    F = 0.5 * (F + F.T)
    d = CS.X_DATA[ok]
    # derivatives, on the coarse grid, binned the same way -- binning is what puts them on a
    # common footing, so the LSTEP difference never has to be interpolated in ell at all.
    g, h = {}, {}
    for k in STEP:
        zp = np.load(f"{D}/{arm['tag']}_{k}p.npz")
        zm = np.load(f"{D}/{arm['tag']}_{k}m.npz")
        zb = np.load(arm['base'])
        mp = binned(np.asarray(zp['ls'], float), np.asarray(zp['Dl'], float))[ok]
        mm = binned(np.asarray(zm['ls'], float), np.asarray(zm['Dl'], float))[ok]
        mb = binned(np.asarray(zb['ls'], float), np.asarray(zb['Dl'], float))[ok]
        g[k] = (mp - mm) / (2 * STEP[k])
        h[k] = (mp - 2 * mb + mm) / STEP[k] ** 2
    return dict(ls=ls, m0=m0[ok], ok=ok, F=F, d=d, g=g, h=h, th0=arm['th0'])


def model(B, dth):
    m = B['m0'].copy()
    for k, v in dth.items():
        m = m + B['g'][k] * v + 0.5 * B['h'][k] * v * v
    return m


def chi2_at(B, x):
    dth = dict(zip(STEP, x))
    m = model(B, dth)
    if np.any(m <= 0):
        return 1e12
    A = float((m @ B['F'] @ B['d']) / (m @ B['F'] @ m))
    r = B['d'] - A * m
    return float(r @ B['F'] @ r)


if __name__ == '__main__':
    need = [f"{a['tag']}_{s}" for a in ARMS.values() for s in
            ['base'] + [f'{k}{sg}' for k in STEP for sg in 'pm']]
    miss = [n for n in need if not os.path.exists(f'{D}/{n}.npz')]
    if miss:
        print(f"  waiting on {len(miss)} of {len(need)} runs: {', '.join(miss[:6])}"
              f"{' ...' if len(miss) > 6 else ''}")
        sys.exit(2)
    print("=" * 104)
    print("  THE PARAMETER REFIT -- both arms, 185 bins, ell 100-1996, lensing switchable (LENS=1 default)")
    print("=" * 104)
    for nm, arm in ARMS.items():
        B = build(arm)
        n = int(B['ok'].sum())
        c0 = chi2_at(B, np.zeros(4))
        r = minimize(lambda x: chi2_at(B, x), np.zeros(4), method='Nelder-Mead',
                     options=dict(xatol=1e-4, fatol=1e-3, maxiter=4000))
        th = {k: B['th0'][k] + v for k, v in zip(STEP, r.x)}
        print(f"\n  {nm}   ({n} bins)")
        print(f"    {'':>10} {'start':>10} {'best fit':>10} {'moved':>10} {'in steps':>9}")
        for i, k in enumerate(STEP):
            print(f"    {k:>10} {B['th0'][k]:>10.4f} {th[k]:>10.4f} {r.x[i]:>+10.4f} "
                  f"{r.x[i] / STEP[k]:>+8.2f}s")
        print(f"    chi^2  as-computed {c0:>9.1f} ({c0 / n:.2f}/bin)   "
              f"refitted {r.fun:>9.1f} ({r.fun / n:.2f}/bin)   d = {r.fun - c0:+.1f}")
        np.save(f"{D}/best_{arm[chr(39)+chr(116)+chr(97)+chr(103)+chr(39)] if False else arm['tag']}_{'L' if LENS else 'U'}.npy", np.array([th[k] for k in STEP]))
