# -*- coding: utf-8 -*-
"""⛭⛭⛭ THE WEIGHT CHANGE ALONE ALREADY CROSSES ONE AND ALREADY TAKES EE OUT OF BAND, SO THE
OVERSHOOT IS NOT THE CONTINUITY OR THE EULER CHANGE'S DOING; THE THREE CHANGES ARE NEARLY ADDITIVE
IN `A`; AND THE EXACT ADIABATIC SOUND SPEED IS ONLY A BETTER MEMBER OF THE SAME FAMILY.

COMPUTES: the decomposition of the previous revision's three-part repair into its three changes --
the source weight, the continuity equation and the Euler equation -- each run ALONE through the
instrument at two sums, with `A` and `eps` refitted on each against CAMB by the fit of record,
executed and not re-implemented, its reproduction leg required to return that fit's four headline
amplitudes first; the attribution of the joint move to the three separate ones, registered in
advance as a MEASUREMENT of whether the question is well posed at all; the exact adiabatic sound
speed `c_a^2 = w - w-dot/(3H(1+w))` in place of `c_s^2 = w`, with all three changes live and again
with the subset the decomposition names; and the two new switches' byte-identity when off, their
five refusals, and the tightening of the eighth strip class measured both ways.
** IT PINS AS RESULTS: the weight change alone at `A = 0.99510` and `1.05621` in TT -- which is
PAST one at the smaller sum, by `0.00490` -- with EE at `0.04005` and `0.05961` from one, the
second outside the `0.05` band; the continuity change alone at `1.13111` and `1.26394`, and the
Euler change alone at `1.05464` and `1.13902`, removing `0.1353`/`0.1081` and `0.6396`/`0.5302` of
the excess against the weight change's `0.9677`/`0.8101`; the attribution ratios `0.9527` and
`0.8906`, from summed moves `-0.274003` and `-0.428590` against the joint `-0.287610` and
`-0.481260`; and the exact sound speed at `0.92115` and `0.90786` against `c_s^2 = w`'s `0.86401`
and `0.81466`, removing `0.4202` and `0.5029` of the overshoot, with EE back INSIDE its band at the
smaller sum (`0.04650`) and outside it at the larger (`0.07225`). **
⛔ ** AND IT PINS A DEFECT OF THIS SEAT'S OWN REGISTRATION, NOT OF ITS CODE: ** the registered rows
`Ⓒ` and `Ⓓ` are NOT mutually exclusive and the result fires BOTH -- a crossing and an EE band
violation, at different sums -- and the first version of the verdict block hid that behind an
`elif` chain that silently preferred `Ⓒ`, the softer of the two, since `Ⓓ` is the row that reads
REFUTED. Every firing row is reported now, the overlap is named rather than resolved, and not one
registered condition is touched.
⛔ ** AND IT PINS THE ORDERING OF THE SUBSET CHOICE, because the registration demanded it: ** the
subset is `CE`, named by exclusion of the one member the decomposition condemns, and the naming was
committed and pushed BEFORE either of its legs existed -- which is checked here as a fact about the
record and not asserted.
⛔ ** NO LIMIT IS PINNED HERE. ** The only registered row that licenses one is `Ⓔ` and no arm
reached it; the verdicts are `Ⓒ+Ⓓ` on item ① and `Ⓖ` on item ②.

⌷ ** THE ID. **  `69` ordered this as `r7877`, which merged `r7876`, took this line's fork (a) --
EE's agreement is a CONSTRAINT -- and asked for the decomposition, the exact adiabatic sound speed,
and the tightening of the fifth and seventh strip classes.

⚠ ** TWO THINGS IN THIS RECORD ARE THIS SEAT'S OWN: ** the overlapping registration above, and a
naming rule this seat followed against its own expectation -- the subset the rule names drops the
only one of the three changes with a closure argument behind it.

    NODE=60 python3 <this file>

Written r7878 (60).  Stated for reversal.
"""
import io
import json
import os
import re
import subprocess
import sys

import numpy

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
D = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                 'r7878_60_the_three_changes_decomposed_and_the_exact_adiabatic_sound_speed')
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
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

RF = load('refit_parts.json')
SW = load('switch_arms.json')
TG = load('tighten.json')
CK = load('clock.json')
LV = load('leverage.json')
#: ⛔ *the prose is matched on a WHITESPACE-FLATTENED copy -- four arms of an earlier revision's
#: receipt failed on where a line happened to wrap, which is a fact about the editor and not about
#: the record.*
RESULT = ' '.join(text('RESULT.md').split())
PRED = ' '.join(text('PREDICTION.md').split())
NAMED = ' '.join(text('SUBSET_NAMED.md').split())
INST = text('ACOUSTIC_two_arm.py', BW)
GEN = ' '.join(text('gen_parts.sh').split())

A = RF['arms']
L = RF['A_landed']
WCE = RF['A_WCE']
AT = RF['attribution']


def fit(arm, key, what='best_A'):
    return A[arm]['fits'][key][what]


def ee(arm, s):
    return abs(fit(arm, 'EE|%s' % s) - 1.0)


# ══ Ⓐ ① WHAT THE TWO SWITCHES ARE, READ OFF THE INSTRUMENT ══════════════════════════════════════
# *The decomposition is only readable if the three changes really are separable in the file, and
#  that is a fact about the source, not about the banks.*

