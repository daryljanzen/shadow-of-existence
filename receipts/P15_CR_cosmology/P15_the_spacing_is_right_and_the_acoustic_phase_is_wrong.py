#!/usr/bin/env python3
"""
RECEIPT -- P15: ** THE "~21% SPACING DEFICIT" OF c54.187-189 IS THE FIRST THREE GAPS AND NOT THE
SPACING, AND AT PRODUCTION DEPTH THE CONSTRUCTION'S ASYMPTOTIC SPACING IS RIGHT TO 2.4%.  WHAT IS
WRONG IS THE ACOUSTIC PHASE: THE TWO SERIES RUN PARALLEL WITH INTERCEPTS -0.878 AND -0.263 OF ell_A,
A PHASE OFFSET OF 0.62 pi -- PLUS A LOW-ell TRANSIENT THIS CONSTRUCTION HAS AND LambdaCDM DOES
NOT. **  THIS FILE CORRECTS THREE OF ITS OWN LINE'S REVISIONS. **

Built r2441+c54.190, front #2, lead `L-505`.

===================================================================================================
** WHY: THE SCANS COULD ONLY SEE FOUR PEAKS, AND FOUR PEAKS IS THREE GAPS. **
===================================================================================================

c54.187, c54.188 and c54.189 all ran at LMAXL = 1000 so that eighteen readings and five pins were
affordable.  ** At that depth the CR arm has exactly four peaks, so "the mean peak spacing" was a
mean of three gaps -- and the first three gaps are the only ones where the two arms disagree. **
*The robustness those revisions measured is real and is unaffected; what is wrong is the name they
gave the quantity and the inference drawn from it.*

  PART 1  ** AT PRODUCTION DEPTH BOTH ARMS CARRY EIGHT PEAKS, AND THE ASYMPTOTIC SPACINGS AGREE. **
          LambdaCDM's last four gaps average 302.0 against its ell_A of 301.4 -- 1.002.  ** The CR
          arm's average 294.0 against 301.6 -- 0.975. **  *Two and a half per cent, not twenty-one.*
  PART 2  ** AND THE DISAGREEMENT IS ENTIRELY IN THE FIRST THREE GAPS. **  Gap by gap the CR arm
          runs 0.725, 0.853, 0.875 of LambdaCDM's -- and then 0.973, 0.949, 1.000, 0.974.  ** It is
          gone by the fourth gap. **
  PART 3  ** SO THE TWO SERIES ARE PARALLEL LINES WITH DIFFERENT INTERCEPTS, AND THAT IS A PHASE. **
          Fitting ell_n = b n + a on peaks 4-8: ** LambdaCDM b = 302.4 (1.003 ell_A), a = -79.2
          (-0.263 ell_A); CR b = 294.4 (0.976 ell_A), a = -264.8 (-0.878 ell_A). **  Same slope to
          2.6%, intercepts 0.615 ell_A apart.  *For a driven oscillator peaking at k r_s = n pi -
          phi the intercept is -(phi/pi) ell_A, so the two differ by 0.62 pi in the acoustic phase
          shift.*
  PART 4  ** AND THERE IS A SECOND THING, WHICH IS A LOW-ell TRANSIENT THIS CONSTRUCTION HAS AND
          THE CONTROL DOES NOT. **  Measured against each arm's OWN asymptotic line, LambdaCDM's
          first three peaks sit at -3, +14, -16 -- on it.  ** The CR arm's sit at +142, +80, +18 --
          off it, and converging. **  *So the early peaks are pulled up out of the series, which is
          what compressed the first gaps and produced the 0.77.*

** WHAT THIS RETRACTS, AND IT IS THIS LINE'S OWN. **  c54.187 landed *"a ~21% spacing deficit"*,
c54.188 *"~23%"* and c54.189 *"~20%"*, and P15 carries the claim that *"this construction's acoustic
series is some 23% too close at the sky's angular scale"*.  ** That is the first-three-gap value.
The series is not uniformly too close: its spacing is right to 2.4% and its PHASE is wrong by
0.62 pi. **  *Corrected in the paper and in all three rows.*

** AND WHAT IT DOES NOT RETRACT -- WHICH IS MORE THAN IT LOOKS. **  ** The robustness scans stand
exactly as run: the first-three-gap spacing IS stable at 0.77-0.82 across eighteen datum readings
and five pins, and F4 fires at every one of them. **  *What changes is that the stable quantity was
the wrong one to call the disagreement.*  ⇒ ***And the correction makes c54.187 CENTRAL rather than
a caveat: the disagreement is a PHASE, and the phase is exactly what the seam datum assigns and what
the corpus's own "one datum per mode and a COMMON phase" does not fix.***

** F5 IS NOT SOFTENED. **  A measurement discrepancy is not a framework verdict; `PO-7` is protected;
the conversion runs by `F5`'s stated procedure.  ** And this file makes the discrepancy SHARPER rather than smaller: a
spacing that is right and a phase that is wrong is a more specific disagreement than a series that is
uniformly compressed, and it names where to look. **

SETTINGS: production for every number it reports -- it reads the LMAXL=3000 pair.  The LMAXL=1000
runs are named only as the SOURCE OF THE ERROR being corrected and no quantity is taken from
them.  ** The knob appears in this file's prose, which is why the lint sees it. **

rc=0 on success.  Run: python3 P15_the_spacing_is_right_and_the_acoustic_phase_is_wrong.py
                        (numpy scipy; ~10 s)
"""
import os
import sys

