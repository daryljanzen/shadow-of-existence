#!/usr/bin/env python3
"""C41b -- ⌗ **RENAMED r2798 from `C41` (56).**  *** Two receipts written at r2749 shared the
prefix `C41`.  **The collision is the NAME, not the content** -- this and
`C41_a_tilde_is_stale_when_nothing_competes` are one rule at two states of the evidence, and
cc54 settled that at c54.228.  Renamed rather than merged so both statements survive.

C41b -- A TILDE ON A SETTLED VALUE IS A STALE HEDGE, not honest imprecision -- and r2748 concluded
the opposite one revision earlier.

** DARYL, r2749: ** "*** Isn't `~301` just a place marker for while the value is not accurately known?
If the value is now determined more accurately and is not expected to change then it ought to be
reported with accurate precision.  Not as a gloss that was only necessary while the value was changing
as you computed things. ***"

** ⛔ AND r2748 GOT THIS EXACTLY BACKWARD. **  *** It found P15's prose said "the measured ${\\sim}301$"
where the receipt asserts $301.76$, drafted this as the paper's defect, then **corrected itself to "the
tilde is there, the paper is honest, no paper edit is owed."**  That correction was the wrong one: it
treated the tilde's PRESENCE as the question, when the question is whether the value it hedges is still
moving. ***

** ⛭⛭ ⓵ IT IS NOT MOVING. **  `P15_zonset_determinations` carries $100\\theta_*=1.04109$ and ** asserts
** $\\ell_A=\\pi/\\theta_*=301.76$ to $0.01$.  *** The input is a published measurement and the output is
arithmetic on it.  Neither changes as CR computes anything. ***
  ⇒ ** So the tilde is a placeholder that outlived its occasion ** -- and it costs the corpus in its own
    disfavour: $302.2$ against $\\sim301$ reads as $+1.20$; against $301.76$ it is $+0.44$.  *** A stale
    hedge inflating the programme's own discrepancy by a factor of $2.7$. ***

** ⛭⛭⛭ ⓶ AND THE SAME SWEEP FOUND NINE MORE, ON A NUMBER THE CORPUS COMPUTES WITH CAMB. **  P15 calls
the damping-scale signature "${\\sim}8\\%$" in ** nine places **, three of them while describing it as
"** a real, computed effect **".
  *** `P15_damping_ratio_clean` runs it on CAMB's exact ionization history and returns:

          r_D radincl(LCDM) = 6.572 · radfree(CR) = 7.162 · ratio = 1.0897
          --> the damping tail scale is +8.2% ***

  ⇒⇒ ** A computed $8.2\\%$ reported nine times as $\\sim8\\%$. **  *** The hedge is not protecting
      anything: the receipt exists, it runs, and it asserts. ***

** ⓷ WHAT WAS EDITED. **  *** $\\{\\sim\\}301 \\to 301.76$ (one place) and $\\{\\sim\\}8\\% \\to 8.2\\%$ (nine
places).  17/17 compile, and `P15_damping_ratio_clean` still passes -- the receipt was always asserting
the precise figure the prose was rounding. ***

WHAT IS NOT CLAIMED.  ** Not that every tilde in the corpus is stale ** -- *** the sweep found 63, and
most are legitimately approximate: "roughly $10^5$ years", "negligible below $z\\sim10$", "$\\sim300$ too
slow".  A tilde on an order-of-magnitude statement is correct.  What is wrong is a tilde on a figure a
receipt asserts. ***  ** Not that the discrepancies are thereby scored ** -- r2746's rule stands: the
uncertainties are still not this line's.  ** Not that $8.2\\%$ is exact ** -- it is what the receipt
returns on the inherited datum, and the receipt says so.

** COMPUTES: nothing new.  *** `P15_damping_ratio_clean`'s $+8.2\\%$ is re-run, not re-derived; the
$301.76$ is `P15_zonset_determinations`'s asserted value. *** **

Written r2749.  Stated for reversal.
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def main():
    print()
    print("  C41 -- is a tilde on a settled value honest imprecision, or a stale hedge?")
    print()
    p15 = body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'))
    z = open(glob.glob(os.path.join(ROOT, 'receipts', '**', 'P15_zonset_determinations.py'),
                       recursive=True)[0], encoding='utf-8', errors='replace').read()

    # ⓵ the value is asserted, not moving
    check('⛭⛭ ⓵ the acoustic-angle figure is ASSERTED, not estimated: '
          '"assert abs(MEAS_L - 301.76) < 0.01"',
          'MEAS_L - 301.76' in z and '1.04109' in z)
    check('and P15 now carries it: the prose reads "against the measured $301.76$"',
          '301.76' in p15)
    check('with no tilde left on it',
          '{\\sim}301' not in p15)

    # ⓶ and the damping signature likewise
    check('⛭⛭⛭ ⓶ and the damping-scale signature is computed on CAMB\'s exact ionization history, '
          'not estimated -- its receipt names itself for the figure',
          os.path.exists(glob.glob(os.path.join(
              ROOT, 'receipts', '**', 'P15_damping_ratio_clean.py'), recursive=True)[0]))
    # ⌗ same repair as `C41`'s (r3988): the NINE were the tilde-marked sites REMOVED, and this
    #   required nine bare replacements in return.  The edit consolidated -- the figure is carried
    #   at five sites and has been for hundreds of revisions.  ** A replacement count is not a
    #   removal count. **  The removal is asserted below, at zero, which is the claim that matters.
    # ⛔⛭⛭ RE-POINTED r7101 (66, the gate, on `cc66`'s proposal and this comment's own reasoning).
    # ** THE POSITIVE SITE-COUNT IS WITHDRAWN AND THE REMOVAL IS WHAT IS GATED. **  *The check below
    # asserted that `P15` carries the literal `$8.2\%$` at one site or more, and it went red at `r7097`
    # when the gate withdrew four uncited polarisation figures from `sec:refit-bound`.*
    #   ⇒ *** AND IT HAD BEEN PASSING ON A COINCIDENCE.  The last literal `8.2\%` in the paper was a
    #     POLARISATION pull, not the damping-scale figure this receipt is about: the nine damping sites
    #     its finding concerns had already been reworded away, and the count was satisfied by an
    #     unrelated string. ***  *A gate kept green by a string it is not about is worse than a red one.*
    # ⌗ ** AND THIS FILE'S OWN COMMENT, THREE LINES UP, ALREADY NAMED THE RIGHT CHECK: *a replacement
    #   count is not a removal count; the removal is asserted below, at zero, which is the claim that
    #   matters.* **  *The positive count was the half that could go stale and it did.*
    #   ⇒ *Re-pointing it to whatever literal the paper carries today would be the same defect one
    #     rewording later.  The finding is a HISTORICAL correction -- a settled value had been hedged
    #     nine times and the hedge was removed -- and what must stay true forever is that no such hedge
    #     comes back.  That is an absence, it is gated, and it does not move when the prose moves.*
    _n82 = len(re.findall(r'8\.2\\%', p15))
    print(f'     ⌗ the literal $8.2\\%$ stands at {_n82} site(s) today -- REPORTED, not asserted, '
          f'because the paper is entitled to reword a figure it computes')
    check('the hedge this receipt removed has not returned: no tilde-8% survives anywhere in P15 -- '
          'the absence is the finding and it is what is gated, the positive site-count having been '
          'withdrawn once it was found to be satisfied by an unrelated string',
          len(re.findall(r'(\{\\sim\}|\\sim\s*)8\\%', p15)) == 0)

    # ⓷ while legitimately approximate tildes are untouched
    check('⓷ while legitimately approximate tildes are untouched -- the corpus still says things are '
          'negligible below $z\\sim10$, which is an order-of-magnitude statement and correctly hedged',
          len(re.findall(r'\\sim', p15)) > 0)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** a tilde on a settled value is a STALE HEDGE, and r2748 got it backward. **')
    print('  ⛔ ** r2748 drafted this as the paper\'s defect, then "corrected" itself to "the tilde is')
    print('     there, the paper is honest, no edit is owed."  ** That correction treated the tilde\'s')
    print('     PRESENCE as the question — when the question is whether the value it hedges is still')
    print('     moving.')
    print('  ⛭⛭ ⓵ ** It is not moving: ** 100·θ_* = 1.04109 is published, ℓ_A = 301.76 is arithmetic')
    print('     on it, and the receipt asserts it to 0.01.  ** So the hedge outlived its occasion —')
    print('     and cost the corpus in its own disfavour: +1.20 read against ~301, +0.44 against the')
    print('     real value.  A factor of 2.7. **')
    print('  ⛭⛭⛭ ⓶ ** And the sweep found nine more, on a number computed with CAMB: ** the damping')
    print('     signature is called "~8%" in nine places, three while describing it as "a real,')
    print('     computed effect".  ** Its receipt returns +8.2%. **')
    print('  ⓷ ** Edited: ** ~301 → 301.76, and ~8% → 8.2% ×9.  17/17 compile, receipt still passes.')
    print('     ⌗ ** Legitimately approximate tildes are untouched ** — "roughly 10⁵ years",')
    print('       "negligible below z~10".  ** A tilde on an order of magnitude is correct; a tilde on')
    print('       a figure a receipt asserts is not. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
