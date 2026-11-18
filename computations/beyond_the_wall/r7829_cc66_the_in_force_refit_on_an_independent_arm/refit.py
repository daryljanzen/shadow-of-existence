#!/usr/bin/env python3
r"""r7829 (cc66) -- PO-24's discharge test: the in-force refit on an independently built arm.

Order r7827 (69): refit on this arm at r = 0.9918 with the IN-FORCE lD = 1489.5783 at exponent ONE
-- the configuration 60's -2.37 is at -- and report Delta chi2 against this arm's own LCDM, at an
interior minimum.  PO-24's clause is now "decided by a refit, discharged when the refit at the
adjudicated configuration reproduces on a second, independently built arm", so this IS that test.

** lD IS HELD FIXED, NOT RECOMPUTED. **  That is the whole correction r7828 (60) made: alpha = 1.70
is already folded into the in-force length (1951.9/sqrt(1.70) = 1497.0390, then 1489.5783 after the
one-rate move), so a per-trial lD is a DIFFERENT estimator and multiplying by 1.70 on top of the
in-force one double-counts.  r7826 did the latter and my own r7827 reported the result as an 8.53x
arm-sensitivity; both figures are withdrawn.  Prediction (5) measures the difference between the two
estimators on this arm rather than restating the guard.

Usage:  python3 refit.py fit [budget]   then   python3 refit.py report
"""
import json
import os
import sys

import numpy as np
from scipy.optimize import minimize

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall',
                                'r7823_cc66_PO24_the_joint_best_fit'))
import fit_joint as FJ                                                     # noqa: E402

R7827 = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                     'r7827_cc66_the_adjudicated_endpoint_on_an_independent_arm', 'out')
OUT = os.path.join(HERE, 'out')
os.makedirs(OUT, exist_ok=True)

# ** 60's OWN CONSTANTS, not re-derived. **
R_ADJ = 0.9918
LD_INFORCE = 1489.5783          # alpha = 1.70 in force, after the one-rate move
AS9_FIXED = 2.1                 # exactly degenerate under a per-block profiled amplitude (r7827 (4))
R7828_DCHI2 = -2.36972560954473
R7828_X = (67.39337020608676, 0.022091501807431704, 0.11885431725984463, 0.9592842521281604)
R7827_PERTRIAL_DCHI2 = -3.599591356781957      # the per-trial-lD arm, for prediction (5)
BOX = dict(H0=(55.0, 85.0), ombh2=(0.018, 0.026), omch2=(0.09, 0.16), ns=(0.85, 1.25))


def spectrum(pv4):
    """The theory D_l with the suppression at FIXED in-force lD -- lD is never recomputed here."""
    H0, ombh2, omch2, ns = pv4
    d, _ = FJ.run(H0, ombh2, omch2, AS9_FIXED * 1e-9, ns)
    dl = d[2:FJ.LMAX + 1, 0].copy()
    return dl * np.exp(-1.0 * (R_ADJ ** 2 - 1.0) * (FJ.LS / LD_INFORCE) ** 2)


def objective(pv4, n):
    n[0] += 1
    H0, ombh2, omch2, ns = pv4
    if not (BOX['H0'][0] < H0 < BOX['H0'][1] and BOX['ombh2'][0] < ombh2 < BOX['ombh2'][1]
            and BOX['omch2'][0] < omch2 < BOX['omch2'][1] and BOX['ns'][0] < ns < BOX['ns'][1]):
        return 1e6
    try:
        n[1] += 1
        return FJ.joint_chi2_of(spectrum(pv4))[0]
    except Exception:
        return 1e6


def fit(budget):
    dest = os.path.join(OUT, 'fit_inforce.npz')
    if os.path.exists(dest):
        z = np.load(dest)
        print(f"  skip (done): chi2={float(z['chi2']):.4f}  x={np.round(z['x'], 6)}")
        return
    print(f"  arm: Planck {int(FJ.P_KEEP.sum())} bins + ACT {int(FJ.A_KEEP.sum())} bandpowers "
          f"= {int(FJ.P_KEEP.sum()) + int(FJ.A_KEEP.sum())} points")
    print(f"  configuration: r = {R_ADJ}, lD = {LD_INFORCE} HELD FIXED, exponent one, "
          f"A_s9 = {AS9_FIXED}")
    # start from this arm's own LCDM point, nudged well inside every bound
    x0 = [68.988922, 0.022681, 0.116120, 0.977116]
    n = [0, 0]
    r = minimize(objective, x0, args=(n,), method='Nelder-Mead',
                 options={'maxfev': budget, 'xatol': 2e-3, 'fatol': 0.2})
    c, cp, ca, ap, aa = FJ.joint_chi2_of(spectrum(r.x))
    np.savez(dest, x=r.x, fun=float(r.fun), chi2=c, chi2_planck=cp, chi2_act=ca,
             amp_planck=ap, amp_act=aa, nfev=n[0], nfev_inbounds=n[1],
             r=R_ADJ, lD=LD_INFORCE, as9=AS9_FIXED)
    print(f"  chi2={c:.4f} (Planck {cp:.4f}, ACT {ca:.4f})  x={np.round(r.x, 6)}  "
          f"after {n[0]} evals ({n[1]} in bounds)")


