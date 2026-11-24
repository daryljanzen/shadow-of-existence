# -*- coding: utf-8 -*-
"""Ⓒ③ THE REPAIRED RULER, TABULATED -- `r_d(omega_m, omega_b, Sum)` on the new background.

⛭ *At `r7862` this table was TWO-dimensional, because the ruler was exactly flat in the neutrino
sum and the sum axis would have been a constant.  The repair is precisely that it is not flat any
more, so the table gains that axis -- which is the clearest statement of what item ① changed.*

⌗ *Driven with THREADS over subprocesses, not a process pool: each probe is its own fresh `python3`,
so nothing is forked after a threaded library has initialised.  `r7862` lost forty-three minutes to
exactly that mistake and the record of it is in `ref_ruler.py`.*

    python3 rd_grid_nufd.py
"""
import io
import json
import os
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BTW = os.path.dirname(HERE)
PROBE = os.path.join(BTW, 'r7862_60_the_calibrated_case_on_the_references_terms_and_the_damping_'
                          'tails_share_of_the_gap', '_drag_probe.py')
CENTRE = dict(H0=67.40, OM=0.3150, WB=0.0224, NS=0.965)
STEP = dict(H0=2.0, OM=0.015, WB=0.0008, NS=0.02)
NSTEP = 6.0


def probe(H0, OM, WB, S):
    env = dict(os.environ)
    env.update(ARM='lcdm', LMAXL='2', NUFD='1',
               LH0='%.10g' % H0, LOM='%.10g' % OM, WBH2='%.10g' % WB, MNU='%.10g' % S)
    fd, path = tempfile.mkstemp(suffix='.json')
    os.close(fd)
    env['OUTJSON'] = path
    try:
        r = subprocess.run([sys.executable, PROBE], env=env,
                           stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        if not os.path.getsize(path):
            raise RuntimeError(r.stderr.decode()[-1500:])
        return json.load(io.open(path, encoding='utf-8'))
    finally:
        os.unlink(path)


def main(n_wm=17, n_wb=9, n_s=7, workers=3):
    h_lo = (CENTRE['H0'] - NSTEP * STEP['H0']) / 100.0
    h_hi = (CENTRE['H0'] + NSTEP * STEP['H0']) / 100.0
    om_lo, om_hi = CENTRE['OM'] - NSTEP * STEP['OM'], CENTRE['OM'] + NSTEP * STEP['OM']
    wm = np.linspace(om_lo * h_lo ** 2, om_hi * h_hi ** 2, n_wm)
    wb = np.linspace(CENTRE['WB'] - NSTEP * STEP['WB'], CENTRE['WB'] + NSTEP * STEP['WB'], n_wb)
    #: the sum axis covers the profile's nodes and a little beyond, so no node is extrapolated
    ss = np.linspace(0.0, 0.70, n_s)
    H0 = CENTRE['H0']
    jobs = [(float(H0), float(a / (H0 / 100.0) ** 2), float(b), float(s))
            for a in wm for b in wb for s in ss]
    print('    %d probes on %d workers' % (len(jobs), workers), flush=True)
    with ThreadPoolExecutor(max_workers=workers) as ex:
        res = list(ex.map(lambda j: probe(*j), jobs))
    Z = np.array([r['r_drag'] for r in res], float).reshape(n_wm, n_wb, n_s)
    ZD = np.array([r['z_drag'] for r in res], float).reshape(n_wm, n_wb, n_s)
    np.savez(os.path.join(HERE, 'rd_grid_nufd.npz'),
             omega_m=wm, omega_b=wb, sums=ss, r_drag=Z, z_drag=ZD)
    print('    %d x %d x %d nodes, r_d %.4f to %.4f Mpc' % (n_wm, n_wb, n_s, Z.min(), Z.max()))
    print('    and the SUM axis is no longer a constant: at the grid centre r_d runs %s'
          % ' '.join('%.4f' % v for v in Z[n_wm // 2, n_wb // 2, :]))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
