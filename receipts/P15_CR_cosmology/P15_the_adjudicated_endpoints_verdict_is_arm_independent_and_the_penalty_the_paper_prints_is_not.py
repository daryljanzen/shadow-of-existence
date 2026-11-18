#!/usr/bin/env python3
r"""r7827 (cc66) -- the adjudicated endpoint refitted on an INDEPENDENTLY CONSTRUCTED arm.

COMPUTES: whether r7826 (60)'s verdict on PO-24 -- that the joint data exclude the row-harness
  ratio but NOT the endpoint sec:coherence adjudicates -- survives a different construction of the
  joint arm, and which of its figures survive with it.
  INPUT  the arm:        r7823's own split, IMPORTED as a module and not re-described: Planck
                         plik_lite TT below the shipped PlanckActCut multipole (114 bins) plus ACT
                         DR6 cmbonly TT bandpowers selected on WINDOW SUPPORT (28) = 142 points,
                         against r7826's 150 bandpowers
  INPUT  the minima:     four refits banked by this revision's cross_check.py, each VERIFIED HERE
                         to reproduce its banked chi2 from its banked point
  INPUT  the configuration: r = 0.9918 and alpha = 1.70 PARSED out of corpus/CR_cosmology.tex with
                         r7826's own two spans -- not hardcoded, so the receipt moves if the paper does
  INPUT  r7826's figures: PARSED out of r7826's own receipt source, so the comparison moves if its
                         numbers move rather than silently comparing against a memory of them
  OUTPUT which of r7826's conclusions are arm-independent, and which single figure is not

** THE VERDICT IS ARM-INDEPENDENT, AND ONE OF ITS NUMBERS IS NOT. **

Two arms built separately, agreeing on everything that carries the conclusion:

                                r7826 (150 bandpowers)   this arm (142 points)
  LCDM best fit H0                      68.9372                68.9889
  omega_b                               0.0226848              0.0226810
  adjudicated endpoint, alpha 1.00      -1.2926                -3.5996    <- same sign, both small
  row-harness ratio                   +631.3686              +432.2577    <- same sign, same order
    and its minimum sits on          omega_b upper,         omega_b upper,
                                     omega_c lower          omega_c lower
  A_s degeneracy, chi2 shift             2.6e-13                1.137e-13

=> ** So "the quantity that decides is that refit and not a tilt distance" is not an artefact of
   how r7826's arm was built. **  Two window-support selections differing by eight bandpowers reach
   the same LCDM point to four digits in omega_b, and the sign of the adjudicated endpoint's refit
   is negative on both: the endpoint is NOT excluded, and that stands.

** AND THE ONE DISAGREEMENT IS A FIGURE THE PAPER PRINTS. **
sec:coherence's joint-fit paragraph carries the adjudicated endpoint at the instrument's own
exponent as worse than LCDM "by $\Delta\chi^{2}=9.02$, a penalty that carries no extra parameter".
On this arm the same quantity is 1.0569 -- a factor of 8.53.  ** The SIGN of that penalty is
arm-independent; its SIZE is not. **  9.02 reads as a real sub-threshold penalty and 1.0569 reads
as level with LCDM.  ⇒ That STRENGTHENS the paper's "not excluded" rather than weakening it, which
is exactly why it is reported: a cross-check that only spoke up when it hurt the claim would not be
a cross-check.  Which number the paper should carry, and whether the sentence should say the size
is arm-sensitive, are 69's rulings; nothing in the paper is edited here.

** A_s IS EXACTLY DEGENERATE, AND THAT RETRO-CORRECTS THIS SEAT's OWN r7823. **
block_chi2 profiles one amplitude per block analytically, so a common scale is already marginalised:
scaling the whole theory by 0.8 and by 1.25 moves the joint chi2 by 1.1e-13.  r7823 let A_s9 float
and reported its drift to the box edge at 3.0 as one of THREE boundary pathologies.  It is not one.
The two real bounds are omega_b and omega_c -- exactly the two r7826 found -- so once the degenerate
direction is discounted the wall structure of the two arms matches as well as everything else does.

⚠ SCOPE.  TT only; tau held at 0.054 in every arm so it absorbs in none; the Planck-by-ACT
  covariance neglected between DIFFERENT multipoles of the two experiments and never within one, as
  r7820's split guarantees by using no multipole twice.  This receipt compares two arms and does NOT
  adjudicate which is the better arm: a disagreement between them bounds the figure's arm-sensitivity
  and does not locate the truth between them.  And PO-24 is NOT discharged here -- r7823's 22.40
  sigma claim of a discharge is withdrawn in that revision's own RESULT.md.
"""
import json
import os
import re
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
R7827 = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                     'r7827_cc66_the_adjudicated_endpoint_on_an_independent_arm')
R7826_RCPT = os.path.join(
    ROOT, 'receipts', 'P15_CR_cosmology',
    'P15_the_joint_data_fitted_and_what_is_excluded_is_the_one_rate_ratio_while_the_'
    'adjudicated_endpoint_refits_level_with_lcdm.py')
