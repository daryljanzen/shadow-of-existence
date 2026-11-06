#!/usr/bin/env python3
"""r7689+70: the hierarchy ONE-CLOCK (SPLITCLOCK unset) at the distances point, both tower builds, banked with its point.

Point: H0 68.60, Om 0.2973, omega_b 0.02237, radiation 4.1833e-5/h^2 (HIER's defaults; OBF/ORF unset) -- r7683's point.
Rows: the sweep's two adjudicated cases through the receipt's arm-B harness (`r7109_directions/rederive_lowell_sweep.engine()`),
exactly as r7683's `bank_depths.py` with SPLITCLOCK=1 removed. With ARM and SPLITCLOCK unset HIER runs the content-carrying
leaf rate for everything, so the ionisation history is on the leaf rate (LEAFREC=1 in effect; HIER has no LEAFREC switch).
Compared against: the one-clock namesake `cc66_lowell_sweep.npz`, r7683's split rows and arm A
(`p15_lowell_depths_distances_leafrec1.npz`).
Banked as `spectra/p15_lowell_depths_distances_oneclock_leafrec1.npz` (an addition). Writes `one_clock.json`.
"""
import importlib.util
import json
import os
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.join(HERE, '..')
ROOT = os.path.abspath(os.path.join(BW, '..', '..'))
SP = os.path.join(BW, 'spectra')
ARP, WB = (68.60, 0.2973), 0.02237
ELLS = list(range(2, 9))

_s = importlib.util.spec_from_file_location('rl', os.path.join(BW, 'r7109_directions', 'rederive_lowell_sweep.py'))
rl = importlib.util.module_from_spec(_s)
_s.loader.exec_module(rl)
ns = rl.engine()
ns['R0'].setdefault(ARP, ns['r0_of'](*ARP))
CASES = {k: env for k, w, env in rl.CASES if w == 'ADJ'}
assert 'SPLITCLOCK' not in os.environ and 'ARM' not in os.environ

NSK = np.load(os.path.join(SP, 'cc66_lowell_sweep.npz'))
SPL = np.load(os.path.join(SP, 'p15_lowell_depths_distances_leafrec1.npz'))
A = np.asarray(SPL['armA_exact'], float)


def recovery(d):
    return next((l for l, v in zip(ELLS, d) if l >= 5 and v >= 0.99), None)


def run(item):
    key, name = item
    t0 = time.time()
    v, meta = ns['armB'](ARP, **CASES[key])
    if v is None:
        raise SystemExit(f'{key}: {meta}')
    v = [round(float(x), 4) for x in v[:len(ELLS)]]
    split = [float(x) for x in SPL[name]]
    rec = dict(depths=v, recovery=recovery(v), minimum_at=ELLS[int(np.argmin(v[:4]))], sweep_key=key,
               wall_s=round(time.time() - t0, 1),
               vs_namesake=[round(a - float(b), 4) for a, b in zip(v, NSK[key][:len(ELLS)])],
               split_minus_one_clock=[round(s - a, 4) for s, a in zip(split, v)],
               rel_to_armA_pct=[round(100 * (a - b) / b, 2) for a, b in zip(v, A)],
               split_rel_to_armA_pct=[round(100 * (s - b) / b, 2) for s, b in zip(split, A)])
    print(name, v, rec['wall_s'], flush=True)
    return name, rec


ITEMS = (('DECOUPLED_adjudicated_KLO_0_1_NS3_60000', 'armB_decoupled'), ('FROZEN_adjudicated_KLO_0_1', 'armB_frozen'))
with ThreadPoolExecutor(2) as ex:
    res = dict(ex.map(run, ITEMS))
res['armA_exact'] = [round(float(x), 4) for x in A]
res['max_abs_vs_namesake'] = max(abs(x) for n in ('armB_frozen', 'armB_decoupled') for x in res[n]['vs_namesake'])

blob = subprocess.run(['git', 'rev-parse', 'HEAD:storyboard_receipts/HIER_photon_hierarchy.py'], cwd=ROOT,
                      capture_output=True, text=True).stdout.strip()
out = {'ells': np.array(ELLS), 'armB_frozen': np.array(res['armB_frozen']['depths']),
       'armB_decoupled': np.array(res['armB_decoupled']['depths'])}
out['config'] = np.array(json.dumps(dict(
    instrument='storyboard_receipts/HIER_photon_hierarchy.py (arm B) through the receipt arm-B harness', HIER_blob=blob,
    H0=ARP[0], Om=ARP[1], WBH2=WB, radiation='4.1833e-5/h^2', BR0=ns['R0'][ARP], SPLITCLOCK=False, ARM=None,
    LEAFREC=True, note_leafrec='one clock: HIER runs the content-carrying leaf rate for everything, ionisation history '
    'included; HIER has no LEAFREC switch',
    LEAFSCALES=None, ZSTART=None, STACKPERT=None, VISLEAF=None,
    note_defining='LEAFSCALES/ZSTART/STACKPERT/VISLEAF are ACOUSTIC_two_arm.py switches; HIER has none of them, '
                  'so each is written out as null.')))
out['manifest'] = np.array(json.dumps(dict(
    stem='p15_lowell_depths_distances_oneclock_leafrec1',
    namesake='spectra/cc66_lowell_sweep.npz adjudicated rows (one clock, no point recorded)', LEAFREC=1,
    point=dict(H0=ARP[0], Om=ARP[1], WBH2=WB, radiation='4.1833e-5/h^2'), SPLITCLOCK=False,
    rows=['armB_frozen', 'armB_decoupled'], recovery_definition='first l >= 5 with depth >= 0.99',
    held="the receipt's arm-B harness and CASES, unaltered; r7683's run with SPLITCLOCK=1 removed",
    note_r7689='the one-clock leg at the distances point (69, r7689); sibling of '
               'p15_lowell_depths_distances_leafrec1 (split clock, same point)')))
np.savez(os.path.join(SP, 'p15_lowell_depths_distances_oneclock_leafrec1.npz'), **out)
res['banked'] = 'spectra/p15_lowell_depths_distances_oneclock_leafrec1.npz'
json.dump(res, open(os.path.join(HERE, 'one_clock.json'), 'w'), indent=1)
print(json.dumps(res, indent=1))
