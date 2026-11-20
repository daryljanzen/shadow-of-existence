"""r7842+60: chi^2 OF AN ARBITRARY BINNED-ELL TT, TE AND EE SPECTRUM AGAINST plik_lite, WITH ONE
FITTED AMPLITUDE ACROSS ALL THREE.

On order r7841 (69) item ①.  This is `computations/planck_tt_likelihood/chi2_of_spectrum.py`
extended from one spectrum to three, with that module's THREE DOCUMENTED CHOICES KEPT EXACTLY and
nothing else changed:

  1  the restriction to covered bins is done on the COVARIANCE and re-inverted, which MARGINALISES
     over the multipoles the instrument did not compute, where dropping rows of the Fisher matrix
     would CONDITION on them;
  2  one amplitude is fitted and fitted in CLOSED FORM, A = (m F d)/(m F m);
  3  the spectrum is interpolated in ell BEFORE binning, because the instrument samples ell on a
     stride and the likelihood's bins are weighted sums over every ell.

** AND ONE THING THE EXTENSION HAS TO DECIDE, WHICH THE TT MODULE NEVER FACED. **  The amplitude is
ONE amplitude across TT, TE and EE, not three.  `A_s` is a single number in the physics and the
relative normalisation of the three spectra is most of what polarisation adds: three amplitudes
would throw exactly that away and score only three shapes.  So `m` is the CONCATENATED 555-bin
model and `A` is solved once on it.

** AND ONE GUARD THAT HAD TO CHANGE. **  The TT harness refuses a model with any non-positive bin.
TE IS NEGATIVE over part of its range -- it changes sign three times inside this instrument's own
reach -- so the positivity guard is applied to the TT and EE blocks ONLY.  A guard copied across
unexamined would have rejected every physical model.

The instrument's own convention is used for all three: `POLSAVE` writes `D_l = C_l l(l+1)` for TT,
TE and EE alike, so the one conversion is applied to all three and whatever constant it leaves is
absorbed by the single `A` identically.  The RELATIVE normalisation, which is what matters, is
untouched.

Used as a module:  chi2_of(ls, Dtt, Dte, Dee) -> (chi2, nbins, A, per-spectrum bin counts)
"""
import os
import sys

import numpy as np
import scipy.linalg
from scipy.io import FortranFile

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
_LIKDIR = os.path.join(_ROOT, 'computations', 'planck_tt_likelihood')
sys.path.insert(0, _LIKDIR)
from planck_lite_py import PlanckLitePy                                    # noqa: E402

LIK = PlanckLitePy(data_directory=os.path.join(_LIKDIR, 'data'), year=2018, spectra='TTTEEE',
                   use_low_ell_bins=False)
_f = FortranFile(LIK.cov_file, 'r')
_c = _f.read_reals(dtype=float).reshape((LIK.nbin_hi, LIK.nbin_hi))
COV = np.tril(_c) + np.tril(_c, -1).T                     # the FULL 613-bin covariance, TT+TE+EE
X_DATA = np.asarray(LIK.X_data, float)                    # binned C_l / calPlanck^2, 613 of them
NTT, NTE, NEE = LIK.nbintt, LIK.nbinte, LIK.nbinee
NBIN = NTT + NTE + NEE
assert NBIN == LIK.nbin_tot == COV.shape[0], 'the covariance and the bin count disagree'

# the bin edges: TT has its own, TE and EE share one set, exactly as `loglike` reads them
BIN_LO = np.concatenate([[LIK.blmin_TT[i] + LIK.plmin_TT for i in range(NTT)],
                         [LIK.blmin[i] + LIK.plmin for i in range(NTE)],
                         [LIK.blmin[i] + LIK.plmin for i in range(NEE)]]).astype(int)
BIN_HI = np.concatenate([[LIK.blmax_TT[i] + LIK.plmin_TT for i in range(NTT)],
                         [LIK.blmax[i] + LIK.plmin for i in range(NTE)],
                         [LIK.blmax[i] + LIK.plmin for i in range(NEE)]]).astype(int)
# which block each bin belongs to: 0 = TT, 1 = TE, 2 = EE
BLOCK = np.concatenate([np.zeros(NTT, int), np.ones(NTE, int), 2 * np.ones(NEE, int)])
POSITIVE = BLOCK != 1                                     # the guard applies to TT and EE, not TE


def _bin_one(ls, Dl, which):
    """interpolate D_l onto every ell, convert to C_l on the instrument's own convention, and bin

    `which` picks the bin set: 'TT' uses blmin_TT/plmin_TT, 'P' uses blmin/plmin (TE and EE share).
    Bins not fully covered by [ls[0], ls[-1]] come back NaN; the caller drops them.
    """
    ls = np.asarray(ls, float)
    lo, hi = int(np.ceil(ls[0])), int(np.floor(ls[-1]))
    lfull = np.arange(2, LIK.plmax + 1)
    Dfull = np.full(len(lfull), np.nan)
    m = (lfull >= lo) & (lfull <= hi)
    Dfull[m] = np.interp(lfull[m], ls, np.asarray(Dl, float))
    Cl = Dfull / (lfull * (lfull + 1) / (2 * np.pi))
    if which == 'TT':
        bl0, bl1, w, n = LIK.blmin_TT, LIK.blmax_TT, LIK.bin_w_TT, NTT
        p = LIK.plmin_TT
    else:
        bl0, bl1, w, n = LIK.blmin, LIK.blmax, LIK.bin_w, NTE
        p = LIK.plmin
    out = np.full(n, np.nan)
    for i in range(n):
        a, b = bl0[i] + p - 2, bl1[i] + p + 1 - 2
        seg = Cl[a:b]
        if len(seg) == 0 or not np.all(np.isfinite(seg)):
            continue
        out[i] = float(np.sum(seg * w[bl0[i]:bl1[i] + 1]))
    return out


def bin_three(ls, Dtt, Dte, Dee):
    """the 613-bin model vector, NaN on every bin the instrument's reach does not cover"""
    return np.concatenate([_bin_one(ls, Dtt, 'TT'), _bin_one(ls, Dte, 'P'), _bin_one(ls, Dee, 'P')])


def fisher_for(keep):
    """the inverse of the covariance RESTRICTED to the kept bins -- choice 1, on three spectra"""
    cov = COV[np.ix_(keep, keep)]
    F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(cov), np.identity(int(keep.sum())))
    return 0.5 * (F + F.T)


def chi2_of(ls, Dtt, Dte, Dee, amplitude=None, blocks=(0, 1, 2)):
    """chi^2 against plik_lite over the bins this spectrum covers, ONE amplitude across the blocks

    `blocks` selects which of TT, TE, EE to score, so the TT-only closure runs through the same
    code path as the joint fit rather than through a second implementation.
    """
    mb = bin_three(ls, Dtt, Dte, Dee)
    keep = np.isfinite(mb) & np.isin(BLOCK, list(blocks))
    if keep.sum() < 10:
        raise ValueError(f'only {keep.sum()} bins covered -- too short to score')
    F = fisher_for(keep)
    m, d = mb[keep], X_DATA[keep]
    A = float((m @ F @ d) / (m @ F @ m)) if amplitude is None else float(amplitude)
    r = d - A * m
    n = {b: int(((BLOCK == b) & keep).sum()) for b in (0, 1, 2)}
    return float(r @ F @ r), int(keep.sum()), A, n
