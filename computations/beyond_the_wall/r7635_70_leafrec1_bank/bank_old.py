"""r7635+70: fold the older §B CR files, regenerated on the arm of record (launch_old.sh), into
spectra/<stem>_leafrec1.npz, each with a `manifest` JSON key (LEAFREC, the point, the switches the run read,
what was held and what was not).  Three names are banked from a run another name shares, because their
namesakes were the same run or now are (said in `held`)."""
import json, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.join(HERE, '..', 'spectra')
D = os.environ.get('D', '/tmp/claude-0/-home-user-shadow-of-existence/4913e7eb-3c04-585c-bc52-ac1b69fc5eb8/scratchpad/bank')
POINT = dict(CRH0=68.570730, CROM=0.291246, WBH2=0.021643, NS=1.015066, LEAFREC=1, ZSTART=3e7, LEAFSCALES=1)
K1 = 'KFAC=2 (the namesake ran at KFAC=1, which the alias gate now refuses)'
A = 'the point: the namesake sat at the built-in defaults (H0 73, Om 0.3066) with z_onset solved to l_A 301.6; here the arm of record'
B = 'the point: the namesake sat at its own CRH0/CROM with ZSTART=3e7 and LEAFSCALES=0; here the arm of record'
RUNS = {  # stem: (run tag, note)
    'c54.175_cr': ('c54.175_cr', f'{A}; {K1}; POLC=8/9 and BSPLIT=0 kept'),
    'c54.177_cr': ('c54.177_cr', f'{A}; {K1}; BSPLIT=0 kept, POLC 16/15 is the default'),
    'c54.178_cr': ('c54.178_cr', f'{A}; {K1}'),
    'c54.186_cr_KCONT': ('c54.186_cr_KCONT', f'{A}; {K1}'),
    'c54.186_cr_L3000': ('c54.186_cr_L3000', f'{A}; {K1}'),
    'c54.191_cr_lA340_L3000': ('c54.191_cr_lA340_L3000', f'the injection l_A=340 held by LATARG=340, so ZSTART is unset and the onset is solved; otherwise the arm of record; {K1}'),
    'c54.191_cr_phipi_L3000': ('c54.191_cr_phipi_L3000', f'{A}; {K1}'),
    'c54.193_cr_nodrive_L3000': ('c54.193_cr_nodrive_L3000', f'{A}; {K1}'),
    'c54.195_cr_phi0.7854_L3000': ('c54.195_cr_phi0.7854_L3000', f'{A}; {K1}'),
    'c54.195_cr_phi1.5708_L3000': ('c54.195_cr_phi1.5708_L3000', f'{A}; {K1}'),
    'item38_cr_phi0.0_prod': ('c54.186_cr_L3000', f'the c54.186_cr_L3000 run: CRPHI=0.0 is the default and the namesakes agreed to 4e-9; {A}; {K1}'),
    'item38_cr_phi3.1416_prod': ('c54.191_cr_phipi_L3000', f'the c54.191_cr_phipi_L3000 run: the namesakes were bit-identical; {A}; {K1}'),
    'r4494_cr_leaf_ISWon': ('r4494_cr_leaf_ISWon', A),
    'r4494_cr_leaf_ISWoff': ('r4494_cr_leaf_ISWoff', A),
    'r4494_cr_stack_ISWon': ('r4494_cr_stack_ISWon', f'{A}; STACKPERT=1 kept (the perturbations on the stacking rate; recombination on the leaf rate)'),
    'r4494_cr_stack_ISWoff': ('r4494_cr_stack_ISWoff', f'{A}; STACKPERT=1 kept'),
    'r6784_cr_crossing_hier': ('r6784_cr_crossing_hier', f'{B} (68.62, 0.2973); CRIC=branchpoint kept'),
    'r6784_cr_crossing_hier_noCRIC': ('r6784_cr_crossing_hier_noCRIC', f'{B} (68.62, 0.2973)'),
    'r6784_cr_crossing_los': ('r6784_cr_crossing_los', f'{B} (68.62, 0.2973); line-of-sight, CRIC=branchpoint kept (README: drop HIER, change nothing else)'),
    'cc66_cr_x_h686_pol': ('cc66_cr_x_h686_pol', f'{B} (68.60, 0.2973)'),
    'cc66_cr_x_h6862_pol': ('cc66_cr_x_h686_pol', f'the cc66_cr_x_h686_pol run: the pair differed ONLY in CRH0 (68.60 vs 68.62), and on the arm of record both are the one point; {B}'),
    'cc66_cr_x_h686_L2000': ('cc66_cr_x_h686_L2000', f'{B} (68.60, 0.2973)'),
    'cc66_refit_verify_cr': ('cc66_refit_verify_cr', f'{B} (the cc66 refit minimum, ~68.6077/0.2967/0.0217/0.9949, digits unrecorded)'),
    'cc66_cr_x_lstep1': ('cc66_cr_x_lstep1', f'⚠ LOW CONFIDENCE: no command was recorded for the namesake (default background, LMAXL=1300, LSTEP=1); rebuilt as HIER=1 LSTEP=1 LMAXL=1300 on the arm of record'),
}
MAN, fail = {}, []


