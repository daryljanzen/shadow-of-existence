# -*- coding: utf-8 -*-
"""⛭⛭⛭ THE UNREADABLE MINIMISED LIMIT WAS THE PROFILER MIXING TWO BASINS -- NOT THE REPAIRED
BACKGROUND AND NOT THE N_eff RULING -- AND THE CORRECTED CONTROL CONFIRMS THE LANDED FIGURES TO
WITHIN A QUARTER OF A meV.

COMPUTES: both limits on the bank re-solved at the CORRECTED N_eff offset, with the precondition
read off all thirty-two of that bank's own recorded configs and the lensing plumbing measured in
the run against the superseded grid rather than labelled; the top of the minimised profile
separated into the grid's edge, a convergence failure, the bank's own top point, or an unseparated
verdict, over three independent start sets; the second basin that separation found, carried from
its own solution to every node of the axis; both limits again on the resulting one-basin envelope;
and the reference's relabelled column re-read with the cache keyed on what its value depends on.
** IT PINS AS RESULTS: the calibrated limit `185.92` meV at the corrected offset and its `+0.23`
move from the superseded reading; the corrected `rd_camb` move `-0.26` meV and its factor `2.106`
against the other ruler; and the five nodes the lower basin reaches with the depth at each. **
⛔ ** AND IT PINS TWO ABSENCES AS THE ABSENCES THEY ARE: ** the minimised limit is NOT READABLE as
the raw profiler reads this bank -- the same absence `r7866` reported -- and the `300.98` meV the
one-basin envelope gives is NOT PINNED AS A LIMIT, because it is a lower envelope of what has been
found and not a proved global minimum.  *An arm that pinned it as a limit would be asserting more
than this revision measured.*

⌷ ** THE ID. **  `69` ordered this as `r7869`, which merged `r7866`, applied this line's census
routing, routed `cc66`'s cache defect, and ruled the separating grid.

⚠ ** THE HEADLINE CONTRADICTS THIS SEAT'S OWN TWO PREVIOUS REVISIONS, AND FIVE THINGS IN THE RECORD
ARE THIS SEAT'S OWN -- THE FIRST OF THEM AN OVERREACH IN THIS REVISION'S OWN EDGE TEST, WHOSE
CORRECTION IS WHAT FOUND THE BASIN AT ALL. **

    NODE=60 python3 <this file>

Written r7870 (60).  Stated for reversal.
"""
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
D = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                 'r7870_60_the_separating_grid_the_corrected_control_and_the_cache_that_'
                 'relabelled_a_column')
D66 = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                   'r7866_60_the_low_end_lean_located_and_the_bank_re_solved_on_the_repaired_'
                   'background')
FAILS = []
NARMS = 0


def load(name, d=None):
    with io.open(os.path.join(d or D, name), encoding='utf-8') as fh:
        return json.load(fh)


def text(name, d=None):
    with io.open(os.path.join(d or D, name), encoding='utf-8') as fh:
        return fh.read()


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

LIM = load('limits_corrected.json')
TOP = load('top_node.json')
BAS = load('second_basin.json')
ONE = load('one_basin.json')
SB = load('same_bins.json', D66)
SEP = load('limits_separating.json')
ECO = load('envelope_closed_nufd_only.json')
ECD = load('envelope_closed_nufd_dneff044.json')
RESULT = text('RESULT.md')
PRED = text('PREDICTION.md')

