#!/usr/bin/env python3
"""
RECEIPT -- P15: ** THE TWO MEASURES OF THE SEPARATION, PINNED ON THE ARM OF RECORD, WITH THE IDENTITY
THAT RELATES THEM AND THE BOUND THAT PRICES THEIR AGREEMENT CHECKED ON EVERY ROW. **

Built `r7654` (node 60), discharging `r7653`'s order.  `P18` l.1557-1559 was re-stated at `r7653` on
`r7652`'s branch 1 and now prints two figures and a gap:

  * the separation between the two arms is ** 1.77 ** times the control's own distance from the data,
  * the difference of the two arms' scores is ** 1.35 ** times it (** 288.04 ** over ** 214.1 **),
  * and the two measures are ** a quarter ** apart.

Those figures were produced in a computations directory.  This receipt makes them runnable by a reader
who did not write them, and pins each one against the value the paper prints.

=====================================================================================================
** WHAT THE TWO MEASURES ARE.  Fixed here, because the order's own wording left it open and reading
   `r4236`'s printed numbers is what settled it. **
=====================================================================================================

For a spectrum binned onto the kept bins, `F` the marginalised inverse covariance on those bins
(restrict, then invert), `A = (m' F d)/(m' F m)` the closed-form amplitude and
`chi2(m) = (d - A m)' F (d - A m)`:

  F2        := chi2(arm) - chi2(control)   -- the DIFFERENCE OF THE TWO ARMS' OWN DISTANCES from the
               data.  `r4236` printed 15752.0 and 279.4 and called their difference 15473; 15752.0 -
               279.4 = 15472.6, which is what identifies F2 as a difference of two scores and NOT a
               second model-model distance.
  chi2_sep  := (A_a m_a - A_c m_c)' F (A_a m_a - A_c m_c)  -- the distance between the two FITTED
               MODELS, the data entering only through F and through the two amplitudes.

** AND THEY ARE NOT INDEPENDENT.  The identity, which this receipt CHECKS rather than asserts: **

    F2  ==  chi2_sep  -  2 delta' F r_c ,      delta = A_a m_a - A_c m_c ,   r_c = d - A_c m_c

so the two differ by a cross term with the CONTROL's own residual.  ** Hence the bound, by
Cauchy-Schwarz on that cross term: **

    | F2 / chi2_sep  -  1 |   <=   2 / sqrt( chi2_sep / chi2_c )

*** WHICH IS WHY `P18`'s OLD "agree to within 5%" WAS NEVER A PROPERTY OF THE TWO MEASURES. *** It was
a property of the RATIO's size: the bound does not reach 5% until chi2_sep/chi2_c exceeds 1600, and at
the 58.2 of `r4236`'s build it is 0.2622, which is what made that build's 4.84% available at all.  At
the 1.77 of the arm of record the bound is 1.50 and nothing forces agreement to anything.  Both are
printed below.

** COMPUTES: the ratio chi2_sep/chi2_c and the ratio F2/chi2_c on the arm of record's 185 lensed bins
   against its control, and the two chi^2 values they are formed from -- the four figures `P18`
   l.1557-1559 prints, each pinned against the printed value by a parsed comparison; the identity and
   the bound above on all eight (arm, half, bin set) rows this file produces; and the failability of
   every pin, measured by perturbing the arm rather than claimed. ***

STATUS: OK
rc=0 on success.  Run: python3 <this file>   (numpy, scipy; ~20 s -- reads banked spectra, no camb)

=====================================================================================================
** WHAT THIS RECEIPT DOES NOT CLAIM. **
=====================================================================================================

  (1) ** THE DATA IS SHARED ON PURPOSE. **  `plik_lite` TT, its binning weights and its covariance
      ARE the measurement.  This is an agreement about arithmetic on the likelihood's own bins; it is
      not a claim that those bins are the right confrontation, and this file does not make one.
  (2) ** IT DOES NOT SAY WHICH ARM IS THE ARM OF RECORD. **  It takes the file the corpus names.
  (3) ** AND ONE CLAUSE OF `P18`'s SENTENCE IS TRUE OF ITS OWN CONFIGURATION AND NOT IN GENERAL. **
      The sentence says both measures put "the arms further from each other than the control is from
      the data".  On the arm of record both ratios exceed 1 -- 1.77 and 1.35 -- so it holds THERE.  It
      does NOT hold on every configuration this instrument reaches: the 185 unlensed rows return 0.67
      and 0.53, and the 133 unlensed rows 0.94 and 0.88, all below 1.  *** So the clause is a fact
      about the full-range lensed bins, which is what the sentence names, and the table below prints
      the other rows so no reader can take the stronger reading. ***  Reported, not repaired: the
      sentence as re-stated at `r7653` is correct as written.
"""
import math
import os
import sys

