#!/usr/bin/env python3
"""r7856 (60), on order `r7853`: the absolute lensing scale located -- two factor-two errors that
cancelled, and the baryon repair broke the cancellation.

COMPUTES: the ratio of this instrument's repaired lensing power to the independent reference's, bin
by bin at the control's fixed cosmology; the primordial normalisation the lensing path never carried,
derived from the instrument's own seed and checked against the reference's absolutely normalised
Weyl potential power; the amplitude the joint fit hands from the CMB side to the lensing side; and
which of the two sides carries the factor two between them.  ** It pins NO cosmological parameter as
a result, and it WITHDRAWS a reading rather than offering one: `r7854`'s 598 meV is reported here as
an artefact of a broken cancellation and no replacement limit is computed. **

⌷ ** THE ID. **  69 ordered this work as `r7853`, which merged `r7854` with this seat's three
patches to `cc66`'s provenance receipts applied and ruled that the control's target is `cc66`'s CAMB
reference scored on the same likelihood as this harness.  This revision's directory, its
PREDICTION.md (committed and pushed at `ca690af46`, amended at `fd524dd6c`, both before a line of
the computation existed) and this receipt carry `r7856`.

** THE RESULT. **  After `r7854`'s baryon repair the instrument-over-reference ratio is flat to 1.86
per cent across the nine bandpowers against the landed instrument's 33.20, so the order's ① is
answered: what is left is ONE NUMBER.  The lensing path carries the tilt unpivoted and no amplitude
at all, and the missing factor follows from the instrument's own seed -- `(4/9) A_s k_p^(1-ns)`,
which agrees with the reference's own absolutely normalised Weyl power to 0.13 per cent on the
super-horizon modes with nothing fitted on either side.  ⇒ ** But the joint fit does not lack a
normalisation: it hands over one that is twice too big, ** and the carrier is measured rather than
inferred -- the CMB bank's binned TT at the derived normalisation is 0.504672 of CAMB's own over 185
bins, range 0.500015 to 0.510557.  ⇒ ** So `r7852`'s cancellation is named in both factors: ** the
CMB bank is 2x low so its fitted amplitude is 2x high, and the landed instrument's lensing power was
2x low because the baryons never clustered.  The repair broke the cancellation and the joint fit
bought the excess lensing back with the only knob it has.

⛔ ** FOUR THINGS FAIL OR ARE WITHDRAWN, AND THREE OF THEM ARE THIS SEAT'S OWN. **  Ⓐ①ᶜ's registered
expectation is REFUTED -- the repair moved the scale TOWARD the reference, which was invisible until
the normalisation existed.  Ⓐ①ᵈᵖʳᵉ's conclusion is WITHDRAWN -- that arm's own test omitted the
`T_CMB^2` conversion the joint model itself applies.  Ⓑ②ᵃ's share bound holds and its ATTRIBUTION is
refuted by the sign of its trend.  Ⓑ②ᶜ passes BY CONSTRUCTION and is reported as vacuous.  And Ⓒ③
FAILS its registered bin clause at 0.1528 against 0.10, with the criterion unmoved.

STATUS: OK
rc=0 on success.  Run: NODE=60 python3 <this file>   (numpy; a few seconds, reads banked json)
"""
import io
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
RUN = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                   'r7856_60_the_lensing_powers_absolute_scale_located_and_sized')
BTW = os.path.join(ROOT, 'computations', 'beyond_the_wall')


# ⛔ *Two bare-token pins were cut from this file before it landed: `'PRIMNORM' in PHIPHI` and
#   `'withdrawn' in RESULT`.  A bare presence test on a token is the vacuous form this corpus's own
#   sweep keeps catching -- it caught `'BVEL'` on this line one revision ago -- and in both cases a
#   SENTENCE carrying the same claim was already available: the switch's `os.environ` line, which
#   proves the name exists AND that it defaults off, and the document's own
#   "this arm's conclusion is withdrawn".*


def rd(name):
    with io.open(os.path.join(RUN, name), encoding='utf-8') as fh:
        return json.load(fh)


RESULT = ' '.join(io.open(os.path.join(RUN, 'RESULT.md'), encoding='utf-8').read().split())
PHIPHI = ' '.join(io.open(os.path.join(
    BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_lensing_bandpowers',
    'phiphi.py'), encoding='utf-8').read().split())
S = rd('summary.json')

