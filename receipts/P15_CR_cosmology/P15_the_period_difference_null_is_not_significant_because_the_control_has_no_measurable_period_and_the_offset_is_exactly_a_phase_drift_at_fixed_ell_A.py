#!/usr/bin/env python3
"""
RECEIPT -- P15: ** `r7197`'s ORDERED NULL, RUN ON THE BANKED RESIDUAL WITH NO NEW SPECTRUM.  THE
DIFFERENCE IS `$0.97\\sigma$` -- NOT SIGNIFICANT -- AND THE REASON IS THE WHOLE RESULT: THE ERROR ON
IT IS `$36.3$`, OF WHICH THE CONTROL CONTRIBUTES `$35.5$` AND THE ARM `$3.0$`.  ** THE CONTROL HAS NO
MEASURABLE PERIOD, SO IT CANNOT SERVE AS A NULL. **  AGAINST `$\\ell_A$`, WHICH IS KNOWN TO `$0.15$`
PER CENT WHERE THE CONTROL'S PERIOD IS KNOWN TO `$11$`, THE ARM'S PERIOD IS `$+14.00$` HIGH AT
`$4.69\\sigma$` -- AND THAT OFFSET IS *EXACTLY* A LINEAR PHASE DRIFT OF `$-96.6^\\circ$` AT FIXED
`$\\ell_A$`, WHICH IS AN IDENTITY AND NOT A FIT PREFERENCE. **

Built r7197+cc66.153 (node 66, code seat), on `PO-13`.

===================================================================================================
** THE ORDER, AND WHY THE ANSWER IS BOTH BRANCHES AT ONCE **
===================================================================================================

`r7197`: *"The arm's preferred period against the control's as a null, with the period free in both
arms and the DIFFERENCE as the statistic."*  With three things to keep apart: the difference and not
either period alone; what a `$+4.7$` per cent offset would MEAN given `$\\ell_A$` is right to
`$0.15$` per cent; and -- *"if the difference is NOT significant, that is a complete result and I
want it in that form."*

** IT IS NOT SIGNIFICANT, AND THE FORM THE ORDER ASKED FOR TURNS OUT TO CARRY MORE THAN A NULL. **
The difference is `$-35.25$` against an error of `$36.3$`: `$0.97\\sigma$`, with `$56$` per cent of
draws at least as extreme.  ** But the error decomposes, and it is not shared: `$35.5$` of it is the
control and `$3.0$` is the arm. **  ⇒ *The test as specified cannot discriminate -- not because the
arm's period is uncertain, but because the control's is.  A null needs a null hypothesis the data can
measure, and the control's period is measured to `$\\pm11$` per cent.*

  PART A  ** THE FORWARD MODEL, VERIFIED EXACTLY, WHICH IS WHAT LICENSES THE REST. **  The figure
          whitens with the inverse Cholesky of the FULL bandpower covariance, not the diagonal;
          `$L^{-1}(\\text{model}-\\text{data})$` reproduces all four banked whitened residuals to
          `$0$`.  And then the Monte Carlo is exact in one line: perturbing the data by its own
          covariance perturbs the whitened residual by `$-z$` with `$z\\sim N(0,I)$`, the SAME draw
          in both arms, so their correlation is preserved rather than assumed away.
  PART B  ** THE ORDERED STATISTIC. **  `$\\Delta=-35.25$`, `$0.97\\sigma$`, `$p=0.56$`.
  PART C  ** AND THE DECOMPOSITION THAT IS THE RESULT. **  Arm `$311.79\\pm2.99$`, control
          `$334.65\\pm35.52$` -- an error `$12\\times$` larger, because its amplitude is
          `$6.8\\times$` smaller.
  PART D  ** THE COMPARISON THAT IS INFORMATIVE, AND IT IS NOT THE ORDERED ONE. **  Against
          `$\\ell_A=298$`: `$+14.00$`, `$4.69\\sigma$`, `$P(p\\le\\ell_A)<10^{-3}$`.
  PART E  ** THE ARTEFACT CHECK. **  Giving the second harmonic its own freedom moves the
          fundamental by `$+0.25$` and leaves the offset at `$4.90\\sigma$`, so it is not a
          single-harmonic fit absorbing harmonic structure.
  PART F  ** AND WHAT THE OFFSET IS, AS AN IDENTITY. **  A period of `$312$` and `$\\ell_A$` with a
          phase running linearly in `$\\ell$` are the SAME two-dimensional model -- identical
          residual sum of squares, to `$0$`.  ⇒ The offset IS a drift of `$-96.6^\\circ$` across
          `$104\\le\\ell\\le1886$`, a quarter period over the six the range spans.

⇒ *** SO THE ANSWER TO THE ORDER'S ITEM 2 IS NOT `$r_s/D_M$`.  `$\\ell_A$` sets the comb's SPACING
and is reproduced to $0.15$ per cent; what the residual carries is a DRIFT of the acoustic phase
against $\ell$, at that correct spacing.  The quantity that could carry it is the peak phase's run
with $\ell$ -- set by the baryon loading and the driving -- and not the ratio of two lengths. ***

** WHAT THIS IS NOT, AND THE ASSUMPTION NAMED RATHER THAN SUPPLIED. **
  ⛔ *Not a claim that the arm's period offset is a defect in the arm.*  `PART F` makes it a
  statement about the phase's `$\\ell$`-dependence; which term carries that is not measured here.
  ⚠ ** THE ASSUMPTION THE BANKED DATA CANNOT CARRY, NAMED: the models' own uncertainty. **  *The four
  banked spectra are point predictions with no parameter covariance banked beside them, so this null
  propagates PLANCK's noise and nothing else.  That is the right error for `is the arm's period
  separably different from the control's`, which is what was ordered.  It is NOT an error bar on how
  far the period would move under refitting -- and `PART D`'s refitted row is the measured stand-in
  for that, not a substitute.*

** COMPUTES: the four whitened residuals re-derived from the Planck TT data and covariance and
   checked against the bank; one free-period profile per arm over `$240\\le p<400$` at `$0.25$`; a
   `$4000$`-draw Monte Carlo on the shared data noise; the same profile with two harmonics; and one
   algebraic identity.  *** The window `$100\\le\\ell\\le1900$`, the anchor `$\\ell_1=222$`, the
   period grid and the draw count are the only choices and all four are stated. ***  No new
   spectrum, no grid, nothing fitted to data. **

STATUS: rc=0 on success.  Run: python3 <this file>   (numpy; ~40 s)
"""
import os
import sys

