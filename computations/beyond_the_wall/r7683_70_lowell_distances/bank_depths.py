#!/usr/bin/env python3
"""r7683+70: the low-l depths at l = 2-8 at the DISTANCES' POINT (68.60, 0.2973), split clock, banked beside the refit rows.

Rows, all at the distances' point (H0 68.60, Om 0.2973, omega_b 0.02237, radiation 4.1833e-5/h^2 -- HIER's defaults, OBF/ORF unset):
  * armA_exact   -- the receipt's own `armA` (CAMB's exact transfer through the discrete projection), lifted by ast;
  * armB_frozen / armB_decoupled -- the sweep's two adjudicated cases through the receipt's arm-B harness (lifted by
    `r7109_directions/rederive_lowell_sweep.engine()`), with SPLITCLOCK=1, exactly as r7675's `run_bank.py`.
Recipe checks: arm A at the adjudicated point (68.60, 0.2973) against P15's printed seven; arm B against r7675's
banked `spectra/cc66_lowell_sweep_leafrec1.npz`.
Banked as `spectra/p15_lowell_depths_distances_leafrec1.npz` (an addition), with `config` and `manifest`. Writes `depths.json`.
Recovery = first l >= 5 with depth >= 0.99.
"""
import ast
import importlib.util
import json
import os
import subprocess
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.join(HERE, '..')
ROOT = os.path.abspath(os.path.join(BW, '..', '..'))
SP = os.path.join(BW, 'spectra')
RECEIPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                       'P15_the_low_multipole_depth_gap_closes_and_two_defects_were_cancelling.py')
ARP, WB = (68.60, 0.2973), 0.02237
ELLS = list(range(2, 9))
PRINTED = [0.487, 0.435, 0.359, 0.666, 0.911, 0.983, 0.998]          # P15 l.2809-2810, the adjudicated point


def recovery(d):
    return next((l for l, v in zip(ELLS, d) if l >= 5 and v >= 0.99), None)


tree = ast.parse(open(RECEIPT, encoding='utf-8').read())
keep = [n for n in tree.body if isinstance(n, (ast.Import, ast.ImportFrom))
        or (isinstance(n, ast.FunctionDef) and n.name in ('armA', 'r0_of'))
        or (isinstance(n, ast.Assign) and any(getattr(t, 'id', None) in ('C', 'NS', 'LMAX') for t in n.targets))]
A = {'__name__': 'armA_lift', '__file__': RECEIPT}
exec(compile(ast.Module(body=keep, type_ignores=[]), RECEIPT + '[armA]', 'exec'), A)

_s = importlib.util.spec_from_file_location('rl', os.path.join(BW, 'r7109_directions', 'rederive_lowell_sweep.py'))
rl = importlib.util.module_from_spec(_s)
_s.loader.exec_module(rl)
ns = rl.engine()
ns['R0'].setdefault(ARP, ns['r0_of'](*ARP))   # the receipt's own ADJ key when equal
ENV_AR = {'SPLITCLOCK': '1'}                  # the distances' point's own omega_b and radiation: OBF/ORF unset
CASES = {k: env for k, w, env in rl.CASES if w == 'ADJ'}

res, out = {}, {'ells': np.array(ELLS)}
for label, (H0, Om), wb in (('distances', ARP, WB),):
    t0 = time.time()
    e, r = A['armA'](H0, Om, ombh2=wb)
    d = dict(zip((int(x) for x in e), (float(x) for x in r)))
    res[f'armA_{label}'] = dict(depths=[round(d[l], 4) for l in ELLS], recovery=recovery([d[l] for l in ELLS]),
                                wall_s=round(time.time() - t0, 1))
res['armA_recipe_check'] = dict(printed=PRINTED, max_abs=max(abs(round(a, 3) - b) for a, b in
                                                             zip(res['armA_distances']['depths'], PRINTED)))
out['armA_exact'] = np.array(res['armA_distances']['depths'])

bank75 = np.load(os.path.join(SP, 'cc66_lowell_sweep.npz'))      # the one-clock namesake at this same point
for key, name in (('FROZEN_adjudicated_KLO_0_1', 'armB_frozen'),
                  ('DECOUPLED_adjudicated_KLO_0_1_NS3_60000', 'armB_decoupled')):
    t0 = time.time()
    v, meta = ns['armB'](ARP, **CASES[key], **ENV_AR)
    if v is None:
        sys.exit(f'{key}: {meta}')
    v = [round(float(x), 4) for x in v[:len(ELLS)]]
    res[name] = dict(depths=v, recovery=recovery(v), minimum_at=ELLS[int(np.argmin(v[:4]))],
                     vs_one_clock_namesake=[round(float(a - b), 4) for a, b in zip(v, bank75[key][:len(ELLS)])],
                     wall_s=round(time.time() - t0, 1), sweep_key=key)
    out[name] = np.array(v)
    res[name]['A_minus_B'] = [round(a - b, 4) for a, b in zip(res['armA_distances']['depths'], v)]
    print(name, v, res[name]['wall_s'], flush=True)

blob = subprocess.run(['git', 'rev-parse', 'HEAD:storyboard_receipts/HIER_photon_hierarchy.py'], cwd=ROOT,
                      capture_output=True, text=True).stdout.strip()
out['config'] = np.array(json.dumps(dict(
    instrument='receipt armA (CAMB) + storyboard_receipts/HIER_photon_hierarchy.py (arm B)', HIER_blob=blob,
    camb=__import__('camb').__version__, H0=ARP[0], Om=ARP[1], WBH2=WB, radiation='4.1833e-5/h^2', SPLITCLOCK=True,
    LEAFREC=True, ARM='cr (arm of record); arm A is CAMB with its own recombination',
    LEAFSCALES=None, ZSTART=None, STACKPERT=None, VISLEAF=None,
    note_defining='LEAFSCALES/ZSTART/STACKPERT/VISLEAF are ACOUSTIC_two_arm.py switches; neither CAMB nor HIER has '
                  'them, so each is written out as null.')))
out['manifest'] = np.array(json.dumps(dict(
    stem='p15_lowell_depths_distances_leafrec1', namesake='P15 l.2809-2810 (arm A) and spectra/cc66_lowell_sweep.npz '
    '(arm B, one clock) at this same point', LEAFREC=1, rows=['armA_exact', 'armB_frozen', 'armB_decoupled'],
    recovery_definition='first l >= 5 with depth >= 0.99',
    held='the receipt\'s armA and its arm-B harness and CASES, unaltered; arm B adds SPLITCLOCK=1 only',
    note_r7683='the distances\' point P15\'s low-l section stays on (69, r7683); sibling of p15_lowell_depths_leafrec1 (the refit point)')))
np.savez(os.path.join(SP, 'p15_lowell_depths_distances_leafrec1.npz'), **out)
res['banked'] = 'spectra/p15_lowell_depths_distances_leafrec1.npz'
json.dump(res, open(os.path.join(HERE, 'depths.json'), 'w'), indent=1)
print(json.dumps(res, indent=1))