# ── Ⓐ ① the corrected control ──────────────────────────────────────────────────────────────────
_pre = LIM['precondition']
check('Ⓐ①ᵃ ** THE BANK AT THE CORRECTED OFFSET IS WHAT IT SAYS IT IS, read off ALL THIRTY-TWO of '
      'its own recorded configs rather than a sample or a directory name: thirty-two CMB points, '
      'sixteen control and sixteen arm of record, sixteen lensing points on each arm, the offset '
      'key present everywhere, the CORRECTED offset on every control point and NONE on any '
      'arm-of-record point. **  ⇒ *the arm of record carries no offset under either figure, which '
      'is why its points could be carried across byte-identically rather than re-solved*',
      _pre['cmb_points'] == 32 and _pre['lcdm_points'] == 16 and _pre['cr_points'] == 16
      and _pre['lensing_points_lcdm'] == 16 and _pre['lensing_points_cr'] == 16
      and _pre['dneff_key_present'] is True
      and _pre['dneff_corrected_on_control_only'] is True
      and _pre['holds'] is True,
      '%d points, control-only offset %s' % (_pre['cmb_points'],
                                             _pre['dneff_corrected_on_control_only']))

check('Ⓐ①ᵃᵃ ⛭ and the repair reads ON at every nonzero sum and OFF at the zero-sum node, which is '
      'the TRUTHFUL record and not a gap: the switch is conditioned on a nonzero sum, and at zero '
      'mass the two backgrounds are the same program to the bit',
      _pre['nufd_true_at_every_nonzero_sum'] is True
      and _pre['nufd_false_at_zero_sum'] is True)

_pl = LIM['plumbing']
check('Ⓐ①ᵇ ⛔ ** THE PLUMBING IS MEASURED IN THE RUN, NOT LABELLED: the model holds the corrected '
      'lensing grid, and the corrected bandpowers differ from the superseded ones by a measured '
      'amount at the same sum. **  ⇒ *`r7866` spent a whole thirty-two-point grid on a '
      'disagreement between what a re-point changed and what the totals showed, so a run that '
      'cannot show it read the grid it claims is not evidence about that grid*',
      _pl['pp_grid_is_the_corrected_one'] is True
      and _pl['pp_grid'].endswith('nufd_dneff044')
      and _pl['pol_dir'].endswith('nufd_dneff044')
      and _pl['max_rel_change_vs_superseded_grid'] > 1e-4,
      'max relative change %.3e' % _pl['max_rel_change_vs_superseded_grid'])

_adj = LIM['adjudication']
_mini = LIM['profiles']['minimised']
check('Ⓐ①ᶜ ⛔ ** THE MINIMISED LIMIT IS NOT READABLE AT THE CORRECTED OFFSET EITHER, and the arm '
      'was registered as a comparison whose NEGATIVE was that landed state. **  The profile rises '
      'from its minimum to the second-highest node and then FALLS at the top one.  ⇒ *** unreadable '
      'at BOTH figures of the offset, so the N_eff ruling is RULED OUT as its cause -- and this is '
      'pinned as the absence it is, not as a number ***',
      _mini['limit_meV'] is None and _mini['monotonic_above_min'] is False
      and _adj['minimised_readable_at_corrected_offset'] is False
      and len(LIM['top_node']['minimised_dips']) == 1
      and abs(LIM['top_node']['minimised_dips'][0][0] - 0.60) < 1e-9,
      'NOT READABLE, dip at %.3f eV' % LIM['top_node']['minimised_dips'][0][0])

_cal = LIM['profiles']['calibrated']
check('Ⓐ①ᵈ ** THE CALIBRATED LIMIT IS `185.92` meV AND MOVED `+0.23` FROM THE SUPERSEDED READING, '
      'inside the registered band of ten. **  ⇒ *So the whole corrected re-solve confirms `r7866`\'s '
      'figures to within a quarter of a meV, which is the useful content of order `r7867`\'s '
      'correction: the control\'s spectra are weakly sensitive to an offset this small, exactly as '
      'registered*',
      _cal['limit_meV'] is not None
      and abs(_cal['limit_meV'] - 185.92) < 0.005
      and abs(_adj['calibrated_move_meV'] - 0.23) < 0.005
      and _adj['band_holds'] is True,
      '%.2f meV, moved %+.2f' % (_cal['limit_meV'], _adj['calibrated_move_meV']))

