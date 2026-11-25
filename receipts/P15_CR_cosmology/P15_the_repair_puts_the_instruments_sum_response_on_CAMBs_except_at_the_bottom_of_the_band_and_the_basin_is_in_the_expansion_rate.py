# -*- coding: utf-8 -*-
"""⛭⛭⛭ THE FERMI-DIRAC REPAIR PUTS THE INSTRUMENT'S SUM RESPONSE ONTO CAMB's IN TT AND EE --
EVERYWHERE EXCEPT THE BOTTOM OF THE BAND, WHICH IS THE SAME STRETCH THE LEAN WAS LOCATED IN -- AND
THE TWO BASINS ARE SEPARATED IN THE EXPANSION RATE ALONE, WITH A BARRIER BETWEEN THEM.

COMPUTES: the sum response at SPECTRUM level, `Dl(Sum)/Dl(0) - 1`, for TT, EE and TE at three sums,
on the control arm of two banks differing in exactly ONE switch, against a CAMB leg run here at the
control's own centre with the total matter held and `omch2` reduced by `omega_nu`, sampled on the
banks' own two hundred and thirty-eight multipoles; the count of multipoles departing a band fixed
before the measurement, per block, per sum, on both CAMB legs; the direction the repair moves the
instrument, per block; the ell-dependence of every response at the two ends of the band; and, on
the basin side, the two recorded basin vectors pushed through the instrument's OWN parameter map
and the chi-squared walked along the segment joining them.
** IT PINS AS RESULTS: zero departing multipoles in TT and in EE at the lowest sum with the repair
on, against forty-seven and one hundred and twenty-eight with it off; the surviving departures as
runs at the BOTTOM of the band, `100`-`212` in TT and `100`-`196` in EE; the instrument's `0.070234`
against CAMB's `0.039702` at `ell = 100` and their agreement to about one per cent at `ell = 1996`;
the basins' separation of `3.302` km/s/Mpc in `H0` and `1.6511` grid steps, against `0.0223` steps
in the next largest parameter; and the barrier's height, `7.6718` over the higher end. **
⛔ ** AND IT PINS WHAT WAS REFUTED AND WHAT WAS NOT ESTABLISHED: ** the order's candidate predicted
a nearly ell-INDEPENDENT response and the instrument's is MORE ell-dependent than CAMB's, so that
half is refuted in the form it was stated; the other half is CONSISTENT with the shape and is NOT
established by it; and whether the reference branches along `H0` is UNESTABLISHED from the record
that was supposed to answer it, and is pinned as unestablished rather than inferred.
⛔ ** NO LIMIT AND NO ENVELOPE CROSSING IS PINNED HERE, because this revision read none. **

⌷ ** THE ID. **  `69` ordered this as `r7871`, which merged `r7870`, retired the fork, and ruled
that profiles are read on a closed cross-seeded envelope from now on.

⚠ ** THE SECOND BANK IN THIS COMPARISON WAS RUN RATHER THAN READ, and the reason is the arm: the
older bank carries NEITHER switch key, so it cannot say it is off, AND it differs in more than one
switch, so it would not isolate the one under test even if it could. **

    NODE=60 python3 <this file>

Written r7872 (60).  Stated for reversal.
"""
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
D = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                 'r7872_60_the_sum_response_at_spectrum_level_against_camb_and_the_lower_basins_'
                 'direction')
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

RSP = load('response.json')
BAS = load('basin_direction.json')
RGA = load('basin_across_rungs_nufd_dneff044.json')
RGB = load('basin_across_rungs_nufd_only.json')
RESULT = text('RESULT.md')
PRED = text('PREDICTION.md')
GEN = text('gen_pol_nufd_off.sh')
#: ⛔ *the prose is matched on a WHITESPACE-FLATTENED copy.  An arm that matched the raw file would
#: pass or fail on where a line happened to wrap, which is a fact about the editor and not about
#: the record -- and four arms of this receipt did exactly that on the first run.*
RESULT = ' '.join(RESULT.split())
PRED = ' '.join(PRED.split())
GEN_FLAT = ' '.join(GEN.split())


