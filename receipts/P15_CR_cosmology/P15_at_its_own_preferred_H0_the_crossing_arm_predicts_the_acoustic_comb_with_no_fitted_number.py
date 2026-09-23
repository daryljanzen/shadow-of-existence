#!/usr/bin/env python3
"""
RECEIPT -- P15: ** THE CROSSING ARM, WITH NO PIN, AT THE (H0, Om) ITS OWN RULER PREFERS, PUTS THE
ACOUSTIC COMB AT 298.0 AGAINST THE SKY'S 298.4 -- 0.13% -- AS AN OUTPUT.  P1/P2 = 2.264 AGAINST
2.217, P1/P3 = 2.298 AGAINST 2.277, AND THE GAP RATIOS AT 0.8861 AND 1.1286 AGAINST 0.8812 AND
1.0966.  ** chi^2 IS 4.19 PER BIN AGAINST THE CONTROL'S 2.10, WHERE THE CODED ARM IS 118.44. **

** ⇒ AND NO NUMBER IN THE SPECTRUM IS FITTED. **  The onset is forced -- the handover is at the
crossing, so there is nothing to solve -- `LATARG` is not used, and (H0, Om) = (68.60, 0.2973) come
from the DESI DR2 BAO + theta_* joint fit of r6760+cc66.2, not from TT.  ** The spectrum is
out-of-sample against the data that set the cosmology. **

⛔ ** IT IS STILL REJECTED AGAINST LCDM, 4.19 PER BIN AGAINST 2.10, AND THAT IS STATED AS THE
RESULT AND NOT AS A CAVEAT. **  What has changed is the size of the gap: a factor 2.0, where the
corpus's own configuration is a factor 56 and the same crossing arm at H0 = 73 is a factor 17.

Built r6760+cc66.7 (node 66, code seat), on `PO-13`, at node 66 (chat seat)'s work order:
"THE CROSSING ARM, NO PIN, AT H0 = 68.6 ... on that branch the comb should land on the sky's 298.4
as an OUTPUT, not a fit."

===================================================================================================
** WHAT IS SELF-CONSISTENT ABOUT THIS CONFIGURATION, STATED BEFORE ANY NUMBER **
===================================================================================================

Three choices, each made for its own reason and none for this one:

  ** THE HANDOVER AT THE CROSSING ** -- the branch point, where aH diverges and every mode is
  super-horizon, so the adiabatic datum is the correct one there (r6760+cc66.1).
  ** ONE CLOCK, THE LEAF CLOCK ** -- node 66 (chat)'s adjudication, for r_s and r_D together,
  because `sec:coherence`'s own consistency demand forbids splitting them.
  ** H0 = 68.60, Om = 0.2973 ** -- what the leaf ruler's joint DESI BAO fit returns, with theta_*
  alone returning 68.55 independently (r6760+cc66.2).

*The corpus runs the arm at H0 = 73.00, Om = 0.3066 -- the local distance-ladder value -- on a ruler
that prefers 68.6.  ** This receipt asks what the arm says when it is run at its own ruler's
answer. **  The three choices were made in three separate places for three unrelated reasons; that
they land together is the result.*

  PART 1  ** THE COMB, THE PHASE AND THE PEAKS. **  Against the sky and against the control.
  PART 2  ** THE HEIGHTS AND THE GAP RATIOS. **
  PART 3  ** THE LIKELIHOOD, BY BAND. **
  PART 4  ** BOTH INSTRUMENT PATHS, ** because they are not interchangeable and the paper's own
          height numbers are polarisation-path numbers.
  PART 5  ** WHAT IS NOT FITTED, ITEMISED, ** since the whole claim rests on it.
  PART 6  ** AND WHAT IS STILL WRONG. **

** COMPUTES: nothing.  *** It reads spectra already produced and scores them; every parameter is
   baked into the .npz it reads.  The runs are `ARM=cr CRH0=68.6 CROM=0.2973 ZSTART=3e7
   LEAFSCALES=1 LSTEP=2 LMAXL=1300`, with `HIER=1` for the polarisation path and absent for the
   fluid path.  The comb fit has no parameter and the likelihood fits one amplitude in closed
   form. *** **

rc=0 on success.  Run: python3 <this file>   (numpy, scipy; ~15 s; reads spectra/cc66_*.npz)
"""
import os
import sys

import numpy as np
import scipy.linalg
from scipy.signal import argrelextrema

print(__doc__.split("rc=0")[0])
fail = []
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

