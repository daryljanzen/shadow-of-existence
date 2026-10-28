"""r7633+70: the lensed/unlensed TT ratio refit_grid185/fit.py reads from /tmp/n66/lens_ratio.npy (no longer on disk),
regenerated with CAMB at Planck's control parameters -- the operator P15 names (as the collapse receipt builds it)."""
import os, numpy as np, camb
p = camb.set_params(H0=67.40, ombh2=0.02237, omch2=0.3150 * 0.674 ** 2 - 0.02237, mnu=0.06, omk=0, tau=0.054,
                    As=2.1e-9, ns=0.965, lmax=3000)
c = camb.get_results(p).get_cmb_power_spectra(p, CMB_unit='muK', lmax=3000)
L, U = c['total'][:, 0], c['unlensed_scalar'][:, 0]
lg = np.arange(len(L)); r = np.ones_like(L); m = U > 0; r[m] = L[m] / U[m]
np.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lens_ratio.npy'), np.vstack([lg, r]))
print(f"ratio at l = 1900: {np.interp(1900, lg, r):.4f}")
