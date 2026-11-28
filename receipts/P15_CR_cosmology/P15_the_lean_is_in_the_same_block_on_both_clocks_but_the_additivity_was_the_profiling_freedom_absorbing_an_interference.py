# -*- coding: utf-8 -*-
"""⛭⛭⛭ THE LEAN IS IN THE SAME BLOCK ON BOTH CLOCKS, BUT THE ADDITIVITY WAS THE PROFILING FREEDOM
ABSORBING A CROSS-BLOCK INTERFERENCE — SO THE LOCATION IS CONTENT AND THE CLEAN DECOMPOSITION WAS NOT.

COMPUTES: nothing physical. It reads the record `r7894` produced by re-running `r7892`'s block
decomposition on the OTHER clock — the four parameters HELD at the zero-sum fit, which is the
reference's own treatment — and it checks the teeth of that reading.
** IT PINS AS RESULTS: ** on the held clock the whole mask crosses at `57.0775` meV and minus all
thirty-six at `77.1644`, a move of `+20.0868`; minus `TT`'s twelve gives `78.4487`, a move of
`+21.3711`, which is `106.4` per cent of the whole move -- `TT` ALONE MOVES THE CROSSING FURTHER
THAN ALL THIRTY-SIX TOGETHER. `TE` gives `+3.4048` and `EE` `+0.2703`. The three sum to `+25.0463`
against `+20.0868`, a residual of `4.9594` meV or `24.7` per cent, well over the ten-per-cent bar.
⛔ ** SO THE REGISTERED OUTCOME IS `Ⓦ⓷`, NOT ADDITIVE, AND THE REGISTERED EXPECTATION `Ⓦ⓵` IS
REFUTED. ** The registration fixed in advance that `Ⓦ⓷` is not exclusive with a dominance reading
and is the stronger one where both fire, so `TT`'s dominance is reported beside it and the shares
below the leading block are not offered as shares.
⛔ ** AND IT PINS THE ANSWER TO THE QUESTION THE REVISION ASKED: ** `TT` dominates on BOTH clocks,
`84.4` per cent re-profiled against `106.4` per cent held, so by the standing `r7138` guard the
LOCATION survives the change of clock and is content. What does NOT survive is the ADDITIVITY: the
residual goes `6.5` to `24.7` per cent. ⇒ *The four parameters, when free, were absorbing a
cross-block interference, and `r7892`'s clean decomposition was clean because of it.*
⛔ ** AND IT PINS THE CONTROL, WHICH IS READ OUT OF THE RECORD: ** both banked frozen crossings, the
banked move, and the HELD PARAMETER VECTOR itself all come from `r7866`'s `same_bins.json`, and a
fresh zero-sum fit reproduces that vector with a maximum deviation of EXACTLY zero.
⛔ ** AND WHAT IS NOT TOUCHED: ** no mechanism is named, the `12`-of-`13` ISW overlap stays
unregistered where `r7892` banked it, no limit is read, and the interference is measured on the held
clock only.

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
R7894 = glob.glob(os.path.join(BW, 'r7894_60_*'))[0]
R7892 = glob.glob(os.path.join(BW, 'r7892_60_*'))[0]
R7866 = glob.glob(os.path.join(BW, 'r7866_60_*'))[0]

BLOCKS = ('TT', 'TE', 'EE')
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


D = json.load(io.open(os.path.join(R7894, 'held_by_block.json'), encoding='utf-8'))
BB = json.load(io.open(os.path.join(R7892, 'by_block.json'), encoding='utf-8'))
SBJ = json.load(io.open(os.path.join(R7866, 'same_bins.json'), encoding='utf-8'))
SRC = io.open(os.path.join(R7894, 'held_by_block.py'), encoding='utf-8').read()
TREE = ast.parse(SRC)
PRED = ' '.join(io.open(os.path.join(R7894, 'PREDICTION.md'), encoding='utf-8')
                .read().replace('*', '').replace('`', '').split())
RES = ' '.join(io.open(os.path.join(R7894, 'RESULT.md'), encoding='utf-8')
               .read().replace('*', '').replace('`', '').split())

print(__doc__)
print('=' * 100)

# ---------------------------------------------------------------------------------------------- Ⓐ
print('\nⒶ  IT IS THE OTHER CLOCK OF THE SAME INSTRUMENT, HELD AT THE RECORD\'S OWN VECTOR')

_defs = {n.name for n in ast.walk(TREE) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
_forbidden = sorted(d for d in _defs if d in ('fit_x4', 'cross_of', 'the_thirty_six', 'chi2_cmb'))
_calls = [n.func.attr for n in ast.walk(TREE)
          if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)]
_n_chi2 = _calls.count('chi2_cmb')
_n_fit = _calls.count('fit_x4')
check('Ⓐ① the revision defines no fitter, no crossing solver and no mask of its own — it imports '
      '`r7866`\'s module whole — and the one thing it DOES define is a held evaluator, which is the '
      'single substitution this revision is, and it FITS EXACTLY ONCE — the zero-sum fit the '
      'control needs — so no fitting happens inside the scan. ⌗ *Read on the parse tree, because a source-text '
      'search for these names matches the very line that forbids them*',
      not _forbidden
      and any(isinstance(n, ast.Import)
              and any(a.name == 'same_bins' and a.asname == 'SB' for a in n.names)
              for n in ast.walk(TREE))
      and _n_chi2 >= 1 and _n_fit == 1,
      'imports same_bins as SB; %d chi2 call(s), %d fit call(s); redefines %s'
      % (_n_chi2, _n_fit, _forbidden or 'nothing'))

_held = [n.value for n in ast.walk(TREE) if isinstance(n, ast.Assign)
         for t in n.targets if isinstance(t, ast.Name) and t.id == 'HELD_X4']
_from_record = bool(_held) and all(
    '_SB' in {x.id for x in ast.walk(v) if isinstance(x, ast.Name)}
    and not [x for x in ast.walk(v) if isinstance(x, ast.Constant) and isinstance(x.value, float)]
    for v in _held)
check('Ⓐ② and the HELD PARAMETER VECTOR is read out of `r7866`\'s banked record rather than typed '
      'or re-fitted into place, with no float literal anywhere in its assignment — which is what '
      'makes the two clocks the SAME instrument held two ways instead of two instruments',
      _from_record and len(D['held_x4']) == len(SBJ['instrument_frozen_whole']['x4'])
      and all(abs(a - float(b)) < 1e-12
              for a, b in zip(D['held_x4'], SBJ['instrument_frozen_whole']['x4'])),
      'from the record: %s, %d parameter(s)' % (_from_record, len(D['held_x4'])))

check('Ⓐ③ and a fresh zero-sum fit on the whole mask reproduces that banked vector to EXACTLY zero '
      'deviation, so the record is the fit and not a stale copy of one. ⌗ *The record supplies the '
      'number so it cannot be misremembered; the fit proves the number is still the fit*',
      D['x4_max_deviation'] == 0.0
      and all(a == b for a, b in zip(D['held_x4'], D['x4_refit'])),
      'max deviation %.3e' % D['x4_max_deviation'])

check('Ⓐ④ and the mask is the population `r7866` named: twelve dropped from each of the three '
      'blocks, the total derived from the per-block counts rather than asserted as a figure',
      all(D['per_block_dropped'][b] == 12 for b in BLOCKS)
      and sum(D['per_block_dropped'].values())
      == len(BLOCKS) * D['per_block_dropped'][BLOCKS[0]],
      '%s, %d in all' % (D['per_block_dropped'], sum(D['per_block_dropped'].values())))

# ---------------------------------------------------------------------------------------------- Ⓑ
print('\nⒷ  THE CONTROL REPRODUCES r7866\'s BANKED FROZEN ROW, BOTH CROSSINGS')

check('Ⓑ① the whole-mask held crossing reproduces the banked frozen row to all digits',
      abs(D['base_crossing_meV'] - float(SBJ['instrument_frozen_whole']['crossing_meV'])) < 1e-09
      and abs(D['base_crossing_meV'] - 57.0775) < 5e-05,
      '%.4f meV' % D['base_crossing_meV'])

check('Ⓑ② and so does the minus-thirty-six held crossing, so BOTH are checked and not only their '
      'difference — a pair of errors cancelling in the difference could not pass this control',
      abs(D['all36_crossing_meV'] - float(SBJ['instrument_frozen_minus36']['crossing_meV'])) < 1e-09
      and abs(D['all36_crossing_meV'] - 77.1644) < 5e-05,
      '%.4f meV' % D['all36_crossing_meV'])

check('Ⓑ③ and the move reproduces the banked frozen move in magnitude, the two revisions signing '
      'it oppositely by a convention this revision states rather than leaves to be noticed',
      abs(abs(D['move_all36_meV']) - abs(float(SBJ['moves_meV']['instrument_frozen']))) < 1e-09
      and abs(D['move_all36_meV'] - 20.0868) < 5e-05 and D['move_all36_meV'] > 0.0
      and float(SBJ['moves_meV']['instrument_frozen']) < 0.0,
      '%+.4f here against %+.4f banked' % (D['move_all36_meV'],
                                           float(SBJ['moves_meV']['instrument_frozen'])))

check('Ⓑ④ and this is demonstrably the OTHER clock and not the column `r7892` decomposed: the held '
      'move is smaller than the re-profiled move by a factor over two on identical bins',
      abs(float(BB['move_all36_meV'])) / abs(D['move_all36_meV']) > 2.0
      and abs(abs(float(BB['move_all36_meV'])) - 48.2020) < 5e-05,
      'held %+.4f against re-profiled %+.4f' % (D['move_all36_meV'],
                                                float(BB['move_all36_meV'])))

# ---------------------------------------------------------------------------------------------- Ⓒ
print('\nⒸ  THE THREE SINGLE-BLOCK HELD CROSSINGS AND MOVES, ONE FIGURE AT A TIME')

_c, _m, _s = D['block_crossings_meV'], D['block_moves_meV'], D['block_shares']
check('Ⓒ① the three held crossings are pinned one figure at a time, within half the last printed '
      'digit',
      abs(_c['TT'] - 78.4487) < 5e-05 and abs(_c['TE'] - 60.4823) < 5e-05
      and abs(_c['EE'] - 57.3479) < 5e-05,
      'TT %.4f | TE %.4f | EE %.4f' % (_c['TT'], _c['TE'], _c['EE']))

check('Ⓒ② and so are the three moves they carry',
      abs(_m['TT'] - 21.3711) < 5e-05 and abs(_m['TE'] - 3.4048) < 5e-05
      and abs(_m['EE'] - 0.2703) < 5e-05,
      'TT %+.4f | TE %+.4f | EE %+.4f' % (_m['TT'], _m['TE'], _m['EE']))

check('Ⓒ③ and the three shares, with `TT`\'s over one hundred per cent',
      abs(100 * _s['TT'] - 106.4) < 0.05 and abs(100 * _s['TE'] - 17.0) < 0.05
      and abs(100 * _s['EE'] - 1.3) < 0.05 and _s['TT'] > 1.0,
      'TT %.1f | TE %.1f | EE %.1f per cent' % (100 * _s['TT'], 100 * _s['TE'], 100 * _s['EE']))

check('Ⓒ④ ⛭⛭⛭ AND THE HEADLINE STRUCTURE: `TT` ALONE MOVES THE CROSSING FURTHER THAN ALL '
      'THIRTY-SIX TOGETHER, so removing `TE`\'s and `EE`\'s twelve on top of `TT`\'s partially '
      'CANCELS the move. ⇒ *That is an interference between blocks with a sign, not a rounding '
      'residual*',
      _m['TT'] > D['move_all36_meV'] and _s['TT'] > 1.0,
      'TT alone %+.4f against all thirty-six %+.4f' % (_m['TT'], D['move_all36_meV']))

check('Ⓒ⑤ and every single-block move is still POSITIVE, so the interference is a partial '
      'cancellation between same-signed contributions and not a block pulling the other way',
      all(_m[b] > 0.0 for b in BLOCKS) and D['move_all36_meV'] > 0.0,
      'signs %s' % {b: ('+' if _m[b] > 0 else '-') for b in BLOCKS})

check('Ⓒ⑥ and each single-block move is a crossing DIFFERENCE against the same whole-mask '
      'crossing, so the three are commensurable with each other and with the whole',
      all(abs((_c[b] - D['base_crossing_meV']) - _m[b]) < 1e-09 for b in BLOCKS),
      'all three reconstruct from their own crossings')

# ---------------------------------------------------------------------------------------------- Ⓓ
print('\nⒹ  THE REGISTERED OUTCOME IS `Ⓦ⓷`, AND THE REGISTERED EXPECTATION IS REFUTED')

check('Ⓓ① the three single-block moves sum to `+25.0463` against the whole `+20.0868`, a residual '
      'of `4.9594` meV',
      abs(D['sum_of_blocks_meV'] - 25.0463) < 5e-05
      and abs(D['residual_meV'] - 4.9594) < 5e-05,
      'sum %+.4f, residual %+.4f meV' % (D['sum_of_blocks_meV'], D['residual_meV']))

check('Ⓓ② which is `24.7` per cent of the whole move, OVER the ten-per-cent bar, so the held move '
      'is NOT additive and the registered outcome is `Ⓦ⓷`',
      abs(100 * D['residual_fraction'] - 24.7) < 0.05
      and D['residual_fraction'] > 0.10 and D['additive'] is False
      and D['outcome'] == 'Ⓦ⓷',
      'residual %.1f per cent, additive %s, outcome %s' % (100 * D['residual_fraction'],
                                                           D['additive'], D['outcome']))

check('Ⓓ③ and `TT`\'s dominance is reported ALONGSIDE it rather than instead of it, which the '
      'registration required by fixing in advance that the two are not exclusive and that the '
      'non-additive reading is the stronger where both fire',
      D['concentrated'] and D['largest_block'] == 'TT'
      and len(set(re.findall('Ⓦ([⓵-⓷])', PRED))) == len(('additive', 'other', 'non')),
      'concentrated %s in %s, both reported' % (D['concentrated'], D['largest_block']))

check('Ⓓ④ and the registered expectation `Ⓦ⓵` is recorded REFUTED against what was registered '
      'rather than reshaped to fit — the registration having said in advance that this seat '
      'expected to be wrong about as often as it had been',
      D['outcome'] != 'Ⓦ⓵'
      and 'I expect to be wrong about this roughly as often as I have been: r7890 and '
          'r7892 both refuted their own registered expectations, and both were more useful '
          'for it' in PRED,
      'expected Ⓦ⓵, got %s' % D['outcome'])

# ---------------------------------------------------------------------------------------------- Ⓔ
print('\nⒺ  THE CLOCK COMPARISON — LOCATION SURVIVES, ADDITIVITY DOES NOT')

check('Ⓔ① `r7892`\'s shares are read out of ITS record rather than retyped here, so the comparison '
      'is against that revision\'s measurement and not a remembered version of it',
      all(abs(D['reprofiled_shares'][b] - float(BB['block_shares'][b])) < 1e-12 for b in BLOCKS)
      and D['reprofiled_largest'] == BB['largest_block'],
      're-profiled %s' % {b: '%.1f' % (100 * D['reprofiled_shares'][b]) for b in BLOCKS})

check('Ⓔ② the SAME block dominates on both clocks — `84.4` per cent re-profiled against `106.4` '
      'per cent held — so by the standing `r7138` guard the LOCATION survives the change of clock '
      'and is content, not an artefact of the freedom the instrument gets and the reference does not',
      D['largest_block'] == D['reprofiled_largest'] == 'TT'
      and abs(100 * D['reprofiled_shares']['TT'] - 84.4) < 0.05
      and abs(100 * D['block_shares']['TT'] - 106.4) < 0.05
      and D['location_survives'] is True,
      'TT on both: %.1f -> %.1f per cent' % (100 * D['reprofiled_shares']['TT'],
                                             100 * D['block_shares']['TT']))

check('Ⓔ③ ⛭⛭⛭ AND THE ADDITIVITY DOES NOT SURVIVE: the residual goes `6.5` per cent re-profiled to '
      '`24.7` per cent held, a near-fourfold rise, so the four parameters when FREE were absorbing '
      'the cross-block interference. ⇒ *`r7892`\'s clean decomposition was a true measurement of '
      'its own column and a misleading guide to the data, and only the second clock shows which*',
      abs(100 * float(BB['residual_fraction']) - 6.5) < 0.05
      and bool(BB['additive']) is True and D['additive'] is False
      and D['residual_fraction'] / float(BB['residual_fraction']) > 3.0,
      'residual %.1f -> %.1f per cent, ratio %.2f'
      % (100 * float(BB['residual_fraction']), 100 * D['residual_fraction'],
         D['residual_fraction'] / float(BB['residual_fraction'])))

# ---------------------------------------------------------------------------------------------- Ⓕ
print('\nⒻ  THE RECORD SAYS WHAT THIS ESTABLISHES AND WHAT IT REFUSES')

check('Ⓕ① the record states the arithmetic and that it clears the bar in the wrong direction',
      'The three sum to +25.0463 against the whole +20.0868: a residual of 4.9594 meV, 24.7 per '
      'cent, well over the ten-per-cent bar' in RES)

check('Ⓕ② and that the non-additive reading is the stronger one, so the lesser shares are not '
      'offered as shares',
      'is the stronger reading and the shares below the leading block are not to be trusted as '
      'shares' in RES)

check('Ⓕ③ and the headline structure, that one block alone outruns all three together',
      'TT alone moves the crossing FURTHER than all thirty-six together — +21.3711 against '
      '+20.0868. So removing TE\'s and EE\'s twelve on top of TT\'s partially cancels the move'
      in RES)

check('Ⓕ④ and the answer to the question the revision asked, in those words',
      'THE LOCATION SURVIVES THE CHANGE OF CLOCK AND THE ADDITIVITY DOES NOT' in RES)

check('Ⓕ⑤ and that the location is therefore content rather than the profiling freedom',
      'the location is content: r7892\'s TT is the data\'s and not an artefact of the freedom the '
      'instrument is given and the reference is not' in RES)

check('Ⓕ⑥ and that the freedom was absorbing the interference',
      'So the profiling freedom was absorbing the cross-block interference, and r7892\'s clean '
      'decomposition was clean because of it' in RES)

check('Ⓕ⑦ and that it says so about its OWN predecessor plainly rather than softening it',
      'r7892\'s additivity was a true measurement of its own column and a misleading guide to the '
      'data, and only the second clock shows which' in RES)

check('Ⓕ⑧ and that the held vector was gated against a fresh fit at exactly zero deviation',
      'which reproduces it with a maximum deviation of exactly zero, so the record is the fit and '
      'not a stale copy of one' in RES)

check('Ⓕ⑨ and that naming an interference is not explaining one',
      'A block is not a mechanism, and naming the interference is not explaining it' in RES)

check('Ⓕ⑩ and that the interference is measured on one clock only, leaving partial freedom unopened',
      'The interference is measured on the held clock only' in RES)

print('\n' + '=' * 100)
print('  %d arm(s); %d failed' % (NARMS, len(FAILS)))
for f in FAILS:
    print('    FAILED: %s' % f)
print('=' * 100)
sys.exit(1 if FAILS else 0)
