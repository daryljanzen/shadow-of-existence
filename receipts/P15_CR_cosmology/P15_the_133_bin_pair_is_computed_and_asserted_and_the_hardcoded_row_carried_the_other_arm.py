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

*** AND ON `r7645`'s POINT THE PAPER'S `a factor 1.98` GOES UP RATHER THAN DOWN: $2.09$ AT 70's
DISTANCES' POINT. TWO BANKS CARRY THE ARM OF RECORD -- ONE AT THE DISTANCES' BACKGROUND AND ONE AT
THE REFIT POINT -- AND THIS FILE NARRATED THE REFIT ONE'S $1.60$. READING THE WRONG ONE TURNS A
FINDING THAT SLIGHTLY STRENGTHENS THE CLAIM INTO ONE THAT HALVES IT. ***

⌗ ** AND FIVE FIGURES THIS FILE REPORTED WERE NARRATED AND NOT ASSERTED -- IN THE FILE WHOSE WHOLE
SUBJECT IS THAT A NARRATED NUMBER IS NOT A MEASURED ONE. **  `447.3733`, `3.363709`, `1.601078`,
`938.3175` and `5.071986` sat in this docstring and in no check.  *They reproduce exactly and are
gated in PART 5; the point is that nothing would have failed if they had not.*

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
  PART 3  ** HISTORICAL -- AND THE THIRD FIGURE, WHICH IS WHERE THE DEFECT WAS: 4.157889 BELONGS
          TO 68.62. **  The literal is read out of the other receipt's SOURCE, so the claim is about
          the file as it stands and not about a memory of it.  ** On the arm of record the two runs
          are ONE POINT, so the distinction this PART draws has nothing left to measure there, and
          that is asserted rather than asserted away. **
  PART 4  ** WHAT DOES NOT MOVE, SAID AS PLAINLY AS WHAT DOES. **  Both ratios are 2.0 to the two
          figures the conclusion quotes, and the 185-bin rows are recomputed here so all three rows
          of that table are live numbers from named files.
  PART 5  ** `r7645`'s ARM, SCORED RATHER THAN NARRATED. **  Three arms on one control over both
          ranges: the namesake, the arm of record at 70's DISTANCES' point (whose `l_A`, `D_M` and
          `r_s` are bit-identical to the namesake's, so it alone is like-for-like), and the arm of
          record at its REFIT point.  The five figures this file used to narrate are asserted here,
          the paper's `1.98` is shown to move UP to `2.09`, and the direction of the re-point is
          shown NOT to be common to the two ranges.

===================================================================================================
** WHY PART 3 IS MARKED HISTORICAL, AND WHY THE REST IS NOT RE-POINTED (r7639 ⑶) **
===================================================================================================

`r7639` ⑶: *"mark PART 3 of the 133-bin receipt historical.  On the arm of record the pair is one
point, so there is nothing left to measure."*  ** Measured here rather than taken on the word: **
`cc66_cr_x_h686_pol_leafrec1` and `cc66_cr_x_h6862_pol_leafrec1` differ by `max |dD_l| = 0.0000e+00`,
where the namesakes differ by `2.4067e-04`.  The two spectra ARE one file's content on the arm of
record -- `r7635+70`'s manifest records the 68.62 leg as banked from the h686 run for exactly that
reason -- so `4.16` against `4.19` is a distinction of the SUPERSEDED instrument state.  It stays
recorded, because the provenance defect it found was real and the hardcoded literal it names is still
in the other receipt's source; it is not re-asserted on the arm of record, because there is no second
point there to assert it against.

⛔ ** AND THAT RULING'S SCOPE IS THE BANK IT NAMED, WHICH IS NOT `r7645`'s POINT. **  There are TWO
arm-of-record banks for this pair.  The one `r7639` ⑶ ruled on sits at the arm's REFIT point
(`CRH0=68.57073`, `CROM=0.291246`) and its two legs ARE one file's content.  **70's DISTANCES'-point
bank is a different bank** (`CRH0=68.60`, `CROM=0.2973`, and `l_A`/`D_M`/`r_s` bit-identical to the
namesakes'), and there the two legs are `2.3601e-04` apart -- `0.9806` of the namesakes' own
separation -- so the 68.62-versus-68.60 distinction PART 3 draws is ALIVE on `r7645`'s point and is
not spent. *That is a statement about the scope of 69's ruling and not a contradiction of it: the
ruling named a bank, and this is the other one.*  ⌗ LEAFREC moves the spectrum at the distances'
point by `6.4169e-03`, 27 times the leg separation, which is what moves the $\chi^2$ at all.

** AND THE WHOLE FILE IS A PROVENANCE RECORD OF THREE NAMED BANKED SPECTRA, NOT A LIVE SCORE. **
PART 2 identifies `cc66_cr_x_h686_pol` by reproducing the `556.7` `FOR_66` records for `cc66.7`: that
identification is of a file and cannot move with an arm.  So this receipt's reads stay on their
namesakes and its figures stay as recorded.  *What the arm of record says about the same bins is a
different measurement, and PART 5 now SCORES it on both banks instead of narrating one:*

      arm                        bins        chi^2    per bin   ratio vs control
      namesake                    133     556.6858   4.185607           1.992290
      arm of record, distances    133     583.9890   4.390895         ** 2.090004 **
      arm of record, refit        133     447.3733   3.363709           1.601078
      namesake                    185    1169.8183   6.323342           1.680854
      arm of record, distances    185    1129.7632   6.106828           1.623301
      arm of record, refit        185     938.3175   5.071986           1.348222

*So `sec:refit-bound`'s "$279.4$ against $556.7$, a factor $1.98$" moves to $583.99$ and $2.09$ on
`r7645`'s point -- the claim that the arm is about twice the control SURVIVES and is slightly larger,
while the printed $1.98$ is stale and even the "$\times2.0$" rounds to $2.1$.*  ⇒ Under `r7639` ⑴ it
is reported to 69 with proposed wording and not edited here.  ⚠ **And the direction is not common to
the two ranges:** on 133 bins the arm of record is WORSE than its namesake and on 185 bins BETTER,
which this seat had registered as "worse on both" before measuring and got wrong.

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
# the same two on the arm of record AT ITS REFIT POINT (CRH0=68.57073, CROM=0.291246), which is
# the pair `r7639` ⑶ ruled on: there the two legs are one file's content.
AOR_8660 = 'cc66_cr_x_h686_pol_leafrec1'
AOR_8662 = 'cc66_cr_x_h6862_pol_leafrec1'
# ⛭⛭⛭ AND THE SAME TWO AT 70's DISTANCES' POINT (CRH0=68.60, CROM=0.2973) -- `r7645`'s point, and
#   a DIFFERENT BANK.  Their `l_A`, `D_M` and `r_s` are bit-identical to the NAMESAKES', so this is
#   the arm of record on the background the distances fix, which is what makes it like-for-like
#   against the control.  PART 5 scores it; PART 3 records that its two legs do NOT collapse.
AORD_8660 = 'cc66_cr_x_h686_pol_leafrec1_distances'
AORD_8662 = 'cc66_cr_x_h6862_pol_leafrec1_distances'
L2000_AOR = 'cc66_cr_x_h686_L2000_leafrec1'                 # 185 bins, the refit point
L2000_AORD = 'cc66_cr_x_h686_L2000_leafrec1_distances'      # 185 bins, the distances' point
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

INPUTS = [os.path.join(SP, t + '.npz')
          for t in (CONTROL, ARM_8660, ARM_8662, AOR_8660, AOR_8662, AORD_8660, AORD_8662,
                    L2000_AOR, L2000_AORD) + L2000] \
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
print("  PART 3 (HISTORICAL) -- ** AND THE HARDCODED ROW IS THE OTHER ARM: 4.16 IS 68.62 -- A")
print("                          DISTINCTION OF THE SUPERSEDED STATE, SPENT ON THE ARM OF RECORD **")
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

# ---------------------------------------------------------------------
# ** AND WHY THE ABOVE IS HISTORICAL, MEASURED HERE AND NOT ASSERTED AWAY (r7639 ⑶). **
_zn = [np.load(os.path.join(SP, t + '.npz')) for t in (ARM_8660, ARM_8662)]
_za = [np.load(os.path.join(SP, t + '.npz')) for t in (AOR_8660, AOR_8662)]
if not (np.array_equal(_zn[0]['ls'], _zn[1]['ls']) and np.array_equal(_za[0]['ls'], _za[1]['ls'])):
    fail.append("the 68.60/68.62 pair is not on one ell grid on one of the two arms -- "
                "nothing below compares like with like")
else:
    _dn = float(np.max(np.abs(np.asarray(_zn[0]['Dl'], float) - np.asarray(_zn[1]['Dl'], float))))
    _da = float(np.max(np.abs(np.asarray(_za[0]['Dl'], float) - np.asarray(_za[1]['Dl'], float))))
    print()
    print(f"  the namesakes differ by     max |dD_l| = {_dn:.4e}  -- two runs, and PART 3 reads them")
    print(f"  the arm of record differs by max |dD_l| = {_da:.4e}"
          + ("  -- ** ONE POINT **" if _da == 0.0 else "  -- ** AND THAT IS NOT ONE POINT **"))
    _zd = [np.load(os.path.join(SP, t + '.npz')) for t in (AORD_8660, AORD_8662)]
    _dd = float(np.max(np.abs(np.asarray(_zd[0]['Dl'], float) - np.asarray(_zd[1]['Dl'], float))))
    _dl = float(np.max(np.abs(np.asarray(_zn[0]['Dl'], float)
                              - np.asarray(_zd[0]['Dl'], float))))
    print(f"  at 70's DISTANCES' point it differs by max |dD_l| = {_dd:.4e}  -- ** TWO POINTS, "
          f"{_dd / _dn:.4f} of the namesakes' separation **")
    check_hist = (_dn > 0.0 and _da == 0.0)
    if not check_hist:
        fail.append(f"PART 3's historical marking rests on the pair being two points on the "
                    f"namesakes ({_dn:.4e}) and one on the arm of record ({_da:.4e}), and it is not")
    if not (_dd > 0.0 and 0.97 < _dd / _dn < 0.99 and _dl > 20 * _dd):
        fail.append(f"⛔ the SCOPE of `r7639` ⑶'s ruling: the legs must still be TWO points at the "
                    f"distances' point ({_dd:.4e}, {_dd / _dn:.4f} of the namesakes') while LEAFREC "
                    f"moves the spectrum there by {_dl:.4e}, and they are not")
    else:
        print("  ⛔ ** AND `r7639` ⑶'s RULING DOES NOT TRANSFER TO `r7645`'s POINT. **  The collapse "
              "to one")
        print("     point is a property of the REFIT-point bank alone.  At the DISTANCES' point the "
              f"two legs")
        print(f"     are {_dd:.4e} apart -- {_dd / _dn:.4f} of the namesakes' own separation, so the "
              "68.62-versus-68.60")
        print("     distinction PART 3 draws is ALIVE there and is not spent.  *That is a statement "
              "about")
        print("     the scope of 69's ruling and not a contradiction of it: the ruling named the "
              "bank it named,")
        print(f"     and this is a different bank.*  ⌗ LEAFREC moves the spectrum at the distances' "
              f"point by")
        print(f"     {_dl:.4e}, {_dl / _dd:.0f} times the leg separation, which is why PART 5's "
              "chi^2 moves at all.")
    if check_hist:
        print("  ** SO PART 3 IS HISTORICAL. **  `r7635+70` banked the 68.62 leg from the h686 run")
        print("   because on the arm of record the pair is one point, and that is what this reads:")
        print("   the 4.16/4.19 distinction is a property of the SUPERSEDED instrument state.  It")
        print("   stays recorded -- the provenance defect was real and the literal is still in the")
        print("   other receipt's source -- and it is NOT re-asserted on the arm of record, because")
        print("   there is no second point there to assert it against.")

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
print("  PART 5 -- ** THE SAME BINS ON 70's DISTANCES' POINT: `r7645`'s ARM, SCORED NOT NARRATED **")
print("=" * 100)

# ⛭⛭⛭ THREE ARMS ON ONE CONTROL, all scored through the same `chi2_of_spectrum` route:
#   ⒜ the NAMESAKE (LEAFREC=0) on the distances' background;
#   ⒝ the ARM OF RECORD at 70's DISTANCES' point -- `r7645`'s arm, whose `l_A`, `D_M` and `r_s` are
#      bit-identical to the namesake's, so it is the only one of the two that is like-for-like;
#   ⒞ the ARM OF RECORD at its REFIT point -- a DIFFERENT background (68.57073 / 0.291246), and the
#      bank this file used to NARRATE in its own prose without asserting.
# ⚠ ** THAT NARRATION IS THE DEFECT THIS FILE EXISTS TO NAME, COMMITTED BY THIS FILE. **  Five
#   figures -- 447.3733, 3.363709, 1.601078, 938.3175, 5.071986 -- sat in the docstring above and in
#   NO check.  A narrated number is not a measured one; they are asserted here.
CTL = {133: S[CONTROL][0], 185: lc[1]}
ROWS = (('namesake', 133, ARM_8660), ('arm of record, distances', 133, AORD_8660),
        ('arm of record, refit', 133, AOR_8660), ('namesake', 185, L2000[1]),
        ('arm of record, distances', 185, L2000_AORD), ('arm of record, refit', 185, L2000_AOR))
P5 = {}
print(f"  {'arm':>26} {'bins':>5} {'chi2':>12} {'per bin':>10} {'ratio vs control':>18}")
for _lab, _nb, _tag in ROWS:
    _ls, _c, _n = score(_tag)
    if _n != _nb:
        fail.append(f"{_tag} covers {_n} bins, not the {_nb} its row is named for")
    P5[(_lab, _nb)] = (_c, _c / _n, _c / CTL[_nb])
    print(f"  {_lab:>26} {_nb:>5d} {_c:>12.4f} {_c / _n:>10.6f} {_c / CTL[_nb]:>18.6f}")

_rf, _rf185 = P5[('arm of record, refit', 133)], P5[('arm of record, refit', 185)]
if not (abs(_rf[0] - 447.3733214661322) < 1e-6 and abs(_rf[1] - 3.3637091839558813) < 1e-9
        and abs(_rf[2] - 1.6010782480251757) < 1e-9
        and abs(_rf185[0] - 938.3174809880677) < 1e-6
        and abs(_rf185[1] - 5.071986383719285) < 1e-9):
    fail.append("the five figures this file NARRATED are not reproduced where it narrated them -- "
                f"{_rf[0]:.4f}/{_rf[1]:.6f}/{_rf[2]:.6f} and {_rf185[0]:.4f}/{_rf185[1]:.6f}")
else:
    print(f"\n  ⛭ the five formerly-narrated figures reproduce EXACTLY and are now asserted: "
          f"{_rf[0]:.4f}, {_rf[1]:.6f} per bin,")
    print(f"    a factor {_rf[2]:.6f} on 133 bins, and {_rf185[0]:.4f} at {_rf185[1]:.6f} per bin "
          "on 185 -- all at the REFIT point.")

_nm, _ad = P5[('namesake', 133)][2], P5[('arm of record, distances', 133)][2]
if not (1.9920 < _nm < 1.9926 and 2.0897 < _ad < 2.0903):
    fail.append(f"the 133-bin ratio is {_nm:.6f} on the namesake and {_ad:.6f} at the distances' "
                "point, not the pair this part pins")
else:
    print(f"\n  ⛔⛔ ** AND `sec:refit-bound`'s PRINTED `a factor 1.98` MOVES TO {_ad:.2f} ON "
          f"`r7645`'s POINT, NOT DOWN TO THE {_rf[2]:.2f}")
    print(f"     THIS FILE NARRATES. **  The namesake is {_nm:.4f} and the arm of record at the "
          f"distances' point is {_ad:.4f}:")
    print(f"     *the conclusion that the arm is about twice the control SURVIVES and is slightly "
          "LARGER, while the")
    print(f"     printed `1.98` is stale and even the `x2.0` rounds to {round(_ad, 1)} rather than "
          f"{round(_nm, 1)}.*  ⇒ The {_rf[2]:.2f} is the")
    print("     REFIT point's, where the arm has four parameters the control does not, so it is not "
          "the figure")
    print("     `sec:refit-bound`'s sentence is about.  ⌗ Reading the wrong one of these two banks "
          "turns a")
    print("     finding that strengthens the claim into one that halves it.")

_n1, _a1 = P5[('namesake', 133)][1], P5[('arm of record, distances', 133)][1]
_n2, _a2 = P5[('namesake', 185)][1], P5[('arm of record, distances', 185)][1]
if not (_a1 > _n1 and _a2 < _n2):
    fail.append(f"the re-point's DIRECTION is asserted to differ between the ranges and does not: "
                f"133 {_n1:.6f}->{_a1:.6f}, 185 {_n2:.6f}->{_a2:.6f}")
else:
    print(f"\n  ⛔ ** AND THE DIRECTION IS NOT COMMON TO THE TWO RANGES, WHICH THIS SEAT PREDICTED "
          "IT WOULD BE. **")
    print(f"     On 133 bins the arm of record is WORSE than its namesake ({_n1:.6f} -> {_a1:.6f} "
          "per bin); on 185")
    print(f"     bins it is BETTER ({_n2:.6f} -> {_a2:.6f}).  *Registered before measuring as "
          "`worse on both`,")
    print("     and the reachable negative fired.  A re-point's sign is a property of the RANGE and "
          "not of the arm.*")

if not (_rf[1] < _n1 and _rf[1] < _a1 and _rf185[1] < _n2 and _rf185[1] < _a2):
    fail.append("the refit point is asserted to beat both unrefit arms on both ranges and does not")
else:
    print(f"\n  ⌗ the refit point beats both unrefit arms on both ranges ({_rf[1]:.4f} against "
          f"{_n1:.4f} and {_a1:.4f};")
    print(f"    {_rf185[1]:.4f} against {_n2:.4f} and {_a2:.4f}), which is what four fitted "
          "parameters buy and is why it")
    print("    cannot stand in for an unrefit comparison.")

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
print("  ⌗ PART 3 is HISTORICAL as of `r7639` ⑶ FOR THE REFIT-POINT BANK, where the two runs are")
print("    one point.  ⛔ At 70's DISTANCES' point -- `r7645`'s -- they are two points again, 0.9806")
print("    of the namesakes' own separation, so that ruling's scope is the bank it named.")
print(f"  ⛔ And `sec:refit-bound`'s printed `a factor 1.98` moves UP to {_ad:.2f} there, not down to")
print(f"    the {_rf[2]:.2f} this file used to narrate from the other bank.")
print("=" * 100)
sys.exit(0)
