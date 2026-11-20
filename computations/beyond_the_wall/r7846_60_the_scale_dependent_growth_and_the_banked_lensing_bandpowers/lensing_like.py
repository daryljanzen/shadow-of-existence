#!/usr/bin/env python3
"""** THE NINE BANKED LENSING BANDPOWERS, SCORED WITH NO AMPLITUDE FITTED TO THEM. **

Order `r7845` ②, and registered arm `Ⓓ④`.  The bandpowers are Planck 2018 conservative, banked by
node `70` at `r7471` with their `9 x 9` covariance and nine windows; `r7844` found them after two
seats had carried the claim that the measurement was missing.

** WHY NO AMPLITUDE IS FITTED HERE, AND WHY THAT IS THE WHOLE POINT. **  Every mode of this
instrument's solve starts at `Phi = -1`, so the CMB spectra and the lensing potential share ONE
primordial normalisation.  Reionisation screens the high-`l` CMB by `exp(-2 tau)` and does not
screen the lensing potential:

    CMB    = AMP * exp(-2 tau) * shape_cmb
    phiphi = AMP              * shape_phiphi

The CMB fit already determines `AMP * exp(-2 tau)`.  So the lensing prediction is that same fitted
number multiplied by `exp(+2 tau)` -- and `tau` therefore cannot cancel.  *Fitting a second
amplitude to the lensing data would throw exactly that away, which is what `Ⓓ④`'s reachable
negative names.*  ⇒ So this module takes a model vector and returns a `chi^2`.  It solves nothing.

** THE COVARIANCE IS INVERTED ONCE, AT IMPORT. **  It is `9 x 9` and fixed; inverting it inside a
likelihood call would be a million needless factorisations in a chain.

`Ⓕ⑥`: the `tau` prior is `0.054 +/- 0.007`, which is **not invented here** -- it is the stand-in
node `70` used at `r7471` for the low-`l` EE data this repository does not hold, and `r7844`
confirmed that absence against the likelihood's own `FileNotFoundError`.  It is a STAND-IN for data
and is reported as one.
"""
import os

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
LENS = os.path.join(os.path.dirname(_HERE), 'r7471_70_PO24_tilt_off_the_tail', 'lensing')

_lb = np.loadtxt(os.path.join(LENS, 'x_bandpowers.dat'))
L_MIN = _lb[:, 1].astype(int)
L_MAX = _lb[:, 2].astype(int)
L_AV = _lb[:, 3]
DATA = _lb[:, 4]
ERR = _lb[:, 5]
AHAT = _lb[:, 6]
COV = np.loadtxt(os.path.join(LENS, 'x_cov.dat'))
COV = 0.5 * (COV + COV.T)
FISHER = np.linalg.inv(COV)
FISHER = 0.5 * (FISHER + FISHER.T)
NBP = len(DATA)

WINDOWS = []
for _i in range(1, NBP + 1):
    _w = np.loadtxt(os.path.join(LENS, 'win', f'window{_i}.dat'))
    WINDOWS.append((_w[:, 0].astype(int), _w[:, 1]))

TAU_MEAN = 0.054
TAU_SIGMA = 0.007
SOURCE = 'Planck 2018 conservative, banked at r7471+70; the tau prior is 70\'s own stand-in'


def chi2(model):
    """(d - m)^T F (d - m) over the nine bandpowers.  ** NO AMPLITUDE IS SOLVED IN HERE. **"""
    m = np.asarray(model, float)
    if m.shape != (NBP,):
        raise ValueError(f'the lensing model wants {NBP} bandpowers, got {m.shape}')
    if not np.all(np.isfinite(m)):
        return 1e12
    r = DATA - m
    return float(r @ FISHER @ r)


def chi2_tau(tau):
    """the `tau` prior as an additive term: `((tau - 0.054)/0.007)^2`, 70's stand-in at r7471"""
    return float(((float(tau) - TAU_MEAN) / TAU_SIGMA) ** 2)


def bandpowers_from(ls, cl):
    """bin a `C_L^phiphi` through the nine windows, in the data's own convention

    ** `[L(L+1)]^2 C_L^phiphi / (2 pi)`, read off `r7471`'s own scoring code. **  `r7846` first
    binned raw `C_L^phiphi` and the normalisation check caught it as a factor `1.9e5` drift rising
    with `L`, which is what a missing `L^4` looks like.
    """
    from scipy.interpolate import CubicSpline
    spl = CubicSpline(np.asarray(ls, float), np.asarray(cl, float))
    out = []
    for L, w in WINDOWS:
        Lf = L.astype(float)
        out.append(float(np.sum(w * spl(L) * (Lf * (Lf + 1.0)) ** 2 / (2.0 * np.pi))))
    return np.asarray(out)


def describe():
    return dict(nbandpowers=int(NBP), L_min=int(L_MIN[0]), L_max=int(L_MAX[-1]),
                L_av=[float(v) for v in L_AV], data=[float(v) for v in DATA],
                error=[float(v) for v in ERR], ahat=[float(v) for v in AHAT],
                fractional_error=[float(e / d) for e, d in zip(ERR, DATA)],
                cov_symmetric_to=float(np.max(np.abs(COV - COV.T))),
                cov_min_eigenvalue=float(np.min(np.linalg.eigvalsh(COV))),
                tau_prior=dict(mean=TAU_MEAN, sigma=TAU_SIGMA, is_a_stand_in_for_data=True,
                               source='r7471+70, standing in for low-l EE'),
                source=SOURCE)


if __name__ == '__main__':
    import json
    d = describe()
    print(json.dumps(d, indent=1, sort_keys=True))
    # the two-sided sanity of the scorer itself: the data scores zero against itself, and a
    # ten-per-cent offset scores something a chain would notice
    print('\n  chi2(data) = %.3e   (must be 0)' % chi2(DATA))
    print('  chi2(1.1 x data) = %.2f   (a ten per cent offset, for scale)' % chi2(1.1 * DATA))
    print('  chi2(fiducial) = %.2f   (the data divided by its own Ahat)' % chi2(DATA / AHAT))
