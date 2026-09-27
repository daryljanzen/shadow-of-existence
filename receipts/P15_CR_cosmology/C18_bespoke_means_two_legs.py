#!/usr/bin/env python3
"""C18 -- what "bespoke" means for `PO-12`, precisely: the transfer must carry TWO backgrounds joined at
the branch point, and the paper's own consistency rule forbids mixing them.

** THE QUESTION LEFT BY r2659. **  The debt is now "the background the instrument runs on" -- the
instrument is "the full ** flat-projection ** transfer" and the debt names "the ** geometric stacking **
background", with "** the whole difference is carried by $H(a)$ **".  ⇒ ** Does that $H(a)$-only
difference hold for every source term, or only for the diffusion length where it was established? **

** ⚠ ⓵ AND THE FIRST ANSWER LOOKED LIKE A CONTRADICTION AND WAS NOT. **  `sec:envelope`'s driving is
$\\Phi''+(4/\\eta)\\Phi'+(k^2/3)\\Phi=0$, and $4/\\eta$ is the ** radiation-dominated ** friction
($a\\sim\\eta$); on a matter-dominated background it would be $8/\\eta$.  *** So the perturbation sector
appeared to assume radiation while the debt asks for a geometric stacking background. ***
  ⇒ ** It does not.  The paper scopes it in the same sentence: ** "** On the radiation-dominated collapse
    leg ** the potential obeys ..."  *** The collapse leg IS radiation-dominated -- it is the prior
    universe's contraction, heating into the hot handover. ***

** ⛭⛭ ⓶ THE TWO LEGS CARRY DIFFERENT CONTENT BY CONSTRUCTION. **  P15: "there the self-gravitating
excursion sets ** the L2 rate radiation is included in **, here ** the diffuse plasma rides the L1
foliation radiation is excluded from **."

  ⇒⇒ *** So the transfer is not one background with a modified $H(a)$.  It is TWO: a radiation-dominated
      collapse leg supplying the driving in closed form, joined at the branch point to a geometric stacking
      expansion leg carrying the observable history.  THAT is what "bespoke" names. ***

** ⛭ ⓷ AND THE PAPER STATES THE CONSISTENCY RULE THE TRANSFER MUST OBEY. **  "This is forced: it is the
same L1 rate that dissolves the Hubble tension, and ** one may not take the rate geometric stacking for the
peak spacing and radiation-included for the diffusion **."
  ⌗ *** That is a constraint ON the transfer, stated before the transfer exists: whatever it computes, the
      rate must be the SAME rate for every observable on the expansion leg.  A flat-projection instrument
      run at one background satisfies it trivially and answers a different question. ***

** ⇒ ⓸ SO `PO-12`'s DEBT, AT ITS SHARPEST. **  *** Not "build a transfer" -- one exists and is validated.
Not "swap $H(a)$" -- that understates it.  It is: run the existing hierarchy across a TWO-LEG background
joined at the branch point, with the L1 rate on the expansion leg for every observable at once. ***
  ⌗ ** And the pieces for both legs are separately in hand: ** the closed-form driving on the collapse leg
  (`sec:envelope`, verified r2658), the geometric stacking rate and its consequences on the expansion leg
  ($r_s$, the diffusion length, $\\ell_*$).

WHAT IS NOT CLAIMED.  ** Not that the join is straightforward ** -- *** the matching at the branch point
is where a two-leg transfer would be hardest, and nothing here addresses it. ***  ** Not that the
$H(a)$-only statement is wrong ** -- it is exact for the diffusion-length ratio, where the microphysics
cancels; *** what this shows is that it describes a ratio ON one leg and not the two-leg structure. ***
** Not that the instrument is inadequate ** -- it is validated for what it does.

Written r2660.  Stated for reversal.

** r6931+70.1 (PO-59) -- TWO OF THIS RECEIPT'S QUOTATIONS WERE CORRECTED BY THE CORPUS, AND ⓸ WITH THEM. **
*** ⓶'s "the diffuse plasma rides the L1 foliation radiation is excluded from" is gone (r6899, `1a2ab59c`):
the plasma's scales and the perturbations ride the LEAF rate, radiation included, the same side as the
nucleosynthesis window, and only the comoving distance rides the stacking rate.  ⓷'s "the same L1 rate
that dissolves the Hubble tension" is gone (r6772+66.25, `06459d04`): the construction leaves the ladder
discrepancy where the standard model leaves it. ***  So ⓸'s prescription -- "the L1 rate on the expansion
leg for every observable at once" -- is not the corpus's rule; the rule is the leaf for what the plasma
accumulates and the stacking rate for separations read across leaves, and the transfer was run that way
(r6719).  The friction-coefficient finding ⓵ and the consistency rule itself stand.
"""
import os
import re

