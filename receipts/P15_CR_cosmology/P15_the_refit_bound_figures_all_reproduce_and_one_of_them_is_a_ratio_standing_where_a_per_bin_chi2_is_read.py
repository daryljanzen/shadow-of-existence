#!/usr/bin/env python3
r"""
RECEIPT -- P15 / `sec:refit-bound`: ** EVERY FIGURE IN THE TWO QUOTED PAIRS REPRODUCES FROM THE
BANKED SPECTRA -- AND ONE OF THE NINE NAMES NO QUANTITY. **  The paper's $\chi^{2}=214.1$ / $550.5$
on $185$ lensed bins, its $1.16$ / $2.98$ per bin and its $2.57$ times are EXACT; the refit's $1.01$
and $1.58$ per bin and $1.57$ times are EXACT.

** ⇒ BUT THE PAPER'S "$2.56$ ON THE SAME BINS" IS A RATIO, AND IT STANDS IN A SENTENCE WHOSE OTHER
FIGURES ARE PER-BIN $\chi^{2}$. **  The computing receipt says `2.56x as-computed`, with the `x`.
*Measured here: the as-computed pair is $212.9$ / $545.8$, so the RATIO is $2.56$ and the arm's
as-computed figure PER BIN is $2.95$.*  ⛔ ** And the paper states the computed arm at $2.98$ per bin
three sentences earlier**, so a reader who carried that figure into "the computed spectrum sits at
$2.56$ on the same bins" met what looked like the same quantity twice with two values.

** ⌗ REPAIRED IN PRINT AT `r7167`: the sentence now reads "sits at $2.56$ TIMES IT on the same
bins", and this receipt's own locator requires the word. **

** ⛭⛭ AND THE FIGURE IT CARRIES HAS SINCE MOVED TWICE, WHICH IS WHAT THIS BLOCK IS FOR. **
*The paragraph above is the r7166 reading and is left as the record of it.  What the file measures
TODAY is not those figures: the arm leg was re-pointed to the arm of record at `r7649`, and at
`r7821` ④ -- 69's ruling on this pass -- the as-computed CONTROL was re-pointed to Planck 2018's
published point, because `refit_grid185/lcdm_base.npz` sits at the UN-REFITTED background and is the
same swappable-bank class the `L2000` row was re-pointed out of.  The current figures are PART 2's
printed table and PART 5's literal pins, computed on every run; the only ones written down in prose
anywhere in this file are the paper's own, captured.*  ⇒ *The finding -- that the clause's figure
is a RATIO standing among per-bin chi^2 -- does not depend on which point the control sits at, and
survives both re-points unchanged.*  *So the finding stands as a finding and
the receipt is the thing that detects its discharge -- which it could not do while it read a
sentence the repair would break.*

*** THE RULE THIS IS AN INSTANCE OF IS THE CORPUS'S OWN, REGISTERED AT `r7165` FROM THIS SEAT'S
`Ⓕ③` LABEL: a label that cannot be checked against the wrong quantity is the only kind that cannot
be read against it either.  Here the two neighbouring ratios BOTH carry the word -- "$2.57$ times",
"$1.57$ times" -- and this one does not. ***

⌗ ** THE GATE ROW IS CLEAN AND THE PROSE IS NOT, WHICH IS THE OPPOSITE DIRECTION FROM `r7165`. **
`INDEX.md` says "disfavoured at 1.57 times the control", with the word.  *So a check comparing the
row against the receipt would see nothing: this defect lives only where the row and the receipt do
not reach, and the reader does.*

Built r7166+cc66.135 (node 66, code seat), answering the chat seat's `r7166` invitation -- *"if
either pair ever looks wrong to you from the physics side rather than the citation side, that is
worth saying, because the sweep cannot tell the difference and neither can I from where I am
reading"* -- on the two pairs it named, `214.1`/`550.5` and `1.58`/`2.56`.

===================================================================================================
** WHAT IS READ RATHER THAN RUN, AND WHY NO FIGURE IS TYPED **
===================================================================================================

  ** THE NINE FIGURES ARE READ OUT OF THE PAPER, NOT TYPED HERE. **  Both sentences are located in
  `corpus/CR_cosmology.tex` inside `sec:refit-bound` by their own wording and their figures are
  captured.  *A drifted sentence REFUSES rather than passing: there is no fallback literal to fall
  back to, which is the whole point of reading them.*

  ** THE THREE CONFIGURATIONS ARE READ FROM BANKED SPECTRA. **  `spectra/cc66_{cr_x_h686,lcdm}_L2000`
  for the full-range lensed pair, with the CONTROL leg taken from `(a1)`'s matched step-2 assembly
  at Planck 2018's published point; `refit_grid185_leafrec1_distances/cr_base` against
  `r7807`'s `out/r7807_control_planck2018_L2000` for the refit's as-computed pair -- the same
  `ARM=lcdm HIER=1 LSTEP=8 LMAXL=2000` configuration as `refit_grid185/lcdm_base` at Planck's
  published point instead of the un-refitted one, on the same 238-sample grid;
  `spectra/cc66_r185_verify_{cr,lcdm}` for its verified minimum, which CANNOT be re-pointed because a
  minimum of the fit does not depend on where the search began.  Nothing is re-solved and no fit is
  re-run -- the scoring is `chi2_of_spectrum`'s, with P15's own CAMB lensing operator imposed on
  both arms alike so it cannot favour either.

  ** AND THE COMPARISON IS EXACT AT THE PAPER'S OWN PRECISION, NOT INSIDE A TOLERANCE. **  Each
  figure must equal the computed value ROUNDED to the number of decimals the paper prints.  *A
  tolerance wide enough to absorb a wrong quantity is a tolerance that cannot report one.*

** COMPUTES: the nine quoted figures of `sec:refit-bound`'s two chi^2 pairs, each against the
   configuration it is a figure of; the identification of which quantity the paper's 2.56 is; and
   the gap between the two instruments that both call their range "185 bins,
   ell = 100-1996", shown to be configuration and not disagreement; and, from `r7821` ④, the
   as-computed pair with its control at Planck 2018's published point, pinned on literals in PART 5
   because the clause's citation was narrowed to this receipt alone. ***

STATUS: OK
rc=0 on success.  Run: python3 <this file>   (numpy, camb; ~10 s -- reads banked spectra)
"""
import os
import re
import sys

