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


def check(label, ok, got=None):
    #: ⛭ r7651+cc66.91: this file had NO `check` -- every gate was a bare
    #: `if ...: fail.append(...)`, so a gate that PASSED printed nothing at all and a reader
    #: could not tell a satisfied condition from an absent one.  The gates PART 4B adds print
    #: their verdict and what they measured; the existing bare ones are left as they are,
    #: because rewriting them is not what `r7651` asked for and would hide this change.
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}" + (f"   ({got})" if got is not None else ""))
    if not ok:
        fail.append(label)
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
# ⛭⛭⛭ `r7647` ❷ -- THE SAME ARM ON 70's DISTANCES' POINT.  Its `l_A`, `D_M` and `r_s` are
#   bit-identical to the namesake's, so it is the like-for-like arm of record; the namesake row
#   stays because this file's identity is a named banked file and cannot move with an arm.
AORD = score('cr_x_h686_pol_leafrec1_distances')
#: ⛭ r7651+cc66.91: the L2000 rows PART 4B needs, scored by the SAME raw-grid method as every
#: row above, so the provenance of the paper's 298.0 is established in this file's own terms
#: before the matched procedure is run against it.
NEWL2 = score('cr_x_h686_L2000')
AORL2 = score('cr_x_h686_L2000_leafrec1_distances')
NEWF = score('cr_x_h686_fluid')
PIN = score('cr_leafpin')
PINF = score('cr_leafpin_fluid')
lA_sky, phi_sky = fit_comb(SKY)

print("=" * 112)
print("  PART 1 -- ** THE COMB, THE PHASE AND THE PEAKS **")
print("=" * 112)
print(f"  {'configuration':>34} {'l_A rep':>8} {'peaks':>26} {'fitted comb':>12} {'phi/pi':>8} "
      f"{'l1/lA':>7}")
# ⛭ r7653 ⓵: the ARM OF RECORD row joins PART 1 and PART 2, because l.2073-2074 prints THIS path's
#   raw-grid peaks (222/538/818/1134) and heights (2.264/2.298) and they are the NAMESAKE's.
for nm, s in (('control (LCDM)', CTL), ('the arm as coded, H0 = 73.0', CODED),
              ('crossing, H0 = 73.0', X73), ('** crossing, H0 = 68.6 **', NEW),
              ('** the same, ARM OF RECORD **', AORD), ('run 1, the pin', PIN)):
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
              ('** the same, ARM OF RECORD **', AORD), ('run 1, the pin', PIN)):
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
              ('** the same, ARM OF RECORD **', AORD), ('run 1, the pin', PIN)):
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

# =====================================================================================
# ⛭⛭⛭ `r7647` ⑵ -- THE QUARTERS ON THE ARM OF RECORD, AND THEY DO NOT SCALE: THEY MOVE AROUND.
#   `sec:refit-bound` l.958-959 prints the arm at 1.70 / 2.22 / 4.23 / 9.29 against the control's
#   0.77 / 1.44 / 2.62 / 3.73.  All eight are computed in this file already; none was pinned, and
#   the only band gate here asked whether each was within FOUR TIMES the control's -- which the
#   largest, at 2.75, was never going to fail.
_pc = {b: (AORD['bands'][b] / NEW['bands'][b] - 1) * 100 for b in BANDS}
_tot = (AORD['chi2'] / AORD['n']) / (NEW['chi2'] / NEW['n']) - 1
print(f"\n  {'band':>12} {'control':>10} {'namesake':>10} {'arm of record':>14} {'change':>11}")
for b in BANDS:
    print(f"  {f'{b[0]}-{b[1]}':>12} {CTL['bands'][b]:>10.6f} {NEW['bands'][b]:>10.6f} "
          f"{AORD['bands'][b]:>14.6f} {_pc[b]:>+10.4f}%")
print(f"  {'TOTAL/bin':>12} {CTL['chi2'] / CTL['n']:>10.6f} {NEW['chi2'] / NEW['n']:>10.6f} "
      f"{AORD['chi2'] / AORD['n']:>14.6f} {_tot * 100:>+10.4f}%")

if not (abs(CTL['bands'][(100, 400)] - 0.765826) < 5e-6
        and abs(CTL['bands'][(400, 700)] - 1.436731) < 5e-6
        and abs(CTL['bands'][(700, 1000)] - 2.620049) < 5e-6
        and abs(CTL['bands'][(1000, 1300)] - 3.725004) < 5e-6):
    fail.append("the CONTROL's four quarters are not the ones the paper prints (0.77/1.44/2.62/3.73)")
if not (abs(NEW['bands'][(100, 400)] - 1.700203) < 5e-6
        and abs(NEW['bands'][(400, 700)] - 2.222014) < 5e-6
        and abs(NEW['bands'][(700, 1000)] - 4.228463) < 5e-6
        and abs(NEW['bands'][(1000, 1300)] - 9.293875) < 5e-6):
    fail.append("the NAMESAKE arm's four quarters are not the ones the paper prints")
if not (abs(AORD['bands'][(100, 400)] - 2.105510) < 5e-6
        and abs(AORD['bands'][(400, 700)] - 1.904985) < 5e-6
        and abs(AORD['bands'][(700, 1000)] - 6.702414) < 5e-6
        and abs(AORD['bands'][(1000, 1300)] - 8.736422) < 5e-6):
    fail.append("the ARM OF RECORD's four quarters are not where this part pins them")
