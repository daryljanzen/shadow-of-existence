#!/usr/bin/env python3
"""q=1..3 positional-parity ALT across CR compositions -- is the r3548 0.111 CR's or GSRC=1's?
ALT = |mean((-1)^n * residual)| after a floated-l_A linear fit to the first 3 peak positions (sub-grid).
Result (r3549): SWINGS with the source -- GSRC=0 -> 0.007, GSRC=1 -> ~0.11 (flat/seam/drag stable);
neither determined composition reproduces the sky's 0.028 (control 0.029)."""
import sys, numpy as np
from scipy.signal import argrelextrema
SKY = np.array([220.6, 538.1, 809.8]); E = np.array([0.6, 1.3, 1.0])
def peaks(f, n=3):
    d = np.load(f); ls, Dl = d['ls'], d['Dl']; idx = argrelextrema(Dl, np.greater, order=3)[0][:n]; o = []
    for i in idx:
        y0, y1, y2 = Dl[i-1], Dl[i], Dl[i+1]; den = y0 - 2*y1 + y2
        o.append(float(ls[i] + (0.5*(y0-y2)/den if den else 0)*(ls[i+1]-ls[i])))
    return np.array(o)
def alt(p, sig=None):
    n = np.arange(1, len(p)+1); w = 1/sig**2 if sig is not None else np.ones(len(p))
    M = np.vstack([n, np.ones(len(p))]).T; A, B = np.linalg.lstsq(M*w[:, None], w*p, rcond=None)[0]
    return abs(float(np.mean((-1.)**n * (p-(A*n+B))/A)))
SD = sys.argv[1] if len(sys.argv) > 1 else '.'
print(f"SKY {alt(SKY,E):.3f}  CONTROL {alt(peaks(SD+'/lcdm_p6.npz')):.3f}")
for tag, f in (("GSRC=1 flat", "cr_p6.npz"), ("GSRC=1 drag", "cr_d1.npz"),
               ("GSRC=1 seam", "cr_seam.npz"), ("GSRC=0", "cr_gsrc0.npz")):
    print(f"  {tag:12s} {alt(peaks(SD+'/'+f)):.3f}")
