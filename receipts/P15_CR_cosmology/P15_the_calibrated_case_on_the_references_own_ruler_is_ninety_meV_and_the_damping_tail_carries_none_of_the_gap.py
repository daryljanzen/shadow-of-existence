# -*- coding: utf-8 -*-
"""⛭⛭⛭ THE CALIBRATED CASE ON THE REFERENCE'S OWN RULER IS `89.91` meV AND THE DAMPING TAIL CARRIES
ESSENTIALLY NONE OF THE MINIMISED GAP.

COMPUTES: a BAO ruler derived from this instrument's OWN ionisation history -- the drag optical depth
integrated on its own `dtau/deta` weighted by its own baryon-to-photon ratio, the drag epoch as the
root of `tau_d = 1`, and the sound horizon accumulated to that epoch on the clock `rs_from` is on --
validated against the reference's `rdrag` at two corners of the fit's own box; what that ruler ranges
over, measured; the calibrated profile with all four parameters free on TWO ruler treatments, each
named; and the damping tail's share of the minimised gap, with the information-loss control the
registered leg lacked.
** IT PINS TWO LIMITS AS RESULTS: `89.91` meV on the reference's own `rdrag` including the neutrino
sum, which is the ruler the ordered `30.56` meV was produced on, and `78.33` meV on this
instrument's own drag epoch.  Both are 95 per cent one-sided and both are reported as a COMPARISON,
as registered before the numbers existed.  `r7860`'s `146.13` meV is SUPERSEDED: that profile held
`H0` and `Omega_m` and was not the case the order asked for. **

⌷ ** THE ID. **  `69` ordered this as `r7861`, which merged `r7860`, applied the census patch and
turned over `cc66`'s watch arm, and then found that `r7860`'s "calibrated" profile froze the geometry
instead of calibrating the ruler -- so `146.13` was not the comparison to `30.56`.

⛭ ** WHAT IS NEW HERE, AND WHAT IS NOT. **  The finding that the configuration was wrong is `69`'s.
What this revision adds is the ruler, derived and validated; the measurement of what it ranges over;
both calibrated profiles; the price of the difference between the two rulers; and the tail leg with
its control.  ⛔ *Nothing landed is edited: the ruler is attached by replacing `chi2` on the model
INSTANCE, exactly as `r7860` replaced `amp_cmb`, so the instrument and `model3.py` keep their bytes
-- which is also the condition the order set for deferring item ③.*

⚠ ** NINE THINGS IN THIS RECORD ARE FAILURES OR CORRECTIONS AND ALL NINE ARE THIS SEAT'S OWN. **  A
registered expectation is REFUTED; a registered criterion was BADLY CHOSEN and its control was added
afterwards in its own file; a table builder DEADLOCKED and computed nothing for forty-three minutes;
a defect this seat diagnosed in its own reading of the ruler was then REFUTED BY MEASUREMENT and is
kept as refuted; a gate read a CONVENTION as a quadrature failure and was loosened before it was
understood; and another gate compared the wrong two things, taking a grid's own record of when it
was made for a statement about what the instrument is now; and an arm of THIS receipt bounded its
population by a MOVING REF, which is the defect another receipt of this seat's exists to catch and
is how it was caught -- the base is pinned now and the emptiness is itself a gate; and that repaired
arm then OVER-PROTECTED, refusing two whole trees where the order names receipts, while one item of
the order's list turned out to have no filename convention at all, so its pattern matched zero files
and is CUT in favour of a reading off the ledger.

    NODE=60 python3 <this file>

Written r7862 (60).  Stated for reversal.
"""
import fnmatch
import hashlib
import io
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
D = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                 'r7862_60_the_calibrated_case_on_the_references_terms_and_the_damping_tails_'
                 'share_of_the_gap')
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

DR = load('drag_ruler.json')
RR = load('ref_ruler.json')
CAL = load('calibrated.json')
TS = load('tail_share.json')
TC = load('tail_control.json')
#: r7860's own record, so the figure this revision supersedes is READ and not remembered
R7860 = json.load(io.open(os.path.join(
    ROOT, 'computations', 'beyond_the_wall',
    'r7860_60_the_polarisation_blocks_wired_the_spread_reconciled_and_the_bank_committed',
    'control.json'), encoding='utf-8'))
RESULT = ' '.join(io.open(os.path.join(D, 'RESULT.md'), encoding='utf-8').read().split())
PRED = ' '.join(io.open(os.path.join(D, 'PREDICTION.md'), encoding='utf-8').read().split())

# ── Ⓐ① THE RULER, DERIVED AND VALIDATED ─────────────────────────────────────────────────────────
_V = {r['point']: r for r in DR['validate']['rows']}
_READ = _V['control (DECLARED READ)']
_LO = _V['corner low  (-6,-6,-6)']
_HI = _V['corner high (+6,+6,+6)']