else:
    print("\n  ⛔⛔ ** AND THE RE-POINT REDISTRIBUTES THE COMB RATHER THAN SCALING IT. **  The TOTAL "
          f"moves {_tot * 100:+.2f} per cent")
    print(f"     while the four quarters move {_pc[(100, 400)]:+.2f}, {_pc[(400, 700)]:+.2f}, "
          f"{_pc[(700, 1000)]:+.2f} and {_pc[(1000, 1300)]:+.2f} per cent --")
    print("     UP, DOWN, UP, DOWN.  *So \"the arm of record is about five per cent worse over these "
          "bins\" hides a")
    print("     reorganisation an order of magnitude larger than itself, and the band that moves "
          "most is the")
    print("     700-1000 one -- the band that survived the crossing handover, the equality scan and "
          "the pin alike.*")

_signs = [AORD['bands'][b] > NEW['bands'][b] for b in BANDS]
if _signs != [True, False, True, False]:
    fail.append(f"the quarters' signs are {_signs}, not the up/down/up/down this part asserts -- "
                "the redistribution finding has changed shape")
if not (0.048 < _tot < 0.050):
    fail.append(f"the total moves {_tot * 100:.4f} per cent, not the +4.90 this part pins")
if not (max(abs(v) for v in _pc.values()) > 10.0 * abs(_tot * 100)):
    fail.append("the largest quarter move is no longer an order of magnitude above the total's, "
                "so the redistribution claim does not hold as stated")
if not (56.0 < _pc[(700, 1000)] < 61.0 and -16.0 < _pc[(400, 700)] < -12.5
        and 22.0 < _pc[(100, 400)] < 25.5 and -7.5 < _pc[(1000, 1300)] < -4.5):
    fail.append("the four per-cent moves are not where this part pins them two-sided")
if not (2.70 < max(AORD['bands'][b] / CTL['bands'][b] for b in BANDS) < 2.80):
    fail.append("the arm of record's worst band ratio is not the 2.75 this part pins")

print()
print("=" * 112)
print("  PART 4 -- ** BOTH INSTRUMENT PATHS, EACH AGAINST ITS OWN-PATH CONTROL **")
print("=" * 112)
# ** THE FLUID-PATH CONTROL DID NOT EXIST IN THE TREE UNTIL r6760+cc66.10, AND ITS ABSENCE WAS
# MAKING THE FLUID ROWS UNREADABLE. **  *Every fluid row had been scored against the POLARISATION
# control, so the fluid path's own height behaviour was being charged to the arm.  It is not the
# arm's: the LCDM control on the fluid path overshoots the sky too.*
CTLF = score('lcdm_fluid')
X62 = score('cr_x_h6862_pol')
X62F = score('cr_x_h6862_fluid')
print(f"  {'':>30} {'peaks':>26} {'comb':>7} {'P1/P2':>8} {'P1/P3':>8} {'chi2/bin':>9}")
for nm, s in (('POLARISATION: control LCDM', CTL), ('POLARISATION: arm, H0 = 68.60', NEW),
              ('POLARISATION: arm, H0 = 68.62', X62),
              ('FLUID:        control LCDM', CTLF), ('FLUID:        arm, H0 = 68.60', NEWF),
              ('FLUID:        arm, H0 = 68.62', X62F)):
    print(f"  {nm:>30} {str([int(v) for v in s['P']]):>26} {s['lA']:>7.1f} {s['p12']:>8.3f} "
          f"{s['p13']:>8.3f} {s['chi2'] / s['n']:>9.2f}")
print(f"  {'THE SKY':>30} {str([float(v) for v in SKY]):>26} {lA_sky:>7.1f} {SKY_P12:>8.3f} "
      f"{SKY_P13:>8.3f} {'--':>9}")
print(f"""
  ** THE FLUID PATH'S HEIGHT OVERSHOOT IS THE PATH'S, NOT THE ARM'S. **  The LCDM CONTROL on the
  fluid path returns {CTLF['p12']:.3f}/{CTLF['p13']:.3f} against the sky's {SKY_P12}/{SKY_P13} --
  {(CTLF['p12'] / SKY_P12 - 1) * 100:+.1f}% and {(CTLF['p13'] / SKY_P13 - 1) * 100:+.1f}% -- and its chi^2 is
  {CTLF['chi2'] / CTLF['n']:.2f} per bin against the polarisation control's {CTL['chi2'] / CTL['n']:.2f}.
  *So a fluid row scored against the polarisation control was charging the path to the arm.*

  ** AGAINST ITS OWN-PATH CONTROL THE ARM SITS THE SAME DISTANCE ON BOTH: **
      polarisation   P1/P2 {(X62['p12'] / CTL['p12'] - 1) * 100:+.1f}%   P1/P3 {(X62['p13'] / CTL['p13'] - 1) * 100:+.1f}%   chi^2 x{X62['chi2'] / CTL['chi2']:.1f}
      fluid          P1/P2 {(X62F['p12'] / CTLF['p12'] - 1) * 100:+.1f}%   P1/P3 {(X62F['p13'] / CTLF['p13'] - 1) * 100:+.1f}%   chi^2 x{X62F['chi2'] / CTLF['chi2']:.1f}
  ⇒ *** The comb is path-proof AND the arm-to-control height OFFSET is path-robust.  What is
  path-specific is the ABSOLUTE height, which both arms and both controls carry alike. ***
  *That is a weaker caveat than the one r6760+cc66.7 stated, and it is weaker because the control
  that settles it had not been run.*

  ⌗ ** AND H0 = 68.62, THE VALUE ACTUALLY ORDERED, CONFIRMS 68.60 TO EVERY DIGIT THAT MATTERS: **
  the same four peaks on both paths, comb {X62['lA']:.1f}, P1/P2 {X62['p12']:.3f}, P1/P3 {X62['p13']:.3f}.""")
if abs(NEWF['lA'] - NEW['lA']) > 2.0:
    fail.append("the comb is NOT path-independent -- PART 4's claim is wrong")
