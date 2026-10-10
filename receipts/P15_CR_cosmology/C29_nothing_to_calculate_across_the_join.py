#!/usr/bin/env python3
"""C29 -- `PO-12`'s remaining half DISSOLVES: the pre-onset stretch is pressureless, its potential
equation contains no $k$, and the residue P15 names is `PO-7`'s question, not this row's.

** WHAT r2663 LEFT AND NOTHING HAS TOUCHED. **  "The acoustic evolution from the branch point to
recombination is what the instrument already runs; ** joining the two as a single calculation is unrun
**."  *** This row has carried that sentence for forty revisions. ***

** ⛭⛭ ⓵ AND P15 ANSWERS IT IN ITS OWN VOICE. **  "On the geometric stacking rate the crossing occurs under
pressureless matter to better than a part in $10^4$, and the potential equation for a pressureless
component, $\\Phi''+3\\mathcal H(1+w)\\Phi'+[2\\mathcal H'+(1+3w)\\mathcal H^2]\\Phi+wk^2\\Phi=0$, ** contains
no $k$ at all once $w=0$ **---the wavenumber enters only through the pressure term."

  ** Verified symbolically: ** setting $w=0$ leaves

      *** Phi'' + 3H Phi' + (H^2 + 2H') Phi = 0     ->  k ABSENT ***

  ⇒ *** Every mode's potential obeys the SAME equation on that stretch, whatever its wavenumber.  There
      is no scale-dependent evolution to compute, so there is nothing for a "single calculation across
      the join" to calculate. ***

** ⓶ AND THE GEOMETRY AGREES FROM BOTH ENDS. **
  * ** branch point: ** the comoving horizon $\\to0$, so ** every mode is outside ** (r2662).
  * ** onset: ** $k_{\\rm hor}=0.010$ Mpc$^{-1}$ against peaks at $0.022$ and above -- ** inside by a
    factor $2.2$ ** (`prop:subhorizon`).
  ⇒⇒ ** So every acoustic mode crosses in between them ** -- and P15 names the boundary mode,
  $k=0.0111$ Mpc$^{-1}$, $\\ell\\simeq144$: "** every mode at and above the acoustic peaks crossed before
  the plasma began **".  *** The crossing happens where there is no plasma to record it. ***

** ⓷ SO WHAT REMAINS IS NOT THIS ROW'S. **  P15 states the residue exactly: "the open question is now
sharp: ** on this rate nothing before the onset can imprint an acoustic phase **, so whatever sets it
must act on modes ** already inside the sound horizon when the plasma begins **."
  ⇒ *** That is the first peak's position -- `PO-7`'s question, and cc54's `L-812` held at the
      turnaround obstacle.  `PO-12`'s own remaining half is empty. ***

WHAT IS NOT CLAIMED.  ** Not that `PO-12` closes ** -- *** that is a verdict on a protected row and `F5`
reserves the strike; what is established is that the sentence this row has carried since r2663 names a
calculation with no content. ***  ** Not that the $10^{-4}$ is re-derived ** -- it is P15's, with its own
receipt.  ** Not that `PO-7` is thereby easier ** -- it inherits a sharper statement, not a smaller
problem.

Written r2701.  Stated for reversal.

** r6931+70.1 (PO-59) -- THIS RECEIPT'S FINDING WAS CORRECTED BY THE CORPUS. **  *** "Nothing to calculate
across the join" held on the stacking rate, where a pressureless stretch has no $k$.  r6772+66.9
(`c893df06`) put the re-entry on the rate the perturbations actually run on -- the leaf, radiation
included -- where it is an event and the modes above equality are driven, and states the pressureless
reading as the stacking rate's answer, which the perturbations do not take. ***  The calculation this
receipt called empty is the end-to-end transfer, run at r6719 (`440623b6`).  The $w=0$ algebra (⓵) and the
collapse-leg phase not crossing (⓷, second half) stand; ⓶'s onset-based census and "nothing is imprinted
there" do not.
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
    print("  C29 -- is there anything to calculate across the join?")
    print()
    p15 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')))

    # ⓵ the paper's clause
    # ** r6931+70.1 (PO-59): ALL FIVE PINS BELOW WENT AT ONE COMMIT, `c893df06` (r6772+66.9, "the re-entry
    #    argument on the rate the perturbations run on: the modes are driven, and the pressureless
    #    reading is what the rate rule closes").  *** That commit CORRECTS this receipt's finding. ***
    #    The w=0 algebra survives (and is verified below), but P15 now says it is "the stacking rate's
    #    answer, and the perturbations do not take it: they take the leaf's, which carries the radiation
    #    term and therefore the driving".  So the stretch this receipt called pressureless is, on the
    #    rate the perturbations run on, radiation-dominated for everything above l_eq ~ 144, re-entry
    #    there IS an event, and there WAS something to calculate across the join -- which the
    #    end-to-end transfer (r6719) and the closed-form driving of sec:envelope calculate.  The fitted
    #    onset these pins located the boundary against was retired as a repair (r6770+66.3).
    #    Receipt passed at r6502 (`b96e1a49`), failing from r6774.
    #
    #    ⓵a CLASS (c) for the algebra: the clause is reworded, "contains no $k$ at all once $w=0$}, so on
    #       a radiation-free rate the problem is scale-free" -- the same statement, now scoped to the
    #       rate on which it holds.  ⓵b CLASS (a): "the crossing occurs under pressureless matter" is
    #       what the corpus corrected; the check follows the correction. **
    check('⛭⛭ ⓵ P15: the potential equation for a pressureless component "contains no $k$ at all once '
          '$w=0$" -- now scoped: "so on a radiation-free rate the problem is scale-free"',
          '\\emph{contains no $k$ at all once $w=0$}, so on a radiation-free rate the problem is '
          'scale-free' in p15)
    check('[corrected r6772+66.9] but the stretch is NOT pressureless on the rate the perturbations run on: '
          '"That is the stacking rate\'s answer, and the perturbations do not take it: they take the '
          'leaf\'s, which carries the radiation term and therefore the driving"',
          'the crossing occurs under pressureless matter to better than a part in' not in p15
          and "That is the stacking rate's answer, and the perturbations do not take it: they take the "
              "leaf's, which carries the radiation term and therefore the driving" in p15)

    # verify it
    Phi = sp.Function('Phi')
    eta, k, w = sp.symbols('eta k w')
    H = sp.Function('H')
    eq = (sp.diff(Phi(eta), eta, 2) + 3*H(eta)*(1+w)*sp.diff(Phi(eta), eta)
          + (2*sp.diff(H(eta), eta) + (1+3*w)*H(eta)**2)*Phi(eta) + w*k**2*Phi(eta))
    check('and $k$ IS in the general equation, so the check is not vacuous', k in eq.free_symbols)
    check('while at $w=0$ it becomes $\\Phi\'\'+3\\mathcal H\\Phi\'+(\\mathcal H^2+2\\mathcal H\')\\Phi=0$ -- '
          '$k$ ABSENT',
          k not in sp.simplify(eq.subs(w, 0)).free_symbols)

    # ⓶ the two ends
    # ** r6931+70.1: ⓶ CLASS (a).  The boundary mode "whose crossing coincides with the onset" and "every
    #    mode ... crossed before the plasma began" were computed against the fitted onset and on the
    #    stacking rate (P15's own footnote then said the leaf moves the boundary and was not recomputed).
    #    With the plasma handed over at the branch point, every mode is outside the horizon at the
    #    handover and each re-enters on the expanding leg; on the leaf, everything above l_eq ~ 144 is
    #    driven.  The checks now pin that census, and the absence of the retired one. **
    check('⓶ [corrected r6772+66.9] the geometry, restated on the handover: every mode is outside at the '
          'branch point "so each re-enters on the expanding leg at its own time", and no boundary mode '
          '"coincides with the onset"',
          'the mode whose crossing coincides with the onset is' not in p15
          and 'so each re-enters on the expanding leg at its own time' in p15)
    # ⛔⛭ r6937 (66, on node 70's routed mis-citation): ** THE NUMBER THIS CHECK PINNED WAS THE WRONG
    #   BACKGROUND'S, AND PINNING IT FROZE THAT. **  156 is `ell_eq` for the ARM AS CODED at
    #   H0 = 73.00, Om = 0.3066 -- not for "the epoch the distance data fix", which is
    #   (68.60, 0.2973) and gives 143.5.  *Recomputed two ways at r6937, independently of the
    #   receipt that reports it: k_eq = a_eq H_leaf(a_eq)/c = 0.010245/Mpc on the leaf rate,
    #   projected by D_M = 14011 Mpc on the radiation-free stacking rate the distances take.*
    #   ⇒ *** The qualifier and the figure named two different backgrounds, so the paper moved to
    #   144 and this pin follows it. ***  ⌗ *The FINDING this check carries is the CENSUS -- driven
    #   at re-entry rather than "crossed before the plasma began" -- and that is unaffected either
    #   way, the first peak sitting above 144 as it sat above 156.  ** The number is pinned because
    #   a figure whose qualifier disagrees with it is exactly what went unread here for one
    #   revision. **
    check('with the modes above equality DRIVEN at re-entry rather than "crossed before the plasma began": '
          '"everything above $\\ell_{\\mathrm{eq}}\\simeq144$ at the epoch the distance data fix---are '
          'driven", the figure being the one that epoch actually gives',
          'crossed before the plasma began' not in p15
          and 'everything above $\\ell_{\\mathrm{eq}}\\simeq144$ at the epoch the distance data '
              'fix---are driven' in p15
          and '\\simeq156$ at the epoch the distance data fix' not in p15)

    # ⓷ the residue is PO-7's
    # ⛔⛭ RE-PINNED r3952 -- r3841's sweep, same cause as r3950's five.  ⛭ AND THIS ONE IS KIND ①, NOT ⑥: the SENTENCE was rewritten, not just the term.
    #   "nothing before the onset can imprint an acoustic phase" is now "** nothing is imprinted
    #   there, and the reason is STRUCTURAL RATHER THAN QUANTITATIVE **" -- the same claim, stated
    #   more strongly, so the pin moves to the new sentence's load-bearing fragment.
    # ** r6931+70.1: ⓷ CLASS (a) for its first half, (c) for its second.  "But nothing is imprinted
    #    there, and the reason is structural rather than quantitative" went at `c893df06`: on the leaf
    #    rate re-entry imprints the driving, so that clause is what the corpus corrected.  The half that
    #    survives is the one r3952 already found -- the collapse leg's oscillatory content does not
    #    cross ("the kernel annihilates it"), which "leaves the comb to be set on the expansion side".
    #    *** So the residue is still located on the expansion side, which is this check's finding; what
    #    changed is that the expansion side is now where the driving is computed, not an empty
    #    interval. ***
    check('⓷ and P15 states the residue: the collapse-leg phase does not cross -- "What does not cross is '
          'the oscillatory content itself", "the kernel annihilates it", which "leaves the comb to be set '
          'on the expansion side" -- [corrected r6772+66.9] where re-entry is driven, not "nothing is '
          'imprinted there"',
          'nothing is imprinted there' not in p15
          and 'What does not cross is the oscillatory content itself' in p15
          and 's sub-horizon earlier carries an oscillation, and the kernel annihilates it' in p15
          and 'it is what leaves the comb to be set on the expansion side' in p15)
    # ⌗ THE SECOND HALF NEEDED ITS OWN SEARCH.  The old tail -- "so whatever sets it must act on
    #   modes already inside the sound horizon when the plasma begins" -- runs ZERO times now, and
    #   dropping the conjunct would have quietly narrowed the check.  The claim SURVIVES, rewritten
    #   and sharper: "** What does not cross is the oscillatory content itself, and that is the
    #   collapse leg's acoustic phase: a mode that was sub-horizon earlier carries an oscillation,
    #   and THE KERNEL ANNIHILATES IT **."  Same physics -- the sub-horizon oscillation is what
    #   fails to cross -- stated as a mechanism rather than as a requirement on whatever sets it.
    #   ⇒ *** A conjunct whose phrase is gone is not a conjunct to delete.  Look for the claim
    #       first: deleting it would have made the receipt pass by asking less. ***

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT (r6931+70.1): ** CORRECTED -- on the leaf rate the perturbations run on, re-entry is")
    print("     DRIVEN for every mode above l_eq ~ 144 (r6772+66.9; the figure corrected r6937 -- 156")
    print("     was the arm as coded, not the epoch the distance data fix), so the join had content, and the")
    print("     end-to-end transfer computes it (r6719).  The w=0 algebra and the non-crossing of the")
    print("     collapse-leg phase stand.  The r2701 finding as it stood: **")
    print("  ** PO-12's remaining half has NO CONTENT. **")
    print('  ⛭⛭ ⓵ ** The pre-onset stretch is pressureless, and at w = 0 the potential equation loses')
    print('     k entirely: ** Φ\'\' + 3ℋΦ\' + (ℋ² + 2ℋ\')Φ = 0.  ** Verified symbolically, and k IS present')
    print('     in the general equation, so the check is not vacuous. **')
    print('     ⇒ *** Every mode obeys the SAME equation there.  There is no scale-dependent evolution,')
    print('       so there is nothing for a "single calculation across the join" to calculate. ***')
    print('  ⓶ ** The geometry agrees from both ends: ** the comoving horizon → 0 at the branch point')
    print('     (every mode outside, r2662), against peaks inside by 2.2 at the onset — so every')
    print('     acoustic mode crosses in between, ** "before the plasma began". **')
    print('  ⓷ ** And P15 states the residue exactly: ** "nothing before the onset can imprint an')
    print('     acoustic phase, so whatever sets it must act on modes ** already inside the sound horizon')
    print('     when the plasma begins **".')
    print('     ⇒ *** That is the first peak\'s position — PO-7\'s question. PO-12\'s own remaining half')
    print('       is empty. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
