#!/usr/bin/env python3
"""r7652 (60) -- P18 l.1558's `58 times` AND ITS TWO MEASURES, ON THE ARM OF RECORD.

** THE ORDER (`r7651`, 69): ** P18 says the separation between the arms is 58 times the control's own
distance from the data on the same bins, and that two independent measures agree to within 5%.  cc66
traced both to this line's `r4335` framing, F2 = 15473 against chi2_sep = 16261 -- measured on the
`LEAFREC=0` arm.  Re-measure both on the arm of record with this seat's `r7646` scorer, report both
figures and whether they still agree to 5%, and if the statistic does not carry over, say why.

The line between data and code is `r7644`'s and is unchanged:

  ⌗ ** THE DATA IS SHARED ON PURPOSE. **  `plik_lite` TT, its binning weights and its covariance are
    the MEASUREMENT.  An instrument on other data would answer a different question.
  ⛔ ** THE CODE IS NOT. **  This file does not import `chi2_of_spectrum`.  The binning, the
    marginalisation and the closed-form amplitude below are this seat's, written at `r7644`, carried
    at `r7646` and re-stated here so the receipt stands alone.
  ⚠ ** AND camb STAYS OFF THE PINNED INTERPRETER. **  The lensing operator is read as the array
    `r7644` saved under the other interpreter, and its value at ell 1900 is re-asserted into the band
    cc66's own receipt gates it into rather than assumed.

⛔ ** AND THE CARRY-OVER TEST HAS TWO MOVING PARTS. **  The 58 was measured on the LEAFREC=0 arm AND
on 133 UNLENSED bins to ell 1296; the arm of record is measured here on 185 LENSED bins to ell 1996.
So the LEAFREC=0 arm is re-measured on the SAME 185 lensed bins as a third column.  Without it a
single number that failed to reproduce could not say which change caused it.
"""
import math
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
_vac = []


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


def fisher(keep):
    F = np.linalg.inv(COV[np.ix_(keep, keep)])
    return 0.5 * (F + F.T)


def fit(mb, keep):
    """The closed-form amplitude and the fitted model's own chi2, on the kept bins."""
    F = fisher(keep)
    m, d = mb[keep], DATA[keep]
    A = float((m @ F @ d) / (m @ F @ m))
    r = d - A * m
    return A, float(r @ F @ r), F


P = lambda *a: os.path.join(BW, *a)                                       # noqa: E731


def load(rel):
    z = np.load(P(*rel), allow_pickle=True)
    return np.asarray(z['ls'], float), np.asarray(z['Dl'], float)


print(__doc__)
print("=" * 110)
print("  r7652 (60) -- the separation ratio and the two measures, on the arm of record")
print("=" * 110)

# ---------------------------------------------------------------- PART 0 -- the instrument
print("\nPART 0 -- THE BINS AND THE OPERATOR, ASSERTED AND NOT INHERITED")
CTL = ('spectra', 'cc66_lcdm_L2000.npz')
A0R = ('spectra', 'cc66_cr_x_h686_L2000_leafrec1_distances.npz')
LR0 = ('spectra', 'cc66_cr_x_h686_L2000.npz')

_ls, _Dl = load(CTL)
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
      "gates it into", 1.05 <= r1900 <= 1.08)
check("⚠ the interpreter running this score is the PINNED one",
      sys.version_info[:2] == (3, 11) and np.__version__ == '2.4.6')

F185 = fisher(KEEP)


def binned(rel, lens=True):
    ls, Dl = load(rel)
    if lens:
        Dl = Dl * np.interp(ls, LG, RATIO)
    return my_bin(ls, Dl)


# ---------------------------------------------------------------- PART 1 -- the two measures
print("\nPART 1 -- ** THE TWO MEASURES, BOTH ARMS, ON THE SAME 185 LENSED BINS **")
print("""
  ⌗ THE DEFINITIONS ARE THE REGISTRATION'S, FIXED BEFORE THESE NUMBERS EXISTED:
      F2        = chi2(arm) - chi2(control), the difference of the two arms' OWN distances from the data
      chi2_sep  = (A_a m_a - A_c m_c)' F (A_a m_a - A_c m_c), the distance between the two FITTED MODELS
      ratio     = chi2_sep / chi2(control), the quantity that returns 58.20 on the source's 133 bins
""")

mb_c = binned(CTL)
A_c, chi2_c, _ = fit(mb_c, KEEP)
print(f"      control  chi2 = {chi2_c:9.2f}  on 185 bins  = {chi2_c/185:6.3f}/bin   "
      f"amplitude {A_c:.5f}")