def dep(blk, s, leg, arm, key='n_departing'):
    return RSP['departures']['%s|%.2f|%s|%s' % (blk, s, leg, arm)][key]


def depr(blk, s, leg, arm, key='n_departing'):
    return RSP['departures_rms_normalised']['%s|%.2f|%s|%s' % (blk, s, leg, arm)][key]


def shape(blk, s, who, key):
    return RSP['shape']['%s|%.2f|%s' % (blk, s, who)][key]


# ── Ⓐ the comparison is like for like, and that is measured rather than claimed ─────────────────
check('Ⓐ①ᵃ ** THE TWO BANKS DIFFER IN EXACTLY ONE SWITCH, read off EACH POINT\'S OWN config and '
      'not off a directory name: the repair reads TRUE at every nonzero sum on one arm and FALSE '
      'at every sum on the other, with the mass carried on BOTH. **  ⇒ *at zero mass the switch is '
      'conditioned off by its own definition, so the two zero-sum points are the same program and '
      'the ratio\'s denominator is not a difference*',
      all(RSP['switch_states']['on'][t]['NUFD'] is True for t in ('S006', 'S030', 'S060'))
      and RSP['switch_states']['on']['S000']['NUFD'] is False
      and all(RSP['switch_states']['off'][t]['NUFD'] is False
              for t in ('S000', 'S006', 'S030', 'S060'))
      and all(abs(RSP['switch_states'][n][t]['MNU'] - v) < 1e-12
              for n in ('on', 'off') for t, v in (('S006', 0.06), ('S030', 0.30), ('S060', 0.60))),
      'on: %s ; off: %s' % (RSP['switch_states']['on']['S060']['NUFD'],
                            RSP['switch_states']['off']['S060']['NUFD']))

check('Ⓐ①ᵃᵃ ⛭ and the OFF arm was RUN, from the previous revision\'s own generator with ONE switch '
      'flipped, which is why nothing else can have drifted between the two banks  ⇒ *the generator '
      'carries the reason in its own header: the older bank has NEITHER key, so it cannot say it '
      'is off, and it differs in more than one switch, so it would not isolate this one anyway*',
      'NUFD=0 ARM=lcdm' in GEN and 'NUFD=0 ARM=cr' in GEN
      and 'NUFD=1 ARM=' not in GEN          # the INVOCATIONS, not the header that quotes the old one
      and 'cannot say' in GEN_FLAT and 'more than one thing' in GEN_FLAT
      and 'NARROWED TO WHAT ITEM' in GEN_FLAT)

check('Ⓐ①ᵃᵇ ⛭ and nothing was interpolated, re-binned or carried across banks: both banks\' '
      'multipole vectors were compared ELEMENT FOR ELEMENT, two hundred and thirty-eight of them '
      'from `100` to `1996`, and the registered BLOCKED outcome is empty',
      RSP['blocked'] == [] and RSP['n_ls'] == 238
      and RSP['ls'][0] == 100 and RSP['ls'][-1] == 1996
      and 'OWN S000' in RSP['denominator'],
      '%d multipoles, %d blocked' % (RSP['n_ls'], len(RSP['blocked'])))

check('Ⓐ①ᵃᶜ ⛭ and the CAMB leg holds the TOTAL matter as the instrument does, which is the whole '
      'of the like-for-like: `omega_nu` grows with the sum and is taken OUT of the cold component '
      'rather than added to the total',
      abs(RSP['camb_omnuh2']['0.0']) < 1e-12
      and RSP['camb_omnuh2']['0.06'] < RSP['camb_omnuh2']['0.3'] < RSP['camb_omnuh2']['0.6']
      and abs(RSP['camb_omnuh2']['0.6'] - 0.0064487) < 5e-7,
      'omega_nu at 0.60 eV = %.7f' % RSP['camb_omnuh2']['0.6'])

