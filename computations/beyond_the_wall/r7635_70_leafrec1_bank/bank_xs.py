"""r7635+70: the control's r6911 source with SRCXS re-pointed at the arm of record's distance (launch_xs.sh), folded
as r6911_directions/bank.py folds it, into spectra/r6911_source_lcdm_leafrec1.npz.  The control itself is unchanged
(its Dl must equal the banked r6911_source_lcdm's); only Dl_swap -- the control's source through the ARM's distance
-- and xswap move."""
import json, os, re, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.join(HERE, '..', 'spectra')
D = os.environ.get('D', '/tmp/claude-0/-home-user-shadow-of-existence/4913e7eb-3c04-585c-bc52-ac1b69fc5eb8/scratchpad/bank') + '/srcl'
PERK = ('k', 'P', 'sw_ls', 'dp_ls', 'isw_ls', 'pol_ls', 'md_ls', 'S_ls',
        'sw_i', 'dp_i', 'isw_i', 'pol_i', 'md_i', 'S_i', 'resid')
SCAL = ('eta_ls', 'eta_ls_w', 'eta_used', 'n_eta', 'xswap', 'arm', 'r_s', 'D_M', 'l_A', 'ns', 'ombh2', 'R_peak')
fs = sorted((int(re.search(r'_k(\d+)_', f).group(1)), f) for f in os.listdir(D) if f.endswith('_fields.npz'))
ds = [np.load(os.path.join(D, f)) for _, f in fs]
n = 0
for (i0, _), d in zip(fs, ds):
    assert i0 == n, f'slice at {i0} follows {n}'
    n += len(d['k'])
assert n == 2547, n
for _, f in fs:
    assert '__DONE__ rc=0' in open(os.path.join(D, f.replace('_fields.npz', '.log'))).read(), f
out = {q: np.concatenate([d[q] for d in ds]) for q in PERK}
out['ls'] = ds[0]['ls']
out['Dl'] = sum(np.load(os.path.join(D, f.replace('_fields', '')))['Dl'] for _, f in fs)
out['Dl_swap'] = sum(d['Dl_swap'] for d in ds)
for q in SCAL:
    out[q] = ds[0][q]
out['n_slices'] = np.array(len(ds))
out['config'] = np.load(os.path.join(D, fs[0][1].replace('_fields', '')), allow_pickle=True)['config']
old = np.load(os.path.join(SP, 'r6911_source_lcdm.npz'))
dd = float(np.max(np.abs(out['Dl'] - old['Dl'])) / np.max(old['Dl']))
assert dd < 1e-11, f'the control moved: {dd:.3e}'
assert not [k for k in old.files if k not in out]
out['manifest'] = np.array(json.dumps(dict(stem='r6911_source_lcdm_leafrec1', namesake='r6911_source_lcdm',
    LEAFREC='control unchanged', point='the control (LH0 67.410309, LOM 0.309826, WBH2 0.021966, NS 0.954248)',
    switches='HIER=1 LSTEP=8 LMAXL=2000 SRCXS=1.012870613', held='everything; only SRCXS moved, to D_M(arm of record)/D_M(control) (was 1.004492152)')))
np.savez(os.path.join(SP, 'r6911_source_lcdm_leafrec1.npz'), **out)
print(f'  control Dl unchanged to {dd:.2e}; xswap {float(out["xswap"]):.9f}; split residual {float(np.max(out["resid"])):.2e} -> spectra/r6911_source_lcdm_leafrec1.npz')
