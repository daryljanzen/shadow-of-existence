#!/usr/bin/env python3
r"""RECEIPT -- P15 (r7838, node 60): ** THE LENSING OPERATOR NOW MOVES WITH THE SUM, THE PROFILE IS A
CONVERGED SAMPLER, AND THE RULER IS MARGINALISED OVER A BRACKET THAT NO LONGER BINDS -- SO EVERY
DEFECT r7836 NAMED OR THIS REVISION FOUND IS CLOSED, THE CONTROL'S MATTER-DENSITY GAP NOW TAKES THE
PUBLISHED SIGN, AND THE CONTROL'S LIMIT IS STILL A FACTOR FOUR TOO LOOSE.  WHAT THE HARNESS LACKS IS
DATA, NOT PHYSICS. **

COMPUTES: the lensing operator's response to the sum, in the fit's own convention and in the one
  r7836's figure was measured in; the interpolation error of the sum direction; the two arms' 95 per
  cent limits, effective masses, matter-density gaps and convergence diagnostics, read from this
  revision's own runs; and the size of three defects of the borrowed harness.  ** It pins NO
  cosmological parameter as a result.  The headline is that an apparatus was repaired, converged, and
  still fails its own control -- so nothing is concluded about the neutrino mass on either arm. **

THE ORDER (r7833, 69, restated unchanged at r7835): ① recompute the CAMB lensing ratio at each trial
sum on the control and carry the construction's own lensing response the same way on the arm of
record, showing the control's lensing change against CAMB's 0.372 per cent at Sum = 0.06 eV and 0.768
at 0.12, peaking near l = 1980; ② replace the profile with a sampler and show convergence; ③ the
control first, landing near the published effective mass of -0.101 eV and 95 per cent limit of 64.2
meV before the arm is read; ④ then the arm, with the limit and where 59 and 64 meV sit on it.
PREDICTION.md was committed and pushed BEFORE any run, at `ff5463ba2`, with eight arms.

** THE SHAPE OF THE RESULT. **
  Ⓔ⑤, the decisive arm, FAILS: the control's 95 per cent upper limit is 277.7 meV against the
  published 64.2, outside the registered 42.8-to-96.3 band, and its effective mass is POSITIVE where
  the published one is negative.  It is reported as failed, with the criterion exactly as registered.
  So Ⓖ⑦, the arm of record, is NOT JUDGED -- its registered DIRECTION holds, the arm being looser
  than the control, but a direction read off an apparatus that misses its own control is not a result.

  Ⓕ⑥ PASSES, and it is the half r7836 called decisive: the gap is +3.70 per cent against the
  published +2.48, the published SIGN, where r7836's was -2.43.  The arm's gap comes out -1.11 per
  cent against 72's banked estimate of -1.00, where r7836's apparatus gave -5.21.

** AND THE LOOSENESS IS LOCATED RATHER THAN LISTED. **  Holding the ruler at the instrument's own
sound horizon instead of marginalising it moves the limit five per cent.  So it is not the operator,
not the minimiser and not the ruler: what is left is WHAT this harness scores -- 185 temperature
bins, no polarisation, no lensing reconstruction, no low-l.  (r7842: the lensing bandpowers ARE
banked -- see the amendment below.  This harness still does not SCORE them, which is what this
sentence turns on, and the reason is the instrument and not the repository.)

⌗ ** AMENDED AT r7842 UNDER THE r2673 RULE -- THE FINDING STANDS AND ONE OF ITS REASONS WAS WRONG. **
This receipt's diagnosis, that what the harness lacks is DATA and not physics, named the
lensing-reconstruction spectrum as a measurement the repository does not hold.  *It holds it.*  The
nine Planck 2018 conservative `C_L^phiphi` bandpowers, their covariance and their nine windows have
been in `computations/beyond_the_wall/r7471_70_PO24_tilt_off_the_tail/lensing/` since node 70 banked
them, and 70 scored against them there.  r7842 found this while writing a gate that ASSERTS the
absence, and its `lensing_reach.py` then measured why the data still cannot be used from this seat:
at fixed total Omega_m this instrument's background rate is EXACTLY independent of the sum --
0.000e+00 across four decades of scale factor -- so the background-only growth factor that
`L171x_lensing_potential.py` builds carries exactly zero neutrino effect, and the one channel that
does respond is a Poisson source flat in k and frozen at z = 12.8.
  ⇒ ** EVERY FIGURE AND EVERY ARM BELOW IS UNCHANGED, and so is the finding: the looseness is in
    WHAT this harness scores. **  What changes is one clause of the reason.  It is not that the
    lensing measurement is missing; it is that this instrument cannot carry a neutrino effect into
    the lensing power it computes.  That is an instrument extension and not a data request, which
    makes it a different order from the one r7841 wrote on the strength of this sentence.

rc=0 when every arm holds, including the arms that record a registered failure AS a failure.
Run: python3 <this file>                                                        (numpy only)
"""
import io
import json
import os
import re
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
RUN = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                   'r7838_60_the_lensing_operator_moves_with_the_sum_and_the_profile_becomes_a_sampler')

