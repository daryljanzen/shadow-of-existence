#!/usr/bin/env python3
r"""RECEIPT -- P15 (r7850, node 60): ** THE ORDER ASKED FOR THE CARRY TO START INSIDE THE RADIATION
ERA AND THE MEASUREMENT SAYS THE OPPOSITE: THE CARRY'S ERROR IS THE RADIATION SHARE AT ITS HANDOVER,
SO THE HANDOVER BELONGS AS LATE AS THE INSTRUMENT CAN AFFORD.  THE INITIAL-CONDITION REPAIR TAKES THE
CONTROL FROM 111.38 TO 100.40 meV AND THE NORMALISATION FROM NINE PER CENT LOW TO 2.55 -- AND THE
DECISIVE ARM STILL FAILS BOTH HALVES.  AND camb 2.0.4 IS INSTALLED IN THIS CONTAINER, WHERE THE
CHANNEL SAYS IT WILL NOT INSTALL: IT FITS THE NINE BANDPOWERS WITH NOTHING FITTED, SO THE SHAPE
ERROR THIS LINE HAS BEEN ATTRIBUTING TO ITS CARRY IS ITS OWN INSTRUMENT'S. **

COMPUTES: the closed test of a growth-factor carry against the instrument's own potential at five
  handover/judge combinations and the domain its identity ranges over; the carry's error as a
  function of the radiation share at the handover; the asymptote and the lensing shape under
  initial conditions read off the instrument rather than off a closed form; the control's 95 per
  cent limit and effective mass with their Monte-Carlo errors; the absolute normalisation; an
  independent CAMB reference for the nine banked bandpowers; and the instrument's own solve cost
  with the configuration beside every number.  ** It pins NO cosmological parameter as a result,
  and the arm of record is NOT JUDGED. **

⌷ ** THE ID. **  69 ordered this work as r7847 and this revision's directory, its PREDICTION.md at
`77f16be96` and its commits all carry r7850, which is this line's next EVEN id above the trunk's
front.  It lands as r7850.

THE ORDER (r7847, 69): ① carry Phi through the radiation era with its scale-dependent decay, from
the handover through matter-radiation equality into the late growth, on the instrument's own rate,
replacing the matter-plus-Lambda closed form r7848's Ⓐ① found wrong by about half a per cent in D;
② show what it buys on the missing neutrino suppression (about 44 per cent) and the lensing shape
drift; ③ the control first, against 64.2 meV and -0.101 eV, compared against cc66's independent CAMB
decomposition when it lands.  P15 is not to change.  PREDICTION.md was committed and pushed BEFORE
any computation, with eleven arms.

** THE SHAPE OF THE RESULT -- THE ORDER'S OWN PREMISE IS REFUTED, AND THEN THE FAULT MOVES. **

  ① CANNOT BE DELIVERED AS ASKED, AND THE REASON IS MEASURED.  The instrument ALREADY carries Phi
  through the radiation era and through equality -- evolve() runs from a = 3.3e-08 past equality at
  z ~ 3400 to z = 53.6 by default and further when asked.  What the late carry threw away was the
  instrument's own solve.  And carrying from INSIDE the radiation era, which is what the order asked
  for, is worse: Ⓐ①'s residual on the modes its identity covers runs 0.0986, 0.0615, 0.0239, 0.0264
  and 0.0224 at handovers whose radiation-to-matter ratio is 0.1401, 0.0548, 0.0268, 0.0158 and
  0.0040, and at the production handover it FLOORS at 3.7771e-03 -- the radiation share 0.00401 to
  within six per cent.  ** So the carry's own error is first order in the one thing the growth
  equation omits, and the handover belongs as LATE as the instrument can afford. **  r7848 had it in
  the right place for a reason r7848 did not know.

  ② IS TWO HALVES THAT PULL AGAINST EACH OTHER.  Recovering the missing suppression needs an early
  handover; an early handover costs the radiation share.  Ⓓ④ measured the asymptote at 0.294419 of
  the textbook against a registered AT LEAST 0.667 -- and a -0.54 per cent move AWAY from r7848's
  0.296012 at matched f_nu.  Ⓒ③'s chi^2 half RISES, 2.048681 to 2.131182.

  ③ IS DELIVERED AND Ⓕ⑥ FAILS BOTH HALVES -- but not by as much: 100.402 +/- 0.353 meV against
  111.383 +/- 0.409, and +21.913 +/- 44.423 against +44.253 +/- 39.792, so the distance above the
  order's own ceiling falls from 36.91 standard errors to 11.61 and the effective mass closes 0.88
  of the 3.65 it was out by.  Ⓔ⑤ HOLDS: the absolute normalisation goes from 9.04 per cent low to
  2.55.  ** One arm of eleven holds, and it is a real improvement rather than a tie. **

** AND THEN THE REFERENCE THE ORDER WAS WAITING FOR TURNS OUT TO BE INSTALLED. **  FOR_66 states
repeatedly that camb 2.0.4 will not install in this container.  Probed rather than taken on the
page's word: it is installed and it runs.  At the control's own cosmology, with A_s stated as a
parameter and NOTHING fitted, CAMB scores the nine bandpowers at chi^2 8.8173 on nine bins, every
bin inside 1.34 of its own error, and the amplitude it would choose is 1.002494.  This instrument
scores 16.3894 with the quadrature's initial conditions and 17.0507 with the instrument's, and its
shape disagrees with CAMB's by -14.3 to +27.2 and -14.6 to +28.0 per cent.
  ⇒ ** THE NINE BANDPOWERS ARE NOT HARD TO FIT.  The chi^2/dof of 2.05 this line has been
  attributing to its carry is its own instrument's lensing potential disagreeing with an independent
  one by up to 28 per cent in shape at fixed cosmology. **  That refutes the premise the whole
  repair programme rests on, this revision's own included.
  ⌗ Third consecutive revision in which a stated absence was false on probing: r7844 found the
  lensing bandpowers banked, r7848 found ACT DR6 banked, this finds the reference pipeline installed.

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
                   'r7850_60_phi_carried_through_the_radiation_era')
R7846 = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                     'r7846_60_the_scale_dependent_growth_and_the_banked_lensing_bandpowers')

PUBLISHED_LIMIT_MEV = 64.2          # arXiv:2503.14744, the standard-model 95 per cent upper limit
PUBLISHED_EFFECTIVE_EV = -0.101     # its effective mass, the sum free to go negative
ORDER_BAND_MEV = (42.8, 96.3)       # the order's factor-1.5 window on the published limit
SEAT_EXPECTATION_MEV = (70.0, 110.0)   # this seat's own registered expectation, falsifiable
CRITERION = 0.023                   # Ⓐ①'s registered spread, one tenth of r7848's matter-only 0.2276
R7848_SPREAD = 0.2276267789861
D4_REGISTERED = 0.667               # Ⓓ④'s registered floor

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


CARRY = jload('phi_carry.json')                      # Ⓐ①/Ⓑ②, the registered configuration
CARRY2 = jload('phi_carry_judge4000_from_1400_1893.json')
ISO = jload('carry_isolate.json')                    # the isolation, registered configuration
ISO2 = jload('carry_isolate_judge4000_from_1400_1893.json')
ISO3 = jload('carry_isolate_judge6000_from_4000.json')
THRESH = jload('poisson_threshold_sensitivity.json')
GFI = jload('growth_from_instrument_sum0.3.json')    # Ⓓ④ at r7848's own f_nu
SENS = jload('shape_sensitivity.json')               # Ⓒ③
NORM = jload('normalisation.json')                   # Ⓔ⑤
CAMB = jload('camb_reference.json')                  # Ⓖ⑦
CTRL = jload('sampler6_lcdm_ics.json')               # Ⓕ⑥/Ⓘ⑨
COST = jload('cost_table.json')                      # Ⓙ⑩
OLD = jload('sampler6_lcdm.json', R7846)             # r7848's control, read not retyped
OLDINFO = jload('lensing_informative.json', R7846)
PRED = src('PREDICTION.md')
RESULT = src('RESULT.md')
PRED1 = ' '.join(PRED.split())
RESULT1 = ' '.join(RESULT.split())
PCSRC = src('phi_carry.py')
GFISRC = src('growth_from_instrument.py')

_b, _u = CTRL['lcdm_bounded'], CTRL['lcdm_unbounded']
_lim, _se = _b['upper95_mev'], _b['upper95_mcse_mev']
_eff, _effsd = _u['sum_mean_ev'] * 1e3, _u['sum_sd_ev'] * 1e3
_ob, _ou = OLD['lcdm_bounded'], OLD['lcdm_unbounded']
_olim, _ose = _ob['upper95_mev'], _ob['upper95_mcse_mev']
_oeff, _oeffsd = _ou['sum_mean_ev'] * 1e3, _ou['sum_sd_ev'] * 1e3

print('r7850 (60), ordered as r7847 -- where the handover belongs, and whose instrument is wrong\n')

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓐ①  THE REGISTERED FAILURE, ASSERTED -- AND ITS DOMAIN ESTABLISHED RATHER THAN ASSUMED
_rows = CARRY['handovers'] + CARRY2['handovers'] + ISO3['handovers']
_spreads = [r['spread'] if 'spread' in r else r['full_band']['spread'] for r in _rows]
check('Ⓐ① the registered criterion was a residual spread below 0.023 across the band, one tenth of '
      'the 0.2276 r7848\'s matter-only carry scored, and the carry gives 0.3206 to 0.6295 instead -- '
      'REPORTED FAILED with the criterion exactly as registered.  ** And the domain is ESTABLISHED '
      'rather than assumed: the Poisson relation the test rests on is a SUB-HORIZON statement, it '
      'holds to one per cent on only 16 to 23 of 40 modes and only above k*eta of 18.9 to 32.8, and '
      'at the lowest k its own residual is 0.94 to 0.998 -- wrong by a factor two, saying nothing. '
      '** So more than half of the full-band spread comes from modes where this arm\'s own '
      'comparison is invalid, which is the same category error r7848\'s first growth attempt made',
      CARRY['any_holds'] is False and min(_spreads) > CRITERION
      and abs(CARRY['criterion'] - CRITERION) < 1e-09
      and abs(CARRY['r7848_matter_only_spread'] - R7848_SPREAD) < 1e-09
      and all(16 <= h['poisson']['n_ok'] <= 23 for h in ISO['handovers'] + ISO3['handovers'])
      and all(h['poisson']['k_eta_min_ok'] > 18.0
              for h in ISO['handovers'] + ISO3['handovers'])
      and all(h['poisson']['worst_at_low_k'] > 0.9
              for h in ISO['handovers'] + ISO3['handovers']),
      'spreads %.4f..%.4f against the criterion %.3f; the identity covers %d..%d of 40 modes'
      % (min(_spreads), max(_spreads), CRITERION,
         min(h['poisson']['n_ok'] for h in ISO['handovers'] + ISO3['handovers']),
         max(h['poisson']['n_ok'] for h in ISO['handovers'] + ISO3['handovers'])))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓐ①ᵇ  AND THE RESIDUAL FLOORS AT THE RADIATION SHARE, WHICH IS THE REVISION'S CLEANEST READING
_t = THRESH['by_poisson_threshold']
_floor = float(_t['0.0001']['spread'])
_rad = float(ISO3['handovers'][0]['radiation_over_matter'])
check('Ⓐ①ᵇ the carry\'s own error is FIRST ORDER in what the growth equation omits.  At the handover '
      'the production path uses, tightening the Poisson admission takes the restricted spread from '
      '2.2388e-02 at one per cent through 1.2396e-02 and 5.1421e-03 to 3.7771e-03, where it FLOORS '
      '-- and 3.7771e-03 is the radiation-to-matter ratio 0.00401 there, to within six per cent.  '
      '** So the handover belongs as LATE as the instrument can afford, which is the OPPOSITE of '
      'what the order asked for, and r7848 had it in the right place for a reason r7848 did not '
      'know **',
      abs(_floor - 0.0037771) < 4.5e-07 and abs(_rad - 0.00401) < 4.5e-05
      and abs(_floor / _rad - 1.0) < 0.07
      and float(_t['0.01']['spread']) > float(_t['0.001']['spread']) > _floor
      and abs(float(_t['1e-05']['spread']) - _floor) < 1e-12,
      'floors at %.4e against a radiation share of %.5f, a ratio of %.4f'
      % (_floor, _rad, _floor / _rad))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓑ②  THE HANDOVER IS NOT A FREE PARAMETER, AND THE DEPENDENCE IS MEASURED AT FIVE COMBINATIONS
_res = [(h['eta_h'], h['radiation_over_matter'], h['restricted']['spread'])
        for h in ISO['handovers'] + ISO2['handovers'] + ISO3['handovers']]
check('Ⓑ② the residual is measured at FIVE handover/judge combinations, so the handover cannot be '
      'tuned without this arm saying so, and what it tracks is the RADIATION SHARE and not the '
      'carry\'s length: 500 to 1893 is a shorter carry than 1893 to 4000 and scores four times '
      'worse.  The restricted spreads run 0.0986, 0.0615, 0.0239, 0.0396, 0.0264 and 0.0224 at '
      'shares of 0.1401, 0.0548, 0.0268, 0.0268, 0.0158 and 0.0040',
      len(_res) >= 5 and abs(_res[0][2] - 0.0986) < 0.0045
      and abs(_res[1][2] - 0.0615) < 0.0045 and abs(_res[2][2] - 0.0239) < 0.0045
      and abs(ISO3['handovers'][0]['restricted']['spread'] - 0.0224) < 0.0045
      and _res[0][1] > _res[1][1] > _res[2][1],
      '%d combination(s); the spread falls with the share, 0.1401 -> %.4f and 0.0040 -> %.4f'
      % (len(_res), _res[0][2], ISO3['handovers'][0]['restricted']['spread']))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓑ②ᵇ  A REPAIR WRITTEN HERE IS PROVABLY NOT ONE, AND THE MEASUREMENT SAYS SO TO TWELVE DIGITS
# the identity is read PER HANDOVER, because that is where every record carries it: the registered
# configuration's own record was first written before the identity was instrumented, and refreshing
# it is what put the measurement in the registered record rather than only in a later one.
_ts = [h['two_species'] for h in CARRY['handovers'] + CARRY2['handovers']]
check('Ⓑ②ᵇ carrying the two clustering species SEPARATELY changes nothing, and that is asserted as a '
      'measurement rather than left as a derivation: the worst relative difference from carrying '
      'their weighted sum is 2.298e-12 across five configurations.  ⌷ That figure read '
      '1.672e-12 until the REGISTERED configuration\'s own record was refreshed to carry '
      'the measurement: the smaller number was the maximum over the subset of records '
      'that happened to have it, which is one more figure quoted from the wrong SET '
      'rather than the wrong switches.  ** Both obey the same equation '
      'with the same source, because the source depends only on the TOTAL, so the weighted sum obeys '
      'it too with the weighted sum of their initial conditions. **  The baryon shortfall the '
      'isolation measured -- d_b/d_c of 1.0000 at k = 2e-4 and 0.0101 at k = 1 -- is real and is NOT '
      'an error the carry can fix by splitting them.  ⌗ The guard is this seat\'s own: when a fork '
      'names two objects, check that the thing they are alternatives FOR has a slot for only one',
      all(t['identical_to_one_species'] for t in _ts)
      and max(t['worst_relative_difference_from_one_species'] for t in _ts) < 1e-09
      and abs(ISO['handovers'][0]['baryons']['at_k_min'] - 1.0) < 4.5e-05
      and abs(ISO['handovers'][0]['baryons']['at_k_max'] - 0.0101) < 4.5e-05
      and 'slot for only one' in PCSRC,
      'identical to %.3e relative; d_b/d_c runs %.4f to %.4f at the first handover'
      % (max(t['worst_relative_difference_from_one_species'] for t in _ts),
         ISO['handovers'][0]['baryons']['at_k_min'],
         ISO['handovers'][0]['baryons']['at_k_max']))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓒ③  THE SHAPE HALF -- FAILED, AND ITS OTHER HALF CANNOT BE COMPARED AT ALL
_q, _i = SENS['quadrature_ics'], SENS['instrument_ics']
check('Ⓒ③ registered that BOTH the chi^2 per degree of freedom and the drift would FALL.  The chi^2 '
      'per dof RISES, 2.048681 to 2.131182 -- REPORTED FAILED with the criterion exactly as '
      'registered.  ** And the quadrature reading reproduces r7848\'s to every digit, 16.389450 '
      'against 16.389449912869935, which is the closure that says the difference measured here is '
      'the repair and not the plumbing. **  ⌗ The DRIFT half cannot be compared and that is a defect '
      'in r7848\'s record this seat owns: its "+49.8 per cent" lives only in a JSON and the code '
      'that made it was not kept, so the definition is unrecoverable and this revision\'s own drift '
      'is a DIFFERENT QUANTITY, reported with its definition and not as a refutation',
      abs(_q['chi2'] - OLDINFO['chi2_at_own_best_normalisation']) < 1e-05
      and _i['chi2_per_dof'] > _q['chi2_per_dof']
      and abs(_q['chi2_per_dof'] - 2.048681) < 0.00045
      and abs(_i['chi2_per_dof'] - 2.131182) < 0.00045
      and 'drift half cannot be compared' in RESULT1
      and not os.path.exists(os.path.join(R7846, 'phiphi_carry_compare.py')),
      'chi^2/dof %.6f -> %.6f; the quadrature reading matches r7848 to %.3e'
      % (_q['chi2_per_dof'], _i['chi2_per_dof'],
         abs(_q['chi2'] - OLDINFO['chi2_at_own_best_normalisation'])))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓓ④  THE ASYMPTOTE -- FAILED, AT MATCHED f_nu, AND THE REPAIR MOVES IT THE WRONG WAY
check('Ⓓ④ registered that the new carry would reach AT LEAST 0.667 of the textbook -8 f_nu, which is '
      'what r7848 measured by starting at z = 188.  At f_nu = 0.0225069 -- r7848\'s own value '
      'EXACTLY, not approximately -- it reaches 0.294419 against r7848\'s 0.296012, a -0.54 per cent '
      'move AWAY from the textbook.  REPORTED FAILED with the criterion exactly as registered.  ** '
      'So the initial-condition repair does essentially nothing for the missing suppression, because '
      'the missing suppression is about the interval NOT COVERED and the initial conditions do not '
      'change the interval **',
      abs(GFI['f_nu'] - 0.0225069) < 4.5e-08
      and abs(GFI['ratio_to_textbook'] - 0.294419) < 4.5e-07
      and GFI['ratio_to_textbook'] < D4_REGISTERED
      and abs(GFI['suppression'][-1] - -0.053012) < 4.5e-07
      and GFI['ratio_to_textbook'] < 0.296012,
      'reached %.6f against the registered %.3f; r7848 got 0.296012 at the same f_nu'
      % (GFI['ratio_to_textbook'], D4_REGISTERED))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓔ⑤  THE ONE ARM THAT HOLDS
check('Ⓔ⑤ the absolute normalisation moves TOWARD one, which is what the arm registered, and the '
      'move is large: the ratio of what the bandpowers prefer to what the CMB fit holds goes from '
      '0.909563 to 0.974476, so the miss falls from 9.04 per cent to 2.55 -- a factor 3.5, with '
      'NOTHING fitted to the bandpowers at any point.  ** The held number comes from the CMB fit and '
      'does not depend on which growth carries Phi, so only the preferred one can move, and the '
      'arithmetic is in a file that reads both records rather than in a sentence **',
      NORM['moves_toward_one'] and abs(NORM['ratio_r7848'] - 0.909563) < 4.5e-07
      and abs(NORM['ratio_r7850'] - 0.974476) < 4.5e-07
      and abs(NORM['miss_r7850_pc'] - 2.55) < 0.0045
      and abs(NORM['held'] - 1.617967e-09) < 4.5e-16
      and NORM['held_does_not_depend_on_the_growth'] is True,
      'ratio %.6f -> %.6f, so %.2f per cent low instead of %.2f'
      % (NORM['ratio_r7848'], NORM['ratio_r7850'], NORM['miss_r7850_pc'], NORM['miss_r7848_pc']))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓕ⑥  THE DECISIVE ARM -- FAILS BOTH HALVES, AND BY LESS THAN BEFORE
_above = (_lim - ORDER_BAND_MEV[1]) / _se
_oabove = (_olim - ORDER_BAND_MEV[1]) / _ose
_from_pub = (_eff - PUBLISHED_EFFECTIVE_EV * 1e3) / _effsd
_ofrom_pub = (_oeff - PUBLISHED_EFFECTIVE_EV * 1e3) / _oeffsd
check('Ⓕ⑥ THE DECISIVE ARM FAILS BOTH HALVES.  The criterion as registered was a limit inside '
      '42.8-96.3 meV AND a NEGATIVE effective mass.  Measured: 100.402 +/- 0.353 meV, outside the '
      'band, and +21.913 +/- 44.423 meV, positive.  ** But not by as much: the limit improves 10.981 '
      'meV from r7848\'s 111.383, the distance above the order\'s own ceiling falls from 36.91 '
      'standard errors to 11.61, and the effective mass closes 0.88 of the 3.65 it was out by. **  '
      'chi^2 at the minimum falls from 576.0427 to 570.3427',
      not (ORDER_BAND_MEV[0] <= _lim <= ORDER_BAND_MEV[1]) and _eff > 0.0
      and abs(_lim - 100.402) < 0.0045 and abs(_se - 0.353) < 0.0045
      and abs(_eff - 21.913) < 0.0045 and abs(_effsd - 44.423) < 0.0045
      and abs(_above - 11.61) < 0.0045 and abs(_oabove - 36.91) < 0.0045
      and _lim < _olim and abs(_from_pub) < abs(_ofrom_pub)
      and abs(_b['best_fit']['chi2'] - 570.3427) < 0.00045,
      '%.3f +/- %.3f meV at %.2f sigma above the ceiling, from %.2f; effective %+.3f +/- %.3f'
      % (_lim, _se, _above, _oabove, _eff, _effsd))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓕ⑥ᵇ  AND THIS SEAT'S OWN EXPECTATION SPLITS TWO OF THREE, REPORTED AS A SPLIT
check('Ⓕ⑥ᵇ this seat registered its own expectation separately and falsifiable both ways: FAIL, with '
      'a limit between 70 and 110 meV and a NEGATIVE effective mass.  The failure is right.  The '
      'window is right -- 100.402 sits inside it.  ** The SIGN is wrong: I predicted negative and it '
      'is positive. **  Two of three, and the third is the half that matters most, so the '
      'expectation is NOT claimed as vindicated',
      SEAT_EXPECTATION_MEV[0] <= _lim <= SEAT_EXPECTATION_MEV[1] and _eff > 0.0
      and 'not claimed as vindicated' in RESULT1
      and (SEAT_EXPECTATION_MEV[1] - SEAT_EXPECTATION_MEV[0]) > 30.0 * _se,
      'limit inside the window, sign refuted; the window is %.0f meV wide against an error of %.2f'
      % (SEAT_EXPECTATION_MEV[1] - SEAT_EXPECTATION_MEV[0], _se))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓖ⑦  THE REFERENCE THE ORDER WAS WAITING FOR IS INSTALLED, AND IT MOVES THE FAULT
_inst = CAMB['instrument']
_shape_q = np.array(_inst['r7848_quadrature_ics']['shape_vs_camb'], float)
_shape_i = np.array(_inst['r7850_instrument_ics']['shape_vs_camb'], float)
check('Ⓖ⑦ cc66\'s ordered decomposition has NOT landed and the receipt says so and infers nothing '
      'from the silence -- ** but camb 2.0.4 IS installed in this container, where FOR_66 says '
      'repeatedly that it will not install, and it runs. **  At the control\'s own cosmology with '
      'A_s stated as a parameter and NOTHING fitted it scores the nine bandpowers at chi^2 8.8173 on '
      'nine bins, every bin inside 1.34 of its own error, and the amplitude it would choose is '
      '1.002494.  This instrument scores 16.3894 and 17.0507 on the two growths and its shape '
      'disagrees with CAMB\'s by -14.3 to +27.2 and -14.6 to +28.0 per cent.  ** So the chi^2/dof of '
      '2.05 this line has been attributing to its carry is its own instrument\'s, and the repair '
      'moves the shape AWAY from CAMB rather than toward it **',
      CAMB['decomposition_from_cc66_has_landed'] is False
      and CAMB['camb_version'] == '2.0.4'
      and abs(CAMB['chi2_nothing_fitted'] - 8.8173) < 0.00045
      and abs(CAMB['fitted_amplitude'] - 1.002494) < 4.5e-07
      and max(abs(v) for v in CAMB['in_bin_sigma']) < 1.35
      and CAMB['as_is_a_parameter'] is True
      and abs(_shape_q.min() - -0.1433) < 4.5e-05 and abs(_shape_q.max() - 0.2723) < 4.5e-05
      and abs(_shape_i.min() - -0.1456) < 4.5e-05 and abs(_shape_i.max() - 0.2802) < 4.5e-05
      and abs(_shape_i).max() > abs(_shape_q).max(),
      'CAMB chi^2 %.4f on nine bins with nothing fitted, amplitude %.6f; this instrument %.4f and '
      '%.4f' % (CAMB['chi2_nothing_fitted'], CAMB['fitted_amplitude'],
                _inst['r7848_quadrature_ics']['chi2_free'],
                _inst['r7850_instrument_ics']['chi2_free']))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓖ⑦ᵇ  AND THE CONVENTION IS SETTLED EMPIRICALLY, NOT ASSUMED
_ratio = np.array(CAMB['ratio_camb_over_data'], float)
check('Ⓖ⑦ᵇ the convention is settled by measurement rather than assumed, which this revision has '
      'learned to do five times over: CAMB\'s lensing-potential output binned STRAIGHT through the '
      'nine windows lands at 0.84 to 1.13 of the data.  A missing or extra factor of [L(L+1)]^2/(2 '
      'pi) would put that out by nine orders of magnitude and a single missing factor of L by 28 to '
      '377.  ** It is neither, so the convention matches the banked data\'s **',
      0.8 < _ratio.min() and _ratio.max() < 1.2
      and abs(_ratio.min() - 0.8410) < 4.5e-05 and abs(_ratio.max() - 1.1294) < 4.5e-05,
      'the ratio to the data runs %.4f to %.4f over nine bins' % (_ratio.min(), _ratio.max()))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓗ⑧  NOT JUDGED, AND THE ARM'S GRID DELIBERATELY NOT RUN
check('Ⓗ⑧ the arm of record is NOT JUDGED, as registered conditional on Ⓕ⑥, which did not pass -- the '
      'same ruling r7838, r7844 and r7848 all made.  ** And because the order\'s "control first" was '
      'taken literally, the arm\'s sixteen grid points were NOT run: three hours not spent on a '
      'reading that could not have been reported. **  P15 is untouched',
      'and only if Ⓕ⑥ passes' in PRED1 and 'NOT JUDGED' in RESULT1
      and 'P15` is untouched' in RESULT1
      and not os.path.exists(os.path.join(RUN, 'grid_ics_eta4000', 'cr_S000.json'))
      and os.path.exists(os.path.join(RUN, 'grid_ics_eta4000', 'lcdm_S000.json')),
      'registered conditional, condition not met, the arm\'s grid absent by choice')

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓘ⑨  THE SAMPLER'S GUARDS, INCLUDING THE PER-DIRECTION ONE WITH NOTHING TO CATCH
_rhat = max(v['rhat'] for v in _b['diagnostics'].values())
_ess = min(v['ess'] for v in _b['diagnostics'].values())
_span = max(_b['upper95_per_chain_mev']) - min(_b['upper95_per_chain_mev'])
check('Ⓘ⑨ every registered guard holds: six chains, worst split R-hat 1.000101 against 1.05, '
      'smallest effective sample size 44608 against 1000, kept-chain acceptance 0.2440 and 0.2383 '
      'inside 0.03-0.70, the six chains\' limits spanning 1.088 meV -- and the per-direction guard '
      'r7848 had to write has NOTHING TO CATCH here: the unbounded minimum is not on a bound and the '
      'curvature probe returns a real width in every direction',
      _rhat < 1.05 and _ess >= 1000.0 and 0.03 <= _b['accept'] <= 0.70
      and 0.03 <= _u['accept'] <= 0.70 and _b['chains'] == 6 and _u['chains'] == 6
      and CTRL['lcdm_proposal']['minimum_on_a_bound'] is False
      and CTRL['lcdm_proposal']['curvature_unmeasurable_in'] == []
      and abs(_rhat - 1.0001) < 4.5e-05 and abs(_ess - 44608) < 0.45
      and abs(_span - 1.088) < 0.0045,
      'R-hat %.6f, ESS %.0f, accept %.4f and %.4f, per-chain span %.3f meV, no frozen direction'
      % (_rhat, _ess, _b['accept'], _u['accept'], _span))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓙ⑩  THE COST, WITH THE CONFIGURATION BESIDE EVERY NUMBER -- AND r7848's RECORD CORRECTED
_c914 = COST['carries']['914']
_c4000 = COST['carries']['4000']
check('Ⓙ⑩ the cost is recorded with the configuration beside every number, and r7848\'s record is '
      'CORRECTED: re-measured at the production mode count, phi_shape costs 40.8 s at ETAREF = 914 '
      'and 667.0 s at 4000.  r7848 recorded 40.38 s and did NOT record its ETAREF, while its own '
      'script takes ETAREF from the environment with no default.  ** The closest carry measured here '
      'is 914, a factor 1.011 away, so the record was taken at the carry that same revision then '
      'REVERSED and it understates the carry it landed on by a factor 16.5. **  ⌗ And the cost is '
      'essentially independent of the mode count -- five wavenumbers to eta = 1000 cost 40.4 s and '
      '220 to eta = 914 cost 40.8 -- so the expensive axis is the END TIME, which is why eta_0 is '
      'recorded UNMEASURED rather than extrapolated',
      abs(_c914['seconds'] - 40.8) < 0.045 and abs(_c4000['seconds'] - 667.0) < 0.045
      and _c914['n_modes'] == 220 and _c4000['n_modes'] == 220
      and COST['r7848_record']['records_its_etaref'] is False
      and abs(COST['r7848_record']['nearest_ratio'] - 1.011) < 0.00045
      and abs(_c4000['seconds'] / COST['r7848_record']['phi_seconds'] - 16.5) < 0.045
      and 'unmeasured' in json.dumps(COST['five_mode_probe']),
      '40.8 s at z = 188 and 667.0 s at z = 12.8, against a record of %.2f s with no ETAREF'
      % COST['r7848_record']['phi_seconds'])

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# ⌷  EVERY FIGURE THIS REVISION'S INDEX ROW PRINTS, PINNED TWO-SIDED AGAINST WHAT MEASURED IT
_pins = {
    'limit': abs(_lim - 100.402) < 0.0045,
    'limit_mcse': abs(_se - 0.353) < 0.00045,
    'r7848_limit': abs(_olim - 111.383) < 0.0045,
    'r7848_limit_mcse': abs(_ose - 0.409) < 0.0045,
    'limit_improvement': abs((_olim - _lim) - 10.981) < 0.0045,
    'effective': abs(_eff - 21.913) < 0.0045,
    'effective_sd': abs(_effsd - 44.423) < 0.0045,
    'r7848_effective': abs(_oeff - 44.253) < 0.0045,
    'r7848_effective_sd': abs(_oeffsd - 39.792) < 0.0045,
    'sigma_above_ceiling': abs(_above - 11.61) < 0.0045,
    'r7848_sigma_above_ceiling': abs(_oabove - 36.91) < 0.0045,
    'from_published': abs(_from_pub - 2.767) < 0.00045,
    'r7848_from_published': abs(_ofrom_pub - 3.650) < 0.00045,
    'published_limit': abs(CTRL['published']['limit_mev'] - 64.2) < 0.045,
    'published_eff': abs(CTRL['published']['effective_ev'] - -0.101) < 0.00045,
    'order_ceiling_is_the_factor_the_order_names':
        abs(ORDER_BAND_MEV[1] / PUBLISHED_LIMIT_MEV - 1.5) < 0.00045,
    'chi2_min': abs(_b['best_fit']['chi2'] - 570.3427) < 0.00045,
    'r7848_chi2_min': abs(_ob['best_fit']['chi2'] - 576.0427) < 0.00045,
    'placement_59': abs(_b['frac_below_0.059'] * 100.0 - 70.5125) < 0.0045,
    'placement_64': abs(_b['frac_below_0.064'] * 100.0 - 75.2014) < 0.0045,
    'carry_spread_best': abs(min(_spreads) - 0.3206) < 0.0045,
    'carry_spread_worst': abs(max(_spreads) - 0.6295) < 0.0045,
    'criterion': abs(CARRY['criterion'] - 0.023) < 0.00045,
    'r7848_matter_only_spread': abs(CARRY['r7848_matter_only_spread'] - 0.2276) < 0.0045,
    'restricted_floor': abs(_floor - 0.0037771) < 4.5e-07,
    'radiation_share_at_production_handover': abs(_rad - 0.00401) < 4.5e-06,
    'radiation_share_at_the_earliest_handover':
        abs(ISO['handovers'][0]['radiation_over_matter'] - 0.1401) < 4.5e-05,
    'camb_worst_bin': abs(max(abs(v) for v in CAMB['in_bin_sigma']) - 1.34) < 0.0045,
    'normalisation_miss_r7848': abs(NORM['miss_r7848_pc'] - 9.04) < 0.0045,
    'restricted_at_one_per_cent': abs(float(_t['0.01']['spread']) - 0.0224) < 0.0045,
    'two_species_identity': abs(max(
        t['worst_relative_difference_from_one_species'] for t in _ts) - 2.298e-12) < 4.5e-16,
    'baryon_ratio_high_k': abs(ISO['handovers'][0]['baryons']['at_k_max'] - 0.0101) < 4.5e-05,
    'chi2_per_dof_quadrature': abs(_q['chi2_per_dof'] - 2.048681) < 4.5e-07,
    'chi2_per_dof_instrument': abs(_i['chi2_per_dof'] - 2.131182) < 4.5e-07,
    'asymptote_ratio': abs(GFI['ratio_to_textbook'] - 0.294419) < 4.5e-07,
    'r7848_asymptote_ratio': abs(OLDINFO['amp_ratio_preferred_over_cmb'] - 0.909563) < 4.5e-07,
    'd4_registered': abs(D4_REGISTERED - 0.667) < 0.00045,
    'f_nu': abs(GFI['f_nu'] - 0.0225069) < 4.5e-08,
    'normalisation_ratio_r7848': abs(NORM['ratio_r7848'] - 0.909563) < 4.5e-07,
    'normalisation_ratio_r7850': abs(NORM['ratio_r7850'] - 0.974476) < 4.5e-07,
    'normalisation_miss': abs(NORM['miss_r7850_pc'] - 2.55) < 0.0045,
    'camb_chi2': abs(CAMB['chi2_nothing_fitted'] - 8.8173) < 0.00045,
    'camb_amplitude': abs(CAMB['fitted_amplitude'] - 1.002494) < 4.5e-07,
    'camb_ratio_min': abs(_ratio.min() - 0.8410) < 4.5e-05,
    'camb_ratio_max': abs(_ratio.max() - 1.1294) < 4.5e-05,
    'instrument_chi2_quadrature': abs(_inst['r7848_quadrature_ics']['chi2_free'] - 16.3894) < 0.00045,
    'instrument_chi2_instrument': abs(_inst['r7850_instrument_ics']['chi2_free'] - 17.0507) < 0.00045,
    'shape_vs_camb_quadrature_max': abs(_shape_q.max() - 0.2723) < 4.5e-05,
    'shape_vs_camb_instrument_max': abs(_shape_i.max() - 0.2802) < 4.5e-05,
    'rhat': abs(_rhat - 1.0001) < 4.5e-05,
    'ess': abs(_ess - 44608) < 0.45,
    'accept': abs(_b['accept'] - 0.2440) < 4.5e-05,
    'per_chain_span': abs(_span - 1.088) < 0.0045,
    'cost_914': abs(_c914['seconds'] - 40.8) < 0.045,
    'cost_4000': abs(_c4000['seconds'] - 667.0) < 0.045,
    'cost_understated_by': abs(_c4000['seconds'] / COST['r7848_record']['phi_seconds'] - 16.5)
                           < 0.045,
}
check('⌷ every figure this revision\'s INDEX row prints is pinned TWO-SIDED here, each tolerance '
      'inside the coarser of half its last printed digit and 0.05 per cent, against the quantity '
      'that MEASURED it.  ** The pins are explicit literal comparisons, not calls to a helper, '
      'because a figure held only by a helper is not held where the gate that polices the row can '
      'see it **',
      all(_pins.values()),
      '%d figure(s) pinned, from the carry, the isolation, the asymptote, the normalisation, the '
      'control, the CAMB reference and the cost' % len(_pins)
      if all(_pins.values())
      else 'UNPINNED: ' + ', '.join(k for k, v in _pins.items() if not v))

# ─────────────────────────────────────────────────────────────────────────────────────────────────
# Ⓚ⑪  THE COUNT
_ran = 11
check('Ⓚ⑪ the count: this receipt adjudicates all %d registered arms.  FOUR are reported FAILED or '
      'NOT JUDGED with their criteria exactly as registered -- Ⓐ① because its own identity does not '
      'range over the band it was written for, Ⓒ③ because the shape got worse, Ⓓ④ because the '
      'missing suppression is not the initial conditions\' to recover, and Ⓗ⑧ because it was '
      'conditional on Ⓕ⑥.  ONE holds outright: Ⓔ⑤.  ** And the arm that was supposed to wait for '
      'another seat, Ⓖ⑦, is answered by measurement instead, and it is the one that moves the '
      'fault **' % _ran,
      _ran == 11 and PRED.count('**Ⓚ⑪') == 1 and PRED.count('**Ⓖ⑦') == 1,
      '%d arm-check(s) failed' % len(fail))

print()
if not fail:
    print('  r7850 OK -- every arm holds, and the registered failures are ASSERTED rather than '
          'suffered:')
    print('    => Ⓐ①: the handover belongs LATE, not early; the carry\'s error is the radiation '
          'share at it, flooring at %.3e against a share of %.5f.' % (_floor, _rad))
    print('    => Ⓕ⑥: %.3f +/- %.3f meV and %+.1f meV, so both halves fail -- and the limit '
          'improved %.3f meV.' % (_lim, _se, _eff, _olim - _lim))
    print('    => Ⓔ⑤: the normalisation miss falls from %.2f per cent to %.2f.'
          % (NORM['miss_r7848_pc'], NORM['miss_r7850_pc']))
    print('    => Ⓖ⑦: CAMB fits the nine bandpowers at chi^2 %.4f with nothing fitted, so the shape '
          'error is this instrument\'s.' % CAMB['chi2_nothing_fitted'])
    print('    => Ⓗ⑧: NOT JUDGED, as registered.  P15 is not touched.')
    sys.exit(0)
print('  ⛔ %d arm(s) failed: %s' % (len(fail), fail))
sys.exit(1)