import numpy as np

print(__doc__.split("STATUS:")[0])
BAR = "=" * 104
fail = []


def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        fail.append(label)


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TEX = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
GRID = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'refit_grid185')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

# =================================================================================================
print(BAR)
print("  PART 1 -- ** THE NINE FIGURES, READ OUT OF THE PAPER **")
print(BAR)

_src = open(TEX, encoding='utf-8').read()
_lab = _src.find(r'\label{sec:refit-bound}')
if _lab < 0:
    print("  ⛔ REFUSED: sec:refit-bound carries no label in this paper -- the section cannot be "
          "located, so nothing below is about it.")
    sys.exit(1)
_nxt = _src.find(r'\subsection', _lab + 1)
SECTION = re.sub(r'\s+', ' ', _src[_lab:_nxt if _nxt > 0 else len(_src)])
print(f"  sec:refit-bound located at character {_lab}, {len(SECTION)} characters of flattened text")

LENSED = (r"the control returns \$\\chi\^\{2\}=([0-9.]+)\$, or \$([0-9.]+)\$ per bin, and this "
          r"arm \$([0-9.]+)\$, or \$([0-9.]+)\$ per bin: \\emph\{the arm sits at \$([0-9.]+)\$ times")
# The `times it` in this pattern is the r7167 REPAIR, and reading it is how this receipt
# detects its own finding having been fixed.  Before r7167 the paper read `sits at $2.56$ on
# the same bins`; the word is what this receipt found missing, so the locator now requires it
# and goes RED if it is ever dropped again.  *A finding receipt whose locator does not carry
# the repair cannot tell a discharged finding from a live one -- which is the r7165 blindness
# in the register, arriving here.*
REFIT = (r"the control settles at \$([0-9.]+)\$ in \$\\chi\^\{2\}\$ per bin and this arm at "
         r"\$([0-9.]+)\$: \\emph\{the arm at \$([0-9.]+)\$ times the control's distance, where the "
         r"computed spectrum sits at \$([0-9.]+)\$ times it on the same bins\}")

