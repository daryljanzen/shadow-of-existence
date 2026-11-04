#!/usr/bin/env python3
"""r7669+70 ③: fold `launch_r7041.sh` into the r7041 acceptance bank on the arm of record.

Recipe check first (lr0 = the recorded recipe + LEAFREC=0): every grid's sha256s and r_s against the namesake
`spectra/r7041_accept_digest.npz`, every A_l against `r7041_accept_Al.npz`, every k0 slice against
`r7041_accept_nk_slices.npz`, the four samples against `r7041_accept_sample.npz`. Only if the recipe reproduces is
the lr1 build banked: `spectra/r7041_accept_{digest,Al,sample,nk_slices}_leafrec1.npz`, each in its namesake's key
layout, with `config` and `manifest` (additions). The A_l are computed by `r7041_directions/acceptance_convergence.py`'s
own `acceptance()`, lifted by import, with its own LO/HI/NL. Writes `r7041.json`. Idempotent.
"""
import hashlib
import importlib.util
import json
import os
import re
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.join(HERE, '..')
SP = os.path.join(BW, 'spectra')
D = os.environ.get('D', '/tmp/claude-0/-home-user-shadow-of-existence/4913e7eb-3c04-585c-bc52-ac1b69fc5eb8/scratchpad/r7669/r7041')
_s = importlib.util.spec_from_file_location('acc', os.path.join(BW, 'r7041_directions', 'acceptance_convergence.py'))
acc = importlib.util.module_from_spec(_s)
_s.loader.exec_module(acc)
TAGS = ['base', 'kfac26', 'kfac32', 'kfac40', 'nk15', 'nk20',
        'nlos1120', 'nlos2240', 'nlosw9', 'nlosw12', 'nlosf90', 'lstep4']
KEYS = ('k', 'dk', 'eta', 'x0', 'vis')
SAMPLE = [('cr', 'base'), ('cr', 'kfac40'), ('lcdm', 'base'), ('lcdm', 'kfac40')]
SLICES = (('arm_base', 'real_cr_base_k0'), ('arm_nk15', 'real_cr_nk15_k0'), ('arm_nk20', 'real_cr_nk20_k0'),
          ('ctl_nk15', 'inj_fixed_lcdm_nk15_k0'), ('ctl_nk20', 'inj_fixed_lcdm_nk20_k0'))
AR = 'ARM=cr CRH0=68.570730 CROM=0.291246 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021643 NS=1.015066 LEAFREC=1'
LCDM = 'ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248 LEAFREC=1'
SET = dict(base='', kfac26='KFAC=2.6', kfac32='KFAC=3.2', kfac40='KFAC=4.0', nk15='NK=1274', nk20='NK=1698',
           nlos1120='NLOS=1120', nlos2240='NLOS=2240', nlosw9='NLOSW=9.0', nlosw12='NLOSW=12.0', nlosf90='NLOSF=0.90',
           lstep4='LSTEP=4')
fail = []


def sha(a):
    return hashlib.sha256(np.ascontiguousarray(a).tobytes()).hexdigest()


def build(lr):
    """-> the four banks' dicts for build lr, in the namesake's key layout"""
    dig, Al, sample, sl = {}, {}, {}, {}
    for arm in ('cr', 'lcdm'):
        lA = float(np.load(f'{D}/lr{lr}/grid/g_{arm}_base.npz')['l_A'])
        ls = np.unique(np.round(np.linspace(acc.LO, acc.HI, acc.NL) * lA).astype(int))
        for t in TAGS:
            g = f'{D}/lr{lr}/grid/g_{arm}_{t}.npz'
            gd = np.load(g)
            for q in KEYS:
                dig[f'{arm}_{t}_{q}'] = sha(gd[q])
            dig[f'{arm}_{t}_r_s'] = f"{float(gd['r_s']):.17g}"
            A, wd, _, RS, nk, nlos = acc.acceptance(g, ls)
            Al[f'{arm}_{t}_A'], Al[f'{arm}_{t}_wd'], Al[f'{arm}_{t}_ls'] = A, wd, np.asarray(ls)
            Al[f'{arm}_{t}_n'] = np.array([int(gd['n_modes']), int(gd['nlos'])])
            Al[f'{arm}_{t}_span'] = np.array([float(np.nanmean(2 * RS * wd))])
            if (arm, t) in SAMPLE:
                for q in KEYS + ('r_s', 'l_A'):
                    sample[f'{arm}_{t}_{q}'] = np.asarray(gd[q])
    for nm, tag in SLICES:
        log = open(f'{D}/lr{lr}/k0/{tag}.log').read()
        if '__DONE__ rc=0' not in log:
            fail.append(f'lr{lr} {tag}: not rc=0')
        d = np.load(f'{D}/lr{lr}/k0/{tag}.npz')
        sl[f'{nm}_Dl'], sl[f'{nm}_ls'] = np.asarray(d['Dl']), np.asarray(d['ls'])
    return dict(digest=dig, Al=Al, sample=sample, nk_slices=sl)


