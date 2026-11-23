# -*- coding: utf-8 -*-
"""r7862 (60) Ⓑ② -- THE CALIBRATED CASE, ON BOTH RULERS, EACH NAMED.

⛭ `r7861` (69) item ①.  `r7860`'s "calibrated" profile froze `H0` and `Om` at the grid's centre and
freed `omega_b` and `n_s`; the reference frees all four and takes the BAO ruler at each point from
that point's own drag epoch.  **So `146.13` meV was not the comparison to `30.56`, and this file
computes the case that is.**

Two ruler treatments, registered in the amendment BEFORE either profile was minimised:

  ⒜ **the instrument's own** `r_d(omega_m, omega_b)`, derived in `drag_ruler.py` from the
     instrument's own ionisation history and validated against the reference at two corners of the
     fit's box.  ⚠ *It is exactly FLAT in the neutrino sum, because the instrument carries the
     neutrino mass inside `OM` at every epoch.*
  ⒝ **the reference's own** `rdrag`, which does move with the sum.  *This is the ruler `cc66`'s
     `30.56` meV was produced on, and it is the reference's number -- said here rather than
     presented as this instrument's.*

⛔ **Nothing landed is edited.**  The ruler is attached by replacing `mod.cmb.chi2` on the instance,
exactly as `r7860` replaced `amp_cmb`, so `model3.py` and the instrument keep their bytes.

    python3 calibrated.py
"""
import io
import json
import os
import sys

import numpy as np
from scipy.interpolate import RectBivariateSpline, RegularGridInterpolator
from scipy.optimize import minimize

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
#: ⛔ FOUR dirnames: this file sits three directories below the repository root.
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT
BANK = os.path.join(_BTW, 'bank')
LANDED_BLOB = '291f4477c37ed7fbb13dea2f32ca1744f1ed4d68'
REF_CALIB = 30.56               # the figure item ① asks the calibrated case to be read against
REF_RULER = 54.00               # the reference's minimised figure, for the gap Ⓒ③ prices
R7860_MINIMISED = 69.97         # this line's own minimised limit, read from r7860's record below
DCHI2 = 2.71
# ⛭ registered in the amendment: the band the expectation is adjudicated in, and the minimum's node
EXPECT_LO, EXPECT_HI = 15.3, 61.1
EXPECT_MIN_BELOW = 0.030

os.environ['POL_DIR'] = os.path.join(BANK, 'pol_grid_bvel1')
os.environ['PPGRID'] = os.path.join(BANK, 'phiphi_grid_eta4000_bvel1_primnorm1')
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '4')
sys.path.insert(0, os.path.join(_BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_'
                                      'lensing_bandpowers'))
sys.path.insert(0, os.path.join(_BTW, 'r7842_60_polarisation_added_to_the_score_and_the_two_data_'
                                      'the_harness_does_not_have'))
sys.path.insert(0, _HERE)


def _wm(p):
    return p['OM'] * (p['H0'] / 100.0) ** 2


class InstrumentRuler(object):
    """⒜ the instrument's own ruler, read off `drag_ruler.py`'s table

    ⌗ *Flat in the sum BY MEASUREMENT, not by choice: `drag_ruler.py` found the sum moves it by
    exactly zero, and the table is built at one sum for that reason.  The `sum_ev` argument is
    accepted and IGNORED, and the receipt reports that it is.*
    """

    label = "the instrument's own drag epoch (flat in the sum, by measurement)"
    name = 'instrument'

    def __init__(self):
        z = np.load(os.path.join(_HERE, 'rd_grid.npz'))
        self.wm, self.wb = z['omega_m'], z['omega_b']
        self.spl = RectBivariateSpline(self.wm, self.wb, z['r_drag'][0], kx=3, ky=3, s=0)
        self.lo = (float(self.wm[0]), float(self.wb[0]))
        self.hi = (float(self.wm[-1]), float(self.wb[-1]))
        self.clipped = 0

    def __call__(self, p):
        a, b = _wm(p), p['WB']
        if not (self.lo[0] <= a <= self.hi[0] and self.lo[1] <= b <= self.hi[1]):
            self.clipped += 1
            a = min(max(a, self.lo[0]), self.hi[0])
            b = min(max(b, self.lo[1]), self.hi[1])
        return float(self.spl(a, b)[0, 0])


