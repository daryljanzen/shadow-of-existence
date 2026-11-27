# -*- coding: utf-8 -*-
"""⛭⛭⛭ THE LIMIT IS READ ON THE RUNNER'S COMPLETE GRID AND THE REPAIR MOVES IT **AWAY** FROM THE
REFERENCE -- AND THE ENVELOPE CLOSURE IS RULED OUT AS THE CAUSE BY A CONTROL THAT WAS ALREADY BANKED,
NOT BY AN ARGUMENT.

COMPUTES: nothing new. It reads the record `r7888` produced by running `r7884`'s landed limit module
on the ten lensing points `70`'s runners banked at `refs/ci/r7884_phiphi`, and the control `r7870`
banked for the same rung with the hierarchy off.
** IT PINS AS RESULTS: ** the registered fork fired `Ⓝ⓵′`, the calibrated minimum at `0.060` eV with
no dips above it, so the limit is READABLE and is read; the limit is `193.545` meV against the
reference's `30.56` meV, a ratio of `6.333`; and the move from `r7870`'s `185.95834` meV is `+7.587`
meV, `+4.08` per cent, in the direction AWAY from the reference, widening a gap of `155.398` meV to
`162.985` meV.
⛔ ** AND IT PINS THE DECOMPOSITION, WHICH IS WHAT MAKES THE MOVE ATTRIBUTABLE: ** on the same rung
with the hierarchy OFF, closing the envelope moves the calibrated crossing from `185.95834` to
`185.95842` meV -- `+0.00008` meV, a no-op, and it must be, because that profile is already monotonic
above its minimum. So the whole `+7.587` meV belongs to the hierarchy and none of it to the closure.
⌗ *On the MINIMISED column closure is the opposite, `181.436` to `287.772` meV on that same rung,
because that column is NOT monotonic above its minimum -- which is why the limit is read on the
calibrated column and a crossing on the minimised one is never a limit.*
⛔ ** AND IT PINS THE TEETH OF TWO GATES THIS REVISION REPAIRED WHILE THEY WERE REFUSING. ** Both had
never executed, because `r7884` landed the module registered and UNRUN, and both were wrong. Repairing
a refusing gate is exactly the move that needs checking, so each is RUN here on faulted inputs and
watched to bite, and on the real inputs and watched to pass.
⛔ ** AND IT PINS WHAT IS NOT CLAIMED: ** the limit is NOT joint -- one fitter, `cc66`'s second fit
outstanding -- and `193.545` meV is not offered as the control's limit of record.

    python3 <this file>
"""
import glob
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
R7888 = os.path.join(BW, 'r7888_60_the_limit_read_on_the_runners_complete_grid')
R7884 = os.path.join(BW, 'r7884_60_the_controls_limits_on_the_jointly_validated_sector')
R7870 = glob.glob(os.path.join(BW, 'r7870_60_*'))[0]

REFERENCE_MEV = 30.56                    #: the reference's calibrated limit, from the order
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


def load(p):
    return json.load(io.open(p, encoding='utf-8')) if os.path.isfile(p) else {}


REC = load(os.path.join(R7888, 'limit_on_runner_grid.json'))
CTRL = load(os.path.join(R7870, 'envelope_closed_nufd_only.json'))
SEP = load(os.path.join(R7870, 'limits_separating.json'))
#: ⛭ EMPHASIS STRIPPED, AND ONE LONG SENTENCE PER ARM.  An earlier draft asked for NINETEEN short
#:   fragments -- `'one fitter'`, `'it is not zero'`, `'never a limit'` -- and the quote-pin instrument
#:   counted every one as a key.  Nineteen weak pins raise the ceiling and each matches loosely; one
#:   long sentence per claim is a TIGHTER pin and costs one key.  Stripping `*` and backticks means the
#:   pin is the prose rather than its formatting, so re-emphasising a line cannot break it.
RES = ' '.join(io.open(os.path.join(R7888, 'RESULT.md'), encoding='utf-8')
               .read().replace('*', '').replace('`', '').split())

print(__doc__)
print('=' * 100)

# ---------------------------------------------------------------------------------------------- Ⓐ
print('\nⒶ  THE FORK FIRED AS REGISTERED, AND THE LIMIT IS THEREFORE READABLE')

_fork = REC.get('fork', {})
check('Ⓐ① the registered fork fired `Ⓝ⓵′` -- the calibrated minimum at `0.06` eV or above, so every '
      'profile point from it upward is supported by nodes the hierarchy actually solved, plus the '
      'exactly-carried zero node. ⌗ *This was fixed at `r7884` BEFORE any number existed; the branch '
      'is read here, not chosen*',
      _fork.get('branch') == 'Ⓝ⓵′' and abs(float(_fork.get('min_at', -1)) - 0.06) < 1e-12
      and _fork.get('limit_readable') is True,
      'branch %s at %s, readable %s'
      % (_fork.get('branch'), _fork.get('min_at'), _fork.get('limit_readable')))

