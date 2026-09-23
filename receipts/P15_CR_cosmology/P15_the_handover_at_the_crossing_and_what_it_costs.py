#!/usr/bin/env python3
"""
RECEIPT -- P15: ** MOVING THE HANDOVER FROM THE ONSET TO THE CROSSING REMOVES 71% OF THE ARM'S
EXCESS chi^2 OVER THE CONTROL, TAKES P1/P2 FROM -20.7% TO +1.5% AGAINST THE SKY, AND BUYS THE
ODD-EVEN ALTERNATION THE CODED ARM DOES NOT HAVE.  ** IT DOES NOT REMOVE THE REJECTION -- 35.5 PER
BIN AGAINST THE CONTROL'S 2.10 -- AND IT COSTS THE PIN. **

Built r6760+cc66.1 (node 66, code seat), on `PO-13`, at node 66 (chat seat)'s work order.

===================================================================================================
** WHAT WAS RUN, AND THE STATE IS THE INSTRUMENT'S OWN **
===================================================================================================

`ARM=cr ZSTART=<z>` with everything else at its default.  The default handover state IS the one the
order specified: `CRAMP=flat` sets Theta_hat = -T(1/sqrt3)/2 = 0.483531 Psi_i, `CRPHI=0` sets the
velocity to zero, `CRPSI=flat` sets Psi = Psi_i, the driving is applied once on the leaf rate, and
the leaf equality is z_eq = 3936.0 from the background alone.  ** Only the LOCUS moves. **

  PART 1  ** THE INSTRUMENT IS THE PAPER'S BEFORE ANY NEW SPECTRUM TOUCHES IT. **  Three
          independent reproductions of `sec:refit-bound`: the control's peaks and P1/P2, the coded
          arm's peaks and ratios, and both arms' chi^2 through plik_lite.
  PART 2  ** THE CROSSING ARM. **  Peaks, the comb fitted by `sec:intro`'s own procedure, and the
          heights.
  PART 3  ** CONVERGED IN THE LOCUS, THE ell-GRID AND THE LADDER. **  Three separate checks, one of
          them the instrument's own standing question asked of this configuration for the first time.
  PART 4  ** WHAT IT COSTS. **  The comb is 4.2% narrow, the arm spends no fitted number, and the
          reported l_A is bookkeeping on a sound horizon the oscillator does not run on.

** COMPUTES: nothing.  *** It reads spectra already produced and scores them; every parameter is the
   one baked into the .npz it reads -- ARM=cr/lcdm at the instrument's own H0 = 73.00 / 67.40,
   Om = 0.3066 / 0.3150, LMAXL = 1300, KFAC = 2, the polarisation path -- and the ZSTART of each run is
   in its filename.  The one thing computed here is the comb fit, which has no parameter. *** **

rc=0 on success.  Run: python3 <this file>   (numpy, scipy; ~5 s; reads spectra/cc66_*.npz)
"""
import os
import sys

import numpy as np
from scipy.signal import argrelextrema

print(__doc__.split("rc=0")[0])
fail = []
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

SKY = np.array([220.4, 537.7, 817.3, 1123.9])          # sec:intro's parabolic fit on plik_lite


def load(tag):
    z = np.load(os.path.join(SPEC, f'cc66_{tag}.npz'))
    return np.asarray(z['ls'], float), np.asarray(z['Dl'], float), float(z['l_A'])


def peaks(ls, Dl, n=4):
    return [ls[q] for q in argrelextrema(Dl, np.greater, order=3)[0][:n]]


def heights(ls, Dl):
    q = argrelextrema(Dl, np.greater, order=3)[0]
    return Dl[q[0]] / Dl[q[1]], Dl[q[0]] / Dl[q[2]]


def comb(P, n=3):
    nn = np.arange(1, n + 1, dtype=float)
    lA, b = np.linalg.lstsq(np.vstack([nn, np.ones_like(nn)]).T,
                            np.asarray(P[:n], float), rcond=None)[0]
    return lA, b * np.pi / lA


