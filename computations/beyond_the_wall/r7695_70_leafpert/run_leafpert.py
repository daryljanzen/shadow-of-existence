#!/usr/bin/env python3
"""r7695+70 step 1: HIER under (L), SPLITCLOCK=L, at both points and both adjudicated builds, banked per row.

Through the receipt's arm-B harness (`r7109_directions/rederive_lowell_sweep.engine()`), exactly as r7681/r7683's
`bank_depths.py`, with SPLITCLOCK=L in place of SPLITCLOCK=1. Also run here, from the same tree: the ONE-CLOCK legs at the
refit point (SPLITCLOCK unset), which no bank holds for DECOUPLED. The SPLITCLOCK=1 rows and the distances point's one-clock
rows are read from their banks (r7681, r7683, r7689) -- and the `=1` rows are bitwise reproducible (gate G1).
Separation at l = 2..8: total split shift = split(=1) - one clock; dynamics share = split(=1) - (L); projection share =
(L) - one clock. Banked as `spectra/p15_lowell_depths_leafpert_leafrec1.npz` (addition). Writes `leafpert.json`.
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
BUILD = {F: 'frozen', D: 'decoupled'}
POINTS = {
    'refit': dict(bg=(68.570730, 0.291246), wb=0.021643, rad='4.15e-5/h^2',
                  env={'OBF': f'{0.021643 / 0.02237:.12f}', 'ORF': f'{4.15 / 4.1833:.12f}'}),
    'distances': dict(bg=(68.60, 0.2973), wb=0.02237, rad='4.1833e-5/h^2', env={}),
}
for p in POINTS.values():
    ns['R0'].setdefault(p['bg'], ns['r0_of'](*p['bg']))
for k in ('SPLITCLOCK', 'SPLITIC', 'ARM'):
    assert k not in os.environ, k

JOBS = []
for pt in POINTS:
    for case in (D, F):
        JOBS.append((pt, case, 'L', {'SPLITCLOCK': 'L'}))
for case in (D, F):
    JOBS.append(('refit', case, 'one_clock', {}))


def run(job):
    pt, case, lab, extra = job
    t0 = time.time()
    v, meta = ns['armB'](POINTS[pt]['bg'], **CASES[case], **POINTS[pt]['env'], **extra)
    if v is None:
        raise SystemExit(f'{job}: {meta}')
    v = [round(float(x), 4) for x in v[:len(ELLS)]]
    print(pt, BUILD[case], lab, v, round(time.time() - t0), flush=True)
    return (pt, BUILD[case], lab), dict(depths=v, wall_s=round(time.time() - t0, 1))


with ThreadPoolExecutor(4) as ex:
    got = dict(ex.map(run, sorted(JOBS, key=lambda j: j[1] != D)))

# reference rows from the banks
B81 = np.load(os.path.join(SP, 'p15_lowell_depths_leafrec1.npz'))
B83 = np.load(os.path.join(SP, 'p15_lowell_depths_distances_leafrec1.npz'))
B89 = np.load(os.path.join(SP, 'p15_lowell_depths_distances_oneclock_leafrec1.npz'))
REF = {'refit': {'split1': B81, 'armA': B81}, 'distances': {'split1': B83, 'armA': B83, 'one_clock': B89}}


def rec(d):
    return next((l for l, x in zip(ELLS, d) if l >= 5 and x >= 0.99), None)


res, out = {'ells': ELLS}, {'ells': np.array(ELLS)}
for pt in POINTS:
    A = [float(x) for x in REF[pt]['armA']['armA_exact']]
    res[pt] = {'armA_exact': [round(x, 4) for x in A]}
    for b in ('frozen', 'decoupled'):
        L = got[(pt, b, 'L')]['depths']
        S1 = [round(float(x), 4) for x in REF[pt]['split1'][f'armB_{b}']]
        OC = (got[(pt, b, 'one_clock')]['depths'] if pt == 'refit'
              else [round(float(x), 4) for x in REF[pt]['one_clock'][f'armB_{b}']])
        tot = [round(s - o, 4) for s, o in zip(S1, OC)]
        dyn = [round(s - l, 4) for s, l in zip(S1, L)]
        prj = [round(l - o, 4) for l, o in zip(L, OC)]
        res[pt][b] = dict(L=L, split1=S1, one_clock=OC, total_shift=tot, dynamics_share=dyn, projection_share=prj,
                          dynamics_fraction_l3=round(dyn[1] / tot[1], 3) if tot[1] else None,
                          L_rel_armA_pct=[round(100 * (l - a) / a, 2) for l, a in zip(L, A)],
                          minimum_at=ELLS[int(np.argmin(L[:4]))], recovery=rec(L),
                          wall_s=got[(pt, b, 'L')]['wall_s'])
        out[f'{pt}__armB_{b}__L'] = np.array(L)
        if pt == 'refit':
            out[f'refit__armB_{b}__one_clock'] = np.array(OC)

blob = subprocess.run(['git', 'rev-parse', 'HEAD:storyboard_receipts/HIER_photon_hierarchy.py'], cwd=ROOT,
                      capture_output=True, text=True).stdout.strip()
PAIR_L = ('(L): perturbations on the LEAF rate chain-ruled onto the stacking grid (HIER SPLITCLOCK=L); grid, '
          'projection D_M on the stacking rate; ionisation on the leaf rate; source Psi and visibility measure on the grid '
          'clock, as ACOUSTIC_two_arm.py LEAFPERT/VISLEAF=0')
PAIR_1 = 'one clock: the leaf rate for everything (HIER SPLITCLOCK unset)'
pairing = {k: (PAIR_L if k.endswith('__L') else PAIR_1) for k in out if '__armB_' in k}
out['config'] = np.array(json.dumps(dict(
    instrument='storyboard_receipts/HIER_photon_hierarchy.py (arm B) through the receipt arm-B harness', HIER_blob=blob,
    points={k: dict(H0=v['bg'][0], Om=v['bg'][1], WBH2=v['wb'], radiation=v['rad'], BR0=ns['R0'][v['bg']])
            for k, v in POINTS.items()},
    SPLITCLOCK={k: ('L' if k.endswith('__L') else None) for k in pairing}, pairing=pairing,
    ARM='per row: HIER with ARM unset; __L rows are the arm of record\'s construction (L), one-clock rows the leaf rate',
    LEAFREC=True, LEAFSCALES=None, ZSTART=None, STACKPERT=None, VISLEAF=None,
    note_defining='LEAFSCALES/ZSTART/STACKPERT/VISLEAF are ACOUSTIC_two_arm.py switches; HIER has none, so each is '
                  'written out as null. (L) mirrors STACKPERT unset (LEAFPERT) and VISLEAF=0.')))
out['manifest'] = np.array(json.dumps(dict(
    stem='p15_lowell_depths_leafpert_leafrec1', LEAFREC=1, rows=[k for k in out if '__armB_' in k],
    recovery_definition='first l >= 5 with depth >= 0.99',
    held="the receipt's arm-B harness and CASES, unaltered; SPLITCLOCK=L in place of r7681/r7683's SPLITCLOCK=1",
    note_r7695='HIER under (L) at both points (69, r7695); siblings p15_lowell_depths_leafrec1 (refit, =1), '
               'p15_lowell_depths_distances_leafrec1 (distances, =1), p15_lowell_depths_distances_oneclock_leafrec1')))
np.savez(os.path.join(SP, 'p15_lowell_depths_leafpert_leafrec1.npz'), **out)
res['banked'] = 'spectra/p15_lowell_depths_leafpert_leafrec1.npz'
res['walls'] = {f'{a}/{b}/{c}': v['wall_s'] for (a, b, c), v in got.items()}
json.dump(res, open(os.path.join(HERE, 'leafpert.json'), 'w'), indent=1)
print(json.dumps(res, indent=1))
