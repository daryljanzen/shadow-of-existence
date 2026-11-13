#!/usr/bin/env python3
"""`r7751+cc66` PRICING THE LEAF-RATE READING AGAINST THE BAO, AND THE HALF-PER-CENT CANDIDATES.

⛭ Registered in `PREDICTION.md` at `r7751+cc66.0`, pushed before this file existed. `R1`'s and `R2`'s
licences were set there and are not moved.

⛭ ** THE RATE LAWS ARE 60's, READ BY PATH AND NOT REIMPLEMENTED ** (`r7445`'s practice, `r7612`'s
precedent): `r7580/lightpath.py` carries `H_stack`, `H_leaf` and the background the prior `P15` receipt
fits. If it has moved, this refuses rather than substituting a background of my own.
"""
import os
import runpy
import sys
import contextlib
import io

import numpy as np
from scipy.integrate import quad

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
LP = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                  'r7580_60_whether_the_observers_readout_identification_forces_the_stacking_rate_distance',
                  'lightpath.py')
if not os.path.exists(LP):
    sys.exit("FATAL: 60's lightpath.py is not where this reads it from; the instrument has moved.")

buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    NS = runpy.run_path(LP)
H0, OM, OMR = NS['H0'], NS['OM'], NS['OMR']
H_stack, H_leaf, C = NS['H_stack'], NS['H_leaf'], NS['C']
Z_REC = NS['Z_REC']
print(__doc__)
print("=" * 100)
print(f"\n  background read from 60's script: H0 {H0}  Om {OM}  Om_r {OMR:.4e}  z* {Z_REC}")


def DM(z, H):
    return quad(lambda zz: C / H(zz), 0.0, z, limit=200)[0]


# ------------------------------------------------------------------ R1: the epoch split
BAO = [0.295, 0.510, 0.706, 0.930, 1.317, 2.330]       # DESI-like tracer redshifts, declared
print("\n  ⛭ R1 -- Delta = D_M(leaf)/D_M(stack) - 1, at the BAO redshifts and at z*")
print(f"      {'z':>7} {'D_M stack':>12} {'D_M leaf':>12} {'Delta':>12}")
worst = 0.0
for z in BAO:
    a, b = DM(z, H_stack), DM(z, H_leaf)
    d = b / a - 1.0
    worst = max(worst, abs(d))
    print(f"      {z:7.3f} {a:12.3f} {b:12.3f} {100*d:11.5f} %")
a_s, b_s = DM(Z_REC, H_stack), DM(Z_REC, H_leaf)
d_rec = b_s / a_s - 1.0
print(f"      {'z*':>7} {a_s:12.3f} {b_s:12.3f} {100*d_rec:11.5f} %")
print(f"\n      worst |Delta| over the BAO redshifts: {100*worst:.5f} %")
print(f"      |Delta| at z*:                        {100*abs(d_rec):.5f} %")
if worst <= 5e-4 and 3e-3 <= abs(d_rec) <= 7e-3:
    print("      ⇒ R1 ROW ONE: no split is needed. Putting EVERY cross-leaf accumulation on the leaf")
    print("        rate leaves the BAO where it is and moves only the distance to last scattering.")
elif worst >= 2e-3:
    print("      ⛔ R1 ROW TWO: the reading COSTS the BAO fit; that is the contradiction.")
else:
    print("      ⇒ R1 ROW THREE: between the lines; the range is reported and neither is claimed.")

# ------------------------------------------------------------------ R2: the candidates
print("\n  ⛭ R2 -- sensitivity of D_M(z*) to each parameter the rate carries")
TARGET = -0.498e-2


def dm_with(**kw):
    h0 = kw.get('H0', H0); om = kw.get('OM', OM)
    return quad(lambda z: C / (h0 * np.sqrt(om * (1 + z) ** 3 + 1.0 - om)),
                0.0, Z_REC, limit=200)[0]


base = dm_with()
print(f"      base D_M(z*) on the stacking rate: {base:.3f} Mpc")
for name, kw, eps, note in (
        ('H0 (the rate amplitude)', 'H0', 1e-3, 'fixed BY the angle and the BAO together (link 8)'),
        ('Om  (the epoch, x0^-3)', 'OM', 1e-3, 'x0 measured calibration-free, z_acc = x0 - 1')):
    p = {'H0': H0, 'OM': OM}[kw]
    up = dm_with(**{kw: p * (1 + eps)})
    sens = (up / base - 1.0) / eps
    need = TARGET / sens
    print(f"      {name:26s} dlnD_M/dln p = {sens:+8.4f}   needs {100*need:+7.3f} % in p")
    print(f"          ⌗ {note}")
print("\n" + "=" * 100)

# ------------------------------------------------------------------ POST-REGISTRATION, labelled
print("\n  ⛭ POST-REGISTRATION (the registration asked only for D_M(z*)): is any other lever LOCAL?")
print("     ⌗ Added because R1 showed the leaf rate moves z* by 0.5 per cent and the BAO by 0.02,")
print("       which raises a question the registration did not: whether the other levers do that too.")
print(f"      {'lever':26s} {'dlnD_M(z*)':>12} {'dlnD_M(z=0.51)':>16} {'dlnD_M(z=2.33)':>16}")
for name, kw, eps in (('the leaf rate (Om_r on)', 'LEAF', None),
                      ('H0 (the rate amplitude)', 'H0', 1e-3),
                      ('Om (the epoch, x0^-3)', 'OM', 1e-3)):
    if kw == 'LEAF':
        row = [(DM(z, H_leaf) / DM(z, H_stack) - 1.0) for z in (Z_REC, 0.510, 2.330)]
        # expressed as the fractional change itself, not a log-derivative
        print(f"      {name:26s} {100*row[0]:11.5f}% {100*row[1]:15.5f}% {100*row[2]:15.5f}%")
        continue
    p = {'H0': H0, 'OM': OM}[kw]

    def dm_at(z, **kwx):
        h0 = kwx.get('H0', H0); om = kwx.get('OM', OM)
        return quad(lambda zz: C / (h0 * np.sqrt(om * (1 + zz) ** 3 + 1.0 - om)),
                    0.0, z, limit=200)[0]
    row = []
    for z in (Z_REC, 0.510, 2.330):
        up = dm_at(z, **{kw: p * (1 + eps)})
        row.append((up / dm_at(z) - 1.0) / eps)
    print(f"      {name:26s} {row[0]:11.4f}  {row[1]:15.4f}  {row[2]:15.4f}")
print("\n      ⇒ the leaf rate is the only LOCAL lever: it moves the distance to last scattering")
print("        and leaves the BAO. The others are global rescalings and drag the BAO with them.")
print("=" * 100)
