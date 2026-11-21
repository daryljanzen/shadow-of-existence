#!/usr/bin/env python3
"""r7852 (60), on order `r7849`: the lensing potential reconciled with CAMB term by term.

COMPUTES: the nine banked Planck 2018 lensing-potential bandpowers, decomposed into the source, the
projection and the binning, each against an independent CAMB reference at the control's fixed
cosmology; the source split again into the transfer handed over at the carry start and the growth
after it; the nine-bandpower score and the joint 555-bin-plus-nine score at thirteen handover times;
and the control's 95 per cent upper limit on the neutrino mass sum at the handover that minimises the
nine-bandpower shape.  ** It pins NO cosmological parameter as a result: the limit it reports is a
reading at a configuration this revision rules AGAINST landing, and the arm of record is NOT
JUDGED. **

⌷ ** THE ID. **  69 ordered this work as `r7849` and this revision's directory, its PREDICTION.md
(committed and pushed at `414b989bd` before a line of the computation existed) and this receipt
carry `r7852`, this line's next even id.

** WHAT THE ORDER ASKED AND WHAT CAME BACK. **  ① locate the -14 to +28 per cent shape difference to
its term.  Located: the SOURCE carries 98.47 per cent of it and the source's own TRANSFER carries
99.80 per cent of that, so the transfer the instrument hands over carries about 98 per cent of
everything.  The projection carries 0.49 per cent and the binning 1.04 per cent.  ② repair it there
and show the score at or near the reference's.  The nine bandpowers go from 2.048681 per dof to
0.891264 by moving ONE switch, which passes the registered criterion -- ** and the criterion was the
wrong test. **  The joint fit, whose lensing side carries no fitted amplitude, gets much worse:
570.3427 to 740.6253, and the control's limit goes from 100.4021 to 583.9810 meV.  ③ the reference
has landed and its BAO rerun has not, so the comparison is made where it can be and the rest said.

⇒ ** AND THE TWO READINGS ARE THE SAME DEFECT. **  The instrument's `Phi` decays through matter
domination instead of freezing.  Between two handovers that decay is a factor `2.234` in power, and
the absolute-normalisation deficit the later handover has to cover is `2.204`: they agree to `1.36`
per cent from records that share no quantity.  So the landed handover's absolute normalisation is a
CANCELLATION of two errors, no handover makes the shape and the normalisation right at once, and the
repair belongs in the instrument's potential evolution -- which recalibrates every spectrum the
corpus rests on and is therefore 69's to order, not this seat's to take.
"""
import io
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
BTW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
RUN = os.path.join(BTW, 'r7852_60_the_lensing_potential_reconciled_with_camb_term_by_term')
R7846 = os.path.join(BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_lensing_bandpowers')
R7850 = os.path.join(BTW, 'r7850_60_phi_carried_through_the_radiation_era')
R7847C = os.path.join(BTW, 'r7847_cc66_a_camb_reference_for_60s_neutrino_mass_harness')


def j(*p):
    return json.load(io.open(os.path.join(*p), encoding='utf-8'))


TERMS = j(RUN, 'terms.json')
SPLIT = j(RUN, 'source_terms.json')
HIST = j(RUN, 'transfer_history_eta500-914-1400-1893-2500-3200-4000.json')
HAND = j(RUN, 'handover_optimum.json')
NORM = j(RUN, 'normalisation_vs_handover.json')
SCORE = j(RUN, 'scoring_path.json')
S400 = j(RUN, 'sampler6_eta400_ics.json')
S400K = j(RUN, 'sampler6_eta400_kdep.json')
S4000 = j(R7850, 'sampler6_lcdm_ics.json')
PRED = ' '.join(io.open(os.path.join(RUN, 'PREDICTION.md'), encoding='utf-8').read().split())
RESULT = ' '.join(io.open(os.path.join(RUN, 'RESULT.md'), encoding='utf-8').read().split())
TSRC = ' '.join(io.open(os.path.join(RUN, 'terms.py'), encoding='utf-8').read().split())
NSRC = ' '.join(io.open(os.path.join(RUN, 'normalisation_vs_handover.py'),
                        encoding='utf-8').read().split())

fail = []


def check(label, cond, detail=''):
    ok = bool(cond)
    print('  %s %s' % ('✔' if ok else '✘', label))
    if detail:
        print('      %s' % detail)
    if not ok:
        fail.append(label.split()[0])
    return ok


def row(name):
    return next(r for r in HAND['rows'] if abs(r['eta'] - name) < 1e-9)


def nrow(eta):
    return next(r for r in NORM['rows'] if abs(r['eta'] - eta) < 1e-9)


print(__doc__.split('\n')[0])
print()

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# ⓪ THE CONTROLS -- without these nothing below is a reading
_pc = TERMS['positive_control']
check('⓪ᵃ the positive control: this revision\'s own projection reproduces, EXACTLY, the banked run '
      'of the code it replicates, at the same configuration.  ** Its first version did not, by a '
      'factor eight thousand in the top bandpower, because it clipped the wavenumber before '
      'dividing by its cube instead of only inside the lookup -- so every term share computed '
      'before this control passed was a measurement of this file\'s own bug **',
      _pc is not None and _pc['max_relative'] == 0.0 and _pc['median_relative'] == 0.0
      and 'phiphi_z13' in _pc['banked']
      and 'that divides and the `k` that looks up are not the same' in TSRC.lower(),
      'max relative difference %.1e over the 36 multipoles' % _pc['max_relative'])

_sd = TERMS['seed_weyl_k_minus_4']
_sb = TERMS['seed_weyl_raw']
check('⓪ᵇ the seed: the reference\'s Weyl transfer carries a squared wavenumber, and which form is '
      'the potential power is MEASURED rather than asserted -- the right one reproduces the '
      'reference\'s own spectrum and the other is out by orders, so the seed cannot pass by accident',
      TERMS['seed_holds'] is True
      and all(abs(x['ratio'] - 1.0) < 0.005 for x in _sd)
      and all(x['ratio'] < 0.01 for x in _sb)
      and abs(_sd[0]['ratio'] - 0.9983) < 5.5e-05
      and abs(_sd[2]['ratio'] - 1.0012) < 5.5e-05,
      'ratios %.4f %.4f %.4f against %.3e %.3e %.3e for the form without it'
      % (_sd[0]['ratio'], _sd[1]['ratio'], _sd[2]['ratio'],
         _sb[0]['ratio'], _sb[1]['ratio'], _sb[2]['ratio']))

check('⓪ᶜ both sides are LINEAR: the reference\'s lensing potential is non-linear by default and '
      'this instrument has none, so the reference is forced linear -- a non-linear reference '
      'against a linear instrument puts a real difference in the wrong term',
      TERMS['config']['nonlinear'] == 'NonLinear_none'
      and SPLIT['config']['nonlinear'] == 'NonLinear_none'
      and TERMS['config']['camb_version'] == '2.0.4',
      'camb %s, %s' % (TERMS['config']['camb_version'], TERMS['config']['nonlinear']))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓐ① THE DECOMPOSITION CLOSES
_sh = TERMS['shares_per_cent']
check('Ⓐ① the decomposition closes, so a statement about WHICH TERM is meaningful: the three '
      'term-by-term differences sum to the total in every one of the nine bins, and the source\'s '
      'two factors do not interact',
      TERMS['closure_max_abs'] < 1e-12
      and abs(TERMS['closure_max_abs'] - 1.6653e-16) < 5.5e-20
      and SPLIT['worst_interaction'] < 1e-03
      and abs(SPLIT['worst_interaction'] - 4.1660e-04) < 5.5e-08,
      'closure %.4e; worst interaction %.4e against the split\'s own total movement of '
      '%.4f (the three terms\' own total is %.4f)'
      % (TERMS['closure_max_abs'], SPLIT['worst_interaction'],
         sum(abs(v) for v in SPLIT['split']['total']),
         sum(abs(v) for v in TERMS['terms']['total'])))

# Ⓑ② THE SOURCE -- registered to agree to better than ten per cent, and it does not
_s1 = SPLIT['S1_worst']
_kk = np.array(SPLIT['S1_transfer_shape']['k'], float)
_sv = np.array(SPLIT['S1_transfer_shape']['instrument_over_camb_minus_1'], float)


def at_k(q):
    return float(_sv[int(np.argmin(np.abs(_kk - q)))])


check('Ⓑ② FAILED AS REGISTERED, and the failure is the finding.  The arm registered that the SOURCE '
      'agrees with the reference to better than ten per cent over the wavenumbers the Limber kernel '
      'weights.  ** It does not: the worst is +111 per cent, and the source carries 98.47 per cent '
      'of the whole shape difference **',
      abs(_s1 - 1.112172) < 5.6e-04 and _s1 > 0.10
      and abs(at_k(5e-3) - 0.8390) < 5.5e-04
      and abs(at_k(1e-2) - 0.3482) < 5.5e-04
      and abs(at_k(2e-2) - 0.1298) < 5.5e-05
      and abs(at_k(1.0) - 0.0554) < 5.5e-05
      and abs(_sh['T1'] - 98.47) < 0.049
      and _sh['T1'] > 50.0,
      'worst %+.4f at k = %.5f /Mpc; the source carries %.2f per cent of the movement'
      % (_s1, SPLIT['S1_worst_k'], _sh['T1']))

# Ⓒ③ THE PROJECTION -- this seat registered the fault HERE, and it is not here
_clip = TERMS['projection_defects']['clip_cost_log']
check('Ⓒ③ FAILED AS REGISTERED, on both halves, and the registered expectation was BACKWARDS.  This '
      'seat registered that the PROJECTION carries the majority of the difference and that the '
      'wavenumber clip is worth more than ten per cent at the top bandpower.  ** The projection '
      'carries 0.49 per cent and the clip 0.17 per cent. **  ⌗ Fed a correct source, the '
      'instrument\'s whole projection reproduces the reference to four parts in a thousand in chi^2',
      abs(_sh['T2'] - 0.4900) < 0.0050
      and _sh['T2'] < 50.0
      and abs(_clip[8] - 0.00165) < 5.5e-05
      and abs(_clip[8]) < 0.10
      and abs(TERMS['chi2'][1]['per_dof'] - 1.070949) < 5.3e-04
      and abs(TERMS['chi2'][5]['per_dof'] - 1.066836) < 5.3e-04,
      'projection %.2f per cent, clip %+.5f in log at the top bandpower; projection on the '
      'reference\'s source %.6f per dof against the reference\'s own %.6f'
      % (_sh['T2'], _clip[8], TERMS['chi2'][1]['per_dof'], TERMS['chi2'][5]['per_dof']))

# Ⓓ④ LIMBER -- registered large at low L and monotone; it is small and not monotone
_le = TERMS['projection_defects']['limber_error_log']
_mono = all(abs(_le[i + 1]) > abs(_le[i]) for i in range(8))
check('Ⓓ④ FAILED AS REGISTERED, on both halves.  The arm registered that Limber underestimates at '
      'the lowest bandpower by more than three per cent and that the error falls monotonically in '
      'multipole.  ** It is 0.16 per cent at the lowest, 0.58 per cent at the highest, and it is '
      'not monotone. **  ⌗ Once the reference is forced linear, Limber on its own source is good '
      'to better than six parts in a thousand across the whole band',
      abs(_le[0] + 0.00159) < 5.5e-05
      and abs(_le[0]) < 0.03
      and abs(_le[8] - 0.00579) < 5.5e-05
      and max(abs(v) for v in _le) < 0.006
      and not _mono,
      'the Limber error runs %+.5f at L = %.1f to %+.5f at L = %.1f, worst %.5f, monotone %s'
      % (_le[0], 28.1, _le[8], 377.3, max(abs(v) for v in _le), _mono))

# Ⓔ⑤ THE BINNING -- registered under half a per cent, and the top bin is above it
_t3 = TERMS['terms']['T3_bandpowers']
check('Ⓔ⑤ FAILED AS REGISTERED, marginally, and the arm existed to make a previous revision\'s '
      'verification a measurement rather than a memory.  Registered under half a per cent; the top '
      'bandpower is +0.71 per cent, which is located in the instrument\'s own 36-node multipole '
      'spline at the top of the band and not in the convention',
      abs(_t3[8] - 0.00710) < 5.5e-05
      and abs(_t3[8]) > 0.005
      and max(abs(v) for v in _t3[:8]) < 0.005
      and abs(_t3[7] + 0.00107) < 5.5e-05
      and abs(_sh['T3'] - 1.0400) < 0.0050,
      'the eight lower bins are within %.5f and the top is %+.5f; the binning carries %.2f per cent'
      % (max(abs(v) for v in _t3[:8]), _t3[8], _sh['T3']))

# Ⓕ⑥ THE VARIABLE -- registered under two per cent, bounded in the reference
_f6 = SPLIT['f_six_weyl_over_poisson_phi']
_w6 = max(abs(v) for row_ in _f6.values() for v in row_)
check('Ⓕ⑥ HOLDS, and it is reported as a BOUND and not as a reading of the instrument.  The '
      'deflection is sourced by the mean of the two potentials and this instrument projects one of '
      'them; the difference between them is bounded in the reference, where both are available at '
      'the same wavenumber and time, at 2.3e-04.  ⚠ That bounds what the VARIABLE can account for; '
      'the instrument\'s own difference is not a state it carries, and this arm does not read it',
      _w6 < 0.02
      and abs(_w6 - 2.2902e-04) < 5.5e-07
      and SPLIT['f_six_is_a_bound_in_camb'] is True
      and 'not a reading of the instrument' in RESULT.lower(),
      'worst %.4e over the four wavenumbers and four times probed' % _w6)

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# the located fault, and the two readings
check('⌗ᵃ the instrument\'s super-horizon value is RIGHT, so what is wrong is the suppression\'s '
      'shape in wavenumber and not the normalisation: at the smallest mode and the landed handover '
      'the potential reads -0.901020 against the analytic -9/10',
      abs(-HIST['phi_at_k_min'] - 0.901020) < 4.5e-04
      and HIST['superhorizon_analytic'] == -0.9,
      'Phi(k -> 0) = %+.6f against %.1f' % (HIST['phi_at_k_min'], HIST['superhorizon_analytic']))

_fr = HIST['frozen_ratio_to_last']
_k005 = [k for k in _fr if k.startswith('k0.05')][0]
_k0001 = [k for k in _fr if k.startswith('k0.0009')][0]
check('⌗ᵇ AND IT HAS NOT FROZEN.  In matter domination the potential is constant.  The '
      'instrument\'s keeps falling right up to the landed handover -- by a factor 1.49473 at the '
      'pivot between two handovers and only 1.05275 at the largest scales, and still moving 4.3 per '
      'cent over the last interval, where the one term the growth equation omits is 0.4 per cent of '
      'the budget.  ** That wavenumber dependence IS the shape disagreement **',
      abs(_fr[_k005][0] - 1.49473) < 7.4e-04
      and abs(_fr[_k0001][0] - 1.05275) < 5.2e-04
      and abs(HIST['largest_move_over_last_interval'] - 4.308e-02) < 5.5e-06
      and HIST['largest_move_over_last_interval'] > 10.0 * 0.00401,
      'the pivot falls by %.5f and the largest scale by %.5f; the last interval still moves %.3e'
      % (_fr[_k005][0], _fr[_k0001][0], HIST['largest_move_over_last_interval']))

check('⌗ᶜ the SOURCE SPLITS, and the growth was already right.  The transfer carries 99.80 per cent '
      'of the source difference and the growth 0.20; the growth agrees with the reference to '
      'between 0.797 and 2.106 per cent at every mode over the whole interval.  ** Swapping only '
      'the transfer takes the nine bandpowers to the reference\'s own value; swapping only the '
      'growth leaves them where they were **',
      abs(SPLIT['shares_per_cent']['transfer'] - 99.80) < 0.049
      and abs(SPLIT['shares_per_cent']['growth'] - 0.2039) < 0.0050
      and abs(SPLIT['chi2']['X2']['per_dof'] - 1.071326) < 5.3e-04
      and abs(SPLIT['chi2']['X1']['per_dof'] - 2.055264) < 1.1e-03
      and abs(SPLIT['chi2']['A']['per_dof'] - 2.048681) < 1.1e-03
      and abs(min(min(v) for v in SPLIT['S2_growth'].values()) - 0.0079680) < 5.5e-07
      and abs(max(max(v) for v in SPLIT['S2_growth'].values()) - 0.0210625) < 5.5e-07
      and abs(100.0 * min(min(v) for v in SPLIT['S2_growth'].values()) - 0.797) < 3.9e-04
      and abs(100.0 * max(max(v) for v in SPLIT['S2_growth'].values()) - 2.106) < 1.0e-03,
      'transfer only %.6f per dof, growth only %.6f, neither moved %.6f'
      % (SPLIT['chi2']['X2']['per_dof'], SPLIT['chi2']['X1']['per_dof'],
         SPLIT['chi2']['A']['per_dof']))

# Ⓖ⑦ THE REPAIR -- it passes as registered, and the criterion was the wrong test
_best, _late = row(400.0), row(4000.0)
check('Ⓖ⑦ PASSES AS REGISTERED -- and ** the criterion was the wrong test, which this receipt says '
      'rather than banking the pass. **  Registered: the nine bandpowers at or below 1.3 per dof '
      'with one amplitude fitted.  Moving ONE switch, the handover, gives 0.891264 on the growth '
      'before last and 1.201007 on the landed scoring path, against 2.131339 where it sits and '
      '1.066836 for the reference.  The handover trade has an INTERIOR minimum, bracketed on both '
      'sides over thirteen handovers',
      abs(_best['per_dof'] - 0.891264) < 4.6e-04
      and _best['per_dof'] <= 1.3
      and abs(SCORE['eta400_kdep']['per_dof'] - 0.891264) < 4.6e-04
      and abs(SCORE['eta400_instrument_ics']['per_dof'] - 1.201007) < 6.1e-04
      and SCORE['eta400_instrument_ics']['per_dof'] <= 1.3
      and abs(SCORE['eta4000_instrument_ics']['per_dof'] - 2.131339) < 1.1e-03
      and abs(SCORE['ics_costs_per_dof_at_eta400'] - 0.309744) < 1.6e-04
      and abs(_late['per_dof'] - 2.048681) < 1.1e-03
      and abs(HAND['improvement_factor'] - 2.299) < 1.2e-03
      and HAND['best']['eta'] == 400.0
      and len(HAND['rows']) == 13
      and HAND['rows'][0]['per_dof'] > _best['per_dof']
      and HAND['rows'][-1]['per_dof'] > _best['per_dof']
      and abs(HAND['rows'][0]['per_dof'] - 31.0007) < 1.6e-02,
      'best %.6f per dof at eta = %.0f, a factor %.3f on the latest; the earliest of the thirteen '
      'is %.4f, so the minimum is interior'
      % (_best['per_dof'], HAND['best']['eta'], HAND['improvement_factor'],
         HAND['rows'][0]['per_dof']))

_cl = NORM['closure']
check('⌗ᵈ ** AND WHY THE CRITERION WAS THE WRONG TEST, in one number. **  The lensing side of the '
      'joint fit carries NO fitted amplitude -- one primordial normalisation serves both sides, '
      'which is the mechanism that gives the optical depth its reach -- so the joint fit tests the '
      'ABSOLUTE normalisation and the nine-bandpower score with an amplitude fitted tests only the '
      'SHAPE.  The two order the handovers in opposite directions, strictly and monotonically, over '
      'the eight from the shape\'s minimum to the latest probed',
      NORM['opposed_from_shape_minimum_onward'] is True
      and NORM['absolute_improves_monotonically_everywhere'] is True
      and len(NORM['tail_etas']) == 8
      and abs(nrow(400.0)['per_cent_low'] - 63.5934) < 3.2e-02
      and abs(nrow(4000.0)['per_cent_low'] - 9.0437) < 5.0e-03
      and abs(nrow(4000.0)['ratio'] - 0.909563) < 4.6e-04
      and abs(nrow(400.0)['ratio'] - 0.364066) < 1.9e-04,
      'at the shape\'s best handover the absolute is %.2f per cent low; at the latest, %.2f'
      % (nrow(400.0)['per_cent_low'], nrow(4000.0)['per_cent_low']))

check('⌗ᵉ ** THE CANCELLATION, from two records that share no quantity. **  The instrument\'s own '
      'spurious decay between two handovers is a factor 2.234 in power; the absolute-normalisation '
      'deficit the later one has to cover between the same two is 2.204.  They agree to 1.36 per '
      'cent.  ⇒ So the landed handover\'s absolute normalisation is a CANCELLATION of two errors '
      'and not a correctness, and no handover makes the shape and the normalisation right at once',
      abs(_cl['decay_in_power'] - 2.23420) < 1.1e-03
      and abs(_cl['normalisation_deficit_ratio'] - 2.20426) < 1.1e-03
      and abs(100.0 * _cl['relative_disagreement'] - 1.36) < 5.0e-03
      and _cl['agrees_within_5_per_cent'] is True
      and 'cancellation' in _cl['verdict'].lower()
      and 'the claim is made only where it is true' in NSRC.lower(),
      'decay in power %.5f against a deficit ratio of %.5f, agreeing to %.2f per cent'
      % (_cl['decay_in_power'], _cl['normalisation_deficit_ratio'],
         100.0 * _cl['relative_disagreement']))

# Ⓗ⑧ THE CONTROL, owed because Ⓖ⑦ passed
_b4, _u4 = S400['lcdm_bounded'], S400['lcdm_unbounded']
_b0, _u0 = S4000['lcdm_bounded'], S4000['lcdm_unbounded']
_span = max(_b4['upper95_per_chain_mev']) - min(_b4['upper95_per_chain_mev'])
check('Ⓗ⑧ DELIVERED, because Ⓖ⑦ passed and the arm was registered conditional on it -- and it is '
      'the measurement that rules AGAINST the repair.  At the handover that minimises the shape the '
      'control reads 583.9810 +/- 0.2036 meV against the published 64.2, with an effective mass of '
      '+532.588 +/- 32.475 meV and a joint minimum of 740.6253, against 100.4021 +/- 0.3533, '
      '+21.913 +/- 44.423 and 570.3427 where the handover sits.  ** Nothing is below 59 or 64 meV, '
      'against 70.51 and 75.20 per cent before **',
      abs(_b4['upper95_mev'] - 583.9810) < 0.30
      and abs(_b4['upper95_mcse_mev'] - 0.2036) < 1.1e-04
      and abs(1000.0 * _u4['sum_mean_ev'] - 532.588) < 0.27
      and abs(1000.0 * _u4['sum_sd_ev'] - 32.475) < 1.7e-02
      and abs(_b4['best_fit']['chi2'] - 740.6253) < 0.37
      and abs(_b0['upper95_mev'] - 100.4021) < 5.1e-02
      and abs(_b0['best_fit']['chi2'] - 570.3427) < 0.29
      and _b4['best_fit']['chi2'] > _b0['best_fit']['chi2']
      and _b4['frac_below_0.059'] == 0.0 and _b4['frac_below_0.064'] == 0.0
      and abs(_b0['frac_below_0.059'] - 0.705125) < 3.6e-04,
      'the limit worsens %.4f -> %.4f meV and the joint minimum %.4f -> %.4f'
      % (_b0['upper95_mev'], _b4['upper95_mev'], _b0['best_fit']['chi2'], _b4['best_fit']['chi2']))

check('Ⓗ⑧ᵇ and the chains it is read off are HEALTHY, so the reading is the model\'s and not the '
      'sampler\'s: every direction below 1.0002 on the convergence statistic, every effective '
      'sample size above 55000, acceptance 0.2309 and 0.2240, the minimum NOT on a bound, no '
      'direction with unmeasurable curvature, and the six chains\' own limits spanning 1.283 meV '
      'against a Monte-Carlo error of 0.2036',
      max(v['rhat'] for v in _b4['diagnostics'].values()) < 1.0002
      and max(v['rhat'] for v in _u4['diagnostics'].values()) < 1.0002
      and min(v['ess'] for v in _b4['diagnostics'].values()) > 55000.0
      and abs(_b4['accept'] - 0.230865) < 5.5e-05
      and abs(_u4['accept'] - 0.223994) < 5.5e-05
      and S400['lcdm_proposal']['minimum_on_a_bound'] is False
      and S400['lcdm_proposal']['curvature_unmeasurable_in'] == []
      and abs(_span - 1.283) < 7.0e-04,
      'worst R-hat %.6f, least effective sample size %.0f, per-chain span %.3f meV'
      % (max(v['rhat'] for v in _b4['diagnostics'].values()),
         min(v['ess'] for v in _b4['diagnostics'].values()), _span))

check('Ⓗ⑧ᶜ and the ALTERNATIVE growth at the same handover reports its own unreportability, in its '
      'guard fields and not in prose: the minimum sits ON A BOUND at the model\'s own upper edge '
      'with the optical depth at zero, the curvature is unmeasurable in BOTH of those directions, '
      'and the joint minimum is 1413.3085.  ** Its nominal 95 per cent figure is the grid\'s edge, '
      'so no limit from it is reported and only these flags are pinned **',
      S400K['lcdm_proposal']['minimum_on_a_bound'] is True
      and sorted(S400K['lcdm_proposal']['curvature_unmeasurable_in']) == ['MNU', 'TAU']
      and abs(S400K['lcdm_bounded']['best_fit']['chi2'] - 1413.3085) < 0.71
      and abs(S400K['lcdm_bounded']['best_fit']['x'][4] - 0.600000) < 5.5e-07
      and S400K['lcdm_bounded']['best_fit']['chi2'] > _b4['best_fit']['chi2'],
      'minimum on a bound at Sum = %.6f eV with tau = %.6f, joint minimum %.4f, curvature '
      'unmeasurable in %s' % (S400K['lcdm_bounded']['best_fit']['x'][4],
                              S400K['lcdm_bounded']['best_fit']['x'][5],
                              S400K['lcdm_bounded']['best_fit']['chi2'],
                              S400K['lcdm_proposal']['curvature_unmeasurable_in']))

# Ⓘ⑨ THE COST, with its configuration beside it
_t = dict(TERMS['timings'])
_need = ('etaref', 'nkp', 'clamp')
_solve = _t.get('instrument_phi_solve')
check('Ⓘ⑨ HOLDS: every timing in the record carries its own configuration, which is the defect this '
      'line found in r7848 and understated a cost by a factor 16.5.  ⌗ And the cost is set by the '
      'END TIME and not by the mode count: the same 220-mode solve costs about 700 s to the landed '
      'handover and about 12 s to the repaired one, which is why thirteen handovers were affordable '
      'at all',
      all(('multipoles' in v or 'etaref' in v or 'lmax' in v or 'nk_growth' in v)
          for v in _t.values())
      and all('seconds' in v for v in _t.values())
      and (_solve is None or all(k in _solve for k in _need))
      and HIST['nk_modes'] == 220
      and TERMS['etaref'] == 4000.0,
      '%d timing(s) recorded, each with its switches' % len(_t))

# Ⓙ⑩ cc66's REFERENCE AND ITS ORDERED RERUN -- probed, not taken on the channel's word
_cc = j(R7847C, 'score_reference.json')
check('Ⓙ⑩ HOLDS, and it is PROBED rather than taken on the page\'s word, this line having found '
      'three stated absences false in three revisions.  ** cc66\'s reference HAS landed ** -- '
      '82.890 meV on 613 bins with the nine bandpowers and a stated optical-depth prior -- and the '
      'BAO rerun 69 ordered on top of it has NOT, so the comparison is made where it can be and '
      'the rest is said and not inferred.  ⚠ cc66\'s own record states its bin set is not this '
      'harness\'s 555, so the two limits are not on identical data and this receipt does not treat '
      'them as if they were',
      abs(_cc['limit95_meV'] - 82.890) < 4.2e-02
      and _cc['nbandpowers'] == 9
      and _cc['scored_bins'] == 613
      and 'is NOT reproducible here' in _cc['bin_subset_note']
      and abs(_cc['tau_prior']['mean'] - 0.054) < 5.5e-05
      and 'bao rerun' in RESULT.lower(),
      'cc66 %.3f meV on %d bins; this harness scores 555, so the comparison is stated with that '
      'caveat' % (_cc['limit95_meV'], _cc['scored_bins']))

# Ⓚ⑪ THE COUNT
_ran = 11
check('Ⓚ⑪ the count: this receipt adjudicates all %d registered arms.  FOUR are reported FAILED '
      'with their criteria exactly as registered -- Ⓑ② because the source is wrong by far more than '
      'the registered ten per cent, Ⓒ③ because this seat registered the projection as the fault and '
      'it is not, Ⓓ④ because the Limber error is small and not monotone rather than large and '
      'monotone, and Ⓔ⑤ because the top bandpower exceeds the registered half a per cent.  ** The '
      'one arm this seat registered an expectation on, it got BACKWARDS, and that is reported as a '
      'refutation and not reframed **' % _ran,
      _ran == 11
      and 'registered the projection' in RESULT.lower()
      and 'and only if Ⓖ⑦ passes' in PRED,
      'four failed as registered, one of them this seat\'s own expectation')

print()
if not fail:
    print('  ✔ r7852: all %d arms adjudicated.' % _ran)
    print('    => the fault is the TRANSFER (%.2f per cent of the source, %.2f per cent of the '
          'whole), not the carry and not the projection.'
          % (SPLIT['shares_per_cent']['transfer'], _sh['T1']))
    print('    => the shape and the absolute normalisation order the handovers OPPOSITELY, and the '
          'landed one is right by a cancellation that closes to %.2f per cent.'
          % (100.0 * _cl['relative_disagreement']))
    print('    => so the handover is NOT changed and the control\'s limit of record stands; the '
          'repair belongs in the instrument\'s potential evolution, which is 69\'s to order.')
    print('    => Ⓗ⑧ delivered at the repaired handover: %.4f meV, and it is worse. P15 is '
          'untouched.' % _b4['upper95_mev'])
    sys.exit(0)
print('  ⛔ %d arm(s) failed: %s' % (len(fail), fail))
sys.exit(1)