# ── Ⓒ ③ the top node ───────────────────────────────────────────────────────────────────────────
check('Ⓒ③ᵃ THE TOP OF THE PROFILE IS REPORTED BEFORE ANY LIMIT IS READ THROUGH IT, as the order '
      'requires, and the minimised profile\'s only dip is AT the top node while the calibrated '
      'profile has NONE  ⇒ *the asymmetry between the two is itself a reading: whatever is '
      'happening is not in the bank, which both columns share*',
      LIM['top_node']['minimised_dip_at_top_node'] is True
      and LIM['top_node']['calibrated_dips'] == []
      and abs(LIM['top_node']['top_node_eV'] - 0.60) < 1e-9)

_bank = TOP['bank']
check('Ⓒ③ᵇ ⛔ ** THE GRID\'S EDGE IS RULED OUT, AND ON TWO GROUNDS NEITHER OF WHICH INVOLVES A FIT: '
      'the bank is SMOOTH across the whole sum axis -- no sign change in the step of its summed '
      '`TT` -- and the top node is a BANK NODE, where a cubic spline returns that knot\'s own '
      'value, so the model there IS the banked spectra and not an extrapolation. **',
      _bank['sign_changes_eV'] == [] and len(_bank['rows']) == 8
      and abs(_bank['rows'][-1][0] - 0.60) < 1e-9,
      '0 sign change(s) over %d banked sums' % len(_bank['rows']))

_ss = TOP['start_sets']
check('Ⓒ③ᶜ ⛭⛭ ** WHAT THE SEPARATION FOUND INSTEAD: three INDEPENDENT start sets agree to `0.0000` '
      'at nine of eleven nodes and to EXACTLY ZERO across the crossing region, and disagree by '
      '`12.5367` at one node. **  ⇒ *** A profile whose independent start sets disagree is NOT '
      'CONVERGED, and nothing about what the dip IS follows from it -- which is why the verdict is '
      'allowed to come back unseparated rather than naming a cause ***',
      abs(_ss['worst_spread'] - 12.5367) < 0.001
      and abs(_ss['worst_spread_at_eV'] - 0.40) < 1e-9
      and _ss['crossing_region_worst_spread'] == 0.0
      and _ss['profile_is_converged'] is False
      and TOP['dip_survives_convergence'] is None,
      'worst %.4f at %.3f eV; crossing region %.1e'
      % (_ss['worst_spread'], _ss['worst_spread_at_eV'], _ss['crossing_region_worst_spread']))

check('Ⓒ③ᵈ ⌗ and the DISTANCE between the dip and the crossing it suppresses is measured and '
      'REPORTED rather than acted on: the discipline refuses a limit on a non-monotonicity about '
      'three times higher in the sum than the crossing.  ⇒ *Whether that rule should be narrowed '
      'to a neighbourhood of the crossing is the RULE\'S own question, and narrowing it would also '
      'have hidden this basin -- so the measurement is routed and the ruling is not made here*',
      TOP['dip_over_crossing'] is not None and 2.5 < TOP['dip_over_crossing'] < 3.5,
      '%.2fx' % TOP['dip_over_crossing'])

# ── Ⓔ the second basin, and what it does to the profile ────────────────────────────────────────
_reach = sorted(float(k) for k in BAS['carried']
                if BAS['carried'][k] < BAS['agreed'][k] - 1e-4)
