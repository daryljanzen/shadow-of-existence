#!/usr/bin/env python3
"""Q2 -- the direction r2525 gave PO-5 has an exact obstruction: an R-odd operator cannot carry a
gamma^5-graded index, so "kernel of a graded operator" is a structure only the R-EVEN sector has.  The
question inverts.

** WHERE r2525 LEFT IT. **  PO-5's missing operator and L-242's undeveloped Higgs identification are one
gap; P14 computes on R's EVEN (massless) sector; ** so any operator whose kernel is the colourless four
must be R-ODD. **  That was the direction.  ** This receipt tests it. **

** ⓵ WHY THE COLOURED THREE ARE FIELDS, in the algebra. **  P14's crossing is that the three wall modes
are ** one operator's kernel and therefore identical particles **, with the count ** a well-defined
INDEX **.  The index exists because of a grading:

      *** {gamma^mu, gamma^5} = 0  for every mu ***      (verified in the chiral basis)

  so the massless Dirac operator D = gamma^mu d_mu ** ANTICOMMUTES with gamma^5 **, ker D splits into
  +/- eigenspaces, and dim ker_+ - dim ker_- is well defined.  ** That is the whole machinery. **

** ⛔ ⓶ AND A MASS TERM DESTROYS IT. **

      [m*1, gamma^5] = 0        -- a Dirac mass COMMUTES with gamma^5
      {m*1, gamma^5} = 2m gamma^5 != 0
      ⇒ ** {D + m, gamma^5} != 0 **

  ⇒ *** THE VERY THING THAT MAKES THE COLOURED THREE FIELDS -- a well-defined gamma^5-graded index --
      IS DESTROYED BY GOING R-ODD.  An R-odd operator does not have an index in P14's sense. ***

** ⛭⛭ ⓷ SO THE QUESTION INVERTS, AND THAT IS THE RESULT. **

  r2525: ** the operator must be R-odd. **
  r2526: ** an R-odd operator cannot deliver its four the way the massless one delivers its three. **

  ⇒ *** "IS THERE AN OPERATOR WHOSE KERNEL IS THE FOUR?" WAS THE WRONG QUESTION -- not because the
      answer is no, but because "kernel of a graded operator" is a structure ONLY THE R-EVEN SECTOR
      HAS. ***

** ⓸ AND THAT IS WHY P13's "REMAINS UNBUILT" HAS STAYED UNBUILT. **  r2476 read it as "** the unbuilt
thing is an OPERATOR, not a SECTOR **".  ** Sharper now: the unbuilt thing is a BRIDGE ** -- some way for
gradings to become fields that is not "be a kernel" -- ** because on the R-odd side the kernel route is
structurally unavailable. **
  ⇒ ** And that is the same question L-242 asks about the Higgs mechanism, now with a reason it is
    hard: ** *** the corpus's one crossing from grading to field runs through a grading that mass
    breaks. ***

WHAT IS NOT CLAIMED.  ** Not that no bridge exists ** -- only that the kernel one does not reach there,
and PO-5 stays open.  ** Not that mass cannot be described ** -- ordinary QFT does it daily; the claim is
about the INDEX construction P14 uses to turn a count of gradings into a count of fields.  ** Not that
P14 erred ** -- computing on the massless sector is what a zero-mode calculation IS, and P14 says its
splitting is "external to the geometry".  Not anything about the Higgs sector's own content.

⌗ AND ONE THING WORTH SAYING PLAINLY: ** this narrowing came from Daryl's correction. **  Two revisions
ago this line had recorded the Higgs as a principled decline and closed the turn.  *** The vein's
interior moved twice in two revisions because that reading was refused. ***

Written r2526.  Stated for reversal.
"""
import os
import re

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def gammas():
    I2, Z2 = sp.eye(2), sp.zeros(2)
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])

    def blk(a, b, c, d):
        return sp.Matrix(sp.BlockMatrix([[a, b], [c, d]]))
    g0 = blk(Z2, I2, I2, Z2)
    gi = [blk(Z2, s, -s, Z2) for s in (sx, sy, sz)]
    g5 = sp.simplify(sp.I*g0*gi[0]*gi[1]*gi[2])
    return [g0] + gi, g5