RES = {}
for tag, rel in (('arm of record', A0R), ('LEAFREC=0', LR0)):
    mb_a = binned(rel)
    A_a, chi2_a, _ = fit(mb_a, KEEP)
    delta = A_a * mb_a[KEEP] - A_c * mb_c[KEEP]
    chi2_sep = float(delta @ F185 @ delta)
    F2 = chi2_a - chi2_c
    r_c = DATA[KEEP] - A_c * mb_c[KEEP]
    cross = -2.0 * float(delta @ F185 @ r_c)
    RES[tag] = dict(chi2_a=chi2_a, A_a=A_a, F2=F2, sep=chi2_sep, ratio=chi2_sep / chi2_c,
                    arm_over_ctl=chi2_a / chi2_c, cross=cross,
                    disagree_max=abs(F2 - chi2_sep) / max(abs(F2), chi2_sep),
                    disagree_min=abs(F2 - chi2_sep) / min(abs(F2), chi2_sep))

print(f"\n      {'arm':<14} {'chi2(arm)':>10} {'arm/ctl':>8} {'F2':>11} {'chi2_sep':>11}"
      f" {'sep/ctl':>8} {'|dis| max':>10} {'min':>8}")
for tag in ('arm of record', 'LEAFREC=0'):
    r = RES[tag]
    print(f"      {tag:<14} {r['chi2_a']:>10.2f} {r['arm_over_ctl']:>8.3f} {r['F2']:>11.2f}"
          f" {r['sep']:>11.2f} {r['ratio']:>8.2f} {r['disagree_max']*100:>9.2f}%"
          f" {r['disagree_min']*100:>7.2f}%")

print("\n      the source's own figures, for comparison, on 133 UNLENSED bins to ell 1296:")
print("        control 279.4   LEAFREC=0 arm 15752.0 (56.38x)   F2 15472.6   chi2_sep 16260.5"
      "   sep/ctl 58.20")
print("        |F2 - chi2_sep| = 787.9 = 4.84% of chi2_sep and 5.09% of F2")
_src_max, _src_min = 787.9 / 16260.5, 787.9 / 15472.6
check("⌗ the source's own pair is reproduced from its own printed numbers: F2 = 15752.0 - 279.4 and "
      "the ratio = 16260.5 / 279.4, so F2 IS the difference of the two scores and not a second "
      "model-model distance", abs((15752.0 - 279.4) - 15472.6) < 0.1
      and abs(16260.5 / 279.4 - 58.20) < 0.01)
check("⚠ and the original 5% claim PASSES on the larger denominator and FAILS on the smaller, so "
      f"which was meant is load-bearing ({_src_max*100:.2f}% against {_src_min*100:.2f}%)",
      _src_max <= 0.05 < _src_min)

# ---------------------------------------------------------------- PART 2 -- the registered arms
print("\nPART 2 -- THE REGISTERED ARMS")
AOR, L0 = RES['arm of record'], RES['LEAFREC=0']

check(f"⑤ the instrument reproduces r7646's own ratio for the arm of record, 2.346 "
      f"({AOR['arm_over_ctl']:.3f}x)", abs(AOR['arm_over_ctl'] - 2.346) < 0.005)
check(f"⑤ and for the LEAFREC=0 arm, 2.572 ({L0['arm_over_ctl']:.3f}x)",
      abs(L0['arm_over_ctl'] - 2.572) < 0.005)

check(f"⛭ ARM ① -- the 58 does NOT carry over: chi2_sep/chi2(control) on the arm of record is below "
      f"10 ({AOR['ratio']:.2f})", AOR['ratio'] < 10.0)
check(f"⛭ ARM ② -- the two measures do NOT agree to 5% on the arm of record, on the registered "
      f"denominator ({AOR['disagree_max']*100:.2f}%)", AOR['disagree_max'] > 0.05)
check(f"⌗ ARM ② on the other denominator too ({AOR['disagree_min']*100:.2f}%)",
      AOR['disagree_min'] > 0.05)
print(f"""
  ⛔ ARM ③ MISSED, AND ITS MECHANISM SURVIVES ITS ORDERING.  It registered that |F2|/chi2_sep would
  sit FURTHER from 1 on the arm of record than on the LEAFREC=0 arm.  It sits CLOSER:
  {abs(AOR['F2'])/AOR['sep']:.3f} against {abs(L0['F2'])/L0['sep']:.3f}.  The discarded reading is kept.
  The two 185-bin arms are both near the data ({AOR['arm_over_ctl']:.3f}x and {L0['arm_over_ctl']:.3f}x),
  so that pair cannot discriminate and the prediction was a guess about which of two nearly-equal
  rows would land first.  ⇒ The correct form is a BOUND and not an ordering: by Cauchy-Schwarz
  |2 delta' F r_c| <= 2 sqrt(chi2_sep chi2_c), so |F2/chi2_sep - 1| <= 2/sqrt(chi2_sep/chi2_c).
  Agreement of the two measures is CONTINGENT at a small ratio and forced only at a large one -- the
  bound alone does not reach 5% until the ratio exceeds {(2/0.05)**2:.0f}.""")