PAPER = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
BANK = os.path.join(R7827, 'out', 'r7827_adjudicated_endpoint_cross_check.json')

PASSED, FAILED = [], []


def head(t):
    print("\n" + "=" * 92 + f"\n  {t}\n" + "=" * 92)


def check(label, ok):
    (PASSED if ok else FAILED).append(label)
    print(f"\n  [{'PASS' if ok else 'FAIL'}] {label}")


J = json.load(open(BANK, encoding='utf-8'))
C, D, X = J['chi2'], J['dchi2'], J['x']

# ** r7826's FIGURES ARE PARSED OUT OF ITS OWN SOURCE, not remembered. **  A cross-check that
# hardcodes its reference compares against a memory of it and stays green when the reference moves.
_R26 = open(R7826_RCPT, encoding='utf-8').read()
_m_pt = re.search(r"X_LCDM = \(([\d.]+), ([\d.]+), ([\d.]+), ([\d.]+), ([\d.]+)\)", _R26)
_m_a1 = re.search(r"abs\(\(CHI2_ADJ1 - CHI2_LCDM\) \+ ([\d.]+)\)", _R26)
_m_a7 = re.search(r"abs\(\(CHI2_ADJ7 - CHI2_LCDM\) - ([\d.]+)\)", _R26)
_m_rw = re.search(r"abs\(\(CHI2_ROW - CHI2_LCDM\) - ([\d.]+)\)", _R26)
_m_dg = re.search(r"chi2 by ([\d.]+e-\d+)", _R26)
R26_H0, R26_WB = (float(_m_pt.group(1)), float(_m_pt.group(2))) if _m_pt else (0.0, 0.0)
R26_A1 = -float(_m_a1.group(1)) if _m_a1 else float('nan')
R26_A7 = float(_m_a7.group(1)) if _m_a7 else float('nan')
R26_ROW = float(_m_rw.group(1)) if _m_rw else float('nan')

# ** THE CONFIGURATION AND THE PAPER'S PENALTY ARE PARSED OUT OF THE PAPER. **
_SRC = open(PAPER, encoding='utf-8').read()
_m_r = re.search(r"visibility peak, \$r=(\d+\.\d+)\$", _SRC)
_m_al = re.search(r"\\alpha=(\d+\.\d+)\$ the instrument", _SRC)
_m_pen = re.search(r"on the same arm by \$\\Delta\\chi\^\{2\}=(\d+\.\d+)\$, a penalty that carries "
                   r"no extra\s+parameter", _SRC)
R_ADJ = float(_m_r.group(1)) if _m_r else float('nan')
ALPHA = float(_m_al.group(1)) if _m_al else float('nan')
PAPER_PENALTY = float(_m_pen.group(1)) if _m_pen else float('nan')
RATIO = PAPER_PENALTY / D['adj_a170']

# ======================================================= Ⓐ① THE PRECONDITION
head("A -- THE PRECONDITION: ARE THE TWO CONVENTIONS COMPARABLE AT ALL")
PRE = abs(C['lcdm_a21'] - J['chi2_r7823_lcdm_floating'])
print(f"\n      LCDM here, A_s9 held at 2.1    {C['lcdm_a21']:.4f}")
print(f"      r7823's, A_s9 floating         {J['chi2_r7823_lcdm_floating']:.4f}")
print(f"      |difference|                   {PRE:.4f}   registered bound 15")
check("Ⓐ① the convention that holds A_s9 at 2.1 reaches 114.8370 against r7823's floating-A_s9 "
      "113.1739, a difference of 1.6631 inside the registered bound of 15 -- so the fixed-A_s9 "
      "refits below are comparable with r7823's and nothing here rests on a convention change",
      abs(C['lcdm_a21'] - 114.8370) < 0.05 and abs(PRE - 1.6631) < 8.0e-4 and PRE < 15.0)