fail = []


def check(label, cond, detail=''):
    ok = bool(cond)
    print('  %s %s' % ('✔' if ok else '✘', label))
    if detail:
        print('      %s' % detail)
    if not ok:
        fail.append(label.split()[0])
    return ok


print()
print('=' * 100)

# ── Ⓞ⓪ the controls
_c = S['O0']
check('Ⓞ⓪ THE POSITIVE CONTROL: this revision reproduces r7854\'s banked record before it reads '
      'anything -- the landed fitted factor 1.5768615382e-09 and per dof 2.1313389647, the repaired '
      '8.1642357010e-10 and 1.0533934590, each to a relative 1e-6, and r7850\'s reference at '
      '8.8173475455 with nothing fitted and 1.0024938505 with one amplitude.  ** Nothing below is a '
      'reading of the scale until this holds **',
      _c['holds'] is True
      and abs(_c['landed_amp'] - 1.5768615382253947e-09) < 1e-6 * 1.5768615382253947e-09
      and abs(_c['repaired_per_dof'] - 1.0533934590398568) < 1e-6,
      'landed %.10e / %.10f, repaired %.10e / %.10f'
      % (_c['landed_amp'], _c['landed_per_dof'], _c['repaired_amp'], _c['repaired_per_dof']))

_s = S['O0b']
check('Ⓞ⓪ᵇ AND THE REPAIR IS BEHIND A DEFAULT-OFF SWITCH, PROBED IN A CHILD PROCESS AND NOT '
      'ASSERTED: `PRIMNORM` reads False unset and True set, and the constant it applies is the '
      'derived one.  *The same discipline r7854 used for `BVEL`, for the same reason: an edit to a '
      'shared path owes the reader a statement, in the code, that it changes nothing until asked*',
      _s['holds'] is True and _s['unset'] == 'False' and _s['set'] == 'True'
      and "os.environ.get('PRIMNORM', '0') == '1'" in PHIPHI,
      'unset -> %s, set -> %s' % (_s['unset'], _s['set']))

# ── Ⓐ① the ratio is one number
_a1 = S['A1']
check('Ⓐ① PASSES AS REGISTERED: the repaired instrument over the reference is ONE NUMBER, flat to '
      '1.86 per cent across the nine bandpowers against a registered 10, where the landed '
      'instrument drifts 33.20 per cent.  ⇒ So what r7852 and r7854 left is a NORMALISATION and '
      'not a shape at the bandpower level',
      _a1['passes'] is True and _a1['repaired_worst'] < 0.10
      and abs(_a1['repaired_worst'] - 0.0186) < 5e-4
      and abs(_a1['landed_worst'] - 0.3320) < 5e-4
      and _a1['criterion'] == 0.10,
      'repaired worst %.4f, landed worst %.4f' % (_a1['repaired_worst'], _a1['landed_worst']))

_a1b = S['A1b']
check('Ⓐ①ᵇ ⚠ PASSED AS REGISTERED AND VACUOUS IN THE DIRECTION IT WAS AIMED, which this revision\'s '
      'own amendment registered BEFORE measuring it: r_bar is not within ten per cent of 2, and the '
      'passing means nothing because r_bar is 1/the fitted factor to 0.52 per cent -- the '
      'instrument\'s missing normalisation and not a gap',
      _a1b['passes_as_registered'] is True
      and _a1b['vacuous_in_the_direction_aimed'] is True
      and abs(_a1b['rbar_times_fitted_factor'] - 1.0) < 0.01,
      'r_bar x the fitted factor = %.6f, a departure from one of %.4f per cent'
      % (_a1b['rbar_times_fitted_factor'], 100 * abs(_a1b['rbar_times_fitted_factor'] - 1)))

_a1c = S['A1c']['revisited']
check('Ⓐ①ᶜ ⚠ THE REGISTERED EXPECTATION IS REFUTED: this seat registered that the repair moved the '
      'absolute scale AWAY from the reference and it moved it TOWARD -- from 0.5330 of the data to '
      '1.0294.  ** The refutation was invisible until the normalisation existed: ** all the first '
      'file could see was the raw vector growing by 1.9939, and a raw vector growing does not say '
      'which way the scale went.  The criterion is unchanged',
      _a1c['registered_expectation_refuted'] is True and _a1c['moved_toward'] is True
      and abs(_a1c['before'] - 0.532975) < 5e-5 and abs(_a1c['after'] - 1.029402) < 5e-5,
      'before %.6f, after %.6f' % (_a1c['before'], _a1c['after']))

