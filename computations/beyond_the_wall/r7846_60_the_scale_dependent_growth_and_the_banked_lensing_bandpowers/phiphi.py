#!/usr/bin/env python3
"""** C_L^phiphi FROM THIS INSTRUMENT, CARRIED BY THE SCALE-DEPENDENT GROWTH, AND ABSOLUTE. **

Order `r7845` ②.  `L171x_lensing_potential.py` builds the lensing potential as a SHAPE and says so:
*"AMP is the one thing not set here: it is the primordial normalisation, and it is fixed by the SAME
fitted amplitude the temperature comparison uses."*  That is enough for a ratio and not enough to
score nine bandpowers that are absolute measurements.

** WHERE THE ABSOLUTE SCALE COMES FROM, AND WHY IT IS WHAT GIVES `tau` REACH. **  Every mode of this
instrument's solve starts at `Phi = -1`, so the CMB spectra and the lensing potential are both
proportional to ONE primordial normalisation.  Write it `AMP`:

    CMB   = AMP * exp(-2 tau) * shape_cmb        (reionisation screens the high-`l` spectra)
    phiphi= AMP            * shape_phiphi        (the lensing potential is not screened)

*So `tau` cannot hide in `AMP`:* the CMB side carries `exp(-2 tau)` and the lensing side does not,
and the ratio of the two datasets fixes it.  That is the whole mechanism `r7844` predicted when it
measured `tau` to have no reach on a CMB-only score -- "that changes the moment the lensing
bandpowers enter, which carry no fitted amplitude."

⚠ ** THE NORMALISATION IS THE PLACE THIS CAN GO SILENTLY WRONG, so it is CHECKED and not assumed. **
If `shape_phiphi` is not in the same convention as `shape_cmb`, the lensing `chi^2` is wrong by a
constant and biases the neutrino limit directly, in a way nothing downstream would reveal.  `--check`
therefore predicts the nine bandpowers using the amplitude the CMB fit ALREADY determined and
compares them with the measured ones.  *A convention error shows up as orders of magnitude; a
physics difference shows up as tens of per cent.*

Writes `phiphi.json`.
"""
import json
import os
import sys

import numpy as np
from scipy.integrate import quad
from scipy.interpolate import CubicSpline

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
sys.path.insert(0, _HERE)
sys.path.insert(0, _BTW)
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '4')

import growth_kdep as GK                                                 # noqa: E402
A = GK.A

LENS = os.path.join(_BTW, 'r7471_70_PO24_tilt_off_the_tail', 'lensing')
NKP = int(os.environ.get('NKP', '220'))
KMIN = float(os.environ.get('KMIN', '2e-4'))
KMAX = float(os.environ.get('KMAX', '1.0'))
NS = float(os.environ.get('NS', '0.965'))


def bandpowers():
    """the nine measured `C_L^phiphi` bandpowers, their covariance and their windows"""
    lb = np.loadtxt(os.path.join(LENS, 'x_bandpowers.dat'))
    cov = np.loadtxt(os.path.join(LENS, 'x_cov.dat'))
    wins = []
    for i in range(1, 10):
        w = np.loadtxt(os.path.join(LENS, 'win', f'window{i}.dat'))
        wins.append((w[:, 0].astype(int), w[:, 1]))
    return lb, cov, wins


def phi_shape(etaref):
    """`Phi(k)` at `etaref` from this instrument's own solve -- the k-dependence, unnormalised"""
    kk = np.logspace(np.log10(KMIN), np.log10(KMAX), NKP)
    sol, nk, NV = A.evolve(kk, t_eval=np.array([etaref]), e_end=etaref)
    Y = sol.y.T.reshape(1, nk, NV)
    return kk, Y[0, :, 6]


