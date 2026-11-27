# -*- coding: utf-8 -*-
"""⛭⛭⛭ THE SWITCH CENSUS COUNTED FOUR AND THE BLOB EQUALITY NEEDED NINE -- THE STRIP-CLASS PATCH
`r7882` OWED IS NINE MECHANISMS AND NOT FOUR BINDINGS, EACH HALF OF IT MEASURED LOAD-BEARING
SEPARATELY; AND THE LENSING GRID DOES NOT FIT A LEG'S LIFETIME, SO ORDER `r7879` ITEM ⓷ SPLITS ON
THE CONDITION ITS OWN REGISTRATION DECLARED.

COMPUTES: the escape-hatch strip reduction of the acoustic instrument against the blob its spectral
bank records, measured on the working tree at this revision with the extension `r7882` owed to the
eighth strip class; each half of that extension measured load-bearing on its own, which are two
different measurements neither of which implies the other; the by-name hole closed for each of the
four switches `r7882` added, measured in both directions; the arithmetic of the switch census the
same change moved, including the invariant beside the moved number; the completeness and recorded
configuration of this revision's CMB grid; and the zero-sum property of the sixteen parameter-offset
legs the grid carries rather than re-runs.
** IT PINS AS RESULTS: ** the reduction is a FIXED POINT -- `2986` lines of working tree reducing
exactly to the banked blob's `2261` -- and it is so only with all nine parts: the four bindings
alone, in the machinery `r7879` applied, do NOT reduce, and the other eight parts with the bindings
omitted do NOT reduce either. The by-name hole is closed `4` of `4` in both directions: a moved
DEFAULT passes under by-name stripping and is red on exact value. The census's swept set carries
`35` names and none of the four; its gate asserts a total of `95`, which the instrument now reports
as `99`; and the clause beside that number, a difference of `60`, is preserved IDENTICALLY by the
patch because the same four names enter both the total and the swept set.  The CMB grid is `10` of
`10` points at sums `0.06`, `0.15`, `0.30`, `0.45` and `0.60` eV on both arms, every leg recording
`NQ = 12`, `LMAXNU = 12` and `QMAXNU = 20`; and all `16` carried offset legs sit at a sum of exactly
`0.0`.
⛔ ** AND IT PINS THE ERROR, WHICH IS THE PART WORTH KEEPING: ** the first patch written for this
debt was the four new switch bindings and nothing else, because four is what the CENSUS counts. It
failed the fixed point. A census is a COUNT; the blob comparison is an EQUALITY, and the same diff
added a module-level block, four functions, nine guarded statements, two offsets, two aliases and a
narrowed handover slice as well as the four bindings. ** The label "the four switches" was
many-to-one over a diff of nine mechanisms, and the standing guard says to check that before an
identification is made. ** The residual diff was then PRINTED rather than reasoned about further,
because a gate that compares a hash tells you the trees differ and nothing whatever about where.
⛔ ** AND IT PINS A SECOND ERROR, IN THE LABELLING OF THE TWO NECESSITY MEASUREMENTS: ** this file's
two halves were once the wrong way round -- the measurement that drops eight parts and keeps the
bindings was described as showing the bindings load-bearing, and the measurement that keeps the
eight and drops the bindings as showing the eight. ** Neither implies the other, and both are
asserted here separately so the swap cannot recur silently. **
⛔ ** AND IT PINS WHAT IS NOT CLAIMED: ** NO LIMIT IS READ IN THIS REVISION and the registered fork
is NOT decided; the three receipts this debt reddens are NOT run with the patch applied, because
applying it means editing receipts that are another seat's, so what is measured is the MACHINERY and
not those receipts' exit codes; and the lensing cost figure is a FLOOR -- `1h58m` is where a leg was
interrupted and not where it would end.

    python3 <this file>
"""
import ast
import io
import json
import os
import re
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
D = os.path.join(BW, 'r7884_60_the_controls_limits_on_the_jointly_validated_sector')
BANK = os.path.join(BW, 'bank')
NEWGRID = os.path.join(BANK, 'pol_grid_bvel1_nuhier')
OLDGRID = os.path.join(BANK, 'pol_grid_bvel1_nufd_only')
INSTF = os.path.join(BW, 'ACOUSTIC_two_arm.py')
CENSUS = os.path.join(HERE, 'P15_the_free_streaming_knob_is_common_to_both_arms_and_the_switch_'
                            'sweep_finds_no_further_shadow.py')
