# -*- coding: utf-8 -*-
"""⛭⛭⛭ THE MASSIVE-NEUTRINO BACKGROUND IS REPAIRED IN THE MODEL, THE DRAG RULER MOVES WITH THE SUM
WHERE IT WAS EXACTLY FLAT, AND `r7862`'s SECOND BASIN DOES NOT SURVIVE THE REPAIR.

COMPUTES: three degenerate neutrino states of mass `Sum/3` at `T_nu = (4/11)^(1/3) T_gamma` given
their Fermi-Dirac energy density at each epoch and carried through both rate functions, the
conformal-time grid, the sound horizon, the drag epoch and the distances behind a switch that is
default off; the species taken OUT of the two places the stack counted it and the exact term added
back, so it is counted once; that construction validated against the reference before use; the five
provenance keys `r7861` ③ ordered batched, paid here because this revision moves the blob; and both
limits re-read on the repaired ruler.
** IT PINS TWO LIMITS AS RESULTS: `69.97` meV with the ruler minimised and `81.94` meV calibrated on
this instrument's OWN repaired drag epoch, both 95 per cent one-sided, against the reference's
`54.00` and `30.56`.  Both are reported as a COMPARISON, as registered before the numbers existed,
and both are read on the BANKED SPECTRA WITH THE RULER REPAIRED and not on a re-solved bank -- which
this receipt PROVES from the bank's own recorded config rather than asserting. **

⌷ ** THE ID. **  `69` ordered this as `r7863`, which merged `r7862`, accepted this line's
recommendation not to patch the ruler from the reference's pipeline, and ruled the stronger thing:
that the background itself is repaired now rather than carried as a standing gap.

⛭ ** WHAT IS NEW HERE, AND WHAT IS NOT. **  That the instrument counts the neutrino mass as matter
at every epoch is `r7862`'s finding, and the instrument named the double-count in its own text
before either.  What this revision adds is the Fermi-Dirac background, its validation, the keys, and
both limits re-read on it.

⚠ ** FIVE THINGS IN THIS RECORD ARE THIS SEAT'S OWN DEFECTS, EACH FOUND BY MEASURING RATHER THAN BY
READING, AND THREE REGISTERED BANDS FAIL AND ARE REPORTED AS FAILURES WITH THEIR CRITERIA UNMOVED. **

    NODE=60 python3 <this file>

Written r7864 (60).  Stated for reversal.
"""
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
D = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                 'r7864_60_the_massive_neutrino_background_given_its_fermi_dirac_density_and_both_'
                 'limits_re_read')
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

