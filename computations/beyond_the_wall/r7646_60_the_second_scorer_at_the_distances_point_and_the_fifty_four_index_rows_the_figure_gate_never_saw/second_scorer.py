#!/usr/bin/env python3
"""r7646 (60) PART 1 -- THE SECOND SCORER AT THE DISTANCES' POINT, ON THE SAME 185 BINS.

** THE ORDER (`r7645`, 69) item 1: ** run this seat's independent scorer on `70`'s no-fit spectrum
and refit grid at the distances' point, report whether it reproduces `2.346` and `1.596`, and the
lensed-against-unlensed pair on the same bins -- **before** 69 lands those figures corpus-wide.

The line between data and code is `r7644`'s and is unchanged:

  ⌗ ** THE DATA IS SHARED ON PURPOSE. **  `plik_lite` TT, its binning weights and its covariance are
    the MEASUREMENT.  An instrument on other data would answer a different question.
  ⛔ ** THE CODE IS NOT. **  This file does not import `chi2_of_spectrum`, the corpus's own scorer
    and the one `70`'s `measure.py` calls.  The binning, the marginalisation and the amplitude fit
    below are this seat's, written at `r7644` and re-stated here so the receipt stands alone.
  ⚠ ** AND camb STAYS OFF THE PINNED INTERPRETER. **  `70`'s `measure.py` imports `camb` directly.
    This file reads the FULL lensed/unlensed operator as the array `r7644` computed under the other
    interpreter and saved -- the fork `r7645` calls the right one -- and re-asserts its value at
    ell 1900 into the band cc66's own receipt gates it into rather than assuming it.

⌗ *What an agreement here is: an agreement about arithmetic on the same 185 bins.  It is not a claim
that those bins are the right confrontation, and this file does not make one.*
"""
import os
import sys

import numpy as np
from scipy.io import FortranFile

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(BW))
LIKDIR = os.path.join(ROOT, 'computations', 'planck_tt_likelihood')
OPER = os.path.join(BW, 'r7644_60_an_independent_instrument_on_the_headline_pair',
                    'lensing_operator.npz')
sys.path.insert(0, LIKDIR)
from planck_lite_py import PlanckLitePy                                    # noqa: E402

_fail = []


def check(label, ok):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        _fail.append(label)


# ---------------------------------------------------------------- the data, read for myself
LIK = PlanckLitePy(data_directory=os.path.join(LIKDIR, 'data'), year=2018, spectra='TT',
                   use_low_ell_bins=False)
NB_ALL = LIK.nbintt
_f = FortranFile(LIK.cov_file, 'r')
_c = _f.read_reals(dtype=float).reshape((LIK.nbin_hi, LIK.nbin_hi))
COV = (np.tril(_c) + np.tril(_c, -1).T)[:NB_ALL, :NB_ALL]
DATA = LIK.X_data[:NB_ALL]
LO = np.array([LIK.blmin_TT[i] + LIK.plmin_TT for i in range(NB_ALL)])
HI = np.array([LIK.blmax_TT[i] + LIK.plmin_TT for i in range(NB_ALL)])


def my_bin(ls, Dl):
    """D_l -> C_l on every ell in the bin, then the likelihood's own weights (this seat's binning)."""
    ls, Dl = np.asarray(ls, float), np.asarray(Dl, float)
    out = np.full(NB_ALL, np.nan)
    for i in range(NB_ALL):
        a, b = LIK.blmin_TT[i], LIK.blmax_TT[i]
        ell = np.arange(a, b + 1) + LIK.plmin_TT
        w = LIK.bin_w_TT[a:b + 1]
        if ell[0] < ls[0] or ell[-1] > ls[-1]:
            continue
        d = np.interp(ell, ls, Dl)
        out[i] = float(np.sum(w * d / (ell * (ell + 1) / (2.0 * np.pi))))
    return out


