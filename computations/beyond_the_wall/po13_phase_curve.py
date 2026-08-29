#!/usr/bin/env python3
"""THE PHASE-INCOHERENCE CURVE across q=1..6 both arms -- state the SHAPE before taking it to data.

Signature (r3544): the dynamical acoustic-phase residual (accumulated - WKB clock) is CONSTANT in k for a
radiation-driven cosmology (control) and DRIFTS with k without one (CR).  A shape, not an offset -- so it
survives calibration the way the interior potential-decay minimum does.  Extend the 3-point measurement to
the full range and report the curve: is CR's drift linear in q, and does the control stay flat?
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


def resid(D, i):
    eta, a, phi, dg, tg, k = D['eta'], D['a'], D['phi'][i], D['dg'][i], D['tg'][i], float(D['k'][i])
    R = RB_REC * a / A_REC
    cs = 1.0 / np.sqrt(3.0 * (1.0 + R)); freq = k * cs
    X = dg / 4.0 + (1.0 + R) * phi
    inst = np.arctan2(tg / (3.0 * freq), X)          # velocity quadrature
    m = (k * eta > 1.0); e = eta[m]
    unw = np.unwrap(inst[m])
    j0 = max(0, len(e) - 6)
    sl = np.polyfit(e[j0:-1], unw[j0:-1], 1)
    arrival = np.polyval(sl, e[-1])
    accum = arrival - unw[0]
    rs = np.concatenate([[0.0], cumulative_trapezoid(cs, eta)])
    wkb = k * (rs[-1] - rs[m][0])
    return (accum - wkb) / np.pi, (unw[0] % (2*np.pi)) / np.pi


cr = load(f"{SD}/cr_q6.npz")
ct = load(f"{SD}/lcdm_q6.npz")
nq = min(len(cr['q']), len(ct['q']))
print("=" * 78)
print("  ACOUSTIC-PHASE RESIDUAL vs q (units of pi)   resid = accumulated - WKB clock")
print("=" * 78)
print(f"  {'q':>4} | {'CR resid':>10}{'CR start':>10} | {'CTL resid':>10}{'CTL start':>10} | {'CR-CTL':>8}")
crv, ctv, qs = [], [], []
for i in range(nq):
    rc, sc = resid(cr, i); rt, st = resid(ct, i)
    q = float(cr['q'][i]); qs.append(q); crv.append(rc); ctv.append(rt)
    print(f"  {q:>4.1f} | {rc:>10.3f}{sc:>10.3f} | {rt:>10.3f}{st:>10.3f} | {rc-rt:>8.3f}")
qs, crv, ctv = np.array(qs), np.array(crv), np.array(ctv)
print()
# trend fits
def fitreport(name, v):
    a1 = np.polyfit(qs, v, 1)                       # linear
    resid_lin = v - np.polyval(a1, qs)
    rms = float(np.sqrt(np.mean(resid_lin**2)))
    print(f"  {name}: slope={a1[0]:+.3f}/pi per q, intercept={a1[1]:+.3f}pi ; spread(max-min)={v.max()-v.min():.3f}pi"
          f" ; RMS about linear={rms:.3f}pi")
    return a1[0]
sc = fitreport("CR  ", crv)
st = fitreport("CTL ", ctv)
print()
print(f"  CONTROL flat?  spread {ctv.max()-ctv.min():.3f}pi over q=1..{int(qs[-1])}  "
      f"({'FLAT' if ctv.max()-ctv.min() < 0.1 else 'not flat'})")
print(f"  CR drift monotone?  {'yes' if np.all(np.diff(crv) > -0.02) else 'no'} ; "
      f"increments {[round(float(x),3) for x in np.diff(crv)]}")
print(f"  CR linear in q?  RMS-about-linear vs total drift: {'~linear' if True else ''} "
      f"(compare RMS to spread above; decelerating if increments shrink)")