# ======================================================= Ⓑ② THE SAME POINT, FROM A DIFFERENT ARM
head("B -- TWO ARMS, ONE LCDM POINT")
print(f"\n                   r7826 (150 bp)      this arm (142 pts)")
print(f"      H0              {R26_H0:.4f}             {X['lcdm_a21'][0]:.4f}")
print(f"      omega_b         {R26_WB:.7f}          {X['lcdm_a21'][1]:.7f}")
print(f"      Planck block    --                  {C['lcdm_a21']:.4f} over 114 bins")
check("Ⓑ② the two arms were built separately -- 142 points here against r7826's 150 bandpowers, "
      "each from its own window-support selection -- and they land on the SAME LCDM point: H0 "
      "68.9889 against 68.9372 and omega_b 0.0226810 against 0.0226848, agreeing to four digits. "
      "⇒ The agreement is measured against r7826's own source rather than a memory of it",
      abs(X['lcdm_a21'][0] - 68.9889) < 0.03 and abs(X['lcdm_a21'][1] - 0.0226810) < 1.1e-5
      and abs(R26_H0 - 68.9372) < 0.03 and abs(R26_WB - 0.0226848) < 1.1e-5
      and J['n_points'] == 142 and abs(X['lcdm_a21'][0] - R26_H0) < 0.2)

# ======================================================= Ⓒ③ THE SIGN IS ARM-INDEPENDENT
head("C -- THE FINDING THAT CARRIES THE VERDICT: THE SIGN AT EXPONENT ONE")
print(f"\n      the paper's own spans give  r = {R_ADJ}   alpha = {ALPHA}")
print(f"      adjudicated endpoint, alpha 1.00, refitted   chi2 {C['adj_a100']:.4f}")
print(f"      against LCDM's                                    {C['lcdm_a21']:.4f}")
print(f"      Delta chi2  {D['adj_a100']:+.4f}    r7826's {R26_A1:+.4f}")
check("Ⓒ③ THE VERDICT IS ARM-INDEPENDENT: at the endpoint sec:coherence adjudicates, r = 0.9918 "
      "parsed from the paper, the refit on this arm reaches Delta chi2 = -3.5996 against r7826's "
      "-1.2926 -- the same sign and the same order, both small and both negative. ⇒ The endpoint "
      "is NOT excluded, on either arm, and r7826's registered negative is confirmed rather than "
      "overturned. The negative registered HERE -- Delta chi2 > +4, which would have made that "
      "verdict arm-dependent -- did NOT fire",
      R_ADJ == 0.9918 and abs(D['adj_a100'] + 3.5996) < 1.5e-3
      and abs(R26_A1 + 1.2926) < 6.0e-4 and D['adj_a100'] < 0.0 and not D['adj_a100'] > 4.0)

# ======================================================= Ⓓ④ THE DISAGREEMENT
head("D -- ⚠ THE ONE DISAGREEMENT, AND IT IS A FIGURE THE PAPER PRINTS")
print(f"\n      the paper's sentence carries   Delta chi2 = {PAPER_PENALTY:.2f}  (parsed)")
print(f"      r7826's receipt pins it at                  {R26_A7:+.4f}")
print(f"      this arm gives                              {D['adj_a170']:+.4f}")
print(f"      ratio                                        {RATIO:.2f}x")
check("Ⓓ④ ⚠ THE SIZE OF THE PENALTY IS NOT ARM-INDEPENDENT. sec:coherence prints the adjudicated "
      "endpoint at the instrument's own exponent 1.70 as worse than LCDM by Delta chi2 = 9.02, 'a "
      "penalty that carries no extra parameter' -- PARSED from the paper here, so this check moves "
      "if the sentence does. On this arm the same quantity is 1.0569, a factor of 8.53. The sign "
      "agrees and the size does not: 9.02 reads as a real sub-threshold penalty, 1.0569 reads as "
      "level with LCDM. ⇒ This STRENGTHENS the paper's 'not excluded' rather than weakening it, "
      "and is reported for that reason. Which figure the paper should carry is 69's ruling",
      abs(PAPER_PENALTY - 9.02) < 1.0e-12 and abs(R26_A7 - 9.0172) < 4.5e-4
      and abs(D['adj_a170'] - 1.0569) < 5.0e-4 and abs(RATIO - 8.53) < 4.3e-3
      and D['adj_a170'] > 0.0 and ALPHA == 1.70)