import numpy as np
from scipy.io import FortranFile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
LIKDIR = os.path.join(ROOT, 'computations', 'planck_tt_likelihood')
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
OPER = os.path.join(BW, 'r7644_60_an_independent_instrument_on_the_headline_pair',
                    'lensing_operator.npz')
sys.path.insert(0, LIKDIR)
from planck_lite_py import PlanckLitePy                                    # noqa: E402

_fail = []


def check(label, ok):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        _fail.append(label)


# ------------------------------------------------------------------ the data, read here
LIK = PlanckLitePy(data_directory=os.path.join(LIKDIR, 'data'), year=2018, spectra='TT',
                   use_low_ell_bins=False)
NB = LIK.nbintt
_f = FortranFile(LIK.cov_file, 'r')
_c = _f.read_reals(dtype=float).reshape((LIK.nbin_hi, LIK.nbin_hi))
COV = (np.tril(_c) + np.tril(_c, -1).T)[:NB, :NB]
DATA = LIK.X_data[:NB]
LO = np.array([LIK.blmin_TT[i] + LIK.plmin_TT for i in range(NB)])
HI = np.array([LIK.blmax_TT[i] + LIK.plmin_TT for i in range(NB)])

CTL = os.path.join(BW, 'spectra', 'cc66_lcdm_L2000.npz')
AOR = os.path.join(BW, 'spectra', 'cc66_cr_x_h686_L2000_leafrec1_distances.npz')
LR0 = os.path.join(BW, 'spectra', 'cc66_cr_x_h686_L2000.npz')

_z = np.load(OPER, allow_pickle=True)
LG, RATIO = np.asarray(_z['ell'], float), np.asarray(_z['ratio'], float)
R1900 = float(_z['r1900'])


def my_bin(ls, Dl):
    """D_l -> C_l on every ell in the bin, then the likelihood's own weights."""
    out = np.full(NB, np.nan)
    for i in range(NB):
        a, b = LIK.blmin_TT[i], LIK.blmax_TT[i]
        ell = np.arange(a, b + 1) + LIK.plmin_TT
        w = LIK.bin_w_TT[a:b + 1]
        if ell[0] < ls[0] or ell[-1] > ls[-1]:
            continue
        out[i] = float(np.sum(w * np.interp(ell, ls, Dl) / (ell * (ell + 1) / (2.0 * np.pi))))
    return out


def binned(path, lens, warp=None):
    z = np.load(path, allow_pickle=True)
    ls, Dl = np.asarray(z['ls'], float), np.asarray(z['Dl'], float)
    if warp is not None:
        Dl = Dl * warp(ls)
    if lens:
        Dl = Dl * np.interp(ls, LG, RATIO)
    return my_bin(ls, Dl)


def row(keep, arm_path, lens, warp=None, ctl_warp=None):
    """The whole row: both scores, both measures, the cross term and the bound.

    `warp` perturbs the ARM, `ctl_warp` the CONTROL -- separately, because the four figures do not
    all depend on both: chi2_c reads the control alone (`r7654+60.1`).
    """
    F = np.linalg.inv(COV[np.ix_(keep, keep)])
    F = 0.5 * (F + F.T)
    mc, ma = binned(CTL, lens, ctl_warp)[keep], binned(arm_path, lens, warp)[keep]
    d = DATA[keep]
    Ac = float((mc @ F @ d) / (mc @ F @ mc))
    Aa = float((ma @ F @ d) / (ma @ F @ ma))
    rc, ra = d - Ac * mc, d - Aa * ma
    c2c, c2a = float(rc @ F @ rc), float(ra @ F @ ra)
    dl = Aa * ma - Ac * mc
    sep = float(dl @ F @ dl)
    F2 = c2a - c2c
    return dict(n=int(keep.sum()), c2c=c2c, c2a=c2a, F2=F2, sep=sep,
                sep_over=sep / c2c, F2_over=F2 / c2c,
                cross=-2.0 * float(dl @ F @ rc),
                gap=abs(F2 - sep) / max(abs(F2), sep),
                bound=2.0 / math.sqrt(sep / c2c))


