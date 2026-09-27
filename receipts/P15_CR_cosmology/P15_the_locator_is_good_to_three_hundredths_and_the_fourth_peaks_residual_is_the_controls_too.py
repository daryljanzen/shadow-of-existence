#!/usr/bin/env python3
r"""P15 sec:refit-bound -- ** THE LOCATOR IS GOOD TO THREE HUNDREDTHS OF A MULTIPOLE AT EVERY PEAK,
INCLUDING THE FOURTH -- AND THE RESIDUAL IT MEASURES THERE IS THE CONTROL'S TOO. **

** WHY IT EXISTS. **  `r6941`'s order: `cc66.44` closed the clock route, so what is left undecomposed
is the fourth peak -- the decisive run reporting $222/538/818/1134$ against the sky's
$220.4/537.7/817.3/1123.9$, peaks one to three landing within a grid step while peak four is $10.1$
out, and the comb fitted on the first three, which makes peak four *** the only one of the four that is
out of sample. ***  ⚠ But the first thing asked is the instrument and not the physics: **establish the
locator's own precision at each of the four peaks before reading any residual off them**, since it was
validated at $\ell_1$ and $\ell_4$ sits where the damping has flattened the peak.  *The stopping rule:
if the locator at $\ell_4$ is worse than ten multipoles the residual is not measured, the order ends at
step one, and that outcome is worth as much as the decomposition.*

⛭⛭ ** THE STOPPING RULE DOES NOT FIRE, AND IT MISSES BY A FACTOR OF FOUR HUNDRED. **  Run again at
`LSTEP=1 LMAXL=2000` -- eight times the multipole sampling, $1900$ multipoles against the reported
$238$, on BOTH arms -- the coarse grid's locator recovers the fine-grid position to
$0.0007/0.0126/0.0283/0.0176$ of a multipole on the control and $0.0035/0.0089/0.0167/0.0229$ on the
arm.  *** At $\ell_4$ it is two hundredths of a multipole against a bar of ten. ***  ⌗ *And the
extremum search is insensitive to its own width: order $3$ through $40$ on the fine grid return the
same four peaks to every printed digit, so the peaks are cleanly isolated and the flattening does not
cost precision.*

⛔ ** WHAT IS NOT PRECISE IS THE PARABOLA'S WINDOW, AND IT IS A BIAS RATHER THAN A NOISE. **  Swept over
`PO-47`'s admissible range $W=15\ldots110$ the located peak moves $0.08/2.77/4.73/5.82$ on the arm and
$0.11/2.98/4.97/6.49$ on the control -- *growing steeply with peak index, because a wider fit on an
increasingly asymmetric, damping-suppressed hump pulls its apex down the envelope's slope.*  ⇒ ** So
the fourth peak's window bias is comparable to the residual being read there -- but it displaces the
sky and both models the same way, which is exactly why the corpus's matched-procedure differencing is
what makes the comparison readable ** and not a convenience.  *At the tight window $W=25$ the anchored
parabola and the three-point parabola agree to $0.2$ of a multipole at every peak.*

⛭⛭⛭ ** AND THE ORDER'S PATTERN IS TWO ARTEFACTS, NEITHER OF THEM PHYSICS. **  *First, the
quartet: $222/538/818/1134$ is `sec:refit-bound`'s LINE-OF-SIGHT path, while every bank in this campaign
is the HIERARCHY path, whose raw grid reading is $220/540/812/1132$ --- and ** at $\ell_3$ the two
bracketing `LSTEP=8` bins differ by four parts in TEN THOUSAND, so which of them is called the peak is a
coin flip: the paper quotes $820$ on this path, this run's locator picks $812$, and the sub-bin apex is
$815.40$ with the fine grid's own maximum at $815$. **  Sub-bin the arm is
$221.96/536.11/815.40/1130.53$, so the residual is $+1.56/-1.60/-1.90/+6.63$ --- peaks two and three are
not "on", they are each about $1.7$ LOW, and peak four is $6.6$ out rather than $10.1$.*  ** Second, and decisive: the
CONTROL produces nearly all of it. **  Through the identical locator the control's residual is
$-0.05/-1.41/-2.97/+5.32$, so

    arm  -  control  =  +1.61 / -0.19 / +1.07 / +1.31       (mean +0.95, spread 1.79)

⇒ *** What belongs to this construction is a near-constant displacement of about ONE multipole at all
four peaks -- a constant $\Delta\ell$, the FIRST of the three shapes the order enumerated, and not the
ruler's constant $\Delta\ell/\ell$ (which would need $0.52/1.25/1.91/2.65$) nor a driving error growing
with $\ell$. ***  ⇒ ** So the pattern needs ONE systematic and not two, and the "one-off,
two-and-three-on, four-off" shape that fitted none of the three candidates was the raw grid plus an
undifferenced sky comparison. **  ⌗ *And `PO-47` already measured what the sky can say about that one
multipole: at the fourth peak the arm-minus-control displacement is $0.83\sigma$ of the sky's own
locating spread of $2.36$ -- so the sky cannot tell it from zero at any peak, which is why this is
reported as a shape and not as a disagreement.*

⚑ ** ⓷ THE THREE-WAY SEPARATION AT EVERY PEAK INDEX, AND THE SHARES ARE STRONGLY $n$-DEPENDENT. **
Running `cc66.44`'s guard -- the relocation through $r_s(\mathrm{ETA\_LS})$, the visibility's
re-weighting of the kernel from the $\cos(kr_s)$ injection, and the plasma's own phase as the
remainder -- at all four peaks on the fine grid:

    n    total motion     relocation      visibility        plasma
    1      +1.893%           31.2%           9.2%           59.6%
    2      +0.628%           94.1%          26.4%          -20.5%
    3      +0.709%           83.4%          22.7%           -6.0%
    4      +0.662%           89.3%          23.5%          -12.8%

*** $\ell_1$ is the outlier and nothing else is: at $\ell_2$ through $\ell_4$ the motion is almost
entirely geometric and the plasma's phase partially CANCELS it, while at $\ell_1$ the plasma dominates
and adds. ***  By the order's reading, fixed in advance: the plasma's share does not grow with $n$, so
the residual is not in the driving; the relocation share does grow, which points at the ruler.  ⚠ ** But
the third reading is the one that applies: the shares are not flat and the residual is not reached. **
The family's motion is $+0.6$ to $+0.7$ per cent with one sign at every peak, and the sky residual
alternates -- *so the decomposition does not cover the four-peak pattern, which is a statement about
the guard's coverage and not a failure of the run.*

⌗ *The motions themselves are resolved: fine against coarse they agree to $0.02$ of a multipole at every
peak, so the shares are the spectra's and not the grid's.*

** WHAT IS NOT CLAIMED. **  NOT a mechanism for the one-multipole constant offset; it is measured,
named as a constant $\Delta\ell$, and left.  NOT a re-derivation of the sky's locating spread, which is
`PO-47`'s and is cited.  NOT that the window bias is an error in the corpus's comparisons -- it is a
convention, and what is established here is that it is shared and that the tight window agrees with the
three-point locator.  NOT that peak four is uninteresting: it is the largest residual of the four, and
what this shows is that four fifths of it is the control's.  NOT a verdict on the two-rate assignment,
which is the row's question.  No refit, nothing touching `prop:flat` or the clock family, and no corpus
edits -- the paper-side consequences are reported to 66 rather than applied.

COMPUTES: scope.
  * ** EVERY COSMOLOGICAL PARAMETER IS BANKED, NOT CHOSEN HERE. **  Both arms at `r6825+cc66.25`'s
    verified 185-bin refit minima, and the fine runs are the SAME configuration at `LSTEP=1 LMAXL=2000`
    -- eight times the multipole sampling and nothing else changed.  Nothing here re-fits.
  * `spectra/r6941_fine_{lcdm,cr}.npz` (the fine reference, both arms) and
    `r6941_fine_cr_visleaf.npz` (the arm's `VISLEAF=1` endpoint, real and injected).
  * The coarse side is `cc66_r185_verify_*`, the reported spectra, and the `VISLEAF` motions are
    checked against `r6929_scan_cr.npz`; the relocation uses `r6929_geometry.npz`'s
    $r_s(\mathrm{ETA\_LS})$.  Read with the SAME locator throughout.
  * The sky quartet $220.4/537.7/817.3/1123.9$ is `P15` \S`intro`'s own locator on `plik_lite` TT and
    the fourth peak's spread $2.36$ is `PO-47`'s; both are taken as given and neither is re-derived.
"""
import os
import sys