PUBLISHED_LIMIT_MEV = 64.2          # arXiv:2503.14744, the standard-model 95 per cent upper limit
PUBLISHED_EFFECTIVE_EV = -0.101     # its effective mass, the sum free to go negative
PUBLISHED_GAP_PC = 2.48             # its CMB-above-distances matter-density gap
BANKED_ARM_GAP_PC = -1.00           # 72's banked estimate for the arm of record

fail = []


def check(label, ok, witness=''):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}" + (f"   ({witness})" if witness else ''))
    if not ok:
        fail.append(label)


def jload(name):
    with io.open(os.path.join(RUN, name), encoding='utf-8') as fh:
        return json.load(fh)


S = jload('sampler.json')                 # both arms, the registered configuration
S_HELD = jload('sampler_held_ruler.json')  # the control with r_d held, the decomposition
S_CAP = jload('sampler_cap030.json')      # the control before the range was doubled
CONV = jload('conventions.json')['conventions']
EFF = jload('operator_effect.json')
RESULT = io.open(os.path.join(RUN, 'RESULT.md'), encoding='utf-8').read()

print('r7838 (60) -- the rebuilt harness, read from its own runs\n')

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓐ①  THE OPERATOR'S RESPONSE, IN BOTH CONVENTIONS -- and r7836's figure reproduced in ITS OWN
#      ⌗ The registered arm asked for r7836's 0.372 and 0.768 "peaking at l ~ 1980".  The rebuild in
#        the FIT's convention does not give them.  Each convention that could have was measured; one
#        does, to the printed digits.  BOTH are pinned here, because the whole point of the arm is
#        that a figure quoted for a signature has to say which convention it was measured in.
R7836 = CONV['omch2_held_camb_default_split']
FITC = CONV['fit_convention_total_held_three_degenerate']
a6, a12 = R7836['0.06|30-2000'], R7836['0.12|30-2000']
f6, f12 = FITC['0.06|30-2000'], FITC['0.12|30-2000']
print('PART 1 -- THE OPERATOR, AND WHICH CONVENTION A FIGURE WAS MEASURED IN')
print('  r7836\'s convention (CAMB default split, omch2 held, l = 30-2000): '
      '%.4f per cent at l = %d and %.4f at l = %d'
      % (a6['pct'], a6['peak_l'], a12['pct'], a12['peak_l']))
print('  the FIT\'s convention (total held, three degenerate):               '
      '%.4f per cent at l = %d and %.4f at l = %d'
      % (f6['pct'], f6['peak_l'], f12['pct'], f12['peak_l']))
check('Ⓐ① r7836\'s 0.372 and 0.768 "peaking at l ~ 1980" are REPRODUCED, to the printed digits, in '
      'the convention they were measured in -- CAMB\'s default one-massive split with omch2 held, on '
      'the window the arms\' spectra reach',
      abs(a6['pct'] - 0.3717) < 0.00017 and abs(a12['pct'] - 0.7681) < 0.00035
      and 1900 <= a6['peak_l'] <= 2060 and 1900 <= a12['peak_l'] <= 2060
      and abs(round(a6['pct'], 3) - 0.372) < 1e-9 and abs(round(a12['pct'], 3) - 0.768) < 1e-9,
      '%.4f at l=%d, %.4f at l=%d' % (a6['pct'], a6['peak_l'], a12['pct'], a12['peak_l']))