print(__doc__)
print("=" * 104)
print("  r7654 (60) -- P18 l.1557-1559's two measures, pinned, with the identity and the bound")
print("=" * 104)

# ------------------------------------------------------------------ Ⓐ the instrument
print("\nⓐ  THE BINS AND THE OPERATOR, ASSERTED AND NOT INHERITED")
FULL = np.isfinite(binned(CTL, True))
R133 = FULL & (HI <= 1296)
print(f"      full set       {int(FULL.sum())} bins, ell {int(LO[FULL][0])}-{int(HI[FULL][-1])}")
print(f"      restricted     {int(R133.sum())} bins, ell {int(LO[R133][0])}-{int(HI[R133][-1])}")
check(f"ⓐ① the full set is 185 bins at ell {int(LO[FULL][0])}-{int(HI[FULL][-1])}, the range P18's "
      f"sentence names", int(FULL.sum()) == 185 and int(HI[FULL][-1]) == 1996)
check(f"ⓐ② and the ell<=1296 restriction is 133 bins, taken from the likelihood's own edges rather "
      f"than from a count", int(R133.sum()) == 133)
print(f"      the saved FULL lensing operator at ell 1900: {R1900:.4f}")
check("ⓐ③ the operator is the full lensed/unlensed ratio, inside the [1.05, 1.08] band cc66's own "
      "receipt gates it into -- read as a saved array, so camb stays off this interpreter",
      1.05 <= R1900 <= 1.08)
check("ⓐ④ and this file does not import the corpus's own scorer, so the figures P18 prints are "
      "pinned by a second instrument and not by a re-run of the one that made them",
      'chi2_of_spectrum' not in sys.modules)

# ------------------------------------------------------------------ Ⓑ every row
print("\nⓑ  EVERY (ARM, HALF, BIN SET) ROW -- the one P18 names is the first")
ROWS = {}
for kn, keep in (('185', FULL), ('133', R133)):
    for half, lens in (('LENSED', True), ('unlensed', False)):
        for tag, path in (('arm of record', AOR), ('LEAFREC=0', LR0)):
            ROWS[(kn, half, tag)] = row(keep, path, lens)
print(f"\n      {'bins':>5} {'half':<9} {'arm':<14} {'chi2_c':>9} {'chi2_a':>9} {'F2':>9}"
      f" {'chi2_sep':>9} {'sep/c':>7} {'F2/c':>7} {'gap':>7} {'bound':>7}")
for kn in ('185', '133'):
    for half in ('LENSED', 'unlensed'):
        for tag in ('arm of record', 'LEAFREC=0'):
            r = ROWS[(kn, half, tag)]
            print(f"      {r['n']:>5} {half:<9} {tag:<14} {r['c2c']:>9.2f} {r['c2a']:>9.2f}"
                  f" {r['F2']:>9.2f} {r['sep']:>9.2f} {r['sep_over']:>7.2f} {r['F2_over']:>7.2f}"
                  f" {r['gap']*100:>6.2f}% {r['bound']:>7.3f}")

P18 = ROWS[('185', 'LENSED', 'arm of record')]

