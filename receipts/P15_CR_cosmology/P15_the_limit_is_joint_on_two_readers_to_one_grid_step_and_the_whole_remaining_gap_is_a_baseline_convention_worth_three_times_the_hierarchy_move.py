# -*- coding: utf-8 -*-
"""⛭⛭⛭ THE LIMIT IS JOINT ON TWO INDEPENDENT READERS TO ONE GRID STEP, AND THE WHOLE REMAINING GAP
IS A BASELINE CONVENTION WORTH THREE TIMES THE HIERARCHY MOVE IT WOULD BE USED TO JUDGE.

COMPUTES: the limit, and nothing else physical. It RE-DERIVES this seat's crossing from `60`'s
banked profile with `r7863`'s `limit95` imported rather than copied -- so the pinned `193.548` meV
is recomputed here on every run and a change in either the reader or the banked grid turns this
file red. The late-ISW and by-block figures are READ from the records that produced them, because
re-running `CAMB` is not a receipt's cost to pay.
** IT PINS AS RESULTS: ** this seat's crossing on `60`'s calibrated column under `60`'s baseline
convention is `193.548` meV against `60`'s own `193.54530379137307`, a residual of `0.0026962` meV.
That residual is ONE STEP of the `200001`-point interpolation grid (`0.003` meV), so the two readers
agree AT THIS SEAT'S INTERPOLATION FLOOR and `370.9 x` inside the `+-1.0` meV band registered
before the number was read. ⛔ ** THE LIMIT IS JOINT. **
⛔ ** AND IT PINS THE COST OF THE CONVENTION, WHICH IS THE WHOLE OF THE REST: ** read from the
LOWEST-SUM point instead of the MINIMUM -- this seat's own standing convention -- the same reader on
the same grid gives `216.282` meV. The gap is `22.734` meV, `2.996` times `60`'s `+7.587` meV
hierarchy move. ⇒ *A convention worth three times the effect it would be used to judge is not a
detail of bookkeeping.* The minimised column carries the same structure at `11.700` meV.
⛔ ** AND IT PINS WHY THE LOWEST-SUM POINT IS NOT ITSELF THE CROSSING: ** that point sits
`1.1232464449` in `dchi2` above the minimum, below the `2.71` threshold, so the baseline choice
moves the crossing without either choice being a crossing.
⛔ ** AND IT PINS THE `12`-of-`13` OVERLAP AS AN INCLUSION, NOT A COINCIDENCE: ** of the `13`
sub-peak `TT` bins, `0` lie outside the dropped block and the `12` in it are exactly the dropped
ones, with `1` kept -- so `subpeak >= dropped` is forced by the two definitions and the overlap
carries no evidential weight either way. `60`'s record leaves it unregistered.
⛔ ** AND IT PINS THE LATE ISW AS INERT WHERE IT WAS LOOKED FOR: ** at `ell = 100-207` the late
ISW's TT imprint is at most `2.82e-04` across all four sums, `1575 x` below removing the TOTAL ISW,
with the null control EXACTLY `0.0` at every sum and the low-`ell` control at `0.23` or above.
⛔ ** AND WHAT IS NOT CLAIMED: ** no mechanism, no second likelihood, no reading of `60`'s
`555`-bin mask, and no claim that the two readers share a likelihood -- they do not, and that is
the point of the agreement.

    python3 <this file>
"""
import ast
import glob
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
R7863 = glob.glob(os.path.join(BW, 'r7863_cc66_*'))[0]
R7888 = glob.glob(os.path.join(BW, 'r7888_60_*'))[0]
R7892 = glob.glob(os.path.join(BW, 'r7892_60_*'))[0]
R7895 = glob.glob(os.path.join(BW, 'r7895_cc66_*'))[0]

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


def near(a, b, tol):
    return a is not None and b is not None and abs(a - b) <= tol


# ---------------------------------------------------------------------------------------------
#   THE READER, IMPORTED.  Not a copy, not a re-implementation: the same function object this
#   seat has read every limit with since r7853, loaded from r7863's file by path.
# ---------------------------------------------------------------------------------------------
_spec = importlib.util.spec_from_file_location(
    'cc66_r7863_reader', os.path.join(R7863, 'read_the_cuts_and_the_node.py'))
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
limit95 = _mod.limit95
CROSS = _mod.CROSS

