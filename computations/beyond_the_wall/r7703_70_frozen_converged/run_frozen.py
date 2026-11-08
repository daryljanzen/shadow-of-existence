#!/usr/bin/env python3
"""r7703+70 item 2: FROZEN converged in NS3, on (L) at the refit point and on the control background (one clock).
The distances point's (L) rungs exist: 1800 in r7701's ns3_frozen_followup.json, 2400 in diag_2400.log here.
Each run is the receipt's own `_RUN` (read from its source) plus one line printing max|Phi| over the stored source
window, because r7703 item 1 found that a finite blow-up passes the harness's isfinite guard and returns r = 1."""
import importlib.util, json, os, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); BW = os.path.join(HERE, '..')
_s = importlib.util.spec_from_file_location('rl', os.path.join(BW, 'r7109_directions', 'rederive_lowell_sweep.py'))
rl = importlib.util.module_from_spec(_s); _s.loader.exec_module(rl)
ns = rl.engine(); FROZEN = {k: env for k, w, env in rl.CASES}['FROZEN_adjudicated_KLO_0_1']
POINTS = {'refit_L': ((68.570730, 0.291246), {'OBF': f'{0.021643 / 0.02237:.12f}', 'ORF': f'{4.15 / 4.1833:.12f}',
                                              'SPLITCLOCK': 'L'}),
          'control': (ns['CTL'], {})}
JOBS = [('refit_L', n) for n in (1800, 2400)] + [('control', n) for n in (900, 1800, 2400)]
GUARD = "\nprint('PHIMAX %.6g' % float(np.max(np.abs(Yv[:,:,2]))))\n"
for bg, _ in POINTS.values():
    ns['R0'].setdefault(bg, ns['r0_of'](*bg))
for k in ('SPLITCLOCK', 'SPLITIC', 'ARM', 'HKCAP', 'LG', 'LN'):
    assert k not in os.environ, k


def run(job):
    pt, n3 = job; bg, extra = POINTS[pt]; t0 = time.time()
    env = dict(os.environ, BH0=f"{bg[0]}", BOM=f"{bg[1]}", BR0=f"{ns['R0'][bg]:.10f}", HIER_DIR=ns['HIER_DIR'])
    env.update({k: str(v) for k, v in dict(FROZEN, NS3=n3, **extra).items()})
    p = subprocess.run([sys.executable, '-c', ns['_RUN'] + GUARD], env=env, capture_output=True, text=True)
    res = [l for l in p.stdout.splitlines() if l.startswith('RESULT ')]
    phm = [float(l.split()[1]) for l in p.stdout.splitlines() if l.startswith('PHIMAX')]
    if not res:
        raise SystemExit(f'{job}: {(p.stdout + p.stderr)[-300:]}')
    d = [round(float(x), 4) for x in res[0][7:].split('|')[0].split()[:7]]
    print(pt, n3, d, 'PHIMAX', phm, round(time.time() - t0), flush=True)
    return f'{pt}__NS3_{n3}', dict(depths=d, phimax=phm[0] if phm else None, wall_s=round(time.time() - t0, 1))


with ThreadPoolExecutor(2) as ex:
    out = dict(ex.map(run, JOBS))
json.dump(out, open(os.path.join(HERE, 'frozen_runs.json'), 'w'), indent=1)
print(json.dumps(out, indent=1))
