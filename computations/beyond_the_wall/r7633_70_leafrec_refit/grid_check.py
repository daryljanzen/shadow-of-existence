"""r7633+70: is the LSTEP=8 grid plus spline good enough to locate the fourth acoustic feature in EE and TE?
CAMB's spectra at every multipole stand in for a fine run: each feature is located on the full grid (three-point
parabola at the extremum, as on r6941_fine) and on the LSTEP=8 subsample l = 100, 108, ... splined to every
multipole (as the POLSAVE spectra are), for the control and for a shifted-H0 variant (a stand-in arm)."""
import numpy as np, camb
from scipy.interpolate import CubicSpline
from scipy.signal import argrelextrema
FEAT = {'TT': (1050, 1200, 1, 0), 'EE': (930, 1060, 1, 1), 'TE': (1010, 1130, -1, 3)}
def three(l, y):
    i = np.argmax(y); return l[i] + 0.5 * (y[i - 1] - y[i + 1]) / (y[i - 1] - 2 * y[i] + y[i + 1])
for H0 in (67.41, 68.58):
    p = camb.set_params(H0=H0, ombh2=0.021966, omch2=0.309826 * (H0 / 100) ** 2 - 0.021966, ns=0.954248, As=2.1e-9,
                        tau=0.054, mnu=0.0, lmax=2200)
    cl = camb.get_results(p).get_unlensed_scalar_cls(CMB_unit='muK', lmax=2100)
    L = np.arange(cl.shape[0]).astype(float)
    for s, (lo, hi, sg, col) in FEAT.items():
        m = (L >= lo) & (L <= hi); fine = three(L[m], sg * cl[m, col])
        lc = np.arange(100, 2000, 8).astype(float); sp = CubicSpline(lc, cl[lc.astype(int), col])
        lf = np.arange(lo, hi + 1.0); coarse = three(lf, sg * sp(lf))
        print(f"  H0 {H0:5.2f} {s}: fine {fine:8.3f}  coarse+spline {coarse:8.3f}  error {coarse - fine:+.3f}")
