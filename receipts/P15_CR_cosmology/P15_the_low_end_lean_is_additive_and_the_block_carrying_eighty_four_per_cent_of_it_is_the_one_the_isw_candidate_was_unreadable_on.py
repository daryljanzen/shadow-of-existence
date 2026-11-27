# -*- coding: utf-8 -*-
"""⛭⛭⛭ THE LOW-END LEAN IS ADDITIVE, AND THE BLOCK CARRYING EIGHTY-FOUR PER CENT OF IT IS THE ONE
THE LATE-ISW CANDIDATE WAS UNREADABLE ON — DECOMPOSED ON CROSSINGS, NOT ON A DIFFERENCE MAP.

COMPUTES: nothing physical. It reads the record `r7892` produced by removing one polarisation block
at a time from `r7866`'s thirty-six lowest bandpowers and re-reading the CROSSING each time — the
quantity the limit is made of — after `r7890` established that a difference map cannot name this
move, its own artefact there being seven times the signal. It checks the teeth of that reading.
** IT PINS AS RESULTS: ** removing `TT`'s twelve moves the crossing `68.1331 -> 108.8034`, a move of
`+40.6703`; `TE`'s twelve `+7.9668`; `EE`'s twelve `+2.6853`. The three sum to `+51.3224` against
the whole `+48.2020`, a residual of `3.1205` meV or `6.5` per cent, so BOTH registered outcomes fire
-- `Ⓚ⓵` ADDITIVE, inside its ten-per-cent bar, and `Ⓚ⓶` CONCENTRATED, `TT` alone carrying `84.4`
per cent over its eighty-per-cent bar. Both are reported because the registration said they are not
exclusive.
⛔ ** AND IT PINS THAT BOTH REGISTERED EXPECTATIONS ARE REFUTED: ** `Ⓚ⓷` non-additive is refuted,
and the weak expectation that `EE` would dominate is refuted -- it is `TT`, five times `TE` and
fifteen times `EE`. The registration said in advance a refutation here was the better outcome.
⛔ ** AND IT PINS THAT THE REGISTERED CONTROL FIRED AND WAS RIGHT: ** `PREDICTION.md` named
`-20.09` meV, which is `r7866`'s PARAMETERS-HELD row, while this profiler re-profiles the four at
every sum and so computes `r7866`'s other row, `-48.20`. The error was in the registration. The
repair is read out of `r7866`'s own record rather than typed, and checks BOTH crossings rather than
only their difference -- stricter than the registration asked for, not looser.
⛔ ** AND ONE THING MEASURED AFTER THE OUTCOME, FLAGGED AS NOT REGISTERED: ** twelve of the `13` TT
bins `r7866` recorded the late ISW as UNREADABLE on are exactly the twelve `TT` bins dropped here.
That cannot confirm the candidate -- it is unreadable on precisely those bins -- but it removes
"unreadable" as a reason to set it aside.
⛔ ** AND WHAT IS NOT TOUCHED: ** this decomposes the RE-PROFILED move. The parameters-held `-20.09`
move is a separate question and remains undecomposed. No limit is read.

    python3 <this file>
"""
import ast
import glob
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
R7892 = glob.glob(os.path.join(BW, 'r7892_60_*'))[0]
R7866 = glob.glob(os.path.join(BW, 'r7866_60_*'))[0]

BLOCKS = ('TT', 'TE', 'EE')
CARRY = ('R7866_WHOLE', 'R7866_MINUS36', 'R7866_MOVE', 'R7866_FROZEN_MOVE')
FAILS = []
NARMS = 0


def check(name, ok, got=None):
    global NARMS
    NARMS += 1
    if ok:
        print('  [PASS] %s' % name + ('   (%s)' % got if got is not None else ''))
    else:
        FAILS.append(name)
        print('  [FAIL] %s' % name + ('   (got %s)' % got if got is not None else ''))


D = json.load(io.open(os.path.join(R7892, 'by_block.json'), encoding='utf-8'))
SB = json.load(io.open(os.path.join(R7866, 'same_bins.json'), encoding='utf-8'))
SRC = io.open(os.path.join(R7892, 'by_block.py'), encoding='utf-8').read()
PRED = ' '.join(io.open(os.path.join(R7892, 'PREDICTION.md'), encoding='utf-8')
                .read().replace('*', '').replace('`', '').split())
