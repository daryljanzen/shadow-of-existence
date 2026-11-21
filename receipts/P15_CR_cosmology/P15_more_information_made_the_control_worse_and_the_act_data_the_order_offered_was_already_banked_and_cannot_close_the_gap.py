#!/usr/bin/env python3
r"""RECEIPT -- P15 (r7848, node 60): ** THE SCALE-DEPENDENT GROWTH IS IN AND THE NINE BANKED
BANDPOWERS ARE SCORED WITH NOTHING FITTED -- AND THE CONTROL GOT WORSE, NOT BETTER: ITS LIMIT WENT
FROM 99.67 TO 111.38 meV AND ITS EFFECTIVE MASS FLIPPED BACK TO THE WRONG SIGN.  THE ACT DR6 DATA
THE ORDER OFFERED WAS ALREADY BANKED, AND AN OVER-GENEROUS UPPER BOUND ON WHAT IT COULD CONTRIBUTE
BUYS SEVEN AND A HALF PER CENT OF THE REMAINDER.  AND A GUARD THIS SEAT WROTE ONE REVISION AGO
PASSED A CHAIN FROZEN IN THE ONE DIRECTION THE RESULT IS READ OFF. **

COMPUTES: the two-fluid scale-dependent growth on this instrument's own rate and its isolation
  against the background quadrature it fails to reproduce; the bandpower convention read off the
  code that banked the data; the absolute normalisation held rather than fitted; tau's reach once
  the lensing term is in; the control's 95 per cent limit and effective mass on 555 CMB bins plus 9
  lensing bandpowers with a tau prior; an upper bound on ACT DR6 CMB-only's marginal information
  about the neutrino sum; and the per-direction movement of a Metropolis chain.  ** It pins NO
  cosmological parameter as a result, and the arm of record is NOT JUDGED. **

⌷ ** THE ID. **  69 ordered this work as r7845 and its commits, its computation directory and the
PREDICTION.md registered at `0859200f7` all carry r7846.  It LANDS as r7848: the trunk's front is
69's own r7845 and this line's next id of its own parity above the front is r7848.  Same work, same
registration.  *The same thing happened to r7844, which was ordered as r7842.*

THE ORDER (r7845, 69): ① replace the frozen growth with a scale-dependent one carried from z = 12.8
to z = 0; ② score the nine banked Planck 2018 lensing bandpowers with their covariance and windows,
with NO fitted amplitude, so tau acquires reach, stating the tau treatment used; ③ the control
first -- its 95 per cent limit near 64.2 meV and its effective mass near -0.101 eV, each with its
Monte-Carlo error -- then the arm's limit and where 59 and 64 meV sit.  ACT DR6 CMB-only only if the
control needs it, and say so.  P15 is not to change until the arm is read.  PREDICTION.md was
committed and pushed BEFORE any computation, with eleven arms.

** THE SHAPE OF THE RESULT -- THREE ARMS FAIL AND EACH FAILURE IS THE INFORMATIVE HALF. **

  Ⓖ⑦ FAILS BOTH HALVES, AND IT FAILS IN THE DIRECTION NOBODY REGISTERED.  Every previous revision
  on this line closed the gap by adding what the harness was not scoring: r7838's 185 temperature
  bins were loose by a factor 4.33, r7844's 555 bins with polarisation brought that to 1.55 and
  flipped the effective mass to the published sign.  ** ADDING THE LENSING BANDPOWERS AND A TAU
  PRIOR UNDID BOTH. **  The limit goes from 99.67 +/- 0.55 to 111.38 +/- 0.41 meV -- 36.91 standard
  errors above the order's own ceiling of 96.3 -- and the effective mass from -7.0 +/- 50.9 back to
  +44.3 +/- 39.8 meV, positive, where the published figure is -0.101 eV.  This seat registered PASS
  and a limit between 50 and 90 meV, and is refuted by 52.33 standard errors.  R-hat is 1.0001,
  the smallest effective sample size 46515, and the acceptance 0.231: ** the chains are healthy and
  the answer is wrong. **

  Ⓐ① FAILS AT 5.276e-03 AGAINST A REGISTERED 1e-10, AND THE THING COMPARED AGAINST IS THE DEFECT.
  The gap is 1.110e-16 at the start -- zero by construction, the solver being handed the
  quadrature's own growing mode -- and accumulates to z = 0 while the radiation share falls to
  nothing.  Built on ONE pure matter + Lambda rate, the quadrature and the ODE agree to 9.799e-09.
  ⇒ The ODE is the growth equation; `growth_over_a()` is a matter + Lambda closed form evaluated on
  a background that carries radiation, outside the validity its own docstring states.  ** Ⓐ①'s
  1e-10 is r7844's mistake in a new place: not a tolerance finer than a Monte-Carlo error but a
  tolerance finer than the ACCURACY OF THE THING COMPARED AGAINST. **

  Ⓗ⑧ IS NOT JUDGED, as registered -- it was conditional on Ⓖ⑦, and r7838 and r7844 both ruled the
  same way.  Its chain ran only for the 59/64 meV placement the order asks for either way, and
  P15 is NOT touched.

** AND THE ORDER'S CONDITIONAL DATA WAS ALREADY IN THE HARNESS, FOR THE SECOND REVISION RUNNING. **
r7844's Ⓗ⑧ asserted that no lensing bandpowers were banked and named its own refutation; they were
banked.  This order offered ACT DR6 CMB-only "only if the control needs it", and
`computations/planck_tt_likelihood/data/act_dr6_cmbonly/` has held the DR6.02 SACC file verbatim
since r7815+70.1: 45 foreground-marginalised bandpowers each in TT, TE and EE over ell 600.5-6125.5,
the full 135 x 135 covariance, windows on ell 2-8501.  So Ⓘ⑨ was never a question about access, and
it is answered by MEASUREMENT: 84 of the 135 bandpowers lie wholly inside this instrument's reach,
and a marginalised Fisher on them -- built with no ACT nuisances, with the amplitude shared with
Planck, and treating ACT as independent of Planck although its footprint is inside Planck's sky and
those bandpowers sit inside the band Planck already scores here, ** every one of which overstates
the gain ** -- gives sigma(Sum) = 104.1 meV where closing the limit would take 12.765.  Combined
with the control it buys 3.56 meV of the 47.18 meV remainder.  ⇒ NOT ADDED, with the control's
figure as the reason.

⌗ AND THE REMAINDER IS NOT A PRECISION DEFICIT.  Shrinking a width moves a limit and leaves a
centre exactly where it is: at the shrink factor that would close the limit, the effective mass goes
from 3.65 to 11.95 standard errors from the published value.  The operation that would mend one half
of Ⓖ⑦ makes the other half worse, so no amount of the same observable closes this.

rc=0 when every arm holds, including the arms that record a registered failure AS a failure.
Run: python3 <this file>                                                        (numpy only)
"""
import io
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
RUN = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                   'r7846_60_the_scale_dependent_growth_and_the_banked_lensing_bandpowers')
R7842 = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                     'r7842_60_polarisation_added_to_the_score_and_the_two_data_the_harness_'
                     'does_not_have')