class ReferenceRuler(object):
    """⒝ the reference's own `rdrag`, read off `ref_ruler.py`'s table -- and it MOVES with the sum"""

    label = "the reference's own rdrag at each point, including its neutrino sum"
    name = 'reference'

    def __init__(self):
        z = np.load(os.path.join(_HERE, 'ref_grid.npz'))
        self.wm, self.wb, self.ss = z['omega_m'], z['omega_b'], z['sums']
        self.itp = RegularGridInterpolator((self.wm, self.wb, self.ss), z['rdrag'],
                                           method='cubic', bounds_error=False, fill_value=None)
        self.lo = (float(self.wm[0]), float(self.wb[0]), float(self.ss[0]))
        self.hi = (float(self.wm[-1]), float(self.wb[-1]), float(self.ss[-1]))
        self.clipped = 0

    def __call__(self, p):
        v = [_wm(p), p['WB'], p['MNU']]
        if not all(self.lo[i] <= v[i] <= self.hi[i] for i in range(3)):
            self.clipped += 1
            v = [min(max(v[i], self.lo[i]), self.hi[i]) for i in range(3)]
        return float(self.itp(np.asarray([v]))[0])


def spline_error(ruler, probe_direct, n=7):
    """the table's own interpolation error, measured OFF ITS NODES

    ⌗ *A ruler read off a table is only as good as the table between its nodes, and this corpus has
    been bitten by a spline standing in for a computation before -- `bao_error` exists for the same
    reason.  So the error is MEASURED at off-node points rather than assumed small.*
    """
    rng = np.random.RandomState(7862)
    worst, rows = 0.0, []
    for _ in range(n):
        a = float(rng.uniform(ruler.lo[0], ruler.hi[0]))
        b = float(rng.uniform(ruler.lo[1], ruler.hi[1]))
        s = (float(rng.uniform(ruler.lo[2], ruler.hi[2]))
             if hasattr(ruler, 'ss') else 0.0)
        H0 = 67.40
        p = dict(H0=H0, OM=a / (H0 / 100.0) ** 2, WB=b, NS=0.965, MNU=s)
        got, want = ruler(p), probe_direct(p)
        rel = abs(got / want - 1.0)
        rows.append(dict(omega_m=a, omega_b=b, sum=s, table=got, direct=want, rel=rel))
        worst = max(worst, rel)
    return dict(points=rows, worst_rel=float(worst))


def attach(mod, ruler, M3, DI):
    """replace the instance's `chi2` so the BAO ruler is this point's own -- NOT a file edit

    ⌗ *`model3.chi2` calls `chi2_bao(H0, Om)` with two arguments, and a calibrated ruler needs
    `omega_b` and the sum as well, so the replacement is at the level that HAS the whole point.
    Everything else -- the CMB term, the amplitude, the barrier -- is the landed code.*
    """
    E = M3.ARMS[mod.cmb.arm]['E']
    cache, seen = {}, []

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
            seen.append((float(s), float(rd), float(p['H0']), float(p['OM']), float(p['WB'])))
        return float(c)

    mod.cmb.chi2 = chi2_cal
    return seen


