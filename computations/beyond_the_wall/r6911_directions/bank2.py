"""fold r6911's no-op pair and its uniform-grid arm into the last two banks the receipt reads.

  * `r6911_noop.npz` -- the two arms with `SRCSAVE` unset, and again with `SRCXS=1.5` and `SRCSAVE`
    still unset, at the screen grid.  The receipt gates all four against `r6893_switch_screen_*`'s
    banked base BIT-IDENTICALLY, which is what makes "the edit added nothing" a measurement.
  * `r6911_source_cr_kcont.npz` -- the arm with `KCONT=1`, the uniform continuum sampling at the
    control's own mode count, everything else the adjudicated minimum.  ** The one artefact that
    could have produced the whole answer, run out rather than argued. **
"""
import os, re, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.join(HERE, '..', 'spectra')
PERK = ('k', 'P', 'sw_ls', 'dp_ls', 'isw_ls', 'pol_ls', 'md_ls', 'S_ls',
        'sw_i', 'dp_i', 'isw_i', 'pol_i', 'md_i', 'S_i', 'resid')
SCAL = ('eta_ls', 'eta_ls_w', 'eta_used', 'n_eta', 'xswap', 'arm', 'r_s', 'D_M', 'l_A', 'ns',
        'ombh2', 'R_peak')

out = {}
for tag in ('noop_lcdm', 'noop_cr', 'xsonly_lcdm', 'xsonly_cr'):
    d = np.load(f'/tmp/n66/r6911/noop/{tag}.npz')
    out[f'ls__{tag}'] = d['ls']
    out[f'Dl__{tag}'] = d['Dl']
np.savez(os.path.join(SP, 'r6911_noop.npz'), **out)
print(f'  the no-op pair and the SRCXS guard: 4 spectra -> spectra/r6911_noop.npz')

D = '/tmp/n66/r6911/kcont'
fs = sorted((int(re.search(r'_k(\d+)_', f).group(1)), f)
            for f in os.listdir(D) if f.startswith('src_crkc_k') and f.endswith('_fields.npz'))
if not fs:
    sys.exit('no KCONT slices')
ds = [np.load(os.path.join(D, f)) for _, f in fs]
o = {q: np.concatenate([d[q] for d in ds]) for q in PERK}
n = 0
for (i0, f), d in zip(fs, ds):
    assert i0 == n, f'slice at {i0} follows {n} -- a gap or an overlap'
    n += len(d['k'])
assert np.all(np.diff(o['k']) > 0), 'k not increasing after the concatenation'
o['ls'] = ds[0]['ls']
sp = [np.load(os.path.join(D, f.replace('_fields', ''))) for _, f in fs]
o['Dl'] = sum(s['Dl'] for s in sp)
o['Dl_swap'] = sum(d['Dl_swap'] for d in ds)
for q in SCAL:
    o[q] = ds[0][q]
o['n_slices'] = np.array(len(ds))
np.savez(os.path.join(SP, 'r6911_source_cr_kcont.npz'), **o)
print(f'  the arm on the uniform grid: {len(ds)} slices, {len(o["k"])} modes, '
      f'split residual {float(np.max(o["resid"])):.3e} -> spectra/r6911_source_cr_kcont.npz')