BLOBREC = [
    'P15_the_1p57_has_no_parameter_address_because_the_arms_tt_minimum_sits_on_its_own_bao_minimum'
    '_while_the_controls_pays_fifteen_in_chi2_to_leave_planck.py',
    'P15_the_fitted_comb_moves_nine_times_less_than_the_scale_that_rules_it_so_the_one_rate_takes'
    '_the_comb_from_299_1_to_298_94.py',
]
FAILS = []
NARMS = 0


def text(path):
    with io.open(path, encoding='utf-8') as fh:
        return fh.read()


def flat(path):
    """⌗ *whitespace-FLATTENED, so a prose pin does not depend on where a line happens to wrap*"""
    return ' '.join(text(path).split())


def check(name, ok, got=None):
    global NARMS
    NARMS += 1
    if ok:
        print('  [PASS] %s' % name + ('   (%s)' % got if got is not None else ''))
    else:
        FAILS.append(name)
        print('  [FAIL] %s' % name + ('   (got %s)' % got if got is not None else ''))


def leg_config(path):
    """each leg's OWN recorded configuration, read off the file rather than off the generator"""
    z = np.load(path, allow_pickle=True)
    return json.loads(str(np.atleast_1d(z['config'])[0]))


print(__doc__)
print('=' * 100)

sys.path.insert(0, D)
import tighten_nuhier as TN                                                    # noqa: E402

INST = text(INSTF)
_CFG = leg_config(TN.T.ARMNPZ)
BLOBSHA = _CFG['instrument_blob']
BLOB = subprocess.run(['git', 'cat-file', '-p', BLOBSHA], cwd=ROOT,
                      capture_output=True).stdout.decode()

# ---------------------------------------------------------------------------------------------- Ⓐ
print('\nⓐ'.replace('ⓐ', 'Ⓐ') + '  THE DEBT IS THIS SEAT\'S AND THE THREE RECEIPTS ARE NOT')

_present = [f for f in BLOBREC + [os.path.basename(CENSUS)]
            if os.path.exists(os.path.join(HERE, f))]
check('Ⓐ① all THREE receipts this revision\'s debt reddens are present to be read, so the claim '
      'about them is made against the files and not from memory',
      len(_present) == 3, '%d of 3' % len(_present))

#: ⛭ *the seat is read from the corpus's OWN revision-marker syntax -- `r####+seat` -- rather than
#: by hunting for a bare seat name in the text.  Three weak token pins became one pattern that
#: means something: a marker is a revision attributing a change, and a name in a sentence is not.*
_MARK = re.compile(r'r\d{4}\+(cc66|70)')
_marks = {}
for f in BLOBREC + [os.path.basename(CENSUS)]:
    _marks[f] = sorted(set(_MARK.findall(text(os.path.join(HERE, f)))))
check('Ⓐ② every one of the three carries at least one `r####+seat` marker naming a seat OTHER than '
      'this one, which is WHY the patch is routed and not applied: a shared receipt is not this '
      'seat\'s to edit',
      all(_marks.values()) and all('60' not in m for v in _marks.values() for m in v),
      '%d of 3 marked; seats %s'
      % (sum(1 for v in _marks.values() if v), sorted({m for v in _marks.values() for m in v})))

_reply = flat(os.path.join(ROOT, 'FOR_66_FROM_60.md'))
_stems = ['P15_the_1p57_has_no_parameter_address', 'P15_the_fitted_comb_moves_nine_times_less',
          'P15_the_free_streaming_knob']
check('Ⓐ③ the routed reply names all three by their own stems, so the patch has an addressee for '
      'each red rather than a general remark about the sector',
      all(s in _reply for s in _stems),
      '%d of 3 named' % sum(1 for s in _stems if s in _reply))

check('Ⓐ④ and the census gate\'s own failing text is in the census receipt verbatim, so the red '
      'named here is that gate and not another',
      'the instrument reads sixty environment switches' in flat(CENSUS))

# ---------------------------------------------------------------------------------------------- Ⓑ
print('\nⒷ  THE REDUCTION IS A FIXED POINT, AND EACH HALF OF THE PATCH IS LOAD-BEARING SEPARATELY')

