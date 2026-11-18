#!/usr/bin/env python3
r"""r7827 (cc66) -- the adjudicated endpoint refitted on an INDEPENDENTLY CONSTRUCTED arm.

Cross-checks r7826 (60)'s deciding number.  Predictions registered in PREDICTION.md BEFORE this
file existed.  Usage:  python3 cross_check.py <arm> [budget]   with arm in
  lcdm_a21 | adj_a100 | adj_a170 | row_a21     -- each banked idempotently to out/fit_<arm>.npz
then  python3 cross_check.py report.

Every arm here holds A_s9 at 2.1 because block_chi2 profiles one amplitude per block
analytically: a common scale is EXACTLY marginalised, so A_s9 carries no information.  r7826 holds
it at 2.1 for the same reason; r7823 let it float and misread its drift to the box edge as a
boundary pathology.  Prediction (4) measures the degeneracy rather than asserting it.
"""
import json
import os
import re
import sys

import numpy as np
from scipy.optimize import minimize

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall',
                                'r7823_cc66_PO24_the_joint_best_fit'))
import fit_joint as FJ                                                     # noqa: E402

OUT = os.path.join(HERE, 'out')
os.makedirs(OUT, exist_ok=True)
AS9_FIXED = 2.1                       # held, not fitted -- exactly degenerate; see (4)
CHI2_R7823_LCDM = 113.17391783140775  # r7823's own LCDM best fit, A_s9 floating
PAPER = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')

# ** THE CONFIGURATION IS PARSED OUT OF THE PAPER, with r7826's own two spans. **
_SRC = open(PAPER, encoding='utf-8').read()
_m_adj = re.search(r"visibility peak, \$r=(\d+\.\d+)\$", _SRC)
_m_alp = re.search(r"\\alpha=(\d+\.\d+)\$ the instrument", _SRC)
R_ADJ = float(_m_adj.group(1)) if _m_adj else float('nan')
ALPHA_PAPER = float(_m_alp.group(1)) if _m_alp else float('nan')


def dl_of(pv4):
    """The four informative parameters -> an unsuppressed theory D_l, plus its own l_D."""
    H0, ombh2, omch2, ns = pv4
    d, dp = FJ.run(H0, ombh2, omch2, AS9_FIXED * 1e-9, ns)
    dl = d[2:FJ.LMAX + 1, 0].copy()
    _, _, lD = FJ.cr_supp(d, dp, H0, ombh2, omch2)
    return d, dp, dl, float(lD)


def spectrum(pv4, arm):
    H0, ombh2, omch2, ns = pv4
    d, dp, dl, lD = dl_of(pv4)
    if arm == 'lcdm_a21':
        return dl, lD, float('nan')
    if arm == 'row_a21':
        s, r_row, lD2 = FJ.cr_supp(d, dp, H0, ombh2, omch2)
        return dl * s, float(lD2), float(r_row)
    alpha = 1.0 if arm == 'adj_a100' else ALPHA_PAPER
    return dl * np.exp(-alpha * (R_ADJ ** 2 - 1.0) * (FJ.LS / lD) ** 2), lD, R_ADJ


def objective(pv4, arm, n):
    H0, ombh2, omch2, ns = pv4
    if not (55 < H0 < 85 and 0.018 < ombh2 < 0.026 and 0.09 < omch2 < 0.16 and 0.85 < ns < 1.25):
        return 1e6
    try:
        n[0] += 1
        return FJ.joint_chi2_of(spectrum(pv4, arm)[0])[0]
    except Exception:
        return 1e6


def fit(arm, budget):
    dest = os.path.join(OUT, f'fit_{arm}.npz')
    if os.path.exists(dest):
        z = np.load(dest)
        print(f"  skip {arm} (done): chi2={float(z['fun']):.4f}  x={np.round(z['x'], 6)}")
        return
    print(f"  arm={arm}  Planck {int(FJ.P_KEEP.sum())} bins, ACT {int(FJ.A_KEEP.sum())} "
          f"bandpowers, A_s9 held at {AS9_FIXED}, budget {budget}")
    if arm == 'row_a21':
        x0 = [83.977742, 0.026000, 0.090297, 1.133791]      # r7823's own CR point, A_s9 dropped
    else:
        x0 = [69.734909, 0.022834, 0.114712, 0.981426]      # r7823's own LCDM point
    n = [0]
    r = minimize(objective, x0, args=(arm, n), method='Nelder-Mead',
                 options={'maxfev': budget, 'xatol': 2e-3, 'fatol': 0.2})
    dl, lD, rr = spectrum(r.x, arm)
    c, cp, ca, ap, aa = FJ.joint_chi2_of(dl)
    np.savez(dest, x=r.x, fun=float(r.fun), chi2=c, chi2_planck=cp, chi2_act=ca,
             amp_planck=ap, amp_act=aa, lD=lD, r=rr, nfev=n[0], as9=AS9_FIXED)
    print(f"  {arm}: chi2={c:.4f} (Planck {cp:.4f}/{int(FJ.P_KEEP.sum())}, "
          f"ACT {ca:.4f}/{int(FJ.A_KEEP.sum())})  x={np.round(r.x, 6)}  "
          f"lD={lD:.3f} r={rr:.6f}  after {n[0]} evals")