if abs(X62['lA'] - NEW['lA']) > 1.0 or abs(X62['p12'] - NEW['p12']) > 0.01:
    fail.append("H0 = 68.62 does not reproduce 68.60 -- the 0.03% argument is wrong")
if CTLF['p13'] < SKY_P13 * 1.05:
    fail.append("the fluid control does NOT overshoot the sky -- PART 4's premise is wrong")
for lab, arm, ctl in (('polarisation', X62, CTL), ('fluid', X62F, CTLF)):
    if abs(arm['p12'] / ctl['p12'] - 1) > 0.08:
        fail.append(f"the {lab} arm-to-control P1/P2 offset is "
                    f"{(arm['p12'] / ctl['p12'] - 1) * 100:.1f}%, outside 8%")

# =================================================================================================
# ⛭⛭⛭ r7651+cc66.91 -- PART 4B: ** THE COMB BY THE PROCEDURE THE SENTENCE NAMES, ON THE ARM OF
#   RECORD -- ordered by `r7651` ⓵ because none of the receipts the four sentences cite computes it,
#   and the two that print it only quote it. **
#
#   l.813, l.883, l.945 and l.2067 all rest on ONE pair: `$298.0$` against the sky's `$298.4$`, which
#   l.2067 calls "right to a part in six hundred".  l.813's wording is the claim this PART tests:
#   *"fitted to those peaks BY THE PROCEDURE THIS PAPER RUNS ON THE SKY"*.
#
#   ⛔ ** THE PAIR IS NOT THAT PROCEDURE, AND THE PROVENANCE IS EXACT. **  `score()` above finds peaks
#   with `argrelextrema(Dl, order=3)` on the model's OWN NATIVE GRID and fits three of them.  The
#   L2000 banks are `LSTEP=2`, so those maxima are QUANTISED TO EVEN `ell`: the namesake's come out
#   `222 / 538 / 818 / 1134`, every one of them a grid point, and the three-peak fit of them is
#   `298.00` -- the paper's figure to the digit.  The sky's `298.4` is `sec:intro`'s stored quartet
#   through the same three-peak fit, `298.45`.  So the pair is internally consistent in its FIT and
#   the arm's half of it is not located by the parabolic procedure at all.
#   ⇒ *** AND THE AGREEMENT IS CLAIMED FINER THAN THE METHOD THAT PRODUCED IT CAN RESOLVE: 0.13 per
#   cent, on peaks quantised to 2 in `ell`, where the parabolic locator moves the fourth peak by 3.2.
#   That is the same defect class as the 10-per-cent RELATIVE tolerance `cc66.81` found on a shift a
#   fiftieth of its locator's grain -- a number stated to a precision its own instrument lacks. ***
#
#   ⌗ *So this PART runs the procedure the sentence names -- lens with P15's own operator, bin through
#   `plik_lite`, cubic-spline to a 1-in-`ell` grid, locate humps, parabola over +-W, W swept over the
#   seven windows -- IDENTICALLY on the sky and on each arm, which is `cc66.28`'s matched-procedure
#   discipline.  The sky row is the check that the port is faithful: it must reproduce `sec:intro`.*
print()
print("=" * 112)
print("  PART 4B -- ** THE COMB BY THE PROCEDURE THE SENTENCE NAMES (r7651 ⓵) **")
print("=" * 112)
from scipy.interpolate import CubicSpline                                  # noqa: E402
import camb                                                               # noqa: E402

_LC, _FACB = CS.bin_center_and_fac()
_WS = (40., 45., 50., 55., 60., 70., 80.)
_cp = camb.set_params(H0=67.40, ombh2=0.02237, omch2=0.3150 * 0.674 ** 2 - 0.02237,
                      mnu=0.06, omk=0, tau=0.054, As=2.1e-9, ns=0.965, lmax=3000)
_ccl = camb.get_results(_cp).get_cmb_power_spectra(_cp, CMB_unit='muK', lmax=3000)
_cle, _clu = _ccl['total'][:, 0], _ccl['unlensed_scalar'][:, 0]
_CLG = np.arange(len(_cle), dtype=float)
_RAT = np.ones_like(_cle)
_msk = _clu > 0
_RAT[_msk] = _cle[_msk] / _clu[_msk]


def _locate(Db, W, n=4):
    """`cc66.28`'s locator, unchanged, so the sky and both arms go through ONE procedure.

    ⛭ r7653 ⓵: it now returns the parabola's VERTEX VALUE beside its vertex position.  *The heights
    l.2075 claims come from the SAME fit as the positions l.148 claims, over the SAME seven windows, on
    the sky and on every arm -- which is the only way a height ratio can be compared with the sky's
    published one without a second procedure smuggled in.*  Nothing about the positions changes.
    """
    m = (_LC >= 100) & np.isfinite(Db)
    lf = np.arange(100.0, 1300.0, 1.0)
    Df = CubicSpline(_LC[m], Db[m])(lf)
    out = []
    for i in argrelextrema(Df, np.greater, order=40)[0]:
        k = (lf >= lf[i] - W) & (lf <= lf[i] + W)
        if k.sum() < 5:
            continue
        c = np.polyfit(lf[k], Df[k], 2)
        if c[0] >= 0:
            continue
        x = float(-c[1] / (2 * c[0]))
        out.append((x, float(np.polyval(c, x))))
    return out[:n]


