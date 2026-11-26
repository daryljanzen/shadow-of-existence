# -*- coding: utf-8 -*-
"""r7875+cc66 item ⑭ -- THE TWO-START MIDPOINT TEST AT Sigma = 0.20, 0.30, 0.50 and 0.60, BOTH RULERS.

`r7873` ran this at `Σ = 0.400` only and found ONE BASIN on both rulers, and held the scope to that
sum.  This extends it across the range so "one branch" is established or is not.

⛔ TWO OF THE FOUR SUMS HAVE NO BANKED BEST FIT.  `r7853`'s bank holds 0.000-0.300 and 0.400.
   `Σ = 0.50` and `0.60` are NOT there.  At `r7873` the two starts set the other four parameters to
   the banked best fit for that ruler; with no bank there is nothing to read, so a COLD profile run
   produces that point first.  Which sums were read and which were computed is printed and recorded.

⛔ THE CRITERION IS `r7873`'s, SCALED.  The midpoint of the two converged five-parameter points is
   scored; a barrier is compared against the profiler's own `fatol = 5e-3` and against the
   one-parameter unit `Δχ² = 1`.  A ridge under either is NOT a basin boundary.  The UNSCALED form
   is not used: at `r7873` it called a barrier a hundredth of `fatol` a second basin, and that was
   my defect, recorded there.

⛔ THE BOX MAY DECIDE THIS BEFORE THE LIKELIHOOD DOES.  `BOX` caps `Ω_m` at 0.40 and `τ` at 0.12.
   At `Σ = 0.400` the `rd_min` best fit already sat at `Ω_m = 0.34387`.  A midpoint test between two
   points ON a boundary measures the box, not the basin, so interiority is checked per run and a
   boundary hit is reported as NO VERDICT AT THAT SUM -- never as one basin.

⌗ IDEMPOTENT BY DESIGN.  Every minimisation is cached to its own JSON under `runs/`, and a rerun
  skips what is already there.  This container restarts unpredictably and the full scan is up to
  twenty minimisations, so a restart must cost only the run in flight.

    NODE=cc66 python3 branch_scan.py
"""
import io
import json
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
ROOT = os.path.dirname(os.path.dirname(_BTW))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT
R7853 = os.path.join(_BTW, 'r7853_cc66_the_repaired_transfer_and_the_like_for_like_reference')
sys.path.insert(0, R7853)
import profile_likeforlike as PL                                            # noqa: E402

NAMES = ('H0', 'Om', 'ombh2', 'ns', 'tau')
SUMS = (0.20, 0.30, 0.50, 0.60)
MODES = ('rd_camb', 'rd_min')
H0_STARTS = (65.29, 68.59)          # 60's own basin figures, as at r7873
FATOL, XATOL, UNIT = 5e-3, 1e-3, 1.0
BANK = os.path.join(R7853, 'out5')
RUNS = os.path.join(_HERE, 'runs')
OUT = os.path.join(_HERE, 'branch_scan.json')


def interior(x, frac=1e-9):
    return all(lo + frac * (hi - lo) < v < hi - frac * (hi - lo)
               for v, (lo, hi) in zip(x, PL.BOX))


def on_boundary(x, frac=1e-3):
    """a point within 0.1 per cent of the box's span of any wall -- the Ⓛ⑫ risk"""
    out = []
    for n, v, (lo, hi) in zip(NAMES, x, PL.BOX):
        if v - lo < frac * (hi - lo) or hi - v < frac * (hi - lo):
            out.append(n)
    return out


def cached(key, fn):
    """the idempotent step: one JSON per minimisation, skipped if already on disk"""
    os.makedirs(RUNS, exist_ok=True)
    p = os.path.join(RUNS, key + '.json')
    if os.path.exists(p):
        d = json.load(io.open(p, encoding='utf-8'))
        print('      [cached] %s' % key)
        return d
    print('      [running] %s ...' % key, flush=True)
    d = fn()
    io.open(p, 'w', encoding='utf-8').write(json.dumps(d, indent=1, sort_keys=True))
    return d


def banked(mode, s):
    """the banked best fit if r7853 has it, else a COLD run that makes one -- stated either way"""
    p = os.path.join(BANK, '%s_%.3f.json' % (mode, s))
    if os.path.exists(p):
        d = json.load(io.open(p, encoding='utf-8'))
        return d, 'READ from r7853 bank'
    d = cached('cold_%s_%.3f' % (mode, s),
               lambda: PL.profile(s, mode, PL.X0))
    return d, 'COLD run here (r7853 banks no such sum)'