check('Ⓑ① the banked blob is reachable and is the object the bank names, so the comparison below '
      'is against a recorded instrument and not against a reconstruction',
      len(BLOB) > 0 and len(BLOBSHA) == 40,
      '%s, %d lines' % (BLOBSHA[:12], BLOB.count('\n')))

check('Ⓑ② the four bindings are the instrument\'s OWN lines, read at source and not remembered',
      all(('%s = %s' % (k, v)) in INST for k, v in TN.EXACT_R7882.items()),
      '%d of 4 verbatim' % sum(1 for k, v in TN.EXACT_R7882.items()
                               if ('%s = %s' % (k, v)) in INST))

_fix = TN.reduces(INST, BLOB, 'exact')
check('Ⓑ③ THE FIXED POINT -- with all nine parts the working tree reduces to the banked blob '
      'EXACTLY, so the escape hatch certifies the instrument that produced the bank', _fix)

check('Ⓑ④ and the two trees it identifies are the pinned sizes, so the fixed point is not a '
      'comparison of something with itself',
      INST.count('\n') == 2986 and BLOB.count('\n') == 2261,
      'tree %d lines, blob %d lines' % (INST.count('\n'), BLOB.count('\n')))

_half1 = TN.reduces_bindings_only(INST, BLOB)
check('Ⓑ⑤ EACH HALF IS NECESSARY, FIRST HALF -- the four bindings alone, in the machinery `r7879` '
      'applied and otherwise UNEXTENDED, do NOT reduce, so parts Ⓕ through Ⓢ bear load',
      not _half1, 'reduces anyway' if _half1 else 'does not reduce')

_half2 = TN.reduces(INST, BLOB, 'off')
check('Ⓑ⑥ EACH HALF IS NECESSARY, SECOND HALF -- parts Ⓕ through Ⓢ with the four bindings OMITTED '
      'do NOT reduce either, so the bindings bear load. ⛔ *This is a DIFFERENT measurement from '
      'Ⓑ⑤ and neither implies the other, which is the labelling this file once had reversed*',
      not _half2, 'reduces anyway' if _half2 else 'does not reduce')

_both = {}
for _n, (_a, _b) in TN.CONTROLS:
    _mut = INST.replace(_a, _b, 1)
    _both[_n] = (INST.count(_a) == 1, TN.reduces(_mut, BLOB, 'byname'),
                 not TN.reduces(_mut, BLOB, 'exact'))
check('Ⓑ⑦ THE HOLE, BOTH WAYS, 4 of 4 -- for each of the four switches a moved DEFAULT PASSES '
      'under by-name stripping (that is the hole) and is RED on exact value (that is it closed); a '
      'control red both ways would have shown nothing',
      all(all(v) for v in _both.values()),
      '%d of 4 both ways' % sum(1 for v in _both.values() if all(v)))

_rec = json.load(io.open(os.path.join(D, 'tighten_nuhier.json'), encoding='utf-8'))
check('Ⓑ⑧ and the COMMITTED record agrees with what this run measures, so the file in the tree is '
      'not a stale copy of an earlier reading',
      _rec['fixed_point'] is True and _rec['blob'] == BLOBSHA
      and _rec['bindings_only_in_r7878_machinery'] is False
      and _rec['floor_bindings_only'] is False
      and all(c['byname_passes'] and c['exact_red'] for c in _rec['controls'].values()),
      '%d control(s) recorded' % len(_rec['controls']))

# ---------------------------------------------------------------------------------------------- Ⓒ
print('\nⒸ  THE PATCH IS NINE PARTS, AND THE MACHINERY IS IMPORTED RATHER THAN RETYPED')

_tn = ast.parse(text(os.path.join(D, 'tighten_nuhier.py')))
_imports = [n for n in ast.walk(_tn) if isinstance(n, ast.Import)
            and any(a.name == 'tighten' for a in n.names)]
_cls = [n for n in ast.walk(_tn) if isinstance(n, ast.ClassDef) and n.name == '_Strip82']
_bases = [ast.unparse(b) for n in _cls for b in n.bases]
check('Ⓒ① `r7878`\'s machinery is IMPORTED and its strip class SUBCLASSED, so the landed behaviour '
      'is inherited and not copied -- a copy would drift from what `r7879` actually applied',
      len(_imports) == 1 and len(_cls) == 1 and _bases == ['base'],
      '1 import, base %r' % (_bases,))