# ── Ⓑ ①ᵇ the departure, against the band fixed before the measurement ──────────────────────────
check('Ⓑ①ᵇ ⛭⛭⛭ ** WITH THE REPAIR ON, THE INSTRUMENT\'S TT AND EE SUM RESPONSE IS INSIDE THE '
      'REGISTERED BAND AT EVERY ONE OF THE TWO HUNDRED AND THIRTY-EIGHT MULTIPOLES AT THE LOWEST '
      'SUM -- `0` departing in each -- WHERE WITH IT OFF THE SAME COUNTS ARE `47` AND `128`. **  '
      '⇒ *the band is five parts in a thousand of `Dl(0)`, which is the band the background itself '
      'was verified to, and it was fixed in the registration before any spectrum was read*',
      dep('TT', 0.06, 'unlensed', 'on') == 0 and dep('EE', 0.06, 'unlensed', 'on') == 0
      and dep('TT', 0.06, 'unlensed', 'off') == 47
      and dep('EE', 0.06, 'unlensed', 'off') == 128
      and abs(RSP['threshold_of_Dl0'] - 5.0e-3) < 1e-12,
      'on 0 and 0; off %d and %d' % (dep('TT', 0.06, 'unlensed', 'off'),
                                     dep('EE', 0.06, 'unlensed', 'off')))

check('Ⓑ①ᵇᵃ and the ordering holds at the two higher sums as well, by an order of magnitude at '
      'each: TT `5` and `15` departing with the repair on against `190` and `211` with it off, EE '
      '`10` and `63` against `203` and `220`',
      (dep('TT', 0.30, 'unlensed', 'on'), dep('TT', 0.60, 'unlensed', 'on')) == (5, 15)
      and (dep('TT', 0.30, 'unlensed', 'off'), dep('TT', 0.60, 'unlensed', 'off')) == (190, 211)
      and (dep('EE', 0.30, 'unlensed', 'on'), dep('EE', 0.60, 'unlensed', 'on')) == (10, 63)
      and (dep('EE', 0.30, 'unlensed', 'off'), dep('EE', 0.60, 'unlensed', 'off')) == (203, 220))

check('Ⓑ①ᵇᵇ ⛭⛭ ** AND WHAT SURVIVES THE REPAIR SITS AT THE BOTTOM OF THE BAND: the longest '
      'departing run is `100`-`212` in TT and `100`-`196` in EE, and TT\'s LARGEST discrepancy is '
      'AT `ell = 100` at both higher sums. **  ⇒ *`r7869` located the low-end lean at multipoles '
      '`100`-`207`; the surviving spectrum-level departure occupies the same stretch, which is a '
      'coincidence of RANGES between two independently measured things and is recorded as that*',
      dep('TT', 0.60, 'unlensed', 'on', 'runs')[0][:2] == [100, 212]
      and dep('EE', 0.60, 'unlensed', 'on', 'runs')[0][:2] == [100, 196]
      and dep('TT', 0.30, 'unlensed', 'on', 'at_ell') == 100
      and dep('TT', 0.60, 'unlensed', 'on', 'at_ell') == 100
      and '100' in RESULT and '207' in RESULT,
      'TT run %s, EE run %s' % (dep('TT', 0.60, 'unlensed', 'on', 'runs')[0][:2],
                                dep('EE', 0.60, 'unlensed', 'on', 'runs')[0][:2]))

check('Ⓑ①ᵇᶜ and the worst discrepancy with the repair on is smaller than with it off in every '
      'block and at every sum, by factors between two and ten: `0.0305` against `0.0838` in TT at '
      'the top sum, `0.0159` against `0.1581` in EE',
      all(dep(b, s, 'unlensed', 'on', 'max_abs_diff')
          < dep(b, s, 'unlensed', 'off', 'max_abs_diff')
          for b in ('TT', 'EE') for s in (0.06, 0.30, 0.60))
      and abs(dep('TT', 0.60, 'unlensed', 'on', 'max_abs_diff') - 0.03053) < 5e-5
      and abs(dep('TT', 0.60, 'unlensed', 'off', 'max_abs_diff') - 0.08384) < 5e-5
      and abs(dep('EE', 0.60, 'unlensed', 'on', 'max_abs_diff') - 0.01589) < 5e-5
      and abs(dep('EE', 0.60, 'unlensed', 'off', 'max_abs_diff') - 0.15811) < 5e-5)