def _sweep(Db):
    A3, A4, F3, F4, PK, HT = [], [], [], [], [], []
    for W in _WS:
        ph = _locate(Db, W)
        if len(ph) < 4:
            continue
        p = [x for x, _h in ph]
        PK.append(p)
        HT.append([h for _x, h in ph])
        _l3, _f3 = fit_comb(p, 3)
        _l4, _f4 = fit_comb(p, 4)
        A3.append(_l3), F3.append(_f3), A4.append(_l4), F4.append(_f4)
    PK, HT = np.array(PK), np.array(HT)
    H = HT.mean(axis=0)
    return dict(pk=PK.mean(axis=0), ht=H, a3=float(np.mean(A3)), a4=float(np.mean(A4)),
                f3=float(np.mean(F3)), f4=float(np.mean(F4)),
                a4_s=float(np.std(A4, ddof=1)), nW=len(PK),
                p12=float(H[0] / H[1]), p13=float(H[0] / H[2]))


def _matched(fn, lensed=True):
    """`fn` is a `spectra/` basename or, for the hierarchy path, a path under `beyond_the_wall/`."""
    _p = fn if os.path.isabs(fn) else os.path.join(SPEC, fn)
    if not os.path.exists(_p):
        _p = os.path.join(ROOT, 'computations', 'beyond_the_wall', fn)
    z = np.load(_p)
    ls, Dl = np.asarray(z['ls'], float), np.asarray(z['Dl'], float)
    if lensed:
        Dl = Dl * np.interp(ls, _CLG, _RAT)
    s = _sweep(CS.bin_spectrum(ls, Dl) * _FACB)
    s['lA_rep'] = float(z['l_A'])
    return s


#: ⛔⛭⛭ r7651+cc66.94: ** THE PAPER'S OWN THREE FIGURES ARE READ OUT OF THE PAPER, because
#:   `check_unread_figure` reddened on this PART and was right -- FOR THE THIRD TIME ON THIS SEAT. **
#:   *The gates below argue about what l.813, l.945 and l.2067 print.  Their labels named `298.0`,
#:   `298.4` and `302.9` while nothing in the file opened `corpus/CR_cosmology.tex`, so if 69 moved
#:   any of them the gates would have stayed green while the argument went false.  `cc66.89` was
#:   told this once and my own `r7651` PREDICTION.md listed it as commitment 4 -- "a figure
#:   attributed to the paper is READ OUT OF THE PAPER, not retyped from it" -- and I did it anyway.
#:   The cause is worth naming: the provenance argument lives in the LABEL, and the gate's whole
#:   point is that an argument about the paper has to read the paper.*
#:   ⇒ ** AND IT IS A PIN ON 69's SENTENCES, so each locator is a DISJUNCTION: ** when the sentence
#:   is found the paper's figures must equal what this file computes by the two methods; when it is
#:   not found the ALT arm says so and holds the computed values.  Adjudicated in
#:   `corpus/quote_pin_baseline.tsv` in this same pass.
import re                                                                  # noqa: E402

_TEXW = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'),
                                 encoding='utf-8').read())
_M813 = re.search(r"fitted to those peaks by the procedure this paper runs on the sky, it is "
                  r"\$([0-9.]+)\$ against the sky's \$([0-9.]+)\$", _TEXW)
#: ⛭ r7653 ⓵: l.945's locator is a disjunction over the two WORDINGS, not just the two figures.  *69's
#:   order says the landed sentence prints "the parting (299.06 against the ruler's 302.89) beside it",
#:   which is a different clause from "the comb at 298.0 against a reported scale of 302.9".  So both
#:   forms are tried and the ruler is read from whichever is there.*
_M945 = (re.search(r"the comb at \$([0-9.]+)\$ against a reported scale of \$([0-9.]+)\$", _TEXW)
         or re.search(r"\$([0-9.]+)\$ against the ruler's \$([0-9.]+)\$", _TEXW))
PAPER = dict(comb=float(_M813.group(1)) if _M813 else None,
             sky=float(_M813.group(2)) if _M813 else None,
             ruler=float(_M945.group(2)) if _M945 else None)
print(f"  read out of corpus/CR_cosmology.tex: l.813's comb/sky = "
      f"{PAPER['comb']}/{PAPER['sky']}, l.945's reported scale = {PAPER['ruler']}"
      + ("" if _M813 and _M945 else "   ⛔ ALT ARM: a sentence was not locatable in this form"))

_MSKY = _sweep(CS.X_DATA * _FACB)
_MCTL = _matched('cc66_lcdm_L2000.npz')
_MNSK = _matched('cc66_cr_x_h686_L2000.npz')
_MAOR = _matched('cc66_cr_x_h686_L2000_leafrec1_distances.npz')
# ⛭⛭ r7653 ⓵: THE SECOND INSTRUMENT -- the HIERARCHY path l.2070-2076 reads, through the SAME locator.
#   *`r7653`'s ⓵c predicted this could not be done for want of a bank, and that prediction is
#   FALSIFIED: the arm-of-record hierarchy spectrum is not in `spectra/` under any `*_leafrec1_distances`
#   name -- it is a GRID bank, `refit_grid185_leafrec1_distances/cr_base.npz`, reached through
#   `...the_full_range_refit_holds_the_background...`'s own `GRIDS` map.  ** The cause is worth keeping:
#   I searched by FILENAME CONVENTION instead of asking which receipt computes the quantity. **  (The two
#   `spectra/r6784_cr_crossing_hier{,_leafrec1}.npz` banks sit at `l_A` ~ 172, the H0=73 crossing, so
#   they are the wrong configuration and are not it.)*
_MHCT = _matched('refit_grid185/lcdm_base.npz')
_MHNS = _matched('refit_grid185/cr_base.npz')
_MHAO = _matched('refit_grid185_leafrec1_distances/cr_base.npz')
# ⌗ *the phi column is PART 1's own convention, `fit_comb()[1] / pi`, so the rows here and the rows
#   there are the same quantity and l.2147's pair can be read against either.*
print(f"  {'row':>34} {'peaks (matched locator)':>30} {'comb 1-4':>10} {'1-3':>8} "
      f"{'phi/pi 1-4':>11} {'1-3':>9} {'P1/P2':>7} {'P1/P3':>7} {'geom l_A':>9}")
