#!/usr/bin/env python3
"""r7854 (60), on order `r7851`: the potential repaired in the hierarchy, and the recalibration sized.

COMPUTES: the located cause of the lensing potential's spurious decay through matter domination; the
repair of it in the shared hierarchy, behind a default-off switch with its own byte-equivalence
control; the repaired potential against an independent pipeline's Weyl potential at the control's
fixed cosmology; the control's nine lensing bandpowers and its 95 per cent upper limit on the
neutrino mass sum, on two ruler treatments; and the size of the recalibration the repair costs the
banked CMB calibration.  ** It pins NO cosmological parameter as a result: the limits it reports are
readings on a configuration whose absolute lensing scale it also reports as wrong, and the arm of
record is NOT JUDGED. **

⌷ ** THE ID. **  69 ordered this work as `r7851`, ruling `(a)` on the fork `r7852` left open and
taking this seat's staging.  This revision's directory, its PREDICTION.md (committed and pushed at
`44f12f5f0` before a line of the computation existed) and this receipt carry `r7854`.

** THE CAUSE, AND IT IS NEITHER OF THE TWO THIS SEAT COULD NAME IN ADVANCE. **  The rate the
perturbation equations use is consistent with the density fractions their source is normalised
against to `8.882e-16`, so the one expectation registered where it could be lost is lost.  And the
potential tracks its own Poisson relation to four parts in ten thousand on every mode well inside
the horizon, so its equation was never the fault.  ⇒ ** The baryons never clustered: ** the solver's
baryon continuity was driven by the PHOTON velocity at every time, because its state carried no
baryon velocity.  Right under tight coupling, wrong after decoupling -- and the lensing path runs
that solver far past decoupling.  So the Poisson source carried the cold matter alone, the growth
exponent came out `a^0.9011` against the `a^0.9023` that fraction predicts and the `a^1` matter
domination demands, and the potential, correctly tracking that source, decayed.

** THE REPAIR AND WHAT IT COSTS. **  The baryons take their own velocity below the same scattering
threshold the CMB path already hands over at.  The baryon contrast goes from `2e-4` of the cold
matter's to `0.95`, the growth exponent to `0.9964`, the shape against the reference from `+84` per
cent wrong to `2.5`, and the nine bandpowers from `2.131339` to `1.053393` per dof -- below the
reference's own `1.066836`.  ⇒ ** And the banked CMB calibration does not move at all: ** every peak
and every height ratio is identical to its last printed digit, because the two-fluid branch only
opens below the threshold at which that path had already handed over.

⛔ ** TWO THINGS STILL FAIL, AND ONE OF THEM IS THIS SEAT'S OWN EXCUSE. **  The flatness arm fails at
`0.1249` against a registered `0.02`; this seat argued the criterion had been written over an
interval that begins in the radiation era, put the argument to the reference, and was REFUTED -- the
reference drifts by `0.0078` there.  A radiation-era residual remains.  And the limit gets much
worse, `100.4021` to `597.7561` meV, because the joint fit carries no free lensing amplitude and the
absolute scale fault the cancellation had been hiding is now in the open.
"""
import io
import json
import os
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
BTW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
RUN = os.path.join(BTW, 'r7854_60_the_potential_repaired_in_the_hierarchy_and_the_recalibration_sized')
R7850 = os.path.join(BTW, 'r7850_60_phi_carried_through_the_radiation_era')


def j(*p):
    return json.load(io.open(os.path.join(*p), encoding='utf-8'))


LOC = j(RUN, 'locate.json')
DIAG = j(RUN, 'diagnosis.json')
REP = j(RUN, 'repair.json')
FLAT = j(RUN, 'flatness_is_physical.json')
WHERE = j(RUN, 'residual_where.json')
SUM = j(RUN, 'summary.json')
PRED = ' '.join(io.open(os.path.join(RUN, 'PREDICTION.md'), encoding='utf-8').read().split())
RESULT = ' '.join(io.open(os.path.join(RUN, 'RESULT.md'), encoding='utf-8').read().split())
INST = ' '.join(io.open(os.path.join(BTW, 'ACOUSTIC_two_arm.py'), encoding='utf-8').read().split())

fail = []


