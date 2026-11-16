#!/usr/bin/env python3
"""r7812/r7815 (a1): what the ASSEMBLED step-2 spectrum is, measured against the two
banks it has to be read beside.

⛔ There is NO straight LMAXL=2000 LSTEP=2 run to difference against -- that run not
fitting the container is the whole reason (a1) was ordered.  The exactness of the
PARTITION was established on the short range instead (LMAXL=400, four slices against a
straight run, agreeing to 1.72 ULPs, registered in advance as not bit-identical).  This
file does not re-make that claim at L2000 and says so rather than implying it.

What it DOES measure, because both are claims the one pass will rest on:
 (A) the assembled step-2 bank against the step-8 bank at the SAME point -- the size of
     r7809's correction (a), "a step-8 bank cannot serve step-2 figures", now in numbers
     on the control's own spectrum rather than on a receipt's located peaks;
 (B) the assembled step-2 bank against the OLD step-2 bank at the un-refitted point --
     the re-pointing move on the grid the figures are actually read on.
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)

ASM = os.path.join(HERE, 'out', 'r7812_control_step2_L2000_assembled.npz')
STEP8 = os.path.join(BW, 'r7807_cc66_the_23_items_and_the_repointed_control', 'out',
                     'r7807_control_planck2018_L2000.npz')
OLD2 = os.path.join(BW, 'spectra', 'cc66_lcdm_L2000.npz')


def z(p):
    return np.load(p, allow_pickle=True)


def bg(a):
    return (round(float(a['r_s']), 6), round(float(a['D_M']), 6))


def compare(tag, a, b, name_a, name_b):
    """on the multipoles the two share, since the grids differ by construction in (A)"""
    la, lb = np.asarray(a['ls']), np.asarray(b['ls'])
    shared = np.intersect1d(la, lb)
    ia = np.searchsorted(la, shared)
    ib = np.searchsorted(lb, shared)
    da = np.asarray(a['Dl'], float)[ia]
    db = np.asarray(b['Dl'], float)[ib]
    rel = np.abs(db / da - 1.0)
    print(f'\n  ===== {tag} =====')
    print(f'    {name_a}: {len(la)} multipoles;  {name_b}: {len(lb)};  shared: {len(shared)}')
    print(f'    max |{name_b}/{name_a} - 1| = {rel.max():.3e}  at l = {int(shared[rel.argmax()])}')
    print(f'    median                      = {np.median(rel):.3e}')
    print(f'    bit-identical               = {np.array_equal(da, db)}')
    return rel.max()


asm, s8, o2 = z(ASM), z(STEP8), z(OLD2)
print(f'  assembled : (r_s, D_M) = {bg(asm)}   {len(asm["ls"])} multipoles, '
      f'l {int(asm["ls"][0])}..{int(asm["ls"][-1])}')
print(f'  step-8    : (r_s, D_M) = {bg(s8)}    {len(s8["ls"])} multipoles, '
      f'l {int(s8["ls"][0])}..{int(s8["ls"][-1])}')
print(f'  old step-2: (r_s, D_M) = {bg(o2)}   {len(o2["ls"])} multipoles, '
      f'l {int(o2["ls"][0])}..{int(o2["ls"][-1])}')

assert bg(asm) == bg(s8), 'the assembled bank and the step-8 bank are NOT at the same point'
print('\n  ✓ the assembled bank and the step-8 bank carry the SAME background, asserted:')
print('    so comparison (A) isolates the MODE SAMPLING and nothing else')
assert bg(asm) != bg(o2), 'the assembled bank is at the OLD point -- the run did not re-point'
assert np.array_equal(np.asarray(asm['ls']), np.asarray(o2['ls'])), \
    'the assembled bank and the old step-2 bank do NOT share a grid -- the swap would not be exact'
print('  ✓ the assembled bank and the old step-2 bank share their l grid EXACTLY (950 samples),')
print('    so the re-pointing swap moves the point and nothing else')

a = compare('(A) the same point, step-2 against step-8', asm, s8, 'step2', 'step8')
b = compare('(B) step-2, Planck\'s point against the un-refitted point', asm, o2, 'new', 'old')

print('\n  ⇒ (A) is the size of r7809\'s correction (a) on the spectrum itself: a step-8 bank '
      f'differs from\n       the step-2 one at the same point by up to {100 * a:.2f} per cent, '
      'which is why the\n       figures read on the step-2 grid could not be re-pointed with the '
      'step-8 bank.')
print(f'  ⇒ (B) is the re-pointing, on the grid the figures are read on: up to {100 * b:.2f} '
      'per cent.')
sys.exit(0)
