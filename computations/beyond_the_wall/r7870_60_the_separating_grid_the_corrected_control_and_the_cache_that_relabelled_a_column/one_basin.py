# -*- coding: utf-8 -*-
"""⛔⛭⛭ BOTH LIMITS ON A PROFILE THAT CANNOT MIX BASINS -- and the unreadable limit was the PROFILER.

`second_basin.py` measured that the lower basin found at `0.400` eV reaches `0.200`, `0.250`,
`0.300`, `0.400` and `0.500`, going deeper at every one of them, and that at `0.600` it gives
nothing further. ⇒ *** So `0.600` was ALREADY in the lower basin while `0.500` was in the higher
one, and the dip at the top node simply WAS the basin switch. *** Taking the lower of the two at
every node, the profile is monotonic above its minimum and there is no dip to refuse a limit on.

** WHAT THAT MEANS FOR WHAT THIS LINE HAS BEEN REPORTING, STATED PLAINLY BECAUSE IT CUTS AGAINST
THIS SEAT'S OWN RESULTS. **  `r7866` reported NO READABLE MINIMISED LIMIT on the re-solved bank,
`r7870`'s item ① reported the same on the bank at the corrected offset, and order `r7869` ruled a
thirty-two-point separating grid to decide whether the repaired background or the `N_eff` ruling
carried that unreadability. *If the unreadability is the profiler mixing basins, then it is NEITHER
of them, and the fork those two branches belong to has no slot for the answer.*

⚠ ** WHAT THIS FILE CAN AND CANNOT ESTABLISH. **  It reads both limits on the best-known envelope:
at every node it starts from cold starts, from the node below (as the original profiler does), AND
from each known basin's own solution, and takes the lowest. *That is a LOWER ENVELOPE of what has
been found, not a proof of the global minimum.* A third basin deeper still would move these numbers
again, and nothing here rules one out. So the limit below is reported as `the limit on the
one-basin envelope`, and the claim that is actually solid is the NEGATIVE one: the earlier
unreadability is explained by basin mixing, which is a defect of the profile and not of the model.

⌗ *And one tension with this line's own record, reported rather than reconciled: `r7864` measured a
second basin and reported that the repaired background did not survive it. A second basin is
plainly present here, ON the repaired background. Whether it is the same object is NOT settled by
this file, and it is named so that it is not quietly assumed either way.*

    NODE=60 python3 one_basin.py
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

os.environ['POL_DIR'] = os.path.join(BANK, 'pol_grid_bvel1_nufd_dneff044')
os.environ['PPGRID'] = os.path.join(BANK, 'phiphi_grid_eta4000_bvel1_primnorm1_nufd_dneff044')

DCHI2 = 2.71
SUMS = [0.0, 0.03, 0.06, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 0.60]
REF_RULER = 54.00
REF_CALIB = 30.56
R7866_CALIBRATED = 185.69
ITEM1_CALIBRATED = 185.92           # what item ① read on this same bank, mixed basins and all


def _starts(seed, n_x):
    rng = np.random.default_rng(seed)
    out = [[0.0, 0.0, 0.0, 0.0, t] for t in (0.030, 0.040, 0.054, 0.075, 0.100, 0.140)]
    for _ in range(n_x):
        for t in (0.054, 0.100):
            out.append(list(rng.normal(0.0, 1.0, 4)) + [t])
    return out


def _fit(mod, s, starts, ruler=None, free=(0, 1, 2, 3)):
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


def envelope(mod, label, seeds):
    """the lowest total found at each node, from cold starts, the node below, and every known basin"""
    ss = [s for s in SUMS if mod.cmb.s_lo - 1e-9 <= s <= mod.cmb.s_hi + 1e-9]
    tot, xs = [], []
    prev = None
    print('\n  %s' % label)
    print('  ' + '-' * 104)
    for s in ss:
        starts = _starts(7870, 6)
        if prev is not None:
            starts.insert(0, list(prev))                 # warm, as the original profiler does
        for sd in seeds:
            starts.insert(0, list(sd))                   # every known basin's own solution
        b, bx = _fit(mod, s, starts)
        tot.append(b)
        xs.append(bx)
        prev = bx
        print('    Sum = %.3f eV   total chi2 %12.4f' % (s, b))
    tot = np.asarray(tot, float)
    i0 = int(np.argmin(tot))
    d = tot - tot[i0]
    dips = [(float(ss[k]), float(tot[k] - tot[k - 1]))
            for k in range(i0 + 1, len(ss)) if tot[k] < tot[k - 1] - 1e-6]
    above = [k for k in range(i0 + 1, len(ss)) if d[k] >= DCHI2]
    lim = None
    if above:
        k = above[0]
        lim = float(ss[k - 1] + (DCHI2 - d[k - 1]) * (ss[k] - ss[k - 1])
                    / (d[k] - d[k - 1])) * 1000.0
    print('    minimum at Sum = %.3f eV;  dips above it: %s'
          % (ss[i0], ', '.join('%.3f eV' % x[0] for x in dips) if dips else 'NONE'))
    print('    the %.2f crossing: %s meV%s'
          % (DCHI2, ('%.2f' % lim) if lim is not None else 'not reached',
             '' if not dips else '   ⛔ but the profile DIPS, so this is not reported as a limit'))
    return dict(sums=[float(v) for v in ss], totals=[float(v) for v in tot],
                delta=[float(v) for v in d], min_at=float(ss[i0]),
                dips=[list(x) for x in dips], monotonic_above_min=not dips,
                crossing_meV=lim, limit_meV=(None if dips else lim),
                x_at_node=[list(map(float, x)) if x else None for x in xs])


def main():
    print(__doc__)
    print('=' * 104)
    import model3 as M3                                                     # noqa: E402
    import distances as DI                                                  # noqa: E402
    import model6 as M6                                                     # noqa: E402
    out = {}

    def _mod():
        m = M6.Model6('lcdm')
        raw = m.amp_cmb
        m.amp_cmb = lambda x4, s, _r=raw: _r(x4, s) / 2.0
        return m

    #: the two basins' own solutions at 0.400, as `second_basin.py` found them
    mod = _mod()
    lo_b = _fit(mod, 0.40, _starts(60, 3))[1]
    hi_b = _fit(mod, 0.40, _starts(7870, 10))[1]
    seeds = [lo_b, hi_b]
    print('\n  THE SEEDS -- every known basin, carried to every node')
    print('  ' + '-' * 104)
    for nm, sd in (('lower', lo_b), ('higher', hi_b)):
        print('    the %-6s basin at 0.400 eV: x4 %s  tau %.5f'
              % (nm, np.array2string(np.asarray(sd[:4]), precision=4), sd[4]))
    out['seeds'] = dict(lower=[float(v) for v in lo_b], higher=[float(v) for v in hi_b])

    out['minimised'] = envelope(
        _mod(), 'THE RULER MINIMISED, on the one-basin envelope -- item ① read NO readable limit '
                'here', seeds)

    r_inst = L7864.Ruler(os.path.join(R7864, 'rd_grid_nufd.npz'), 'r_drag',
                         "this instrument's own drag epoch ON THE REPAIRED BACKGROUND",
                         'instrument')
    modc = _mod()
    L7864.attach(modc, r_inst, M3, DI)
    out['calibrated'] = envelope(
        modc, 'CALIBRATED on the repaired drag epoch, one-basin envelope -- item ① read %.2f'
              % ITEM1_CALIBRATED, seeds)

    mini, cal = out['minimised'], out['calibrated']
    print('\n  THE ADJUDICATION')
    print('  ' + '-' * 104)
    print('    minimised  %s meV on the envelope, against the reference\'s %.2f'
          % (('%.2f' % mini['limit_meV']) if mini['limit_meV'] else 'STILL NOT REPORTED',
             REF_RULER))
    print('    calibrated %s meV against the ordered %.2f  (item ① read %.2f on the same bank '
          'with the basins mixed)'
          % (('%.2f' % cal['limit_meV']) if cal['limit_meV'] else 'NOT REPORTED',
             REF_CALIB, ITEM1_CALIBRATED))
    readable = bool(mini['limit_meV'] is not None)
    out['adjudication'] = dict(
        limit_minimised=mini['limit_meV'], limit_calibrated=cal['limit_meV'],
        reference_minimised=REF_RULER, reference_calibrated=REF_CALIB,
        item1_calibrated_mixed_basins=ITEM1_CALIBRATED,
        minimised_readable_on_one_basin=readable,
        what_the_unreadability_was=(
            'THE PROFILER MIXING BASINS -- neither the repaired background nor the N_eff ruling. '
            'The dip the discipline refused on was the switch from the higher basin to the lower '
            'one between the two top nodes.' if readable else
            'NOT the basin mixing alone -- the envelope still dips, so a further cause remains '
            'and is not named here'),
        is_a_lower_envelope_not_a_proved_global_minimum=True,
        caveat='a third basin deeper still would move these numbers; nothing here rules one out, '
               'so the solid claim is the negative one about the earlier unreadability')
    print('    ⇒ %s' % out['adjudication']['what_the_unreadability_was'])
    print('    ⌗ reported as the limit on the one-basin ENVELOPE, which is a lower bound on what '
          'has been found and not a proved global minimum')
    with io.open(os.path.join(_HERE, 'one_basin.json'), 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=float))
    print('')
    return 0


if __name__ == '__main__':
    sys.exit(main())
