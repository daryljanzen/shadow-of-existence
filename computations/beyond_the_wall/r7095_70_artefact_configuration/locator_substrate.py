"""r7095 (70) Q2 -- the two registered locator validations, re-run unchanged on a RE-DERIVABLE substrate.

Both receipts validate the sub-bin peak locator on `spectra/cc66_cr_x_lstep1.npz`, which has no command in the
repository and fingerprints to the superseded stacking ruler (l_A = 172.841).  The candidate is
`spectra/r6941_fine_cr.npz`: LSTEP=1, ell 100-1999, the reported model B, launched by r6941_directions/launch.sh.
The locator functions and both checks are copied verbatim from the two receipts; only the substrate changes.
"""
import os
import numpy as np
from scipy.signal import argrelextrema

SP = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'spectra')


def peaks_raw(ls, Dl, n=4, order=3):
    return [float(ls[i]) for i in argrelextrema(Dl, np.greater, order=order)[0][:n]]


def peaks_sub(ls, Dl, n=4, order=3):
    out = []
    for i in argrelextrema(Dl, np.greater, order=order)[0][:n]:
        if i < 1 or i > len(ls) - 2:
            out.append(float(ls[i]))
            continue
        y0, y1, y2 = Dl[i - 1], Dl[i], Dl[i + 1]
        den = y0 - 2 * y1 + y2
        off = 0.5 * (y0 - y2) / den if den != 0 else 0.0
        out.append(float(ls[i] + off * (ls[i + 1] - ls[i])))
    return out


for name in ('cc66_cr_x_lstep1', 'r6941_fine_cr'):
    z = np.load(os.path.join(SP, name + '.npz'))
    l1, D1 = np.asarray(z['ls'], float), np.asarray(z['Dl'], float)
    print(f'== {name}   (l_A {float(z["l_A"]):.3f}, ell {l1[0]:.0f}-{l1[-1]:.0f}, spacing {l1[1]-l1[0]:.0f})')
    # --- the refit receipt's (a): native sub-bin peaks at order 20; decimate x2, x4, x8
    native = peaks_sub(l1, D1, order=20)
    er = es = 0.0
    for st in (2, 4, 8):
        ls, Ds = l1[::st], D1[::st]
        o = max(3, 20 // st)
        r, s = peaks_raw(ls, Ds, order=o), peaks_sub(ls, Ds, order=o)
        e_r = max(abs(a - b) for a, b in zip(r, native))
        e_s = max(abs(a - b) for a, b in zip(s, native))
        er, es = max(er, e_r), max(es, e_s)
        print(f'   refit (a)  x{st}: raw errs {e_r:5.2f}, refined {e_s:5.3f}')
    ok_a = er > 2.0 and es < 0.2
    print(f'   refit receipt\'s check  "raw errs by ~3, refined < 0.2": raw {er:.2f}, refined {es:.3f} -> {"HOLDS" if ok_a else "FAILS"}')
    # --- the comb receipt's PART 3: full grid against the LSTEP=8 grid (100, 108, ...)
    m8 = np.isin(l1, np.arange(100, 2000, 8))
    pf, p8 = peaks_sub(l1, D1), peaks_sub(l1[m8], D1[m8])
    d1 = abs(pf[0] - p8[0])
    dw = max(abs(a - b) for a, b in zip(pf, p8))
    ok_c = d1 < 0.01 and dw < 0.2
    print(f'   comb receipt\'s check  "l_1 to < 0.01, worst of four < 0.2": l_1 {d1:.4f}, worst {dw:.3f} -> {"HOLDS" if ok_c else "FAILS"}')
    print(f'      fine {[round(x, 3) for x in pf]}   coarse {[round(x, 3) for x in p8]}')
