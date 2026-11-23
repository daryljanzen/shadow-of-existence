# -*- coding: utf-8 -*-
"""⒝ THE REFERENCE'S OWN RULER, tabulated -- `camb`'s `rdrag` as a function of the point.

⛭ *The amendment registers two ruler treatments and names each.  This file builds the second: the
reference's `rdrag` at each point's own cosmology INCLUDING ITS NEUTRINO SUM, which is what moves
and what this instrument's own background cannot produce.  It is the reference's number and the
receipt says so wherever it is used.*

⌗ *What it ranges over is MEASURED here too, not assumed: `rdrag` is checked to be a function of
`(omega_m, omega_b, Sum)` by reading it at two `(H0, Om)` pairs carrying the same three.*
"""
import io
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import drag_ruler as DR                                                     # noqa: E402

TOL_RANGE = 1.0e-5


def ranging():
    wm = DR.CENTRE['OM'] * (DR.CENTRE['H0'] / 100.0) ** 2
    wb = DR.CENTRE['WB']
    rows = []
    for H0 in (59.40, 75.40):
        OM = wm / (H0 / 100.0) ** 2
        d = DR.camb_drag(H0, OM, wb, MNU=0.30)
        rows.append(d)
        print('    H0 %6.2f  Om %.6f  (omega_m %.6f, Sum 0.30 eV)  ->  rdrag %10.5f  zdrag %9.3f'
              % (H0, OM, wm, d['rdrag'], d['zdrag']))
    rel = abs(rows[0]['rdrag'] / rows[1]['rdrag'] - 1.0)
    print('    ⇒ the two readings differ by %.3e  (band %.0e): %s'
          % (rel, TOL_RANGE, 'ONE LABEL' if rel < TOL_RANGE else '⛔ TWO OBJECTS'))
    return dict(rows=rows, r_rel=float(rel), tol=TOL_RANGE, holds=bool(rel < TOL_RANGE))


def grid(n_wm=17, n_wb=9, n_s=9):
    # ⛔ ** THIS RAN IN A PROCESS POOL AND DEADLOCKED, AND THAT IS KEPT HERE. **  *`ranging()` calls
    #   `camb` in the PARENT before the pool is built, so the children were forked after `camb`'s
    #   OpenMP runtime had been initialised, and all three sat at zero CPU for forty-three minutes
    #   without computing one point.  ⌗ The fix is not a bigger timeout: a background solve costs
    #   about `0.1` s, so the whole table is two or three minutes SERIALLY, and the pool was buying
    #   nothing it could not have been measured not to need.*
    h_lo = (DR.CENTRE['H0'] - DR.NSTEP * DR.STEP['H0']) / 100.0
    h_hi = (DR.CENTRE['H0'] + DR.NSTEP * DR.STEP['H0']) / 100.0
    om_lo = DR.CENTRE['OM'] - DR.NSTEP * DR.STEP['OM']
    om_hi = DR.CENTRE['OM'] + DR.NSTEP * DR.STEP['OM']
    wm = np.linspace(om_lo * h_lo ** 2, om_hi * h_hi ** 2, n_wm)
    wb = np.linspace(DR.CENTRE['WB'] - DR.NSTEP * DR.STEP['WB'],
                     DR.CENTRE['WB'] + DR.NSTEP * DR.STEP['WB'], n_wb)
    # ⌗ the sum axis covers the profile's own nodes and a little beyond, so no node is extrapolated
    ss = np.linspace(0.0, 0.70, n_s)
    H0 = DR.CENTRE['H0']
    jobs = [(float(H0), float(a / (H0 / 100.0) ** 2), float(b), float(s))
            for a in wm for b in wb for s in ss]
    res = [_one(j) for j in jobs]
    Z = np.array([r['rdrag'] for r in res], float).reshape(n_wm, n_wb, n_s)
    ZD = np.array([r['zdrag'] for r in res], float).reshape(n_wm, n_wb, n_s)
    return dict(omega_m=wm, omega_b=wb, sums=ss, rdrag=Z, zdrag=ZD)


def _one(job):
    H0, OM, WB, S = job
    return DR.camb_drag(H0, OM, WB, MNU=S)


def sum_dependence():
    """the reference's ruler ACROSS THE NEUTRINO SUM at one geometry -- the amendment's evidence

    *This is the measurement that forced the amendment: the instrument's own ruler is exactly flat
    in the sum and this one is not, so the two cannot both be "the calibrated case".*
    """
    c = DR.CENTRE
    rows = []
    for sv in (0.0, 0.06, 0.30, 0.60):
        d = DR.camb_drag(c['H0'], c['OM'], c['WB'], MNU=sv)
        rows.append(dict(sum=float(sv), rdrag=d['rdrag'], zdrag=d['zdrag']))
        print('    Sum %.2f eV   rdrag %10.5f   zdrag %9.3f' % (sv, d['rdrag'], d['zdrag']))
    spread = max(r['rdrag'] for r in rows) / min(r['rdrag'] for r in rows) - 1.0
    print('    ⇒ the reference\'s ruler spreads %.4f per cent across [0, 0.60] eV, where this'
          ' instrument\'s moves by exactly zero' % (100.0 * spread))
    return dict(rows=rows, spread=float(spread))


def _merge(out):
    path = os.path.join(HERE, 'ref_ruler.json')
    old = json.load(io.open(path, encoding='utf-8')) if os.path.exists(path) else {}
    old.update(out)
    with io.open(path, 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(old, indent=1, sort_keys=True, default=float))


if __name__ == '__main__':
    out = {}
    if len(sys.argv) > 1 and sys.argv[1] == 'sums':
        print('\n  THE REFERENCE\'S RULER ACROSS THE SUM -- why the amendment exists')
        print('  ' + '-' * 104)
        out['sum_dependence'] = sum_dependence()
        _merge(out)
        print('')
        raise SystemExit(0)
    print('\n  Ⓑ②ᶠ⒝ WHAT THE REFERENCE\'S RULER RANGES OVER')
    print('  ' + '-' * 104)
    out['ranging'] = ranging()
    print('\n  Ⓑ②ᶠ⒝ THE REFERENCE\'S RULER TABULATED')
    print('  ' + '-' * 104)
    g = grid()
    np.savez(os.path.join(HERE, 'ref_grid.npz'), **g)
    print('    %d x %d x %d nodes, rdrag from %.4f to %.4f Mpc'
          % (len(g['omega_m']), len(g['omega_b']), len(g['sums']),
             g['rdrag'].min(), g['rdrag'].max()))
    out['grid'] = dict(n=[int(len(g['omega_m'])), int(len(g['omega_b'])), int(len(g['sums']))],
                       r_lo=float(g['rdrag'].min()), r_hi=float(g['rdrag'].max()))
    out['sum_dependence'] = sum_dependence()
    _merge(out)
    print('')
