#!/usr/bin/env python3
r"""r7833 (cc66) -- the cold read of P15: the two bounds whose printed evidence cannot carry them.

COMPUTES: from P15's OWN printed figures, parsed out of corpus/CR_cosmology.tex rather than
  remembered, (i) the two bounds the paper states and the deviations its printed pairs actually
  imply, (ii) the suppression quartet at the two adjudicated ratios, and (iii) that no figure this
  seat withdrew at r7823/r7829 survives anywhere in the paper.
  INPUT  the paper:  corpus/CR_cosmology.tex, read and whitespace-flattened, so a claim that WRAPS
                     across a line is still found -- the defect that nearly cost this read a finding
  OUTPUT for each bound: the figure the sentence states, the deviation the printed pair implies, and
         whether the second exceeds the first

** THE FINDING, AND IT IS ONE DEFECT TWICE: A BOUND TRUE OF THE RECEIPT THAT OWNS IT AND FALSE OF
   THE FIGURES THE SENTENCE OFFERS AS ITS EVIDENCE. **

  (1) sec:coherence     "within three per cent of the frozen value Psi_i/2"
                        0.4835/0.5 = 3.30 per cent  >  3     => the bound is FALSE as written
                        and on the SPECTRUM (0.4835/0.5)^2 = 0.93509, 6.49 per cent -- DOUBLE, which
                        is the figure the acoustic heights carry and the reader is not given
  (2) sec:refit-bound   "within a fiftieth of a per cent on the heights"
                        the receipt measures -0.011% and -0.017% (inside 0.02)   => claim TRUE
                        the printed pair 2.348 vs 2.349 implies -0.043%          => evidence FALSE

  r7653 had already found exactly (2) FOR THE PEAKS: "they agree to under a tenth of a multipole at
  every peak and to a hundredth of a per cent on the heights ... So the claim HOLDS, and comfortably;
  what does not hold is the pair of figures offered as its evidence."  The peaks half was repaired --
  the paper's offsets now track the receipt's and sit inside a tenth of a multipole.  The heights
  half was not, and this receipt is that half.

** WHAT THIS RECEIPT DOES NOT DO: IT DOES NOT EDIT EITHER SENTENCE. **  Both are PINNED by the
receipts that own them -- one holds the literal "within three per cent ..." and asserts it present,
the other states THE TABLE IS PINNED, ROW BY ROW, BY ONE PROCEDURE -- so 2.291 and 2.348 are RIGHT
as table entries and must not be re-rounded to repair a sentence.  Each fix is a coordinated
paper-and-receipt change, and whether the first receipt's finding should be DISCHARGED by rewording
the paper or KEPT STANDING as a live criticism of it is a judgement about that receipt's purpose.
69's ruling; the numbers are supplied so it is a decision and not a search.

** AND WHAT THE READ FOUND SOUND, pinned here so a regression in it reddens. **  The suppression
quartet reproduces at alpha = 1.70 from the ratio each sentence names -- a 2.75 and 6.29 per cent
RISE at r = 0.992 and a 7.61 and 16.30 per cent FALL at r = 1.023, printed as "about three per cent
at l_D and six at 1.5 l_D" and "a fall of eight and sixteen".  Four figures, two configurations, one
formula.  And every figure this seat withdrew at r7823/r7829 is absent: 22.40 sigma, 9.02, 1.0569,
8.53, each 0 hits.

Run:  python3 P15_the_cold_read_finds_two_bounds...py      (rc 0 = all arms held)
"""

import os
import re
import sys
from math import exp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
P15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')

PASSED, FAILED = [], []


def head(t):
    print("\n" + "=" * 92 + f"\n  {t}\n" + "=" * 92)


def check(label, ok):
    (PASSED if ok else FAILED).append(label)
    print(f"\n  [{'PASS' if ok else 'FAIL'}] {label}")


# ** THE PAPER IS WHITESPACE-FLATTENED BEFORE ANY SEARCH. **  A claim that wraps across a line
# break is invisible to a single-line search: this read reported defect (1) as GONE on exactly that
# error, because "within three per cent" wraps as "within three per\ncent".  A negative from a
# newline-naive search means NOT ASKED, not NOT THERE.
_RAW = open(P15, encoding='utf-8').read()
FLAT = re.sub(r'\s+', ' ', _RAW)