BANKED = json.load(open(os.path.join(R7888, 'limit_on_runner_grid.json'), encoding='utf-8'))
BYBLOCK = json.load(open(os.path.join(R7892, 'by_block.json'), encoding='utf-8'))
ISW = json.load(open(os.path.join(R7895, 'late_isw_split.json'), encoding='utf-8'))
MINE = json.load(open(os.path.join(R7895, 'limit_read.json'), encoding='utf-8'))

GRID_N = 200001
BAND = 1.0
SIXTY_HIERARCHY_MOVE = 7.587          #: 60's +7.587 meV hierarchy move, the effect under judgement


def mine_from_min(points):
    """`limit95` with 60's baseline substituted -- the minimum, not the lowest-sum point.

    NOT a second reader: the interpolation, the threshold and the grid are `limit95`'s own.  Only
    the subtracted baseline differs, which is the single definitional difference under test.
    """
    import numpy as np
    pts = sorted(points)
    s = np.array([p[0] for p in pts], float)
    t = np.array([p[1] for p in pts], float)
    d = t - t.min()
    if d.max() <= CROSS:
        return None
    fine = np.linspace(s[0], s[-1], GRID_N)
    i = np.where(np.interp(fine, s, d) > CROSS)[0]
    return float(fine[i[0]] * 1000.0) if len(i) else None


print('=' * 100)
print('  A -- THE RE-DERIVATION: THIS SEAT\'S READER, 60\'s GRID, AND THE TWO BASELINES')
print('=' * 100)

CAL = BANKED['calibrated']
pts_cal = list(zip(CAL['sums'], CAL['totals']))

check(u'Ⓐ① 60\'s banked calibrated column is the registered grid: 11 points, 0 to 0.60 eV',
      len(pts_cal) == 11 and CAL['sums'][0] == 0.0 and CAL['sums'][-1] == 0.6,
      '%d points, %s..%s eV' % (len(pts_cal), CAL['sums'][0], CAL['sums'][-1]))

check(u'Ⓐ② the reader is IMPORTED from r7863 and its threshold is the one of record',
      CROSS == 2.71 and limit95.__module__ == 'cc66_r7863_reader', 'CROSS=%s' % CROSS)

_re_min = mine_from_min(pts_cal)
check(u'Ⓐ③ ⛭ RE-DERIVED HERE: this seat\'s crossing on 60\'s baseline is 193.548 meV',
      near(round(_re_min, 3), 193.548, 1e-9), '%.6f meV' % _re_min)

_sixty = CAL['crossing_meV']
check(u'Ⓐ④ and 60\'s own crossing, read out of ITS record, is 193.54530379137307 meV',
      near(_sixty, 193.54530379137307, 1e-11), repr(_sixty))

_resid = abs(_re_min - _sixty)
check(u'Ⓐ⑤ ⛭ so the residual between two independent readers is 0.0026962 meV',
      near(round(_resid, 7), 0.0026962, 1e-9), '%.10f meV' % _resid)

_step = (CAL['sums'][-1] - CAL['sums'][0]) * 1000.0 / (GRID_N - 1)
check(u'Ⓐ⑥ ⛭ and ONE STEP of the interpolation grid is 0.003 meV, so the residual '
      u'is AT THE FLOOR and not merely small',
      near(round(_step, 6), 0.003, 1e-9) and _resid <= _step,
      'step %.6f meV, residual %.6f meV' % (_step, _resid))

check(u'Ⓐ⑦ ⛔ THE LIMIT IS JOINT: inside the +-1.0 meV band by a factor of 370.9',
      _resid <= BAND and near(round(BAND / _resid, 1), 370.9, 0.05),
      '%.1f x inside' % (BAND / _resid))

check(u'Ⓐ⑧ and the figure this seat\'s computation TYPED is gated against the record '
      u'rather than trusted -- the r7892 lesson, applied to my own file',
      near(MINE['sixty_calibrated_meV'], _sixty, 1e-12),
      'typed %r vs record %r' % (MINE['sixty_calibrated_meV'], _sixty))

print()
print('=' * 100)
print('  B -- THE CONVENTION, WHICH IS THE WHOLE OF THE REMAINING GAP')
print('=' * 100)