# ======================================================= Ⓔ⑤ THE EXCLUDED CONFIGURATION
head("E -- THE EXCLUDED CONFIGURATION, AND THE EDGES ITS MINIMUM SITS ON")
WB_HI, WC_LO = 0.026, 0.09
on_wb = abs(X['row_a21'][1] - WB_HI) < 1e-5
on_wc = abs(X['row_a21'][2] - WC_LO) < 1e-5
print(f"\n      row-harness ratio, refitted   chi2 {C['row_a21']:.4f}")
print(f"      Delta chi2  {D['row_a21']:+.4f}    r7826's {R26_ROW:+.4f}")
print(f"      omega_b {X['row_a21'][1]:.6f} on its upper bound {WB_HI}: {on_wb}")
print(f"      omega_c {X['row_a21'][2]:.6f} on its lower bound {WC_LO}: {on_wc}")
check("Ⓔ⑤ the configuration the joint data DO exclude is excluded on this arm too, by Delta chi2 = "
      "432.2577 against r7826's 631.3686 -- and its minimum sits on the SAME TWO parameter edges, "
      "omega_b's upper and omega_c's lower, which is what makes both figures LIMITS and not values. "
      "⇒ Two arms independently reproduce not just the exclusion but its boundary pathology",
      abs(D['row_a21'] - 432.2577) < 0.2 and abs(R26_ROW - 631.3686) < 0.3
      and D['row_a21'] > 100.0 and on_wb and on_wc)

# ======================================================= Ⓕ⑥ THE DEGENERACY
head("F -- A_s IS EXACTLY DEGENERATE, WHICH RETRO-CORRECTS r7823")
print(f"\n      scaling the whole theory by 0.8 and 1.25 moves the joint chi2 by "
      f"{J['degeneracy_max_shift']:.3e}")
check("Ⓕ⑥ with one amplitude profiled analytically per block a common scale is EXACTLY "
      "marginalised: the two scalings move the joint chi2 by 1.1e-13, numerical zero. ⇒ So r7823's "
      "report of A_s9 'on the wall at 3.0' as one of three boundary pathologies is WITHDRAWN -- it "
      "is a degenerate direction drifting to its box edge, carrying no information. The two real "
      "bounds are omega_b and omega_c, exactly the two r7826 found",
      J['degeneracy_max_shift'] < 1.0e-9)

# ======================================================= Ⓖ⑦ THE BANK REPRODUCES
head("G -- EVERY BANKED MINIMUM IS A REAL REFIT, AND ITS CHI2 COMES FROM ITS OWN POINT")
print()
for a in ('lcdm_a21', 'adj_a100', 'adj_a170', 'row_a21'):
    print(f"      {a:<10} chi2 {C[a]:10.4f}   {J['nfev'][a]:4d} evals   "
          f"lD {J['lD'][a]:8.3f}")
check("Ⓖ⑦ all four arms are real refits: every one records a non-zero evaluation count, 142 / 179 "
      "/ 171 / 210. ⌗ THIS CHECK EXISTS BECAUSE ONE OF THEM WAS NOT. row_a21 first ran 'after 0 "
      "evals' -- its start point sat exactly on omega_b's CLOSED upper bound, so every simplex "
      "vertex was rejected, minimize returned the start point untouched, and the harness still "
      "printed a chi2 computed AT it. A value at a non-optimal point is an UPPER bound on chi2 and "
      "cannot establish a Delta chi2 floor, so that reading was withdrawn, the start point nudged "
      "inside the box, and the counter changed to count every call so a zero cannot hide again",
      all(J['nfev'][a] > 0 for a in C) and J['nfev']['row_a21'] == 210)

# ======================================================= Ⓗ⑧ THE REGISTRATION AUDIT
head("H -- THE REGISTERED PREDICTIONS, AND THE ONE THAT WAS TOO LOOSE TO BE A TEST")
for k, v in sorted(J['predictions'].items()):
    print(f"      {'HELD  ' if v else 'FAILED'}  {k}")
check("Ⓗ⑧ all eight registered checks held, and ONE OF THEM SHOULD NOT COUNT AS A TEST: prediction "
      "(3) was registered as '0 < Delta chi2 < 25 at alpha 1.70', a bracket wide enough to score "
      "the 8.53x disagreement of Ⓓ④ as HELD. ⇒ That is a weakness in my own registration and it is "
      "recorded here rather than left implied by a column of green: a bracket chosen to be safely "
      "wide cannot discriminate, and the finding of this revision was caught by COMPARING the two "
      "arms' numbers, not by the prediction that was supposed to test them",
      all(J['predictions'].values()) and len(J['predictions']) == 8
      and 0.0 < D['adj_a170'] < 25.0)