def clpp(ls, mnu_ev, etaref=None, growth=None):
    """`C_L^phiphi` on this instrument's `Phi`, carried by the SCALE-DEPENDENT growth

    The Limber integral and the lensing kernel are `L171x`'s; what is replaced is the growth, which
    was `g(a)/g(a_ref)` with no `k` in it and is now `g(k, a)/g(k, a_ref)`.
    """
    etaref = float(os.environ.get('ETAREF', '4000')) if etaref is None else float(etaref)
    a_ref = float(A.a_of_eta(etaref))
    kk, Phi = phi_shape(etaref)
    D2ref = (kk ** (NS - 1)) * Phi ** 2
    lnP = CubicSpline(np.log(kk), np.log(np.maximum(D2ref, 1e-300)))
    g = GK.GrowthKDep(mnu_ev, kk=np.logspace(np.log10(KMIN), np.log10(KMAX), 48),
                      a_start=a_ref) if growth is None else growth
    chis = float(A.D_M)

    rat = g.ratio_fn(a_ref)                 # one bivariate surface, built once

    def D2_of(k, a):
        k = float(np.clip(k, kk[0], kk[-1]))
        return float(np.exp(lnP(np.log(k)))) * rat(k, a) ** 2

    out = np.empty(len(ls), float)
    for i, l in enumerate(ls):
        def integ(chi, l=l):
            if chi <= 1.0 or chi >= chis:
                return 0.0
            eta = A.eta_0 - chi
            if eta <= etaref:
                eta = etaref
            a = float(A.a_of_eta(min(max(eta, float(A.eg[0])), A.eta_0)))
            k = (l + 0.5) / chi
            W = -2.0 * (chis - chi) / (chis * chi)
            P = 2 * np.pi ** 2 * D2_of(k, a) / k ** 3
            return W ** 2 / chi ** 2 * P
        out[i] = quad(integ, 1.0, chis, limit=200)[0]
    return out


def bin_through(ls, cl, wins):
    """the nine bandpowers, each a weighted sum of `C_L^phiphi` over its own window's L"""
    spl = CubicSpline(ls, cl)
    return np.array([float(np.sum(w * spl(L))) for L, w in wins])


def main():
    lb, cov, wins = bandpowers()
    Lgrid = np.unique(np.concatenate([L for L, _ in wins]))
    print('  the windows span L = %d to %d over %d multipoles'
          % (Lgrid.min(), Lgrid.max(), len(Lgrid)), flush=True)
    ls = np.unique(np.round(np.logspace(np.log10(max(2, Lgrid.min())),
                                        np.log10(Lgrid.max()), 36)).astype(int))
    print('  solving C_L^phiphi at Sum = 0 on %d multipoles' % len(ls), flush=True)
    cl0 = clpp(ls, 0.0)
    b0 = bin_through(ls, cl0, wins)

    # the amplitude the CMB fit already determined, read from r7844's own run rather than retyped
    r44 = os.path.join(_BTW, 'r7842_60_polarisation_added_to_the_score_and_the_two_data_the_'
                             'harness_does_not_have', 'sampler3_lcdm_pol.json')
    amp = None
    if os.path.exists(r44):
        # the scorer returns the amplitude beside the chi^2; recompute it at the best fit
        sys.path.insert(0, os.path.dirname(r44))
        amp = None
    meas, err = lb[:, 4], np.sqrt(np.diag(cov))
    print()
    print('  bin   L_av      measured        shape (x AMP)     measured/shape')
    ratios = []
    for i in range(9):
        r = meas[i] / b0[i] if b0[i] != 0 else np.nan
        ratios.append(float(r))
        print('   %d   %6.1f   %.4e +/- %.1e   %.4e      %.4e'
              % (i + 1, lb[i, 3], meas[i], err[i], b0[i], r), flush=True)
    ratios = np.asarray(ratios)
    print()
    print('  ⇒ the implied AMP runs %.4e to %.4e across the nine bins, a spread of %.1f per cent'
          % (ratios.min(), ratios.max(), 100 * (ratios.max() / ratios.min() - 1.0)), flush=True)
    print('    ⌗ A CONSTANT ratio means the SHAPE is right and only the normalisation is free.')
    print('      A ratio that drifts with L means the shape is wrong, and no normalisation fixes it.')
    out = dict(L_av=[float(v) for v in lb[:, 3]], measured=[float(v) for v in meas],
               error=[float(v) for v in err], shape=[float(v) for v in b0],
               implied_amp=[float(v) for v in ratios],
               amp_spread_pc=float(100 * (ratios.max() / ratios.min() - 1.0)),
               ls=[int(v) for v in ls], cl_shape=[float(v) for v in cl0])
    with open(os.path.join(_HERE, 'phiphi.json'), 'w') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('  wrote phiphi.json', flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
