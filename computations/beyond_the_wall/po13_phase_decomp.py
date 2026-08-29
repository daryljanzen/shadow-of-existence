#!/usr/bin/env python3
"""IS THE PHASE DRIFT DYNAMICAL OR AN IC ARTIFACT?  arrival = start + accumulated.

For the 3 peak modes both arms, decompose the arrival phase (r3543) into:
  - START phase at horizon entry (k eta = 1, first moment the oscillation phase is defined),
  - ACCUMULATED phase entry->recombination (unwrapped instantaneous phase swept),
  - WKB clock over the same window = k * INT c_s deta,
  - DYNAMICAL RESIDUAL = accumulated - WKB  (the driving/gravity phase shift beyond the sound clock).

The coherence question: the control's odd peaks (q=1,3) arrive at the SAME phase.  Is that because their
START phases are arranged that way (an IC), or because the accumulated/residual is LOCKED across scales
(dynamical, maintained by radiation driving)?
  - control residual ~equal across odd modes AND CR's drifts  -> coherence is DYNAMICAL; no IC supplies it.
  - CR accumulated ~agree and only START phases differ         -> it IS an IC; a seam phase reset is worth it.
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


def decomp(D, i):
    eta, a, phi, dg, tg, k = D['eta'], D['a'], D['phi'][i], D['dg'][i], D['tg'][i], float(D['k'][i])
    R = RB_REC * a / A_REC
    cs = 1.0 / np.sqrt(3.0 * (1.0 + R))
    freq = k * cs
    X = dg / 4.0 + (1.0 + R) * phi
    inst = np.arctan2(-(-tg / (3.0 * freq)), X)      # quadrature B (velocity; no numeric deriv)
    m = (k * eta > 1.0)
    e = eta[m]
    unw = np.unwrap(inst[m])
    start = unw[0]                                    # phase at horizon entry
    # arrival by extrapolation from interior points (slope = freq), as in phase2
    j0, j1 = max(0, len(e) - 6), len(e) - 1
    sl = np.polyfit(e[j0:j1], unw[j0:j1], 1)
    arrival = np.polyval(sl, e[-1])
    accum = arrival - start
    rs = np.concatenate([[0.0], cumulative_trapezoid(cs, eta)])
    wkb = k * (rs[-1] - rs[m][0])                     # WKB phase over the same entry->rec window
    return dict(start=start / np.pi, arrival=(arrival % (2*np.pi)) / np.pi,
                accum=accum / np.pi, wkb=wkb / np.pi, resid=(accum - wkb) / np.pi,
                start_wrap=(start % (2*np.pi)) / np.pi)


cr = load(f"{SD}/cr_wi.npz")
ct = load(f"{SD}/lcdm_wi.npz")
print("=" * 90)
print("  PHASE DECOMPOSITION (units of pi)   arrival = start + accumulated ;  resid = accum - WKB clock")
print("=" * 90)
print(f"  {'arm/q':>8} | {'start(wrap)':>12}{'arrival':>9} | {'accum':>8}{'WKB':>8}{'RESID(dyn)':>12}")
for arm, D in (("CR", cr), ("CTL", ct)):
    for i in range(3):
        r = decomp(D, i)
        print(f"  {arm+' q'+str(i+1):>8} | {r['start_wrap']:>12.3f}{r['arrival']:>9.3f} |"
              f"{r['accum']:>8.3f}{r['wkb']:>8.3f}{r['resid']:>12.3f}")
    print()
# coherence read: compare RESID across odd modes (q1,q3) within each arm
print("  COHERENCE across odd peaks (q1 vs q3):")
for arm, D in (("CTL", ct), ("CR", cr)):
    r1, r3 = decomp(D, 0)['resid'], decomp(D, 2)['resid']
    s1, s3 = decomp(D, 0)['start_wrap'], decomp(D, 2)['start_wrap']
    print(f"   {arm}: dynamical residual q1={r1:.3f} q3={r3:.3f}  (spread {abs(r3-r1):.3f}pi) ;"
          f"  start q1={s1:.3f} q3={s3:.3f} (spread {abs(s3-s1):.3f}pi)")
print()
print("  control resid coherent + CR resid drifts -> DYNAMICAL (radiation locks phase; no IC supplies it).")
print("  CR resid coherent + CR start differs      -> IC question (a seam PHASE reset is worth building).")