# ── Ⓒ ①ᶜ the direction, with the mixed case reported as mixed ──────────────────────────────────
check('Ⓒ①ᶜ ** THE REPAIR MOVES THE INSTRUMENT TOWARDS CAMB IN EVERY BLOCK ON THE LIKE-FOR-LIKE '
      'LEG. **  ⇒ *mean absolute discrepancy over the multipoles where either arm departs: TT '
      '`0.00088` against `0.01693` at the middle sum, EE `0.00172` against `0.03607` -- factors of '
      'nineteen and twenty-one*',
      all(RSP['direction']['unlensed']['per_block'][b]['verdict'] == 'TOWARDS'
          for b in ('TT', 'EE', 'TE'))
      and 'TOWARDS, in every block' in RSP['direction']['unlensed']['overall'],
      RSP['direction']['unlensed']['overall'])

check('Ⓒ①ᶜᵃ ⛔ ** AND ON THE LENSED LEG THE VERDICT IS MIXED AND IS REPORTED AS MIXED: TT and EE '
      'towards, TE away. **  ⇒ *the registration fixed in advance that a mixed result is NOT to be '
      'resolved by choosing a block, averaging them or weighting them, and it was not -- a '
      'direction that is not common does not exist*',
      RSP['direction']['lensed']['per_block']['TE']['verdict'] == 'AWAY'
      and RSP['direction']['lensed']['per_block']['TT']['verdict'] == 'TOWARDS'
      and RSP['direction']['lensed']['per_block']['EE']['verdict'] == 'TOWARDS'
      and 'MIXED' in RSP['direction']['lensed']['overall']
      and 'not resolved by choosing' in RSP['direction']['lensed']['overall']
      and 'reported as mixed' in RESULT
      and 'A mixed result is reported as mixed' in PRED
      and 'not resolved by choosing a block' in PRED,
      RSP['direction']['lensed']['overall'])

# ── Ⓓ ①ᵈ the ell-dependence: half the candidate refuted, half consistent and NOT established ───
check('Ⓓ①ᵈ ⛭⛭⛭ ** THE ORDER\'S CANDIDATE IS REFUTED IN THE FORM IT WAS STATED. **  *"No '
      'free-streaming scale" predicts a nearly ell-INDEPENDENT response; the instrument\'s falls '
      'off FASTER with ell than CAMB\'s -- top over bottom `0.323` against `0.564` at the top sum '
      '-- so it is MORE scale-dependent, not less.*  ⇒ *this arm asserts the refutation of a '
      'candidate this seat did not author, on the seat\'s own measurement*',
      shape('TT', 0.60, 'instrument on', 'ratio') < shape('TT', 0.60, 'CAMB unlensed', 'ratio')
      and abs(shape('TT', 0.60, 'instrument on', 'ratio') - 0.3232) < 5e-4
      and abs(shape('TT', 0.60, 'CAMB unlensed', 'ratio') - 0.5643) < 5e-4
      and 'refuted in the form it was stated' in RESULT,
      '%.4f against %.4f' % (shape('TT', 0.60, 'instrument on', 'ratio'),
                             shape('TT', 0.60, 'CAMB unlensed', 'ratio')))

check('Ⓓ①ᵈᵃ ** AND WHAT THE SHAPE IS INSTEAD IS A LOW-ell EXCESS GROWING WITH THE SUM: at '
      '`ell = 100` the instrument returns `0.070234` against CAMB\'s `0.039702` at the top sum, a '
      'factor `1.77`, and `0.029072` against `0.021022` at the middle sum, a factor `1.38`, while '
      'at `ell = 1996` the two agree to about ONE PER CENT. **',
      abs(shape('TT', 0.60, 'instrument on', 'bottom') - 0.070234) < 5e-6
      and abs(shape('TT', 0.60, 'CAMB unlensed', 'bottom') - 0.039702) < 5e-6
      and abs(shape('TT', 0.30, 'instrument on', 'bottom') - 0.029072) < 5e-6
      and abs(shape('TT', 0.30, 'CAMB unlensed', 'bottom') - 0.021022) < 5e-6
      and abs(shape('TT', 0.60, 'instrument on', 'top') - 0.022702) < 5e-6
      and abs(shape('TT', 0.60, 'CAMB unlensed', 'top') - 0.022404) < 5e-6
      and abs(shape('TT', 0.60, 'instrument on', 'top')
              / shape('TT', 0.60, 'CAMB unlensed', 'top') - 1.0) < 0.02,
      'bottom %.6f against %.6f; top %.6f against %.6f'
      % (shape('TT', 0.60, 'instrument on', 'bottom'),
         shape('TT', 0.60, 'CAMB unlensed', 'bottom'),
         shape('TT', 0.60, 'instrument on', 'top'),
         shape('TT', 0.60, 'CAMB unlensed', 'top')))

