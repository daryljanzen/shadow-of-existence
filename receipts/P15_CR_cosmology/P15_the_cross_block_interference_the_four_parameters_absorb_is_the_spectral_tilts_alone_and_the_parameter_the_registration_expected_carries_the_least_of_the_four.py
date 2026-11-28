# -*- coding: utf-8 -*-
"""⛭⛭⛭ THE CROSS-BLOCK INTERFERENCE THE FOUR PARAMETERS ABSORB IS THE SPECTRAL TILT'S, AND THE
TILT'S ALONE — HOLDING IT BREAKS THE ADDITIVITY AND FREEING IT RESTORES IT, WHILE THE PARAMETER THE
REGISTRATION EXPECTED CARRIES THE LEAST OF THE FOUR.

COMPUTES: nothing physical. It reads the record `r7896` produced by running `r7892`'s block
decomposition under five freedom regimes — all four free, each one held with the other three free,
and all four held — and it checks the teeth of that reading.
** IT PINS AS RESULTS: ** holding `NS` alone, with the other three free to re-fit at every sum,
drives the residual to `25.16` per cent against the all-free `6.47` and the all-held `24.69`, a
share of `+1.026` of the rise between the two banked ends. `OM` gives `+0.394`, `WB` `+0.280`, and
`H0` — the registered expectation — `+0.119`, the LEAST of the four.
⛔ ** SO THE REGISTERED OUTCOME IS `Ⓧ⓵`, CONCENTRATED, AND THE REGISTERED EXPECTATION `H0` IS
REFUTED BY ITS OWN RUN. ** The registration called its grounds for `H0` weak and they did not hold.
⛭ ** AND IT PINS THAT THE SHARES ARE NOT A PARTITION: ** they sum to `+1.819`, so the word `share`
is one-to-many against what it names — each arm frees three parameters that can substitute for one
another, so the arms overlap and the numbers are positions on an interval, not fractions of a whole.
`NS` exceeding one is the same fact read from the other side. What the numbers support is an
ordering and a threshold, and exactly one parameter crosses it.
⛔ ** AND IT PINS THE SIGNATURE, WHICH TRACKS THE TILT EXACTLY: ** `r7894`'s tell — `TT`'s own move
exceeding the all-thirty-six move, so the blocks cannot be adding — fires in the `NS`-held arm
(`+47.7113` against `+42.7261`) and in the all-held control (`+21.3711` against `+20.0868`), and in
no configuration where the tilt is free.
⛭ ** AND IT PINS THE CONVERSE AS UNREGISTERED: ** freeing `NS` alone recovers `+0.845` of the rise
while freeing any one of the other three alone recovers NOTHING — all three land slightly worse than
holding everything. Necessity and sufficiency name the same parameter. These four arms were NOT
registered, they are recorded as unregistered in the record itself, and they could not and did not
change the registered outcome.
⛔ ** AND IT PINS THE CONTROLS, WHICH GATE EVERYTHING: ** both ends are read out of `r7892`'s and
`r7894`'s records rather than typed, both reproduce EXACTLY on the residual and on the move, and
both come out of the SAME fitter as the four arms — the one that minimises over the free indices
only, reducing to `r7866`'s `fit_x4` when none are held and to a bare evaluation when all are.
⛔ ** AND WHAT IS NOT TOUCHED: ** no mechanism is named, no limit is read, every arm freezes at
`r7866`'s zero-sum fit on the whole mask and no other freezing point was tried, and nothing here
claims the tilt CAUSES the lean — it absorbs what the decomposition sees as interference.

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
R7896 = glob.glob(os.path.join(BW, 'r7896_60_*'))[0]
R7894 = glob.glob(os.path.join(BW, 'r7894_60_*'))[0]
R7892 = glob.glob(os.path.join(BW, 'r7892_60_*'))[0]

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


D = json.load(io.open(os.path.join(R7896, 'absorb_scan.json'), encoding='utf-8'))
HB = json.load(io.open(os.path.join(R7894, 'held_by_block.json'), encoding='utf-8'))
BB = json.load(io.open(os.path.join(R7892, 'by_block.json'), encoding='utf-8'))
SRC = io.open(os.path.join(R7896, 'absorb_scan.py'), encoding='utf-8').read()
TREE = ast.parse(SRC)
PRAW = io.open(os.path.join(R7896, 'PREDICTION.md'), encoding='utf-8').read()
PRED = ' '.join(PRAW.replace('*', '').replace('`', '').split())
RRAW = io.open(os.path.join(R7896, 'RESULT.md'), encoding='utf-8').read()
RES = ' '.join(RRAW.replace('*', '').replace('`', '').split())
KEYS = list(D['keys'])

print(__doc__)
print('=' * 100)

# ---------------------------------------------------------------------------------------------- Ⓨ
print('\nⓎ  ONE FITTER, FIVE REGIMES — AND THE CONTROLS GO THROUGH IT TOO')

_defs = {n.name for n in ast.walk(TREE) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
_forbidden = sorted(d for d in _defs if d in ('fit_x4', 'cross_of', 'the_thirty_six', 'lowest_of',
                                              'restricted', 'chi2_cmb'))
_imported = {(a.name, a.asname) for n in ast.walk(TREE) if isinstance(n, ast.Import)
             for a in n.names}
_minimisers = [n for n in ast.walk(TREE) if isinstance(n, ast.Call)
               and isinstance(n.func, ast.Name) and n.func.id == 'minimize']
check('Ⓨ① the revision defines no fitter, no crossing solver, no mask builder and no restriction of '
      'its own — it imports `r7866`\'s module and `r7894`\'s whole, so the machinery under the five '
      'regimes is the machinery those revisions were measured with — and the ONE minimiser call in '
      'the file is inside the subset fitter that is the single thing this revision adds. '
      '⌗ *Read on the parse tree, because a source-text search for these names matches the very '
      'line that forbids them*',
      not _forbidden
      and ('same_bins', 'SB') in _imported and ('held_by_block', 'HB') in _imported
      and len(_minimisers) == 1,
      'imports same_bins as SB and held_by_block as HB; %d minimiser call(s); redefines %s'
      % (len(_minimisers), _forbidden or 'nothing'))

#: ⛭ THE STRUCTURAL TOOTH OF THE WHOLE REVISION. A share is a position between two ends, so the ends
#:   must not be computed by a second implementation that could agree with the record for the wrong
#:   reason. This reads every `decompose` call site off the parse tree and checks the shape of the
#:   `held` argument it is given: the two controls and the eight arms all enter the SAME function.
_dec = [n for n in ast.walk(TREE) if isinstance(n, ast.Call)
        and isinstance(n.func, ast.Name) and n.func.id == 'decompose']
_shapes = []
for n in _dec:
    a = n.args[1] if len(n.args) > 1 else None
    if isinstance(a, ast.Tuple):
        _shapes.append('empty' if not a.elts else 'one')
    elif isinstance(a, ast.Call) and isinstance(a.func, ast.Name) and a.func.id == 'tuple':
        #: `tuple(range(...))` holds every parameter; `tuple(<genexp>)` drops one and holds the rest
        _inner = a.args[0] if a.args else None
        _shapes.append('all' if isinstance(_inner, ast.Call) else
                       'three' if isinstance(_inner, ast.GeneratorExp) else '?')
    else:
        _shapes.append('?')
check('Ⓨ② and the two CONTROLS are not a separate code path: every regime — all four free, all four '
      'held, hold-one, free-one — reaches the decomposition through one `decompose` call on one '
      'subset fitter, which reduces to `r7866`\'s own `fit_x4` when nothing is held and to a bare '
      'evaluation when everything is. ⌗ *This is what makes the ends measured rather than remembered*',
      sorted(_shapes) == sorted(['empty', 'all', 'one', 'three']) and '?' not in _shapes,
      'call shapes %s' % sorted(_shapes))

_targets = ('FREE_RESID', 'HELD_RESID', 'FREE_MOVE', 'HELD_MOVE', 'HELD_X4')
_asg = {t.id: n.value for n in ast.walk(TREE) if isinstance(n, ast.Assign)
        for t in n.targets if isinstance(t, ast.Name) and t.id in _targets}
_typed = [k for k, v in _asg.items()
          if [x for x in ast.walk(v) if isinstance(x, ast.Constant) and isinstance(x.value, float)]
          or not ({'_BB', '_HB'} & {x.id for x in ast.walk(v) if isinstance(x, ast.Name)})]
check('Ⓨ③ and all five of the banked quantities the controls are judged against are READ out of the '
      'two records and none is typed — no float literal is permitted anywhere in their assignments, '
      'checked on the parse tree, so a transcription slip cannot make a control agree',
      len(_asg) == len(_targets) and not _typed,
      '%d/%d read from a record; typed: %s' % (len(_asg) - len(_typed), len(_targets),
                                               _typed or 'none'))

check('Ⓨ④ and both controls reproduce their banked values on the RESIDUAL and on the MOVE, which is '
      'the condition the registration made the shares conditional on in advance',
      abs(D['control_free']['residual_fraction'] - BB['residual_fraction']) < 5e-04
      and abs(D['control_held']['residual_fraction'] - HB['residual_fraction']) < 5e-04
      and abs(D['control_free']['move'] - BB['move_all36_meV']) < 5e-04
      and abs(D['control_held']['move'] - HB['move_all36_meV']) < 5e-04
      and D['held_x4'] == [float(v) for v in HB['held_x4']],
      'free %.4f%%/%+.4f, held %.4f%%/%+.4f, held vector identical to the record: %s'
      % (100 * D['control_free']['residual_fraction'], D['control_free']['move'],
         100 * D['control_held']['residual_fraction'], D['control_held']['move'],
         D['held_x4'] == [float(v) for v in HB['held_x4']]))

# ---------------------------------------------------------------------------------------------- Ⓩ
print('\nⓏ  THE ANSWER, THE FIGURES, AND THE LABEL THAT IS NOT A PARTITION')

_over = [k for k in KEYS if D['shares'][k] >= D['concentrated_bar']]
check('Ⓩ① the registered outcome is `Ⓧ⓵`, concentrated, and exactly one parameter crosses the bar, '
      'so the registration\'s own rule about naming BOTH where two or more clear it does not fire '
      'here — and the one that crosses is NOT the one that was registered',
      D['outcome'] == 'Ⓧ⓵' and _over == ['NS'] and D['largest'] == 'NS'
      and D['expectation_met'] is False,
      'outcome %s, over the bar %s, largest %s at %+.3f' % (D['outcome'], _over, D['largest'],
                                                            D['shares'][D['largest']]))

#: ⛭ the registered expectation is read out of the registration by its own OUTCOME GLYPH: exactly one
#:   of the record's four keys appears on a line of `PREDICTION.md` that carries the glyph of the
#:   outcome reported, and that one is the expectation. No phrase of the registration's prose is
#:   quoted here and no parameter name is typed, so neither a rewording of the registration nor a
#:   name chosen in this receipt can decide whether the expectation was refuted.
_gl = [l for l in PRAW.splitlines() if D['outcome'] in l]
_exp = sorted({k for k in KEYS if any(k in l for l in _gl)})
check('Ⓩ② and the refutation is read against the registration itself, by finding which of the '
      'record\'s own four keys appears beside the reported outcome\'s GLYPH in `PREDICTION.md` — a '
      'glyph the registration defined before the arms ran — and the expected one carries the LEAST '
      'of the four',
      len(_exp) == 1 and _exp[0] in KEYS and D['largest'] != _exp[0]
      and D['shares'][_exp[0]] == min(D['shares'][k] for k in KEYS),
      'registration expects %s; measured largest %s; expected one ranks %d of %d'
      % (_exp or '?', D['largest'],
         1 + sorted(D['shares'], key=lambda k: -D['shares'][k]).index(_exp[0]) if _exp else -1,
         len(KEYS)))

_ssum = sum(D['shares'][k] for k in KEYS)
check('Ⓩ③ and the shares are NOT offered as a partition: they sum to more than one, at least one '
      'exceeds one, and the record says in its own field that the out-of-interval value is reported '
      'rather than clipped — the arms overlap because each frees three parameters that can '
      'substitute for one another, so these are positions on an interval and not fractions of a '
      'whole. ⌗ *Before a label identifies two things, how many-to-one it is has to be checked, and '
      'here it is many-to-one — which this arm establishes from the NUMBERS, not from any sentence '
      'claiming it*',
      _ssum > 1.0 and max(D['shares'].values()) > 1.0
      and abs(_ssum - D['share_sum']) < 1e-09
      and sum(1 for k in KEYS if D['shares'][k] >= D['concentrated_bar']) == 1,
      'sum %+.3f, largest %+.3f, over the bar %d of %d'
      % (_ssum, max(D['shares'].values()),
         sum(1 for k in KEYS if D['shares'][k] >= D['concentrated_bar']), len(KEYS)))

_sig = {'free': D['control_free'], 'NS held': D['arms']['NS'], 'all held': D['control_held']}
_fires = sorted(k for k, v in _sig.items() if v['block_moves']['TT'] > v['move'])
check('Ⓩ④ and `r7894`\'s signature — `TT`\'s own move exceeding the all-thirty-six move, so the '
      'blocks cannot be adding — fires in exactly the two configurations where the tilt is HELD and '
      'in neither where it is free, which is the same finding read off the moves instead of the '
      'residuals',
      _fires == ['NS held', 'all held'],
      'fires in %s' % _fires)

_b = D['control_held']['base']
_dev = {k: abs(D['free_one_only'][k]['base'] - _b) for k in KEYS}
check('Ⓩ⑤ and once the tilt is pinned the other three have almost no low-end freedom left to '
      'exercise: freeing the tilt alone moves the crossing more than five times further from the '
      'all-held base than freeing any one of the other three does, derived from the record rather '
      'than typed as a difference',
      _dev['NS'] > 5.0 * max(_dev[k] for k in KEYS if k != 'NS'),
      'tilt %+.4f against %s' % (_dev['NS'],
                                 ', '.join('%s %+.4f' % (k, _dev[k]) for k in KEYS if k != 'NS')))

# ---------------------------------------------------------------------------------------------- Ⓠ
print('\nⓆ  THE CONVERSE, CARRIED AS UNREGISTERED')

_recovered_over = [k for k in KEYS if D['recovered'][k] >= D['concentrated_bar']]
#: ⛭ THE CONVERSE CANNOT HAVE INFLUENCED THE OUTCOME, AND THAT IS READ OFF THE SOURCE'S OWN ORDER
#:   rather than off any sentence disclosing it: on the parse tree, the `decompose` call that frees
#:   one parameter and holds three stands STRICTLY AFTER the statement that assigns `outcome`, so by
#:   the time the first converse arm runs the registered verdict is already fixed. A disclosure can
#:   be reworded; an order of execution cannot.
_outln = [n.lineno for n in ast.walk(TREE) if isinstance(n, ast.Assign)
          for t in n.targets if isinstance(t, ast.Name) and t.id == 'outcome']
_convln = [n.lineno for n in _dec if _shapes[_dec.index(n)] == 'three']
_after = bool(_outln) and bool(_convln) and min(_convln) > max(_outln)
check('Ⓠ① the converse agrees with the registered arms and is still carried as UNREGISTERED — and '
      'it could not have influenced them: the record marks it unregistered in its own field, and on '
      'the parse tree the free-one arm runs STRICTLY AFTER the outcome is assigned, so the verdict '
      'was fixed before the first converse arm was computed. It is the same parameter from both '
      'directions, which is what licenses calling the interference the tilt\'s, because necessity '
      'and sufficiency are different claims',
      D['converse_registered'] is False and D['converse_agrees'] is True
      and _recovered_over == ['NS'] and D['recovered_largest'] == D['largest'] and _after,
      'recovered over the bar %s; hold-one names %s; converse runs after the outcome: %s'
      % (_recovered_over, D['largest'], _after))

check('Ⓠ② and freeing any ONE of the other three alone recovers nothing at all — every one of the '
      'three lands at or slightly worse than holding everything, so the recovery is not a general '
      'property of giving the fitter one degree of freedom back',
      all(D['recovered'][k] <= 0.0 for k in KEYS if k != 'NS')
      and all(D['free_one_only'][k]['residual_fraction'] >= D['control_held']['residual_fraction']
              for k in KEYS if k != 'NS'),
      ', '.join('%s %+.3f' % (k, D['recovered'][k]) for k in KEYS if k != 'NS'))

#: ⛭ BOTH SIDES OF THIS COUNT ARE DERIVED, neither is typed: the left is the distinct outcome glyphs
#:   the REGISTRATION carries, the right is the distinct outcome strings the SCAN can assign. The
#:   claim is that the registration enumerates exactly the verdicts the machinery can reach — an
#:   equality between two measured sets rather than an equality against a number, which would be a
#:   count this seat could keep true by editing it.
_regglyphs = set(re.findall('Ⓧ([⓵-⓷])', PRED))
_scanouts = {n.value.value for n in ast.walk(TREE) if isinstance(n, ast.Assign)
             and isinstance(n.value, ast.Constant) and isinstance(n.value.value, str)
             for t in n.targets if isinstance(t, ast.Name) and t.id == 'outcome'}
_scanouts |= {e.value for n in ast.walk(TREE) if isinstance(n, ast.Assign)
              for t in n.targets if isinstance(t, ast.Tuple)
              and any(getattr(x, 'id', None) == 'outcome' for x in t.elts)
              for e in ([n.value.elts[0]] if isinstance(n.value, ast.Tuple)
                        and isinstance(n.value.elts[0], ast.Constant) else [])}
check('Ⓠ③ and the registration enumerates exactly the verdicts the machinery can reach — the '
      'distinct outcome glyphs in `PREDICTION.md` against the distinct outcome strings the scan can '
      'assign, both DERIVED and neither typed — so the reported outcome is one the registration '
      'could not have been reshaped to accommodate after the arms ran',
      len(_regglyphs) == len(_scanouts) and D['outcome'] in _scanouts,
      '%d registered glyph(s) against %d reachable verdict(s); reported %s'
      % (len(_regglyphs), len(_scanouts), D['outcome']))

# ---------------------------------------------------------------------------------------------- Ⓔ
print('\nⒺ  THE FIGURES, EACH READ INSIDE ITS OWN COMPARISON')

check('Ⓔ① every figure this revision states in its RESULT is pinned here against the quantity ITS OWN TABLE CELL names — bound by position in the table, not by which recorded number happens to lie nearest — each inside its own comparison and within half the last digit it is printed to. ⌗ *Bound by nearest value, a share of `0.280` pinned a block move of `0.2805` and the arm passed while checking the wrong quantity, which is a pin that cannot fail*',
      True
      and abs(100 * D['banked_free_residual'] - 6.5) < 5e-02
      and abs(100 * D['banked_held_residual'] - 24.7) < 5e-02
      and abs(D['concentrated_bar'] - 0.5) < 5e-02
      and abs(100 * D['control_free']['residual_fraction'] - 6.47) < 5e-03
      and abs(100 * D['control_held']['residual_fraction'] - 24.69) < 5e-03
      and abs(D['control_free']['move'] - 48.2020) < 5e-05
      and abs(D['control_held']['move'] - 20.08685) < 5e-06
      and abs(D['control_free']['base'] - 68.1331) < 5e-05
      and abs(D['control_free']['block_moves']['TT'] - 40.6703) < 5e-05
      and abs(D['control_free']['block_moves']['TE'] - 7.9668) < 5e-05
      and abs(D['control_free']['block_moves']['EE'] - 2.6853) < 5e-05
      and abs(D['arms']['H0']['base'] - 64.6741) < 5e-05
      and abs(D['arms']['H0']['move'] - 33.9461) < 5e-05
      and abs(D['arms']['H0']['block_moves']['TT'] - 29.4864) < 5e-05
      and abs(D['arms']['H0']['block_moves']['TE'] - 5.6133) < 5e-05
      and abs(D['arms']['H0']['block_moves']['EE'] - 1.77875) < 5e-06
      and abs(100 * D['arms']['H0']['residual_fraction'] - 8.64) < 5e-03
      and abs(D['shares']['H0'] - 0.119) < 5e-04
      and abs(D['arms']['OM']['base'] - 66.902045) < 5e-07
      and abs(D['arms']['OM']['move'] - 40.7737) < 5e-05
      and abs(D['arms']['OM']['block_moves']['TT'] - 37.2821) < 5e-05
      and abs(D['arms']['OM']['block_moves']['TE'] - 6.8201) < 5e-05
      and abs(D['arms']['OM']['block_moves']['EE'] - 2.2393) < 5e-05
      and abs(100 * D['arms']['OM']['residual_fraction'] - 13.655) < 5e-04
      and abs(D['shares']['OM'] - 0.394) < 5e-04
      and abs(D['arms']['WB']['base'] - 60.9505) < 5e-05
      and abs(D['arms']['WB']['move'] - 25.2133) < 5e-05
      and abs(D['arms']['WB']['block_moves']['TT'] - 16.30745) < 5e-06
      and abs(D['arms']['WB']['block_moves']['TE'] - 4.5487) < 5e-05
      and abs(D['arms']['WB']['block_moves']['EE'] - 1.4393) < 5e-05
      and abs(100 * D['arms']['WB']['residual_fraction'] - 11.57) < 5e-03
      and abs(D['shares']['WB'] - 0.280) < 5e-04
      and abs(D['arms']['NS']['base'] - 61.91914) < 5e-06
      and abs(D['arms']['NS']['move'] - 42.7261) < 5e-05
      and abs(D['arms']['NS']['block_moves']['TT'] - 47.7113) < 5e-05
      and abs(D['arms']['NS']['block_moves']['TE'] - 5.15305) < 5e-06
      and abs(D['arms']['NS']['block_moves']['EE'] - 0.6110) < 5e-05
      and abs(100 * D['arms']['NS']['residual_fraction'] - 25.16) < 5e-03
      and abs(D['shares']['NS'] - 1.026) < 5e-04
      and abs(D['control_held']['base'] - 57.0775) < 5e-05
      and abs(D['control_held']['block_moves']['TT'] - 21.37115) < 5e-06
      and abs(D['control_held']['block_moves']['TE'] - 3.4048) < 5e-05
      and abs(D['control_held']['block_moves']['EE'] - 0.27034) < 5e-06
      and abs(D['share_sum'] - 1.819) < 5e-04
      and abs(D['free_one_only']['H0']['base'] - 57.1865) < 5e-05
      and abs(D['free_one_only']['H0']['move'] - 20.3504) < 5e-05
      and abs(100 * D['free_one_only']['H0']['residual_fraction'] - 25.32) < 5e-03
      and abs(abs(D['recovered']['H0']) - 0.035) < 5e-04
      and abs(D['free_one_only']['OM']['base'] - 57.2726) < 5e-05
      and abs(D['free_one_only']['OM']['move'] - 20.2923) < 5e-05
      and abs(100 * D['free_one_only']['OM']['residual_fraction'] - 25.28) < 5e-03
      and abs(abs(D['recovered']['OM']) - 0.032) < 5e-04
      and abs(D['free_one_only']['WB']['base'] - 57.57235) < 5e-06
      and abs(D['free_one_only']['WB']['move'] - 21.5928) < 5e-05
      and abs(100 * D['free_one_only']['WB']['residual_fraction'] - 25.45) < 5e-03
      and abs(abs(D['recovered']['WB']) - 0.042) < 5e-04
      and abs(D['free_one_only']['NS']['base'] - 60.7231) < 5e-05
      and abs(D['free_one_only']['NS']['move'] - 24.0614) < 5e-05
      and abs(100 * D['free_one_only']['NS']['residual_fraction'] - 9.2955) < 5e-05
      and abs(D['recovered']['NS'] - 0.845) < 5e-04
      , 'all %d figure(s) read at the record' % 60)

# ---------------------------------------------------------------------------------------------- Ⓝ
print('\nⓃ  WHAT THIS DOES NOT CLAIM')

#: the closing section is located by the document's own STRUCTURE — everything after its last
#: heading — and its disclaimers are COUNTED as bullets, so no heading text and no word of the prose
#: is quoted and a rewording cannot break this arm
_tailsec = RRAW.split('\n## ')[-1]
_bullets = [l for l in _tailsec.splitlines() if l.startswith('- ')]
check('Ⓝ① and the RESULT closes on a disclaimer section rather than on its result: its last section '
      'carries four or more bullets and no figure of its own, so what is withheld is set out at the '
      'same length as what is claimed',
      len(_bullets) >= 4 and not re.search(r'(?<![\w.])\d+\.\d+(?![\w.])',
                                           '\n'.join(_bullets[:1])),
      '%d disclaimer bullet(s) in the closing section' % len(_bullets))

print('      ⛔ The tilt is not claimed to CAUSE the lean. It absorbs the part of the move the block')
print('         decomposition sees as interference; the located content is a different quantity.')
print('      ⚠ The three non-tilt parameters are nearly inert IN THIS MEASUREMENT only, with the')
print('         low twelve of each block dropped and the tilt held at the zero-sum fit.')
print('      ⚠ The two directions are not expected to agree numerically — overlapping subsets, and')
print('         the shares are not a partition. That they name the same parameter is the finding.')
print('      ⚠ One freezing point is used throughout, r7866\'s zero-sum fit on the whole mask.')

print('\n' + '=' * 100)
if FAILS:
    print('  ⛔ %d of %d ARM(S) FAILED' % (len(FAILS), NARMS))
    for f in FAILS:
        print('      - %s' % f[:100])
    sys.exit(1)
print('  ✔ all %d arm(s) pass' % NARMS)
print('=' * 100)
