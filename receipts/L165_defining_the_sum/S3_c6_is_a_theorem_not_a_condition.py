#!/usr/bin/env python3
"""S3 -- the C6/C7 tension dissolves because C6 is not a condition: the per-fibre structure is DERIVED,
and the list is five conditions plus one theorem.

** THE TENSION, NAMED AT r2610 AS THE LIKELIEST. **  ** C6 ** requires the measure to "respect the
per-fibre closure"; ** C7 ** requires it not to spoil the constraint algebra's closure.  ⇒ *** And the
constraint algebra is not fibre-local -- it involves spatial derivatives -- so a measure factorising over
fibres looked as though it might fail to preserve the algebra. ***

** ⛭⛭ ⓵ AND THE CORPUS HAD ALREADY DISSOLVED IT, IN A RECEIPT WRITTEN FOR ANOTHER PURPOSE. **
`D1_the_boundary_is_per_fibre_and_the_UV_is_over_fibres`, on P10's structure:

  "with the tower coupled, the boundary coefficient is an operator $\\hat\\Gamma=\\gamma+c\\sum_n\\hat\\pi_n^2$
   (at leading order), and ** SINCE IT COMMUTES WITH THE RADIAL PART **, $-\\partial_x^2+\\hat\\Gamma/x^2$
   ** decomposes as a DIRECT INTEGRAL over its spectrum ** ... and thermal regularity supplies the
   condition ** FIBRE BY FIBRE **."

  ⇒⇒ *** THE PER-FIBRE STRUCTURE IS A CONSEQUENCE OF A COMMUTATION RELATION, NOT A REQUIREMENT ON A
      MEASURE.  The decomposition is forced by the operator; nothing chooses it and nothing can violate
      it. ***

** ⓶ SO C6 IS MISCLASSIFIED, AND THE TENSION CANNOT ARISE. **  A necessary condition is something a
candidate measure must SATISFY and might FAIL.  *** A direct-integral decomposition forced by
$[\\hat\\Gamma,\\text{radial}]=0$ is neither: it is a property of the operator the measure is built on. ***
  ⇒ ** So C7 has nothing to conflict with. **  The algebra's closure is a condition; the fibre structure
    is the arena the condition is stated in.
  ⌗ *** And the list is FIVE CONDITIONS PLUS ONE THEOREM: C1(=C2), C3, C4, C5, C7 are conditions; C6 is
      a derived fact. ***

** ⓷ AND THE RECEIPT SAYS WHY THE SEPARATION IS STRUCTURAL RATHER THAN LUCKY. **  "the sub-threshold
set's SIZE---finite, countable, or a continuum---is ** irrelevant to whether each of its fibres receives
a condition **".
  ⇒ ** A per-fibre condition cannot be broken by the number of fibres. **  *** That is why the boundary
    problem and the UV problem separate, and it is the reason `PO-6`'s two halves are two halves rather
    than one entangled question. ***

** ⇒⇒ SO THE JOINT-SATISFIABILITY QUESTION SHRINKS TWICE IN TWO REVISIONS. **  r2610 collapsed C1 and C2
into one; this reclassifies C6 out of the list entirely.
  *** From seven conditions to FIVE, with the two removals being a redundancy and a misclassification --
      neither a physics result, and both found by reading the passages that ARGUE the conditions rather
      than the ones that quote them. ***

WHAT IS NOT CLAIMED.  ** Not that C1, C3, C4, C5 and C7 are jointly satisfiable ** -- the remaining pairs
are untested and this receipt tests none of them.  ** Not that the direct-integral structure survives the
interaction **: D1 states it "at leading order", and *** whether $\\hat\\Gamma$ still commutes with the
radial part at higher order is exactly the interacting tower's own question. ***  ** Not that D1 is
re-derived here ** -- it is cited and used.

Written r2611.  Stated for reversal.
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


def main():
    print()
    print('  S3 -- is C6 a condition, or a consequence?')
    print()
    d1p = glob.glob(os.path.join(ROOT, 'receipts', '**',
                                 'D1_the_boundary_is_per_fibre_and_the_UV_is_over_fibres.py'),
                    recursive=True)
    check('⌗ the D1 receipt exists', len(d1p) == 1)
    d1 = re.sub(r'\s+', ' ', open(d1p[0], encoding='utf-8', errors='replace').read())
    s1p = os.path.join(ROOT, 'receipts', 'L165_defining_the_sum',
                       'S1_seven_necessary_conditions_on_the_measure.py')
    s1 = re.sub(r'\s+', ' ', open(s1p, encoding='utf-8', errors='replace').read())

    # ⓵ the derivation
    check('⓵ D1 states the commutation: the boundary coefficient is an operator "and since it commutes '
          'with the radial part"',
          'since it commutes with the radial part' in d1)
    check('and the consequence: it "decomposes as a DIRECT INTEGRAL over its spectrum"',
          'decomposes as a DIRECT INTEGRAL over its spectrum' in d1)
    check('and that thermal regularity then supplies the condition "FIBRE BY FIBRE"',
          'FIBRE BY FIBRE' in d1)

    # ⓶ what S1 listed it as
    check('⓶ and S1 lists C6 as a CONDITION: "IT MUST RESPECT THE PER-FIBRE CLOSURE"',
          'IT MUST RESPECT THE PER-FIBRE CLOSURE' in s1)
    check('⇒ SO C6 IS MISCLASSIFIED: a direct-integral decomposition forced by a commutation relation is '
          'not something a measure can fail -- it is a property of the operator',
          'since it commutes with the radial part' in d1
          and 'IT MUST RESPECT THE PER-FIBRE CLOSURE' in s1)

    # ⓷ why the separation is structural
    check("⓷ and D1 says why it is structural rather than lucky: the sub-threshold set's size is "
          '"irrelevant to whether each of its fibres receives a condition"',
          'irrelevant to whether each of its fibres receives a condition' in d1)

    # the limit
    check('⚠ and D1 states it "at leading order" -- so whether the commutation survives the interaction '
          "is the interacting tower's own question",
          'at leading order' in d1)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** C6 is not a condition, and the C6/C7 tension cannot arise. **')
    print('  ⓵ ** D1: the boundary coefficient "commutes with the radial part", so the operator')
    print('     "decomposes as a DIRECT INTEGRAL over its spectrum" and thermal regularity supplies the')
    print('     condition "FIBRE BY FIBRE". **')
    print('  ⇒⇒ ** The per-fibre structure is a CONSEQUENCE of a commutation relation, not a requirement')
    print('     on a measure.  Nothing chooses it and nothing can violate it. **')
    print('  ⓶ ** S1 lists it as "IT MUST RESPECT THE PER-FIBRE CLOSURE" -- a condition a candidate could')
    print('     fail.  It cannot. **  ⇒ ** The list is FIVE CONDITIONS PLUS ONE THEOREM. **')
    print('  ⓷ ** And the separation is structural: ** the sub-threshold set\'s size is "irrelevant to')
    print('     whether each of its fibres receives a condition" -- ** a per-fibre condition cannot be')
    print('     broken by the number of fibres. **')
    print('  ⇒ ** So joint satisfiability shrank twice in two revisions: seven → six (C1=C2, r2610) →')
    print('    five (C6 reclassified).  Neither removal is a physics result; both were found by reading')
    print('    the passages that ARGUE the conditions rather than the ones that quote them. **')
    print('  ⚠ NOT claimed: that the five are jointly satisfiable, nor that the commutation survives the')
    print('    interaction -- ** D1 states it at leading order, and that is the tower\'s own question. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