_pre = S['A1d_pre']
check('Ⓐ①ᵈᵖʳᵉ ⚠ THIS ARM\'S CONCLUSION IS WITHDRAWN, in the record and not quietly: it measured '
      'A_cmb 1.1111821251e+04 against A_lens 8.1642357010e-10 and concluded the two sides were '
      'never put on one AMP.  ** model6.pp_model hands one across and applies the T_CMB^2 '
      'conversion the arm omitted, so the sides ARE joined ** -- the measured numbers stand and it '
      'is the reading of them that was wrong',
      _pre['withdrawn'] is True
      and abs(_pre['as_measured']['A_cmb'] - 1.1111821251e+04) < 1e-2
      and _pre['as_measured']['holds'] is False
      and "this arm's conclusion is withdrawn" in RESULT.lower(),
      'A_cmb %.10e, and the withdrawal is carried in handover.py\'s own header'
      % _pre['as_measured']['A_cmb'])

# ── Ⓐ①ᵈ one AMP, three readings
_d = S['A1d']
check('Ⓐ①ᵈ PASSES AS REGISTERED, on the arm the amendment added: ONE AMP read three ways disagrees '
      'by a factor 2.041179.  The CMB side hands over 1.6664668460e-09, the instrument\'s own seed '
      'implies 8.4042841352e-10, and the nine bandpowers want 8.1642357010e-10 -- so the seed and '
      'the data agree to 2.94 per cent and the HANDOVER is the reading that is out',
      _d['A1d_passes'] is True and abs(_d['handed_over_r_wanted'] - 2.041179) < 5e-5
      and abs(_d['derived_r_wanted'] - 1.029402) < 5e-5
      and abs(_d['handed_over_r_derived'] - 1.982878) < 5e-5,
      'handed/wanted %.6f, handed/derived %.6f, derived/wanted %.6f'
      % (_d['handed_over_r_wanted'], _d['handed_over_r_derived'], _d['derived_r_wanted']))

# ── Ⓑ②ᵇ the carrier and its independent check
_b = S['B2b']
check('Ⓑ②ᵇ HOLDS AS REGISTERED AND ITS CHECK IS INDEPENDENT OF EVERY FIT: the normalisation '
      'derived from the instrument\'s OWN seed -- (4/9) A_s k_p^(1-ns), the (4/9) from |Phi| = '
      '(2/3)|zeta| in the regime `Ph0 = -1, dg0 = -2 Ph0, dc0 = 0.75 dg0` sets -- puts the '
      'instrument on the reference\'s absolutely normalised Weyl power to 0.13 PER CENT on the '
      'super-horizon modes, with nothing fitted on either side, and it carries 0.9193 of the gap',
      _b['holds'] is True and _b['share'] > 0.50
      and abs(_b['superhorizon_check'] - 1.0013) < 5e-4
      and abs(_b['mean_ratio_landed'] - 0.500060) < 5e-5
      and abs(_b['derivation']['amp'] - 8.4042841352e-10) < 1e-6 * 8.4042841352e-10,
      'super-horizon %.4f, share %.4f, the landed instrument\'s sub-horizon deficit %.6f'
      % (_b['superhorizon_check'], _b['share'], _b['mean_ratio_landed']))

_a = S['B2a']
check('Ⓑ②ᵃ ⚠ THE SHARE BOUND HOLDS AND THE ATTRIBUTION IS REFUTED BY THE SIGN OF ITS OWN TREND: the '
      'remainder is at most 0.0807 of the gap, so the registered "less than a fifth" holds -- but a '
      'radiation-era residual DIES with the radiation share and this one GROWS, 1.03498 at a share '
      'of 0.14014 to 1.05211 at 0.00401.  ⇒ So the order\'s first candidate is bounded AND refused',
      _a['holds'] is True and _a['share_at_most'] < 0.20
      and _a['attribution_refuted'] is True
      and _a['trend_last'] > _a['trend_first'],
      'share at most %.4f; the ratio runs %.5f at a radiation share of %.5f to %.5f at %.5f'
      % (_a['share_at_most'], _a['trend_first'], _a['rad_first'], _a['trend_last'], _a['rad_last']))

