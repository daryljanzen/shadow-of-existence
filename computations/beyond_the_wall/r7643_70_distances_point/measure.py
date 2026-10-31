"""r7643+70: the no-fit and refit headlines, old -> new, scored exactly as the refit-bound receipt scores them
(P15's CAMB lensing operator on both arms, `chi2_of_spectrum.chi2_of`, 185 lensed bins)."""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(BW))
SP = os.path.join(BW, 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import camb                                                                # noqa: E402
import chi2_of_spectrum as CS                                              # noqa: E402

_p = camb.set_params(H0=67.40, ombh2=0.02237, omch2=0.3150 * 0.674 ** 2 - 0.02237,
                     mnu=0.06, omk=0, tau=0.054, As=2.1e-9, ns=0.965, lmax=3000)
_cl = camb.get_results(_p).get_cmb_power_spectra(_p, CMB_unit='muK', lmax=3000)
_le, _un = _cl['total'][:, 0], _cl['unlensed_scalar'][:, 0]
LG = np.arange(len(_le), dtype=float)
RATIO = np.ones_like(_le)
RATIO[_un > 0] = _le[_un > 0] / _un[_un > 0]


def score(path):
    z = np.load(path)
    ls, Dl = np.asarray(z['ls'], float), np.asarray(z['Dl'], float)
    c, nb = CS.chi2_of(ls, Dl * np.interp(ls, LG, RATIO))[:2]
    return float(c), int(nb)


P = lambda *a: os.path.join(BW, *a)                                       # noqa: E731
CFG = [
    ('no-fit L2000, LEAFREC=0 (namesake, the paper)', P('spectra', 'cc66_lcdm_L2000.npz'),
     P('spectra', 'cc66_cr_x_h686_L2000.npz')),
    ('no-fit L2000, LEAFREC=1, distances\' point', P('spectra', 'cc66_lcdm_L2000.npz'),
     P('spectra', 'cc66_cr_x_h686_L2000_leafrec1_distances.npz')),
    ('grid base (LSTEP 8), LEAFREC=0 (namesake)', P('refit_grid185', 'lcdm_base.npz'), P('refit_grid185', 'cr_base.npz')),
    ('grid base (LSTEP 8), LEAFREC=1, distances\' point', P('refit_grid185', 'lcdm_base.npz'),
     P('refit_grid185_leafrec1_distances', 'cr_base.npz')),
    ('refit verified minimum, LEAFREC=0 (namesake)', P('spectra', 'cc66_r185_verify_lcdm.npz'),
     P('spectra', 'cc66_r185_verify_cr.npz')),
    ('refit, LEAFREC=1, arm of record', P('spectra', 'cc66_r185_verify_lcdm.npz'),
     P('spectra', 'cc66_r185_verify_cr_leafrec1.npz')),
]
OUT = {}
print(f"{'configuration':>52} {'bins':>5} {'control':>9} {'/bin':>6} {'arm':>9} {'/bin':>6} {'ratio':>7}")
for tag, pc, pa in CFG:
    (cc, cn), (ac, an) = score(pc), score(pa)
    assert cn == an == 185, (tag, cn, an)
    OUT[tag] = dict(control=cc, arm=ac, bins=cn, ratio=ac / cc)
    print(f"{tag:>52} {cn:>5d} {cc:>9.1f} {cc / cn:>6.2f} {ac:>9.1f} {ac / an:>6.2f} {ac / cc:>6.3f}x")
nf = OUT['no-fit L2000, LEAFREC=1, distances\' point']['ratio']
rf = OUT['refit, LEAFREC=1, arm of record']['ratio']
print(f"\nprediction 1: no-fit ratio in [2.2, 2.9]: {nf:.3f} -> {'HOLDS' if 2.2 <= nf <= 2.9 else 'FIRES'}")
print(f"prediction 2: refit ratio 1.60 +- 0.05:   {rf:.3f} -> {'HOLDS' if abs(rf - 1.60) <= 0.05 else 'FIRES'}")
json.dump(OUT, open(os.path.join(HERE, 'measure.json'), 'w'), indent=1)
