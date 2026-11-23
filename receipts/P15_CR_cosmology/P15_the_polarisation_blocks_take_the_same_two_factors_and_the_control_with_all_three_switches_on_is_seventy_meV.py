# -*- coding: utf-8 -*-
"""⛭⛭⛭ THE POLARISATION BLOCKS TAKE THE SAME TWO FACTORS, THE DISAGREEMENT OVER THE SPREAD WAS TWO
ARRAYS AND NOT TWO READINGS, AND THE ORDERED CONTROL COMES TO `69.97` meV.

COMPUTES: the two factors wired onto the polarisation blocks at the lines where each block's own
definition lives, with their inertness and their exactness measured on three legs of one
configuration; all three blocks against an independent reference with the switch on, TE by the
cross-correlation coefficient that a shared constant cannot move; the reconciliation of this seat's
per-bin spread with the other seat's, on the same arrays; the banked grids moved out of `/tmp` and
proved readable from a stripped environment; and the ordered control with all three switches on.
** IT PINS TWO LIMITS AS RESULTS: `69.97` meV with the ruler minimised and `146.13` meV with the
ruler calibrated, both 95 per cent one-sided, against the reference's `54.00` and `30.56`.  They are
reported as a COMPARISON, as registered before the numbers existed, and both are limits THROUGH THIS
INSTRUMENT, which `Ⓑ②ᵃ` measures still carries a few-per-cent shape residual against the reference. **

⌷ ** THE ID. **  `69` ordered this as `r7857`, which merged `r7858`, ruled that the polarisation
blocks take the same two factors as TT, ruled that the provenance ratchet keeps comparing the
instrument's blob with named inert classes, asked for the spread to be reconciled on the same
arrays, told this line to get the bank out of `/tmp`, and then asked for the control.

⛭ ** WHAT IS NEW HERE, AND WHAT IS NOT. **  The two factors are `r7858`'s; the ruling that they
apply to EE and TE is `69`'s.  What this revision adds is the wiring, the measurement of all three
blocks against the reference, the reconciliation, the committed bank, and the control.

⚠ ** SIX THINGS IN THIS RECORD ARE FAILURES, CORRECTIONS OR REFUSALS, AND FIVE ARE THIS SEAT'S OWN. **
A comment this seat wrote one revision ago is FALSE and is corrected rather than replaced; the first
version of the windowed leg BINNED A RATIO and returned a meaningless number; the first run of the
control's profile was NOT CONVERGED and its limit was 15 per cent TIGHTER than the converged one; a
census of another seat's goes red BECAUSE this revision obeyed the order, and is routed rather than
edited; and the instrument's resolved config does not record the solver switch, which is reported
rather than repaired here because repairing it moves the blob; and the comparator that
settled which of this seat's three absolute statements holds the amplitude knew only one of
this corpus's two verdict-marker conventions, so one of the three was compared VACUOUSLY on
its first run.

    NODE=60 python3 <this file>

Written r7860 (60).  Stated for reversal.
"""
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
D = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                 'r7860_60_the_polarisation_blocks_wired_the_spread_reconciled_and_the_bank_'
                 'committed')
FAILS = []


def load(name):
    with io.open(os.path.join(D, name), encoding='utf-8') as fh:
        return json.load(fh)


def check(name, ok, got=None):
    if ok:
        print('  [PASS] %s' % name + ('   (%s)' % got if got is not None else ''))
    else:
        FAILS.append(name)
        print('  [FAIL] %s' % name + ('   (got %s)' % got if got is not None else ''))


print(__doc__)
print('=' * 100)

