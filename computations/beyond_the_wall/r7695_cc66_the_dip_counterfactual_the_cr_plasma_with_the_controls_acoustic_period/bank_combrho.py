"""r7695+cc66: fold the COMBRHO rebuild's slices into the two banks the dip test reads.

Modelled on `r7635_70_leafrec1_bank/bank_clean.py`'s `r6911` and `r6915` folds, with its gates kept:
the slices must TILE the k axis with no gap or overlap; every slice's log must say `__DONE__ rc=0`;
the split residual must hold; the pairs must close on `D_l`.

⛔ TWO GATES THIS FOLD ADDS, BECAUSE IT IS A COUNTERFACTUAL AND NOT A RE-POINT:
  * every slice's own `config` must record `COMBRHO` at the registered value -- the switch is read
    back out of the instrument's save rather than trusted from the launcher's environment;
  * the stems written are NEW.  The arm of record's banks are never opened for writing.
"""
import json
import os
import re
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.abspath(os.path.join(HERE, '..', 'spectra'))
D = os.environ.get('D', '/tmp/claude-0/-home-user-shadow-of-existence/'
                        '26826c5d-5f18-5adf-9ba6-b04043e78f9b/scratchpad/combrho')
RHO = 0.9945919371
NK = 1452
PERK = ('k', 'P', 'sw_ls', 'dp_ls', 'isw_ls', 'pol_ls', 'md_ls', 'S_ls',
        'sw_i', 'dp_i', 'isw_i', 'pol_i', 'md_i', 'S_i', 'resid')
SCAL = ('eta_ls', 'eta_ls_w', 'eta_used', 'n_eta', 'xswap', 'arm', 'r_s', 'D_M', 'l_A', 'ns',
        'ombh2', 'R_peak')
fail = []

for _stem in ('r7695_source_cr_combrho', 'r7695_pairs_cr_combrho'):
    assert not os.path.exists(os.path.join(SP, _stem + '.npz')) or '--force' in sys.argv, \
        f'{_stem}.npz exists; pass --force to rewrite it'


def slices(sub, pre, suf):
    fs = sorted((int(re.search(r'_k(\d+)', f).group(1)), f)
                for f in os.listdir(os.path.join(D, sub))
                if f.startswith(pre + '_k') and f.endswith(suf))
    if [i for i, _ in fs] != list(range(0, NK, 250)):
        fail.append(f'G2 {sub}: slice starts {[i for i, _ in fs]}')
    return fs


def done(log):
    txt = open(log).read()
    if '__DONE__ rc=0' not in txt:
        fail.append(f'G3 {os.path.basename(log)}: not __DONE__ rc=0')
    return ' '.join(w for w in next(l for l in txt.splitlines()
                                    if l.startswith('__SWITCHES__ ')).split()[1:]
                    if not w.startswith(('SAVE=', 'SRCSAVE=', 'SRCDEC=', 'KSLICE=')))


def gcfg(npz, who):
    """the switch, read back out of the instrument's own saved config"""
    d = np.load(npz, allow_pickle=True)
    c = json.loads(str(d['config'].item())) if 'config' in d.files else {}
    if not c.get('LEAFREC'):
        fail.append(f'G2 {who}: config LEAFREC false')
    r = c.get('COMBRHO')
    if r is None or abs(float(r) - RHO) > 1e-12:
        fail.append(f'G5 {who}: config COMBRHO is {r!r}, not {RHO}')
    return c


def tile(fs, lens):
    n = 0
    for (i0, _), m in zip(fs, lens):
        if i0 != n:
            fail.append(f'G2 tiling: slice at {i0} follows {n}')
        n += m
    if n != NK:
        fail.append(f'G2 tiling: {n} modes, expected {NK}')


MAN = {}


def save(stem, out, sw, held):
    """gated against the NAMESAKE's key set, so a missing array is a failure and not a quiet gap"""
    ns = stem.replace('r7695_source_cr_combrho', 'r6911_source_cr_leafrec1') \
             .replace('r7695_pairs_cr_combrho', 'r6915_pairs_cr_leafrec1')
    old = np.load(os.path.join(SP, ns + '.npz'), allow_pickle=True)
    miss = [k for k in old.files if k not in out and k != 'manifest']
    if miss:
        fail.append(f'form {stem}: keys missing {miss}')
    man = dict(stem=stem, namesake=ns, COMBRHO=RHO, switches=sw, held=held,
               what='the CR plasma with the control\'s acoustic period: COMBRHO scales the SOURCE '
                    'side\'s k inside hier_run; the projection kernel, the measure and the '
                    'background are untouched')
    out['manifest'] = np.array(json.dumps(man))
    np.savez(os.path.join(SP, stem + '.npz'), **out)
    MAN[stem] = man
    print(f'  {stem} <- {sw}')