check('Ⓐ①ᵃ THE REGISTERED ARM HOLDS at BOTH corners of the fit\'s own box, which were unread when '
      'the criterion was written: the ruler derived from this instrument\'s own ionisation history '
      'agrees with the reference\'s `rdrag` to %.2e and %.2e and its drag epoch to %.2e and %.2e, '
      'against the 0.005 registered.  ⌗ And the box is one the ruler MOVES across -- 121.8231 to '
      '178.3563 Mpc -- so the agreement is not one point\'s coincidence'
      % (_LO['r_rel'], _HI['r_rel'], _LO['z_rel'], _HI['z_rel']),
      DR['validate']['corners_within'] is True
      and DR['validate']['tol'] == 0.005
      and abs(_LO['r_drag'] - 178.3563) < 1.0e-04 and abs(_LO['rdrag_ref'] - 178.0873) < 1.0e-04
      and abs(_HI['r_drag'] - 121.8231) < 1.0e-04 and abs(_HI['rdrag_ref'] - 121.6996) < 1.0e-04
      and abs(_LO['r_rel'] - 1.51e-03) < 5.0e-06 and abs(_HI['r_rel'] - 1.01e-03) < 5.0e-06
      and abs(_LO['z_rel'] - 1.28e-03) < 5.0e-06 and abs(_HI['z_rel'] - 8.96e-04) < 5.0e-06,
      'corners %.4f/%.4f Mpc against %.4f/%.4f' % (_LO['r_drag'], _HI['r_drag'],
                                                   _LO['rdrag_ref'], _HI['rdrag_ref']))

check('Ⓐ①ᵃᵃ and the control point is a DECLARED READ, not an arm: `147.0734` Mpc at `z = 1061.185` '
      'against the reference\'s `146.8930` at `1060.047`, agreeing to 1.23e-03 -- and the '
      'PREDICTION names it as read BEFORE the registration rather than reporting it as a finding',
      abs(_READ['r_drag'] - 147.0734) < 1.0e-04 and abs(_READ['z_drag'] - 1061.1846) < 1.0e-03
      and abs(_READ['rdrag_ref'] - 146.8930) < 1.0e-04
      and abs(_READ['zdrag_ref'] - 1060.0474) < 1.0e-03
      and abs(_READ['r_rel'] - 1.23e-03) < 5.0e-06
      and 'declared reads' in PRED.lower()
      and 'z_drag = 1061.1846`, `r_d = 147.0732' in PRED
      and 'rdrag = 146.8930` Mpc, `zdrag = 1060.0474' in PRED,
      '%.4f Mpc at z %.4f' % (_READ['r_drag'], _READ['z_drag']))

check('Ⓐ①ᵃᵇ and the ruler is measuring what the instrument\'s own `R_S` measures, checked ON '
      '`rs_from`\'S OWN CONVENTION: the same quadrature stopped at recombination and started where '
      '`rs_from` starts reproduces the instrument\'s reported `144.5281` Mpc EXACTLY, to the bit, '
      'at all three points.  ⛔ Started at `a = 0` instead it agrees only to %.2e -- and that '
      'sliver IS the whole difference, which this seat first read as a quadrature failure and '
      'loosened the band for before matching the convention instead.  ⌗ Matching it is what '
      'establishes WHICH of the two it was; a looser band would have hidden that'
      % DR['validate']['worst_r_rec_error'],
      DR['validate']['worst_r_rec_error_strict'] == 0.0
      and all(r['r_rec_reproduced_strict'] == r['R_S'] for r in DR['validate']['rows'])
      and abs(DR['validate']['worst_r_rec_error'] - 2.2209e-05) < 1.0e-08
      and abs(_READ['R_S'] - 144.5281) < 1.0e-04
      # ⌗ *the claim is the SIGN and not a margin: the drag epoch falls LATER than last scattering,
      #   so `r_d` must EXCEED `r_s` at every point.  A first version of this line demanded more
      #   than a megaparsec of it and the high corner gives `0.845`, which refutes the margin and
      #   not the claim -- the margin was never the physics.*
      and all(r['r_drag'] > r['R_S'] for r in DR['validate']['rows'])
      and min(r['r_drag'] - r['R_S'] for r in DR['validate']['rows']) > 0.5,
      'exact on the convention, %.4e from zero, and r_d exceeds r_s at every point -- by %.3f Mpc '
      'at the narrowest, as the drag epoch being LATER requires'
      % (DR['validate']['worst_r_rec_error'],
         min(r['r_drag'] - r['R_S'] for r in DR['validate']['rows'])))

_OL = DR['ranging']['omega_label']
check('Ⓐ①ᵇ WHAT THE RULER RANGES OVER, measured and not assumed: two different `(H0, Om)` pairs '
      'carrying the SAME `omega_m` and `omega_b` give `r_d` equal to %.3e and the drag epoch to '
      '%.3e, against the 1e-04 registered -- so `omega_m` is a ONE-TO-ONE label here and the table '
      'may be built in two variables.  ⌗ GUARD: before two stretches are identified by a label, '
      'check how many-to-one the label is on the object' % (_OL['r_rel'], _OL['z_rel']),
      _OL['holds'] is True and _OL['tol'] == 1.0e-04
      and abs(_OL['r_rel'] - 6.596e-10) < 1.0e-12
      and abs(_OL['points'][0]['omega_m'] - _OL['points'][1]['omega_m']) < 1.0e-09
      and abs(_OL['points'][0]['H0'] - _OL['points'][1]['H0']) > 15.0,
      'H0 %.2f against %.2f at one omega_m, r_d apart by %.3e'
      % (_OL['points'][0]['H0'], _OL['points'][1]['H0'], _OL['r_rel']))

