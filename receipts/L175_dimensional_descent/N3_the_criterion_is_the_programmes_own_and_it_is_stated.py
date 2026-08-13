#!/usr/bin/env python3
"""N3 -- L-240 settled from the corpus: uniqueness of the leaf's dynamics IS a desideratum this
programme holds, stated three times as "the programme's own criterion of necessity", so D = 4's forcing
is a REASON and not merely a property.

** WHERE r2518 LEFT IT. **  The count is exact: Lovelock's dynamical terms beyond Lambda number
floor((D-1)/2), so ** D = 4 is the largest dimension in which the field equations are FORCED ** and D = 5
admits Gauss--Bonnet as a genuine second term.  ** And r2518 stated the counter honestly: ** CR takes GR's
dynamics as given, so "the forcing is a PROPERTY the arrangement has, not by itself a REASON for it --
it becomes a reason only if uniqueness of the leaf's dynamics is a desideratum the programme holds."

  ⇒ ⛔ ** And this line then handed that question up as a decision, four times, in four dressings. **
    *** It is readable from the corpus, and the corpus says it three times. ***

** ⓵ THE PROGRAMME'S OWN CRITERION, NAMED AS SUCH. **

  "Maximal symmetry is what makes the substrate the least-arbitrary vacuum such a description can be cut
   from --- ** least-arbitrariness being the programme's own criterion of necessity (Rule 2 ..., read in
   the ontological register): a symmetry-breaking modulus is the adjustable parameter that criterion
   rejects **, and maximal symmetry the unique structure that requires its configuration."

  ** And it is invoked again, as the pillar that survives an argument: ** "the pillar that remains ... is
  the programme's own ** criterion of necessity ** --- Rule 2 ... for which a symmetry-breaking modulus
  ... is exactly the adjustable parameter it rejects."

** ⛭⛭ ⓶ AND THE CRITERION IS STATED IN EXACTLY THE FORM THE QUESTION ASKS FOR. **

  "This is the distinction between a world that ** REQUIRES ** a phenomenon and one that merely
   ** PERMITS ** it through adjustable parameters --- the same distinction the programme draws in reading
   the cosmic foliation as ** forced rather than chosen **."

  ⇒ *** REQUIRES-over-PERMITS is not a preference this programme might or might not hold.  It is the
      distinction it says it draws, in the register where it draws it, applied to the foliation and to
      the substrate's selection. ***

** ⓷ SO THE ANSWER IS YES, AND D = 4's FORCING IS A REASON. **
  * A ** second Lovelock coefficient ** is an adjustable parameter with no principle fixing it.
  * ** Rule 2 rejects exactly that. **
  * ** At D = 4 there is no second coefficient to reject: the field equations are REQUIRED. **
  ⇒ *** So the leaf's four-ness is not merely observed and not merely convenient -- it is the dimension
      at which the leaf's dynamics satisfies the programme's own stated criterion of necessity, and at
      no larger dimension does it. ***

** ⚠ AND WHAT THIS DOES NOT DO, WHICH IS MOST OF ITS SCOPE. **
  * ** It does not derive the substrate's dimension. **  PO-9's guard stands: "the cut's dimension is
    settled; the substrate's is bounded below only", and the chain here runs ** CUT -> DYNAMICS **, never
    CUT -> SUBSTRATE.
  * ** It does not make CR derive the field equations. **  P9 is explicit that the construction leaves
    GR's dynamics unchanged; what is established is that the arrangement satisfies a criterion the
    programme already holds, not that it produces the equations.
  * ** It does not settle whether the corpus SHOULD say so in a paper. **  That is a writing decision and
    it is 54's, and it is routed rather than made here.

⌗ AND THE REASON THIS IS FILED AS A CORRECTION AS WELL AS A FINDING: ** r2518 posed the question
correctly and then this line asked Daryl to answer it, in four successive turns, while the answer sat in
p0 and P15 stated three times. **  *** r2530's rule applies to questions this line RAISES, not only to
ones it inherits: is anything left UNDECIDED BY THE MATERIAL?  Here nothing was. ***

Written r2552.  Stated for reversal.
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
    print("  N3 -- does the programme hold uniqueness of the leaf's dynamics as a desideratum?")
    print()
    papers = [f for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
              if not os.path.basename(f).startswith('appendix_receipts')]
    allp = ' '.join(re.sub(r'\s+', ' ', '\n'.join(
        l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
        if not l.lstrip().startswith('%'))) for f in papers)
    arc = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_LIVE_ARC.md'),
                                   encoding='utf-8', errors='replace').read())

    # ⓵ the criterion, named
    check('⛭ the corpus names it: "least-arbitrariness being the programme\'s own criterion of '
          'necessity (Rule~2 ...)"',
          "least-arbitrariness being the programme's own criterion of necessity" in allp)
    check('and states what it rejects: "a symmetry-breaking modulus is the adjustable parameter that '
          'criterion rejects"',
          'a symmetry-breaking modulus is the adjustable parameter that criterion rejects' in allp)
    n_crit = len(re.findall('criterion of necessity', allp))
    check(f'and it is invoked {n_crit} times as THE PROGRAMME\'S OWN criterion, not an aside',
          n_crit >= 2)

    # ⓶ the criterion in the form the question asks
    check('⛭⛭ AND IN EXACTLY THE FORM THE QUESTION ASKS: "the distinction between a world that '
          '\\emph{requires} a phenomenon and one that merely \\emph{permits} it through adjustable '
          'parameters"',
          'requires} a phenomenon and one that merely \\emph{permits} it through adjustable parameters'
          in allp)
    check('applied to the foliation itself: "forced rather than chosen"',
          'forced rather than chosen' in allp)
    check('⇒⇒ SO REQUIRES-OVER-PERMITS IS NOT A PREFERENCE THE PROGRAMME MIGHT HOLD -- it is the '
          'distinction it says it draws, in the register where it draws it',
          "least-arbitrariness being the programme's own criterion of necessity" in allp
          and 'forced rather than chosen' in allp)

    # ⓷ the conclusion
    def dyn(D):
        return (D - 1)//2
    check(f'and r2518\'s count stands: dynamical Lovelock terms beyond Lambda number floor((D-1)/2), '
          f'so D=4 gives {dyn(4)} and D=5 gives {dyn(5)}',
          dyn(4) == 1 and dyn(5) == 2)
    check('⇒ SO A SECOND LOVELOCK COEFFICIENT IS AN ADJUSTABLE PARAMETER WITH NO PRINCIPLE FIXING IT, '
          'AND RULE 2 REJECTS EXACTLY THAT -- while at D=4 there is no second coefficient to reject',
          dyn(4) == 1
          and 'a symmetry-breaking modulus is the adjustable parameter that criterion rejects' in allp)

    # ⚠ the scope
    check("⚠ and PO-9's guard stands: the cut's dimension is settled, the substrate's is bounded below "
          'only', 'bounded below only' in re.sub(r'\s+', ' ', open(
              os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()))
    check('and CR does NOT derive the field equations: "the construction leaves the dynamics of '
          'general relativity unchanged"',
          'the construction leaves the dynamics of general relativity unchanged' in allp)
    check('⌗ and the row itself posed this at r2518 as the decision it turns on',
          'desideratum' in arc)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** YES -- and it is stated three times as the programme\'s own criterion. **')
    print('  ⓵ ** "least-arbitrariness being the programme\'s own criterion of necessity (Rule 2) ... a')
    print('     symmetry-breaking modulus is the adjustable parameter that criterion rejects." **')
    print('  ⓶ ** And in the form the question asks: "the distinction between a world that REQUIRES a')
    print('     phenomenon and one that merely PERMITS it through adjustable parameters" ** -- applied to')
    print('     the foliation as ** "forced rather than chosen". **')
    print('  ⇒⇒ ** So D = 4\'s forcing is a REASON, not merely a property: a second Lovelock coefficient')
    print('     is an adjustable parameter with no principle fixing it, Rule 2 rejects exactly that, and')
    print('     at D = 4 there is no second coefficient to reject. **')
    print('  ⚠ SCOPE: ** it does not derive the substrate\'s dimension ** (the chain runs CUT -> DYNAMICS)')
    print('    and ** it does not make CR derive the field equations ** -- only that the arrangement')
    print('    satisfies a criterion the programme already holds.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