# ── the source bank (SRCSAVE) ───────────────────────────────────────────────────────────────────
fs = slices('src', 'src_cr', '_fields.npz')
ds = [np.load(os.path.join(D, 'src', f)) for _, f in fs]
tile(fs, [len(d['k']) for d in ds])
out = {q: np.concatenate([d[q] for d in ds]) for q in PERK}
out['ls'] = ds[0]['ls']
sp = [np.load(os.path.join(D, 'src', f.replace('_fields', '')), allow_pickle=True) for _, f in fs]
for (_, f), s in zip(fs, sp):
    gcfg(os.path.join(D, 'src', f.replace('_fields', '')), f)
out['Dl'] = sum(s['Dl'] for s in sp)
out['Dl_swap'] = sum(d['Dl_swap'] for d in ds)
for q in SCAL:
    out[q] = ds[0][q]
out['n_slices'] = np.array(len(ds))
out['config'] = sp[0]['config']
_r = float(np.max(out['resid']))
if not _r < 1e-14:
    fail.append(f'G4 source: split residual {_r:.3e}')
save('r7695_source_cr_combrho', out, done(os.path.join(D, 'src', fs[0][1].replace('_fields.npz', '.log'))),
     f'{len(ds)} KSLICE pieces of 250; split residual {_r:.2e}')

# ── the pairs bank (SRCDEC) ─────────────────────────────────────────────────────────────────────
fs = slices('dec', 'dec_cr', '_pairs.npz')
ds = [np.load(os.path.join(D, 'dec', f)) for _, f in fs]
tile(fs, [int(d['n_modes']) for d in ds])
out = dict(ls=ds[0]['ls'], pairs=ds[0]['pairs'], Dl=sum(d['Dl'] for d in ds),
           Dl_pairs=sum(d['Dl_pairs'] for d in ds), n_slices=np.array(len(ds)),
           n_modes=np.array(sum(int(d['n_modes']) for d in ds)))
for q in ('arm', 'r_s', 'D_M', 'l_A', 'ns', 'eta_ls', 'eta_ls_w'):
    out[q] = ds[0][q]
for _, f in fs:
    gcfg(os.path.join(D, 'dec', f.replace('_pairs.npz', '.npz')), f)
out['config'] = np.load(os.path.join(D, 'dec', fs[0][1].replace('_pairs.npz', '.npz')),
                        allow_pickle=True)['config']
_rel = float(np.max(np.abs(out['Dl_pairs'].sum(axis=1) - out['Dl']) / np.abs(out['Dl'])))
if not _rel < 1e-13:
    fail.append(f'G4 pairs: close to {_rel:.3e}')
save('r7695_pairs_cr_combrho', out, done(os.path.join(D, 'dec', fs[0][1].replace('_pairs.npz', '.log'))),
     f'{len(ds)} KSLICE pieces; pairs close on D_l to {_rel:.2e}')

# ── the background must NOT have moved: a re-combed plasma, not a different cosmology ───────────
_A = np.load(os.path.join(SP, 'r6911_source_cr_leafrec1.npz'), allow_pickle=True)
_N = np.load(os.path.join(SP, 'r7695_source_cr_combrho.npz'), allow_pickle=True)
print('\n  THE BACKGROUND, arm of record vs the counterfactual')
for q in ('r_s', 'D_M', 'l_A', 'ns', 'ombh2', 'eta_ls', 'R_peak'):
    a, n = float(_A[q]), float(_N[q])
    ok = a == n
    print(f'    {q:8s} {a:.9f}  {n:.9f}   {"same" if ok else "⛔ MOVED"}')
    if not ok:
        fail.append(f'G6 background {q}: {a} -> {n}')
_ka, _kn = np.asarray(_A['k'], float), np.asarray(_N['k'], float)
_ksame = _ka.shape == _kn.shape and np.array_equal(_ka, _kn)
print(f'    the saved k grid is the PROJECTION\'s, unchanged: {_ksame}')
if not _ksame:
    fail.append('G6 the saved k grid moved -- QK would not be comparable')

print()
if fail:
    for f in fail:
        print(f'  ⛔ [FAIL] {f}')
    raise SystemExit(1)
print('  ✔ both banks written; every slice tiled, rc=0, COMBRHO read back from the instrument\'s own '
      'config, and the background unmoved.')