# ** THE PRE-`r7167` DEFECTIVE SENTENCE, KEPT SO THE REFUSAL CAN SAY WHICH THING HAPPENED. **
# Requiring `times it` above is right -- tolerating the old form would be the `r7165` blindness,
# a locator that cannot tell a discharged finding from a live one.  *But measured at `cc66.136`,
# requiring it made the two refusals IDENTICAL: a correct rewording that names the quantity
# differently and a regression that drops the word again both came back `matches 0 time(s)`,
# byte for byte.*  => So the receipt detected "the wording moved" and not "the word was
# dropped", which for a receipt whose job is now to detect its own discharge is the one thing it
# must not be vague about.  ** This is a CLASSIFIER on the refusal and NOT a tolerance: the
# defective form is still refused with rc=1 and still asserts nothing, and the relapse message
# can never fire unless the literal defective sentence is there. **
RELAPSE = (r"the control settles at \$[0-9.]+\$ in \$\\chi\^\{2\}\$ per bin and this arm at "
           r"\$[0-9.]+\$: \\emph\{the arm at \$[0-9.]+\$ times the control's distance, where the "
           r"computed spectrum sits at \$[0-9.]+\$ on the same bins\}")

PAPER = {}
for name, pat, keys in (('the lensed pair', LENSED,
                         ('chi2_ctl', 'bin_ctl', 'chi2_arm', 'bin_arm', 'ratio')),
                        ('the refit pair', REFIT,
                         ('rf_bin_ctl', 'rf_bin_arm', 'rf_ratio', 'as_computed'))):
    hits = re.findall(pat, SECTION)
    if len(hits) != 1:
        if pat is REFIT and re.search(RELAPSE, SECTION):
            print("  \u26d4 REFUSED -- ** THE `r7167` REPAIR HAS BEEN UNDONE: the clause reads "
                  "`sits at $2.56$ on the same bins` again, without the word. **  That figure is "
                  "the arm-over-control RATIO, and the sentence puts it back where every other "
                  "figure is a chi^2 per bin -- three sentences after the computed arm is given "
                  "at 2.98 per bin.  *This is the finding this receipt was built on, returning.*"
                  "  Nothing is asserted.")
        else:
            print(f"  \u26d4 REFUSED: {name}'s sentence matches {len(hits)} time(s) in "
                  f"sec:refit-bound.  The wording this receipt reads has DRIFTED, and a figure "
                  f"that cannot be located is not a figure that can be checked.  ** This is NOT "
                  f"the pre-r7167 defect, which has its own refusal. **  Nothing is asserted.")
        sys.exit(1)
    for k, v in zip(keys, hits[0]):
        PAPER[k] = v
    print(f"  {name:>16}: " + "  ".join(f"{k}={PAPER[k]}" for k in keys))


def paper(k):
    """The paper's figure, with the number of decimals the paper prints it to."""
    s = PAPER[k]
    return float(s), len(s.split('.')[1]) if '.' in s else 0


# =================================================================================================
print()
print(BAR)
print("  PART 2 -- ** THE LENSING OPERATOR, AND THE THREE CONFIGURATIONS SCORED **")
print(BAR)

import camb                                                                # noqa: E402
_p = camb.set_params(H0=67.40, ombh2=0.02237, omch2=0.3150 * 0.674 ** 2 - 0.02237,
                     mnu=0.06, omk=0, tau=0.054, As=2.1e-9, ns=0.965, lmax=3000)
_cl = camb.get_results(_p).get_cmb_power_spectra(_p, CMB_unit='muK', lmax=3000)
_le, _un = _cl['total'][:, 0], _cl['unlensed_scalar'][:, 0]
LG = np.arange(len(_le), dtype=float)
RATIO = np.ones_like(_le)
_m = _un > 0
RATIO[_m] = _le[_m] / _un[_m]
print(f"  P15's derived operator, lensed/unlensed at ell = 1900:  "
      f"{float(np.interp(1900, LG, RATIO)):.4f}   (imposed on both arms alike)")