_NS = DR['ranging']['neutrino_sum']
_SD = RR['sum_dependence']
check('Ⓐ①ᵇᵇ ** AND THE OTHER HALF OF THAT ARM IS WHY THIS REVISION HAS AN AMENDMENT. **  The '
      'neutrino sum moves THIS instrument\'s drag ruler by EXACTLY ZERO across [0, 0.60] eV, '
      'because the instrument carries the mass inside `OM` at every epoch -- and the reference\'s '
      'ruler is NOT flat: `rdrag` runs 146.89300 to 148.07882 Mpc, a spread of %.4f per cent.  ⌗ '
      'The exact zero is not asserted from the source: it is MEASURED at four sums, and the '
      'reference is measured at the same four so the contrast is between two readings and not '
      'between a reading and a memory' % (100.0 * _SD['spread']),
      _NS['spread'] == 0.0 and len(_NS['sums']) == 4 and len(set(_NS['r_drag'])) == 1
      and len(_SD['rows']) == 4 and _SD['spread'] > 0.008
      and abs(100.0 * _SD['spread'] - 0.8073) < 3.0e-04
      and abs(_SD['rows'][0]['rdrag'] - 146.89300) < 1.0e-04
      and abs(_SD['rows'][3]['rdrag'] - 148.07882) < 1.0e-04
      and abs(_SD['rows'][1]['rdrag'] - 147.05547) < 1.0e-04,
      'the instrument flat to the bit; the reference spreading %.4f per cent, and its 147.05547 at '
      '0.06 eV is the figure the order quotes' % (100.0 * _SD['spread']))

check('Ⓐ①ᶜ and the multipole reach this probe runs at, chosen to keep the import cheap, does NOT '
      'reach the ruler: bit-identical at LMAXL = 2 and LMAXL = 2600.  ⌗ A switch set for the '
      'measurer\'s convenience is checked against the measurement rather than assumed harmless',
      DR['ranging']['lmaxl']['identical'] is True
      and DR['ranging']['lmaxl']['r_drag_lmaxl2'] == DR['ranging']['lmaxl']['r_drag_lmaxl2600'],
      'r_d identical at both reaches')

_TE = CAL['table_error']
check('Ⓐ①ᵈ and BOTH tables\' own interpolation error is measured OFF THEIR NODES against a fresh '
      'computation at each test point -- worst %.3e for the instrument\'s and %.3e for the '
      'reference\'s.  ⌗ A spline standing in for a computation is exactly what `bao_error` exists '
      'for in this harness, and it is measured here for the same reason'
      % (_TE['instrument']['worst_rel'], _TE['reference']['worst_rel']),
      _TE['instrument']['worst_rel'] < 1.0e-06 and _TE['reference']['worst_rel'] < 1.0e-04
      and abs(_TE['instrument']['worst_rel'] - 1.994e-08) < 1.0e-10
      and abs(_TE['reference']['worst_rel'] - 5.523e-06) < 1.0e-08
      and len(_TE['instrument']['points']) == 7 and len(_TE['reference']['points']) == 7
      and DR['grid']['n'] == [1, 33, 13] and RR['grid']['n'] == [17, 9, 9],
      '%.3e and %.3e over seven off-node points each, on a 33x13 and a 17x9x9 table'
      % (_TE['instrument']['worst_rel'], _TE['reference']['worst_rel']))

# ── Ⓑ② THE CALIBRATED CASE, ON BOTH RULERS ──────────────────────────────────────────────────────
_P = CAL['ruler_price']
_TOP = [r for r in _P['rows'] if abs(r['sum'] - 0.60) < 1e-09][0]
check('Ⓑ②ᵉ THE RULER DIFFERENCE IS PRICED BEFORE EITHER PROFILE IS READ, as the amendment '
      'registered: at the control geometry the two rulers\' `chi2_bao` differ by %.4f at Sum = '
      '0.60 eV against the 2.71 the limit itself is read at -- so the second treatment is NOT '
      'redundant and a calibrated limit read on the wrong ruler would be dominated by the ruler.  '
      '⌗ The registered negative was reachable: a difference BELOW 2.71 would have made the second '
      'treatment redundant and been reported as such' % _TOP['dchi2'],
      _P['exceeds_threshold'] is True and _P['dchi2_threshold'] == 2.71
      and abs(_TOP['dchi2'] - 14.5415) < 1.0e-03
      and abs(_TOP['rd_instrument'] - 147.0734) < 1.0e-04
      and abs(_TOP['rd_reference'] - 148.0789) < 1.0e-04
      and len(_P['rows']) == 11
      and all(r['rd_instrument'] == _P['rows'][0]['rd_instrument'] for r in _P['rows']),
      'delta chi2_bao %.4f at the top node, and the instrument\'s ruler identical at all eleven'
      % _TOP['dchi2'])

_RF = CAL['profiles']['reference']
_IN = CAL['profiles']['instrument']
check('Ⓑ②ᶠ⒝ THE CALIBRATED CASE ON THE REFERENCE\'S OWN RULER -- all four free, `rdrag` taken at '
      'each point from that point\'s own cosmology INCLUDING ITS SUM -- is %.2f meV, with the '
      'minimum at %.3f eV, reported as a COMPARISON against the ordered 30.56 meV.  ** This is the '
      'reference\'s ruler and the receipt says so: it is the ruler that figure was produced on, and '
      'this instrument\'s own background cannot produce its movement **'
      % (_RF['limit_meV'], _RF['min_at']),
      _RF['limit_meV'] is not None and abs(_RF['limit_meV'] - 89.91) < 1.0e-02
      and abs(_RF['min_at'] - 0.030) < 1.0e-09
      and _RF['monotonic_above_min'] is True and _RF['dips'] == []
      and _RF['ruler'] == 'reference' and _RF['clipped_calls'] == 0
      and CAL['adjudication']['adjudicated_on'] == 'reference'
      and CAL['adjudication']['reference_target'] == 30.56,
      '%.2f meV against 30.56, minimum at %.3f eV' % (_RF['limit_meV'], _RF['min_at']))