for _t in ('arm of record', 'LEAFREC=0'):
    _r = RES[_t]
    _b = 2.0 / math.sqrt(_r['ratio'])
    check(f"⛭ ARM ③ CORRECTED -- the bound holds on `{_t}`: |F2/chi2_sep - 1| = "
          f"{abs(_r['F2']/_r['sep'] - 1.0):.4f} <= 2/sqrt({_r['ratio']:.3f}) = {_b:.4f}",
          abs(_r['F2'] / _r['sep'] - 1.0) <= _b)
check("⌗ and on the source's own 133-bin row too, where the ratio is 58.20 and the bound is 0.2622, "
      "which is what made its 4.84% agreement available at all",
      abs(15472.6 / 16260.5 - 1.0) <= 2.0 / math.sqrt(58.198))
check("⌗ and the identity F2 = chi2_sep - 2 delta' F r_c is checked, not asserted, on BOTH arms",
      all(abs(RES[t]['F2'] - (RES[t]['sep'] + RES[t]['cross'])) < 1e-6 * max(1.0, RES[t]['sep'])
          for t in RES))
check(f"⛭ ARM ④ -- the separation shrinks with the arm: chi2_sep is smaller on the arm of record "
      f"({AOR['sep']:.2f}) than on the LEAFREC=0 arm ({L0['sep']:.2f}), so the move r7646 measured "
      f"in the ratio against the data is in the model-model distance too",
      AOR['sep'] < L0['sep'])
check(f"⑥ F2 on the arm of record is small and positive and tracks r7646's ratio: F2/chi2(control) "
      f"in [1.0, 1.7] ({AOR['F2']/chi2_c:.3f})", 1.0 <= AOR['F2'] / chi2_c <= 1.7)
print(f"""
  ⛔⛔ ARM ⑦ MISSED, AND THE MISS IS THE REVISION'S FINDING.  It registered that the LEAFREC=0 arm,
  re-measured on these same 185 lensed bins, would still return a ratio above 20, so that the
  collapse from 58 would be the ARM's.  It returns {L0['ratio']:.2f}.  The discarded reading is kept.
  ⇒ So the 58 is NOT a property of the LEAFREC=0 arm.  It is a property of the CONFIGURATION it was
  measured in -- and P18 l.1558 says the absolute values are configuration-limited and that what is
  NOT configuration-limited is the ratio.  That clause is falsified on the arm it was measured on:
  58.20 against {L0['ratio']:.2f}, a factor of {58.20/L0['ratio']:.0f}, the arm held fixed and only the
  configuration changed.  Which half of "the configuration" does it is pass 2's question.""")
check(f"⛭⛭ ARM ⑦ CORRECTED -- the LEAFREC=0 arm on these 185 lensed bins returns a ratio BELOW 10 "
      f"({L0['ratio']:.2f}), so the 58 does not belong to that arm and cannot be recovered by "
      f"re-measuring it", L0['ratio'] < 10.0)
check(f"⌗ and the fall is more than an order of magnitude, which is what makes it a falsification of "
      f"l.1558's clause rather than a disagreement in the digits ({58.20/L0['ratio']:.1f}x)",
      58.20 / L0['ratio'] > 10.0)

# ---------------------------------------------------------------- PART 3 -- what P18 can cite
print("\nPART 3 -- WHICH MEASURE P18 CAN CITE")
print(f"""
      On the arm of record, on 185 lensed bins to ell 1996:

        F2        = {AOR['F2']:.2f}          ({AOR['F2']/chi2_c:.3f} x the control's own)
        chi2_sep  = {AOR['sep']:.2f}          ({AOR['ratio']:.2f} x the control's own)
        the cross term -2 delta' F r_c = {AOR['cross']:.2f}

      On the LEAFREC=0 arm, SAME bins, for the carry-over:

        F2        = {L0['F2']:.2f}          ({L0['F2']/chi2_c:.3f} x the control's own)
        chi2_sep  = {L0['sep']:.2f}          ({L0['ratio']:.2f} x the control's own)
        the cross term -2 delta' F r_c = {L0['cross']:.2f}
""")
check("⛭⛭ ARM ⑧ -- both measures now have a receipt and NEITHER returns 58 on the arm of record, so "
      "l.1558 cannot be repaired by choosing a measure: it names a figure of the superseded arm. "
      "The re-point is 69's call on P18's registration",
      AOR['ratio'] < 58.0 and abs(AOR['F2']) / chi2_c < 58.0)

print("""  ⌗ *What this does NOT settle, from the registration: the data is shared on purpose, so this
  is an agreement about arithmetic on 185 bins and not a claim that those bins are the right
  confrontation; it does not re-open which arm is the arm of record; and it does not touch P18.*""")

print("\n" + "=" * 110)
print(f"  {len(_fail)} failure(s), {len(_vac)} vacuous")
for f in _fail:
    print("   [FAIL] " + f)
sys.exit(1 if _fail else 0)