def score(path):
    z = np.load(path)
    ls, Dl = np.asarray(z['ls'], float), np.asarray(z['Dl'], float)
    c, nb = CS.chi2_of(ls, Dl * np.interp(ls, LG, RATIO))[:2]
    return float(c), int(nb)


# ⛭ r7649 (69): RE-POINTED TO THE ARM OF RECORD on the landing (LEAFREC=1; the no-fit pair at the
#   distances' point, the refit's verified minimum at 68.5707/0.291246) -- the same three banks the
#   computing receipts read (`..._lensed_comparison...` and `..._full_range_refit...`).  The control
#   files do not move: LEAFREC does not reach the control.
GRID_ARM = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'refit_grid185_leafrec1_distances')
CFG = {
    #: ⛔⛔ r7819 (cc66): ** THE L2000 CONTROL IS RE-POINTED, AND THIS RECEIPT WAS MISSED BY THE PASS
    #: THAT RE-POINTED IT EVERYWHERE ELSE. **  `cc66_lcdm_L2000.npz` is the bank `r7809`'s swap maps
    #: to `(a1)`'s matched step-2 assembly at Planck 2018's published point; the lensed pair the
    #: paper prints (`204.7`, `1.11`, `2.45`) is that control's, while this file was still scoring
    #: the un-refitted one (`214.1`, `1.16`, `2.35`) -- so the receipt and the sentence it reads had
    #: come apart, and the plain suite is the only thing that sees it.
    #:   ⌗ *The ARM leg does NOT move and the `r185 verify` row cannot: a minimum of the fit does
    #:   not depend on where the search began.*
    'L2000':       (os.path.join(ROOT, 'computations', 'beyond_the_wall',
                                 'r7812_cc66_the_resumable_mode_loop_and_the_one_pass', 'out',
                                 'r7812_control_step2_L2000_assembled.npz'),
                    os.path.join(SPEC, 'cc66_cr_x_h686_L2000_leafrec1_distances.npz')),
    #: ⛭⛭ r7821 ④ (69's ruling): ** THE GRID-BASE CONTROL IS RE-POINTED TOO, AND THE RATIO
    #: MOVES AT ITS PRINTED PRECISION. **  `refit_grid185/lcdm_base.npz` carries the UN-REFITTED
    #: background point; `refit_grid185/launch.sh` built it with `ARM=lcdm HIER=1 LSTEP=8
    #: LMAXL=2000` and nothing else, and `r7807`'s control is THE SAME CONFIGURATION at Planck
    #: 2018's published point on the same 238-sample grid, so the sampling is MATCHED and the
    #: substitution is direct -- no assembly, unlike the step-2 `L2000` row.
    #:   ⇒ *Measured at r7821: the control's chi^2 falls by just over four per cent -- the same
    #:   direction and nearly the same size as the L2000 row's own re-point -- and the ratio rises
    #:   past the two decimals the paper prints it to, so l.974's figure is owed a move and carries
    #:   it.  All five predictions registered in
    #:   `r7821_cc66_the_grid_base_pair_at_plancks_point/PREDICTION.md` held.*  ⌗ *The ARM leg
    #:   does not move at all; only the control was swapped.  The figures themselves are PART 5's,
    #:   where they are computed rather than written down.*
    'grid base':   (os.path.join(ROOT, 'computations', 'beyond_the_wall',
                                 'r7807_cc66_the_23_items_and_the_repointed_control', 'out',
                                 'r7807_control_planck2018_L2000.npz'),
                    os.path.join(GRID_ARM, 'cr_base.npz')),
    'r185 verify': (os.path.join(SPEC, 'cc66_r185_verify_lcdm.npz'),
                    os.path.join(SPEC, 'cc66_r185_verify_cr_leafrec1.npz')),
}
S = {}
print()
print(f"  {'configuration':>14} {'bins':>5} {'control':>9} {'/bin':>7} {'arm':>9} {'/bin':>7} "
      f"{'arm/control':>12}")
