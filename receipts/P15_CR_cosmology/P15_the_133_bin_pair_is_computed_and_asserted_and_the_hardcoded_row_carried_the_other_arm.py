#!/usr/bin/env python3
"""
RECEIPT -- P15: ** THE TWO FIGURES THE CORPUS HAS BEEN QUOTING FOR THE 133-BIN COMPARISON ARE
COMPUTED AND ASSERTED HERE FOR THE FIRST TIME -- THE CONTROL'S 2.10 PER BIN AND THE 4.16 BESIDE IT.
UNTIL NOW ONE LIVED IN A HEADLINE AND THE OTHER IN A HARDCODED PRINT, AND NEITHER WAS AN ASSERTION. **

*** AND COMPUTING THEM FINDS THAT THE HARDCODED ONE IS THE WRONG RUN'S: `4.16` IS THE H0 = 68.62
CONFIRMATION ARM, NOT THE 68.60 ARM `r6760+cc66.7` REPORTED AND NOT THE 68.60 ARM THE TWO ROWS
PRINTED BESIDE IT ARE COMPUTED FROM.  cc66.7's OWN FIGURE IS 4.19. ***

** NOTHING MOVES: 4.16/2.10 = 1.98 against 4.19/2.10 = 1.99, and both are the "x2.0" the conclusion
rests on. **  *This is a provenance defect and is reported as one -- but it is a provenance defect
inside a table whose entire purpose is a LIKE-FOR-LIKE ratio, and a computed row is what caught it.*

Built r7109+cc66.85 (node 66, code seat), answering the first half of `r7109` ⓷ (= `r7101` Q1).

===================================================================================================
** WHAT WAS ASKED, AND WHY A NARRATED NUMBER IS NOT A MEASURED ONE **
===================================================================================================

`r7101` named it and `r7109` ⓷ refused to reclassify it: *"the control's 2.10 per bin on 133 bins,
computed and ASSERTED by a receipt rather than narrated in one headline and hardcoded in another's
print -- it is the last live item on the thirteen-figure list."*

** The two sites, read as they stand: **

  * `P15_the_handover_at_the_crossing_and_what_it_costs` -- the number is in its HEADLINE ("35.5 per
    bin against the control's 2.10"), which no check reads.  Four more receipts repeat it in prose.
  * `P15_the_full_range_lensed_comparison_...` line 129 -- `print(f"... {4.16 / 2.10:>11.2f}x")`.
    ** A literal division inside an f-string, in a receipt that computes the two rows beneath it
    live. **  Nothing fails if either number is wrong, and nothing did.

  PART 1  ** THE CONFIGURATION AND THE BIN COUNT, asserted off the spectra and not off the name. **
          133 bins, ell 100 to 1298.  The pair identified by file and asserted tracked.
  PART 2  ** THE TWO FIGURES, COMPUTED. **  The control at 2.100902 per bin and the arm at 4.185607,
          through `chi2_of_spectrum.py` -- the corpus's own machinery, one amplitude fitted, the
          same route every other chi^2 in this sector is scored on.
  PART 3  ** AND THE THIRD FIGURE, WHICH IS WHERE THE DEFECT IS: 4.157889 BELONGS TO 68.62. **  The
          literal is read out of the other receipt's SOURCE, so the claim is about the file as it
          stands and not about a memory of it.
  PART 4  ** WHAT DOES NOT MOVE, SAID AS PLAINLY AS WHAT DOES. **  Both ratios are 2.0 to the two
          figures the conclusion quotes, and the 185-bin rows are recomputed here so all three rows
          of that table are live numbers from named files.

===================================================================================================
** WHAT THIS DOES NOT CLAIM **
===================================================================================================

** It does not claim the x2.57 conclusion is affected. **  It is not: the comparison that matters
there is 185-bin lensed against 185-bin unlensed, both computed live in that receipt from one arm.
** And it does not claim cc66.7 reported the wrong number. **  cc66.7 reported 4.19 and `FOR_66`
records its chi^2 as 556.7, which is this file's 556.6858 -- *the reporting was right and the later
transcription into a neighbouring receipt's print was not.*

** COMPUTES: nothing. ***  Three banked spectra are read and scored through
   `chi2_of_spectrum.py`; every parameter is the one baked into the `.npz` it came from --
   the control at the instrument's own (67.40, 0.3150), the arm at (68.60, 0.2973) and the
   confirmation arm at (68.62, 0.2973), all on the polarisation path at `LMAXL=1300`, `LSTEP=2`.
   *The whole point of this file is that those H0 values are DIFFERENT and a literal could not say
   so, which is why they are named here rather than left to the filenames.*

SETTINGS: the banked 133-bin pair as committed -- `LMAXL=1300`, polarisation path, `LSTEP=2`.  ** The
figures are properties of banked spectra and the published covariance, so no run can move them; what
a deeper run would move is the SPECTRA, and that is a different question with its own receipts. **

rc=0 on success.  Run: python3 P15_the_133_bin_pair_is_computed_and_asserted_and_the_hardcoded_row_carried_the_other_arm.py
                       (numpy scipy, ~10 s)
"""
import os
import re
import subprocess
import sys