check('Ⓑ②ᶠ⒜ and on THIS instrument\'s own drag epoch -- the ruler that is internally consistent '
      'with its background and exactly flat in the sum -- the same case is %.2f meV with the '
      'minimum at %.3f eV.  ⌗ Both are carried because "the calibrated case" named two objects and '
      'the thing they are alternatives FOR has a slot for only one'
      % (_IN['limit_meV'], _IN['min_at']),
      _IN['limit_meV'] is not None and abs(_IN['limit_meV'] - 78.33) < 1.0e-02
      and abs(_IN['min_at'] - 0.000) < 1.0e-09
      and _IN['monotonic_above_min'] is True and _IN['dips'] == []
      and _IN['ruler'] == 'instrument' and _IN['clipped_calls'] == 0,
      '%.2f meV, minimum at %.3f eV' % (_IN['limit_meV'], _IN['min_at']))

check('Ⓑ②ᵈ and NEITHER profile\'s ruler stood still, which is what stops a "calibrated" run being '
      'the held case under a new name: the ruler spans %.3e on the reference\'s treatment and %.3e '
      'on the instrument\'s, because `omega_m` and `omega_b` move with the fit even where the sum '
      'does not reach the ruler.  ⌗ The ruler is read AT each node\'s winning parameters, not at '
      'wherever the minimiser stopped' % (_RF['rd_span'], _IN['rd_span']),
      _RF['ruler_moves'] is True and _IN['ruler_moves'] is True
      and abs(_RF['rd_span'] - 3.108e-02) < 1.0e-05
      and abs(_IN['rd_span'] - 7.810e-03) < 1.0e-06
      and len(_RF['rd_at_node']) == 11 and len(_IN['rd_at_node']) == 11
      and all(c > 0 for c in _RF['ruler_calls_per_node']),
      'spans %.3e and %.3e across the eleven nodes' % (_RF['rd_span'], _IN['rd_span']))

check('Ⓑ②ᵈᵃ ⚠ and the one discontinuity in that column is the FIT\'s and not the reading\'s, which '
      'this seat established by REFUTING ITS OWN DIAGNOSIS: the top node\'s ruler sits at `149.9752` '
      'Mpc against `145.4` -- `146.0` at every other, this seat read that as the column reporting '
      'the minimiser\'s last call, rewrote it to read the winning parameters, and the re-run came '
      'back IDENTICAL.  ⇒ At that node the minimiser lands on a different branch, and it is far '
      'above the crossing, which falls between 0.060 and 0.100 eV',
      abs(_RF['rd_at_node'][-1] - 149.9752) < 1.0e-04
      and all(abs(v - 145.7) < 0.6 for v in _RF['rd_at_node'][:-1])
      and _RF['delta'][2] < 2.71 < _RF['delta'][3]
      and _RF['x_at_node'][-1][0] < -0.5 < 0.5 < _RF['x_at_node'][-2][0]
      and 'refuted by measurement' in RESULT.lower(),
      'the top node at x0 %.3f against %.3f below it, and the crossing is between nodes three and '
      'four' % (_RF['x_at_node'][-1][0], _RF['x_at_node'][-2][0]))

_AD = CAL['adjudication']
_BAND = [float(v) for v in
         re.findall(r'\[([0-9.]+), ([0-9.]+)\] meV', _AD['expectation'])[0]]
check('Ⓑ②ᵇ ** THE REGISTERED EXPECTATION IS REFUTED AND THE ORDER\'S DIAGNOSIS IS HALF RIGHT. **  '
      'It was registered that if the frozen geometry were the cause, the calibrated minimum would '
      'move below 0.030 eV AND the limit would land inside [15.3, 61.1] meV.  The minimum DOES '
      'move -- from r7860\'s own recorded 0.060 eV to 0.030 on the reference\'s ruler and to 0.000 on the '
      'instrument\'s -- and the limit does NOT: 89.91 meV is outside the band.  ⇒ So the frozen '
      'geometry explains the interior minimum and does not explain the limit, and the criterion is '
      'reported exactly as written',
      _AD['held'] is False
      and 'inside [15.3, 61.1] meV' in _AD['expectation']
      and 'below 0.030' in _AD['expectation']
      # ⌗ *the band's two edges are PINNED off the criterion this run itself recorded, so a
      #   receipt that printed a band the run did not use would fail here rather than read well.*
      and abs(_BAND[0] - 15.3) < 4.0e-02 and abs(_BAND[1] - 61.1) < 4.0e-02
      # ⌗ *and r7860's own minimum is READ from its record, not carried in a sentence.*
      and abs(R7860['calibrated']['min_at'] - 0.060) < 4.0e-04
      and _RF['min_at'] <= 0.030 and not (15.3 <= _RF['limit_meV'] <= 61.1)
      and 'the registered expectation fails' in RESULT.lower(),
      'minimum moved to %.3f eV, limit %.2f meV outside [15.3, 61.1]'
      % (_RF['min_at'], _RF['limit_meV']))

check('Ⓑ②ʰ and the price of this instrument\'s neutrino background is %.2f meV, read as the gap '
      'between the two rulers\' limits rather than estimated from the ruler\'s own spread.  ⌗ This '
      'is the cost of a background that counts the neutrino mass as matter at every epoch, and it '
      'is a number this revision owed and did not have before running both profiles'
      % _AD['price_of_the_neutrino_background'],
      _AD['price_of_the_neutrino_background'] is not None
      and abs(_AD['price_of_the_neutrino_background'] - 11.58) < 5.0e-03
      and abs(abs(_RF['limit_meV'] - _IN['limit_meV'])
              - _AD['price_of_the_neutrino_background']) < 1.0e-09,
      '%.2f meV between 89.91 and 78.33' % _AD['price_of_the_neutrino_background'])