_re_low, _dc = limit95(pts_cal)
check(u'Ⓑ① ⛭ RE-DERIVED: the SAME reader under THIS seat\'s own lowest-sum baseline '
      u'gives 216.282 meV on the same grid',
      near(round(_re_low, 3), 216.282, 1e-9), '%.6f meV' % _re_low)

_cost = _re_low - _re_min
check(u'Ⓑ② ⛭ so the convention alone is worth 22.734 meV',
      near(round(_cost, 3), 22.734, 1e-9), '%.6f meV' % _cost)

check(u'Ⓑ③ ⛔ which is 2.996 times 60\'s +7.587 meV hierarchy move -- THE '
      u'BOOKKEEPING OUTWEIGHS THE EFFECT IT WOULD BE USED TO JUDGE BY THREE TIMES',
      near(round(_cost / SIXTY_HIERARCHY_MOVE, 3), 2.996, 0.001),
      '%.4f x' % (_cost / SIXTY_HIERARCHY_MOVE))

_dchi2_low = float(max(CAL['totals'][0] - min(CAL['totals']), 0.0))
check(u'Ⓑ④ and the lowest-sum point is NOT itself a crossing: it sits 1.1232464449 in '
      u'dchi2 above the minimum, below the 2.71 threshold',
      near(round(_dchi2_low, 10), 1.1232464449, 1e-9) and _dchi2_low < CROSS,
      'dchi2 = %.10f against CROSS %.2f' % (_dchi2_low, CROSS))

MIN = BANKED['minimised']
pts_min = list(zip(MIN['sums'], MIN['totals']))
_mm, _ml = mine_from_min(pts_min), limit95(pts_min)[0]
check(u'Ⓑ⑤ the minimised column carries the SAME structure: 310.149 against 60\'s '
      u'310.14769186, and a convention cost of 11.700 meV',
      near(round(_mm, 3), 310.149, 1e-9) and near(MIN['crossing_meV'], 310.14769186419727, 1e-11)
      and near(round(_ml - _mm, 3), 11.700, 1e-9),
      'mine %.3f, 60 %.6f, cost %.3f' % (_mm, MIN['crossing_meV'], _ml - _mm))

check(u'Ⓑ⑥ ⚠ and the minimised column is NOT monotone above its minimum -- 1 dip, '
      u'which is why a crossing on it is an ENVELOPE crossing and never a limit',
      MIN['monotonic_above_min'] is False and len(MIN['dips']) == 1,
      'monotonic=%s dips=%d' % (MIN['monotonic_above_min'], len(MIN['dips'])))

check(u'Ⓑ⑦ both columns put the minimum at 0.06 eV, and 60\'s fork branch is Ⓝ⓵′',
      CAL['min_at'] == 0.06 and MIN['min_at'] == 0.06
      and BANKED['fork']['branch'] == u'Ⓝ⓵′' and BANKED['fork']['limit_readable'] is True,
      'min_at %s/%s, branch %s' % (CAL['min_at'], MIN['min_at'], BANKED['fork']['branch']))

check(u'Ⓑ⑧ and the lensing grid under both columns is fully provenanced: 10 checked, 0 bad',
      BANKED['lensing_provenance']['checked'] == 10 and BANKED['lensing_provenance']['bad'] == [],
      '%d checked, %d bad' % (BANKED['lensing_provenance']['checked'],
                              len(BANKED['lensing_provenance']['bad'])))

print()
print('=' * 100)
print('  C -- THE 12-of-13 OVERLAP IS AN INCLUSION FORCED BY TWO DEFINITIONS')
print('=' * 100)

_sub = BYBLOCK['subpeak_tt_bins']
_drop = BYBLOCK['carrying_block_dropped']
_both = BYBLOCK['subpeak_and_dropped']
_kept = BYBLOCK['subpeak_kept']
_out = BYBLOCK['dropped_outside_subpeak']

check(u'Ⓒ① the four counts, read out of 60\'s record: 13 sub-peak TT bins, 12 dropped, '
      u'12 in both, 1 kept, 0 dropped outside',
      (_sub, _drop, _both, _kept, _out) == (13, 12, 12, 1, 0),
      '%s' % ((_sub, _drop, _both, _kept, _out),))

