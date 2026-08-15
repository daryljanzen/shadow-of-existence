#!/usr/bin/env python3
r"""S1 -- cc54, PO-10 (56's pin test, routed on restart -- 56's container OOM'd at projection twice):
does the CR arm's peak SPACING follow LATARG? It does, rigidly. Running the CR spectrum with full
projection at LATARG = 280, 301.6, 320 (the fitted acoustic scale l_A = pi D_M / r_s set to each value),
the mean peak spacing Delta_ell = 240, 258, 274 tracks L_A at slope d(Delta_ell)/d(L_A) = 0.85, and
the RATIO Delta_ell / L_A = 0.857, 0.855, 0.856 is CONSTANT to 0.002. So the ~14% spacing deficit
(Delta_ell = 0.856 L_A, against the sky's ~0.98) is a FIXED STRUCTURAL RATIO -- the comb's period
follows the fitted scale rather than sitting where the projection puts it -- NOT an artefact of the
particular LATARG = 301.6. Meanwhile the first peak l_1 = 164, 172, 172 is nearly PINNED while L_A
grows, so l_1 / L_A = 0.586, 0.570, 0.537 DRIFTS: the first-peak OFFSET is a separate phase (PO-7's),
not a scale. The pin test settles 56's question: the spacing deficit is acoustic structure, and the
residual is the phase, not a projection/fit artefact.

** THE TEST. ** LATARG is the corpus's one fitted number (z_onset solved so l_A = pi D_M / r_s hits a
target). Varying it moves r_s (145.91, 135.46, 127.67 for LATARG 280, 301.6, 320) and hence L_A =
LATARG by construction. If the projected comb's spacing FOLLOWS L_A, the deficit is a fixed ratio the
acoustics carry; if the spacing stayed put while L_A moved, the l_A fit would be cosmetic and the
deficit an artefact. Banked spectra: full c54.178 config (HIER=1 BSPLIT=1 ARM=cr NK=600 LMAXL=2000
ETAEND=4000 KBATCH=300) at each LATARG.

** THE NUMBERS (peaks from argrelextrema, first-4-gap mean; scored on the banked spectra). **
      LATARG    L_A     r_s    Delta_ell   Delta_ell/L_A   l_1   l_1/L_A
       280     280    145.91     240          0.857        164    0.586
       301.6   301.6  135.46     258          0.855        172    0.570
       320     320    127.67     274          0.856        172    0.537
  ** Delta_ell/L_A CONSTANT (0.856 +- 0.002), l_1/L_A DRIFTS (l_1 pinned ~170). **

COMPUTES: the CR arm's peak positions, mean spacing and l_1 at three LATARG values, and the slope
d(Delta_ell)/d(L_A) and the constancy of Delta_ell/L_A. ** LATARG 280/301.6/320 brackets the fitted
301.6; the three points are the pin-test scan, not a pinned working point. **

** WHAT THIS RECEIPT ASSERTS. **
  1. THE SPACING FOLLOWS LATARG: Delta_ell/L_A = 0.857/0.855/0.856 is constant to 0.002 and
     d(Delta_ell)/d(L_A) = 0.85 -- the comb's period tracks the fitted scale, so the ~14% spacing
     deficit (0.856 vs the sky's ~0.98) is a FIXED STRUCTURAL RATIO, not an artefact of LATARG=301.6.
  2. THE FIRST-PEAK OFFSET IS A SEPARATE PHASE: l_1 = 164/172/172 is nearly pinned while L_A grows, so
     l_1/L_A = 0.586/0.570/0.537 DRIFTS -- the intercept is a phase (PO-7/L-171), not a scale, which is
     why l_1/L_A moves while Delta_ell/L_A does not.
  3. SO THE DEFICIT IS ACOUSTIC STRUCTURE, NOT A FIT ARTEFACT: the spacing responds to the fitted
     scale (structural), and the residual disagreement with the sky lives in the phase (the offset),
     exactly the scale-vs-phase split L-171 named -- the pin test 56 asked for.

** WHAT IS NOT CLAIMED, stated for reversal. ** NOT a framework verdict (F5): PO-10/PO-7 are the
observer line's; this supplies the pin test's measurement, not a conversion. NOT that 0.856 is derived
here -- it is measured across the scan; whether the acoustic phase that sets it is CR's prediction is
PO-7's, protected. NOT that l_1 is exactly constant -- it moves 164->172 within the step-8 peak
resolution, so "nearly pinned" is the claim, and the DRIFT of l_1/L_A against the CONSTANCY of
Delta_ell/L_A is the signal. NOT that the projection is uniform -- the comb is measured in ell on the
projected spectrum, as the row scores it; the source-k comb is a separate object (the instrument's own
caveat).

** Board lead L-830 (cc54's band); the pin test 56 routed (container-blocked on their side). Informs
L-147 (PO-10), L-171 (PO-7), L-822. Routed to 56. **

Written r2803 (cc54, L-830). Asserts against the banked CR spectra at three LATARG values -- never the
register. Stated for reversal.
"""
import os