import numpy as np
from scipy.signal import argrelextrema

FAILS = []


def check(name, cond, got=None):
    if cond:
        print(f"  [PASS] {name}" + (f"   ({got})" if got is not None else ""))
    else:
        FAILS.append(name)
        print(f"  [FAIL] {name}" + (f"   (got {got})" if got is not None else ""))


print(__doc__)
print("=" * 100)

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
NEED = ('r6941_fine_lcdm.npz', 'r6941_fine_cr.npz', 'r6941_fine_cr_visleaf.npz',
        'r6929_scan_cr.npz', 'r6929_geometry.npz', 'cc66_r185_verify_lcdm.npz',
        'cc66_r185_verify_cr.npz')
for _n in NEED:
    check(f"the bank this receipt reads is present: `spectra/{_n}`",
          os.path.exists(os.path.join(SP, _n)), _n)
if FAILS:
    print("\n  ⛔ A BANK THIS RECEIPT READS IS NOT ON DISK, so nothing is read and this receipt FAILS.")
    print("=" * 100)
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)

F = {t: np.load(os.path.join(SP, f'r6941_fine_{t}.npz')) for t in ('lcdm', 'cr')}
V = np.load(os.path.join(SP, 'r6941_fine_cr_visleaf.npz'))
C = {t: np.load(os.path.join(SP, f'cc66_r185_verify_{t}.npz')) for t in ('lcdm', 'cr')}
S = np.load(os.path.join(SP, 'r6929_scan_cr.npz'))
GE = np.load(os.path.join(SP, 'r6929_geometry.npz'))

