"""r7639+70: fold the second leaf-rate bank (launch.sh) into its namesakes' places, each `<name>_leafrec1.npz`
beside its namesake, in the namesake's own format, with the instrument's `config` and a `manifest` key.

  * the response grids (CR side), centred on the arm of record:
      refit_grid/        <- g1300   (LMAXL=1300; its best_cr and verify_cr are its base on the arm of record)
      refit_grid185/     <- g2000   (LMAXL=2000; its verify_cr likewise)
      r7095_directions/grid_licensed/ <- g2000 (the same recipe, now that LEAFREC=1 is the default)
      r7093_directions/grid_oneclock/ <- gone  (LEAFGEOM=1)
      r7201_cc66_loading_lever/ <- lever
  * spectra/r6919_injected_cr_leafrec1, spectra/r6919_injected_lcdm_leafrec1 (the control: only `viswap`, which
    carries the arm's visibility width, moves; every other key is the namesake's own), spectra/r6929_scan_cr_leafrec1,
    spectra/r6941_fine_cr_visleaf_leafrec1;
  * the crossing set at LEAFSCALES=0 (its recorded configuration), REPLACING r7635's LEAFSCALES=1 `_leafrec1` files.
Gates: every run __DONE__ rc=0 (the switch guard); slices tile; every output carries `config` with LEAFREC true.
"""
import json
import os
import re
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.join(HERE, '..')
SP = os.path.join(BW, 'spectra')
D = os.environ.get('D', '/tmp/claude-0/-home-user-shadow-of-existence/4913e7eb-3c04-585c-bc52-ac1b69fc5eb8/scratchpad/bank2')
POINT = dict(CRH0=68.570730, CROM=0.291246, WBH2=0.021643, NS=1.015066, LEAFREC=1, ZSTART=3e7)
MAN, fail = {}, []


def log_ok(path):
    t = open(path).read()
    if '__DONE__ rc=0' not in t:
        fail.append(f'G {os.path.relpath(path, D)}: not __DONE__ rc=0')
    line = next((l for l in t.splitlines() if l.startswith('__SWITCHES__ ')), '__SWITCHES__ ?')
    return ' '.join(w for w in line.split()[1:] if not w.startswith(('SAVE=', 'KSLICE=')))


def extras(log):
    """The `switches` and `oneclock` keys some namesakes carry: the run's own __SWITCHES__ / __ONECLOCK__ lines."""
    t = open(log).read().splitlines()
    out = {'switches': np.array(next(l for l in t if l.startswith('__SWITCHES__ ')))}
    one = [l.strip() for l in t if '__ONECLOCK__' in l]
    if one:
        out['oneclock'] = np.array(one[0])
    return out


def cfg_ok(cfg, name):
    if not json.loads(str(cfg)).get('LEAFREC'):
        fail.append(f'config {name}: LEAFREC not true')
    return cfg


def save(path, out, sw, held, namesake):
    if os.path.exists(namesake):
        old = np.load(namesake, allow_pickle=True)
        miss = [k for k in old.files if k not in out]
        if miss:
            fail.append(f'form {os.path.basename(path)}: keys missing {miss}')
    man = dict(file=os.path.relpath(path, BW), namesake=os.path.relpath(namesake, BW), LEAFREC=1,
               point=POINT, switches=sw, held=held)
    out['manifest'] = np.array(json.dumps(man))
    np.savez(path, **out)
    MAN[os.path.relpath(path, BW)] = man


def fold(sub, tag, nk, step):
    fs = sorted((int(re.search(r'_k(\d+)$', x[:-4]).group(1)), x) for x in os.listdir(f'{D}/{sub}')
                if x.startswith(f'{tag}_k') and x.endswith('.npz'))
    if [i for i, _ in fs] != list(range(0, nk, step)):
        fail.append(f'tiling {tag}: {[i for i, _ in fs]}')
    ds = [np.load(os.path.join(D, sub, x), allow_pickle=True) for _, x in fs]
    for d in ds:
        if not np.array_equal(d['ls'], ds[0]['ls']):
            fail.append(f'{tag}: slices differ on the multipoles')
    sw = log_ok(os.path.join(D, sub, fs[0][1][:-4] + '.log'))
    for _, x in fs[1:]:
        log_ok(os.path.join(D, sub, x[:-4] + '.log'))
    return ds, sw


