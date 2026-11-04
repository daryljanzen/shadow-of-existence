#!/usr/bin/env python3
"""`r7677` (cc66) ITEM 2 -- `CR_PK` RE-DERIVED ON THE ARM OF RECORD.

** THE ORDER (`r7677`, 69) item 2: ** "Re-derive each on the arm of record, or read it from a bank."

`CR_PK = np.array([221.8, 536.8, 812.9, 1126.5])` in
`P15_the_skys_own_fourth_peak_cannot_tell_the_arms_apart...` is `cc66.28`'s NAMESAKE peak quartet,
and ⛔ ** that receipt loads NO SPECTRA AT ALL: ** the quartet is its input, not its measurement.  So
there is nothing to repoint -- the re-derivation has to run the receipt's own locator on the
arm-of-record bank, which is what this file does.

⛭⛭ ** THE LOCATOR IS NOT COPIED, IT IS LIFTED FROM THE RECEIPT'S OWN SOURCE BY `ast`. **  A copied
locator is the drift `r7667/sentence.py`'s header is about, and here it would be worse than drift:
the whole question is whether the arm-of-record quartet is what THIS locator returns, so a locator
that differs from the receipt's by one line measures something else.  Gate ⓪ asserts the lift.

⛔ ** AND THE NAMESAKE SIDE HAD TO BE REPRODUCED FIRST, WHICH IS WHERE THIS STOPPED. **  If the
lifted locator does not return `cc66.28`'s own quartet off some banked spectrum, then nothing this
file computes is `cc66.28`'s quantity and an arm-of-record number would be a different measurement
wearing its name.

*** THE RESULT: NO BANKED SPECTRUM IN THE TREE REPRODUCES EITHER QUARTET.  Across every `.npz`
under `computations/beyond_the_wall/`, the closest approach to the arm's quartet is 0.86 multipoles
-- and it is `cr_NSp`, a TILT-PERTURBED grid leg rather than any base spectrum -- while the
control's quartet is not approached at all.  ⇒ `CR_PK` and `LCDM_PK` are hardcoded constants whose
PROVENANCE CANNOT BE RECOVERED FROM THE TREE, so they cannot be re-derived on the arm of record by
this route, and what they carry into print at `l.2790` rests on an unreproducible namesake input. ***

⛭ *That is a better answer than a number would have been, and it is the answer gate ① was written
to force: the arm-of-record quartet off `cc66_r185_verify_cr_leafrec1` is computed below and
reported as NOT cc66.28's quantity, rather than offered as a replacement for its constants.*
"""
import ast
import glob
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

RCPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                    'P15_the_skys_own_fourth_peak_cannot_tell_the_arms_apart_and_the_displacement'
                    '_is_shared_with_the_control.py')

fail = []


def check(label, ok, got=None):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}" + (f"   ({got})" if got is not None else ""))
    if not ok:
        fail.append(label)


def head(t):
    print('\n' + '=' * 100)
    print('  ' + t)
    print('=' * 100 + '\n')


# ══ ⓪ THE LOCATOR, LIFTED ════════════════════════════════════════════════════════════════════════
head('⓪ THE LOCATOR AND THE CONSTANTS, LIFTED FROM THE RECEIPT RATHER THAN COPIED')
_src = open(RCPT, encoding='utf-8').read()
_tree = ast.parse(_src)
_WANT_FN = {'spline_of', 'find_free'}
_WANT_NAME = {'WS', 'LF', 'CR_PK', 'LCDM_PK'}
_fns = [n for n in _tree.body if isinstance(n, ast.FunctionDef) and n.name in _WANT_FN]
_names = [n for n in _tree.body
          if isinstance(n, ast.Assign) and len(n.targets) == 1
          and isinstance(n.targets[0], ast.Name) and n.targets[0].id in _WANT_NAME]
NS = {'np': np, 'CS': CS}
NS['LC'], NS['FACB'] = CS.bin_center_and_fac()
from scipy.interpolate import CubicSpline                                  # noqa: E402
from scipy.signal import argrelextrema                                     # noqa: E402
NS['CubicSpline'], NS['argrelextrema'] = CubicSpline, argrelextrema
exec(compile(ast.Module(body=_names + _fns, type_ignores=[]), RCPT, 'exec'), NS)
check('⓪ the locator, its window sweep and both hardcoded quartets are LIFTED from the '
      "receipt's own source by `ast` -- not copied, because the question is what THIS locator "
      'returns and a locator differing by one line answers a different one',
      {n.name for n in _fns} == _WANT_FN
      and {n.targets[0].id for n in _names} == _WANT_NAME,
      f"lifted {sorted({n.name for n in _fns})} and {sorted({n.targets[0].id for n in _names})}")