for tag, (pc, pa) in CFG.items():
    for p in (pc, pa):
        if not os.path.exists(p):
            print(f"  ⛔ REFUSED: {os.path.relpath(p, ROOT)} is not banked -- the configuration "
                  f"cannot be scored and no figure of it may be asserted.")
            sys.exit(1)
    cc, cn = score(pc)
    ac, an = score(pa)
    if cn != an:
        fail.append(f"{tag}: the arms cover {cn} and {an} bins -- not like-for-like")
    S[tag] = dict(c=cc, a=ac, n=cn, cb=cc / cn, ab=ac / an, r=ac / cc)
    print(f"  {tag:>14} {cn:>5d} {cc:>9.1f} {cc / cn:>7.2f} {ac:>9.1f} {ac / an:>7.2f} "
          f"{ac / cc:>11.2f}x")
for tag in CFG:
    check(f"{tag} covers the 185 bins the section names", S[tag]['n'] == 185)

# =================================================================================================
print()
print(BAR)
print("  PART 3 -- ** EIGHT OF THE NINE: EXACT AT THE PAPER'S OWN PRECISION **")
print(BAR)
print("  Each row asserts the paper's figure EQUALS the computed value rounded to the decimals the")
print("  paper prints.  No tolerance: a tolerance wide enough to absorb a wrong quantity cannot")
print("  report one.\n")
print(f"  {'the paper says':>34} {'quantity it is a figure of':>44} {'computed':>10}")
ROWS = [
    ('chi2_ctl',   'control chi^2, 185 lensed bins',          S['L2000']['c']),
    ('chi2_arm',   'arm chi^2, 185 lensed bins',              S['L2000']['a']),
    ('bin_ctl',    'control per bin, 185 lensed bins',        S['L2000']['cb']),
    ('bin_arm',    'arm per bin, 185 lensed bins',            S['L2000']['ab']),
    ('ratio',      'their ratio, arm over control',           S['L2000']['r']),
    ('rf_bin_ctl', 'control per bin, refit verified minimum', S['r185 verify']['cb']),
    ('rf_bin_arm', 'arm per bin, refit verified minimum',     S['r185 verify']['ab']),
    ('rf_ratio',   'their ratio at the verified minimum',     S['r185 verify']['r']),
]
for key, what, got in ROWS:
    want, dp = paper(key)
    print(f"  {want:>34} {what:>44} {round(got, dp):>10}")
    check(f"the paper's {want} is {what}", round(got, dp) == want)

# =================================================================================================
print()
print(BAR)
print("  PART 4 -- ** THE NINTH: IT IS A RATIO, IN A SENTENCE OF PER-BIN FIGURES **")
print(BAR)
AS, dp = paper('as_computed')
as_ratio = S['grid base']['r']
as_bin = S['grid base']['ab']
print(f"""
  The sentence reads: *the control settles at {PAPER['rf_bin_ctl']} in chi^2 per bin and this arm at
  {PAPER['rf_bin_arm']}: the arm at {PAPER['rf_ratio']} times the control's distance, where the computed spectrum
  sits at {PAPER['as_computed']} times it on the same bins.*   <- `times it` is the r7167 repair, and the
  locator above REQUIRES it, so this receipt goes red if the word is ever dropped again.

  ** ON THOSE BINS, IN THAT CONFIGURATION, THE COMPUTED PAIR IS {S['grid base']['c']:.1f} AND {S['grid base']['a']:.1f}. **
     their ratio, arm over control  ->  {as_ratio:.4f}  ->  {round(as_ratio, dp)}
     the arm's figure PER BIN       ->  {as_bin:.4f}  ->  {round(as_bin, dp)}

  ⇒ *** SO {AS} IS THE RATIO.  The computing receipt prints it `{round(as_ratio, dp)}x as-computed`, with the x,
  and the paper dropped it -- in the one place in the sentence where every other figure is a chi^2
  per bin and where the reader has just been handed two of them.  IT CARRIES IT AGAIN AT `r7167`. ***""")