check('Ⓔ⓹ᵃ ⛔⛭⛭ ** THE SECOND BASIN IS NOT ONE NODE\'S: carried from its own solution it reaches '
      'FIVE nodes, going DEEPER at every one, and gives nothing further at the top node. **  ⇒ '
      '*** SO THE TOP NODE WAS ALREADY IN THE LOWER BASIN WHILE THE NODE BELOW IT WAS IN THE '
      'HIGHER ONE, AND THE DIP THE DISCIPLINE REFUSED A LIMIT ON *WAS* THE BASIN SWITCH ***',
      #: ⛭ r7870: the five nodes are pinned ONE BY ONE as well as as a set.  The set equality
      #:   already says the same thing, but `check_figures_pinned` reads COMPARISONS on figures
      #:   and a list equality is not one -- and it was right to flag it: the INDEX row prints
      #:   these five figures beside this receipt, so each one has to fail this arm on its own.
      #:   *The repair is to spell the pin per figure, not to print fewer digits.*
      _reach == [0.2, 0.25, 0.3, 0.4, 0.5]
      and abs(_reach[0] - 0.200) < 5e-4 and abs(_reach[1] - 0.250) < 5e-4
      and abs(_reach[2] - 0.300) < 5e-4 and abs(_reach[3] - 0.400) < 5e-4
      and abs(_reach[4] - 0.500) < 5e-4
      and abs(BAS['at_0400']['gap'] - 12.5367) < 0.001,
      'reaches %s' % ', '.join('%.3f' % v for v in _reach))

_depths = [BAS['agreed'][k] - BAS['carried'][k]
           for k in ('0.2', '0.25', '0.3', '0.4', '0.5')]
check('Ⓔ⓹ᵃᵃ and the depth GROWS monotonically with the sum across those five nodes, which is what '
      'a single basin diverging from another looks like rather than five unrelated local minima',
      all(_depths[i + 1] > _depths[i] for i in range(len(_depths) - 1)),
      'depths %s' % ', '.join('%.2f' % v for v in _depths))

check('Ⓔ⓹ᵇ ** TAKING THE LOWER OF THE TWO AT EVERY NODE, THE PROFILE IS MONOTONIC ABOVE ITS '
      'MINIMUM AND THERE IS NO DIP TO REFUSE A LIMIT ON. **',
      BAS['best_of_both']['monotonic_above_min'] is True
      and BAS['best_of_both']['dips'] == []
      and abs(BAS['best_of_both']['min_at'] - 0.06) < 1e-9)

_o = ONE['adjudication']
check('Ⓔ⓹ᶜ ⛭ ** AND THE CALIBRATED LIMIT IS IDENTICAL TO THE DIGIT WITH AND WITHOUT BASIN SEEDING, '
      'which is the control this finding needed: the lower basin NEVER REACHES the calibrated '
      'surface, so only the minimised profile was ever basin-mixed. **',
      _o['limit_calibrated'] is not None
      and abs(_o['limit_calibrated'] - _o['item1_calibrated_mixed_basins']) < 0.005,
      '%.2f both ways' % _o['limit_calibrated'])

check('Ⓔ⓹ᵈ ⛔ ** THE ENVELOPE\'S MINIMISED CROSSING IS READABLE AND IS **NOT PINNED AS A LIMIT**, '
      'because it is a LOWER ENVELOPE of what has been found and not a proved global minimum: a '
      'third basin deeper still would move it and nothing in this revision rules one out. **  ⇒ '
      '*What this arm asserts is that the run SAYS SO about itself -- the flag is set in its own '
      'output -- and that the record never offers the number as a limit*',
      ONE['minimised']['limit_meV'] is not None
      and ONE['minimised']['monotonic_above_min'] is True
      and _o['is_a_lower_envelope_not_a_proved_global_minimum'] is True
      and 'lower envelope' in RESULT and 'not a proved global minimum' in RESULT
      and 'not offered as one anywhere in this record' in RESULT,
      'readable at %.2f, declared an envelope' % ONE['minimised']['limit_meV'])

check('Ⓔ⓹ᵉ and the two basins differ almost entirely in ONE of the four parameters at the same '
      'tau, which is the shape that makes the physical question worth routing rather than '
      'answering here',
      abs(BAS['at_0400']['x_lower'][4] - BAS['at_0400']['x_higher'][4]) < 1e-6
      and abs(BAS['at_0400']['x_lower'][0] - BAS['at_0400']['x_higher'][0]) > 1.0,
      'first parameter differs by %.3f at equal tau'
      % abs(BAS['at_0400']['x_lower'][0] - BAS['at_0400']['x_higher'][0]))