def price_the_rulers(mod, M3, DI, r_inst, r_ref, sums):
    """Ⓑ②ᵉ -- what the difference between the two rulers is WORTH, before any profile is read

    *One per cent in the ruler was about seventeen in `chi2_bao` at `r7854`; the limit is read at
    `2.71`.  So the two rulers' `chi2_bao` is differenced at the control geometry, node by node.*
    """
    E = M3.ARMS['lcdm']['E']
    c = M3.ARMS['lcdm']['centre']
    rows = []
    for s in sums:
        p = dict(H0=c['H0'], OM=c['OM'], WB=c['WB'], NS=c['NS'], MNU=float(s))
        ri, rr = r_inst(p), r_ref(p)
        ci = float(DI.chi2_bao(p['H0'], p['OM'], ri, E))
        cr = float(DI.chi2_bao(p['H0'], p['OM'], rr, E))
        rows.append(dict(sum=float(s), rd_instrument=ri, rd_reference=rr,
                         rd_rel=abs(ri / rr - 1.0), chi2_instrument=ci, chi2_reference=cr,
                         dchi2=abs(ci - cr)))
        print('    Sum %.3f eV   r_d  %9.4f (instrument)  vs %9.4f (reference)   %.2e'
              '    chi2_bao %9.4f vs %9.4f   delta %8.4f'
              % (s, ri, rr, rows[-1]['rd_rel'], ci, cr, rows[-1]['dchi2']))
    top = max(rows, key=lambda r: r['sum'])
    out = dict(rows=rows, dchi2_threshold=DCHI2, dchi2_at_top=top['dchi2'],
               sum_at_top=top['sum'], exceeds_threshold=bool(top['dchi2'] > DCHI2))
    print('    ⇒ at Sum = %.3f eV the two rulers differ by %.4f in chi2_bao against the %.2f the'
          ' limit is read at: %s' % (top['sum'], top['dchi2'], DCHI2,
                                     'THE SECOND TREATMENT IS NOT REDUNDANT'
                                     if out['exceeds_threshold'] else
                                     'the instrument\'s own ruler is adequate here'))
    return out


def profile(mod, sums, label, seen, ruler):
    """the profile, with the convergence discipline `r7860` had to learn, carried unchanged

    ⛔ *`r7860`'s first control profile DIPPED above its minimum and its limit was `14.8` per cent
    TIGHTER than the converged one -- an unconverged profile FLATTERS the instrument.  So each node
    is minimised from several starts INCLUDING the previous node's solution, polished once, and
    monotonicity above the minimum is CHECKED.  A profile that dips reports NO limit.*
    """
    free = [0, 1, 2, 3]
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
    t, xs, rds, calls = [], [], [], []
    for v in s:
        del seen[:]
        b, bx = prof(float(v))
        t.append(b)
        xs.append(bx)
        calls.append(len(seen))
        # ⌗ Ⓑ②ᵈ: the ruler AT THE NODE'S OWN MINIMUM, recorded so a ruler that never moved cannot
        #   pass for a calibrated one.
        #   ⛔⚠ *The first version of this column read `seen[-1]` -- the ruler's LAST call at the
        #   node, which is the final polish's last trial point and not the minimum.  It put
        #   `149.9752` Mpc at the top node against `145.4` -- `146.0` at every other, and this seat
        #   read that jump as the instrumentation's and fixed it here, evaluating the ruler AT the
        #   winning parameters instead.*  ⇒ ** AND THE RE-RUN REFUTED THAT DIAGNOSIS: the column
        #   comes back IDENTICAL, `149.9752` included. **  *So the jump is the FIT's and not the
        #   reading's -- at the top node the minimiser lands on a different branch, `H0 = 65.74`
        #   against `69.17` at the node below -- and the hypothesis is kept here as refuted rather
        #   than quietly dropped.  The change stands on its own merits: evaluating at the winning
        #   parameters is the right reading whether or not it moves a number.*
        if bx is None:
            rds.append(float('nan'))
        else:
            rds.append(float(ruler(mod.cmb.phys(list(bx[:4]), float(v)))))
    t = np.array(t, float)
    d = t - np.nanmin(t)
    i0 = int(np.nanargmin(t))
    above = [k for k in range(i0 + 1, len(s)) if d[k] >= DCHI2]
    lim = None
    if above:
        k = above[0]
        s0, s1, d0, d1 = s[k - 1], s[k], d[k - 1], d[k]
        lim = float(s0 + (DCHI2 - d0) * (s1 - s0) / (d1 - d0)) * 1000.0
    print('\n  Ⓑ②  %s' % label)
    print('  ' + '-' * 104)
    for a, b, c, r in zip(s, t, d, rds):
        print('    Sum = %.3f eV   total chi2 %12.4f   delta %8.4f   r_d %9.4f Mpc'
              % (a, b, c, r))
    print('    minimum at Sum = %.3f eV' % s[i0])
    dips = [(float(s[k]), float(t[k] - t[k - 1]))
            for k in range(i0 + 1, len(s)) if t[k] < t[k - 1] - 1e-6]
    if dips:
        print('    ⛔ NOT MONOTONIC above the minimum at %s -- the profile is not converged,'
              % ', '.join('%.3f eV' % x[0] for x in dips))
        print('      so the crossing below is NOT reported as a limit.')
    else:
        print('    monotonic above the minimum: the profile is converged where the limit is read')
    if lim is None:
        print('    ⛔ NO CROSSING of delta chi2 = %.2f inside the grid\'s own sum range' % DCHI2)
    else:
        print('    95 per cent limit (delta chi2 = %.2f): %.2f meV' % (DCHI2, lim))
    rd_moved = float(np.nanmax(rds) / np.nanmin(rds) - 1.0)
    print('    the ruler across the profile: %.4f to %.4f Mpc, a span of %.3e'
          % (np.nanmin(rds), np.nanmax(rds), rd_moved))
    return dict(sums=[float(v) for v in s], totals=[float(v) for v in t],
                delta=[float(v) for v in d], min_at=float(s[i0]),
                limit_meV=(None if dips else lim), crossing_meV=lim,
                monotonic_above_min=not dips, dips=[list(x) for x in dips],
                rd_at_node=rds, rd_span=rd_moved, ruler_moves=bool(rd_moved > 1e-6),
                ruler_calls_per_node=calls,
                x_at_node=[list(map(float, x)) if x else None for x in xs])