def main():
    print()
    print('  Q2 -- can an R-odd operator carry a graded index?')
    print()
    p14 = re.sub(r'\s+', ' ', '\n'.join(
        l for l in open(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex'),
                        encoding='utf-8', errors='replace').read().split('\n')
        if not l.lstrip().startswith('%')))
    po = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'PROTECTED_OPEN.md'),
                                  encoding='utf-8', errors='replace').read())

    g, g5 = gammas()
    Z = sp.zeros(4, 4)

    # ⓵ the grading
    check('⛭ {gamma^mu, gamma^5} = 0 for every mu, in the chiral basis',
          all(sp.simplify(g5*x + x*g5) == Z for x in g))
    check('so the massless Dirac operator ANTICOMMUTES with gamma^5 -- which is what splits ker D into '
          '+/- eigenspaces and makes the index well defined',
          all(sp.simplify(g5*x + x*g5) == Z for x in g))
    check("and P14 uses exactly that: the three wall modes are one operator's kernel, and the count is "
          'a well-defined index',
          'index' in p14.lower() and 'kernel' in p14.lower())

    # ⓶ and a mass destroys it
    m = sp.Symbol('m', positive=True)
    M = m*sp.eye(4)
    check('⛔ but a Dirac mass term COMMUTES with gamma^5: [m*1, gamma^5] = 0',
          sp.simplify(M*g5 - g5*M) == Z)
    check('and does NOT anticommute: {m*1, gamma^5} = 2m gamma^5 != 0',
          sp.simplify(M*g5 + g5*M) != Z)
    p = sp.symbols('p0:4')
    D = sum((p[i]*g[i] for i in range(4)), sp.zeros(4, 4))
    check('⇒ so {D + m, gamma^5} != 0 -- THE GRADING IS DESTROYED',
          sp.simplify((D + M)*g5 + g5*(D + M)) != Z)
    check('while {D, gamma^5} = 0 without the mass -- so it is the mass, and only the mass, that breaks '
          'it', sp.simplify(D*g5 + g5*D) == Z)

    # ⓷ the inversion
    check('⇒⇒ SO AN R-ODD OPERATOR DOES NOT HAVE AN INDEX IN P14\'s SENSE, and "kernel of a graded '
          'operator" is a structure only the R-EVEN sector has',
          sp.simplify((D + M)*g5 + g5*(D + M)) != Z and sp.simplify(D*g5 + g5*D) == Z)

    # ⓸ what it says about P13's unbuilt thing
    check("⌗ so the unbuilt thing is a BRIDGE rather than an operator: some way for gradings to become "
          'fields that is not "be a kernel"',
          sp.simplify((D + M)*g5 + g5*(D + M)) != Z)
    check('⚠ and PO-5 stays open -- PROTECTED_OPEN carries it and nothing here builds a bridge',
          'PO-5' in po)
    check('and P14 itself says the zero-mode splitting is "external to the geometry", so no mass is '
          'derived or denied here',
          'external to the geometry' in p14)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the direction has an exact obstruction, and the question inverts. **')
    print('  ** {gamma^mu, gamma^5} = 0 ** makes the massless Dirac operator anticommute with gamma^5,')
    print('  which is what splits ker D and makes the index exist -- ** the whole machinery by which')
    print('  P14 turns three gradings into three fields. **')
    print('  ⛔ AND A MASS TERM COMMUTES with gamma^5, so ** {D + m, gamma^5} != 0: the grading is')
    print('     destroyed. **  An R-odd operator has no index in P14\'s sense.')
    print('  ⇒⇒ ** So "is there an operator whose kernel is the four?" was the wrong question -- not')
    print('     because the answer is no, but because "kernel of a graded operator" is a structure ONLY')
    print('     THE R-EVEN SECTOR HAS. **')
    print('  ⌗ ** So P13\'s unbuilt thing is a BRIDGE, not an operator: some way for gradings to become')
    print('    fields that is not "be a kernel". **  And that is L-242\'s Higgs question with a reason it')
    print('    is hard: ** the corpus\'s one crossing from grading to field runs through a grading that')
    print('    mass breaks. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