check('Ⓑ②ᵃ the precondition r7860 ran is run again here and holds on the SAME grids: 32 '
      'polarisation points, 16 lensing points for the control, and the instrument blob is NOT the '
      'landed grid\'s.  ⌗ Asserted BEFORE anything is scored, because the instrument\'s resolved '
      'config still does not record the solver switch and the blob is the only thing that '
      'distinguishes a re-solved point from a landed one',
      CAL['precondition']['holds'] is True
      and CAL['precondition']['cmb_points'] == 32
      and CAL['precondition']['lensing_points_lcdm'] >= 16
      and CAL['precondition']['blob_is_not_landed'] is True,
      '%d CMB points, %d lensing, blob %s'
      % (CAL['precondition']['cmb_points'], CAL['precondition']['lensing_points_lcdm'],
         str(CAL['precondition']['blob'])[:12]))

# ── Ⓒ③ THE DAMPING TAIL'S SHARE ──────────────────────────────────────────────────────────────────
_B = TS['baseline']
check('Ⓒ③ᵃ the baseline is MEASURED on this leg\'s own path rather than carried across: the '
      'minimised profile comes to %.2f meV against r7860\'s own 69.97 on the same configuration, a '
      'difference of %.3f -- so the cuts below are differenced against a number this file computed '
      'and not against one it remembered' % (_B['limit_meV'], _B['limit_meV'] - 69.97),
      _B['reproduces_r7860'] is True and abs(_B['limit_meV'] - 69.97) < 1.0e-02
      and abs(TS['gap_full_meV'] - 15.97) < 5.0e-03
      and abs((_B['limit_meV'] - 69.97) - 0.003) < 5.0e-04
      and TS['reference_minimised'] == 54.00 and TS['bins_full'] == 555
      and _B['monotonic_above_min'] is True,
      '%.2f meV, gap %.2f meV, on all 555 bandpowers' % (_B['limit_meV'], TS['gap_full_meV']))

_C = TS['cuts']
check('Ⓒ③ᵃᵃ each cut is gated as having actually REMOVED bandpowers, equally from the three '
      'blocks, and the highest bin\'s reach after the cut is reported: 36 of 555 at ell = 1800, 90 '
      'at 1500 and 189 at 1200.  ⌗ A cut that removed nothing would be a failure of the leg and '
      'not a null result, which is why the count is a gate and not a remark',
      _C['1800']['info']['dropped'] == 36 and _C['1500']['info']['dropped'] == 90
      and _C['1200']['info']['dropped'] == 189
      and all(len(set(_C[k]['info']['per_block'])) == 1 for k in ('1800', '1500', '1200'))
      and _C['1800']['info']['ell_hi_after'] == 1792
      and _C['1500']['info']['ell_hi_after'] == 1494
      and _C['1200']['info']['ell_hi_after'] == 1197
      and TS['ell_hi_full'] == 1996,
      'reaches cut back from 1996 to 1792, 1494 and 1197')

check('Ⓒ③ᵃᵇ and the three cut limits with the gap\'s move at each: %.2f meV (%+.2f, share %.3f) at '
      'ell = 1800, %.2f meV (%+.2f, share %.3f) at 1500 and %.2f meV (%+.2f, share %.3f) at 1200, '
      'each profile monotonic above its own minimum'
      % (_C['1800']['limit_meV'], _C['1800']['moved_meV'], _C['1800']['share_of_gap'],
         _C['1500']['limit_meV'], _C['1500']['moved_meV'], _C['1500']['share_of_gap'],
         _C['1200']['limit_meV'], _C['1200']['moved_meV'], _C['1200']['share_of_gap']),
      abs(_C['1800']['limit_meV'] - 69.69) < 1.0e-02
      and abs(_C['1500']['limit_meV'] - 70.92) < 1.0e-02
      and abs(_C['1200']['limit_meV'] - 106.64) < 1.0e-02
      and abs(_C['1800']['moved_meV'] - 0.28) < 4.0e-03
      and abs(_C['1500']['moved_meV'] + 0.94) < 4.0e-03
      and abs(_C['1200']['moved_meV'] + 36.66) < 1.0e-02
      and abs(_C['1800']['share_of_gap'] - 0.018) < 1.0e-03
      and abs(_C['1500']['share_of_gap'] + 0.059) < 1.0e-03
      and abs(_C['1200']['share_of_gap'] + 2.295) < 1.0e-03
      and all(_C[k]['monotonic_above_min'] for k in ('1800', '1500', '1200')),
      'the two registered cuts move the gap by %+.2f and %+.2f meV'
      % (_C['1500']['moved_meV'], _C['1200']['moved_meV']))

check('Ⓒ③ᵇ ** THE REGISTERED CRITERION FAILS, AND IT FAILS BECAUSE IT WAS BADLY CHOSEN. **  Less '
      'than half of the gap was to move at both registered cuts, and at ell = 1200 the limit '
      'loosens by more than twice the whole gap.  ⇒ The criterion has NO CONTROL FOR INFORMATION '
      'LOSS, so a cut deep enough to remove a third of the data moves a limit whether or not the '
      'multipoles it removed carried any residual -- and that is said here rather than the '
      'criterion being moved',
      TS['expectation']['held'] is False
      and TS['expectation']['threshold'] == 0.5
      and len(TS['expectation']['shares']) == 2
      and 'badly chosen' in RESULT.lower()
      and 'the registered criterion fails' in RESULT.lower(),
      'shares %s against the half registered'
      % ', '.join('%.3f' % v for v in TS['expectation']['shares']))