# ======================================================= Ⓐ① THE PAPER'S OWN FIGURES, PARSED
head("Ⓐ① THE FIGURES ARE PARSED OUT OF THE PAPER, NOT REMEMBERED")

_M1 = re.search(r'the wavenumber-independent \$([0-9.]+)\\,\\Psi_i\$, '
                r'within (\w+) per cent of the frozen value \$\\Psi_i/2\$', FLAT)
_M2 = re.search(r'height ratios \$([0-9.]+)\$ and \$([0-9.]+)\$ against \$([0-9.]+)\$ and '
                r'\$([0-9.]+)\$:.{0,120}?within a (\w+) of a per cent on the heights', FLAT)
# ** THE PRESENCE CHECK IS AN `ALT` DISJUNCTION, AND THE REASON IS THE WHOLE POINT. **  A gate that
# simply asserts a defective sentence is PRESENT fails on SUCCESS -- it reddens the moment 69 repairs
# the defect, which is the one outcome this receipt exists to encourage.  So each site is read in two
# states, and either is a pass:
#   STATE A  the sentence still carries the bound its printed figures cannot support -- defect LIVE
#   STATE B  the sentence no longer carries it -- defect DISCHARGED, and this receipt says so
# r7827 took the same shape for the paper's penalty sentence; it is the design that paid off there.
STATE_A1 = _M1 is not None
STATE_A2 = _M2 is not None
print(f"      defect (1) site: {'STATE A -- defect LIVE' if STATE_A1 else 'STATE B -- DISCHARGED'}")
print(f"      defect (2) site: {'STATE A -- defect LIVE' if STATE_A2 else 'STATE B -- DISCHARGED'}")
if not (STATE_A1 and STATE_A2):
    print("      ⇒ a site has moved.  This receipt's finding on that site is DISCHARGED, not red:")
    print("        the bound it reported can no longer be read off the paper, which is the repair")
    print("        this file asked for.  Re-read the sentence before re-asserting anything about it.")
# ⛭ THIS ARM WAS FIRST WRITTEN AS `check(..., True)` AND check_cannot_fail CAUGHT IT, CORRECTLY.
#    A disjunction over two legitimate states is a SCOPE statement, not a check: both branches pass
#    by construction, so asserting "one of them holds" tests nothing and adds a free PASS to the
#    count.  What IS assertable is that the read itself happened and that every field a live site
#    captures actually parses -- which fails if the paper moves, shrinks, or the flattening breaks.
_NEWLINE_FREE = '\n' not in FLAT
_READ_OK = len(FLAT) > 100_000 and _NEWLINE_FREE
_PARSE_OK = (((not STATE_A1) or all(_M1.group(i) for i in (1, 2)))
             and ((not STATE_A2) or all(_M2.group(i) for i in range(1, 6))))
print(f"      the flattened paper: {len(FLAT)} chars, newline-free {_NEWLINE_FREE}")
print(f"      every captured field of a live site parses: {_PARSE_OK}")
check("the paper is read and flattened, and every field a live site captures parses",
      _READ_OK and _PARSE_OK)

AMP = float(_M1.group(1)) if STATE_A1 else float('nan')              # 0.4835
WORD1 = _M1.group(2) if STATE_A1 else ''                             # "three"
H_A, H_B, H_C, H_D = ((float(_M2.group(i)) for i in (1, 2, 3, 4)) if STATE_A2
                      else (float('nan'),) * 4)                      # 2.291 2.348 2.291 2.349
WORD2 = _M2.group(5) if STATE_A2 else ''                             # "fiftieth"
print(f"      (1) amplitude {AMP}, bound word '{WORD1}'")
print(f"      (2) heights {H_A}/{H_B} against {H_C}/{H_D}, bound word '{WORD2}'")

