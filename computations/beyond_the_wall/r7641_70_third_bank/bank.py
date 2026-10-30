"""r7641+70: fold the third leaf-rate bank (launch.sh) into spectra/<name>_leafrec1.npz, each in its namesake's
own format (r6893 bank.py/bank2.py, r6925 bank.py, the plain r6885/r6889 form), with the instrument's `config` and
a `manifest` key.  Gates: every run __DONE__ rc=0 except where the namesake also failed (the screen's `failed`
list); slices tile; every output carries `config` with LEAFREC true; the forms match.  And the predictions read:
the control's knob runs against their namesakes, the noop against the plain arm, the screen's failed list."""
import glob
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.join(HERE, '..', 'spectra')
D = os.environ.get('D', '/tmp/claude-0/-home-user-shadow-of-existence/4913e7eb-3c04-585c-bc52-ac1b69fc5eb8/scratchpad/bank3')
POINT = dict(CRH0=68.570730, CROM=0.291246, WBH2=0.021643, NS=1.015066, LEAFREC=1, ZSTART=3e7, LEAFSCALES=1)
MAN, fail, report = {}, [], []


def rc(log):
    for line in open(log):
        if line.startswith('__DONE__'):
            return int(line.split('rc=')[1])
    return None


def sw(log):
    return ' '.join(w for w in next((l for l in open(log) if l.startswith('__SWITCHES__ ')), '__SWITCHES__ ?').split()[1:]
                    if not w.startswith(('SAVE=', 'KSLICE=')))


def save(name, out, switches, held, arm='cr'):
    old = np.load(os.path.join(SP, name + '.npz'), allow_pickle=True)
    miss = [k for k in old.files if k not in out]
    if miss:
        fail.append(f'form {name}: keys missing {miss[:6]}')
    if 'config' in out and not json.loads(str(out['config'])).get('LEAFREC'):
        fail.append(f'{name}: config LEAFREC not true')
    man = dict(file=f'spectra/{name}_leafrec1.npz', namesake=f'spectra/{name}.npz', LEAFREC=1,
               point=POINT if arm == 'cr' else 'the control, unchanged', switches=switches, held=held)
    out['manifest'] = np.array(json.dumps(man))
    np.savez(os.path.join(SP, name + '_leafrec1.npz'), **out)
    MAN[name + '_leafrec1'] = man


def plain(sub, tag):
    p = f'{D}/{sub}/{tag}'
    if rc(p + '.log') != 0:
        fail.append(f'{sub}/{tag}: rc {rc(p + ".log")}')
    d = np.load(p + '.npz', allow_pickle=True)
    return {k: d[k] for k in d.files}, sw(p + '.log')


# ---- the r6885 knob pairs, both arms, and r6889's three
for k in ('ln24', 'noisw', 'dre0', 'drc0'):
    for arm in ('cr', 'lcdm'):
        out, s = plain('knob', f'{k}_{arm}')
        if arm == 'lcdm':
            old = np.load(os.path.join(SP, f'r6885_{k}_lcdm.npz'))
            dd = float(np.max(np.abs(out['Dl'] - old['Dl'])) / np.max(old['Dl']))
            report.append(f'r6885_{k}_lcdm: the control rebuilt against its namesake, max|dDl|/max = {dd:.2e}')
        save(f'r6885_{k}_{arm}', out, s, 'r6885_directions/launch.sh (HIER=1 LSTEP=8 LMAXL=2000)'
             + ('' if arm == 'cr' else '; the CONTROL, rebuilt because the knob is switched on both arms'), arm)
for t, name in (('noop_cr', 'r6889_noop_cr'), ('hdp0_cr', 'r6889_hdp0_cr'), ('hsw0_cr', 'r6889_hsw0_cr')):
    out, s = plain('r6889', t)
    save(name, out, s, 'r6889_directions/launch.sh (HIER=1 LSTEP=8 LMAXL=2000)')
    if t == 'noop_cr':
        ref = np.load(os.path.join(SP, 'cc66_r185_verify_cr_leafrec1.npz'))
        report.append(f'r6889_noop_cr_leafrec1 against cc66_r185_verify_cr_leafrec1: bit-identical '
                      f'{np.array_equal(out["Dl"], ref["Dl"])}, max|d| {np.max(np.abs(out["Dl"] - ref["Dl"])):.2e}')