check('Ⓐ①ᵇ and in the convention the FIT ACTUALLY RUNS ON the same signature is 0.1896 and 0.4541, '
      'peaking at l = 1967 -- so r7836\'s figure is a factor 1.96 too large at 0.06 eV for the fit '
      'it was quoted about, and "the same order as the retained 0.84 per cent lever" overstates it',
      abs(f6['pct'] - 0.1896) < 0.00009 and abs(f12['pct'] - 0.4541) < 0.00022
      and f6['peak_l'] == 1967 and abs(a6['pct'] / f6['pct'] - 1.96) < 0.0045,
      'factor %.4f' % (a6['pct'] / f6['pct']))

# Ⓑ②  the response is monotone across the whole scan
GRID = np.load(os.path.join(RUN, 'ratio_grid.npz'))
_ls, _g, _R = GRID['ls'], GRID['grid'], GRID['ratio']
_w = (_ls >= 30) & (_ls <= 2000) & (_R[0] > 0)
_resp = [100.0 * float(np.max(np.abs(_R[i][_w] / _R[0][_w] - 1.0))) for i in range(len(_g))]
check('Ⓑ② the operator\'s response is STRICTLY INCREASING in the sum across the whole scan, 0.1896 '
      'per cent at 0.06 eV to 2.4034 at 0.60, on 21 generated nodes',
      len(_g) == 21 and float(_g[-1]) == 0.6
      and all(b > a for a, b in zip(_resp, _resp[1:]))
      and abs(_resp[-1] - 2.4034) < 0.0012,
      '%d nodes, last %.4f per cent' % (len(_g), _resp[-1]))

# Ⓒ③  the interpolation is not the limiting error -- leave-one-out AND an off-grid rebuild
_loo = max(max(v['max_over_sigma'] for v in EFF[a]['leave_one_out'].values()) for a in ('cr', 'lcdm'))
_off = max(EFF[a]['off_grid']['max_over_sigma'] for a in ('cr', 'lcdm'))
check('Ⓒ③ the sum direction\'s interpolation is nowhere near the limiting error: leave-one-out at '
      'every interior node and a spectrum GENERATED at the off-grid sum of 0.21 eV both agree with '
      'the interpolated model to under a thousandth of the smallest bin uncertainty, against the '
      'tenth that was registered',
      _loo < 1e-3 and _off < 1e-3 and all(EFF[a]['off_grid']['sum_ev'] == 0.21 for a in ('cr', 'lcdm')),
      'leave-one-out %.3e, off-grid %.3e, in units of the bin sigma' % (_loo, _off))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
print('\nPART 2 -- THE SAMPLER, AND WHAT IT MEASURED')
CB, CU = S['lcdm_bounded'], S['lcdm_unbounded']
AB, AU = S['cr_bounded'], S['cr_unbounded']
_rh = max(max(v['rhat'] for v in d['diagnostics'].values()) for d in (CB, CU, AB, AU))
_es = min(min(v['ess'] for v in d['diagnostics'].values()) for d in (CB, CU, AB, AU))
check('Ⓓ④ THE SAMPLER CONVERGES, on six chains with the proposal held after a staged burn-in: the '
      'worst split R-hat over four runs and five parameters is 1.0012 against the registered 1.05, '
      'and the smallest effective sample size is 9301 against the registered 1000',
      _rh < 1.05 and _es >= 1000 and abs(_rh - 1.0012) < 0.00045 and round(_es) == 9301
      and all(d['chains'] == 6 for d in (CB, CU, AB, AU)),
      'R-hat %.5f, ESS %d' % (_rh, _es))

lim_c, lim_a = CB['upper95_mev'], AB['upper95_mev']
fac_c, fac_a = lim_c / PUBLISHED_LIMIT_MEV, lim_a / PUBLISHED_LIMIT_MEV
eff_c, eff_a = CU['sum_mean_ev'] * 1000.0, AU['sum_mean_ev'] * 1000.0
sd_c, sd_a = CU['sum_sd_ev'] * 1000.0, AU['sum_sd_ev'] * 1000.0
print('  control:       limit %.1f meV (factor %.2f), effective mass %+.1f +/- %.1f meV, gap %+.2f pc'
      % (lim_c, fac_c, eff_c, sd_c, CB['gap_mean_pc']))
print('  arm of record: limit %.1f meV (factor %.2f), effective mass %+.1f +/- %.1f meV, gap %+.2f pc'
      % (lim_a, fac_a, eff_a, sd_a, AB['gap_mean_pc']))