check('Ⓑ②ᵃᶜᵒⁿᶠ AND THAT RESIDUAL IS LARGER THAN ITS OWN CONFOUND, reconstructed from the '
      'instrument\'s OWN line rather than taken as negligible: `Psi = Phi - 6 Hc^2 (Onv sig)/k^2` '
      'gives |Phi-Psi|/Phi at most 0.00053 over the sub-horizon modes against a residual of '
      '0.05211, a hundredth of it.  *A residual smaller than its own confound is not a measurement*',
      _a['confound']['residual_exceeds_confound'] is True
      and _a['confound']['worst_phi_minus_psi_over_phi'] < 1e-3,
      'confound %.5f against residual %.5f' % (_a['confound']['worst_phi_minus_psi_over_phi'],
                                               _a['confound']['residual_at_last_eta']))

_c2 = S['B2c']
check('Ⓑ②ᶜ ⚠ PASSES BY CONSTRUCTION AND IS REPORTED AS VACUOUS: the pair sums to 1.0000 against a '
      'criterion of 0.80, which is an IDENTITY because the normalisation\'s share was formed as '
      '1 minus the residual\'s.  *The content is the two shares, each measured, with nothing left '
      'unaccounted; the arm as coded could not have failed and this row says so rather than '
      'claiming it*',
      _c2['passes'] is True and _c2['vacuous_by_construction'] is True
      and abs(_c2['pair'] - 1.0) < 1e-9,
      'pair %.4f, and the arm could not have failed as coded' % _c2['pair'])

# ── Ⓒ③ the repair
_c3, _c3b = S['C3'], S['C3b']
check('Ⓒ③ FAILS AS REGISTERED ON ITS BIN CLAUSE AND THE CRITERION IS NOT MOVED: worst |ratio - 1| '
      'is 0.1528 against a registered 0.10.  ** What the clause asked for is tighter than the data '
      'can resolve ** -- the deviations at the four bins that carry it are +1.49, +1.60, +1.30 and '
      '-1.29 in units of each bin\'s OWN sigma -- and the chi^2 clause, which weights by those '
      'errors, passes at 1.1132 of the reference\'s against a registered 1.20',
      _c3['passes'] is False
      and abs(_c3['worst_ratio_minus_one'] - 0.1528) < 5e-4
      and _c3['fraction_of_reference'] < 1.20
      and abs(_c3['fraction_of_reference'] - 1.1132) < 5e-4,
      'worst ratio %.4f against 0.10; chi2 %.4f of the reference\'s against 1.20'
      % (_c3['worst_ratio_minus_one'], _c3['fraction_of_reference']))

check('Ⓒ③ᵃᵃᵃ ⇒ AND WITH NOTHING FITTED ANYWHERE THE INSTRUMENT LANDS ON THE NINE BANDPOWERS '
      'ABSOLUTELY FOR THE FIRST TIME: the repaired shape at the derived amplitude scores 8.4297 '
      'against the reference\'s own 8.8173, where the repaired shape at the HANDED-OVER amplitude '
      'scores 1551.7312 and the landed shape at the derived amplitude 340.8400.  ** The ordering of '
      'those four numbers is the whole finding **',
      abs(_c3['chi2_repaired_nothing_fitted'] - 9.815333) < 5e-5
      and abs(S['cancellation']['chi2']['the REPAIRED shape at the derived amplitude'] - 8.4297)
      < 5e-4
      and S['cancellation']['chi2']['the REPAIRED shape at the handed-over amplitude'] > 1000.0
      and S['cancellation']['chi2']['the REPAIRED shape at the derived amplitude']
      < S['cancellation']['chi2_reference'],
      'repaired x derived %.4f, below the reference\'s %.4f; repaired x handed %.1f'
      % (S['cancellation']['chi2']['the REPAIRED shape at the derived amplitude'],
         S['cancellation']['chi2_reference'],
         S['cancellation']['chi2']['the REPAIRED shape at the handed-over amplitude']))

check('Ⓒ③ᵇ AND THE FREE AMPLITUDE IS REFUSED THE CLAIM: with one fitted the repaired vector scores '
      '8.427148 at a factor 0.971437, only 0.0286 from one, so the free amplitude is NOT what makes '
      'the repair land -- and Ⓒ③ above is scored at a factor of exactly one.  *r7854 reported 1.0534 '
      'per dof WITH an amplitude free and the reference\'s 8.8173 has nothing free; this revision '
      'does not compare those two numbers*',
      abs(_c3b['fitted_factor'] - 0.971437) < 5e-6
      and _c3b['factor_distance_from_one'] < 0.05,
      'the fitted factor is %.6f, %.4f from one' % (_c3b['fitted_factor'],
                                                    _c3b['factor_distance_from_one']))

