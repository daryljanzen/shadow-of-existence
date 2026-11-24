# -*- coding: utf-8 -*-
"""Ⓒ③ AND Ⓓ④ -- BOTH LIMITS RE-READ ON THE REPAIRED BACKGROUND, AND THE SECOND BASIN.

⛭ `r7863` (69) items ③ and ④.

⚠ ** WHAT THIS CAN AND CANNOT READ, STATED FIRST BECAUSE IT BOUNDS EVERY NUMBER BELOW. **  *The
banked CMB and lensing grids were SOLVED on the old background.  Item ① repairs the background, so a
fully consistent re-read needs the bank re-solved -- about `35` minutes per CMB point on four cores
and `32` points, which is not this revision's to spend without being asked.*  ⇒ ** So what is read
here is the BANKED SPECTRA WITH THE RULER REPAIRED, and that is said beside every figure. **
  ⌗ *And item ② just made the mismatch CHECKABLE instead of assertable: the resolved config now
  carries the switch, so a bank taken after the repair would SAY so.  The precondition below reads
  the bank's own config and gates that the key is ABSENT -- which is the proof that these spectra
  predate the repair, and is a different statement from "the switch was off", exactly as this
  instrument's own `COMBRHO` note says.*

    python3 limits.py
"""
import io
import json
import os
import sys

import numpy as np
from scipy.interpolate import RegularGridInterpolator
from scipy.optimize import minimize

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
ROOT = os.path.dirname(os.path.dirname(_BTW))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT
BANK = os.path.join(_BTW, 'bank')
R7862 = os.path.join(_BTW, 'r7862_60_the_calibrated_case_on_the_references_terms_and_the_damping_'
                           'tails_share_of_the_gap')
LANDED_BLOB = '291f4477c37ed7fbb13dea2f32ca1744f1ed4d68'
REF_RULER, REF_CALIB = 54.00, 30.56
R7862_CALIB_ON_REF = 89.91          # what the calibrated case read on the reference's ruler
R7862_CALIB_ON_INST = 78.33         # and on the instrument's own, before the repair
R7862_MINIMISED = 69.97
DCHI2 = 2.71
EXPECT_WITHIN = 4.0                 # ⛭ registered: within 4 meV of 89.91

os.environ['POL_DIR'] = os.path.join(BANK, 'pol_grid_bvel1')
os.environ['PPGRID'] = os.path.join(BANK, 'phiphi_grid_eta4000_bvel1_primnorm1')
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '4')
sys.path.insert(0, os.path.join(_BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_'
                                      'lensing_bandpowers'))
sys.path.insert(0, os.path.join(_BTW, 'r7842_60_polarisation_added_to_the_score_and_the_two_data_'
                                      'the_harness_does_not_have'))


def _wm(p):
    return p['OM'] * (p['H0'] / 100.0) ** 2


class Ruler(object):
    """a `r_d(omega_m, omega_b, Sum)` table, read with its own bounds and its clipping counted"""

    def __init__(self, path, key, label, name):
        z = np.load(path)
        self.wm, self.wb, self.ss = z['omega_m'], z['omega_b'], z['sums']
        self.itp = RegularGridInterpolator((self.wm, self.wb, self.ss), z[key],
                                           method='cubic', bounds_error=False, fill_value=None)
        self.lo = (float(self.wm[0]), float(self.wb[0]), float(self.ss[0]))
        self.hi = (float(self.wm[-1]), float(self.wb[-1]), float(self.ss[-1]))
        self.label, self.name, self.clipped = label, name, 0

    def __call__(self, p):
        v = [_wm(p), p['WB'], p['MNU']]
        if not all(self.lo[i] <= v[i] <= self.hi[i] for i in range(3)):
            self.clipped += 1
            v = [min(max(v[i], self.lo[i]), self.hi[i]) for i in range(3)]
        return float(self.itp(np.asarray([v]))[0])