SKY = np.array([220.4, 537.7, 817.3, 1123.9])   # P15 sec:intro's own locator on plik_lite TT
SKY_SIG4 = 2.36                                 # PO-47: the sky's fourth peak, 1121.9 +- 2.36
BAR = 10.0                                      # the order's stopping rule at l_4
WS = [15, 25, 40, 55, 80, 110]                  # PO-47's admissible parabola windows


def peaks_sub(ls, Dl, n=4, order=3):
    """the three-point parabola at the extremum -- `cc66`'s locator, unchanged"""
    out = []
    for i in argrelextrema(Dl, np.greater, order=order)[0][:n]:
        if i < 1 or i > len(ls) - 2:
            out.append(float(ls[i]))
            continue
        y0, y1, y2 = Dl[i - 1], Dl[i], Dl[i + 1]
        den = y0 - 2 * y1 + y2
        off = 0.5 * (y0 - y2) / den if den != 0 else 0.0
        out.append(float(ls[i] + off * (ls[i + 1] - ls[i])))
    return out


def peaks_raw(ls, Dl, n=4, order=3):
    return [float(ls[i]) for i in argrelextrema(Dl, np.greater, order=order)[0][:n]]


def anchored(ls, Dl, anchors, W):
    """`PO-47`'s window-anchored parabola: the same fit, the window fixed on the peak"""
    out = []
    for a in anchors:
        k = (ls >= a - W) & (ls <= a + W)
        if k.sum() < 5:
            out.append(np.nan)
            continue
        c = np.polyfit(ls[k], Dl[k], 2)
        out.append(float(-c[1] / (2 * c[0])) if c[0] < 0 else np.nan)
    return out


FINE = {t: peaks_sub(F[t]['ls'].astype(float), F[t]['Dl']) for t in F}
COARSE = {t: peaks_sub(C[t]['ls'].astype(float), C[t]['Dl']) for t in C}
RAW = {t: peaks_raw(C[t]['ls'].astype(float), C[t]['Dl']) for t in C}

# ===================================================================================================
print("\nPART 1 -- ⓶a THE GRID HALF: THE LOCATOR AGAINST A REFERENCE EIGHT TIMES AS FINE, PER PEAK.")
print("-" * 100)
check("the fine runs ARE eight times the reported sampling, at the reported reach, on both arms",
      all(len(F[t]['ls']) == 1900 and F[t]['ls'][1] - F[t]['ls'][0] == 1 for t in F)
      and all(len(C[t]['ls']) == 238 for t in C),
      f"{len(F['cr']['ls'])} multipoles at LSTEP=1 against {len(C['cr']['ls'])} at LSTEP=8")
