#!/usr/bin/env python3
"""r7819 ⑥ (cc66): CAMB AT C59'S OWN POINT, THROUGH C59'S OWN LOCATOR.

P15 `l.857` prints the control's `P1/P2 = 2.1969` *"against a standard code's
2.200---agreement to 0.14%"*.  `C59` line 116 is `CAMB_R2 = 2.200`, a HARDCODED
LITERAL: no CAMB is run in that receipt and no locator touches that number.  So
the `0.14 %` compares a LOCATED instrument number against a QUOTED one.

This measures what the quoted one should be: CAMB at `C59`'s point, on `C59`'s
own reported grid, through `C59`'s own locator -- raw cell maxima, which is what
`argrelextrema(Dl, np.greater, order=3)` returns and is why `C59`'s peaks print
as the grid cells `220 / 540 / 812`.

Registered at `PREDICTION.md` before a line of this existed.
"""
import os
import sys

import numpy as np
from scipy.signal import argrelextrema

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', 'planck_tt_likelihood'))
import camb                                                               # noqa: E402

#: C59's point: the instrument's UN-REFITTED control default (ACOUSTIC_two_arm l.149-151, l.93),
#: with no LH0/LOM/WBH2/NS in C59's environment.  Three MASSLESS species, as the instrument has.
H0, OM, OMBH2, NS = 67.40, 0.3150, 0.0224, 0.965
H2 = (H0 / 100.0) ** 2
OMCH2 = OM * H2 - OMBH2
#: C59's reported grid, verbatim: `ls = np.arange(100, int(AT.LMAXL), int(LSTEP))` at LMAXL=900.
LS = np.arange(100, 900, 8)

print(__doc__)
print(f'  the point: H0 {H0}  Omega_m {OM}  omega_b {OMBH2}  -> omega_c {OMCH2:.5f}  n_s {NS}')
print(f'  the grid : {len(LS)} cells, {LS[0]}..{LS[-1]} step {LS[1] - LS[0]}\n')


def located(cl_tt):
    """C59's locator verbatim: raw cell maxima on ITS grid, ratio of the first two."""
    Dl = np.asarray([cl_tt[int(l)] for l in LS], float)
    pk = [q for q in argrelextrema(Dl, np.greater, order=3)[0]]
    assert len(pk) >= 3, f'fewer than three peaks: {pk}'
    return ([float(LS[q]) for q in pk[:3]],
            float(Dl[pk[0]] / Dl[pk[1]]), float(Dl[pk[0]] / Dl[pk[2]]))


p = camb.set_params(H0=H0, ombh2=OMBH2, omch2=OMCH2, ns=NS, tau=0.0544, As=2.1e-9,
                    mnu=0.0, num_massive_neutrinos=0, omk=0, lmax=1500)
cl = camb.get_results(p).get_cmb_power_spectra(p, CMB_unit='muK', lmax=1500)

OUT = {}
for tag, key in (('unlensed', 'unlensed_scalar'), ('lensed', 'total')):
    pks, r2, r3 = located(cl[key][:, 0])
    OUT[tag] = (pks, r2, r3)
    print(f'  CAMB {tag:>8}:  peaks {[int(x) for x in pks]}  '
          f'P1/P2 = {r2:.4f}   P1/P3 = {r3:.4f}')

PAPER_INSTR, PAPER_CAMB, PAPER_PCT = 2.1969, 2.200, 0.14
print(f"\n  the paper's pair: the instrument's {PAPER_INSTR} against a quoted {PAPER_CAMB} "
      f'-> {abs(PAPER_INSTR - PAPER_CAMB) / PAPER_CAMB * 100:.2f} %')
print('  -' * 38)
for tag, (pks, r2, r3) in OUT.items():
    print(f'  against CAMB {tag:>8} through this locator, {r2:.4f}: '
          f'{abs(PAPER_INSTR - r2) / r2 * 100:.2f} %')

print('\n  ' + '=' * 74)
print('  PREDICTIONS, as registered')
u, l_ = OUT['unlensed'][1], OUT['lensed'][1]
P = [('(1) unlensed P1/P2 in 2.15 .. 2.30', 2.15 < u < 2.30, f'{u:.4f}'),
     ('(2) it is NOT 2.200 to three decimals: |CAMB - 2.200| > 0.002',
      abs(u - 2.200) > 0.002, f'{abs(u - 2.200):.4f}'),
     ('(3) lensing moves P1/P2 by less than 1 per cent',
      abs(l_ / u - 1.0) < 0.01, f'{(l_ / u - 1.0) * 100:+.2f} %'),
     ('(4) the restated agreement moves off 0.14 by more than 0.1 point',
      abs(abs(PAPER_INSTR - u) / u * 100 - PAPER_PCT) > 0.1,
      f'{abs(PAPER_INSTR - u) / u * 100:.2f} %')]
for label, ok, got in P:
    print(f"    [{'HELD' if ok else 'FAILED'}]  {label}\n              -> {got}")
print('  ' + '=' * 74)
sys.exit(0)
