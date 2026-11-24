# -*- coding: utf-8 -*-
"""⛭⛭⛭ THE ORDER'S FORTY-FOLD WAS A RATIO BETWEEN TWO DIFFERENT REMOVALS.  ON THE SAME BINS THE
INSTRUMENT'S LIMIT LEANS ON ITS LOWEST BANDPOWERS A HUNDRED AND SIXTY-TWO TIMES HARDER THAN THE
REFERENCE'S, AND THE BANK RE-SOLVED ON THE REPAIRED BACKGROUND GIVES NO READABLE MINIMISED LIMIT.

COMPUTES: the thirty-six bandpowers this line's matched-count low cut removes, named by block and
multipole and checked against the landed cut's own record; the reference's forty-nine by its own
rule; the two sets compared as sets; the per-bandpower sum-derivative of chi2_cmb for the
instrument in closed form and for the reference on identical bins; the move the SAME thirty-six
cause in each column with the parameters treated the same way, and the asymmetry control for it;
the high-end control; the order's three named candidates each tested so it can come back NO; and
both limits re-read on a bank re-solved at thirty-two CMB and thirty-two lensing points with the
ruling's DNEFF on the control only.
** IT PINS AS RESULTS: the ratio `162` on identical bins and `389` with this line's own parameters
re-profiled, the moves `-20.09` and `-0.12` meV they come from, the high-end control's `+1.52`,
the calibrated limit `185.69` meV on the re-solved bank, and the share `33` per cent of the move
the solved amplitude carries. ** The minimised limit is NOT a figure: it is NOT READABLE on the
re-solved bank, and that is pinned as the absence it is.

⌷ ** THE ID. **  `69` ordered this as `r7865`, which merged `r7864`, applied all four of this
line's routed patches, and named the low end as the lead.

⚠ ** FOUR THINGS IN THIS RECORD ARE THIS SEAT'S OWN, AND ONE OF THEM IS A DIAGNOSIS THIS SEAT MADE
MID-REVISION AND THEN REFUTED BY THE MEASUREMENT IT PROVOKED.  TWO REGISTERED CRITERIA FAIL AND TWO
REGISTERED EXPECTATIONS ARE REFUTED, ALL FOUR WITH THEIR CRITERIA UNMOVED. **

    NODE=60 python3 <this file>

Written r7866 (60).  Stated for reversal.
"""
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
D = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                 'r7866_60_the_low_end_lean_located_and_the_bank_re_solved_on_the_repaired_'
                 'background')
FAILS = []
NARMS = 0


def load(name):
    with io.open(os.path.join(D, name), encoding='utf-8') as fh:
        return json.load(fh)


def check(name, ok, got=None):
    global NARMS
    NARMS += 1
    if ok:
        print('  [PASS] %s' % name + ('   (%s)' % got if got is not None else ''))
    else:
        FAILS.append(name)
        print('  [FAIL] %s' % name + ('   (got %s)' % got if got is not None else ''))


print(__doc__)
print('=' * 100)

LB = load('low_bins.json')
LN = load('lean.json')
SB = load('same_bins.json')
LR = load('limits_resolved.json')
CA = load('candidates.json')
RESULT = ' '.join(io.open(os.path.join(D, 'RESULT.md'), encoding='utf-8').read().split())
PRED = ' '.join(io.open(os.path.join(D, 'PREDICTION.md'), encoding='utf-8').read().split())

# ── Ⓐ① THE THIRTY-SIX, AND THE TWO LOW ENDS AS SETS ─────────────────────────────────────────────
check('Ⓐ①ᵃ THE THIRTY-SIX ARE NAMED AND THE NAMING IS CHECKED AGAINST THE LANDED CUT ITSELF: '
      'twelve lowest-BIN_LO bandpowers of EACH block, every one between multipoles 100 and 207, '
      'because that is where this instrument\'s score begins.  ⌗ The check is against '
      '`tail_control.narrow_low`\'s own three figures and not against a re-derivation of them',
      LB['instrument']['total'] == 36 and LB['instrument']['n_per_block'] == 12
      and LB['instrument']['agrees_with_landed'] is True
      and LB['instrument']['landed']['dropped'] == 36
      and LB['instrument']['bins_after'] == 519
      and LB['instrument']['ell_lo_after'] == 208
      and all(LB['instrument']['per_block'][b]['n'] == 12
              and LB['instrument']['per_block'][b]['ell_lo'] == 100
              and LB['instrument']['per_block'][b]['ell_hi'] == 207
              for b in ('TT', 'TE', 'EE')),
      '36 bins, 12 per block, ell 100..207, agreeing with the landed record')

