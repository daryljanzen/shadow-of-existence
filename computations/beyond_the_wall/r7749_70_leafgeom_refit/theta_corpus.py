"""r7753 ①: theta_* on the corpus's own definition, re-solved on the leaf-rate assignment.

The corpus's definition is the P15 DESI receipt's (`P15_the_desi_dissolution_survives_the_leaf_ruler...`):
    theta_* = r_snd(H0, Om, z_hi, z_rec, E_leaf) / D_M(z_rec, H0, Om, E_geom)
with the sound horizon ALWAYS on the leaf clock (node 66's ruling: one clock for r_s and r_D), c_s set by the
baryon loading R0 = 3 omega_b / (4 omega_gamma), z_rec = 1090, and the distance on the GEOMETRY'S rate:
    arm of record:            E_geom = E_stack (radiation-free)
    leaf-rate assignment:     E_geom = E_leaf  (radiation included)
Two readings, both the receipt's:
  (i)  z_hi = the arm's own start, ZSTART = 3e7 (the arm of record runs with the onset dissolved, from 3e7);
       the receipt's `theta_noonset` uses z_hi = 1e8 -- reported too, to show z_hi this high does not matter.
  (ii) the onset that MATCHES THETA_OBS, solved for by brentq as the receipt's `z_onset_of` does, with its
       rho_r/rho_m = (1+z_on) * omega_r / omega_m.
omega_b is each point's own (the receipt hard-codes Planck's 0.02237; at a refit point the fitted omega_b is used,
and the 0.02237 reading is printed beside it so the choice is visible).
"""
import json
import os

import numpy as np
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
trapz = np.trapezoid
c = 299792.458
WG, WR = 2.47e-5, 4.15e-5
ZREC = 1090.0
THETA_OBS, THETA_SIG = 0.0104085, 3.1e-6


def E_stack(z, Om, h):
    return np.sqrt(Om * (1 + z) ** 3 + (1 - Om))


def E_leaf(z, Om, h):
    return np.sqrt(Om * (1 + z) ** 3 + (WR / h ** 2) * (1 + z) ** 4 + (1 - Om))


def D_M(z, H0, Om, E, n=20000):
    zz = np.linspace(0, z, n)
    return trapz(c / (H0 * E(zz, Om, H0 / 100)), zz)


def r_snd(H0, Om, wb, z_hi, z_lo, E, n=60000):
    R0 = 3 * wb / (4 * WG)
    u = np.linspace(np.log(1 + z_lo), np.log(1 + z_hi), n)
    z = np.exp(u) - 1
    cs = c / np.sqrt(3 * (1 + R0 / (1 + z)))
    return trapz(cs / (H0 * E(z, Om, H0 / 100)) * (1 + z), u)


def theta(H0, Om, wb, z_hi, Egeom):
    return r_snd(H0, Om, wb, z_hi, ZREC, E_leaf) / D_M(ZREC, H0, Om, Egeom)


def onset(H0, Om, wb, Egeom):
    f = lambda zo: theta(H0, Om, wb, zo, Egeom) - THETA_OBS        # noqa: E731
    lo, hi = 1.2e3, 1e9
    if f(lo) * f(hi) > 0:
        return None
    return brentq(f, lo, hi, xtol=1e-3)


POINTS = {
    "distances' point (68.60, 0.2973), omega_b built-in 0.02237": (68.60, 0.2973, 0.02237),
    'arm of record refit point (68.5707, 0.29125, 0.021643)': (68.570730, 0.291246, 0.021643),
    'leaf-rate refit minimum (68.5857, 0.29446, 0.022181)': (68.585672, 0.294463, 0.022181),
}
out = {}
print(f"  THETA_OBS {THETA_OBS}  sigma {THETA_SIG}   z_rec {ZREC}")
for name, (H0, Om, wb) in POINTS.items():
    row = {}
    for gname, Eg in (('arm of record (D_M on stacking rate)', E_stack), ('leaf-rate assignment (D_M on leaf rate)', E_leaf)):
        t3 = theta(H0, Om, wb, 3e7, Eg)
        t8 = theta(H0, Om, wb, 1e8, Eg)
        zo = onset(H0, Om, wb, Eg)
        row[gname] = dict(theta_zstart=t3, pull_zstart=(t3 - THETA_OBS) / THETA_SIG, theta_1e8=t8,
                          onset_matching=zo, rho_r_over_rho_m_at_onset=(None if zo is None else (1 + zo) * WR / (Om * (H0 / 100) ** 2)))
        zs = 'none in [1.2e3, 1e9]' if zo is None else f"{zo:.4g} (rho_r/rho_m {row[gname]['rho_r_over_rho_m_at_onset']:.2f})"
        print(f"  {name:>58} | {gname:>40}: 100theta {100 * t3:.5f} ({row[gname]['pull_zstart']:+.1f} sigma at z_hi=3e7; "
              f"1e8 gives {100 * t8:.5f}); matching onset {zs}")
    out[name] = row
json.dump(out, open(os.path.join(HERE, 'theta_corpus.json'), 'w'), indent=1)
