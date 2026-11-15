#!/usr/bin/env python3
r"""r7783+cc66 item (4): is the l=3 sign reversal the LADDER's?

Registered in PREDICTION.md (r7783+cc66.11) before any transfer was computed.

THE HYPOTHESIS, in one line: the depth is the L=2-floored Riemann sum (step dL=1) of the very
integral it is divided by, the ladder k_L = sqrt(L(L+2))/r0 carries no projection distance, and so
-- to the extent a chi change acts on Delta_l as a k-stretch -- moving the distance is the same
operation as moving the ladder.  Moving r_0 alone is therefore the test.

The transfer, the weight and the ladder are this producer's own, lifted from
`computations/perturbation_verify/verify_lowell_boltzmann.py` with its own control configuration.

rc=0 if every row holds.
"""
import os
import sys

import numpy as np
from scipy.interpolate import interp1d

OK = []


def row(tag, good, text):
    OK.append((tag, good, text))
    print(f'{"PASS" if good else "FAIL"}  {tag}  {text}', flush=True)


# ---- the producer's own configuration and definitions, unchanged
H0, ombh2, omch2 = 67.4, 0.02237, 0.1200
ns, As, kpiv = 0.9649, 2.1e-9, 0.05
R0 = 5064.0
LMAX = 10
print('computing the transfer (CAMB, the producer\'s own accuracy settings) ...', flush=True)
import camb                                                                    # noqa: E402
pars = camb.CAMBparams()
pars.set_cosmology(H0=H0, ombh2=ombh2, omch2=omch2, mnu=0.06, tau=0.0544)
pars.InitPower.set_params(As=As, ns=ns)
pars.set_for_lmax(LMAX + 8, lens_potential_accuracy=0)
pars.set_accuracy(AccuracyBoost=3, lSampleBoost=50, lAccuracyBoost=3)
res = camb.get_results(pars)
td = res.get_cmb_transfer_data()
DL = np.array(td.delta_p_l_k)[0]
Larr, q = np.array(td.L), np.array(td.q)
lnq = np.log(q)
ELLS = [l for l in range(2, 9)]


def weight(k):
    return (k / kpiv) ** (ns - 1.0)


def depth(ell, r0, floor_only_shift=False):
    """the producer's own depth: floored Riemann sum over the ladder, divided by the integral"""
    i = int(np.argmin(np.abs(Larr - ell)))
    Dl = DL[i]
    cont = float(np.trapezoid(weight(q) * Dl ** 2, lnq))
    f = interp1d(lnq, Dl, kind='cubic', bounds_error=False, fill_value=0.0)
    Ls = np.arange(2, 4000)
    kL = np.sqrt(Ls * (Ls + 2)) / r0
    m = (kL >= q.min()) & (kL <= q.max())
    wL = (Ls + 1.0) / (Ls * (Ls + 2.0))
    terms = wL[m] * weight(kL[m]) * f(np.log(kL[m])) ** 2
    return float(np.sum(terms) / cont), float(terms[0]) / cont if terms.size else 0.0


EPS = 2e-3
print(f'\n      {"l":>3} {"depth":>10} {"dlnDepth/dlnr0":>16} {"-that":>9} '
      f'{"floor term":>12} {"dFloor/dlnr0":>14}')
d_r0, floor_sign = {}, {}
for l in ELLS:
    dp, fl = depth(l, R0)
    dh, flh = depth(l, R0 * (1 + EPS))
    dl_, fll = depth(l, R0 * (1 - EPS))
    der = (np.log(dh) - np.log(dl_)) / (2 * EPS)
    fder = (flh - fll) / (2 * EPS)
    d_r0[l], floor_sign[l] = float(der), float(fder)
    print(f'      {l:>3} {dp:>10.4f} {der:>+16.4f} {-der:>+9.4f} {fl:>12.4f} {fder:>+14.4f}')

# the measured depth moves, from r7779+cc66.2's arm-B frozen pair at the refit point (per cent)
MEASURED = {2: -1.430, 3: +1.547, 4: -1.333, 5: -1.976, 6: -0.738, 7: -0.102, 8: +0.271}
DM_MOVE = -0.4984          # the projection distance's own move, per cent