# ---- the grids
GRIDS = (('refit_grid', 'g1300', 'refit_grid/launch.sh, LMAXL=1300'),
         ('refit_grid185', 'g2000', 'refit_grid185/launch.sh, LMAXL=2000'),
         ('r7095_directions/grid_licensed', 'g2000', 'r7095 launch_licensed.sh -- the refit_grid185 run: the same '
                                                      'recipe now that LEAFREC=1 is the default'),
         ('r7093_directions/grid_oneclock', 'gone', 'r7093 launch_grid.sh, LEAFGEOM=1'))
TAGS = ['cr_base', 'cr_H0p', 'cr_H0m', 'cr_OMp', 'cr_OMm', 'cr_WBp', 'cr_WBm', 'cr_NSp', 'cr_NSm']
for dest, sub, held in GRIDS:
    for t in TAGS:
        src = os.path.join(D, sub, t + '.npz')
        if not os.path.exists(src):
            fail.append(f'missing {sub}/{t}'); continue
        d = np.load(src, allow_pickle=True)
        out = {**{k: d[k] for k in d.files}, **extras(src[:-4] + '.log')}
        cfg_ok(out['config'], t)
        save(os.path.join(BW, dest, t + '_leafrec1.npz'), out, log_ok(src[:-4] + '.log'),
             f'{held}; centred on the arm of record with the launcher\'s steps (H0 +-2, Om +-0.015, '
             f'omega_b +-0.0008, n_s +-0.02)', os.path.join(BW, dest, t + '.npz'))
    if dest in ('refit_grid', 'refit_grid185'):
        for alias in ('best_cr', 'verify_cr'):
            nm = os.path.join(BW, dest, alias + '.npz')
            if os.path.exists(nm):
                d = np.load(os.path.join(D, sub, 'cr_base.npz'), allow_pickle=True)
                save(os.path.join(BW, dest, alias + '_leafrec1.npz'), {k: d[k] for k in d.files},
                     log_ok(os.path.join(D, sub, 'cr_base.log')),
                     f'{held}; the grid base: on the arm of record the refit point IS the centre', nm)
LEV = os.path.join(BW, 'r7201_cc66_loading_lever')
for t in ('cr_rb0.1', 'cr_rb0.5', 'cr_rb1.5', 'cr_nodrive'):
    src = os.path.join(D, 'lever', t + '.npz')
    if not os.path.exists(src):
        fail.append(f'missing lever/{t}'); continue
    d = np.load(src, allow_pickle=True)
    out = {**{k: d[k] for k in d.files}, **extras(src[:-4] + '.log')}
    cfg_ok(out['config'], t)
    save(os.path.join(LEV, t + '_leafrec1.npz'), out, log_ok(src[:-4] + '.log'),
         'r7201 launch_ten/launch_three (LEAFGEOM=1), at the arm of record', os.path.join(LEV, t + '.npz'))

# ---- r6919: the arm's five injections, and the control's viswap
out, sw = {}, ''
for tag in ('sweepown', 'sweepph', 'fixed', 'sweepstk', 'viswap'):
    ds, sw = fold('inj', f'inj_{tag}_cr', 1452, 250)
    out[f'ls__{tag}'], out[f'Dl__{tag}'], out[f'n__{tag}'] = ds[0]['ls'], sum(d['Dl'] for d in ds), np.array(len(ds))
    for q in ('l_A', 'D_M', 'r_s', 'arm'):
        out[f'{q}__{tag}'] = ds[0][q]
    out['config'] = cfg_ok(ds[0]['config'], tag)
save(os.path.join(SP, 'r6919_injected_cr_leafrec1.npz'), out, sw,
     'r6919_directions/launch.sh, five injections x six KSLICE pieces of 250', os.path.join(SP, 'r6919_injected_cr.npz'))
old = np.load(os.path.join(SP, 'r6919_injected_lcdm.npz'), allow_pickle=True)
out = {k: old[k] for k in old.files}
ds, sw = fold('injl', 'inj_viswap_lcdm', 2547, 250)
out['Dl__viswap'], out['n__viswap'] = sum(d['Dl'] for d in ds), np.array(len(ds))
if not np.array_equal(out['ls__viswap'], ds[0]['ls']):
    fail.append('r6919 lcdm viswap: multipoles differ from the namesake')