_ovr = {n.name for c in _cls for n in c.body if isinstance(n, ast.FunctionDef)}
_need = {'visit_Name', 'visit_FunctionDef', 'visit_If', 'visit_IfExp', 'visit_BinOp',
         'visit_Subscript', 'visit_Assign'}
check('Ⓒ② all SEVEN transformer overrides the nine parts need are present on the subclass',
      _need <= _ovr, '%d of 7' % len(_need & _ovr))

check('Ⓒ③ and the two maps the other two parts are, are present with their four entries each',
      len(TN.EXACT_R7882) == 4 and len(TN.CONFIG_R7882) == 4 and len(TN.FUNCS_R7882) == 4
      and len(TN.NAMES_R7882) == 3 and len(TN.ALIAS_R7882) == 2,
      'exact %d, config %d, funcs %d, by-name %d, aliases %d'
      % (len(TN.EXACT_R7882), len(TN.CONFIG_R7882), len(TN.FUNCS_R7882),
         len(TN.NAMES_R7882), len(TN.ALIAS_R7882)))

_S, _x = TN.make_strip_r7882('exact')
_s = _S()
_s.UNIT = set()
_withelse = ast.parse('if NUHIER:\n    a = 1\nelse:\n    b = 2\n')
_noelse = ast.parse('if NUHIER:\n    a = 1\n')
_r1 = ast.unparse(_s.visit(_withelse)).strip()
_r2 = ast.unparse(_S().visit(_noelse)).strip()
check('Ⓒ④ Ⓘ drops a `NUHIER` guard BOTH BRANCHES, measured on a tree built for it -- ⛔ *not "take '
      'the orelse" as the landed `_NU_ON` class does: the module-level block\'s `else` binds the '
      'quadrature to `None`, which the landed file does not do either*',
      _r1 == '' and _r2 == '', 'with-else %r, no-else %r' % (_r1, _r2))

_ifexp = ast.parse('z = q if NUHIER else dn\n')
_r3 = ast.unparse(_S().visit(_ifexp)).strip()
_binop = ast.parse('NV = 7 + _NH\n')
_r4 = ast.unparse(_S().visit(_binop)).strip()
check('Ⓒ⑤ Ⓧ reduces a `NUHIER` conditional to its `orelse` and Ⓞ drops `+ _NH` from an offset, '
      'each measured on a tree built for it rather than asserted of the diff',
      _r3 == 'z = dn' and _r4 == 'NV = 7', '%r and %r' % (_r3, _r4))

# ---------------------------------------------------------------------------------------------- Ⓓ
print('\nⒹ  THE CENSUS ARITHMETIC, AND THE CLAUSE BESIDE THE MOVED NUMBER')

_cen = ast.parse(text(CENSUS))
_swept = [ast.literal_eval(n.value) for n in ast.walk(_cen)
          if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Name)
          and n.targets[0].id == 'SWEPT_SIXTY_PLUS']
SW = _swept[0] if _swept else set()
check('Ⓓ① the census\'s swept set is read off its own source and carries `35` names, none of them '
      'one of the four this debt adds',
      len(_swept) == 1 and len(SW) == 35 and not (set(TN.EXACT_R7882) & SW),
      '%d names, %d of the four already in it' % (len(SW), len(set(TN.EXACT_R7882) & SW)))

_nums = set()
for n in ast.walk(_cen):
    if isinstance(n, ast.Compare) and isinstance(n.left, ast.Call) \
            and ast.unparse(n.left) == 'len(ROWS)' and isinstance(n.ops[0], ast.Eq):
        _nums.add(ast.literal_eval(n.comparators[0]))
check('Ⓓ② and its asserted TOTAL is read off the same source as `95`, not recalled from the failure '
      'message, so the number the patch moves is the number the gate holds',
      _nums == {95}, 'asserted total(s) %s' % sorted(_nums))

_diffs = set()
for n in ast.walk(_cen):
    if isinstance(n, ast.Compare) and isinstance(n.left, ast.Call) \
            and ast.unparse(n.left) == 'len(_ROWENVS - SWEPT_SIXTY_PLUS)':
        _diffs.add(ast.literal_eval(n.comparators[0]))
check('Ⓓ③ the clause BESIDE the moved number -- a difference of `60`, which is the one doing the '
      'work in that gate -- is read off the source too',
      _diffs == {60}, 'asserted difference(s) %s' % sorted(_diffs))