check('Ⓐ①ᵃ ⛭ ** THE THREE CHANGES ARE SEPARATELY ADDRESSABLE: ** `NUPARTS` is a LETTER SET, '
      'defaulting to all three, and the weight, continuity and Euler changes are each gated on '
      'their own letter.  ⇒ *before this revision nothing could run them apart*',
      INST.count("NUPARTS = os.environ.get('NUPARTS', 'WCE')") == 1
      and INST.count("if 'W' in NUPARTS:") == 1
      and INST.count("if 'C' in NUPARTS:") == 2
      and INST.count("if 'E' in NUPARTS:") == 2)

check('Ⓐ①ᵇ ⛭ and the exact adiabatic sound speed is one conditional expression, in BOTH '
      'right-hand sides, with `c_s^2 = w` as its own else -- so `NUCA` selects between two '
      'members of the same family and nothing else',
      INST.count('_cs2 = (_w - _wd / (3.0 * float(Hc_of(e)) * (1.0 + _w))) if NUCA else _w') == 2
      and INST.count("NUCA = os.environ.get('NUCA', '0') == '1'") == 1)

check('Ⓐ①ᶜ ⛭ ** AND THE LANDED LINES ARE UNTOUCHED AND NOW OCCUR FOUR TIMES EACH: ** twice as the '
      'inner else of the letter gates and twice as the outer else of the switch, byte-identical.  '
      '⇒ *that is why the eighth strip class still reduces this tree to the banked blob*',
      INST.count('out[:, 4] = -(4 / 3) * tn + DRC * 4 * Php') == 4
      and INST.count('out[:, 5] = kk ** 2 * (dn / 4 - sig) + DRE * kk ** 2 * Ps') == 4,
      '%d and %d occurrence(s)'
      % (INST.count('out[:, 4] = -(4 / 3) * tn + DRC * 4 * Php'),
         INST.count('out[:, 5] = kk ** 2 * (dn / 4 - sig) + DRE * kk ** 2 * Ps')))

check('Ⓐ①ᵈ ⌗ and both names are in the switch snapshot, so every bank of this revision records '
      'which letters and which sound speed produced it',
      "'NUPARTS': NUPARTS," in INST and "'NUCA': bool(NUCA)," in INST)

#: ⌘ ** AND THE TEN BANKS' OWN PROVENANCE, which is also where the two sums are pinned: ** every
#:   leg records the sum it ran at, the letter set it ran with and which sound speed, so the table's
#:   rows cannot be mislabelled, and `0.30` and `0.60` are facts about the banks rather than figures
#:   printed beside a receipt that would not notice if they were wrong.
_SPECS = {'S030W': (0.30, 'W', False), 'S060W': (0.60, 'W', False),
          'S030C': (0.30, 'C', False), 'S060C': (0.60, 'C', False),
          'S030E': (0.30, 'E', False), 'S060E': (0.60, 'E', False),
          'S030A1': (0.30, 'WCE', True), 'S060A1': (0.60, 'WCE', True),
          'S030CE': (0.30, 'CE', True), 'S060CE': (0.60, 'CE', True)}
_CFG, _BLOBS = {}, set()
for _tag in sorted(_SPECS):
    _z = numpy.load(os.path.join(D, 'parts', 'lcdm_%s_tt.npz' % _tag), allow_pickle=True)
    _c = json.loads(str(_z['config']))
    _CFG[_tag] = _c
    _BLOBS.add(_c.get('instrument_blob'))

check('Ⓐ①ᵉ ⛭ ** THE TEN BANKS RECORD THE SUMS THEY RAN AT, AND THEY ARE EXACTLY `0.30` AND '
      '`0.60` eV: ** five legs at each, with the letter set and the sound speed each leg was '
      'specified with.  ⇒ *so the sums are pinned where they are used, and a mislabelled row '
      'would fail here*',
      all(abs(_CFG[t]['MNU'] - _SPECS[t][0]) < 5e-09 for t in _SPECS)
      and sum(1 for t in _SPECS if abs(_CFG[t]['MNU'] - 0.30) < 5e-09) == 5
      and sum(1 for t in _SPECS if abs(_CFG[t]['MNU'] - 0.60) < 5e-09) == 5
      and all(_CFG[t]['NUPARTS'] == _SPECS[t][1] for t in _SPECS)
      and all(bool(_CFG[t]['NUCA']) is _SPECS[t][2] for t in _SPECS)
      and all(_CFG[t]['NUPERT'] and _CFG[t]['NUFD'] and _CFG[t]['ARM'] == 'lcdm' for t in _SPECS),
      '%d bank(s)' % len(_CFG))

check('Ⓐ①ᶠ ⌘ and all ten were produced by ONE state of the instrument -- a single recorded '
      'blob -- so no row of the table was generated by a different file from the others',
      len(_BLOBS) == 1 and None not in _BLOBS,
      '%d distinct blob(s): %s' % (len(_BLOBS), sorted(b[:12] for b in _BLOBS)))

# ══ Ⓑ ② THE SWITCHES ARE INERT OFF AND THE REFUSALS HOLD ════════════════════════════════════════