# ------------------------------------------------------------------ Ⓒ the pins
print("\nⓒ  THE FOUR FIGURES P18 PRINTS, EACH PINNED BY A PARSED COMPARISON")
PINS = [
    ('the separation is 1.77 times the control\'s own distance from the data',
     'sep_over', 1.77, 0.005),
    ('the difference of the two arms\' scores is 1.35 times it', 'F2_over', 1.35, 0.005),
    ('that difference is 288.04', 'F2', 288.04, 0.005),
    ('against the control\'s own 214.1', 'c2c', 214.1, 0.05),
]
for label, key, want, tol in PINS:
    got = P18[key]
    print(f"      {label:<62} printed {want:>9.2f}   computed {got:>9.4f}"
          f"   |d| {abs(got-want):.4f} <= {tol}")
    check(f"ⓒ `{label}` -- pinned to half a unit in its last printed digit", abs(got - want) <= tol)
_q = P18['gap']
print(f"      the two measures are a quarter apart{'':<27} printed     0.25   computed {_q:>9.4f}"
      f"   nearest 5pp {round(_q*20)/20:.2f}")
check("ⓒ⑤ and \"a quarter apart\" -- the one prose figure, pinned at the nearest five percentage "
      "points rather than to a digit it does not print, and the measured value printed beside it",
      abs(round(_q * 20) / 20 - 0.25) < 1e-9)

# ------------------------------------------------------------------ Ⓓ the identity and the bound
print("\nⓓ  THE IDENTITY AND THE BOUND, ON ALL EIGHT ROWS AND NOT ONLY THE ONE THE PAPER NEEDS")
_id = [(k, abs(r['F2'] - (r['sep'] + r['cross'])) <= 1e-6 * max(1.0, r['sep']))
       for k, r in ROWS.items()]
check(f"ⓓ① F2 == chi2_sep - 2 delta' F r_c on all {len(_id)} rows, to floating point -- CHECKED, "
      f"with the cross term computed and not inferred", all(ok for _k, ok in _id))
_bd = [(k, abs(r['F2'] / r['sep'] - 1.0) <= r['bound']) for k, r in ROWS.items()]
check(f"ⓓ② and the bound |F2/chi2_sep - 1| <= 2/sqrt(chi2_sep/chi2_c) on the same {len(_bd)} rows",
      all(ok for _k, ok in _bd))
_r4236 = abs(15472.6 / 16260.5 - 1.0) <= 2.0 / math.sqrt(58.198)
print(f"      r4236's own printed row, for the price of its 5%: ratio 58.20, bound "
      f"{2.0/math.sqrt(58.198):.4f}, gap {abs(15472.6/16260.5-1.0):.4f}")
check("ⓓ③ the bound holds on r4236's row too, read from its own printed numbers -- which is why its "
      "4.84% agreement was available there and is not available at 1.77", _r4236)
print(f"      and at the arm of record the bound is {P18['bound']:.3f}, so NOTHING forces the two "
      f"measures to agree to anything;")
print(f"      the bound alone does not reach 5% until chi2_sep/chi2_c exceeds {(2/0.05)**2:.0f}.")
check("ⓓ④ so the old \"agree to within 5%\" is priced: at the arm of record the bound exceeds 1, "
      "i.e. the two measures could differ by more than 100% and still satisfy it",
      P18['bound'] > 1.0)

# ------------------------------------------------------------------ Ⓔ failability, measured
print("\nⓔ  EVERY PIN IS FAILABLE -- MEASURED, AGAINST THE SPECTRUM EACH FIGURE DEPENDS ON")
print("""      ⌗ A PURE RESCALING WOULD BE THE WRONG PERTURBATION and the receipt says so by running it:
      the amplitude is fitted in closed form, so multiplying the arm by a constant is absorbed exactly
      and moves no pin.  A perturbation that cannot move the pin cannot show it failable.  So the
      failability arm uses a 1% TILT in ell, which one amplitude cannot absorb.""")
_resc = row(FULL, AOR, True, warp=lambda ls: np.full_like(ls, 1.01))
check("ⓔ① the control run: a 1% RESCALING moves none of the four pins, because the fitted amplitude "
      "absorbs it exactly -- so this is not the perturbation that tests them",
      all(abs(_resc[k] - P18[k]) <= tol for _l, k, _w, tol in PINS))
