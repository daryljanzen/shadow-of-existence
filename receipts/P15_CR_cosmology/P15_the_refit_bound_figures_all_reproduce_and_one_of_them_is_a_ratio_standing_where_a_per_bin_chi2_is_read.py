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
bins", and this receipt's own locator requires the word. **  *So the finding stands as a finding and
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
  for the full-range lensed pair; `refit_grid185/{cr,lcdm}_base` for the refit's as-computed pair;
  `spectra/cc66_r185_verify_{cr,lcdm}` for its verified minimum.  Nothing is re-solved and no fit is
  re-run -- the scoring is `chi2_of_spectrum`'s, with P15's own CAMB lensing operator imposed on
  both arms alike so it cannot favour either.

  ** AND THE COMPARISON IS EXACT AT THE PAPER'S OWN PRECISION, NOT INSIDE A TOLERANCE. **  Each
  figure must equal the computed value ROUNDED to the number of decimals the paper prints.  *A
  tolerance wide enough to absorb a wrong quantity is a tolerance that cannot report one.*

** COMPUTES: the nine quoted figures of `sec:refit-bound`'s two chi^2 pairs, each against the
   configuration it is a figure of; the identification of which quantity the paper's 2.56 is; and
   the 2.95-against-2.98 gap between the two instruments that both call their range "185 bins,
   ell = 100-1996", shown to be configuration and not disagreement. ***

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


CFG = {
    'L2000':       (os.path.join(SPEC, 'cc66_lcdm_L2000.npz'),
                    os.path.join(SPEC, 'cc66_cr_x_h686_L2000.npz')),
    'grid base':   (os.path.join(GRID, 'lcdm_base.npz'), os.path.join(GRID, 'cr_base.npz')),
    'r185 verify': (os.path.join(SPEC, 'cc66_r185_verify_lcdm.npz'),
                    os.path.join(SPEC, 'cc66_r185_verify_cr.npz')),
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
check("the two readings are far enough apart that the wrong one is not harmless "
      f"({abs(as_bin - AS) / AS:.1%} of the figure)", abs(as_bin - AS) / AS > 0.10)

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
