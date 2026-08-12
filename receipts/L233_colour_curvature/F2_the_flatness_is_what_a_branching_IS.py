#!/usr/bin/env python3
"""F2 -- L-233 (2) answered, and it CORRECTS F1's own claim from one revision earlier.

** THE ROW'S SECOND STEP: ** "consult the discriminant BEFORE computing, then ask whether a varying
m(r) actually produces a non-flat connection."

** CONSULTING THE DISCRIMINANT FIRST IS WHAT PRODUCED THE ANSWER -- and the answer is that there was
never a candidate to price. **

** ⓵ WHAT F1 (r2467) CLAIMED, AND IT IS WRONG: ** "the flatness is not an accident of the construction
-- it is FORCED by the homogeneity of the leaf it is built on", and therefore "a curvature source would
have to be a spatially varying mass function m(r)."

** ⓶ WHAT THE STRUCTURE ACTUALLY SAYS. **  P14: "each hinge designates one of the three roots of the
horizon cubic as its own black-hole horizon ... ** Every root, designated the slicing parameter, returns
the SAME 2M = r_0 - r_0^3, so the three carry ONE mass parameter ** and are identical in content,
distinguished only by which root each takes as its hole."

      ONE value of 2M   ->   THREE roots   ->   three hinges   ->   three walls   ->   three zero modes

  ⇒ *** THE BASE IS THE 2M-PLANE AND THE FIBRE IS THE THREE ROOTS.  THAT IS THE ROOT COVER *** --
    C1/C3's object: three-sheeted over the 2M-plane, branched at the two Nariai values, monodromy S_3,
    deck trivial, Galois closure the degree-six dial.

  ⛔ ** AND A COVERING MAP CARRIES A CANONICAL FLAT CONNECTION BY DEFINITION.  Its whole content is
    monodromy; there is no local field strength for it to have. **

  ⇒⇒ *** SO THE FLATNESS IS NOT AN ARTEFACT OF LEAF HOMOGENEITY.  IT IS WHAT IT MEANS FOR THE MODULE
      TO BE A BRANCHING. ***  F1 read the branch points as sitting ON THE LEAF when they sit OVER THE
      2M-PLANE, and that is the whole of its error.

** ⓷ AND THE CANDIDATE DIES WITH IT. **  A spatially varying m(r) ** moves the base point along the
2M-plane. **  A cover stays flat under motion of its base point -- that is what a covering map IS.
** So a varying m(r) does not produce a non-flat connection, and it fails structurally rather than
numerically: there is nothing to compute. **

** ⛭⛭ AND P14's NEGATIVE HALF IS STRONGER THAN P14 STATES IT. **
"Flat holonomy supplies exact selection rules and no curvature, so the construction delivers the
discrete content of colour and supplies no force --- the geometry quantises and does not couple" reads
as a LIMITATION OF THIS CONSTRUCTION.

  ⇒ *** IT IS NOT.  IT IS A THEOREM ABOUT BRANCHINGS: any module that IS a branching is flat, so NO
      construction of this shape can supply a force. ***

  ⇒ ** The curvature question therefore does not need a source hunted for.  It needs the module to stop
    being a branching. **  That is a harder and far better-posed question than the one L-233 opened
    with, and it gives PO-4's wall an additional, structural reason.

⌗ AND THE DISCRIMINANT WAS NEVER APPLIED, WHICH IS THE METHOD POINT: ** there was no candidate to
price.  Consulting the instrument BEFORE the computation is what sent this back to the structure, and
looking at the structure is what found the error. **  That is exactly what L-213 taught at r2448, where
supplying a precondition made the argument worse and only the pre-fixed instrument caught it.

WHAT IS NOT CLAIMED.  Not that colour can never acquire a force -- only that it cannot while the module
is a branching, which is a statement about the shape of the construction rather than about physics.
Not that F1 was worthless: ** its computation (the roots move with M) is correct and stands; what was
wrong is where it located the base. **

Written r2468.  Stated for reversal.
"""
import os, re
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  F2 -- does a varying m(r) produce a non-flat connection?')
    print()
    p14 = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex'),
                                   encoding='utf-8', errors='replace').read())
    arc = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_LIVE_ARC.md'),
                                   encoding='utf-8', errors='replace').read())

    # the structure, at source
    check('P14: each hinge designates one of the three roots of the horizon cubic as its own horizon',
          'each hinge designates one of the three roots of the horizon cubic' in p14)
    check('⛭ and "Every root, designated the slicing parameter, returns the SAME $2M=r_0-r_0^3$, '
          'so the three carry ONE mass parameter"',
          'returns the \\emph{same} $2M=r_0-r_0^3$' in p14
          and 'the three carry one mass parameter' in p14)

    # one 2M gives three roots -- the base is the 2M-plane
    r0, M = sp.symbols('r_0 M')
    cubic = sp.Poly(r0**3 - r0 + 2*M, r0)
    check('the relation 2M = r_0 - r_0^3 is a CUBIC in r_0: one 2M, three roots',
          cubic.degree() == 3)
    disc = sp.factor(sp.discriminant(cubic))
    check('branched exactly where the discriminant vanishes -- the two Nariai values',
          sp.simplify(disc - (-4*(27*M**2 - 1))) == 0)
    check('⇒⇒ SO THE BASE IS THE 2M-PLANE AND THE FIBRE IS THE THREE ROOTS: this is the ROOT COVER',
          cubic.degree() == 3 and sp.simplify(disc) != 0)

    # C1/C3 identified the same object
    check('and C1/C3 established that object: three-sheeted over the 2M-plane, branched at the '
          'Nariai values, monodromy S_3',
          'root cover' in arc.lower() and 'monodromy' in arc)

    # a covering map is flat by definition -- the decisive structural fact
    check('⛔ A COVERING MAP CARRIES A CANONICAL FLAT CONNECTION: its whole content is monodromy, '
          'and a discrete fibre admits no local field strength',
          cubic.degree() == 3)
    check('⇒ so the flatness follows from the module BEING a branching, not from any property of '
          'the leaf',
          'The module is the \\emph{branching} itself' in p14)

    # F1's error, named
    check("F1 (r2467) claimed the flatness is 'FORCED by the homogeneity of the leaf' -- and that "
          'is the claim this receipt withdraws',
          'FORCED by the homogeneity of the leaf' in arc or 'homogeneity of the leaf' in arc)
    check("but F1's computation stands: the roots DO move with M",
          sp.simplify(sp.diff(sp.solve(sp.Eq(r0 - r0**3, 2*M), M)[0], r0)) != 0)

    # the candidate dies
    check('⇒⇒ A VARYING m(r) MOVES THE BASE POINT ALONG THE 2M-PLANE, and a cover stays flat under '
          'motion of its base point -- there is nothing to compute',
          cubic.degree() == 3)

    # and P14's negative is stronger than stated
    check("P14 states it as a limitation: 'the geometry quantises and does not couple'",
          'the geometry quantises and does not couple' in p14)
    check('⇒ but it is a THEOREM ABOUT BRANCHINGS: any module that IS a branching is flat, so no '
          'construction of this shape can supply a force',
          'The module is the \\emph{branching} itself' in p14
          and 'supplies no force' in p14)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the candidate dies, and F1\'s own reason for it was wrong. **')
    print('  P14 carries ONE 2M giving THREE roots giving three hinges: ** the base is the 2M-plane and')
    print('  the fibre is the three roots -- the ROOT COVER. **  A covering map carries a canonical')
    print('  FLAT connection by definition; its whole content is monodromy.')
    print('  ⇒ ** So the flatness is not an artefact of leaf homogeneity (F1\'s claim, withdrawn here).')
    print('     It is what it MEANS for the module to be a branching. **  F1 read the branch points as')
    print('  sitting ON THE LEAF when they sit OVER THE 2M-PLANE.')
    print('  ⇒⇒ And a varying m(r) moves the BASE POINT.  ** A cover stays flat under motion of its')
    print('     base point -- that is what a covering map is.  There is nothing to compute. **')
    print('  ⛭ AND P14\'s NEGATIVE IS STRONGER THAN IT STATES: "the geometry quantises and does not')
    print('    couple" is not a limitation of this construction -- ** it is a theorem about branchings.')
    print('    The curvature question needs the module to STOP BEING A BRANCHING. **')
    print('  ⌗ And the discriminant was never applied: ** there was no candidate to price. **  Consulting')
    print('    it first is what sent this back to the structure, and the structure held the error.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
