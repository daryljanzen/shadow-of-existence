# -*- coding: utf-8 -*-
"""⛭⛭ THE LOWER ENVELOPE CLOSED UNDER CROSS-SEEDING — and a correction to this revision's own
verdict on the separating rung.

`limits_separating.py` read the separating rung two ways and its verdict logic asked one crude
question: *does the envelope dip at all?*  It did, so the file reported the rung UNSEPARATED. ** That
verdict is not what its own numbers say, and this file is the correction. **

  ⓵ The raw reading dips at `0.600` eV by `-2.85`. **The envelope REMOVES that dip** — on the
    envelope `0.600` sits above `0.500`, because the envelope brought `0.500` down by `18.3`.
  ⓶ What the envelope leaves is a dip at `0.200` eV of **`-0.0206`** — two orders of magnitude
    smaller, and at a node whose neighbour `0.150` the seeds improved by only `0.21` where `0.200`
    came down by `2.22`.
⇒ *** That is a RAGGED LOWER ENVELOPE: the seeds, taken from another bank's basins, help some nodes
more than others, so the envelope is not converged and its raggedness is seed luck rather than a
feature of the model.  A verdict about the model drawn from it would be the same mistake the edge
test made earlier in this revision. ***

** THE FIX, WHICH IS THE STANDARD ONE FOR A RAGGED ENVELOPE: CLOSE IT UNDER CROSS-SEEDING. **  Every
node is restarted from EVERY node's current best parameters, and the pass repeats until no node
improves. *A node cannot then be left in a higher basin that any other node has already found a way
into, and the result no longer depends on which bank the seeds came from.*

⚠ ** WHAT IS STILL NOT CLAIMED. **  A closed envelope is a lower envelope over the basins REACHED,
not a proved global minimum. Cross-seeding cannot find a basin no node ever entered. *So a crossing
read here is still reported as an envelope crossing and never as a limit,* and the honest negative
claim is the only one this revision makes about the minimised column.

    NODE=60 python3 envelope_closed.py
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
import limits as L7864                                                      # noqa: E402

#: the two rungs this file closes the envelope on: the separating grid, and the corrected-offset
#: bank, so the comparison between them is made on ONE method rather than two
RUNGS = {
    'nufd_only': (os.path.join(BANK, 'pol_grid_bvel1_nufd_only'),
                  os.path.join(BANK, 'phiphi_grid_eta4000_bvel1_primnorm1_nufd_only')),
    'nufd_dneff044': (os.path.join(BANK, 'pol_grid_bvel1_nufd_dneff044'),
                      os.path.join(BANK, 'phiphi_grid_eta4000_bvel1_primnorm1_nufd_dneff044')),
}
WHICH = os.environ.get('RUNG', 'nufd_only')
POL, PP = RUNGS[WHICH]
os.environ['POL_DIR'] = POL
os.environ['PPGRID'] = PP

DCHI2 = 2.71
SUMS = [0.0, 0.03, 0.06, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 0.60]
MAX_PASSES = 6


def _fit(mod, s, starts):
    def f(v):
        return float(mod.chi2(list(v[:4]) + [s, float(v[4])]))
    best, bestx = np.inf, None
    for x0 in starts:
        r = minimize(f, x0, method='Nelder-Mead',
                     options=dict(xatol=1e-8, fatol=1e-8, maxiter=40000, maxfev=40000))
        if np.isfinite(r.fun) and r.fun < best:
            best, bestx = float(r.fun), list(r.x)
    if bestx is not None:
        r = minimize(f, bestx, method='Nelder-Mead',
                     options=dict(xatol=1e-9, fatol=1e-9, maxiter=40000, maxfev=40000))
        if np.isfinite(r.fun) and r.fun < best:
            best, bestx = float(r.fun), list(r.x)
    return best, bestx


def _cold(seed=7870, n_x=6):
    rng = np.random.default_rng(seed)
    out = [[0.0, 0.0, 0.0, 0.0, t] for t in (0.030, 0.040, 0.054, 0.075, 0.100, 0.140)]
    for _ in range(n_x):
        for t in (0.054, 0.100):
            out.append(list(rng.normal(0.0, 1.0, 4)) + [t])
    return out


def _read(ss, tot):
    tot = np.asarray(tot, float)
    i0 = int(np.argmin(tot))
    d = tot - tot[i0]
    dips = [(float(ss[k]), float(tot[k] - tot[k - 1]))
            for k in range(i0 + 1, len(ss)) if tot[k] < tot[k - 1] - 1e-6]
    above = [k for k in range(i0 + 1, len(ss)) if d[k] >= DCHI2]
    cross = None
    if above:
        k = above[0]
        cross = float(ss[k - 1] + (DCHI2 - d[k - 1]) * (ss[k] - ss[k - 1])
                      / (d[k] - d[k - 1])) * 1000.0
    return dict(sums=[float(v) for v in ss], totals=[float(v) for v in tot],
                delta=[float(v) for v in d], min_at=float(ss[i0]),
                dips=[list(x) for x in dips], monotonic_above_min=not dips,
                crossing_meV=cross)


def closed_envelope(mod, label):
    """every node restarted from EVERY node's best, until no node improves"""
    ss = [s for s in SUMS if mod.cmb.s_lo - 1e-9 <= s <= mod.cmb.s_hi + 1e-9]
    best, bx = {}, {}
    cold = _cold()
    for s in ss:
        best[s], bx[s] = _fit(mod, s, cold)
    print('\n  %s' % label)
    print('  ' + '-' * 104)
    print('    pass 0 (cold starts only):  %s' % ' '.join('%.2f' % best[s] for s in ss))
    passes = 0
    for p in range(1, MAX_PASSES + 1):
        pool = [list(bx[t]) for t in ss if bx[t] is not None]
        improved = 0
        for s in ss:
            b, x = _fit(mod, s, pool)
            if b < best[s] - 1e-7:
                best[s], bx[s] = b, x
                improved += 1
        passes = p
        print('    pass %d: %d node(s) improved' % (p, improved))
        if improved == 0:
            break
    tot = [best[s] for s in ss]
    out = _read(ss, tot)
    out['passes'] = passes
    out['x_at_node'] = {str(s): [float(v) for v in bx[s]] for s in ss if bx[s] is not None}
    print('    the closed envelope:')
    for s in ss:
        print('      Sum = %.3f eV   total chi2 %12.4f' % (s, best[s]))
    print('    minimum at Sum = %.3f eV;  dips above it: %s'
          % (out['min_at'], ', '.join('%.3f eV (%+.4f)' % tuple(x) for x in out['dips'])
             if out['dips'] else 'NONE'))
    print('    the %.2f crossing on the CLOSED envelope: %s meV  ⌗ *an envelope crossing, NOT a '
          'limit*' % (DCHI2, ('%.2f' % out['crossing_meV']) if out['crossing_meV'] else 'not '
                      'reached'))
    return out