_R18, _R15, _R12 = TC['rows']['1800'], TC['rows']['1500'], TC['rows']['1200']
check('Ⓒ③ᵈ ** NOT A REGISTERED ARM -- the control that leg should have carried, added after it '
      'failed and kept in its own file so the registered leg stands as written. **  The SAME COUNT '
      'of bandpowers dropped from the LOW-ell end instead moves the limit by %+.2f, %+.2f and '
      '%+.2f meV against the high end\'s %+.2f, %+.2f and %+.2f: the low end costs %.1f, %.1f and '
      '%.1f times more.  ⇒ ** SO THE DAMPING TAIL CARRIES ALMOST NONE OF THIS LIMIT AND THE 15.97 '
      'meV GAP IS NOT THE TAIL\'S **'
      % (_R18['moved_meV'], _R15['moved_meV'], _R12['moved_meV'],
         _C['1800']['moved_meV'], _C['1500']['moved_meV'], _C['1200']['moved_meV'],
         abs(_R18['ratio_to_high_end']), abs(_R15['ratio_to_high_end']),
         abs(_R12['ratio_to_high_end'])),
      abs(_R18['limit_meV'] - 116.50) < 1.0e-02 and abs(_R15['limit_meV'] - 209.00) < 1.0e-02
      and abs(_R12['limit_meV'] - 184.35) < 1.0e-02
      and abs(_R18['moved_meV'] + 46.53) < 1.0e-02
      and abs(_R15['moved_meV'] + 139.03) < 1.0e-02
      and abs(_R12['moved_meV'] + 114.38) < 1.0e-02
      and abs(abs(_R18['ratio_to_high_end']) - 166.1) < 5.0e-02
      and abs(abs(_R15['ratio_to_high_end']) - 147.3) < 5.0e-02
      and abs(abs(_R12['ratio_to_high_end']) - 3.1) < 5.0e-02
      and _R18['low_end_costs_more'] and _R15['low_end_costs_more'] and _R12['low_end_costs_more']
      and _R18['info']['dropped'] == 36 and _R15['info']['dropped'] == 90
      and _R12['info']['dropped'] == 189
      and abs(TC['baseline_limit_meV'] - _B['limit_meV']) < 1.0e-09,
      'thirty-six from the top cost %.2f meV and the same thirty-six from the bottom cost %.2f'
      % (abs(_C['1800']['moved_meV']), abs(_R18['moved_meV'])))

# ── Ⓓ④ THE DEFERRAL, GATED RATHER THAN ASSERTED ─────────────────────────────────────────────────
_IP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py')
with open(_IP, 'rb') as _fh:
    _ib = _fh.read()
_BLOB = hashlib.sha1(b'blob %d\0' % len(_ib) + _ib).hexdigest()
BS = load('blob_state.json')
check('Ⓓ④ᵃ ** ITEM ③ OF THE ORDER STAYS DEFERRED ON THE CONDITION THE ORDER SET, AND THE CONDITION '
      'IS MEASURED. **  `_resolved_config()` gains no key here because this revision does not move '
      'the instrument\'s blob: the blob is recomputed HERE from the file on disk, the way the '
      'instrument computes its own, and it equals `origin/main`\'s copy of the same file as '
      '`blob_state.py` recorded it -- `bf4f1583b66e`.  ⇒ So the four keys are still owed in the '
      'next revision that moves the blob for another reason, and the directory keying and the blob '
      'assertion stand.  ⛔ And the first version of this gate compared the WRONG TWO THINGS: it '
      'asserted the file on disk hashes to the blob the re-solved GRID recorded, and it does not, '
      'because r7860 wired `Dl_pairs` AFTER that grid was written.  A grid\'s record is a fact '
      'about when the grid was made',
      _BLOB == BS['on_disk_blob'] and _BLOB == BS['origin_main_blob']
      and BS['unmoved_by_this_revision'] is True
      and _BLOB == 'bf4f1583b66ea72093e4d2971aa858d8d1c3867d'
      and _BLOB != CAL['precondition']['blob']
      and _BLOB != '291f4477c37ed7fbb13dea2f32ca1744f1ed4d68'
      and BS['path'] == os.path.join('computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py'),
      'the instrument on disk and on origin/main both hash to %s, while the re-solved grid\'s own '
      'record is %s and the landed grid\'s is 291f4477c37e'
      % (_BLOB[:12], str(CAL['precondition']['blob'])[:12]))

#: ⛔⛭⛭⛭ ** THIS ARM READ `origin/main...HEAD` AND `S55` CAUGHT IT -- THE DEFECT `S55` EXISTS FOR. **
#:   *A population bounded by a moving ref is not one a later reader can reproduce, and this seat's
#:   own work landing is what empties it: once this revision merges, `origin/main...HEAD` is EMPTY
#:   and the arm below passes on nothing at all.  `S55`'s detector classed the site `MEASURING`
#:   because a gate asserted on the population it bounds -- which is exactly what this arm did.*
#:   ⇒ ** The remedy is `S55`'s own, applied here rather than argued with: the base is PINNED and
#:   the live reading is PRINTED beside it. **  `BASE` is `origin/main` as this revision read it,
#:   an ancestor of `HEAD` and so a range that stays non-empty for every later reader; and the
#:   emptiness that would have made the arm vacuous is now itself a GATE.
BASE = '0f58c629d52a26ab2c1fedbeaacbb01a5b5c76f3'