W = load('wire.json')
C3 = load('camb_three.json')
S = load('spread.json')
B = load('bank_in_repo.json')
DB = load('doubling.json')
CT = load('control.json')
PR = load('pairs.json')
AH = load('amplitude_held.json')
with io.open(os.path.join(ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py'),
             encoding='utf-8') as fh:
    INST = fh.read()

check('Ⓐ① THE POLARISATION BLOCKS ARE WIRED AT THE LINES WHERE EACH BLOCK\'S OWN DEFINITION LIVES, '
      'AND BOTH LEGS ARE MEASURED RATHER THAN ASSERTED: with the switch unset the edited instrument '
      'is BITWISE IDENTICAL to the merged head\'s on ls, Dl, Dl_EE and Dl_TE, and with it set EACH '
      'of the three blocks is multiplied by exactly two.  ** The second leg could have come back at '
      'something other than two, which would have refuted the ruling\'s premise for that block **',
      W['holds'] is True and W['off']['byte_identical'] is True
      and all(W['on'][b]['exactly_two'] for b in ('TT', 'EE', 'TE'))
      and max(W['on'][b]['worst_distance_from_two'] for b in ('TT', 'EE', 'TE')) < 1e-12
      and abs(W['on']['TE']['worst_distance_from_two'] - 5.329e-15) < 4e-18,
      'byte-identical off over %d multipoles; on, worst |ratio-2| %.3e across the three blocks'
      % (W['off']['n_multipoles'],
         max(W['on'][b]['worst_distance_from_two'] for b in ('TT', 'EE', 'TE'))))

check('Ⓐ①ᵇ AND A COMMENT THIS SEAT WROTE ONE REVISION AGO IS FALSE AND IS CORRECTED RATHER THAN '
      'QUIETLY REPLACED: it said these two blocks carry no `l(l+1)` despite their names, and the '
      'save line multiplies by it.  ** That is exactly why `r7858`\'s source-read of them was '
      'refuted by its own measurement: the `l(l+1)` was already carried and only the constant was '
      'not **',
      '_ee_te[j] = (np.sum(P * _dE ** 2) * _FP_ACC,' in INST
      and '_pt = sum(_POLS_B) * (ls * (ls + 1))[:, None] / _FP_DL' in INST,
      'both wired lines are present in the instrument, each beside the definition it carries')

check('Ⓑ②ᵃ WITH THE SWITCH ON, TT AND EE BOTH LAND WITHIN THREE PER CENT OF THE REFERENCE over the '
      'bank\'s own 238 multipoles -- TT at 1.002278 and EE at 0.991831.  ** One revision ago EE '
      'wanted a factor of 2.016 with an 18 per cent spread, which is why `r7858` refused to ship '
      'it; with both factors applied where each definition lives it is within 0.8 per cent of one **',
      C3['B2a_holds'] is True
      and abs(C3['ratios']['TT']['geometric_mean'] - 1.002278) < 5e-6
      and abs(C3['ratios']['EE']['geometric_mean'] - 0.991831) < 5e-6,
      'TT %.6f, EE %.6f over %d multipoles'
      % (C3['ratios']['TT']['geometric_mean'], C3['ratios']['EE']['geometric_mean'],
         C3['ratios']['TT']['n']))

check('Ⓑ②ᵇ AND TE IS CHECKED BY THE ONE QUANTITY A SHARED CONSTANT CANNOT MOVE, as the order '
      'directs: the cross-correlation coefficient `TE / sqrt(TT x EE)` against the reference\'s own, '
      'median absolute difference 0.0196 against a criterion of 0.05.  ** This arm could have '
      'FAILED while `Ⓐ①` passed exactly, because a correlation coefficient is blind to the constant '
      'the wiring adds -- it tests the cross spectrum\'s SHAPE, which is the one thing a factor of '
      'two cannot repair **',
      C3['B2b_holds'] is True
      and abs(C3['correlation']['median_abs_diff'] - 0.0196) < 4e-5
      and C3['correlation']['criterion'] == 0.05,
      'median %.4f, worst %.4f over %d multipoles'
      % (C3['correlation']['median_abs_diff'], C3['correlation']['worst_abs_diff'],
         C3['correlation']['n']))

check('Ⓒ③ᵃ THE TWO SEATS\' SPREADS ARE NOT TWO READINGS OF ONE ARRAY, AND THE FIRST QUESTION WAS '
      'NOT WHICH IS RIGHT BUT WHETHER THEY DESCRIBE THE SAME OBJECT: every array of this seat\'s '
      'bank point and of the other seat\'s committed regenerated one is BITWISE EQUAL, and the only '
      'config key that differs is the instrument blob.  ** Identical arrays across a moved blob is '
      'what the inert-class ratchet exists to allow, so that difference is a reading on the ratchet '
      'and not on the physics **',
      S['same_object']['same'] is True
      and S['same_object']['config_differing'] == ['instrument_blob']
      and S['same_object']['arrays']['Dl']['equal'] is True
      and S['same_object']['arrays']['Dl_EE']['equal'] is True
      and S['same_object']['arrays']['Dl_TE']['equal'] is True,
      'all %d array(s) equal; config differs only in %s'
      % (len(S['same_object']['arrays']), S['same_object']['config_differing']))

check('Ⓒ③ᵇ SO THE OTHER SEAT\'S SPREAD IS THE ONE THAT STANDS AND THIS SEAT\'S UNDERSTATED IT: the '
      'raw bank point per multipole gives a worst excursion of 0.0565 against their 0.0566, with '
      'its negative lobe where they put it; binning through the windows does NOT remove it; and '
      'this seat\'s own smaller figure is the response-bank vector against a densely binned '
      'reference, REPRODUCED here to six decimals at 1.009345 and 0.011660.  ** The question asked '
      'is whether the bank\'s factor is a CONSTANT, which is a question about the bank, so the raw '
      'point is the right array **',
      abs(S['per_multipole']['worst_rel'] - 0.0565) < 4e-5
      and abs(S['per_multipole']['worst_rel'] - 0.057) < 4.9e-4
      and S['r7858_response_bank_path']['reproduces_r7858'] is True
      and abs(S['r7858_response_bank_path']['geometric_mean'] - 1.009345) < 5e-6
      and abs(S['r7858_response_bank_path']['worst_rel'] - 0.011660) < 5e-6,
      'per multipole %.4f, through the windows %.4f, response-bank path %.6f'
      % (S['per_multipole']['worst_rel'], S['through_the_windows']['worst_rel'],
         S['r7858_response_bank_path']['worst_rel']))

check('Ⓒ③ᶜ AND THAT COMPARATOR WAS SHOWN TO FIND A DIFFERENCE THAT IS REALLY THERE BEFORE ITS '
      'VERDICT WAS BELIEVED: a known 5 per cent oscillation put through it comes back at 0.0500 and '
      'raises the scatter.  ** Written first, because `r7858`\'s census reported zero and was nearly '
      'believed **',
      S['positive_control']['holds'] is True
      and abs(S['positive_control']['recovered'] - 0.05) < 2e-2,
      'injected %.2f, recovered %.4f; rms %.4f -> %.4f'
      % (S['positive_control']['injected'], S['positive_control']['recovered'],
         S['positive_control']['rms_before'], S['positive_control']['rms_after']))

check('Ⓒ③ᵃᵃ ⚠ AND THE FIRST VERSION OF THE WINDOWED LEG BINNED A RATIO, WHICH IS WRONG, AND IT IS '
      'KEPT IN THE FILE RATHER THAN DELETED: a window average of a ratio is not the ratio of the '
      'window averages, and run that way it returned a mean of 1e-05 and a scatter of 7.78.  ** A '
      'quantity formed in the wrong order and nearly read as a result, the same shape of error as '
      '`r7858`\'s first test of the accumulation factor **',
      abs(S['through_the_windows']['geometric_mean'] - 1.004095) < 5e-5,
      'the corrected leg, with the two spectra binned separately: mean %.6f'
      % S['through_the_windows']['geometric_mean'])

check('Ⓓ④ THE BANK IS OUT OF `/tmp` AND THAT IS MEASURED RATHER THAN READ OFF A DEFAULT: a '
      'subprocess with both bank variables STRIPPED from its environment resolves both paths under '
      'the repository, finds the banked spectra and the lensing files, and SCORES.  ** And a '
      'negative control, because a loader that tolerated an empty directory would pass the positive '
      'leg while establishing nothing: pointed at an empty directory the same probe fails **',
      B['holds'] is True and B['empty_dir_fails'] is True
      and B['resolved']['pol_in_repo'] is True and B['resolved']['pp_in_repo'] is True
      and abs(B['resolved']['chi2'] - 584.4130) < 5e-4,
      '%d banked spectra and %d lensing files, chi2 %.4f, empty directory fails: %s'
      % (B['resolved']['n_pol'], B['resolved']['n_pp'], B['resolved']['chi2'],
         B['empty_dir_fails']))

check('Ⓔ⑤ᵃ WHAT THE ORDERED CONTROL NEEDS IS ESTABLISHED SWITCH BY SWITCH, AND ONLY ONE OF THE '
      'THREE IS SUBSTITUTED: the accumulation-and-save factor is exactly twice the grid at the '
      'bank\'s OWN reach, worst distance from one 3.8e-15 across all three blocks; the primordial '
      'normalisation is a constant PER POINT and the grid carries six distinct tilts, so it is '
      'generated natively rather than multiplied; and the solver switch is neither, so the grid was '
      'RE-SOLVED.  ** The substitution is stated and measured rather than made silently, which is '
      'what this seat promised in the reply the order merged **',
      DB['fourpi_doubling']['holds'] is True
      and max(DB['fourpi_doubling']['blocks'][b]['worst_abs_rel']
              for b in ('Dl', 'Dl_EE', 'Dl_TE')) < 1e-12
      and len(DB['primnorm']) == 6 and DB['bvel']['points'] == 32
      and abs(max(DB['fourpi_doubling']['blocks'][b]['worst_abs_rel']
                  for b in ('Dl', 'Dl_EE', 'Dl_TE')) - 3.775e-15) < 4e-18,
      '%d distinct tilt constants, %d points re-solved, worst doubling error %.3e'
      % (len(DB['primnorm']), DB['bvel']['points'],
         max(DB['fourpi_doubling']['blocks'][b]['worst_abs_rel']
             for b in ('Dl', 'Dl_EE', 'Dl_TE'))))

check('Ⓔ⑤ᵃᵇ AND THE CONTROL PROVES IT IS READING THE RE-SOLVED GRID BEFORE IT SCORES ANYTHING, '
      'because the instrument\'s resolved config does NOT record the solver switch: a re-solved '
      'point and a landed one differ in their own records only by the instrument blob, so the blob '
      'is asserted not to be the landed grid\'s.  ** A control that silently read the old grid would '
      'produce a number that looks like an answer **',
      CT['precondition']['holds'] is True
      and CT['precondition']['blob_is_not_landed'] is True
      and CT['precondition']['cmb_points'] == 32
      and CT['substitution']['cmb_chi2_unchanged'] is True
      and CT['substitution']['worst_halving_error'] < 1e-12,
      '%d points, blob %s, CMB chi2 unchanged by the substitution: %s, lensing halved exactly'
      % (CT['precondition']['cmb_points'], str(CT['precondition']['blob'])[:9],
         CT['substitution']['cmb_chi2_unchanged']))

check('Ⓔ⑤ᵇ ⛭⛭ THE ORDERED CONTROL, WITH ALL THREE SWITCHES ON: 69.97 meV with the ruler minimised '
      'against the reference\'s 54.00, and 146.13 meV with the ruler calibrated against its 30.56, '
      'both 95 per cent one-sided and both inside the window registered before the numbers existed. '
      '** Reported as a COMPARISON and not as a target, and the calibrated case\'s minimum sits at '
      '0.060 eV rather than at zero, so holding the ruler does not tighten this instrument the way '
      'it tightens the reference **',
      CT['ruler_minimised']['limit_meV'] is not None
      and abs(CT['ruler_minimised']['limit_meV'] - 69.97) < 3e-2
      and abs(CT['calibrated']['limit_meV'] - 146.13) < 5e-2
      and abs(CT['ruler_minimised']['reference_meV'] - 54.00) < 4e-3
      and abs(CT['calibrated']['reference_meV'] - 30.56) < 4e-3
      and CT['ruler_minimised']['in_registered_window'] is True
      and CT['calibrated']['in_registered_window'] is True
      and abs(CT['calibrated']['min_at'] - 0.06) < 1e-9,
      'ruler minimised %.2f meV (ratio %.3f), calibrated %.2f meV (ratio %.3f), calibrated minimum '
      'at %.3f eV' % (CT['ruler_minimised']['limit_meV'], CT['ruler_minimised']['ratio_to_reference'],
                      CT['calibrated']['limit_meV'], CT['calibrated']['ratio_to_reference'],
                      CT['calibrated']['min_at']))

check('Ⓔ⑤ᶜ ⚠ AND THE FIRST RUN OF THAT PROFILE WAS NOT CONVERGED, WHICH IS KEPT IN THE FILE RATHER '
      'THAN DELETED, AND IT MATTERED IN THE DIRECTION THAT COUNTS: one minimiser start per node gave '
      'a profile that went DOWN between 0.300 and 0.400 eV, and its limit was 59.62 meV against the '
      'converged 69.97 -- 15 per cent TIGHTER.  ** So an unconverged profile FLATTERS the '
      'instrument, and the monotonicity above the minimum is now CHECKED rather than assumed on both '
      'profiles **',
      CT['ruler_minimised']['monotonic_above_min'] is True
      and CT['calibrated']['monotonic_above_min'] is True
      and not CT['ruler_minimised']['dips'] and not CT['calibrated']['dips']
      and abs(CT['unconverged']['limit_meV'] - 59.62) < 3e-2
      and abs(CT['unconverged']['tighter_by_per_cent'] - 14.8) < 4e-2
      and abs(CT['unconverged']['dips_at'][0] - 0.400) < 4e-4,
      'both profiles monotonic above their minima; the unconverged profile dips at %.3f eV and its '
      'limit is %.2f meV, %.1f per cent tighter'
      % (CT['unconverged']['dips_at'][0], CT['unconverged']['limit_meV'],
         CT['unconverged']['tighter_by_per_cent']))

check('Ⓕ⑥ AND TWO THINGS ARE ROUTED RATHER THAN DONE HERE, each because doing it belongs to another '
      'seat or costs something only `69` should spend: a census arm of another seat\'s goes red '
      'BECAUSE this revision obeyed the order\'s own ruling about the bank, with its patch measured; '
      'and the instrument\'s resolved config records neither the solver switch nor the two this '
      'line added, so adding a key would move the blob and red the two hash receipts again.  ** The '
      'bank sits where the census can SEE it: moving data out of a census\'s reach to keep the '
      'census green is the defect and not the repair **',
      DB['bvel']['committed_blob'] is not None
      and DB['bvel']['note'] == 'a solver change: no constant stands in for it',
      'both routed with their measurements attached')

check('Ⓖ⑦ AND THE SWITCH REACHES THE BILINEAR PAIRS TOO, WHICH IS NOT THIS SEAT\'S FINDING: '
      '`cc66` read the source at `r7859` and saw that the decomposition is accumulated BESIDE the '
      'TT sum, so it never saw the accumulation factor, and that its save wrote the pairs without '
      'the `D_l` factor the `D_l` beside them carries.  ** Un-repaired with the switch on, the ten '
      'pairs sum to 0.500000 of that `D_l` and the instrument\'s own closure print reads 9.2e-01 '
      'while still printing a number -- both reproduced here rather than taken on trust ** ⇒ and '
      'repaired, the two move together to the last bit and the closure is unmoved',
      PR['holds'] is True and PR['off']['byte_identical'] is True
      and PR['on']['dl_worst'] < 1e-12 and PR['on']['pairs_worst'] < 1e-12
      and abs(PR['unrepaired_pairs_over_dl'] - 0.5) < 1e-6
      and PR['closure']['tree_on'] < 1e-6 and PR['closure']['base_on'] > 0.1,
      'un-repaired the pairs are %.6f of the D_l and the closure reads %.3e; repaired the closure '
      'is %.3e and both blocks move by two to %.3e'
      % (PR['unrepaired_pairs_over_dl'], PR['closure']['base_on'], PR['closure']['tree_on'],
         max(PR['on']['dl_worst'], PR['on']['pairs_worst'])))

check('Ⓗ⑧ AND NONE OF THIS SEAT\'S THREE ABSOLUTE STATEMENTS ACTUALLY HOLDS THE AMPLITUDE, '
      'MEASURED THE WAY `cc66` MEASURED THEIRS: the committed grid is doubled -- what the switch '
      'does -- and each of the three is run against both banks.  ** All three come back with their '
      'exit code, their verdict pattern AND their whole output byte-identical, so the fit solves '
      'for the amplitude in every one ** ⇒ so `r7858`\'s sweep was WRONG to call them absolute, on '
      'the ground `r7859` names: "nothing fitted" in this sector means no cosmological parameter '
      'fitted, not the amplitude held, and the sweep\'s phrase-matching was too wide',
      AH['n_holding'] == 0 and len(AH['receipts']) == 3
      and all(v['normal']['n_marks'] > 0 for v in AH['receipts'].values())
      and all(not v['verdict_moves'] for v in AH['receipts'].values()),
      '%d of %d hold the amplitude; verdict marks parsed per receipt: %s'
      % (AH['n_holding'], len(AH['receipts']),
         ', '.join(str(v['normal']['n_marks']) for v in sorted(AH['receipts'].values(),
                                                               key=lambda x: -x['normal']['n_marks']))))

check('Ⓗ⑧ᵃ ⚠ AND THAT COMPARATOR\'S FIRST VERSION KNEW ONLY ONE OF THIS CORPUS\'S TWO MARKER '
      'CONVENTIONS, so one of the three came back with ZERO verdict marks parsed and its '
      'comparison was VACUOUS while reporting `UNMOVED`.  ** Both conventions are read now, the '
      'whole output is hashed beside them so that `unmoved` means the run did not differ AT ALL, '
      'and the comparator ASSERTS it parsed at least one mark rather than trusting that it did **',
      all(v['normal']['n_marks'] >= 16 for v in AH['receipts'].values())
      and all(v['normal']['stdout_sha'] == v['doubled']['stdout_sha']
              for v in AH['receipts'].values()),
      'the quietest of the three now parses %d marks, and all three outputs are byte-identical '
      'across the doubling'
      % min(v['normal']['n_marks'] for v in AH['receipts'].values()))

print()
print('=' * 100)
print()
if not FAILS:
    print('  ✔ r7860: the polarisation blocks take the same two factors, and the control is 69.97 meV.')
    print('    => wired at each block\'s own definition, byte-identical off and exactly two on, on '
          'all three blocks.')
    print('    => TT %.6f and EE %.6f against the reference, TE by the correlation coefficient at a '
          'median %.4f.'
          % (C3['ratios']['TT']['geometric_mean'], C3['ratios']['EE']['geometric_mean'],
             C3['correlation']['median_abs_diff']))
    print('    => one bank point, bitwise: the other seat\'s spread stands and this seat\'s was a '
          'different array, reproduced to six decimals.')
    print('    => the bank reads from the repository with the environment stripped, and an empty '
          'directory fails as it must.')
    print('    => the control: %.2f meV ruler-minimised and %.2f meV calibrated, against %.2f and '
          '%.2f.' % (CT['ruler_minimised']['limit_meV'], CT['calibrated']['limit_meV'],
                     CT['ruler_minimised']['reference_meV'], CT['calibrated']['reference_meV']))
    print('    => and the unconverged profile would have reported 59.62, which is TIGHTER: the '
          'failure flattered the instrument.')
else:
    print('  ⛔ FAIL  %d of %d arms' % (len(FAILS), len(FAILS) + 0))
print()
sys.exit(1 if FAILS else 0)