check('Ⓑ②ᵃ ⛭ ** OFF IS BYTE-IDENTICAL, BOTH WAYS OF BEING OFF: ** absent from the environment and '
      'set to the perturbation switch\'s zero, every array of both banks identical -- 6 in TT and '
      '11 in polarisation',
      SW['off_identical'] is True
      and all(SW['off_rows'][k][b]['arrays_identical'] for k in ('absent', 'zero')
              for b in ('tt', 'pol'))
      and SW['off_rows']['absent']['tt']['n_arrays'] == 6
      and SW['off_rows']['absent']['pol']['n_arrays'] == 11)

check('Ⓑ②ᵇ ⛭ ** AND ON-WITH-DEFAULTS IS BIT-IDENTICAL TO `origin/main`\'S OWN OUTPUT with the '
      'previous revision\'s switch live. **  ⇒ *so the letter set at its default is the landed '
      'repair itself and not an approximation of it*',
      SW['on_identical'] is True
      and all(SW['on_rows'][b]['arrays_identical'] for b in ('tt', 'pol')))

check('Ⓑ②ᶜ ⛭ and the five refusals all refuse, each naming the state it was given',
      len(SW['refusals']) == 5
      and all(v['refused'] and v['rc'] == 1 for v in SW['refusals'].values())
      and "NUCA=1 needs E in NUPARTS" in SW['refusals']['NUCA without E']['message']
      and "NUPARTS='WX'" in SW['refusals']['a bad letter']['message'],
      '%d refusal(s)' % len(SW['refusals']))

check('Ⓑ②ᵈ ⌗ and the whole set is reported as passing by its own runner, which is the arm that '
      'would have caught a leg generated before the keys existed',
      SW['all_pass'] is True)

# ══ Ⓒ ① THE DECOMPOSITION ═══════════════════════════════════════════════════════════════════════
# *The reproduction leg runs first at every reading and returns the fit of record's four headline
#  amplitudes, or nothing below is readable.*

check('Ⓒ①ᵃ ⛭ ** THE REPRODUCTION LEG REPRODUCED: ** the fit of record returns `1.15162`, '
      '`1.29592`, `1.01405` and `1.04630` on the landed bank, which is the arm of record this '
      'whole decomposition is measured against',
      RF['reproduced'] is True
      and abs(L['TT|0.30'] - 1.15162) < 5e-06 and abs(L['TT|0.60'] - 1.29592) < 5e-06
      and abs(L['EE|0.30'] - 1.01405) < 5e-06 and abs(L['EE|0.60'] - 1.04630) < 5e-06)

check('Ⓒ①ᵇ ⛭⛭ ** THE WEIGHT CHANGE ALONE CROSSES ONE: ** `A = 0.99510` at `0.30` eV, which is PAST '
      'one by `0.00490`, and `1.05621` at `0.60`.  ⇒ *so the overshoot is already there with the '
      'weight change alone, and it is not the continuity or the Euler change\'s doing -- which is '
      'the whole of what the order asked*',
      abs(fit('W', 'TT|0.30') - 0.99510) < 5e-06
      and abs(fit('W', 'TT|0.60') - 1.05621) < 5e-06
      and fit('W', 'TT|0.30') < 1.0
      and fit('W', 'TT|0.30', 'crosses_one') is True
      and abs((1.0 - fit('W', 'TT|0.30')) - 0.00490) < 5e-06,
      'crossing of %.5f' % (1.0 - fit('W', 'TT|0.30')))

check('Ⓒ①ᶜ ⛭ ** AND IT DOES NOT LEAVE EE IN BAND, which is the order\'s second question: ** '
      '`0.04005` from one at `0.30` eV, inside the `0.05` band, and `0.05961` at `0.60`, OUTSIDE '
      'it',
      abs(ee('W', '0.30') - 0.04005) < 5e-06 and abs(ee('W', '0.60') - 0.05961) < 5e-06
      and ee('W', '0.30') <= RF['bands']['EE'] < ee('W', '0.60'))

check('Ⓒ①ᵈ ⛭ and it is nonetheless very nearly the whole of the repair\'s magnitude: `0.9677` of '
      'the TT excess at `0.30` eV and `0.8101` at `0.60`.  ⇒ *the order\'s expectation was right '
      'about the SIZE of the change the closure deficit asks for, and wrong about it stopping '
      'short of one*',
      abs(fit('W', 'TT|0.30', 'frac_of_excess') - 0.9677) < 5e-05
      and abs(fit('W', 'TT|0.60', 'frac_of_excess') - 0.8101) < 5e-05)

check('Ⓒ①ᵉ ⌗ the continuity change alone is the smallest of the three -- `1.13111` and `1.26394`, '
      '`0.1353` and `0.1081` of the excess -- and leaves EE inside its band at both sums',
      abs(fit('C', 'TT|0.30') - 1.13111) < 5e-06
      and abs(fit('C', 'TT|0.60') - 1.26394) < 5e-06
      and abs(fit('C', 'TT|0.30', 'frac_of_excess') - 0.1353) < 5e-05
      and abs(fit('C', 'TT|0.60', 'frac_of_excess') - 0.1081) < 5e-05
      and max(ee('C', '0.30'), ee('C', '0.60')) <= RF['bands']['EE'])

