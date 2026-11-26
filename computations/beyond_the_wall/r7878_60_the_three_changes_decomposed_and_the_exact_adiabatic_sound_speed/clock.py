#!/usr/bin/env python3
"""r7878+60 — ** WHICH CLOCK THE EXACT SOUND SPEED'S DERIVATIVE IS TAKEN ON. **

The guard: *when two descriptions differ, first ask whether the difference survives a change of
clock.*  Applied to this revision's own new term rather than to someone else's claim.

`c_a^2 = w - w-dot/(3 H (1+w))` is clock-INDEPENDENT when the two factors share a clock, because
`d w/d eta = Hc * d w/d ln a` exactly:

    w-dot/(3 H (1+w))  =  (d w/d ln a)/(3 (1+w))        <-- the standard, clock-free form

In the instrument, `Wdot_of` is `d/d eta` on the GRID's conformal time, and the grid is built on
`Hgeom`; but the perturbation right-hand side reads `Hc = Hl_of(e)` when `LEAFPERT` is on, which it
is by default.  So what the code computes is

    w - Jac(e) * (d w/d ln a)/(3 (1+w))      with  Jac = Hgeom/Hleaf

⇒ exact where `Jac == 1`, and off by exactly that factor where it is not.  This script MEASURES
`Jac` on both arms with the legs' own environment, rather than reasoning about it.  It
reimplements nothing: it executes the instrument's own prelude, as `r7876`'s `closure.py` does.
"""
import io
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)
SRC = os.path.join(BW, 'ACOUSTIC_two_arm.py')
_CUT = 645                                   # the `D_M = eta_0 - eta_rec` line, as r7876 pinned it

LC = dict(LH0='67.40', LOM='0.3150', WBH2='0.0224', NS='0.965')   # the control's environment


def prelude(arm, mnu):
    with io.open(SRC, encoding='utf-8') as fh:
        head = ''.join(fh.readlines()[:_CUT])
    keep = dict(os.environ)
    os.environ.update(LC)
    os.environ.update(ARM=arm, MNU=str(mnu), NUFD='1', BVEL='1', HIER='1',
                      NUPERT='1', NUPARTS='WCE', NUCA='1')
    ns = {'__name__': '_prelude', '__file__': SRC}
    try:
        sys.path.insert(0, BW)
        exec(compile(head, SRC, 'exec'), ns)
    finally:
        sys.path.pop(0)
        os.environ.clear()
        os.environ.update(keep)
    return ns


def window(ns):
    """+-3 FWHM of the visibility, in grid conformal time -- the stretch that makes the spectrum"""
    e = np.asarray(ns['eg'], dtype=float)
    g = np.asarray(ns['gvis_of'](e), dtype=float) if 'gvis_of' in ns else None
    if g is None or not np.isfinite(g).any() or g.max() <= 0:
        er = float(ns['eta_rec'])
        return e[(e > 0.6 * er) & (e < 1.8 * er)]
    half = g.max() / 2.0
    hit = e[g >= half]
    fwhm = float(hit[-1] - hit[0]) if len(hit) > 1 else 0.1 * float(ns['eta_rec'])
    c = float(e[int(np.argmax(g))])
    return e[(e >= c - 3 * fwhm) & (e <= c + 3 * fwhm)]


