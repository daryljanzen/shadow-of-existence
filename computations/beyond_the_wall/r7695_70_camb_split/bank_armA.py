#!/usr/bin/env python3
"""r7695+70 steps 2-3: bank arm A under (L) and its one-clock gate rows, and set them against arm B (L).

Runs `camb_L.py` at {distances, refit} x {one, L}, two at a time (three at once ran out of memory here). Gate G: the one-clock rows reproduce stock arm A (the
`armA_exact` rows banked at r7681/r7683) to within 1% at every l = 2..8. Step 3: arm A (L) against arm B (L)
(`p15_lowell_depths_leafpert_leafrec1`, both builds) at l = 2..8, relative to arm A (L).
Banked as `spectra/p15_lowell_depths_armA_leafpert_leafrec1.npz` (addition). Writes `armA_L.json`.
"""
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.join(HERE, '..')
ROOT = os.path.abspath(os.path.join(BW, '..', '..'))
SP = os.path.join(BW, 'spectra')
ELLS = list(range(2, 9))
JOBS = [(p, m) for p in ('distances', 'refit') for m in ('one', 'L')]


def run(job):
    env = {k: v for k, v in os.environ.items() if k not in ('SPLITCLOCK', 'SPLITIC', 'ARM')}
    out = subprocess.run([sys.executable, os.path.join(HERE, 'camb_L.py'), *job], capture_output=True, text=True,
                         env=env, cwd=HERE).stdout
    line = next(l for l in out.splitlines() if l.startswith('__R__'))
    return job, json.loads(line[5:])


with ThreadPoolExecutor(2) as ex:
    got = dict(ex.map(run, JOBS))

STOCK = {'distances': np.load(os.path.join(SP, 'p15_lowell_depths_distances_leafrec1.npz'))['armA_exact'],
         'refit': np.load(os.path.join(SP, 'p15_lowell_depths_leafrec1.npz'))['armA_exact']}
BL = np.load(os.path.join(SP, 'p15_lowell_depths_leafpert_leafrec1.npz'))


def rec(d):
    return next((l for l, x in zip(ELLS, d) if l >= 5 and x >= 0.99), None)


res, out = {'ells': ELLS}, {'ells': np.array(ELLS)}
ok = True
for pt in ('distances', 'refit'):
    one = [round(x, 4) for x in got[(pt, 'one')]['depths']]
    L = [round(x, 4) for x in got[(pt, 'L')]['depths']]
    st = [float(x) for x in STOCK[pt]]
    gate = [round(100 * (a - b) / b, 2) for a, b in zip(got[(pt, 'one')]['depths'], st)]
    gate_ok = max(abs(x) for x in gate) < 1.0
    ok &= gate_ok
    r = dict(stock_armA=[round(x, 4) for x in st], armA_one_clock_via_projection=one, gate_rel_pct=gate,
             gate_holds=gate_ok, armA_L=L, L_minus_one=[round(a - b, 4) for a, b in zip(L, one)],
             minimum_at=ELLS[int(np.argmin(L[:4]))], recovery=rec(L))
    for b in ('frozen', 'decoupled'):
        B = [float(x) for x in BL[f'{pt}__armB_{b}__L']]
        r[f'armB_{b}_L'] = [round(x, 4) for x in B]
        r[f'B_minus_A_rel_pct_{b}'] = [round(100 * (x - a) / a, 2) for x, a in zip(B, L)]
    res[pt] = r
    out[f'{pt}__armA__L'] = np.array(L)
    out[f'{pt}__armA__one_clock_gate'] = np.array(one)
res['gate_G_holds'] = ok
out['config'] = np.array(json.dumps(dict(
    instrument='stock CAMB 2.0.4 (the receipt armA parameters) for the dynamics; storyboard_receipts/HIER_photon_hierarchy.py '
               'source_terms and the arm-B harness depth arithmetic for the projection (r7695_70_camb_split/camb_L.py)',
    camb=got[('distances', 'L')]['camb'],
    points={'distances': dict(H0=68.60, Om=0.2973, WBH2=0.02237), 'refit': dict(H0=68.57073, Om=0.291246, WBH2=0.021643)},
    pairing={k: ('(L): CAMB leaf-rate dynamics (its own Recfast, reionisation tau=0.0544); projection chi, visibility '
                 'measure (kappa over d eta_stack, from CAMB opacity) and source Psi on the stacking grid, via HIER '
                 'SPLITCLOCK=L' if k.endswith('__L') else
                 'gate: CAMB dynamics through the same projection on ONE clock (HIER SPLITCLOCK unset)') for k in out
             if '__armA__' in k},
    SPLITCLOCK={k: ('L' if k.endswith('__L') else None) for k in out if '__armA__' in k},
    ARM='CAMB has no ARM switch; __L rows carry the arm of record\'s construction (L) in the projection',
    LEAFREC=True, LEAFSCALES=None, ZSTART=None, STACKPERT=None, VISLEAF=None,
    note_defining='LEAFSCALES/ZSTART/STACKPERT/VISLEAF are ACOUSTIC_two_arm.py switches; neither CAMB nor HIER has '
                  'them, so each is written out as null. (L) mirrors STACKPERT unset (LEAFPERT) and VISLEAF=0.')))
out['manifest'] = np.array(json.dumps(dict(
    stem='p15_lowell_depths_armA_leafpert_leafrec1', LEAFREC=1, rows=[k for k in out if '__armA__' in k],
    gate='one-clock rows reproduce stock armA_exact (r7681/r7683 banks) within 1% at every l = 2..8',
    note_r7695='arm A of the arm of record (69, r7695 item 2); sibling p15_lowell_depths_leafpert_leafrec1 (arm B (L))')))
np.savez(os.path.join(SP, 'p15_lowell_depths_armA_leafpert_leafrec1.npz'), **out)
res['banked'] = 'spectra/p15_lowell_depths_armA_leafpert_leafrec1.npz'
json.dump(res, open(os.path.join(HERE, 'armA_L.json'), 'w'), indent=1)
print(json.dumps(res, indent=1))
sys.exit(0 if ok else 1)