V = load('validate.json')
L = load('limits.json')
RESULT = ' '.join(io.open(os.path.join(D, 'RESULT.md'), encoding='utf-8').read().split())
PRED = ' '.join(io.open(os.path.join(D, 'PREDICTION.md'), encoding='utf-8').read().split())
with io.open(os.path.join(ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py'),
             encoding='utf-8') as fh:
    INST = ' '.join(fh.read().split())

# ── Ⓐ① THE BACKGROUND ───────────────────────────────────────────────────────────────────────────
check('Ⓐ①ᵃ and Ⓐ①ᵃᵃ THE TWO INERTNESS CLAIMS, which are two different claims, BOTH HOLD '
      'BIT-IDENTICALLY: with the switch off every reported value is the landed one, and with it ON '
      'AT ZERO SUM every one is still the landed one -- the sound horizon, both rate functions at '
      'four scale factors each, the density at four more, and both ends of the stack.  ⌗ The second '
      'holds BY CONSTRUCTION: the factor is the Fermi-Dirac energy integral over its own zero-mass '
      'value, exactly 1.0 there, so the expression reduces to the landed line rather than agreeing '
      'with it to the precision of two normalisations',
      V['inert']['holds'] is True
      and all(V['inert']['identical'][k] for k in
              ('R_S', 'Hleaf', 'Hphys', 'Onu', 'rt_head', 'rt_tail'))
      and V['inert']['off']['R_S'] == V['inert']['on_zero']['R_S'],
      'six quantities bit-identical on both claims')

check('Ⓐ①ᵃᵇ ⛔ and the switch REQUIRES a nonzero mass, because a first version asked only whether it '
      'was set and the stack\'s late tail then differed at zero sum -- not from the physics but '
      'because SPLITTING A SUM AND ADDING IT BACK IS NOT THE IDENTITY IN FLOATING POINT: near a = 1 '
      'the radiation term is a tiny addition to the matter and vacuum terms and the last bits do '
      'not survive the re-association.  At zero mass the repair IS the identity, so the switch is '
      'given nothing to do',
      'splitting a sum and adding it back is not the identity in floating point' in INST.lower()
      and 'at zero mass the repair is the identity' in INST.lower()
      and "float(os.environ.get('MNU', '0.0')) != 0.0" in INST,
      'the flag is conditioned on the mass and the reason is in the file')

_B = L['precondition']
check('Ⓐ①ᵉ THE BOOKKEEPING: the species is counted ONCE.  The total at a = 1 differs from the '
      'landed total by the double-count removed PLUS the convention gap, and the residual closes '
      'to %.2e or better at every sum.  ⛔ A first version of this gate expected only the '
      'double-count and so could not have closed -- the second term is that the dust total loses '
      'the 93.14 value this file put there while what is added back is the integral\'s own late '
      'density, about 1.2 per cent apart.  Both are named now'
      % max(abs(r['diff'] - r['expected']) for r in V['bookkeeping']['rows']),
      V['bookkeeping']['one_count'] is True
      and V['bookkeeping']['tol'] == 1.0e-12
      and len(V['bookkeeping']['rows']) == 4
      and max(abs(r['diff'] - r['expected'])
              for r in V['bookkeeping']['rows']) < 1.1e-16,
      'residual %.2e at worst over four sums'
      % max(abs(r['diff'] - r['expected']) for r in V['bookkeeping']['rows']))

check('Ⓐ①ᵉᵃ ⛔ ** AND THE REGISTERED FLATNESS BAND FAILS, reported as written and not moved. **  It '
      'was registered that the densities at a = 1 sum to 1 to 1e-12.  They do not, before OR after: '
      'the landed convention does not subtract the radiation from the vacuum term, so the total is '
      '1 + Omega_r either way.  ⇒ The claim that MATTERS is the difference, which Ⓐ①ᵉ measures, and '
      'the band as registered asked for the wrong thing',
      V['bookkeeping']['flatness_as_registered'] is False
      and 'sum to `1` to `1e-12` — **fails**' in RESULT.lower()
      and 'the claim that matters is the difference' in RESULT.lower()
      and 'flatness is preserved exactly' in PRED.lower(),
      'the band is in the PREDICTION, it fails, and the record says so')

_RF = V['reference']
_RD = {round(r['sum'], 2): r for r in _RF['rdrag']}
check('Ⓐ①ᶜ AGAINST THE REFERENCE BEFORE USE, as the order directs: `rdrag` agrees to %.2e, %.2e, '
      '%.2e and %.2e at Sum = 0, 0.06, 0.30 and 0.60 eV against the 0.005 registered -- WITHIN AT '
      'ALL FOUR -- and H(z) to %.2e, %.2e and %.2e at z = 0, 1 and 1100 against the 0.002 '
      'registered.  ⌗ The four reference values are r7862\'s own reads, carried as reads'
      % (_RD[0.0]['rel'], _RD[0.06]['rel'], _RD[0.3]['rel'], _RD[0.6]['rel'],
         _RF['H_rel'][0], _RF['H_rel'][1], _RF['H_rel'][2]),
      _RF['rdrag_within'] is True and _RF['H_within'] is True
      and _RF['tol']['rdrag'] == 0.005 and _RF['tol']['H'] == 0.002
      and abs(_RD[0.0]['rel'] - 1.228e-03) < 5.0e-06
      and abs(_RD[0.6]['rel'] - 3.393e-03) < 5.0e-06
      and abs(_RD[0.06]['rdrag_read'] - 147.05547) < 1.0e-04
      and abs(_RD[0.6]['rdrag_read'] - 148.07882) < 1.0e-04,
      'all four rulers and all three rates inside their registered bands')

check('Ⓐ①ᶜᵃ ⛔ ** AND THE DENSITY BAND FAILS, WITH ITS CAUSE MEASURED AND NOT ASSERTED. **  '
      '`rho_nu/rho_crit` lands %.3e from the reference against the 0.005 registered.  The '
      'instrument\'s neutrino fraction codes N_eff = 3.000 exactly where the reference reports '
      '3.0293 with a per-state degeneracy of 1.0147, and 3.0293/3.0000 accounts for it to the '
      'digit.  ⇒ PUT TO A TEST THAT COULD HAVE REFUTED IT: at DNEFF = +0.0293 the gap falls to '
      '%.3e, inside the band.  So the diagnosis HOLDS, and it is a question about N_eff sitting '
      'underneath the ruler\'s flatness -- two questions, and this revision repairs the second'
      % (_RF['rho_rel'], V['neff']['rel']),
      _RF['rho_within'] is False
      and abs(_RF['rho_rel'] - 1.241e-02) < 1.0e-05
      and V['neff']['diagnosis_holds'] is True
      and abs(V['neff']['rel'] - 2.760e-03) < 1.0e-05
      and V['neff']['rel'] < _RF['rho_rel'] / 3.0
      and 'and its cause is measured rather than asserted' in RESULT.lower(),
      'the band fails at %.3e and the diagnosis closes it to %.3e'
      % (_RF['rho_rel'], V['neff']['rel']))

_RU = V['ruler']
check('Ⓐ①ᵈ ** AND THE RULER MOVES WITH THE SUM NOW, WHICH IS THE WHOLE POINT. **  `r_d` runs '
      '147.07345, 147.24127, 147.87291 and 148.58123 Mpc at Sum = 0, 0.06, 0.30 and 0.60 eV -- a '
      'spread of %.4f per cent against the 0.5 registered and against EXACTLY ZERO at r7862.  ⌗ And '
      'the repaired ruler\'s table needed a sum axis it could not have had before: at the grid '
      'centre it runs 142.3190 to 143.8603 Mpc, where those seven numbers would have been identical'
      % (100.0 * _RU['spread']),
      _RU['holds'] is True and _RU['min_spread'] == 5.0e-03
      and abs(100.0 * _RU['spread'] - 1.0252) < 4.0e-04
      and abs(_RU['r_drag'][0] - 147.07345) < 1.0e-04
      and abs(_RU['r_drag'][3] - 148.58123) < 1.0e-04
      and all(_RU['r_drag'][i] < _RU['r_drag'][i + 1] for i in range(3)),
      'spread %.4f per cent, monotonic in the sum' % (100.0 * _RU['spread']))

_LIM = V['limits']
check('Ⓐ①ᵇ the two limits of the new term: the EARLY limit is exact to %.2e, and ⛔ ** THE LATE '
      'LIMIT\'S REGISTERED BAND FAILS AT THE LIGHTEST SUM **, where `Omega_nu a^3` is constant to '
      '%.2e at Sum = 0.06 eV against the 1e-03 registered, while at 0.60 eV it is %.2e.  ⇒ The '
      'cause is PHYSICS and not error -- at 0.06 eV the species still carries a residual pressure '
      'between a = 0.5 and 1 -- and the trend across the two sums is what says so.  Reported as '
      'written'
      % (_LIM['rows']['0.06']['early_err'], _LIM['rows']['0.06']['late_err'],
         _LIM['rows']['0.6']['late_err']),
      _LIM['holds'] is False
      and _LIM['rows']['0.06']['early_err'] < 1.0e-04
      and _LIM['rows']['0.6']['early_err'] < 1.0e-04
      and abs(_LIM['rows']['0.06']['late_err'] - 1.36e-03) < 1.0e-05
      and abs(_LIM['rows']['0.6']['late_err'] - 1.36e-05) < 1.0e-07
      and _LIM['rows']['0.06']['late_err'] > _LIM['rows']['0.6']['late_err'] * 50.0,
      'early exact, late %.2e at 0.06 eV against %.2e at 0.60'
      % (_LIM['rows']['0.06']['late_err'], _LIM['rows']['0.6']['late_err']))

check('Ⓐ①ᶠ and the instrument\'s inline factor agrees with this revision\'s INDEPENDENT module to '
      '%.3e over eight points.  ⌗ That is why there are two implementations: one measures the '
      'other, and a single implementation agreeing with itself is not a measurement'
      % V['two_impls']['worst_rel'],
      V['two_impls']['holds'] is True
      and abs(V['two_impls']['worst_rel'] - 4.366e-10) < 1.0e-12,
      'worst %.3e' % V['two_impls']['worst_rel'])

# ── Ⓑ② THE PROVENANCE KEYS ──────────────────────────────────────────────────────────────────────
check('Ⓑ② THE FIVE KEYS `r7861` ③ ORDERED BATCHED ARE PAID HERE, because item ① moves the blob and '
      'the deferral r7862 gated on is spent.  All five are in the resolved config with the '
      'None-when-unset convention the existing keys use.  ⌗ The mass and the new switch are the '
      'pair that matters: a bank taken on the repaired background and one taken on the old one are '
      'different objects, and until now neither could say which it was',
      all(("'%s':" % k) in INST for k in ('BVEL', 'MNU', 'FOURPI', 'NUFD'))
      and "'PRIMNORM_env': os.environ.get('PRIMNORM')" in INST
      and 'THE FIVE KEYS `r7861` ③ ORDERED BATCHED' in INST,
      'five keys recorded, the blob moved with them')

check('Ⓑ②ᵃ ⛔ and ONE ITEM OF THE ORDER\'S LIST IS NAMED RATHER THAN SILENTLY FIXED: this '
      'instrument DOES NOT READ the lensing path\'s primordial normalisation at all -- it is read '
      'where that path is generated, and this file mentions it nowhere but in the key.  ⇒ So that '
      'key records the ENVIRONMENT the run was made in and is labelled as such, because a config '
      'claiming to resolve a switch it never reads would be the vacuous form this corpus keeps '
      'catching',
      'THIS FILE DOES NOT READ IT' in INST
      and 'PRIMNORM_env' in INST
      and INST.count('PRIMNORM') == 3
      and 'this instrument does not\nread `primnorm` at all'.replace('\n', ' ') in RESULT.lower(),
      'the key is labelled and the reason is in both records')

# ── Ⓒ③ BOTH LIMITS ─────────────────────────────────────────────────────────────────────────────
_P = L['precondition']
check('Ⓒ③ᵃ ** WHAT THESE LIMITS CAN BE READ ON IS PROVED FROM THE BANK\'S OWN CONFIG AND NOT '
      'ASSERTED, which is what item ② just bought. **  The banked spectra were SOLVED on the old '
      'background, and the precondition gates that the new switch key is ABSENT from the bank\'s '
      'recorded config.  ⇒ A bank taken after the repair would say `false`; these cannot say at '
      'all, and that is a DIFFERENT STATEMENT -- exactly the distinction this instrument\'s own '
      'note on an earlier key draws.  So both limits below are the banked spectra with the RULER '
      'repaired, not a re-solved bank, and the record says so beside each',
      _P['holds'] is True
      and _P['nufd_key_present'] is False and _P['mnu_key_present'] is False
      and _P['cmb_points'] == 32 and _P['lensing_points_lcdm'] >= 16
      and _P['blob_is_not_landed'] is True
      and 'the banked spectra with the ruler repaired' in RESULT.lower(),
      '%d CMB points, %d lensing, and the bank cannot state its background'
      % (_P['cmb_points'], _P['lensing_points_lcdm']))

_MI, _CA = L['profiles']['minimised'], L['profiles']['calibrated']
#: the threshold the limit was read at, solved back out of the profile's own recorded nodes
_s, _d, _lm = _MI['sums'], _MI['delta'], _MI['limit_meV'] / 1000.0
_k = min(k for k in range(1, len(_s)) if _s[k] >= _lm)
_THRESH = _d[_k - 1] + (_lm - _s[_k - 1]) * (_d[_k] - _d[_k - 1]) / (_s[_k] - _s[_k - 1])
_G = L['ruler_gap']
check('Ⓒ③ᵇ ** THE REPAIR CLOSES MOST OF THE RULER DISAGREEMENT, AND BELOW THE THRESHOLD THAT MADE '
      'THE SECOND TREATMENT NECESSARY. **  At Sum = 0.60 eV the two rulers now differ by %.4f in '
      'chi2_bao against 14.5415 before it -- under the 2.71 the limit itself is read at, which is '
      'the number r7862 used to show the second treatment was not redundant' % _G['dchi2_at_top'],
      _G['closed'] is True
      and abs(_G['dchi2_at_top'] - 2.1989) < 1.0e-03
      and _G['dchi2_at_top_before'] == 14.5415
      and _G['dchi2_at_top'] < _THRESH
      # ⌗ *and the threshold itself is PINNED, recovered from the profile the run stored rather
      #   than taken from a sentence: the crossing the limit is read at is solved back out of the
      #   recorded sums and deltas, and it has to come to the number the limit was read at.*
      and abs(_THRESH - 2.71) < 4.0e-03,
      '%.4f against 14.5415, and below the %.4f the limit is read at'
      % (_G['dchi2_at_top'], _THRESH))

check('Ⓒ③ᶜ BOTH LIMITS, each with the treatment named beside it: %.2f meV with the ruler minimised '
      'against the reference\'s 54.00, and %.2f meV calibrated on this instrument\'s OWN REPAIRED '
      'drag epoch against the ordered 30.56.  Both minima at 0.000 eV, both profiles monotonic '
      'above them, so both are reported -- and r7860\'s convergence discipline is carried unchanged'
      % (_MI['limit_meV'], _CA['limit_meV']),
      _MI['limit_meV'] is not None and _CA['limit_meV'] is not None
      and abs(_MI['limit_meV'] - 69.97) < 1.0e-02
      and abs(_CA['limit_meV'] - 81.94) < 1.0e-02
      and _MI['monotonic_above_min'] is True and _CA['monotonic_above_min'] is True
      and _MI['dips'] == [] and _CA['dips'] == []
      and abs(_MI['min_at']) < 1.0e-09 and abs(_CA['min_at']) < 1.0e-09
      and _CA['clipped_calls'] == 0,
      '%.2f and %.2f meV, no clipped ruler call' % (_MI['limit_meV'], _CA['limit_meV']))

_AD = L['adjudication']
check('Ⓒ③ᵈ ⛔ ** THE REGISTERED EXPECTATION FAILS. **  It was registered that the calibrated limit '
      'on this instrument\'s own repaired ruler would land within 4 meV of r7862\'s 89.91 meV read '
      'on the reference\'s ruler.  It lands %.2f meV away.  ⇒ So the repair moves that limit a long '
      'way in the right direction -- 78.33 on the unrepaired ruler, %.2f on the repaired one, '
      'against 89.91 on the reference\'s -- and NOT FAR ENOUGH to meet the band this seat wrote.  '
      'Reported as refuted with the criterion exactly as registered'
      % (_AD['gap_to_r7862_on_reference'], _CA['limit_meV']),
      _AD['held'] is False and _AD['within'] == 4.0
      and abs(_AD['gap_to_r7862_on_reference'] - 7.97) < 4.0e-03
      # ⌗ *the figure this gap is taken against is PINNED too, from the two numbers the run itself
      #   stored rather than from the sentence that quotes it: the limit plus the gap is r7862's
      #   own reading on the reference's ruler.*
      and abs(_CA['limit_meV'] + _AD['gap_to_r7862_on_reference'] - 89.91) < 4.0e-02
      # ⌗ *and the two ordered figures are pinned off the record the run wrote, not off prose.*
      and abs(_AD['reference_calibrated'] - 30.56) < 1.0e-02
      and abs(_AD['reference_minimised'] - 54.00) < 2.0e-02
      and 'lands within `4` meV of the `89.91` meV' in PRED
      and 'the registered expectation fails' in RESULT.lower(),
      'the gap is %.2f meV against the 4 registered' % _AD['gap_to_r7862_on_reference'])

# ── Ⓓ④ THE SECOND BASIN ────────────────────────────────────────────────────────────────────────
_SB = L['second_basin']
check('Ⓓ④ ** THE SECOND BASIN DOES NOT SURVIVE THE REPAIR. **  r7862 found the fit landing on a '
      'different branch at Sum = 0.60 eV, H0 = 65.74 against 69.17 at the node below.  After the '
      'repair BOTH profiles sit on the same branch as their own node below -- %.3f against %.3f '
      'minimised and %.3f against %.3f calibrated.  ⇒ So the basin was a fact about the BACKGROUND '
      'and not about the likelihood surface, which is the alternative this revision REGISTERED for '
      'it rather than a reading invented afterwards'
      % (_SB['rows']['minimised']['H0_top'], _SB['rows']['minimised']['H0_below'],
         _SB['rows']['calibrated']['H0_top'], _SB['rows']['calibrated']['H0_below']),
      _SB['persists'] is False
      and _SB['r7862_H0_top'] == 65.74 and _SB['r7862_H0_below'] == 69.17
      and all(abs(v['H0_top'] - v['H0_below']) < 1.0 for v in _SB['rows'].values())
      and len(_SB['rows']) == 2
      and 'a basin that disappears when the background is' in PRED.lower(),
      'both branches within %.3f of their own node below'
      % max(abs(v['H0_top'] - v['H0_below']) for v in _SB['rows'].values()))

check('Ⓔ⑤ the record carries its five own defects rather than only its results: the forward '
      'declaration that silently zeroed the subtraction, the first subtraction that broke inertness '
      'at zero mass, the switch that did not require a nonzero mass, the bookkeeping gate that '
      'expected the wrong number, and the gate written one revision ago that would have reddened on '
      'its successor OBEYING AN ORDER -- all five in RESULT.md, and all five this seat\'s own',
      'five things in this record are this seat' in RESULT.lower()
      and 'silently zeroed the subtraction' in RESULT.lower()
      and 'stopped being inert exactly where it must be' in RESULT.lower()
      and 'is not the identity in' in RESULT.lower()
      and 'expected the wrong number' in RESULT.lower()
      and 'would have reddened on its successor obeying an' in RESULT.lower(),
      'five named in the result document')

check('Ⓕ⑥ the count: this receipt adjudicates every leg of the revision, and THREE REGISTERED '
      'BANDS ARE REPORTED AS FAILED with their criteria unchanged -- the flatness band, which asked '
      'for the wrong thing; the density band, whose cause is the instrument\'s N_eff and is '
      'diagnosed by a test that could have refuted it; and the late-limit band at the lightest '
      'sum, where the cause is the species\' residual pressure.  ** Not one criterion was moved **',
      V['bookkeeping']['flatness_as_registered'] is False
      and V['reference']['rho_within'] is False
      and V['limits']['holds'] is False
      and _AD['held'] is False,
      'three bands and one expectation refuted, no criterion loosened')

print()
if not FAILS:
    print('  ✔ r7864: all %d arms adjudicated.' % NARMS)
    print('    => the background is repaired in the model: inert off AND inert at zero sum, both '
          'bit-identically, and the species counted once.')
    print('    => the drag ruler moves with the sum by %.4f per cent where r7862 measured it '
          'EXACTLY FLAT, and tracks the reference to 3.4e-03 at worst.'
          % (100.0 * V['ruler']['spread']))
    print('    => the two rulers now differ by %.4f in chi2_bao at the top of the range against '
          '14.5415, below the 2.71 the limit is read at.' % _G['dchi2_at_top'])
    print('    => both limits: %.2f meV minimised against 54.00 and %.2f meV calibrated against '
          '30.56, on the banked spectra with the ruler repaired.'
          % (_MI['limit_meV'], _CA['limit_meV']))
    print('    => and the second basin does NOT survive the repair, so it was the background\'s '
          'and not the likelihood surface\'s.')
else:
    print('  ⛔ FAIL  %d of %d arms' % (len(FAILS), NARMS))
print()
sys.exit(1 if FAILS else 0)