check('Ⓐ①ᵇ ⛔ THE REGISTERED EXPECTATION THAT THE REFERENCE\'S FORTY-NINE COME FROM FEWER THAN '
      'THREE BLOCKS IS **REFUTED**: they come from all three, split seventeen/sixteen/sixteen.  '
      '** And the rule is reproduced before the sets are compared -- 49 of 613 leaving 564, which '
      'is cc66\'s own recorded count to the integer. **',
      LB['reference']['n_cut'] == 49 and LB['reference']['n_covered'] == 613
      and LB['reference']['reproduces_cc66_record'] is True
      and LB['reference']['n_blocks'] == 3
      and LB['reference']['per_block']['TT']['n'] == 17
      and LB['reference']['per_block']['TE']['n'] == 16
      and LB['reference']['per_block']['EE']['n'] == 16
      and LB['sets']['expectation_three_blocks_refuted'] is True
      and 'is REFUTED' in RESULT,
      'refuted: three blocks, 17/16/16')

check('Ⓐ①ᶜ ** AND THE SETS DIFFER FOR A STRONGER REASON: THEY SHARE SEVEN BINS OF THIRTY-SIX AND '
      'FORTY-NINE. **  Forty-two of the reference\'s forty-nine are bins this instrument does not '
      'cover at all, below the multipole its score starts at, and only seven of the forty-nine '
      'are bins it has.  ⇒ *So the reference\'s low cut leaves standing almost exactly the band '
      'this line\'s removes, and the order\'s forty-fold was never a comparison on one set*',
      LB['sets']['n_in_both'] == 7
      and LB['sets']['n_only_instrument'] == 29
      and LB['sets']['n_only_reference'] == 42
      and LB['sets']['reference_bins_the_instrument_covers'] == 7
      and LB['uncovered']['n'] == 58 and LB['uncovered']['n_below_100'] == 42,
      '7 shared, 29 this line\'s only, 42 the reference\'s only, 58 uncovered of which 42 below 100')

# ── Ⓑ② THE LEAN ────────────────────────────────────────────────────────────────────────────────
check('Ⓑ②ᵃ THE DECOMPOSITION IS EXACT AND NOT DIFFERENCED: the binned model is a spline in the '
      'sum and the amplitude is solved, so the gradient in the amplitude vanishes and the '
      'per-bandpower numbers sum to the whole-spectrum derivative BY CONSTRUCTION.  The relative '
      'gap is exactly zero against the 1e-6 the registration set.  ⌗ *The same quantity '
      'differenced at the banked spacing is more than four times it, so a difference-based '
      'decomposition would have been measuring the step*',
      LN['instrument']['holds'] is True and LN['instrument']['rel_gap'] == 0.0
      and abs(LN['instrument']['total'] - 8.913384436) < 5e-6
      and abs(LN['instrument']['fd_step'] - 39.58226) < 2e-3
      and abs(LN['instrument']['fd_half'] - 24.05570) < 2e-3,
      'relative gap 0.0; analytic %.5f against %.3f differenced'
      % (LN['instrument']['total'], LN['instrument']['fd_step']))

check('Ⓑ②ᵇ THE REFERENCE IS REBUILT WITH cc66\'s OWN CONSTRUCTION AND REPRODUCES ITS OWN BANKED '
      '`chi2_cmb` TO 1.3e-08 AND 1.6e-08 RELATIVE, against the 1.3e-02 the registration allowed.  '
      '⚠ The registered wording asked it to reproduce cc66\'s banked `dchi2`, which is a '
      'five-parameter PROFILE difference where this is a frozen-parameter derivative -- two '
      'different objects, and this seat\'s own defect in the registration.  It is reported rather '
      'than repaired by moving the criterion',
      LN['reference']['rd_min']['within'] is True
      and LN['reference']['rd_camb']['within'] is True
      and LN['reference']['rd_min']['rel'] < 1.3e-8
      and LN['reference']['rd_camb']['rel'] < 1.7e-8
      and LN['reference']['rd_min']['n_covered'] == 613
      and 'two different objects' in RESULT,
      'reproduced to %.2e and %.2e' % (LN['reference']['rd_min']['rel'],
                                       LN['reference']['rd_camb']['rel']))