def precondition():
    """the bank's own config, read -- and the ABSENCE of the new key is the proof it predates ①"""
    pol = [f for f in os.listdir(os.environ['POL_DIR'])
           if f.endswith('.npz') and not f.endswith('_tt.npz')]
    z = np.load(os.path.join(os.environ['POL_DIR'], 'lcdm_S000.npz'), allow_pickle=True)
    cfg = json.loads(str(np.atleast_1d(z['config'])[0]))
    pp = [f for f in os.listdir(os.environ['PPGRID'])
          if f.endswith('.json') and f.startswith('lcdm_')]
    ok = dict(cmb_points=len(pol), lensing_points_lcdm=len(pp),
              blob=cfg.get('instrument_blob'),
              blob_is_not_landed=bool(cfg.get('instrument_blob') != LANDED_BLOB),
              nufd_key_present=bool('NUFD' in cfg),
              mnu_key_present=bool('MNU' in cfg),
              config_keys=sorted(cfg.keys()))
    #: ⛔ *the gate is that the key is ABSENT.  A bank whose config SAID `NUFD: false` would be one
    #: taken after item ② with the switch off -- a different object, and one this revision could
    #: have compared like for like.  These banks cannot say, and that is the finding.*
    ok['holds'] = bool(len(pol) == 32 and len(pp) >= 16 and ok['blob_is_not_landed']
                       and not ok['nufd_key_present'])
    return ok


def attach(mod, ruler, M3, DI):
    """the ruler on the model INSTANCE -- as r7860 replaced `amp_cmb`, so nothing landed is edited"""
    E = M3.ARMS[mod.cmb.arm]['E']
    cache = {}

    def chi2_cal(x5, bao=True):
        x4, s = x5[:4], float(x5[4])
        if not (mod.cmb.s_lo <= s <= mod.cmb.s_hi):
            return 1e12
        c = mod.cmb.chi2_cmb(x4, s)
        if bao:
            p = mod.cmb.phys(x4, s)
            rd = ruler(p)
            key = (round(p['H0'], 6), round(p['OM'], 7), round(rd, 6))
            if key not in cache:
                cache[key] = float(DI.chi2_bao(p['H0'], p['OM'], rd, E))
            c += cache[key]
        return float(c)

    mod.cmb.chi2 = chi2_cal


def profile(mod, sums, label, free, ruler=None):
    """r7860's convergence discipline, carried unchanged -- a profile that dips reports NO limit"""
    _prev = {}

    def prof(sum_ev):
        best, bestx = np.inf, None

        def f(v):
            x4 = np.zeros(4)
            for j, k in enumerate(free):
                x4[k] = v[j]
            return float(mod.chi2(list(x4) + [sum_ev, float(v[-1])]))
        starts = [[0.0] * len(free) + [t0] for t0 in (0.040, 0.054, 0.075, 0.100)]
        if 'x' in _prev:
            starts.insert(0, list(_prev['x']))
        for x0 in starts:
            r = minimize(f, x0, method='Nelder-Mead',
                         options=dict(xatol=1e-6, fatol=1e-6, maxiter=20000, maxfev=20000))
            if np.isfinite(r.fun) and r.fun < best:
                best, bestx = float(r.fun), list(r.x)
        if bestx is not None:
            r = minimize(f, bestx, method='Nelder-Mead',
                         options=dict(xatol=1e-7, fatol=1e-7, maxiter=20000, maxfev=20000))
            if np.isfinite(r.fun) and r.fun < best:
                best, bestx = float(r.fun), list(r.x)
            _prev['x'] = bestx
        return best, bestx

    s = np.array(sums, float)
    t, xs, rds = [], [], []
    for v in s:
        b, bx = prof(float(v))
        t.append(b)
        xs.append(bx)
        if bx is None or ruler is None:
            rds.append(float('nan'))
        else:
            x4 = np.zeros(4)
            for j, k in enumerate(free):
                x4[k] = bx[j]
            rds.append(float(ruler(mod.cmb.phys(list(x4), float(v)))))
    t = np.array(t, float)
    d = t - np.nanmin(t)
    i0 = int(np.nanargmin(t))
    above = [k for k in range(i0 + 1, len(s)) if d[k] >= DCHI2]
    lim = None
    if above:
        k = above[0]
        lim = float(s[k - 1] + (DCHI2 - d[k - 1]) * (s[k] - s[k - 1])
                    / (d[k] - d[k - 1])) * 1000.0
    dips = [(float(s[k]), float(t[k] - t[k - 1]))
            for k in range(i0 + 1, len(s)) if t[k] < t[k - 1] - 1e-6]
    print('\n  %s' % label)
    print('  ' + '-' * 104)
    for a, b, c, r in zip(s, t, d, rds):
        print('    Sum = %.3f eV   total chi2 %12.4f   delta %8.4f   r_d %s'
              % (a, b, c, ('%9.4f Mpc' % r) if r == r else '       --'))
    print('    minimum at Sum = %.3f eV' % s[i0])
    if dips:
        print('    ⛔ NOT MONOTONIC above the minimum at %s -- NO limit is reported'
              % ', '.join('%.3f eV' % x[0] for x in dips))
    else:
        print('    monotonic above the minimum: converged where the limit is read')
    print('    95 per cent limit: %s meV'
          % (('%.2f' % lim) if (lim is not None and not dips) else 'NOT REPORTED'))
    out = dict(sums=[float(v) for v in s], totals=[float(v) for v in t],
               delta=[float(v) for v in d], min_at=float(s[i0]),
               limit_meV=(None if dips else lim), crossing_meV=lim,
               monotonic_above_min=not dips, dips=[list(x) for x in dips],
               rd_at_node=rds, x_at_node=[list(map(float, x)) if x else None for x in xs])
    if ruler is not None and all(r == r for r in rds):
        out['rd_span'] = float(np.nanmax(rds) / np.nanmin(rds) - 1.0)
        print('    the ruler across the profile: %.4f to %.4f Mpc, a span of %.3e'
              % (np.nanmin(rds), np.nanmax(rds), out['rd_span']))
    return out