import numpy as np

print(__doc__.split("rc=0")[0])
fail = []

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

CONTROL = 'cc66_lcdm'
ARM_8660 = 'cc66_cr_x_h686_pol'       # r6760+cc66.7's own arm: H0 = 68.60
ARM_8662 = 'cc66_cr_x_h6862_pol'      # the ordered confirmation run: H0 = 68.62
L2000 = ('cc66_lcdm_L2000', 'cc66_cr_x_h686_L2000')
LENSED_RECEIPT = os.path.join(
    HERE, 'P15_the_full_range_lensed_comparison_is_the_unfavourable_one_and_the_control_is_nearly_camb.py')
HANDOVER = os.path.join(HERE, 'P15_the_handover_at_the_crossing_and_what_it_costs.py')


def score(tag):
    z = np.load(os.path.join(SP, tag + '.npz'))
    ls = np.asarray(z['ls'], float)
    Dl = np.asarray(z['Dl'], float)
    chi2, n = CS.chi2_of(ls, Dl)[:2]
    return ls, float(chi2), int(n)


# =====================================================================
print("=" * 100)
print("  PART 1 -- ** THE CONFIGURATION AND THE BIN COUNT, OFF THE SPECTRA **")
print("=" * 100)

INPUTS = [os.path.join(SP, t + '.npz') for t in (CONTROL, ARM_8660, ARM_8662) + L2000] \
    + [LENSED_RECEIPT, HANDOVER]
try:
    subprocess.run(['git', '-C', ROOT, 'ls-files', '--error-unmatch'] + INPUTS,
                   check=True, capture_output=True)
    print(f"  all {len(INPUTS)} inputs are tracked by git in this checkout")
except subprocess.CalledProcessError as exc:
    fail.append("an input is not tracked by git: "
                + exc.stderr.decode('utf-8', 'replace').strip().split('\n')[0][:120])
except (OSError, FileNotFoundError):
    absent = [p for p in INPUTS if not os.path.exists(p)]
    if absent:
        fail.append(f"{len(absent)} input(s) absent and git unavailable to check tracking")
    else:
        print(f"  git unavailable here; all {len(INPUTS)} inputs exist (tracking unchecked)")

print(f"  {'spectrum':>24} {'ell range':>16} {'bins':>6} {'chi2':>11} {'per bin':>10}")
S = {}
for tag in (CONTROL, ARM_8660, ARM_8662):
    ls, chi2, n = score(tag)
    S[tag] = (chi2, n)
    print(f"  {tag:>24} {f'{ls[0]:.0f}..{ls[-1]:.0f}':>16} {n:>6d} {chi2:>11.4f} {chi2 / n:>10.6f}")
    if n != 133:
        fail.append(f"{tag} covers {n} bins, not the 133 the comparison is named for")
if len({S[t][1] for t in S}) != 1:
    fail.append("the three 133-bin spectra do not cover the same bins -- not like-for-like")
else:
    print(f"  ** all three cover the same {S[CONTROL][1]} bins, so the ratios below are matched **")