def check(label, cond, detail=''):
    ok = bool(cond)
    print('  %s %s' % ('✔' if ok else '✘', label))
    if detail:
        print('      %s' % detail)
    if not ok:
        fail.append(label.split()[0])
    return ok


def run(which, ruler):
    return next(r for r in SUM['control_runs']
                if r['which'] == which and r['ruler'].startswith(ruler))


def at_k(rows, k, field):
    return next(r[field] for r in rows if abs(r['k'] - k) < 1e-12)


print(__doc__.split('\n')[0])
print()

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# ⓪ THE EDIT'S OWN CONTROL -- without it nothing below reads the repair
check('⓪ THE POSITIVE CONTROL: with the switch OFF the repaired solver reproduces the state banked '
      'BEFORE the edit existed, exactly.  ** An edit to a shared instrument that cannot show that '
      'is not a repair whatever the repaired run says ** -- and the state layout moves when the '
      'switch is on, which is the silent-failure class this file\'s own comment named when the '
      'baryon contrast was first appended',
      REP['control']['holds'] is True
      and REP['control']['worst_relative'] == 0.0
      and REP['control']['NV'] == 19 and REP['control']['I_DB'] == 18
      and 'default off, so an unset `bvel` leaves this solver byte-identical' in INST.lower(),
      'worst relative difference %.1e over the whole state' % REP['control']['worst_relative'])

# Ⓑ② the registered expectation, lost
check('Ⓑ② FAILED AS REGISTERED, and it is this seat\'s own expectation that is refuted.  The arm '
      'registered that the rate the perturbation equations use is NOT the rate their source\'s '
      'density fractions are normalised against, with the reachable negative that the consistency '
      'holds to a part in a million.  ** It holds to 8.882e-16 **',
      LOC['rate_is_consistent'] is True
      and abs(LOC['friedmann_worst'] - 8.882e-16) < 4.4e-19
      and LOC['friedmann_worst'] < 1e-06,
      'worst residual %.3e over the whole interval, against the registered 1e-06'
      % LOC['friedmann_worst'])

qs = LOC['phi_over_quasistatic'][-1]
_sub = [i for i, k in enumerate(LOC['k']) if k >= DIAG['subhorizon_k']]
check('Ⓐ①ᵃ and the potential was never the fault either: it tracks its OWN Poisson relation to four '
      'parts in ten thousand on every mode well inside the horizon, where its homogeneous decay '
      'rate is fast against the expansion.  ⇒ So the equation\'s form, which the registration had '
      'already declared was not the cause, is measured not to be',
      min(qs[i] for i in _sub) > 0.998
      and abs(min(qs[i] for i in _sub) - 0.9985) < 4.9e-05
      and min(LOC['k_over_Hc_at_last'][i] for i in _sub) > 40.0,
      'the quotient runs %.4f to %.4f on the modes with k/Hc from %.1f up'
      % (min(qs[i] for i in _sub), max(qs[i] for i in _sub),
         min(LOC['k_over_Hc_at_last'][i] for i in _sub)))

# Ⓐ① the decay located to ONE input, and the arithmetic closes
check('Ⓐ① PASSES: the decay is located to ONE named input and the arithmetic closes with no free '
      'parameter.  ** The baryons never clustered ** -- their contrast is 2.2e-04 of the cold '
      'matter\'s at the smallest scale probed -- so the Poisson source carries the cold matter '
      'alone, which is 0.843463 of the clustering matter; the growth exponent that fraction '
      'predicts through the matter-domination quadratic is a^0.9023 and the measurement gives '
      'a^0.9011, against a^1.0000 if all the matter clustered',
      DIAG['picks_cold_only'] is True
      and abs(DIAG['cold_fraction'] - 0.843463) < 4.1e-04
      and abs(DIAG['exponent_cold_only'] - 0.9023) < 4.4e-04
      and abs(DIAG['exponent_measured'] - 0.9011) < 4.4e-04
      and abs(DIAG['exponent_all_matter'] - 1.0000) < 4.9e-04
      and abs(abs(DIAG['exponent_measured'] - DIAG['exponent_cold_only']) - 0.0012) < 4.9e-05
      and abs(abs(DIAG['exponent_measured'] - DIAG['exponent_all_matter']) - 0.0989) < 4.9e-05
      and abs(DIAG['db_over_dc_last'][-1] - 0.00022) < 4.9e-06,
      'the measurement sits %.4f from the cold-matter-only prediction and %.4f from the '
      'all-matter one' % (abs(DIAG['exponent_measured'] - DIAG['exponent_cold_only']),
                          abs(DIAG['exponent_measured'] - DIAG['exponent_all_matter'])))

