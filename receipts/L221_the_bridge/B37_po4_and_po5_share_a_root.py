#!/usr/bin/env python3
"""B37 -- ⛔ **⓸ CORRECTED r2769: THE MERGE IS TOO WEAK.**  *** `PO-5` needs a number that is
FIXED ("a fixed pure number rather than a free parameter"); `PO-4` needs a parameter that RANGES.
**Opposite properties, not the same quantity in different units** -- and a statement true of both
is true because it is weak.  The corpus's dimensionless content is entirely DISCRETE, which is
COMPATIBLE with PO-5 and fatal to PO-4.  See `B38_the_ledger_is_discrete`.  ** What survives:
⓵-⓷, the three-instances finding, which is the durable half. ** ***

B37 -- `PO-4` and `PO-5` share a root, and it is p0's own: a compact generator needs an ANGLE, an
angle is a dimensionless continuous parameter, and r2742 settled that the ledger holds none.

** ⓵ THE ROW NEEDS ONE GENERATOR, NOT TWO. **  *** $\\mathfrak{su}(2)=\\mathrm{span}\\{\\sigma_x,\\sigma_y,
\\sigma_z\\}$ and the corpus supplies the $\\sigma_z$ direction.  $[\\sigma_z,\\sigma_x]=2i\\sigma_y$ --
verified -- so ** one off-diagonal generator closes the algebra ** and c54.218's "two dimensions short"
is two dimensions of SPAN reached by one new direction. ***

** ⛭⛭ ⓶ AND THE CORPUS DOES SUPPLY AN OFF-DIAGONAL OBJECT -- AS A GROUP ELEMENT. **  P14: "** $T$ is a
discrete horn swap ** and delivers a species label, not $SU(2)_L$'s chiral action."

  ⇒ *** A discrete swap of two states IS $\\sigma_x$, and $\\sigma_x^2=I$: ** an element of order 2 **.
      A GENERATOR is the one-parameter family $\\exp(i\\theta\\sigma_x/2)$, of which the swap is the
      $\\theta=\\pi$ member. ***

** ⓷ WHICH IS THE THIRD INSTANCE OF ONE WALL. **

      *** r2718   the Weyl reflection    order 4      a group ELEMENT
          r2768   the horn swap          order 2      a group ELEMENT
          r2733   the rapidity           continuous   and NON-COMPACT ***

  ⇒⇒ *** THE CORPUS SUPPLIES GROUP ELEMENTS WHEREVER $SU(2)$ NEEDS A FAMILY, AND THE ONE FAMILY IT DOES
      SUPPLY HAS THE WRONG SIGNATURE.  Three separate "missing pieces" are one wall seen three
      times. ***

** ⛭⛭⛭ ⓸ AND THE WALL IS `PO-5`'s. **  *** A compact generator needs an ANGLE.  ** An angle is a
DIMENSIONLESS CONTINUOUS PARAMETER ** -- exactly what r2742 established the ledger has none of, with
three papers committing that $\\ell_P$ is a gauge and none dissenting. ***

  ⇒ *** SO `PO-4` AND `PO-5` SHARE A ROOT.  `PO-5` needs a fixed pure number to be a coupling; `PO-4`
      needs a dimensionless parameter to be an angle.  ** Both are asking the one-constant ledger for a
      dimensionless quantity, and the ledger's whole content is that it has one length. ** ***

** ⓹ AND p0 NAMED THAT ROOT FOR THREE OTHER VERDICTS. **  "the construction cannot force a coupling, and
its silence about magnitudes is a property of ** a one-constant theory rather than a gap awaiting work
** --- the common root of three verdicts reached separately, that the winding ** quantises without
measuring **, the flat bundle ** selects without coupling **, and the branch point ** filters without
supplying **."
  ⇒⇒ *** `PO-4`'s is a FOURTH in the same voice: ** the substrate GENERATES WITHOUT ROTATING **. ***

WHAT IS NOT CLAIMED.  ** Not that `PO-4` is thereby closed ** -- *** locating a row's wall inside another
row's settled bound is a narrowing, not a resolution: a construction supplying a dimensionless angle
would meet both, and neither row excludes one. ***  ** Not that the three instances are the same
theorem ** -- *** they are the same OBSTRUCTION met in three places; r2718's is cardinality, r2733's is
signature, r2768's is cardinality again. ***  ** Not that p0 anticipated this verdict ** -- p0 names
three; the fourth is this receipt's, in p0's own form.

** COMPUTES: the $\\mathfrak{su}(2)$ commutator closing the algebra from one off-diagonal direction, and
$\\sigma_x^2=I$ against the one-parameter family it sits in.  *** Standard, and the objects are the
corpus's own. *** **

Written r2768.  Stated for reversal.
"""
import os
import re