check('Ⓒ①ᶠ ⌗ and the Euler change alone is the middle one -- `1.05464` and `1.13902`, `0.6396` and '
      '`0.5302` of the excess -- and it is the one that leaves EE closest to where it was, at '
      '`0.00060` and `0.02019`',
      abs(fit('E', 'TT|0.30') - 1.05464) < 5e-06
      and abs(fit('E', 'TT|0.60') - 1.13902) < 5e-06
      and abs(fit('E', 'TT|0.30', 'frac_of_excess') - 0.6396) < 5e-05
      and abs(fit('E', 'TT|0.60', 'frac_of_excess') - 0.5302) < 5e-05
      and abs(ee('E', '0.30') - 0.00060) < 5e-06
      and abs(ee('E', '0.60') - 0.02019) < 5e-06)

check('Ⓒ①ᵍ ⛭ ** AND NEITHER OF THOSE TWO CROSSES ONE AT EITHER SUM. **  ⇒ *that is the fact ①\'s '
      'verdict is read through: exactly ONE of the three members is the one the registered rows '
      'condemn*',
      not any(fit(x, 'TT|%s' % s, 'crosses_one') for x in ('C', 'E')
              for s in ('0.30', '0.60')))

# ══ Ⓓ ① THE REGISTERED ROWS, AND THE DEFECT IN THE REGISTRATION ═════════════════════════════════

check('Ⓓ①ᵃ ⛭⛭⛭ ** TWO REGISTERED ROWS FIRE AT ONCE AND BOTH ARE REPORTED: ** `Ⓒ` on the crossing '
      'and `Ⓓ` on EE leaving its band, with `Ⓐ` and `Ⓑ` not firing.  ** The registration did not '
      'make the rows exclusive -- that is a defect of this seat\'s own registration, and it is '
      'named here rather than resolved by a precedence invented at reading time. **',
      RF['verdict_1'] == 'C+D'
      and RF['verdict_1_rows'] == {'A': False, 'B': False, 'C': True, 'D': True},
      'verdict %s' % RF['verdict_1'])

check('Ⓓ①ᵇ ⛭ and the first version of the block DID resolve it by precedence, silently preferring '
      'the softer row, and the record says so in those terms -- `Ⓓ` is the row that reads REFUTED, '
      'so the `elif` chain was biased toward the gentler reading of this seat\'s own result',
      'TWO REGISTERED ROWS FIRE AT ONCE, AND THE REGISTRATION DID NOT MAKE THEM EXCLUSIVE'
      in RESULT
      and 'A precedence invented at reading time is a criterion moved after the result' in RESULT)

check('Ⓓ①ᶜ ⌗ and not one registered condition was touched: the bands are still the `0.03` and '
      '`0.05` the previous revision was judged on, and they are the numbers the registration '
      'carries',
      abs(RF['bands']['TT'] - 0.03) < 1e-12 and abs(RF['bands']['EE'] - 0.05) < 1e-12
      and 'The thresholds are the ones `r7876` was judged' in PRED)

# ══ Ⓔ ① THE ATTRIBUTION, REGISTERED AS A MEASUREMENT ════════════════════════════════════════════

check('Ⓔ①ᵃ ⛭ ** THE THREE CHANGES ARE NEARLY ADDITIVE IN `A`, AND THAT IS WHAT MAKES THE '
      'ATTRIBUTION READABLE AT ALL: ** the summed separate moves are `-0.274003` and `-0.428590` '
      'against the joint `-0.287610` and `-0.481260` -- ratios `0.9527` and `0.8906`',
      abs(AT['0.30']['summed'] + 0.274003) < 5e-06
      and abs(AT['0.60']['summed'] + 0.428590) < 5e-06
      and abs(AT['0.30']['all_three'] + 0.287610) < 5e-06
      and abs(AT['0.60']['all_three'] + 0.481260) < 5e-06
      and abs(AT['0.30']['ratio'] - 0.9527) < 5e-05
      and abs(AT['0.60']['ratio'] - 0.8906) < 5e-05)

check('Ⓔ①ᵇ ⛭ and it was registered IN ADVANCE as a measurement and not an assumption, with a value '
      'far from one declared beforehand to be a result about the coupling rather than an error.  '
      '⇒ *it came back near one, so the attribution may be read -- to `5` and `11` per cent and no '
      'better*',
      'Registered as a measurement and not as an assumption' in PRED
      and 'a value far from 1 is a result about the coupling, not an error' in PRED
      and 'to within `5 %` and `11 %`' in RESULT)

check('Ⓔ①ᶜ ⌗ and the joint move the ratio is taken against is the LANDED one, `c_s^2 = w` with all '
      'three changes -- `0.86401` and `0.81466` -- which is the number the registration fixed, not '
      'the exact sound speed\'s',
      abs(WCE['TT|0.30'] - 0.86401) < 5e-06 and abs(WCE['TT|0.60'] - 0.81466) < 5e-06
      and abs(AT['0.30']['all_three'] - (WCE['TT|0.30'] - L['TT|0.30'])) < 1e-09)

# ══ Ⓕ ② THE EXACT ADIABATIC SOUND SPEED, ALL THREE CHANGES LIVE ═════════════════════════════════

check('Ⓕ②ᵃ ⛭⛭ ** `Ⓖ` -- A BETTER MEMBER OF THE FAMILY, STILL NOT THE REPAIR: ** `A = 0.92115` and '
      '`0.90786` against `c_s^2 = w`\'s `0.86401` and `0.81466`, closer to one at BOTH sums and '
      'still outside the `0.03` band at both',
      RF['verdict_2'] == 'G'
      and abs(fit('A1', 'TT|0.30') - 0.92115) < 5e-06
      and abs(fit('A1', 'TT|0.60') - 0.90786) < 5e-06
      and abs(fit('A1', 'TT|0.30') - 1.0) < abs(WCE['TT|0.30'] - 1.0)
      and abs(fit('A1', 'TT|0.60') - 1.0) < abs(WCE['TT|0.60'] - 1.0)
      and min(abs(fit('A1', 'TT|%s' % s) - 1.0) for s in ('0.30', '0.60')) > RF['bands']['TT'])