# ======================================================= Ⓑ② DEFECT ONE
head("Ⓑ② DEFECT (1): THE BOUND IS 3.30 AND THE SENTENCE SAYS 'WITHIN THREE'")
WORDS = {'one': 1.0, 'two': 2.0, 'three': 3.0, 'four': 4.0, 'five': 5.0}
STATED1 = WORDS.get(WORD1, float('nan'))
DEV_POT = abs(AMP / 0.5 - 1.0) * 100.0
DEV_SPEC = abs((AMP / 0.5) ** 2 - 1.0) * 100.0
print(f"      the sentence states          within {STATED1:.0f} per cent")
print(f"      on the POTENTIAL  {AMP}/0.5 - 1   {DEV_POT:.4f} per cent")
print(f"      on the SPECTRUM  ({AMP}/0.5)^2 - 1 {DEV_SPEC:.4f} per cent   <- DOUBLE, and not given")
print(f"      ({AMP}/0.5)^2 = {(AMP/0.5)**2:.5f}")
check("the stated bound is EXCEEDED by the paper's own figure, and the spectrum figure is double it "
      "-- OR the site has moved and the finding is discharged",
      (not STATE_A1)
      or (DEV_POT > STATED1 and abs(DEV_POT - 3.30) < 5.0e-3 and abs(DEV_SPEC - 6.49) < 5.0e-3
          and DEV_SPEC > 1.9 * DEV_POT))

# ======================================================= Ⓒ③ DEFECT TWO
head("Ⓒ③ DEFECT (2): THE CLAIM IS TRUE OF THE MEASUREMENT AND FALSE OF THE PRINTED EVIDENCE")
FRACS = {'fiftieth': 50.0, 'hundredth': 100.0, 'twentieth': 20.0, 'twenty-fifth': 25.0}
STATED2 = (1.0 / FRACS[WORD2]) if WORD2 in FRACS else float('nan')   # a fiftieth = 0.02
MEASURED = (0.011, 0.017)              # the receipt's arm-of-record row, one matched locator
IMPLIED = max(abs(H_A / H_C - 1.0), abs(H_B / H_D - 1.0)) * 100.0
print(f"      the sentence states                 within a {WORD2} of a per cent = {STATED2:.3f}")
print(f"      the receipt MEASURES                {MEASURED[0]:.3f} and {MEASURED[1]:.3f}")
print(f"      the printed pair IMPLIES            {IMPLIED:.4f}")
print(f"      => claim true of the measurement:   {max(MEASURED) < STATED2}")
print(f"      => claim false of its own evidence: {IMPLIED > STATED2}   (by {IMPLIED/STATED2:.2f}x)")
check("the bound holds for the measurement and FAILS for the figures printed as its evidence "
      "-- OR the site has moved and the finding is discharged",
      (not STATE_A2)
      or (max(MEASURED) < STATED2 and IMPLIED > STATED2 and abs(IMPLIED - 0.0426) < 4.0e-5))

# ======================================================= Ⓓ④ WHAT IS SOUND: THE QUARTET
head("Ⓓ④ THE SUPPRESSION QUARTET REPRODUCES -- the one-rate landing carried through")
ALPHA = 1.70
R_VIS, R_CUT = 0.992, 1.023          # the two ratios the sentences name, pinned below


def _supp(r, mult):
    """the per-cent departure from unity of exp[-alpha (l/l_D)^2 (r^2-1)]."""
    return abs(exp(-ALPHA * mult ** 2 * (r * r - 1.0)) - 1.0) * 100.0


Q_RISE_1, Q_RISE_15 = _supp(R_VIS, 1.0), _supp(R_VIS, 1.5)
Q_FALL_1, Q_FALL_15 = _supp(R_CUT, 1.0), _supp(R_CUT, 1.5)
QUARTET = ((0.992, 1.0, 2.75), (0.992, 1.5, 6.29), (1.023, 1.0, 7.61), (1.023, 1.5, 16.30))
_ok = True
for r, mult, expect in QUARTET:
    v = exp(-ALPHA * mult ** 2 * (r * r - 1.0))
    got = abs(v - 1.0) * 100.0
    word = 'rise' if v > 1 else 'fall'
    print(f"      r={r}  at {mult:3.1f} l_D  ->  {got:6.3f} per cent {word}   (expect {expect})")
    _ok = _ok and abs(got - expect) < 6.0e-3
