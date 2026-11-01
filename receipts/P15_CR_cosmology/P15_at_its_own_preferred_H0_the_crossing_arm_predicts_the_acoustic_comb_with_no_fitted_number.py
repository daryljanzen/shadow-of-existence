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
    """`cc66.28`'s locator, unchanged, so the sky and both arms go through ONE procedure."""
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
        out.append(float(-c[1] / (2 * c[0])))
    return out[:n]


def _sweep(Db):
    A3, A4, PK = [], [], []
    for W in _WS:
        p = _locate(Db, W)
        if len(p) < 4:
            continue
        PK.append(p)
        A3.append(fit_comb(p, 3)[0])
        A4.append(fit_comb(p, 4)[0])
    PK = np.array(PK)
    return dict(pk=PK.mean(axis=0), a3=float(np.mean(A3)), a4=float(np.mean(A4)),
                a4_s=float(np.std(A4, ddof=1)), nW=len(PK))


def _matched(fn):
    z = np.load(os.path.join(SPEC, fn))
    ls, Dl = np.asarray(z['ls'], float), np.asarray(z['Dl'], float)
    s = _sweep(CS.bin_spectrum(ls, Dl * np.interp(ls, _CLG, _RAT)) * _FACB)
    s['lA_rep'] = float(z['l_A'])
    return s


_MSKY = _sweep(CS.X_DATA * _FACB)
_MNSK = _matched('cc66_cr_x_h686_L2000.npz')
_MAOR = _matched('cc66_cr_x_h686_L2000_leafrec1_distances.npz')
print(f"  {'row':>34} {'peaks (matched locator)':>30} {'comb 1-4':>10} {'1-3':>8} {'geom l_A':>9}")
for _nm, _s in (('THE SKY, this locator', _MSKY),
                ('namesake L2000 (LEAFREC=0)', _MNSK),
                ('** ARM OF RECORD, distances **', _MAOR)):
    _g = f"{_s['lA_rep']:9.3f}" if 'lA_rep' in _s else f"{'--':>9}"
    print(f"  {_nm:>34} {' '.join(f'{v:7.2f}' for v in _s['pk'])} {_s['a4']:>10.3f} "
          f"{_s['a3']:>8.3f} {_g}")
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
      and _MSKY['nW'] == 7,
      f"sky comb 1-4 = {_MSKY['a4']:.3f} +- {_MSKY['a4_s']:.3f} over {_MSKY['nW']} windows; "
      f"sec:intro's three-peak {fit_comb(SKY, 3)[0]:.2f}")
check("⛔⛭⛭ ** AND THE PAPER'S 298.0 IS NOT THE PROCEDURE THE SENTENCE NAMES. **  By that procedure "
      "the NAMESAKE's comb is 300.589 and the ARM OF RECORD's is 299.057, neither of them 298.0.  "
      "The 298.0 is the namesake's raw-grid three-peak comb, on maxima quantised to even `ell` by "
      "`LSTEP=2`.  ⇒ *The pair (298.0, 298.4) is consistent in its FIT -- both three-peak -- and the "
      "arm's half of it is not located by the parabolic procedure at all*",
      abs(_MNSK['a4'] - 300.589) < 0.01 and abs(_MAOR['a4'] - 299.057) < 0.01
      and abs(NEWL2['lA'] - 298.00) < 0.005
      and all(float(v) % 2.0 == 0.0 for v in NEWL2['P']),
      f"matched: namesake {_MNSK['a4']:.3f}, arm of record {_MAOR['a4']:.3f}; raw-grid namesake "
      f"{NEWL2['lA']:.2f} on peaks {[int(v) for v in NEWL2['P']]}")
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
      and _MAOR['a4'] / _MAOR['lA_rep'] < _MNSK['a4'] / _MNSK['lA_rep'] < 1.0,
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