check('Ⓕ②ᵇ ⛭ and the improvement as a fraction of the overshoot it inherits: `0.4202` at `0.30` eV '
      'and `0.5029` at `0.60`',
      abs((abs(WCE['TT|0.30'] - 1.0) - abs(fit('A1', 'TT|0.30') - 1.0))
          / abs(WCE['TT|0.30'] - 1.0) - 0.4202) < 5e-05
      and abs((abs(WCE['TT|0.60'] - 1.0) - abs(fit('A1', 'TT|0.60') - 1.0))
              / abs(WCE['TT|0.60'] - 1.0) - 0.5029) < 5e-05)

check('Ⓕ②ᶜ ⛭ ** AND IT MOVES EE BACK INSIDE ITS BAND AT THE SMALLER SUM: ** `0.04650` against the '
      '`0.05526` `c_s^2 = w` gave, and `0.07225` against `0.08880` at the larger, which is still '
      'outside.  ⇒ *the constraint `69` ruled binding is half satisfied, and half is not satisfied*',
      abs(ee('A1', '0.30') - 0.04650) < 5e-06
      and abs(ee('A1', '0.60') - 0.07225) < 5e-06
      and abs(abs(WCE['EE|0.30'] - 1.0) - 0.05526) < 5e-06
      and abs(abs(WCE['EE|0.60'] - 1.0) - 0.08880) < 5e-06
      and ee('A1', '0.30') <= RF['bands']['EE'] < ee('A1', '0.60'))

check('Ⓕ②ᵈ ⛭ ** AND NO LIMIT IS READ THROUGH ANY OF IT: ** the only registered row that licenses '
      'one is `Ⓔ`, no arm reached it, and the record says so',
      RF['verdict_2'] != 'E'
      and 'No limit is read through any switch unless Ⓔ' in PRED
      and 'No limit is read through it: that needs `Ⓔ`' in RESULT)

check('Ⓕ②ᵉ ⌗ and the sound speed carries no fitted quantity: `w` is the species\' own Fermi-Dirac '
      'spline and `w-dot` is that spline\'s own derivative, with `H` the conformal rate the '
      'equations already use',
      'No fitted quantity' in PRED
      and '_w_eg = NUW_of(np.log(ag))' in INST
      and 'Wdot_of = Wnu_of.derivative()' in INST)

# ══ Ⓕ ② WHICH CLOCK THE DERIVATIVE IS ON — MEASURED, NOT ARGUED ═════════════════════════════════
# *The guard: when two descriptions differ, first ask whether the difference survives a change of
#  clock.  Applied to this revision's OWN new term.  `c_a^2` is clock-free only when `w-dot` and
#  `H` share a clock, and in this instrument they do not automatically: `Wdot_of` is `d/d eta` on
#  the GRID while the right-hand side reads the LEAF rate under `LEAFPERT`.*

check('Ⓕ②ᶠ ⛭⛭ ** THE TERM THE CODE APPLIES IS `Jac * (dw/dln a)/(3(1+w))`, AND ON THE ARM EVERY '
      'LEG OF THIS REVISION RAN THE FACTOR IS EXACTLY ONE: ** `Jac` is `1.000000` to `1.000000` '
      'across the visibility on `lcdm`, with worst departure `0`.  ⇒ *so the clock cancels and not '
      'one number of this revision moves*',
      CK['lcdm']['worst_dev'] == 0.0
      and CK['lcdm']['jac_min'] == 1.0 and CK['lcdm']['jac_max'] == 1.0
      and CK['numbers_affected'] is False and CK['legs_were_run_on'] == 'lcdm')

check('Ⓕ②ᵍ ⛭⛭ ** AND THAT IS ESTABLISHED ON THE WHOLE INTEGRATION RANGE AND BIT FOR BIT, not on '
      'the visibility alone: ** the grid rate and the leaf rate are identical on all `40000` grid '
      'points, worst absolute difference exactly `0`.  ⇒ *which is what makes "unaffected" a '
      'measurement rather than an expectation*',
      CK['lcdm_full_grid']['bit_identical_everywhere'] is True
      and CK['lcdm_full_grid']['worst_abs_rate_difference'] == 0.0
      and CK['lcdm_full_grid']['n'] == 40000)

check('Ⓕ②ʰ ⛭ ** AND ON THE CR ARM IT IS NOT ONE: ** `Jac` runs `0.748581` to `0.959339`, so the '
      'correction term there departs from the clock-free form by up to `25.1` per cent -- which is '
      'the finding, and it is reported rather than silently patched',
      #: ⚠ *written as a flat conjunction on purpose: an `A and B if C else D` shape makes the
      #:   quote-pin instrument read one claim as a multi-key ALT group, and it reads badly besides.*
      abs(CK['cr']['jac_min'] - 0.748581) < 5e-07
      and abs(CK['cr']['jac_max'] - 0.959339) < 5e-07
      and abs(100 * CK['cr']['worst_dev'] - 25.1) < 0.05
      and CK['cr_full_grid']['bit_identical_everywhere'] is False,
      'worst %.4f' % CK['cr']['worst_dev'])

