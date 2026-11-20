#!/usr/bin/env python3
r"""RECEIPT -- P15 (r7844, node 60): ** POLARISATION IS IN THE SCORE AND THE EXTENSION IS EXACT ON
THE OLD BINS; THE LENSING MEASUREMENT THE ORDER ASKED THIS SEAT TO FETCH HAS BEEN BANKED SINCE
r7471 AND THE OBSTRUCTION IS THE INSTRUMENT, WHOSE BACKGROUND RATE IS EXACTLY INDEPENDENT OF THE
SUM; AND TWO REGISTERED ARMS FAIL -- ONE BECAUSE ITS PREMISE WAS FALSE AND ONE BECAUSE ITS
TOLERANCE WAS TIGHTER THAN THE INSTRUMENT IT JUDGES. **

COMPUTES: the three-spectrum score over 555 bins and its exact closure on the 185-bin temperature
  score; the polarisation outputs' sanity on both arms; the Monte-Carlo error of a posterior
  quantile this seat had been reading to a tenth of a meV; the mis-scaling of the sampler's
  proposal and the repair; tau's reach in this harness; and the exact reach of the neutrino sum
  into this instrument's background and its clustering source.  ** It pins NO cosmological parameter
  as a result. **

⌷ ** THE ID. **  69 ordered this work as "finish r7842" and its commits carry that number,
which is also the name of its computation directory and of the PREDICTION.md registered at
`4e7aa1721`.  It LANDS as r7844, because the trunk's front advanced to 69's own r7843 while it
was running, and this line's next id of its own parity above the front is r7844.  *Same work,
same registration, one number higher than the order names, and said here so that nobody has to
reconstruct it.*

THE ORDER (r7841, 69, restated unchanged at r7843): ① add polarisation to the score, TE and EE on
the same bandpower and covariance treatment as TT, from POLSAVE on both arms; ② add the
lensing-reconstruction spectrum with its covariance; ③ add the low-l and optical-depth information
the published fit carries, or a tau prior equivalent to it, and SAY WHICH; ④ the control first, near
64.2 meV and an effective mass near -0.101 eV, before the arm is read.  PREDICTION.md was committed
and pushed BEFORE any run, at `4e7aa1721`, with ten arms.

** THE SHAPE OF THE RESULT -- TWO ARMS FAIL AND BOTH FAILURES ARE INFORMATIVE. **

  Ⓗ⑧ FAILS EXACTLY AS ITS OWN REACHABLE NEGATIVE DESCRIBED.  The arm asserted, from the repository,
  that no lensing bandpowers and no lensing covariance are banked, and named its own refutation:
  *"finding them banked, in which case the arm is wrong and item ② is runnable."*  They are banked.
  Nine Planck 2018 conservative `C_L^phiphi` bandpowers over `L = 8`-`400`, a `9 x 9` covariance and
  nine windows have been in `r7471_70_PO24_tilt_off_the_tail/lensing/` since node 70 put them there,
  and 70 scored against them.  ** TWO SEATS CARRIED THE CLAIM THAT THE MEASUREMENT WAS MISSING --
  r7838's receipt and r7841's order, which was written on r7838's sentence -- AND NEITHER HAD
  LOOKED. **  Nor did this one find it by looking: it surfaced while writing a gate that ASSERTS the
  absence, which is why `check_data_absent.py` exists and why its first act was to delete one of its
  own rows.

  Ⓑ② FAILS ON ITS LIMIT HALF, AND THE CRITERION IS THE DEFECT.  Its chi^2 half holds identically.
  Its named negative -- that the extension changed the TT scoring -- is ruled out by measurement and
  not by argument: spectra bit-identical, node set identical, operator bit-identical, Fisher
  bit-identical, chi^2 agreeing to 4.1e-12 over 200 points.  What moved is a posterior quantile read
  off a finite chain, whose own Monte-Carlo standard error is about 1.7 meV, against a tolerance I
  registered at 1.  ** A WINDOW THAT NARROW COULD NOT HAVE BEEN MET BY A RERUN OF r7838's OWN CODE
  AGAINST ITSELF. **  Three realisations of the one posterior read 277.7, 275.3 and 277.7 meV; the
  third is in the record BECAUSE it passes, so that the failing run cannot be quietly replaced by
  the passing one.

** AND ITEM ② IS NOT BLOCKED ON DATA AFTER ALL, WHICH IS THE FINDING THAT MATTERS FOR THE NEXT
ORDER. **  At fixed total Omega_m this instrument's background rate is EXACTLY independent of the
neutrino sum -- 0.000e+00, not nearly -- because ACOUSTIC_two_arm holds Omega_m as the TOTAL by
design.  `L171x_lensing_potential.py` builds its lensing potential on a growth factor made from that
rate, so ** the growth it carries responds to the sum by exactly nothing **, and the lensing kernel
peaks at `z ~ 3.3`, entirely downstream of the `z = 12.8` where the k-dependence is frozen.  The one
channel that does respond is the Poisson source, flat in k and frozen at that same redshift.  So the
gap is a scale-dependent growth: an instrument extension, not a measurement.  ** THIS RECEIPT DOES
NOT SAY HOW LARGE THE MISSING PART IS. **  The textbook asymptote is -8 f_nu and this harness has
not produced it; printing it here would be borrowing a result.

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
                   'r7842_60_polarisation_added_to_the_score_and_the_two_data_the_harness_'
                   'does_not_have')
LENS = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                    'r7471_70_PO24_tilt_off_the_tail', 'lensing')

PUBLISHED_LIMIT_MEV = 64.2          # arXiv:2503.14744, the standard-model 95 per cent upper limit
PUBLISHED_EFFECTIVE_EV = -0.101     # its effective mass, the sum free to go negative
ORDER_BAND_MEV = (42.8, 96.3)       # the order's factor-1.5 window on the published limit
SEAT_EXPECTATION_MEV = (100.0, 250.0)   # this seat's own registered expectation, falsifiable
R38_LIMIT_MEV = 277.7               # r7838's control, which Ⓑ② closes against
R38_CHI2 = 194.57

fail = []


def check(label, ok, witness=''):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}" + (f"   ({witness})" if witness else ''))
    if not ok:
        fail.append(label)


def jload(name, where=RUN):
    with io.open(os.path.join(where, name), encoding='utf-8') as fh:
        return json.load(fh)


CLO = jload('closure_tt.json')        # the TT-only closure, and the quantile's own error
POL = jload('pol_sanity.json')        # the polarisation outputs
TAU = jload('tau_reach.json')         # tau's reach
REACH = jload('lensing_reach.json')   # what the sum reaches in the background and the source
SCORE = io.open(os.path.join(RUN, 'score_ttteee.py'), encoding='utf-8').read()
MODEL = io.open(os.path.join(RUN, 'model3.py'), encoding='utf-8').read()
SAMP = io.open(os.path.join(RUN, 'sampler3.py'), encoding='utf-8').read()
PRED = io.open(os.path.join(RUN, 'PREDICTION.md'), encoding='utf-8').read()

_POLRUN = os.path.join(RUN, 'sampler3_lcdm_pol.json')
PR = jload('sampler3_lcdm_pol.json') if os.path.exists(_POLRUN) else None
_ARMRUN = os.path.join(RUN, 'sampler3_cr_pol.json')
AR = jload('sampler3_cr_pol.json') if os.path.exists(_ARMRUN) else None

print('r7844 (60), ordered as r7842 -- polarisation in the score, read from this '
      'revision\'s own runs\n')


def pin(x, printed, pc=0.0005):
    """the pin rule: the allowance is the COARSER of half a unit in the last printed digit and
    0.05 per cent of |X|, and a tolerance is written INSIDE that bound, never at it"""
    s = f'{printed}'
    dec = len(s.split('.')[1]) if '.' in s else 0
    half = 0.5 * 10 ** (-dec)
    return abs(float(x) - float(printed)) <= max(half, pc * abs(float(printed))) * 0.9


# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓐ①  THE POLARISATION OUTPUTS ARE WHAT THEIR OWN DOCSTRING SAYS
_arms = POL['arms_present']
_ok = bool(_arms) and all(
    POL[a]['axis_shared'] and POL[a]['ee_positive'] and POL[a]['te_changes_sign']
    and POL[a]['ee_peak_in_band'] and POL[a]['tt_peak_in_band'] and POL[a]['ee_peak_below_tt']
    for a in _arms)
check('Ⓐ① both arms\' POLSAVE outputs sit on TT\'s own multipole axis; EE is positive everywhere it '
      'is scored, TE CHANGES SIGN, and EE\'s first acoustic maximum falls in 120-160 where TT\'s '
      'falls in 190-250 -- so the E-mode kernel does what its docstring says',
      _ok and POL['both_arms'],
      '; '.join(f"{a}: EE>0 min {POL[a]['ee_min_on_scored']:.3g}, TE crosses "
                f"{POL[a]['te_sign_changes']}x, EE peak l={POL[a]['ee_first_max']:.0f}, "
                f"TT peak l={POL[a]['tt_first_max']:.0f}" for a in _arms))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓑ②  THE CLOSURE: THE chi^2 HALF HOLDS, THE LIMIT HALF DOES NOT, AND THE TOLERANCE IS THE DEFECT
_c = CLO['chains']
_dchi2min = abs(_c['chi2min_r7842'] - _c['chi2min_r7838'])
check('Ⓑ② the chi^2 half HOLDS: scored on TT alone the extended harness returns r7838\'s own '
      'minimum to every printed digit, and inside the registered 0.05.  ** THE TEST IS NOT '
      'BITWISE EQUALITY **, because the two minima differ in their last two digits for exactly the '
      'reason this arm\'s own negative was ruled out by -- summation order over a masked '
      '613-vector against a 185-vector.  Asserting bitwise here would have been asserting the '
      'opposite of what was measured',
      abs(_c['chi2min_r7842'] - R38_CHI2) <= 0.045 and _dchi2min < 1e-10
      and f"{_c['chi2min_r7842']:.6f}" == f"{_c['chi2min_r7838']:.6f}",
      f"{_c['chi2min_r7842']:.6f} both, {_dchi2min:.3e} apart, and "
      f"{CLO['chi2']['at_best_fit']['abs_diff']:.3e} apart at r7838's recorded best fit")

check('Ⓑ② its REACHABLE NEGATIVE is ruled out by measurement: the extension did NOT change the TT '
      'scoring.  Direction spectra bit-identical, sum node set identical, TT operator '
      'bit-identical, Fisher matrix bit-identical, and the two models\' chi^2 agreeing to the last '
      'few bits -- summation order over a masked 613-vector against a 185-vector, nothing more',
      CLO['verdict']['scoring_unchanged'] and CLO['directions_max_rel'] == 0.0
      and CLO['fisher']['bitwise'] and CLO['operator']['bitwise'] and CLO['nodes']['identical']
      and CLO['chi2']['max_abs'] < 1e-10,
      f"max |dchi^2| = {CLO['chi2']['max_abs']:.3e} over {CLO['chi2']['points']} points, median "
      f"{CLO['chi2']['median_abs']:.3e}, bitwise equal at {CLO['chi2']['bitwise_equal']}")

check('Ⓑ② THE LIMIT HALF IS REPORTED FAILED WITH THE CRITERION EXACTLY AS REGISTERED -- 275.3 meV '
      'against 277.7, outside the 1 meV window',
      not CLO['verdict']['limit_half_holds']
      and CLO['registered']['limit_tol_mev'] == 1.0
      and abs(CLO['r7842']['upper95_mev'] - 275.3) <= 0.045,
      f"{CLO['r7842']['upper95_mev']:.1f} meV against {CLO['registered']['limit_mev']}, a gap of "
      f"{CLO['limit_gap_mev']:.2f} meV")

check('Ⓑ② AND THE DEFECT IS THE TOLERANCE, NOT THE HARNESS: the quantile\'s own Monte-Carlo '
      'standard error is larger than the window the arm was registered with, so a 1 meV agreement '
      'was not achievable by a rerun of r7838\'s code against itself',
      CLO['verdict']['tolerance_tighter_than_instrument']
      and CLO['combined_mcse_mev'] > CLO['registered']['limit_tol_mev']
      and abs(CLO['limit_gap_in_mcse'] - 1.00) <= 0.045,
      f"standard errors {CLO['r7838']['mcse_mev']:.2f} and {CLO['r7842']['mcse_mev']:.2f} meV, "
      f"combined {CLO['combined_mcse_mev']:.2f}; the gap is "
      f"{CLO['limit_gap_in_mcse']:.2f} of it, and the six chains inside each run span "
      f"{CLO['r7838']['per_chain_range_mev']:.1f} and "
      f"{CLO['r7842']['per_chain_range_mev']:.1f} meV")

_three = CLO.get('three_realisations')
check('Ⓑ② the THIRD realisation is in the record BECAUSE it passes -- on the repaired sampler the '
      'same closure returns r7838\'s figure inside the registered window.  Three draws from one '
      'posterior, against a standard error of about 1.7: that is consistency and NOT restoration, '
      'and the arm stands FAILED as registered and as first measured',
      _three is not None and CLO['verdict']['limit_half_holds_on_fixed_sampler'] is True
      and max(_three) - min(_three) < 3.0 * CLO['combined_mcse_mev'],
      f"{', '.join(f'{v:.1f}' for v in _three)} meV, spread "
      f"{max(_three) - min(_three):.2f}" if _three else 'the fixed-sampler run is absent')

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓒ③  ONE AMPLITUDE, JOINT, AND THE POSITIVITY GUARD OFF TE
check('Ⓒ③ ONE amplitude is solved analytically and JOINTLY across TT, TE and EE -- not three -- and '
      'the positivity guard is applied to TT and EE only, because TE is negative over part of its '
      'range.  ** ASSERTED OFF THE CODE THE CHAINS ACTUALLY RAN. **  The scorer DEFINES the guard '
      'and `model3` is what APPLIES it, and the amplitude the sampler used is `model3`\'s own '
      'joint solve -- so asserting the scorer alone would have asserted a definition and called it '
      'a measurement',
      'A = float((m @ F @ d) / (m @ F @ m))' in SCORE
      and 'POSITIVE = BLOCK != 1' in SCORE
      and SCORE.count('np.tril(_c) + np.tril(_c, -1).T') == 1
      and 'self.pos = SC.POSITIVE[self.ok]' in MODEL
      and 'np.any(m[self.pos] <= 0)' in MODEL
      and MODEL.count('A = float((m @ self.F @ self.d) / (m @ self.F @ m))')
      == MODEL.count('A = float('),
      'EVERY amplitude solve in the model the chains called is the same joint closed form over the '
      'whole kept vector -- %d of %d, the objective\'s and the barrier\'s, with no per-spectrum '
      'solve anywhere -- and the guard\'s mask excludes block 1 and is applied there as a 1e12 '
      'return.  ⌗ The first version of this arm asserted there was only ONE solve; there are two, '
      'both joint, and counting them was never the claim'
      % (MODEL.count('A = float((m @ self.F @ self.d) / (m @ self.F @ m))'),
         MODEL.count('A = float(')))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓘ⑨  ITEM ③'s TWO HALVES
check('Ⓘ⑨ the low-l bin file IS absent, and the likelihood itself names what it wants rather than '
      'this receipt guessing: asking planck_lite_py for those bins raises FileNotFoundError on '
      'CTT_bin_low_ell_2018.dat, while nbintt_low_ell and use_low_ell_bins both exist -- the '
      'capability is wired and the data was never given',
      not os.path.exists(os.path.join(ROOT, 'computations', 'planck_tt_likelihood', 'data',
                                      'planck2018_low_ell', 'CTT_bin_low_ell_2018.dat')),
      'and node 70 stood a tau prior of 0.054 +/- 0.007 in for low-l EE at r7471 rather than '
      'score it, which corroborates the absence from outside this seat')

check('Ⓘ⑨ and tau\'s reach is MEASURED and not assumed: the score does not move across '
      'tau = 0.02-0.20, because this harness solves one overall amplitude analytically and a '
      'uniform exp(-2 tau) is EXACTLY degenerate with it, and the instrument\'s visibility carries '
      'recombination only.  ⇒ That changes the moment the lensing bandpowers enter, which carry no '
      'fitted amplitude',
      TAU['worst_abs_dchi2'] < 1e-10
      and sum(TAU['reionisation_words'].values()) == 0
      and TAU['baseline']['nbins'] == 555,
      f"worst |dchi^2| = {TAU['worst_abs_dchi2']:.3e} across tau = "
      f"{min(float(k) for k in TAU['uniform_suppression']):.4f}-"
      f"{max(float(k) for k in TAU['uniform_suppression']):.4f} on all "
      f"{TAU['baseline']['nbins']} bins, while the amplitude absorbs it from "
      f"{min(v['amplitude'] for v in TAU['uniform_suppression'].values()):.0f} to "
      f"{max(v['amplitude'] for v in TAU['uniform_suppression'].values()):.0f}; and the "
      f"instrument's source contains none of "
      f"{', '.join(sorted(TAU['reionisation_words']))}")

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓗ⑧  THE ARM THAT FAILS BECAUSE ITS PREMISE WAS FALSE
_d = REACH['data']
check('Ⓗ⑧ IS REPORTED FAILED, with the criterion exactly as registered.  It asserted that no '
      'lensing bandpowers and no lensing covariance are banked; its own reachable negative was '
      '"finding them banked, in which case the arm is wrong and item ② is runnable".  THEY ARE '
      'BANKED -- nine Planck 2018 conservative bandpowers, a covariance symmetric to 0.0 and '
      'positive definite, and nine bandpower windows, put there by node 70 at r7471 and scored '
      'there.  ⌗ THE WINDOW SUMS ARE REPORTED AND NOT ASSERTED: this seat wrote "each summing to '
      'one" from the ACT DR6 bank\'s provenance without checking it against THESE windows, and '
      'they run 0.9961 to 1.0277.  A lensing bandpower window is not required to be a partition '
      'of unity',
      _d['bandpowers'] == 9 and _d['cov_shape'] == [9, 9]
      and _d['cov_min_eigenvalue'] > 0 and _d['cov_symmetric_to'] == 0.0
      and _d['windows'] == 9
      and pin(min(_d['window_weight_sums']), 0.996127)
      and pin(max(_d['window_weight_sums']), 1.027688)
      and 'in which case the arm is wrong and item ② is runnable' in PRED,
      f"L = {_d['L_min']:.0f} to {_d['L_max']:.0f}, fractional errors "
      f"{100 * min(_d['fractional_error']):.1f} to {100 * max(_d['fractional_error']):.1f} per "
      f"cent, smallest eigenvalue {_d['cov_min_eigenvalue']:.3e}, window sums "
      f"{min(_d['window_weight_sums']):.6f} to {max(_d['window_weight_sums']):.6f}")

_b = REACH['background']
check('Ⓗ⑧ AND THE OBSTRUCTION IS THE INSTRUMENT, MEASURED: at fixed total Omega_m this '
      'instrument\'s background rate is EXACTLY independent of the neutrino sum -- 0.000e+00, not '
      'nearly -- so the background-only growth factor L171x builds carries exactly zero neutrino '
      'effect, and the lensing kernel peaks at z ~ 3.3, entirely downstream of the z = 12.8 where '
      'the k-dependence is frozen',
      _b['exactly_independent'] and _b['max_rel_dH'] == 0.0 and _b['rel_dDM'] == 0.0,
      f"max |dH/H| = {_b['max_rel_dH']:.3e} across four decades of scale factor, comoving distance "
      f"to last scattering identical at {_b['D_M'][0]:.4f} Mpc")

_cl = REACH['clustering']
check('Ⓗ⑧ and the one channel that DOES respond is scale-independent and frozen at that redshift: '
      'the sum enters the clustering source and nothing else, dropping it by exactly f_nu, flat in '
      'k.  The physical suppression is neither -- it switches on above the free-streaming scale and '
      'accumulates to z = 0 -- so item ② is an INSTRUMENT EXTENSION and not a data request',
      _cl['matches_f_nu_to'] < 1e-12 and _cl['scale_independent_to'] < 1e-12
      and pin(100 * _cl['source_drop'], 2.250892),
      f"the source drops {100 * _cl['source_drop']:.6f} per cent against f_nu = "
      f"{100 * _cl['f_nu']:.6f}, flat in k to {_cl['scale_independent_to']:.3e}")

check('Ⓗ⑧ and this receipt does NOT say how large the missing part is: the textbook asymptote is '
      '-8 f_nu, this harness has not produced it, and printing it here would be borrowing a result '
      'and presenting it as a measurement',
      '-8 f_nu' not in SCORE and 'missing_piece' in REACH['verdict'],
      REACH['verdict']['blocked_on'])

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# THE SAMPLER DEFECT -- NOT A REGISTERED ARM.  Found, not predicted, and said so.
check('⌗ FOUND NOT PREDICTED -- the sampler\'s proposal was mis-scaled by up to three orders of '
      'magnitude and r7838 survived it by luck.  Burn stage 1 accepted 0.002 in BOTH the 185-bin '
      'and the 555-bin problem; at 185 bins the between-chain scatter of the dispersed starts '
      'happened to resemble the posterior and stage 3 recovered, and at 555 bins the tuner ran AWAY '
      '-- 0.002, 0.001, 0.002, 0.004, 0.006, 0.009.  The proposal covariance is now 2 H^-1 at the '
      'minimum, the starts are dispersed in its own metric, and a kept chain outside '
      '0.03 <= accept <= 0.70 is REFUSED rather than reported',
      'def laplace_cov(' in SAMP
      and 'REFUSING to report a chain that' in SAMP
      and 'assert 0.03 <= rate <= 0.70' in SAMP
      and 'np.diag(scale ** 2)' not in SAMP,
      'six frozen chains agree with themselves, so they return an R-hat near 1 and a serviceable '
      'quantile: nothing in the output said that run was dead')

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓓ④ Ⓔ⑤ Ⓕ⑥  THE CONTROL ON TT+TE+EE
if PR is None:
    check('Ⓓ④ the sampler converges on the wider score', False, 'the control\'s 555-bin run is absent')
    check('Ⓔ⑤ THE DECISIVE ARM -- the control on TT+TE+EE', False, 'absent')
    check('Ⓕ⑥ the gap\'s sign survives the wider score', False, 'absent')
else:
    _pb = PR['lcdm_bounded']
    _dg = _pb['diagnostics']
    check('Ⓓ④ THE SAMPLER STILL CONVERGES on the wider score: six chains, split Gelman-Rubin below '
          '1.05 on every parameter and effective sample size on the sum at or above 1000',
          _pb['chains'] == 6 and all(v['rhat'] < 1.05 for v in _dg.values())
          and _dg['MNU']['ess'] >= 1000,
          'R-hat max %.4f, ESS on the sum %.0f, acceptance %.3f'
          % (max(v['rhat'] for v in _dg.values()), _dg['MNU']['ess'], _pb['accept']))

    _pu = PR['lcdm_unbounded']
    _lim = _pb['upper95_mev']
    # ** THE EFFECTIVE MASS IS THE UNBOUNDED FIT'S MEAN, NOT THE BOUNDED ONE'S. **  The published
    # -0.101 eV is a fit with the sum FREE TO GO NEGATIVE, and r7838 read it off its own unbounded
    # chain for that reason.  This arm was first written against the BOUNDED mean, which is
    # bounded below at zero and therefore could not have come out negative however the data fell:
    # a half that cannot fail is not a test, and it was testing the wrong clause.
    _eff = _pu['sum_mean_ev']
    _eff_sd = _pu['sum_sd_ev']
    # the limit's own standard error: recorded by runs from r7842 on, computed from the saved chain
    # for this one, whose JSON predates the field.  ** ONE DEFINITION, NOT TWO. **
    if 'upper95_mcse_mev' in _pb:
        _se = _pb['upper95_mcse_mev']
        _span = (max(_pb['upper95_per_chain_mev']) - min(_pb['upper95_per_chain_mev']))
    else:
        sys.path.insert(0, RUN)
        from sampler3 import quantile_mcse            # noqa: E402
        _z = np.load(os.path.join(RUN, 'chain3_lcdm_b_012.npz'), allow_pickle=True)
        _C = np.asarray(_z[list(_z.keys())[0]], float)
        _se = quantile_mcse(_C.reshape(-1, 5)[:, 4], _pb['diagnostics']['MNU']['ess'], 0.95)
        _pcq = [float(np.quantile(_C[i, :, 4], 0.95) * 1000.0) for i in range(_C.shape[0])]
        _span = max(_pcq) - min(_pcq)

    _in_band = ORDER_BAND_MEV[0] <= _lim <= ORDER_BAND_MEV[1]
    _neg = _eff < 0
    _passes = bool(_in_band and _neg)
    _over = (_lim - ORDER_BAND_MEV[1]) / _se
    check('Ⓔ⑤ THE DECISIVE ARM IS REPORTED FAILED AGAINST THE ORDER\'S CRITERION, with the '
          'criterion exactly as registered -- but it fails on ONE half of two, and the other half '
          'HOLDS.  The limit had to fall inside 42.8 to 96.3 meV: it is above the ceiling by SIX '
          'standard errors of its own quantile, a decisive miss and not a boundary case',
          not _passes and not _in_band and _over > 3.0,
          '%.2f +/- %.2f meV against the published %.1f, a factor %.2f; above the band\'s ceiling '
          'by %.2f meV = %.2f standard errors'
          % (_lim, _se, PUBLISHED_LIMIT_MEV, _lim / PUBLISHED_LIMIT_MEV,
             _lim - ORDER_BAND_MEV[1], _over))

    check('Ⓔ⑤ AND ITS SECOND HALF HOLDS, WHICH IS NEW: the effective mass comes out NEGATIVE, the '
          'sign the published -0.101 eV carries, where r7838\'s was +67.5 meV on temperature '
          'alone.  ** POLARISATION FLIPPED THE SIGN. **  ⌗ The quantity is the UNBOUNDED fit\'s '
          'mean, with the sum free to go negative, which is what the published figure is and what '
          'r7838 read; this arm was first written against the BOUNDED mean, which is bounded below '
          'at zero and so could not have come out negative however the data fell -- a half that '
          'cannot fail is not a test',
          _neg,
          '%+.1f +/- %.1f meV against the published %+.0f -- same sign, and %.2f sigma from it on '
          'this fit\'s own width; r7838 gave %+.1f on 185 bins'
          % (1000 * _eff, 1000 * _eff_sd, 1000 * PUBLISHED_EFFECTIVE_EV,
             abs(_eff - PUBLISHED_EFFECTIVE_EV) / _eff_sd, 67.5))

    _seat_fails = not _passes
    _seat_size = SEAT_EXPECTATION_MEV[0] <= _lim <= SEAT_EXPECTATION_MEV[1]
    _short = (SEAT_EXPECTATION_MEV[0] - _lim) / _se
    check('Ⓔ⑤ AND THIS SEAT\'S OWN EXPECTATION, registered separately and falsifiable both ways, '
          'SPLITS: it predicted a FAILURE, and the failure happened; it predicted the size as a '
          'limit between 100 and 250 meV, and that half is REFUTED.  ** THE MISS IS 0.33 meV, '
          'WHICH IS SIX TENTHS OF THE QUANTILE\'S OWN STANDARD ERROR ** -- so the prediction was '
          'right to the instrument\'s precision and is STILL reported refuted, because the '
          'criterion is what was registered and not what it nearly was.  That is the SECOND '
          'tolerance in this revision written finer than the quantile it judges, after Ⓑ②, and '
          'the sampler now records every limit with its error beside it so there is not a third',
          _seat_fails and not _seat_size and _short < 1.0,
          'the failure half HOLDS; the size half is REFUTED -- %.2f meV against a registered floor '
          'of %.0f, short by %.2f meV = %.2f standard errors, the six chains themselves spanning '
          '%.2f'
          % (_lim, SEAT_EXPECTATION_MEV[0], SEAT_EXPECTATION_MEV[0] - _lim, _short, _span))

    check('Ⓔ⑤ and WHAT POLARISATION BOUGHT, which is the half the order was after: the limit '
          'tightens from r7838\'s 277.7 meV on 185 temperature bins to this, on 555.  ⇒ The '
          'published 64.2 is now a factor 1.55 away where it was 4.33, so r7838\'s diagnosis -- '
          'that the looseness was in WHAT the harness scores -- is confirmed by the repair rather '
          'than by argument',
          _lim < R38_LIMIT_MEV and (R38_LIMIT_MEV / _lim) > 2.0,
          '%.1f -> %.2f meV, a factor %.2f tighter; the published limit goes from a factor %.2f '
          'away to %.2f'
          % (R38_LIMIT_MEV, _lim, R38_LIMIT_MEV / _lim, R38_LIMIT_MEV / PUBLISHED_LIMIT_MEV,
             _lim / PUBLISHED_LIMIT_MEV))

    _gap = _pb['gap_mean_pc']
    check('Ⓕ⑥ the gap\'s sign survives the wider score: the control\'s fitted matter-density gap '
          'stays POSITIVE, as it was on TT alone',
          _gap > 0,
          '%+.2f per cent on 555 bins against %+.2f on 185 and the published +2.48' %
          (_gap, 3.70))

    # ─────────────────────────────────────────────────────────────────────────────────────────────
    # Ⓖ⑦  THE ARM OF RECORD -- and ONLY if Ⓔ⑤ passes
    if not _passes:
        check('Ⓖ⑦ THE ARM OF RECORD IS NOT JUDGED, because Ⓔ⑤ did not pass and the arm was '
              'registered as conditional on it.  A limit read off an apparatus that misses its own '
              'control is not a result, and P15 is NOT touched',
              True,
              'where 59 and 64 meV sit is reported for the record only: %.1f and %.1f per cent of '
              'the control\'s posterior lies below them'
              % (100 * _pb['frac_below_0.059'], 100 * _pb['frac_below_0.064']))
    elif AR is None:
        check('Ⓖ⑦ the arm of record', False, 'Ⓔ⑤ passed but the arm\'s 555-bin run is absent')
    else:
        _ab = AR['cr_bounded']
        check('Ⓖ⑦ THE ARM OF RECORD, read because Ⓔ⑤ passed: its limit is LOOSER than the '
              'control\'s, as registered',
              _ab['upper95_mev'] > _lim,
              '%.1f meV against the control\'s %.1f; %.1f per cent of its posterior below 59 meV '
              'and %.1f per cent below 64'
              % (_ab['upper95_mev'], _lim, 100 * _ab['frac_below_0.059'],
                 100 * _ab['frac_below_0.064']))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓙ⑩  THE COUNT
_ran = 10
check('Ⓙ⑩ the count: this receipt adjudicates all %d registered arms, and TWO of them are reported '
      'FAILED with their criteria exactly as registered -- Ⓗ⑧ because its premise was false and its '
      'own reachable negative said so, and Ⓑ②\'s limit half because its tolerance was tighter than '
      'the instrument it judges.  A failure asserted is not a failure suffered' % _ran,
      _ran == 10 and PRED.count('**Ⓙ⑩') == 1,
      '%d arm-check(s) failed' % len(fail))

print()
if not fail:
    print('  r7844 OK -- every arm holds, and the two registered failures are ASSERTED rather than '
          'suffered:')
    print('    => Ⓗ⑧: the lensing measurement IS banked, at r7471+70.  Item ② is not blocked on '
          'data; it is blocked on a scale-dependent growth, which is an instrument extension.')
    print('    => Ⓑ②: the extension did not change the TT scoring (chi^2 to 4.1e-12, Fisher '
          'bitwise); the 1 meV window was below the quantile\'s own 1.7 meV standard error.')
    if PR is not None:
        print('    => the control on 555 bins: %.1f meV against the published %.1f.'
              % (PR['lcdm_bounded']['upper95_mev'], PUBLISHED_LIMIT_MEV))
    sys.exit(0)
print('  ⛔ %d arm(s) failed: %s' % (len(fail), fail))
sys.exit(1)
