#!/usr/bin/env python3
"""r7815 (cc66): THE 0.964, RE-MEASURED AT MATCHED MODE SAMPLING.

`r7809`'s `0.918 -> 0.964` was scored with the OLD control at `LSTEP=2` (950 samples
on 100..1998) against the RE-POINTED control at `LSTEP=8` (238 samples on 100..1996).
`chi2_of_spectrum.chi2_of(ls, Dl)` bins whatever grid it is handed into 185 bins, so
the two sides of that ratio were binned from different samplings.

⛔ That is my own surviving correction (a) in the only form that survived: a step-8
bank cannot be SUBSTITUTED for a step-2 one, because the arrays are 238 long against
950 and every procedure that samples the grid reads the difference.  At the SAME
point the two banks' `Dl` agree to 5.55e-16 at shared multipoles -- so if the ratio
moves here, the move is the BINNING and not the physics, and that is worth knowing
before a paper sentence is edited to the number.

(a1) built the matched bank.  This re-scores the ratio three ways, through the
receipt's OWN scoring path (`chi2_of_spectrum`, P15's CAMB lensing operator), and
reproduces the receipt's own two figures first as its anchor.
"""
import os
import re
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
SP = os.path.join(BW, 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import camb                                                            # noqa: E402
import chi2_of_spectrum as CS                                          # noqa: E402

WB, WC, H = 0.02237, 0.1200, 0.6736

#: P15's own lensing operator, built exactly as the r7809 receipt builds it
_p = camb.set_params(H0=67.40, ombh2=WB, omch2=0.3150 * 0.674 ** 2 - WB, mnu=0.06, omk=0,
                     tau=0.054, As=2.1e-9, ns=0.965, lmax=3000)
_cl = camb.get_results(_p).get_cmb_power_spectra(_p, CMB_unit='muK', lmax=3000)
_le, _un = _cl['total'][:, 0], _cl['unlensed_scalar'][:, 0]
LG = np.arange(len(_le), dtype=float)
LENS = np.ones_like(_le)
LENS[_un > 0] = _le[_un > 0] / _un[_un > 0]


def score(p):
    with np.load(p, allow_pickle=True) as z:
        ls, Dl = np.asarray(z['ls'], float), np.asarray(z['Dl'], float)
    c, nb = CS.chi2_of(ls, Dl * np.interp(ls, LG, LENS))[:2]
    return float(c), int(nb), len(ls)


OLD2 = os.path.join(SP, 'cc66_lcdm_L2000.npz')
NEW8 = os.path.join(BW, 'r7807_cc66_the_23_items_and_the_repointed_control', 'out',
                    'r7807_control_planck2018_L2000.npz')
NEW2 = os.path.join(BW, 'r7812_cc66_the_resumable_mode_loop_and_the_one_pass', 'out',
                    'r7812_control_step2_L2000_assembled.npz')
PUB = 0.918

rows = [('the old control, step 2  (the published 0.918\'s denominator)', OLD2),
        ('the re-pointed control, step 8  (what r7809 scored)', NEW8),
        ('the re-pointed control, step 2  (matched -- (a1) built it)', NEW2)]
out = {}
print(f'  {"spectrum":58s} {"samples":>8s} {"bins":>5s} {"chi^2":>10s}')
for tag, p in rows:
    c, nb, n = score(p)
    out[tag] = (c, nb, n)
    print(f'  {tag:58s} {n:8d} {nb:5d} {c:10.3f}')

CO = out[rows[0][0]][0]
C8 = out[rows[1][0]][0]
C2 = out[rows[2][0]][0]
ARM = PUB * CO                      # the arm's own chi^2, recovered as the receipt recovers it

print(f'\n  the arm\'s chi^2, recovered as the receipt recovers it: {PUB} x {CO:.3f} = {ARM:.3f}')
print(f'\n  {"ratio":58s} {"value":>10s} {"prints as":>10s}')
print(f'  {"published, old control":58s} {PUB:10.4f} {PUB:10.3f}')
print(f'  {"r7809: arm / re-pointed control at step 8 (MISMATCHED)":58s} '
      f'{ARM / C8:10.4f} {ARM / C8:10.3f}')
print(f'  {"r7815: arm / re-pointed control at step 2 (MATCHED)":58s} '
      f'{ARM / C2:10.4f} {ARM / C2:10.3f}')

# ── the anchors: the receipt's own two figures must reproduce before anything here is read
assert abs(CO - 214.057) < 0.05, f'the old control does not reproduce: {CO:.3f} vs 214.057'
assert abs(C8 - 203.823) < 0.05, f'r7809\'s step-8 figure does not reproduce: {C8:.3f} vs 203.823'
assert abs(ARM / C8 - 0.9641) < 0.0004, 'r7809\'s 0.9641 does not reproduce'
print('\n  ✓ anchors held: the receipt\'s own 214.057, 203.823 and 0.9641 all reproduce here,')
print('    so the third row is a change of ONE input and not of two procedures')

d8, d2 = 100 * (C8 - CO) / CO, 100 * (C2 - CO) / CO
print(f'\n  the control\'s improvement:  step 8 {d8:+.3f} %   step 2 {d2:+.3f} %   '
      f'difference {d2 - d8:+.3f} %')
print(f'  the ratio at matched sampling is {ARM / C2:.4f}, printing as {ARM / C2:.3f}, against '
      f'{ARM / C8:.3f} at mismatched sampling')
if round(ARM / C2, 3) == round(ARM / C8, 3):
    print('  ⇒ THE PUBLISHED FIGURE IS THE SAME TO THREE DECIMALS EITHER WAY: the step mismatch did '
          'NOT\n    reach the printed digits, so r7809\'s 0.964 stands as printed and (a1) has '
          'CONFIRMED it\n    rather than corrected it.')
else:
    print('  ⇒ ⛔ THE STEP MISMATCH REACHED THE PRINTED DIGITS: the number P15 should carry is the '
          'MATCHED\n    one, and r7809\'s figure was an artefact of binning two different samplings.')