check('Ⓕ②ⁱ ⛭⛭⛭ ** AND THE TWO READINGS OF `LEAFPERT` AGREE ON THE DIVISOR, WHICH IS WHY THIS IS '
      'NOT A FORK: ** read as a correct Euler equation in the integration variable, every '
      'derivative is `d/d eta_grid` and the conversion takes the GRID rate; read as a sector on '
      'the leaf clock, `w-dot` becomes `w-dot/Jac` and `Jac * H_leaf == H_grid` identically, so it '
      'is the SAME expression.  ⇒ *the term divided by the leaf rate, which is neither, and that '
      'is a defect of this revision\'s own new code*',
      'Both readings divide by the grid rate. The term divided by the leaf rate, which is neither.'
      in RESULT
      and 'It is corrected to `Hc_of(e)` in both right-hand sides.' in RESULT
      and 'it collapsed under the arithmetic' in RESULT)

check('Ⓕ②ʲ ⛭ ** AND THE CORRECTION IS A BIT-LEVEL NO-OP ON EVERY BANK THIS REVISION HAS: ** the '
      'two rate splines are built from bit-identical ordinate arrays on an identical abscissa, so '
      'they are the same function, which is why no leg is regenerated and no number is restated',
      CK['lcdm_off_knot']['ordinates_bit_identical'] is True
      and CK['lcdm_off_knot']['bit_identical_off_knot'] is True
      and CK['lcdm_off_knot']['n'] == 200001
      and 'bit-identical ordinate arrays on an identical abscissa' in RESULT
      and 'bit-level no-op' in RESULT)

check('Ⓕ②ᵏ ⛭ ** AND THE PREVIOUS REVISION\'S LANDED EULER `w-dot` TERM IS NOT TOUCHED: ** it is '
      'already `d/d eta_grid`, which is the clock the ODE is integrated in, so it is correct under '
      'the reading the instrument\'s structure implies -- and the switch that moves the rate in '
      'that sector is `LEAFPERT`, which is ON by default here with `LEAFGEOM` off',
      'EULER TERM IS CORRECT AS IT STANDS' in RESULT
      and CK['lcdm']['leafpert'] is True and CK['lcdm']['leafgeom'] is False
      and INST.count('- (_wd / (1.0 + _w)) * tn)') == 2)

check('Ⓕ②ˡ ⛭ and the registration\'s own wording is where the defect hid, which is said in the '
      'record rather than smoothed: it asked for "the conformal rate the perturbation equations '
      'already use", and that is the leaf rate',
      'the conformal rate the perturbation equations already use' in PRED
      and 'the registration described loosely enough to hide its own error' in RESULT)

# ══ Ⓖ ③ THE TIGHTENING, MEASURED BOTH WAYS AND ROUTED ═══════════════════════════════════════════

check('Ⓖ③ᵃ ⛭ ** THE FIXED POINT: ** tightened, this tree still reduces to the BANKED blob '
      '`e5319ce49686` -- so the tightening does not break the class it tightens',
      TG['fixed_point'] is True
      and TG['blob'] == 'e5319ce4968602ca6d8de89fdc871e8f9b0a645e')

check('Ⓖ③ᵇ ⛭ ** AND THE FLOOR: ** without this revision\'s two names the tree does NOT reduce, so '
      'the extension is load-bearing and not decoration',
      TG['floor_without_r7878'] is False)

check('Ⓖ③ᶜ ⛭⛭ ** THE HOLE WAS MEASURED BOTH WAYS ON FOUR BINDINGS, NOT THE TWO THE ORDER NAMED -- '
      'and the fourth is the NEUTRINO MASS ITSELF. **  Each of the four PASSES before the '
      'tightening and goes RED after it, which is what makes the tightening a repair rather than a '
      'claim',
      sorted(k for k, v in TG['controls'].items()
             if v['passes_before'] and v['red_after'])
      == ["BVEL's default", "NUFD's default", "_NU_ON's default", 'the early MNU default']
      and all(v['good'] for v in TG['controls'].values()),
      '%d of %d control(s) pass-before-and-red-after'
      % (sum(1 for v in TG['controls'].values() if v['passes_before'] and v['red_after']),
         len(TG['controls'])))

check('Ⓖ③ᵈ ⌗ and this revision\'s own two names are red BOTH ways, which is the honest reading: '
      'they are new, so there is no "before" in which they passed',
      all(not TG['controls'][k]['passes_before'] and TG['controls'][k]['red_after']
          and TG['controls'][k]['this_revisions_own']
          for k in ("NUPARTS's default", "NUCA's default")))

check('Ⓖ③ᵉ ⌗ and the three landed controls stay red throughout -- a changed operand, a deleted '
      'line and a moved constant',
      len(TG['landed_controls']) == 3 and all(TG['landed_controls'].values())
      and TG['all_pass'] is True)