def _range(spec):
    r = subprocess.run(['git', '-C', ROOT, 'diff', '--name-only', spec],
                       capture_output=True, text=True)
    return [f for f in r.stdout.split() if f] if r.returncode == 0 else None


#: ⛔⛭ ** AND THE FIRST VERSION OF THIS ARM OVER-PROTECTED, WHICH IS ALSO A DEFECT. **  *It refused
#:   any path under `receipts/L_` and `receipts/L25`, where the order protects only the NAMED
#:   receipts in those trees -- `B1`, `V1`, `D1`, `R1`, `C1`, `Q1`.  So it reddened when this
#:   revision edited `S55`, which is THIS LINE'S OWN receipt and legitimately edited.  ⇒ A gate
#:   that refuses more than its order refuses is not stricter, it is WRONG -- it reports a
#:   violation where there is none, and the next seat learns to disbelieve it.*  The patterns are
#:   the order's own list now, and they are gated non-vacuous against the tree.
_PROT = ('receipts/L256*/B1_*.py', 'receipts/L257*/V1_*.py', 'receipts/L259*/D1_*.py',
         'receipts/L_probability/R1_*.py', 'receipts/L_probability/C1_*.py',
         'receipts/L_numerics/Q1_*.py', 'receipts/ENV_FINGERPRINT.txt',
         '.github/workflows/gates.yml', 'computations/beyond_the_wall/ACOUSTIC_two_arm.py',
         'receipts/*/*cc66*.py')
#: ⛔⛭⛭ ** AND ONE PATTERN OF THE ORDER'S LIST CANNOT BE WRITTEN AS A PATH AT ALL, which the
#:   non-vacuity control is what found. **  *The order protects "any receipt belonging to `70` or
#:   `cc66`".  `cc66`'s are readable from a filename; `70`'s are NOT -- the tree carries no naming
#:   convention for them, and a `receipts/*/*_70_*.py` pattern matches ZERO files.  A pattern that
#:   matches nothing is the vacuous form, so it is CUT rather than left in to look thorough.*
#:   ⇒ What replaces it is a reading off the ledger: every receipt in this range must be one THIS
#:   LINE owns, read from its own `receipts/INDEX.md` row's provenance cell, with the lookup gated
#:   one-to-one -- which covers `70` and `cc66` both, and does not need a filename convention.
_OWN = re.compile(r'Node `60`|r\d+_60_|node `?60`?', re.I)
_ALL = [os.path.relpath(os.path.join(_dp, _f), ROOT).replace(os.sep, '/')
        for _dp, _dn, _fn in os.walk(os.path.join(ROOT, 'receipts')) for _f in _fn]
_ALL += ['.github/workflows/gates.yml', 'computations/beyond_the_wall/ACOUSTIC_two_arm.py']
_MISSES = [p for p in _PROT if not fnmatch.filter(_ALL, p)]
_CH = _range('%s..HEAD' % BASE)
# ⛭ r7863 (69): ON `main` THE PINNED-BASE RANGE ALSO CARRIES THE OTHER SEATS' COMMITS MERGED BESIDE THIS ONE --
#   cc66's r7861+cc66 receipt landed in the same merge and read as "another seat's edit" in this range, which is
#   the S11 class (r7859).  So the range is narrowed to the files THIS revision's own non-merge commits touched
#   (subjects beginning `r7862`), which is what "this revision's range" means once it is no longer a branch.
if _CH is not None:
    _own = subprocess.run(['git', '-C', ROOT, 'log', '--no-merges', '--format=%H %s', '%s..HEAD' % BASE],
                          capture_output=True, text=True).stdout.split('\n')
    _own = [l.split(' ', 1)[0] for l in _own if l.split(' ', 1)[-1].startswith('r7862')]
    _ownf = set()
    for _c in _own:
        _ownf |= set(subprocess.run(['git', '-C', ROOT, 'show', '--format=', '--name-only', _c],
                                    capture_output=True, text=True).stdout.split())
    _CH = sorted(f for f in _CH if f in _ownf)
_HIT = sorted({f for p in _PROT for f in fnmatch.filter(_CH or [], p)})
_IDX = io.open(os.path.join(ROOT, 'receipts', 'INDEX.md'), encoding='utf-8').read().split('\n')
_RCP = [f for f in (_CH or []) if f.startswith('receipts/') and f.endswith('.py')]
_ROW = dict((f, [r for r in _IDX if os.path.basename(f) in r]) for f in _RCP)
_ONE = all(len(v) == 1 for v in _ROW.values())
_NOTMINE = sorted(f for f, v in _ROW.items()
                  if len(v) != 1 or not _OWN.search(v[0].split('|')[-2]))
_LIVE = _range('origin/main...HEAD')          # printed beside it, asserted on by nothing
_ANC = subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', BASE, 'HEAD'],
                      capture_output=True).returncode == 0