for _nm, _s in (('THE SKY, this locator', _MSKY),
                ('the CONTROL, L2000', _MCTL),
                ('namesake L2000 (LEAFREC=0)', _MNSK),
                ('** ARM OF RECORD, distances **', _MAOR),
                ('--- hier: the CONTROL', _MHCT),
                ('--- hier: namesake', _MHNS),
                ('--- hier: ** ARM OF RECORD **', _MHAO)):
    _g = f"{_s['lA_rep']:9.3f}" if 'lA_rep' in _s else f"{'--':>9}"
    print(f"  {_nm:>34} {' '.join(f'{v:7.2f}' for v in _s['pk'])} {_s['a4']:>10.3f} "
          f"{_s['a3']:>8.3f} {_s['f4'] / np.pi:>11.4f} {_s['f3'] / np.pi:>9.4f} "
          f"{_s['p12']:>7.3f} {_s['p13']:>7.3f} {_g}")
print(f"  the sky's own published pair, `sec:intro`'s: P1/P2 {SKY_P12}, P1/P3 {SKY_P13}; this locator "
      f"returns {_MSKY['p12']:.3f} / {_MSKY['p13']:.3f} on the sky")
for _nm, _s in (('control', _MCTL), ('namesake', _MNSK), ('ARM OF RECORD', _MAOR)):
    print(f"    against the sky's own locator values, {_nm:>13}: P1/P2 "
          f"{100 * (_s['p12'] / _MSKY['p12'] - 1):+6.2f}%   P1/P3 "
          f"{100 * (_s['p13'] / _MSKY['p13'] - 1):+6.2f}%")
# ⛭⛭⛭ r7653 ⓵: AND THIS IS THE ANSWER TO THE QUESTION `MEASURED_item1.md` FLAGGED AND DID NOT ASSERT.
#   *l.2075 claims the two instrument paths agree "within a multipole on every peak".  Read off the
#   figures l.2072-2074 PRINTS -- hier 221.96/536.11/815.40/1130.53 against "this path's" 222/538/818/
#   1134 -- the offsets are -0.04, -1.90, -2.60, -3.47, and the claim is false in its own numbers.
#   ** But those two are not one measurement: the hier figures are located SUB-BIN on a unit-step grid
#   and the line-of-sight figures are RAW MAXIMA on an LSTEP=2 grid, quantised to even `ell`. **  The
#   paper says so in terms, and then compares them anyway.  ⇒ Put BOTH paths through the one matched
#   locator and they agree to under a tenth of a multipole at every peak and to a hundredth of a per
#   cent on the heights, on the namesake and on the arm of record alike.  *So the claim HOLDS, and
#   comfortably; what does not hold is the pair of figures offered as its evidence.*
for _nm, _h, _l in (('namesake', _MHNS, _MNSK), ('ARM OF RECORD', _MHAO, _MAOR)):
    print(f"    hierarchy against line-of-sight, ONE locator on both, {_nm:>13}: peak offsets "
          f"{' '.join(f'{a - b:+.2f}' for a, b in zip(_h['pk'], _l['pk']))}  "
          f"P1/P2 {100 * (_h['p12'] / _l['p12'] - 1):+.3f}%  "
          f"P1/P3 {100 * (_h['p13'] / _l['p13'] - 1):+.3f}%")
print(f"    against which the paper's own printed pair, l.2072-2074, offers "
      f"-0.04 -1.90 -2.60 -3.47 -- hier located sub-bin, line-of-sight quantised to even `ell`")

#: ⛭⛭⛭ r7653 ⓵ -- ** THE TABLE IS PINNED, ROW BY ROW, BY ONE PROCEDURE. **  *69's order asks for the
#:   four peaks, the four- and three-peak combs, phi/pi, and P1/P2 and P1/P3 for the arm, the control
#:   and the sky, plus the same on the second instrument.  Every figure below is held to the digit it is
#:   tabled at, so a re-point of any bank fails here rather than changing a reported number silently.*
for _nm, _s, _PKL, _A4, _A3, _F4, _P12, _P13 in (
        ('THE SKY', _MSKY, (220.98, 533.79, 814.79, 1121.85), 298.362, 296.906, -0.7692, 2.221, 2.262),
        ('the control, L2000', _MCTL, (220.44, 537.29, 811.06, 1123.99), 298.441, 295.308, -0.7674,
         2.204, 2.225),
        ('the namesake, L2000', _MNSK, (221.11, 538.63, 815.49, 1130.79), 300.589, 297.189, -0.7835,
         2.274, 2.336),
        ('the ARM OF RECORD', _MAOR, (220.03, 536.25, 811.59, 1125.11), 299.057, 295.782, -0.7815,
         2.291, 2.349),
        ('hier, the control', _MHCT, (220.45, 537.31, 811.04, 1123.96), 298.429, 295.299, -0.7672,
         2.204, 2.225),
        ('hier, the namesake', _MHNS, (221.11, 538.64, 815.47, 1130.76), 300.578, 297.180, -0.7834,
         2.274, 2.335),
        ('hier, the ARM OF RECORD', _MHAO, (220.03, 536.27, 811.58, 1125.02), 299.029, 295.773,
         -0.7811, 2.291, 2.348)):
    check(f"⛭ the matched locator's whole row for {_nm} is held to its tabled digits -- four peaks, "
          f"both combs, phi and both height ratios, over all seven windows",
          _s['nW'] == 7
          and all(abs(float(a) - b) <= 0.005 for a, b in zip(_s['pk'], _PKL))
          and abs(_s['a4'] - _A4) <= 0.0005 and abs(_s['a3'] - _A3) <= 0.0005
          and abs(_s['f4'] - _F4) <= 5e-5
          and abs(_s['p12'] - _P12) <= 0.0005 and abs(_s['p13'] - _P13) <= 0.0005,
          f"peaks {' '.join(f'{v:.2f}' for v in _s['pk'])}; combs {_s['a4']:.3f}/{_s['a3']:.3f}; "
          f"phi {_s['f4']:.4f}; heights {_s['p12']:.3f}/{_s['p13']:.3f}")

