#!/usr/bin/env python3
"""r7639+cc66: 70's own-comb carry, GENERALISED TO ALL FOUR OF THE STEP RECEIPT'S READINGS.

`r7637+70`'s `own_comb.band_excess_own` carries the arm onto the control's comb coordinate before the
seven bands are cut, which removes the beat 69's ruling names.  Its envelope is the retention law's
running arithmetic MEAN, lifted unchanged -- and that is exactly ONE of the four readings the step
receipt uses to show that the step is the excess's and not the estimator's.  The other three are a
running MEDIAN, a Savitzky-Golay fit, and a reading that needs no envelope at all (the peak-to-trough
depths between consecutive extrema).

** THE CARRY IS ABOUT THE ABSCISSA AND THE WINDOW WIDTH, NOT ABOUT THE KIND OF ENVELOPE. **  It maps
the arm's x onto u = T_c (x / T_a + dphi / 2pi) and widens the arm's envelope window to one of ITS OWN
periods, T_a / T_c.  Neither step mentions how the envelope is estimated, so it generalises to all
four, and the depths reading carries by mapping the extrema's own q.  That generalisation is this
seat's; the combs, the phase fit and the carry are 70's.

** VERIFIED THE WAY 70 VERIFIED THEIRS. **  Two checks, both run by `main()`:
  * REPRODUCTION -- the mean reading returns `r7637+70`'s own-comb row on the arm of record to the
    digits that result prints: +0.0295 +0.0595 +0.0610 +0.0639 +0.0777 +0.0728 +0.0795, step -0.0396,
    rise +0.0061.  An instrument that runs is not an instrument that measures, so it is checked
    against a result computed elsewhere before it is used.
  * REDUCTION -- with T_a = T_c and dphi = 0 the carry must BE the shared statistic.  Fed the control
    against itself, all four readings return every band at zero (0.0, 2.2e-16, 2.2e-16, 0.0).

Run it to reproduce `own_comb_kinds.txt`.  Writes nothing.
"""
import os
import sys

import numpy as np
from scipy.signal import argrelextrema, savgol_filter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7637_70_own_comb_statistic'))
import own_comb as OC                                                      # noqa: E402

QE = np.round(np.arange(0.85, 5.75 + 1e-9, 0.70), 10)
ARM_OF_RECORD = 'r6941_fine_cr_leafrec1'
CONTROL = 'r6941_fine_lcdm'
KINDS = ('mean', 'median', 'savgol')


def fine(tag):
    """one bank on q = l / l_A, the step receipt's abscissa"""
    d = np.load(os.path.join(SP, tag + '.npz'))
    return d['ls'].astype(float) / float(d['l_A']), d['Dl']


def envelope(x, y, win, kind):
    """the step receipt's three envelope kinds, unchanged, with the window as an argument"""
    if kind == 'savgol':
        n = int(round(win / np.median(np.diff(x))))
        return savgol_filter(y, n + (n + 1) % 2, 2, mode='nearest')
    e = np.empty_like(y, dtype=float)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m]) if kind == 'mean' else np.median(y[m])
    return e


def _rms(xs, o, a, b):
    return float(np.std(np.interp(np.linspace(a, b, 400), xs, o)))


def _combs(banks):
    P = {t: OC.comb(*banks[t])[1:] for t in banks}
    Tc, pc, _ = P['lcdm']
    Ta, pa, _ = P['cr']
    return Tc, pc, Ta, pa, (pa - pc + np.pi) % (2 * np.pi) - np.pi


def band_excess_own_kind(banks, kind, QE=QE):
    """70's carry with the step receipt's envelope KIND.  `kind='mean'` is 70's own function."""
    Tc, pc, Ta, pa, dphi = _combs(banks)
    xc, yc = banks['lcdm']
    xa, ya = banks['cr']
    ec = envelope(xc, yc, 1.0, kind)
    ea = envelope(xa, ya, Ta / Tc, kind)                   # one of the ARM's own periods
    oc, oa = (yc - ec) / ec, (ya - ea) / ea
    ua = Tc * (xa / Ta + dphi / (2 * np.pi))               # the arm on the control's comb coordinate
    Rc = np.array([_rms(xc, oc, a, b) for a, b in zip(QE[:-1], QE[1:])])
    Ra = np.array([_rms(ua, oa, a, b) for a, b in zip(QE[:-1], QE[1:])])
    return Ra / Rc - 1.0