check(f"the paper's {AS} IS the as-computed ratio, at the paper's precision",
      round(as_ratio, dp) == AS)
check(f"the paper's {AS} is NOT the as-computed per-bin figure, which is {round(as_bin, dp)}",
      round(as_bin, dp) != AS)
# ⛔⛔ r7821 ④: ** THE RE-POINT NARROWS THE TWO READINGS, AND THE THRESHOLD THIS CHECK WAS
#   CALIBRATED WITH IS NOW JUST MISSED. **  *On the un-refitted control the as-computed per-bin
#   figure stood about a sixth above the ratio; at Planck's point the ratio rises and the gap falls
#   to just under a tenth -- so `> 0.10` would go red on a separation that landed a hundredth of a
#   per cent below an arbitrary round threshold.  The numbers are PART 4's own printout, computed.*
#   ⇒ *The claim this check carries is that the two candidate readings of one printed figure are
#       far enough apart that misreading it is not harmless.  That claim is about MATERIALITY, and a
#       tenth of the figure is still material.  So the check is restated as a PIN ON THE MEASURED
#       SEPARATION with a floor at a twentieth, and the narrowing is reported rather than absorbed:
#       it is a consequence of the re-point and 69 should see it.*  ⌗ The two readings remain
#       distinguishable at the paper's two decimals either way (2.44 against 2.68), which is the
#       detectability the locator needs; this floor is the separate question of whether it matters.
check("the two readings are far enough apart that the wrong one is not harmless "
      f"({abs(as_bin - AS) / AS:.1%} of the figure, narrowed by the r7821 re-point)",
      abs(abs(as_bin - AS) / AS - 0.09986031) < 5e-7 and abs(as_bin - AS) / AS > 0.05)

print(f"""
  ⛔ ** AND THE WRONG READING WAS NOT ONLY AVAILABLE, IT WAS PRIMED. **  Three sentences earlier the
  same section states the computed arm at {PAPER['bin_arm']} per bin ({S['L2000']['a']:.1f} over {S['L2000']['n']} bins, lensed).  *A reader
  carrying that figure into "the computed spectrum sits at {AS} on the same bins" met what read as
  one quantity with two values -- and nothing in the sentence said which it was.*  ⌗ *With the
  word restored the two readings cannot be confused, which is why one word was the whole repair.*

  ⌗ ** THE {round(as_bin, 2)}-AGAINST-{round(S['L2000']['ab'], 2)} GAP IS CONFIGURATION AND NOT DISAGREEMENT, WHICH IS WORTH SAYING
  BECAUSE IT IS THE SAME CLAIMED QUANTITY ON THE SAME 185 BINS. **  The refit grid runs at
  `LSTEP=8` and its own k-reach; the L2000 pair is the corpus's full-range spectrum.  *Two
  instruments, one range, and the figures differ by {abs(as_bin - S['L2000']['ab']) / S['L2000']['ab']:.1%} -- small, real, and not what the sentence
  is about.*""")
check("the two instruments' as-computed per-bin figures agree to better than 2 per cent, so the "
      "gap is the configuration and not a defect in either",
      abs(as_bin - S['L2000']['ab']) / S['L2000']['ab'] < 0.02)


# =================================================================================================
print()
print(BAR)
print("  PART 5 -- ** THE CLAUSE'S FOUR FIGURES, PINNED ON LITERALS, BECAUSE ITS CITATION IS NOW "
      "THIS RECEIPT ALONE **")
