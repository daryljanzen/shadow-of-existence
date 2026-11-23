# -*- coding: utf-8 -*-
"""Ⓐ① THE DRAG-EPOCH RULER: derived, validated against the reference, and ranged.

Order `r7861` (69) item ①.  Three legs, in the order the registration fixes:

  ⒜ **validate** -- `r_d` and `z_drag` against `camb`'s `rdrag` and `zdrag` at the control point
     (a DECLARED READ) and at TWO CORNERS of the fit's own box (the registered comparison),
     criterion `0.005` relative on both quantities at both corners;
  ⒝ **range** -- whether `r_d` is a function of `(omega_m, omega_b)` alone in THIS instrument,
     measured on two `(H0, Om)` pairs carrying the same pair, and whether the neutrino sum moves it;
  ⒞ **grid** -- the ruler tabulated over the box so a likelihood call can read it.

⛔ *No fitting formula is used anywhere.  Every value comes from one import of the instrument at
that point's own switches.*
"""
import io
import json
import os
import subprocess
import sys
import tempfile

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
PROBE = os.path.join(HERE, '_drag_probe.py')

# the fit's own box: `model3`'s `lcdm` centre and `R.STEP`, with the barrier at six steps
CENTRE = dict(H0=67.40, OM=0.3150, WB=0.0224, NS=0.965)
STEP = dict(H0=2.0, OM=0.015, WB=0.0008, NS=0.02)
NSTEP = 6.0
TOL_REF = 0.005          # ⛭ registered: the band on r_d and z_drag against the reference
TOL_RANGE = 1.0e-4       # ⛭ registered: the band the (omega_m, omega_b) identity has to hold to


