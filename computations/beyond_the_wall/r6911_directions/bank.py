"""fold r6911's sliced source runs into the two banks the receipt reads.

** THE SLICES ADD EXACTLY AND THE PER-k ARRAYS CONCATENATE EXACTLY, AND THE TWO FACTS ARE
DIFFERENT. **  `Dl` is a SUM over k, so disjoint `KSLICE` pieces add -- and only on `KBATCH`
boundaries, which r6895+cc66.38 measured as exact to 1e-16 on both arms because the whole run and
the pieces then use the same batches.  The SOURCE arrays are indexed by k alone, so they simply
concatenate in k order; the one array that carries a batch-dependent quantity is `P`, whose
`dk = np.gradient(kb)` is one-sided at each batch edge -- banked as computed, and the receipt
measures what including it does rather than assuming a smooth factor is inert.
"""
import os, re, sys
import numpy as np

D = '/tmp/n66/r6911/src'
SP = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'spectra')
PERK = ('k', 'P', 'sw_ls', 'dp_ls', 'isw_ls', 'pol_ls', 'md_ls', 'S_ls',
        'sw_i', 'dp_i', 'isw_i', 'pol_i', 'md_i', 'S_i', 'resid')
SCAL = ('eta_ls', 'eta_ls_w', 'eta_used', 'n_eta', 'xswap', 'arm', 'r_s', 'D_M', 'l_A', 'ns',
        'ombh2', 'R_peak')

for arm in ('lcdm', 'cr'):
    fs = sorted((int(re.search(r'_k(\d+)_', f).group(1)), f)
                for f in os.listdir(D) if f.startswith(f'src_{arm}_k') and f.endswith('_fields.npz'))
    if not fs:
        sys.exit(f'no slices for {arm}')
    ds = [np.load(os.path.join(D, f)) for _, f in fs]
    out = {q: np.concatenate([d[q] for d in ds]) for q in PERK}
    # the slice starts must tile the k axis with no gap and no overlap, or the concatenation is
    # not the run's k grid -- gated here rather than trusted, because a missing slice would show
    # up as a perfectly plausible shorter grid.
    n = 0
    for (i0, f), d in zip(fs, ds):
        assert i0 == n, f'{arm}: slice at {i0} follows {n} -- a gap or an overlap'
        n += len(d['k'])
    assert np.all(np.diff(out['k']) > 0), f'{arm}: k not increasing after the concatenation'
    out['ls'] = ds[0]['ls']
    for d in ds:
        assert np.array_equal(d['ls'], out['ls']), f'{arm}: the slices report different multipoles'
    # the partial spectra add: Dl = l(l+1) sum_k, so the pieces sum to the whole
    sp = [np.load(os.path.join(D, f.replace('_fields', '')))
          for _, f in fs]
    out['Dl'] = sum(s['Dl'] for s in sp)
    out['Dl_swap'] = sum(d['Dl_swap'] for d in ds)
    for q in SCAL:
        out[q] = ds[0][q]
    out['n_slices'] = np.array(len(ds))
    np.savez(os.path.join(SP, f'r6911_source_{arm}.npz'), **out)
    print(f'  {arm}: {len(ds)} slices, {len(out["k"])} modes, {len(out["ls"])} multipoles, '
          f'split residual {float(np.max(out["resid"])):.3e}, xswap {float(out["xswap"]):.6f} '
          f'-> spectra/r6911_source_{arm}.npz')