_k = len(TN.EXACT_R7882)
check('Ⓓ④ and the patch preserves that difference IDENTICALLY, because the same four names enter '
      'BOTH the asserted total and the swept set: `(95 + 4) - (35 + 4) == 95 - 35`. ⌗ *An identity '
      'in the patch\'s shape, so it does not depend on the row count at all*',
      (95 + _k) - (len(SW) + _k) == 95 - len(SW) == 60,
      '(95 + %d) - (%d + %d) = %d' % (_k, len(SW), _k, (95 + _k) - (len(SW) + _k)))

_reads = {}
for k in TN.EXACT_R7882:
    _reads[k] = any(isinstance(n, ast.Call) and ast.unparse(n.func) == 'os.environ.get'
                    and n.args and isinstance(n.args[0], ast.Constant) and n.args[0].value == k
                    for n in ast.walk(ast.parse(INST)))
check('Ⓓ⑤ and every one of the four IS read by the instrument through the environment, so each '
      'will appear as a census row and the total moves by exactly four',
      all(_reads.values()), '%d of 4 read' % sum(_reads.values()))

# ---------------------------------------------------------------------------------------------- Ⓔ
print('\nⒺ  THIS REVISION\'S CMB GRID IS COMPLETE AND ITS LEGS RECORD THE HIERARCHY')

SUMS = ['S006', 'S015', 'S030', 'S045', 'S060']
WANT = {'%s_%s' % (a, s) for a in ('lcdm', 'cr') for s in SUMS}
_have = {f[:-4] for f in os.listdir(NEWGRID) if f.endswith('.npz') and not f.endswith('_tt.npz')}
_tt = {f[:-7] for f in os.listdir(NEWGRID) if f.endswith('_tt.npz')}
check('Ⓔ① `10` of `10` points are banked -- five sums on each of the two arms -- each with its TT '
      'companion beside it',
      _have == WANT and _tt == WANT, '%d point(s), %d companion(s)' % (len(_have), len(_tt)))

_legs = {t: leg_config(os.path.join(NEWGRID, t + '.npz')) for t in sorted(WANT)}
_sw = all(c.get('NUHIER') is True and c.get('NUFD') is True and c.get('NQ') == 12
          and c.get('LMAXNU') == 12 and float(c.get('QMAXNU', -1)) == 20.0
          for c in _legs.values())
check('Ⓔ② every leg records the hierarchy ON at the registered resolution -- `NQ = 12`, '
      '`LMAXNU = 12`, `QMAXNU = 20` -- in its OWN stored configuration, so the grid\'s settings '
      'are read off the legs and not off the generator that was meant to set them', _sw,
      '%d of %d legs' % (sum(1 for c in _legs.values()
                             if c.get('NUHIER') is True and c.get('NQ') == 12), len(_legs)))

_bysum = {}
for t, c in _legs.items():
    _bysum.setdefault(t.split('_')[0], set()).add(round(float(c['MNU']), 6))
check('Ⓔ③ and each arm\'s five sums are `0.06`, `0.15`, `0.30`, `0.45` and `0.60` eV, read off the '
      'legs\' own configurations',
      _bysum.get('lcdm') == _bysum.get('cr') == {0.06, 0.15, 0.3, 0.45, 0.6},
      '%s' % {k: sorted(v) for k, v in sorted(_bysum.items())})

# ---------------------------------------------------------------------------------------------- Ⓕ
print('\nⒻ  THE SIXTEEN OFFSET LEGS THE GRID CARRIES ARE AT A ZERO SUM, WHICH IS WHY IT CARRIES THEM')

_off = sorted(f[:-4] for f in os.listdir(OLDGRID)
              if f.endswith('.npz') and not f.endswith('_tt.npz')
              and not f.split('_', 1)[1].startswith('S'))
_offc = {t: leg_config(os.path.join(OLDGRID, t + '.npz')) for t in _off}
check('Ⓕ① all `16` parameter-offset legs the read carries from the landed rung sit at a sum of '
      'EXACTLY `0.0`, so the hierarchy is inert on every one of them and carrying rather than '
      're-running them is exact and not an approximation',
      len(_off) == 16 and all(float(c['MNU']) == 0.0 for c in _offc.values()),
      '%d leg(s), %d at zero' % (len(_off), sum(1 for c in _offc.values()
                                                if float(c['MNU']) == 0.0)))