SKY = np.array([220.4, 537.7, 817.3, 1123.9])          # sec:intro's parabolic fit on plik_lite
SKY_P12, SKY_P13 = 2.217, 2.277
BANDS = ((100, 400), (400, 700), (700, 1000), (1000, 1300))


def fit_comb(pk, n=3):
    nn = np.arange(1, n + 1, dtype=float)
    A = np.vstack([nn, np.ones_like(nn)]).T
    lA, b = np.linalg.lstsq(A, np.asarray(pk[:n], float), rcond=None)[0]
    return float(lA), float(np.pi * b / lA)


def _F(keep):
    cov = CS.COV_TT[np.ix_(keep, keep)]
    M = scipy.linalg.cho_solve(scipy.linalg.cho_factor(cov), np.identity(int(keep.sum())))
    return 0.5 * (M + M.T)


def score(tag):
    z = np.load(os.path.join(SPEC, f'cc66_{tag}.npz'))
    ls, Dl = np.asarray(z['ls'], float), np.asarray(z['Dl'], float)
    q = argrelextrema(Dl, np.greater, order=3)[0][:4]
    P = [float(ls[i]) for i in q]
    H = [float(Dl[i]) for i in q]
    lA, phi = fit_comb(P)
    mb = CS.bin_spectrum(ls, Dl)
    ok = np.isfinite(mb)
    Fg = _F(ok)
    m, d = mb[ok], CS.X_DATA[ok]
    A = float((m @ Fg @ d) / (m @ Fg @ m))
    chi2 = float((d - A * m) @ Fg @ (d - A * m))
    bands = {}
    for lo, hi in BANDS:
        inb = ok & (CS.BIN_LO >= lo) & (CS.BIN_HI <= hi)
        r = CS.X_DATA[inb] - A * mb[inb]
        bands[(lo, hi)] = float(r @ _F(inb) @ r) / int(inb.sum())
    g = np.diff(np.asarray(P, float))
    return dict(P=P, lA=lA, phi=phi, p12=H[0] / H[1], p13=H[0] / H[2], chi2=chi2,
                n=int(ok.sum()), bands=bands, g21=g[1] / g[0], g32=g[2] / g[1],
                lA_rep=float(z['l_A']), r_s=float(z['r_s']), D_M=float(z['D_M']))


CTL = score('lcdm')
CODED = score('cr_coded')
X73 = score('cr_crossing')
NEW = score('cr_x_h686_pol')
NEWF = score('cr_x_h686_fluid')
PIN = score('cr_leafpin')
PINF = score('cr_leafpin_fluid')
lA_sky, phi_sky = fit_comb(SKY)

print("=" * 112)
print("  PART 1 -- ** THE COMB, THE PHASE AND THE PEAKS **")
print("=" * 112)
print(f"  {'configuration':>34} {'l_A rep':>8} {'peaks':>26} {'fitted comb':>12} {'phi/pi':>8} "
      f"{'l1/lA':>7}")
for nm, s in (('control (LCDM)', CTL), ('the arm as coded, H0 = 73.0', CODED),
              ('crossing, H0 = 73.0', X73), ('** crossing, H0 = 68.6 **', NEW),
              ('run 1, the pin', PIN)):
    print(f"  {nm:>34} {s['lA_rep']:>8.1f} {str([int(v) for v in s['P']]):>26} {s['lA']:>12.1f} "
          f"{s['phi'] / np.pi:>8.4f} {s['P'][0] / s['lA']:>7.4f}")
print(f"  {'THE SKY':>34} {301.7:>8.1f} {str([float(v) for v in SKY]):>26} {lA_sky:>12.1f} "
      f"{phi_sky / np.pi:>8.4f} {SKY[0] / lA_sky:>7.4f}")
d_comb = abs(NEW['lA'] / lA_sky - 1)
print(f"\n  ⌗ the comb is off by {d_comb * 100:.2f}%, against {abs(X73['lA'] / lA_sky - 1) * 100:.1f}% "
      f"at H0 = 73 and {abs(CODED['lA'] / lA_sky - 1) * 100:.1f}% as coded")
print(f"  ⌗ and the RULER and the SPECTRUM now nearly agree: reported l_A = {NEW['lA_rep']:.1f} "
      f"against a fitted comb of {NEW['lA']:.1f}, {abs(NEW['lA_rep'] / NEW['lA'] - 1) * 100:.1f}%")