out['config'] = ds[0]['config']
save(os.path.join(SP, 'r6919_injected_lcdm_leafrec1.npz'), out, sw,
     "the CONTROL: only `viswap` moves -- it carries the ARM's visibility width, 43.591 -> 43.957 (the arm of record's); "
     "every other key is the namesake's own", os.path.join(SP, 'r6919_injected_lcdm.npz'))

# ---- r6929: the VISLEAF scan
out = {}
for f in ('0', '0.1', '0.25', '0.5', '0.75', '1'):
    t = f.replace('.', '')
    for tag in (f'comb_cr_f{t}', f'inj_cr_f{t}'):
        ds, sw = fold('scan', tag, 1452, 250)
        out[f'ls__{tag}'], out[f'Dl__{tag}'] = ds[0]['ls'], sum(d['Dl'] for d in ds)
        for q in ('l_A', 'D_M', 'r_s'):
            out[f'{q}__{tag}'] = ds[0][q]
        out['config'] = ds[0]['config']
out['f'] = np.array([0, 0.1, 0.25, 0.5, 0.75, 1.0])
save(os.path.join(SP, 'r6929_scan_cr_leafrec1.npz'), out, sw.replace('VISLEAF=1', 'VISLEAF=<f>'),
     'r6929_directions/launch.sh: six VISLEAF values, real and injected, x six KSLICE pieces',
     os.path.join(SP, 'r6929_scan_cr.npz'))

# ---- r6941: the visleaf endpoint and the injections, LSTEP=1
out = {}
for key, tag in (('comb_f1', 'fine_cr_f1'), ('inj_f0', 'finj_cr'), ('inj_f1', 'finj_cr_f1')):
    ds, sw = fold('visleaf', tag, 1452, 250)
    out[f'ls__{key}'], out[f'Dl__{key}'] = ds[0]['ls'], sum(d['Dl'] for d in ds)
    for q in ('l_A', 'D_M', 'r_s'):
        out[f'{q}__{key}'] = ds[0][q]
    out['config'] = ds[0]['config']
save(os.path.join(SP, 'r6941_fine_cr_visleaf_leafrec1.npz'), out, sw,
     'r6941_directions/launch.sh: VISLEAF=1 real, and the injection at f=0 and f=1, LSTEP=1, six KSLICE pieces',
     os.path.join(SP, 'r6941_fine_cr_visleaf.npz'))

# ---- the crossing set at LEAFSCALES=0, replacing r7635's LEAFSCALES=1 files
X = ('the CROSSING configuration (README:47-50) with LEAFSCALES unset (=0), its recorded command, so the 172 '
     'radiation-free ruler is the crossing background\'s; the POINT is the arm of record (the namesake sat at '
     'CRH0 68.62, CROM 0.2973). Replaces r7635\'s LEAFSCALES=1 file (69, r7639 item 3)')
for t in ('r6784_cr_crossing_hier', 'r6784_cr_crossing_hier_noCRIC', 'r6784_cr_crossing_los'):
    src = os.path.join(D, 'cross', t + '.npz')
    d = np.load(src, allow_pickle=True)
    out = {k: d[k] for k in d.files}
    cfg_ok(out['config'], t)
    if json.loads(str(out['config'])).get('LEAFSCALES'):
        fail.append(f'{t}: LEAFSCALES is not 0')
    save(os.path.join(SP, t + '_leafrec1.npz'), out, log_ok(src[:-4] + '.log'), X, os.path.join(SP, t + '.npz'))
ds, sw = fold('cross', 'kc', 2700, 450)
out = {k: ds[0][k] for k in ds[0].files}
out['Dl'] = sum(d['Dl'] for d in ds)
save(os.path.join(SP, 'r6794_cr_crossing_kcont_summed_leafrec1.npz'), out, sw,
     X + '; six KSLICE pieces of 450 summed, as r6794', os.path.join(SP, 'r6794_cr_crossing_kcont_summed.npz'))

json.dump(MAN, open(os.path.join(HERE, 'MANIFEST.json'), 'w'), indent=1)
print(f'{len(MAN)} files banked')
print('\n'.join(['FAILS:'] + fail) if fail else 'all gates hold')
sys.exit(1 if fail else 0)