TILT = (lambda ls: 1.0 + 0.01 * (ls / 1000.0 - 1.0))
_tilt = row(FULL, AOR, True, warp=TILT)
_ctilt = row(FULL, AOR, True, ctl_warp=TILT)
print(f"\n      {'pin':<52} {'unperturbed':>12} {'arm tilted':>12} {'ctl tilted':>12}")
for label, key, want, tol in PINS:
    print(f"      {label[:52]:<52} {P18[key]:>12.4f} {_tilt[key]:>12.4f} {_ctilt[key]:>12.4f}")
_ARM = [k for _l, k, _w, _t in PINS if k != 'c2c']
check("ⓔ② the THREE ARM-DEPENDENT pins -- 1.77, 1.35 and 288.04 -- each fall outside tolerance under "
      "a 1% tilt of the ARM, so each is a guard that can fail on the data it is given",
      all(abs(_tilt[k] - w) > t for _l, k, w, t in PINS if k != 'c2c'))
print("""
      ⛔ ARM ⑤ AS FIRST REGISTERED MISSED HERE, AND THE MISS IS KEPT (`r7654+60.1`).  It said ONE
      perturbation of the ARM would move all FOUR pins.  The fourth is chi2 of the CONTROL, which does
      not read the arm's spectrum anywhere, so no perturbation of the arm can move it -- and the arm
      was asking a quantity to depend on something it does not depend on.  ⇒ The corrected rule tests
      each figure against the spectrum it actually depends on, and is strictly stronger: it pins an
      INVARIANCE the original never tested.""")
check(f"ⓔ③ ⑤″ the control's 214.1 is INVARIANT under the arm's tilt, EXACTLY -- which is what makes "
      f"it the control's figure and not the comparison's ({_ctilt['c2c']:.4f} computed with the "
      f"control tilted against {_tilt['c2c']:.4f} with only the arm tilted)",
      _tilt['c2c'] == P18['c2c'])
check("ⓔ④ ⑤‴ and it IS failable under a 1% tilt of the CONTROL, the perturbation it does depend on -- "
      "under which ALL FOUR of the sentence's figures move outside tolerance, since all four read the "
      "control", all(abs(_ctilt[k] - w) > t for _l, k, w, t in PINS))
check("ⓔ⑤ the arm's tilt also moves the ratio the sentence leads with by more than its last printed "
      f"digit, so the 1.77 is pinned and not merely printed ({P18['sep_over']:.4f} -> "
      f"{_tilt['sep_over']:.4f})", abs(_tilt['sep_over'] - P18['sep_over']) > 0.005)

# ------------------------------------------------------------------ Ⓕ the one clause to read narrowly
print("\nⓕ  THE CLAUSE THAT IS TRUE OF THIS CONFIGURATION AND NOT IN GENERAL")
_above = {k: (r['sep_over'] > 1.0 and r['F2_over'] > 1.0) for k, r in ROWS.items()}
print("""      P18: both measures put "the arms further from each other than the control is from the
      data".  That is BOTH ratios above 1.  Where it holds, by row:""")
for kn in ('185', '133'):
    for half in ('LENSED', 'unlensed'):
        for tag in ('arm of record', 'LEAFREC=0'):
            r = ROWS[(kn, half, tag)]
            print(f"        {kn:>3} {half:<9} {tag:<14} sep/c {r['sep_over']:>5.2f}  "
                  f"F2/c {r['F2_over']:>5.2f}   both>1: {_above[(kn, half, tag)]}")
check("ⓕ① it HOLDS on the configuration the sentence names -- the full-range LENSED bins, arm of "
      "record", _above[('185', 'LENSED', 'arm of record')])
check("ⓕ② and it FAILS on the unlensed rows, so it is a fact about those bins and not a general "
      "statement -- printed here so no reader takes the stronger reading, and reported rather than "
      "repaired, because the sentence as re-stated at r7653 names its configuration",
      not _above[('185', 'unlensed', 'arm of record')]
      and not _above[('133', 'unlensed', 'arm of record')])

print("\n" + "=" * 104)
print(f"  {len(_fail)} failure(s)")
for f in _fail:
    print("   [FAIL] " + f)
sys.exit(1 if len(_fail) > 0 else 0)
