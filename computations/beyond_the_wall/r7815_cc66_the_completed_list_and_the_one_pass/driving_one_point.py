#!/usr/bin/env python3
"""r7817 (cc66): THE DRIVING SUBTRACTION AT ONE POINT, BOTH LEGS.

Site 2 is the control's `l_1/l_A` shift when every coupling to the potential is
removed.  It is a difference of TWO control spectra, and the swap could only
re-point one of them -- `cc66_lcdm_nodrive_pol.npz` sits at the un-refitted
`(144.528076, 13864.662715)`, so the swap's `0.1792 -> 0.1790` is one spectrum at
Planck's point minus another at the corpus's old one.  `r7817+cc66.2` reported
that and launched the undriven leg at Planck's point; this reads the subtraction
off both legs at each point, so each figure is one point's own.

It reproduces the paper's `0.1792` at the old point first, as its anchor.
"""
import os
import sys

import numpy as np
from scipy.signal import argrelextrema

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
SP = os.path.join(BW, 'spectra')
R7812 = os.path.join(BW, 'r7812_cc66_the_resumable_mode_loop_and_the_one_pass')


def peak1(path):
    """the receipt's own locator, verbatim: argrelextrema(order=3), first maximum"""
    z = np.load(path, allow_pickle=True)
    ls, Dl = np.asarray(z['ls'], float), np.asarray(z['Dl'], float)
    q = argrelextrema(Dl, np.greater, order=3)[0]
    return float(ls[q[0]]), float(z['l_A']), (round(float(z['r_s']), 6), round(float(z['D_M']), 6))


POINTS = {
    "the corpus's old point": (
        os.path.join(SP, 'cc66_lcdm.npz'),
        os.path.join(SP, 'cc66_lcdm_nodrive_pol.npz')),
    "Planck 2018's published point": (
        os.path.join(R7812, 'out_L1300', 'r7812_control_step2_L1300_assembled.npz'),
        os.path.join(R7812, 'out_L1300_nodrive',
                     'r7812_control_step2_L1300_nodrive_assembled.npz')),
}

ARM = 0.1717           # this arm's own subtraction; the arm is not re-pointed
out = {}
for tag, (dp, up) in POINTS.items():
    l1d, lAd, bgd = peak1(dp)
    l1u, lAu, bgu = peak1(up)
    shift = l1u / lAu - l1d / lAd
    out[tag] = shift
    print(f'  {tag}')
    print(f'      driven  : l_1 = {l1d:7.1f}  l_A = {lAd:8.4f}  l_1/l_A = {l1d / lAd:.4f}  bg {bgd}')
    print(f'      undriven: l_1 = {l1u:7.1f}  l_A = {lAu:8.4f}  l_1/l_A = {l1u / lAu:.4f}  bg {bgu}')
    print(f'      ⇒ the shift = {shift:.4f}')
    if bgd != bgu:
        print(f'      ⛔ THE TWO LEGS ARE AT DIFFERENT POINTS -- this shift is a mixed-point '
              f'difference')
    else:
        print(f'      ✓ both legs at one point, so the shift is that point\'s own')
    print()

OLD, NEW = out["the corpus's old point"], out["Planck 2018's published point"]
assert abs(OLD - 0.1792) < 5e-4, f"the paper's 0.1792 does not reproduce at the old point: {OLD:.4f}"
print(f"  ✓ anchor held: the paper's 0.1792 reproduces at the old point ({OLD:.4f})")
print(f'\n  the control\'s driving shift: {OLD:.4f} -> {NEW:.4f}   (the swap\'s mixed-point '
      f'answer was 0.1790)')
print(f'  the arm\'s own shift is {ARM} and does not move; so the grip ratio arm/control goes '
      f'{ARM / OLD:.4f} -> {ARM / NEW:.4f},')
print(f'  i.e. the arm\'s grip weaker by {100 * (1 - ARM / OLD):.2f} % -> '
      f'{100 * (1 - ARM / NEW):.2f} %')
w = 100 * (1 - ARM / NEW)
print(f'\n  ⇒ "within four per cent" ' + ('STANDS' if round(w) <= 4 else
      f'DOES NOT STAND: {w:.2f} % rounds to {round(w)}') +
      f';  "slightly weaker rather than stronger" '
      f'{"stands" if ARM / NEW < 1 else "FAILS"} at {ARM / NEW:.3f}')
sys.exit(0)