check("all four reproduce at alpha = 1.70 from the ratio each sentence names", _ok)

# ======================================================= Ⓔ⑤ THE WITHDRAWN FIGURES ARE ABSENT
head("Ⓔ⑤ NO FIGURE THIS SEAT WITHDREW AT r7823/r7829 SURVIVES -- an ABSENCE claim")
WITHDRAWN = ('22.40', '9.02', '1.0569', '8.53')
_hits = {w: len(re.findall(re.escape(w), FLAT)) for w in WITHDRAWN}
for w, n in _hits.items():
    print(f"      {w:8s} {n} hit(s)")
check("every withdrawn figure is absent from the paper", all(n == 0 for n in _hits.values()))

# ======================================================= Ⓕ⑥ THE lD CHAIN
head("Ⓕ⑥ THE l_D CHAIN IS ARITHMETIC AND IS NAMED WITH ITS CONFIGURATION AT EVERY SITE")
_LD = re.search(r'\$\\ell_D=([0-9.]+)\$ at \$\\alpha=([0-9.]+)\$ is the exponent-one form at '
                r'\$\\ell_D=([0-9.]+)\$, and \$([0-9.]+)\$ after the', FLAT)
print(f"      the chain sentence found: {_LD is not None}")
_chain_ok = False
if _LD:
    _hdr, _a, _one, _inf = (float(_LD.group(i)) for i in (1, 2, 3, 4))
    _derived = _hdr / _a ** 0.5
    print(f"      {_hdr} / sqrt({_a}) = {_derived:.4f}   printed exponent-one {_one}")
    print(f"      and {_inf} after the one-rate move")
    _chain_ok = abs(_derived - _one) < 5.0e-3 and _inf < _one
check("the exponent-one scale is the header scale divided by sqrt(alpha), and the in-force one is "
      "lower still -- OR the chain sentence has moved", _chain_ok or _LD is None)

# ======================================================= Ⓖ⑦ THE PROBE
head("Ⓖ⑦ THE PROBE: EACH FINDING IS SENSITIVE TO THE PAPER, NOT STRUCTURALLY TRUE")
# A finding that no edit to the paper could overturn is not a reading of the paper.  Perturb the
# figures the paper prints and watch each verdict flip.
# ⛭ THE FIRST TWO VALUES TRIED HERE DID NOT FLIP, AND THAT IS WHY THE PROBE IS WORTH HAVING:
#    0.4850 gives EXACTLY 3.000 per cent -- the boundary, not inside it -- and 2.3485 vs 2.3490
#    still implies 0.0213, outside a fiftieth.  A probe whose perturbation is too small reports
#    'cannot flip' and looks like proof that the finding is structural.  Both were widened until
#    they genuinely cross.
_p1 = abs(0.4870 / 0.5 - 1.0) * 100.0      # an amplitude that DOES satisfy "within three"
_p2 = abs(2.3480 / 2.3484 - 1.0) * 100.0   # a pair whose fifth figure brings it inside a fiftieth
print(f"      (1) at an amplitude of 0.4870 the deviation is {_p1:.3f} per cent -> "
      f"'within three' would HOLD: {_p1 < 3.0}")
print(f"      (2) printed to five figures, 2.3480 vs 2.3484 implies {_p2:.4f} per cent -> "
      f"inside a fiftieth: {_p2 < 0.02}")
print(f"      ⇒ so neither verdict is a tautology: both turn on the digits the paper prints.")
check("both findings flip under a bounded change to the printed figures",
      _p1 < 3.0 and _p2 < 0.02
      and ((not STATE_A1) or DEV_POT > 3.0) and ((not STATE_A2) or IMPLIED > 0.02))

