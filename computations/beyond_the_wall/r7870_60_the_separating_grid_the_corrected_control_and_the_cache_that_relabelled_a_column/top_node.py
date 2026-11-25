# -*- coding: utf-8 -*-
"""Ⓒ③ THE DIP AT THE TOP NODE: is it the grid's edge, a convergence failure, or a feature?

Order `r7869` item ③, and it is run BEFORE any limit is read through this profile, as the order
requires. Item ① measured the dip: on the bank at the corrected offset the minimised profile rises
monotonically from its minimum at `0.060` eV to `0.500` eV and then **falls** by `3.35` in `chi2`
at `0.600`, which is the top node of the sum axis. The calibrated profile has no dip at all.

⛭ ** THE FIRST THING TO GET RIGHT, BECAUSE IT CHANGES WHAT THE TEST IS. **  `0.600` eV is a BANK
NODE, not a point between nodes. The model's sum dependence is a cubic spline through the banked
sums, and a spline AT a knot returns that knot's own value, so at `0.600` the model is the banked
spectra themselves and not an extrapolation. *So "the grid's edge" cannot mean the spline running
off the end of its data here: whatever is happening at `0.600` is happening in the bank's own top
point or in the fit at it.* That leaves three candidates, and this file separates them:

  ⓵ **a convergence failure at `0.500`** -- if that node's minimiser stopped high, the dip is an
    artefact of the node BELOW it rather than of the top one.  Tested by COLD starts, which is one
    of the two tests the order names, and by many more of them than the profile uses.
  ⓶ **the top bank point itself** -- a point that solved to something slightly different from its
    neighbours.  Tested on the bank's own spectra, independent of any fit.
  ⓷ **a feature of the model** -- if the dip survives ⓵ and ⓶ it is neither the edge nor the
    minimiser, and it is reported as a fact about the model rather than tidied away.

⚠ ** AND ONE FACT THAT IS REPORTED WHICHEVER WAY ⓵-⓷ GO, because it bears on what the discipline
is refusing. **  The `2.71` crossing on this profile sits between `0.150` and `0.200` eV. The dip
is at `0.600`. *The discipline refuses a limit on the strength of a non-monotonicity three times
higher than the crossing it suppresses.* That is stated here as a measurement, and whether the
discipline should be narrowed is NOT decided here -- it is the convergence rule's own question and
it belongs to whoever owns that rule, with this measurement attached.

    NODE=60 python3 top_node.py
"""
import io
import json
import os
import sys

import numpy as np
from scipy.optimize import minimize

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
BANK = os.path.join(_BTW, 'bank')
R7864 = os.path.join(_BTW, 'r7864_60_the_massive_neutrino_background_given_its_fermi_dirac_'
                           'density_and_both_limits_re_read')
sys.path.insert(0, R7864)

NEWBANK = os.path.join(BANK, 'pol_grid_bvel1_nufd_dneff044')
NEWPP = os.path.join(BANK, 'phiphi_grid_eta4000_bvel1_primnorm1_nufd_dneff044')
os.environ['POL_DIR'] = NEWBANK
os.environ['PPGRID'] = NEWPP

DCHI2 = 2.71
SUMS = [0.0, 0.03, 0.06, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 0.60]


def _model():
    import model6 as M6
    mod = M6.Model6('lcdm')
    raw = mod.amp_cmb
    mod.amp_cmb = lambda x4, s, _r=raw: _r(x4, s) / 2.0      # r7866's own halving, carried
    return mod


def _fit(mod, s, starts, xatol=1e-7, fatol=1e-7):
    """the best of `starts`, with NO value carried in from another node"""
    def f(v):
        return float(mod.chi2(list(v[:4]) + [s, float(v[4])]))
    best, bestx = np.inf, None
    for x0 in starts:
        r = minimize(f, x0, method='Nelder-Mead',
                     options=dict(xatol=xatol, fatol=fatol, maxiter=40000, maxfev=40000))
        if np.isfinite(r.fun) and r.fun < best:
            best, bestx = float(r.fun), list(r.x)
    if bestx is not None:
        r = minimize(f, bestx, method='Nelder-Mead',
                     options=dict(xatol=1e-8, fatol=1e-8, maxiter=40000, maxfev=40000))
        if np.isfinite(r.fun) and r.fun < best:
            best, bestx = float(r.fun), list(r.x)
    return best, bestx