check("⛭⛭ ** THE LOCATOR IS VALIDATED ON THE SKY BEFORE ANYTHING IS READ OFF IT: ** it returns P1/P2 "
      "2.221 and P1/P3 2.262 against `sec:intro`'s own published 2.217 and 2.277 -- 0.2 and 0.7 per "
      "cent.  *A locator that could not find the sky's own height ratios would not be evidence about "
      "an arm's.*",
      abs(_MSKY['p12'] / SKY_P12 - 1) < 0.005 and abs(_MSKY['p13'] / SKY_P13 - 1) < 0.01,
      f"sky locator {_MSKY['p12']:.3f}/{_MSKY['p13']:.3f} against published {SKY_P12}/{SKY_P13}")

check("⛭⛭⛭ ** THE RE-POINT MOVES THE POSITIONS TOWARD THE SKY AND THE HEIGHTS AWAY FROM IT, which is "
      "the finding and not a figure. **  *The comb's agreement improves from 1 part in 134 to 1 part "
      "in 429, while P1/P2 against the sky goes +2.40 to +3.16 per cent and P1/P3 +3.24 to +3.82.  And "
      "the CONTROL is nearer the sky than either arm on the heights, -0.75 per cent, which is the "
      "direction l.146's 'the heights are the path's and the positions are the construction's' already "
      "asserts.*",
      abs(_MAOR['a4'] - _MSKY['a4']) < abs(_MNSK['a4'] - _MSKY['a4'])
      and abs(_MAOR['p12'] / _MSKY['p12'] - 1) > abs(_MNSK['p12'] / _MSKY['p12'] - 1)
      and abs(_MAOR['p13'] / _MSKY['p13'] - 1) > abs(_MNSK['p13'] / _MSKY['p13'] - 1)
      and abs(_MCTL['p12'] / _MSKY['p12'] - 1) < abs(_MNSK['p12'] / _MSKY['p12'] - 1),
      f"positions {abs(_MNSK['a4'] - _MSKY['a4']):.3f} -> {abs(_MAOR['a4'] - _MSKY['a4']):.3f}; "
      f"heights {100 * (_MNSK['p12'] / _MSKY['p12'] - 1):+.2f}% -> "
      f"{100 * (_MAOR['p12'] / _MSKY['p12'] - 1):+.2f}%; control "
      f"{100 * (_MCTL['p12'] / _MSKY['p12'] - 1):+.2f}%")

check("⛭⛭⛭ ** AND THE SECOND INSTRUMENT ANSWERS l.2075 IN ITS FAVOUR, ON BOTH ARMS, ONCE THE TWO PATHS "
      "GO THROUGH ONE PROCEDURE. **  *The hierarchy path and the line-of-sight path agree to under a "
      "tenth of a multipole at every peak and to under a twentieth of a per cent on both height "
      "ratios.*  ⇒ *** So 'within a multipole on every peak and within one per cent on the heights' "
      "HOLDS, and comfortably.  What does not hold is the PAIR OF FIGURES l.2072-2074 offers as its "
      "evidence: hier located sub-bin on a unit-step grid against line-of-sight maxima quantised to "
      "even `ell` by LSTEP=2, which gives offsets -0.04, -1.90, -2.60 and -3.47 and makes the claim "
      "look false in its own numbers. ***",
      max(abs(float(a) - float(b)) for _h, _l in ((_MHNS, _MNSK), (_MHAO, _MAOR))
          for a, b in zip(_h['pk'], _l['pk'])) < 0.10
      and max(abs(_h['p12'] / _l['p12'] - 1) for _h, _l in ((_MHNS, _MNSK), (_MHAO, _MAOR))) < 0.0005
      and max(abs(_h['p13'] / _l['p13'] - 1) for _h, _l in ((_MHNS, _MNSK), (_MHAO, _MAOR))) < 0.0005,
      f"worst peak offset {max(abs(float(a) - float(b)) for _h, _l in ((_MHNS, _MNSK), (_MHAO, _MAOR)) for a, b in zip(_h['pk'], _l['pk'])):.3f} in ell")