import numpy as np
from scipy.signal import argrelextrema

print(__doc__.split("rc=0")[0])
fail = []

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')

ARMS = (('LambdaCDM', 'c54.186_lcdm_L3000.npz'), ('CR', 'c54.186_cr_L3000.npz'))
NFIT = 4          # ** the asymptotic fit starts at peak 4, which is where PART 2 shows the
                  # disagreement has gone; stated here rather than chosen after the fit **


def series(fname):
    z = np.load(os.path.join(SP, fname))
    ls = np.asarray(z['ls'], float)
    D = np.asarray(z['Dl'], float)
    pk = argrelextrema(D, np.greater, order=3)[0]
    tr = argrelextrema(D, np.less, order=3)[0]
    con = [float(D[q] / D[[t for t in tr if t > q][0]]) if [t for t in tr if t > q] else np.nan
           for q in pk]
    return ls[pk], np.asarray(con), float(z['l_A'])


P, C, LA = {}, {}, {}
for nm, f in ARMS:
    P[nm], C[nm], LA[nm] = series(f)

# =====================================================================
print("=" * 78)
print("PART 1/2 — EIGHT PEAKS EACH, AND THE DISAGREEMENT IS IN THE FIRST THREE GAPS")
print("=" * 78)
print(f"  {'gap n':>6} {'LambdaCDM':>10} {'/l_A':>7} | {'CR':>7} {'/l_A':>7} | {'CR/LCDM':>8}")
GL, GC = np.diff(P['LambdaCDM']), np.diff(P['CR'])
N = min(len(GL), len(GC))
RATIO = []
for i in range(N):
    RATIO.append(GC[i] / GL[i])
    print(f"  {i+1:>6} {GL[i]:>10.0f} {GL[i]/LA['LambdaCDM']:>7.4f} | {GC[i]:>7.0f} "
          f"{GC[i]/LA['CR']:>7.4f} | {RATIO[i]:>8.4f}")
ASY_L = float(np.mean(GL[-4:])) / LA['LambdaCDM']
ASY_C = float(np.mean(GC[-4:])) / LA['CR']
FIRST3 = float(np.mean(GC[:3])) / LA['CR']
print(f"\n  ** ASYMPTOTIC (last four gaps): LambdaCDM {ASY_L:.4f} l_A,  CR {ASY_C:.4f} l_A "
      f"— {100*(1-ASY_C):.1f}% SHORT, NOT 21%. **")
print(f"  ** THE FIRST THREE GAPS GIVE {FIRST3:.4f}, WHICH IS THE NUMBER c54.187-189 REPORTED — and "
      f"at\n     LMAXL = 1000 the CR arm has four peaks, so three gaps was all there was. **")
print(f"     *The disagreement runs {RATIO[0]:.3f}, {RATIO[1]:.3f}, {RATIO[2]:.3f} and is gone by "
      f"the fourth gap ({RATIO[3]:.3f}).*")