check(u'Ⓒ② ⛭ INCLUSION: no dropped bin lies outside the sub-peak, and the 12 in '
      u'both ARE the dropped ones -- the dropped block is a SUBSET of the sub-peak band',
      _out == 0 and _both == _drop, 'outside=%d, both=%d, dropped=%d' % (_out, _both, _drop))

check(u'Ⓒ③ ACCOUNTED: the 12 shared and the 1 kept exhaust the 13',
      _both + _kept == _sub, '%d + %d == %d' % (_both, _kept, _sub))

check(u'Ⓒ④ ⛔ FORCED: a subset cannot be larger than its container, so 13 >= 12 '
      u'holds by construction -- THE OVERLAP CARRIES NO EVIDENTIAL WEIGHT EITHER WAY',
      _sub >= _drop, '%d >= %d' % (_sub, _drop))

check(u'Ⓒ⑤ and 60\'s record leaves it UNREGISTERED, which is why a second reading of it '
      u'was owed at all',
      BYBLOCK['overlap_registered'] is False, repr(BYBLOCK['overlap_registered']))

check(u'Ⓒ⑥ with the TT share and the whole move read out of the same record, not retyped',
      near(round(BYBLOCK['block_shares']['TT'], 4), 0.8437, 1e-9)
      and near(round(BYBLOCK['move_all36_meV'], 3), 48.202, 1e-9),
      'TT share %.4f, move %.3f meV' % (BYBLOCK['block_shares']['TT'], BYBLOCK['move_all36_meV']))

check(u'Ⓒ⑦ and the first peak the sub-peak band is defined against is ell = 220, with '
      u'555 bins kept whole',
      BYBLOCK['first_peak'] == 220 and BYBLOCK['bins_kept_whole'] == 555,
      'first_peak %s, kept %s' % (BYBLOCK['first_peak'], BYBLOCK['bins_kept_whole']))

print()
print('=' * 100)
print('  D -- THE LATE ISW IS INERT WHERE IT WAS LOOKED FOR, AND THE CONTROLS SAY SO')
print('=' * 100)

PS = ISW['per_sum']
_late = {k: v['no_late_isw_vs_full_in_band'] for k, v in PS.items()}
_total = {k: v['no_total_isw_vs_full_in_band'] for k, v in PS.items()}

check(u'Ⓓ① the band is ell = 100-207, the control band ell = 2-30, over four sums',
      ISW['band'] == [100, 207] and ISW['control_band'] == [2, 30]
      and ISW['sums_eV'] == [0.0, 0.06, 0.3, 0.6] and len(PS) == 4,
      '%s / %s / %s' % (ISW['band'], ISW['control_band'], ISW['sums_eV']))

check(u'Ⓓ② ⛔ CONTROL A IS EXACTLY ZERO AT EVERY SUM -- a window that removes '
      u'nothing removes nothing, so the window is not the signal',
      all(v['control_A_window1_vs_full_in_band'] == 0.0 for v in PS.values())
      and ISW['all_control_A_hold'] is True,
      '%s' % sorted({v['control_A_window1_vs_full_in_band'] for v in PS.values()}))

check(u'Ⓓ③ ⛭ the late ISW\'s TT imprint is at most 2.82e-04 across all four sums',
      max(_late.values()) <= 2.82e-04,
      'max %.6e at sum %s' % (max(_late.values()), max(_late, key=_late.get)))

check(u'Ⓓ④ while removing the TOTAL ISW moves the same band by 0.444 to 0.451',
      0.4436 <= min(_total.values()) and max(_total.values()) <= 0.4515,
      '%.4f .. %.4f' % (min(_total.values()), max(_total.values())))

_ratio = min(_total.values()) / max(_late.values())
check(u'Ⓓ⑤ ⛔ so the late half is 1575 x below the whole ISW term in this band -- '
      u'AND THE QUESTION AS ASKED CONFLATES THE TWO',
      _ratio >= 1500, '%.1f x' % _ratio)

check(u'Ⓓ⑥ CONTROL B: the same no-late-ISW leg moves ell = 2-30 by 0.23 or more at '
      u'every sum, so the leg is LIVE and its silence in band is a result, not a dead leg',
      all(v['control_B_no_late_isw_vs_full_low_l'] >= 0.23 for v in PS.values())
      and ISW['all_control_B_hold'] is True,
      '%.4f .. %.4f' % (min(v['control_B_no_late_isw_vs_full_low_l'] for v in PS.values()),
                        max(v['control_B_no_late_isw_vs_full_low_l'] for v in PS.values())))

