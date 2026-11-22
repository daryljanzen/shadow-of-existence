"""
P15, r7855+cc66.5, on 69's order r7855: an INDEPENDENT check of 60's factor two in the CMB bank.

** THE FACTOR REPRODUCES.  ITS FLATNESS DOES NOT. **

  blk  bins   abs mean    abs min    abs max   abs spread   slope/bin
  TT    185   0.503313   0.471195   0.527829     0.056634   9.11e-07
  EE    185   0.497180   0.419497   0.565890     0.146394   8.51e-05
  TE    185   0.622380  -2.850705  10.590077    13.440782   1.45e-04

  60 report 0.504672 over 185 bins, ranging 0.500015 to 0.510557.

① `0.503313` against their `0.504672` is agreement to `0.27` per cent, on THE SAME BIN COUNT.
② And EE comes out `0.497180`, within `0.0061` of TT, so ONE mis-normalisation sits upstream of
   both and it is not a TT-path defect.
⛔ BUT THE PER-BIN SPREAD IS `0.056634`, FIVE TIMES the `0.010542` range they report.  The departure
   is NOT a slope -- `9.11e-07` per bin is nothing -- but oscillatory in `ell`, one to two per cent
   through the mid range and reaching `-6.4` per cent near `ell = 1920`.  That is the shape of a
   small acoustic-scale and damping difference, and the instrument's own log names it: peaks at
   220/540/812/1132 and `l_A = 301.375` against the sky's 220.6/538.1/809.8.
  ⇒ So "a flat factor of two" describes this bank to about five per cent, NOT to the one part in a
    hundred their range states, and anything read off that range's tightness should be re-read.

** THE BANK WAS REGENERATED, NOT READ FROM A CACHE, BECAUSE THE CACHE IS GONE. **  The order asked
for a comparison against "the arrays model6 reads".  Those arrays are NOT in the repository:
model3 reads them from POL_DIR, default /tmp/claude-0/pol_grid, which this container has lost, and
the committed ratio_grid3.npz beside it carries only SUM-DEPENDENCE RATIOS plus a divisor model3
never reads.  So the instrument was re-run for the one point the item needs, under POLSAVE, with
60's own switch values -- which compares the bank's DEFINITION rather than their arithmetic over a
cache, and is the stronger test.  ⌗ Third bank lost to a /tmp default on this line: r7847's 555-bin
mask, r7851's Phi bandpowers, this grid.  The regenerated point is COMMITTED, 12K.

** AND THE NORMALISATION CONVENTION IS DERIVED HERE, WHICH IS THE WHOLE POINT. **  An absolute
ratio is meaningless without it, and a factor two hides in exactly such a constant.  The instrument
normalises every mode to Phi = -1, so its spectra carry no primordial amplitude; in matter
domination Phi = -(3/5) zeta with P_zeta = A_s, so the missing constant is A_s * (3/5)^2, and the
muK^2 step is the harness's own T_CMB = 2.7255e6.  Measured with T_CMB^2 ALONE the ratio came out
6.657574e8; dividing 60's 0.504672 into that gives 7.58e-10 against A_s * (3/5)^2 = 7.56e-10,
identifying the convention to 0.3 per cent -- which was then APPLIED, not tuned.  ⌗ Stated plainly:
the convention was IDENTIFIED with the help of their number and then used independently of it; the
0.27 per cent agreement that follows is therefore a check of the SPECTRA, not of the constant.

** BANDS: TWO HOLD, ONE IS REFUTED, ONE SPLITS. **
  Ⓐ "the mean TT ratio is between 0.49 and 0.52"        -> HOLDS, 0.503313.
  Ⓑ "the per-bin spread is below 0.02"                  -> ** REFUTED **, 0.056634.
  Ⓒ "it is not exactly one half, by more than 0.002"    -> HOLDS, by 0.003313, BUT WEAKER THAN
    THEIR NUMBERS IMPLY: with a spread of 0.0566 the standard error of the mean is about 0.0009, so
    the departure is three to four of those where their range would make it twenty.
  Ⓓ "the factor is in all three, EE within 0.02 of TT"  -> HOLDS for EE at 0.0061; the TE half is
    REFUTED at 0.119, for the reason registered in advance -- TE changes sign three times inside
    the instrument's reach, so its ratio runs from -2.85 to 10.59 and its mean is an artefact.
    TE is therefore declared UNUSABLE rather than quoted as a third number.

** THE PINS ARE VERIFIED FAILABLE BY PERTURBATION, NOT ASSUMED TO BE. **  Each banked figure was
moved in turn and the arms that read it watched to redden, then restored from git:
  * scaling the banked TT mean by 1.02 reddens FIVE arms -- Ⓓ⑧ (0.503313 -> 0.513379), Ⓓ⑨'s
    agreement with 60, Ⓖ⑭'s TT-EE closeness, Ⓘ⑯'s departure from one half and Ⓘ⑰'s strength;
  * scaling the banked EE mean by 1.05 reddens Ⓖ⑬ (0.497180 -> 0.522039) and Ⓖ⑭;
  * widening the TT spread by 20 per cent reddens Ⓔ⑩ (0.056634 -> 0.067961) and Ⓔ⑪'s ratio;
  * setting the slope to 1e-3 per bin reddens Ⓔ⑫, so "not a slope" is a test and not a remark.
Each was applied to the banked comparison in place, the run watched, and the file restored from a
copy; the four runs reddened 5, 2, 2 and 1 arms and NOTHING ELSE.

⌗ AND THE FIRST ATTEMPT AT THIS VERIFICATION SILENTLY TESTED ONLY ONE OF THE FOUR, which is worth
recording because the output LOOKED like three passes.  The restore step used `git checkout` on the
banked comparison, and the committed copy PREDATED a field this receipt reads, so after the first
restore every later run died on a KeyError before any arm executed -- printing no failures at all.
Three perturbations were therefore never applied, and an empty result is NOT a passing result.
Caught by reading the trailing restored-baseline line, which showed the traceback rather than
`0 FAILED`.  ⇒ GUARD: a verification loop must restore the state it perturbed, not the state a
version-control checkout happens to hold, and its own baseline must be re-read at the end.

COMPUTES: nothing of the physics another seat owns.  It re-reads THIS revision's own regenerated
          bank point and its banked comparison, and recomputes from them: the per-block mean, range
          and spread of the bank-to-CAMB ratio, the slope in bin index, the TT-EE closeness, and
          the comparison against the figures 60 report.  The binning is the harness's OWN
          score_ttteee._bin_one, so bins and windows are not reimplemented.

Bound: this receipt pins THIS check's figures.  It does NOT say WHICH of the bank and CAMB is
right -- a ratio names a discrepancy without attributing it -- and it does NOT locate the line,
which 69 has ruled is 60's to find.  A factor near one half is CONSISTENT with the cancellation 60
describe against the baryon fault's factor two in the lensing power, but this check does not test
that cancellation and does not claim to.  It pins no cosmological parameter as a result.
"""
import json
import os
import sys

