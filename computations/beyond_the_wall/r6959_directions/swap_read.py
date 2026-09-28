#!/usr/bin/env python3
"""r6959 ⓵ᵇ/⓵ᶜ -- read the swap: the contrast, the comb and the depths, against the prediction.

Usage: swap_read.py [/tmp/n66/r6959]   (expects eta/prediction.json and swap/*.npz already summed)
"""
import json
import os
import sys

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.signal import argrelextrema

ROOT = '/home/user/shadow-of-existence'
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                             # noqa: E402

D = sys.argv[1] if len(sys.argv) > 1 else '/tmp/n66/r6959'
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
PR = json.load(open(os.path.join(D, 'eta', 'prediction.json')))
ED = np.arange(0.85, 5.76, 0.7)
QC = 0.5 * (ED[:-1] + ED[1:])
LF = np.arange(100.0, 1300.0, 1.0)
TR = np.array([396.0, 674.0, 994.0])
PK = np.array([238.0, 537.0, 828.0])
ANCH = np.array([220.6, 538.1, 809.8, 1121.9])       # the sky's own four, PO-47
LC, FAC = CS.bin_center_and_fac()


def env_a(x, y, win=1.0):
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m])
    return e


def osc(x, y, win=1.0):
    e = env_a(x, y, win)
    return (y - e) / e


def band_std(q, o):
    out = []
    for a, b in zip(ED[:-1], ED[1:]):
        x = np.linspace(a, b, 400)
        out.append(float(np.std(np.interp(x, q, o))))
    return np.array(out)


def peaks_sub(ls, Dl, anch, W=40):
    """the anchored parabola at the extremum -- cc66.45's locator, cleared to 0.028 of a multipole"""
    out = []
    for a in anch:
        m = (ls >= a - W) & (ls <= a + W)
        x, y = ls[m].astype(float), Dl[m]
        i = int(np.argmax(y))
        if 0 < i < len(x) - 1:
            d = 0.5 * (y[i - 1] - y[i + 1]) / (y[i - 1] - 2 * y[i] + y[i + 1])
            out.append(float(x[i] + d * (x[1] - x[0])))
        else:
            out.append(float(x[i]))
    return np.array(out)


def spl(Db):
    m = (LC >= 100) & np.isfinite(Db)
    return CubicSpline(LC[m], Db[m])(LF)


def anchored(o, anch, W, kind):
    out = []
    for a in anch:
        k = (LF >= a - W) & (LF <= a + W)
        out.append(float(abs(np.min(o[k]))) if kind == 'min' else float(np.max(o[k])))
    return np.array(out)


def load(p):
    return np.load(p)


B = {t: load(os.path.join(SP, f'r6941_fine_{t}.npz')) for t in ('lcdm', 'cr')}
S = {}
for nm, f in (('swap_lcdm', 'r6959_swap_lcdm.npz'), ('big_lcdm', 'r6959_big_lcdm.npz')):
    p = os.path.join(SP, f)
    if os.path.exists(p):
        S[nm] = load(p)
    elif os.path.exists(os.path.join(D, 'swap', f'{nm}.npz')):
        S[nm] = load(os.path.join(D, 'swap', f'{nm}.npz'))

print("=" * 100)
print("r6959 ⓵ᵇ -- THE SWAP, AGAINST THE PREDICTION MADE BEFORE IT RAN")
print("=" * 100)
Q = {t: B[t]['ls'].astype(float) / float(B[t]['l_A']) for t in B}
O = {t: osc(Q[t], B[t]['Dl']) for t in B}
C0 = {t: band_std(Q[t], O[t]) for t in B}
print("  baseline band contrast (r6941_fine_*):")
print("    lcdm " + "  ".join(f"{x:.6f}" for x in C0['lcdm']))
print("    cr   " + "  ".join(f"{x:.6f}" for x in C0['cr']))
print("    ratio" + "  ".join(f"{a / b:.5f}" for a, b in zip(C0['cr'], C0['lcdm'])))

for nm, arm, pred in (('swap_lcdm', 'lcdm', np.array(PR['f'])),
                      ('big_lcdm', 'lcdm', np.array(PR['f_big']))):
    if nm not in S:
        print(f"\n  ({nm} not on disk yet)")
        continue
    d = S[nm]
    q = d['ls'].astype(float) / float(d['l_A'])
    o = osc(q, d['Dl'])
    c = band_std(q, o)
    print(f"\n  {nm}: l_A {float(d['l_A']):.3f} against the untapered {float(B[arm]['l_A']):.3f}")
    print("    band    own-baseline ratio   predicted f   [f, f^2]          in interval?")
    for b in range(len(QC)):
        r = c[b] / C0[arm][b]
        lo, hi = sorted((pred[b], pred[b] ** 2))
        print(f"    q={QC[b]:.2f}   {r:.5f}            {pred[b]:.5f}     "
              f"[{lo:.5f}, {hi:.5f}]   {'YES' if lo - 1e-9 <= r <= hi + 1e-9 else 'no'}")
    if arm == 'lcdm':
        print("    and the EXCESS after the swap -- cr against the tapered control:")
        print("    " + "  ".join(f"{a / b:.5f}" for a, b in zip(C0['cr'], c)))

print("\n" + "=" * 100)
print("⓵ᶜ R4 -- WHAT THE SWAP DOES TO THE COMB AND TO THE DEPTHS")
print("=" * 100)
for nm, arm in (('swap_lcdm', 'lcdm'), ('big_lcdm', 'lcdm')):
    if nm not in S:
        continue
    d = S[nm]
    p0 = peaks_sub(B[arm]['ls'].astype(float), B[arm]['Dl'], ANCH)
    p1 = peaks_sub(d['ls'].astype(float), d['Dl'], ANCH)
    print(f"\n  {nm}: peak positions  " + "  ".join(f"{x:.3f}" for x in p1))
    print(f"    untapered         " + "  ".join(f"{x:.3f}" for x in p0))
    print(f"    moved by          " + "  ".join(f"{a - b:+.3f}" for a, b in zip(p1, p0))
          + "   (sky's locating widths 1.0/1.2/1.6/2.36)")
    print(f"    l_1/l_A {p1[0] / float(d['l_A']):.6f} against {p0[0] / float(B[arm]['l_A']):.6f}"
          f"   (moved {p1[0] / float(d['l_A']) - p0[0] / float(B[arm]['l_A']):+.6f})")
    b0 = CS.bin_spectrum(B[arm]['ls'].astype(float), B[arm]['Dl'])
    b1 = CS.bin_spectrum(d['ls'].astype(float), d['Dl'])
    for lab, bb in (('untapered', b0), ('tapered  ', b1)):
        oo = osc(LF / 301.6, spl(bb))
        print(f"    {lab}: anchored trough depths " + "  ".join(
            f"{x:.5f}" for x in anchored(oo, TR, 40, 'min'))
            + "   peaks " + "  ".join(f"{x:.5f}" for x in anchored(oo, PK, 40, 'max')))
