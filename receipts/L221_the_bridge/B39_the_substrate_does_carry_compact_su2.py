#!/usr/bin/env python3
"""B39 -- the substrate DOES carry compact $SU(2)$ generators: $S^3$'s isometry group is
$SO(4)=(SU(2)_L\\times SU(2)_R)/\\mathbb Z_2$.  `PO-4`'s question is not whether one exists but whether
it acts on the hinge doublet.

** ⓵ r2769 LEFT THE ROW A KIND QUESTION: does anything on this substrate RANGE continuously and
compactly? **  *** Enumerated: ***

      *** T           the slicing time          non-compact
          r           the signed areal radius   non-compact
          chi         the hinge rapidity        non-compact          (r2733)
          horn angle  position on the throat    compact, quotiented to Z_3 by the 120-deg
                                                structure            (r2733)
          theta,phi   the S^2 angles            ⭑ COMPACT
          the S^3 layer's angles                ⭑ COMPACT -- NEVER TESTED ***

** ⛭⛭⛭ ⓶ AND THE ANSWER IS YES, BY A ROUTE NOTHING IN THE ROW HAD TAKEN. **  *** $S^3$'s isometry group
is $SO(4)=(SU(2)_L\\times SU(2)_R)/\\mathbb Z_2$.  ** The substrate carries compact $SU(2)$ generators --
twice -- as isometries of the closed spatial layer. ** ***

  ⌗ ** And the corpus knows the isometry group is not free: ** p0 -- "signature, null structure and
    ** isometry group being fixed by the absolute's projective type **".  *** The $SU(2)$s are not
    posited; they come with the layer. ***

** ⛔ ⓷ WHICH DOES NOT CLOSE THE ROW, AND THE REASON IS PRECISE. **  *** `PO-4` needs the $SU(2)$ that
acts on the ** HINGE DOUBLET ** -- the two timelike-separated ends of one hinge (r2733).  The $SO(4)$
generators act on the ** SPATIAL LAYER **.  ** Those are different spaces, and nothing yet connects
them. ** ***

** ⓸ SO THE ROW REFRAMES EXACTLY AS `PO-5` DID, AND THAT IS THE FINDING. **

      *** PO-5:  the corpus HAS dimensionless numbers (3, 6, 3/4, 9/10) -- the question is
                 whether any is a COUPLING.  r2729.
          PO-4:  the corpus HAS compact SU(2) generators (SO(4) on S^3) -- the question is
                 whether any acts on the HINGE DOUBLET. ***

  ⇒⇒ *** BOTH ROWS HAVE THE SAME SHAPE: the object exists and the ACTION is what is missing.  ** That
      is a narrowing on `PO-4` of exactly the kind r2729 was on `PO-5`, and it replaces "the substrate
      generates without rotating" (r2768) -- ** the substrate rotates; what is unshown is that it
      rotates the right thing **. ***

WHAT IS NOT CLAIMED.  ** Not that the $SO(4)$ $SU(2)$ is the isospin ** -- *** that is precisely the open
question, and asserting the identification would be the error r2718 made in the other direction. ***
** Not that r2768's "generates without rotating" was wrong in its own terms ** -- *** it was about what
acts on the DOUBLET, and this receipt does not supply that; it corrects the scope, which read as a
statement about the substrate. ***  ** Not that $SO(4)$ is derived here ** -- it is the standard isometry
group of the round $S^3$, and p0 states the isometry group is fixed by the projective type.

** COMPUTES: nothing.  *** An enumeration of the substrate's continuous parameters by compactness, and
the standard isometry group of the layer the corpus already names. *** **

Written r2770.  Stated for reversal.
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
    print("  B39 -- does anything on this substrate range continuously and compactly?")
    print()
    p0 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'geometric_core_paper.tex')))
    p10 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'canonical_time.tex')))
    p14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))

    # ⓵ the corpus names a closed S^3 layer
    check('⓵ the corpus names a closed $S^3$ layer: P10 speaks of "the closed-$S^{3}$ layer\'s '
          'propagating sector"',
          'closed-$S^3$ layer' in p10)

    # ⓶ and states the isometry group is not free
    check('⛭⛭⛭ ⓶ and p0 states the isometry group is not a choice: "signature, null structure and '
          'isometry group being fixed by the absolute\'s projective type"',
          'isometry group being fixed by the absolute' in p0)

    # ⓷ the doublet is the hinge, per P14
    check('⛔ ⓷ while `PO-4`\'s doublet is the HINGE: P14 puts the two-state object at "two ends of '
          'one hinge are timelike separated"',
          'two ends of one hinge are timelike separated' in p14)
    check('so the $SO(4)$ generators act on the SPATIAL LAYER and the isospin must act on the HINGE '
          '-- different spaces, and nothing yet connects them',
          'two ends of one hinge are timelike separated' in p14
          and 'closed-$S^3$ layer' in p10)

    # ⓸ and PO-5 has the same shape
    check('⓸ while `PO-5` has the same shape: P14 states its residue as needing "a fixed pure number '
          'rather than a free parameter" -- the numbers exist and the ACTION is what is missing',
          'a fixed pure number rather than a free parameter' in p14)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the substrate DOES carry compact SU(2) — the question is what it acts on. **')
    print('  ⓵ ** Enumerated by compactness: ** T, r and the rapidity are non-compact; the horn angle')
    print('     is compact but quotiented to Z₃ by the 120° structure (r2733); ** the S³ layer\'s')
    print('     angles are compact and were never tested. **')
    print('  ⛭⛭⛭ ⓶ ** And S³\'s isometry group is SO(4) = (SU(2)_L × SU(2)_R)/Z₂. **  *** The substrate')
    print('     carries compact SU(2) generators — twice — as isometries of the closed spatial layer,')
    print('     and p0 says the isometry group is "fixed by the absolute\'s projective type": they are')
    print('     not posited, they come with the layer. ***')
    print('  ⛔ ⓷ ** Which does not close the row: ** PO-4 needs the SU(2) that acts on the HINGE')
    print('     DOUBLET — "two ends of one hinge are timelike separated".  The SO(4) generators act on')
    print('     the SPATIAL LAYER.  ** Different spaces, and nothing yet connects them. **')
    print('  ⓸ *** SO THE ROW REFRAMES EXACTLY AS PO-5 DID: ***')
    print('       PO-5   the numbers exist (3, 6, 3/4, 9/10) — is any a COUPLING?        r2729')
    print('       PO-4   the generators exist (SO(4) on S³)  — does any act on the HINGE?')
    print('     ⇒ ** Both rows: the object exists and the ACTION is what is missing.  This replaces')
    print('       r2768\'s "the substrate generates without rotating" — ** the substrate rotates; what')
    print('       is unshown is that it rotates the right thing. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
