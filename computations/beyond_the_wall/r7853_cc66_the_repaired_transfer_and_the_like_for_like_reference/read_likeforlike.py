"""r7853+cc66 item ⑤: read the limits, vertices and ruler spread off the completed grid.

** THE LIMIT IS SCANNED UP FROM THE MINIMUM, NOT FROM Sum = 0. **  r7847's defect was a scan that
began at the grid's bottom when the minimum sat elsewhere: Sum = 0 itself then exceeded the 2.71
threshold, the scan returned grid point 0.0, and 0.0 is falsy, so it printed "ABOVE THE GRID" --
the exact opposite of the truth.  The fix is to locate argmin first and scan from there.

** THE VERTEX IS AN EXTRAPOLATION, NOT A SOLVE BELOW ZERO. **  CAMB has no negative-sum
construction, so the parabolic vertex of Delta chi^2(sum) fitted to the lowest 4, 5 and 6 points is
what stands in for an effective mass here.  60's effective mass is a posterior MEAN over a chain
whose lower bound is negative, which their own growth solver can evaluate.  The two are DIFFERENT
ESTIMATORS and are not equated.

COMPUTES: nothing new -- it re-reads this revision's own 16 banked profile points and recomputes
          each arm's minimum, 95 per cent limit, parabolic vertices and the ruler spread.  It pins
          no cosmological parameter.
Run: python3 -I read_likeforlike.py
"""
import glob
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'likeforlike.json')
#: r7849's values with omega_b and n_s HELD, for the comparison item ⑤ exists to make
R7849 = dict(rd_camb=26.06, rd_min=54.28, spread_per_cent=52.0)
PUBLISHED_MEV = 64.2


def arm(mode):
    rows = sorted((json.load(open(f)) for f in
                   glob.glob(os.path.join(HERE, 'out5', '%s_*.json' % mode))),
                  key=lambda d: d['sum'])
    rows = [r for r in rows if not r.get('cold')]
    s = np.array([r['sum'] for r in rows], float)
    t = np.array([r['total'] for r in rows], float)
    dc = t - t.min()
    i = int(np.argmin(t))
    hs, hd = s[i:], dc[i:]
    fine = np.linspace(float(hs[0]), float(hs[-1]), 20001)
    k = np.where(np.interp(fine, hs, hd) > 2.71)[0]
    lim = float(fine[k[0]]) if k.size else None
    vx = []
    for n in (4, 5, 6):
        a, b, _c = np.polyfit(s[:n], dc[:n], 2)
        vx.append(float(-b / (2 * a) * 1000.0))
    return dict(mode=mode, n_points=len(rows), sum_at_min_eV=float(s[i]),
                limit95_meV=(lim * 1000.0) if lim is not None else None,
                vertices_meV=vx, dchi2=[float(v) for v in dc],
                H0_run=float(rows[-1]['H0'] - rows[0]['H0']),
                Om_run=float(rows[-1]['Om'] - rows[0]['Om']),
                H0_at_min=float(rows[i]['H0']), Om_at_min=float(rows[i]['Om']),
                ombh2_at_min=float(rows[i]['ombh2']), ns_at_min=float(rows[i]['ns']),
                free=rows[0]['free'])


def main():
    C, M = arm('rd_camb'), arm('rd_min')
    spread = 100.0 * (1.0 - C['limit95_meV'] / M['limit95_meV'])
    out = dict(rd_camb=C, rd_min=M, ruler_spread_per_cent=float(spread),
               r7849_held=R7849, published_meV=PUBLISHED_MEV,
               tighter_than_published=dict(
                   rd_camb=float(PUBLISHED_MEV / C['limit95_meV']),
                   rd_min=float(PUBLISHED_MEV / M['limit95_meV'])),
               loosening_vs_r7849_per_cent=dict(
                   rd_camb=float(100.0 * (C['limit95_meV'] / R7849['rd_camb'] - 1.0)),
                   rd_min=float(100.0 * (M['limit95_meV'] / R7849['rd_min'] - 1.0))),
               note=('the vertex is an EXTRAPOLATED parabolic vertex, not a solve below zero and '
                     'not 60s posterior-mean estimator'))
    json.dump(out, open(OUT, 'w'), indent=1)

    print('  %-9s %8s %10s %-28s %8s %9s' % ('arm', 'min eV', '95% meV', 'vertex 4/5/6 meV',
                                             'H0 run', 'Om run'))
    for a in (C, M):
        print('  %-9s %8.3f %10.3f  %-27s %8.3f %9.4f'
              % (a['mode'], a['sum_at_min_eV'], a['limit95_meV'],
                 '/'.join('%+.2f' % v for v in a['vertices_meV']), a['H0_run'], a['Om_run']))
    print('\n  ruler spread: %.1f per cent of the looser   (r7849 held: %.1f)'
          % (spread, R7849['spread_per_cent']))
    print('  against r7849 HELD: %.2f -> %.2f meV (%+.1f%%) calibrated ; %.2f -> %.2f meV (%+.1f%%) minimised'
          % (R7849['rd_camb'], C['limit95_meV'], out['loosening_vs_r7849_per_cent']['rd_camb'],
             R7849['rd_min'], M['limit95_meV'], out['loosening_vs_r7849_per_cent']['rd_min']))
    print('  against the published %.1f meV: %.2f times tighter calibrated, %.2f minimised'
          % (PUBLISHED_MEV, out['tighter_than_published']['rd_camb'],
             out['tighter_than_published']['rd_min']))
    print('\n  wrote %s' % os.path.basename(OUT))
    return 0


if __name__ == '__main__':
    sys.exit(main())
