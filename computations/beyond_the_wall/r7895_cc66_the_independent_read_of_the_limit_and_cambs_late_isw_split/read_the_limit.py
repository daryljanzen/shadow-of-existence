"""⑱① — the limit read independently, with THIS seat's own reader, on 60's banked profile.

Order `r7895` (69) item ⑱①.  `PREDICTION.md` registered the band (`1.0` meV) and the two
definitional mismatches BEFORE this file existed; the registration is commit `38535a933`.

** THE READER IS IMPORTED, NOT COPIED. **  `r7863`'s `limit95` is this seat's limit reader of
record (`r7853`'s method, carried forward).  Copying it would make this a second reader that
happens to agree; importing it is what makes the read independent of 60 and dependent on my own
history.  The same discipline as `r7885`, which imported `r7879`'s fitter.

⛔ WHAT THIS FILE DOES NOT CLAIM.  It reads 60's *banked profile* — their `sums` and `totals` from
`r7888`'s record — with my reader.  That isolates THE READER.  It does not recompute the
instrument's spectra, so it cannot and does not test 60's model; a disagreement here is a
disagreement about how a crossing is read off one profile, which is exactly what ⑱① asks and what
60's Ⓡ⓶ needs settled before the two limits can be called the same quantity.
"""
import importlib.util
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BTW = os.path.dirname(HERE)
R7863 = os.path.join(BTW, 'r7863_cc66_the_ell_cuts_and_the_top_node_on_the_reference')
R7888 = os.path.join(BTW, 'r7888_60_the_limit_read_on_the_runners_complete_grid')

#: ⛭ import this seat's own reader from the revision that landed it
_spec = importlib.util.spec_from_file_location(
    'cc66_cuts', os.path.join(R7863, 'read_the_cuts_and_the_node.py'))
_mod = importlib.util.module_from_spec(_spec)
sys.modules['cc66_cuts'] = _mod
_spec.loader.exec_module(_mod)
limit95 = _mod.limit95
CROSS = _mod.CROSS

SIXTY = 193.54530379137307          #: r7888's calibrated crossing, the figure under test
BAND = 1.0                          #: meV, registered in PREDICTION.md before this file existed


def mine_from_min(points):
    """the same crossing, but referenced to the profile MINIMUM instead of the lowest-sum point.

    This is NOT a second reader.  It is `limit95` with 60's baseline convention substituted, so the
    difference between the two numbers IS the convention's contribution, measured rather than
    argued.  `r7888` decomposed its own `+7.587` meV the same way.
    """
    pts = sorted(points)
    s = np.array([p[0] for p in pts], float)
    t = np.array([p[1] for p in pts], float)
    d = t - t.min()
    if d.max() <= CROSS:
        return None
    fine = np.linspace(s[0], s[-1], 200001)
    i = np.where(np.interp(fine, s, d) > CROSS)[0]
    return float(fine[i[0]] * 1000.0) if len(i) else None


def main():
    rec = json.load(open(os.path.join(R7888, 'limit_on_runner_grid.json'), encoding='utf-8'))
    out = {'source': 'r7888 limit_on_runner_grid.json, 60 banked profile, read with r7863 limit95',
           'sixty_calibrated_meV': SIXTY, 'band_meV': BAND, 'cross': CROSS,
           'reader': 'imported from r7863 read_the_cuts_and_the_node.limit95', 'columns': {}}

    for col in ('calibrated', 'minimised', 'minimized'):
        if col not in rec:
            continue
        c = rec[col]
        sums, totals = c.get('sums'), c.get('totals')
        if not sums or not totals:
            continue
        pts = list(zip([float(x) for x in sums], [float(x) for x in totals]))
        mine, dc = limit95(pts)
        from_min = mine_from_min(pts)
        row = {
            'n_points': len(pts), 'sums': [float(x) for x in sums],
            'min_at': c.get('min_at'), 'monotonic_above_min': c.get('monotonic_above_min'),
            'n_dips': len(c.get('dips') or []),
            'sixty_crossing_meV': c.get('crossing_meV'),
            'mine_base_lowest_sum_meV': mine,
            'mine_base_minimum_meV': from_min,
            'dchi2_at_lowest_sum_vs_min': float(np.array(totals, float)[0]
                                                - np.array(totals, float).min()),
        }
        if mine is not None and c.get('crossing_meV') is not None:
            row['diff_lowest_sum_meV'] = float(mine - c['crossing_meV'])
            row['within_band_lowest_sum'] = bool(abs(mine - c['crossing_meV']) <= BAND)
        if from_min is not None and c.get('crossing_meV') is not None:
            row['diff_minimum_meV'] = float(from_min - c['crossing_meV'])
            row['within_band_minimum'] = bool(abs(from_min - c['crossing_meV']) <= BAND)
        if mine is not None and from_min is not None:
            row['convention_cost_meV'] = float(mine - from_min)
        out['columns'][col] = row

    #: the lensing half's provenance, read rather than assumed
    lp = rec.get('lensing_provenance') or {}
    out['lensing_provenance'] = {'checked': lp.get('checked'), 'n_bad': len(lp.get('bad') or [])}
    out['dchi2_of_record'] = rec.get('dchi2')
    out['fork'] = {k: (rec.get('fork') or {}).get(k) for k in ('branch', 'limit_readable', 'min_at')}

    json.dump(out, open(os.path.join(HERE, 'limit_read.json'), 'w', encoding='utf-8'),
              indent=1, sort_keys=True)

    print('\n  ⑱① THE LIMIT READ WITH THIS SEAT\'S OWN READER, ON 60\'s BANKED PROFILE\n')
    print('    reader: %s' % out['reader'])
    print('    60\'s calibrated crossing: %.11f meV   registered band: +-%.2f meV\n' % (SIXTY, BAND))
    for col, r in sorted(out['columns'].items()):
        print('    [%s]  n=%d  min_at=%s  monotonic_above_min=%s  dips=%d'
              % (col, r['n_points'], r['min_at'], r['monotonic_above_min'], r['n_dips']))
        print('        60                              %s' % _f(r['sixty_crossing_meV']))
        print('        mine, base = lowest-sum point   %s   diff %s  in band: %s'
              % (_f(r['mine_base_lowest_sum_meV']), _f(r.get('diff_lowest_sum_meV')),
                 r.get('within_band_lowest_sum')))
        print('        mine, base = profile minimum    %s   diff %s  in band: %s'
              % (_f(r['mine_base_minimum_meV']), _f(r.get('diff_minimum_meV')),
                 r.get('within_band_minimum')))
        print('        Δχ² at the lowest sum above the minimum: %.10f' % r['dchi2_at_lowest_sum_vs_min'])
        print('        ⇒ the baseline convention is worth %s meV on this column\n'
              % _f(r.get('convention_cost_meV')))
    print('    lensing provenance: %s point(s) checked, %s bad'
          % (out['lensing_provenance']['checked'], out['lensing_provenance']['n_bad']))
    print('    60\'s fork: %s, readable=%s, min_at=%s\n'
          % (out['fork']['branch'], out['fork']['limit_readable'], out['fork']['min_at']))


def _f(x):
    return 'not read' if x is None else ('%14.8f' % x)


if __name__ == '__main__':
    main()