check('Ⓓ①ᵈᵇ ⛔ ** AND THE SHAPE IS NOT OFFERED AS THE MECHANISM. **  The record states that it is '
      'CONSISTENT with the surviving half of the candidate -- a subtraction from the clustering '
      'matter applied at ALL times -- and that consistency is not establishment.  ⇒ *an arm that '
      'read the mechanism off the shape would be asserting more than this revision measured*',
      'does not establish it' in RESULT
      and 'A shape agreeing with a mechanism is not the mechanism' in RESULT
      and 'claims no mechanism' in RESULT)

check('Ⓓ①ᵈᶜ ⌗ and the low-ell departure is not a lensing artefact, which is measured rather than '
      'argued: CAMB\'s two legs differ by under `0.0003` at `ell = 100` against a departure of '
      '`0.0305` there, a factor above one hundred -- so the choice of leg matters at the TOP of '
      'the band and is irrelevant at the BOTTOM, which is where the surviving departure is',
      abs(shape('TT', 0.60, 'CAMB unlensed', 'bottom')
          - shape('TT', 0.60, 'CAMB lensed', 'bottom')) < 3e-4
      and dep('TT', 0.60, 'unlensed', 'on', 'max_abs_diff') > 100 * abs(
          shape('TT', 0.60, 'CAMB unlensed', 'bottom')
          - shape('TT', 0.60, 'CAMB lensed', 'bottom')),
      'legs differ by %.6f at ell 100'
      % abs(shape('TT', 0.60, 'CAMB unlensed', 'bottom')
            - shape('TT', 0.60, 'CAMB lensed', 'bottom')))

# ── Ⓔ TE: the criterion unmoved, the degeneracy named, the second form beside it ───────────────
check('Ⓔ①ᵉ ⛔ ** THE REGISTERED CRITERION WAS APPLIED UNMOVED WHERE IT IS DEGENERATE, AND THE '
      'DEGENERACY WAS COUNTED RATHER THAN THE CRITERION SWAPPED: ** TE crosses zero, so a pointwise '
      'threshold in `|Dl(0)|` goes to zero with it; `5` multipoles sit under one per cent of the '
      'block\'s own RMS, and TE\'s maximum values -- up to `37` -- are that degeneracy and not a '
      'measurement',
      RSP['te_degeneracy']['n_multipoles_under_one_percent_of_block_rms'] == 5
      and 'applied as registered' in RSP['te_degeneracy']['note']
      and dep('TE', 0.60, 'unlensed', 'on', 'max_abs_diff') > 30.0
      and 'not readable as a percentage' in RESULT,
      '%d degenerate multipoles; TE max %.1f'
      % (RSP['te_degeneracy']['n_multipoles_under_one_percent_of_block_rms'],
         dep('TE', 0.60, 'unlensed', 'on', 'max_abs_diff')))

check('Ⓔ①ᵉᵃ ⛭⛭ ** AND THE SECOND FORM THE REGISTRATION PUT BESIDE IT VINDICATED THE WORRY: with '
      'each side normalised by ITS OWN block RMS, TE\'s departure at the middle sum goes from `119` '
      'multipoles to `0`. **  ⇒ *so the wide TE departure the pointwise form reported there was the '
      'criterion\'s degeneracy and not the instrument\'s -- and keeping the criterion unmoved while '
      'ADDING a reading is what let that be visible at all*',
      dep('TE', 0.30, 'unlensed', 'on') == 119
      and depr('TE', 0.30, 'unlensed', 'on') == 0
      and 'not the registered criterion' in RSP['departures_rms_normalised_note'],
      '%d under the registered form, %d under the additional one'
      % (dep('TE', 0.30, 'unlensed', 'on'), depr('TE', 0.30, 'unlensed', 'on')))