# ── Ⓓ ④ the cache ──────────────────────────────────────────────────────────────────────────────
_mv = SB['moves_meV']
check('Ⓓ④ᵃ ** THE CACHE IS KEYED ON WHAT ITS VALUE DEPENDS ON NOW, AND THE TWO REFERENCE MODES ARE '
      'DISTINCT COLUMNS: their totals are no longer bit-identical on either bin set. **  ⇒ *the '
      'defect was a cache built once outside the mode loop and keyed on the sum alone, so the '
      'first mode to run populated it and the second was served the first mode\'s spectra*',
      SB['reference_rd_min_whole']['totals'] != SB['reference_rd_camb_whole']['totals']
      and SB['reference_rd_min_minus36']['totals'] != SB['reference_rd_camb_minus36']['totals']
      and SB['reference_rd_min_whole']['params'] != SB['reference_rd_camb_whole']['params'])

check('Ⓓ④ᵇ ⛭ ** THE RELABELLED COLUMN WAS HIDING A REAL DIFFERENCE: the corrected move is `-0.26` '
      'meV against the voided `-0.12`, a factor of `2.106`, and that ruler\'s own crossing was '
      'misreported as well.  ⇒ THE REFERENCE CARRIES TWO RULERS AT THE LOW END AND THEY DIFFER BY '
      'A FACTOR OF TWO. **',
      abs(_mv['reference_rd_camb'] - (-0.26)) < 0.005
      and abs(_mv['reference_rd_camb'] / _mv['reference_rd_min'] - 2.106) < 0.001,
      '%+.4f against %+.4f, ratio %.3f'
      % (_mv['reference_rd_camb'], _mv['reference_rd_min'],
         _mv['reference_rd_camb'] / _mv['reference_rd_min']))

check('Ⓓ④ᶜ ** AND THE HEADLINE IS UNTOUCHED IN EVERY DIGIT, which is a fact about the CODE PATH '
      'and not a hope: both ratios divide by the move of the mode that POPULATED the cache, so '
      'that mode was always served its own spectra. **  `162.28` frozen and `389.42` re-profiled, '
      'unchanged',
      abs(SB['ratio_on_the_same_bins_frozen'] - 162.28) < 0.005
      and abs(SB['ratio_on_the_same_bins'] - 389.42) < 0.005
      and abs(_mv['reference_rd_min'] - (-0.1238)) < 0.0005)

_second = abs(_mv['instrument_frozen'] / _mv['reference_rd_camb'])
check('Ⓓ④ᵈ ⇒ ** SO THE LEAN HAS A SECOND DENOMINATOR AND IS A RANGE RATHER THAN ONE NUMBER: about '
      '`77`-fold frozen against the other ruler, where it is `162` against the first.  THE '
      'CONCLUSION SURVIVES THE WORSE DENOMINATOR -- two orders of magnitude either way. **',
      70.0 < _second < 85.0
      and abs(_second - 77.07) < 0.5,
      '%.2f-fold on the other ruler' % _second)

# ── Ⓑ ② the separating grid ────────────────────────────────────────────────────────────────────
_sp = SEP['precondition']
check('Ⓑ②ᵃ ** THE SEPARATING RUNG IS THE ONE THE ORDER NAMED, read off ALL THIRTY-TWO of its own '
      'recorded configs: thirty-two CMB points and sixteen lensing points on each arm, the offset '
      'key present everywhere and reading NONE on EITHER arm, the repair on at every nonzero sum '
      'and off at the zero-sum node. **  ⇒ *nothing is carried on this rung -- both arms are '
      'solved here, unlike the offset rungs where the arm of record was copied across*',
      _sp['cmb_points'] == 32 and _sp['lcdm_points'] == 16 and _sp['cr_points'] == 16
      and _sp['lensing_points_lcdm'] == 16 and _sp['lensing_points_cr'] == 16
      and _sp['dneff_key_present'] is True
      and _sp['no_offset_on_either_arm'] is True
      and _sp['nufd_true_at_every_nonzero_sum'] is True
      and _sp['nufd_false_at_zero_sum'] is True
      and _sp['holds'] is True,
      'no offset on either arm: %s' % _sp['no_offset_on_either_arm'])

