"""fold r6919's injected-source runs into one bank per arm, plus the no-op pair.

** THESE ARE NOT SPECTRA OF THE MODEL AND THE BANK SAYS SO IN ITS OWN KEYS. **  Each is what this
arm's projection makes of a KNOWN analytic oscillation -- the transfer of the machinery, not a
prediction -- so nothing here may be compared with a banked spectrum or with the sky.  The `D_l`
slices add over k exactly as always, on `KBATCH` boundaries (r6895+cc66.38).
"""
import os, re, sys
import numpy as np

D = '/tmp/n66/r6919/inj'
SP = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'spectra')
TAGS = ('sweepown', 'sweepph', 'fixed', 'sweepstk', 'viswap')
NK = {'lcdm': 2547, 'cr': 1452}

for arm in ('lcdm', 'cr'):
    out = {}
    for tag in TAGS:
        fs = sorted((int(re.search(r'_k(\d+)$', f[:-4]).group(1)), f)
                    for f in os.listdir(D)
                    if f.startswith(f'inj_{tag}_{arm}_k') and f.endswith('.npz'))
        if not fs:
            sys.exit(f'no slices for {tag} {arm}')
        ds = [np.load(os.path.join(D, f)) for _, f in fs]
        ls = ds[0]['ls']
        for d in ds:
            assert np.array_equal(d['ls'], ls), f'{tag} {arm}: slices differ on the multipoles'
        # the slice starts must tile the k axis -- a missing slice reads as a plausible spectrum
        want = list(range(0, NK[arm], 250))
        assert [i for i, _ in fs] == want, f'{tag} {arm}: slices {[i for i,_ in fs]} != {want}'
        out[f'ls__{tag}'] = ls
        out[f'Dl__{tag}'] = sum(d['Dl'] for d in ds)
        out[f'n__{tag}'] = np.array(len(ds))
        for q in ('l_A', 'D_M', 'r_s', 'arm'):
            out[f'{q}__{tag}'] = ds[0][q]
    np.savez(os.path.join(SP, f'r6919_injected_{arm}.npz'), **out)
    print(f'  {arm}: {len(TAGS)} configurations x {len(out["ls__fixed"])} multipoles '
          f'-> spectra/r6919_injected_{arm}.npz')

out = {}
for tag in ('noop_lcdm', 'noop_cr'):
    d = np.load(f'/tmp/n66/r6919/noop/{tag}.npz')
    out[f'ls__{tag}'], out[f'Dl__{tag}'] = d['ls'], d['Dl']
np.savez(os.path.join(SP, 'r6919_noop.npz'), **out)
print('  the no-op pair: 2 spectra -> spectra/r6919_noop.npz')