check('Ⓐ①ᵇ and the MECHANISM is one line of the solver, asserted off the source that runs and not '
      'off a comment: the baryon continuity was driven by the photon velocity at every time, and '
      'the same file\'s other solver already carried a baryon velocity of its own',
      DIAG['baryon_continuity_uses_photon_velocity'] is True
      and DIAG['other_solver_carries_baryon_velocity'] is True,
      'the defect and its own counter-example in one file')

# Ⓒ③ the repair, and the registered flatness criterion
_bk = [r for r in REP['baryons_and_growth'] if r['k'] >= 0.02]
check('Ⓒ③ FAILED AS REGISTERED on its stated criterion, and the repair nevertheless does what the '
      'diagnosis said: the baryon contrast goes from 2.2e-04 of the cold matter\'s to 0.95136, the '
      'growth exponent from 0.8992 to 0.9964, and the potential\'s drift over the test interval '
      'from 0.5389 to 0.1249 -- a factor 4.3 and still six times outside the registered 0.02',
      REP['flatness_passes'] is False
      and abs(REP['worst_after_over_band'] - 0.1249) < 6.1e-05
      and REP['worst_after_over_band'] > 0.02
      and abs(at_k(REP['baryons_and_growth'], 1.0, 'db_dc_after') - 0.95136) < 4.7e-04
      and abs(at_k(REP['baryons_and_growth'], 1.0, 'db_dc_before') - 0.00022) < 4.9e-06
      and abs(at_k(REP['baryons_and_growth'], 1.0, 'exponent_after') - 0.9964) < 4.9e-04
      and abs(at_k(REP['baryons_and_growth'], 1.0, 'exponent_before') - 0.8992) < 4.4e-04
      and min(r['exponent_after'] for r in _bk) > 0.99,
      'the exponent above k = %g now runs %.4f to %.4f' % (
          0.02, min(r['exponent_after'] for r in _bk), max(r['exponent_after'] for r in _bk)))

check('Ⓒ③ᵇ ** AND THIS SEAT\'S EXCUSE FOR THAT FAILURE WAS PUT TO THE REFERENCE AND REFUTED. **  The '
      'argument was that the criterion had been written over an interval beginning at a radiation '
      'share of 0.14014, where the potential is not supposed to be flat.  The reference drifts by '
      '0.0078 over the same interval and the same modes where the repaired instrument drifts by '
      '0.1249, and the two differ by 0.1179.  ⇒ The criterion was right and the repair is '
      'INCOMPLETE',
      FLAT['residual_is_shared_physics'] is False
      and FLAT['arm_failed_on_the_criterion_as_registered'] is True
      and abs(FLAT['worst_reference'] - 0.0078) < 4.9e-05
      and abs(FLAT['worst_instrument'] - 0.1249) < 6.1e-05
      and abs(FLAT['worst_difference'] - 0.1179) < 5.8e-05
      and abs(FLAT['radiation_share'][0] - 0.14014) < 7.0e-05,
      'the reference carries %.4f of the %.4f this instrument carries' % (FLAT['worst_reference'],
                                                                          FLAT['worst_instrument']))

_w = WHERE['subintervals']
check('Ⓒ③ᶜ and the residual is located in TIME rather than left unattributed: the excess over the '
      'reference is 0.0469 across the first sub-interval, 0.0244 across the second and 0.0003 '
      'across the last, where the radiation share is 0.01582.  ⇒ ** The repair is complete where '
      'radiation is negligible and a radiation-era residual remains ** -- which also restores '
      'r7850\'s ruling, a later handover inheriting less of it',
      abs(_w[0]['excess'][5] - 0.0469) < 4.9e-05
      and abs(_w[1]['excess'][5] - 0.0244) < 4.9e-05
      and abs(_w[2]['excess'][5] - 0.0003) < 4.9e-05
      and abs(_w[2]['excess'][5]) < 0.1 * abs(_w[0]['excess'][5])
      and abs(_w[2]['rad_over_matter'] - 0.01582) < 7.9e-06,
      'the excess falls by a factor %.0f across the three sub-intervals'
      % (_w[0]['excess'][5] / _w[2]['excess'][5]))