REC = {}
for arm in ('lcdm', 'cr'):
    ns = prelude(arm, 0.30)
    e = window(ns)
    #: ⌘ *and the claim "this revision's numbers are unaffected" is about the WHOLE integration
    #:   range, not only the visibility, so the rate sources are compared on every grid point too.*
    _eg = np.asarray(ns['eg'], dtype=float)
    _hlf, _hcf = (np.asarray(ns['Hl_of'](_eg), dtype=float),
                  np.asarray(ns['Hc_of'](_eg), dtype=float))
    REC[arm + '_full_grid'] = {
        'n': int(len(_eg)),
        'worst_abs_rate_difference': float(np.abs(_hcf - _hlf).max()),
        'bit_identical_everywhere': bool(np.abs(_hcf - _hlf).max() == 0.0),
    }
    #: ⌘ *and OFF the knots too, because the integrator asks for `e` wherever its step lands:
    #:   the two splines are compared at 200001 points spread across the window, and the ORDINATE
    #:   ARRAYS the two splines are built from are compared directly -- identical ordinates on an
    #:   identical abscissa give identical coefficients, hence identical values everywhere.*
    _off = np.linspace(float(e[0]), float(e[-1]), 200001)
    _ag = np.asarray(ns['ag'], dtype=float)
    _ordinate_g = _ag * ns['Hgeom'](_ag) / ns['C']
    _ordinate_l = _ag * ns['Hleaf'](_ag) / ns['C']
    REC[arm + '_off_knot'] = {
        'n': int(len(_off)),
        'worst_abs_rate_difference': float(np.abs(np.asarray(ns['Hc_of'](_off), dtype=float)
                                                  - np.asarray(ns['Hl_of'](_off),
                                                               dtype=float)).max()),
        'ordinates_bit_identical': bool(np.array_equal(_ordinate_g, _ordinate_l)),
    }
    REC[arm + '_off_knot']['bit_identical_off_knot'] = bool(
        REC[arm + '_off_knot']['worst_abs_rate_difference'] == 0.0)
    print('  %-5s  off knot: %d point(s), worst |Hc - Hl| = %.3e, spline ordinates identical: %s'
          % (arm, REC[arm + '_off_knot']['n'],
             REC[arm + '_off_knot']['worst_abs_rate_difference'],
             REC[arm + '_off_knot']['ordinates_bit_identical']))
    print('  %-5s  full grid: %d point(s), worst |Hc - Hl| = %.3e, bit-identical everywhere: %s'
          % (arm, REC[arm + '_full_grid']['n'],
             REC[arm + '_full_grid']['worst_abs_rate_difference'],
             REC[arm + '_full_grid']['bit_identical_everywhere']))
    jac = np.asarray(ns['Jac_of'](e), dtype=float)
    hl = np.asarray(ns['Hl_of'](e), dtype=float)
    hc = np.asarray(ns['Hc_of'](e), dtype=float)
    #: the factor the code actually applies to the clock-free form, measured two ways
    direct = hc / hl
    REC[arm] = {
        'rad_in_rate': bool(ns['RAD_IN_RATE']),
        'leafpert': bool(ns['LEAFPERT']),
        'leafgeom': bool(ns['LEAFGEOM']),
        'n': int(len(e)),
        'jac_min': float(jac.min()), 'jac_max': float(jac.max()),
        'worst_dev': float(np.abs(jac - 1.0).max()),
        'jac_equals_hc_over_hl': float(np.abs(jac - direct).max()),
        'identical_rate_source': bool(np.abs(hc - hl).max() == 0.0),
    }
    print('  %-5s  RAD_IN_RATE=%-5s  Jac in [%.6f, %.6f]  worst |Jac-1| = %.3e  on %d point(s)'
          % (arm, REC[arm]['rad_in_rate'], REC[arm]['jac_min'], REC[arm]['jac_max'],
             REC[arm]['worst_dev'], REC[arm]['n']))

print('\n  ⇒ the term the code applies is  Jac * (dw/dln a)/(3(1+w)),  so:')
for arm in ('lcdm', 'cr'):
    r = REC[arm]
    print('     %-5s %s' % (arm, 'EXACT -- the two rate expressions are the same object here, so '
                                 'the clock cancels and every number of this revision stands'
                            if r['worst_dev'] == 0.0 else
                            'OFF by up to %.1f per cent of the correction term'
                            % (100 * r['worst_dev'])))
REC['legs_were_run_on'] = 'lcdm'
REC['numbers_affected'] = bool(REC['lcdm']['worst_dev'] != 0.0)
print('\n  ⇒ the eight-plus-two legs of this revision were all run on `lcdm`, so the revision\'s '
      'own numbers are %s' % ('** AFFECTED **' if REC['numbers_affected'] else 'UNAFFECTED'))
json.dump(REC, io.open(os.path.join(HERE, 'clock.json'), 'w', encoding='utf-8'),
          indent=1, sort_keys=True)
print('  wrote clock.json')
