"""r7633+70: the peak-family figures P15 prints off the banked LEAFREC=0 arm, recomputed on a given arm.
The locator is cc66's three-point parabola at the extremum (the one the locator receipt runs on r6941_fine),
applied to the spectrum splined to every multipole -- the LSTEP=8 grid is splined first, which grid_check.py
measures to 0.016 of a multipole.  python3 census_peaks.py ARM_NPZ [CONTROL_NPZ] [label]"""
import sys, numpy as np
from scipy.interpolate import CubicSpline
from scipy.signal import argrelextrema
SKY = np.array([220.4, 537.7, 817.3, 1123.9])          # P15 sec:intro's own locator on plik_lite TT
def peaks(path):
    z = np.load(path); ls = z['ls'].astype(float); D = z['Dl']
    lf = np.arange(ls[0], ls[-1] + 1.0); y = CubicSpline(ls, D)(lf) if np.diff(ls).max() > 1 else D
    out = []
    for i in argrelextrema(y, np.greater, order=3)[0][:4]:
        out.append(lf[i] + 0.5 * (y[i - 1] - y[i + 1]) / (y[i - 1] - 2 * y[i] + y[i + 1]))
    h = [y[int(round(p - lf[0]))] for p in out]
    return np.array(out), np.array(h)
def comb(pk):
    n = np.arange(1, 4.0); lA, b = np.linalg.lstsq(np.vstack([n, np.ones(3)]).T, pk[:3], rcond=None)[0]
    return lA, b / lA            # the comb spacing and phi/pi with l_m = l_A (m - phi/pi) (P15's convention)
a, ha = peaks(sys.argv[1]); lab = sys.argv[3] if len(sys.argv) > 3 else sys.argv[1]
print(f"  {lab}")
print(f"    peaks            " + " / ".join(f"{x:.2f}" for x in a))
print(f"    arm - sky        " + " / ".join(f"{x:+.2f}" for x in a - SKY))
lA, ph = comb(a)
print(f"    comb l_A {lA:.2f}   phi/pi {-ph:+.4f}   P1/P2 {ha[0] / ha[1]:.3f}   P1/P3 {ha[0] / ha[2]:.3f}")
if len(sys.argv) > 2 and sys.argv[2] != '-':
    c, hc = peaks(sys.argv[2])
    print(f"    arm - control    " + " / ".join(f"{x:+.2f}" for x in a - c))
    print(f"    control's share of the arm's offset at the fourth peak: {(c[3] - SKY[3]) / (a[3] - SKY[3]):.2f}")