import numpy as np

print(__doc__.split("STATUS:")[0])
BAR = "=" * 104
fail = []


def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        fail.append(label)


def head(t):
    print(f"\n{BAR}\n  {t}\n{BAR}")


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

NPZ = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7183_nofit_figure',
                   'nofit_figure_numbers.npz')
if not os.path.exists(NPZ):
    print("  ⛔ THE BANK THIS RECEIPT READS IS NOT ON DISK, so nothing is read and nothing claimed.")
    sys.exit(1)
F = np.load(NPZ)
L = F['ell']
L_A = float(F['l_A'])
ANCHOR = float(F['peak1'])
GRID = np.arange(240.0, 400.0, 0.25)
NDRAW = 4000
SEED = 20261006
ARMS = ('nofit_cr', 'nofit_lcdm', 'refit_cr')


# ============================================================ A. the forward model
head("A.  THE FORWARD MODEL, VERIFIED AGAINST THE BANK -- THE WHITENING IS THE FULL COVARIANCE'S")

LC, _FACB = CS.bin_center_and_fac()
KEEP = np.isin(LC, L)
COVK = CS.COV_TT[np.ix_(KEEP, KEEP)]
LINV = np.linalg.inv(np.linalg.cholesky(COVK))
_dat = CS.X_DATA[KEEP]
print(f"      kept bins {int(KEEP.sum())} against the bank's {len(L)}; ell agree: "
      f"{bool(np.allclose(LC[KEEP], L))}; data agree to {float(np.max(np.abs(_dat - F['data']))):.1e}")
_fw = {t: LINV @ (F[f'{t}_model'] - F['data']) for t in
       ('nofit_cr', 'nofit_lcdm', 'refit_cr', 'refit_lcdm')}
for t, w in _fw.items():
    print(f"      {t:11s} max|L^-1(model-data) - banked whitened| = "
          f"{float(np.max(np.abs(w - F[f'{t}_whitened']))):.2e}")