def precondition():
    """the same precondition `r7860` ran: the grids must be the re-solved ones, blob and all"""
    pol = [f for f in os.listdir(os.environ['POL_DIR'])
           if f.endswith('.npz') and not f.endswith('_tt.npz')]
    z = np.load(os.path.join(os.environ['POL_DIR'], 'lcdm_S000.npz'), allow_pickle=True)
    blob = json.loads(str(np.atleast_1d(z['config'])[0])).get('instrument_blob')
    pp = [f for f in os.listdir(os.environ['PPGRID'])
          if f.endswith('.json') and f.startswith('lcdm_')]
    ok = dict(cmb_points=len(pol), blob=blob, blob_is_not_landed=bool(blob != LANDED_BLOB),
              lensing_points_lcdm=len(pp))
    ok['holds'] = bool(len(pol) == 32 and blob != LANDED_BLOB and len(pp) >= 16)
    return ok


def main():
    print(__doc__)
    print('=' * 104)
    out = {}

    print('\n  THE PRECONDITION -- is this the re-solved grid?')
    print('  ' + '-' * 104)
    pre = precondition()
    print('    CMB polarisation points %d, lensing points %d, blob %s, and it is NOT the landed'
          ' grid\'s: %s' % (pre['cmb_points'], pre['lensing_points_lcdm'],
                            str(pre['blob'])[:12], pre['blob_is_not_landed']))
    out['precondition'] = pre
    if not pre['holds']:
        print('\n  ⛔ the precondition FAILS -- no limit is reported.\n')
        _save(out)
        return 1

    # ── the two rulers, each with its table's own interpolation error MEASURED ──────────────────
    import drag_ruler as DR
    r_inst, r_ref = InstrumentRuler(), ReferenceRuler()
    print('\n  Ⓑ②ᵍ THE TABLES\' OWN INTERPOLATION ERROR, measured OFF their nodes')
    print('  ' + '-' * 104)
    e_inst = spline_error(r_inst, lambda p: DR.probe(p['H0'], p['OM'], p['WB'], MNU=p['MNU'])
                          ['r_drag'])
    e_ref = spline_error(r_ref, lambda p: DR.camb_drag(p['H0'], p['OM'], p['WB'],
                                                       MNU=p['MNU'])['rdrag'])
    print('    the instrument\'s table: worst %.3e over %d off-node points'
          % (e_inst['worst_rel'], len(e_inst['points'])))
    print('    the reference\'s table : worst %.3e over %d off-node points'
          % (e_ref['worst_rel'], len(e_ref['points'])))
    out['table_error'] = dict(instrument=e_inst, reference=e_ref)

    import model3 as M3
    import distances as DI
    import model6 as M6

    sums = [0.0, 0.03, 0.06, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 0.60]

    print('\n  Ⓑ②ᵉ WHAT THE DIFFERENCE BETWEEN THE TWO RULERS IS WORTH')
    print('  ' + '-' * 104)
    mod0 = M6.Model6('lcdm')
    sums = [s for s in sums if mod0.cmb.s_lo - 1e-9 <= s <= mod0.cmb.s_hi + 1e-9]
    out['ruler_price'] = price_the_rulers(mod0, M3, DI, r_inst, r_ref, sums)

    # ── the profiles, one per ruler, each on its own model instance ─────────────────────────────
    out['profiles'] = {}
    for ruler in (r_ref, r_inst):
        mod = M6.Model6('lcdm')
        raw_amp = mod.amp_cmb
        # the one substitution `r7860` measured: `FOURPI` doubles all three blocks, so the FREE
        # amplitude the CMB solves for halves.  Carried here unchanged and NOT re-measured.
        mod.amp_cmb = lambda x4, s, _r=raw_amp: _r(x4, s) / 2.0
        seen = attach(mod, ruler, M3, DI)
        res = profile(mod, sums, 'CALIBRATED on %s' % ruler.label, seen, ruler)
        res['ruler'] = ruler.name
        res['ruler_label'] = ruler.label
        res['clipped_calls'] = int(ruler.clipped)
        out['profiles'][ruler.name] = res

    # ── the adjudication, on the ruler the order's target was produced on ───────────────────────
    ref = out['profiles']['reference']
    inst = out['profiles']['instrument']
    lim = ref['limit_meV']
    held = bool(lim is not None and EXPECT_LO <= lim <= EXPECT_HI
                and ref['min_at'] < EXPECT_MIN_BELOW)
    out['adjudication'] = dict(
        expectation=('the calibrated profile\'s minimum moves below %.3f eV and its limit lands'
                     ' inside [%.1f, %.1f] meV' % (EXPECT_MIN_BELOW, EXPECT_LO, EXPECT_HI)),
        adjudicated_on='reference', limit_meV=lim, min_at=ref['min_at'],
        reference_target=REF_CALIB, held=held,
        limit_on_instrument_ruler=inst['limit_meV'], min_at_on_instrument_ruler=inst['min_at'],
        price_of_the_neutrino_background=(None if (lim is None or inst['limit_meV'] is None)
                                          else abs(lim - inst['limit_meV'])))
    print('\n  THE ADJUDICATION')
    print('  ' + '-' * 104)
    print('    the registered expectation: %s' % out['adjudication']['expectation'])
    print('    on the reference\'s ruler: minimum at %.3f eV, limit %s meV against the ordered'
          ' %.2f' % (ref['min_at'],
                     ('%.2f' % lim) if lim is not None else 'NOT REPORTED (profile dipped)',
                     REF_CALIB))
    print('    on the instrument\'s own ruler: minimum at %.3f eV, limit %s meV'
          % (inst['min_at'], ('%.2f' % inst['limit_meV'])
             if inst['limit_meV'] is not None else 'NOT REPORTED (profile dipped)'))
    print('    ⇒ the registered expectation %s' % ('HOLDS' if held else '** FAILS **, reported as'
                                                   ' failed with the criterion unmoved'))
    if out['adjudication']['price_of_the_neutrino_background'] is not None:
        print('    ⇒ the price of this instrument\'s neutrino background, read as the gap between'
              ' the two rulers\' limits: %.2f meV'
              % out['adjudication']['price_of_the_neutrino_background'])
    _save(out)
    return 0


def _save(out):
    with io.open(os.path.join(_HERE, 'calibrated.json'), 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=float))


if __name__ == '__main__':
    raise SystemExit(main())