def main():
    print(__doc__)
    print('=' * 104)
    out = {}

    print('\n  THE PRECONDITION -- what background are the banked spectra on?')
    print('  ' + '-' * 104)
    pre = precondition()
    print('    CMB points %d, lensing points %d, blob %s'
          % (pre['cmb_points'], pre['lensing_points_lcdm'], str(pre['blob'])[:12]))
    print('    the new switch key is present in the bank\'s own config: %s   (MNU key: %s)'
          % (pre['nufd_key_present'], pre['mnu_key_present']))
    print('    ⇒ ** the key is ABSENT, which is the PROOF these spectra predate item ①.  A bank '
          'taken after it would SAY `false`, and that is a different statement. **')
    out['precondition'] = pre
    if not pre['holds']:
        print('\n  ⛔ the precondition FAILS -- no limit is reported.\n')
        _save(out)
        return 1

    import model3 as M3
    import distances as DI
    import model6 as M6

    r_inst = Ruler(os.path.join(_HERE, 'rd_grid_nufd.npz'), 'r_drag',
                   "this instrument's own drag epoch ON THE REPAIRED BACKGROUND", 'instrument')
    r_ref = Ruler(os.path.join(R7862, 'ref_grid.npz'), 'rdrag',
                  "the reference's own rdrag at each point", 'reference')

    print('\n  Ⓒ③ᵃ THE RULER DIFFERENCE AFTER THE REPAIR -- it was 14.5415 in chi2_bao at r7862')
    print('  ' + '-' * 104)
    c = M3.ARMS['lcdm']['centre']
    E = M3.ARMS['lcdm']['E']
    rows = []
    for s in (0.0, 0.06, 0.30, 0.60):
        p = dict(H0=c['H0'], OM=c['OM'], WB=c['WB'], NS=c['NS'], MNU=float(s))
        ri, rr = r_inst(p), r_ref(p)
        ci = float(DI.chi2_bao(p['H0'], p['OM'], ri, E))
        cr = float(DI.chi2_bao(p['H0'], p['OM'], rr, E))
        rows.append(dict(sum=float(s), rd_instrument=ri, rd_reference=rr,
                         rd_rel=abs(ri / rr - 1.0), dchi2=abs(ci - cr)))
        print('    Sum %.3f eV   r_d %9.4f (instrument) vs %9.4f (reference)   %.2e    '
              'delta chi2_bao %8.4f' % (s, ri, rr, rows[-1]['rd_rel'], rows[-1]['dchi2']))
    top = rows[-1]
    out['ruler_gap'] = dict(rows=rows, dchi2_at_top=top['dchi2'],
                            dchi2_at_top_before=14.5415,
                            closed=bool(top['dchi2'] < 14.5415 / 2.0))
    print('    ⇒ at Sum = 0.60 eV the two rulers now differ by %.4f in chi2_bao, against 14.5415 '
          'before the repair: %s' % (top['dchi2'],
                                     'most of it is closed' if out['ruler_gap']['closed']
                                     else '** it is NOT closed **'))

    sums = [0.0, 0.03, 0.06, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 0.60]
    out['profiles'] = {}
    for which, free, ruler, label in (
            ('minimised', [0, 1, 2, 3], None,
             'Ⓒ③ᵇ THE RULER MINIMISED, on the banked spectra -- against the reference\'s 54.00 meV'),
            ('calibrated', [0, 1, 2, 3], r_inst,
             'Ⓒ③ᶜ CALIBRATED on this instrument\'s own REPAIRED drag epoch -- against 30.56 meV')):
        mod = M6.Model6('lcdm')
        raw = mod.amp_cmb
        #: the one substitution r7860 measured, carried unchanged and NOT re-measured here
        mod.amp_cmb = lambda x4, s, _r=raw: _r(x4, s) / 2.0
        sums = [s for s in sums if mod.cmb.s_lo - 1e-9 <= s <= mod.cmb.s_hi + 1e-9]
        if ruler is not None:
            attach(mod, ruler, M3, DI)
        res = profile(mod, sums, label, free, ruler)
        res['clipped_calls'] = (0 if ruler is None else int(ruler.clipped))
        out['profiles'][which] = res

    mini, cal = out['profiles']['minimised'], out['profiles']['calibrated']
    print('\n  THE ADJUDICATION')
    print('  ' + '-' * 104)
    print('    minimised  %s meV against the reference\'s %.2f  (r7862 read %.2f)'
          % (('%.2f' % mini['limit_meV']) if mini['limit_meV'] else 'NOT REPORTED',
             REF_RULER, R7862_MINIMISED))
    print('    calibrated %s meV against the ordered %.2f  (r7862 read %.2f on the reference\'s '
          'ruler and %.2f on this instrument\'s unrepaired one)'
          % (('%.2f' % cal['limit_meV']) if cal['limit_meV'] else 'NOT REPORTED',
             REF_CALIB, R7862_CALIB_ON_REF, R7862_CALIB_ON_INST))
    gap = (None if cal['limit_meV'] is None
           else abs(cal['limit_meV'] - R7862_CALIB_ON_REF))
    held = bool(gap is not None and gap <= EXPECT_WITHIN)
    out['adjudication'] = dict(
        expectation=('the calibrated limit on this instrument\'s own repaired ruler lands within '
                     '%.1f meV of r7862\'s %.2f read on the reference\'s ruler'
                     % (EXPECT_WITHIN, R7862_CALIB_ON_REF)),
        gap_to_r7862_on_reference=gap, within=EXPECT_WITHIN, held=held,
        limit_minimised=mini['limit_meV'], limit_calibrated=cal['limit_meV'],
        reference_minimised=REF_RULER, reference_calibrated=REF_CALIB,
        read_on='the banked spectra with the ruler repaired, NOT a re-solved bank')
    print('    the registered expectation: %s' % out['adjudication']['expectation'])
    print('    ⇒ the gap is %s meV, so the expectation %s'
          % (('%.2f' % gap) if gap is not None else 'unreadable',
             'HOLDS' if held else '** FAILS **, reported as failed with the criterion unmoved'))

    # ── Ⓓ④ the second basin ────────────────────────────────────────────────────────────────────
    print('\n  Ⓓ④ THE SECOND BASIN AT Sum = 0.60 eV -- r7862 found H0 = 65.74 against 69.17 below')
    print('  ' + '-' * 104)
    STEPH = 2.0
    bas = {}
    for which in ('minimised', 'calibrated'):
        xs = out['profiles'][which]['x_at_node']
        if not xs or xs[-1] is None or xs[-2] is None:
            continue
        h_top = c['H0'] + STEPH * xs[-1][0]
        h_below = c['H0'] + STEPH * xs[-2][0]
        jumped = bool(abs(h_top - h_below) > 1.0)
        bas[which] = dict(H0_top=h_top, H0_below=h_below, jumped=jumped,
                          chi2_top=out['profiles'][which]['totals'][-1],
                          chi2_below=out['profiles'][which]['totals'][-2],
                          x_top=xs[-1], x_below=xs[-2])
        print('    %-11s H0 at Sum = 0.60 eV: %7.3f   at the node below: %7.3f   %s'
              % (which, h_top, h_below,
                 'A DIFFERENT BRANCH' if jumped else 'the same branch -- the basin is GONE'))
    out['second_basin'] = dict(rows=bas, r7862_H0_top=65.74, r7862_H0_below=69.17,
                               persists=bool(any(v['jumped'] for v in bas.values())))
    print('    ⇒ the basin %s after the repair'
          % ('PERSISTS' if out['second_basin']['persists'] else 'does NOT persist'))
    _save(out)
    print('')
    return 0


def _save(out):
    with io.open(os.path.join(_HERE, 'limits.json'), 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=float))


if __name__ == '__main__':
    raise SystemExit(main())