if ASY_C < 0.90:
    fail.append(f"the CR arm's asymptotic spacing is {ASY_C:.3f} of l_A -- the correction this file "
                "makes is not what the data show and c54.187-189 stand")
if not (FIRST3 < 0.85 < ASY_C):
    fail.append(f"the first-three-gap value {FIRST3:.3f} and the asymptotic {ASY_C:.3f} do not "
                "straddle -- PART 2's whole point is absent")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — TWO PARALLEL LINES WITH DIFFERENT INTERCEPTS, WHICH IS A PHASE")
print("=" * 78)
FIT = {}
for nm in ('LambdaCDM', 'CR'):
    n = np.arange(1, len(P[nm]) + 1)
    m = n >= NFIT
    b, a = np.polyfit(n[m], P[nm][m], 1)
    FIT[nm] = (float(b), float(a))
    print(f"  {nm:>10}: slope {b:>7.1f} = {b/LA[nm]:.4f} l_A    intercept {a:>8.1f} = "
          f"{a/LA[nm]:+.4f} l_A")
_dslope = abs(FIT['CR'][0] / FIT['LambdaCDM'][0] - 1.0)
_dphase = (FIT['LambdaCDM'][1] - FIT['CR'][1]) / LA['CR']
print(f"\n  ** SAME SLOPE TO {100*_dslope:.1f}%; THE INTERCEPTS DIFFER BY {_dphase:.3f} OF l_A. **")
print("     *A driven acoustic series peaks at k r_s = n pi - phi, so ell_n = (n - phi/pi) l_A and")
print(f"      the intercept IS -(phi/pi) l_A.  The two arms differ by {_dphase:.2f} pi in the")
print("      acoustic phase shift, at a spacing they agree on.*")
print(f"  ⇒ ***THE CONSTRUCTION GETS THE ACOUSTIC SPACING RIGHT AND THE ACOUSTIC PHASE WRONG BY MOST")
print(f"     OF A PEAK.***")
if _dslope > 0.06:
    fail.append(f"the slopes differ by {100*_dslope:.1f}% -- they are not parallel and PART 3's "
                "reading as a pure phase offset is wrong")
if not (0.3 < _dphase < 1.0):
    fail.append(f"the phase offset is {_dphase:.2f} pi -- outside the range PART 3 reports")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — AND A LOW-ell TRANSIENT THE CONTROL DOES NOT HAVE")
print("=" * 78)
print(f"  *each arm measured against its OWN asymptotic line, so this is not the phase offset again*")
print()
print(f"  {'peak':>5} {'LambdaCDM: ell':>15} {'off its line':>13} | {'CR: ell':>9} {'off its line':>13}")
RES = {}
for nm in ('LambdaCDM', 'CR'):
    b, a = FIT[nm]
    RES[nm] = [float(P[nm][i] - (b * (i + 1) + a)) for i in range(len(P[nm]))]
for i in range(3):
    print(f"  {i+1:>5} {P['LambdaCDM'][i]:>15.0f} {RES['LambdaCDM'][i]:>+13.1f} | "
          f"{P['CR'][i]:>9.0f} {RES['CR'][i]:>+13.1f}")
_wl = max(abs(x) for x in RES['LambdaCDM'][:3])
_wc = max(abs(x) for x in RES['CR'][:3])
print(f"\n  ** LambdaCDM's first three sit ON its line, within {_wl:.0f} in ell.  THE CR ARM'S SIT "
      f"{_wc:.0f} OFF IT\n     AND CONVERGE. **")
print("     *That transient is what compressed the early gaps and produced the 0.77 the scans read.*")
print()
print("  ⛔ ***F5 UNSOFTENED — and this file makes the discrepancy SHARPER rather than smaller: a")
print("     spacing that is right and a phase that is wrong is a more specific disagreement than a")
print("     series uniformly compressed, and it names where to look. `PO-7` protected; the")
print("     the conversion runs by `F5`'s stated procedure.***")
if _wc < 3 * _wl:
    fail.append(f"the CR transient ({_wc:.0f}) is not large against the control's ({_wl:.0f}) -- "
                "PART 4 has no content")