def band_excess_own_depths(banks, QE=QE):
    """the envelope-free reading, carried: the extrema's own q is mapped, nothing is windowed"""
    Tc, pc, Ta, pa, dphi = _combs(banks)
    got = {}
    for t, (x, y) in banks.items():
        e = np.sort(np.concatenate([argrelextrema(y, np.greater, order=20)[0],
                                    argrelextrema(y, np.less, order=20)[0]]))
        q = 0.5 * (x[e[:-1]] + x[e[1:]])
        d = np.abs(y[e[1:]] - y[e[:-1]]) / (y[e[1:]] + y[e[:-1]])
        got[t] = (Tc * (q / Ta + dphi / (2 * np.pi)) if t == 'cr' else q, d)
    qa, da = got['cr']
    qc, dc = got['lcdm']
    return np.array([da[(qa >= a) & (qa < b)].mean() / dc[(qc >= a) & (qc < b)].mean() - 1.0
                     for a, b in zip(QE[:-1], QE[1:])])


def all_four(banks, QE=QE):
    """{kind: per-band excess} for all four readings, every one carried"""
    out = {k: band_excess_own_kind(banks, k, QE) for k in KINDS}
    out['none'] = band_excess_own_depths(banks, QE)
    return out


def ratio_step(E):
    """the step receipt's OWN step: band 1 as a RATIO to the mean of bands 2-7, not 70's difference"""
    return float(E[0] / E[1:].mean())


def main():
    banks = {'lcdm': fine(CONTROL), 'cr': fine(ARM_OF_RECORD)}
    Tc, pc, Ta, pa, dphi = _combs(banks)
    print("THE FOUR READINGS ON THE ARM OF RECORD, EVERY ONE CARRIED ONTO THE CONTROL'S COMB")
    print(f"  {CONTROL} against {ARM_OF_RECORD}")
    print(f"  combs: control T {Tc:.4f} phi {pc:.3f};  arm T {Ta:.4f} phi {pa:.3f};  dphi {dphi:+.4f}\n")
    F = all_four(banks)
    for k in KINDS + ('none',):
        E = F[k]
        extra = (f"   70-step {OC.step(E):+.4f}  rise {OC.rise(E, QE):+.4f}" if k != 'none' else "")
        print(f"  {k:8s} " + '  '.join(f'{v:+.4f}' for v in E)
              + f"   ratio-step {ratio_step(E):.3f}{extra}")
    print(f"\n  max ratio-step {max(ratio_step(F[k]) for k in F):.3f}  "
          f"-- the step receipt asserts < 0.7")
    RA = F['none']
    print(f"  envelope-free band 1 {RA[0]:+.4f} (it asserts |.| < 0.01), "
          f"bands 2-7 mean {RA[1:].mean():+.4f} (it asserts > 0.04)")

    print("\n** REPRODUCTION: the mean reading against `r7637+70`'s own-comb row on the arm of record **")
    ROW = np.array([0.0295, 0.0595, 0.0610, 0.0639, 0.0777, 0.0728, 0.0795])
    E = F['mean']
    print("  70  " + '  '.join(f'{v:+.4f}' for v in ROW) + "   step -0.0396  rise +0.0061")
    print("  here" + '  '.join(f'{v:+.4f}' for v in E)
          + f"   step {OC.step(E):+.4f}  rise {OC.rise(E, QE):+.4f}")
    ok = (float(np.max(np.abs(np.round(E, 4) - ROW))) == 0.0
          and round(OC.step(E), 4) == -0.0396 and round(OC.rise(E, QE), 4) == 0.0061)
    print(f"  -> {'REPRODUCED to every digit that result prints' if ok else 'DOES NOT REPRODUCE'}")

    print("\n** REDUCTION: the control against ITSELF -- T_a = T_c and dphi = 0, so the carry must BE the")
    print("   shared statistic and every band must be zero **")
    same = {'lcdm': fine(CONTROL), 'cr': fine(CONTROL)}
    worst = 0.0
    for k, E in all_four(same).items():
        m = float(np.max(np.abs(E)))
        worst = max(worst, m)
        print(f"  {k:8s} max |band| = {m:.3e}")
    print(f"  -> {'REDUCES' if worst < 1e-12 else 'DOES NOT REDUCE'} "
          f"(worst {worst:.1e}, floating-point and not a difference)")
    return 0 if (ok and worst < 1e-12) else 1


if __name__ == '__main__':
    sys.exit(main())