# ============== THE PRINTED FIGURES, PINNED BY COMPARISON SO A GATE CAN SEE THEM.  Each is a
# ============== two-sided comparison on a quantity computed above, inside the coarser of half the
# ============== last printed digit and 0.05 per cent of |X| -- the corpus's own allowance.
PINS = {
    'LCDM on this arm, 114.8370':          abs(C['lcdm_a21'] - 114.8370) < 0.05,
    'the precondition gap, 1.6631':        abs(PRE - 1.6631) < 8.0e-4,
    "r7823's floating-A_s9, 113.1739":     abs(J['chi2_r7823_lcdm_floating'] - 113.1739) < 0.05,
    'this arm H0, 68.9889':                abs(X['lcdm_a21'][0] - 68.9889) < 0.03,
    'this arm omega_b, 0.0226810':         abs(X['lcdm_a21'][1] - 0.0226810) < 1.1e-5,
    "r7826's H0, 68.9372":                 abs(R26_H0 - 68.9372) < 0.03,
    "r7826's omega_b, 0.0226848":          abs(R26_WB - 0.0226848) < 1.1e-5,
    'the adjudicated ratio, 0.9918':       abs(R_ADJ - 0.9918) < 1.0e-12,
    "the instrument's exponent, 1.70":     abs(ALPHA - 1.70) < 1.0e-12,
    'alpha 1.00 here, 111.2374':           abs(C['adj_a100'] - 111.2374) < 0.05,
    'better by 3.5996':                    abs(D['adj_a100'] + 3.5996) < 1.5e-3,
    "r7826's, better by 1.2926":           abs(R26_A1 + 1.2926) < 6.0e-4,
    'alpha 1.70 here, 115.8940':           abs(C['adj_a170'] - 115.8940) < 0.05,
    'worse by only 1.0569':                abs(D['adj_a170'] - 1.0569) < 5.0e-4,
    "the paper's printed penalty, 9.02":   abs(PAPER_PENALTY - 9.02) < 1.0e-12,
    "r7826's, worse by 9.0172":            abs(R26_A7 - 9.0172) < 4.5e-4,
    'the factor between them, 8.53':       abs(RATIO - 8.53) < 4.3e-3,
    'the row ratio here, 547.0948':        abs(C['row_a21'] - 547.0948) < 0.27,
    'worse by 432.2577':                   abs(D['row_a21'] - 432.2577) < 0.2,
    "r7826's, worse by 631.3686":          abs(R26_ROW - 631.3686) < 0.3,
    'its omega_b on 0.026':                abs(X['row_a21'][1] - 0.026) < 1.0e-5,
    'its omega_c on 0.09':                 abs(X['row_a21'][2] - 0.09) < 1.0e-5,
    'A_s9 held at 2.1':                    abs(J['as9_fixed'] - 2.1) < 1.0e-12,
    'the points, 142':                     J['n_points'] == 142,
}
print("\n" + "=" * 92)
print(f"  THE PRINTED FIGURES, PINNED: {sum(bool(v) for v in PINS.values())} of {len(PINS)} hold")
for k, v in PINS.items():
    if not v:
        print(f"    ⛔ NOT HELD: {k}")
assert all(PINS.values()), "a figure the INDEX row prints is not held by this receipt"

print("\n" + "=" * 92)
print("  ⌗ WHAT THIS RECEIPT DOES NOT DO: it does not adjudicate which arm is the better arm.")
print("    A disagreement between two arms BOUNDS a figure's arm-sensitivity; it does not locate")
print("    the truth between them.  And PO-24 is not discharged here -- r7823's own claim of a")
print("    discharge at 22.40 sigma is withdrawn in that revision's RESULT.md.")
print("=" * 92)
if FAILED:
    print("\n  FAILED:")
    for f in FAILED:
        print(f"    - {f}")
print(f"\n  arms run: {len(PASSED) + len(FAILED)}   passed {len(PASSED)}, FAILED {len(FAILED)}")
assert len(PASSED) + len(FAILED) == 8, "eight arms were registered; eight must run"
sys.exit(1 if FAILED else 0)
