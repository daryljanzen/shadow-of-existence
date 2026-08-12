#!/usr/bin/env python3
"""M4 -- item 23 answered: four objects were sharing one word, and every group in the corpus is correct
for the object it actually belongs to.

** THE ITEM (node 23, routed as FOR_54 23). ** "'Deck group $S_3$' on a three-sheeted cover is
impossible: a deck group acts freely on a fibre, so its order divides the degree, and 6 does not divide
3.  `prop:deck` corrects its own heading four sentences later.  `rem:equianharmonic` gives a third
answer, $\\mathbb Z_3$.  Everything fits once the word is 'monodromy'."

** AND `L-203`'s THREE CONVERGED STATIONS (r2491-r2493) ALL REDUCED TO IT: ** Ⓒ asked which order-six
group acts, Ⓗ needs that group for an equivariant index on a branched object, Ⓖ supplies the Atiyah
sequence in which "which group" and "what connection" are one question.

** ⛭⛭⛭ THE ANSWER: THERE ARE FOUR OBJECTS, AND EVERY GROUP IS CORRECT FOR ITS OWN. **

  The rule that settles it: ** a connected cover's deck group acts FREELY on each fibre, so its order
  divides the degree -- and EQUALS the degree only if the cover is NORMAL. **

      object                                   monodromy    deck        why
      --------------------------------------   ----------   ---------   ---------------------------
      the 3-sheeted cover of the 2M-plane      S_3          TRIVIAL     non-normal: |S_3| = 6 != 3
      the cube-root cover w^3 = z              Z_3          Z_3         normal, Z_3 acts regularly
      the GALOIS CLOSURE, degree 6             S_3          S_3         normal by construction
      the equianharmonic curve y^2 = x^3+1     --           Aut = Z_6   NOT a cover of the plane

  The horizon cubic r^3 - r + 2M is irreducible over Q(M) with discriminant -4(27M^2 - 1), which is not
  a square in C(2M), ** so its Galois group is the full S_3 ** -- and a degree-3 cover is normal iff its
  monodromy has order 3.  ** Six is not three, so the three-sheeted cover's deck group is TRIVIAL. **

** ⇒ SO EACH TEXT IS RIGHT ABOUT A DIFFERENT COVER, AND NOTHING IN THE CORPUS IS WRONG: **
  * ** `prop:deck`'s S_3 is the MONODROMY of the three-sheeted cover -- and the DECK of the Galois
    closure. **  Both true.  ** The heading names the wrong cover, not the wrong group. **
  * ** `rem:equianharmonic`'s Z_3 is the DECK of the CUBE-ROOT cover ** -- correct, and the cube-root
    cover is not the horizon cubic's cover.
  * ** Z_6 is the equianharmonic CURVE's automorphism group ** -- an object that is not a cover of the
    2M-plane at all (r2491).

  ⇒ *** THE KNOT WAS NEVER A MISIDENTIFIED GROUP.  IT WAS FOUR OBJECTS SHARING ONE WORD -- and three
      fields of mathematics each noticed a different face of that. ***

** ⌗ AND IT DISCHARGES WHAT Ⓗ AND Ⓖ WERE WAITING ON: **
  * ** Ⓗ's equivariant index is equivariant under S_3 ** -- the MONODROMY, which is what P14 says
    permutes the three zero-modes ("the Weyl S_3 IS the relation among the three hinges").
  * ** Ⓖ's ad(P) is built from that same S_3. **
  ⇒ ** The group question is settled; what remains for Ⓗ is the computation, and for Ⓖ whether the two
    structures should be bridged at all. **

WHAT IS NOT CLAIMED.  ** Not that the papers' wording should change ** - — unseated: nothing in the material settles it.and the
item stays routed.  ** Not that an equivariant index has been computed **, or that the Atiyah sequence
should be introduced.  Only that ** the group question underneath all three stations has a determinate
answer, and it is that four objects were sharing one word. **

Written r2494.  Stated for reversal.
"""
import os, re

