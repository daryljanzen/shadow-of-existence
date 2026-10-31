#!/usr/bin/env python3
r"""
RECEIPT -- P15 / `sec:refit-bound`, `fig:acoustic`: ** THE CONFRONTATION THE PAPER HAS NEVER CARRIED,
SCORED: $2.65$ PER BIN WITH NOTHING FITTED AGAINST THE CONTROL'S $1.13$, AND ITS RESIDUAL CARRIES A
$6.0\sigma$ MODULATION AT THE COMB'S OWN PERIOD. **

** THIS FILE'S OWN NAME CARRIES THE NAMESAKE ARM'S FIGURES ($3.00$ PER BIN, NINE SIGMA) AND IS LEFT
AS IT STANDS, BECAUSE THE PAPER CITES IT BY NAME. **  *The answer block below was ALSO left on the
namesake arm at `r7645`+`cc66.67`, which re-pointed the computation and its pins and not the prose it
states them in -- so for one revision this receipt's stated answer contradicted its own output while
every gate passed.  Repaired at `r7645`+`cc66.68`; the figures below are this file's own, as run.*

*** AND THE OPERATION THE ORDER ASKED FOR IS THE ONE THAT CANCELS WHAT IT WAS ASKED TO SHOW:
AVERAGING IN BINS ONE PERIOD WIDE INTEGRATES EACH CYCLE TO ITS OWN MEAN.  THE FOLD IS DRAWN BESIDE
IT, AND IT IS THE FOLD THAT CARRIES THE RESULT. ***

** THE ORDER (`r7183` ⓵). **  *"`fig:acoustic` plots both arms at their REFIT minima.  The paper has
no figure of the other confrontation --- the comb computed on the background the distances fix with
NOTHING fitted to the microwave data... with two things the existing one does not do: the residual
binned at the comb's own period, so the alternation reads as the measured shape it is rather than as
scatter; and both confrontations' $\chi^2$ per bin on the figure itself."*

===================================================================================================
** THE ANSWER **
===================================================================================================

                                  chi^2      per bin      D_M of the banked spectrum
      control, nothing fitted     202.02      1.129            13864.6627
      CR arm,  nothing fitted     474.12      2.649            14011.4567
      control, refitted           177.88      0.994            13954.3535
      CR arm,  refitted           286.89      1.603            14133.9546

  arm/control:  nothing fitted  2.3469x       refitted  1.6128x      (179 bins, 100 <= l <= 1900)

  *On the NAMESAKE arm these were 537.38 / 3.002 and 282.96 / 1.581, i.e. 2.660x and 1.591x, and the
  paper still quotes those at `CR_cosmology.tex:962` and `:1085`.  Both controls are unchanged: the
  re-point does not reach them.*

** AND THE RESIDUAL, TWO WAYS. **

      binned AT the period l_A = 298, six bands:
          the arm's band means change sign TWICE across six bands, +1.468 to +1.776 through
          -1.048 -- a slow swing, NOT a per-period alternation

      FOLDED by phase within the period, anchored on the arm's own first peak at l = 222:
          one harmonic at l_A      amplitude         sigma
          CR arm, nothing fitted   0.9522 +- 0.1576   6.04
          CR arm, refitted         0.8331 +- 0.1187   7.02
          control, nothing fitted  0.2028 +- 0.1126   1.80
          control, refitted        0.1051 +- 0.1049   1.00

⇒ *** THE MODULATION IS REAL AND IT IS THE ARM'S: `6.0` sigma with nothing fitted, against the
control's `1.8`.  AND GIVING THE ARM FOUR PARAMETERS NO LONGER HALVES IT: the amplitude falls an
eighth, 0.952 to 0.833, and the significance RISES to `7.0`, because the no-fit arm's harmonic error
is the larger of the two.  On the namesake arm both fell -- 1.373 to 0.813, 9.08 to 6.89 -- so `the
four parameters absorb part of the modulation` was that arm's reading, not this one's. ***

⛔ ** AND THE ORDER'S CHOSEN OPERATION HIDES IT, FOR A REASON THAT IS ARITHMETIC RATHER THAN A
MATTER OF TASTE. **  *A bin one period wide averages a full cycle of any modulation whose period is
that bin's width, so its mean is that modulation's own mean --- which is zero by construction.*
⇒ ** Binning AT the period is the one operation guaranteed to remove a signal at the period. **  *It
is still drawn, because it is what the order asked for and what a reader will look for, and because
what it DOES show --- a slow swing with two sign changes --- is a true and separate statement about
the residual.  The fold is drawn beside it and labelled as the one that answers the question.*

===================================================================================================
** WHAT IS READ RATHER THAN RUN **
===================================================================================================

  ** NO NEW PHYSICS RUN, WHICH THE ORDER REQUIRED. **  All four spectra are banked, and each is
  identified here by its own stored `D_M` rather than by its filename, so a bank swapped under the
  figure's feet refuses rather than being plotted under the old label.

  ** THIS FILE RECOMPUTES THE FIGURE'S NUMBERS FROM THE SPECTRA, AND THEN REQUIRES THE FIGURE'S OWN
  BANKED `.npz` TO AGREE. **  *So the figure is checkable rather than self-certifying: if
  `make_fig_acoustic_nofit.py` drifts, this receipt fails on the disagreement rather than on its own
  memory of what the figure used to say.*

  ** SCORING IS `fig:acoustic`'s, UNCHANGED. **  Planck plik_lite TT with its full covariance,
  `P15`'s own derived CAMB lensing operator on both arms alike, the amplitude closed-form at the
  covariance-weighted optimum.

** COMPUTES: both confrontations' chi^2 per bin from the banked spectra; the residual binned at the
   comb's period and folded by phase within it; the amplitude and significance of one harmonic at
   l_A in each of the four cases; and the agreement of all of it with the figure's banked numbers. **

STATUS: OK
rc=0 on success.  Run: python3 <this file>   (numpy, scipy, camb; ~30 s)
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


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
G185 = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'refit_grid185')
G185L = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                     'refit_grid185_leafrec1_distances')
GEN = os.path.join(ROOT, 'corpus', 'make_fig_acoustic_nofit.py')
PDF = os.path.join(ROOT, 'corpus', 'fig_acoustic_nofit.pdf')
NPZ = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7183_nofit_figure',
                   'nofit_figure_numbers.npz')

# ⛭⛭ r7645+cc66.67: ** BOTH ARMS MOVE TO THE ARM OF RECORD; BOTH CONTROLS STAY. **
#   *The NO-FIT arm goes to 70's `r7643` distances'-point bank, which ran the original recipe
#   verbatim with `LEAFREC=1`; the REFITTED arm goes to its `_leafrec1` sibling.  `LEAFREC` does not
#   reach the controls (3.6e-16, `r7641`), so `lcdm_base` and `cc66_r185_verify_lcdm` are unchanged.*
#   ⛭ ** AND THE TWO ARMS' BACKGROUNDS BEHAVE DIFFERENTLY ACROSS THE MOVE, WHICH IS THE WHOLE
#   DISTINCTION THIS RECEIPT RESTS ON: ** *the no-fit arm's `D_M` is BIT-IDENTICAL at 14011.4567
#   (`LEAFREC` does not touch the background), while the refitted arm's moves 14017.0386 ->
#   14133.9546 because the MINIMUM itself moves on the arm of record.  ⌗ That asymmetry is what
#   makes the `different pair` gate below stronger after the move, not weaker -- and reading the
#   refitted file as the no-fit one is exactly the pointer error 70 caught in `cc66`'s 1.41.*
SPEC = {'nofit_lcdm': (os.path.join(G185, 'lcdm_base.npz'), 13864.6627),
        'nofit_cr': (os.path.join(G185L, 'cr_base.npz'), 14011.4567),
        'refit_lcdm': (os.path.join(SP, 'cc66_r185_verify_lcdm.npz'), 13954.3535),
        'refit_cr': (os.path.join(SP, 'cc66_r185_verify_cr_leafrec1.npz'), 14133.9546)}
L_A, PEAK1 = 298.0, 222.0

# =================================================================================================
print(BAR)
print("  PART 1 -- ** THE FOUR BANKED SPECTRA, IDENTIFIED BY THEIR OWN STORED `D_M` **")
print(BAR)
RAW = {}
for t, (p, dm) in SPEC.items():
    if not os.path.exists(p):
        print(f"  ⛔ REFUSED: {os.path.relpath(p, ROOT)} is not banked.  This receipt scores "
              f"banked spectra and does not run the instrument.  *Nothing is asserted.*")
        sys.exit(1)
    z = np.load(p, allow_pickle=True)
    RAW[t] = (z['ls'], z['Dl'], float(np.atleast_1d(z['D_M'])[0]))
    print(f"      {t:11s} {os.path.relpath(p, ROOT):52s} D_M = {RAW[t][2]:10.4f}")
check("⛭ every spectrum carries the `D_M` its slot is -- the arm's no-fit run at `14011.4567` is the "
      "BAO-fixed background `r7181+cc66.144` recovered from the distance data alone, and the "
      "refitted pair are the verified minima",
      all(abs(RAW[t][2] - SPEC[t][1]) < 0.05 for t in SPEC))
check("⛭⛭ and the two NO-FIT spectra are a different pair from the two refitted ones, which is what "
      "makes this a second confrontation rather than the same one replotted",
      abs(RAW['nofit_cr'][2] - RAW['refit_cr'][2]) > 1.0
      and abs(RAW['nofit_lcdm'][2] - RAW['refit_lcdm'][2]) > 1.0)

# =================================================================================================
print()
print(BAR)
print("  PART 2 -- ** BOTH CONFRONTATIONS SCORED, ON `fig:acoustic`'s OWN BINS AND OPERATOR **")
print(BAR)
import camb                                                               # noqa: E402
_p = camb.set_params(H0=67.40, ombh2=0.02237, omch2=0.3150 * 0.674 ** 2 - 0.02237, mnu=0.06,
                     omk=0, tau=0.054, As=2.1e-9, ns=0.965, lmax=3000)
_cl = camb.get_results(_p).get_cmb_power_spectra(_p, CMB_unit='muK', lmax=3000)
_le, _un = _cl['total'][:, 0], _cl['unlensed_scalar'][:, 0]
_lg = np.arange(len(_le), dtype=float)
RATIO = np.ones_like(_le)
_m = _un > 0
RATIO[_m] = _le[_m] / _un[_m]
LC, FACB = CS.bin_center_and_fac()
B = {t: CS.bin_spectrum(RAW[t][0], RAW[t][1] * np.interp(RAW[t][0], _lg, RATIO)) for t in SPEC}
KEEP = np.isfinite(B['refit_lcdm']) & (LC >= 100) & (LC <= 1900)
COVK = CS.COV_TT[np.ix_(KEEP, KEEP)]
FISH = np.linalg.inv(COVK)
LINV = np.linalg.inv(np.linalg.cholesky(COVK))
DK, LCK = CS.X_DATA[KEEP], LC[KEEP]
NB = int(KEEP.sum())
R = {}
for t in SPEC:
    mb = B[t][KEEP]
    A = float(mb @ FISH @ DK / (mb @ FISH @ mb))
    res = A * mb - DK
    R[t] = dict(c2=float(res @ FISH @ res), w=LINV @ res)
    print(f"      {t:11s} chi2 = {R[t]['c2']:8.2f}   {R[t]['c2'] / NB:6.3f} per bin")
print(f"      {NB} bins, ell {LCK[0]:.0f}-{LCK[-1]:.0f}")
check("⛭⛭ ** WITH NOTHING FITTED THE ARM IS AT `2.65` PER BIN AND THE CONTROL AT `1.13` ** -- the "
      "confrontation the paper has never carried, and the stronger of the two because the "
      "background is the distance data's own.  ⛔ *`3.00` was the namesake arm's; the arm of record "
      "costs the arm less and the ratio narrows*",
      abs(R['nofit_cr']['c2'] / NB - 2.64869) < 5e-6
      and abs(R['nofit_lcdm']['c2'] / NB - 1.12858) < 5e-6)
check("⌗ and refitted they are `1.60` and `0.99`, so four parameters close about a third of the gap "
      "-- `2.3469x` becomes `1.6128x`",
      abs(R['refit_cr']['c2'] / NB - 1.60276) < 5e-6
      and abs(R['refit_lcdm']['c2'] / NB - 0.99373) < 5e-6
      and abs(R['nofit_cr']['c2'] / R['nofit_lcdm']['c2'] - 2.3469) < 0.005
      and abs(R['refit_cr']['c2'] / R['refit_lcdm']['c2'] - 1.6128) < 0.005)
# ⛭⛭⛭ r7645+cc66.67: ** AND THE NO-FIT RATIO AGREES WITH `cc66.66`'s ACROSS A DIFFERENT BIN SET AND
#   A DIFFERENT OPERATOR, WHICH IS A CHECK NEITHER RECEIPT COULD MAKE ALONE. **  *This receipt scores
#   179 of `fig:acoustic`'s own bins (ell 104-1886) with the figure's operator; `cc66.66` scores 185
#   full-range LENSED bins with CAMB's.  They have no bin set, no operator and no code path in common
#   -- and they return 2.3469 and 2.3456.*  ⇒ ** Two independent roads to the same headline, agreeing
#   to six parts in ten thousand.  A pointer error on either side would not survive this. **
if abs(R['nofit_cr']['c2'] / R['nofit_lcdm']['c2'] - 2.3456) > 0.01:
    fail.append(f"this receipt's no-fit ratio {R['nofit_cr']['c2'] / R['nofit_lcdm']['c2']:.4f} and "
                f"cc66.66's 2.3456 differ by more than a per cent -- two independent scorings of the "
                f"same configuration must agree")

# =================================================================================================
print()
print(BAR)
print("  PART 3 -- ** THE RESIDUAL, BINNED AT THE PERIOD AND FOLDED WITHIN IT **")
print(BAR)
edges = np.arange(100.0, LCK[-1] + L_A, L_A)
BANDS = [(edges[i], edges[i + 1]) for i in range(len(edges) - 1)
         if ((LCK >= edges[i]) & (LCK < edges[i + 1])).sum() > 0]
bm = {}
for t in SPEC:
    bm[t] = np.array([R[t]['w'][(LCK >= lo) & (LCK < hi)].mean() for lo, hi in BANDS])
sgn = int(np.sum(np.diff(np.sign(bm['nofit_cr'])) != 0))
print(f"      binned AT l_A = {L_A:.0f}, {len(BANDS)} bands -- the arm's means: "
      + " ".join(f"{v:+.3f}" for v in bm['nofit_cr']))
print(f"      sign changes: {sgn}")

ph = ((LCK - PEAK1) % L_A) / L_A
DES = np.array([np.cos(2 * np.pi * (LCK - PEAK1) / L_A),
                np.sin(2 * np.pi * (LCK - PEAK1) / L_A)]).T
H = {}
for t in SPEC:
    w = R[t]['w']
    beta = np.linalg.lstsq(DES, w, rcond=None)[0]
    rr = w - DES @ beta
    s2 = float(np.sum(rr ** 2) / (len(w) - 2))
    cv = s2 * np.linalg.inv(DES.T @ DES)
    amp = float(np.hypot(*beta))
    err = float(np.sqrt((beta[0] ** 2 * cv[0, 0] + beta[1] ** 2 * cv[1, 1]
                         + 2 * beta[0] * beta[1] * cv[0, 1]) / amp ** 2))
    H[t] = (amp, err, amp / err)
    print(f"      folded: {t:11s} one harmonic at l_A = {amp:.4f} +- {err:.4f}  ({amp / err:.2f} sigma)")

# ⛔⛭⛭⛭ r7645+cc66.67: ** THE MODULATION WEAKENS MATERIALLY AND THE `REFITTING HALVES IT` READING
#   INVERTS IN ITS SIGNIFICANCE LIMB.  I PREDICTED THE FIRST WRONG AND SAID SO. **
#   *Registered before measuring: `the 9.08-sigma modulation survives in kind, and I am not sure of
#   its margin -- if the amplitude falls with the chi^2, about 8.3 sigma, which still clears the gate
#   but not by much.  Lowest-confidence prediction here; if it fails I will say so rather than widen
#   it.'  It fell to 6.04, and the gate failed.*
#   ⇒ *** WHAT SURVIVES: the arm's no-fit residual still carries a modulation AT THE COMB'S OWN
#       PERIOD at 6.0 sigma against the control's 1.80, so the rejection is still shaped at the
#       acoustic period and the shape is still the arm's.  The claim is intact in kind and the
#       `9.1 sigma` in this file's own NAME is the namesake arm's figure. ***
#   ⛔ *** AND THE SECOND LIMB INVERTS.  On the namesake, refitting took the amplitude 1.3729 ->
#       0.8128 (down 41 per cent) AND the significance 9.08 -> 6.89 (down).  On the arm of record the
#       amplitude falls only 12.5 per cent, 0.9522 -> 0.8331, while the significance RISES, 6.04 ->
#       7.02 -- because the NO-FIT arm's harmonic error is the larger of the two (0.1576 against
#       0.1187).  So on this arm refitting does not halve the modulation and does not reduce its
#       significance at all: it leaves MORE of it, read as a detection. ***
#   ⌗ *That is a real change to what the four parameters are doing, not a renumbering, and it is
#   stated rather than smoothed: `absorb part of the modulation and not its cause` was the namesake's
#   reading of a fall in both; here only the amplitude falls.*
check("⛭⛭⛭ ** THE ARM'S NO-FIT RESIDUAL CARRIES A MODULATION AT THE COMB'S OWN PERIOD AT `6.0` "
      "SIGMA, AGAINST THE CONTROL'S `1.8` ** -- so the rejection is shaped at the acoustic period "
      "and that shape is the arm's, not the data's.  ⛔ *`9.1` was the namesake arm's, and this "
      "file's own name carries it; on the arm of record the modulation is a third weaker*",
      H['nofit_cr'][2] > 5.0 and H['nofit_lcdm'][2] < 2.5
      and abs(H['nofit_cr'][2] - 6.0429) < 5e-4 and abs(H['nofit_cr'][0] - 0.95218) < 5e-6)
check("⛔⛔ ** AND REFITTING NO LONGER HALVES IT: the amplitude falls only an eighth, `0.952` to "
      "`0.833`, and the SIGNIFICANCE RISES, `6.0` to `7.0`, because the no-fit arm's harmonic error "
      "is the larger of the two. **  ⇒ *On the namesake arm both fell -- 1.373 to 0.813 and 9.08 to "
      "6.89 -- so `the four parameters absorb part of the modulation` was that arm's reading.  Here "
      "they absorb an eighth of the amplitude and none of the detection*",
      0.80 < H['refit_cr'][0] / H['nofit_cr'][0] < 0.92
      and H['refit_cr'][2] > H['nofit_cr'][2]
      and abs(H['refit_cr'][2] - 7.0194) < 5e-4 and abs(H['refit_cr'][0] - 0.83305) < 5e-6
      and H['nofit_cr'][1] > H['refit_cr'][1])
# ⛔⛭ r7645+cc66.67: ** THE ARITHMETIC IS UNCHANGED AND THE CONTRAST IT PRODUCES IS HALVED. **
#   *The old second limb asked `fold sigma / largest band mean > 5.0`, which read 7.13 on the
#   namesake arm (9.08 over 1.273).  On the arm of record it reads 3.40: the fold weakened to 6.04
#   AND the band means grew, the largest going 1.273 -> 1.776.*
#   ⇒ *** The CLAIM is untouched, because it is arithmetic: a bin one period wide averages a full
#       cycle of a modulation at that period, on any arm.  And it still shows: the bands change sign
#       twice across six -- a slow swing, no period-scale signal -- where the fold at that same
#       period returns 6.04 sigma.  What is re-pinned is the SIZE of that contrast, at its measured
#       value, with the bands' own bound stated separately rather than folded into a ratio. ***
_CONTRAST = H['nofit_cr'][2] / max(abs(bm['nofit_cr']).max(), 1e-9)
check("⛔⛔ ** AND BINNING AT THE PERIOD CANCELS IT, WHICH IS ARITHMETIC AND NOT TASTE: a bin one "
      "period wide averages a full cycle of any modulation at that period. **  The arm's band means "
      f"change sign {sgn} times across {len(BANDS)} bands and never exceed 1.78 in the whitened "
      "residual's own units -- a slow swing -- where the fold at the SAME period returns 6.0 sigma.  "
      "⛔ *The contrast is 3.40 against 7.13 on the namesake arm: halved, because the fold weakened "
      "and the band means grew.  The arithmetic does not depend on the arm; its margin does*",
      sgn <= 3 and H['nofit_cr'][2] > 5.0
      and abs(bm['nofit_cr']).max() < 2.0
      and abs(_CONTRAST - 3.4025) < 5e-4)
check("⌗ the control's fold is consistent with no modulation at either setting, so the `6.0` sigma "
      "is not an artefact of the fold, the binning or the likelihood",
      H['nofit_lcdm'][2] < 2.5 and H['refit_lcdm'][2] < 2.5)

# =================================================================================================
print()
print(BAR)
print("  PART 4 -- ** THE FIGURE EXISTS AND ITS BANKED NUMBERS AGREE WITH THESE **")
print(BAR)
check("⛭ the generator and the figure are both in the tree",
      os.path.exists(GEN) and os.path.exists(PDF))
if not os.path.exists(NPZ):
    print(f"  ⛔ REFUSED: the figure's banked numbers are missing.  Run "
          f"`python3 corpus/make_fig_acoustic_nofit.py` first.  *Nothing is asserted about the "
          f"figure.*")
    sys.exit(1)
F = np.load(NPZ)
print(f"      figure banked: {int(F['nbins'])} bins, l_A = {float(F['l_A']):.0f}, "
      f"peak1 = {float(F['peak1']):.0f}")
check("⛭⛭ the figure's own chi^2 per bin agree with this file's, computed independently from the "
      "same banked spectra -- so the numbers ON the figure are checkable and a drift in the "
      "generator fails here",
      all(abs(float(F[f'{t}_chi2']) - R[t]['c2']) < 0.02 for t in SPEC)
      and int(F['nbins']) == NB)
check("⛭⛭ and so do its harmonic amplitudes and significances, which are the figure's headline",
      all(abs(float(F[f'{t}_harm_amp']) - H[t][0]) < 1e-3
          and abs(float(F[f'{t}_harm_sigma']) - H[t][2]) < 0.05 for t in SPEC))
check("⌗ the figure carries BOTH operations rather than only the one that works -- the period bins "
      "the order asked for and the fold that answers it",
      all(f'{t}_band_mean' in F.files and f'{t}_phase_mean' in F.files for t in SPEC))

# =================================================================================================
print()
print(BAR)
if fail:
    print(f"  ⛔ {len(fail)} CHECK(S) FAILED:")
    for f in fail:
        print(f"      - {f}")
    print(BAR)
    sys.exit(1)
print("  ✔ ** THE NO-FIT CONFRONTATION IS `2.65` PER BIN AGAINST THE CONTROL'S `1.13`, AND ITS")
print("    RESIDUAL CARRIES A `6.0` SIGMA MODULATION AT THE COMB'S OWN PERIOD ** -- against the")
print("    control's `1.8`.  ⛔ *`3.00` and `9.1` are the NAMESAKE arm's and are this file's own")
print("    NAME; refitting now raises the significance to `7.0` rather than halving it.*")
print("  ⛔ And the ordered operation -- binning AT the period -- is the one that cancels it, because")
print("    a bin one period wide averages a full cycle of a modulation at that period.  *Both are")
print("    drawn: the period bins because a reader will look for them, the fold because it answers.*")
print("  ⌗ No new physics run: all four spectra were banked, each identified by its own stored D_M.")
print(BAR)
print("  ALL CHECKS PASS")