def my_chi2(ls, Dl, keep):
    """MARGINALISE over the uncovered bins (restrict the covariance, then invert) and fit one
    amplitude exactly in closed form.  `r7644` PART 3 priced both choices: +9.5% and load-bearing."""
    mb = my_bin(ls, Dl)
    k = keep & np.isfinite(mb)
    n = int(k.sum())
    F = np.linalg.inv(COV[np.ix_(k, k)])
    F = 0.5 * (F + F.T)
    m, d = mb[k], DATA[k]
    A = float((m @ F @ d) / (m @ F @ m))
    r = d - A * m
    return float(r @ F @ r), n, A


P = lambda *a: os.path.join(BW, *a)                                       # noqa: E731


def load(rel):
    z = np.load(P(*rel), allow_pickle=True)
    return np.asarray(z['ls'], float), np.asarray(z['Dl'], float)


print(__doc__)
print("=" * 108)
print("  r7646 (60) PART 1 -- 70's distances' point on a second scorer, same 185 bins")
print("=" * 108)

# ---------------------------------------------------------------- PART 0
print("\nPART 0 -- THE BINS AND THE OPERATOR, ASSERTED AND NOT INHERITED")
_ctl = ('spectra', 'cc66_lcdm_L2000.npz')
_ls, _Dl = load(_ctl)
KEEP = np.isfinite(my_bin(_ls, _Dl))
print(f"      control covers ell {_ls[0]:.0f}-{_ls[-1]:.0f}, {int(KEEP.sum())} bins, "
      f"ell {int(LO[KEEP][0])}-{int(HI[KEEP][-1])}")
check(f"the bin count is 185, ell {int(LO[KEEP][0])} to {int(HI[KEEP][-1])}, as the corpus calls it",
      int(KEEP.sum()) == 185)
check("⌗ and this file does not import the corpus's own scorer, which is what makes this a second "
      "reading rather than a re-run of 70's", 'chi2_of_spectrum' not in sys.modules)
_z = np.load(OPER, allow_pickle=True)
LG, RATIO = np.asarray(_z['ell'], float), np.asarray(_z['ratio'], float)
r1900 = float(_z['r1900'])
print(f"      the saved FULL operator at ell 1900: {r1900:.4f}   (camb {str(_z['camb_version'])})")
check("the operator is the full lensed/unlensed ratio, inside the [1.05, 1.08] cc66's own receipt "
      "gates it into, and not the first-order kernel's spurious ~1.13", 1.05 <= r1900 <= 1.08)
check("⚠ and the interpreter running this score is still the PINNED one, so reading the operator as "
      "data did not move the arithmetic under the corpus's floats",
      sys.version_info[:2] == (3, 11) and np.__version__ == '2.4.6')

# ---------------------------------------------------------------- PART 1
print("\nPART 1 -- ** THE THREE ROWS 69 IS ABOUT TO LAND, LENSED AND UNLENSED ON THE SAME BINS **")
ROWS = [
    ('no-fit L2000', ('spectra', 'cc66_lcdm_L2000.npz'),
     ('spectra', 'cc66_cr_x_h686_L2000.npz'),
     ('spectra', 'cc66_cr_x_h686_L2000_leafrec1_distances.npz'), 2.572, 2.346),
    ('grid base L8', ('refit_grid185', 'lcdm_base.npz'),
     ('refit_grid185', 'cr_base.npz'),
     ('refit_grid185_leafrec1_distances', 'cr_base.npz'), 2.564, 2.332),
    ('refit verify', ('spectra', 'cc66_r185_verify_lcdm.npz'),
     ('spectra', 'cc66_r185_verify_cr.npz'),
     ('spectra', 'cc66_r185_verify_cr_leafrec1.npz'), 1.568, 1.596),
]
print(f"\n      {'configuration':<14} {'half':<9} {'control':>9} {'LEAFREC=0':>10} {'LEAFREC=1':>10}"
      f" {'r0/c':>7} {'r1/c':>7}   70 prints")
