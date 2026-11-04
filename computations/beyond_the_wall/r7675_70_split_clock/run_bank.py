#!/usr/bin/env python3
"""r7675+70: the low-l sweep's two adjudicated configurations on the arm of record, banked, and arm A beside them.

Arm B (the sweep): `cc66_lowell_sweep`'s two adjudicated cases, with `r7109_directions/rederive_lowell_sweep.py`'s own
CASES and the receipt's own harness lifted by its `engine()`, at the refit licensed point:
  H0 68.570730, Om 0.291246 (BH0/BOM, R0 from the receipt's r0_of), omega_b 0.021643 (OBF = 0.021643/0.02237),
  radiation 4.15e-5/h^2 (ORF = 4.15/4.1833), SPLITCLOCK=1 (grid and projection on the stacking rate, xe on the leaf).
Banked as `spectra/cc66_lowell_sweep_leafrec1.npz`: the two keys under the namesake's own key names plus `ells`, with
`config` and `manifest` (an addition; the namesake is untouched).

Arm A (CAMB, the figures P15 prints) is not a LEAFREC object. It is reported beside, at the adjudicated point (the
recipe check against 0.487/0.435/0.359/0.666) and at the refit licensed point with omega_b 0.021643. It is not banked.
Writes `result.json`. The recovery multipole is the first l >= 5 with depth >= 0.99.
"""
import ast
import importlib.util
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.join(HERE, '..')
ROOT = os.path.abspath(os.path.join(BW, '..', '..'))
SP = os.path.join(BW, 'spectra')
RECEIPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                       'P15_the_low_multipole_depth_gap_closes_and_two_defects_were_cancelling.py')
_s = importlib.util.spec_from_file_location('rl', os.path.join(BW, 'r7109_directions', 'rederive_lowell_sweep.py'))
rl = importlib.util.module_from_spec(_s)
_s.loader.exec_module(rl)
ns = rl.engine()
ARP = (68.570730, 0.291246)
WB = 0.021643
ENV_AR = {'OBF': f'{WB / 0.02237:.12f}', 'ORF': f'{4.15 / 4.1833:.12f}', 'SPLITCLOCK': '1'}
ns['R0'][ARP] = ns['r0_of'](*ARP)
bank = np.load(os.path.join(SP, 'cc66_lowell_sweep.npz'))
ells = [int(x) for x in bank['ells']]


def recovery(d):
    return next((l for l, v in zip(ells, d) if l >= 5 and v >= 0.99), None)


def lift_armA():
    tree = ast.parse(open(RECEIPT, encoding='utf-8').read())
    keep = [n for n in tree.body if isinstance(n, (ast.Import, ast.ImportFrom))
            or (isinstance(n, ast.FunctionDef) and n.name in ('armA', 'r0_of'))
            or (isinstance(n, ast.Assign) and any(getattr(t, 'id', None) in ('C', 'NS', 'LMAX') for t in n.targets))]
    g = {'__name__': 'armA_lift', '__file__': RECEIPT}
    exec(compile(ast.Module(body=keep, type_ignores=[]), RECEIPT + '[armA]', 'exec'), g)
    return g


res = {'point': dict(H0=ARP[0], Om=ARP[1], ombh2=WB, radiation='4.15e-5/h^2', SPLITCLOCK=1), 'armB': {}, 'armA': {}}
out = {'ells': bank['ells']}
for key, which, env in rl.CASES:
    if which != 'ADJ':
        continue
    t0 = time.time()
    v, meta = ns['armB'](ARP, **env, **ENV_AR)
    if v is None:
        sys.exit(f'{key}: FAILED {meta}')
    v = np.asarray(v, float)[:len(ells)]
    ns_v = np.asarray(bank[key], float)
    out[key] = np.round(v, 4)                 # the namesake's own precision (its producer rounds to 4 dp)
    res['armB'][key] = dict(depths=[round(float(x), 4) for x in v], namesake=[float(x) for x in ns_v],
                            delta=[round(float(a - b), 4) for a, b in zip(v, ns_v)],
                            minimum_at=ells[int(np.argmin(v[:4]))], recovery=recovery(v),
                            recovery_namesake=recovery(ns_v), wall_s=round(time.time() - t0, 1), meta=str(meta)[:160])
    print(key, res['armB'][key]['depths'], res['armB'][key]['wall_s'], 's', flush=True)

g = lift_armA()
for label, (H0, Om), wb in (('adjudicated', (68.60, 0.2973), 0.02237), ('refit_licensed', ARP, WB)):
    t0 = time.time()
    e, r = g['armA'](H0, Om, ombh2=wb)
    d = {int(l): float(x) for l, x in zip(e, r)}
    res['armA'][label] = dict(depths={l: round(d[l], 4) for l in range(2, 9) if l in d},
                              recovery=next((l for l in range(5, 9) if d.get(l, 0) >= 0.99), None),
                              wall_s=round(time.time() - t0, 1))
    print('armA', label, res['armA'][label]['depths'], flush=True)

import subprocess
cfg = subprocess.run(['git', 'rev-parse', 'HEAD:storyboard_receipts/HIER_photon_hierarchy.py'], cwd=ROOT,
                     capture_output=True, text=True).stdout.strip()
out['config'] = np.array(json.dumps(dict(instrument='storyboard_receipts/HIER_photon_hierarchy.py', instrument_blob=cfg,
                                         ARM='lcdm(branch)', SPLITCLOCK=True, LEAFREC=True, H0_L=ARP[0],
                                         OMF=ARP[1] / 0.3150, OBF=WB / 0.02237, ORF=4.15 / 4.1833, ZS=1e6,
                                         LEAFSCALES=None, ZSTART=None, STACKPERT=None, VISLEAF=None,
                                         note_defining='LEAFSCALES/ZSTART/STACKPERT/VISLEAF are ACOUSTIC_two_arm.py '
                                                       'switches; HIER has none of them, so each is written out as '
                                                       'null (not a switch of this instrument). Its onset is ZS.')))
out['manifest'] = np.array(json.dumps(dict(
    stem='cc66_lowell_sweep_leafrec1', namesake='cc66_lowell_sweep', LEAFREC=1,
    point=dict(H0=ARP[0], Om=ARP[1], WBH2=WB, radiation='4.15e-5/h^2'),
    keys='the namesake\'s two ADJUDICATED keys only; its six CONTROL keys need no counterpart (r7669: one rate is '
         'correct on the control)',
    switches='the receipt\'s arm-B harness (rederive_lowell_sweep.engine) with its own CASES; BH0/BOM at the point, '
             'BR0 = r0_of(point), OBF, ORF, SPLITCLOCK=1',
    held='the sweep\'s numerical axes (NTAU, KLO, NLOW, ZDEC, NS3, ZEND) and its tilt 0.9649, as recorded',
    note_r7675='SPLITCLOCK=1: the time grid and projection on the stacking rate, xe_history on the leaf rate; '
               'byte-identical unset (r7675_70_split_clock/gate_unset.json)')))
np.savez(os.path.join(SP, 'cc66_lowell_sweep_leafrec1.npz'), **out)
res['banked'] = 'spectra/cc66_lowell_sweep_leafrec1.npz'
json.dump(res, open(os.path.join(HERE, 'result.json'), 'w'), indent=1)
print(json.dumps(res, indent=1))
