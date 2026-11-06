#!/usr/bin/env python3
"""r7693+70 item 1 (approved by 69): re-key the two arm-A/arm-B low-l depth banks with a per-row clock.

`p15_lowell_depths_leafrec1.npz` (r7681, refit point) and `p15_lowell_depths_distances_leafrec1.npz` (r7683, distances
point) carried one bank-level `config` saying `SPLITCLOCK: True` and `ARM: "cr (arm of record); arm A is CAMB..."`,
which is true of the arm-B rows only: `armA_exact` is CAMB on one clock, the leaf rate (r7691+70.1, measured).
This rewrites `config` only:
  * adds `clock` = {row: ...} for every row;
  * `SPLITCLOCK` becomes per-row ({armA_exact: false, armB_*: true});
  * `ARM` keeps the key (a DEFINING switch for check_banked_config) and states the per-row reading;
  * `manifest` gains `note_r7693`.
Every array (`ells`, `armA_exact`, `armB_frozen`, `armB_decoupled`) is written back from the loaded bytes and checked
byte-identical (dtype, shape, tobytes) against the file before the rewrite; the key order and np.savez's
(uncompressed) format are kept. Writes `rekey.json` with each file's sha256 and config before and after.
"""
import hashlib
import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.join(HERE, '..', 'spectra')
STEMS = ('p15_lowell_depths_leafrec1', 'p15_lowell_depths_distances_leafrec1')
ROWS = ('armA_exact', 'armB_frozen', 'armB_decoupled')
CLOCK = {
    'armA_exact': 'one clock: the leaf rate (content-carrying Friedmann rate) for grid, projection, perturbations and '
                  'recombination -- stock CAMB with its own Recfast (r7691+70.1: H_CAMB/H_leaf = 1 to 0.2%, z = 10..1e5)',
    'armB_frozen': 'split: grid, Hc_of and projection on the stacking rate, ionisation history on the leaf rate '
                   '(HIER SPLITCLOCK=1)',
    'armB_decoupled': 'split: grid, Hc_of and projection on the stacking rate, ionisation history on the leaf rate '
                      '(HIER SPLITCLOCK=1)',
}


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


out = {}
for stem in STEMS:
    path = os.path.join(SP, f'{stem}.npz')
    before_sha = sha(path)
    z = np.load(path)
    keys = list(z.files)
    data = {k: z[k] for k in keys}
    z.close()
    cfg = json.loads(str(data['config']))
    man = json.loads(str(data['manifest']))
    assert cfg.get('SPLITCLOCK') is True and 'clock' not in cfg, f'{stem}: already re-keyed or unexpected config'
    new = dict(cfg)
    new['clock'] = {r: CLOCK[r] for r in ROWS}
    new['SPLITCLOCK'] = {'armA_exact': False, 'armB_frozen': True, 'armB_decoupled': True}
    new['ARM'] = ('per row: armB_* are HIER on the arm of record (split clock, the cr arm\'s construction); '
                  'armA_exact is CAMB on one clock (the leaf rate) and carries no ARM switch')
    new['note_r7693'] = ('re-keyed at r7693 (69 approved, r7691+70.1 proposal): SPLITCLOCK and ARM were bank-wide and '
                         'true of the arm-B rows only; arrays untouched')
    man['note_r7693'] = 'config re-keyed per row (clock, SPLITCLOCK, ARM); every array byte-identical to the r76' + \
                        ('81' if stem.endswith('depths_leafrec1') else '83') + ' bank'
    data['config'] = np.array(json.dumps(new))
    data['manifest'] = np.array(json.dumps(man))
    np.savez(path, **{k: data[k] for k in keys})
    z2 = np.load(path)
    assert list(z2.files) == keys
    for k in keys:
        if k in ('config', 'manifest'):
            continue
        a, b = data[k], z2[k]
        assert a.dtype == b.dtype and a.shape == b.shape and a.tobytes() == b.tobytes(), f'{stem}:{k} moved'
    out[stem] = dict(sha_before=before_sha, sha_after=sha(path), keys=keys,
                     arrays_byte_identical=[k for k in keys if k not in ('config', 'manifest')],
                     config_before=cfg, config_after=json.loads(str(z2['config'])))
    print(stem, 'ok', before_sha[:12], '->', out[stem]['sha_after'][:12])
json.dump(out, open(os.path.join(HERE, 'rekey.json'), 'w'), indent=1)