check('Ⓑ②ᶜ ⛔ THE REGISTERED EXPECTATION THAT THE TWO PIPELINES DIFFER MOST BELOW MULTIPOLE 300 IN '
      'TE OR EE IS **REFUTED ON BOTH CLOCKS**: they differ most in TT between 1001 and 1500, with '
      'OPPOSITE SIGNS there.  ** And the clock is this seat\'s own caught defect: the first cut '
      'compared an exact derivative against a finite difference, which is not the same quantity, '
      'so the comparison was re-taken with both columns on ONE clock. **  ⇒ *The refutation '
      'survives the change of clock, which is what makes it content and not an artefact*',
      LN['reference']['rd_min']['worst_band'] == 'TT 1001-1500'
      and LN['reference']['rd_camb']['worst_band'] == 'TT 1001-1500'
      and LN['reference']['rd_min']['expectation_met'] is False
      and LN['reference']['rd_camb']['expectation_met'] is False
      and abs(LN['reference']['rd_min']['worst_diff'] - 63.65019) < 5e-4
      and LN['instrument_same_clock']['banded']['TT 1001-1500'] > 0
      and LN['reference']['rd_min']['banded']['TT 1001-1500'] < 0
      and 'on BOTH clocks' in RESULT,
      'TT 1001-1500 by %+.5f, signs %+.2f against %+.2f'
      % (LN['reference']['rd_min']['worst_diff'],
         LN['instrument_same_clock']['banded']['TT 1001-1500'],
         LN['reference']['rd_min']['banded']['TT 1001-1500']))

_mv = SB['moves_meV']
check('Ⓑ②ᵈ ** THE COMPARABLE NUMBER, ON THE SAME THIRTY-SIX BINS: THE INSTRUMENT MOVES 162 TIMES '
      'THE REFERENCE ON THE REFERENCE\'S OWN TREATMENT OF THE PARAMETERS, AND 389 WITH ITS OWN '
      'FOUR RE-PROFILED. **  -20.09 meV against -0.12 frozen, -48.20 against -0.12 profiled.  ⇒ '
      '*The order\'s forty-fold was a ratio between two removals sharing seven bins; this is the '
      'one taken on one set*',
      abs(_mv['instrument_frozen'] - (-20.09)) < 0.005
      and abs(_mv['reference_rd_min'] - (-0.12)) < 0.005
      and abs(_mv['reference_rd_camb'] - (-0.12)) < 0.005
      and abs(_mv['instrument'] - (-48.20)) < 0.005
      and abs(SB['ratio_on_the_same_bins_frozen'] - 162.28) < 0.005
      and abs(SB['ratio_on_the_same_bins'] - 389.42) < 0.005
      and SB['instrument_whole']['nbins'] == 555
      and SB['instrument_minus36']['nbins'] == 519
      and SB['reference_rd_min_whole']['nbins'] == 555,
      '%.0f times frozen and %.0f profiled, on 555 bins against 519'
      % (SB['ratio_on_the_same_bins_frozen'], SB['ratio_on_the_same_bins']))

check('Ⓑ②ᵈᵃ THE ASYMMETRY CONTROL WAS RUN BEFORE ANYTHING WAS READ INTO THAT RESULT, because the '
      'instrument\'s column profiles four parameters where the reference\'s holds five, and that '
      'freedom could itself have BEEN the move.  It carries 28.11 meV of it and leaves two orders '
      'of magnitude standing.  ⇒ ** so the asymmetry is NOT the cause **',
      abs(SB['freedom_share_of_the_move_meV'] - (-28.11)) < 0.01
      and abs(_mv['instrument_frozen'] / _mv['reference_rd_min']) > 100.0,
      'the freedom carries %.2f meV of the move' % SB['freedom_share_of_the_move_meV'])