check('Ⓐ② and no plumbing gate refused, so the number was reachable at all -- the module raises '
      'before either envelope read and prints nothing when one fails',
      'gates_failed' not in REC, REC.get('gates_failed', 'none failed'))

# ---------------------------------------------------------------------------------------------- Ⓑ
print('\nⒷ  THE NUMBER, AND IT MOVES THE WRONG WAY')

_moved = float(REC.get('moved_meV', 0.0))
_base = float(REC.get('baseline', {}).get('calibrated_limit_meV', 0.0))
_lim = _base + _moved
check('Ⓑ① the limit is `193.545` meV, read on the calibrated column of the closed envelope',
      abs(_lim - 193.545) < 5e-04, '%.3f meV' % _lim)

check('Ⓑ② the baseline it is read against is `r7870`\'s SEPARATING rung at `185.958` meV, which is '
      'the like-for-like lineage. ⛔ *Not `185.92`, the control\'s limit of record, which is a '
      'different rung*',
      abs(_base - 185.958) < 5e-04, '%.3f meV' % _base)

check('Ⓑ③ ⛔ the move is `+7.587` meV, `+4.08` per cent, and it is AWAY from the reference: the '
      'reference sits at `30.56` meV, so the instrument goes from `6.085` to `6.333` times it',
      abs(_moved - 7.587) < 5e-04 and _moved > 0.0
      #: ⛭ HALF A PRINTED DIGIT, not a decade looser.  These were pinned at `5e-03` against figures
      #:   printed to three decimals, which `check_figures_pinned` refused -- correctly: a pin ten
      #:   times wider than the last digit it prints would not fail if that digit were wrong.
      and abs(_lim / REFERENCE_MEV - 6.333) < 5e-04
      and abs(_base / REFERENCE_MEV - 6.085) < 5e-04,
      '%+.3f meV, %+.2f per cent; %.3f x -> %.3f x'
      % (_moved, 100.0 * _moved / _base, _base / REFERENCE_MEV, _lim / REFERENCE_MEV))

check('Ⓑ④ and the GAP widens: `155.398` meV becomes `162.985` meV, which is `+4.88` per cent of the '
      'gap that was already there',
      abs((_base - REFERENCE_MEV) - 155.398) < 5e-03
      and abs((_lim - REFERENCE_MEV) - 162.985) < 5e-03
      and abs(100.0 * _moved / (_base - REFERENCE_MEV) - 4.88) < 5e-02,
      '%.3f -> %.3f meV, +%.2f per cent of the old gap'
      % (_base - REFERENCE_MEV, _lim - REFERENCE_MEV, 100.0 * _moved / (_base - REFERENCE_MEV)))

# ---------------------------------------------------------------------------------------------- Ⓒ
print('\nⒸ  AND THE MOVE IS THE HIERARCHY\'S, NOT THE CLOSURE\'S -- A BANKED CONTROL, NOT AN ARGUMENT')

_craw = float(SEP.get('raw_calibrated', {}).get('crossing_meV', 0.0))
_cenv = float(SEP.get('env_calibrated', {}).get('crossing_meV', 0.0))
check('Ⓒ① the control exists and was banked BEFORE this revision: `r7870`\'s own record carries the '
      'calibrated crossing on the same rung both WITHOUT closure and WITH it, hierarchy OFF',
      _craw > 0.0 and _cenv > 0.0, 'raw %.5f meV, closed %.5f meV' % (_craw, _cenv))

check('Ⓒ② ⛔ CLOSING THE ENVELOPE IS A NO-OP ON THE CALIBRATED COLUMN -- `+0.00008` meV. So the '
      '`+7.587` meV cannot be the closure, and the whole of it belongs to the hierarchy. ⌗ *Reported '
      'without this control, the move would have credited the repair with whatever the closure did*',
      abs(_cenv - _craw) < 1e-03, '%+.5f meV' % (_cenv - _craw))

check('Ⓒ③ and it HAS to be a no-op there, which is the reason and not a coincidence: that profile is '
      'already monotonic above its minimum, so cross-seeding has nothing to repair',
      SEP.get('raw_calibrated', {}).get('monotonic_above_min') is True
      and SEP.get('env_calibrated', {}).get('monotonic_above_min') is True,
      'raw %s, closed %s' % (SEP.get('raw_calibrated', {}).get('monotonic_above_min'),
                             SEP.get('env_calibrated', {}).get('monotonic_above_min')))