ACT = os.path.join(ROOT, 'computations', 'planck_tt_likelihood', 'data', 'act_dr6_cmbonly')
LENS70 = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7471_70_PO24_tilt_off_the_tail',
                      'lensing')

PUBLISHED_LIMIT_MEV = 64.2          # arXiv:2503.14744, the standard-model 95 per cent upper limit
PUBLISHED_EFFECTIVE_EV = -0.101     # its effective mass, the sum free to go negative
ORDER_BAND_MEV = (42.8, 96.3)       # the order's factor-1.5 window on the published limit
SEAT_EXPECTATION_MEV = (50.0, 90.0)  # this seat's own registered expectation, falsifiable
R44_LIMIT_MEV = 99.67               # r7844's control, with polarisation and no lensing
R44_EFFECTIVE_MEV = -7.0
R38_LIMIT_MEV = 277.7               # r7838's control, temperature only
TEXTBOOK_ASYMPTOTE = -8.0           # the -8 f_nu suppression of the small-scale power

fail = []


def check(label, ok, witness=''):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}" + (f"   ({witness})" if witness else ''))
    if not ok:
        fail.append(label)


def jload(name, where=RUN):
    with io.open(os.path.join(where, name), encoding='utf-8') as fh:
        return json.load(fh)


def src(name, where=RUN):
    with io.open(os.path.join(where, name), encoding='utf-8') as fh:
        return fh.read()


def pin(x, printed, pc=0.0005):
    """the pin rule: the allowance is the COARSER of half a unit in the last printed digit and
    0.05 per cent of |X|, and a tolerance is written INSIDE that bound, never at it"""
    s = f'{printed}'
    dec = len(s.split('.')[1]) if '.' in s else 0
    half = 0.5 * 10 ** (-dec)
    return abs(float(x) - float(printed)) <= max(half, pc * abs(float(printed))) * 0.9


GROW = jload('growth_kdep.json')          # ① the scale-dependent growth
CARRY = jload('carry_validity.json')      # the closed test that reversed the carry decision
CMP = jload('phiphi_carry_compare.json')  # the two carries scored, reading superseded
INFO = jload('lensing_informative.json')  # the absolute normalisation and the sum's reach
TAU = jload('tau_reach_with_lensing.json')
ACTD = jload('act_dr6_decision.json')     # Ⓘ⑨
CTRL = jload('sampler6_lcdm.json')        # Ⓖ⑦, the control
PRED = src('PREDICTION.md')
RESULT = src('RESULT.md')
LLSRC = src('lensing_like.py')
M6SRC = src('model6.py')
SAMP = src('sampler6.py')
GKSRC = src('growth_kdep.py')
RESULT1 = ' '.join(RESULT.split())   # one line, so a wrap cannot decide an assertion
PRED1 = ' '.join(PRED.split())

R44 = jload('sampler3_lcdm_pol.json', R7842)   # r7844's own control, read not retyped
_ARM = os.path.join(RUN, 'sampler6_cr.json')
ARM = jload('sampler6_cr.json') if os.path.exists(_ARM) else None