check('Ⓑ②ᵉ THE HIGH-END CONTROL HOLDS, and it is the arm that keeps the whole of item ② honest: '
      'the same COUNT off the TOP of each block moves the crossing +1.52 meV against the low '
      'end\'s -20.09.  ⇒ *The method is not measuring the count.*  ⛔ Had both ends moved it '
      'alike, ② would have been reported as NOT LOCATED',
      CA['high_end_control']['holds'] is True
      and abs(CA['high_end_control']['move_high'] - 1.52) < 0.005
      and abs(CA['high_end_control']['move_low'] - (-20.09)) < 0.005
      and abs(CA['high_end_control']['whole'] - 57.08) < 0.005,
      'high end %+.2f against low end %+.2f'
      % (CA['high_end_control']['move_high'], CA['high_end_control']['move_low']))

check('Ⓑ②ᵈ⓵ THE TAU-PRIOR CANDIDATE COMES BACK **NO, STRUCTURALLY**: the function whose crossing '
      'moved carries no `tau` at all.  `tau` enters the joint score through the lensing half, and '
      'the lensing half does not reach this crossing -- which is MEASURED and not argued, by '
      're-solving the lensing grid and finding every profile total unchanged',
      CA['tau_prior']['chi2_cmb_carries_tau'] is False
      and 'NO' in CA['tau_prior']['verdict']
      and LR['plumbing']['pp_grid_is_the_new_one'] is True
      and 'bit-identical' in RESULT,
      'no tau in the path, and the lensing grid the run holds is the re-solved one')

check('Ⓑ②ᵈ⓶ THE LATE-ISW CANDIDATE WAS ATTEMPTED AND IS **UNREADABLE ON THIS MASK**, reported as '
      'neither confirmed nor refuted: there are thirteen TT bandpowers below the first peak and '
      'no crossing is readable on them.  ⇒ *That is a fact about the mask Ⓐ① named -- the score '
      'starts at multipole 100 -- and not a result about the ISW*',
      CA['late_isw']['n_bins'] == 13
      and CA['late_isw'].get('whole') is None
      and 'Neither confirmed nor refuted' in RESULT,
      '13 TT bins below the first peak, no crossing readable')

check('Ⓑ②ᵈ⓷ THE SHARED-NORMALISATION CANDIDATE COMES BACK **PARTLY, AND MEASURED**: with the '
      'amplitude FIXED instead of solved the move is -13.52 against -20.09, so the solved '
      'amplitude carries 33 per cent of it and 67 per cent SURVIVES it.  ⇒ *a contributor, not '
      'the mechanism*',
      abs(CA['amplitude_handover']['move'] - (-13.52)) < 0.005
      and abs(100.0 * CA['amplitude_handover']['share_of_the_move_the_amplitude_carries']
              - 33.0) < 1.0,
      'the amplitude carries %.0f per cent, %.0f per cent survives'
      % (100.0 * CA['amplitude_handover']['share_of_the_move_the_amplitude_carries'],
         100.0 * (1.0 - CA['amplitude_handover']['share_of_the_move_the_amplitude_carries'])))

# ── Ⓒ③ THE RE-SOLVED BANK ──────────────────────────────────────────────────────────────────────
_pre = LR['precondition']
check('Ⓒ③ᵃ+ᵇ THE PRECONDITION RUNS THE OTHER WAY NOW, AND IS GATED THAT WAY.  `r7864` proved the '
      'landed bank could not say which background solved it because the switch key was ABSENT; '
      'this bank carries the key at every one of thirty-two CMB points, reads TRUE at every '
      'nonzero sum and FALSE at the zero-sum node -- ** which is the TRUTHFUL record and not a '
      'gap: the repair is conditioned on a nonzero sum, so at zero mass the two backgrounds are '
      'ONE PROGRAM, which r7864 measured to the bit. **  And the ruling\'s DNEFF is on the '
      'CONTROL only, the arm of record carrying none',
      _pre['holds'] is True and _pre['cmb_points'] == 32
      and _pre['lcdm_points'] == 16 and _pre['cr_points'] == 16
      and _pre['nufd_key_present'] is True
      and _pre['nufd_true_at_every_nonzero_sum'] is True
      and _pre['nufd_false_at_zero_sum'] is True
      and _pre['dneff_on_control_only'] is True
      and _pre['lensing_bank_resolved'] is True,
      '32 CMB points, 16 and 16, the key present and the ruling split')

