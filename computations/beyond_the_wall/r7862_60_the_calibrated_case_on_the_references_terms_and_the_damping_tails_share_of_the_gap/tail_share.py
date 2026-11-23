# -*- coding: utf-8 -*-
"""r7862 (60) Ⓒ③ -- THE DAMPING TAIL'S SHARE OF THE MINIMISED GAP.

⛭ `r7861` (69) item ②.  `r7860`'s minimised control came to `69.97` meV against the reference's
`54.00`: a gap of `15.97` meV.  `cc66` measured the raw spectrum departing from `CAMB` by `-6.35`
per cent near `ell = 1920`, so the order asks how much of the gap moves when the high-`ell`
bandpowers are cut back.

**What is measured:** the same minimised profile, re-scored with every bandpower whose bin REACHES
above a cut dropped -- from the model, from the data, from the covariance's inverse and from the
free amplitude's own solve, so the cut is a cut and not a re-weighting.  The gap's move is then
`limit(full) - limit(cut)`, which needs no re-scoring of the reference's own figure.

⚠ ** AND THE LIMIT OF THAT READING IS STATED, NOT HIDDEN: the reference's `54.00` is NOT re-scored
under the cut, because this harness does not have the reference's pipeline. **  *So what is measured
is THIS instrument's limit's dependence on its own tail.  A cut removes information as well as
residual, and both effects are in the number; the receipt says so rather than reporting the move as
if it were the residual's contribution alone.*

⛔ Nothing landed is edited: the bin mask is narrowed on the INSTANCE after construction.

    python3 tail_share.py
"""
import io
import json
import os
import sys

import numpy as np
from scipy.optimize import minimize

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT
BANK = os.path.join(_BTW, 'bank')
REF_RULER = 54.00
R7860_MINIMISED = 69.97
DCHI2 = 2.71
CUTS_REGISTERED = (1500, 1200)      # ⛭ the TWO cuts the registration fixes
CUT_EXTRA = (1800,)                 # ⌗ one more, flagged as beyond the registration
HALF_OF_THE_GAP = 0.5

os.environ['POL_DIR'] = os.path.join(BANK, 'pol_grid_bvel1')
os.environ['PPGRID'] = os.path.join(BANK, 'phiphi_grid_eta4000_bvel1_primnorm1')
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '4')
sys.path.insert(0, os.path.join(_BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_'
                                      'lensing_bandpowers'))
sys.path.insert(0, os.path.join(_BTW, 'r7842_60_polarisation_added_to_the_score_and_the_two_data_'
                                      'the_harness_does_not_have'))


def narrow(mod, SC, M3, lcut):
    """drop every bandpower whose bin REACHES above `lcut`, consistently through the whole score

    ⌗ *`BIN_HI` and not the bin centre: a bin straddling the cut carries the multipoles the cut is
    meant to remove, so it goes.  The count dropped is returned and gated -- a cut that removed
    nothing is a failure of the leg and not a null result.*
    """
    ok = mod.cmb.ok
    keep = SC.BIN_HI[ok] <= int(lcut)
    newok = ok.copy()
    newok[ok] = keep
    dropped = int(ok.sum() - newok.sum())
    base, g, h = mod.cmb.base, dict(mod.cmb.g), dict(mod.cmb.h)
    mod.cmb.base = lambda s, _o=base, _k=keep: np.asarray(_o(s), float)[_k]
    mod.cmb.g = {k: (lambda s, _o=g[k], _k=keep: np.asarray(_o(s), float)[_k]) for k in M3.KEYS4}
    mod.cmb.h = {k: (lambda s, _o=h[k], _k=keep: np.asarray(_o(s), float)[_k]) for k in M3.KEYS4}
    mod.cmb.ok = newok
    mod.cmb.nb = int(newok.sum())
    mod.cmb.F = SC.fisher_for(newok)          # the inverse of the SUB-covariance, not a sub-block
    mod.cmb.d = SC.X_DATA[newok]
    mod.cmb.pos = SC.POSITIVE[newok]
    return dict(lcut=int(lcut), bins_before=int(ok.sum()), bins_after=int(newok.sum()),
                dropped=dropped,
                ell_hi_before=int(SC.BIN_HI[ok].max()),
                ell_hi_after=(int(SC.BIN_HI[newok].max()) if newok.any() else None),
                per_block=[int(((SC.BLOCK == b) & ok).sum() - ((SC.BLOCK == b) & newok).sum())
                           for b in (0, 1, 2)])