print(f"    {'arm':7} {'':8} " + " ".join(f"{'l'+str(i+1):>10}" for i in range(4)))
ERR = {}
for t in ('lcdm', 'cr'):
    ERR[t] = [abs(a - b) for a, b in zip(FINE[t], COARSE[t])]
    print(f"    {t:7} {'fine':8} " + " ".join(f"{x:10.3f}" for x in FINE[t]))
    print(f"    {'':7} {'LSTEP=8':8} " + " ".join(f"{x:10.3f}" for x in COARSE[t]))
    print(f"    {'':7} {'error':8} " + " ".join(f"{x:10.4f}" for x in ERR[t]))
check("⛭⛭ ** THE STOPPING RULE DOES NOT FIRE. **  The coarse locator recovers the fine-grid position "
      "to better than three hundredths of a multipole at EVERY peak on BOTH arms -- including the "
      "fourth, where the damping has flattened it",
      max(max(ERR[t]) for t in ERR) < 0.03,
      f"worst of eight: {max(max(ERR[t]) for t in ERR):.4f} of a multipole")
check(f"⇒ and it misses the order's ten-multipole bar at l_4 by a factor of four hundred, so the "
      f"residual IS measured and the order does not end at step one",
      max(ERR['cr'][3], ERR['lcdm'][3]) < BAR / 100,
      f"l_4 error {ERR['cr'][3]:.4f} (arm) / {ERR['lcdm'][3]:.4f} (control) against the bar {BAR:.0f}")
_ords = {od: peaks_sub(F['cr']['ls'].astype(float), F['cr']['Dl'], order=od)
         for od in (3, 8, 16, 24, 40)}
check("⌗ and the extremum search is insensitive to its own width on the fine grid -- order 3 to 40 "
      "returns the same four peaks -- so the flattening does not cost the SEARCH either",
      max(abs(_ords[od][i] - _ords[3][i]) for od in _ords for i in range(4)) < 1e-9,
      "identical to every printed digit at order 3, 8, 16, 24 and 40")

# ===================================================================================================
print("\nPART 2 -- ⓶b THE PROCEDURE HALF: THE PARABOLA'S WINDOW, WHICH IS A BIAS AND NOT A NOISE.")
print("-" * 100)
SPREAD, TIGHT = {}, {}
for t in ('lcdm', 'cr'):
    ls, Dl = F[t]['ls'].astype(float), F[t]['Dl']
    R = np.array([anchored(ls, Dl, FINE[t], W) for W in WS])
    SPREAD[t] = [float(np.nanmax(R[:, i]) - np.nanmin(R[:, i])) for i in range(4)]
    TIGHT[t] = [abs(float(R[1, i]) - FINE[t][i]) for i in range(4)]
    print(f"    {t}:")
    for W, row in zip(WS, R):
        print(f"      W={W:4d} " + " ".join(f"{x:10.3f}" for x in row))
    print(f"      spread " + " ".join(f"{x:10.3f}" for x in SPREAD[t]))
check("⛔ the window bias GROWS steeply with peak index on both arms -- hundredths at l_1, nearly six "
      "multipoles at l_4 -- because a wider fit on an asymmetric, damping-suppressed hump pulls its "
      "apex down the envelope's slope",
      all(SPREAD[t][0] < 0.2 and SPREAD[t][3] > 5.0 and SPREAD[t] == sorted(SPREAD[t]) for t in SPREAD),
      f"arm {['%.2f' % x for x in SPREAD['cr']]}, control {['%.2f' % x for x in SPREAD['lcdm']]}")
check("⇒ ** so at l_4 the window's bias is comparable to the residual being read there ** -- and it "
      "displaces the sky and both models alike, which is why matched-procedure differencing is what "
      "makes the comparison readable rather than a convenience",
      SPREAD['cr'][3] > 0.5 * abs(FINE['cr'][3] - SKY[3]),
      f"window bias {SPREAD['cr'][3]:.2f} against the arm's residual "
      f"{FINE['cr'][3]-SKY[3]:+.2f} at l_4")