_adj = LR['adjudication']
check('Ⓒ③ᶜ ⛔⛭ ** BOTH LIMITS RE-READ ON THE RE-SOLVED BANK, AND THE MINIMISED ONE IS **NOT '
      'READABLE**: the profile stops being monotonic above its minimum at the top node, so '
      'r7860\'s convergence discipline reports NO limit, as it is built to. **  The calibrated one '
      'is 185.69 meV against the ordered 30.56 and r7864\'s 81.94.  Both profiles now put their '
      'minimum at a NONZERO sum.  ⇒ ** The registered expectation that the minimised limit moves '
      'TOWARDS 54.00 is REFUTED -- there is no readable limit to move -- and the registered band '
      'of 8 meV FAILS, both with their criteria unmoved **',
      _adj['limit_minimised'] is None
      and abs(_adj['limit_calibrated'] - 185.69) < 0.005
      and _adj['band_holds'] is False
      and _adj['gap_to_54'] is None
      and abs(_adj['band_meV'] - 8.0) < 1e-12
      and abs(_adj['r7864_minimised'] - 69.97) < 0.005
      and abs(_adj['r7864_calibrated'] - 81.94) < 0.005
      and 'NOT READABLE' in RESULT
      and 'FAILS, with the criterion unmoved' in RESULT,
      'minimised NOT READABLE, calibrated %.2f against 30.56' % _adj['limit_calibrated'])

check('Ⓒ③ᵈ AND WHAT THIS REVISION CANNOT SEPARATE IS SAID RATHER THAN LEFT IMPLICIT: the re-solve '
      'changed TWO things at once, the repaired background and the ruling\'s N_eff on the control. '
      'At zero sum the switch is inert, so the move there is the N_eff ruling alone -- but the '
      'sum-dependence cannot be attributed between the two from this bank, and the separating run '
      'is ROUTED rather than guessed at',
      'cannot be attributed between the two' in RESULT
      and 'separating run' in RESULT,
      'the attribution is named as unseparated and routed')

# ── Ⓓ④ THE RECORD'S OWN FOUR ────────────────────────────────────────────────────────────────────
check('Ⓓ④ THE RECORD CARRIES ITS FOUR OWN ITEMS rather than only its results: the registration '
      'that asked for an object it is not, the first cut that compared across two clocks, the '
      'prose pin that was slack by three, and -- the one that cost the most -- a DIAGNOSIS THIS '
      'SEAT MADE MID-REVISION AND THEN REFUTED BY THE MEASUREMENT IT PROVOKED.  It read a declared '
      'scope limit as load-bearing, spent a grid re-solve on it, and the re-solve changed NOTHING: '
      'every profile total bit-identical while the lensing shape the model reads differs by up to '
      '4.5 per cent.  ⇒ *The hypothesis is kept as refuted because its refutation is what rules '
      'out the first of the order\'s three candidates*',
      'FOUR THINGS IN THIS RECORD ARE THIS SEAT\'S OWN' in RESULT
      and 'REFUTED BY THE MEASUREMENT IT PROVOKED' in RESULT
      and 'slack by three' in RESULT
      and 'the hedge was never load-bearing' in RESULT,
      'four named in the result document, one of them a refuted diagnosis')

check('Ⓓ④ᵃ and the registration this is read against was committed and pushed BEFORE any '
      'computation of this revision existed, with its reads declared -- including the one that '
      'mattered, that both pipelines score against the same bandpowers while their two low cuts '
      'are built by different rules',
      'Committed and pushed before any computation of this revision exists' in PRED
      and 'DECLARED READS' in PRED
      and 'twelve per block' in PRED
      and 'forty-nine globally lowest' in PRED,
      'the registration carries its declared reads')

print('=' * 100)
if FAILS:
    print('  ⛔ %d CHECK(S) FAILED:' % len(FAILS))
    for f in FAILS:
        print('      - %s' % f)
else:
    print('  ✔ ALL %d ARM-CHECK(S) PASS.' % NARMS)
    print('    => the two low ends share seven bins of thirty-six and forty-nine, so the order\'s')
    print('       forty-fold was a ratio between two different removals.')
    print('    => on the SAME thirty-six the instrument moves 162 times the reference frozen and')
    print('       389 profiled, the high-end control holds at +1.52 against -20.09, and of the')
    print('       three named candidates one is NO structurally, one unreadable, one worth 33 per')
    print('       cent of the move.')
    print('    => and on the bank re-solved at thirty-two CMB and thirty-two lensing points the')
    print('       minimised limit is NOT READABLE and the calibrated one is 185.69 meV.')
print('=' * 100)
sys.exit(1 if FAILS else 0)