def probe(H0, OM, WBH2, MNU=0.0, LMAXL='2', extra=None):
    env = dict(os.environ)
    env.update(ARM='lcdm', LH0='%.10g' % H0, LOM='%.10g' % OM, WBH2='%.10g' % WBH2,
               MNU='%.10g' % MNU, LMAXL=str(LMAXL))
    if extra:
        env.update(extra)
    fd, path = tempfile.mkstemp(suffix='.json')
    os.close(fd)
    env['OUTJSON'] = path
    try:
        r = subprocess.run([sys.executable, PROBE], env=env,
                           stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        if not os.path.getsize(path):
            raise RuntimeError('probe wrote nothing: %s' % r.stderr.decode()[-2000:])
        d = json.load(io.open(path, encoding='utf-8'))
    finally:
        os.unlink(path)
    if 'error' in d:
        raise RuntimeError(d['error'])
    return d


def camb_drag(H0, OM, WBH2, MNU=0.0):
    """the reference's own `rdrag` and `zdrag` at the same cosmology.

    ⌗ *`omch2` is formed so that the TOTAL matter density matches this point's `Om h^2` with the
    neutrino mass taken out of it, which is how the instrument splits it (`OCDM = OM - OB - ONU`).*
    """
    import camb
    h = H0 / 100.0
    onu = MNU / 93.14 / h ** 2
    omch2 = (OM - WBH2 / h ** 2 - onu) * h ** 2
    p = camb.set_params(H0=H0, ombh2=WBH2, omch2=omch2, mnu=MNU, tau=0.054,
                        ns=0.965, As=2.1e-9)
    d = camb.get_background(p).get_derived_params()
    return dict(rdrag=float(d['rdrag']), zdrag=float(d['zdrag']),
                rstar=float(d['rstar']), zstar=float(d['zstar']))


def _corner(sh0, som, swb):
    return (CENTRE['H0'] + sh0 * NSTEP * STEP['H0'],
            CENTRE['OM'] + som * NSTEP * STEP['OM'],
            CENTRE['WB'] + swb * NSTEP * STEP['WB'])


def validate():
    """⒜ the ruler against the reference, at the read point and at two unread corners."""
    pts = [('control (DECLARED READ)', CENTRE['H0'], CENTRE['OM'], CENTRE['WB']),
           ('corner low  (-6,-6,-6)',) + _corner(-1, -1, -1),
           ('corner high (+6,+6,+6)',) + _corner(+1, +1, +1)]
    rows = []
    for name, H0, OM, WB in pts:
        mine = probe(H0, OM, WB)
        ref = camb_drag(H0, OM, WB)
        row = dict(point=name, H0=H0, OM=OM, WB=WB,
                   omega_m=mine['omega_m'], omega_b=mine['omega_b'],
                   r_drag=mine['r_drag'], z_drag=mine['z_drag'],
                   rdrag_ref=ref['rdrag'], zdrag_ref=ref['zdrag'],
                   r_rel=abs(mine['r_drag'] / ref['rdrag'] - 1.0),
                   z_rel=abs((1.0 + mine['z_drag']) / (1.0 + ref['zdrag']) - 1.0),
                   r_rec_error=mine['r_rec_error'], R_S=mine['R_S'],
                   taud_at_eta_rec=mine['taud_at_eta_rec'], clock=mine['clock'])
        row['within'] = bool(row['r_rel'] < TOL_REF and row['z_rel'] < TOL_REF)
        rows.append(row)
        print('    %-24s  r_d %9.4f vs %9.4f  (%.2e)   z_d %9.3f vs %9.3f  (%.2e)  %s'
              % (name, row['r_drag'], row['rdrag_ref'], row['r_rel'],
                 row['z_drag'], row['zdrag_ref'], row['z_rel'],
                 'within' if row['within'] else '⛔ OUTSIDE'))
    # ⌗ the CORNERS are the registered arm; the control point is a read and is excluded from it
    corners = [r for r in rows if 'corner' in r['point']]
    return dict(rows=rows, tol=TOL_REF,
                corners_within=bool(all(r['within'] for r in corners)),
                read_point_within=bool(rows[0]['within']),
                worst_r_rec_error=max(r['r_rec_error'] for r in rows))


def ranging():
    """⒝ what the ruler ranges over -- the label's many-to-one-ness, measured."""
    out = {}
    # ⓵ two different (H0, Om) carrying the SAME omega_m and the same omega_b
    wm, wb = CENTRE['OM'] * (CENTRE['H0'] / 100.0) ** 2, CENTRE['WB']
    pairs = []
    for H0 in (CENTRE['H0'] - 4.0 * STEP['H0'], CENTRE['H0'] + 4.0 * STEP['H0']):
        OM = wm / (H0 / 100.0) ** 2
        d = probe(H0, OM, wb)
        pairs.append(d)
        print('    omega_m %.6f  omega_b %.5f   H0 %6.2f  Om %.6f   ->  r_d %10.5f  z_d %9.3f'
              % (d['omega_m'], d['omega_b'], H0, OM, d['r_drag'], d['z_drag']))
    rel = abs(pairs[0]['r_drag'] / pairs[1]['r_drag'] - 1.0)
    zrel = abs((1 + pairs[0]['z_drag']) / (1 + pairs[1]['z_drag']) - 1.0)
    out['omega_label'] = dict(points=pairs, r_rel=rel, z_rel=zrel, tol=TOL_RANGE,
                              holds=bool(rel < TOL_RANGE and zrel < TOL_RANGE))
    print('    ⇒ the two readings differ by %.3e in r_d and %.3e in z_drag  (band %.0e): %s'
          % (rel, zrel, TOL_RANGE, 'ONE LABEL' if out['omega_label']['holds'] else '⛔ TWO OBJECTS'))

    # ⓶ the neutrino sum, at fixed omega_m and omega_b -- the profile moves it, so it is measured
    sums, rds = [], []
    for s in (0.0, 0.06, 0.30, 0.60):
        d = probe(CENTRE['H0'], CENTRE['OM'], wb, MNU=s)
        sums.append(s)
        rds.append(d['r_drag'])
        print('    Sum = %.2f eV  ->  r_d %10.5f   z_d %9.3f   (omega_m %.6f)'
              % (s, d['r_drag'], d['z_drag'], d['omega_m']))
    spread = float(max(rds) / min(rds) - 1.0)
    out['neutrino_sum'] = dict(sums=sums, r_drag=rds, spread=spread, tol=TOL_RANGE,
                               negligible=bool(spread < TOL_RANGE))
    print('    ⇒ the sum moves r_d by %.3e across [0, 0.60] eV: %s'
          % (spread, 'inside the band' if out['neutrino_sum']['negligible']
             else 'OUTSIDE -- the ruler carries the sum too'))

    # ⓷ and the reach switch, which this file sets to keep the import cheap, must not touch it
    a = probe(CENTRE['H0'], CENTRE['OM'], wb, LMAXL='2')
    b = probe(CENTRE['H0'], CENTRE['OM'], wb, LMAXL='2600')
    out['lmaxl'] = dict(r_drag_lmaxl2=a['r_drag'], r_drag_lmaxl2600=b['r_drag'],
                        identical=bool(a['r_drag'] == b['r_drag']))
    print('    ⇒ the multipole reach this probe runs at does not reach the ruler: %s'
          % ('bit-identical' if out['lmaxl']['identical'] else '⛔ IT MOVES IT'))
    return out


def grid(n_wm=17, n_wb=9, sums=(0.0,), workers=4):
    """⒞ the ruler tabulated over the box, as `r_d(omega_m, omega_b)` per neutrino sum."""
    from concurrent.futures import ProcessPoolExecutor
    h_lo = (CENTRE['H0'] - NSTEP * STEP['H0']) / 100.0
    h_hi = (CENTRE['H0'] + NSTEP * STEP['H0']) / 100.0
    om_lo, om_hi = CENTRE['OM'] - NSTEP * STEP['OM'], CENTRE['OM'] + NSTEP * STEP['OM']
    wm = np.linspace(om_lo * h_lo ** 2, om_hi * h_hi ** 2, n_wm)
    wb = np.linspace(CENTRE['WB'] - NSTEP * STEP['WB'], CENTRE['WB'] + NSTEP * STEP['WB'], n_wb)
    H0 = CENTRE['H0']
    jobs = [(float(H0), float(a / (H0 / 100.0) ** 2), float(b), float(s))
            for s in sums for a in wm for b in wb]
    with ProcessPoolExecutor(max_workers=workers) as ex:
        res = list(ex.map(_grid_one, jobs))
    Z = np.array([r['r_drag'] for r in res], float).reshape(len(sums), n_wm, n_wb)
    ZD = np.array([r['z_drag'] for r in res], float).reshape(len(sums), n_wm, n_wb)
    return dict(omega_m=wm, omega_b=wb, sums=np.array(sums, float), r_drag=Z, z_drag=ZD)


def _grid_one(job):
    H0, OM, WB, S = job
    return probe(H0, OM, WB, MNU=S)


if __name__ == '__main__':
    what = sys.argv[1] if len(sys.argv) > 1 else 'all'
    res = {}
    if what in ('all', 'validate'):
        print('\n  Ⓐ①ᵃ THE RULER AGAINST THE REFERENCE')
        print('  ' + '-' * 110)
        res['validate'] = validate()
    if what in ('all', 'range'):
        print('\n  Ⓐ①ᵇ WHAT THE RULER RANGES OVER')
        print('  ' + '-' * 110)
        res['ranging'] = ranging()
    if what in ('all', 'grid'):
        print('\n  Ⓐ①ᶜ THE RULER TABULATED')
        print('  ' + '-' * 110)
        sums = tuple(float(x) for x in (os.environ.get('RD_SUMS', '0.0').split(',')))
        g = grid(sums=sums)
        np.savez(os.path.join(HERE, 'rd_grid.npz'), **g)
        print('    %d x %d x %d nodes, r_d from %.4f to %.4f Mpc'
              % (len(g['sums']), len(g['omega_m']), len(g['omega_b']),
                 g['r_drag'].min(), g['r_drag'].max()))
        res['grid'] = dict(n=[int(len(g['sums'])), int(len(g['omega_m'])), int(len(g['omega_b']))],
                           r_lo=float(g['r_drag'].min()), r_hi=float(g['r_drag'].max()))
    with io.open(os.path.join(HERE, 'drag_ruler.json'), 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(res, indent=1, sort_keys=True, default=float))
    print('')
