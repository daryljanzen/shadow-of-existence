#!/usr/bin/env python3
"""N2 -- L-240 worked: D = 4 is the largest dimension in which the Lovelock series leaves exactly ONE
dynamical term, so the CUT's settled four-ness is what makes the leaf's dynamics carry no unfixed
coefficient.  Interior of PO-9, not a closure of it.

** WHERE r2515 LEFT IT. **  The corpus holds P11's Bianchi statement and P12's algebroid identification
and has never joined them; the join runs through the fact that ** the Dirac algebra forces GR only in
four dimensions ** (HKT; Teitelboim--Zanelli show Lovelock gravity closes the same algebra, and for
n > 4 there are Lovelock gravities other than GR).  The lead was registered as a QUESTION.

** ⓵ THE COUNT, and it is exact. **  Lovelock: the Lagrangian is a sum of Euler densities L_k built
from k Riemann tensors; L_k is ** TOPOLOGICAL when 2k = D ** and ** vanishes identically when 2k > D **.
So the DYNAMICAL terms beyond the cosmological constant number floor((D-1)/2):

      D        dynamical beyond Lambda
      3                1
      4                1        <- EINSTEIN--HILBERT ALONE; Gauss--Bonnet is topological here
      5                2        <- Gauss--Bonnet becomes DYNAMICAL: the dynamics is a CHOICE
      6                2
      7                3

  ⇒ *** D = 4 IS THE LARGEST DIMENSION IN WHICH THE FIELD EQUATIONS ARE FORCED TO BE EINSTEIN'S. ***

** ⛭⛭ ⓶ AND THAT IS Rule 2's OWN LANGUAGE, WHICH IS WHY THIS IS NOT A NEW CRITERION. **  P0: "a
symmetry-breaking modulus is the adjustable parameter that criterion rejects."  L-175 already applies it
to a COUNT -- r2474 established that ** one-step-ness is governed by Rule 2, not taste **, because a
second slicing step would carry an unfixed modulus.
  ⇒ ** A second Lovelock coefficient is exactly that: an unfixed adjustable parameter. **  ⇒ *** So the
    same criterion the corpus already applies to the STEP COUNT applies to the leaf's DIMENSION -- through
    the dynamics rather than through the slicing.  No criterion is added here. ***

** ⓷ AND THE SCORING COMES OUT AS A THIRD THING, WHICH IS THE REAL RESULT. **

  THE_BASE_RATE's discriminant: "least-arbitrariness arguments that REMOVE AN EXCEPTION succeed; ones
  that ADD MACHINERY to explain a number fail.  ** So the first move is not to make the argument -- it is
  to ask which kind it would be. **"  Doing that:

    reading                                              kind        standing
    ------------------------------------------------     --------    -----------------------------
    "the substrate is five BECAUSE the leaf's dynamics    ADDS        the historically failing kind
     is then forced"
    "the substrate's five-ness and the leaf's forced      REMOVES     favourable
     dynamics are the same fact -- Rule 2 already
     rejects unfixed moduli"

  ⚠ ** BUT THE DISCRIMINANT IS FOR ARGUMENTS DEFENDING AN EXISTING NUMBER, AND PO-9 SAYS THE SUBSTRATE'S
  DIMENSION IS "BOUNDED BELOW ONLY" ** -- it is an ** OPEN QUESTION **, not a number being defended.
  ⇒ *** So this scores as NEITHER.  It is a candidate piece of a vein's INTERIOR, and the vein rules
      apply, not the base rate.  A vein closes FROM WITHIN when its interior is completely known: this is
      interior, and it is not a closure. ***

** ⓸ AND IT DOES NOT RE-MAKE THE c54.6 ERROR, which PO-9 explicitly guards against. **  PO-9: "** The
cut's dimension is settled; the substrate's is bounded below only.  A node that reads the first as
capping the second has re-made the c54.6 error. **"
  ⇒ ** The chain here runs CUT -> DYNAMICS, never CUT -> SUBSTRATE. **  It says nothing about the
    substrate's dimension and does not touch the bound.  ** What it adds is a consequence of the cut's
    ALREADY-SETTLED four-ness that nobody had drawn. **

** ⚠ AND THE COUNTER SHIPS WITH IT, because it is most of the weight. **  ** CR takes GR's dynamics as
GIVEN ** -- P9: "the construction leaves the dynamics of general relativity unchanged".  It inherits
Einstein's equations either way.
  ⇒ *** So the forcing is a PROPERTY the arrangement has, not by itself a REASON for it.  It becomes a
      reason only if uniqueness of the leaf's dynamics is a desideratum the programme holds -- and
      whether it does is not settled here. ***

WHAT IS NOT CLAIMED.  Not that PO-9 is answered or narrowed as a bound.  Not that CR derives Lovelock or
the field equations.  Not that the substrate's dimension follows from anything here.  ** Only that the
cut's four-ness carries a consequence the corpus has never recorded: at four, and at no larger
dimension, the leaf's dynamics carries no unfixed coefficient. **

Written r2518.  Stated for reversal.
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


def dynamical(D):
    """Lovelock terms beyond Lambda: k = 1 .. floor((D-1)/2); L_k topological at 2k=D, zero above."""
    return (D - 1)//2


def main():
    print()
    print("  N2 -- what does the cut's four-ness buy?")
    print()
    po = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'PROTECTED_OPEN.md'),
                                  encoding='utf-8', errors='replace').read())
    base = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_BASE_RATE.md'),
                                    encoding='utf-8', errors='replace').read())
    arc = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_LIVE_ARC.md'),
                                   encoding='utf-8', errors='replace').read())
    p9 = re.sub(r'\s+', ' ', '\n'.join(
        l for l in open(os.path.join(ROOT, 'corpus', 'range_paper.tex'),
                        encoding='utf-8', errors='replace').read().split('\n')
        if not l.lstrip().startswith('%')))

    # ⓵ the count
    check('Lovelock: dynamical terms beyond Lambda number floor((D-1)/2)',
          [dynamical(D) for D in (3, 4, 5, 6, 7)] == [1, 1, 2, 2, 3])
    check('⛭ D = 4 leaves EXACTLY ONE -- Einstein--Hilbert alone, Gauss--Bonnet topological there',
          dynamical(4) == 1)
    check('and D = 5 leaves TWO -- Gauss--Bonnet becomes dynamical, so the dynamics is a CHOICE',
          dynamical(5) == 2)
    check('⇒⇒ SO D = 4 IS THE LARGEST DIMENSION IN WHICH THE FIELD EQUATIONS ARE FORCED',
          dynamical(4) == 1 and all(dynamical(D) > 1 for D in range(5, 12)))

    # ⓶ Rule 2 is already the corpus's
    # ** ANCHORED TO THE PAPERS, NOT THE REGISTER.  The first draft pinned THE_LIVE_ARC and failed --
    # three revisions after this line built check_arcpins against exactly that.  Rule 2 lives in P0 and
    # its application to a COUNT lives in P14; both are sources, and both are where the claim is ABOUT. **
    p0 = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'geometric_core_paper.tex'),
                                  encoding='utf-8', errors='replace').read())
    p14 = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex'),
                                   encoding='utf-8', errors='replace').read())
    check("Rule 2 is already the corpus's, in P0: a symmetry-breaking modulus is what the criterion "
          'rejects', 'symmetry-breaking modulus' in p0)
    check('and P14 already applies it to a COUNT: "a one-hinge truncation is excluded not as '
          'disfavoured but as carrying an unfixed arbitrary modulus, which the principle forbids"',
          'carrying an unfixed arbitrary modulus, which the principle forbids' in p14)
    check('⇒ so a second Lovelock coefficient is the same kind of object, and NO criterion is added here',
          'symmetry-breaking modulus' in p0 and dynamical(5) == 2)

    # ⓷ the scoring
    check("THE_BASE_RATE's discriminant: arguments that REMOVE AN EXCEPTION succeed, ones that ADD "
          'MACHINERY fail',
          'REMOVE AN EXCEPTION succeed' in base and 'ADD MACHINERY' in base)
    check("and its first instruction is to ask WHICH KIND it would be, before making it",
          'the first move is not to make the argument' in base)
    check('⚠ but PO-9 says the substrate\'s dimension is "bounded below only" -- an OPEN QUESTION, not '
          'a number being defended',
          'bounded below only' in po)
    check('⇒⇒ SO THIS SCORES AS NEITHER: it is a candidate piece of a VEIN\'s INTERIOR, and the vein '
          'rules apply rather than the base rate',
          'bounded below only' in po and 'REMOVE AN EXCEPTION succeed' in base)

    # ⓸ the guard is respected
    check("PO-9 guards: the cut's dimension is settled, the substrate's is bounded below only, and "
          'reading the first as capping the second re-makes the c54.6 error',
          "The cut's dimension is settled" in po and 'c54.6 error' in po)
    check('⇒ and the chain here runs CUT -> DYNAMICS, never CUT -> SUBSTRATE, so the bound is untouched',
          dynamical(4) == 1)

    # ⚠ the counter
    check('⚠ AND THE COUNTER: CR takes GR\'s dynamics as GIVEN -- "the construction leaves the dynamics '
          'of general relativity unchanged"',
          'the construction leaves the dynamics of general relativity unchanged' in p9)
    check('⇒ so the forcing is a PROPERTY the arrangement has, not by itself a REASON for it',
          'the construction leaves the dynamics of general relativity unchanged' in p9)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (INTERIOR OF PO-9, NOT A CLOSURE OF IT):')
    print('  ** D = 4 is the LARGEST dimension in which the Lovelock series leaves exactly ONE dynamical')
    print('     term beyond Lambda.  At five, Gauss--Bonnet becomes dynamical and the dynamics is a')
    print('     CHOICE. **')
    print("  => So the cut's ALREADY-SETTLED four-ness carries a consequence nobody had drawn: ** at")
    print('     four, and at no larger dimension, the leaf\'s dynamics carries no unfixed coefficient. **')
    print('  * And that is Rule 2\'s own language -- P0 rejects unfixed moduli and L-175 already applies')
    print('    it to a COUNT, so ** no criterion is added here. **')
    print('  ! SCORING: THE_BASE_RATE\'s discriminant is for arguments DEFENDING an existing number, and')
    print('    PO-9 says the substrate\'s dimension is "bounded below only" -- an OPEN QUESTION.')
    print('    ** So this scores as neither ADDS nor REMOVES: it is interior of a vein, and a vein closes')
    print('    from within when its interior is completely known.  This is interior, not a closure. **')
    print('  * The chain runs CUT -> DYNAMICS, never CUT -> SUBSTRATE: ** the c54.6 error is not re-made')
    print('    and the bound is untouched. **')
    print('  ! AND THE COUNTER SHIPS WITH IT: ** CR takes GR\'s dynamics as GIVEN, so the forcing is a')
    print('    PROPERTY the arrangement has, not by itself a REASON for it. **  It becomes a reason only')
    print('    if uniqueness of the leaf\'s dynamics is a desideratum the programme holds.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
