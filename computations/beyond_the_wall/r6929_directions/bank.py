"""fold r6929's runs into the banks the receipt reads -- r6929+cc66.44.

  * `r6929_scan_cr.npz` -- the arm's REAL spectrum and its INJECTION at six values of `VISLEAF`,
    each summed over its six `KSLICE` pieces.  ⚠ The `inj_*` arrays are the projection's transfer of
    a KNOWN input and are NOT spectra of the model; only `comb_*` are -- kept under separate keys so
    nothing reads one as the other, which is `r6925`'s caveat carried forward.
  * `r6929_noop.npz` -- the gates: `VISLEAF=0` against the unset path on the ARM (the fraction's
    zero must BE the flag's off), and the CONTROL at f=0 against f=0.5 (`Jac == 1` there by the rate
    identity, so the whole family collapses to one run -- gated, not assumed).
  * the geometry is `geom.py`'s and lands in `r6929_geometry.npz`.
"""
import os
import re
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.join(HERE, '..', 'spectra')
D = '/tmp/n66/r6929'
NK, STEP = 1452, 250
FS = ['0', '0.1', '0.25', '0.5', '0.75', '1']

out = {}
for f in FS:
    t = f.replace('.', '')
    for tag, sub in ((f'comb_cr_f{t}', 'comb'), (f'inj_cr_f{t}', 'inj')):
        fs = sorted((int(re.search(r'_k(\d+)$', x[:-4]).group(1)), x)
                    for x in os.listdir(f'{D}/{sub}')
                    if x.startswith(f'{tag}_k') and x.endswith('.npz'))
        assert [i for i, _ in fs] == list(range(0, NK, STEP)), f'{tag}: slices {[i for i, _ in fs]}'
        ds = [np.load(os.path.join(D, sub, x)) for _, x in fs]
        ls = ds[0]['ls']
        for d in ds:
            assert np.array_equal(d['ls'], ls), f'{tag}: slices differ on the multipoles'
        out[f'ls__{tag}'] = ls
        out[f'Dl__{tag}'] = sum(d['Dl'] for d in ds)
        for q in ('l_A', 'D_M', 'r_s'):
            out[f'{q}__{tag}'] = ds[0][q]
    print(f'  VISLEAF={f}: the real spectrum and the injection, {len(out[f"ls__comb_cr_f{t}"])} multipoles')
out['f'] = np.array([float(x) for x in FS])
np.savez(os.path.join(SP, 'r6929_scan_cr.npz'), **out)
print('  -> spectra/r6929_scan_cr.npz')

g = {}
for tag in ('unset_cr', 'zero_cr', 'noop_lcdm_f0', 'noop_lcdm_f050'):
    d = np.load(f'{D}/noop/{tag}.npz')
    g[f'ls__{tag}'], g[f'Dl__{tag}'] = d['ls'], d['Dl']
np.savez(os.path.join(SP, 'r6929_noop.npz'), **g)
print('  the gates: 4 spectra -> spectra/r6929_noop.npz')