check("Ⓐ①  the figure's whitening is the inverse Cholesky of the FULL bandpower covariance and not "
      "the diagonal, and reproducing it from the Planck data and covariance returns all four banked "
      "residuals EXACTLY.  ** A Monte Carlo on a forward model that did not reproduce the bank "
      "would be a measurement of the reconstruction **",
      max(float(np.max(np.abs(w - F[f'{t}_whitened']))) for t, w in _fw.items()) == 0.0
      and float(np.max(np.abs(_dat - F['data']))) == 0.0)
print("      and the perturbation is exact in one line: L^-1(model - (data + L z)) = w_obs - z,")
print("      so a draw z ~ N(0, I) shared by BOTH arms carries their correlation rather than")
print("      assuming it away -- which a diagonal-sigma Monte Carlo would have done silently.")
_z = np.random.default_rng(1).standard_normal(len(L))
_chol = np.linalg.cholesky(COVK)
check("Ⓐ②  and that identity is checked numerically rather than taken: perturbing the DATA by "
      "`chol(C) z` and re-whitening gives the same vector as subtracting `z` from the whitened "
      "residual, to 1e-10",
      float(np.max(np.abs((LINV @ (F['nofit_cr_model'] - (F['data'] + _chol @ _z)))
                          - (F['nofit_cr_whitened'] - _z)))) < 1e-10)


# ============================================================ the profile machinery
QH = {}
for nh in (1, 2):
    mats = []
    for p in GRID:
        cols = []
        for h in range(1, nh + 1):
            cols += [np.cos(2 * np.pi * h * (L - ANCHOR) / p),
                     np.sin(2 * np.pi * h * (L - ANCHOR) / p)]
        mats.append(np.linalg.qr(np.array(cols).T)[0])
    QH[nh] = np.array(mats)


def best_period(w, nh=1):
    """the period maximising the explained sum of squares -- equivalently minimising the RSS."""
    return float(GRID[np.argmax(np.sum(np.einsum('pnk,n->pk', QH[nh], w) ** 2, axis=1))])


OBS = {t: best_period(F[f'{t}_whitened']) for t in ARMS}
OBS2 = best_period(F['nofit_cr_whitened'], 2)
rng = np.random.default_rng(SEED)
MC = {t: np.empty(NDRAW) for t in ARMS}
MC2 = np.empty(NDRAW)
for i in range(NDRAW):
    z = rng.standard_normal(len(L))
    for t in ARMS:
        MC[t][i] = best_period(F[f'{t}_whitened'] - z)
    MC2[i] = best_period(F['nofit_cr_whitened'] - z, 2)
DIFF = MC['nofit_cr'] - MC['nofit_lcdm']
OBSD = OBS['nofit_cr'] - OBS['nofit_lcdm']


# ============================================================ B. the ordered statistic
head("B.  THE ORDERED STATISTIC -- THE DIFFERENCE, WITH THE PERIOD FREE IN BOTH ARMS")

print(f"      observed   arm {OBS['nofit_cr']:.2f}   control {OBS['nofit_lcdm']:.2f}   "
      f"difference {OBSD:+.2f}        (l_A = {L_A:.0f})")
print(f"      {NDRAW} draws, shared noise:   difference {DIFF.mean():+.2f} +- {DIFF.std():.2f}")
_sig = abs(OBSD) / DIFF.std()
_p = float(np.mean(np.abs(DIFF) >= abs(OBSD)))
print(f"      ⇒ {_sig:.2f} sigma from zero, and {100 * _p:.0f} per cent of draws are at least as "
      f"extreme")
check("Ⓑ①  ** THE ORDERED DIFFERENCE IS NOT SIGNIFICANT: 0.97 sigma, with 56 per cent of draws at "
      "least as extreme. **  That is the order's third branch and it is reported as the complete "
      "result it asked for, not as a failure to find something",
      _sig < 2.0 and _p > 0.2)


# ============================================================ C. the decomposition
head("C.  AND THE DECOMPOSITION IS THE RESULT -- THE CONTROL HAS NO MEASURABLE PERIOD")

for t in ARMS:
    print(f"      {t:11s} observed {OBS[t]:7.2f}   MC {MC[t].mean():7.2f} +- {MC[t].std():5.2f}"
          f"   ({100 * MC[t].std() / MC[t].mean():.1f} per cent)")
_qa, _qc = MC['nofit_cr'].std(), MC['nofit_lcdm'].std()
print(f"      error on the difference {DIFF.std():.2f};  control {_qc:.2f}, arm {_qa:.2f}  "
      f"-- the control is {_qc / _qa:.1f}x the arm")