def main():
    print(__doc__)
    print('=' * 104)
    print('\n  the rung under test: %s' % WHICH)
    import model3 as M3                                                     # noqa: E402
    import distances as DI                                                  # noqa: E402
    import model6 as M6                                                     # noqa: E402
    print('  the CMB grid in use     : %s' % os.path.basename(os.environ['POL_DIR']))
    print('  the lensing grid in use : %s' % os.path.basename(M6.GRID))
    out = {'rung': WHICH, 'pol_dir': os.path.basename(POL), 'pp_grid': os.path.basename(M6.GRID),
           'max_passes': MAX_PASSES}

    def _mod():
        m = M6.Model6('lcdm')
        raw = m.amp_cmb
        m.amp_cmb = lambda x4, s, _r=raw: _r(x4, s) / 2.0
        return m

    out['minimised'] = closed_envelope(
        _mod(), 'THE RULER MINIMISED, on the envelope CLOSED under cross-seeding')

    r_inst = L7864.Ruler(os.path.join(R7864, 'rd_grid_nufd.npz'), 'r_drag',
                         "this instrument's own drag epoch ON THE REPAIRED BACKGROUND",
                         'instrument')
    modc = _mod()
    L7864.attach(modc, r_inst, M3, DI)
    out['calibrated'] = closed_envelope(
        modc, 'CALIBRATED on the repaired drag epoch, envelope CLOSED under cross-seeding')

    m = out['minimised']
    print('\n  THE VERDICT ON THIS RUNG')
    print('  ' + '-' * 104)
    if m['monotonic_above_min']:
        verdict = ('** THE CLOSED ENVELOPE IS MONOTONIC. **  ⇒ *** The non-monotonicity on this '
                   'rung was the profile sitting in mixed basins, exactly as on the rungs that '
                   'carry an offset.  So basin mixing is GENERAL to this score and not a property '
                   'of any one bank -- and the order\'s fork named the repaired background and the '
                   'N_eff ruling as the alternatives, when the unreadability is NEITHER. ***  '
                   '⌗ The crossing above is an ENVELOPE crossing over the basins reached, and is '
                   'not reported as a limit.')
    else:
        verdict = ('** THE CLOSED ENVELOPE STILL DIPS. **  Cross-seeding cannot find a basin no '
                   'node ever entered, so this is reported as UNSEPARATED on this rung rather '
                   'than named -- and the dips are printed above with their sizes so the next '
                   'revision can see whether they are of the order the raw dip was')
    print('    %s' % verdict)
    out['verdict'] = verdict
    with io.open(os.path.join(_HERE, 'envelope_closed_%s.json' % WHICH), 'w',
                 encoding='utf-8') as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=float))
    print('')
    return 0


if __name__ == '__main__':
    sys.exit(main())