#: ⛔⛭⛭ r7653 ⓵ -- ** AND THE RAW-GRID ROW ON THE ARM OF RECORD IS THE LSTEP=2 TRAP IN ITS PUREST FORM. **
#:   *l.2073-2074 prints "this path's" peaks and heights from `score()`, the RAW-GRID method: the
#:   namesake gives 222/538/818/1134, comb 298.0, phi/pi -0.2349, heights 2.264/2.298.  On the arm of
#:   record the same method gives 220/536/814/1130 -- and its first THREE maxima land on the CONTROL's
#:   own cells, so its three-peak comb (297.0) and its phi (-0.2379) come out BIT-IDENTICAL to the
#:   control's while the heights (2.281/2.312) do not.*  ⇒ ** So the arm-of-record figure for l.813's
#:   comb cannot come from this method: 69's landed 299.1 is the MATCHED locator's 299.057, and the
#:   raw grid's 297.0 is an artefact of where the LSTEP=2 cells fall. **
check("⛔⛭⛭ the raw-grid row on the arm of record is held to its own digits -- peaks 220/536/814/1130, "
      "comb 297.0, phi/pi -0.2379, heights 2.281 and 2.312 -- AND its comb and phi are bit-identical "
      "to the control's, because its first three maxima land on the control's own LSTEP=2 cells while "
      "its fourth does not (1130 against the control's 1128)",
      [int(v) for v in AORD['P']] == [220, 536, 814, 1130]
      and abs(AORD['lA'] - 297.0) < 0.05 and abs(AORD['phi'] / np.pi - (-0.2379)) < 5e-5
      and abs(AORD['p12'] - 2.281) < 0.0005 and abs(AORD['p13'] - 2.312) < 0.0005
      and AORD['lA'] == CTL['lA'] and AORD['phi'] == CTL['phi']
      and [int(v) for v in AORD['P']][:3] == [int(v) for v in CTL['P']][:3]
      and int(AORD['P'][3]) != int(CTL['P'][3]),
      f"arm of record raw grid {[int(v) for v in AORD['P']]} comb {AORD['lA']:.1f} "
      f"phi/pi {AORD['phi'] / np.pi:.4f} heights {AORD['p12']:.3f}/{AORD['p13']:.3f}; "
      f"control {[int(v) for v in CTL['P']]} comb {CTL['lA']:.1f} phi/pi {CTL['phi'] / np.pi:.4f}")
print(f"\n  the RAW-GRID method `score()` uses, for the provenance: the namesake's maxima are "
      f"{[int(v) for v in NEWL2['P']]},")
print(f"  every one an even multipole on the LSTEP=2 grid, and their three-peak comb is "
      f"{NEWL2['lA']:.2f} -- the paper's 298.0.")
print(f"  `sec:intro`'s stored quartet through that same three-peak fit is {fit_comb(SKY, 3)[0]:.2f} "
      f"-- the paper's 298.4.")
print(f"  the parabolic locator moves the namesake's fourth peak by "
      f"{abs(_MNSK['pk'][3] - NEWL2['P'][3]):.2f} in ell, against an agreement claimed at 0.13%.")
check("⛭⛭⛭ ** THE PORT IS FAITHFUL, WHICH IS THE ONLY REASON THE ROWS BELOW MEAN ANYTHING: the "
      "matched locator run on the SKY reproduces `sec:intro`'s own quartet. **  *Its four-peak comb "
      "is 298.362 against the 298.45 `sec:intro`'s stored quartet gives through the same fit, and "
      "its peaks are 220.98 / 533.79 / 814.79 / 1121.85 against the stored 220.4 / 537.7 / 817.3 / "
      "1123.9.  A port that could not find the sky would not be evidence about an arm.*",
      abs(_MSKY['a4'] - 298.362) < 0.01 and abs(_MSKY['a4'] - fit_comb(SKY, 3)[0]) < 0.2
      and _MSKY['nW'] == 7
      and (PAPER['sky'] is None or abs(fit_comb(SKY, 3)[0] - PAPER['sky']) < 0.06),
      f"sky comb 1-4 = {_MSKY['a4']:.3f} +- {_MSKY['a4_s']:.3f} over {_MSKY['nW']} windows; "
      f"sec:intro's three-peak {fit_comb(SKY, 3)[0]:.2f}")
#: ⛭⛭⛭ r7653 ⓵ -- ** THE LANDED FORM: THIS GATE IS NOW A DISJUNCTION OVER THE TWO STATES l.813 CAN BE
#:   IN, because this turn's table proposes the second one and 69 lands it. **
#:   ⓐ THE NAMESAKE STATE, which the paper is in as this is written: l.813 prints `298.0`, and that is
#:     the NAMESAKE's RAW-GRID three-peak comb on maxima quantised to even `ell`, not the procedure the
#:     sentence names.  The finding is that the matched locator gives 300.589 there, over two multipoles
#:     away, so the arm's half of the printed pair is not located by the named procedure at all.
#:   ⓑ THE LANDED STATE: l.813 prints the MATCHED locator's own figure, `299.1` from 299.057, against
#:     the sky's `298.4` from the matched 298.362 -- a part in 429.  There the printed pair IS the named
#:     procedure on both halves, and the provenance finding above is RESOLVED rather than standing.
#:   ⌗ *A gate pinned to ⓐ alone would go red the day 69 lands the table this turn tables; one pinned to
#:   ⓑ alone is red today.  Both arms are asserted, the state is PRINTED, and a MIXED state -- a figure
#:   that is neither -- fails.*
_PCOMB = None
if PAPER['comb'] is not None:
    if abs(NEWL2['lA'] - PAPER['comb']) < 0.05:
        _PCOMB = 'namesake raw-grid (298.0)'
    elif abs(round(_MAOR['a4'], 1) - PAPER['comb']) < 0.05:
        _PCOMB = 'arm of record, matched locator (299.1)'
print(f"  l.813's comb is in the state: {_PCOMB}")
check("⛭⛭⛭ ** l.813's COMB IS ONE OF THE TWO STATES THIS QUANTITY HAS, AND THE PROVENANCE ARGUMENT IS "
      "STATED FOR EACH. **  *In the namesake state the paper's 298.0 IS NOT the procedure the sentence "
      "names: by that procedure the namesake gives 300.589 and the arm of record 299.057, and 298.0 is "
      "the namesake's RAW-GRID three-peak comb on maxima quantised to even `ell` by LSTEP=2 -- the pair "
      "(298.0, 298.4) being internally consistent in its FIT, both three-peak, while the arm's half is "
      "not parabolically located at all.  In the landed state the paper prints the matched locator's "
      "own 299.1 against the sky's 298.4 and the provenance finding is resolved.*",
      abs(_MNSK['a4'] - 300.589) < 0.01 and abs(_MAOR['a4'] - 299.057) < 0.01
      and abs(NEWL2['lA'] - 298.00) < 0.005
      and all(float(v) % 2.0 == 0.0 for v in NEWL2['P'])
      and (PAPER['comb'] is None or _PCOMB is not None)
      and (_PCOMB != 'namesake raw-grid (298.0)' or abs(_MNSK['a4'] - PAPER['comb']) > 2.0)
      and (_PCOMB != 'arm of record, matched locator (299.1)'
           or abs(_MAOR['a4'] - PAPER['comb']) < 0.05),
      f"state {_PCOMB}; matched: namesake {_MNSK['a4']:.3f}, arm of record {_MAOR['a4']:.3f}; "
      f"raw-grid namesake {NEWL2['lA']:.2f} on peaks {[int(v) for v in NEWL2['P']]}")