print(f"    *at H0 = 73 the same two were {X73['lA_rep']:.1f} and {X73['lA']:.1f}, "
      f"{abs(X73['lA_rep'] / X73['lA'] - 1) * 100:.0f}% apart -- so this is not bookkeeping agreeing"
      f" with itself*")
if d_comb > 0.01:
    fail.append(f"the comb is {d_comb * 100:.2f}% off, not sub-per-cent -- it did not land")
if abs(NEW['lA_rep'] / NEW['lA'] - 1) > 0.04:
    fail.append("the reported ruler and the fitted comb still disagree by more than 4%")

print()
print("=" * 112)
print("  PART 2 -- ** THE HEIGHTS AND THE GAP RATIOS **")
print("=" * 112)
print(f"  {'configuration':>34} {'P1/P2':>8} {'vs sky':>8} {'P1/P3':>8} {'vs sky':>8} "
      f"{'g2/g1':>8} {'g3/g2':>8}")
for nm, s in (('control (LCDM)', CTL), ('the arm as coded, H0 = 73.0', CODED),
              ('crossing, H0 = 73.0', X73), ('** crossing, H0 = 68.6 **', NEW),
              ('run 1, the pin', PIN)):
    print(f"  {nm:>34} {s['p12']:>8.3f} {(s['p12'] / SKY_P12 - 1) * 100:>+7.1f}% {s['p13']:>8.3f} "
          f"{(s['p13'] / SKY_P13 - 1) * 100:>+7.1f}% {s['g21']:>8.4f} {s['g32']:>8.4f}")
g_sky = np.diff(SKY)
print(f"  {'THE SKY':>34} {SKY_P12:>8.3f} {'':>8} {SKY_P13:>8.3f} {'':>8} "
      f"{g_sky[1] / g_sky[0]:>8.4f} {g_sky[2] / g_sky[1]:>8.4f}")
for lab, got, want, tol in (('P1/P2', NEW['p12'], SKY_P12, 0.05),
                            ('P1/P3', NEW['p13'], SKY_P13, 0.05),
                            ('g2/g1', NEW['g21'], g_sky[1] / g_sky[0], 0.03),
                            ('g3/g2', NEW['g32'], g_sky[2] / g_sky[1], 0.05)):
    if abs(got / want - 1) > tol:
        fail.append(f"{lab} = {got:.4f} against the sky's {want:.4f}, "
                    f"{abs(got / want - 1) * 100:.1f}% -- outside {tol * 100:.0f}%")

print()
print("=" * 112)
print("  PART 3 -- ** THE LIKELIHOOD, BY BAND **")
print("=" * 112)
print(f"  {'configuration':>34} {'chi2':>9} {'/bin':>7} " +
      " ".join(f"{f'{lo}-{hi}':>10}" for lo, hi in BANDS))
for nm, s in (('control (LCDM)', CTL), ('the arm as coded, H0 = 73.0', CODED),
              ('crossing, H0 = 73.0', X73), ('** crossing, H0 = 68.6 **', NEW),
              ('run 1, the pin', PIN)):
    print(f"  {nm:>34} {s['chi2']:>9.1f} {s['chi2'] / s['n']:>7.2f} " +
          " ".join(f"{s['bands'][b]:>10.2f}" for b in BANDS))
print(f"""
  ⇒ ** EVERY BAND IS WITHIN A FACTOR {max(NEW['bands'][b] / CTL['bands'][b] for b in BANDS):.1f} OF THE CONTROL'S, ** the
  700-1000 band included -- and that band is the one that survived the crossing handover, the
  equality scan and the pin alike.  It goes {X73['bands'][(700, 1000)]:.1f} -> {NEW['bands'][(700, 1000)]:.2f} per bin here.""")
if NEW['chi2'] / NEW['n'] > 6.0:
    fail.append(f"chi^2 is {NEW['chi2'] / NEW['n']:.2f} per bin, not the ~4 claimed")
if NEW['bands'][(700, 1000)] > 0.15 * X73['bands'][(700, 1000)]:
    fail.append("the 700-1000 band did not collapse -- the headline overstates it")
for b in BANDS:
    if NEW['bands'][b] > 4.0 * CTL['bands'][b]:
        fail.append(f"band {b} is {NEW['bands'][b] / CTL['bands'][b]:.1f}x the control, not within 4x")