_rungs = {r['rung']: r for r in SEP['rungs']}
_cal = sorted(r['calibrated_meV'] for r in SEP['rungs'] if 'no repair' not in r['rung'])
check('Ⓑ②ᵈ ⛭⛭ ** THE CALIBRATED COLUMN DECOMPOSES WITH NO AMBIGUITY: `81.94` meV on the landed '
      'bank against `185.96`, `185.69` and `185.92` on the three REPAIRED rungs, which agree to a '
      'third of a meV however the offset is set.  ⇒ THE REPAIR CARRIES THE WHOLE MOVE AND THE '
      'OFFSET IS WORTH ABOUT A THIRD OF A meV. **  ⇒ *this is the part of the order\'s four-rung '
      'question the profiler trouble does not touch*',
      abs(_cal[-1] - _cal[0]) < 0.40
      and all(180.0 < v < 190.0 for v in _cal)
      and abs(_rungs['the landed bank: no repair, no offset']['calibrated_meV'] - 81.94) < 0.005
      and len(_cal) == 3,
      'three repaired rungs span %.2f meV, against 81.94 on the landed bank'
      % abs(_cal[-1] - _cal[0]))

check('Ⓑ②ᵇ⓵ THE RAW READING DIPS ON THIS RUNG TOO, at the top node, so the profiler reports no '
      'limit on a bank that carries NO offset at all  ⇒ *which is already enough to rule the '
      'repaired background out as the cause, the same way item ① ruled out the ruling by '
      'reproducing the dip at both figures of the offset*',
      SEP['raw_minimised']['limit_meV'] is None
      and SEP['raw_minimised']['monotonic_above_min'] is False
      and abs(SEP['raw_minimised']['dips'][-1][0] - 0.600) < 5e-4,
      'raw dips at %.3f eV' % SEP['raw_minimised']['dips'][-1][0])

check('Ⓑ②ᵇ⓶ ⛔⛭⛭ ** AND ON THE OFFSET RUNG THE CLOSED ENVELOPE IS MONOTONIC WITH NO DIPS AT ALL: '
      'closure removes EVERY non-monotonicity there, so the unreadability on that rung was '
      'ENTIRELY the profile sitting in mixed basins. **  ⇒ *** the order\'s fork named the '
      'repaired background and the N_eff ruling as its two branches, and the answer is NEITHER ***',
      ECD['minimised']['monotonic_above_min'] is True
      and ECD['minimised']['dips'] == []
      and ECD['minimised']['crossing_meV'] is not None,
      'monotonic, crossing %.2f meV' % ECD['minimised']['crossing_meV'])

check('Ⓑ②ᵇ⓷ ⛭ AND TWO SEPARATELY WRITTEN METHODS AGREE ON THAT RUNG\'S CROSSING TO EVERY DIGIT -- '
      'the one-basin envelope and the cross-seeded closed envelope  ⇒ *an independent '
      'confirmation, not a repetition: the two files seed differently and converge differently*',
      abs(ECD['minimised']['crossing_meV'] - ONE['minimised']['crossing_meV']) < 0.005,
      '%.2f by both' % ECD['minimised']['crossing_meV'])