check('Ⓔ⑤ FAILS AS REGISTERED, and is reported as failed with the criterion unchanged: the control\'s '
      '95 per cent limit is 277.7 meV against the published 64.2 -- a factor 4.33, OUTSIDE the '
      'registered 42.8 to 96.3 band -- and its effective mass is +67.5 meV, POSITIVE where the '
      'published one is -0.101 eV.  r7836 missed the same limit by 2.42 the other way',
      abs(lim_c - 277.7) < 0.045 and abs(fac_c - 4.33) < 0.0045
      and not (42.8 <= lim_c <= 96.3)
      and abs(eff_c - 67.5) < 0.045 and abs(sd_c - 106.0) < 0.045
      and eff_c > 0 and PUBLISHED_EFFECTIVE_EV < 0,
      '%.1f meV, factor %.2f, effective mass %+.1f' % (lim_c, fac_c, eff_c))

check('Ⓕ⑥ PASSES, and it is the half r7836 called decisive: the control\'s matter-density gap is '
      '+3.70 per cent against the published +2.48 -- the PUBLISHED SIGN -- where r7836\'s came out '
      '-2.43.  And the arm\'s gap is -1.11 per cent against 72\'s banked -1.00, where r7836\'s '
      'apparatus gave -5.21',
      CB['gap_mean_pc'] > 0 and PUBLISHED_GAP_PC > 0
      and abs(CB['gap_mean_pc'] - 3.70) < 0.0045
      and abs(AB['gap_mean_pc'] - (-1.11)) < 0.0045
      and abs(AB['gap_mean_pc'] - BANKED_ARM_GAP_PC) < 0.15,
      'control %+.2f, arm %+.2f, published %+.2f' % (CB['gap_mean_pc'], AB['gap_mean_pc'],
                                                     PUBLISHED_GAP_PC))

check('Ⓖ⑦ NOT JUDGED, and the receipt asserts that rather than reporting the arm\'s number as a '
      'limit: its registered DIRECTION holds -- the arm\'s 304.1 meV is LOOSER than the control\'s '
      '277.7 -- but Ⓔ⑤ failed, so the precondition for reading the arm was never met.  Where the '
      'order\'s two values sit is reported: 29.0 per cent of the arm\'s posterior lies below 59 meV '
      'and 31.4 per cent below 64',
      abs(lim_a - 304.1) < 0.049 and lim_a > lim_c
      and abs(100.0 * AB['frac_below_0.059'] - 29.0) < 0.045
      and abs(100.0 * AB['frac_below_0.064'] - 31.4) < 0.045
      and 'NOT JUDGED' in RESULT and 'NOT reported as a limit' in RESULT,
      '%.1f meV against the control\'s %.1f; %.1f and %.1f per cent below the two values'
      % (lim_a, lim_c, 100.0 * AB['frac_below_0.059'], 100.0 * AB['frac_below_0.064']))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
print('\nPART 3 -- WHERE THE LOOSENESS IS, DECOMPOSED RATHER THAN LISTED')
_held = S_HELD['lcdm_bounded']['upper95_mev']
_cap = S_CAP['lcdm_bounded']['upper95_mev']
check('Ⓘ⑨ the limit is the DATA\'s and not the grid edge\'s: doubling the sum\'s range from 0.30 to '
      '0.60 eV moved the 95 per cent point from 245.9 to 277.7 meV, 12.9 per cent, where a '
      'prior-dominated posterior would have tracked the ceiling',
      abs(_cap - 245.9) < 0.049 and abs(100.0 * (lim_c / _cap - 1.0) - 12.9) < 0.045
      and (lim_c / _cap - 1.0) < 0.5,
      '%.1f -> %.1f meV, a rise of %.1f per cent on a doubled ceiling'
      % (_cap, lim_c, 100.0 * (lim_c / _cap - 1.0)))
check('Ⓙ⑩ and it is NOT the ruler: holding r_d at the instrument\'s own sound horizon instead of '
      'marginalising it gives 262.9 meV, 5.3 per cent tighter, against a factor 4.33 to explain.  '
      'So what is left is WHAT the harness scores -- 185 temperature bins, no polarisation, no '
      'lensing reconstruction, no low-l -- and that is what the next revision has to change.  '
      '(r7842, r2673: the lensing bandpowers are banked at r7471+70 and this harness still does '
      'not score them; the obstruction is the instrument, not the repository.)',
      abs(_held - 262.9) < 0.045 and abs(100.0 * (1.0 - _held / lim_c) - 5.3) < 0.045
      and (1.0 - _held / lim_c) < 0.25,
      '%.1f meV held against %.1f marginalised, %.1f per cent' % (_held, lim_c,
                                                                  100.0 * (1.0 - _held / lim_c)))