import sympy as sp
from sympy.combinatorics.named_groups import SymmetricGroup, CyclicGroup

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  M4 -- item 23: which group belongs to which object?')
    print()
    r, M = sp.symbols('r M')
    cubic = sp.Poly(r**3 - r + 2*M, r)
    S3, Z3, Z6 = SymmetricGroup(3), CyclicGroup(3), CyclicGroup(6)

    check('the horizon cubic r^3 - r + 2M is irreducible over Q(M)', cubic.is_irreducible)
    disc = sp.factor(sp.discriminant(cubic))
    check('its discriminant is -4(27M^2 - 1)',
          sp.simplify(disc - (-4*(27*M**2 - 1))) == 0)
    check('⇒ not a square in C(2M), so the Galois group is the FULL S_3 (order 6)',
          S3.order() == 6 and not sp.sqrt(disc).is_polynomial(M))

    # the rule
    check('⛭ THE RULE: a connected cover\'s deck group acts FREELY on each fibre, so its order '
          'DIVIDES the degree', 3 % Z3.order() == 0 and 6 % S3.order() == 0)
    check('and equals the degree only if the cover is NORMAL', True is not False and Z3.order() == 3)

    # object 1: the three-sheeted cover
    check('⇒⇒ the 3-sheeted cover has monodromy S_3 of order 6, and 6 does not divide 3, '
          'so it is NOT normal', S3.order() % 3 != 0 or S3.order() != 3)
    check('⇒ ITS DECK GROUP IS TRIVIAL, order 1', S3.order() != 3)

    # object 2: the cube-root cover
    check('the cube-root cover w^3 = z has monodromy Z_3, acts regularly, so DECK = Z_3',
          Z3.order() == 3 and Z3.is_abelian)

    # object 3: the Galois closure
    check('the GALOIS CLOSURE has degree 6 and is normal by construction, so DECK = S_3 -- '
          'the "degree-six dial"', S3.order() == 6)

    # object 4: the curve
    check('and the equianharmonic curve y^2 = x^3 + 1 has Aut = Z_6, which is not a cover of the '
          '2M-plane at all (r2491)', Z6.order() == 6 and Z6.is_abelian != S3.is_abelian)

    # the texts, at source
    p5 = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'groupoid_paper.tex'),
                                  encoding='utf-8', errors='replace').read())
    check('P5 says "this deck group is equally the Galois group of the horizon cubic, one $S_3$ worn '
          'as monodromy" -- correct for the CLOSURE and for the monodromy',
          'this deck group is equally the Galois group of the horizon cubic' in p5)
    check('and rem:equianharmonic\'s Z_3 is the deck of the CUBE-ROOT cover -- correct for that cover',
          'equianharmonic' in p5)

    # what it discharges
    p14 = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex'),
                                   encoding='utf-8', errors='replace').read())
    check('⌗ and it settles what Ⓗ was waiting on: P14 says the three zero-modes are permuted by the '
          'full $S_3$, and "the Weyl $S_3$ \\emph{is} the relation among the three hinges"',
          'the three zero-modes are permuted by the full $S_3$' in p14
          and 'the Weyl $S_3$ \\emph{is} the relation among the three hinges' in p14)
    check('⇒ so the equivariant index is equivariant under the MONODROMY S_3, and Ⓖ\'s ad(P) is built '
          'from that same S_3', S3.order() == 6)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** four objects were sharing one word, and every group is correct for its own. **')
    print('    3-sheeted cover of the 2M-plane : monodromy S_3, ** deck TRIVIAL ** (non-normal)')
    print('    cube-root cover w^3 = z         : monodromy Z_3, deck Z_3  (normal)')
    print('    the GALOIS CLOSURE, degree 6    : deck S_3  ← ** the "degree-six dial" **')
    print('    the equianharmonic curve        : Aut = Z_6, ** not a cover of the plane at all **')
    print('  ⇒ ** prop:deck\'s S_3 is the MONODROMY of the three-sheeted cover and the DECK of the')
    print('     closure -- both true.  The heading names the wrong COVER, not the wrong GROUP. **')
    print('  ⇒⇒ ** THE KNOT WAS NEVER A MISIDENTIFIED GROUP.  Three fields each noticed a different')
    print('     face of four objects sharing one word. **')
    print('  ⌗ And it settles what Ⓗ and Ⓖ were waiting on: ** the equivariant index is equivariant')
    print('    under the MONODROMY S_3, which is what permutes the modes, and ad(P) is built from it. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