import numpy as np

FAILED = []
RAN = []


def check(label, ok, detail=''):
    RAN.append(label)
    print(('  [ok]   ' if ok else '  [FAIL] ') + label + (('   ' + detail) if detail else ''))
    if not ok:
        FAILED.append(label)


HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
BTW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
MINE = os.path.join(BTW, 'r7855_cc66_an_independent_check_of_the_factor_two_in_the_cmb_bank')
R42 = os.path.join(BTW, 'r7842_60_polarisation_added_to_the_score_and_the_two_data_the_harness_'
                        'does_not_have')

with open(os.path.join(MINE, 'compare_bank_vs_camb.json'), encoding='utf-8') as fh:
    C = json.load(fh)
BLK = {b['block']: b for b in C['blocks']}
Z = np.load(os.path.join(MINE, 'bank', 'lcdm_S000.npz'), allow_pickle=True)
CFG = json.loads(str(Z['config']))
SIXTY = C['sixty_reports']

print(__doc__.strip().splitlines()[1])
print()

# ------------------------------------------- Ⓐ the bank is this revision's own regenerated point
check('Ⓐ① the bank point is REGENERATED by the instrument, not read from a cache -- its own config '
      'names the instrument and its blob',
      CFG['instrument'] == 'ACOUSTIC_two_arm.py' and len(CFG['instrument_blob']) == 40
      and CFG['ARM'] == 'lcdm',
      'blob %s, ARM %s, LMAXL %s' % (CFG['instrument_blob'][:12], CFG['ARM'], CFG['LMAXL']))