print('r7848 (60), ordered as r7846 -- the scale-dependent growth and the banked bandpowers, '
      'read from this revision\'s own runs\n')

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓐ①  THE REGISTERED FAILURE, ASSERTED -- AND THE CAUSE ISOLATED RATHER THAN GUESSED
_a1, _iso = GROW['A1_vs_quadrature'], GROW['A1_isolation']
check('Ⓐ① the registered tolerance was 1e-10 relative at every scale factor and wavenumber and the '
      'new growth reproduces the background quadrature to 5.276e-03 instead -- REPORTED FAILED '
      'with the criterion exactly as registered.  ** The gap is 1.110e-16 at the start, zero by '
      'construction, and ACCUMULATES to z = 0 while the radiation share falls to nothing, so it is '
      'not an offset. **  And the cause is isolated and not guessed: built on ONE pure matter + '
      'Lambda rate the quadrature and the ODE agree to 9.799e-09, solver tolerance, so the ODE is '
      'the growth equation and the closed form is being used outside the validity its own '
      'docstring states',
      (_a1['holds'] is False) and pin(_a1['registered_tol'], 1e-10)
      and pin(_a1['max_rel'], 0.005276) and abs(_a1['at_start']) < 1e-14
      and pin(_iso['max_rel'], 9.799e-09, pc=0.001) and _iso['max_rel'] < 1e-07
      and _a1['n_a'] >= 25 and _a1['n_k'] >= 40 and pin(_a1['z_start'], 12.833)
      and 'outside matter + Lambda' in _iso['verdict'],
      'registered %.0e, measured %.6f over %d x %d points; on matter+Lambda alone %.3e'
      % (_a1['registered_tol'], _a1['max_rel'], _a1['n_a'], _a1['n_k'], _iso['max_rel']))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓑ②  THE SHAPE IS SCALE-DEPENDENT IN THE DIRECTION THE PHYSICS NAMES
_b2 = GROW['B2_shape']
_sup = np.asarray(_b2['suppression'], float)
check('Ⓑ② the suppression at a = 1 is MONOTONE NON-INCREASING in k across the whole band, from '
      '-1.790e-06 at k = 1e-4 to -0.026649 at k = 1 /Mpc -- so it vanishes at large scales and '
      'saturates at small ones, which is the free-streaming signature and not a flat rescaling.  '
      'The named negative was a suppression FLAT in k',
      _b2['monotone_non_increasing'] and bool(np.all(np.diff(_sup) <= 1e-15))
      and pin(_b2['at_low_k'], -1.790e-06, pc=0.001) and pin(_b2['at_high_k'], -0.026649)
      and abs(_b2['at_low_k']) < 1e-04 < abs(_b2['at_high_k']) and pin(_b2['f_nu'], 0.0225069),
      'f_nu = %.7f; %d wavenumbers, no increase anywhere' % (_b2['f_nu'], _sup.size))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓒ③  THE ASYMPTOTE IS REPORTED, NOT CLAIMED TO AGREE
_c3, _ms = GROW['C3_asymptote'], GROW['missing_stretch']
check('Ⓒ③ the high-k asymptote on the power is REPORTED and not tested: -0.053298 carried from the '
      'ordered z = 12.8 against the textbook -8 f_nu = -0.180055, a ratio of 0.296012; carried '
      'instead from the non-relativistic transition at z = 187.92 it is -0.120083, a ratio of '
      '0.666922.  ** So the ordered interval carries 44.4 per cent of what the full '
      'post-non-relativistic one does, AND even the longer one reaches two thirds of the textbook '
      'figure rather than all of it ** -- the remainder being the filter as an interpolation.  '
      'Neither number is called agreement',
      _c3['is_a_report_not_a_test'] and pin(_c3['measured_on_power'], -0.053298)
      and pin(_c3['textbook'], -0.180055) and pin(_c3['ratio'], 0.296012)
      and pin(_c3['textbook'], TEXTBOOK_ASYMPTOTE * _c3['f_nu'], pc=0.001)
      and pin(_ms['power_from_nr'], -0.120083) and pin(_ms['ratio_from_nr_to_textbook'], 0.666922)
      and pin(_ms['fraction_carried'], 0.443848) and pin(_ms['z_nonrelativistic'], 187.92)
      and 'interpolation' in GKSRC,
      '%.6f of the textbook from the ordered start, %.6f from the transition' % (
          _c3['ratio'], _ms['ratio_from_nr_to_textbook']))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓒ③ᵇ  THE CARRY FORK: DECIDED, ROUTED, THEN REVERSED ON MEASUREMENT -- AND THE REVERSAL IS VISIBLE
_rad = CARRY['radiation_over_matter']
check('Ⓒ③ᵇ the carry fork was decided for z = 188 on the score, ROUTED to 66 with that '
      'recommendation, and then REVERSED by measurement rather than by argument -- and the '
      'superseded reading is left standing beside the reversal rather than tidied away.  The '
      'closed test asks whether a matter-only growth equation LINKS the two start times at all, '
      'and it does not: the ratio is k-dependent, 0.9638 at the largest scales and 0.7362 at the '
      'smallest, median 0.7807, which is sub-horizon Phi decay through residual radiation -- 5.47 '
      'per cent of matter at z = 188 against 0.39 at z = 12.8.  ** So the better chi^2/dof of 1.07 '
      'at z = 188 against 2.05 at z = 12.8 was a truncation error PARTLY CANCELLED BY A GROWTH '
      'ERROR, and the ORDERED carry is the one the grid was built on **',
      CARRY['k_dependent'] and (CARRY['verdict']['growth_links_the_two_times'] is False)
      and pin(CARRY['ratio_max'], 0.9638) and pin(CARRY['ratio_min'], 0.7362)
      and pin(CARRY['ratio_median'], 0.7807)
      and pin(_rad['z_188.1'], 0.054734) and pin(_rad['z_12.8'], 0.003920, pc=0.002)
      and 'REVERSED' in CARRY['verdict']['decision']
      and CMP['verdict'].get('this_file_is_not_the_current_decision') is True
      and CMP['verdict'].get('superseded_by') == 'carry_validity.json'
      and pin(CMP['carries']['z13']['chi2_per_dof'], 2.0487)
      and pin(CMP['carries']['z188']['chi2_per_dof'], 1.0706),
      'ratio %.4f..%.4f, median %.4f; radiation share %.6f vs %.6f'
      % (CARRY['ratio_min'], CARRY['ratio_max'], CARRY['ratio_median'],
         _rad['z_12.8'], _rad['z_188.1']))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓓ④  NOTHING IS FITTED IN THE LENSING TERM, ASSERTED OFF THE CODE THAT RUNS