def degeneracy():
    """(4) Scale the WHOLE theory by 0.8 and 1.25; a per-block profiled amplitude must absorb it."""
    z = np.load(os.path.join(OUT, 'fit_lcdm_a21.npz'))
    dl = spectrum(z['x'], 'lcdm_a21')[0]
    base = FJ.joint_chi2_of(dl)[0]
    return base, max(abs(FJ.joint_chi2_of(dl * f)[0] - base) for f in (0.8, 1.25))


def report():
    Z = {a: np.load(os.path.join(OUT, f'fit_{a}.npz'))
         for a in ('lcdm_a21', 'adj_a100', 'adj_a170', 'row_a21')}
    C = {a: float(z['chi2']) for a, z in Z.items()}
    L = C['lcdm_a21']
    D = {a: C[a] - L for a in ('adj_a100', 'adj_a170', 'row_a21')}
    base, dmax = degeneracy()
    npt = int(FJ.P_KEEP.sum()) + int(FJ.A_KEEP.sum())

    print(f"\n  the paper's own two spans give  r = {R_ADJ}  alpha = {ALPHA_PAPER}")
    print(f"  arm: {int(FJ.P_KEEP.sum())} Planck bins + {int(FJ.A_KEEP.sum())} ACT bandpowers "
          f"= {npt} points   (r7826's arm: 150 bandpowers)")
    print(f"\n  {'configuration':<34}{'chi2':>10}{'Delta chi2':>13}   r7826's")
    print(f"  {'LCDM, A_s9 = 2.1':<34}{L:>10.4f}{'--':>13}   139.8557")
    print(f"  {'adjudicated, alpha 1.00':<34}{C['adj_a100']:>10.4f}"
          f"{D['adj_a100']:>+13.4f}   -1.2926")
    print(f"  {'adjudicated, alpha ' + f'{ALPHA_PAPER:.2f}':<34}{C['adj_a170']:>10.4f}"
          f"{D['adj_a170']:>+13.4f}   +9.0172")
    print(f"  {'the row-harness ratio':<34}{C['row_a21']:>10.4f}"
          f"{D['row_a21']:>+13.4f}   +631.3686")
    print(f"\n  (4) scaling the whole theory 0.8 and 1.25 moves the joint chi2 by {dmax:.3e}")
    print(f"  precondition: LCDM here {L:.4f} vs r7823's floating-A_s9 "
          f"{CHI2_R7823_LCDM:.4f}  |diff| = {abs(L - CHI2_R7823_LCDM):.4f}")

    P = [('PRECONDITION the two conventions are comparable, |dchi2| < 15',
          abs(L - CHI2_R7823_LCDM) < 15.0),
         ('(1) THE ONE THAT MATTERS: the sign reproduces, Delta chi2 < 0 at alpha 1',
          D['adj_a100'] < 0.0),
         ('(1) REGISTERED NEGATIVE did NOT fire (it fires if Delta chi2 > +4)',
          not D['adj_a100'] > 4.0),
         ('(2) level means level: |Delta chi2| < 10 at alpha 1', abs(D['adj_a100']) < 10.0),
         (f'(3) the exponent axis: 0 < Delta chi2 < 25 at alpha {ALPHA_PAPER:.2f}',
          0.0 < D['adj_a170'] < 25.0),
         ('(4) A_s is exactly degenerate: the scalings move chi2 by < 1e-6', dmax < 1e-6),
         ('(5) the excluded configuration stays excluded, Delta chi2 > 100',
          D['row_a21'] > 100.0)]
    print()
    for nm, ok in P:
        print(f"    {'HELD  ' if ok else 'FAILED'}   {nm}")
    arm_dep = D['adj_a100'] > 4.0
    print(f"\n  => r7826's NOT-EXCLUDED is {'ARM-DEPENDENT' if arm_dep else 'ARM-INDEPENDENT'} "
          f"on this arm.")
    print(f"  => (6) the statistic that decides is a REFIT, not a tilt distance: "
          f"{'YES' if (D['adj_a100'] < 0.0 and D['adj_a170'] > 0.0) else 'NOT AS REGISTERED'}")

    json.dump({'r_adjudicated': R_ADJ, 'alpha_paper': ALPHA_PAPER, 'n_points': npt,
               'chi2': C, 'dchi2': D, 'as9_fixed': AS9_FIXED,
               'degeneracy_max_shift': dmax, 'chi2_r7823_lcdm_floating': CHI2_R7823_LCDM,
               'x': {a: [float(v) for v in Z[a]['x']] for a in Z},
               'lD': {a: float(Z[a]['lD']) for a in Z},
               'nfev': {a: int(Z[a]['nfev']) for a in Z},
               'arm_dependent': bool(arm_dep),
               'predictions': {nm: bool(ok) for nm, ok in P}},
              open(os.path.join(OUT, 'r7827_adjudicated_endpoint_cross_check.json'), 'w'),
              indent=2, sort_keys=True)
    print("  wrote out/r7827_adjudicated_endpoint_cross_check.json")


if __name__ == '__main__':
    if sys.argv[1] == 'report':
        report()
    else:
        fit(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 400)