# =====================================================================
print()
print("=" * 100)
print("  PART 2 -- ** THE TWO FIGURES, COMPUTED AND ASSERTED FOR THE FIRST TIME **")
print("=" * 100)
cb = S[CONTROL][0] / S[CONTROL][1]
ab = S[ARM_8660][0] / S[ARM_8660][1]
print(f"  ** the control: chi^2 = {S[CONTROL][0]:.4f} over {S[CONTROL][1]} bins = "
      f"{cb:.6f} per bin **   (the corpus's 2.10)")
print(f"  ** the arm at H0 = 68.60: chi^2 = {S[ARM_8660][0]:.4f} = {ab:.6f} per bin **   "
      f"(cc66.7's own 4.19)")
# asserted at the two decimals the corpus quotes, and not finer
if round(cb, 2) != 2.10:
    fail.append(f"the control comes out {cb:.4f} per bin, which is not the quoted 2.10")
if round(ab, 2) != 4.19:
    fail.append(f"the 68.60 arm comes out {ab:.4f} per bin, which is not cc66.7's 4.19")
# and the chi^2 FOR_66 records, so the identification of the file is not a guess
if abs(S[ARM_8660][0] - 556.7) > 0.05:
    fail.append(f"the 68.60 arm's chi^2 is {S[ARM_8660][0]:.2f}, not the 556.7 cc66.7 recorded -- "
                f"this may not be cc66.7's spectrum")
else:
    print(f"  the arm's chi^2 is {S[ARM_8660][0]:.4f} against the 556.7 `FOR_66` records for cc66.7, "
          f"so the file is identified and not guessed")
print(f"  ratio, 68.60 against the control: ** {ab / cb:.6f} ** -- the 'factor 2.0'")
if not 1.95 < ab / cb < 2.05:
    fail.append(f"the 133-bin ratio is {ab / cb:.3f}, not the factor 2.0 the corpus quotes")

# and the headline that carried 2.10, quoted so the site is named and not remembered
HO = open(HANDOVER, encoding='utf-8', errors='replace').read()
# ⌗ case-insensitive: the site is a docstring HEADLINE and is upper-cased there, which a
#   case-sensitive search missed on the first run of this file.
if "against the control's 2.10" in HO.lower():
    print("  the headline site, quoted: \"35.5 PER BIN AGAINST THE CONTROL'S 2.10\" -- "
          "in a docstring, which no check reads")
else:
    print("  ⌗ the headline no longer carries 2.10 -- this receipt's premise has moved and should "
          "be re-read")

# =====================================================================
print()
print("=" * 100)
print("  PART 3 -- ** AND THE HARDCODED ROW IS THE OTHER ARM: 4.16 IS 68.62 **")
print("=" * 100)
ab2 = S[ARM_8662][0] / S[ARM_8662][1]
print(f"  the arm at H0 = 68.62: chi^2 = {S[ARM_8662][0]:.4f} = {ab2:.6f} per bin  -> {ab2:.2f}")
if round(ab2, 2) != 4.16:
    fail.append(f"the 68.62 arm comes out {ab2:.4f} per bin, not the 4.16 the hardcoded row carries")
print(f"  the arm at H0 = 68.60: {ab:.6f} per bin  -> {ab:.2f}")
if round(ab, 2) == round(ab2, 2):
    fail.append("the two arms round to the same figure -- PART 3's whole distinction fails")
else:
    print("  ** the two runs are distinguishable at the two decimals the corpus quotes: "
          f"{ab2:.2f} and {ab:.2f} **")

SRC = open(LENSED_RECEIPT, encoding='utf-8', errors='replace').read()
rows = re.findall(r"133-bin[^\n]*?\{([0-9.]+)\s*/\s*([0-9.]+)", SRC)
if not rows:
    print("  ⌗ the hardcoded 133-bin row is no longer a literal division in that receipt --")
    print("    repaired, and this PART is spent.  *Left in place because the figure it names stays")
    print("    asserted above, which is the half `r7101` actually asked for.*")