check('Ⓔ①ᵉᵇ and the second form says the SAME thing about where the departure is, which is why it '
      'is worth having: TT\'s surviving runs are `100`-`156` and `100`-`276` at the two higher '
      'sums, TE\'s at the top sum is `188`-`308`, and EE is inside the band at EVERY multipole at '
      'both of the two lower sums',
      depr('TT', 0.30, 'unlensed', 'on', 'runs')[0][:2] == [100, 156]
      and depr('TT', 0.60, 'unlensed', 'on', 'runs')[0][:2] == [100, 276]
      and depr('TE', 0.60, 'unlensed', 'on', 'runs')[0][:2] == [188, 308]
      and depr('EE', 0.06, 'unlensed', 'on') == 0
      and depr('EE', 0.30, 'unlensed', 'on') == 0)

# ── Ⓕ ② the basin's direction, through the instrument and not through an index ─────────────────
_od = BAS['one_direction']
_pm = {r['name']: r for r in BAS['params']}
check('Ⓕ②ᵃ ⛭⛭⛭ ** THE TWO BASINS ARE SEPARATED IN THE EXPANSION RATE ALONE: `65.292248` against '
      '`68.594396` km/s/Mpc, `1.6511` grid steps, where the next largest separation is `0.0223` '
      'steps -- SEVENTY-FOUR times smaller -- and the component the profiler holds separately is '
      'identical to seven digits. **  ⇒ *named through the instrument\'s OWN parameter map and not '
      'off a slot index, because a slot index is a label and a label has to be checked against the '
      'object before two things are identified by it*',
      _od['holds'] is True and _od['largest'] == 'H0'
      and abs(_od['largest_steps'] - 1.6511) < 5e-4
      and abs(_od['next_largest_steps'] - 0.0223) < 5e-4
      and abs(_pm['H0']['lower_phys'] - 65.292248) < 5e-6
      and abs(_pm['H0']['higher_phys'] - 68.594396) < 5e-6
      and abs(_pm['H0']['d_phys'] - 3.302148) < 1e-5
      and abs(BAS['tau']['d']) < 1e-7
      and 'H0' in BAS['parameter_map']['keys_phys_returns'],
      '%s at %.4f steps; next %s at %.4f'
      % (_od['largest'], _od['largest_steps'], _od['next_largest'], _od['next_largest_steps']))

_bar = BAS['barrier']
check('Ⓕ②ᵃ′ ** AND THERE IS A BARRIER, so the word survives its own test: on the straight segment '
      'joining the two vectors the chi-squared rises to `2193.8672`, which is `7.6718` above the '
      'HIGHER end and `20.2085` above the lower. **  ⇒ *two vectors with different chi-squared are '
      'two minima only if something sits between them; the registered negative was that there is '
      'nothing between them, in which case the previous revision\'s own word for them was wrong*',
      _bar['holds'] is True
      and abs(_bar['interior_max'] - 2193.8672) < 5e-4
      and abs(_bar['height_over_higher_end'] - 7.6718) < 5e-4
      and abs(_bar['height_over_lower_end'] - 20.2085) < 5e-4
      and _bar['n_points'] == 81,
      '%.4f at t=%.4f, %.4f over the higher end'
      % (_bar['interior_max'], _bar['interior_max_at_t'], _bar['height_over_higher_end']))