READ = {}
for tag, pc, p0, p1 in [(r[0], r[1], r[2], r[3]) for r in ROWS]:
    e0, e1 = [r[4] for r in ROWS if r[0] == tag][0], [r[5] for r in ROWS if r[0] == tag][0]
    for half, lens in (('unlensed', False), ('LENSED', True)):
        sc, nb = [], []
        for rel in (pc, p0, p1):
            ls, Dl = load(rel)
            if lens:
                Dl = Dl * np.interp(ls, LG, RATIO)
            c, n, _ = my_chi2(ls, Dl, KEEP)
            sc.append(c)
            nb.append(n)
        assert set(nb) == {185}, (tag, half, nb)
        READ[(tag, half)] = (sc, sc[1] / sc[0], sc[2] / sc[0])
        print(f"      {tag:<14} {half:<9} {sc[0]:>9.1f} {sc[1]:>10.1f} {sc[2]:>10.1f}"
              f" {sc[1]/sc[0]:>7.3f} {sc[2]/sc[0]:>7.3f}"
              + (f"   {e0} / {e1}" if lens else ""))

# ---------------------------------------------------------------- PART 2
print("\nPART 2 -- THE REGISTERED ARMS")
for tag, _, _, _, e0, e1 in ROWS:
    got = READ[(tag, 'LENSED')][2]
    check(f"⛭ 70's lensed LEAFREC=1 ratio on `{tag}` reproduces its printed {e1} ({got:.3f}x)",
          abs(got - e1) < 0.005)
for tag, _, _, _, e0, e1 in ROWS:
    got = READ[(tag, 'LENSED')][1]
    check(f"⌗ and its LEAFREC=0 row with it, {e0} ({got:.3f}x), so the MOVE and not only the new "
          f"figure is the same on both scorers", abs(got - e0) < 0.005)
_dir = [(tag, READ[(tag, half)][0][2] < READ[(tag, half)][0][1])
        for tag in ('no-fit L2000', 'grid base L8') for half in ('unlensed', 'LENSED')]
check("⛭ ARM ④ -- the LEAFREC=1 arm is LESS unfavourable than the LEAFREC=0 arm on BOTH halves of "
      "both no-fit rows, so the move down is the spectrum's and not the lensing operator's",
      all(ok for _, ok in _dir))
_u = READ[('no-fit L2000', 'unlensed')][2]
check(f"⛭ ARM ⑤ -- the UNLENSED no-fit ratio at the distances' point lands below r7644's 1.681 for "
      f"the LEAFREC=0 arm, inside the registered [1.3, 1.68] ({_u:.3f}x)", 1.3 <= _u <= 1.68)
_rf = READ[('refit verify', 'LENSED')]
check("⌗ and the refit row moves UP where the no-fit rows move down -- 1.568 -> 1.596 -- which is "
      "the direction 70 reports and the one thing in its table that is not a loosening",
      _rf[2] > _rf[1])

# ---------------------------------------------------------------- PART 3
print("\nPART 3 -- WHAT THIS SETTLES AND WHAT IT DOES NOT")
_worst = max(abs(READ[(t, 'LENSED')][2] - e1) for t, _, _, _, _, e1 in ROWS)
_worst0 = max(abs(READ[(t, 'LENSED')][1] - e0) for t, _, _, _, e0, _ in ROWS)
print(f"      worst |Δ| against 70's printed LEAFREC=1 figures: {_worst:.4f}")
print(f"      worst |Δ| against its LEAFREC=0 figures:          {_worst0:.4f}")
check("⛭⛭ ⇒ THE REGISTERED NEGATIVE DID NOT FIRE: no row disagrees beyond the digits 70 prints, so "
      "the figures 69 lands corpus-wide are not this scorer's artefacts and the check that was "
      "asked for before them is clean", _worst < 0.005 and _worst0 < 0.005)
print("  ⌗ *And what it does NOT settle, from the registration: the two scorers share the data on")
print("  purpose, so this is an agreement about arithmetic on 185 bins and not about whether those")
print("  bins are the right confrontation.  The only claim here is that the disagreement's SIZE is")
print("  instrument-independent at the digits the papers print.*")

print("\n" + "=" * 108)
print(f"  {len(_fail)} failure(s)")
for f in _fail:
    print("   [FAIL] " + f)
sys.exit(1 if _fail else 0)