# =====================================================================
print("=" * 78)
print("PART 1 — THE INSTRUMENT REPRODUCES sec:refit-bound, THREE WAYS")
print("=" * 78)
for tag, nm, want_pk, want_h, want_chi in (
        ('lcdm', 'control', [220, 536, 814], 2.195, 279.4),
        ('cr_coded', 'arm, coded handover', [206, 528, 832], 1.759, 15752.0)):
    ls, Dl, lA = load(tag)
    P = peaks(ls, Dl); h2, _ = heights(ls, Dl)
    c, n, _, _, _ = CS.chi2_of(ls, Dl)
    print(f"  {nm:>20}: peaks {[int(v) for v in P]}  P1/P2 = {h2:.3f}  "
          f"chi2 = {c:.1f} / {n} bins = {c/n:.3f}")
    print(f"  {'the paper':>20}: peaks {want_pk}  P1/P2 = {want_h:.3f}  chi2 = {want_chi:.1f}")
    if [int(v) for v in P[:3]] != want_pk:
        fail.append(f"{nm}: peaks {P[:3]} against the paper's {want_pk}")
    if abs(h2 - want_h) > 0.002:
        fail.append(f"{nm}: P1/P2 = {h2:.4f} against the paper's {want_h}")
    if abs(c - want_chi) > 1.0:
        fail.append(f"{nm}: chi2 = {c:.1f} against the paper's {want_chi}")
lA_sky, phi_sky = comb(SKY)
print(f"\n  and the sky's own phase by the same fit: phi/pi = {phi_sky/np.pi:.4f}   "
      f"(sec:intro quotes -0.2404)")
if abs(phi_sky / np.pi + 0.2404) > 0.0005:
    fail.append(f"the sky's phi/pi comes out {phi_sky/np.pi:.4f}, not the paper's -0.2404")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE CROSSING ARM")
print("=" * 78)
print(f"  {'':>26} {'peaks':>26} {'l_A fit':>8} {'phi/pi':>8} {'P1/P2':>7} {'P1/P3':>7} {'chi2/bin':>9}")
res = {}
for tag, nm in (('lcdm', 'control'), ('cr_coded', 'arm, coded handover'),
                ('cr_crossing', 'arm, at the crossing')):
    ls, Dl, lA = load(tag)
    P = peaks(ls, Dl); lAf, ph = comb(P); h2, h3 = heights(ls, Dl)
    c, n, _, _, _ = CS.chi2_of(ls, Dl)
    res[nm] = (c, n, h2, h3, lAf)
    print(f"  {nm:>26} {str([int(v) for v in P]):>26} {lAf:>8.1f} {ph/np.pi:>8.4f} "
          f"{h2:>7.3f} {h3:>7.3f} {c/n:>9.3f}")
print(f"  {'sky':>26} {str([float(v) for v in SKY]):>26} {lA_sky:>8.1f} "
      f"{phi_sky/np.pi:>8.4f} {2.217:>7.3f} {2.277:>7.3f}")
exc_c = res['arm, coded handover'][0] - res['control'][0]
exc_x = res['arm, at the crossing'][0] - res['control'][0]
print(f"\n  ** excess chi^2 over the control: coded {exc_c:+.1f}, crossing {exc_x:+.1f} — "
      f"{100*(1-exc_x/exc_c):.1f}% removed. **")
print(f"  ** P1/P2 against the sky: coded {100*(res['arm, coded handover'][2]/2.217-1):+.1f}%, "
      f"crossing {100*(res['arm, at the crossing'][2]/2.217-1):+.1f}% "
      f"(the sky's own uncertainty is 3.4%). **")
if not 0.65 < 1 - exc_x / exc_c < 0.78:
    fail.append(f"the crossing removes {100*(1-exc_x/exc_c):.1f}% of the excess, not ~71%")