_gap_ns = _MNSK['a4'] - _MSKY['a4']
_gap_ao = _MAOR['a4'] - _MSKY['a4']
print(f"\n  against the sky, by the named procedure: namesake {_gap_ns:+.3f} in ell "
      f"(1 part in {abs(_MSKY['a4'] / _gap_ns):.0f}); arm of record {_gap_ao:+.3f} "
      f"(1 part in {abs(_MSKY['a4'] / _gap_ao):.0f})")
check("⛭⛭⛭ ** AND BY THE PROCEDURE THE SENTENCE NAMES THE AGREEMENT IS BETTER ON THE ARM OF RECORD "
      "THAN ON THE NAMESAKE -- 1 part in 429 against 1 part in 134 -- though it was never 1 part in "
      "six hundred on either. **  ⇒ *So l.2067's claim survives in DIRECTION and not in SIZE, and it "
      "survives better on this arm, which is the opposite of residue*",
      abs(_gap_ao) < abs(_gap_ns) and abs(_MSKY['a4'] / _gap_ao) > 300.0
      and abs(_MSKY['a4'] / _gap_ns) < 200.0,
      f"arm of record 1 part in {abs(_MSKY['a4'] / _gap_ao):.0f}, namesake 1 part in "
      f"{abs(_MSKY['a4'] / _gap_ns):.0f}")
check("⛭⛭⛭ ** AND HERE IS THE PARTING `cc66.81` FOUND, IN ITS CLEANEST FORM: THE GEOMETRIC RULER IS "
      "BIT-IDENTICAL ON THE TWO ARMS WHILE THE FITTED COMB MOVES. **  *At the distances' point the "
      "banked `l_A`, `D_M` and `r_s` are the SAME NUMBERS in both files -- the background cannot see "
      "the arm -- and the comb the spectrum actually has goes 300.589 to 299.057.  `cc66.81` measured "
      "the same parting at the refit point as a difference BETWEEN arms; here the geometric value is "
      "literally the same file value and the spectrum's own comb still moves by 1.5 in `ell`.*  ⇒ "
      "*** The fitted comb sits 1.265 per cent below the reported ruler on the arm of record and "
      "0.759 per cent below it on the namesake: the ruler is not the comb, and l.945's 'the comb at "
      "298.0 against a reported scale of 302.9' is the paper already printing the parting. ***",
      _MNSK['lA_rep'] == _MAOR['lA_rep']
      and abs(_MNSK['a4'] - _MAOR['a4']) > 1.0
      and _MAOR['a4'] / _MAOR['lA_rep'] < _MNSK['a4'] / _MNSK['lA_rep'] < 1.0
      and (PAPER['ruler'] is None or abs(_MAOR['lA_rep'] - PAPER['ruler']) < 0.05
           or abs(round(_MAOR['lA_rep'], 2) - PAPER['ruler']) < 0.005),
      f"geometric l_A identical at {_MAOR['lA_rep']:.4f}; fitted comb {_MNSK['a4']:.3f} -> "
      f"{_MAOR['a4']:.3f}; fitted/geometric {100 * (_MNSK['a4'] / _MNSK['lA_rep'] - 1):+.3f}% -> "
      f"{100 * (_MAOR['a4'] / _MAOR['lA_rep'] - 1):+.3f}%")

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
    ⛭ **and on the ARM OF RECORD, by this same raw-grid method, it is {AORD['phi'] / np.pi:.4f} pi,
    {abs(AORD['phi'] / phi_sky - 1) * 100:.1f}% from the sky's** -- which is NEARER, not further.  *But
    that figure is the LSTEP=2 trap: the arm of record's first three raw maxima land on the control's
    own cells, so its raw phase comes out bit-identical to the control's.  By the matched locator of
    PART 4B, which is the procedure l.813's sentence names, the pair is {_MAOR['f4'] / np.pi:.4f} pi
    against the sky's {_MSKY['f4'] / np.pi:.4f} pi on the four-peak fit, and {_MAOR['f3'] / np.pi:.4f}
    against {_MSKY['f3'] / np.pi:.4f} on the three-peak one.*  ⇒ ** l.2147's intercept pair,
    {NEW['phi'] / np.pi:.4f} against the sky's {phi_sky / np.pi:.4f}, is the NAMESAKE's raw-grid
    three-peak fit; the pair that goes with a landed comb of {_MAOR['a4']:.1f} is the matched
    four-peak one. **
    ⌗ *Those two are INTERPOLATED and not typed, deliberately: `marker_transposition_baseline.tsv`
    adjudicates l.2147's sky intercept as "the own group prints it at run time", and hard-coding the
    figure here makes that adjudication STALE -- which is what it did at `r7653+cc66.110` and what the
    CI `fast` tier then reddened on.  ** And this sentence may not spell the figure either: naming it in
    the comment that explains the interpolation carries it just as surely as typing it in the gate, and
    that is the second half of the same red. **  The marker gate reads the SOURCE.*

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