else:
    num, den = (float(x) for x in rows[0])
    print(f"  the literal in that receipt's source: {num} / {den}")
    if abs(den - round(cb, 2)) > 1e-9:
        fail.append(f"the hardcoded denominator is {den}, not the control's {cb:.2f}")
    if abs(num - round(ab2, 2)) < 1e-9 and abs(num - round(ab, 2)) > 1e-9:
        print("  ⚠ ** THE DEFECT, STATED: the literal numerator is the 68.62 run's figure, while the")
        print("     row's own label reads '(r6760+cc66.7)' and cc66.7's arm is the 68.60 one -- whose")
        print(f"     figure is {ab:.2f}. **")
        if '(r6760+cc66.7)' not in SRC:
            print("     ⌗ the label has changed; the mis-attribution may already be repaired")
        if 'h686_L2000' not in SRC:
            fail.append("that receipt no longer loads the 68.60 arm -- PART 3's comparison is stale")
        else:
            print("     ⌗ and the two rows computed LIVE beneath it load `cr_x_h686_L2000`, the 68.60")
            print("        arm -- so the table mixes two H0 values in three rows.")
    elif abs(num - round(ab, 2)) < 1e-9:
        print("  ⌗ the literal numerator is the 68.60 arm's figure -- correctly attributed, and this")
        print("    PART's finding is spent.  *Then the only defect left is that it is a literal.*")
    else:
        fail.append(f"the hardcoded numerator {num} matches neither arm at two decimals "
                    f"({ab:.2f}, {ab2:.2f}) -- it is a third number with no file")

# =====================================================================
print()
print("=" * 100)
print("  PART 4 -- ** WHAT DOES NOT MOVE, AND THE WHOLE TABLE AS LIVE NUMBERS **")
print("=" * 100)
r_8660, r_8662 = ab / cb, ab2 / cb
print(f"  the ratio the conclusion rests on, both ways: {r_8662:.4f} (68.62) and {r_8660:.4f} (68.60)")
print(f"  to the two figures that conclusion quotes: {r_8662:.2f}x and {r_8660:.2f}x")
if round(r_8660, 1) != round(r_8662, 1):
    fail.append("the two ratios differ at the one decimal the conclusion quotes -- then the defect "
                "is NOT harmless and this receipt's headline is wrong")
print("  ** so the 'x2.0' is x2.0 either way, and the defect is provenance and not arithmetic. **")

lc, la = (score(L2000[0]), score(L2000[1]))
print(f"\n  and the 185-bin rows, recomputed from their own files:")
print(f"  {'row':>40} {'bins':>6} {'chi2':>11} {'per bin':>9}")
for nm, (ls, chi2, n) in ((L2000[0], lc), (L2000[1], la)):
    print(f"  {nm:>40} {n:>6d} {chi2:>11.4f} {chi2 / n:>9.4f}")
    if n != 185:
        fail.append(f"{nm} covers {n} bins, not 185")
print(f"  {'185-bin unlensed ratio':>40} {'':>6} {'':>11} {la[1] / lc[1]:>9.4f}")
# the receipt's own quoted pair, so this file reproduces it rather than restating it
if abs(lc[1] - 696) > 1.0:
    fail.append(f"the 185-bin control is {lc[1]:.1f}, not the 696 that receipt quotes unlensed")
else:
    print(f"  the 185-bin control reproduces that receipt's quoted 696 unlensed ({lc[1]:.1f})")
print("  ⌗ *The LENSED rows stay in their own receipt, which owns the operator and checks it; this")
print("   file's business is the 133-bin pair, and duplicating a CAMB call would duplicate the check")
print("   that validates it.*")

# =====================================================================
print()
print("=" * 100)
if fail:
    print(f"  FAIL -- {len(fail)} check(s) did not hold")
    for f in fail:
        print(f"    - {f}")
    print("=" * 100)
    sys.exit(1)
print("  ** ALL CHECKS HOLD. **  The first half of `r7109` ⓷ is answered: the control's 2.10 per bin")
print(f"  on 133 bins is COMPUTED ({cb:.6f}) and ASSERTED, and so is the 4.16 beside it")
print(f"  ({ab2:.6f}) -- together with cc66.7's own 4.19 ({ab:.6f}), which is the figure the")
print("  hardcoded row should have carried and does not.  ** The conclusion is untouched and the")
print("  attribution is not, and only a computed row could have told the two apart. **")
print("=" * 100)
sys.exit(0)