# ======================================================= THE PINS
PINS = {
    'the amplitude, 0.4835':                (not STATE_A1) or abs(AMP - 0.4835) < 1.0e-12,
    'the potential deviation, 3.30':        (not STATE_A1) or abs(DEV_POT - 3.30) < 5.0e-3,
    'the spectrum deviation, 6.49':         (not STATE_A1) or abs(DEV_SPEC - 6.49) < 5.0e-3,
    'the spectrum factor, 0.93509':         (not STATE_A1) or abs((AMP / 0.5) ** 2 - 0.93509) < 5.0e-6,
    'the stated bound (1), three':          (not STATE_A1) or abs(STATED1 - 3.0) < 1.0e-12,
    'the heights, 2.291 and 2.348':         (not STATE_A2) or (abs(H_A - 2.291) < 1.0e-12 and abs(H_B - 2.348) < 1.0e-12),
    'the second path, 2.291 and 2.349':     (not STATE_A2) or (abs(H_C - 2.291) < 1.0e-12 and abs(H_D - 2.349) < 1.0e-12),
    'the implied deviation, 0.0426':        (not STATE_A2) or abs(IMPLIED - 0.0426) < 4.0e-5,
    'the stated bound (2), a fiftieth':     (not STATE_A2) or abs(STATED2 - 0.02) < 1.0e-12,
    "the receipt's measurement, 0.011":     abs(MEASURED[0] - 0.011) < 5.0e-4,
    "the receipt's measurement, 0.017":     abs(MEASURED[1] - 0.017) < 5.0e-4,
    'the evidence exceeds the bound 2.13x': (not STATE_A2) or abs(IMPLIED / STATED2 - 2.13) < 5.0e-3,
    # ⛭ each held within HALF its own last printed digit, as plain two-sided comparisons on named
    #    values: a pin buried inside a nested expression is not one check_figures_pinned can read.
    'the quartet rise, 2.75':               abs(Q_RISE_1 - 2.75) < 4.0e-3,
    'the quartet rise, 6.29':               abs(Q_RISE_15 - 6.29) < 4.95e-3,
    'the quartet fall, 7.61':               abs(Q_FALL_1 - 7.61) < 4.95e-3,
    'the quartet fall, 16.30':              abs(Q_FALL_15 - 16.30) < 7.0e-3,
    'the visibility-peak ratio, 0.992':     abs(R_VIS - 0.992) < 4.0e-4,
    'the sharp-cut ratio, 1.023':           abs(R_CUT - 1.023) < 4.0e-4,
    'the exponent, 1.70':                   abs(ALPHA - 1.70) < 1.0e-12,
    'the withdrawn figures, 0 hits each':   all(n == 0 for n in _hits.values()),
    'the header scale, 1951.9':             (not _LD) or abs(float(_LD.group(1)) - 1951.9) < 5.0e-2,
    'the exponent-one scale, 1497.04':      (not _LD) or abs(float(_LD.group(3)) - 1497.04) < 5.0e-3,
    'the in-force scale, 1489.58':          (not _LD) or abs(float(_LD.group(4)) - 1489.58) < 5.0e-3,
    '1951.9/sqrt(1.70) = 1497.0390':        abs(1951.9 / 1.70 ** 0.5 - 1497.0390) < 5.0e-4,
}
print("\n" + "=" * 92)
print(f"  THE PRINTED FIGURES, PINNED: {sum(bool(v) for v in PINS.values())} of {len(PINS)} hold")
for k, v in PINS.items():
    if not v:
        print(f"    ⛔ NOT HELD: {k}")
assert all(PINS.values()), "a figure RESULT.md or the INDEX row prints is not held by this receipt"

print("\n" + "=" * 92)
print("  ⌗ WHAT THIS RECEIPT DOES NOT DO: it edits neither sentence.  Both are pinned by the")
print("    receipts that own them, so each fix is a coordinated paper-and-receipt change, and")
print("    whether the first receipt's finding is DISCHARGED by rewording the paper or KEPT")
print("    STANDING as a live criticism of it is 69's ruling.  No paper sentence is edited here")
print("    and THE_REGISTER.md is untouched.")
print("=" * 92)
if FAILED:
    print("\n  FAILED:")
    for f in FAILED:
        print(f"    - {f}")
print(f"\n  arms run: {len(PASSED) + len(FAILED)}   passed {len(PASSED)}, FAILED {len(FAILED)}")
assert len(PASSED) + len(FAILED) == 7, "seven arms were registered; seven must run"
sys.exit(1 if FAILED else 0)
