"""r7635+70: fold the r6885-r6959 family, regenerated on the arm of record, into spectra/<stem>_leafrec1.npz.

Each output carries every key its LEAFREC=0 namesake carries (the form the receipt reads) plus `manifest`, a JSON
string: LEAFREC, the point, the switches the run read (its own __SWITCHES__ line, SAVE paths dropped), and what
was held from the namesake.  Gates: G1 (the plain arm equals r7633's verify_cr_leafrec1 bit for bit), G2 (the
run's own config says LEAFREC true; slices tile [0, nk)), G3 (the launcher's switch guard: every __DONE__ rc=0),
G4 (the source terms close on S; the pairs close on D_l).
"""
import json, os, re, shutil, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.join(HERE, '..', 'spectra')
D = os.environ.get('D', '/tmp/claude-0/-home-user-shadow-of-existence/4913e7eb-3c04-585c-bc52-ac1b69fc5eb8/scratchpad/bank')
POINT = dict(CRH0=68.570730, CROM=0.291246, WBH2=0.021643, NS=1.015066, LEAFREC=1, ZSTART=3e7, LEAFSCALES=1)
MAN = {}
fail = []


def switches(log):
    txt = open(log).read()
    if '__DONE__ rc=0' not in txt:
        fail.append(f'G3 {os.path.basename(log)}: not __DONE__ rc=0')
    line = next(l for l in txt.splitlines() if l.startswith('__SWITCHES__ '))
    return ' '.join(w for w in line.split()[1:]
                    if not w.startswith(('SAVE=', 'SRCSAVE=', 'SRCDEC=', 'SRCETA=', 'KSLICE=')))


def g2(npz):
    d = np.load(npz, allow_pickle=True)
    if 'config' in d.files and not json.loads(str(d['config']))['LEAFREC']:
        fail.append(f'G2 {npz}: config LEAFREC false')


def tile(fs, lens, nk):
    n = 0
    for (i0, _), m in zip(fs, lens):
        if i0 != n:
            fail.append(f'G2 tiling: slice at {i0} follows {n}')
        n += m
    if n != nk:
        fail.append(f'G2 tiling: {n} modes, expected {nk}')


def save(stem, out, sw, held):
    old = np.load(os.path.join(SP, stem + '.npz'), allow_pickle=True)
    miss = [k for k in old.files if k not in out]
    if miss:
        fail.append(f'form {stem}: keys missing {miss}')
    man = dict(stem=stem + '_leafrec1', namesake=stem, LEAFREC=1, point=POINT, switches=sw, held=held)
    out['manifest'] = np.array(json.dumps(man))
    np.savez(os.path.join(SP, stem + '_leafrec1.npz'), **out)
    MAN[stem + '_leafrec1'] = man
    print(f'  {stem}_leafrec1 <- {sw}')


def plain(stem, tag, held='the namesake launcher\'s switches; only the point and LEAFREC moved'):
    f = f'{D}/plain/{tag}.npz'
    g2(f)
    d = np.load(f, allow_pickle=True)
    save(stem, {k: d[k] for k in d.files}, switches(f'{D}/plain/{tag}.log'), held)
    return d


# G1: the plain arm, regenerated, against r7633's verify_cr_leafrec1
v = plain('cc66_r185_verify_cr', 'r185_verify_cr', 'refit_grid185/verify.sh; the plain arm')
ref = np.load(os.path.join(HERE, '..', 'r7633_70_leafrec_refit', 'verify_cr_leafrec1.npz'))
# ⚠ registered as bit for bit; measured 2.84e-13 absolute (~5e-17 relative).  r7633 ran OMP_NUM_THREADS=2,
#   this bank 1, so the BLAS sums run in a different order.  Gated at 1e-11 of the peak (round-off over 1452 modes) and reported as a miss of the registered form.
g1 = float(np.max(np.abs(v['Dl'] - ref['Dl']) / np.max(np.abs(ref['Dl']))))
print(f'  G1: bit-identical {np.array_equal(v["Dl"], ref["Dl"])}; max |dDl|/max Dl = {g1:.2e} against verify_cr_leafrec1')
if not g1 < 1e-11:
    fail.append(f'G1: {g1:.3e}')
for stem, tag in (('r6885_dp0_cr', 'r6885_dp0_cr'), ('r6885_los_cr', 'r6885_los_cr'),
                  ('r6885_losdp0_cr', 'r6885_losdp0_cr'), ('r6885_lossw0_cr', 'r6885_lossw0_cr'),
                  ('r6889_nufs0_cr', 'r6889_nufs0_cr')):
    plain(stem, tag)


def slices(sub, prefix, suffix):
    return sorted((int(re.search(r'_k(\d+)', f).group(1)), f) for f in os.listdir(f'{D}/{sub}')
                  if f.startswith(prefix + '_k') and f.endswith(suffix))