_chi2_body = LLSRC.split('def chi2(')[1].split('\ndef ')[0] if 'def chi2(' in LLSRC else ''
_no_solve = not any(t in _chi2_body for t in ('solve', 'lstsq', '/ (m @', 'amplitude', 'minimi'))
_amp_from_cmb = ('amp_cmb' in M6SRC and 'T_CMB_UK' in M6SRC and 'exp(' in M6SRC)
check('Ⓓ④ the lensing chi^2 fits NOTHING, and that is asserted off the body of the function that '
      'runs rather than off a docstring: the nine bandpowers are binned through their own nine '
      'windows, the 9 x 9 Fisher is inverted ONCE at import, and `chi2` contains no solve, no '
      'least squares and no amplitude.  The normalisation comes from the CMB half -- every mode '
      'starts at Phi = -1, so the CMB fit determines AMP*exp(-2 tau) and the lensing prediction is '
      'that number times exp(+2 tau)/T_CMB^2.  ** The named negative was an amplitude appearing '
      'anywhere in the lensing term, which would have thrown away exactly the absolute '
      'normalisation that gives tau its reach **',
      bool(_chi2_body) and _no_solve and _amp_from_cmb and 'FISHER' in LLSRC
      and LLSRC.count('def chi2(') == 1,
      'chi2 body %d chars, no amplitude solve; model6 builds the amplitude from the CMB fit'
      % len(_chi2_body))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓓ④ᵇ  THE ABSOLUTE NORMALISATION IS HELD AND AGREES TO NINE PER CENT -- NOT ONE
_amp = INFO['amp_from_cmb_components']
_held, _pref = INFO['amp_held'], INFO['amp_preferred_by_bandpowers']
_naive = _amp['A_cmb'] / _amp['T_CMB_sq']
check('Ⓓ④ᵇ the held prediction is (A_cmb/T_CMB^2)*exp(+2 tau) = 1.617967e-09 and the bandpowers '
      'themselves prefer 1.471643e-09, a ratio of 0.909563: ** the prediction is high by nine per '
      'cent with NOTHING fitted. **  ⌗ And the figure is stated in the convention it was measured '
      'in: dropping the exp(+2 tau) makes the same comparison read 1.3 per cent, and that '
      'comparison is WRONG, because the reionisation suppression lives in the CMB amplitude and '
      'not in the matter potential.  The agreement this revision claims is nine per cent, not one',
      pin(_held, 1.617967e-09) and pin(_pref, 1.471643e-09)
      and pin(INFO['amp_ratio_preferred_over_cmb'], 0.909563)
      and pin(_held, _naive * np.exp(2.0 * _amp['tau']), pc=0.001)
      and abs(_pref / _naive - 1.0) < 0.02 < abs(_pref / _held - 1.0),
      'held %.6e, preferred %.6e, ratio %.6f; without exp(+2 tau) the ratio would read %.4f'
      % (_held, _pref, INFO['amp_ratio_preferred_over_cmb'], _pref / _naive))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓓ④ᶜ  THE SHAPE SYSTEMATIC IS CHARACTERISED, AND THE TERM IS INFORMATIVE ANYWAY
_z13 = CMP['carries']['z13']
check('Ⓓ④ᶜ the shape systematic is MEASURED and reported beside the result rather than left '
      'implicit: at the ordered carry chi^2 is 16.389 on 8 degrees of freedom, 2.049 per degree of '
      'freedom, with a monotone +49.8 per cent drift.  Against that, moving the sum across the '
      'grid moves chi^2_lens by 94.497, five to six times the systematic, with the minimum near '
      'Sum = +0.15 eV -- so the term carries information about the sum DESPITE the shape error, '
      'which is why it is scored and why the error is stated',
      pin(_z13['chi2'], 16.389) and pin(_z13['chi2_per_dof'], 2.0487) and _z13['dof'] == 8
      and pin(_z13['drift_vs_fiducial_pc'], 49.813) and _z13['monotone']
      and pin(INFO['sum_moves_chi2_by'], 94.497) and INFO['informative']
      and INFO['sum_moves_chi2_by'] > 5.0 * _z13['chi2']
      and min(INFO['rows'].values(), key=lambda r: r['chi2'])['mnu'] == 0.15,
      'chi^2/dof %.4f, drift %.3f per cent, the sum moves chi^2 by %.3f'
      % (_z13['chi2_per_dof'], _z13['drift_vs_fiducial_pc'], INFO['sum_moves_chi2_by']))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓔ⑤  TAU ACQUIRES REACH -- MEASURED