print()
print("=" * 112)
print("  PART 4 -- ** BOTH INSTRUMENT PATHS **")
print("=" * 112)
print(f"  {'':>26} {'peaks':>26} {'comb':>7} {'P1/P2':>8} {'P1/P3':>8} {'chi2/bin':>9}")
for nm, s in (('H0 = 68.6, POLARISATION', NEW), ('H0 = 68.6, FLUID', NEWF),
              ('run 1 pin, POLARISATION', PIN), ('run 1 pin, FLUID', PINF)):
    print(f"  {nm:>26} {str([int(v) for v in s['P']]):>26} {s['lA']:>7.1f} {s['p12']:>8.3f} "
          f"{s['p13']:>8.3f} {s['chi2'] / s['n']:>9.2f}")
print(f"""
  ** THE COMB IS PATH-INDEPENDENT AND THE HEIGHTS ARE NOT, which is this instrument's standing
  behaviour and not a new caveat. **  The fitted comb is {NEW['lA']:.1f} on both paths.  The heights
  are {NEW['p12']:.3f}/{NEW['p13']:.3f} on the polarisation path and {NEWF['p12']:.3f}/{NEWF['p13']:.3f} on the fluid path,
  and the fluid path already overshot at H0 = 73 -- so moving H0 did not cause that and cannot cure
  it.  *`sec:refit-bound`'s height numbers are polarisation-path numbers, so the comparison above is
  the like-for-like one.*  ⇒ ** The COMB result is path-proof; the HEIGHT result is not, and is
  reported as polarisation-path specific. **""")
if abs(NEWF['lA'] - NEW['lA']) > 2.0:
    fail.append("the comb is NOT path-independent -- PART 4's claim is wrong")

print()
print("=" * 112)
print("  PART 5 -- ** WHAT IS NOT FITTED, ITEMISED **")
print("=" * 112)
print("""
  ** z_onset ** -- not solved.  The handover is at the crossing, `ZSTART=3e7`, and `LATARG` is
     never reached: `brentq` does not run.  *The corpus calls z_onset "the one fitted number";
     this configuration does not spend it.*
  ** l_A **      -- not pinned.  It is REPORTED as pi D_M / r_s and comes out 302.9; the comb is
     fitted to the spectrum's own peaks and comes out 298.0.  Two independent quantities, 1.6%
     apart.
  ** A_s **      -- one amplitude, fitted in closed form by the likelihood, as for every arm and
     the control alike.  *That is the only fitted number anywhere in these rows.*
  ** H0, Om **   -- (68.60, 0.2973) from DESI DR2 BAO on the leaf ruler with theta_*, r6760+cc66.2.
     ⚠ *These ARE fitted -- to BAO and the acoustic angle, not to TT.  So the cosmology is not
     parameter-free; what is out-of-sample is the SPECTRUM against the data that set it.*
""")

print("=" * 112)
print("  PART 6 -- ** AND WHAT IS STILL WRONG **")
print("=" * 112)
print(f"""
  ⛔ ** {NEW['chi2'] / NEW['n']:.2f} PER BIN AGAINST THE CONTROL'S {CTL['chi2'] / CTL['n']:.2f}. **  A factor
  {NEW['chi2'] / CTL['chi2']:.1f}.  *That is the result, not a caveat on it: this construction is still
  disfavoured against flat LCDM on this data.*  What changed is the SIZE: the coded arm is a factor
  {CODED['chi2'] / CTL['chi2']:.0f} and the same crossing arm at H0 = 73 is a factor {X73['chi2'] / CTL['chi2']:.0f}.

  ⌗ ** THE PHASE IS THE LARGEST SURVIVING POSITION ERROR: ** {NEW['phi'] / np.pi:.4f} pi against the
  sky's {phi_sky / np.pi:.4f} pi, {abs(NEW['phi'] / phi_sky - 1) * 100:.1f}%, where the comb is {d_comb * 100:.2f}%.
  *`sec:refit-bound`'s standing finding is that the spacing is right and the acoustic phase is the
  disagreement; on this configuration that is still true, and it is now the ONLY thing left in the
  positions.*

  ⌗ ** AND THE CONFIGURATION IS THE 133-BIN UNLENSED ONE AT LMAXL = 1300. **  The corpus's own
  185-bin full-range lensed comparison needs ell ~ 2000 and is not run here.  *A number scored on
  one configuration may not be quoted against the other.*
""")

print("=" * 112)
if fail:
    print("  FAILED:")
    for f in fail:
        print(f"    - {f}")
    sys.exit(1)
print("  ✓ ALL CHECKS PASSED")
print("=" * 112)