check("⌗ and at the tight window the anchored parabola and the three-point locator agree to a fifth of "
      "a multipole at every peak, so the two conventions are the same measurement where the bias is "
      "small", max(max(TIGHT[t]) for t in TIGHT) < 0.25,
      f"worst of eight at W=25: {max(max(TIGHT[t]) for t in TIGHT):.3f}")

# ===================================================================================================
print("\nPART 3 -- ⛭⛭⛭ THE ORDER'S PATTERN IS TWO ARTEFACTS: THE RAW GRID, AND AN UNDIFFERENCED SKY.")
print("-" * 100)
print(f"    {'n':>2} {'arm':>9} {'control':>9} {'sky':>8} {'arm-sky':>9} {'ctl-sky':>9} {'arm-ctl':>9}")
D_AC = []
for n in range(4):
    D_AC.append(FINE['cr'][n] - FINE['lcdm'][n])
    print(f"    {n+1:>2} {FINE['cr'][n]:9.3f} {FINE['lcdm'][n]:9.3f} {SKY[n]:8.1f} "
          f"{FINE['cr'][n]-SKY[n]:+9.3f} {FINE['lcdm'][n]-SKY[n]:+9.3f} {D_AC[n]:+9.3f}")
D_AC = np.array(D_AC)
_i812, _i820 = (int(np.where(C['cr']['ls'] == L)[0][0]) for L in (812, 820))
_tie = abs(float(C['cr']['Dl'][_i812] - C['cr']['Dl'][_i820])) / float(C['cr']['Dl'][_i812])
print(f"    the order's quartet 222/538/818/1134 is `sec:refit-bound`'s LINE-OF-SIGHT path; every bank")
print(f"    here is the HIERARCHY path, whose raw grid reading is "
      f"{[int(x) for x in RAW['cr']]} -- and at l_3 the two bracketing bins differ by "
      f"{100*_tie:.3f} per cent")
check("⛔ ** AND THE RAW GRID READING IS NOT A MEASUREMENT AT l_3 AT ALL: the two bracketing `LSTEP=8` "
      "bins differ by four parts in TEN THOUSAND, so which one is called the peak is a coin flip -- "
      "the paper quotes 820 on this path, this run's locator picks 812, and the sub-bin apex is "
      "815.40, with the fine grid's own maximum at 815 **",
      _tie < 1e-3 and set(RAW['cr'][2:3]) <= {812.0, 820.0} and abs(FINE['cr'][2] - 815.40) < 0.05,
      f"the l_3 bins differ by {100*_tie:.3f} per cent; raw {int(RAW['cr'][2])}, sub-bin "
      f"{FINE['cr'][2]:.2f}")
check("⇒ and sub-bin the arm's quartet is 221.96/536.11/815.40/1130.53, so the residual against the "
      "sky is +1.56 / -1.60 / -1.90 / +6.63: ** peaks two and three are not 'on', they are each about "
      "1.7 LOW, and peak four is 6.6 out rather than the order's 10.1 **",
      abs((FINE['cr'][3] - SKY[3]) - 6.6) < 0.2 and abs(FINE['cr'][1] - SKY[1]) > 1.0
      and abs(FINE['cr'][2] - SKY[2]) > 1.0,
      f"sub-bin residual {['%+.2f' % (FINE['cr'][n]-SKY[n]) for n in range(4)]} against the order's "
      f"+1.6 / +0.3 / +0.7 / +10.1")
check("⛭⛭⛭ ** AND THE CONTROL PRODUCES NEARLY ALL OF IT. **  Through the identical locator the "
      "control's fourth-peak residual is +5.32 against the arm's +6.63, so four fifths of the largest "
      "residual in this sector is not the construction's",
      (FINE['lcdm'][3] - SKY[3]) / (FINE['cr'][3] - SKY[3]) > 0.75,
      f"control +{FINE['lcdm'][3]-SKY[3]:.2f} of the arm's +{FINE['cr'][3]-SKY[3]:.2f}, "
      f"{100*(FINE['lcdm'][3]-SKY[3])/(FINE['cr'][3]-SKY[3]):.0f} per cent")
