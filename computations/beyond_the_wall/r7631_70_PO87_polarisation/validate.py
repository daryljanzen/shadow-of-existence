"""r7631+70: does POLSAVE's EE/TE on the control match CAMB's at the same parameters?  Peak positions only.
   python3 validate.py CONTROL_POL_NPZ"""
import sys
import numpy as np, camb
from scipy.signal import argrelextrema
d = np.load(sys.argv[1]); ls = d['ls'].astype(float)
h = 0.67410309; om = 0.309826; wb = 0.021966; ns = 0.954248      # r6941's control
p = camb.set_params(H0=100 * h, ombh2=wb, omch2=om * h * h - wb, ns=ns, As=2.1e-9, tau=0.054, mnu=0.0, lmax=2200)
p.WantTensors = False
cl = camb.get_results(p).get_unlensed_scalar_cls(CMB_unit='muK', lmax=2100)    # columns TT EE BB TE, already l(l+1)/2pi
L = np.arange(cl.shape[0])
def peaks(l, y, lo, hi, n=6, sign=1):
    m = (l >= lo) & (l <= hi); l, y = l[m], sign * y[m]
    out = []
    for i in argrelextrema(y, np.greater, order=3)[0]:
        if 0 < i < len(l) - 1:
            y0, y1, y2 = y[i - 1], y[i], y[i + 1]
            out.append(l[i] + 0.5 * (y0 - y2) / (y0 - 2 * y1 + y2) * (l[i + 1] - l[i]))
    return np.array(out[:n])
for name, col, key in (('TT', 0, 'Dl'), ('EE', 1, 'Dl_EE'), ('TE+', 3, 'Dl_TE'), ('TE-', 3, 'Dl_TE')):
    sg = -1 if name == 'TE-' else 1
    a = peaks(ls, sg * d[key], 50, 1400); b = peaks(L.astype(float), sg * cl[:, col], 50, 1400)
    n = min(len(a), len(b))
    print(f"  {name:>4} instrument {np.round(a[:n], 1)}\n  {'':>4} CAMB       {np.round(b[:n], 1)}\n  {'':>4} diff       {np.round(a[:n] - b[:n], 1)}")
