"""fold r6941's fine-grid runs into the banks the receipt reads -- r6941+cc66.45.

  * `r6941_fine_{lcdm,cr}.npz` -- the reported configuration at `LSTEP=1 LMAXL=2000`, eight times the
    multipole sampling, on both arms.  ** This is the reference the coarse grid's locator is measured
    against, peak by peak, which is what the order asks for before any residual is read. **
  * `r6941_fine_cr_visleaf.npz` -- the arm's `VISLEAF=1` endpoint, real and injected, at the same fine
    sampling, so `cc66.44`'s three-way separation can be read at l_2, l_3 and l_4 rather than at l_1
    alone.  ⚠ The injected arrays are the projection's transfer of a known input and are NOT spectra of
    the model -- separate keys.
"""
import os
import re
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.join(HERE, '..', 'spectra')
D = '/tmp/n66/r6941'
STEP = 250
NK = {'lcdm': 2547, 'cr': 1452}


def fold(sub, tag, nk):
    fs = sorted((int(re.search(r'_k(\d+)$', x[:-4]).group(1)), x)
                for x in os.listdir(f'{D}/{sub}')
                if x.startswith(f'{tag}_k') and x.endswith('.npz'))
    assert [i for i, _ in fs] == list(range(0, nk, STEP)), f'{tag}: slices {[i for i, _ in fs]}'
    ds = [np.load(os.path.join(D, sub, x)) for _, x in fs]
    ls = ds[0]['ls']
    for d in ds:
        assert np.array_equal(d['ls'], ls), f'{tag}: slices differ on the multipoles'
    return dict(ls=ls, Dl=sum(d['Dl'] for d in ds), l_A=ds[0]['l_A'], D_M=ds[0]['D_M'],
                r_s=ds[0]['r_s'], arm=ds[0]['arm'])


for arm, tag in (('lcdm', 'fine_lcdm'), ('cr', 'fine_cr')):
    out = fold('fine', tag, NK[arm])
    np.savez(os.path.join(SP, f'r6941_fine_{arm}.npz'), **out)
    print(f'  {arm}: {len(out["ls"])} multipoles at LSTEP=1 -> spectra/r6941_fine_{arm}.npz')

out = {}
for key, sub, tag in (('comb_f1', 'fine', 'fine_cr_f1'), ('inj_f0', 'inj', 'finj_cr'),
                      ('inj_f1', 'inj', 'finj_cr_f1')):
    d = fold(sub, tag, NK['cr'])
    for q in ('ls', 'Dl', 'l_A', 'D_M', 'r_s'):
        out[f'{q}__{key}'] = d[q]
    print(f'  cr {key}: {len(d["ls"])} multipoles at LSTEP=1')
np.savez(os.path.join(SP, 'r6941_fine_cr_visleaf.npz'), **out)
print('  -> spectra/r6941_fine_cr_visleaf.npz')