#: ⚠ *the routing is counted by MATCHING A HEADING SHAPE, not by quoting a sentence: a bare
#:   `'r7878'` is a weak pin -- it is four characters that occur all over the corpus -- and the
#:   ratchet is better served by replacing such a key than by adjudicating it.
_ROUTED = re.findall(r'^## .*`r7878`.*$', text('FOR_66_FROM_60.md', ROOT), re.M)
check('Ⓖ③ᶠ ⛭ ** AND NOTHING OF ANOTHER SEAT\'S IS EDITED: ** every patch of this revision is '
      'routed through `FOR_66_FROM_60.md` under its own heading, counted off the tree here rather '
      'than asserted',
      len(_ROUTED) >= 2 and all('r7878' in h for h in _ROUTED),
      '%d routed heading(s)' % len(_ROUTED))

# ══ Ⓗ ② THE SUBSET, AND THE ORDER IN WHICH IT WAS CHOSEN ════════════════════════════════════════
# *The registration required the subset to be named in the result before its `A` was quoted.  That
#  is an ordering claim about the record, so it is checked as one.*


def _git(*a):
    r = subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else None


_NAMING = _git('log', '--format=%H', '-1', '--',
               os.path.relpath(os.path.join(D, 'SUBSET_NAMED.md'), ROOT))
_LEGS = _git('log', '--format=%H', '-1', '--',
             os.path.relpath(os.path.join(D, 'parts', 'lcdm_S030CE_tt.npz'), ROOT))
_ORDER = (_NAMING and _LEGS
          and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor',
                              _NAMING, _LEGS], capture_output=True).returncode == 0)

check('Ⓗ②ᵃ ⛭ ** THE SUBSET IS `CE`, AND IT IS NAMED BY A RULE FIXED BY ①\'S VERDICT: ** exclusion '
      'of the one member the registered rows condemn.  ⇒ *the rule could have been written down '
      'before ① ran; all ① supplied was WHICH member to exclude*',
      '**The subset is `NUPARTS=CE`**' in NAMED
      and 'It is named by **exclusion**' in NAMED
      and 'S030CE 0.30 CE 1' in GEN and 'S060CE 0.60 CE 1' in GEN)

check('Ⓗ②ᵇ ⛭⛭ ** AND THE ORDERING IS A FACT ABOUT THE REPOSITORY, NOT A CLAIM: ** the commit that '
      'names the subset is an ANCESTOR of the commit that first carries a `CE` bank, so no '
      'amplitude of the subset existed when the choice was made',
      bool(_ORDER), 'naming %s, legs %s' % (str(_NAMING)[:9], str(_LEGS)[:9]))

check('Ⓗ②ᶜ ⛭ and the naming says out loud that it goes against this seat\'s expectation: the '
      'subset the rule names DROPS the only one of the three changes with a closure argument '
      'behind it, and keeps the two that have none',
      'one of the three with a closure argument behind it' in RESULT
      and 'drops it and keeps the two that have none' in RESULT
      and 'the subset that **drops the only change with a closure argument behind it**' in NAMED)

V2 = RF['verdict_2_arms']

check('Ⓗ②ᵈ ⛭⛭ ** THE SUBSET READS `Ⓗ` ON THE REGISTERED TEST: ** `A = 1.08759` and `1.18952`, '
      'against `c_s^2 = w`\'s `0.86401` and `0.81466`.  `Ⓖ` needs TT closer to one at BOTH sums; '
      'at `0.30` eV it is much closer and at `0.60` eV it is NOT, so `Ⓖ` does not fire and `Ⓗ` '
      'does',
      V2['CE']['verdict'] == 'H'
      and abs(V2['CE']['tt'][0] - 1.08759) < 5e-06
      and abs(V2['CE']['tt'][1] - 1.18952) < 5e-06
      and V2['CE']['closer'] == [True, False],
      'verdict %s, closer %s' % (V2['CE']['verdict'], V2['CE']['closer']))

check('Ⓗ②ᵉ ⛭ ** AND THE MARGIN THAT DECIDES IT IS `0.00418`, WHICH IS `2.26` PER CENT OF THE '
      'OVERSHOOT IT IS READ AGAINST -- a near thing, reported as near, with the threshold left '
      'exactly where the registration put it. **  ⌗ *What is NOT marginal is the rest of the row: '
      'TT stays `0.0876` and `0.1895` from one, nowhere near the `0.03` band*',
      abs((abs(V2['CE']['tt'][1] - 1.0) - abs(WCE['TT|0.60'] - 1.0)) - 0.00418) < 5e-06
      and abs(100 * (abs(V2['CE']['tt'][1] - 1.0) - abs(WCE['TT|0.60'] - 1.0))
              / abs(WCE['TT|0.60'] - 1.0) - 2.25) < 0.005
      and min(abs(x - 1.0) for x in V2['CE']['tt']) > RF['bands']['TT']
      and abs(RF['bands']['TT'] - 0.03) < 1e-12)

check('Ⓗ②ᶠ ⛭ ** AND THE ONE THING THE SUBSET DOES WELL IS THE CONSTRAINT `69` RULED BINDING: ** EE '
      'comes back to `0.00769` and `0.03424`, inside its band at both sums -- and at the larger '
      'sum that is closer to one than the ARM OF RECORD itself, `0.04630`.  ⇒ *the changes that '
      'keep EE agreeing are the ones that do not fix TT*',
      abs(V2['CE']['ee'][0] - 0.00769) < 5e-06
      and abs(V2['CE']['ee'][1] - 0.03424) < 5e-06
      and V2['CE']['ee_out_of_band'] is False
      and V2['CE']['ee'][1] < abs(L['EE|0.60'] - 1.0))