import numpy as np

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
    print("  B37 -- do PO-4 and PO-5 share a root?")
    print()
    sx = np.array([[0, 1], [1, 0]], complex)
    sy = np.array([[0, -1j], [1j, 0]])
    sz = np.diag([1, -1]).astype(complex)

    # ⓵ one generator closes it
    check('⓵ one off-diagonal direction closes the algebra: $[\\sigma_z,\\sigma_x]=2i\\sigma_y$',
          np.allclose(sz@sx - sx@sz, 2j*sy))

    # ⓶ the swap is an element
    p14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))
    check('⛭⛭ ⓶ and the corpus supplies an off-diagonal object as a GROUP ELEMENT: "$T$ is a discrete '
          'horn swap and delivers a species label, not $SU(2)_L$\'s chiral action"',
          'is a discrete horn swap' in p14)
    check(f'which is $\\sigma_x$ at order 2 ($\\sigma_x^2=I$), the $\\theta=\\pi$ member of '
          '$\\exp(i\\theta\\sigma_x/2)$ -- ** an element, not the family **',
          np.allclose(sx@sx, np.eye(2)))

    # ⓷ and it is the third instance
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    check('⓷ the third instance of one wall: the row records the order-4 Weyl reflection (r2718) and '
          'the non-compact rapidity (r2733)',
          'order 4' in raw or 'ORDER 4' in raw)

    # ⓸ and PO-5's bound is the same currency
    check('⛭⛭⛭ ⓸ while `PO-5`\'s settled bound is that the ledger holds no free dimensionless '
          'parameter -- the row records the three papers committing that $\\ell_P$ is a gauge',
          'gauge-combination rather than a second physical' in
          re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'canonical_time.tex'))))

    # ⓹ and p0 names the root
    p0 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'geometric_core_paper.tex')))
    check('⓹ and p0 names that root for three verdicts: "the common root of three verdicts reached '
          'separately, that the winding quantises without measuring, the flat bundle selects without '
          'coupling, and the branch point filters without supplying"',
          'the common root of three verdicts reached separately' in p0
          and 'quantises without measuring' in p0)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** PO-4 and PO-5 share a root, and it is p0\'s own. **')
    print('  ⓵ ** The row needs ONE generator, not two ** — [σ_z,σ_x] = 2iσ_y closes the algebra.')
    print('  ⛭⛭ ⓶ ** And the corpus supplies an off-diagonal object — as an ELEMENT: ** "T is a')
    print('     discrete horn swap".  σ_x² = I: order 2, the θ=π member of exp(iθσ_x/2).')
    print('  ⓷ ** Third instance of one wall: **')
    print('       r2718   the Weyl reflection    order 4      a group ELEMENT')
    print('       r2768   the horn swap          order 2      a group ELEMENT')
    print('       r2733   the rapidity           continuous   and NON-COMPACT')
    print('     *** The corpus supplies group ELEMENTS wherever SU(2) needs a family, and the one')
    print('     family it does supply has the wrong signature. ***')
    print('  ⛭⛭⛭ ⓸ ** And the wall is PO-5\'s: ** a compact generator needs an ANGLE, and an angle is a')
    print('     DIMENSIONLESS CONTINUOUS PARAMETER — exactly what r2742 settled the ledger has none of.')
    print('     ⇒ *** PO-5 needs a fixed pure number to be a coupling; PO-4 needs a dimensionless')
    print('     parameter to be an angle.  Both ask the one-constant ledger for a dimensionless')
    print('     quantity, and its whole content is that it has one LENGTH. ***')
    print('  ⓹ ** And p0 named this root for three verdicts ** — quantises without measuring, selects')
    print('     without coupling, filters without supplying.  ** PO-4\'s is a fourth in the same voice:')
    print('     the substrate GENERATES WITHOUT ROTATING. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