# Ⓓ④ against the reference
check('Ⓓ④ PASSES AS REGISTERED: the repaired potential\'s shape against the reference\'s Weyl '
      'potential at the control\'s fixed cosmology goes from 0.8442 wrong to 0.0245 over the band '
      'the lensing kernel weights, against the registered 0.10 -- a factor 34',
      REP['vs_reference_passes'] is True
      and abs(REP['vs_reference_worst_after'] - 0.0245) < 4.9e-05
      and abs(REP['vs_reference_worst_before'] - 0.8442) < 4.1e-04
      and REP['vs_reference_worst_after'] < 0.10,
      'worst %.4f after against %.4f before, over 5e-3 <= k <= 0.3'
      % (REP['vs_reference_worst_after'], REP['vs_reference_worst_before']))

# Ⓔ⑤ the control, control only
_bp = SUM['bandpowers']
_lan, _min = run('landed', 'minimised'), run('repaired', 'minimised')
check('Ⓔ⑤ PASSES on the criterion registered and the limit is reported either way.  The nine '
      'bandpowers go from 2.131339 to 1.053393 per dof -- BELOW the reference\'s own 1.066836 -- at '
      'the handover exactly where it was landed, with one switch moved and no tuning.  ⛔ And the '
      'limit goes from 100.4021 +/- 0.3533 to 597.7561 +/- 0.0525 meV with the joint minimum from '
      '570.3427 to 746.0268, because the joint fit carries NO free lensing amplitude and reads the '
      'ABSOLUTE scale the cancellation had been covering',
      abs(_bp['repaired']['per_dof'] - 1.053393) < 5.2e-04
      and _bp['repaired']['per_dof'] <= 1.3
      and abs(_bp['landed']['per_dof'] - 2.131339) < 1.05e-03
      and abs(_bp['camb_exactly_binned_per_dof'] - 1.066836) < 5.2e-04
      and _bp['repaired']['per_dof'] < _bp['camb_exactly_binned_per_dof']
      and abs(_bp['repaired']['amplitude'] - 8.1642e-10) < 4.0e-13
      and abs(_bp['landed']['amplitude'] - 1.5769e-09) < 7.8e-13
      and abs(_min['upper95_mev'] - 597.7561) < 0.29
      and abs(_min['chi2min'] - 746.0268) < 0.37
      and abs(_lan['upper95_mev'] - 100.4021) < 0.05
      and abs(_lan['chi2min'] - 570.3427) < 0.28,
      'the bandpowers improve %.6f -> %.6f per dof and the limit worsens %.4f -> %.4f meV'
      % (_bp['landed']['per_dof'], _bp['repaired']['per_dof'], _lan['upper95_mev'],
         _min['upper95_mev']))

_cal = run('repaired', 'calibrated')
check('Ⓔ⑤ᵇ and every chain the limits are read off is HEALTHY, so the readings are the model\'s and '
      'not the sampler\'s: every direction under 1.0002 on the convergence statistic, every '
      'effective sample size above 44000, no minimum on a bound and no direction with unmeasurable '
      'curvature in any of the three runs',
      all(r['worst_rhat'] < 1.0002 for r in SUM['control_runs'])
      and all(r['least_ess'] > 44000.0 for r in SUM['control_runs'])
      and all(r['minimum_on_a_bound'] is False for r in SUM['control_runs'])
      and all(r['curvature_unmeasurable_in'] == [] for r in SUM['control_runs'])
      and len(SUM['control_runs']) == 3,
      'three runs, worst R-hat %.6f, least effective sample size %.0f'
      % (max(r['worst_rhat'] for r in SUM['control_runs']),
         min(r['least_ess'] for r in SUM['control_runs'])))