def report():
    z = np.load(os.path.join(OUT, 'fit_inforce.npz'))
    lc = np.load(os.path.join(R7827, 'fit_lcdm_a21.npz'))
    CHI2 = float(z['chi2'])
    LCDM = float(lc['chi2'])
    D = CHI2 - LCDM
    X = [float(v) for v in z['x']]
    names = ['H0', 'ombh2', 'omch2', 'ns']
    # ** INTERIOR: the order requires it.  A minimum on an edge is a LIMIT. **
    edge = [f"{nm}={X[i]:.6f} on {BOX[nm]}" for i, nm in enumerate(names)
            if min(abs(X[i] - BOX[nm][0]), abs(X[i] - BOX[nm][1]))
            < 1e-4 * max(1.0, abs(BOX[nm][1] - BOX[nm][0]))]
    npt = int(FJ.P_KEEP.sum()) + int(FJ.A_KEEP.sum())

    print(f"\n  arm: {npt} points        (r7828's arm: 150)")
    print(f"  r = {R_ADJ}   lD = {LD_INFORCE} held fixed   exponent one   A_s9 = {AS9_FIXED}")
    print(f"\n  {'':34}{'this arm':>12}{'r7828 (60)':>14}")
    print(f"  {'the construction, refitted':<34}{CHI2:>12.4f}{137.4859:>14.4f}")
    print(f"  {'LCDM on the same arm':<34}{LCDM:>12.4f}{139.8557:>14.4f}")
    print(f"  {'Delta chi2':<34}{D:>+12.4f}{R7828_DCHI2:>+14.4f}")
    print(f"  {'H0':<34}{X[0]:>12.4f}{R7828_X[0]:>14.4f}")
    print(f"  {'n_s':<34}{X[3]:>12.6f}{R7828_X[3]:>14.6f}")
    print(f"\n  interior? {'YES -- no parameter on a box edge' if not edge else 'NO: ' + '; '.join(edge)}")
    print(f"  evals {int(z['nfev'])} ({int(z['nfev_inbounds'])} in bounds)")
    print(f"\n  (5) the two lD estimators: in-force {D:+.4f} vs per-trial "
          f"{R7827_PERTRIAL_DCHI2:+.4f}, apart by {abs(D - R7827_PERTRIAL_DCHI2):.4f}")

    P = [('PRECONDITION the LCDM reference is r7827\'s, within 0.5', abs(LCDM - 114.8370) < 0.5),
         ('(1) THE DISCHARGE: the sign reproduces, Delta chi2 < 0', D < 0.0),
         ('(1) REGISTERED NEGATIVE did NOT fire (it fires if Delta chi2 > 0)', not D > 0.0),
         ('(2) it reproduces in SIZE: |Delta chi2 - (-2.3697)| < 2.0',
          abs(D - R7828_DCHI2) < 2.0),
         ('(3) INTERIOR: no parameter on a box edge', not edge),
         ('(4) the two arms land on the same point: |dH0| < 2.5, |dn_s| < 0.025',
          abs(X[0] - R7828_X[0]) < 2.5 and abs(X[3] - R7828_X[3]) < 0.025),
         ('(5) the two lD estimators are different objects, apart by > 0.3',
          abs(D - R7827_PERTRIAL_DCHI2) > 0.3)]
    print()
    for nm, ok in P:
        print(f"    {'HELD  ' if ok else 'FAILED'}   {nm}")
    repro = D < 0.0 and abs(D - R7828_DCHI2) < 2.0 and not edge
    print(f"\n  => the refit {'REPRODUCES' if repro else 'DOES NOT REPRODUCE'} on this second, "
          f"independently built arm.")
    print(f"  => so PO-24, by its rewritten clause, is {'DISCHARGED' if repro else 'NOT discharged'}"
          f" -- 69's to strike.")
    print(f"  ⌗ and what this is NOT: {D:+.4f} on {npt} points is two models LEVEL, not a "
          f"preference for either.")

    json.dump({'chi2': CHI2, 'chi2_planck': float(z['chi2_planck']),
               'chi2_act': float(z['chi2_act']),
               'chi2_lcdm': LCDM, 'dchi2': D, 'x': X, 'edge': edge,
               'r': R_ADJ, 'lD': LD_INFORCE, 'as9': AS9_FIXED, 'n_points': npt,
               'nfev': int(z['nfev']), 'nfev_inbounds': int(z['nfev_inbounds']),
               'r7828_dchi2': R7828_DCHI2, 'r7827_pertrial_dchi2': R7827_PERTRIAL_DCHI2,
               'estimators_apart': abs(D - R7827_PERTRIAL_DCHI2),
               'reproduces': bool(repro), 'predictions': {nm: bool(ok) for nm, ok in P}},
              open(os.path.join(OUT, 'r7829_in_force_refit.json'), 'w'), indent=2, sort_keys=True)
    print("  wrote out/r7829_in_force_refit.json")


if __name__ == '__main__':
    if sys.argv[1] == 'report':
        report()
    else:
        fit(int(sys.argv[2]) if len(sys.argv) > 2 else 600)
