#!/usr/bin/env python3
"""C18 -- what "bespoke" means for `PO-12`, precisely: the transfer must carry TWO backgrounds joined at
the branch point, and the paper's own consistency rule forbids mixing them.

** THE QUESTION LEFT BY r2659. **  The debt is now "the background the instrument runs on" -- the
instrument is "the full ** flat-projection ** transfer" and the debt names "the ** radiation-free **
background", with "** the whole difference is carried by $H(a)$ **".  ⇒ ** Does that $H(a)$-only
difference hold for every source term, or only for the diffusion length where it was established? **

** ⚠ ⓵ AND THE FIRST ANSWER LOOKED LIKE A CONTRADICTION AND WAS NOT. **  `sec:envelope`'s driving is
$\\Phi''+(4/\\eta)\\Phi'+(k^2/3)\\Phi=0$, and $4/\\eta$ is the ** radiation-dominated ** friction
($a\\sim\\eta$); on a matter-dominated background it would be $8/\\eta$.  *** So the perturbation sector
appeared to assume radiation while the debt asks for a radiation-free background. ***
  ⇒ ** It does not.  The paper scopes it in the same sentence: ** "** On the radiation-dominated collapse
    leg ** the potential obeys ..."  *** The collapse leg IS radiation-dominated -- it is the prior
    universe's contraction, heating into the hot handover. ***

** ⛭⛭ ⓶ THE TWO LEGS CARRY DIFFERENT CONTENT BY CONSTRUCTION. **  P15: "there the self-gravitating
excursion sets ** the L2 rate radiation is included in **, here ** the diffuse plasma rides the L1
foliation radiation is excluded from **."

  ⇒⇒ *** So the transfer is not one background with a modified $H(a)$.  It is TWO: a radiation-dominated
      collapse leg supplying the driving in closed form, joined at the branch point to a radiation-free
      expansion leg carrying the observable history.  THAT is what "bespoke" names. ***

** ⛭ ⓷ AND THE PAPER STATES THE CONSISTENCY RULE THE TRANSFER MUST OBEY. **  "This is forced: it is the
same L1 rate that dissolves the Hubble tension, and ** one may not take the rate radiation-free for the
peak spacing and radiation-included for the diffusion **."
  ⌗ *** That is a constraint ON the transfer, stated before the transfer exists: whatever it computes, the
      rate must be the SAME rate for every observable on the expansion leg.  A flat-projection instrument
      run at one background satisfies it trivially and answers a different question. ***

** ⇒ ⓸ SO `PO-12`'s DEBT, AT ITS SHARPEST. **  *** Not "build a transfer" -- one exists and is validated.
Not "swap $H(a)$" -- that understates it.  It is: run the existing hierarchy across a TWO-LEG background
joined at the branch point, with the L1 rate on the expansion leg for every observable at once. ***
  ⌗ ** And the pieces for both legs are separately in hand: ** the closed-form driving on the collapse leg
  (`sec:envelope`, verified r2658), the radiation-free rate and its consequences on the expansion leg
  ($r_s$, the diffusion length, $\\ell_*$).

WHAT IS NOT CLAIMED.  ** Not that the join is straightforward ** -- *** the matching at the branch point
is where a two-leg transfer would be hardest, and nothing here addresses it. ***  ** Not that the
$H(a)$-only statement is wrong ** -- it is exact for the diffusion-length ratio, where the microphysics
cancels; *** what this shows is that it describes a ratio ON one leg and not the two-leg structure. ***
** Not that the instrument is inadequate ** -- it is validated for what it does.

Written r2660.  Stated for reversal.
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
    check('⛭⛭ ⓶ and the two legs carry different content: "there the self-gravitating excursion sets the '
          'L2 rate radiation is included in, here the diffuse plasma rides the L1 foliation radiation is '
          'excluded from"',
          'the L2 rate radiation is included in' in p15
          and 'the L1 foliation radiation is excluded from' in p15)

    # ⓷ the consistency rule
    check('⛭ ⓷ and the paper states the rule the transfer must obey: "one may not take the rate '
          'radiation-free for the peak spacing and radiation-included for the diffusion"',
          'one may not take the rate radiation-free for the peak spacing and radiation-included for the '
          'diffusion' in p15)
    check('calling it forced: "This is forced: it is the same L1 rate that dissolves the Hubble tension"',
          'This is forced: it is the same L1 rate that dissolves the Hubble tension' in p15)

    # ⓸ the instrument is single-background
    check('⓸ while the instrument is described as single-background: "The full flat-projection transfer"',
          'The full flat-projection transfer' in p15)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** "bespoke" means TWO backgrounds joined at the branch point. **')
    print('  ⚠ ⓵ ** The driving\'s 4/eta friction is the RADIATION-dominated coefficient ** (8/eta for')
    print('     matter) -- ** which looked like the perturbation sector assuming radiation while the debt')
    print('     asks for a radiation-free background. **  *** It is not: the paper scopes it in the same')
    print('     sentence -- "ON THE RADIATION-DOMINATED COLLAPSE LEG". ***')
    print('  ⛭⛭ ⓶ ** The two legs carry different content BY CONSTRUCTION: ** "the self-gravitating')
    print('     excursion sets the L2 rate ** radiation is included in **" against "the diffuse plasma')
    print('     rides the L1 foliation ** radiation is excluded from **".')
    print('  ⛭ ⓷ ** And the paper states the rule a transfer must obey, before the transfer exists: **')
    print('     "** one may not take the rate radiation-free for the peak spacing and radiation-included')
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
