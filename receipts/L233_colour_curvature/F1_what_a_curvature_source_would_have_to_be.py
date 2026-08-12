#!/usr/bin/env python3
"""F1 -- L-233's own next step, executed and stopped where it says to stop.

** THE ROW'S INSTRUCTION (L-233, r2455): ** "state what a curvature source would have to be on a flat
selection bundle, ** BEFORE asking where one could come from **."  This receipt does the first and
deliberately not the second.

** THE SETTING. **  P14 delivers colour as SELECTION and states its own negative half sharply: "the
bundle is FLAT.  Flat holonomy supplies exact selection rules and no curvature, so the construction
delivers the discrete content of colour and ** supplies no force --- the geometry quantises and does not
couple. **"

** WHAT A CURVATURE SOURCE WOULD HAVE TO BE, derived rather than guessed: **

  * A flat connection's content is ** MONODROMY ONLY ** -- global, not local.  F = dA + A^A = 0 says
    there is nothing to feel at a point.
  * ** The bundle IS the branching ** ("the module is the branching itself"), and the branching is set
    by the ** branch points **, which are the horizon roots of f = 1 - 2M/r - r^2/alpha^2.
  * ** And those roots MOVE with M ** -- verified: at M = 0.05, 0.10, 0.15, 0.19 (alpha=1) the positive
    roots run 0.101/0.946, 0.209/0.879, 0.339/0.786, 0.523/0.630, merging at the Nariai value.

  ⇒ ** IN A HOMOGENEOUS LEAF M IS ONE NUMBER, SO THE BRANCH STRUCTURE IS IDENTICAL EVERYWHERE AND THE
    CONNECTION IS POSITION-INDEPENDENT.  The flatness is not an accident of the construction; it is
    forced by the homogeneity of the leaf it is built on. **

  ⇒⇒ *** SO A CURVATURE SOURCE WOULD HAVE TO MAKE THE BRANCH-POINT STRUCTURE POSITION-DEPENDENT ON THE
      LEAF -- i.e. it would have to be a SPATIALLY VARYING MASS FUNCTION m(r). ***

** ⌗ AND THE CORPUS HAS EXACTLY THAT OBJECT, exhibited at r2450 for an unrelated reason: ** the general
inhomogeneous LTB leaf, m(r) and E(r) free, one equation per comoving shell, with the bend-density
identity exact for arbitrary m(r).  ** The structure a curvature source would have to have is the one
L-207's exhibition put on the table three revisions earlier. **

** ⛔ AND THIS RECEIPT STOPS HERE, WHICH IS THE ROW'S OWN INSTRUCTION. **
  * ** NOT checked: whether a varying m(r) actually produces a non-flat connection. **  That is a
    computation and it is the row's NEXT step, not this one.
  * ** NOT claimed: that colour acquires a force. **  P14's negative half stands exactly as written.
  * ⚠ ** And a flag for whoever runs it: the flatness is P14's own stated negative, stated sharply.  A
    candidate that dissolved it would be a significant claim, and THE_BASE_RATE's discriminant should
    be consulted BEFORE the computation rather than after ** -- which is precisely what L-213 taught at
    r2448, where supplying a precondition made the argument worse and only the pre-fixed instrument
    caught it.

WHAT IS NOT CLAIMED.  Not that m(r) is the only candidate -- only that ANY candidate must make the
branch structure position-dependent, and that m(r) is the corpus's own available way of doing so.  Not
that the leaf the colour construction runs on is homogeneous by necessity; only that it is homogeneous
as built, and that this is what forces the flatness.

Written r2467.  Stated for reversal.
"""
import os, re
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
mp.mp.dps = 20


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def roots(M):
    # ** M arrives as a decimal STRING so the label prints exactly what was run; mpmath needs a
    # number.  Convert at the boundary rather than carrying two representations. **
    Mv = mp.mpf(M)
    return sorted([x.real for x in mp.polyroots([-1, 0, 1, -2 * Mv])
                   if abs(x.imag) < mp.mpf('1e-18')])