check('Ⓕ② and they are the four directions in each of the four parameters, two signs apiece, so '
      'what is carried is the whole offset block and not a subset of it',
      {t.split('_', 1)[1][:-1] for t in _off} == {'H0', 'OM', 'WB', 'NS'}
      and {t.split('_', 1)[1][-1] for t in _off} == {'p', 'm'},
      '%s' % sorted({t.split('_', 1)[1] for t in _off}))

# ---------------------------------------------------------------------------------------------- Ⓖ
print('\nⒼ  THE LIMIT READ LANDS AS REGISTERED AND UNRUN, WITH ITS GATES AHEAD OF ANY NUMBER')

_lim = ast.parse(text(os.path.join(D, 'limits_nuhier.py')))
_exits = [n for n in ast.walk(_lim) if isinstance(n, ast.Raise)
          and n.exc is not None and 'SystemExit' in ast.unparse(n.exc)]
_envs = [n for n in ast.walk(_lim) if isinstance(n, ast.Call)
         and ast.unparse(n.func).endswith('closed_envelope')]
_lgates = sorted({ast.literal_eval(a).split()[0] for n in ast.walk(_lim)
                  if isinstance(n, ast.Call) and ast.unparse(n.func) == 'gate'
                  and n.args and isinstance(n.args[0], ast.Constant)
                  and ast.literal_eval(n.args[0]).startswith('Ⓛ')
                  for a in [ast.unparse(n.args[0])]})
_guard = [n for n in ast.walk(_lim) if isinstance(n, ast.If)
          and ast.unparse(n.test) == 'FAILS'
          and any(isinstance(b, ast.Raise) and 'SystemExit' in ast.unparse(b.exc)
                  for b in n.body)]
check('Ⓖ① the read carries FOUR distinctly labelled plumbing gates and ONE refusal that fires if '
      'ANY of them failed, so a missing or mis-pointed bank stops it before it prints a number. '
      '⌗ *One refusal over an accumulated list, not four separate raises -- it reports every '
      'failure rather than only the first*',
      len(_lgates) == 4 and len(_guard) == 1 and len(_exits) == 1,
      '%s, %d guarded refusal(s)' % (_lgates, len(_guard)))

check('Ⓖ② and BOTH envelope reads are in it -- the CMB one and the lensing one -- so the lensing '
      'grid is not dropped from the read to make the read fit',
      len(_envs) == 2, '%d read(s)' % len(_envs))

check('Ⓖ③ and every refusal stands AHEAD of the first envelope read by line, which is what makes '
      'them plumbing gates rather than commentary',
      bool(_exits) and bool(_envs) and max(n.lineno for n in _exits) < min(n.lineno for n in _envs),
      'last refusal %d, first read %d'
      % (max(n.lineno for n in _exits), min(n.lineno for n in _envs)))

# ---------------------------------------------------------------------------------------------- Ⓗ
print('\nⒽ  THE SPLIT WAS REGISTERED BEFORE IT WAS TAKEN, AND WHAT IS NOT CLAIMED IS WRITTEN DOWN')

_pred = flat(os.path.join(D, 'PREDICTION.md'))
_res = flat(os.path.join(D, 'RESULT.md'))
_cost = flat(os.path.join(D, 'COST.md'))

check('Ⓗ① the registration declared the split IN ADVANCE, in those words, so taking it is a '
      'registered branch and not a retreat invented after the cost was seen',
      'the measured cost is reported and the item splits' in _pred)

check('Ⓗ② the record states plainly that no limit is read, so the revision cannot be read as '
      'having produced one',
      'NO LIMIT IS READ IN THIS REVISION' in _res)

check('Ⓗ③ and that the cost figure is a FLOOR and not a duration, which is the honest shape of a '
      'measurement taken by interrupting the thing measured',
      '`1h58m` is where a leg was interrupted, not where it would end' in _res
      and '`1h58m` is a floor, not a duration' in _cost)

check('Ⓗ④ and that the three receptacles of the debt are NOT run with the patch applied, with the '
      'reason, so the measurement is not mistaken for their exit codes',
      'The three receipts are not run with the patch applied' in _res)

print('\n' + '=' * 100)
print('  %d arm(s); %d failed' % (NARMS, len(FAILS)))
for f in FAILS:
    print('    FAILED: %s' % f)
print('=' * 100)
sys.exit(1 if FAILS else 0)