print('\nPART 4 -- THREE DEFECTS OF THE BORROWED HARNESS, EACH MEASURED HERE')
_d_arm = EFF['cr']['per_sum']['+0.30']['difference']
_d_ctl = EFF['lcdm']['per_sum']['+0.30']['difference']
check('Ⓚ⑪ r7836\'s NAMED CAUSE RUNS THE WRONG WAY.  It named the frozen operator as the reason its '
      'limit came out too TIGHT; freezing the operator at 0.06 eV LOWERS chi^2 at a sum of 0.30 eV, '
      'by 7.931 on the arm of record and 5.003 on the control, so the frozen harness prefers large '
      'sums MORE than the honest one and its limit is too LOOSE on that account',
      _d_arm > 0 and _d_ctl > 0
      and abs(_d_arm - 7.931) < 0.0038 and abs(_d_ctl - 5.003) < 0.0025
      and abs(EFF['cr']['per_sum']['+0.06']['difference']) < 1e-9,
      'moving minus frozen: %+.3f on the arm, %+.3f on the control' % (_d_arm, _d_ctl))

_tc, _ta = S['lcdm_bao']['truncation'], S['cr_bao']['truncation']
check('Ⓛ⑫ THE RULER WAS PINNED, NOT MARGINALISED.  r7836 minimised r_d inside (120, 170); over the '
      'region the fit explores that bracket BINDS at 78 of 441 box points on the control and 77 of '
      '441 on the arm -- about 17.6 per cent -- adding up to 3113 and 3230 in chi^2 where it binds.  '
      'A bound that binds is not a marginalisation',
      _tc['bound'] == 78 and _ta['bound'] == 77 and _tc['points'] == 441 and _ta['points'] == 441
      and abs(_tc['worst_chi2_added'] - 3113.0) < 0.45
      and abs(_ta['worst_chi2_added'] - 3230.0) < 0.45,
      '%d and %d of %d points, worst %.1f and %.1f in chi^2'
      % (_tc['bound'], _ta['bound'], _tc['points'], _tc['worst_chi2_added'],
         _ta['worst_chi2_added']))

_mdl = io.open(os.path.join(RUN, 'model.py'), encoding='utf-8').read()
check('Ⓜ⑬ AND THE BAO TERM IS ONE-DIMENSIONAL, which is where the degeneracy r7836 orthogonalised '
      'against comes FROM: with r_d minimised the control\'s BAO chi^2 is exactly independent of H0, '
      'because the ruler rescales to absorb it, so a one-dimensional term in Omega_m is the only '
      'thing paying for a moved total.  Read from the instrument that acts on it, not recalled',
      'EXACTLY independent of `H0`' in _mdl and 'RD_BOUNDS = (100.0, 220.0)' in _mdl
      and 'RD_BORROWED = (120.0, 170.0)' in _mdl,
      'the widened bracket and the measured flatness are both in the instrument\'s own source')

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# ⌗ r7836's OWN TWO FIGURES, which the sentences above print beside THIS receipt, are pinned here
#   two-sided -- and READ OUT OF r7836's own stored run rather than retyped, so that if that run is
#   ever regenerated differently the comparison fails instead of agreeing with a literal.  The
#   published limit is pinned two-sided as well, because a sentence that prints it beside this
#   receipt is a sentence this receipt has to be able to fail on.
_R36 = jload(os.path.join(os.pardir, 'r7836_60_the_arm_of_record_refitted_with_the_neutrino_mass_free',
                          'fit_mnu.json')) if False else json.load(io.open(
    os.path.join(ROOT, 'computations', 'beyond_the_wall',
                 'r7836_60_the_arm_of_record_refitted_with_the_neutrino_mass_free', 'fit_mnu.json'),
    encoding='utf-8'))


def _gap_pc(jm, h0_d, om_d):
    h = jm['H0'] / 100.0
    return 100.0 * ((jm['OM'] * h ** 2) / (om_d * (h0_d / 100.0) ** 2) - 1.0)