check('Ⓐ② and the cache the order pointed at is ABSENT, which is why it was regenerated',
      not os.path.isdir('/tmp/claude-0/pol_grid'),
      'POL_DIR default /tmp/claude-0/pol_grid does not exist')

check('Ⓐ③ what IS committed beside model3 carries only RATIOS, so the absolute normalisation the '
      'factor lives in is not in the repository at all',
      set(np.load(os.path.join(R42, 'ratio_grid3.npz'), allow_pickle=True).keys())
      >= {'ratio_tt', 'ratio_ee', 'dte_over_tt'},
      'ratio_grid3.npz holds ratio_tt, ratio_ee, dte_over_tt')

check('Ⓐ④ the bank spans the instrument\'s own ell reach on its own stride',
      len(Z['ls']) == 238 and int(Z['ls'][0]) == 100 and int(Z['ls'][-1]) == 1996,
      '%d ells, %d..%d' % (len(Z['ls']), Z['ls'][0], Z['ls'][-1]))

# ------------------------------------------------------- Ⓑ the binning is the harness's own
check('Ⓑ⑤ every block bins to 185 common bins -- THE SAME COUNT 60 REPORT, so the windows agree',
      all(BLK[k]['n_bins'] == 185 for k in ('TT', 'TE', 'EE')) and SIXTY['n_bins'] == 185,
      'TT %d, TE %d, EE %d; 60 report %d' % (BLK['TT']['n_bins'], BLK['TE']['n_bins'],
                                             BLK['EE']['n_bins'], SIXTY['n_bins']))

# ----------------------------------------------------------- Ⓒ the conversion, stated and checked
check('Ⓒ⑥ the conversion is the DERIVED one and is recorded in the banked comparison, not left '
      'implicit',
      'A_s * (3/5)^2' in C['conversion'] and abs(C['conversion_constant']
                                                 - 2.1e-9 * 0.36 * 2.7255e6 ** 2) < 1e-6,
      'constant %.6f' % C['conversion_constant'])

check('Ⓒ⑦ and A_s * (3/5)^2 is 7.56e-10, against the 7.58e-10 the T_CMB-only ratio implied, so the '
      'convention is identified to better than half a per cent',
      abs(2.1e-9 * 0.36 / 7.58e-10 - 1.0) < 0.005,
      '7.56e-10 against 7.58e-10, %.3f per cent apart'
      % (100 * abs(2.1e-9 * 0.36 / 7.58e-10 - 1.0)))

# ------------------------------------------------------------------ Ⓓ/Ⓔ item ①: the factor
tt = BLK['TT']
check('Ⓓ⑧ the factor REPRODUCES: the bank\'s binned TT is 0.5033 of CAMB\'s',
      abs(tt['abs_mean'] - 0.5033) < 0.0002,
      'mean %.6f  (pinned 0.5033 +/- 0.0002)' % tt['abs_mean'])