# ── Ⓓ④ᵃ the carrier, measured
_d4 = S['D4a']
check('Ⓓ④ᵃ THE CARRIER IS MEASURED AND NOT INFERRED, because elimination is not a measurement: the '
      'CMB bank\'s binned TT at the derived normalisation, times T_CMB^2 and exp(-2 tau), is '
      '0.504672 of CAMB\'s own lensed TT through this harness\'s own plik_lite windows at the same '
      'cosmology and the same A_s -- over 185 bins, range 0.500015 to 0.510557.  ⇒ ** THE CMB BANK '
      'IS LOW BY A FACTOR OF TWO AND THE LENSING SIDE IS SOUND **',
      _d4['bank_low_by_about_two'] is True and _d4['carrier_named'] is True
      and abs(_d4['geometric_mean'] - 0.504672) < 5e-6
      and _d4['n_bins'] == 185 and _d4['ratio_min'] > 0.499 and _d4['ratio_max'] < 0.52,
      '%d bins, geometric mean %.6f, range %.6f .. %.6f'
      % (_d4['n_bins'], _d4['geometric_mean'], _d4['ratio_min'], _d4['ratio_max']))

check('Ⓓ④ᵃᵃ ⇒ SO r7852\'S CANCELLATION IS NAMED IN BOTH OF ITS FACTORS, each measured against the '
      'independent pipeline and neither assumed: the CMB bank is 2x low so its fitted amplitude is '
      '2x high (handed over at 1.982878 of what the seed implies), and the landed instrument\'s '
      'lensing power was 0.500060 of what it should be because the baryons never clustered.  ** The '
      'two cancelled, r7854 repaired the baryons, and the cancellation broke **',
      abs(S['cancellation']['handover_over_derived'] - 1.982878) < 5e-5
      and abs(_b['mean_ratio_landed'] - 0.500060) < 5e-5
      and abs(S['cancellation']['handover_over_derived'] * _b['mean_ratio_landed'] - 1.0) < 0.06,
      'the product of the two factors is %.4f, so they cancelled to %.1f per cent'
      % (S['cancellation']['handover_over_derived'] * _b['mean_ratio_landed'],
         100 * abs(S['cancellation']['handover_over_derived'] * _b['mean_ratio_landed'] - 1)))

# ── Ⓓ④ the fork
_f = S['D4']
check('Ⓓ④ IS NOT ANSWERED AND IS ROUTED AS THE FORK THIS REVISION REGISTERED BEFORE COMPUTING, not '
      'as a discovery: the lensing path\'s own repair is landed, and the remaining factor two is in '
      'the SHARED CMB bank that every CMB score on this paper reads, so it is not "re-run the '
      'control only".  ⛔ ** And no limit is reported here: ** a limit read off a configuration this '
      'revision reports as wrong by a factor two would not be a measurement',
      _f['answered'] is False and _f['routed'] is True
      and 'routed' in _f['reason'] and 'shared cmb bank' in _f['reason'].lower(),
      'the fork is stated in FOR_66_FROM_60.md with both branches and this seat\'s recommendation')

_e = S['E5']
check('Ⓔ⑤ AND A READING IS WITHDRAWN RATHER THAN REPLACED: r7854\'s 598 meV is reported here as an '
      'artefact of the broken cancellation and NO replacement limit is offered.  P15 is untouched '
      'by this revision, the arm of record is NOT JUDGED, 72\'s batch still waits, and nothing is '
      'concluded about the neutrino mass sum',
      _e['nothing_concluded_about_the_neutrino_mass'] is True
      and _e['arm_of_record_judged'] is False and _e['p15_touched'] is False
      and _e['batch_72_waiting'] is True
      and 'withdrawn as a reading' in RESULT.lower(),
      'the document carries the withdrawal and not a replacement figure')

