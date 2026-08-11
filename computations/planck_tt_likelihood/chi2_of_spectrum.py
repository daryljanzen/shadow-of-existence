#!/usr/bin/env python3
"""** chi^2 OF AN ARBITRARY BINNED-ELL SPECTRUM AGAINST plik_lite TT, WITH ONE FITTED AMPLITUDE. **

Built r2376+c54.176.  ** This exists because the chi^2 values quoted in `L-147`'s receipt were
produced by a scratch script in /tmp and could not be re-derived from the corpus. **  A number that
cannot be recomputed is not a receipt, whatever file it is printed in.  Everything the pinned
numbers depended on -- the interpolation onto the full ell grid, the binning, the restriction of the
covariance to covered bins, the single-amplitude fit -- is here and importable.

** THE THREE CHOICES THAT MATTER, AND WHY EACH IS THE ONE IT IS. **

  1  ** THE RESTRICTION TO COVERED BINS IS DONE ON THE COVARIANCE AND NOT ON ITS INVERSE. **  This
     instrument reaches ell = 2000 and plik_lite runs to 2508.  Dropping rows of the FISHER matrix
     would CONDITION on the missing bins; dropping rows of the COVARIANCE and re-inverting
     MARGINALISES over them, which is what "those multipoles were not computed" actually means.
  2  ** ONE AMPLITUDE IS FITTED AND IT IS FITTED EXACTLY, NOT SEARCHED. **  With chi^2(A) =
     (d - A m)^T F (d - A m), dchi^2/dA = 0 gives A = (m^T F d)/(m^T F m) in closed form.  What is
     being compared is SHAPE; A_s is inherited by every spectrum this instrument produces and
     carrying it as a free parameter is the honest accounting.
  3  ** THE SPECTRUM IS INTERPOLATED IN ell BEFORE BINNING, NOT AFTER. **  The instrument samples
     ell on a stride (LSTEP=8); the likelihood's bins are weighted sums over EVERY ell.  Binning a
     strided sample would silently reweight the bins.

Used as a module:  chi2_of(ls, Dl) -> (chi2, nbins, amplitude, ell_lo, ell_hi)
Used as a script:  python3 chi2_of_spectrum.py FILE.npz [FILE.npz ...]
"""
import os
import sys

import numpy as np
import scipy.linalg
from scipy.io import FortranFile

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
from planck_lite_py import PlanckLitePy                                    # noqa: E402

_LIK = PlanckLitePy(data_directory=os.path.join(_HERE, 'data'), year=2018, spectra='TT',
                    use_low_ell_bins=False)
_f = FortranFile(_LIK.cov_file, 'r')
_c = _f.read_reals(dtype=float).reshape((_LIK.nbin_hi, _LIK.nbin_hi))
COV_TT = (np.tril(_c) + np.tril(_c, -1).T)[:_LIK.nbintt, :_LIK.nbintt]
BIN_LO = np.array([_LIK.blmin_TT[i] + _LIK.plmin_TT for i in range(_LIK.nbintt)])
BIN_HI = np.array([_LIK.blmax_TT[i] + _LIK.plmin_TT for i in range(_LIK.nbintt)])
X_DATA = _LIK.X_data[:_LIK.nbintt]


def bin_center_and_fac():
    """the weighted ell centre of each TT bin, and the weighted l(l+1)/2pi that converts C_l -> D_l

    ** X_data IS BINNED C_l AND NOT D_l. **  Peak-finding on X_data directly puts the acoustic peaks
    tens of multipoles low and loses the first one entirely under the falling plateau -- which is
    how this was caught.
    """
    lc = np.zeros(_LIK.nbintt)
    fac = np.zeros(_LIK.nbintt)
    for i in range(_LIK.nbintt):
        ll = np.arange(_LIK.blmin_TT[i], _LIK.blmax_TT[i] + 1) + _LIK.plmin_TT
        w = _LIK.bin_w_TT[_LIK.blmin_TT[i]:_LIK.blmax_TT[i] + 1]
        lc[i] = float(np.sum(w * ll))
        fac[i] = float(np.sum(w * ll * (ll + 1) / (2 * np.pi)))
    return lc, fac


def bin_spectrum(ls, Dl):
    """interpolate D_l onto every ell, convert to C_l, and bin exactly as the likelihood bins

    Bins not fully covered by [ls[0], ls[-1]] come back NaN; the caller drops them.
    """
    ls = np.asarray(ls, dtype=float)
    lo, hi = int(np.ceil(ls[0])), int(np.floor(ls[-1]))
    lfull = np.arange(2, _LIK.plmax + 1)
    Dfull = np.full(len(lfull), np.nan)
    m = (lfull >= lo) & (lfull <= hi)
    Dfull[m] = np.interp(lfull[m], ls, Dl)
    Cl = Dfull / (lfull * (lfull + 1) / (2 * np.pi))
    out = np.full(_LIK.nbintt, np.nan)
    for i in range(_LIK.nbintt):
        a = _LIK.blmin_TT[i] + _LIK.plmin_TT - 2
        b = _LIK.blmax_TT[i] + _LIK.plmin_TT + 1 - 2
        seg = Cl[a:b]
        if len(seg) == 0 or not np.all(np.isfinite(seg)):
            continue
        out[i] = float(np.sum(seg * _LIK.bin_w_TT[_LIK.blmin_TT[i]:_LIK.blmax_TT[i] + 1]))
    return out


def chi2_of(ls, Dl, amplitude=None, lmax=None):
    """chi^2 against plik_lite TT over the bins this spectrum covers, one amplitude fitted

    ** lmax CUTS THE COMPARISON BELOW THE WAVENUMBER TRUNCATION, AND IT IS NOT OPTIONAL HOUSEKEEPING
    (c54.178). **  An instrument that carries k up to LMAXL/D_M has a STARVED k integral for the top
    few hundred multipoles -- c54.176 measured that as a 7% error on P1/P3 at LMAXL=1300 -- so bins
    above roughly 0.8*LMAXL are scoring the truncation and not the physics.  *Left uncut, that
    region dominates chi^2 and can reverse the verdict on a change that improves everything below
    it.*  Both numbers are worth printing; neither replaces the other.
    """
    mb = bin_spectrum(ls, Dl)
    keep = np.isfinite(mb)
    if lmax is not None:
        keep = keep & (BIN_HI <= float(lmax))
    if keep.sum() < 10:
        raise ValueError(f"only {keep.sum()} bins covered -- the spectrum is too short to score")
    cov = COV_TT[np.ix_(keep, keep)]
    F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(cov), np.identity(keep.sum()))
    F = 0.5 * (F + F.T)
    m, d = mb[keep], X_DATA[keep]
    A = float((m @ F @ d) / (m @ F @ m)) if amplitude is None else float(amplitude)
    r = d - A * m
    return float(r @ F @ r), int(keep.sum()), A, int(BIN_LO[keep][0]), int(BIN_HI[keep][-1])


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    _lm = os.environ.get('LMAXCUT')
    print(f"  {'file':>28} {'chi^2':>11} {'bins':>6} {'chi^2/dof':>11} {'amp':>9} {'ell range':>12}")
    for p in argv:
        z = np.load(p, allow_pickle=True)
        c, n, A, lo, hi = chi2_of(z['ls'], z['Dl'], lmax=float(_lm) if _lm else None)
        print(f"  {os.path.basename(p):>28} {c:>11.1f} {n:>6} {c/n:>11.2f} {A:>9.3e} "
              f"{f'{lo}-{hi}':>12}")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
