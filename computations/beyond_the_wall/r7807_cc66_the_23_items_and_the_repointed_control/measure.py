"""r7807+cc66 item ②: what the re-pointed control does to every figure resting on its old point.

Scoring is the refit receipts' own: P15's CAMB lensing operator imposed on both arms,
`chi2_of_spectrum.chi2_of`, 185 lensed bins, one amplitude in closed form.

The published 0.918 is chi2(arm, no fit) / chi2(control, no fit).  The ARM does not move when the
control's point does, so the whole move is the denominator's -- and the arm's chi^2 is recovered from
the published ratio times the published control's own score, so no arm run is needed.

Run: python3 measure.py
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(BW))
SP = os.path.join(BW, 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import camb                                                                   # noqa: E402
import chi2_of_spectrum as CS                                                 # noqa: E402

WB = 0.02237
_p = camb.set_params(H0=67.40, ombh2=WB, omch2=0.3150 * 0.674 ** 2 - WB, mnu=0.06, omk=0, tau=0.054,
                     As=2.1e-9, ns=0.965, lmax=3000)
_cl = camb.get_results(_p).get_cmb_power_spectra(_p, CMB_unit='muK', lmax=3000)
_le, _un = _cl['total'][:, 0], _cl['unlensed_scalar'][:, 0]
LG = np.arange(len(_le), dtype=float)
RATIO = np.ones_like(_le)
RATIO[_un > 0] = _le[_un > 0] / _un[_un > 0]


def load(p):
    with np.load(p, allow_pickle=True) as z:
        return np.asarray(z['ls'], float), np.asarray(z['Dl'], float)


def score(ls, Dl):
    c, nb = CS.chi2_of(ls, Dl * np.interp(ls, LG, RATIO))[:2]
    return float(c), int(nb)


def peaks(ls, Dl, n=4):
    y = Dl * np.interp(ls, LG, RATIO)
    out = []
    for i in range(2, len(ls) - 2):
        if y[i] > y[i - 1] and y[i] > y[i + 1] and y[i] > y[i - 2] and y[i] > y[i + 2]:
            a, b, c = y[i - 1], y[i], y[i + 1]
            d = a - 2 * b + c
            out.append(ls[i] + (0.5 * (a - c) / d if d else 0.0) * (ls[i + 1] - ls[i]))
    return out[:n]


OLD = os.path.join(SP, 'cc66_lcdm_L2000.npz')
NEW = os.path.join(HERE, 'out', 'r7807_control_planck2018_L2000.npz')
lo, Do = load(OLD)
ln, Dn = load(NEW)
co, nbo = score(lo, Do)
cn, nbn = score(ln, Dn)

print("  THE CONTROL'S NO-FIT CHI^2 OVER 185 LENSED BINS")
print(f"    corpus's rounded point (67.40, Om 0.3150)   {co:9.3f}  over {nbo} bins")
print(f"    Planck 2018's published point (67.36, ...)  {cn:9.3f}  over {nbn} bins")
print(f"    moves {cn - co:+.3f} = {100 * (cn - co) / co:+.3f} per cent   "
      f"({'IMPROVES' if cn < co else 'WORSENS'})\n")

PUB = 0.918
arm = PUB * co
new = arm / cn
print("  THE PUBLISHED 0.918  (the arm's distance from the data in units of the control's)")
print(f"    published                     {PUB:.3f}")
print(f"    the arm's implied chi^2       {arm:9.3f}   (0.918 x the control's {co:.3f})")
print(f"    re-pointed, the ratio becomes {new:.4f}  -> prints as {new:.3f}")
print(f"    moves {new - PUB:+.4f}; the arm's margin falls from {100 * (1 - PUB):.1f} to "
      f"{100 * (1 - new):.1f} per cent")
STENCIL = 0.9571
print(f"\n  AGAINST r7805's STENCIL, which held H0 FIXED at 67.40 and moved only Omega_m")
print(f"    stencil said {STENCIL:.4f}; the real run says {new:.4f}; difference {new - STENCIL:+.4f}")
print(f"    ⇒ the stencil's scope {'REACHED' if abs(new - STENCIL) <= 0.01 else 'DID NOT REACH'} "
      f"this far (registered bound 0.01)")

po, pn = peaks(lo, Do), peaks(ln, Dn)
print("\n  THE CONTROL'S PEAK POSITIONS (parabolic on the lensed binned grid)")
for i, (a, b) in enumerate(zip(po, pn), 1):
    print(f"    peak {i}:  {a:8.3f}  ->  {b:8.3f}   moves {b - a:+.4f} multipoles")
if po:
    print(f"    largest move {max(abs(b - a) for a, b in zip(po, pn)):.4f} multipoles")