# ── Ⓙ every figure the INDEX row prints, pinned HERE as EXPLICIT literal comparisons
#   ⛔ *The first version of this row carried the eight literals in a tuple and compared against
#   them in a loop.  `check_figures_pinned` reads the SOURCE and could not see a pin at all -- it
#   called every one of the eight unpinned, and it was right to: a comparison against a variable
#   is not a pin even when the variable happens to hold the right number.  They are written out.*
_sh = 100.0 * abs(S['B2b']['superhorizon_check'] - 1.0)
_w_rep = 100.0 * S['A1']['repaired_worst']
_w_land = 100.0 * S['A1']['landed_worst']
_prod = S['cancellation']['handover_over_derived'] * S['B2b']['mean_ratio_landed']
_cz = S['cancellation']['chi2']
_rep_handed = _cz['the REPAIRED shape at the handed-over amplitude']
_land_derived = _cz['the LANDED shape at the derived amplitude']
_ref = S['cancellation']['chi2_reference']
_bank_max = S['D4a']['ratio_max']
_bank_gm = S['D4a']['geometric_mean']
_rep_derived = _cz['the REPAIRED shape at the derived amplitude']
for _n, _v in (('the super-horizon agreement, per cent', _sh),
               ("the repaired ratio's spread, per cent", _w_rep),
               ("the landed ratio's spread, per cent", _w_land),
               ("the CMB bank's geometric mean over 185 TT bins", _bank_gm),
               ("the CMB bank's worst TT bin", _bank_max),
               ('the product of the two factors', _prod),
               ('the repaired shape at the handed-over amplitude', _rep_handed),
               ('the landed shape at the derived amplitude', _land_derived),
               ('the repaired shape at the derived amplitude', _rep_derived),
               ('the reference, nothing fitted', _ref)):
    print('      %-50s %18.10f' % (_n, _v))
check('Ⓙ EVERY FIGURE THE `INDEX` ROW PRINTS IS PINNED HERE, each as an explicit literal comparison '
      'to half its last printed digit and in the units the row prints it in -- ten of them, from '
      'the super-horizon agreement and both ratio spreads through the CMB bank\'s mean and worst '
      'bin, the cancellation\'s product and all four scores.  ** So no figure cited to this receipt '
      'can be wrong and leave it green **',
      abs(_sh - 0.13) < 0.005
      and abs(_sh / 100.0 - 0.0013) < 4.9e-05
      and abs(_w_rep - 1.86) < 0.005
      and abs(_w_rep / 100.0 - 0.0186) < 4.9e-05
      and abs(_w_land - 33.20) < 0.0166
      and abs(_w_land / 100.0 - 0.3320) < 4.9e-04
      and abs(_bank_gm - 0.504672) < 2.5e-04
      and abs(_bank_max - 0.510557) < 2.5e-04
      and abs(_prod - 0.9916) < 4.9e-04
      and abs(_rep_handed - 1551.7312) < 0.775
      and abs(_land_derived - 340.8400) < 0.170
      and abs(_rep_derived - 8.4297) < 4.2e-03
      and abs(_ref - 8.8173) < 4.4e-03,
      'ten printed figures, each pinned to half its last digit -- and each PER CENT figure pinned in its fraction too, because the gate reads `X per cent` as both X and X/100')

print()
print('=' * 100)
print()
if not fail:
    print('  ✔ r7856: the absolute scale is located, and it is two factor-two errors that '
          'cancelled.')
    print('    => the lensing path had no primordial normalisation; the derived one agrees with '
          'the reference to 0.13 per cent super-horizon with nothing fitted.')
    print('    => the CMB bank is 0.504672 of the reference over 185 TT bins, so its fitted '
          'amplitude is twice too big and the handover passes that on.')
    print('    => with both accounted the instrument scores %.4f on the nine bandpowers with '
          'nothing fitted, below the reference\'s %.4f.'
          % (S['cancellation']['chi2']['the REPAIRED shape at the derived amplitude'],
             S['cancellation']['chi2_reference']))
    print('    => Ⓒ③ FAILED its bin clause with the criterion unmoved, Ⓐ①ᶜ\'s expectation is '
          'refuted, Ⓐ①ᵈᵖʳᵉ\'s conclusion is withdrawn, and Ⓑ②ᶜ is vacuous by construction.')
    print('    => r7854\'s 598 meV is WITHDRAWN as a reading; P15 is untouched, the arm of record '
          'is NOT JUDGED, and 72\'s batch still waits.')
    sys.exit(0)
print('  ⛔ %d arm(s) failed: %s' % (len(fail), fail))
sys.exit(1)