import numpy as np
from scipy.signal import argrelextrema

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def measure(fname):
    z = np.load(os.path.join(SPEC, fname))
    ls, Dl = z['ls'], z['Dl']
    LA = float(z['l_A'])
    pk = [int(ls[q]) for q in argrelextrema(Dl, np.greater, order=3)[0]]
    gaps = np.diff(pk)
    dl = float(np.mean(gaps[:4]))
    return LA, dl, pk[0]


def main():
    print()
    print('  S1 -- PO-10 pin test: does the CR arm\'s peak spacing follow LATARG?')
    print()
    runs = [('280', 'L830_cr_lat280.npz'), ('301.6', 'L830_cr_lat302.npz'),
            ('320', 'L830_cr_lat320.npz')]
    LA, DL, L1 = [], [], []
    print(f"    {'LATARG':>7} {'L_A':>7} {'Delta_ell':>10} {'Dl/L_A':>7} {'l_1':>5} {'l_1/L_A':>8}")
    for lat, fn in runs:
        la, dl, l1 = measure(fn)
        LA.append(la); DL.append(dl); L1.append(l1)
        print(f"    {lat:>7} {la:7.1f} {dl:10.1f} {dl/la:7.3f} {l1:5d} {l1/la:8.3f}")
    LA, DL, L1 = np.array(LA), np.array(DL), np.array(L1)

    dl_la = DL / LA
    slope = np.polyfit(LA, DL, 1)[0]
    check(f'THE SPACING FOLLOWS LATARG: Delta_ell/L_A = {[round(float(x),3) for x in dl_la]} is constant to '
          f'{dl_la.max()-dl_la.min():.3f} and d(Delta_ell)/d(L_A) = {slope:.2f} -- the comb\'s period '
          'tracks the fitted scale, so the ~14% spacing deficit (0.856 vs the sky\'s ~0.98) is a FIXED '
          'STRUCTURAL RATIO, not an artefact of LATARG=301.6',
          (dl_la.max() - dl_la.min()) < 0.01 and 0.7 < slope < 1.0)

    l1_la = L1 / LA
    check(f'THE FIRST-PEAK OFFSET IS A SEPARATE PHASE: l_1 = {L1.tolist()} is nearly pinned while L_A '
          f'grows, so l_1/L_A = {[round(float(x),3) for x in l1_la]} DRIFTS (spread '
          f'{l1_la.max()-l1_la.min():.3f}) -- the intercept is a phase (PO-7/L-171), not a scale',
          (l1_la.max() - l1_la.min()) > 0.03 and (L1.max() - L1.min()) < 0.1 * L1.mean())

    check('SO THE DEFICIT IS ACOUSTIC STRUCTURE, NOT A FIT ARTEFACT: the spacing responds to the fitted '
          'scale (Delta_ell/L_A constant) while the residual lives in the phase (l_1/L_A drifts) -- the '
          'scale-vs-phase split L-171 named',
          (dl_la.max() - dl_la.min()) < 0.01 and (l1_la.max() - l1_la.min()) > 0.03)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (the pin test 56 routed): the CR arm\'s peak SPACING FOLLOWS LATARG -- Delta_ell/L_A')
    print('  = 0.856 constant across LATARG 280/301.6/320, slope 0.85 -- so the ~14% spacing deficit is a')
    print('  fixed structural ratio, NOT an artefact. The first-peak offset l_1 is nearly pinned (the')
    print('  phase drifts in l_1/L_A), so the residual disagreement with the sky is the phase, not the')
    print('  scale. The deficit is acoustic structure; F5 unsoftened, the verdict is PO-7/PO-10\'s.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