def sw(log):
    t = open(log).read()
    if '__DONE__ rc=0' not in t:
        fail.append(f'G3 {os.path.basename(log)}')
    line = next(l for l in t.splitlines() if l.startswith('__SWITCHES__ '))
    return ' '.join(w for w in line.split()[1:] if not w.startswith(('SAVE=', 'KSLICE=')))


def save(stem, out, s, held):
    old = np.load(os.path.join(SP, stem + '.npz'), allow_pickle=True)
    miss = [k for k in old.files if k not in out and k not in ('LMAXL', 'KFAC', 'LSTEP', 'path', 'built', 'rate', 'isw')]
    if miss:
        fail.append(f'form {stem}: keys missing {miss}')
    if 'config' in out and not json.loads(str(out['config']))['LEAFREC']:
        fail.append(f'G2 {stem}: config LEAFREC false')
    if len(old['ls']) and not np.array_equal(old['ls'], out['ls']):
        print(f'  note {stem}: multipole grid {len(old["ls"])} -> {len(out["ls"])} ({old["ls"][0]}..{old["ls"][-1]} -> {out["ls"][0]}..{out["ls"][-1]})')
    for k in ('LMAXL', 'KFAC', 'LSTEP', 'path', 'built', 'rate', 'isw'):   # r4494's own descriptor keys
        if k in old.files and k not in out:
            out[k] = old[k]
    if 'rate' in old.files:
        out['rate'] = np.array('stacking' if 'stack' in stem else 'leaf')
    man = dict(stem=stem + '_leafrec1', namesake=stem, LEAFREC=1, point=POINT, switches=s, held=held)
    out['manifest'] = np.array(json.dumps(man))
    np.savez(os.path.join(SP, stem + '_leafrec1.npz'), **out)
    MAN[stem + '_leafrec1'] = man
    print(f'  {stem}_leafrec1')


for stem, (tag, held) in RUNS.items():
    f = f'{D}/old/{tag}.npz'
    if not os.path.exists(f):
        fail.append(f'missing run {tag}'); continue
    d = np.load(f, allow_pickle=True)
    save(stem, {k: d[k] for k in d.files}, sw(f'{D}/old/{tag}.log'), held)

fs = [f'{D}/r6794/kc_k{a}.npz' for a in range(0, 2700, 450)]
if all(os.path.exists(f) for f in fs):
    ds = [np.load(f, allow_pickle=True) for f in fs]
    out = {k: ds[0][k] for k in ds[0].files}
    out['Dl'] = sum(d['Dl'] for d in ds)
    save('r6794_cr_crossing_kcont_summed', out, sw(fs[0].replace('.npz', '.log')),
         f'six KSLICE pieces of 450 summed (2700 continuum modes), as r6794; {B} (68.62, 0.2973)')
else:
    fail.append('r6794 slices missing')
json.dump(MAN, open(os.path.join(HERE, 'MANIFEST_old.json'), 'w'), indent=1)
print('\n'.join(['FAILS:'] + fail) if fail else 'all gates hold')
sys.exit(1 if fail else 0)
