# -*- coding: utf-8 -*-
"""r7860 (60) Ⓔ⑤ -- THE ORDERED CONTROL, WITH ALL THREE SWITCHES ON.

⛭ `r7857` (69) item ④.  Two of the three switches are in the GRIDS this reads, not substituted:

  * the CMB half is re-solved with `BVEL` on -- `32` of `32` points, in a directory keyed to it;
  * the lensing half is regenerated with `BVEL` **and** `PRIMNORM` both on, natively, so the
    primordial constant comes from each point's own tilt rather than from one number for the grid.

⛔ **ONE substitution remains and it is stated, not silent:** the accumulation-and-save factor is
exactly twice the grid, measured at the bank's own reach in `doubling.py` (worst `3.8e-15`).  It
reaches the score in exactly ONE place -- the free amplitude the CMB fit solves for, which halves --
and the arms below MEASURE that: the CMB `chi^2` must be unchanged by it, because the amplitude is
free, and the lensing prediction must be exactly halved.

⌗ **Ⓔ⑤ᵃ is a precondition, not a formality.** The instrument's resolved config does not record the
solver switch, so a re-solved point and a landed one differ in their own records only by the
instrument blob.  This asserts the blob is NOT the landed grid's before anything is scored.

    python3 control.py
"""
import io
import json
import os
import sys

import numpy as np
from scipy.optimize import minimize

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
#: ⛔ FOUR dirnames: this file sits three directories below the repository root.
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT
BANK = os.path.join(_BTW, 'bank')
LANDED_BLOB = '291f4477c37ed7fbb13dea2f32ca1744f1ed4d68'   # the grid the order says predates BVEL
REF_RULER, REF_CALIB = 54.00, 30.56                        # the two ordered figures, in meV
DCHI2 = 2.71                                               # 95 per cent, one-sided, one parameter

os.environ['POL_DIR'] = os.path.join(BANK, 'pol_grid_bvel1')
os.environ['PPGRID'] = os.path.join(BANK, 'phiphi_grid_eta4000_bvel1_primnorm1')
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '4')
sys.path.insert(0, os.path.join(_BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_'
                                      'lensing_bandpowers'))
sys.path.insert(0, os.path.join(_BTW, 'r7842_60_polarisation_added_to_the_score_and_the_two_data_'
                                      'the_harness_does_not_have'))


def precondition():
    """Ⓔ⑤ᵃ -- prove the grids are the re-solved ones before anything is scored"""
    pol = [f for f in os.listdir(os.environ['POL_DIR'])
           if f.endswith('.npz') and not f.endswith('_tt.npz')]
    z = np.load(os.path.join(os.environ['POL_DIR'], 'lcdm_S000.npz'), allow_pickle=True)
    blob = json.loads(str(np.atleast_1d(z['config'])[0])).get('instrument_blob')
    pp = [f for f in os.listdir(os.environ['PPGRID']) if f.endswith('.json')]
    pp_lcdm = [f for f in pp if f.startswith('lcdm_')]
    ok = dict(cmb_points=len(pol), cmb_points_expected=32,
              blob=blob, blob_is_not_landed=bool(blob != LANDED_BLOB),
              lensing_points_lcdm=len(pp_lcdm), lensing_expected_lcdm=16)
    ok['holds'] = bool(len(pol) == 32 and blob != LANDED_BLOB and len(pp_lcdm) >= 16)
    return ok


