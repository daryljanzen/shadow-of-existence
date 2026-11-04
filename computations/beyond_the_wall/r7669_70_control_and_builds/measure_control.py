#!/usr/bin/env python3
"""r7669+70 ①: does LEAFREC reach the control?

Folds r6941's control recipe, built at LEAFREC=0 and at LEAFREC=1 through the identical code (`launch_control.sh`),
exactly as `r6941_directions/bank.py` folds it (eleven KSLICE pieces of 250 over NK 2547, summed). Then:
  * LEAFREC=1 vs LEAFREC=0, on the folded spectrum and slice by slice;
  * LEAFREC=0 vs the banked namesake `spectra/r6941_fine_lcdm.npz`.
Banks the LEAFREC=1 fold as `spectra/r6941_fine_lcdm_leafrec1.npz` (an addition) with `config` and `manifest`.
Writes `control.json`. Idempotent.
"""
import json
import os
import re
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.join(HERE, '..')
SP = os.path.join(BW, 'spectra')
D = os.environ.get('D', '/tmp/claude-0/-home-user-shadow-of-existence/4913e7eb-3c04-585c-bc52-ac1b69fc5eb8/scratchpad/r7669')
STEP, NK = 250, 2547
TOL = 1e-15          # the registered tolerance for "identical"
LCDM = 'ARM=lcdm HIER=1 LH0=67.410309 LMAXL=2000 LOM=0.309826 LSTEP=1 NS=0.954248 WBH2=0.021966'


def slices(sub):
    fs = sorted((int(re.search(r'_k(\d+)$', x[:-4]).group(1)), x)
                for x in os.listdir(f'{D}/{sub}') if x.startswith('fine_lcdm_k') and x.endswith('.npz'))
    assert [i for i, _ in fs] == list(range(0, NK, STEP)), f'{sub}: slices {[i for i, _ in fs]}'
    for i, _ in fs:
        assert '__DONE__ rc=0' in open(f'{D}/{sub}/fine_lcdm_k{i}.log').read(), f'{sub} k{i}: not rc=0'
    return [np.load(os.path.join(D, sub, x), allow_pickle=True) for _, x in fs]


def fold(ds):
    ls = ds[0]['ls']
    for d in ds:
        assert np.array_equal(d['ls'], ls)
    return dict(ls=ls, Dl=sum(d['Dl'] for d in ds), l_A=ds[0]['l_A'], D_M=ds[0]['D_M'], r_s=ds[0]['r_s'],
                arm=ds[0]['arm'])


def rel(a, b):
    return float(np.max(np.abs(a - b)) / np.max(np.abs(b)))


def wall(sub):
    w = [int(re.search(r'wall=(\d+)s', open(f'{D}/{sub}/fine_lcdm_k{i}.log').read()).group(1))
         for i in range(0, NK, STEP)]
    return dict(per_slice_s=w, sum_s=sum(w), max_s=max(w))


s0, s1 = slices('lr0'), slices('lr1')
f0, f1 = fold(s0), fold(s1)
nm = np.load(os.path.join(SP, 'r6941_fine_lcdm.npz'), allow_pickle=True)
c0, c1 = json.loads(str(s0[0]['config'])), json.loads(str(s1[0]['config']))
diff_cfg = {k: (c0.get(k), c1.get(k)) for k in sorted(set(c0) | set(c1)) if c0.get(k) != c1.get(k)}

res = {
    'recipe': LCDM + ' (r6941_directions/launch.sh fine_lcdm), KSLICE 250 x 11 over NK 2547',
    'tolerance_identical': TOL,
    'config_diff_lr0_vs_lr1': diff_cfg,
    'lr1_vs_lr0': {
        'max_rel_Dl': rel(f1['Dl'], f0['Dl']),
        'bit_identical_Dl': bool(np.array_equal(f1['Dl'], f0['Dl'])),
        'ls_equal': bool(np.array_equal(f1['ls'], f0['ls'])),
        'scalars': {q: [float(f0[q]), float(f1[q])] for q in ('l_A', 'D_M', 'r_s')},
        'per_slice_max_rel': [rel(a['Dl'], b['Dl']) if np.max(np.abs(b['Dl'])) > 0 else 0.0 for a, b in zip(s1, s0)],
    },
    'lr0_vs_namesake': {
        'max_rel_Dl': rel(f0['Dl'], nm['Dl']),
        'bit_identical_Dl': bool(np.array_equal(f0['Dl'], nm['Dl'])),
        'ls_equal': bool(np.array_equal(f0['ls'], nm['ls'])),
        'scalars_namesake': {q: float(nm[q]) for q in ('l_A', 'D_M', 'r_s')},
    },
    'lr1_vs_namesake_max_rel_Dl': rel(f1['Dl'], nm['Dl']),
    'wall': {'lr0': wall('lr0'), 'lr1': wall('lr1')},
}
d = res['lr1_vs_lr0']['max_rel_Dl']
res['verdict'] = ('IDENTICAL (bit for bit)' if res['lr1_vs_lr0']['bit_identical_Dl'] else
                  f'identical within tolerance ({d:.2e} <= {TOL:g})' if d <= TOL else
                  f'MOVES ({d:.3e} > {TOL:g})')

# the LEAFREC=1 fold, banked beside its namesake (addition)
out = dict(f1)
out['config'] = s1[0]['config']
man = dict(stem='r6941_fine_lcdm_leafrec1', namesake='r6941_fine_lcdm', LEAFREC=1,
           point=dict(LH0=67.410309, LOM=0.309826, WBH2=0.021966, NS=0.954248, LEAFREC=1),
           switches=LCDM + ' LEAFREC=1',
           held='r6941 launch fine_lcdm; LSTEP=1, 11 KSLICE pieces of 250; only LEAFREC set',
           note_r7669=f'the control under the switch: vs the same recipe at LEAFREC=0 through the identical code, '
                      f'{res["verdict"]}; vs the namesake {res["lr0_vs_namesake"]["max_rel_Dl"]:.2e} (LEAFREC=0 build)')
assert json.loads(str(out['config'])).get('LEAFREC') is True
out['manifest'] = np.array(json.dumps(man))
np.savez(os.path.join(SP, 'r6941_fine_lcdm_leafrec1.npz'), **out)
res['banked'] = 'spectra/r6941_fine_lcdm_leafrec1.npz'
json.dump(res, open(os.path.join(HERE, 'control.json'), 'w'), indent=1)
print(json.dumps(res, indent=1))
sys.exit(0)