def profile(mod, sums, label):
    _prev = {}

    def prof(sum_ev):
        best, bestx = np.inf, None

        def f(v):
            return float(mod.chi2(list(v[:4]) + [sum_ev, float(v[-1])]))
        starts = [[0.0] * 4 + [t0] for t0 in (0.040, 0.054, 0.075, 0.100)]
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
        return best

    s = np.array(sums, float)
    t = np.array([prof(float(v)) for v in s], float)
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
    print('\n  Ⓒ③ %s' % label)
    print('  ' + '-' * 100)
    for a, b, c in zip(s, t, d):
        print('    Sum = %.3f eV   total chi2 %12.4f   delta %8.4f' % (a, b, c))
    print('    minimum at Sum = %.3f eV' % s[i0])
    if dips:
        print('    ⛔ NOT MONOTONIC above the minimum at %s -- NO limit is reported'
              % ', '.join('%.3f eV' % x[0] for x in dips))
    else:
        print('    monotonic above the minimum: converged where the limit is read')
    print('    95 per cent limit: %s meV'
          % (('%.2f' % lim) if (lim is not None and not dips) else 'NOT REPORTED'))
    return dict(sums=[float(v) for v in s], totals=[float(v) for v in t],
                delta=[float(v) for v in d], min_at=float(s[i0]),
                limit_meV=(None if dips else lim), crossing_meV=lim,
                monotonic_above_min=not dips, dips=[list(x) for x in dips])


def _build(M6, M3):
    mod = M6.Model6('lcdm')
    raw = mod.amp_cmb
    mod.amp_cmb = lambda x4, s, _r=raw: _r(x4, s) / 2.0
    return mod


def main():
    print(__doc__)
    print('=' * 100)
    import model3 as M3
    import model6 as M6
    import score_ttteee as SC

    sums = [0.0, 0.03, 0.06, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 0.60]
    out = dict(reference_minimised=REF_RULER, r7860_minimised=R7860_MINIMISED,
               cuts_registered=list(CUTS_REGISTERED), cuts_extra=list(CUT_EXTRA))

    # ── the baseline, on THIS file's own path, so the cuts are differenced against a number this
    #   file measured rather than against one it remembered ──────────────────────────────────────
    mod = _build(M6, M3)
    sums = [s for s in sums if mod.cmb.s_lo - 1e-9 <= s <= mod.cmb.s_hi + 1e-9]
    out['bins_full'] = int(mod.cmb.ok.sum())
    out['ell_hi_full'] = int(SC.BIN_HI[mod.cmb.ok].max())
    base = profile(mod, sums, 'THE BASELINE -- no cut, the ruler minimised')
    out['baseline'] = base
    if base['limit_meV'] is None:
        print('\n  ⛔ the baseline profile did not converge -- no share is reported.\n')
        _save(out)
        return 1
    base['reproduces_r7860'] = bool(abs(base['limit_meV'] - R7860_MINIMISED) < 0.5)
    print('    ⇒ against r7860\'s own %.2f meV on the same configuration: %s (difference %.3f)'
          % (R7860_MINIMISED, 'REPRODUCED' if base['reproduces_r7860'] else '⛔ DOES NOT REPRODUCE',
             base['limit_meV'] - R7860_MINIMISED))
    gap_full = base['limit_meV'] - REF_RULER
    out['gap_full_meV'] = gap_full
    print('    ⇒ the gap this leg prices: %.2f meV' % gap_full)

    out['cuts'] = {}
    for lcut in list(CUTS_REGISTERED) + list(CUT_EXTRA):
        mod = _build(M6, M3)
        info = narrow(mod, SC, M3, lcut)
        print('\n    the cut at ell = %d drops %d of %d bandpowers (TT %d, TE %d, EE %d); the'
              ' highest bin now reaches %s'
              % (lcut, info['dropped'], info['bins_before'], info['per_block'][0],
                 info['per_block'][1], info['per_block'][2], info['ell_hi_after']))
        if info['dropped'] == 0:
            print('      ⛔ the cut removed NOTHING -- the leg fails rather than reporting a null')
            out['cuts'][str(lcut)] = dict(info=info, failed='the cut removed no bandpower')
            continue
        res = profile(mod, sums, 'THE CUT AT ell = %d, the ruler minimised' % lcut)
        res['info'] = info
        if res['limit_meV'] is not None:
            res['moved_meV'] = base['limit_meV'] - res['limit_meV']
            res['share_of_gap'] = res['moved_meV'] / gap_full
            res['gap_after'] = res['limit_meV'] - REF_RULER
            print('    ⇒ the limit moves %.2f meV, which is %.3f of the %.2f meV gap; the gap'
                  ' after the cut is %.2f meV'
                  % (res['moved_meV'], res['share_of_gap'], gap_full, res['gap_after']))
        out['cuts'][str(lcut)] = res

    shares = [out['cuts'][str(c)].get('share_of_gap') for c in CUTS_REGISTERED]
    shares = [v for v in shares if v is not None]
    out['expectation'] = dict(
        text='less than half of the gap moves with the cut, at both registered cuts',
        threshold=HALF_OF_THE_GAP, shares=shares,
        held=bool(shares and all(abs(v) < HALF_OF_THE_GAP for v in shares)))
    print('\n  THE ADJUDICATION')
    print('  ' + '-' * 100)
    print('    registered: %s' % out['expectation']['text'])
    print('    measured shares at the registered cuts: %s'
          % ', '.join('%.3f' % v for v in shares))
    print('    ⇒ the expectation %s' % ('HOLDS' if out['expectation']['held']
                                        else '** FAILS **, reported as failed with the criterion'
                                             ' unmoved'))
    _save(out)
    return 0


def _save(out):
    with io.open(os.path.join(_HERE, 'tail_share.json'), 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=float))


if __name__ == '__main__':
    raise SystemExit(main())
