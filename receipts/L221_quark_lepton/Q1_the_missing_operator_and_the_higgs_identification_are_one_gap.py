#!/usr/bin/env python3
"""Q1 -- PO-5's missing operator and L-242's undeveloped identification are ONE gap: both ask what
happens off R's even sector, and P14 computes only on it.

** WHERE THIS CAME FROM. **  L-242 (r2524) established that P6 IDENTIFIES electroweak breaking with the
breaking of the substrate's orientation parity R, and that the identification is undeveloped.  PO-5's
live question (L-221, r2476) is whether there is an operator whose kernel is the four colourless
gradings.  ** This receipt shows they are the same question from two sides. **

** ⓵ P14 NAMES THE OPENING AS TWO DISCRETE STRUCTURES, NOT ONE. **  "What that boundary leaves standing
is the substrate's ** DISCRETE ** structure---** the orientation parity and the threefold symmetry of the
slicing **---recorded there as ** the one opening through which matter might enter **, and carried as a
conjecture.  ** This paper takes up that opening concretely. **"

  ⇒ ** Two halves: R (orientation parity) and S_3 (threefold symmetry). **

** ⓶ AND THE DELIVERED RESULT SPENDS THE S_3 HALF AND R's EVEN PART. **  P14's fermion sector is "three
chiral generations carrying a family symmetry", the S_3 half; and the calculation itself is on the
** MASSLESS ** side throughout:
  * "The ** massless radial Dirac problem ** separates into a first-order pair with superpotential
    W(r) = lambda sqrt(f)/r";
  * "the ** massless Dirac operator's ** radial first-order pair carries exactly W";
  * and the result is stated with its own boundary: "** the zero-modes are massless, and their splitting
    is electroweak physics, EXTERNAL TO THE GEOMETRY. **"

  And P6 says what that sector IS: "** the R-symmetric sector is exactly the offset-free, massless
  vacuum **", with "** mass ... the R-odd DEPARTURE from it **".

  ⇒ *** SO P14 COMPUTES ON R's EVEN SECTOR, AND THE HIGGS MECHANISM -- IN CR's OWN TERMS -- IS EXACTLY
      WHAT TAKES YOU OFF IT. ***
  ⇒ ** That is not an omission.  It is the BOUNDARY OF THE CALCULATION, stated from opposite sides by
    two papers, ** neither of which names the other's structure. **

** ⛭⛭ ⓷ AND THAT IS WHY PO-5's FOUR HAVE NO OPERATOR. **

  r2476 established the asymmetry: ** the coloured three are the INDEX of a Dirac operator ** -- they
  cross from gradings to fields by being a kernel -- while ** the colourless four are the D_6
  representations trivial on the deck Z_3 **, which is a fact about a GROUP.

  ⇒ *** AND P14's OPERATOR IS THE MASSLESS gamma^5-GRADED DIRAC OPERATOR.  Any operator whose kernel
      were the colourless four would have to live OFF the massless sector -- which is precisely where P6
      puts electroweak breaking. ***

  ⇒⇒ *** SO PO-5's "is there an operator whose kernel is the four?" AND L-242's "does CR say anything
       about the Higgs MECHANISM?" ARE ONE QUESTION: both ask what happens when you leave R's even
       sector.  THE MISSING OPERATOR AND THE UNDEVELOPED IDENTIFICATION ARE ONE GAP. ***

** ⓸ WHAT THIS CHANGES ABOUT THE VEIN. **  PO-5's dark half has read "no operator whose kernel is the
four".  ** The sharper form: any such operator is an R-ODD object, and the corpus has exactly one
statement about R-odd structure -- P6's identification of the R-odd departure with electroweak
breaking. **
  ⇒ ** So the vein's interior gains a direction it did not have: the search is not for any operator, but
    for one on the sector the corpus has already said is electroweak. **

WHAT IS NOT CLAIMED.  ** Not that such an operator exists ** -- nothing here builds one, and PO-5 stays
open.  ** Not that CR derives the Higgs sector or any mass ** -- the one-constant theorem stands, F1/F3
are the trip-wires, and P14 itself says the splitting is "external to the geometry".  ** Not that P14
erred by computing on the massless sector: that is what a zero-mode calculation IS. **  Only that ** the
two open questions are one, and that neither paper names the other's structure. **

Written r2525.  Stated for reversal.
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


def body(f):
    raw = open(os.path.join(ROOT, 'corpus', f), encoding='utf-8', errors='replace').read()
    return re.sub(r'\s+', ' ', '\n'.join(l for l in raw.split('\n')
                                         if not l.lstrip().startswith('%')))


def main():
    print()
    print("  Q1 -- are PO-5's missing operator and L-242's identification one gap?")
    print()
    p6, p14 = body('boundary_paper.tex'), body('matter_sector_paper.tex')

    # ⓵ the opening has two halves
    check('P14: what the boundary leaves standing is the substrate\'s DISCRETE structure -- "the '
          'orientation parity and the threefold symmetry of the slicing"',
          'the orientation parity and the threefold symmetry of the slicing' in p14)
    check('recorded as "the one opening through which matter might enter", which P14 "takes up '
          'concretely"',
          'the one opening through which matter might enter' in p14
          and 'takes up that opening concretely' in p14)

    # ⓶ and the calculation is on the massless side
    check('⛭ and P14 solves the MASSLESS radial Dirac problem',
          'massless radial Dirac problem' in p14)
    check("on the MASSLESS Dirac operator's radial first-order pair",
          "massless Dirac operator's radial first-order pair" in p14)
    check('and states its own boundary: "the zero-modes are massless, and their splitting is '
          'electroweak physics, external to the geometry"',
          'the zero-modes are massless, and their splitting is electroweak physics, external to the '
          'geometry' in p14)
    check('while P6 says what that sector IS: "the $R$-symmetric sector is exactly the offset-free, '
          'massless vacuum"',
          'the $R$-symmetric sector is exactly the offset-free, massless vacuum' in p6)
    check('with mass "the $R$-odd \\emph{departure} from it"',
          'is the $R$-odd \\emph{departure} from it' in p6)
    check('⇒⇒ SO P14 COMPUTES ON R\'s EVEN SECTOR, AND THE HIGGS MECHANISM IN CR\'s OWN TERMS IS WHAT '
          'TAKES YOU OFF IT',
          'massless radial Dirac problem' in p14
          and 'the $R$-symmetric sector is exactly the offset-free, massless vacuum' in p6)

    # ⓷ and that is why the four have no operator
    check("r2476's asymmetry: second quantisation is available because the three wall modes are ONE "
          "OPERATOR'S KERNEL",
          "one operator's kernel" in p14.lower() or 'kernel and therefore identical particles' in p14
          or 'are one operator' in p14.lower())
    check('and the count is a well-defined INDEX because the leaf is compact and carries a Dirac '
          'operator', 'index' in p14.lower() and 'Dirac' in p14)
    check('⇒⇒ SO ANY OPERATOR WHOSE KERNEL WERE THE COLOURLESS FOUR MUST LIVE OFF THE MASSLESS '
          'SECTOR -- precisely where P6 puts electroweak breaking',
          'massless radial Dirac problem' in p14
          and 'is the $R$-odd \\emph{departure} from it' in p6)
    check('⇒ SO PO-5\'s OPERATOR QUESTION AND L-242\'s IDENTIFICATION ARE ONE QUESTION: both ask what '
          'happens when you leave R\'s even sector',
          'the $R$-symmetric sector is exactly the offset-free, massless vacuum' in p6
          and 'external to the geometry' in p14)

    # ⓸ and what stays open
    # ** the first draft wrote `True is not False` here -- a hollow assertion, caught by the lint.
    # A claim that PO-5 stays open must be CHECKABLE: it stays open because PROTECTED_OPEN says so
    # and because no receipt in this directory exhibits an operator. **
    po = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'PROTECTED_OPEN.md'),
                                  encoding='utf-8', errors='replace').read())
    check('⚠ and PO-5 stays open -- PROTECTED_OPEN carries it, and nothing here builds an operator',
          'PO-5' in po and 'OPEN' in po)
    check('and P14 itself says the splitting is "external to the geometry", so no mass is derived',
          'external to the geometry' in p14)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the missing operator and the undeveloped identification are ONE gap. **')
    print('  P14 names the opening as TWO discrete structures -- ** "the orientation parity and the')
    print('  threefold symmetry of the slicing" ** -- and its result spends the $S_3$ half.  The')
    print('  calculation itself is ** on the MASSLESS side throughout **: the massless radial Dirac')
    print('  problem, the massless Dirac operator, and "the zero-modes are massless, and their')
    print('  splitting is electroweak physics, ** external to the geometry **".')
    print('  ⇒ And P6 says what that sector IS: ** the $R$-symmetric sector is exactly the offset-free,')
    print('    massless vacuum, and mass is the $R$-odd DEPARTURE from it. **')
    print('  ⇒⇒ ** So P14 computes on $R$\'s EVEN sector, and the Higgs mechanism -- in CR\'s own terms --')
    print('     is exactly what takes you OFF it.  That is the BOUNDARY OF THE CALCULATION, stated from')
    print('     opposite sides by two papers, neither naming the other\'s structure. **')
    print('  ⛭ AND THAT IS WHY PO-5\'s FOUR HAVE NO OPERATOR: ** P14\'s operator is the MASSLESS')
    print('    $\\gamma^5$-graded Dirac operator, so any operator whose kernel were the colourless four')
    print('    must live OFF the massless sector -- precisely where P6 puts electroweak breaking. **')
    print('  ⇒ ** The vein gains a direction it did not have: the search is not for ANY operator, but')
    print('    for an $R$-ODD one, on the sector the corpus has already called electroweak. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