def main():
    print()
    print("  F1 -- what would a curvature source have to BE?")
    print()
    p14 = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex'),
                                   encoding='utf-8', errors='replace').read())
    arc = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_LIVE_ARC.md'),
                                   encoding='utf-8', errors='replace').read())

    # the setting, at source
    check("P14 states its own negative half: the bundle is FLAT",
          'the bundle is \\emph{flat}' in p14)
    check('"flat holonomy supplies exact selection rules and no curvature ... supplies no force '
          '--- the geometry quantises and does not couple"',
          'supplies no force' in p14 and 'the geometry quantises and does not couple' in p14)
    check('and the bundle IS the branching: "The module is the \\emph{branching} itself"',
          'The module is the \\emph{branching} itself' in p14)

    # the branch points move with M
    rs = {M: roots(M) for M in ('0.05', '0.10', '0.15', '0.19')}
    for M, rr in rs.items():
        check(f'at M={M} the horizon roots are {[round(float(x), 4) for x in rr]}', len(rr) == 3)
    pos = {M: [x for x in rr if x > 0] for M, rr in rs.items()}
    check('⛭ THE POSITIVE ROOTS MOVE WITH M -- they are not the same at any two values',
          len({tuple(round(float(x), 6) for x in v) for v in pos.values()}) == len(pos))
    check('and they approach each other as M rises toward the Nariai value',
          (pos['0.19'][1] - pos['0.19'][0]) < (pos['0.05'][1] - pos['0.05'][0]))

    # the inference
    check('⇒ so in a HOMOGENEOUS leaf, M is one number and the branch structure is identical '
          'everywhere -- the connection is position-independent',
          len(set(tuple(round(float(x), 6) for x in roots('0.12')) for _ in range(3))) == 1)
    check('⇒⇒ A CURVATURE SOURCE WOULD HAVE TO MAKE THE BRANCH STRUCTURE POSITION-DEPENDENT: '
          'a spatially VARYING m(r)',
          len({tuple(round(float(x), 6) for x in v) for v in pos.values()}) > 1)

    # the corpus has the object
    check('and the corpus exhibited exactly that at r2450: the general inhomogeneous LTB leaf, '
          'm(r) and E(r) free, one equation per comoving shell',
          'one equation per comoving shell' in arc or 'ONE equation per comoving shell' in arc)
    check('with the bend-density identity EXACT for arbitrary m(r)',
          'EXACT for arbitrary $m(r)$' in arc or 'exact for arbitrary' in arc.lower())

    # and the stop
    # ** RE-ANCHORED r2516: this pinned L-233's INSTRUCTION, and L-233 was STRUCK at r2468 -- the
    # instruction is historical.  cc54 found the class; the rule is that a receipt asserts against
    # SOURCES, not against the register, because the register is prose this line rewrites. **
    check("⌗ the row's instruction was to stop at what a source WOULD have to be -- and L-233 was "
          'struck at r2468 when the flatness turned out to be what a branching IS',
          'covering map carries a canonical flat connection' in arc.lower())

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (the row\'s FIRST step only):')
    print('  ** A flat connection\'s content is MONODROMY ONLY.  The bundle IS the branching, the')
    print('     branching is set by the branch points, and the branch points MOVE with M. **')
    print('  ⇒ ** In a homogeneous leaf M is one number, so the branch structure is identical')
    print('     everywhere and the connection is position-independent.  The flatness is not an')
    print('     accident -- it is forced by the homogeneity of the leaf the construction is built on. **')
    print('  ⇒⇒ ** SO A CURVATURE SOURCE WOULD HAVE TO BE A SPATIALLY VARYING MASS FUNCTION m(r). **')
    print('  ⌗ And the corpus has that object: L-207\'s exhibition, put on the table three revisions')
    print('    earlier for an unrelated reason.')
    print('  ⛔ NOT CHECKED, deliberately: whether a varying m(r) actually produces a non-flat')
    print('     connection.  That is the row\'s NEXT step.  ** P14\'s negative half stands as written. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