import sympy as sp

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
    print('  C18 -- what does "bespoke" mean for PO-12?')
    print()
    p15 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')))

    # ⓵ the friction coefficient identifies the content
    eta = sp.symbols('eta', positive=True)
    rd = sp.simplify(4 * sp.diff(eta, eta) / eta)
    md = sp.simplify(4 * sp.diff(eta**2, eta) / eta**2)
    check(f'⓵ the driving friction $4a\'/a$ is {rd} for $a\\sim\\eta$ (radiation) and {md} for '
          '$a\\sim\\eta^{2}$ (matter)',
          rd == 4/eta and md == 8/eta)
    check("and sec:envelope uses $4/\\eta$, the radiation form: \"the potential obeys "
          "$\\Phi''+(4/\\eta)\\Phi'+(k^2/3)\\Phi=0$\"",
          "(4/\\eta)" in p15)
    check('⚠ which is NOT a contradiction, because the paper scopes it: "On the radiation-dominated '
          'collapse leg the potential obeys"',
          'On the radiation-dominated collapse leg the potential obeys' in p15)

    # ⓶ two legs, two contents
    # ** r6931+70.1 (PO-59): CLASS (a), THE PIN FROZE AN ASSIGNMENT THE CORPUS CORRECTED.  The sentence
    #    "here the diffuse plasma rides the L1 foliation radiation is excluded from" was rewritten at
    #    `1a2ab59c` (r6899, "the rate rule settled on the leaf"): the plasma accumulating its own scales
    #    takes the SAME leaf rate the nucleosynthesis excursion does, "the two windows fall on the
    #    same side of it rather than on opposite sides", and only the distance the angle is divided by
    #    rides the stacking rate.  *** So what this check asserted -- the expansion-leg plasma on the
    #    radiation-excluded rate -- is what the corpus now says is wrong; the check follows the
    #    correction.  The receipt's two-leg STRUCTURE survives (the leaf rate is radiation-included
    #    on both legs; what differs is only what is read off it), and its ⓸ prescription "the L1 rate
    #    on the expansion leg for every observable" does not. ***  Passed at r6502 (`b96e1a49`). **
    check('⛭⛭ ⓶ [corrected r6899] the two windows sit on the SAME rate, not different ones: "there the '
          'self-gravitating excursion sets the leaf rate radiation is included in, and here the plasma '
          'accumulating its own scales takes that same rate" -- "the two windows fall on the same side '
          'of it rather than on opposite sides"',
          'the L1 foliation radiation is excluded from' not in p15
          and 'there the self-gravitating excursion sets the leaf rate radiation is included in, and '
              'here the plasma accumulating its own scales takes that same rate' in p15
          and 'the two windows fall on the \\emph{same} side of it rather than on opposite sides' in p15)

    # ⓷ the consistency rule
    # ⛔⛭ RE-PINNED r3952 -- r3841's sweep, same cause as r3950's five.  The paper says "one may not take the rate GEOMETRIC for the peak spacing and
    #   radiation-included for the diffusion" -- a parallel construction (rate geometric vs
    #   radiation-included), and the sweep broke it by inserting a second word into one arm.
    check('⛭ ⓷ and the paper states the rule the transfer must obey: "one may not take the rate '
          'geometric stacking for the peak spacing and radiation-included for the diffusion"',
          'one may not take the rate geometric for the peak spacing and radiation-included for the '
          'diffusion' in p15)
    # ** r6931+70.1 (PO-59): CLASS (a).  "This is forced: it is the same L1 rate that dissolves the
    #    Hubble tension" was removed at `06459d04` (r6772+66.25, "the last seven statements of the
    #    dissolution cleared from P15"): P15 now states the construction does NOT dissolve the
    #    discrepancy with the local distance ladder, and the rule is "forced by consistency", its
    #    force being that the peak spacing is the LEAF accumulation, measured, so both lengths go on
    #    the leaf.  *** The rule is still called forced (the finding this check carried); what it is
    #    forced BY follows the correction. ***
    check('calling it forced -- [corrected r6772+66.25] by consistency and by the measured leaf '
          'accumulation, not by a Hubble-tension dissolution the paper no longer claims: "This is forced '
          'by consistency", "the peak spacing this construction computes is the leaf accumulation", and '
          '"this construction does not dissolve the discrepancy with the local distance ladder"',
          'This is forced: it is the same L1 rate that dissolves the Hubble tension' not in p15
          and 'This is forced by consistency: one may not take the rate geometric for the peak spacing '
              'and radiation-included for the diffusion' in p15
          and '\\emph{the peak spacing this construction computes is the leaf accumulation}' in p15
          and '\\emph{So this construction does not dissolve the discrepancy with the local distance '
              'ladder}' in p15)

    # ⓸ the instrument is single-background
    check('⓸ while the instrument is described as single-background: "The full flat-projection transfer"',
          'The full flat-projection transfer' in p15)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (r6931+70.1): ** CORRECTED IN PART -- the expansion-leg plasma rides the LEAF rate')
    print('     (r6899), not the L1 foliation, and the rule is forced by consistency, not by a Hubble-tension')
    print('     dissolution (r6772+66.25).  The transfer was run on that assignment (r6719).  The r2660')
    print('     finding as it stood, with ⓶ and ⓸ superseded: **')
    print('  ** "bespoke" means TWO backgrounds joined at the branch point. **')
    print('  ⚠ ⓵ ** The driving\'s 4/eta friction is the RADIATION-dominated coefficient ** (8/eta for')
    print('     matter) -- ** which looked like the perturbation sector assuming radiation while the debt')
    print('     asks for a geometric stacking background. **  *** It is not: the paper scopes it in the same')
    print('     sentence -- "ON THE RADIATION-DOMINATED COLLAPSE LEG". ***')
    print('  ⛭⛭ ⓶ ** The two legs carry different content BY CONSTRUCTION: ** "the self-gravitating')
    print('     excursion sets the L2 rate ** radiation is included in **" against "the diffuse plasma')
    print('     rides the L1 foliation ** radiation is excluded from **".')
    print('  ⛭ ⓷ ** And the paper states the rule a transfer must obey, before the transfer exists: **')
    print('     "** one may not take the rate geometric stacking for the peak spacing and radiation-included')
    print('     for the diffusion **" -- called ** forced **.')
    print('  ⇒⇒ ⓸ ** SO THE DEBT AT ITS SHARPEST: ** not "build a transfer" (one exists, validated), not')
    print('     "swap H(a)" (understates it), but ** run the existing hierarchy across a TWO-LEG')
    print('     background joined at the branch point, with the L1 rate on the expansion leg for every')
    print('     observable at once. **')
    print('  ⌗ ** And both legs\' pieces are separately in hand ** -- the closed-form driving on the')
    print('    collapse leg, and r_s, the diffusion length and l_* on the expansion leg.')
    print('  ⚠ ** The JOIN is where it would be hardest, and nothing here addresses it. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
