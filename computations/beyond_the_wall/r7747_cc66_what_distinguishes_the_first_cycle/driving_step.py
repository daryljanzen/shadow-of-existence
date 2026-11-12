#!/usr/bin/env python3
"""`r7747+cc66` DOES REMOVING THE RADIATION DRIVING REMOVE THE LOWEST-BAND STEP?

⛭ Registered in `PREDICTION.md` at `r7747+cc66.0`, pushed before this file existed. Every line below
is that registration's: the four arrays, the band edges, the envelope window `W = 81`, the statistic,
the precondition `P0`, and the `0.30`/`0.70` licences.

⛔ ** THE ABSOLUTE STEPS HERE ARE NOT THE PRINTED ONES ** -- different bank and grid, because the fine
bank the printed step uses has no driving-off counterpart. Only the WITHIN-PAIR ratio is read.
⛔ ** AND THESE ARE THE LEAF-RECOMBINATION ARRAYS, NOT DEMONSTRABLY THE REFITTED ARM OF RECORD. **
"""
import json
import os
import sys

import numpy as np

D = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'spectra')
QE = np.array([0.85, 1.55, 2.25, 2.95, 3.65, 4.35, 5.05, 5.75])   # r6959_eta_cr's own edges
W = 81                                                             # declared in the registration
PAIRS = {'CR arm': ('c54.186_cr_L3000_leafrec1.npz', 'c54.193_cr_nodrive_L3000_leafrec1.npz'),
         'control': ('c54.186_lcdm_L3000.npz', 'c54.193_lcdm_nodrive_L3000.npz')}


def envelope(y, w):
    """centred running mean, edges shortened rather than padded (no invented data)"""
    out = np.empty_like(y)
    h = w // 2
    for i in range(y.size):
        a, b = max(0, i - h), min(y.size, i + h + 1)
        out[i] = y[a:b].mean()
    return out


def step_of(path):
    z = np.load(os.path.join(D, path), allow_pickle=True)
    ls, Dl, lA = np.asarray(z['ls'], float), np.asarray(z['Dl'], float), float(z['l_A'])
    c = (Dl - envelope(Dl, W)) / envelope(Dl, W)
    q = ls / lA
    A, ctr = [], []
    for a, b in zip(QE[:-1], QE[1:]):
        m = (q >= a) & (q < b)
        A.append(float(np.sqrt((c[m] ** 2).mean())))
        ctr.append(0.5 * (a + b))
    A, ctr = np.array(A), np.array(ctr)
    # trend on bands 2..7 only, least squares in q
    p = np.polyfit(ctr[1:], A[1:], 1)
    S = float(A[0] - np.polyval(p, ctr[0]))
    s = S / float(A[1:].mean())
    return dict(lA=lA, A=A, S=S, s=s, trend_at_b1=float(np.polyval(p, ctr[0])), n=ls.size)


def main():
    print(__doc__)
    print("=" * 100)
    R = {}
    for arm, (dr, nd) in PAIRS.items():
        R[arm] = {'driven': step_of(dr), 'undriven': step_of(nd)}
        print(f"\n  {arm}")
        for k in ('driven', 'undriven'):
            r = R[arm][k]
            print(f"      {k:9s} l_A {r['lA']:.3f}  band rms " +
                  " ".join(f"{v:.5f}" for v in r['A']))
            print(f"                trend at band 1 {r['trend_at_b1']:.5f}   "
                  f"S {r['S']:+.6f}   s {r['s']:+.5f}")

    print("\n" + "=" * 100)
    print("  ⛭ P0 -- the PRECONDITION: the DRIVEN pair must show an UPWARD step on both arms")
    p0 = all(R[a]['driven']['S'] > 0 for a in R)
    for a in R:
        print(f"      {a:9s} driven S {R[a]['driven']['S']:+.6f}  "
              f"{'upward' if R[a]['driven']['S'] > 0 else 'NOT upward'}")
    if not p0:
        print("\n  ⛔ P0 FAILS: this grid and envelope do not reproduce the feature the question is")
        print("     about, so the test HAS NO SUBJECT and no verdict is reported. As registered.")
        print("=" * 100)
        return 1
    print("      ⇒ P0 holds, so the test has a subject.")

    print("\n  ⛭ THE READING: rho = |s_undriven| / |s_driven|, per arm")
    rho = {}
    for a in R:
        rho[a] = abs(R[a]['undriven']['s']) / abs(R[a]['driven']['s'])
        print(f"      {a:9s} s driven {R[a]['driven']['s']:+.5f}   "
              f"s undriven {R[a]['undriven']['s']:+.5f}   rho {rho[a]:.4f}")

    print("\n" + "=" * 100)
    if all(v <= 0.30 for v in rho.values()):
        print("  ⇒ ROW ONE: rho <= 0.30 on BOTH arms. ** THE DRIVING CARRIES THE LOWEST-BAND STEP. **")
        print("    Order item 3 opens: the sentence becomes a statement of where it is fixed --")
        print("    standard acoustic physics, shared by both arms.")
        row = 1
    elif any(v >= 0.70 for v in rho.values()):
        print("  ⛔ ROW TWO: rho >= 0.70 on an arm. ** THE DRIVING DOES NOT CARRY IT. **")
        for a in R:
            print(f"    {a}: {100*rho[a]:.1f} per cent of the step survives removing the driving.")
        print("    No sentence is drafted, as registered.")
        row = 2
    else:
        print("  ⇒ ROW THREE: 0.30 < rho < 0.70 on both arms. ** PARTIAL. **")
        for a in R:
            print(f"    {a}: {100*rho[a]:.1f} per cent survives.")
        print("    Nothing is claimed about authorship and no sentence is drafted, as registered.")
        row = 3
    print("=" * 100)
    json.dump({a: {'rho': rho[a], 's_driven': R[a]['driven']['s'],
                   's_undriven': R[a]['undriven']['s'],
                   'A_driven': list(R[a]['driven']['A']),
                   'A_undriven': list(R[a]['undriven']['A'])} for a in R} | {'row': row},
              open('driving_step_result.json', 'w'), indent=1)
    return 0


if __name__ == '__main__':
    sys.exit(main())
