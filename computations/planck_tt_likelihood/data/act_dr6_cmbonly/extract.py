"""ACT DR6 CMB-only (v1.0): verify the banked SACC file and extract it into the harness layout.

Reads  dr6_data_cmbonly.fits  (verbatim from the LAMBDA archive, see PROVENANCE.md) and writes
act_dr6_cmbonly.npz with, for each of TT, TE, EE:
    ell_<s>      bandpower effective multipoles (45)
    Dl_<s>       bandpowers, D_ell in muK^2, foreground-marginalised CMB-only
    win_<s>      bandpower window weights, shape (n_ell_win, 45)
plus
    win_ell      the multipoles the windows are tabulated on (8500)
    cov          the full 135 x 135 covariance in the order TT, TE, EE (45 each)
    order        the data-type order of cov, as strings
and the sha256 of the source file, so a reader can refuse a file that is not this one.

Run: python3 extract.py          (numpy, sacc)
"""
import hashlib
import os
import sys

import numpy as np
import sacc

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'dr6_data_cmbonly.fits')
SHA_FITS = 'c887dc9178d81f5e5e0ce76eca0cd3c9f089056630ab78a1cc4bb28ff8751c29'

h = hashlib.sha256(open(SRC, 'rb').read()).hexdigest()
if h != SHA_FITS:
    sys.exit(f'FATAL: {SRC} has sha256 {h}, not the banked {SHA_FITS}')

s = sacc.Sacc.load_fits(SRC)
T0, T2 = 'dr6_cmb_s0', 'dr6_cmb_s2'
SPEC = (('TT', 'cl_00', (T0, T0)), ('TE', 'cl_0e', (T0, T2)), ('EE', 'cl_ee', (T2, T2)))
out, idx, wl = {}, [], None
for name, dt, tr in SPEC:
    ind = s.indices(dt, tr)
    ell, cl = s.get_ell_cl(dt, *tr)
    w = s.get_bandpower_windows(ind)
    if wl is None:
        wl = np.asarray(w.values, float)
    assert np.array_equal(wl, w.values), 'the three spectra must share one window ell grid'
    out[f'ell_{name}'] = np.asarray(ell, float)
    out[f'Dl_{name}'] = np.asarray(cl, float)
    out[f'win_{name}'] = np.asarray(w.weight, float)
    idx.append(ind)
idx = np.concatenate(idx)
out['cov'] = np.asarray(s.covariance.dense, float)[np.ix_(idx, idx)]
out['win_ell'] = wl
out['order'] = np.array(['TT', 'TE', 'EE'])
out['source_sha256'] = np.array(SHA_FITS)
np.savez_compressed(os.path.join(HERE, 'act_dr6_cmbonly.npz'), **out)

print(f'  source sha256 {h} (verified)')
for name, _dt, _tr in SPEC:
    e = out[f'ell_{name}']
    print(f'  {name}: {len(e)} bandpowers, ell {e.min():.1f}..{e.max():.1f}; window {out[f"win_{name}"].shape}')
c = out['cov']
print(f'  cov {c.shape}, symmetric to {np.max(np.abs(c - c.T)):.1e}, '
      f'min eigenvalue {np.linalg.eigvalsh(c).min():.3e}')
print(f'  windows tabulated on ell {wl.min():.0f}..{wl.max():.0f} ({len(wl)} points)')