_dl_l = np.array([D_AC[n] / FINE['cr'][n] for n in range(4)])
_pred_ruler = _dl_l.mean() * np.array(FINE['cr'])
_r_const = float(np.std(D_AC - D_AC.mean()))
_r_ruler = float(np.std(D_AC - _pred_ruler))
print(f"    arm-control: mean {D_AC.mean():+.3f}, spread {D_AC.max()-D_AC.min():.3f}")
print(f"    a constant dl fits with rms {_r_const:.3f}; a constant dl/l (the ruler) predicts "
      f"{['%.2f' % x for x in _pred_ruler]} and fits with rms {_r_ruler:.3f}")
check("⇒ *** WHAT IS THE CONSTRUCTION'S IS A NEAR-CONSTANT ONE-MULTIPOLE DISPLACEMENT AT ALL FOUR "
      "PEAKS -- a constant dl, the FIRST of the order's three shapes -- and it fits half again better "
      "than the ruler's constant dl/l ***",
      _r_const < 0.75 * _r_ruler and 0.5 < D_AC.mean() < 1.5,
      f"constant dl rms {_r_const:.3f} against the ruler's {_r_ruler:.3f}, a factor "
      f"{_r_ruler/_r_const:.2f}")
check("⇒ ** SO THE PATTERN NEEDS ONE SYSTEMATIC AND NOT TWO **, and the 'one-off, two-and-three-on, "
      "four-off' shape that fitted none of the three candidates was the raw grid plus an "
      "undifferenced sky comparison -- neither of them physics",
      _r_const < 1.2 and abs(D_AC.mean()) > 3 * max(ERR['cr'][:4]),
      f"the four displacements are {['%+.2f' % x for x in D_AC]} about a mean of {D_AC.mean():+.2f}, "
      f"against a locator error of {max(ERR['cr']):.3f}")
check("⌗ and the sky cannot tell that one multipole from zero: `PO-47` measured its fourth peak at "
      "1121.9 +- 2.36 and put the arm-minus-control displacement at 0.83 sigma, so this is reported as "
      "a SHAPE and not as a disagreement",
      abs(D_AC[3]) < SKY_SIG4 and all(abs(x) < SKY_SIG4 for x in D_AC),
      f"every |arm - control| is under the sky's own spread of {SKY_SIG4}: "
      f"{['%.2f' % abs(x) for x in D_AC]}")

# ===================================================================================================
print("\nPART 4 -- ⓷ THE THREE-WAY SEPARATION AT EVERY PEAK INDEX, ON THE FINE GRID.")
print("-" * 100)
P0 = FINE['cr']
P1 = peaks_sub(V['ls__comb_f1'].astype(float), V['Dl__comb_f1'])
I0 = peaks_sub(V['ls__inj_f0'].astype(float), V['Dl__inj_f0'])
I1 = peaks_sub(V['ls__inj_f1'].astype(float), V['Dl__inj_f1'])
_rs = GE['rs_leaf__cr']
REL = float(_rs[0] / _rs[int(np.argmin(np.abs(GE['f__cr'] - 1.0)))] - 1.0)
print(f"    the relocation through r_s(ETA_LS), common to every n: {100*REL:+.4f}%")
print(f"    {'n':>2} {'total %':>9} {'reloc':>8} {'vis':>8} {'plasma':>9}")
SH = []
for n in range(4):
    tot = P1[n] / P0[n] - 1.0
    inj = I1[n] / I0[n] - 1.0
    SH.append((tot, REL / tot, (inj - REL) / tot, (tot - inj) / tot))
    print(f"    {n+1:>2} {100*tot:+9.4f} {100*SH[n][1]:7.1f}% {100*SH[n][2]:7.1f}% "
          f"{100*SH[n][3]:8.1f}%")
_c0 = peaks_sub(S['ls__comb_cr_f0'].astype(float), S['Dl__comb_cr_f0'])
_c1 = peaks_sub(S['ls__comb_cr_f1'].astype(float), S['Dl__comb_cr_f1'])
_dm = max(abs((P1[n] - P0[n]) - (_c1[n] - _c0[n])) for n in range(4))
check("the motions the shares are built on are resolved: fine against coarse they agree to a fiftieth "
      "of a multipole at every peak, so the shares are the spectra's and not the grid's",
      _dm < 0.05, f"worst difference {_dm:.4f} of a multipole")