# ---- r6893 fine grid (bank2.py's fold)
F, miss, cfg, s0 = {}, [], None, ''
for v in ('base', 'nufs0'):
    out, s0 = plain('fine', f'fineA_{v}_cr')
    cfg = out['config']
    F[f'ls__fineA_{v}'] = out['ls'].astype(np.int32)
    F[f'Dl__fineA_{v}'] = out['Dl'].astype(np.float64)
    F[f'lA__fineA_{v}'], F[f'DM__fineA_{v}'], F[f'rs__fineA_{v}'] = (np.float64(out['l_A']), np.float64(out['D_M']),
                                                                       np.float64(out['r_s']))
    sl = sorted(glob.glob(f'{D}/fine/fineB_{v}_cr_k*.npz'), key=lambda q: int(q.split('_k')[-1][:-4]))
    if [int(q.split('_k')[-1][:-4]) for q in sl] != list(range(0, 1452, 250)):
        fail.append(f'fineB_{v}: slices {len(sl)}')
    for q in sl:
        if rc(q[:-4] + '.log') != 0:
            fail.append(f'{os.path.basename(q)}: rc')
    ds = [np.load(q) for q in sl]
    F[f'ls__fineB_{v}'] = ds[0]['ls'].astype(np.int32)
    F[f'Dl__fineB_{v}'] = sum(d['Dl'].astype(np.float64) for d in ds)
    F[f'lA__fineB_{v}'], F[f'DM__fineB_{v}'], F[f'rs__fineB_{v}'] = (np.float64(ds[0]['l_A']), np.float64(ds[0]['D_M']),
                                                                       np.float64(ds[0]['r_s']))
    F[f'nsl__fineB_{v}'] = np.int32(len(ds))
sp = [np.load(f'{D}/slice/{t}.npz') for t in ('sl_cr_0_130', 'sl_cr_130_999')]
F['ls__slicesum'] = sp[0]['ls'].astype(np.int32)
F['Dl__slicesum'] = sum(d['Dl'].astype(np.float64) for d in sp)
F['lA__slicesum'], F['DM__slicesum'], F['rs__slicesum'] = (np.float64(sp[0]['l_A']), np.float64(sp[0]['D_M']),
                                                            np.float64(sp[0]['r_s']))
F['missing'] = np.array(miss, dtype=object)
F['config'] = cfg
save('r6893_fine_grid_cr', F, s0, 'r6893_directions/fine2.sh: A LSTEP=2 LMAXL=900 whole, B LSTEP=4 LMAXL=2000 in six '
     'slices of 250, base and NUFS=0; the slice-sum pair at the screen grid')

# ---- r6925 visleaf (bank.py's fold)
out = {}
for tag in ('injvl', 'combvl'):
    sl = sorted(glob.glob(f'{D}/vl/{tag}_cr_k*.npz'), key=lambda q: int(q.split('_k')[-1][:-4]))
    if [int(q.split('_k')[-1][:-4]) for q in sl] != list(range(0, 1452, 250)):
        fail.append(f'{tag}: slices {len(sl)}')
    ds = [np.load(q, allow_pickle=True) for q in sl]
    out[f'ls__{tag}'], out[f'Dl__{tag}'] = ds[0]['ls'], sum(d['Dl'] for d in ds)
    for q in ('l_A', 'D_M', 'r_s', 'arm'):
        out[f'{q}__{tag}'] = ds[0][q]
    out['config'] = ds[0]['config']
    s0 = sw(sl[0][:-4] + '.log')
save('r6925_visleaf_cr', out, s0, 'r6925_directions/launch.sh: VISLEAF=1, the injection and the comb, six slices each')

# ---- r6893 switch screen (bank.py's fold, the cr half)
S, failed = {}, []
for p in sorted(glob.glob(f'{D}/screen/*_cr.log')):
    t = os.path.basename(p)[:-4]
    if t.startswith('junk'):
        continue
    k = t[:-3]
    r = rc(p)
    if r != 0 or not os.path.exists(p[:-4] + '.npz'):
        failed.append(f'{t}:rc={r}')
        continue
    d = np.load(p[:-4] + '.npz', allow_pickle=True)
    S[f'ls__{k}'] = d['ls'].astype(np.int32)
    S[f'Dl__{k}'] = d['Dl'].astype(np.float64)
    S[f'lA__{k}'], S[f'DM__{k}'], S[f'rs__{k}'] = np.float64(d['l_A']), np.float64(d['D_M']), np.float64(d['r_s'])
    S[f'rc__{k}'] = np.int32(r)
    if k == 'base':
        S['config'] = d['config']
S['failed'] = np.array(failed, dtype=object)
old = np.load(os.path.join(SP, 'r6893_switch_screen_cr.npz'), allow_pickle=True)
of = sorted(x.split(':')[0][:-3] for x in old['failed'])
nf = sorted(x.split(':')[0][:-3] for x in failed)
report.append(f'screen failed-switch list: namesake {of}; arm of record {nf}; same {of == nf}')
n_old = len([k for k in old.files if k.startswith('ls__')])
n_new = len([k for k in S if k.startswith('ls__')])
report.append(f'screen spectra: namesake {n_old}, arm of record {n_new}')
miss = [k for k in old.files if k not in S and k != 'failed']
if miss:
    report.append(f'screen keys the namesake has and this does not: {miss[:8]}')
save('r6893_switch_screen_cr', S, sw(f'{D}/screen/base_cr.log'),
     'r6893_directions/screen.sh, the cr half: HIER=1 LSTEP=16 LMAXL=500, its own absolute switch values; its '
     'LEAFSCALES variant at 0 as recorded')

json.dump(MAN, open(os.path.join(HERE, 'MANIFEST.json'), 'w'), indent=1)
print('\n'.join(report))
print(f'{len(MAN)} files banked')
print('\n'.join(['FAILS:'] + fail) if fail else 'all gates hold')
sys.exit(1 if fail else 0)