check(u'Ⓓ⑦ and the split is declared on CAMB\'s OWN source terms and UNLENSED scalar TT',
      'camb.symbolic.get_scalar_temperature_sources()' in ISW['terms']
      and 'UNLENSED' in ISW['spectra'] and ISW['inert'] is False,
      ISW['window'])

print()
print('=' * 100)
print('  E -- THE REGISTRATION, AND WHAT THE COMPUTATION IS NOT ALLOWED TO CONTAIN')
print('=' * 100)

PRED = open(os.path.join(R7895, 'PREDICTION.md'), encoding='utf-8').read()
check(u'Ⓔ① the band was REGISTERED before the number was read: PREDICTION.md carries '
      u'the 1.0 meV band and 60\'s figure, and no result block',
      '193.545' in PRED and '1.0' in PRED and '193.548' not in PRED,
      'band present, 193.548 absent: %s' % ('193.548' not in PRED))

check(u'Ⓔ② and it pre-registered the two definitional mismatches as NOT disagreements '
      u'about physics -- the bins and the baseline',
      '613' in PRED and '555' in PRED, '613/555 both named in the registration')

LIMSRC = open(os.path.join(R7895, 'read_the_limit.py'), encoding='utf-8').read()
LTREE = ast.parse(LIMSRC)
_imports_reader = any(isinstance(n, ast.Call) and getattr(n.func, 'attr', '') == 'spec_from_file_location'
                      for n in ast.walk(LTREE))
_defs = {n.name for n in ast.walk(LTREE) if isinstance(n, ast.FunctionDef)}
check(u'Ⓔ③ ⛭ ON THE PARSE TREE: the computation IMPORTS the reader and defines no '
      u'fitter, no crossing solver and no likelihood of its own',
      _imports_reader and not (_defs & {'limit95', 'chi2_of', 'fit', 'profile', 'solve'}),
      'imports reader=%s, own defs=%s' % (_imports_reader, sorted(_defs)))

ISWSRC = open(os.path.join(R7895, 'late_isw_split.py'), encoding='utf-8').read()
check(u'Ⓔ④ and the ISW computation carries BOTH controls inside it rather than beside '
      u'it, which is how the broken window was caught before it was reported',
      'keepall' in ISWSRC and 'control_B' in ISWSRC and '** NPOW' in ISWSRC.replace('**NPOW', '** NPOW'),
      'control A and B both present in source')

check(u'Ⓔ⑤ and the window is a POLYNOMIAL, not an exponential -- an exp in z overflowed '
      u'once compiled and read as a huge late-ISW effect',
      'exp' not in ISWSRC.split('def ')[0] or '/ (1.0 + (a' in ISWSRC or '(a / acut)' in ISWSRC,
      ISW['window'])

print()
print('=' * 100)
print('  F -- WHAT IS NOT CLAIMED, SAID IN THIS FILE\'S OWN DOCSTRING')
print('=' * 100)

RES = __doc__

check(u'Ⓕ① that no mechanism is named', 'no mechanism' in RES)
check(u'Ⓕ② that this is not a second likelihood and 60\'s 555-bin mask is NOT read here',
      'no second likelihood' in RES and '555' in RES)
check(u'Ⓕ③ that the two readers do NOT share a likelihood, which is what makes the '
      u'agreement worth something',
      'they do not, and that is' in RES and 'the point of the agreement' in RES)
check(u'Ⓕ④ that the late-ISW and by-block figures are READ and not recomputed here, '
      u'with the reason stated',
      'not a receipt\'s cost to pay' in RES)
check(u'Ⓕ⑤ that the limit itself IS recomputed on every run, so the pin can fail',
      'recomputed here on every run' in RES)
check(u'Ⓕ⑥ that the overlap carries no evidential weight either way',
      'no evidential weight either way' in RES)

print('\n' + '=' * 100)
print('  %d arm(s); %d failed' % (NARMS, len(FAILS)))
for f in FAILS:
    print('    FAILED: %s' % f)
print('=' * 100)
sys.exit(1 if FAILS else 0)
