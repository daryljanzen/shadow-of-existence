#!/usr/bin/env python3
"""r7701+70, UNREGISTERED follow-up to P2's miss: is FROZEN's default late step count (NS3 900, HIER's default, which the
sweep's FROZEN CASES entry leaves unset) converged under (L)? NS3 = 1800 and 3600 at the distances point, otherwise the banked
(L) FROZEN row's settings. Writes `ns3_frozen_followup.json`. Nothing banked: it is a diagnostic of the miss.
"""
import importlib.util
import json
import os
import time
from concurrent.futures import ThreadPoolExecutor

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.join(HERE, '..')
_s = importlib.util.spec_from_file_location('rl', os.path.join(BW, 'r7109_directions', 'rederive_lowell_sweep.py'))
rl = importlib.util.module_from_spec(_s)
_s.loader.exec_module(rl)
ns = rl.engine()
CASES = {k: env for k, w, env in rl.CASES if w == 'ADJ'}
F = 'FROZEN_adjudicated_KLO_0_1'
BG = (68.60, 0.2973)
ns['R0'].setdefault(BG, ns['r0_of'](*BG))


def run(n3):
    t0 = time.time()
    v, meta = ns['armB'](BG, **CASES[F], NS3=n3, SPLITCLOCK='L')
    d = [round(float(x), 4) for x in v[:7]] if v is not None else None
    print(n3, d if d else meta, round(time.time() - t0), flush=True)
    return n3, dict(depths=d, meta=None if d else str(meta), wall_s=round(time.time() - t0, 1))


with ThreadPoolExecutor(2) as ex:
    res = dict(ex.map(run, (1800, 3600)))
base = [round(float(x), 4) for x in np.load(os.path.join(BW, 'spectra', 'p15_lowell_depths_leafpert_leafrec1.npz'))
        ['distances__armB_frozen__L']]
half = json.load(open(os.path.join(HERE, 'convergence.json')))['frozen']['ns3_half']['depths']
out = {'NS3_450': half, 'NS3_900_banked': base, **{f'NS3_{k}': v['depths'] for k, v in res.items()},
       'walls': {k: v['wall_s'] for k, v in res.items()}}
json.dump(out, open(os.path.join(HERE, 'ns3_frozen_followup.json'), 'w'), indent=1)
print(json.dumps(out, indent=1))
