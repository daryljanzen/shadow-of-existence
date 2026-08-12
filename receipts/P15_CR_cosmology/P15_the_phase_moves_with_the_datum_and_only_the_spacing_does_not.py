#!/usr/bin/env python3
"""
RECEIPT -- P15: ** THE OBSERVER LINE'S ITEM 38 ANSWERED, AND THE ANSWER WITHDRAWS c54.190-191's
HEADLINE.  ACROSS FOUR SEAM PHASES AT PRODUCTION DEPTH THE ASYMPTOTIC ACOUSTIC PHASE SPANS 0.891 IN
phi/pi -- AND THE CONTROL'S 0.263 LIES INSIDE THAT SPAN.  ** SO 0.62 pi IS THE VALUE AT THE ONE
READING THE INSTRUMENT CODES, NOT A PREDICTION.  WHAT IS ROBUST ACROSS EVERY FREEDOM NOW SCANNED IS
THE SPACING, AT 0.963-0.981 OF ell_A -- AND NO READING BRINGS THE SPECTRUM NEAR THE CONTROL. **

Built r2491+c54.195, front #2, lead `L-508`.

===================================================================================================
** WHY: THE OBSERVER LINE ASKED THE ONE QUESTION THE SCANS COULD NOT ANSWER, AND IT WAS RIGHT TO. **
===================================================================================================

`FOR_54` item 38 (r2485): *"Of the 23 datum-scan spectra, ZERO reach peak 8 ... The quantity that now
carries the disagreement cannot be tested against the one freedom known to move things, because the
scan that varies that freedom was run too shallow to fit it.  The corrected claim rests on ONE pair
of spectra."*  ** And it named the experiment: two or three seam phases at production depth, fit
peaks 4-8. **  *c54.191 had supplied one further phase; this supplies two more, making four.*

  PART 1  ** THE ASYMPTOTIC INTERCEPT MOVES, AND FAR MORE THAN TWO POINTS SUGGESTED. **  At
          phi = 0, pi/4, pi/2 and pi the fitted phi/pi is 0.878, 0.958, 0.066 and 0.671 -- ** a span
          of 0.891, and the control's 0.263 lies INSIDE it. **  *c54.191 read 34% closure from the
          two endpoints; the interior is where the motion is.*
  PART 2  ** SO c54.190-191's HEADLINE IS WITHDRAWN. **  Those revisions promoted the 0.62 pi to
          *"the whole acoustic disagreement"* and *"one number and one mechanism"*.  ** It is the
          value at phi = 0, which is one reading of a phase the corpus's own datum leaves
          unspecified. **  *The attribution to the driving (c54.193) stands -- the driving is what
          separates the arms AT A GIVEN READING -- but a quantity the datum can move across the
          control's value is not a prediction of the construction.*
  PART 3  ** THE PEAK HEIGHTS MOVE TOO, AND THEY DO NOT REACH THE SKY EITHER. **  P1/P2 runs 0.483,
          0.648, 0.878 and 1.618 across the four -- against the sky's 2.217 and the control's 2.197.
          ** The best reading gets to 1.618 and no further. **
  PART 4  ** WHAT IS ROBUST ACROSS EVERY FREEDOM NOW SCANNED IS THE SPACING. **  0.963-0.981 of
          ell_A over the four phases here, 0.975 at the coded reading, and tracking r_s at 98% of
          the acoustic rate under the fitted parameter (c54.191).  ** That is the one acoustic
          quantity this construction states and does not surrender to a choice. **
  PART 5  ** AND MATCHING THE PHASE DOES NOT FIX THE SPECTRUM, WHICH IS WHAT SETTLES PART 2. **  The
          reading whose phase is closest to the control's is phi = pi/2, at 0.197 in phi/pi -- and
          its chi^2/dof is 224 against the control's 3.71 on the same 185 bins.  ** Sixty times
          worse while agreeing on the phase. **  *So the phase was never carrying the disagreement.*

** WHAT THIS LEAVES, STATED AS PLAINLY AS THE SPAN ALLOWS. **  ** The acoustic SPACING is right and
robust.  The acoustic PHASE and the peak HEIGHTS both move substantially with a datum the corpus
does not fix, and neither reaches the sky at any reading tried.  And no reading brings the spectrum
within sixty times the control. **  *Where the disagreement lives is therefore not a single named
quantity, and this file does not supply one -- which is a worse position than c54.191 reported and a
truer one.*

** F5 IS NOT SOFTENED, AND IT CUTS BOTH WAYS HERE. **  A measurement discrepancy is not a framework
verdict; `PO-7` is protected; the conversion is Daryl's.  ** And a discrepancy that turns out to rest
on a free choice is not a framework verdict either -- the withdrawal is as much a correction of this
line's overreach as the earlier ones were. **

SETTINGS: production -- LMAXL=3000 on all five spectra, fitted on peaks 4 and up.  The reduced-depth
scans of c54.187-189 are named only as the thing being tested and no quantity is taken from them.

rc=0 on success.  Run: python3 P15_the_phase_moves_with_the_datum_and_only_the_spacing_does_not.py
                        (numpy scipy; ~15 s)
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
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

RUNS = (('control',  'c54.186_lcdm_L3000.npz'),
        ('phi=0',    'c54.186_cr_L3000.npz'),
        ('phi=pi/4', 'c54.195_cr_phi0.7854_L3000.npz'),
        ('phi=pi/2', 'c54.195_cr_phi1.5708_L3000.npz'),
        ('phi=pi',   'c54.191_cr_phipi_L3000.npz'))
SKY_P1P2 = 2.217
LMAX0 = 1996.0


def read(fname):
    z = np.load(os.path.join(SP, fname))
    ls = np.asarray(z['ls'], float)
    D = np.asarray(z['Dl'], float)
    lA = float(z['l_A'])
    pk = argrelextrema(D, np.greater, order=3)[0]
    pos, h = ls[pk], D[pk]
    n = np.arange(1, len(pos) + 1)
    m = n >= 4
    b, a = np.polyfit(n[m], pos[m], 1)
    c = CS.chi2_of(ls, D, lmax=LMAX0)
    res = [float(pos[i] - (b * (i + 1) + a)) for i in range(3)]
    return dict(pos=pos, slope=float(b) / lA, phi=-float(a) / lA, npk=len(pos),
                p1p2=float(h[0] / h[1]), dof=c[0] / c[1], res=res)


R = {nm: read(f) for nm, f in RUNS}
CTRL = R['control']
CR = [nm for nm, _ in RUNS if nm != 'control']

# =====================================================================
print("=" * 78)
print("PART 1 — FOUR SEAM PHASES AT PRODUCTION DEPTH, FITTED ON PEAKS 4 AND UP")
print("=" * 78)
print("  *the indexing is checked before it is used: every CR reading shows the low-ell transient")
print("   c54.190 identified — its first peak sits ABOVE its own asymptotic line and the excess")
print("   decays — so the first feature present IS peak one in every case.*")
print()
print(f"  {'run':>10} {'npk':>4} {'first peaks':>28} {'first-3 off line':>20} {'slope/l_A':>10} "
      f"{'phi/pi':>8}")
for nm, _ in RUNS:
    d = R[nm]
    print(f"  {nm:>10} {d['npk']:>4} {str([int(x) for x in d['pos'][:4]]):>28} "
          f"{str([int(round(x)) for x in d['res']]):>20} {d['slope']:>10.4f} {d['phi']:>8.4f}")
PH = [R[nm]['phi'] for nm in CR]
SPAN = max(PH) - min(PH)
INSIDE = min(PH) < CTRL['phi'] < max(PH)
print(f"\n  ** phi/pi SPANS {min(PH):.4f} TO {max(PH):.4f} — A RANGE OF {SPAN:.4f} — AND THE CONTROL'S "
      f"{CTRL['phi']:.4f} IS {'INSIDE' if INSIDE else 'OUTSIDE'} IT. **")
_tr = min(abs(R[nm]['res'][0]) for nm in CR)
print(f"     *the smallest first-peak transient among the four is {_tr:.0f} in ell against the "
      f"control's {abs(CTRL['res'][0]):.0f} — the signature is present in all four.*")
if not INSIDE:
    fail.append("the control's phase is not inside the span the seam phase reaches -- PART 2's "
                "withdrawal has no basis and c54.190-191 stand")
if SPAN < 0.3:
    fail.append(f"the phase spans only {SPAN:.3f} -- item 38's question is answered in the negative "
                "and this file's title is wrong")
if _tr < 3 * abs(CTRL['res'][0]):
    fail.append("a CR reading shows no transient -- the peak indexing is not established by the "
                "test this file uses and PART 1 may be comparing different n")

# =====================================================================
print()
print("=" * 78)
print("PART 3/4 — THE HEIGHTS MOVE TOO; THE SPACING DOES NOT")
print("=" * 78)
print(f"  {'run':>10} {'slope/l_A':>10} {'P1/P2':>8} {'chi^2/dof':>10}")
for nm, _ in RUNS:
    d = R[nm]
    print(f"  {nm:>10} {d['slope']:>10.4f} {d['p1p2']:>8.3f} {d['dof']:>10.2f}")
print(f"  {'the sky':>10} {1.0:>10.4f} {SKY_P1P2:>8.3f} {'—':>10}")
HH = [R[nm]['p1p2'] for nm in CR]
SL = [R[nm]['slope'] for nm in CR]
print(f"\n  ** P1/P2 RUNS {min(HH):.3f} TO {max(HH):.3f} AND NEVER REACHES THE SKY'S {SKY_P1P2:.3f}. **")
print(f"  ** THE SPACING RUNS {min(SL):.4f} TO {max(SL):.4f} — {100*(max(SL)/min(SL)-1):.1f}% — ACROSS "
      f"THE SAME FOUR. **")
print("     ⇒ ***The spacing is the one acoustic quantity this construction states and does not")
print("     surrender to a choice.***")
if max(HH) > SKY_P1P2:
    fail.append(f"a reading reaches P1/P2 = {max(HH):.3f}, at or past the sky's -- PART 3 is wrong")
if max(SL) / min(SL) - 1 > 0.06:
    fail.append(f"the spacing moves {100*(max(SL)/min(SL)-1):.1f}% across the phases -- it is not the "
                "robust quantity and PART 4 must be withdrawn too")

# =====================================================================
print()
print("=" * 78)
print("PART 5 — AND MATCHING THE PHASE DOES NOT FIX THE SPECTRUM")
print("=" * 78)
best = min(CR, key=lambda nm: abs(R[nm]['phi'] - CTRL['phi']))
bfit = min(CR, key=lambda nm: R[nm]['dof'])
print(f"  the reading closest in PHASE is {best} (|d phi/pi| = "
      f"{abs(R[best]['phi']-CTRL['phi']):.4f}), and its chi^2/dof is {R[best]['dof']:.0f}")
print(f"  the BEST-FITTING reading is {bfit} at {R[bfit]['dof']:.0f}, against the control's "
      f"{CTRL['dof']:.2f} on the same {CS.chi2_of(np.asarray(np.load(os.path.join(SP,RUNS[0][1]))['ls'],float), np.asarray(np.load(os.path.join(SP,RUNS[0][1]))['Dl'],float), lmax=LMAX0)[1]} bins")
print(f"\n  ** {R[bfit]['dof']/CTRL['dof']:.0f} TIMES THE CONTROL AT THE BEST READING, AND "
      f"{R[best]['dof']/CTRL['dof']:.0f} TIMES IT WHILE AGREEING ON THE PHASE. **")
print("     ⇒ ***So the phase was never carrying the disagreement, and c54.190-191's promotion of")
print("     it to \"one number and one mechanism\" is withdrawn.***")
print()
print("  ⛔ ***F5 UNSOFTENED, AND IT CUTS BOTH WAYS: a discrepancy that turns out to rest on a free")
print("     choice is not a framework verdict either. `PO-7` protected; the conversion is Daryl's.***")
if R[best]['dof'] < 10 * CTRL['dof']:
    fail.append(f"the phase-matched reading is only {R[best]['dof']/CTRL['dof']:.0f}x the control -- "
                "matching the phase DOES largely fix the spectrum and PART 5 is wrong")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — across four seam phases at production depth the asymptotic acoustic phase")
print("spans 0.891 in phi/pi with the control's 0.263 inside that span, so the 0.62 pi is the value")
print("at one reading and not a prediction; the peak heights move over 0.48-1.62 and never reach the")
print("sky's 2.22; the spacing holds at 0.963-0.981 of l_A; and the phase-matched reading is still")
print("sixty times the control, so the phase was never carrying the disagreement.")
print("=" * 78)

# ============================================================================================
# GATE — r2491+c54.195, `L-508`.  This file WITHDRAWS its own line's headline for the third time
# in the span, so the pins are on the withdrawal being forced by the data and not chosen.
#   (1) the control's phase INSIDE the span the seam phase reaches -- without this there is no
#       withdrawal and c54.190-191 stand as written;
#   (2) the span itself, which is item 38's question;
#   (3) THE TRANSIENT PRESENT IN ALL FOUR, which is what establishes the peak indexing -- if a
#       reading showed none, PART 1 might be comparing different n and the span would be an
#       artefact of labelling;
#   (4) the spacing's stability, which is the one thing this file does NOT withdraw;
#   (5) the heights never reaching the sky's, and the phase-matched reading still far from the
#       control -- PART 5 is what makes the withdrawal a finding rather than a shrug.
# ============================================================================================
assert INSIDE, "the control's phase is not inside the seam phase's span -- no withdrawal is forced"
assert SPAN > 0.3, f"the phase spans only {SPAN:.3f}"
assert abs(SPAN - 0.891) < 0.05, f"the span is {SPAN:.4f}, expected 0.891"
assert _tr > 3 * abs(CTRL['res'][0]), "a CR reading shows no transient -- the indexing is unproven"
assert max(SL) / min(SL) - 1 < 0.06, f"the spacing moves {100*(max(SL)/min(SL)-1):.1f}%"
assert max(HH) < SKY_P1P2, f"a reading reaches P1/P2 = {max(HH):.3f}"
assert R[best]['dof'] > 10 * CTRL['dof'], \
    f"the phase-matched reading is {R[best]['dof']/CTRL['dof']:.0f}x the control"
assert min(R[nm]['npk'] for nm, _ in RUNS) >= 7, "an arm carries fewer than seven peaks"
print(f"GATE c54.195 (r2491), `L-508`: four seam phases at production depth span phi/pi = "
      f"{min(PH):.4f}-{max(PH):.4f} ({SPAN:.3f}) with the control's {CTRL['phi']:.4f} inside; the "
      f"heights span {min(HH):.3f}-{max(HH):.3f} against the sky's {SKY_P1P2}; the spacing holds "
      f"{min(SL):.4f}-{max(SL):.4f}; and the phase-matched reading is {R[best]['dof']/CTRL['dof']:.0f}x "
      f"the control — pinned against `FOR_54` item 38, `L-505`, `L-506`, `L-507` and `L-147` F5.")