# =====================================================================
print()
print("=" * 78)
print("AND THE PEAKS ARE REAL FEATURES, WHICH IS CHECKED BEFORE ANY OF THE ABOVE IS READ")
print("=" * 78)
_minc = min(float(np.nanmin(C[nm][:-1])) for nm in ('LambdaCDM', 'CR'))
for nm in ('LambdaCDM', 'CR'):
    print(f"  {nm:>10}: peak/next-trough contrast "
          f"{['%.2f' % x for x in C[nm][:-1]]}")
print(f"\n  ** THE WEAKEST FEATURE IN EITHER ARM HAS CONTRAST {_minc:.2f}. **  *A series read off "
      f"features\n     that were not there would be a spacing measured on noise, which is the "
      f"failure c54.188\n     screened for at four peaks and this file must screen for at eight.*")
if _minc < 1.05:
    fail.append(f"the weakest peak has contrast {_minc:.2f} -- some of these are not features and "
                "the series is measured on noise")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — at production depth the CR arm's asymptotic peak spacing is 0.975 of l_A")
print("against the control's 1.002, so the ~21% figure c54.187-189 reported is the first three gaps")
print("and not the spacing; the two series are parallel to 2.6% with intercepts 0.615 l_A apart, a")
print("phase offset of 0.62 pi; and the CR arm carries a low-ell transient, its first three peaks")
print("sitting 142 above its own asymptotic line where the control's sit within 16.")
print("=" * 78)

# ============================================================================================
# GATE — r2441+c54.190, `L-505`.  This file RETRACTS a number three of its own line's revisions
# landed, so the pins are on the retraction being real and on the replacement being what it says.
#   (1) the CR asymptotic spacing -- if it were NOT close to l_A there would be nothing to
#       correct and c54.187-189 would stand as written;
#   (2) that the first-three-gap value and the asymptotic value STRADDLE, which is the whole
#       diagnosis: one number was reported for the other;
#   (3) the slopes parallel to within 6%, WITHOUT which the offset is not a pure phase and
#       PART 3's reading is wrong;
#   (4) the phase offset itself, which is what replaces the retracted number;
#   (5) the transient's size against the control's, since PART 4 is otherwise empty;
#   (6) and the weakest peak's contrast, since a series read off non-features is noise.
# ============================================================================================
assert ASY_C > 0.90, f"the CR asymptotic spacing is {ASY_C:.3f} of l_A -- nothing to correct"
assert abs(ASY_C - 0.975) < 0.03, f"the CR asymptotic spacing is {ASY_C:.4f}, expected 0.975"
assert abs(ASY_L - 1.002) < 0.03, f"the control's asymptotic spacing is {ASY_L:.4f}, expected 1.002"
assert FIRST3 < 0.85 < ASY_C, \
    f"first-three {FIRST3:.3f} and asymptotic {ASY_C:.3f} do not straddle -- no diagnosis"
assert _dslope < 0.06, f"the slopes differ by {100*_dslope:.1f}% -- not a pure phase offset"
assert abs(_dphase - 0.615) < 0.08, f"the phase offset is {_dphase:.3f} pi, expected 0.615"
assert _wc > 3 * _wl, f"the CR transient {_wc:.0f} is not large against the control's {_wl:.0f}"
assert _minc > 1.05, f"the weakest peak has contrast {_minc:.2f} -- measured on noise"
assert len(P['CR']) >= 8 and len(P['LambdaCDM']) >= 8, \
    "fewer than eight peaks in an arm -- this is the depth the correction depends on"
print(f"GATE c54.190 (r2441), `L-505`: at production depth the CR arm's asymptotic spacing is "
      f"{ASY_C:.4f} of l_A against the control's {ASY_L:.4f}, while its first three gaps give "
      f"{FIRST3:.4f} — the number c54.187-189 reported; the series are parallel to "
      f"{100*_dslope:.1f}% with intercepts {_dphase:.3f} l_A apart ({_dphase:.2f} pi of acoustic "
      f"phase); and the CR transient is {_wc:.0f} in ell against the control's {_wl:.0f} — pinned "
      f"against `L-501`, `L-502`, `L-504` and P15 sec:refit-bound.")
