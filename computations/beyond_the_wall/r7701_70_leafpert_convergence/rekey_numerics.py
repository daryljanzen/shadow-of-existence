#!/usr/bin/env python3
"""r7701+70 item 1: re-key both (L) banks' configs with each row's numerical knobs. Arrays byte-identical.

* `p15_lowell_depths_leafpert_leafrec1` (HIER via the arm-B harness): each row's knobs are the sweep's adjudicated CASES entry
  as `run_leafpert.py` passed it to `armB` -- read here from `rederive_lowell_sweep.CASES`, not retyped -- plus HIER's own
  default for any knob the entry leaves unset (FROZEN leaves NS3 unset: HIER's `NS3` default, read from the source).
* `p15_lowell_depths_armA_leafpert_leafrec1` (CAMB through the shared projection): KLO and NLOW as `camb_L.py` sets them
  (read from its source); NTAU / NS3 recorded as not applicable, with the grid `camb_L.py` uses instead.
Writes `rekey_numerics.json` (sha before/after, config before/after, the byte-identity check per array).
"""
import hashlib
import importlib.util
import json
import os
import re

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.join(HERE, '..')
ROOT = os.path.abspath(os.path.join(BW, '..', '..'))
SP = os.path.join(BW, 'spectra')
_s = importlib.util.spec_from_file_location('rl', os.path.join(BW, 'r7109_directions', 'rederive_lowell_sweep.py'))
rl = importlib.util.module_from_spec(_s)
_s.loader.exec_module(rl)
CASES = {k: env for k, w, env in rl.CASES if w == 'ADJ'}
HIER = open(os.path.join(ROOT, 'storyboard_receipts', 'HIER_photon_hierarchy.py')).read()
NS3_DEFAULT = int(re.search(r"os\.environ\.get\('NS3','(\d+)'\)", HIER).group(1))
CL = open(os.path.join(BW, 'r7695_70_camb_split', 'camb_L.py')).read()
m = re.search(r'KLO, NLOW = ([0-9.]+), (\d+)', CL)
CAMB_KLO, CAMB_NLOW = float(m.group(1)), int(m.group(2))
F, D = 'FROZEN_adjudicated_KLO_0_1', 'DECOUPLED_adjudicated_KLO_0_1_NS3_60000'


def hier_knobs(case):
    e = dict(CASES[case])
    e.setdefault('NS3', NS3_DEFAULT)
    e['NS3_source'] = 'CASES' if 'NS3' in CASES[case] else 'HIER default'
    return e


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def rekey(stem, numerics, note):
    path = os.path.join(SP, f'{stem}.npz')
    before = sha(path)
    z = np.load(path)
    keys = list(z.files)
    data = {k: z[k] for k in keys}
    z.close()
    cfg = json.loads(str(data['config']))
    man = json.loads(str(data['manifest']))
    assert 'numerics' not in cfg, f'{stem} already re-keyed'
    rows = [k for k in keys if k not in ('ells', 'config', 'manifest')]
    assert set(numerics) == set(rows), (stem, sorted(set(rows) ^ set(numerics)))
    new = dict(cfg, numerics=numerics, note_r7701=note)
    man['note_r7701'] = 'config re-keyed with per-row numerics; every array byte-identical'
    data['config'] = np.array(json.dumps(new))
    data['manifest'] = np.array(json.dumps(man))
    np.savez(path, **{k: data[k] for k in keys})
    z2 = np.load(path)
    assert list(z2.files) == keys
    for k in keys:
        if k in ('config', 'manifest'):
            continue
        assert data[k].dtype == z2[k].dtype and data[k].shape == z2[k].shape and \
            data[k].tobytes() == z2[k].tobytes(), f'{stem}:{k} moved'
    return dict(sha_before=before, sha_after=sha(path), rows=rows, numerics=numerics,
                arrays_byte_identical=[k for k in keys if k not in ('config', 'manifest')])


out = {}
B = 'p15_lowell_depths_leafpert_leafrec1'
rows = [k for k in np.load(os.path.join(SP, f'{B}.npz')).files if '__armB_' in k]
out[B] = rekey(B, {r: hier_knobs(F if '_frozen_' in r else D) for r in rows},
               'per-row NTAU/NS3/KLO/NLOW (and ZEND/ZDEC) as passed to armB from the sweep CASES (r7701, 69)')
A = 'p15_lowell_depths_armA_leafpert_leafrec1'
rows = [k for k in np.load(os.path.join(SP, f'{A}.npz')).files if '__armA__' in k]
grid = 'CAMB opacity and dynamics; projection on camb_L.py\'s own 2801+3001-time grid from eta_rec-160 to eta_0'
out[A] = rekey(A, {r: dict(KLO=CAMB_KLO, NLOW=CAMB_NLOW, NTAU=None, NS3=None, grid=grid,
                           note='NLOW is 320 here against arm B\'s 480: camb_L.py sets it; gate G held at 0.51%')
                   for r in rows},
               'per-row KLO/NLOW as camb_L.py sets them; NTAU/NS3 do not apply (r7701, 69)')
json.dump(out, open(os.path.join(HERE, 'rekey_numerics.json'), 'w'), indent=1)
for k, v in out.items():
    print(k, v['sha_before'][:12], '->', v['sha_after'][:12], 'rows', len(v['rows']))
print('NS3 default', NS3_DEFAULT, 'camb KLO/NLOW', CAMB_KLO, CAMB_NLOW)