check("⚑ l_1 IS THE OUTLIER AND NOTHING ELSE IS: at l_2 through l_4 the motion is almost entirely "
      "geometric and the plasma's phase partially CANCELS it, where at l_1 the plasma dominates and "
      "adds", SH[0][3] > 0.5 and all(SH[n][3] < 0 for n in (1, 2, 3)),
      f"plasma share {100*SH[0][3]:.1f}% at l_1 against "
      f"{', '.join('%.1f%%' % (100*SH[n][3]) for n in (1,2,3))}")
check("⇒ by the order's reading, fixed in advance: the plasma's share does NOT grow with n, so the "
      "residual is not in the driving; and the relocation share DOES grow, which points at the ruler",
      SH[3][3] < SH[0][3] and SH[3][1] > 2 * SH[0][1],
      f"relocation {100*SH[0][1]:.1f}% -> {100*SH[3][1]:.1f}%, plasma {100*SH[0][3]:.1f}% -> "
      f"{100*SH[3][3]:.1f}%")
check("⚠ ** BUT THE THIRD READING IS THE ONE THAT APPLIES: the shares are not flat and the residual is "
      "not reached. **  The family's motion is +0.6 to +0.7 per cent with ONE sign at every peak while "
      "the sky residual ALTERNATES -- so the decomposition does not cover the four-peak pattern, which "
      "is a statement about the guard's coverage rather than a failure of the run",
      all(SH[n][0] > 0 for n in range(4))
      and not all(np.sign(FINE['cr'][n] - SKY[n]) == np.sign(SH[n][0]) for n in range(4)),
      "the motion is positive at every peak; the residual is +1.56 / -1.60 / -1.90 / +6.63")

# ===================================================================================================
print("\n" + "=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    sys.exit(1)
print("GATES: ALL PASS.")
print(f"""
  ⛭⛭ THE LOCATOR IS NOT THE PROBLEM.  Against a reference eight times as fine, at the reported reach,
  the reported grid's locator recovers every peak on both arms to under three hundredths of a
  multipole -- {ERR['cr'][3]:.4f} at l_4 on the arm against the order's bar of ten.  The order does not
  end at step one.  ⛔ What is imprecise is the parabola's WINDOW, whose bias grows with peak index to
  {SPREAD['cr'][3]:.2f} multipoles at l_4 -- comparable to the residual, and shared by the sky and both
  models, which is what matched-procedure differencing is for.

  ⛭⛭⛭ AND THE PATTERN THE ORDER ASKED ABOUT IS TWO ARTEFACTS.  222/538/818/1134 is the raw grid:
  sub-bin the arm is {FINE['cr'][0]:.2f}/{FINE['cr'][1]:.2f}/{FINE['cr'][2]:.2f}/{FINE['cr'][3]:.2f},
  so the residual is +1.56 / -1.60 / -1.90 / +6.63 and peaks two and three were never 'on'.  And the
  CONTROL carries {100*(FINE['lcdm'][3]-SKY[3])/(FINE['cr'][3]-SKY[3]):.0f} per cent of the fourth
  peak's residual, so what is the construction's is {D_AC.mean():+.2f} of a multipole at all four --
  ONE systematic, of the constant-dl shape, fitting half again better than the ruler's constant dl/l,
  with every one of the four inside the sky's own locating spread that PO-47 measured.

  ⚑ THE SEPARATION AT EVERY PEAK: relocation {100*SH[0][1]:.0f}% -> {100*SH[3][1]:.0f}%, the
  visibility's weighting {100*SH[0][2]:.0f}% -> {100*SH[3][2]:.0f}%, the plasma {100*SH[0][3]:.0f}% ->
  {100*SH[3][3]:.0f}%.  l_1 is the outlier; at l_2 to l_4 the motion is geometric and the plasma's
  phase cancels part of it.  The shares are not flat, and they do not reach the residual.

  NOT CLAIMED: a mechanism for the one-multipole offset; a re-derivation of the sky's spread, which is
  PO-47's; that the window convention is an error rather than a convention; a verdict on the two-rate
  assignment; and no corpus edits -- the paper-side consequences go to 66.
""")
sys.exit(0)