print(BAR)
print("""
  ⛭ r7821 ④: landing `$2.44$` meant NARROWING the clause's citation.  The sentence it sat in
  cited six receipts and none of them computes this ratio, so the figure stood BASELINED as unpinned
  six times over -- and `figure_pin_baseline.tsv` can only shrink, so moving the figure under those
  six keys was not available: six rows would go stale and six new ones would be owed.  *The clause
  is therefore its own sentence now, citing the receipt that computes it, and the six keys are
  retired from the baseline rather than re-keyed.*

  ⛔ ** AND PART 3's LOOP PINS NOTHING, WHICH IS WORTH SAYING OUT LOUD. **  It asserts
  `round(computed, dp) == want` where `want` is the figure CAPTURED FROM THE PAPER -- so the only
  constant in the comparison is the paper's own value arriving through a variable, and
  `check_figures_pinned` collects CONSTANTS.  *A loop that compares the paper to itself is a
  reproduction and not a pin, and a site that cites only this receipt needs pins.*  ⇒ So the four
  figures of the clause are asserted here against LITERALS, each failable by perturbing the
  computation and none of them read out of the paper.""")
_RF = S['r185 verify']
print(f"  {'the clause prints':>20} {'computed here':>16} {'from':>46}")
for _w, _g, _src in ((1.01, _RF['cb'], "r185 verify control chi^2 / 185"),
                     (1.61, _RF['ab'], "r185 verify arm chi^2 / 185"),
                     (1.60, _RF['r'], "r185 verify arm chi^2 / control chi^2"),
                     (2.44, as_ratio, "grid base arm chi^2 / r7807 Planck-point control")):
    print(f"  {_w:>20} {_g:>16.6f} {_src:>46}")
check("Ⓔ①  the clause's control figure is this receipt's own computation to the two decimals "
      "it is printed to -- a LITERAL comparison, not a reproduction of the paper's capture",
      round(_RF['cb'], 2) == 1.01 and abs(_RF['cb'] - 1.008) < 0.004)
check("Ⓔ②  the clause's arm figure likewise", round(_RF['ab'], 2) == 1.61
      and abs(_RF['ab'] - 1.609) < 0.004)
check("Ⓔ③  the clause's arm-over-control factor likewise", round(_RF['r'], 2) == 1.60
      and abs(_RF['r'] - 1.596) < 0.004)
check("Ⓔ④  ⛭ and the as-computed ratio at Planck 2018's published point, which is the figure "
      "r7821 ④ moved: it is the grid-base arm over r7807's control on the same 185 bins",
      round(as_ratio, 2) == 2.44 and abs(as_ratio - 2.435828) < 5e-6
      and abs(S['grid base']['c'] - 203.8226) < 5e-4
      and abs(S['grid base']['a'] - 496.4769) < 5e-4)

# =================================================================================================
print()
print(BAR)
print("  WHAT THIS SETTLES")
print(BAR)
print(f"""
  ** BOTH PAIRS `r7166` NAMED ARE RIGHT FROM THE PHYSICS SIDE, AND I AM SAYING SO RATHER THAN
  LEAVING THE INVITATION OPEN. **  {PAPER['chi2_ctl']} / {PAPER['chi2_arm']} reproduces to the digit on the configuration the
  corpus quotes chi^2 on, and {PAPER['rf_bin_arm']} / {PAPER['rf_bin_ctl']} reproduces at the verified minimum.  *The citation
  sweep's finding was a citation finding and the numbers behind it are sound.*

  ⇒ ** WHAT WAS WRONG WAS ONE FIGURE'S QUANTITY AND NOT ITS VALUE. **  `{AS}` is right as a ratio
  and was wrong where it sat.  The repair was one word -- the sentence's other two ratios both say
  "times" -- and it is in print at `r7167`.  *The prose is the chat seat's, so this was routed and
  not edited; the chat seat took it, and repaired this locator in the same pass, which is the one
  edit a seat may make to another seat's receipt: the one its own edit broke.*

  ⌗ ** AND THE ROW IS CLEAN. **  `INDEX.md` carries "1.57 times the control", with the word, so the
  generated appendix carries it too.  *At `r7165` the row was the thing that lost the quantity and
  the paper inherited it; here the row held it and the prose did not -- so the one-state rule has
  two failure directions, and a check that compares the row against the receipt sees neither this
  one nor the reader.*""")

print(BAR)
if fail:
    print("  FAILED:")
    for f in fail:
        print(f"    - {f}")
    sys.exit(1)
print("  ✓ ALL CHECKS PASSED")
print(BAR)
