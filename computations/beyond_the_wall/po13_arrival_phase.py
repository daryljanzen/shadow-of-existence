#!/usr/bin/env python3
"""ARRIVAL PHASE AT RECOMBINATION -- hardened.  Two independent quadratures, endpoint by extrapolation
from accurate interior points (not a one-sided endpoint derivative).

Oscillator variable X = Theta_0 + (1+R)Psi = dg/4 + (1+R)phi (oscillates about 0).
Quadrature A: s_A = (dX/deta)/(k c_s)              [numerical derivative, central/interior]
Quadrature B: s_B = -tg / (3 k c_s)                [the photon velocity itself: dX/deta ~ -(1/3)tg,
                                                     so -tg/(3 k c_s) = the sin component, no numeric deriv]
Instantaneous phase = atan2(-s, X).  Unwrap over the sub-horizon window; the phase at eta_rec is read by
LINEAR EXTRAPOLATION from the last few interior points (slope = local frequency, robust), avoiding the
endpoint-derivative artifact.  Report both quadratures; agreement = trustworthy.
"""
import sys, numpy as np
from scipy.integrate import cumulative_trapezoid

SD = sys.argv[1] if len(sys.argv) > 1 else '.'
OMBH2, Z_REC = 0.0224, 1089.9
A_REC = 1.0 / (1.0 + Z_REC)
RB_REC = 31500 * OMBH2 / (2.7255 / 2.7) ** 4 / (1 + Z_REC)


def load(f):
    d = np.load(f)
    return dict(eta=d['eta'], a=d['a'], phi=d['phi'], dg=d['dg'], tg=d['tg'],
                q=d['qpk'], k=d['kpk'], erec=float(d['eta_rec']))


def phases(D, i):
    eta, a, phi, dg, tg, k = D['eta'], D['a'], D['phi'][i], D['dg'][i], D['tg'][i], float(D['k'][i])
    R = RB_REC * a / A_REC
    cs = 1.0 / np.sqrt(3.0 * (1.0 + R))
    freq = k * cs
    X = dg / 4.0 + (1.0 + R) * phi
    m = (k * eta > 1.0)
    e = eta[m]
    out = {}
    for tag, s in (('A', np.gradient(X, eta) / freq), ('B', -tg / (3.0 * freq))):
        inst = np.arctan2(-s[m], X[m])
        unw = np.unwrap(inst)
        # extrapolate unwrapped phase to eta_rec (=e[-1]) from interior points [-6:-1], slope=freq
        j0, j1 = max(0, len(e) - 6), len(e) - 1
        sl = np.polyfit(e[j0:j1], unw[j0:j1], 1)
        ph_rec = np.polyval(sl, e[-1])
        out[tag] = dict(wrapped=(ph_rec % (2 * np.pi)) / np.pi, accum=(unw[-1] - unw[0]) / np.pi,
                        slope_fit=sl[0], freq_end=float(freq[m][-1]))
    rs = np.concatenate([[0.0], cumulative_trapezoid(cs, eta)])
    out['krs'] = float(k * rs[-1]) / np.pi
    return out


cr = load(f"{SD}/cr_wi.npz")
ct = load(f"{SD}/lcdm_wi.npz")
print("=" * 88)
print("  ARRIVAL PHASE (hardened)  wrapped phase/pi at eta_rec ; 0=one extremum, 1=the other")
print("=" * 88)
print(f"  {'peak(q)':>7} | {'CR-A':>7}{'CR-B':>7}{'CTL-A':>7}{'CTL-B':>7} | {'DIFF-A/pi':>10}{'DIFF-B/pi':>10}"
      f" | {'CRaccum':>8}{'CTLaccum':>9}{'krs CR/CT':>11}")


def wrapdiff(a, b):
    return ((a - b + 1) % 2) - 1     # in units of pi already


for i in range(3):
    mc, mt = phases(cr, i), phases(ct, i)
    dA = wrapdiff(mc['A']['wrapped'], mt['A']['wrapped'])
    dB = wrapdiff(mc['B']['wrapped'], mt['B']['wrapped'])
    print(f"  {float(cr['q'][i]):>7.2f} | {mc['A']['wrapped']:>7.3f}{mc['B']['wrapped']:>7.3f}"
          f"{mt['A']['wrapped']:>7.3f}{mt['B']['wrapped']:>7.3f} | {dA:>10.3f}{dB:>10.3f} |"
          f"{mc['A']['accum']:>8.3f}{mt['A']['accum']:>9.3f}  {mc['krs']:>4.2f}/{mt['krs']:>4.2f}")
print()
print("  A and B agreeing => the arrival phase is real, not a numeric artifact.")
print("  |DIFF| ~ 0  => phases MATCH -> even peak suppressed at FIXED phase -> transfer/projection.")
print("  |DIFF| != 0 => CR arrives at a different cycle point -> parity is TIMING (IC/phase).")
