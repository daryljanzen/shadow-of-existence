#!/usr/bin/env python3
"""r7673+70 item 3: price the low-l sweep's arm-of-record form by running it.

Only two of `cc66_lowell_sweep`'s eight configurations use the adjudicated background:
`FROZEN_adjudicated_KLO_0_1` and `DECOUPLED_adjudicated_KLO_0_1_NS3_60000`. The other six are control.
This runs those two through the receipt's own arm-B harness, lifted by `r7109_directions/rederive_lowell_sweep.py`'s
`engine()`, with that file's own CASES:
  * at the recorded adjudicated background (68.60, 0.2973), as the recipe check against the banked keys;
  * at the refit licensed point (68.570730, 0.291246), with ω_b moved to 0.021643 through HIER's `OBF`.
The second run moves the POINT only. HIER has no switch that puts the time grid on the stacking rate while recombination
stays on the leaf rate, so it is still the one-clock arrangement. It is the cheapest approximation, not the arm of record.
Nothing is banked. Writes `lowell_price.json`.
"""
import importlib.util
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.join(HERE, '..')
_s = importlib.util.spec_from_file_location('rl', os.path.join(BW, 'r7109_directions', 'rederive_lowell_sweep.py'))
rl = importlib.util.module_from_spec(_s)
_s.loader.exec_module(rl)
ns = rl.engine()
ARP = (68.570730, 0.291246)
OBF = 0.021643 / 0.02237
ns['R0'][ARP] = ns['r0_of'](*ARP)
bank = np.load(os.path.join(BW, 'spectra', 'cc66_lowell_sweep.npz'))
res = {}
for key, which, env in rl.CASES:
    if which != 'ADJ':
        continue
    for label, bg, extra in (('recorded', ns['ADJ'], {}), ('arm_of_record_point', ARP, {'OBF': f'{OBF:.10f}'})):
        t0 = time.time()
        v, meta = ns['armB'](bg, **env, **extra)
        if v is None:
            res[f'{key}__{label}'] = dict(wall_s=round(time.time() - t0, 1), error=str(meta)[:300])
            print(key, label, 'FAILED', meta, flush=True)
            continue
        r = np.asarray(v, dtype=float)
        rec = dict(wall_s=round(time.time() - t0, 1), values=r.tolist(), meta=str(meta)[:200])
        if label == 'recorded':
            b = bank[key]
            n = min(len(b), len(r))
            rec['vs_bank_max_abs'] = float(np.max(np.abs(r[:n] - b[:n])))
            rec['vs_bank_after_4dp'] = float(np.max(np.abs(np.round(r[:n], 4) - b[:n])))
        else:
            n = min(len(bank[key]), len(r))
            rec['vs_bank'] = (r[:n] - bank[key][:n]).tolist()
        res[f'{key}__{label}'] = rec
        print(key, label, rec['wall_s'], 's', rec.get('vs_bank_max_abs', ''), flush=True)
res['ells'] = bank['ells'].tolist()
json.dump(res, open(os.path.join(HERE, 'lowell_price.json'), 'w'), indent=1)
sys.exit(0)
