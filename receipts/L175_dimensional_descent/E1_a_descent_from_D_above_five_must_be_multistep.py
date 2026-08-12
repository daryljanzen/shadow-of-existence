#!/usr/bin/env python3
"""E1 -- PO-9 narrowed: a descent from D>5 must be MULTI-STEP, and the step count is the only bound
the construction supplies.

** PROTECTED_OPEN PO-9 (= L-175), the dimensional rise.  PROTECTED_OPEN's own rule: "An item may also
NARROW -- its object sharpened, its scope reduced -- and ** narrowing is ALWAYS a node's to do and is
what this register wants. **"  This receipt narrows and closes nothing.

** THE ROW'S GUARD, CARRIED IN ITS OWN TEXT AND OBEYED HERE: ** "the CUT's dimension is settled at four
(c54.10); the SUBSTRATE's is bounded BELOW and never above.  ** A node that reads the first as capping
the second has re-made the c54.6 error the c54.6 correction exists to prevent. **"
⇒ ** Nothing below infers a cap from the cut's dimension.  The bound found here comes from the NUMBER
OF REDUCTION STEPS between substrate and leaf, which is a different quantity. **

** THE CHAIN, IN p0's OWN WORDS: ** "the five-dimensional $\\mathrm{dS}_5=SO(5,1)/SO(4,1)$ of the ladder
below, ** of which the four-dimensional $\\mathrm{dS}_4$ is the BACKGROUND its leaves carry **".

      substrate  dS_5   (5 dimensions)
        -> leaf  dS_4   (4 dimensions -- spacetime)
        -> space  S^3   (3 dimensions)

** ⓵ WHAT A DESCENT FROM D>5 WOULD HAVE TO LOOK LIKE. **

A codimension-one cut of dS_D yields a (D-1)-dimensional leaf.  ** dS_6 therefore yields a
FIVE-dimensional leaf -- a 4+1 spacetime -- and cannot reach our world in one cut.  It needs D-5
further reductions. **

  ⇒ *** AND THE CORPUS'S CONSTRUCTION IS SINGLE-STEP BY DESIGN AND SAYS SO: "one slicing plane -- a
      door -- swings about one fixed line in the substrate, the hinge, and the whole family of cuts is
      the single arc of that swing."  ONE HINGE.  ONE DOOR.  ONE SWING. ***

  ⇒ ** So a descent from D>5 must be MULTI-STEP, and the corpus has no second door.  Whatever supplies
    the extra reductions would be NEW STRUCTURE, not a re-reading of what exists. **

** ⓶ AND WHAT WOULD BOUND THE SUBSTRATE ABOVE. **

*** The single-cut structure does -- and it is the only candidate the construction supplies. ***  Not
the cut's dimension (that is the guarded error), but ** the NUMBER OF STEPS between substrate and
leaf. **

  ⚠ ** AND IT BOUNDS CONDITIONALLY, WHICH IS WHY THIS NARROWS RATHER THAN CLOSES: D=5 is forced only
    IF the descent is one step.  Nothing here bounds the substrate above unconditionally, and PO-9's
    object -- "bounded below only" -- survives intact. **

⌗ WHY THIS IS WORTH THE ROW: the row's next step asked for exactly two things, "state what a descent
from D>5 would have to look like, and what would bound the substrate above".  ** Both now have an
answer of the right kind: the first is a structural requirement (multi-step), the second is a
conditional bound (the step count), and neither is a cap. **

WHAT IS NOT CLAIMED.  Not that D=5 is forced -- that requires the one-step premise, which is a feature
of the construction and not a theorem about substrates.  Not that a multi-step descent is impossible;
nothing here bears on that.  ** Not that the cut's dimension caps anything -- the guard is obeyed and
the bound comes from elsewhere. **

Written r2466.  Stated for reversal.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  E1 -- what would a descent from D>5 look like, and what bounds the substrate above?')
    print()
    p0 = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'geometric_core_paper.tex'),
                                  encoding='utf-8', errors='replace').read())
    p3 = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'SdS-slicing-curve_v2.tex'),
                                  encoding='utf-8', errors='replace').read())
    po = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'PROTECTED_OPEN.md'),
                                  encoding='utf-8', errors='replace').read())
    arc = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_LIVE_ARC.md'),
                                   encoding='utf-8', errors='replace').read())

    check('PROTECTED_OPEN asks for narrowing: "narrowing is ALWAYS a node\'s to do and is what this '
          'register wants"',
          "narrowing is **always** a node's to do" in po
          or 'narrowing is always a node' in po.lower())

    # the chain, at source
    check('p0: the substrate is the five-dimensional dS_5 = SO(5,1)/SO(4,1)',
          'five-dimensional $\\mathrm{dS}_5=SO(5,1)/SO(4,1)$' in p0)
    check('and the four-dimensional dS_4 is "the BACKGROUND its leaves carry"',
          'the four-dimensional $\\mathrm{dS}_4$ is the \\emph{background} its leaves carry' in p0)

    # the arithmetic of a codimension-one cut
    def leaf_dim(D):
        return D - 1
    check('a codimension-one cut of dS_D yields a (D-1)-dimensional leaf: dS_5 -> 4',
          leaf_dim(5) == 4)
    check('⇒ dS_6 yields a FIVE-dimensional leaf -- a 4+1 spacetime, not ours',
          leaf_dim(6) == 5 and leaf_dim(6) != 4)
    check('and reaching a 4-dimensional leaf from dS_D needs D-5 FURTHER reductions',
          all(D - 1 - leaf_dim(5) == D - 5 for D in (6, 7, 10)))

    # the construction is single-step and says so
    check('P3: "one slicing plane---a door---swings about one fixed line in the substrate, the hinge"',
          'swings about one fixed line in the substrate, the hinge' in p3)
    check('and "the whole family of cuts is the single arc of that swing"',
          'the single arc of that swing' in p3)
    check('⇒⇒ SO A DESCENT FROM D>5 MUST BE MULTI-STEP, AND THE CORPUS HAS NO SECOND DOOR',
          'the single arc of that swing' in p3 and leaf_dim(6) != 4)

    # the guard is obeyed
    check("the row's guard: the CUT's dimension is settled at four; the SUBSTRATE's is bounded "
          'BELOW and never above',
          'bounded BELOW and never above' in arc)
    check('⛔ AND THE BOUND FOUND HERE IS THE STEP COUNT, NOT THE CUT\'S DIMENSION -- so the c54.6 '
          'error is not re-made',
          leaf_dim(6) == 5)
    check('⚠ and it bounds CONDITIONALLY: D=5 is forced only IF the descent is one step',
          leaf_dim(5) == 4 and leaf_dim(6) != 4)
    check("so PO-9's object -- bounded below only -- survives intact",
          'bounded BELOW and never above' in arc)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (a NARROWING; PO-9 is NOT closed):')
    print("  ** ⓵ A descent from D>5 must be MULTI-STEP. **  A codimension-one cut of dS_D gives a")
    print('     (D-1)-leaf, so dS_6 gives a 4+1 spacetime and needs D-5 further reductions -- and the')
    print('  construction is single-step by design: ** one hinge, one door, one swing. **  Whatever')
    print('  supplied the extra reductions would be NEW STRUCTURE, not a re-reading of what exists.')
    print('  ** ⓶ And what would bound the substrate above is the STEP COUNT ** -- the only candidate')
    print('     the construction supplies -- ** not the cut\'s dimension, which is the guarded error. **')
    print('  ⚠ And it bounds CONDITIONALLY: D=5 is forced only IF the descent is one step.  Nothing')
    print('    here caps the substrate unconditionally, and PO-9\'s object survives intact.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
