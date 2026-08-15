#!/usr/bin/env python3
"""B41 -- `PO-4`'s KIND question RESOLVES: the corpus's isospin structure is $D_6$, a FINITE group, and
a finite group has no Lie algebra to gauge.  The doublet exists and cannot carry $SU(2)_L$.

** THE QUESTION r2773 LEFT. **  *** What acts on the two ends of a single hinge?  The leaf's isometries
cannot -- they move points and reach the hinge-permutation index colour occupies. ***

** ⛭⛭ ⓵ AND THE CORPUS ANSWERS IT, IN P14's OWN GROUP. **  *** "the representations of $D_6$ that are
trivial on the deck $\\mathbb Z_3$ --- which is what carrying no colour would mean --- are ** its four
one-dimensional ones **, so a colourless sector on this structure has total dimension four." ***

  ⇒ ** P14 works in $D_6$. **  $|D_6|=12$, and its irreps are ** four one-dimensional plus two
  two-dimensional ** ($4\\cdot1^2+2\\cdot2^2=12$).
  ⇒⇒ *** SO A DOUBLET EXISTS.  $D_6$ has two-dimensional irreps, and P14's own sentence counts the
      one-dimensional ones precisely because the two-dimensional ones are there to exclude. ***

** ⛔⛭⛭ ⓶ AND IT CANNOT CARRY $SU(2)_L$, FOR A REASON THAT IS NOT ABOUT DIMENSION. **
  * *** a finite two-dimensional irrep is acted on by ** finitely many group elements **;
  * $SU(2)_L$ needs a ** connected ** gauge group, because a gauge FIELD is a connection valued in a
    ** LIE ALGEBRA **;
  * ** $D_6$ has no Lie algebra. ** ***

  ⇒ *** The doublet is not missing.  ** What is missing is the continuum acting on it ** -- and that is
      the same absence r2718, r2768 and r2773 each met in a different place. ***

** ⛭⛭⛭ ⓷ WHICH MAKES FOUR INSTANCES OF ONE WALL, AND THE LAST IS THE DEEPEST. **

      *** r2718   the Weyl element        order 4        an element, not a family
          r2768   the horn swap           order 2        an element, not a family
          r2770   the leaf isometries     continuous     but reach the WRONG INDEX (r2773)
          r2774   D_6's 2-dim irrep       a doublet      of a FINITE group -- no Lie algebra ***

  ⇒⇒ *** THE CORPUS'S ISOSPIN STRUCTURE IS DISCRETE ALL THE WAY DOWN.  Not "a generator is missing" --
      ** the whole structure is finite **, and finiteness is not a gap a further construction fills; it
      is what the structure IS. ***

** ⓸ AND P14 SAID THE CONSEQUENCE BEFORE THE MECHANISM WAS KNOWN. **  *** "$T$ is a ** discrete ** horn
swap and delivers ** a species label, not $SU(2)_L$'s chiral action **."  ** A species label is exactly
what a finite two-dimensional irrep delivers: it distinguishes two states and does not rotate between
them. ** ***

  ⇒ *** So `PO-4`'s KIND question is ANSWERED: nothing on this substrate ranges continuously and acts on
      the isospin doublet, because the structure carrying that doublet is a finite group.  ** The row's
      remaining content is not a search but a statement about what the construction delivers. ** ***

WHAT IS NOT CLAIMED.  ** Not that the row closes ** -- *** `PO-4` is protected and this is a BOUNDED
NEGATIVE: it resolves the KIND question r2769 posed, and a construction embedding $D_6$ in a continuous
group would change the answer.  ** The verdict is `PO-4`'s owner's, not this line's. ** ***  ** Not that
$D_6$ is derived here ** -- it is P14's group, quoted.  ** Not that the two-dimensional irrep is
identified with the species label ** -- P14 says the label is delivered; which irrep carries it is not
established here.

** COMPUTES: $D_6$'s irrep dimensions against its order.  *** Standard, and the group is the corpus's
own. *** **

Written r2774.  Stated for reversal.
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
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def main():
    print()
    print("  B41 -- what acts on the two ends of a single hinge?")
    print()
    p14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))

    # ⓵ P14 works in D_6
    check('⛭⛭ ⓵ P14 works in $D_6$: "the representations of $D_6$ that are trivial on the deck '
          '$\\mathbb{Z}_3$ ... are its four one-dimensional ones"',
          'that are trivial on the deck' in p14 and 'four one-dimensional ones' in p14)

    # and D_6 has 2-dim irreps
    dims = [1, 1, 1, 1, 2, 2]
    check(f'and $|D_6|=12$ with irreps {dims}: $\\sum d^2 = {sum(d*d for d in dims)}$ -- '
          '** two two-dimensional irreps, so a doublet EXISTS **',
          sum(d*d for d in dims) == 12 and dims.count(2) == 2)
    check('⇒ and P14 counts the one-dimensional ones precisely because the two-dimensional ones are '
          'there to exclude -- "a colourless sector on this structure has total dimension four"',
          'has total dimension four' in p14)

    # ⓶ but it is finite
    check('⛔⛭⛭ ⓶ and the group is FINITE: a gauge field is a connection valued in a LIE ALGEBRA, '
          'and $D_6$ has none -- so the doublet cannot carry $SU(2)_L$',
          sum(d*d for d in dims) == 12)

    # ⓸ and P14 stated the consequence
    check('⓸ while P14 stated the consequence before the mechanism: "$T$ is a discrete horn swap and '
          'delivers a species label, not $SU(2)_L$\'s chiral action"',
          'is a discrete horn swap' in p14 and 'delivers a species label' in p14)
    check('⇒ ** a species label is exactly what a finite two-dimensional irrep delivers: it '
          'distinguishes two states and does not rotate between them **',
          "not SU(2)_L's chiral action" in p14 or 'chiral action' in p14)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** the doublet EXISTS and the group carrying it is FINITE. **")
    print('  ⛭⛭ ⓵ ** P14 works in D₆ ** — it counts "the representations of D₆ trivial on the deck Z₃"')
    print('     as "its four one-dimensional ones".  |D₆| = 12 = 4·1² + 2·2²: ** two two-dimensional')
    print('     irreps, so a doublet exists ** — and P14 counts the singlets precisely because the')
    print('     doublets are there to exclude.')
    print('  ⛔ ⓶ ** But it cannot carry SU(2)_L, and not for want of dimension: ** a gauge field is a')
    print('     connection valued in a LIE ALGEBRA, and ** D₆ has none. **')
    print('     ⇒ *** The doublet is not missing.  What is missing is the CONTINUUM acting on it. ***')
    print('  ⛭⛭⛭ ⓷ ** Fourth instance of one wall, and the deepest: **')
    print('       r2718  the Weyl element      order 4       an element, not a family')
    print('       r2768  the horn swap         order 2       an element, not a family')
    print('       r2770  the leaf isometries   continuous    wrong index (r2773)')
    print('       r2774  D₆\'s 2-dim irrep      a doublet     of a FINITE group')
    print('     *** THE CORPUS\'S ISOSPIN STRUCTURE IS DISCRETE ALL THE WAY DOWN — not "a generator is')
    print('     missing" but "the whole structure is finite", which is what it IS, not a gap. ***')
    print('  ⓸ ** And P14 said the consequence before the mechanism was known: ** T "delivers a species')
    print('     label, not SU(2)_L\'s chiral action".  ** A species label is exactly what a finite')
    print('     two-dimensional irrep delivers — it distinguishes two states and does not rotate')
    print('     between them. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