def compare(new, name):
    """max relative difference per key against spectra/r7041_accept_<name>.npz (0 for equal strings)"""
    ref = np.load(os.path.join(SP, f'r7041_accept_{name}.npz'))
    out = {}
    for k in ref.files:
        if k not in new:
            out[k] = 'MISSING'
            continue
        a, b = np.asarray(new[k]), ref[k]
        if b.dtype.kind in 'US':
            out[k] = 0.0 if str(a) == str(b) else 1.0
        elif a.shape != b.shape:
            out[k] = f'shape {a.shape} vs {b.shape}'
        else:
            den = np.nanmax(np.abs(b)) if np.any(np.isfinite(b)) else 1.0
            out[k] = float(np.nanmax(np.abs(a - b)) / den) if den > 0 else float(np.nanmax(np.abs(a - b)))
    return out


def worst(c):
    num = [v for v in c.values() if isinstance(v, float)]
    return max(num) if num else None, [k for k, v in c.items() if not isinstance(v, float)]


def walls(lr):
    w = {}
    for sub in ('grid', 'k0'):
        for f in sorted(os.listdir(f'{D}/lr{lr}/{sub}')):
            if f.endswith('.log'):
                m = re.search(r'wall=(\d+)s', open(f'{D}/lr{lr}/{sub}/{f}').read())
                w[f'{sub}/{f[:-4]}'] = int(m.group(1)) if m else None
    return w


res = {'recipe_check_lr0': {}, 'lr1_vs_namesake': {}}
b0, b1 = build(0), build(1)
for name in ('digest', 'Al', 'sample', 'nk_slices'):
    c0 = compare(b0[name], name)
    w0, bad0 = worst(c0)
    res['recipe_check_lr0'][name] = dict(max_rel=w0, nonnumeric=bad0,
                                         keys_off=sorted(k for k, v in c0.items() if v != 0.0))
    c1 = compare(b1[name], name)
    res['lr1_vs_namesake'][name] = dict(
        cr_keys_moved=sorted(k for k, v in c1.items() if v != 0.0 and not k.startswith(('lcdm', 'ctl'))),
        control_keys_moved=sorted(k for k, v in c1.items() if v != 0.0 and k.startswith(('lcdm', 'ctl'))))
recipe_ok = all(not v['keys_off'] for v in res['recipe_check_lr0'].values())
res['recipe_reproduces'] = recipe_ok
res['wall_s'] = {'lr0': walls(0), 'lr1': walls(1)}
res['lr1_l_A'] = {a: float(np.load(f'{D}/lr1/grid/g_{a}_base.npz')['l_A']) for a in ('cr', 'lcdm')}
res['lr1_A_mean_cr_base'] = float(np.nanmean(b1['Al']['cr_base_A']))
res['ns_A_mean_cr_base'] = float(np.nanmean(np.load(os.path.join(SP, 'r7041_accept_Al.npz'))['cr_base_A']))

if recipe_ok and not fail:
    import subprocess
    r = subprocess.run([sys.executable, '-c', 'import ACOUSTIC_two_arm as M; print("__C__" + str(M._resolved_config()))'],
                       cwd=BW, capture_output=True, text=True,
                       env={**os.environ, **dict(x.split('=') for x in AR.split()), 'OMP_NUM_THREADS': '1'})
    cfg = next(l[5:] for l in r.stdout.splitlines() if l.startswith('__C__'))
    assert json.loads(cfg).get('LEAFREC') is True
    for name, out in b1.items():
        man = dict(stem=f'r7041_accept_{name}_leafrec1', namesake=f'r7041_accept_{name}', LEAFREC=1,
                   point=dict(CRH0=68.57073, CROM=0.291246, WBH2=0.021643, NS=1.015066, LEAFREC=1, ZSTART=3e7,
                              LEAFSCALES=1),
                   switches=f'cr keys: {AR} HIER=1 LSTEP=8 LMAXL=2000 + the setting; '
                            f'lcdm/ctl keys: {LCDM} HIER=1 LSTEP=8 LMAXL=2000 + the setting',
                   settings=SET,
                   held='r7041_directions/launch_grid.sh (GRIDSAVE) and the five k0 slices bank_acceptance.py folds '
                        '(KSLICE=0:250); A_l by acceptance_convergence.acceptance() with its own LO/HI/NL; only the '
                        'CR point and LEAFREC moved',
                   note_r7669='the lcdm/ctl keys are the control rebuilt at LEAFREC=1 through the identical code; '
                              'the recipe at LEAFREC=0 reproduces every namesake key (r7669_70_control_and_builds/r7041.json)')
        o = dict(out)
        o['config'] = np.array(cfg)
        o['manifest'] = np.array(json.dumps(man))
        np.savez_compressed(os.path.join(SP, f'r7041_accept_{name}_leafrec1.npz'), **o)
    res['banked'] = [f'spectra/r7041_accept_{n}_leafrec1.npz' for n in b1]
else:
    res['banked'] = []
res['fail'] = fail
json.dump(res, open(os.path.join(HERE, 'r7041.json'), 'w'), indent=1, default=str)
print(json.dumps({k: v for k, v in res.items() if k != 'wall_s'}, indent=1, default=str))
sys.exit(1 if (fail or not recipe_ok) else 0)