print()
print('=' * 99)
print('R1  THE LADDER ALONE HAS AN l-DEPENDENT SENSITIVITY, AND THESE ARE ITS SIGNS')
print('=' * 99)
want = {2: +1, 3: -1, 4: +1, 5: +1}
got = {l: (1 if d_r0[l] > 0 else -1) for l in want}
row('R1', all(got[l] == want[l] for l in want),
    'dlnDepth/dlnr0 signs at l=2..5: '
    + ', '.join(f'l={l}: {"+" if got[l] > 0 else "-"}' for l in sorted(want))
    + f' against the registered {", ".join(f"l={l}: {chr(43) if want[l]>0 else chr(45)}" for l in sorted(want))}')

print()
print('=' * 99)
print('R2  AND IT REPRODUCES THE MEASURED SIGN AT EVERY l <= 6, THE l=3 REVERSAL INCLUDED')
print('=' * 99)
print(f'      {"l":>3} {"measured move %":>16} {"-dlnDepth/dlnr0":>17} {"signs agree":>12}')
agree = {}
for l in (2, 3, 4, 5, 6):
    pred = -d_r0[l]
    agree[l] = (pred > 0) == (MEASURED[l] > 0)
    print(f'      {l:>3} {MEASURED[l]:>+16.3f} {pred:>+17.4f} {str(agree[l]):>12}')
row('R2', all(agree.values()),
    'the ladder alone reproduces the measured sign at '
    f'{sum(agree.values())} of 5 multipoles'
    + (' -- including the l=3 reversal, so the reversal is the LADDER\'s and not the dynamics\''
       if agree.get(3) else ' -- but NOT at l=3, so the reversal is not a commensurability effect'))

print()
print('=' * 99)
print('R3  AND THE SIZE AGREES TO WITHIN THE STRETCH APPROXIMATION (a loose factor 3, registered loose)')
print('=' * 99)
print(f'      {"l":>3} {"measured dlnD/dlnDM":>21} {"-dlnDepth/dlnr0":>17} {"ratio":>8}')
ratios = {}
for l in (2, 3, 4, 5):
    meas = MEASURED[l] / DM_MOVE
    pred = -d_r0[l]
    ratios[l] = abs(pred / meas) if meas else float('inf')
    print(f'      {l:>3} {meas:>+21.4f} {pred:>+17.4f} {ratios[l]:>8.2f}')
row('R3', all(1 / 3.0 <= r <= 3.0 for r in ratios.values()),
    'ratio of the ladder-only prediction to the measured sensitivity: '
    + ', '.join(f'l={l}: {ratios[l]:.2f}' for l in sorted(ratios))
    + ' -- all within the registered factor 3' if all(1 / 3.0 <= r <= 3.0 for r in ratios.values())
    else 'ratio outside the registered factor 3 at '
         + ', '.join(f'l={l}: {ratios[l]:.2f}' for l in sorted(ratios) if not 1 / 3.0 <= ratios[l] <= 3.0))

print()
print('=' * 99)
print('R4  AND IS IT THE FLOOR?  the L=2 term alone, against the whole sum')
print('=' * 99)
print(f'      {"l":>3} {"dDepth/dlnr0":>14} {"dFloor/dlnr0":>14} {"same sign":>10}')
same = {}
for l in (2, 3, 4, 5):
    dp, _ = depth(l, R0)
    whole = d_r0[l] * dp                      # dDepth = dlnDepth * Depth
    same[l] = (whole > 0) == (floor_sign[l] > 0)
    print(f'      {l:>3} {whole:>+14.5f} {floor_sign[l]:>+14.5f} {str(same[l]):>10}')
row('R4', sum(same.values()) >= 3,
    f'the floor term alone carries the sign at {sum(same.values())} of 4 multipoles'
    + (' -- so what sets the sign is the hard floor at L=2, which is a statement about a DISCRETE '
       'source and not about the transfer' if sum(same.values()) >= 3 else
       ' -- so the sign is set by the INTERIOR of the sum and not by the floor, and the mechanism is '
       'the ladder without being the floor'))

print()
print('=' * 99)
row('R5', True, 'no claim that the reversal is observable; no significance; no new figure for the '
                "paper; and the vehicle is the producer's own control configuration (H0 67.4, "
                'r0 5064), stated rather than quietly relied on')
bad = [t for t, g, _ in OK if not g]
print(f'{len(OK) - len(bad)} of {len(OK)} rows hold' + (f'; RED: {bad}' if bad else ''))
print('=' * 99)
raise SystemExit(1 if bad else 0)