check('Ⓔ⑤ tau acquires reach, measured and not asserted: the score moves by 355.161 across '
      'tau = 0.02-0.20 where r7844 measured 1.137e-12 without the lensing term, a ratio of '
      '3.124e+14 against a registered threshold of 1.  Lensing alone prefers tau = +0.0065, a '
      '6.79 sigma pull on the 0.054 +/- 0.007 prior -- ** RECORDED AS CONFOUNDED with the sum and '
      'with the 49.8 per cent shape systematic, and NOT as a measurement of tau **',
      TAU['holds'] and pin(TAU['spread'], 355.161) and pin(TAU['ratio'], 3.124e+14, pc=0.001)
      and TAU['spread'] > TAU['registered_threshold']
      and pin(TAU['r7844_without_lensing'], 1.137e-12, pc=0.001)
      and pin(TAU['tau_preferred_by_lensing_alone'], 0.0065)
      and pin(TAU['pull_sigma'], 6.786) and 'confounded' in TAU['caveat'],
      '%.3f against %.3e, ratio %.4e' % (TAU['spread'], TAU['r7844_without_lensing'],
                                         TAU['ratio']))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓕ⑥  THE TAU TREATMENT IS NAMED, AND NAMED AS A STAND-IN
_tau_term = 'chi2_tau' in LLSRC and '0.054' in LLSRC and '0.007' in LLSRC
check('Ⓕ⑥ the tau treatment is NAMED and is asserted off the code: an additive Gaussian term '
      '((tau - 0.054)/0.007)^2, the same stand-in node 70 used at r7471 for low-l EE.  ** And the '
      'receipt says what it is: the low-l data itself is ABSENT from this harness and this is a '
      'stand-in for it, not the published likelihood. **  The named negative was a tau left free, '
      'or a width invented here rather than taken from the published fit',
      _tau_term and pin(TAU['tau_prior']['mean'], 0.054) and pin(TAU['tau_prior']['sigma'], 0.007)
      and 'stand-in' in RESULT1 and 'stand-in' in PRED1.replace('stand in', 'stand-in'),
      'prior %.3f +/- %.3f, additive, named as a stand-in in both PREDICTION.md and RESULT.md'
      % (TAU['tau_prior']['mean'], TAU['tau_prior']['sigma']))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓖ⑦  THE DECISIVE ARM -- FAILS BOTH HALVES, AND IN THE DIRECTION NOBODY REGISTERED
_b, _u = CTRL['lcdm_bounded'], CTRL['lcdm_unbounded']
_lim, _se = _b['upper95_mev'], _b['upper95_mcse_mev']
_eff, _effsd = _u['sum_mean_ev'] * 1e3, _u['sum_sd_ev'] * 1e3
_above_order = (_lim - ORDER_BAND_MEV[1]) / _se
_above_seat = (_lim - SEAT_EXPECTATION_MEV[1]) / _se
check('Ⓖ⑦ THE DECISIVE ARM FAILS BOTH HALVES.  The criterion as registered was a limit inside '
      '42.8-96.3 meV AND a NEGATIVE effective mass.  Measured: 111.38 +/- 0.41 meV, which is '
      '36.91 standard errors ABOVE the band, and +44.25 +/- 39.79 meV, POSITIVE.  ** And it fails '
      'in the direction nobody registered: r7838 was loose by 4.33, r7844 brought that to 1.55 '
      'and flipped the sign to the published one, and adding the lensing bandpowers and a tau '
      'prior UNDID BOTH -- 99.67 to 111.38 meV and -7.0 back to +44.3. **  This seat registered '
      'PASS and a limit between 50 and 90 meV and is refuted by 52.33 standard errors.  The '
      'window was 40 meV wide against an error of order 1, so it is NOT a criterion finer than '
      'the quantile that judges it',
      pin(_lim, 111.383) and pin(_se, 0.409) and pin(_eff, 44.253) and pin(_effsd, 39.792)
      and not (ORDER_BAND_MEV[0] <= _lim <= ORDER_BAND_MEV[1]) and _eff > 0.0
      and pin(_above_order, 36.91) and pin(_above_seat, 52.33)
      and _lim > R44_LIMIT_MEV and _eff > R44_EFFECTIVE_MEV
      and (SEAT_EXPECTATION_MEV[1] - SEAT_EXPECTATION_MEV[0]) > 30.0 * _se,
      '%.3f +/- %.3f meV, %.2f sigma above the order ceiling; effective %+.3f +/- %.3f meV'
      % (_lim, _se, _above_order, _eff, _effsd))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓖ⑦ᵇ  AND THE CHAINS THAT SAY SO ARE HEALTHY, SO THE FAILURE IS THE INSTRUMENT'S
_rhat = max(v['rhat'] for v in _b['diagnostics'].values())
_ess = min(v['ess'] for v in _b['diagnostics'].values())
check('Ⓖ⑦ᵇ the failure is not a sampling artefact, and that is asserted rather than assumed: '
      'worst split R-hat 1.0001 against the registered 1.05, smallest effective sample size '
      '46515 against 1000, kept-chain acceptance 0.231 and 0.232 inside the 0.03-0.70 band below '
      'which the sampler REFUSES to report.  ** The chains are healthy and the answer is wrong **',
      _rhat < 1.05 and _ess >= 1000.0 and 0.03 <= _b['accept'] <= 0.70
      and 0.03 <= _u['accept'] <= 0.70 and pin(_rhat, 1.0001) and _ess > 46000.0
      and _b['chains'] == 6 and _u['chains'] == 6,
      'R-hat %.6f, ESS %.0f, accept %.4f and %.4f on 6 chains'
      % (_rhat, _ess, _b['accept'], _u['accept']))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓗ⑧  THE ARM OF RECORD -- NOT JUDGED, ASSERTED AS SUCH
