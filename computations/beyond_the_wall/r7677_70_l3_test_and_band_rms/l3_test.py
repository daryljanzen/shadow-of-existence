#!/usr/bin/env python3
"""r7677+70 item 1: the l = 3 separating test.

The sweep's two adjudicated configurations at the refit licensed point under SPLITCLOCK=1, exactly as r7675's
`run_bank.py` runs them (the receipt's arm-B harness, lifted by `rederive_lowell_sweep.engine()`), varied in one thing:
  (Z) the onset ZS in {1e5, 3e5, 3e6, 1e7} (default 1e6): FROZEN at all four, DECOUPLED at 1e5 and 1e7;
  (C) SPLITIC=cr -- ARM=cr's characteristic initial data under the split: FROZEN and DECOUPLED;
plus the split's own default (ZS 1e6) and the one-clock point-only run (SPLITCLOCK unset), recomputed here so every
row comes from the same tree. Four at a time. Writes `l3_test.json`. Nothing is banked.
"""
import importlib.util
import json
import os
from concurrent.futures import ThreadPoolExecutor

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.join(HERE, '..')
_s = importlib.util.spec_from_file_location('rl', os.path.join(BW, 'r7109_directions', 'rederive_lowell_sweep.py'))
rl = importlib.util.module_from_spec(_s)
_s.loader.exec_module(rl)
ns = rl.engine()
ARP = (68.570730, 0.291246)
ns['R0'][ARP] = ns['r0_of'](*ARP)
BASE = {'OBF': f'{0.021643 / 0.02237:.12f}', 'ORF': f'{4.15 / 4.1833:.12f}'}
CASES = {k: env for k, which, env in rl.CASES if which == 'ADJ'}
F, Dc = 'FROZEN_adjudicated_KLO_0_1', 'DECOUPLED_adjudicated_KLO_0_1_NS3_60000'
ells = [int(x) for x in np.load(os.path.join(BW, 'spectra', 'cc66_lowell_sweep.npz'))['ells']]

JOBS = [(F, 'one_clock', {})]
for case in (F, Dc):
    JOBS.append((case, 'split_ZS1e6', {'SPLITCLOCK': '1'}))
    JOBS.append((case, 'split_SPLITIC_cr', {'SPLITCLOCK': '1', 'SPLITIC': 'cr'}))
for zs in ('1e5', '3e5', '3e6', '1e7'):
    JOBS.append((F, f'split_ZS{zs}', {'SPLITCLOCK': '1', 'ZS': zs}))
for zs in ('1e5', '1e7'):
    JOBS.append((Dc, f'split_ZS{zs}', {'SPLITCLOCK': '1', 'ZS': zs}))


def run(job):
    case, label, extra = job
    import time
    t0 = time.time()
    v, meta = ns['armB'](ARP, **CASES[case], **BASE, **extra)
    rec = dict(wall_s=round(time.time() - t0, 1))
    if v is None:
        rec['error'] = str(meta)[:300]
    else:
        v = [round(float(x), 4) for x in v[:len(ells)]]
        rec.update(depths=v, minimum_at=ells[int(np.argmin(v[:4]))],
                   recovery=next((l for l, x in zip(ells, v) if l >= 5 and x >= 0.99), None))
    print(case[:9], label, rec.get('depths', rec.get('error'))[:4] if rec.get('depths') else rec.get('error'),
          rec['wall_s'], flush=True)
    return f'{case}__{label}', rec


# longest first
JOBS.sort(key=lambda j: j[0] != Dc)
with ThreadPoolExecutor(4) as ex:
    res = dict(ex.map(run, JOBS))
res['ells'] = ells
json.dump(res, open(os.path.join(HERE, 'l3_test.json'), 'w'), indent=1)