_r36_ctl_limit = _R36['lcdm']['upper95'] * 1000.0
_r36_arm_gap = _gap_pc(_R36['cr']['joint_min'], 68.60, 0.2973)
_r36_ctl_gap = _gap_pc(_R36['lcdm']['joint_min'], 68.5, 0.2975)
check('Ⓠ⑰ the figures of r7836 that these sentences print are pinned two-sided and READ OUT OF '
      'r7836\'s own stored run rather than retyped: its control limit 26.5 meV and its arm gap '
      '-5.21 per cent, and its control gap -2.43.  And the published limit 64.2 meV is pinned '
      'here too, because a sentence '
      'printing it beside this receipt is one this receipt has to be able to fail on',
      abs(_r36_ctl_limit - 26.5) < 0.045
      and abs(_r36_arm_gap - (-5.21)) < 0.0048
      and abs(_r36_ctl_gap - (-2.43)) < 0.0045
      and abs(PUBLISHED_LIMIT_MEV - 64.2) < 0.045
      and abs(PUBLISHED_GAP_PC - 2.48) < 0.0045
      and abs(PUBLISHED_EFFECTIVE_EV - (-0.101)) < 0.00045
      and abs(BANKED_ARM_GAP_PC - (-1.00)) < 0.0045,
      'r7836 read back at %.1f meV, arm gap %+.2f, control gap %+.2f per cent'
      % (_r36_ctl_limit, _r36_arm_gap, _r36_ctl_gap))

print('\nPART 5 -- THIS REVISION\'S OWN CAUGHT DEFECT, AND THE COUNT')
_smp = io.open(os.path.join(RUN, 'sampler.py'), encoding='utf-8').read()
check('Ⓝ⑭ this revision\'s FIRST sampler had the same class of failure r7836 reported, and a smoke '
      'test caught it before any number was read: Powell walked into the flat penalty region and '
      'reported the plateau as a minimum where Nelder-Mead reached 190.6 on the same tree.  The '
      'infeasible region is sloped now, a barrier result is DISCARDED rather than reported, and the '
      'reported minimum is asserted to be the objective at its own point',
      'chi2_barrier' in _mdl and 'the plateau refused' in _smp
      and 'the reported minimum is not the objective at its point' in _smp
      and abs(AB['best_fit']['chi2'] - 190.61) < 0.0045
      and all(d['best_fit']['chi2'] < 1e5 for d in (CB, CU, AB, AU)),
      'the arm\'s minimum is %.2f, not a barrier value' % AB['best_fit']['chi2'])

check('Ⓞ⑮ P15 is UNCHANGED by this revision, as the order requires until the arm is read',
      'P15` is unchanged' in RESULT)

ARMS_RUN = 16
# ** THE REGISTERED FAILURE IS ASSERTED, NOT SUFFERED. **  Ⓔ⑤ was registered as a comparison with a
#   reachable negative and the negative was reached.  So the arm that carries it PASSES by asserting
#   that the control missed the published limit, outside the band registered before the run, with the
#   effective mass on the wrong side of zero -- and the receipt has no failing arm at all.  A receipt
#   that merely exited nonzero would say "something broke"; this one says WHICH comparison came out
#   which way, which is the thing the corpus has to be able to read.
check('Ⓟ⑱ the count: this receipt ran %d arms and every one of them holds, the registered FAILURE '
      'among them -- Ⓔ⑤ asserts that the control missed its band, and Ⓖ⑦ asserts that the arm of '
      'record is therefore NOT JUDGED' % (ARMS_RUN + 1),
      len(fail) == 0,
      '%d arm(s) failed' % len(fail))

print()
if not fail:
    print('  r7838 OK -- every arm holds, and the registered failure is ASSERTED rather than '
          'suffered:')
    print('    the control\'s limit is %.1f meV against the published %.1f, a factor %.2f, with a '
          'POSITIVE effective mass where the published one is negative.' % (lim_c,
                                                                            PUBLISHED_LIMIT_MEV,
                                                                            fac_c))
    print('    => the arm of record is NOT JUDGED, and nothing is concluded about the neutrino mass '
          'on either arm.')
    print('    => what is owed is polarisation and the lensing-reconstruction spectrum, which '
          'this harness does not score.')
    print('    => r7842 amendment (r2673): the lensing bandpowers ARE banked, at r7471+70.  So the '
          'second half is owed to the INSTRUMENT and not to the repository -- its background rate '
          'is exactly independent of the sum, so the growth it builds carries no neutrino effect.')
    sys.exit(0)
print('  ⛔ %d arm(s) failed: %s' % (len(fail), fail))
sys.exit(1)