check('Ⓑ②ᵉ ⚠ ** AND WHAT SURVIVES ON THE NO-OFFSET RUNG IS REPORTED AS THE RESIDUAL IT IS, NOT '
      'NAMED: closure removes the top-node dip there too -- the big one -- and leaves a dip two '
      'orders of magnitude smaller at a lower node, which SURVIVES cross-seeding. **  ⇒ *this arm '
      'exists because a verdict of this seat\'s explained that residual as seed luck and the '
      'closed envelope refuted it; cross-seeding cannot find a basin no node entered, so the rung '
      'is UNSEPARATED and says so*',
      ECO['minimised']['monotonic_above_min'] is False
      and len(ECO['minimised']['dips']) == 1
      and abs(ECO['minimised']['dips'][0][0] - 0.200) < 5e-4
      and abs(ECO['minimised']['dips'][0][1] - (-0.0206)) < 5e-4
      and abs(SEP['raw_minimised']['dips'][-1][1]) > 50.0 * abs(ECO['minimised']['dips'][0][1]),
      'residual %+.4f at %.3f eV against the raw %+.4f'
      % (ECO['minimised']['dips'][0][1], ECO['minimised']['dips'][0][0],
         SEP['raw_minimised']['dips'][-1][1]))

check('Ⓑ②ᶠ ⛔ AND NO ENVELOPE CROSSING IS PINNED AS A LIMIT ANYWHERE, on either rung: each is a '
      'lower envelope over the basins REACHED, and the record says so of both  ⇒ *the same '
      'discipline the one-basin crossing is under, applied to item ②*',
      SEP['fork']['envelope_is_not_a_limit'] is True
      and 'envelope crossings over the basins REACHED' in RESULT
      and 'does not offer either as a limit' in RESULT)

# ── Ⓕ the scope, and what this revision got wrong ──────────────────────────────────────────────
check('Ⓕ① THE REGISTRATION WAS COMMITTED AND PUSHED BEFORE ANY COMPUTATION OF THIS REVISION '
      'EXISTED, and it registered the fork\'s decider BOTH WAYS before the grid was run so the '
      'branch could not be chosen after the fact',
      'Committed and pushed before any computation of this revision exists' in PRED
      and "THE FORK'S DECIDER, registered both ways before it is run" in PRED,
      'the registration states both')

check('Ⓕ② ⚠ ** FIVE THINGS IN THIS RECORD ARE THIS SEAT\'S OWN, and the FIRST is an overreach in '
      'this revision\'s own edge test: its first verdict claimed a feature of the model while its '
      'own output held two start sets differing by twelve units of chi2 at one node.  CORRECTING '
      'THAT IS WHAT FOUND THE BASIN. **  ⇒ *the others are a batch limit passed wrong, an import '
      'that died on a path side effect, the envelope caveat, and a SECOND verdict of this '
      'seat\'s own that its follow-up measurement refuted*',
      'FIVE THINGS IN THIS RECORD ARE THIS SEAT' in RESULT
      and 'overreach' in RESULT
      and 'batch limit passed wrong' in RESULT
      #: ⛭ r7870: a FIFTH item was added when the closed envelope refuted this revision's own
      #:   explanation of the residual dip, and this arm pins that it is there -- because the
      #:   pattern across the two is the useful part: the verdicts that FAILED were the ones that
      #:   named a cause, and the ones that held named what was ruled OUT.
      and 'seed luck, not a feature' in RESULT
      and 'the verdicts that failed were the ones that named a cause' in RESULT)

check('Ⓕ③ AND THE SCOPE IS DECLARED: this revision does NOT rule on whether the lower basin is '
      'physical, does NOT narrow the convergence discipline, and does NOT reconcile the tension '
      'with the earlier revision that reported a second basin not surviving the repair -- each is '
      'named in the record as routed or unsettled rather than left for a reader to infer',
      'not established' in RESULT and 'belongs to whoever owns the rule' in RESULT)

print('')
print('=' * 100)
if FAILS:
    print('  ⛔ %d CHECK(S) FAILED:' % len(FAILS))
    for f in FAILS:
        print('     - %s' % f[:140])
    print('=' * 100)
    sys.exit(1)
print('  OK  %d of %d arms' % (NARMS, NARMS))
print('=' * 100)
sys.exit(0)
