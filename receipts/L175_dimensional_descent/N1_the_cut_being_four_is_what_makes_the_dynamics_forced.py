#!/usr/bin/env python3
"""N1 -- a LEAD, not a result: the corpus holds two halves of a connection it has never joined, and the
join lands on PO-9.  The four-dimensionality of the CUT is what makes the dynamics FORCED.

** THE OCCASION. **  Daryl asked whether r2514's finding -- "the constraint is CONSERVED, not
re-imposed" -- touches "the whole second-order EFE reason to take vanishing covariant derivative".
** It does, and the corpus holds both halves. **

** ⓵ THE HALF THE CORPUS ALREADY STATES. **  P11: "A first-class constrained system evolves consistently
to all orders ** by the contracted Bianchi identity **: there is no classical dynamical obstruction at
any order."
  ⇒ ** r2514's conserved constraint IS the contracted Bianchi identity, and P11 already states the
    all-orders version -- which bears on the remainder r2514 left open. **

** ⓶ THE OTHER HALF, ALSO ALREADY THERE, AND NEVER USED AS SUCH. **  P12's abstract: the
hypersurface-deformation (Dirac) algebra ** is not a Lie algebra ** -- the bracket of two normal
deformations closes on the tangential generators with a coefficient that is ** the inverse spatial
metric, a structure FUNCTION rather than a constant ** -- so it is, in the precise modern sense, a Lie
ALGEBROID.  And P12 cites ** Teitelboim1973 ** for the brackets.

  ⛔ ** BUT P12 NEVER DRAWS THE UNIQUENESS CONSEQUENCE, AND THE ABSENCE IS MEASURED HERE: ** across every
  .tex in the corpus, ** ZERO occurrences of "Lovelock" **; in P12, ** zero of "uniquely", "embeddab",
  "determines the" **.
  ⇒ *** The corpus cites the paper the uniqueness result lives beside, for the algebra's FORM, and never
      for its CONTENT. ***

** ⓷ WHAT THE OUTSIDE LITERATURE SAYS -- marked as OUTSIDE, and verified by search rather than recalled,
because two receipts in this span failed on quotations written from memory. **

  * Hojman--Kuchar--Teitelboim, Ann. Phys. 96 (1976) 88: ** Einsteinian geometrodynamics is the ONLY
    (time-reversible) canonical representation of the generators of deformations of a spacelike
    hypersurface embedded in a Riemannian spacetime, if the intrinsic metric and a conjugate momentum
    are the sole canonical variables. **
  * Teitelboim showed the Dirac algebra is geometrically ** the embeddability condition **.
  * ⛭⛭ AND THE PIECE THAT MAKES IT BITE: ** Teitelboim and Zanelli showed that LOVELOCK gravity's
    constraints ALSO close as the Dirac algebra **, and for n > 4 there are Lovelock gravities other
    than GR.

  ⇒ *** SO THE DIRAC ALGEBRA FORCES GR ONLY IN FOUR DIMENSIONS.  IN FIVE IT DOES NOT: GAUSS--BONNET
      BECOMES DYNAMICAL AND CLOSES THE SAME ALGEBRA. ***

** ⛭⛭⛭ ⓸ AND THAT IS WHY THIS LEAD LANDS ON PO-9. **

  CR's substrate is dS_5 -- FIVE-dimensional -- and its dynamics lives on a FOUR-dimensional cut.  P12's
  algebroid is the constraint algebra ** of the 4D leaf **.

  ⇒ *** THE FOUR-DIMENSIONALITY OF THE CUT IS WHAT MAKES THE HKT/LOVELOCK FORCING AVAILABLE AT ALL.  Had
      the leaf been five, the same brackets would not have singled out GR. ***

  ⌗ ** AND THAT IS A DIFFERENT CLAIM FROM THE ONE PO-9's MAPPED HALF CARRIES. **  L-175 records that the
  cut is four and ** says nothing about the substrate ** -- a guard against reading leaf-dimension as
  substrate-dimension, and correct.
  ⇒ ** This says something else: the cut being four is DOING WORK.  It is what makes the dynamics on the
    leaf FORCED rather than chosen. **
  ⇒ *** Not a claim about the substrate's dimension -- a claim about what the leaf's four-ness BUYS. ***

** ⚠ WHAT IS NOT CLAIMED, and the scope is most of the value here. **
  * ** NOT that CR derives Lovelock, HKT, or the Einstein equations. **  P9 is explicit that "the
    construction leaves the dynamics of general relativity unchanged", and P12 calls its own claim
    ** "a recognition rather than an addition" **.  ** CR inherits the dynamics; it does not force it. **
  * ** NOT that the connection is established. **  This receipt asserts only (a) what the corpus says,
    (b) what it does not say, MEASURED, and (c) what the outside literature says, MARKED as outside.
  * ** NOT that a five-dimensional substrate is in tension with anything ** -- the dynamics is not on
    the substrate.

  ⇒ *** THE LEAD, stated as a question so it cannot be mistaken for a result: does the leaf's four-ness,
      which the corpus treats as an output of the slicing, ALSO carry the forcing of the dynamics -- and
      if so, is that a second and independent reason the cut is four? ***

Written r2515.  Stated for reversal.
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


def pub(f):
    raw = open(os.path.join(ROOT, 'corpus', f), encoding='utf-8', errors='replace').read()
    return re.sub(r'\s+', ' ', '\n'.join(l for l in raw.split('\n')
                                         if not l.lstrip().startswith('%')))


def main():
    print()
    print('  N1 -- does the corpus hold two halves of an unjoined connection?')
    print()
    p9, p11, p12 = pub('range_paper.tex'), pub('dynamics_paper.tex'), pub('algebroid_paper.tex')
    # ** PO-9's guard lives in BOARD.md's vein summary, not in the register row -- checked at source
    # rather than assumed, after the first run failed against THE_LIVE_ARC. **
    arc = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'BOARD.md'),
                                   encoding='utf-8', errors='replace').read())

    check('P11: "evolves consistently to all orders by the contracted Bianchi identity: there is no '
          'classical dynamical obstruction at any order"',
          'evolves consistently to all orders by the contracted Bianchi identity' in p11
          and 'no classical dynamical obstruction at any order' in p11)

    check('P12: the Dirac algebra "is not a Lie algebra", closing with the inverse spatial metric, '
          '"a structure \\emph{function} rather than a constant"',
          'is not a Lie algebra' in p12
          and 'a structure \\emph{function} rather than a constant' in p12)
    check('and P12 cites Teitelboim1973 for the brackets', 'Teitelboim1973' in p12)

    tex = glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
    lovelock = sum(len(re.findall('Lovelock', open(f, encoding='utf-8', errors='replace').read(), re.I))
                   for f in tex)
    check(f'⛔ ZERO occurrences of "Lovelock" across all {len(tex)} .tex files (found {lovelock})',
          lovelock == 0)
    for w in ('uniquely', 'embeddab', 'determines the'):
        check(f'and ZERO of "{w}" in P12', len(re.findall(w, p12, re.I)) == 0)
    check("⇒ SO THE CORPUS CITES THE PAPER THE UNIQUENESS RESULT LIVES BESIDE, FOR THE ALGEBRA'S FORM, "
          'AND NEVER FOR ITS CONTENT', 'Teitelboim1973' in p12 and lovelock == 0)

    check('the substrate is five-dimensional',
          'SO(5,1)/SO(4,1)' in p12 or 'de Sitter substrate' in p12)
    check("and PO-9's mapped half (in BOARD.md's vein summary) records that the cut is four and "
          '"says nothing about the substrate"',
          'cut is four and **says nothing about the substrate**' in arc)
    check("⇒⇒ SO THE LEAD IS DISTINCT FROM PO-9's GUARD: not a claim about the SUBSTRATE's dimension, "
          "but about what the LEAF's four-ness BUYS",
          'cut is four and **says nothing about the substrate**' in arc and lovelock == 0)

    check('⚠ CR does NOT derive the dynamics: "the construction leaves the dynamics of general '
          'relativity unchanged"',
          'the construction leaves the dynamics of general relativity unchanged' in p9)
    check('and P12 calls its own claim "a recognition rather than an addition"',
          'is a recognition rather than an addition' in p12)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (A LEAD, NOT A RESULT): ** the corpus holds two halves and has never joined them. **')
    print('  1 P11 already states the all-orders version: ** first-class systems evolve consistently by')
    print('    the contracted Bianchi identity ** -- which is what r2514 verified without naming it.')
    print('  2 P12 identifies the Dirac algebra as a Lie ALGEBROID because its structure function is the')
    print('    inverse spatial metric, and cites Teitelboim1973 ** for the FORM and never the CONTENT **:')
    print(f'    zero "Lovelock" across {len(tex)} papers; zero "uniquely"/"embeddab"/"determines the".')
    print('  3 OUTSIDE (verified by search, marked as outside): ** HKT prove Einsteinian geometrodynamics')
    print('    is the ONLY canonical representation of those deformations **; Teitelboim reads the Dirac')
    print('    algebra as the EMBEDDABILITY condition; and ** Teitelboim--Zanelli show LOVELOCK gravity')
    print('    closes the same algebra, so the forcing is a FOUR-DIMENSIONAL fact. **')
    print('  => ** THE LEAD: the four-dimensionality of the CUT is what makes the dynamics forced.  Had')
    print('     the leaf been five, the same brackets would not have singled out GR. **')
    print('  * Different from PO-9\'s guard "the cut is four and says nothing about the substrate":')
    print('    ** this says the cut being four is DOING WORK -- it is what the leaf\'s four-ness BUYS. **')
    print('  ! NOT claimed: that CR derives Lovelock, HKT or the field equations.  ** P9: the construction')
    print('    leaves GR\'s dynamics unchanged.  P12: a recognition rather than an addition. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