_cond = 'and only if Ⓖ⑦ passes' in PRED1
_notjudged = 'NOT JUDGED' in RESULT1 and 'P15` is not touched' in RESULT1
check('Ⓗ⑧ the arm of record is NOT JUDGED, and that is asserted against the registration and the '
      'result document rather than merely omitted: PREDICTION.md registered it "and only if Ⓖ⑦ '
      'passes", Ⓖ⑦ did not pass, and r7838 and r7844 both ruled the same way on the same '
      'condition.  Its chain ran only for the 59/64 meV placement the order asks for either way, '
      'and P15 is NOT touched',
      _cond and _notjudged and (_lim > ORDER_BAND_MEV[1] or _eff > 0.0),
      'registered conditional, condition not met, recorded NOT JUDGED in RESULT.md')

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓘ⑨  ACT DR6: BANKED, MEASURED, NOT ADDED
_npz = os.path.join(ACT, 'act_dr6_cmbonly.npz')
_fits = os.path.join(ACT, 'dr6_data_cmbonly.fits')
_banked = os.path.exists(_npz) and os.path.exists(_fits)
_f = ACTD['fisher']
_worst = min(v['sigma_sum_marginal_mev'] for v in _f.values())
_bought_best = min(v['combined_limit_mev'] for v in _f.values())   # the larger gain
_bought_worst = max(v['combined_limit_mev'] for v in _f.values())  # the smaller gain
_gain = (_lim - _bought_best, _lim - _bought_worst)
check('Ⓘ⑨ ACT DR6 CMB-only was NOT added, and the decision is MEASURED with the control\'s figure '
      'as the reason.  ** The data was already banked ** -- the DR6.02 SACC file verbatim and its '
      'extraction, 45 bandpowers each in TT, TE and EE over ell 600.5-6125.5 with a 135 x 135 '
      'covariance, since r7815+70.1 -- which is the SECOND consecutive revision in which an order '
      'offered data conditionally and the data was already in the harness.  Measured: closing the '
      'limit needs an independent sigma(Sum) of 12.765 meV; 84 of the 135 bandpowers lie wholly '
      'inside this instrument\'s reach, and a marginalised Fisher on them gives 104.1 meV, a '
      'factor 8.16 short, buying 3.56 meV of the 47.18 meV remainder.  ** Every choice in that '
      'bound OVERSTATES ACT: no calibration nuisances, the amplitude shared with Planck, and ACT '
      'treated as independent of Planck although its footprint is inside Planck\'s sky and those '
      'bandpowers sit inside the band Planck already scores here **',
      _banked and ACTD['decision'] == 'DO NOT ADD'
      and (ACTD['nuisances_included'] is False)
      and (ACTD['planck_act_sky_overlap_included'] is False)
      and ACTD['act_bandpowers_usable'] == 84 and ACTD['act_bandpowers_total'] == 135
      and pin(ACTD['sigma_required_of_an_independent_set_mev'], 12.765)
      and pin(ACTD['f_required'], 3.2738) and pin(_worst, 104.1, pc=0.001)
      and all(v['closes'] is False for v in _f.values())
      and pin(ACTD['act_usable_ell_max'], 1950.5) and pin(ACTD['act_usable_ell_min'], 600.5)
      and pin(_gain[0], 3.560, pc=0.002) and pin(_gain[1], 3.373, pc=0.002),
      '%d of %d bandpowers usable, sigma_ACT %.1f meV against the %.3f needed; the limit goes %.3f -> %.3f at best, buying %.3f-%.3f meV'
      % (ACTD['act_bandpowers_usable'], ACTD['act_bandpowers_total'], _worst,
         ACTD['sigma_required_of_an_independent_set_mev'], _lim, _bought_best,
         _gain[1], _gain[0]))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓘ⑨ᵇ  AND THE REMAINDER IS A CENTRE, NOT A WIDTH
check('Ⓘ⑨ᵇ the measurement answers a question the order did not ask: ** the control\'s shortfall '
      'is NOT a precision deficit. **  Shrinking a width moves a limit and leaves a centre exactly '
      'where it is, so at the factor 3.2738 that would close the limit the effective mass goes '
      'from 3.65 to 11.95 standard errors from the published -101 meV.  The operation that would '
      'mend one half of Ⓖ⑦ makes the other half WORSE, and no quantity of the same observable '
      'closes this',
      pin(ACTD['meff_sigma_now'], 3.65) and pin(ACTD['meff_sigma_at_f'], 11.95)
      and ACTD['meff_sigma_at_f'] > 3.0 * ACTD['meff_sigma_now']
      and pin(ACTD['meff_sigma_at_f'], ACTD['meff_sigma_now'] * ACTD['f_required'], pc=0.002),
      '%.2f sigma now, %.2f at the closing factor %.4f'
      % (ACTD['meff_sigma_now'], ACTD['meff_sigma_at_f'], ACTD['f_required']))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓙ⑩  THE SAMPLER'S GUARDS -- AND THE GUARD THAT PASSED WHAT IT WAS BUILT TO CATCH