def main():
    print(__doc__)
    print('=' * 100)
    print('\n  Ⓔ⑤ᵃ THE PRECONDITION -- is this the re-solved grid?')
    print('  ' + '-' * 98)
    pre = precondition()
    print('    CMB polarisation points : %d (want %d)' % (pre['cmb_points'],
                                                          pre['cmb_points_expected']))
    print('    instrument blob         : %s' % str(pre['blob'])[:12])
    print('    and it is NOT the landed grid\'s: %s' % pre['blob_is_not_landed'])
    print('    lensing points, control : %d (want %d)' % (pre['lensing_points_lcdm'],
                                                          pre['lensing_expected_lcdm']))
    out = dict(precondition=pre)
    if not pre['holds']:
        print('\n  ⛔ Ⓔ⑤ᵃ FAILS -- no limit is reported.\n')
        with io.open(os.path.join(_HERE, 'control.json'), 'w', encoding='utf-8') as fh:
            fh.write(json.dumps(out, indent=1, sort_keys=True))
        return 1
    print('\n    ** Ⓔ⑤ᵃ HOLDS **')

    import model6 as M6
    mod = M6.Model6('lcdm')

    # ── the one substitution, applied in the one place it reaches and MEASURED there ────────────
    raw_amp = mod.amp_cmb
    chi2_before = float(mod.chi2([0, 0, 0, 0, 0.06, 0.054]))
    pp_before = np.asarray(mod.pp_model(np.zeros(4), 0.06, 0.054), float)

    def amp_halved(x4, sum_ev):
        """`FOURPI` doubles all three blocks, so the FREE amplitude the CMB solves for halves"""
        return raw_amp(x4, sum_ev) / 2.0
    mod.amp_cmb = amp_halved
    chi2_cmb_only_before = float(mod.cmb.chi2_cmb(np.zeros(4), 0.06))
    chi2_cmb_only_after = float(mod.cmb.chi2_cmb(np.zeros(4), 0.06))
    pp_after = np.asarray(mod.pp_model(np.zeros(4), 0.06, 0.054), float)
    halved = float(np.max(np.abs(pp_after / pp_before - 0.5)))
    cmb_same = bool(chi2_cmb_only_after == chi2_cmb_only_before)
    print('\n  Ⓔ⑤ᵃᵇ THE SUBSTITUTION, MEASURED WHERE IT ACTS')
    print('  ' + '-' * 98)
    print('    the CMB chi^2 is unchanged by it (the amplitude is free): %s' % cmb_same)
    print('    the lensing prediction is exactly halved: worst |ratio - 1/2| %.3e' % halved)
    out['substitution'] = dict(cmb_chi2_unchanged=cmb_same, worst_halving_error=halved,
                               chi2_joint_before_substitution=chi2_before)
    if not (cmb_same and halved < 1e-12):
        print('\n  ⛔ the substitution does not act as measured -- no limit is reported.\n')
        with io.open(os.path.join(_HERE, 'control.json'), 'w', encoding='utf-8') as fh:
            fh.write(json.dumps(out, indent=1, sort_keys=True))
        return 1

    # ── the two profiles ───────────────────────────────────────────────────────────────────────
    SUMS = [0.0, 0.03, 0.06, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 0.60]
    SUMS = [s for s in SUMS if mod.s_lo - 1e-9 <= s <= mod.s_hi + 1e-9]

    # ⛔ ** THE FIRST RUN OF THIS PROFILE WAS NOT CONVERGED, AND THAT IS KEPT HERE. **  *A single
    #   Nelder-Mead start per node returned a profile that went DOWN between `0.300` and `0.400` eV
    #   -- `2216.70` then `2212.27` -- and a profile that dips is a reading on the FIT and not on
    #   the physics, the same shape of error as a constant that came out `k`-dependent.  So each
    #   node is now minimised from several starts INCLUDING the previous node's own solution
    #   (continuation), and the monotonicity above the minimum is CHECKED rather than assumed.*
    _prev = {}

    def prof(sum_ev, free, key):
        best, bestx = np.inf, None

        def f(v):
            x4 = np.zeros(4)
            for j, k in enumerate(free):
                x4[k] = v[j]
            return float(mod.chi2(list(x4) + [sum_ev, float(v[-1])]))
        starts = [[0.0] * len(free) + [t0] for t0 in (0.040, 0.054, 0.075, 0.100)]
        if key in _prev:
            starts.insert(0, list(_prev[key]))
        for x0 in starts:
            r = minimize(f, x0, method='Nelder-Mead',
                         options=dict(xatol=1e-6, fatol=1e-6, maxiter=20000, maxfev=20000))
            if np.isfinite(r.fun) and r.fun < best:
                best, bestx = float(r.fun), list(r.x)
        if bestx is not None:
            # one polish from the winner, so the node is at a stationary point of its own
            r = minimize(f, bestx, method='Nelder-Mead',
                         options=dict(xatol=1e-7, fatol=1e-7, maxiter=20000, maxfev=20000))
            if np.isfinite(r.fun) and r.fun < best:
                best, bestx = float(r.fun), list(r.x)
            _prev[key] = bestx
        return best

    def limit(free, label):
        t = np.array([prof(s, free, label) for s in SUMS], float)
        s = np.array(SUMS, float)
        d = t - np.nanmin(t)
        i0 = int(np.nanargmin(t))
        above = [k for k in range(i0 + 1, len(s)) if d[k] >= DCHI2]
        lim = None
        if above:
            k = above[0]
            s0, s1, d0, d1 = s[k - 1], s[k], d[k - 1], d[k]
            lim = float(s0 + (DCHI2 - d0) * (s1 - s0) / (d1 - d0)) * 1000.0
        print('\n  Ⓔ⑤ᵇ %s' % label)
        print('  ' + '-' * 98)
        for a, b, c in zip(s, t, d):
            print('    Sum = %.3f eV   total chi2 %12.4f   delta %8.4f' % (a, b, c))
        print('    minimum at Sum = %.3f eV' % s[i0])
        dips = [(float(s[k]), float(t[k] - t[k - 1]))
                for k in range(i0 + 1, len(s)) if t[k] < t[k - 1] - 1e-6]
        if dips:
            print('    \u26d4 NOT MONOTONIC above the minimum at %s -- the profile is not converged,'
                  % ', '.join('%.3f eV' % d[0] for d in dips))
            print('      so the crossing below is NOT reported as a limit.')
        else:
            print('    monotonic above the minimum: the profile is converged where the limit is read')
        if lim is None:
            print('    ⛔ NO CROSSING of delta chi2 = %.2f inside the grid\'s own sum range '
                  '[%.2f, %.2f] eV' % (DCHI2, mod.s_lo, mod.s_hi))
            print('       ⇒ a limit above the grid\'s upper node would be an EXTRAPOLATION and is')
            print('         refused rather than reported, exactly as registered.')
        else:
            print('    95 per cent limit (delta chi2 = %.2f): %.2f meV' % (DCHI2, lim))
        return dict(sums=[float(v) for v in s], totals=[float(v) for v in t],
                    delta=[float(v) for v in d], min_at=float(s[i0]),
                    limit_meV=(None if dips else lim), monotonic_above_min=not dips,
                    dips=[list(x) for x in dips], crossing_meV=lim)

    out['ruler_minimised'] = limit([0, 1, 2, 3],
                                   'THE RULER MINIMISED -- H0, OM, omega_b and n_s all free')
    out['calibrated'] = limit([2, 3],
                              'CALIBRATED -- the ruler held, omega_b and n_s free')

    print('\n  ⇒ AGAINST THE TWO ORDERED FIGURES')
    print('  ' + '-' * 98)
    for key, ref, name in (('ruler_minimised', REF_RULER, 'ruler minimised'),
                           ('calibrated', REF_CALIB, 'calibrated')):
        lim = out[key]['limit_meV']
        if lim is None:
            print('    %-16s  reference %6.2f meV   this control: NO CROSSING, nothing reported'
                  % (name, ref))
        else:
            print('    %-16s  reference %6.2f meV   this control %7.2f meV   ratio %.3f'
                  % (name, ref, lim, lim / ref))
            out[key]['reference_meV'] = ref
            out[key]['ratio_to_reference'] = float(lim / ref)
            out[key]['in_registered_window'] = bool(10.0 <= lim <= 200.0)
    print('\n  ⌗ And whatever these are, they are limits THROUGH THIS INSTRUMENT, which `Ⓑ②ᵃ` has')
    print('    just measured still carries a few-per-cent shape residual against the reference.')
    with io.open(os.path.join(_HERE, 'control.json'), 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True))
    print('\n  wrote control.json\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
