#!/usr/bin/env python3
"""`r7801+cc66` item ①: the FROZEN build on the ONE RATE at the distances' point, converged in NS3.

The missing leg.  `r7703+70`'s producer banked `distances__armB_frozen__L__*` and
`control__armB_frozen__one_clock__*`, so the one combination the order needs --
`distances__armB_frozen__one_clock__*` -- does not exist.  This adds it by giving that producer's
own `POINTS` table one more entry: the distances' background with NO `SPLITCLOCK` key, which is
what "one rate" is.  Everything else is held: `FROZEN_adjudicated_KLO_0_1`, `NS3` the only knob.

⛔ TWO GUARDS, BOTH INHERITED RATHER THAN INVENTED:
  * `max|Phi|` is printed per rung, because `r7703` item 1 found that a FINITE blow-up passes the
    harness's `isfinite` test and silently returns `r = 1`.  Every banked rung printed <= 0.93.
  * `NS3 >= ~3000` is NOT used: at 3600 the mode at the `HKCAP` edge (`h*k = 0.079998`) blows up at
    `k*eta ~ 250`.  The rungs are 1800 and 2400, as 70's are.

IDEMPOTENT: a rung already in `frozen_one_clock.json` is skipped, so a container restart costs
nothing.  Re-run it as often as you like.
"""
import importlib.util
import json
import os
import subprocess
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.join(HERE, '..')
OUT = os.path.join(HERE, 'frozen_one_clock.json')

_s = importlib.util.spec_from_file_location(
    'rl', os.path.join(BW, 'r7109_directions', 'rederive_lowell_sweep.py'))
rl = importlib.util.module_from_spec(_s)
_s.loader.exec_module(rl)
ns = rl.engine()
FROZEN = {k: env for k, w, env in rl.CASES}['FROZEN_adjudicated_KLO_0_1']

# the distances' point, one clock: SPLITCLOCK is ABSENT, which is the whole difference from 70's
# `distances__armB_frozen__L__*`.  omega_b and the radiation fraction are the point's own, so both
# factors are exactly 1 -- written as the producer writes them rather than as bare 1.0.
DIST = (68.60, 0.2973)
POINTS = {'distances_one_clock': (DIST, {'OBF': f'{0.02237 / 0.02237:.12f}',
                                         'ORF': f'{4.1833 / 4.1833:.12f}'})}
JOBS = [('distances_one_clock', n) for n in (1800, 2400)]
GUARD = "\nprint('PHIMAX %.6g' % float(np.max(np.abs(Yv[:,:,2]))))\n"

for bg, _ in POINTS.values():
    ns['R0'].setdefault(bg, ns['r0_of'](*bg))
for k in ('SPLITCLOCK', 'SPLITIC', 'ARM', 'HKCAP', 'LG', 'LN'):
    assert k not in os.environ, k


def already_running():
    """A solver of this family already in flight, read from /proc rather than by a name test."""
    mine, pid = set(), os.getpid()
    while pid and pid not in (0, 1):
        mine.add(str(pid))
        try:
            pid = int(open(f'/proc/{pid}/stat').read().split()[3])
        except Exception:
            break
    for e in ('/proc/' + d + '/environ' for d in os.listdir('/proc') if d.isdigit()):
        cand = e.split('/')[2]
        if cand in mine:
            continue
        try:
            env = open(e, 'rb').read().decode('utf-8', 'replace')
        except Exception:
            continue
        if 'FROZEN' in env and 'NS3' in env and 'BH0' in env:
            return cand
    return None


def run(job):
    pt, n3 = job
    bg, extra = POINTS[pt]
    t0 = time.time()
    env = dict(os.environ, BH0=f'{bg[0]}', BOM=f'{bg[1]}',
               BR0=f"{ns['R0'][bg]:.10f}", HIER_DIR=ns['HIER_DIR'])
    env.update({k: str(v) for k, v in dict(FROZEN, NS3=n3, **extra).items()})
    assert 'SPLITCLOCK' not in env, 'the one-rate leg must not carry SPLITCLOCK'
    p = subprocess.run([sys.executable, '-c', ns['_RUN'] + GUARD], env=env,
                       capture_output=True, text=True)
    res = [l for l in p.stdout.splitlines() if l.startswith('RESULT ')]
    phm = [float(l.split()[1]) for l in p.stdout.splitlines() if l.startswith('PHIMAX')]
    if not res:
        raise SystemExit(f'{job}: {(p.stdout + p.stderr)[-400:]}')
    d = [round(float(x), 4) for x in res[0][7:].split('|')[0].split()[:7]]
    print(f'  {pt} NS3={n3}  {d}  PHIMAX {phm}  {round(time.time() - t0)}s', flush=True)
    return f'{pt}__NS3_{n3}', dict(depths=d, phimax=phm[0] if phm else None,
                                   wall_s=round(time.time() - t0, 1))


done = json.load(open(OUT)) if os.path.exists(OUT) else {}
todo = [j for j in JOBS if f'{j[0]}__NS3_{j[1]}' not in done]
print(f'  {len(done)} rung(s) already banked, {len(todo)} to run: {todo}')
if todo:
    busy = already_running()
    if busy:
        raise SystemExit(f'  a solver of this family is already running as pid {busy}; not starting a second')
    for j in todo:
        k, v = run(j)
        done[k] = v
        json.dump(done, open(OUT, 'w'), indent=1)      # bank after EACH rung, not at the end
print(json.dumps(done, indent=1))
