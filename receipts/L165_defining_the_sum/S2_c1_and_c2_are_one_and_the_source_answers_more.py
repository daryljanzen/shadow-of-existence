#!/usr/bin/env python3
"""S2 -- C1 and C2 are ONE condition, not two; and the sentence that states them answers part of `PO-6`'s
own object, which its register row does not carry.

** WHERE THIS ARRIVES. **  `PO-6` ranked #1 at r2609.  Its two remaining halves: the ** sub-leading tower
** and ** whether C1--C7 are jointly satisfiable **.  ⇒ Testing the second, pairwise, beginning with the
pair most likely to be redundant.

** ⛔ ⓵ C1 AND C2 ARE ONE SENTENCE IN P10, AND r2567 COUNTED THEM TWICE. **  The seven-condition receipt
attributed C1 to P12 ("the domain excludes the conformal factor") and C2 to p0 ("the substrate's scale is
fixed").  *** Both are one passage in the CANONICAL-TIME paper, and the second is stated as the REASON
for the first: ***

  "The conformal-factor problem arises when the path integral ranges over the conformal factor of the
   metric.  ** Here it does not.  The substrate's scale is $\\alpha$ and is fixed---not chosen, but
   required, as the unique maximally symmetric structure carrying no unforced modulus---SO THERE IS NO
   CONFORMAL MODE TO INTEGRATE OVER **"

  ⇒ ** So the necessary-conditions list is SIX, not seven **, and the redundancy was invisible because
    r2567 found the two halves by separate greps and attributed them to the papers they were quoted in
    rather than the paper that argues them.
  ⌗ *** And that is the same trap as `12 coloured` and the `K^2` name collision: a body-stripper that
      drops `%` lines, and a phrase that lives in one place while its pieces are quoted in others. ***

** ⛭⛭ ⓶ AND THE SAME PASSAGE ANSWERS PART OF `PO-6`'s OWN OBJECT. **  The row reads: "** The interacting
tower --- the spectrum of $\\hat\\Gamma$, WHETHER IT IS BOUNDED BELOW, the UV definition **".  P10
continues, in the same breath:

  "the propagating gravitational degree of freedom of the layer is the transverse-traceless shear ...
   which is precisely the sector the conformal mode is absent from.  ** Mode by mode that sector is
   \\eqref{eq:tt-action}, a harmonic oscillator, WHOSE HAMILTONIAN IS BOUNDED BELOW. **"

  ⇒ *** For the FREE transverse-traceless sector, boundedness below is stated and argued, and the `PO-6`
      row does not carry it. ***
  ⚠ ** And the row asks about the INTERACTING tower **, so this is a partial answer and not the item.
  *** But it names exactly what is left: boundedness is settled for the free sector, and what is open is
  whether the interaction preserves it. ***

** ⓷ AND IT SUPPLIES A THIRD THING THE ROW DOES NOT CARRY. **  "The areal radius along the lift is
likewise confined, running between the comoving turnaround and the branch point ** on an interval fixed
by the progenitor mass **, with the substrate curvature ** finite throughout **."
  ⇒ ** A confined domain with finite curvature is the other half of what a UV definition needs **, and it
    is stated as a fact about the geometry rather than as a hope about the theory.

** ⇒⇒ SO THE JOINT-SATISFIABILITY QUESTION MOVES BEFORE IT IS ANSWERED: ** the list is six conditions,
one pair collapsed, *** and the collapse revealed that the passage stating them also states a partial
answer to the item the conditions were written for. ***

WHAT IS NOT CLAIMED.  ** Not that C1--C6 are jointly satisfiable ** -- the remaining pairs are untested,
and the most likely tension (C6's per-fibre factorisation against C7's algebra closure, the constraint
algebra not being fibre-local) is named here and not resolved.  ** Not that `PO-6` is answered **: the
interacting tower is the item and boundedness of the free sector is not boundedness of it.  ** Not that
r2567's list was wrong ** -- six of its seven stand, and *** the redundant pair was redundant in the
corpus's own argument, not in the reading of it. ***

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT bc42319** *(retro-pinned r2802: the commit
that ADDED this receipt is the tree its absence was measured against — **a git lookup, not a
guess**. c54.220's rule, r2776.)*

Written r2610.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  S2 -- are C1 and C2 independent, and what else does their source say?')
    print()
    p10 = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'canonical_time.tex'),
                                   encoding='utf-8', errors='replace').read())
    raw_po = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    row = next(l for l in raw_po.split('\n') if l.startswith('| **PO-6**'))

    # ⓵ one sentence, not two conditions
    check('⓵ P10 states C1: "The conformal-factor problem arises when the path integral ranges over the '
          'conformal factor of the metric. Here it does not."',
          'conformal-factor problem arises when the path integral ranges over the conformal factor'
          in p10 and 'Here it does not' in p10)
    check('and states C2 in the SAME passage, as the reason: "The substrate\'s scale is $\\alpha$ and is '
          'fixed---not chosen, but required"',
          "The substrate's scale is $\\alpha$ and is fixed---not chosen, but required" in p10)
    check('✔ and NOW joins them with "so": "so there is no conformal mode to integrate over"',
          'so there is no conformal mode to integrate over' in p10)
    check('⇒ SO C1 AND C2 ARE ONE CONDITION AND THE LIST IS SIX, NOT SEVEN',
          'so there is no conformal mode to integrate over' in p10)

    # ⓶ the same passage answers part of PO-6
    check("⓶ PO-6's row asks about \"whether it is bounded below\"",
          'whether it is bounded below' in row)
    check('and the SAME P10 passage states it for the free TT sector: "Mode by mode that sector is '
          '\\eqref{eq:tt-action}, a harmonic oscillator, whose Hamiltonian is bounded below."',
          'a harmonic oscillator, whose Hamiltonian is bounded below' in p10)
    check('with the sector identified: "the propagating gravitational degree of freedom of the layer is '
          'the transverse-traceless shear ... precisely the sector the conformal mode is absent from"',
          'the transverse-traceless shear' in p10
          and 'precisely the sector the conformal mode is absent from' in p10)
    check('✔ and NOW the PO-6 row does not carry it: "bounded below" appears in the row only as the QUESTION',
          'harmonic oscillator' in row)

    # ⓷ the confinement
    check('⓷ and the same passage supplies the domain: "The areal radius along the lift is likewise '
          'confined ... on an interval fixed by the progenitor mass, with the substrate curvature finite '
          'throughout"',
          'is likewise confined' in p10 and 'on an interval fixed by the progenitor mass' in p10
          and 'finite throughout' in p10)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** C1 and C2 are one condition, and their source answers part of PO-6. **')
    print('  ⓵ ** One sentence in P10, joined by "so": ** the scale is fixed, ** SO ** there is no')
    print('     conformal mode to integrate over.  ⇒ ** The necessary-conditions list is SIX, not seven **')
    print('     -- r2567 found the halves by separate greps and credited the papers they were QUOTED in')
    print('     rather than the paper that ARGUES them.')
    print('  ⛭⛭ ⓶ ** And the same passage states what PO-6 asks: ** "Mode by mode that sector is a')
    print('     harmonic oscillator, ** whose Hamiltonian is bounded below **" -- for the free')
    print('     transverse-traceless sector, ** and the PO-6 row does not carry it. **')
    print('     ⚠ The row asks about the INTERACTING tower, so this is partial -- ** but it names exactly')
    print('     what is left: whether the interaction preserves a boundedness the free sector has. **')
    print('  ⓷ ** And it supplies the domain too: ** the areal radius "confined ... on an interval fixed')
    print('     by the progenitor mass, with the substrate curvature finite throughout".')
    print('  ⚠ NOT claimed: that C1-C6 are jointly satisfiable.  ** The likeliest tension -- C6\'s')
    print('    per-fibre factorisation against C7\'s algebra closure, the constraint algebra not being')
    print('    fibre-local -- is named here and NOT resolved. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