def main():
    print(__doc__)
    print('=' * 100)
    print('\n  bank holds: %s' % ', '.join(sorted(os.listdir(BANK))[:4] + ['...']))
    out = {'sums': list(SUMS), 'modes': list(MODES), 'h0_starts': list(H0_STARTS),
           'box': [list(b) for b in PL.BOX], 'fatol': FATOL, 'xatol': XATOL, 'unit': UNIT,
           'scan': {}}

    for mode in MODES:
        for s in SUMS:
            key = '%s|%.2f' % (mode, s)
            print('\n  === %s ===' % key)
            b, how = banked(mode, s)
            base = [float(b[n]) for n in NAMES]
            print('      base point (%s): %s' % (how, dict(zip(NAMES, ['%.6f' % v
                                                                       for v in base]))))
            print('      its chi2 %.8f' % float(b['total']))
            rec = {'base_from': how, 'base': dict(zip(NAMES, base)),
                   'base_chi2': float(b['total']), 'runs': {}}

            pts, chis = [], []
            for h0 in H0_STARTS:
                start = [h0] + base[1:]
                d = cached('%s_%.3f_h%.2f' % (mode, s, h0),
                           lambda st=start: PL.profile(s, mode, st))
                x = [float(d[n]) for n in NAMES]
                c = float(d['total'])
                pts.append(x)
                chis.append(c)
                rec['runs']['%.2f' % h0] = dict(start=list(start), chi2=c,
                                                params=dict(zip(NAMES, x)),
                                                interior=bool(interior(x)),
                                                on_boundary=on_boundary(x))
                print('      start H0 %.2f -> chi2 %.8f  H0 %.8f  interior %s  walls %s'
                      % (h0, c, x[0], interior(x), on_boundary(x) or 'none'))

            walls = sorted(set(rec['runs']['%.2f' % H0_STARTS[0]]['on_boundary'])
                           | set(rec['runs']['%.2f' % H0_STARTS[1]]['on_boundary']))
            dh0 = abs(pts[0][0] - pts[1][0])
            dchi = abs(chis[0] - chis[1])
            xm = list((np.asarray(pts[0]) + np.asarray(pts[1])) / 2.0)
            cm = cached('%s_%.3f_mid' % (mode, s),
                        lambda xx=xm: dict(total=float(PL.score(s, *xx, mode)[0]),
                                           **dict(zip(NAMES, [float(v) for v in xx]))))
            cmid = float(cm['total'])
            worse, better = max(chis), min(chis)
            excess = cmid - worse
            rec.update(dh0=float(dh0), dchi2=float(dchi), midpoint_chi2=cmid,
                       midpoint=dict(zip(NAMES, [float(v) for v in xm])),
                       worse_endpoint=float(worse), better_endpoint=float(better),
                       midpoint_minus_worse=float(excess),
                       excess_over_fatol=float(excess / FATOL),
                       excess_over_unit=float(excess / UNIT), walls=walls)
            print('      |dH0| %.8f   |dchi2| %.8f   midpoint %.8f  excess %+.8f (%.4f x fatol)'
                  % (dh0, dchi, cmid, excess, excess / FATOL))

            if walls:
                verdict = 'NO VERDICT -- on the box wall in %s' % ','.join(walls)
            elif excess <= 0.0:
                verdict = 'ONE BASIN -- midpoint BELOW the worse endpoint, no ridge at all'
            elif excess <= FATOL:
                verdict = ('ONE BASIN -- ridge %+.2e is under fatol (%.4f of it) and %.1e of '
                           'dchi2=1: no barrier of consequence' % (excess, excess / FATOL,
                                                                   excess / UNIT))
            else:
                verdict = ('⛔ TWO BASINS -- ridge %+.6f EXCEEDS fatol' % excess)
            rec['verdict'] = verdict
            print('      ⇒ %s' % verdict)
            out['scan'][key] = rec
            io.open(OUT, 'w', encoding='utf-8').write(json.dumps(out, indent=1, sort_keys=True))

    print('\n' + '=' * 100)
    print('  THE SCAN, by ruler and sum:')
    for mode in MODES:
        for s in SUMS:
            r = out['scan'].get('%s|%.2f' % (mode, s))
            if r:
                print('    %-8s %.2f  %s' % (mode, s, r['verdict']))
    print('\n  written %s' % os.path.relpath(OUT, ROOT))


if __name__ == '__main__':
    main()