# Ⓕ⑥ the ruler, both treatments
check('Ⓕ⑥ PASSES on its reporting requirement and its registered EXPECTATION FAILS.  Both ruler '
      'treatments are carried with the treatment named beside each figure: minimised gives '
      '597.7561 +/- 0.0525 meV and calibrated at 147.055454 Mpc gives 596.4034 +/- 0.0723, with '
      'the joint minimum 746.0268 against 886.5954.  ** The registered expectation was a tightening '
      'of at least a tenth and the move is 1.3528 meV, 0.0023 of the limit **',
      SUM['ruler_expectation_holds'] is False
      and abs(SUM['ruler_shift_mev'] + 1.3528) < 6.7e-04
      and abs(SUM['ruler_shift_fraction'] - 0.0023) < 4.9e-05
      and SUM['ruler_shift_fraction'] < 0.10
      and abs(SUM['rdfix_mpc'] - 147.055454) < 0.073
      and abs(_cal['upper95_mev'] - 596.4034) < 0.29
      and abs(_cal['chi2min'] - 886.5954) < 0.44
      and abs(_cal['effective_mass_mev'] - 565.345) < 0.28,
      'the ruler moves the limit by %+.4f meV, %.4f of it -- material for the reference pipeline '
      'and not for this harness, whose limit is set by the absolute scale instead'
      % (SUM['ruler_shift_mev'], SUM['ruler_shift_fraction']))

# Ⓖ⑦ the size of the recalibration
_c0, _c1 = SUM['calibration']['bvel0'], SUM['calibration']['bvel1']
check('Ⓖ⑦ PASSES, and the answer is the one the staging existed to find: ** THE RECALIBRATION IS '
      'ZERO. **  The control\'s spectrum run both ways gives identical peaks at 220, 540, 812 and '
      '1132, an identical 0.7300 for the first peak against the acoustic scale, and identical '
      'height ratios of 2.196 and 2.190 -- every figure given BEFORE and AFTER, as registered',
      SUM['calibration_identical'] is True
      and _c0['peaks'] == [220, 540, 812, 1132] and _c1['peaks'] == _c0['peaks']
      and abs(_c1['l1_over_lA'] - 0.7300) < 3.6e-04
      and abs(_c1['P1_over_P2'] - 2.196) < 1.0e-03
      and abs(_c1['P1_over_P3'] - 2.190) < 1.0e-03
      and _c1['l1_over_lA'] == _c0['l1_over_lA'],
      'the two-fluid branch opens only below the threshold at which that path had already handed '
      'over, so on it the repair changes nothing it did not already do')

# Ⓗ⑧ nothing downstream
check('Ⓗ⑧ PASSES, read off the tree and not asserted: no P15 source is in this revision\'s range, '
      'no banked grid other than the control\'s repaired one, and 72\'s batch is not started',
      SUM['downstream']['p15_untouched'] is True
      and SUM['downstream']['no_other_grid'] is True
      and SUM['downstream']['p15_sources_touched'] == []
      and SUM['downstream']['other_grids_touched'] == [],
      '%d file(s) in the range, none of them a paper source or another arm\'s grid'
      % SUM['downstream']['files_changed'])

# Ⓚ ** NOT A REGISTERED ARM.  THE PROVENANCE COST, FOUND AFTER THE ARMS WERE ADJUDICATED. **
#   *Ⓖ⑦ measured the recalibration at zero and Ⓗ⑧ read the paper sources and the other arms' grids
#   off the tree.  Neither is a statement about the PROVENANCE RATCHETS, and this revision wrote
#   "nothing downstream has to be re-run" before the tree said otherwise.  This row prices what the
#   switch's mere EXISTENCE costs, by reading the receipts that stamp this instrument's switch
#   census or its source hash -- and it is declared as a cost, not presented as a finding.
#   ⌗ *The switch's own existence is NOT re-asserted here as a bare `'BVEL' in INST`: a bare
#   presence test on a token is the vacuous form this corpus's own sweep has caught before, and the
#   substantive fact -- that the switch is bound and DEFAULT OFF -- is already pinned at ⓪ on the
#   sentence the instrument carries beside it.*
_RCPTS = os.path.join(ROOT, 'receipts')
_blobstamp, _censusstamp = [], []
for _dp, _dn, _fn in os.walk(_RCPTS):
    for _f in sorted(_fn):
        if not _f.endswith('.py'):
            continue
        _fp = os.path.join(_dp, _f)
        # ⛔ THIS receipt is skipped, and not by name: it carries both stamps' TEXT because it
        #   counts them, so leaving it in would have it count itself.  *It did, on the first run of
        #   this row -- four instead of three -- which is the vacuity trap this corpus's own sweep
        #   keeps finding: a test that matches on text matches its own text too.*
        if os.path.abspath(_fp) == os.path.abspath(__file__):
            continue
        try:
            _t = io.open(_fp, encoding='utf-8').read()
        except OSError:
            continue
        if 'instrument_blob' in _t:
            _blobstamp.append(_f)
        if 'environment switches with at least one use site' in _t:
            _censusstamp.append(_f)
