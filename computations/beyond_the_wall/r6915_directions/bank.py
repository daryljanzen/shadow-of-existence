"""fold r6915's sliced decomposition runs into the banks the receipt reads.

** THE TEN PAIR SPECTRA ADD OVER k EXACTLY AS `Dl` DOES, and for the same reason. **  Each column is
SUM_k P Delta^a Delta^b over the batch's own modes, so disjoint `KSLICE` pieces on `KBATCH`
boundaries sum to the whole -- the property r6895+cc66.38 measured as exact to 1e-16 on both arms,
here re-gated on eleven columns instead of one.
"""
import os, re, sys
import numpy as np

D = '/tmp/n66/r6915/dec'
SP = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'spectra')

for arm in ('lcdm', 'cr'):
    fs = sorted((int(re.search(r'_k(\d+)_', f).group(1)), f)
                for f in os.listdir(D) if f.startswith(f'dec_{arm}_k') and f.endswith('_pairs.npz'))
    if not fs:
        sys.exit(f'no slices for {arm}')
    ds = [np.load(os.path.join(D, f)) for _, f in fs]
    ls = ds[0]['ls']
    for d in ds:
        assert np.array_equal(d['ls'], ls), f'{arm}: the slices report different multipoles'
        assert list(d['pairs']) == list(ds[0]['pairs']), f'{arm}: the pair ORDER differs by slice'
    # the slice starts must tile the k axis with no gap and no overlap -- a missing slice would
    # otherwise show up as a perfectly plausible spectrum that is simply short.
    n = 0
    for (i0, _), d in zip(fs, ds):
        assert i0 == n, f'{arm}: slice at {i0} follows {n} -- a gap or an overlap'
        n += int(d['n_modes'])
    out = dict(ls=ls, pairs=ds[0]['pairs'],
               Dl=sum(d['Dl'] for d in ds), Dl_pairs=sum(d['Dl_pairs'] for d in ds),
               n_slices=np.array(len(ds)), n_modes=np.array(n))
    for q in ('arm', 'r_s', 'D_M', 'l_A', 'ns', 'eta_ls', 'eta_ls_w'):
        out[q] = ds[0][q]
    rel = float(np.max(np.abs(out['Dl_pairs'].sum(axis=1) - out['Dl']) / np.abs(out['Dl'])))
    np.savez(os.path.join(SP, f'r6915_pairs_{arm}.npz'), **out)
    print(f'  {arm}: {len(ds)} slices, {n} modes, {len(ls)} multipoles, 10 pairs; '
          f'the pairs close on D_l to {rel:.3e} relative -> spectra/r6915_pairs_{arm}.npz')

out = {}
for tag in ('noop_lcdm', 'noop_cr'):
    d = np.load(f'/tmp/n66/r6915/noop/{tag}.npz')
    out[f'ls__{tag}'], out[f'Dl__{tag}'] = d['ls'], d['Dl']
np.savez(os.path.join(SP, 'r6915_noop.npz'), **out)
print('  the no-op pair: 2 spectra -> spectra/r6915_noop.npz')