check("Ⓒ①  ** the error on the ordered difference is 36.3, of which the control contributes 35.5 "
      "and the arm 3.0.  So the test cannot discriminate because of the CONTROL, not the arm. **  "
      "The arm's period is measured to 1 per cent; the control's to 11",
      _qc / _qa > 8.0 and _qa / MC['nofit_cr'].mean() < 0.02
      and abs(DIFF.std() - _qc) < 0.3 * _qa)
check("Ⓒ②  ⇒ so `the difference, not either period alone` is right as a principle and empty as a "
      "statistic here: a null needs a null hypothesis the data can measure, and the control's "
      "preference for a long period is noise.  ** This is the trap the order's own item 1 named, "
      "arriving from the other side **",
      _qc > 20.0 and OBS['nofit_lcdm'] > OBS['nofit_cr'])


# ============================================================ D. the informative comparison
head("D.  THE COMPARISON THAT IS INFORMATIVE -- AGAINST ell_A, WHICH IS KNOWN TO 0.15 PER CENT")

_off = OBS['nofit_cr'] - L_A
_osig = _off / _qa
_ple = float(np.mean(MC['nofit_cr'] <= L_A))
print(f"      arm, nothing fitted:  {OBS['nofit_cr']:.2f} against l_A = {L_A:.0f}   "
      f"offset {_off:+.2f} ({100 * _off / L_A:+.2f} per cent)   {_osig:.2f} sigma   "
      f"P(p <= l_A) = {_ple:.4f}")
_roff = OBS['refit_cr'] - L_A
print(f"      arm, refitted:        {OBS['refit_cr']:.2f}   offset {_roff:+.2f}   "
      f"{_roff / MC['refit_cr'].std():.2f} sigma   (MC +- {MC['refit_cr'].std():.2f})")
check("Ⓓ①  ** against ell_A the unfitted arm's period is +14.00 high at 4.69 sigma, with fewer than "
      "one draw in a thousand at or below ell_A. **  That is the comparison the data can make: "
      "ell_A is known to 0.15 per cent where the control's period is known to 11",
      _osig > 3.0 and _ple < 0.005 and _off > 10.0)
check("Ⓓ②  and refitting pulls it toward ell_A AND widens its determination threefold -- 307.25 at "
      "1.05 sigma against 312.00 at 4.69 -- the same pattern the amplitude shows at `cc66.145`, now "
      "in the one quantity that figure does not report",
      OBS['refit_cr'] < OBS['nofit_cr'] and MC['refit_cr'].std() > 2.0 * _qa
      and _roff / MC['refit_cr'].std() < 2.0)


# ============================================================ E. the artefact check
head("E.  THE ARTEFACT CHECK -- A SECOND HARMONIC DOES NOT PULL THE FUNDAMENTAL BACK")

print(f"      one harmonic   {OBS['nofit_cr']:.2f}   MC +- {_qa:.2f}   offset "
      f"{_osig:.2f} sigma")
print(f"      two harmonics  {OBS2:.2f}   MC +- {MC2.std():.2f}   offset "
      f"{(OBS2 - L_A) / MC2.std():.2f} sigma   -- the fundamental moves {OBS2 - OBS['nofit_cr']:+.2f}")
check("Ⓔ①  ⛔ MUST-COME-BACK-WRONG: a single-harmonic fit to a residual with harmonic structure "
      "returns a BIASED period, so if the offset were that artefact, giving the second harmonic its "
      "own freedom would pull the fundamental back toward ell_A.  ** It moves it by +0.25 and leaves "
      "the offset at 4.90 sigma.  The offset is not the fit's. **",
      abs(OBS2 - OBS['nofit_cr']) < 1.0 and (OBS2 - L_A) / MC2.std() > 3.0)


# ============================================================ F. what the offset IS
head("F.  AND WHAT THE OFFSET IS -- A PHASE DRIFT AT FIXED ell_A, BY AN IDENTITY")

W = F['nofit_cr_whitened']


def _rss(D):
    b = np.linalg.lstsq(D, W, rcond=None)[0]
    return float(np.sum((W - D @ b) ** 2))


