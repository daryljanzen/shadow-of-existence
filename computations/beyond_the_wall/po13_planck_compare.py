#!/usr/bin/env python3
"""THREE CURVES, decomposed by PARITY: sky / control / CR peak-position residuals under floated l_A.

The sky's spacings ALTERNATE (317.5,271.7,338.0,299.0,332.2) -- the compression/rarefaction physics. Under
a linear fit l_n=A n+B that leaves a parity ZIGZAG in the residual, NOT a smooth curvature. A zigzag and a
smooth curve are different shapes, and a quadratic coefficient partly absorbs a zigzag -- so the coefficient
alone cannot tell them apart (Daryl). Decompose every residual BY CONSTRUCTION into:
  ALT   = the part that flips sign with peak parity  (projection onto (-1)^n)
  SMOOTH= what remains
The uniform-comb prediction: CR's ALT should be small where the sky's and control's ALT are large. The
~0.08pi 'curvature' from before is the SMOOTH part and may be a separate thing.

Three checks: (1) control must REPRODUCE the sky (not merely be flat); (2) discriminant is |CR-sky| vs
|control-sky|, done per-component; (3) report WITH and WITHOUT the q=5,6 damping tail.  RAW table first,
no fit.  Numbers before interpretation.
"""
import sys, numpy as np
from scipy.signal import argrelextrema

SD = sys.argv[1] if len(sys.argv) > 1 else '.'
SKY = np.array([220.6, 538.1, 809.8, 1147.8, 1446.8, 1779.0])       # Planck 2018 TT, Table 5
SKY_E = np.array([0.6, 1.3, 1.0, 2.3, 1.6, 3.0])


def peaks_from(f, n=6):
    """sub-grid peak positions by parabolic interpolation (remove the LSTEP grid quantization)."""
    d = np.load(f); ls, Dl = d['ls'], d['Dl']
    idx = argrelextrema(Dl, np.greater, order=3)[0][:n]
    out = []
    for i in idx:
        if 0 < i < len(ls) - 1:
            y0, y1, y2 = Dl[i - 1], Dl[i], Dl[i + 1]
            den = (y0 - 2 * y1 + y2)
            dx = 0.5 * (y0 - y2) / den if den != 0 else 0.0
            out.append(float(ls[i] + dx * (ls[i + 1] - ls[i])))
        else:
            out.append(float(ls[i]))
    return np.array(out)


def decomp(p, sig=None):
    N = len(p); n = np.arange(1, N + 1); w = 1.0 / sig**2 if sig is not None else np.ones(N)
    M = np.vstack([n, np.ones(N)]).T
    A, B = np.linalg.lstsq(M * w[:, None], w * p, rcond=None)[0]
    res = (p - (A * n + B)) / A                      # residual in units of pi (spacing = pi)
    par = (-1.0) ** n
    a_alt = float(np.mean(par * res))                # amplitude of the (-1)^n parity component
    alt = a_alt * par
    smooth = res - alt
    return dict(A=A, res=res, alt_amp=abs(a_alt), alt=alt, smooth=smooth,
                smooth_rms=float(np.sqrt(np.mean(smooth**2))),
                smooth_c2=float(np.polyfit(n, smooth, 2)[0]), rms=float(np.sqrt(np.mean(res**2))))


def sky_err(N, key):
    v = []
    for _ in range(30000):
        d = decomp(SKY[:N] + np.random.randn(N) * SKY_E[:N], SKY_E[:N]); v.append(d[key])
    return float(np.std(v))


def spac(p):
    return [round(float(p[i + 1] - p[i]), 1) for i in range(len(p) - 1)]


# ---------- RAW TABLE FIRST, NO FIT ----------
print("=" * 86)
print("  RAW PEAK POSITIONS & SPACINGS -- sky / control / CR -- NO FIT")
print("=" * 86)
try:
    CTP = peaks_from(f"{SD}/lcdm_p6.npz"); CRP = peaks_from(f"{SD}/cr_p6.npz")
except FileNotFoundError as e:
    print(f"  waiting on spectra: {e}"); sys.exit(0)
for nm, p in (("SKY(Planck)", SKY), ("CONTROL", CTP), ("CR", CRP)):
    print(f"  {nm:11s} peaks={[round(float(x),1) for x in p]}")
    print(f"  {'':11s} spac ={spac(p)}")
print("  Direct read: sky spacings ALTERNATE. Does control alternate the same, and CR go REGULAR?")


def block(tag, N):
    print("\n" + "=" * 86)
    print(f"  PARITY-DECOMPOSED RESIDUALS (floated l_A) -- {tag}  q=1..{N}")
    print("=" * 86)
    s = decomp(SKY[:N], SKY_E[:N]); c = decomp(CTP[:N]); r = decomp(CRP[:N])
    ea, es = sky_err(N, 'alt_amp'), sky_err(N, 'smooth_rms')
    print(f"  {'arm':8s}{'ALT amp':>10}{'SMOOTH rms':>12}{'smooth c2':>11}   residual(pi)")
    for nm, o in (("SKY", s), ("CONTROL", c), ("CR", r)):
        print(f"  {nm:8s}{o['alt_amp']:>10.3f}{o['smooth_rms']:>12.3f}{o['smooth_c2']:>+11.4f}   "
              f"{[round(x,3) for x in o['res']]}")
    print(f"  sky err (MC): ALT +/-{ea:.3f}   SMOOTH rms +/-{es:.3f}")
    print(f"  -- (1) CALIBRATION: control ALT {c['alt_amp']:.3f} vs sky {s['alt_amp']:.3f}+/-{ea:.3f}"
          f"  -> {abs(c['alt_amp']-s['alt_amp'])/ea:.1f}sig ; "
          f"control must REPRODUCE the sky's ALT, not be flat")
    print(f"  -- (2) DISCRIMINANT (parity): CR ALT {r['alt_amp']:.3f}  sky {s['alt_amp']:.3f}  "
          f"control {c['alt_amp']:.3f}")
    print(f"       CR-ALT is {r['alt_amp']/max(s['alt_amp'],1e-9):.2f}x the sky's "
          f"({(s['alt_amp']-r['alt_amp'])/ea:+.1f}sig below sky) "
          f"-- uniform-comb predicts CR-ALT ~ 0 where sky/control large")
    print(f"       SMOOTH: CR {r['smooth_rms']:.3f}  sky {s['smooth_rms']:.3f}  control {c['smooth_rms']:.3f}"
          f"  (the ~0.08pi 'curvature' lives here, a SEPARATE question)")


block("WITH damping tail", 6)
block("NO TAIL (drop q5,q6)", 4)