find_free, LF, WS = NS['find_free'], NS['LF'], NS['WS']
CR_PK, LCDM_PK = NS['CR_PK'], NS['LCDM_PK']
LC, FACB = NS['LC'], NS['FACB']
print(f'      cc66.28 CR_PK   : {" ".join(f"{v:8.1f}" for v in CR_PK)}')
print(f'      cc66.28 LCDM_PK : {" ".join(f"{v:8.1f}" for v in LCDM_PK)}')


def quartet_path(path):
    """the receipt's own locator, window-swept, on any banked spectrum binned the likelihood's way.

    None when the file carries no `ls`/`Dl` pair, or the locator does not find four peaks on every
    one of the seven windows -- which is the same completeness the receipt itself requires.
    """
    try:
        z = np.load(path, allow_pickle=True)
        if 'ls' not in z.files or 'Dl' not in z.files:
            return None
        Db = CS.bin_spectrum(np.asarray(z['ls'], float), np.asarray(z['Dl'], float)) * FACB
        sw = [find_free(Db, W) for W in WS]
        sw = np.array([q for q in sw if len(q) == 4])
        return sw.mean(0) if len(sw) == len(WS) else None
    except Exception:
        return None


def quartet(stem):
    """`quartet_path` on a `spectra/` stem, with the spread and the window count beside it."""
    z = np.load(os.path.join(SP, stem + '.npz'))
    Db = CS.bin_spectrum(z['ls'].astype(float), np.asarray(z['Dl'], float)) * FACB
    sw = np.array([q for q in (find_free(Db, W) for W in WS) if len(q) == 4])
    return sw.mean(0), sw.std(0), len(sw)


# ══ ① THE NAMESAKE SIDE DOES NOT REPRODUCE, AND THE WHOLE TREE IS SEARCHED BEFORE SAYING SO ══════
head('① THE NAMESAKE BANKS DO NOT REPRODUCE cc66.28 -- and the search is over the WHOLE TREE')
NM = {t: quartet(f'cc66_r185_verify_{t}') for t in ('lcdm', 'cr')}
for t in ('lcdm', 'cr'):
    m, sd, n = NM[t]
    print(f'      cc66_r185_verify_{t:16s} {" ".join(f"{v:8.1f}" for v in m)}   (spread '
          f'{" ".join(f"{v:5.2f}" for v in sd)}, {n} of {len(WS)} windows)')
_d_cr = np.abs(NM['cr'][0] - CR_PK)
_d_ct = np.abs(NM['lcdm'][0] - LCDM_PK)
print(f'      |difference from cc66.28|   arm {" ".join(f"{v:5.2f}" for v in _d_cr)}')
print(f'                              control {" ".join(f"{v:5.2f}" for v in _d_ct)}')
#: ⛔⛭⛭⛭ AND BEFORE CALLING A CONSTANT UNREPRODUCIBLE, EVERY BANK IN THE TREE IS TRIED.  * The
#:   obvious bank failing is not evidence that no bank works, and `r7667+cc66.2`'s lesson is that
#:   this tree carries the same basename in several directories.  So the locator is run on every
#:   `.npz` under `beyond_the_wall/` that carries an `ls`/`Dl` pair and locates four peaks on all
#:   seven windows, and the closest approach to each quartet is reported. *
_ALL = sorted(glob.glob(os.path.join(ROOT, 'computations', 'beyond_the_wall', '**', '*.npz'),
                        recursive=True))
_near = {'cr': (1e9, None, None), 'lcdm': (1e9, None, None)}
_tried = 0
for _p in _ALL:
    _q = quartet_path(_p)
    if _q is None:
        continue
    _tried += 1
    for _nm, _tgt in (('cr', CR_PK), ('lcdm', LCDM_PK)):
        _d = float(np.abs(_q - _tgt).max())
        if _d < _near[_nm][0]:
            _near[_nm] = (_d, os.path.relpath(_p, ROOT), _q)
print(f'\n      `.npz` files under beyond_the_wall/: {len(_ALL)};  on which this locator finds four '
      f'peaks on all seven windows: {_tried}')
for _nm, _lbl in (('cr', 'CR_PK  '), ('lcdm', 'LCDM_PK')):
    _d, _f, _q = _near[_nm]
    print(f'      closest to {_lbl}: {_d:6.2f} multipoles   {_f}')
    print(f'                        {" ".join(f"{v:8.1f}" for v in _q)}')