check('Ⓗ②ᵍ ⛭ ** AND ②\'s FOUR ROWS ARE MUTUALLY EXCLUSIVE, CHECKED RATHER THAN ASSUMED because '
      '①\'s were not: ** exactly ONE fires on each of ②\'s two registered arms -- `Ⓖ` on all '
      'three changes live, `Ⓗ` on the subset',
      sorted(V2) == ['A1', 'CE']
      and all(sum(1 for c in V2[k]['rows'].values() if c) == 1 for k in V2)
      and V2['A1']['verdict'] == 'G' and V2['CE']['verdict'] == 'H'
      and 'AND ②\'s FOUR ROWS *ARE* MUTUALLY EXCLUSIVE, UNLIKE ①\'s' in RESULT,
      '%s' % {k: V2[k]['verdict'] for k in sorted(V2)})

check('Ⓗ②ʰ ⛭ ** AND THE BASELINE IS DECLARED NOT LIKE-FOR-LIKE ON THE SUBSET: ** the registration '
      'fixed "closer to one than `c_s^2 = w` gave" against the LANDED ALL-THREE figures, and a '
      '`c_s^2 = w` leg of the subset was not run.  ⇒ *the registration chose the baseline before '
      'the result, so it stands, and the limit of what it measures is named rather than assumed '
      'away*',
      RF['verdict_2_baseline']['like_for_like_on_the_subset'] is False
      and abs(RF['verdict_2_baseline']['TT|0.30'] - WCE['TT|0.30']) < 1e-12
      and 'AND THE BASELINE IS DECLARED, BECAUSE IT IS NOT LIKE-FOR-LIKE HERE' in RESULT)

check('Ⓗ②ⁱ ⌗ and all ten banks of this revision record the SAME instrument blob -- the state the '
      'code was in when they ran, before the clock correction -- which is why the correction being '
      'a no-op on this arm is what licenses leaving them alone',
      'all ten record that same blob, which is the code that actually ran' in RESULT
      and CK['lcdm_off_knot']['ordinates_bit_identical'] is True)

# ══ Ⓘ AN UNREGISTERED READ, AND THE ARM THAT KEEPS IT HONEST ════════════════════════════════════
# *A read taken AFTER the verdicts were fixed is not a registered outcome, and the one thing a
#  receipt can do about that is refuse to let it pass as one.  So it is pinned AND its status is
#  pinned: the record must call it unregistered in those words, and nothing above may depend on it.*

check('Ⓘ⓵ᵃ ⛭⛭ ** THE REQUIRED LEVERAGE IS `10.791` AND `6.391`, AND THE TWO SETS DO NOT OVERLAP: ** '
      'the only arm whose leverage is right at both sums within a factor of `4/3` is the subset, '
      'at `0.933` and `1.381` of required, and it removes less than half the TT excess; the only '
      'arm that removes three quarters or more is the weight change, whose leverage is `0.268` and '
      '`0.354` of required.  ⇒ *no member of this family has both the right leverage and enough of '
      'the move*',
      abs(LV['required']['0.30']['leverage'] - 10.791) < 0.0005
      and abs(LV['required']['0.60']['leverage'] - 6.391) < 0.0005
      and LV['right_leverage'] == ['CE'] and LV['strong_enough'] == ['W']
      and LV['strong_but_wrong_leverage'] == ['W']
      and LV['one_statement'] is True
      and abs(LV['arms']['CE']['0.30']['of_required'] - 0.933) < 0.0005
      and abs(LV['arms']['CE']['0.60']['of_required'] - 1.381) < 0.0005
      and abs(LV['arms']['W']['0.30']['of_required'] - 0.268) < 0.0005
      and abs(LV['arms']['W']['0.60']['of_required'] - 0.354) < 0.0005)

check('Ⓘ⓵ᵇ ⛭⛭⛭ ** AND IT IS DECLARED UNREGISTERED IN THE RECORD, IN THOSE WORDS, AND NOTHING '
      'REGISTERED DEPENDS ON IT: ** the registration carries no leverage criterion at all, and the '
      'read was computed after ①\'s and ②\'s verdicts were fixed.  ⌗ *This arm exists so that a '
      'post-hoc read cannot quietly become a result -- which is the failure mode the whole '
      'register-before-measure discipline is against*',
      LV['declared'].startswith('UNREGISTERED')
      and 'AN UNREGISTERED READ, DECLARED' in RESULT
      and 'offered as the next question rather than as a finding of this revision' in RESULT
      and 'leverage' not in PRED.lower()
      and 'AND IT IS NOT A LICENCE TO GO LOOKING FOR A STRONGER `CE`' in RESULT)

check('Ⓘ⓵ᶜ ⌗ and the table is read off the SAME fits the verdicts are read off -- no second fit and '
      'no re-run: every number in it comes from `refit_parts.json`, which is the file ①\'s and ②\'s '
      'rows were decided on',
      all(abs(LV['arms'][k][s]['frac_of_excess']
              - A[k]['fits']['TT|%s' % s]['frac_of_excess']) < 1e-12
          for k in LV['arms'] for s in ('0.30', '0.60')))

print('=' * 100)
print('  %d arm(s), %d failed' % (NARMS, len(FAILS)))
for f in FAILS:
    print('   FAILED: %s' % f)
sys.exit(1 if FAILS else 0)