_mraw = float(SEP.get('raw_minimised', {}).get('crossing_meV', 0.0))
_menv = float(SEP.get('env_minimised', {}).get('crossing_meV', 0.0))
check('Ⓒ④ ⛔ AND THE CONTROL IS NOT VACUOUS: on the MINIMISED column of that same rung closure moves '
      'the crossing `181.436` to `287.772` meV, because THAT column is not monotonic above its '
      'minimum. ⇒ *So "closure did nothing" is a property of the calibrated column, measured, and '
      'not a general claim that closure never matters -- which is what would make `Ⓒ②` worthless*',
      abs(_mraw - 181.436) < 5e-03 and abs(_menv - 287.772) < 5e-03
      and SEP.get('raw_minimised', {}).get('monotonic_above_min') is False,
      '%.3f -> %.3f meV, monotonic %s'
      % (_mraw, _menv, SEP.get('raw_minimised', {}).get('monotonic_above_min')))

check('Ⓒ⑤ and the control\'s closed calibrated crossing agrees with the baseline this revision was '
      'read against, so the two records are the same rung and not two different ones',
      abs(_cenv - _base) < 5e-03 and abs(float(CTRL.get('calibrated', {}).get('crossing_meV', 0))
                                         - _cenv) < 5e-03,
      'baseline %.3f, control closed %.5f' % (_base, _cenv))

# ---------------------------------------------------------------------------------------------- Ⓓ
print('\nⒹ  THE TEETH OF TWO GATES REPAIRED WHILE THEY WERE REFUSING -- RUN, NOT ASSERTED')

sys.path.insert(0, R7884)
import limits_nuhier as L                                                           # noqa: E402

_real = {'%s_%s' % (a, t): {'NUHIER': None, 'MNU': L.CARRY_SUMS.get(t, 0.0)}
         for a in L.ARMS for t in L.CARRY_TAGS}
_bad, _neg, _ok = L.carry_verdict(_real)
check('Ⓓ① `Ⓛ⓵` PASSES on a carry set where every point is the point its tag names, and it counts the '
      'four negative nodes rather than demanding they not exist',
      _ok and not _bad and len(_neg) == 4, '%d negative: %s' % (len(_neg), ' '.join(sorted(_neg))))

_f = dict(_real)
_f['lcdm_Sm06'] = {'NUHIER': None, 'MNU': 0.0}
_b2, _n2, _o2 = L.carry_verdict(_f)
check('Ⓓ② TOOTH -- give a NEGATIVE node the sum `0.00`, which the OLD gate demanded of every carried '
      'point, and `Ⓛ⓵` turns red and names it. ⛔ *So the repair did not loosen the gate: the exact '
      'state the old clause insisted on is now a refusal, because a point at a sum its tag does not '
      'name is not the point it claims to be*',
      not _o2 and any('lcdm_Sm06' in m for m in _b2), '; '.join(_b2[:2]))

_f3 = dict(_real)
_f3['cr_H0p'] = {'NUHIER': '1', 'MNU': 0.0}
_b3, _n3, _o3 = L.carry_verdict(_f3)
check('Ⓓ③ TOOTH -- turn the switch ON in one carried point and `Ⓛ⓵` turns red: the half of the old '
      'clause that was CORRECT is kept intact',
      not _o3 and any('records the switch ON' in m for m in _b3), '; '.join(_b3[:2]))

_f4 = dict(_real)
_f4.pop('cr_S000')
_b4, _n4, _o4 = L.carry_verdict(_f4)
check('Ⓓ④ TOOTH -- remove a carried point altogether and `Ⓛ⓵` turns red rather than silently '
      'checking one fewer',
      not _o4 and any('cr_S000' in m for m in _b4), '; '.join(_b4[:2]))

_src = io.open(os.path.join(R7884, 'limits_nuhier.py'), encoding='utf-8').read()
_imp, _forb, _ok3 = L.machinery_verdict(_src, 2.71, L.EC.SUMS)
check('Ⓓ⑤ `Ⓛ⓷` PASSES on the module\'s real source -- and the module\'s source CONTAINS the names it '
      'forbids, in the very code that forbids them. ⛔ *That is the whole repair: the old clause '
      'substring-searched its own file and so was false for every file carrying it. The parse tree '
      'cannot be fooled by the question being written down*',
      #: ⛭ the clause `'closed_envelope' in _src` is GONE: it was a bare-identifier read that the
      #:   instrument counts as a TOKEN pin, and `Ⓓ⑥` below already establishes non-vacuity by
      #:   PLANTING a real definition and watching this verdict turn red. The dropped clause proved
      #:   nothing `Ⓓ⑥` does not prove better.
      _ok3 and _imp and not _forb,
      'imports EC %s; forbidden %s' % (_imp, _forb or 'none'))

