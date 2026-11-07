#!/usr/bin/env python3
"""r7701+70 item 2: the three convergence knobs on HIER under (L) (SPLITCLOCK=L), distances point, both builds.

Through the receipt's arm-B harness (`r7109_directions/rederive_lowell_sweep.engine()`), exactly as r7695's `run_leafpert.py`,
with ONE knob changed from the sweep's adjudicated CASES entry per run: NTAU 300000 (doubled opacity grid), NS3 halved
(30000 DECOUPLED, 450 FROZEN, whose CASES entry leaves NS3 at HIER's default 900), KLO 0.02 (extended continuum).
Each run's depths are compared with the banked (L) row (`p15_lowell_depths_leafpert_leafrec1`, distances).
Banked as `spectra/p15_lowell_depths_leafpert_convergence_leafrec1.npz` (addition). Writes `convergence.json`.
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
ELLS = list(range(2, 9))
_s = importlib.util.spec_from_file_location('rl', os.path.join(BW, 'r7109_directions', 'rederive_lowell_sweep.py'))
rl = importlib.util.module_from_spec(_s)
_s.loader.exec_module(rl)
ns = rl.engine()
CASES = {k: env for k, w, env in rl.CASES if w == 'ADJ'}
F, D = 'FROZEN_adjudicated_KLO_0_1', 'DECOUPLED_adjudicated_KLO_0_1_NS3_60000'
BG = (68.60, 0.2973)
ns['R0'].setdefault(BG, ns['r0_of'](*BG))
for k in ('SPLITCLOCK', 'SPLITIC', 'ARM', 'NS3', 'NTAU', 'KLO', 'NLOW', 'ZEND', 'ZDEC'):
    assert k not in os.environ, k
KNOBS = {'ntau_x2': {'NTAU': 300000}, 'ns3_half': None, 'klo_0_02': {'KLO': 0.02}}
NS3_HALF = {F: 450, D: 30000}
BUILD = {F: 'frozen', D: 'decoupled'}
JOBS = [(c, k) for c in (D, F) for k in KNOBS]


def run(job):
    case, knob = job
    over = KNOBS[knob] if KNOBS[knob] is not None else {'NS3': NS3_HALF[case]}
    env = {**CASES[case], **over, 'SPLITCLOCK': 'L'}
    t0 = time.time()
    v, meta = ns['armB'](BG, **env)
    rec = dict(env={k: (str(x) if not isinstance(x, (int, float)) else x) for k, x in env.items()},
               wall_s=round(time.time() - t0, 1))
    if v is None:
        rec['nonfinite'] = str(meta)
    else:
        rec['depths'] = [round(float(x), 4) for x in v[:len(ELLS)]]
    print(BUILD[case], knob, rec.get('depths', rec.get('nonfinite')), rec['wall_s'], flush=True)
    return (BUILD[case], knob), rec


with ThreadPoolExecutor(4) as ex:
    got = dict(ex.map(run, JOBS))

BL = np.load(os.path.join(SP, 'p15_lowell_depths_leafpert_leafrec1.npz'))
res, out = {'ells': ELLS}, {'ells': np.array(ELLS)}
worst = (0.0, None)
for b in ('frozen', 'decoupled'):
    base = [round(float(x), 4) for x in BL[f'distances__armB_{b}__L']]
    res[b] = {'base_L': base}
    for k in KNOBS:
        r = got[(b, k)]
        if 'depths' in r:
            mv = [round(x - y, 4) for x, y in zip(r['depths'], base)]
            rel = [round(100 * (x - y) / y, 3) for x, y in zip(r['depths'], base)]
            i = int(np.argmax(np.abs(rel)))
            r.update(move=mv, rel_pct=rel, largest=dict(l=ELLS[i], abs=mv[i], rel_pct=rel[i]),
                     minimum_at=ELLS[int(np.argmin(r['depths'][:4]))],
                     recovery=next((l for l, x in zip(ELLS, r['depths']) if l >= 5 and x >= 0.99), None))
            out[f'distances__armB_{b}__L__{k}'] = np.array(r['depths'])
            if abs(rel[i]) > abs(worst[0]):
                worst = (rel[i], f'{b}/{k} at l={ELLS[i]}')
        res[b][k] = r
res['largest_move'] = dict(rel_pct=worst[0], where=worst[1])
blob = subprocess.run(['git', 'rev-parse', 'HEAD:storyboard_receipts/HIER_photon_hierarchy.py'], cwd=ROOT,
                      capture_output=True, text=True).stdout.strip()
rows = [k for k in out if '__armB_' in k]
out['config'] = np.array(json.dumps(dict(
    instrument='storyboard_receipts/HIER_photon_hierarchy.py (arm B) through the receipt arm-B harness', HIER_blob=blob,
    point=dict(H0=BG[0], Om=BG[1], WBH2=0.02237, radiation='4.1833e-5/h^2', BR0=ns['R0'][BG]),
    SPLITCLOCK={k: 'L' for k in rows},
    pairing={k: '(L): HIER SPLITCLOCK=L, as p15_lowell_depths_leafpert_leafrec1' for k in rows},
    numerics={f'distances__armB_{b}__L__{k}': got[(b, k)]['env'] for b in ('frozen', 'decoupled') for k in KNOBS
              if f'distances__armB_{b}__L__{k}' in out},
    ARM='HIER with ARM unset; the arm of record\'s construction (L)', LEAFREC=True,
    LEAFSCALES=None, ZSTART=None, STACKPERT=None, VISLEAF=None,
    note_defining='LEAFSCALES/ZSTART/STACKPERT/VISLEAF are ACOUSTIC_two_arm.py switches; HIER has none, so each is '
                  'written out as null. (L) mirrors STACKPERT unset (LEAFPERT) and VISLEAF=0.')))
out['manifest'] = np.array(json.dumps(dict(
    stem='p15_lowell_depths_leafpert_convergence_leafrec1', LEAFREC=1, rows=rows,
    held="the receipt's arm-B harness and adjudicated CASES with SPLITCLOCK=L; one knob changed per row",
    note_r7701='the convergence sweep on (L) at the distances point (69, r7701); compare with '
               'p15_lowell_depths_leafpert_leafrec1 distances rows')))
np.savez(os.path.join(SP, 'p15_lowell_depths_leafpert_convergence_leafrec1.npz'), **out)
res['banked'] = 'spectra/p15_lowell_depths_leafpert_convergence_leafrec1.npz'
json.dump(res, open(os.path.join(HERE, 'convergence.json'), 'w'), indent=1)
print(json.dumps({k: v for k, v in res.items() if k not in ('frozen', 'decoupled')}, indent=1))