RES = ' '.join(io.open(os.path.join(R7892, 'RESULT.md'), encoding='utf-8')
               .read().replace('*', '').replace('`', '').split())
TREE = ast.parse(SRC)

print(__doc__)
print('=' * 100)

# ---------------------------------------------------------------------------------------------- Ⓐ
print('\nⒶ  IT IS r7866\'S OWN INSTRUMENT AND r7866\'S OWN MASK, NOT A REBUILD')

_defines = {n.name for n in ast.walk(TREE) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
_forbidden = sorted(d for d in _defines if d in ('inst_profile', 'cross_of', 'the_thirty_six'))
check('Ⓐ① the revision defines no profiler, no crossing solver and no mask of its own: it imports '
      '`r7866`\'s module whole, so what varies between the arms is the MASK and nothing else. '
      '⌗ *Read on the parse tree, because a source-text search for these names matches the very '
      'line that forbids them*',
      not _forbidden and any(isinstance(n, ast.Import)
                             and any(a.name == 'same_bins' and a.asname == 'SB' for a in n.names)
                             for n in ast.walk(TREE)),
      'imports same_bins as SB; redefines %s' % (_forbidden or 'nothing'))

check('Ⓐ② and the whole-instrument crossing it starts from is `r7866`\'s banked whole-mask crossing '
      'to all digits, so the decomposition hangs off that revision\'s record and not off a re-run '
      'that merely lands nearby',
      abs(D['base_crossing_meV'] - SB['instrument_whole']['crossing_meV']) < 1e-09
      and abs(D['base_crossing_meV'] - 68.1331) < 5e-05,
      'base %.4f meV' % D['base_crossing_meV'])

check('Ⓐ③ and the all-three mask drops exactly twelve bandpowers from each of the three blocks, '
      'thirty-six in all, which is the population `r7866` named',
      all(D['per_block_dropped'][b] == 12 for b in BLOCKS)
      and sum(D['per_block_dropped'].values()) == 36,
      '%s, %d in all' % (D['per_block_dropped'], sum(D['per_block_dropped'].values())))

# ---------------------------------------------------------------------------------------------- Ⓑ
print('\nⒷ  THE CONTROL FIRED, AND THE REPAIR IS A TIGHTENING RATHER THAN A LOOSENING')

_assigns = {t.id: n.value for n in ast.walk(TREE) if isinstance(n, ast.Assign)
            for t in n.targets if isinstance(t, ast.Name) and t.id in CARRY}
_from_record, _typed = [], []
for _k in CARRY:
    _v = _assigns.get(_k)
    if _v is None:
        _typed.append('%s absent' % _k)
        continue
    _names = {x.id for x in ast.walk(_v) if isinstance(x, ast.Name)}
    _consts = [x.value for x in ast.walk(_v)
               if isinstance(x, ast.Constant) and isinstance(x.value, float)]
    (_from_record if ('_SB' in _names and not _consts) else _typed).append(_k)

check('Ⓑ① every one of the four carried targets is read out of `r7866`\'s own banked record and not '
      'one of them is a float typed into this revision -- which is the whole of the repair, because '
      'the control fired precisely by naming a row from memory. ⌗ *Read on the parse tree: a target '
      'assigned from a literal would pass any source-text search for the record\'s filename*',
      len(_from_record) == len(CARRY) and not _typed,
      'from the record: %s; typed: %s' % (_from_record, _typed or 'none'))

_PRAW = io.open(os.path.join(R7892, 'PREDICTION.md'), encoding='utf-8').read()
_cl = [l for l in _PRAW.splitlines() if 'control' in l.lower()]
_cnums = [float(x) for x in re.findall(r'\d+\.\d+', ' '.join(_cl))]
_anums = [float(x) for x in re.findall(r'\d+\.\d+', _PRAW)]
_named_held = any(abs(v - abs(D['r7866_frozen_move_banked'])) < 5e-03 for v in _cnums)
_named_prof = any(abs(v - abs(D['move_all36_meV'])) < 5e-03 for v in _cnums)
_had_prof = any(abs(v - abs(D['move_all36_meV'])) < 5e-03 for v in _anums)
check('Ⓑ② the registration demonstrably named the WRONG row, read as a NUMBER out of '
      '`PREDICTION.md` rather than as a phrase: across the lines that DESIGNATE the control, the '
      'parameters-held magnitude appears and the re-profiled magnitude does not. ⌗ *This is what makes the '
      'control a fired control rather than a quietly re-specified one*',
      _named_held and not _named_prof and bool(_cl),
      '%d control line(s): held named %s, re-profiled named %s'
      % (len(_cl), _named_held, _named_prof))

check('Ⓑ②ᵃ and the registration was not short of the right figure -- the re-profiled magnitude appears '
      'ELSEWHERE in the same `PREDICTION.md`, just not in the lines that designate the control. '
      '⇒ *So this was not missing information: it was a misreading of which row the profiler '
      'computes, with both rows on the page*',
      _had_prof,
      're-profiled magnitude present in the registration: %s' % _had_prof)

check('Ⓑ③ and the measured all-three move reproduces `r7866`\'s RE-PROFILED row to all digits, in '
      'magnitude, the two revisions signing it oppositely by stated convention',
      abs(abs(D['move_all36_meV']) - abs(SB['moves_meV']['instrument'])) < 1e-09
      and abs(D['move_all36_meV'] - 48.2020) < 5e-05,
      'move %+.4f against banked %+.4f' % (D['move_all36_meV'], SB['moves_meV']['instrument']))

check('Ⓑ④ and the row the registration WRONGLY named is a real and different row of the same '
      'record, so the control was mis-specified rather than vacuous -- the two differ by more than '
      'a factor of two',
      abs(D['r7866_frozen_move_banked'] - (-20.0868)) < 5e-05
      and abs(abs(D['move_all36_meV']) / abs(D['r7866_frozen_move_banked'])) > 2.0,
      'held %+.4f vs re-profiled %+.4f' % (D['r7866_frozen_move_banked'], D['move_all36_meV']))

check('Ⓑ⑤ and BOTH crossings are carried, not only their difference, so a pair of errors cancelling '
      'in the difference could not pass this control',
      abs(D['all36_crossing_meV'] - SB['instrument_minus36']['crossing_meV']) < 1e-09
      and abs(D['all36_crossing_meV'] - 116.3351) < 5e-05,
      'minus36 %.4f meV' % D['all36_crossing_meV'])

# ---------------------------------------------------------------------------------------------- Ⓒ
print('\nⒸ  THE THREE SINGLE-BLOCK CROSSINGS AND THE MOVES THEY CARRY')

_c, _m, _s = D['block_crossings_meV'], D['block_moves_meV'], D['block_shares']
check('Ⓒ① the three single-block crossings are pinned one figure at a time, within half the last '
      'printed digit',
      abs(_c['TT'] - 108.8034) < 5e-05 and abs(_c['TE'] - 76.0999) < 5e-05
      and abs(_c['EE'] - 70.8184) < 5e-05,
      'TT %.4f | TE %.4f | EE %.4f' % (_c['TT'], _c['TE'], _c['EE']))

check('Ⓒ② and so are the three moves they carry',
      abs(_m['TT'] - 40.6703) < 5e-05 and abs(_m['TE'] - 7.9668) < 5e-05
      and abs(_m['EE'] - 2.6853) < 5e-05,
      'TT %+.4f | TE %+.4f | EE %+.4f' % (_m['TT'], _m['TE'], _m['EE']))

check('Ⓒ③ and the three shares of the whole move',
      abs(_s['TT'] - 0.8437) < 5e-05 and abs(_s['TE'] - 0.1653) < 5e-05
      and abs(_s['EE'] - 0.0557) < 5e-05,
      'TT %.4f | TE %.4f | EE %.4f' % (_s['TT'], _s['TE'], _s['EE']))

check('Ⓒ④ and each single-block move is itself a crossing DIFFERENCE against the same whole-mask '
      'crossing, so the three are commensurable with each other and with the whole',
      all(abs((_c[b] - D['base_crossing_meV']) - _m[b]) < 1e-09 for b in BLOCKS),
      'all three reconstruct from their own crossings')

check('Ⓒ⑤ and every single-block move is POSITIVE -- removing low bandpowers raises the crossing in '
      'each block separately, so no block is pulling the other way and the shares are not a '
      'cancellation dressed as a decomposition',
      all(_m[b] > 0.0 for b in BLOCKS) and D['move_all36_meV'] > 0.0,
      'signs %s' % {b: ('+' if _m[b] > 0 else '-') for b in BLOCKS})

# ---------------------------------------------------------------------------------------------- Ⓓ
print('\nⒹ  BOTH REGISTERED OUTCOMES FIRE, AND BOTH REGISTERED EXPECTATIONS ARE REFUTED')

check('Ⓓ① the three single-block moves sum to `+51.3224` against the whole `+48.2020`, a residual '
      'of `3.1205` meV',
      abs(D['sum_of_blocks_meV'] - 51.3224) < 5e-05
      and abs(D['residual_meV'] - 3.1205) < 5e-05,
      'sum %+.4f, residual %+.4f meV' % (D['sum_of_blocks_meV'], D['residual_meV']))

check('Ⓓ② which is `6.5` per cent of the whole move, inside `Ⓚ⓵`\'s ten-per-cent bar, so the '
      'blocks act independently -- and the departure from independence is SUPER-additive, the parts '
      'summing to slightly more than the whole rather than less',
      abs(D['residual_fraction'] - 0.0647) < 5e-05 and D['residual_fraction'] < 0.10
      and D['additive'] and D['sum_of_blocks_meV'] > D['move_all36_meV'],
      'residual %.2f per cent, additive %s, super-additive' % (100 * D['residual_fraction'],
                                                               D['additive']))

check('Ⓓ③ and `TT` alone carries `84.4` per cent, over `Ⓚ⓶`\'s eighty-per-cent bar, so the second '
      'registered outcome fires as well and the record reports BOTH rather than choosing',
      D['concentrated'] and D['largest_block'] == 'TT' and _s['TT'] >= 0.80
      and len(D['states']) == len(('additive', 'concentrated')),
      '%s, largest %s' % ([s.split(' --')[0] for s in D['states']], D['largest_block']))

check('Ⓓ④ and the registered expectation `Ⓚ⓷` non-additive is recorded REFUTED, together with the '
      'weak expectation that `EE` would dominate -- which the registration named in advance as the '
      'better outcome, since it hands the next step a named block',
      D['expectation_K3_met'] is False and D['weak_expectation_EE'] is False
      and len(set(re.findall('Ⓚ([⓵-⓷])', PRED))) == len(D['states']) + 1,
      'Ⓚ⓷ %s, weak EE %s' % (D['expectation_K3_met'], D['weak_expectation_EE']))

check('Ⓓ⑤ and the carrying block beats the next by a wide margin rather than by a hair, so '
      '"concentrated" is not a verdict resting on the third digit',
      _m['TT'] / _m['TE'] > 4.0 and _m['TT'] / _m['EE'] > 12.0,
      'TT/TE %.2f, TT/EE %.2f' % (_m['TT'] / _m['TE'], _m['TT'] / _m['EE']))

# ---------------------------------------------------------------------------------------------- Ⓔ
print('\nⒺ  THE OVERLAP WITH r7866\'S UNREADABLE CANDIDATE — FLAGGED NOT REGISTERED')

check('Ⓔ① the sub-peak criterion and its multipole are `r7866`\'s own, and the recount reproduces '
      'the count that revision\'s record carries, so the comparison is against its finding and not '
      'against a re-derived set',
      D['first_peak'] == 220 and D['subpeak_tt_bins'] == D['r7866_subpeak_record'] == 13,
      'BIN_HI < %d gives %d, record %d' % (D['first_peak'], D['subpeak_tt_bins'],
                                           D['r7866_subpeak_record']))

check('Ⓔ② twelve of those thirteen are exactly the twelve `TT` bins this revision drops, with none '
      'of the dropped twelve lying outside the set and one sub-peak bin left standing',
      D['subpeak_and_dropped'] == D['carrying_block_dropped'] == 12
      and D['dropped_outside_subpeak'] == 0 and D['subpeak_kept'] == 1,
      '%d in both, %d kept, %d outside' % (D['subpeak_and_dropped'], D['subpeak_kept'],
                                           D['dropped_outside_subpeak']))

check('Ⓔ③ and the record BANKS this as unregistered rather than presenting it as a test that '
      'passed. ⌗ *It was measured after the outcome was read; the registration said nothing about '
      'it, and a post-hoc overlap that is allowed to pose as a prediction is the failure mode this '
      'flag exists to prevent*',
      D['overlap_registered'] is False,
      'overlap_registered %s' % D['overlap_registered'])

check('Ⓔ④ and the clause the comparison reasons FROM is asserted rather than assumed: the sub-peak '
      'set is `TT`\'s by construction, so a re-measure that moved the lean to another block must '
      'fire a gate instead of silently comparing two different blocks',
      any(isinstance(n, ast.Compare)
          and any(isinstance(c, ast.Constant) and c.value == 'TT' for c in n.comparators)
          and isinstance(n.left, ast.Subscript)
          and getattr(n.left.value, 'id', None) == 'NAMES' for n in ast.walk(TREE)),
      'the carrying-block clause is gated, read on the parse tree')

# ---------------------------------------------------------------------------------------------- Ⓕ
print('\nⒻ  THE RECORD SAYS WHAT THIS ESTABLISHES AND WHAT IT DOES NOT')

check('Ⓕ① the record states the arithmetic of the decomposition and the bar it clears',
      'The three single-block moves sum to +51.3224 against the whole +48.2020: a residual of '
      '3.1205 meV, 6.5 per cent of the whole move, inside Ⓚ⓵\'s ten-per-cent bar' in RES)

check('Ⓕ② and that both outcomes are reported because the registration forbade choosing once the '
      'numbers were seen',
      'Ⓚ⓵ additive and Ⓚ⓶ concentrated both fire, and both are reported, '
      'because the registration said they are not exclusive and that choosing between them once '
      'the numbers are seen is exactly what was excluded' in RES)

check('Ⓕ③ and that the weak expectation is refuted, naming the margin',
      'The weak expectation that EE would dominate is REFUTED: it is TT, by a factor of five over '
      'TE and fifteen over EE' in RES)

check('Ⓕ④ and that the control fired because the registration named the wrong row, saying which '
      'row and why this profiler computes the other',
      'The control fired because the registration named the wrong row: −20.09 is r7866\'s '
      'parameters-held move, while this profiler re-profiles the four parameters at every sum and '
      'therefore computes r7866\'s other row, −48.20' in RES)

check('Ⓕ⑤ and that the repair tightens rather than loosens, checking both crossings',
      'it now checks both crossings (68.1331 and 116.3351) and not only their difference, which is '
      'stricter than the registration asked for' in RES)

check('Ⓕ⑥ and that what is decomposed is the RE-PROFILED move, the parameters-held move being left '
      'untouched and named as still open',
      'What this therefore decomposes is the re-profiled move. It says nothing about the '
      'parameters-held −20.09 move, which is a separate question and remains undecomposed'
      in RES)

check('Ⓕ⑦ and that the overlap with the unreadable candidate is stated as an overlap',
      'Twelve of those thirteen are exactly the twelve TT bins this revision drops. None of the '
      'dropped twelve lies outside the set' in RES)

check('Ⓕ⑧ and that a block is not a mechanism -- the record declines to claim it has named one',
      'A block is not a mechanism. This names where the move lives and rules out the difference '
      'map as the way to read it; it does not say what in TT\'s twelve lowest bandpowers does the '
      'work' in RES)

check('Ⓕ⑨ and that the registration carried both rows, so the mis-specification was a misreading '
      'rather than a gap in what was available',
      'And the registration was not short of the right figure. −48.20 appears in PREDICTION.md itself, just not in the lines that designate the control' in RES)

print('\n' + '=' * 100)
print('  %d arm(s); %d failed' % (NARMS, len(FAILS)))
for f in FAILS:
    print('    FAILED: %s' % f)
print('=' * 100)
sys.exit(1 if FAILS else 0)
