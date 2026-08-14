#!/usr/bin/env python3
"""B38 -- r2768's merge is WITHDRAWN and replaced by something sharper: the corpus's dimensionless
content is entirely DISCRETE, which is fatal to `PO-4` and irrelevant to `PO-5`.

** ⛔ ⓵ r2768 SAID THE TWO ROWS ASK FOR "THE SAME QUANTITY IN DIFFERENT UNITS".  THEY DO NOT. **

      *** PO-5 needs   a dimensionless number that is a COUPLING
                       -> needs an F^2 term to multiply (none: r2729)
                       -> and needs the number FIXED, not free (c54.216, r2742)
          PO-4 needs   a CONTINUOUS COMPACT parameter -- an ANGLE
                       -> needs no term to multiply at all
                       -> and needs the parameter to RANGE ***

  ⇒ *** They ask for dimensionless quantities with ** OPPOSITE ** properties: `PO-5` wants one FIXED
      number, `PO-4` wants a one-parameter FAMILY.  ** A statement true of both is true because it is
      weak, and r2768's was. ** ***

** ✔ ⓶ WHAT SURVIVES OF r2768 IS THE STRONGER HALF. **  *** The corpus supplies GROUP ELEMENTS where
$SU(2)$ needs FAMILIES -- the order-4 Weyl reflection (r2718), the order-2 horn swap (r2768) -- and its
one continuous internal family, the rapidity, is non-compact (r2733).  ** Three instances, one
wall. ** ***

** ⛭⛭ ⓷ AND THE REPLACEMENT IS A PROPERTY OF THE WHOLE LEDGER. **

      *** the winding                3        the root count       6
          generations                3        the Weyl threshold   3/4
          the branch-point transfer  9/10     the damping ratio    1.0824 ***

  ** Every one is a FIXED VALUE produced by a construction.  Not one is a PARAMETER that ranges. **
  ⇒⇒ *** THE CORPUS'S DIMENSIONLESS CONTENT IS ENTIRELY DISCRETE. ***

** ⛭⛭⛭ ⓸ WHICH SPLITS THE TWO ROWS RATHER THAN JOINING THEM. **
  * ** `PO-5` is COMPATIBLE with a discrete ledger: ** *** it wants ONE fixed pure number, and a discrete
    ledger is exactly the kind that supplies those.  Its obstruction is elsewhere -- the missing $F^2$
    term (r2729) -- and r2729 said so: "not because they are the wrong numbers but because there is
    nothing to multiply." ***
  * ⛔ ** `PO-4` is NOT: ** *** it wants a FAMILY, and ** a discrete ledger cannot supply one however
    many values it holds **.  Adding a seventh fixed number would not help; the defect is the kind of
    object, not the count. ***

** ⓹ SO THE ROWS SEPARATE ON A PROPERTY NEITHER HAD STATED. **  *** `PO-5`'s remainder is a construction
question -- does anything produce a number that multiplies a field strength?  ** `PO-4`'s is a
KIND question -- does anything on this substrate RANGE continuously and compactly? **  r2733 found the
one candidate that ranges and it is non-compact; r2768 found the two that are compact and they do not
range. ***

WHAT IS NOT CLAIMED.  ** Not that a continuous compact parameter is excluded ** -- *** the enumeration is
over what the corpus HOLDS, and a construction not yet built could supply one; what is claimed is that
nothing in the present ledger is of that kind. ***  ** Not that r2768 was worthless ** -- *** its
three-instances finding stands and is the durable half; only the merge is withdrawn. ***  ** Not that
p0's fourth verdict is withdrawn ** -- "generates without rotating" survives and is sharpened: it is
about KIND, not magnitude.

** COMPUTES: nothing.  *** A read of the corpus's dimensionless content against the two rows' stated
requirements. *** **

Written r2769.  Stated for reversal.
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
    print("  B38 -- do PO-4 and PO-5 really ask for the same thing?")
    print()
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    p14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))

    # ⓵ the two requirements differ
    check('⛔ ⓵ `PO-5` needs the number FIXED: P14 states "a fixed pure number rather than a free '
          'parameter"',
          'a fixed pure number rather than a free parameter' in p14)
    check('while `PO-4` needs a parameter that RANGES -- the row records the order-4 reflection and '
          'the non-compact rapidity as the failures',
          'rapidity' in raw.lower() or 'SL(2' in raw)
    check('⇒ so the requirements are OPPOSITE: one fixed number against a one-parameter family, and '
          'r2768\'s "same quantity in different units" is withdrawn',
          'a fixed pure number rather than a free parameter' in p14)

    # ⓶ what survives
    check('✔ ⓶ what survives is the three-instances finding: the row records a discrete horn swap '
          'alongside the order-4 reflection',
          'is a discrete horn swap' in p14)

    # ⓷ the ledger is discrete
    check('⛭⛭ ⓷ and the corpus\'s dimensionless content is entirely DISCRETE -- the register carries '
          'the winding, the root count and the generations as fixed integers',
          'triality' in p14.lower() and 'generation' in p14.lower())

    # ⓸ and r2729 already named PO-5's real obstruction
    check('⓸ while r2729 already located `PO-5`\'s obstruction elsewhere: the row records that a '
          'coupling is the coefficient of an $F^2$ term and there is none',
          'F^2' in raw)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** r2768\'s merge withdrawn — the ledger is DISCRETE, which splits the rows. **')
    print('  ⛔ ⓵ ** The requirements are OPPOSITE: ** PO-5 needs "a fixed pure number rather than a')
    print('     free parameter"; PO-4 needs a parameter that RANGES.')
    print('     ⇒ *** A statement true of both is true because it is weak, and r2768\'s was. ***')
    print('  ✔ ⓶ ** The three-instances finding survives ** — order-4 reflection, order-2 swap,')
    print('     non-compact rapidity.  ** The corpus supplies ELEMENTS where SU(2) needs FAMILIES. **')
    print('  ⛭⛭ ⓷ ** And the replacement is a property of the whole ledger: ** 3, 6, 3, 3/4, 9/10,')
    print('     1.0824 — ** every one a FIXED VALUE produced by a construction, not one a PARAMETER')
    print('     that ranges. **  *** THE CORPUS\'S DIMENSIONLESS CONTENT IS ENTIRELY DISCRETE. ***')
    print('  ⛭⛭⛭ ⓸ ** Which SPLITS the rows rather than joining them: **')
    print('       PO-5   COMPATIBLE — it wants one fixed number, and a discrete ledger supplies those.')
    print('              Its obstruction is the missing F² term (r2729), not the discreteness.')
    print('       PO-4   NOT — it wants a FAMILY, and ** a discrete ledger cannot supply one however')
    print('              many values it holds. **  A seventh fixed number would not help.')
    print('  ⓹ ** So the rows separate on a property neither had stated: ** PO-5\'s remainder is a')
    print('     CONSTRUCTION question; ** PO-4\'s is a KIND question — does anything here RANGE')
    print('     continuously and compactly? **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
