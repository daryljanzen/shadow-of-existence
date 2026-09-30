"""fold r7039's runs into three banks: the quadrature variations, and the transfer Delta_l(k).

** NOTHING HERE IS A SPECTRUM OF THE MODEL AND THE BANK'S OWN KEYS SAY SO. **  Every run is the
projection's transfer of a KNOWN analytic oscillation -- `SRCINJ` -- so no key here may be compared
with a banked spectrum or with the sky.  The `Dl` slices ADD over k, exactly as always, on `KBATCH`
boundaries (r6895+cc66.38); the TRANSFER slices CONCATENATE, because Delta_l(k) is indexed by (l, k)
and each batch carries a disjoint set of k.
"""
import os, re, sys
import numpy as np

D = '/tmp/n66/r7039'
SP = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'spectra')
NK = {'lcdm': 2547, 'cr': 1452}
QTAGS = ('n1120', 'n2240', 'w9', 'w4', 'f90')
TTAGS = ('fixed', 'sweepown')


def slices(d, pre, arm):
    fs = sorted((int(re.search(r'_k(\d+)$', f[:-4]).group(1)), f)
                for f in os.listdir(d)
                if f.startswith(f'{pre}_{arm}_k') and f.endswith('.npz') and '_T' not in f)
    want = list(range(0, NK[arm], 250))
    got = [i for i, _ in fs]
    if got != want:
        sys.exit(f'{pre} {arm}: slices {got} != {want} -- a missing slice reads as a plausible spectrum')
    return [np.load(os.path.join(d, f)) for _, f in fs]


# ⓐ the quadrature variations: D_l only, summed over the k axis
for arm in ('lcdm', 'cr'):
    out = {}
    for tag in QTAGS:
        ds = slices(os.path.join(D, 'inj'), f'inj_{tag}', arm)
        ls = ds[0]['ls']
        for d in ds:
            assert np.array_equal(d['ls'], ls), f'{tag} {arm}: slices differ on the multipoles'
        out[f'ls__{tag}'] = ls
        out[f'Dl__{tag}'] = sum(d['Dl'] for d in ds)
        out[f'n__{tag}'] = np.array(len(ds))
        for q in ('l_A', 'D_M', 'r_s', 'arm'):
            out[f'{q}__{tag}'] = ds[0][q]
    np.savez(os.path.join(SP, f'r7039_quad_{arm}.npz'), **out)
    print(f'  {arm}: {len(QTAGS)} quadrature variations -> spectra/r7039_quad_{arm}.npz')

# ⓑ/ⓔ the transfer itself, concatenated along k
for arm in ('lcdm', 'cr'):
    out = {}
    for tag in TTAGS:
        ds = slices(os.path.join(D, 'dlk'), f'dlk_{tag}', arm)
        ts = []
        for i, _ in sorted((int(re.search(r'_k(\d+)_T$', f[:-4]).group(1)), f)
                           for f in os.listdir(os.path.join(D, 'dlk'))
                           if f.startswith(f'dlk_{tag}_{arm}_k') and f.endswith('_T.npz')):
            ts.append(np.load(os.path.join(D, 'dlk', f'dlk_{tag}_{arm}_k{i}_T.npz')))
        want = list(range(0, NK[arm], 250))
        if len(ts) != len(want):
            sys.exit(f'{tag} {arm}: {len(ts)} transfer slices, want {len(want)}')
        ls = ts[0]['ls']
        for t in ts:
            assert np.array_equal(t['ls'], ls), f'{tag} {arm}: transfer slices differ on the multipoles'
        k = np.concatenate([t['k'] for t in ts])
        assert np.all(np.diff(k) > 0), f'{tag} {arm}: the concatenated k axis is not increasing'
        out[f'ls__{tag}'] = ls
        out[f'k__{tag}'] = k
        out[f'P__{tag}'] = np.concatenate([t['P'] for t in ts])
        out[f'Dlk__{tag}'] = np.concatenate([t['Dlk'] for t in ts], axis=1)
        out[f'Dl__{tag}'] = sum(d['Dl'] for d in ds)
        out[f'closes__{tag}'] = np.array([float(t['closes']) for t in ts])
        # the eta-side objects are the same on every slice of one configuration, so one copy
        for q in ('eta', 'x0', 'vis', 'rs_leaf', 'rs_stack', 'jac'):
            out[f'{q}__{tag}'] = ts[0][q]
        for q in ('l_A', 'D_M', 'r_s', 'arm', 'ns', 'eta_ls', 'eta_ls_w', 'nlos', 'nlosw', 'nlosf',
                  'inj', 'inj_rs', 'inj_vis', 'inj_ph'):
            out[f'{q}__{tag}'] = ts[0][q]
    np.savez(os.path.join(SP, f'r7039_transfer_{arm}.npz'), **out)
    print(f'  {arm}: {len(TTAGS)} transfers x {len(out["ls__fixed"])} multipoles '
          f'x {len(out["k__fixed"])} modes -> spectra/r7039_transfer_{arm}.npz')

out = {}
for tag in ('noop_lcdm', 'noop_cr'):
    d = np.load(os.path.join(D, 'noop', f'{tag}.npz'))
    out[f'ls__{tag}'], out[f'Dl__{tag}'] = d['ls'], d['Dl']
np.savez(os.path.join(SP, 'r7039_noop.npz'), **out)
print('  the no-op pair: 2 spectra -> spectra/r7039_noop.npz')