check('Ⓕ②ᵇ ⛔ ** AND WHETHER THE REFERENCE BRANCHES ALONG THAT DIRECTION IS PINNED AS '
      'UNESTABLISHED, which is the registered outcome and not a gap: ** the record that was '
      'supposed to answer it carries each ruler\'s fitted rate and NO key naming a branch or a '
      'basin at all.  ⇒ *an order\'s summary of another seat\'s measurement is not that '
      'measurement, and this arm declines to treat it as one*',
      BAS['reference']['resolves_a_branch_along_the_direction'] is False
      and BAS['reference']['keys_naming_a_branch_or_basin'] == []
      and len(BAS['reference']['keys_naming_the_direction']) == 2
      and 'UNESTABLISHED' in RESULT and 'routed' in RESULT,
      'keys naming a branch: %s' % BAS['reference']['keys_naming_a_branch_or_basin'])

# ── Ⓖ the two additional readings are pinned AS additional ─────────────────────────────────────
check('Ⓖ⓵ ⌗ the barrier is on BOTH rungs and is LARGER without the offset -- `22.8620` over the '
      'higher end against `7.6718` -- so the bimodality is not the offset\'s; and BOTH files '
      'declare themselves UNREGISTERED, which is the point of pinning them here',
      RGA['barrier'] is True and RGB['barrier'] is True
      and abs(RGA['height_over_higher_end'] - 7.6718) < 5e-4
      and abs(RGB['height_over_higher_end'] - 22.8620) < 5e-4
      and RGA['registered'] is False and RGB['registered'] is False
      and 'no registered verdict rests on it' in RGA['note'],
      '%.4f at +0.044 against %.4f with no offset'
      % (RGA['height_over_higher_end'], RGB['height_over_higher_end']))

check('Ⓖ⓶ ⌗ and both of the reference\'s fitted rates sit in the UPPER branch, one within `0.030` '
      'km/s/Mpc of it -- which says WHERE ITS FITS ARE and NOT that it has no second one, a '
      'distinction the record keeps rather than blurs',
      all(v['nearer'] == 'higher' for v in BAS['reference']['fitted_H0_per_mode'].values())
      and abs(BAS['reference']['fitted_H0_per_mode']['rd_camb']['to_higher'] - 0.030427) < 5e-6
      and abs(BAS['reference']['fitted_H0_per_mode']['rd_min']['to_higher'] + 0.395809) < 5e-6
      and BAS['reference']['additional_reading_not_registered'] is True
      and 'That says **where its fits are**' in RESULT
      and '**not** that it has no second one' in RESULT,
      '%+.6f and %+.6f from the higher basin'
      % (BAS['reference']['fitted_H0_per_mode']['rd_camb']['to_higher'],
         BAS['reference']['fitted_H0_per_mode']['rd_min']['to_higher']))

# ── Ⓗ the registration, and what this revision refused to do ───────────────────────────────────
check('Ⓗ③ ** THE REGISTRATION CAME FIRST AND ITS NEGATIVES WERE REACHABLE: ** the file declares '
      'six reads taken before it, states that which parameter each basin component IS had '
      'deliberately NOT been established, fixes the departure threshold before any spectrum is '
      'read, and writes the mixed case and the unestablished case in as live outcomes -- two of '
      'which then fired',
      'committed and pushed before any computation' in PRED
      and 'has NOT been established' in PRED
      and 'five parts in a thousand' in PRED
      and 'MIXED' in PRED and 'UNESTABLISHED' in PRED)

check('Ⓗ③ᵃ ⛔ AND THE SCOPE IS DECLARED: no limit is read and NO ENVELOPE CROSSING APPEARS IN THIS '
      'RECORD AT ALL, the arm of record is not re-run, no mechanism is claimed, and the lean\'s '
      'mechanism stays carried -- each named in the record as a decision rather than left for a '
      'reader to notice',
      'No limit is read and no envelope crossing appears in this record at all' in RESULT
      and 'The arm of record was not re-run' in RESULT
      and 'stays carried' in RESULT
      and 'No other seat' in RESULT)

check('Ⓗ③ᵇ ⚠ and THREE things in this record are this seat\'s own, including that the off arm '
      'nearly was not run and that the order\'s candidate came back half refuted -- the half the '
      'order leaned on most',
      "THIS SEAT'S OWN" in RESULT.upper()
      and 'nearly was not run' in RESULT
      and 'half refuted' in RESULT
      and 'would have reported the better number as the registered one' in RESULT)

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