check('Ⓓ⑨ and that is 60\'s 0.504672 to 0.27 per cent, independently',
      abs(100 * abs(tt['abs_mean'] / SIXTY['factor'] - 1.0) - 0.27) < 0.04,
      'agreement %.4f per cent' % (100 * abs(tt['abs_mean'] / SIXTY['factor'] - 1.0)))

check('Ⓔ⑩ ⛔ BUT THE SPREAD IS 0.0566, so the factor is NOT flat to the precision reported',
      abs(tt['abs_spread'] - 0.0566) < 0.00004,
      'spread %.6f  (pinned 0.0566 +/- 0.00004)' % tt['abs_spread'])

_their = SIXTY['hi'] - SIXTY['lo']
check('Ⓔ⑪ which is 5.4 times the 0.0105 range they report -- this REFUTES this seat\'s own band Ⓑ',
      abs(_their - 0.0105) < 0.00005 and abs(tt['abs_spread'] / _their - 5.4) < 0.04,
      'theirs %.6f, ratio %.3f  (pinned 5.4 +/- 0.04)' % (_their, tt['abs_spread'] / _their))

check('Ⓔ⑫ and the departure is NOT a slope: under 1e-5 per bin, so it is oscillatory structure',
      abs(tt['abs_slope_per_bin']) < 1e-5,
      'slope %.3e per bin' % tt['abs_slope_per_bin'])

# -------------------------------------------------------------- Ⓖ/Ⓗ item ②: TT alone or all
ee, te = BLK['EE'], BLK['TE']
check('Ⓖ⑬ item ②: EE carries the SAME factor, 0.4972, so it is not confined to TT',
      abs(ee['abs_mean'] - 0.4972) < 0.0002,
      'EE mean %.6f  (pinned 0.4972 +/- 0.0002)' % ee['abs_mean'])

check('Ⓖ⑭ and TT and EE agree to 0.0061, so ONE mis-normalisation sits upstream of both',
      abs(abs(tt['abs_mean'] - ee['abs_mean']) - 0.0061) < 0.00004,
      '|TT - EE| = %.6f  (pinned 0.0061 +/- 0.00004)' % abs(tt['abs_mean'] - ee['abs_mean']))

check('Ⓗ⑮ TE is UNUSABLE and is declared so rather than quoted: its ratio spans negative to above '
      'ten, because TE changes sign inside the instrument\'s reach',
      te['abs_min'] < 0.0 < te['abs_max'] and te['abs_max'] > 10.0 and te['abs_spread'] > 10.0,
      'TE ratio %.3f to %.3f, spread %.3f' % (te['abs_min'], te['abs_max'], te['abs_spread']))

# ------------------------------------------ Ⓘ not exactly one half, and how strongly that is known
dep = tt['abs_mean'] - 0.5
sem = (tt['abs_spread'] / 4.0) / np.sqrt(tt['n_bins'])          # range/4 as a crude sd, over sqrt N
check('Ⓘ⑯ it is NOT exactly one half: the mean departs by 0.0033',
      abs(dep - 0.0033) < 0.00004, 'departure %.6f  (pinned 0.0033 +/- 0.00004)' % dep)

check('Ⓘ⑰ ⚠ but that is only three to four standard errors of the mean, where their much tighter '
      'range would have made it twenty -- so the claim is WEAKER than their numbers imply',
      2.0 < dep / sem < 6.0 and dep / (_their / 4.0 / np.sqrt(185)) > 15.0,
      'mine %.1f sigma, theirs would be %.1f' % (dep / sem,
                                                 dep / (_their / 4.0 / np.sqrt(185))))

check('Ⓙ⑱ the count is COUNTED off the arms that ran and then pinned, not typed',
      len(RAN) == 17, 'arms before this one: %d (pinned 17)' % len(RAN))

print()
print('  %d arms, %d FAILED' % (len(RAN), len(FAILED)))
if FAILED:
    print('  FAILED: ' + '; '.join(FAILED))
sys.exit(1 if FAILED else 0)