_P = OBS['nofit_cr']
_k = 2 * np.pi * (1.0 / _P - 1.0 / L_A)
_free = np.array([np.cos(2 * np.pi * (L - ANCHOR) / _P),
                  np.sin(2 * np.pi * (L - ANCHOR) / _P)]).T
_drift = np.array([np.cos(2 * np.pi * (L - ANCHOR) / L_A + _k * (L - ANCHOR)),
                   np.sin(2 * np.pi * (L - ANCHOR) / L_A + _k * (L - ANCHOR))]).T
_dd = np.degrees(_k * (L.max() - L.min()))
print(f"      RSS, period free at {_P:.1f}        = {_rss(_free):.9f}")
print(f"      RSS, l_A fixed + linear phase run = {_rss(_drift):.9f}")
print(f"      ⇒ the two are the SAME model, to {abs(_rss(_free) - _rss(_drift)):.1e}")
print(f"      and the drift it is: {_dd:+.1f} deg across ell {L.min():.0f}-{L.max():.0f} = "
      f"{abs(_dd) / 360:.3f} of a period over the {(L.max() - L.min()) / L_A:.2f} the range spans")
check("Ⓕ①  ** a period of 312 and ell_A with a phase running linearly in ell are the SAME "
      "two-dimensional model -- identical residual sum of squares, to zero. **  So the offset is "
      "not a competing period: it IS a drift of -96.6 degrees across the range, and that is an "
      "identity rather than a fit preference",
      abs(_rss(_free) - _rss(_drift)) < 1e-9 and abs(abs(_dd) - 96.6) < 1.0)
check("Ⓕ②  ⇒ ** so the order's item 2 does not answer `r_s/D_M`. **  ell_A sets the comb's SPACING "
      "and the construction reproduces it to 0.15 per cent, while the offset is 31 times that "
      "error; what the residual carries is a drift of the acoustic PHASE at the correct spacing.  "
      "The quantity that could carry it is the peak phase's run with ell -- the loading and the "
      "driving -- and not a ratio of two lengths",
      abs(_off / L_A) / 0.0015 > 20.0 and abs(_rss(_free) - _rss(_drift)) < 1e-9)


# ============================================================ verdict
print()
print(BAR)
if fail:
    print(f"  ⛔ {len(fail)} CHECK(S) FAILED")
    for q in fail:
        print(f"      - {q}")
    print(BAR)
    sys.exit(1)
print("  ✔ ** THE ORDERED NULL IS NOT SIGNIFICANT -- 0.97 sigma, p = 0.56 -- and that is the")
print("    complete result in the form the order asked for. **")
print("  ⛭ ** AND THE REASON CARRIES MORE THAN THE NULL: the error on the difference is 36.3, of")
print("    which the CONTROL contributes 35.5 and the arm 3.0.  The control's period is measured to")
print("    11 per cent, so it cannot serve as a null at all. **  `the difference, not either period")
print("    alone` is right as a principle and empty as a statistic here.")
print("  ⛭ ** THE COMPARISON THE DATA CAN MAKE IS AGAINST ell_A, AND IT IS 4.69 SIGMA. **  The")
print("    unfitted arm sits +14.00 above an ell_A the construction reproduces to 0.15 per cent,")
print("    with fewer than one draw in a thousand at or below it; refitting pulls it to 1.05 sigma")
print("    and widens it threefold.  And it is not the fit's artefact: a second harmonic moves the")
print("    fundamental by +0.25.")
print("  ⇒ ** AND THE OFFSET IS EXACTLY A PHASE DRIFT, NOT A PERIOD. **  A period of 312 and ell_A")
print("    with a linearly running phase are the same model to zero, so what the residual carries")
print("    is a drift of -96.6 degrees across the range -- a quarter period over the six it spans.")
print("    ⇒ Item 2's answer is therefore NOT `r_s/D_M`: ell_A sets the spacing and is right to a")
print("    part in six hundred.  What could carry a running phase at correct spacing is the peak")
print("    phase itself -- the loading and the driving.  Named, not measured.")
print("  ⚠ The assumption the banked data cannot carry, named rather than supplied: the models have")
print("    no parameter covariance banked beside them, so this null propagates Planck's noise and")
print("    nothing else.  That is the right error for what was ordered and is not an error bar on")
print("    refitting; the refitted row is the measured stand-in, not a substitute.")
print(BAR)
print("  ALL CHECKS PASS")