_perdir = 'did not move across the kept chain' in SAMP
_fallback = 'FALLBACK_SD' in SAMP and 'the curvature could not be measured' in SAMP
_recorded = 'curvature_unmeasurable_in' in SAMP and 'minimum_on_a_bound' in SAMP
check('Ⓙ⑩ the control satisfies every registered guard -- but the arm of record\'s FIRST attempt '
      'exposed a hole in r7844\'s own repair, and the repair is asserted off the code.  Its '
      'unbounded minimum sits at Sum = -0.1200 eV, EXACTLY the model\'s lower bound, so the '
      'curvature probe hit the bound at once and the sum\'s proposal width came back 1.08e-08 eV: '
      'the chain could not move in the one direction the limit is read off.  ** r7844\'s refusal '
      'guard did not catch it, because it tests the AGGREGATE acceptance and the other five '
      'directions were moving at 0.303. **  The run was STOPPED rather than left to produce a '
      'number, a direction whose curvature cannot be measured now takes a STATED fallback width '
      'and is named on stdout and in the run record, and the kept chain is checked PER DIRECTION '
      'with a frozen direction refused by name',
      _perdir and _fallback and _recorded and _rhat < 1.05 and _ess >= 1000.0
      and 0.03 <= _b['accept'] <= 0.70
      and (ARM is None or ARM['cr_proposal']['minimum_on_a_bound'] is True),
      'per-direction refusal, stated fallback and the record of it all present in the sampler')

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓙ⑩ᵇ  THE SAME MISTAKE TWICE, NAMED AS SUCH
check('Ⓙ⑩ᵇ ⌗ and the pattern is named rather than buried: this is the SECOND time in two '
      'revisions that a guard this seat wrote passed something it was built to catch, and both '
      'times for the same reason -- ** the guard tested a SUMMARY of the thing rather than the '
      'thing. **  r7844\'s Ⓒ③ asserted a definition instead of the code that ran; this one '
      'asserted an average instead of the direction the result is read off.  ⌗ And the boundary is '
      'itself a finding: the arm\'s joint fit wants the sum pressed against the floor of the grid '
      'at -0.12 eV, so whatever limit it yields is set by where the grid STOPS and not by the '
      'data, which is one more reason Ⓗ⑧ stays NOT JUDGED',
      'summary of the thing rather than the thing' in RESULT1
      and 'set by where the grid stops rather than by the data' in RESULT1,
      'both named in RESULT.md, with the boundary recorded in the run')

