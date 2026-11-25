# -*- coding: utf-8 -*-
"""Ⓒ③ᵇ⓹ THE LOWER BASIN FOUND AT ONE NODE, CARRIED TO ITS NEIGHBOURS.

`top_node.py` measured that three independent start sets agree to `0.0000` at nine of eleven nodes
and disagree by `12.5367` at `0.400` eV, where one set found `2173.66` and two found `2186.20`.
That is a SECOND BASIN, found at one node by one start set.

⛭ ** THE QUESTION THIS FILE ASKS, AND WHY IT IS THE RIGHT ONE. **  A second basin at a single node
is either a local curiosity or it is the whole upper profile sitting in the wrong basin. The two
cases look identical from one node, and they differ in what the profile MEANS: if the lower basin
exists at `0.500` and `0.600` as well, then every number above the crossing is the higher basin's
and the non-monotonicity is an artefact of which basin each node happened to land in. *So the test
is to take the winning parameters AT `0.400` and start the neighbouring nodes from them.* A basin
that is reachable from its neighbour's solution is one basin; a basin that vanishes one node away
is a feature of that node.

⌗ *This is the same shape as the second basin `r7864` measured and the repaired background removed,
so whether this is its remnant is worth knowing and is reported either way.*

⚠ ** WHAT THIS FILE DOES NOT DO. **  It does not re-read any limit, and it does not decide whether
the convergence discipline should be narrowed. The crossing region agrees to zero between all three
start sets, so nothing here bears on where a limit would be read; it bears only on the top of the
profile, which is what the discipline is refusing on.

    NODE=60 python3 second_basin.py
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
import limits as _L7864                                                    # noqa: E402,F401

os.environ['POL_DIR'] = os.path.join(BANK, 'pol_grid_bvel1_nufd_dneff044')
os.environ['PPGRID'] = os.path.join(BANK, 'phiphi_grid_eta4000_bvel1_primnorm1_nufd_dneff044')

SUMS = [0.0, 0.03, 0.06, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 0.60]
SEED_A = 60          # the start set that found the lower basin at 0.400
SEED_B = 7870        # one of the two that did not


def _model():
    import model6 as M6
    mod = M6.Model6('lcdm')
    raw = mod.amp_cmb
    mod.amp_cmb = lambda x4, s, _r=raw: _r(x4, s) / 2.0
    return mod


def _fit(mod, s, starts, tol=1e-8):
    def f(v):
        return float(mod.chi2(list(v[:4]) + [s, float(v[4])]))
    best, bestx = np.inf, None
    for x0 in starts:
        r = minimize(f, x0, method='Nelder-Mead',
                     options=dict(xatol=tol, fatol=tol, maxiter=40000, maxfev=40000))
        if np.isfinite(r.fun) and r.fun < best:
            best, bestx = float(r.fun), list(r.x)
    if bestx is not None:
        r = minimize(f, bestx, method='Nelder-Mead',
                     options=dict(xatol=1e-9, fatol=1e-9, maxiter=40000, maxfev=40000))
        if np.isfinite(r.fun) and r.fun < best:
            best, bestx = float(r.fun), list(r.x)
    return best, bestx


def starts_for(seed, n_x):
    rng = np.random.default_rng(seed)
    out = [[0.0, 0.0, 0.0, 0.0, t] for t in (0.030, 0.040, 0.054, 0.075, 0.100, 0.140)]
    for _ in range(n_x):
        for t in (0.054, 0.100):
            out.append(list(rng.normal(0.0, 1.0, 4)) + [t])
    return out


def main():
    print(__doc__)
    print('=' * 104)
    out = {}
    mod = _model()

    print('\n  ⓵ THE TWO BASINS AT 0.400 eV, AND WHAT EACH ONE\'S PARAMETERS ARE')
    print('  ' + '-' * 104)
    lo, xlo = _fit(mod, 0.40, starts_for(SEED_A, 3))
    hi, xhi = _fit(mod, 0.40, starts_for(SEED_B, 10))
    print('    the lower basin  chi2 %12.4f   x4 %s  tau %.5f'
          % (lo, np.array2string(np.asarray(xlo[:4]), precision=4), xlo[4]))
    print('    the higher basin chi2 %12.4f   x4 %s  tau %.5f'
          % (hi, np.array2string(np.asarray(xhi[:4]), precision=4), xhi[4]))
    print('    ⇒ they differ by %.4f in chi2, and the parameters differ by %s'
          % (abs(hi - lo), np.array2string(np.asarray(xhi[:4]) - np.asarray(xlo[:4]),
                                           precision=4)))
    out['at_0400'] = dict(lower=lo, higher=hi, x_lower=[float(v) for v in xlo],
                          x_higher=[float(v) for v in xhi], gap=float(abs(hi - lo)))

    print('\n  ⓶ THE LOWER BASIN CARRIED TO EVERY OTHER NODE -- is it one basin or one node?')
    print('  ' + '-' * 104)
    #: the whole point: start each node FROM the lower basin's own solution at 0.400, so a basin
    #: that exists there too is found, and compare against the agreed column
    agreed = {}
    carried = {}
    for s in SUMS:
        if not (mod.cmb.s_lo - 1e-9 <= s <= mod.cmb.s_hi + 1e-9):
            continue
        a, _ = _fit(mod, s, starts_for(SEED_B, 10))
        c, _ = _fit(mod, s, [list(xlo)])
        agreed[s], carried[s] = a, c
        mark = ''
        if c < a - 1e-4:
            mark = '   ⬇ LOWER by %.4f -- the basin reaches this node' % (a - c)
        print('    Sum = %.3f eV   agreed %12.4f   from the lower basin %12.4f%s'
              % (s, a, c, mark))
    out['agreed'] = {str(k): float(v) for k, v in agreed.items()}
    out['carried'] = {str(k): float(v) for k, v in carried.items()}

    reaches = sorted(s for s in agreed if carried[s] < agreed[s] - 1e-4)
    print('\n  ⓷ THE VERDICT ON THE UPPER PROFILE')
    print('  ' + '-' * 104)
    print('    the lower basin reaches: %s'
          % (', '.join('%.3f eV' % s for s in reaches) if reaches else 'NO other node'))
    #: with the basin carried wherever it reaches, is the profile monotonic above its minimum?
    best = {s: min(agreed[s], carried[s]) for s in agreed}
    ks = sorted(best)
    vals = [best[s] for s in ks]
    i0 = int(np.argmin(vals))
    dips = [(float(ks[k]), float(vals[k] - vals[k - 1]))
            for k in range(i0 + 1, len(ks)) if vals[k] < vals[k - 1] - 1e-6]
    print('    taking the LOWER of the two at every node, the minimum is at %.3f eV and the dips '
          'above it are: %s'
          % (ks[i0], ', '.join('%.3f eV (%+.4f)' % d for d in dips) if dips else 'NONE'))
    out['best_of_both'] = dict(sums=[float(s) for s in ks], totals=[float(v) for v in vals],
                               min_at=float(ks[i0]), dips=[list(d) for d in dips],
                               monotonic_above_min=not dips)
    if reaches and not dips:
        verdict = ('** ONE BASIN, AND THE UPPER PROFILE WAS IN THE WRONG ONE. **  The lower basin '
                   'reaches other nodes, and once each node is taken in it the profile is '
                   'MONOTONIC above its minimum.  ⇒ the non-monotonicity was which basin each node '
                   'landed in, not the model and not the grid\'s edge')
    elif reaches and dips:
        verdict = ('** ONE BASIN, AND THE PROFILE IS STILL NOT MONOTONIC IN IT. **  The lower '
                   'basin reaches other nodes, so the upper profile was mixing basins -- but '
                   'taking the lower everywhere does not make it monotonic, so a second cause '
                   'remains and is NOT named here')
    elif not reaches and not dips:
        verdict = ('** THE LOWER BASIN IS ONE NODE\'S ONLY, AND REMOVING IT MAKES THE PROFILE '
                   'MONOTONIC. **  ⇒ the dip was that single node')
    else:
        verdict = ('** THE LOWER BASIN IS ONE NODE\'S ONLY, AND THE PROFILE IS NON-MONOTONIC '
                   'EITHER WAY. **  ⇒ reported as unseparated: the basin is local and something '
                   'else carries the dip')
    print('    %s' % verdict)
    out['verdict'] = verdict
    with io.open(os.path.join(_HERE, 'second_basin.json'), 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=float))
    print('')
    return 0


if __name__ == '__main__':
    sys.exit(main())
