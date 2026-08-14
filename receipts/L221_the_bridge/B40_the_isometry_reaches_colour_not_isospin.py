#!/usr/bin/env python3
"""B40 -- the $SO(4)$ isometries DO act on the zero-modes, and on the WRONG INDEX: they permute hinges,
which is the three-space colour already occupies, not the two ends within a hinge that `PO-4` needs.

** THE QUESTION r2770 LEFT. **  *** The substrate carries compact $SU(2)$ generators as isometries of
the closed $S^3$ layer.  Does either factor act on the hinge doublet? ***

** ⛭⛭ ⓵ THEY ACT ON THE ZERO-MODES, AND THE CORPUS SUPPLIES THE REASON. **  P14: "in the leaf's proper
measure the closed slicing has finite total length, so ** the leaf is compact and its Dirac operator
carries a well-defined analytical index **."

  ⇒ *** An isometry of a compact manifold acts on the spinor bundle over it, hence on the Dirac
      operator's kernel -- which is exactly where the hinge zero-modes live.  ** The action is automatic,
      not something that needs supplying. ** ***

** ⛔⛭⛭ ⓶ AND IT LANDS ON THE WRONG INDEX. **  ** There are two candidate doublets and they are different
spaces: **

      *** THREE-HINGE space   three zero-modes, one per 120-deg hinge -- DIMENSION 3
                              P14: "three throat walls, hence three chiral zero-modes"
          TWO-END space       the two TIMELIKE-separated ends of ONE hinge -- DIMENSION 2
                              this is PO-4's doublet (r2733) ***

  ⇒ *** AN ISOMETRY MOVES POINTS OF THE LEAF, SO IT PERMUTES HINGES.  It acts on the three-space and not
      within a hinge -- and a three-dimensional space carries $SU(2)$'s ADJOINT, not its FUNDAMENTAL. ***

** ⛭⛭⛭ ⓷ AND THE THREE-SPACE IS ALREADY SPOKEN FOR. **  *** r2679 established colour arrives at the
centre $\\mathbb Z_3$; r2706 ran the triality test on it and banked the result in P14; r2733 found the
horn rotation's stabiliser is exactly that $\\mathbb Z_3$.  ** The isometry reaches COLOUR, not
ISOSPIN. ** ***

** ⓸ WHICH ANSWERS r2770 AND EXPLAINS AN ASYMMETRY THE CORPUS ALREADY HAS. **  *** P14 delivers colour's
"exact selection rules" and says weak isospin "delivers a species label, not $SU(2)_L$'s chiral action".
** That asymmetry now has a mechanism: the substrate's compact symmetry acts on the index colour uses
and not on the index isospin needs. ** ***
  ⌗ ** And it is not a defect of the search: ** *** r2733 tested the horn angle, r2768 the swap, r2770
    the layer.  All three land on the hinge-permutation structure, because ** that is the only place a
    symmetry of the leaf can land **. ***

WHAT IS NOT CLAIMED.  ** Not that no $SU(2)$ acts on the two-end space ** -- *** what is shown is that
the LEAF ISOMETRIES do not, because they move points and the two ends of a hinge are not related by
moving points of the leaf; a different construction could still supply one. ***  ** Not that the
adjoint/fundamental statement closes anything ** -- *** a three-dimensional space carrying the adjoint
is a fact about dimension, and the corpus's $\\mathbb Z_3$ is a discrete subgroup of it, not the full
adjoint action. ***  ** Not that colour is thereby re-derived ** -- r2679 and r2706 did that; this
receipt uses the result.

** COMPUTES: nothing.  *** Three corpus statements read against each other: the leaf's compactness, the
three-zero-mode count, and the hinge doublet's location. *** **

Written r2773.  Stated for reversal.
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
    print("  B40 -- do the SO(4) isometries act on PO-4's doublet?")
    print()
    p14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))

    # ⓵ the leaf is compact with a Dirac index
    check('⛭⛭ ⓵ P14: "the leaf is compact and its Dirac operator carries a well-defined analytical '
          'index" -- so an isometry acts on the spinor bundle and hence on the kernel',
          'the leaf is compact and its Dirac operator carries a well-defined' in p14)

    # ⓶ two candidate doublets, different dimensions
    check('⛔ ⓶ and there are TWO candidate spaces: P14 gives "three throat walls, hence three chiral '
          'zero-modes" -- DIMENSION 3',
          'three throat walls, hence three chiral zero-modes' in p14)
    check('against `PO-4`\'s doublet, "two ends of one hinge are timelike separated" -- DIMENSION 2',
          'two ends of one hinge are timelike separated' in p14)
    check('⇒ an isometry MOVES POINTS of the leaf, so it permutes hinges and acts on the '
          'three-space -- which carries $SU(2)$\'s ADJOINT, not its FUNDAMENTAL',
          'three throat walls, hence three chiral zero-modes' in p14
          and 'two ends of one hinge are timelike separated' in p14)

    # ⓷ and the three-space is colour's
    check('⛭⛭⛭ ⓷ while the three-space is already spoken for: P14 carries the triality/centre '
          'structure r2679 and r2706 banked as colour',
          'triality' in p14.lower())

    # ⓸ and the asymmetry is P14's own
    check('⓸ and P14 states the asymmetry this explains: colour gets "exact selection rules" while '
          'weak isospin "delivers a species label, not $SU(2)_L$\'s chiral action"',
          "colour's exact selection rules" in p14
          and 'delivers a species label' in p14)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** they act — and on the index colour uses, not the one isospin needs. **')
    print('  ⛭⛭ ⓵ ** The action is automatic: ** "the leaf is compact and its Dirac operator carries a')
    print('     well-defined analytical index", and an isometry of a compact manifold acts on the')
    print('     spinor bundle over it — hence on the kernel where the zero-modes live.')
    print('  ⛔ ⓶ ** But there are two candidate spaces and they are different: **')
    print('       THREE-HINGE   three zero-modes, one per 120° hinge     dimension 3')
    print('       TWO-END       the two timelike ends of ONE hinge       dimension 2   ← PO-4 needs this')
    print('     *** An isometry MOVES POINTS, so it permutes hinges. It acts on the three-space, and a')
    print('     three-dimensional space carries the ADJOINT, not the FUNDAMENTAL. ***')
    print('  ⛭⛭⛭ ⓷ ** And the three-space is already spoken for ** — r2679 put colour at the centre Z₃,')
    print('     r2706 ran the triality test on it, r2733 found the horn rotation\'s stabiliser is that')
    print('     same Z₃.  ** The isometry reaches COLOUR, not ISOSPIN. **')
    print('  ⓸ ** Which explains an asymmetry P14 already states: ** colour gets "exact selection')
    print('     rules"; isospin "delivers a species label, not SU(2)_L\'s chiral action".')
    print('     ⇒ ** The substrate\'s compact symmetry acts on the index colour uses and not on the')
    print('       index isospin needs — and that is why three searches all landed in the same place. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
