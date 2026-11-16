#!/usr/bin/env python3
"""r7815 (cc66) -- the control's theta* pull at Planck 2018's PUBLISHED point.

P15 l.293 prints "at its own background, before refitting, it sits 4.94 standard
deviations high".  r7805's receipt measures that 4.944 at
`PLANCK = (67.40, 0.3150, 0.02237)` -- which it labels "Planck's un-refitted
point" and which `r7807+cc66` showed is NOT Planck 2018's published best fit:
its implied omega_c is 0.120727 against the published 0.1200.  So that figure is
a control number at the UN-REFITTED point, and 69's r7815 list does not name it.

This probe re-derives it at the published point, through the SAME functions the
receipt uses (`theta_corpus.theta_at`'s body, imported rather than retyped), so
the move is a difference of one input and not of two procedures.
"""
import json, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
sys.path.insert(0, os.path.join(BW, 'r7749_70_leafgeom_refit'))
import theta_corpus as T                                           # noqa: E402

ZREC, TOBS, TSIG = T.ZREC, T.THETA_OBS, T.THETA_SIG


def theta_at(H0, Om, wb, z_hi, Egeom):
    span, ref = np.log(1 + z_hi) - np.log(1 + ZREC), np.log(1 + 3e7) - np.log(1 + ZREC)
    n = int(round(60000 * max(1.0, span / ref)))
    return T.r_snd(H0, Om, wb, z_hi, ZREC, T.E_leaf, n=n) / T.D_M(ZREC, H0, Om, Egeom)


def pull(t):
    return (t - TOBS) / TSIG


# the corpus's control point, as the r7805 receipt carries it
OLD = (67.40, 0.3150, 0.02237)
# Planck 2018 TT,TE,EE+lowE+lensing base-LambdaCDM, the point r7807 re-pointed to:
# H0 67.36, omega_c 0.1200, omega_b 0.02237  =>  Om = (0.1200+0.02237)/0.6736**2
H0_NEW, WB_NEW = 67.36, 0.02237
OM_NEW = (0.1200 + WB_NEW) / (H0_NEW / 100.0) ** 2
NEW = (H0_NEW, OM_NEW, WB_NEW)

print(f'  the corpus control point   : H0 {OLD[0]}, Om {OLD[1]}, wb {OLD[2]}')
print(f'      its implied omega_c    : {OLD[1] * (OLD[0] / 100.0) ** 2 - OLD[2]:.6f}')
print(f"  Planck 2018's published pt : H0 {NEW[0]}, Om {NEW[1]:.6f}, wb {NEW[2]}")
print(f'      its omega_c by construction: {0.1200:.4f}')

for tag, p in (('old (67.40, 0.3150)', OLD), ("Planck 2018 published", NEW)):
    t = theta_at(*p, 1e14, T.E_leaf)
    print(f'  {tag:24s}  100theta* = {100 * t:.5f}   pull = {pull(t):+.3f} sigma')

t_old, t_new = theta_at(*OLD, 1e14, T.E_leaf), theta_at(*NEW, 1e14, T.E_leaf)
print(f'\n  the printed 4.94 becomes {pull(t_new):.2f};  the move is '
      f'{pull(t_new) - pull(t_old):+.3f} sigma')

# the receipt's own figure, reproduced, so this probe is anchored and not free-floating
assert abs(pull(t_old) - 4.944) < 0.004, 'the r7805 receipt figure does not reproduce here'
print('  ✓ the r7805 receipt\'s own 4.944 reproduces at the old point (anchor held)')