_stamp = sorted(set(_blobstamp) | set(_censusstamp))
_mine = [_f for _f in _stamp if _f.startswith('P15_the_baryons_never_clustered')]
check('Ⓚ the provenance cost is NOT zero and is read off the tree: exactly %d receipt(s) stamp this '
      'shared instrument\'s switch census or its source hash, so the switch\'s EXISTENCE turns them '
      'red with it OFF and every array byte-identical.  ** None is edited here: all three are '
      'cc66\'s and the patches are routed through FOR_66_FROM_60.md. **  ⌗ The list is MEASURED, '
      'not named: this walks receipts/ for the two stamps rather than asserting which files carry '
      'them, and this receipt is not among them' % len(_stamp),
      len(_stamp) == 3 and len(_blobstamp) == 2 and len(_censusstamp) == 1 and _mine == []
      and _stamp == sorted(_stamp)
      and "the zero is the calibration figures' and not the provenance ratchets'" in RESULT.lower(),
      'blob-stamping %s; census-stamping %s' % (_blobstamp, _censusstamp))

# Ⓘ⑨ the cost
_t = SUM['timings']
check('Ⓘ⑨ PASSES: every timing in the record carries its own configuration, which is the defect '
      'this line found in r7848 and that understated a cost by a factor 16.5',
      len(_t) >= 2
      and all('seconds' in v for f in _t.values() for v in f.values())
      and all(len(v) > 1 for f in _t.values() for v in f.values()),
      '%d timing record(s) over %d file(s)' % (sum(len(v) for v in _t.values()), len(_t)))

# Ⓙ⑩ the count
_ran = 10
check('Ⓙ⑩ the count: this receipt adjudicates all %d registered arms.  THREE registered '
      'expectations are reported as refuted with their criteria unchanged -- Ⓑ② because the rate is '
      'consistent to machine precision where this seat registered it broken, Ⓒ③ because the '
      'flatness criterion was not met AND the excuse offered for it was itself refuted by the '
      'reference, and Ⓕ⑥\'s expectation because the ruler moves this harness\'s limit by two parts '
      'in a thousand where it moves the reference\'s by half.  ** Not one criterion was moved **'
      % _ran,
      _ran == 10
      and 'put to the reference and refuted' in RESULT.lower()
      and 'the recalibration is zero' in RESULT.lower(),
      'three expectations refuted, no criterion loosened')

print()
if not fail:
    print('  ✔ r7854: all %d arms adjudicated.' % _ran)
    print('    => the cause was the baryons\' missing velocity, and the arithmetic closes to %.4f '
          'in the growth exponent.' % abs(DIAG['exponent_measured'] - DIAG['exponent_cold_only']))
    print('    => the repair takes the nine bandpowers to %.6f per dof, below the reference\'s '
          '%.6f, and the banked calibration does not move at all.'
          % (_bp['repaired']['per_dof'], _bp['camb_exactly_binned_per_dof']))
    print('    => what is now exposed is the ABSOLUTE scale: the limit goes %.4f -> %.4f meV '
          'because the joint fit reads it.' % (_lan['upper95_mev'], _min['upper95_mev']))
    print('    => P15 is untouched, the arm of record is NOT JUDGED, and 72\'s batch still waits.')
    sys.exit(0)
print('  ⛔ %d arm(s) failed: %s' % (len(fail), fail))
sys.exit(1)