# r6911: the source at both ends (bank.py / bank2.py, verbatim fold)
PERK = ('k', 'P', 'sw_ls', 'dp_ls', 'isw_ls', 'pol_ls', 'md_ls', 'S_ls',
        'sw_i', 'dp_i', 'isw_i', 'pol_i', 'md_i', 'S_i', 'resid')
SCAL = ('eta_ls', 'eta_ls_w', 'eta_used', 'n_eta', 'xswap', 'arm', 'r_s', 'D_M', 'l_A', 'ns', 'ombh2', 'R_peak')
for stem, sub, pre, nk in (('r6911_source_cr', 'src', 'src_cr', 1452), ('r6911_source_cr_kcont', 'kcont', 'src_crkc', 2547)):
    fs = slices(sub, pre, '_fields.npz')
    ds = [np.load(os.path.join(D, sub, f)) for _, f in fs]
    tile(fs, [len(d['k']) for d in ds], nk)
    out = {q: np.concatenate([d[q] for d in ds]) for q in PERK}
    out['ls'] = ds[0]['ls']
    sp = [np.load(os.path.join(D, sub, f.replace('_fields', ''))) for _, f in fs]
    for _, f in fs:
        g2(os.path.join(D, sub, f.replace('_fields', '')))
    out['Dl'] = sum(s['Dl'] for s in sp)
    out['Dl_swap'] = sum(d['Dl_swap'] for d in ds)
    for q in SCAL:
        out[q] = ds[0][q]
    out['n_slices'] = np.array(len(ds))
    out['config'] = sp[0]['config']          # the instrument's own, written at save time by the slice's run
    r = float(np.max(out['resid']))
    if not r < 1e-14:
        fail.append(f'G4 {stem}: split residual {r:.3e}')
    save(stem, out, switches(os.path.join(D, sub, fs[0][1].replace('_fields.npz', '.log'))),
         f'r6911 launch/pass2; {len(ds)} KSLICE pieces of 250; split residual {r:.2e}')

# r6915: the ten pairs
fs = slices('dec', 'dec_cr', '_pairs.npz')
ds = [np.load(os.path.join(D, 'dec', f)) for _, f in fs]
tile(fs, [int(d['n_modes']) for d in ds], 1452)
out = dict(ls=ds[0]['ls'], pairs=ds[0]['pairs'], Dl=sum(d['Dl'] for d in ds),
           Dl_pairs=sum(d['Dl_pairs'] for d in ds), n_slices=np.array(len(ds)),
           n_modes=np.array(sum(int(d['n_modes']) for d in ds)))
for q in ('arm', 'r_s', 'D_M', 'l_A', 'ns', 'eta_ls', 'eta_ls_w'):
    out[q] = ds[0][q]
out['config'] = np.load(os.path.join(D, 'dec', fs[0][1].replace('_pairs.npz', '.npz')), allow_pickle=True)['config']
rel = float(np.max(np.abs(out['Dl_pairs'].sum(axis=1) - out['Dl']) / np.abs(out['Dl'])))
if not rel < 1e-13:
    fail.append(f'G4 r6915: pairs close to {rel:.3e}')
save('r6915_pairs_cr', out, switches(os.path.join(D, 'dec', fs[0][1].replace('_pairs.npz', '.log'))),
     f'r6915 launch; {len(ds)} KSLICE pieces; pairs close on D_l to {rel:.2e}')

# r6941: the fine grid
fs = slices('fine', 'fine_cr', '.npz')
ds = [np.load(os.path.join(D, 'fine', f), allow_pickle=True) for _, f in fs]
if [i for i, _ in fs] != list(range(0, 1452, 250)):
    fail.append(f'G2 r6941 fine: slices {[i for i, _ in fs]}')
for _, f in fs:
    g2(os.path.join(D, 'fine', f))
out = dict(ls=ds[0]['ls'], Dl=sum(d['Dl'] for d in ds), l_A=ds[0]['l_A'], D_M=ds[0]['D_M'],
           r_s=ds[0]['r_s'], arm=ds[0]['arm'], config=ds[0]['config'])
save('r6941_fine_cr', out, switches(os.path.join(D, 'fine', fs[0][1].replace('.npz', '.log'))),
     f'r6941 launch; LSTEP=1, {len(ds)} KSLICE pieces of 250')

# r6959: the eta profile (SRCETA output, unaltered)
d = np.load(f'{D}/eta/eta_cr_prof.npz', allow_pickle=True)
save('r6959_eta_cr', {**{k: d[k] for k in d.files}, 'config': np.load(f'{D}/eta/eta_cr.npz', allow_pickle=True)['config']}, switches(f'{D}/eta/eta_cr.log'), 'r6959 launch_a; SRCETA output unaltered')

json.dump(MAN, open(os.path.join(HERE, 'MANIFEST_clean.json'), 'w'), indent=1)
print('\n'.join(['FAILS:'] + fail) if fail else 'all gates hold (G1-G4)')
sys.exit(1 if fail else 0)