_ok5 = L.machinery_verdict(_src + '\n\ndef closed_envelope(a, b):\n    return None\n',
                           2.71, L.EC.SUMS)
check('Ⓓ⑥ TOOTH -- actually DEFINE `closed_envelope` in the source and `Ⓛ⓷` turns red, naming it. So '
      'the structural read still catches the thing the substring read was trying to catch',
      not _ok5[2] and 'closed_envelope' in _ok5[1], 'forbidden %s' % (_ok5[1],))

_ok6 = L.machinery_verdict(_src.replace('import envelope_closed as EC',
                                        'import envelope_closed as _EC_OTHER', 1), 2.71, L.EC.SUMS)
check('Ⓓ⑦ TOOTH -- import the file of record under a DIFFERENT name and `Ⓛ⓷` turns red, so the '
      '"imports EC" half is a real requirement and not satisfied by its own wording as before',
      not _ok6[2] and _ok6[0] is False, 'imports EC as EC: %s' % (_ok6[0],))

_ok7 = L.machinery_verdict(_src, 2.71, [0.0, 0.03, 0.06, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50])
_ok8 = L.machinery_verdict(_src, 3.84, L.EC.SUMS)
check('Ⓓ⑧ TOOTH -- drop a sum from the grid, or move the threshold off `2.71`, and `Ⓛ⓷` turns red on '
      'each: the imported machinery is pinned and not merely mentioned',
      not _ok7[2] and not _ok8[2], 'short grid %s, wrong threshold %s' % (_ok7[2], _ok8[2]))

# ---------------------------------------------------------------------------------------------- Ⓔ
print('\nⒺ  THE GRID WAS THE RUNNER\'S, AND THE CROSS-MACHINE CONTROL WAS REPORTED NOT PASSED')

check('Ⓔ① the limit was read on ten re-solved lensing points, all recording the hierarchy on at the '
      'gated grid in their own files',
      REC.get('lensing_provenance', {}).get('checked') == 10
      and not REC.get('lensing_provenance', {}).get('bad'),
      '%s checked, %s bad' % (REC.get('lensing_provenance', {}).get('checked'),
                              len(REC.get('lensing_provenance', {}).get('bad') or [])))

check('Ⓔ② and the record states the agreement with this container\'s own points was `2.121e-09` in '
      'the REGISTERED report state, not zero -- a number a single refuse bar would have passed in '
      'silence',
      'The cross-machine agreement is 2.121e-09, at cr_S015 band 8, in the registered state' in RES)

check('Ⓔ③ and that the two grids were never mixed, so no point\'s machine is left unrecorded',
      'The two were never mixed: filling either from the other would make a grid whose points came '
      'from two machines with nothing recording which came from where' in RES)

# ---------------------------------------------------------------------------------------------- Ⓕ
print('\nⒻ  WHAT IS NOT CLAIMED, WRITTEN DOWN')

check('Ⓕ① ⛔ the record states the limit is NOT joint and names what is outstanding -- one fitter, '
      '`cc66`\'s second fit on the validation legs, which is the order\'s own item ③',
      'The limit is NOT joint. r7882\'s validation stands on one fitter' in RES)

check('Ⓕ② and that a crossing on the minimised column is never a limit, with this revision\'s own '
      'minimised figure given and marked non-monotonic',
      'A crossing on the minimised column is never a limit \u2014 310.148 meV here, non-monotonic '
      'above the minimum' in RES)

check('Ⓕ③ and that the closed envelope is a lower envelope over the basins REACHED and not a proved '
      'global minimum',
      'The closed envelope is a lower envelope over the basins REACHED, not a proved global' in RES)

check('Ⓕ④ and that `193.545` meV is not offered as the control\'s limit of record',
      '193.545 meV is not offered as the control\'s limit of record' in RES)

check('Ⓕ⑤ ⛔ and the record states the ARC-LEVEL negative: the repair `69` named as the candidate for '
      'the exposed compensation is correct on its own terms and moves the limit the wrong way, so '
      'the disagreement is not where either seat put it -- reported, and NOT patched toward the '
      'reference',
      'the limit moved further away again' in RES
      and 'So the candidate 69 named is not the compensation, or is not all of it' in RES)

check('Ⓕ⑥ and the three defects in the landed limit module are recorded with their single cause, '
      'that it was REGISTERED AND UNRUN, and the generalisation stated',
      'registering a gate is not running it. An unrun gate is a claim about a measurement nobody '
      'made' in RES)

print('\n' + '=' * 100)
print('  %d arm(s); %d failed' % (NARMS, len(FAILS)))
for f in FAILS:
    print('    FAILED: %s' % f)
print('=' * 100)
sys.exit(1 if FAILS else 0)