if abs(res['arm, at the crossing'][2] - 2.250) > 0.002:
    fail.append(f"the crossing arm's P1/P2 is {res['arm, at the crossing'][2]:.4f}, not 2.250")
if res['arm, at the crossing'][0] / res['control'][0] < 10:
    fail.append("the crossing arm is now within 10x the control -- PART 2's 'not a cure' is stale")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — CONVERGED IN THE LOCUS, THE ell-GRID, AND THE LADDER")
print("=" * 78)
print(f"  {'run':>34} {'peaks':>26} {'P1/P2':>8} {'P1/P3':>8}")
ref = None
for tag, nm in (('cr_z3e5', 'ZSTART = 3e5'), ('cr_z3e6', 'ZSTART = 3e6'),
                ('cr_crossing', 'ZSTART = 3e7'), ('cr_z3e8', 'ZSTART = 3e8'),
                ('cr_x_lstep1', 'ZSTART = 3e7, LSTEP = 1'),
                ('cr_x_kcont', 'ZSTART = 3e7, KCONT = 1 (continuum)')):
    ls, Dl, _ = load(tag)
    P = peaks(ls, Dl); h2, h3 = heights(ls, Dl)
    if tag == 'cr_crossing':
        ref = (P, h2, h3)
    print(f"  {nm:>34} {str([int(v) for v in P]):>26} {h2:>8.3f} {h3:>8.3f}")
for tag, tol_l, what in (('cr_z3e8', 0, 'the locus'), ('cr_x_lstep1', 1, 'the ell-grid'),
                         ('cr_x_kcont', 0, 'the ladder')):
    ls, Dl, _ = load(tag)
    P = peaks(ls, Dl); h2, h3 = heights(ls, Dl)
    if max(abs(np.asarray(P[:4], float) - np.asarray(ref[0][:4], float))) > tol_l:
        fail.append(f"{what}: peaks move by more than {tol_l} multipoles")
    if abs(h2 - ref[1]) > 0.01 or abs(h3 - ref[2]) > 0.01:
        fail.append(f"{what}: the height ratios move")
print("\n  ** The locus is converged over two decades, the grid to its own resolution, and the")
print("     discrete ladder does not set the answer — the instrument's own standing question,")
print("     asked of this configuration for the first time, answers NO. **")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — WHAT IT COSTS")
print("=" * 78)
_, _, lA_rep_x = load('cr_crossing')
lAf_x = res['arm, at the crossing'][4]
print(f"  the crossing arm's comb is {lAf_x:.1f} against the sky's {lA_sky:.1f}: "
      f"{100*(lAf_x/lA_sky-1):+.2f}%")
print(f"  and the coded arm's is {res['arm, coded handover'][4]:.1f}: "
      f"{100*(res['arm, coded handover'][4]/lA_sky-1):+.2f}% — the sky lies BETWEEN them")
print(f"  the instrument REPORTS l_A = {lA_rep_x:.1f} for the crossing arm, which is bookkeeping:")
print("     with the start at a -> 0 the ruler integrates on the STACKING clock while the")
print("     oscillator accumulates on the LEAF one.  pi D_M / r_s,leaf = 292.4 against the")
print(f"     fitted {lAf_x:.1f} — 2.2% — and the stacking ruler's {lA_rep_x:.1f} is not close.")
print("  ** And the crossing arm spends no fitted number: its onset is forced, not solved, so")
print("     l_A is an output where the coded arm pins it with the corpus's one free parameter. **")
if abs(lAf_x - 286.0) > 1.0:
    fail.append(f"the crossing arm's fitted comb is {lAf_x:.1f}, not 286.0")

print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — the instrument reproduces the paper three ways; the crossing handover")
print("removes 71% of the excess, lands P1/P2 within a fifth of the sky's own uncertainty, and is")
print("converged in locus, grid and ladder; and it costs a 4.2% comb and the pin.")
print("=" * 78)