def cold_starts(n_tau=6, n_x=3, seed=60):
    """a start grid that carries nothing from a neighbouring node: taus spread, x4 spread"""
    rng = np.random.default_rng(seed)
    out = [[0.0, 0.0, 0.0, 0.0, t] for t in (0.030, 0.040, 0.054, 0.075, 0.100, 0.140)[:n_tau]]
    for _ in range(n_x):
        for t in (0.054, 0.100):
            out.append(list(rng.normal(0.0, 1.0, 4)) + [t])
    return out


def main():
    print(__doc__)
    print('=' * 104)
    out = {'top_node_eV': SUMS[-1], 'crossing_target': DCHI2}

    mod = _model()
    ss = [s for s in SUMS if mod.cmb.s_lo - 1e-9 <= s <= mod.cmb.s_hi + 1e-9]
    out['sums'] = ss

    print('\n  Ⓒ③ᵇ⓵ COLD STARTS AT EVERY NODE -- nothing carried in from the node below')
    print('  ' + '-' * 104)
    starts = cold_starts()
    print('    %d independent start(s) per node, tighter tolerances than the profile uses' % len(starts))
    cold = []
    for s in ss:
        b, bx = _fit(mod, s, starts)
        cold.append(b)
        print('    Sum = %.3f eV   cold total chi2 %12.4f' % (s, b))
    cold = np.asarray(cold, float)
    i0 = int(np.argmin(cold))
    d = cold - cold[i0]
    dips = [(float(ss[k]), float(cold[k] - cold[k - 1]))
            for k in range(i0 + 1, len(ss)) if cold[k] < cold[k - 1] - 1e-6]
    above = [k for k in range(i0 + 1, len(ss)) if d[k] >= DCHI2]
    cross = None
    if above:
        k = above[0]
        cross = float(ss[k - 1] + (DCHI2 - d[k - 1]) * (ss[k] - ss[k - 1])
                      / (d[k] - d[k - 1])) * 1000.0
    print('    minimum at Sum = %.3f eV;  dips above it: %s'
          % (ss[i0], ', '.join('%.3f eV (%+.4f)' % x for x in dips) if dips else 'NONE'))
    print('    the 2.71 crossing on the cold profile: %s meV'
          % (('%.2f' % cross) if cross is not None else 'not reached'))
    out['cold'] = dict(totals=[float(v) for v in cold], min_at=float(ss[i0]),
                       delta=[float(v) for v in d], dips=[list(x) for x in dips],
                       monotonic_above_min=not dips, crossing_meV=cross,
                       n_starts=len(starts))

    print('\n  Ⓒ③ᵇ⓶ THE TWO TOP NODES, HAMMERED -- is 0.500 the one that stopped high?')
    print('  ' + '-' * 104)
    hard = {}
    big = cold_starts(n_tau=6, n_x=10, seed=7870)
    for s in (0.40, 0.50, 0.60):
        if s not in ss:
            continue
        b, bx = _fit(mod, s, big, xatol=1e-8, fatol=1e-8)
        hard[s] = b
        print('    Sum = %.3f eV   best of %d start(s) %12.4f' % (s, len(big), b))
    out['hammered'] = {str(k): float(v) for k, v in hard.items()}
    if 0.50 in hard and 0.60 in hard:
        still = hard[0.60] < hard[0.50] - 1e-6
        print('    ⇒ with %d starts at each, the top node is %s the node below it: %.4f against '
              '%.4f  ⇒ the dip %s' % (len(big), 'STILL BELOW' if still else 'NO LONGER BELOW',
                                      hard[0.60], hard[0.50],
                                      'SURVIVES better convergence' if still
                                      else 'was a CONVERGENCE FAILURE at the node below'))
        out['dip_survives_convergence'] = bool(still)

    print('\n  Ⓒ③ᵇ⓷ THE BANK\'S OWN TOP POINT, WITH NO FIT IN IT AT ALL')
    print('  ' + '-' * 104)
    #: the banked spectra themselves, summarised per sum node, so a point that solved to something
    #: different from its neighbours shows up without any minimiser in the way
    tags = [('Sm12', -0.12), ('Sm06', -0.06), ('S000', 0.0), ('S006', 0.06),
            ('S015', 0.15), ('S030', 0.30), ('S045', 0.45), ('S060', 0.60)]
    rows = []
    for tag, s in tags:
        z = np.load(os.path.join(NEWBANK, 'lcdm_%s.npz' % tag), allow_pickle=True)
        tt = np.asarray(z['Dl'], float)
        rows.append((s, tag, float(np.sum(tt)), float(np.max(tt))))
    print('    the control\'s banked TT, summed and peaked, across the sum axis:')
    prev = None
    kinks = []
    for s, tag, tot, pk in rows:
        step = '' if prev is None else '   step %+0.6e' % (tot - prev)
        print('      Sum = %+0.3f  %-5s  sum(Dl) %14.6e   max(Dl) %12.6e%s'
              % (s, tag, tot, pk, step))
        prev = tot
    #: a KINK is a step whose sign differs from the trend of the steps before it
    steps = [rows[k][2] - rows[k - 1][2] for k in range(1, len(rows))]
    if len(steps) >= 2:
        signs = [1 if v > 0 else -1 for v in steps]
        kinks = [tags[k + 1][1] for k in range(1, len(signs)) if signs[k] != signs[k - 1]]
    print('    sign changes in the step of sum(Dl) across the axis: %s'
          % (', '.join('%.3f eV' % v for v in kinks) if kinks else 'NONE -- the bank is smooth'))
    out['bank'] = dict(rows=[[s, tag, tot, pk] for s, tag, tot, pk in rows],
                       steps=[float(v) for v in steps],
                       sign_changes_eV=[float(v) for v in kinks])

    print('\n  Ⓒ③ᵇ⓸ WHERE THE DIP IS RELATIVE TO THE CROSSING IT SUPPRESSES')
    print('  ' + '-' * 104)
    if cross is not None:
        print('    the 2.71 crossing sits at %.1f meV; the dip is at %.0f meV  ⇒ the dip is %.1fx '
              'higher than the limit the discipline is refusing to report'
              % (cross, SUMS[-1] * 1000.0, SUMS[-1] * 1000.0 / cross))
        out['dip_over_crossing'] = float(SUMS[-1] * 1000.0 / cross)
    print('    ⌗ stated as a measurement.  Whether the convergence rule should be narrowed to a '
          'neighbourhood of the crossing is that rule\'s own question, not this file\'s, and it '
          'is routed with this number rather than decided here.')

    print('\n  THE VERDICT')
    print('  ' + '-' * 104)
    if out.get('dip_survives_convergence') is False:
        verdict = ('⓵ A CONVERGENCE FAILURE AT THE NODE BELOW -- not the grid\'s edge and not a '
                   'feature: with many cold starts the node below the top one comes down and the '
                   'profile is monotonic')
    elif kinks:
        verdict = ('⓶ THE BANK\'S TOP POINT -- its own banked spectra turn the trend, with no fit '
                   'involved, so the dip is in the bank and not in the fit')
    elif out.get('dip_survives_convergence'):
        verdict = ('⓷ A FEATURE OF THE MODEL -- the dip survives cold starts and many-start '
                   'convergence, and the bank is smooth across the axis, so it is neither the '
                   'grid\'s edge nor the minimiser.  ⛔ And the top node is a BANK NODE, where a '
                   'spline returns the knot\'s own value, so there is no extrapolation to blame')
    else:
        verdict = 'NOT SEPARATED by these three tests -- reported as unseparated rather than named'
    print('    %s' % verdict)
    out['verdict'] = verdict
    with io.open(os.path.join(_HERE, 'top_node.json'), 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=float))
    print('')
    return 0


if __name__ == '__main__':
    sys.exit(main())