check('① ⛔⛭⛭ ** NO BANKED SPECTRUM IN THE TREE REPRODUCES EITHER QUARTET. **  The '
      f'locator is run on all {_tried} spectra under `beyond_the_wall/` that it can locate four '
      f'peaks on, and the closest approach is {_near["cr"][0]:.2f} multipoles to the arm\'s quartet '
      f'and {_near["lcdm"][0]:.2f} to the control\'s -- both an order of magnitude outside the tenth '
      'of a multipole the constants are quoted to.  ⇒ `CR_PK` and `LCDM_PK` are hardcoded '
      'constants whose PROVENANCE CANNOT BE RECOVERED FROM THE TREE, so they cannot be re-derived '
      'on the arm of record by this route.  *The obvious bank failing would not have been evidence '
      f'of this; {_tried} of {len(_ALL)} failing is*',
      _tried > 200 and _near['cr'][0] > 0.5 and _near['lcdm'][0] > 0.5,
      f'{_tried} spectra tried; nearest {_near["cr"][0]:.2f} (arm) and '
      f'{_near["lcdm"][0]:.2f} (control) multipoles')

# ══ ② WHAT THE ARM-OF-RECORD BANK DOES GIVE, REPORTED AS NOT cc66.28's QUANTITY ══════════════════
head('② THE ARM-OF-RECORD BANK\'s OWN QUARTET -- reported, and NOT offered as a replacement')
AOR, AOR_SD, _n = quartet('cc66_r185_verify_cr_leafrec1')
print(f'      cc66_r185_verify_cr_leafrec1  {" ".join(f"{v:8.1f}" for v in AOR)}   (spread '
      f'{" ".join(f"{v:5.2f}" for v in AOR_SD)}, {_n} of {len(WS)} windows)')
print(f'      its namesake sibling          {" ".join(f"{v:8.1f}" for v in NM["cr"][0])}')
print(f'      the move LEAFREC makes on it  '
      f'{" ".join(f"{v:+8.2f}" for v in AOR - NM["cr"][0])}')
print(f'      cc66.28\'s hardcoded CR_PK     {" ".join(f"{v:8.1f}" for v in CR_PK)}  '
      f'<- a DIFFERENT quantity, per ①')
check('② the `_leafrec1` bank\'s quartet is measured through the same lifted locator and the move '
      'LEAFREC makes on THAT bank is reported -- but it is NOT offered as the arm-of-record value '
      "of `CR_PK`, because ① establishes they are not the same quantity.  ⛔ *Substituting it "
      'would be the `r7645+cc66.68` error in a new place: a number that is internally consistent '
      'and silently answers a different question*',
      _n == len(WS) and float(np.abs(AOR - NM['cr'][0]).max()) > 0.05,
      'LEAFREC moves this bank by up to '
      f'{float(np.abs(AOR - NM["cr"][0]).max()):.2f} multipoles')
#: ⛭ WHAT IS AT STAKE IN PRINT, so 69 can price the gap: `l.2790` says the fourth peak sits 1.4 of
#:   the sky's own locating spreads high with two thirds of that offset shared with the control.
#:   Both halves are built from `CR_PK[3]` and `LCDM_PK[3]`, so both rest on the input ① cannot
#:   reproduce.  *Stated rather than recomputed: a recomputation would need the quantity itself.*
print(f'\n      `l.2790` is built from CR_PK[3] = {CR_PK[3]} and LCDM_PK[3] = {LCDM_PK[3]}:')
print(f'        their difference, the shared-offset numerator: {CR_PK[3] - LCDM_PK[3]:+.1f} '
      f'multipoles')
check('②ᵃ what rests on these constants in print is NAMED rather than left to be found: '
      '`l.2790`\'s "the fourth peak sits 1.4 of the sky\'s own locating spreads high, two thirds of '
      'that offset shared with the control" is built from `CR_PK[3]` and `LCDM_PK[3]`, so BOTH '
      'halves rest on an input no bank in the tree reproduces',
      abs(float(CR_PK[3] - LCDM_PK[3]) - 2.0) < 0.05,
      f'CR_PK[3] - LCDM_PK[3] = {CR_PK[3] - LCDM_PK[3]:+.1f}')

print('\n' + '=' * 100)
if fail:
    print('  FAILED:')
    for f in fail:
        print(f'    - {f}')
    sys.exit(1)
print('  \u2713 ALL CHECKS PASSED')
print('=' * 100)