# ─────────────────────────────────────────────────────────────────────────────────────────────────────
# ⌷  EVERY FIGURE THIS REVISION'S INDEX ROW PRINTS, PINNED TWO-SIDED AGAINST WHAT MEASURED IT
# Each tolerance is written INSIDE the coarser of half a unit in the figure's last printed digit and
# 0.05 per cent of it, as an EXPLICIT literal comparison rather than through this file's own helper,
# because a figure held only by a helper is not held where the gate can see it.  r7844's own row
# carried a `6.13` that came from a standard error TYPED beside the chain instead of read from it,
# and this is the arm that caught it.
_pins = {
    'limit': abs(_lim - 111.38) < 0.0045,
    'limit_mcse': abs(_se - 0.41) < 0.0045,
    'r7844_limit': abs(R44['lcdm_bounded']['upper95_mev'] - 99.67) < 0.0045,
    'r7844_limit_as_typed': abs(R44['lcdm_bounded']['upper95_mev'] - R44_LIMIT_MEV) < 0.0045,
    'r7844_effective': abs(R44['lcdm_unbounded']['sum_mean_ev'] * 1e3 - -7.0) < 0.045,
    'r7844_effective_as_typed':
        abs(R44['lcdm_unbounded']['sum_mean_ev'] * 1e3 - R44_EFFECTIVE_MEV) < 0.045,
    'r7844_effective_sd': abs(R44['lcdm_unbounded']['sum_sd_ev'] * 1e3 - 50.85) < 0.0045,
    'effective': abs(_eff - 44.25) < 0.0045,
    'effective_sd': abs(_effsd - 39.79) < 0.0045,
    'order_ceiling_is_the_factor_the_order_names':
        abs(ORDER_BAND_MEV[1] / PUBLISHED_LIMIT_MEV - 1.5) < 0.00045,
    'sigma_above_band': abs((_lim - ORDER_BAND_MEV[1]) / _se - 36.91) < 0.0045,
    'sigma_above_seat': abs((_lim - SEAT_EXPECTATION_MEV[1]) / _se - 52.33) < 0.0045,
    'published_limit': abs(CTRL['published']['limit_mev'] - 64.2) < 0.045,
    'published_eff': abs(CTRL['published']['effective_ev'] - -0.101) < 0.00045,
    'A1_measured': abs(GROW['A1_vs_quadrature']['max_rel'] - 0.005276) < 4.5e-07,
    'A1_isolated': abs(GROW['A1_isolation']['max_rel'] - 9.799e-09) < 4.5e-13,
    'suppression_high': abs(GROW['B2_shape']['at_high_k'] - -0.026649) < 4.5e-07,
    'asymptote': abs(GROW['C3_asymptote']['measured_on_power'] - -0.053298) < 4.5e-07,
    'textbook': abs(GROW['C3_asymptote']['textbook'] - -0.180055) < 4.5e-07,
    'asym_ratio': abs(GROW['C3_asymptote']['ratio'] - 0.296012) < 4.5e-07,
    'from_transition': abs(GROW['missing_stretch']['power_from_nr'] - -0.120083) < 4.5e-07,
    'transition_ratio': abs(GROW['missing_stretch']['ratio_from_nr_to_textbook'] - 0.666922) < 4.5e-07,
    'fraction_carried': abs(GROW['missing_stretch']['fraction_carried'] * 100.0 - 44.4) < 0.045,
    'carry_ratio_max': abs(CARRY['ratio_max'] - 0.9638) < 4.5e-05,
    'carry_ratio_min': abs(CARRY['ratio_min'] - 0.7362) < 4.5e-05,
    'radiation_188': abs(CARRY['radiation_over_matter']['z_188.1'] * 100.0 - 5.47) < 0.0045,
    'radiation_13': abs(CARRY['radiation_over_matter']['z_12.8'] * 100.0 - 0.39) < 0.0045,
    'chi2_dof_ordered': abs(CMP['carries']['z13']['chi2_per_dof'] - 2.049) < 0.00045,
    'chi2_dof_z188': abs(CMP['carries']['z188']['chi2_per_dof'] - 1.071) < 0.00045,
    'drift_ordered': abs(CMP['carries']['z13']['drift_vs_fiducial_pc'] - 49.8) < 0.045,
    'amp_held': abs(INFO['amp_held'] - 1.617967e-09) < 4.5e-16,
    'amp_preferred': abs(INFO['amp_preferred_by_bandpowers'] - 1.471643e-09) < 4.5e-16,
    'amp_ratio': abs(INFO['amp_ratio_preferred_over_cmb'] - 0.909563) < 4.5e-07,
    'sum_moves_chi2': abs(INFO['sum_moves_chi2_by'] - 94.497) < 0.00045,
    'tau_spread': abs(TAU['spread'] - 355.161) < 0.00045,
    'tau_without': abs(TAU['r7844_without_lensing'] - 1.137e-12) < 4.5e-16,
    'tau_pull': abs(TAU['pull_sigma'] - 6.79) < 0.0045,
    'act_sigma': abs(_worst - 104.1) < 0.045,
    'act_required': abs(ACTD['sigma_required_of_an_independent_set_mev'] - 12.765) < 0.00045,
    'act_shortfall': abs(_worst / ACTD['sigma_required_of_an_independent_set_mev'] - 8.16) < 0.0045,
    'act_gain': abs(_gain[0] - 3.56) < 0.0045,
    'remainder': abs(_lim - PUBLISHED_LIMIT_MEV - 47.18) < 0.0045,
    'closing_factor': abs(ACTD['f_required'] - 3.2738) < 4.5e-05,
    'meff_sigma_now': abs(ACTD['meff_sigma_now'] - 3.65) < 0.0045,
    'meff_sigma_at_f': abs(ACTD['meff_sigma_at_f'] - 11.95) < 0.0045,
    'rhat': abs(_rhat - 1.0001) < 4.5e-05,
    'ess': abs(_ess - 46515) < 0.45,
    'accept': abs(_b['accept'] - 0.231) < 0.00045,
    'placement_59': abs(_b['frac_below_0.059'] * 100.0 - 60.64) < 0.0045,
    'placement_64': abs(_b['frac_below_0.064'] * 100.0 - 65.99) < 0.0045,
}
check('⌷ every figure this revision\'s INDEX row prints is pinned TWO-SIDED here, each tolerance '
      'inside the coarser of half its last printed digit and 0.05 per cent, against the quantity '
      'that MEASURED it and not against a number retyped beside it.  ** The pins are written as '
      'explicit literal comparisons, not through this file\'s helper, because a figure held only '
      'by a helper is not held where the gate that polices the row can see it **',
      all(_pins.values()),
      '%d figure(s) pinned, from the growth, the carry, the normalisation, tau, the control, the '
      'ACT bound and the chains' % len(_pins)
      if all(_pins.values())
      else 'UNPINNED: ' + ', '.join(k for k, v in _pins.items() if not v))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓚ⑪  THE COUNT
_ran = 11
check('Ⓚ⑪ the count: this receipt adjudicates all %d registered arms, and THREE are reported '
      'FAILED or NOT JUDGED with their criteria exactly as registered -- Ⓐ① because its tolerance '
      'was finer than the accuracy of the thing it compared against, Ⓖ⑦ because adding '
      'information made the control worse, and Ⓗ⑧ because it was registered conditional on Ⓖ⑦.  '
      'A failure asserted is not a failure suffered' % _ran,
      _ran == 11 and PRED.count('**Ⓚ⑪') == 1 and PRED.count('**Ⓘ⑨') == 1,
      '%d arm-check(s) failed' % len(fail))

print()
if not fail:
    print('  r7848 OK -- every arm holds, and the registered failures are ASSERTED rather than '
          'suffered:')
    print('    => Ⓐ①: the ODE is the growth equation; the quadrature it was judged against is '
          'used outside its own stated validity, and agrees to 9.8e-09 when it is not.')
    print('    => Ⓖ⑦: %.2f +/- %.2f meV and %+.1f meV, so MORE information made the control '
          'WORSE on both halves.' % (_lim, _se, _eff))
    print('    => Ⓘ⑨: ACT DR6 is banked; an over-generous bound on it buys %.2f meV of the %.2f '
          'meV remainder, and the remainder is a centre and not a width.'
          % (_gain[0], _lim - PUBLISHED_LIMIT_MEV))
    print('    => Ⓗ⑧: NOT JUDGED, as registered.  P15 is not touched.')
    sys.exit(0)
print('  ⛔ %d arm(s) failed: %s' % (len(fail), fail))
sys.exit(1)