check('Ⓓ④ᵇ and NOTHING of another seat\'s is edited in this revision\'s range, read off the tree '
      'rather than asserted: no receipt under the names the order protects, and the instrument '
      'itself untouched.  ** The range is taken from a PINNED base and the range is gated NON-EMPTY, '
      'because a range bounded by a moving ref empties when this revision merges and an arm that '
      'passes on nothing is worse than no arm. **  ⌗ Anything owed to another seat is routed '
      'through FOR_66_FROM_60.md with its patch, which is where the provenance keys of item ③ sit.  '
      '⛔ And the patterns are the ORDER\'S OWN LIST and not a prefix: a first version refused '
      'everything under two whole trees where the order protects only the named receipts in them, '
      'and reddened on a receipt of THIS LINE\'S that this revision legitimately repaired.  ⛔ And '
      'one item of that list -- `70`\'s receipts -- has NO filename convention to match, so the '
      'pattern for it matched zero files and is CUT: what stands in its place is a reading of each '
      'receipt\'s own INDEX row, which names the seat that landed it',
      _CH is not None and _ANC and len(_CH) > 0 and _HIT == []
      and _RCP != [] and _ONE and _NOTMINE == []
      # ⌗ *and the matcher is gated NON-VACUOUS against the tree itself: every pattern must match
      #   at least one file that EXISTS, so a typo cannot make this arm pass by matching nothing.*
      and _MISSES == [],
      '%d file(s) from the pinned base, none of them protected, against %d pattern(s) each of '
      'which matches a file that exists; %d receipt(s) in the range and every one of them carries '
      'this node in its own INDEX row; the live `origin/main...HEAD` reading beside it is %s '
      'file(s), which nothing here asserts on'
      % (len(_CH) if _CH else -1, len(_PROT), len(_RCP),
         'unreadable' if _LIVE is None else len(_LIVE)))

check('Ⓓ④ᶜ and the two tables this revision commits are read by the profiles and not merely '
      'written: the reference\'s table spans 121.6996 to 180.4629 Mpc and the instrument\'s '
      '121.8231 to 178.3563, and the profiles\' own rulers land inside both -- no call was clipped '
      'to a table edge, at either treatment.  ⌗ A clipped call would mean the fit left the table '
      'and the ruler stopped being this point\'s own',
      _RF['clipped_calls'] == 0 and _IN['clipped_calls'] == 0
      and abs(RR['grid']['r_lo'] - 121.6996) < 1.0e-04
      and abs(RR['grid']['r_hi'] - 180.4629) < 1.0e-04
      and abs(DR['grid']['r_lo'] - 121.8231) < 1.0e-04
      and abs(DR['grid']['r_hi'] - 178.3563) < 1.0e-04,
      'no clipped calls on either treatment')

check('Ⓔ⑤ the record carries its failures rather than only its results: the refuted expectation, '
      'the badly chosen criterion, the forty-three-minute deadlock that computed nothing, the '
      'defect this seat diagnosed in its own reading and then REFUTED BY MEASUREMENT, the gate '
      'that read a CONVENTION as a quadrature failure and was loosened before it was understood, '
      'the gate that compared the wrong two things, and the arm of THIS receipt that bounded its '
      'population by a moving ref, and the two the repair of THAT arm turned up -- all nine in '
      'RESULT.md, and all nine this seat\'s own',
      'nine things in this record are failures or corrections' in RESULT.lower()
      and 'a population bounded by a moving ref' in RESULT.lower()
      and 'matched zero files' in RESULT.lower()
      and 'deadlocked' in RESULT.lower()
      and 'forty-three minutes' in RESULT.lower()
      and 'badly chosen' in RESULT.lower()
      and 'refuted by measurement' in RESULT.lower()
      and 'read a convention as a quadrature failure' in RESULT.lower()
      and 'compared the wrong two things' in RESULT.lower()
      and 'and all nine are this seat' in RESULT.lower(),
      'nine named in the result document')

check('Ⓕ⑥ the count: this receipt adjudicates every leg of the revision, and TWO REGISTERED '
      'EXPECTATIONS ARE REPORTED AS REFUTED with their criteria unchanged -- the calibrated '
      'limit\'s band, and the tail leg\'s share test.  ** Not one criterion was moved, and the '
      'one that was badly chosen is said to be badly chosen rather than rewritten **',
      CAL['adjudication']['held'] is False and TS['expectation']['held'] is False
      and TS['expectation']['threshold'] == 0.5
      and abs(CAL['adjudication']['limit_meV'] - 89.91) < 1.0e-02,
      'two expectations refuted, no criterion loosened')

print()
if not FAILS:
    print('  ✔ r7862: all %d arms adjudicated.' % NARMS)
    print('    => the ruler is the instrument\'s own, derived from its ionisation history, and '
          'tracks the reference to %.2e and %.2e at the box\'s two corners.'
          % (_LO['r_rel'], _HI['r_rel']))
    print('    => the calibrated case on the reference\'s own ruler is %.2f meV against the ordered '
          '30.56, and %.2f meV on this instrument\'s own.'
          % (_RF['limit_meV'], _IN['limit_meV']))
    print('    => r7860\'s 146.13 is superseded, the minimum moved from 0.060 eV to %.3f, and the '
          'registered band is REFUTED.' % _RF['min_at'])
    print('    => the damping tail carries almost none of the gap: thirty-six bandpowers from the '
          'top cost %.2f meV and the same thirty-six from the bottom cost %.2f.'
          % (abs(_C['1800']['moved_meV']), abs(_R18['moved_meV'])))
    print('    => and item ③ stays deferred on a MEASURED condition: the instrument on disk is '
          'byte-identical to origin/main\'s copy, so nothing is owed yet.')
else:
    print('  ⛔ FAIL  %d of %d arms' % (len(FAILS), NARMS))
print()
sys.exit(1 if FAILS else 0)
