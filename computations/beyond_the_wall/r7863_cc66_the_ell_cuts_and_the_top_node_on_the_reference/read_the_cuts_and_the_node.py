"""r7863+cc66: READ THE EIGHT CUT LEGS AND THE SIXTEEN NODE POINTS INTO ONE RECORD.

Order r7863 (69) items ① and ②.  Bands registered at `r7863+cc66.1` BEFORE either computation
existed.  This file RECOMPUTES NOTHING: it reads the per-point JSONs the two drivers wrote and
reduces them to the quantities the bands are about, so the receipt pins a record rather than
re-deriving a limit from a profile it would then also have to trust.

** THE LIMIT IS THE INTERPOLATED `2.71` CROSSING, BY r7853's OWN METHOD AND NOT A SECOND ONE. **
`read_likeforlike.py` interpolates `Delta chi^2(sum)` on a fine grid and takes the first crossing of
`2.71`; the same is done here, and the check that it IS the same is that the UNCUT legs reproduce
the landed `30.56` and `54.00` meV to the printed digit -- asserted in the receipt, not assumed.

** THE SECOND-BRANCH TEST IS `cold - warm`, AND ITS SIGN IS THE WHOLE POINT. **  A cold start from
the control landing LOWER than the warm chain means the warm path was following the basin it came
from, which IS the second branch.  Landing higher or equal means it was not.  Reported per point.

Run: python3 -I read_the_cuts_and_the_node.py
"""
import glob
import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
UNCUT = {'rd_camb': 30.56, 'rd_min': 54.00}
BANKED_040 = {'rd_camb': 66.80405, 'rd_min': 64.97111}
SUMS = (0.45, 0.50, 0.55, 0.60)
CROSS = 2.71


def limit95(points):
    """the first interpolated crossing of 2.71, in meV -- r7853's method, not a second one"""
    pts = sorted(points)
    base = pts[0][1]
    s = np.array([p[0] for p in pts], float)
    dc = np.array([p[1] - base for p in pts], float)
    if dc.max() <= CROSS:
        return None, dc
    fine = np.linspace(s[0], s[-1], 200001)
    i = np.where(np.interp(fine, s, dc) > CROSS)[0]
    return (float(fine[i[0]] * 1000.0) if len(i) else None), dc


def main():
    legs, removed = {}, {}
    for f in sorted(glob.glob(os.path.join(HERE, 'cuts', '*.json'))):
        d = json.load(open(f))
        legs.setdefault((d['mode'], d['leg']), []).append((d['sum'], d['total'], d['interior']))
        removed[(d['mode'], d['leg'])] = tuple(d['removed'])
    cuts = {}
    for k in sorted(legs):
        L, dc = limit95(legs[k])
        cuts['%s|%s' % k] = dict(mode=k[0], leg=k[1], limit95_meV=L,
                                 move_meV=(L - UNCUT[k[0]]) if L is not None else None,
                                 n_points=len(legs[k]), dchi2=[float(x) for x in dc],
                                 removed=list(removed[k]),
                                 interior=all(p[2] for p in legs[k]))
    ratios = {}
    for mode in ('rd_camb', 'rd_min'):
        for cut in (1800, 1500):
            t = cuts['%s|top%d' % (mode, cut)]['move_meV']
            b = cuts['%s|bot%d' % (mode, cut)]['move_meV']
            ratios['%s|%d' % (mode, cut)] = (b / t) if (t and b) else None
    node = {}
    for mode in ('rd_camb', 'rd_min'):
        rows, prev = [], BANKED_040[mode]
        for s in SUMS:
            W = json.load(open(os.path.join(HERE, 'out', '%s_warm_%.3f.json' % (mode, s))))
            C = json.load(open(os.path.join(HERE, 'out', '%s_cold_%.3f.json' % (mode, s))))
            best = min((W, C), key=lambda x: x['total'])
            rows.append(dict(sum=s, warm_total=W['total'], cold_total=C['total'],
                             cold_minus_warm=C['total'] - W['total'],
                             H0_best=best['H0'], step=prev - best['H0'],
                             interior=bool(W['interior'] and C['interior'])))
            prev = best['H0']
        st = np.array([r['step'] for r in rows], float)
        node[mode] = dict(rows=rows, all_steps_down=bool((st > 0).all()),
                          max_step=float(st.max()), mean_step=float(st.mean()),
                          bound_3x_mean=float(3 * st.mean()),
                          max_within_bound=bool(st.max() <= 3 * st.mean()),
                          H0_at_060=float(prev),
                          any_cold_lower=bool(any(r['cold_minus_warm'] < -1e-3 for r in rows)),
                          worst_cold_minus_warm=float(min(r['cold_minus_warm'] for r in rows)),
                          all_interior=bool(all(r['interior'] for r in rows)))
    out = dict(cuts=cuts, bot_over_top=ratios, node=node, uncut_meV=UNCUT,
               banked_H0_at_040=BANKED_040, sixty_second_branch_H0=65.74,
               my_rd_min_H0_at_030=65.76700)
    json.dump(out, open(os.path.join(HERE, 'cuts_and_node.json'), 'w'), indent=1)
    print('  ITEM ① -- eight legs')
    for k in sorted(cuts):
        c = cuts[k]
        print('   %-8s %-8s removed %-18s limit95 %8.2f  move %+7.2f  interior %s'
              % (c['mode'], c['leg'], str(tuple(c['removed'])), c['limit95_meV'],
                 c['move_meV'], c['interior']))
    print('   bot/top ratios: %s' % {k: round(v, 3) for k, v in ratios.items()})
    print('\n  ITEM ② -- sixteen points')
    for mode in node:
        n = node[mode]
        print('   %-8s steps %s  all down %s  max %.4f vs bound %.4f  H0(0.60) %.3f  '
              'any cold lower %s  worst cold-warm %+.6f  all interior %s'
              % (mode, [round(r['step'], 4) for r in n['rows']], n['all_steps_down'],
                 n['max_step'], n['bound_3x_mean'], n['H0_at_060'], n['any_cold_lower'],
                 n['worst_cold_minus_warm'], n['all_interior']))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
