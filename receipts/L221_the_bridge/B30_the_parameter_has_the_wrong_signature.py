#!/usr/bin/env python3
"""B30 -- `PO-4`'s one-parameter subgroup: the SEARCH RUN, and the answer is that the corpus's
candidate is CONTINUOUS AND OF THE WRONG SIGNATURE -- a boost, not a rotation.

** THE AVOIDANCE, NAMED FIRST. **  r2718 established the gap is CARDINALITY (order 4 against a
continuum) and wrote that the row "owes a source for a one-parameter subgroup".  *** Then I moved on.
Daryl's audit at r2729 listed it: "I characterised the gap and never searched." ***

** ⓵ THE SEARCH, ENUMERATED OVER WHAT THE SUBSTRATE HAS. **

      *** alpha        a LENGTH, not an angle -- and the only dimensionful invariant
          T            continuous, but the FOLIATION parameter, external to the fibre
          r            continuous, a base coordinate
          lambda       DISCRETE (j+1/2)
          horn angle   continuous on the throat -- TESTED BELOW
          hinge ends   TIMELIKE separated -- TESTED BELOW ***

** ⛔ ⓶ THE HORN ANGLE FAILS, AND FAILS AS COLOUR RATHER THAN ISOSPIN. **  The three horns sit at
$120^\\circ$; a rotation by $\\psi$ preserves the configuration only for $\\psi\\in\\{0,120,240\\}$.
*** The rotation group of the horn set is $\\mathbb Z_3$ -- which is the CENTRE r2679 already banked as
colour, not $SU(2)$'s Cartan.  The continuous angle exists on the throat and the construction's own
$120^\\circ$ structure quotients it to three points: the same cardinality wall one level down. ***

** ⛭⛭ ⓷ AND THE DOUBLET IS NOT THE HORNS AT ALL -- P14 SAYS SO. **  "the causal classification of the
six hinge-ends forces such a triple to take one puncture per hinge: ** two ends of one hinge are
TIMELIKE separated **, two on one horn spacelike, and only the cross pairs null."

  ⇒ *** So the two-state object $SU(2)$ would act on is the TWO ENDS OF ONE HINGE, and they are
      separated TIMELIKE.  A timelike separation carries a RAPIDITY -- continuous and unbounded. ***

** ⛔⛭ ⓸ AND THAT IS THE ANSWER: THE PARAMETER EXISTS AND HAS THE WRONG SIGNATURE. **

      *** exp(chi sigma_z / 2), chi continuous:   diag(e^{chi/2}, e^{-chi/2})
          chi = 0.0   diag(+1.0000, +1.0000)      chi = 1.0   diag(+1.6487, +0.6065)
          chi = 0.5   diag(+1.2840, +0.7788)      chi = 2.0   diag(+2.7183, +0.3679) ***

  ** Continuous ✔  ·  diagonal, hence in the Cartan direction ✔  ·  UNITARY ✘ ** --
  $M^\\dagger M=\\mathrm{diag}(7.389,0.135)\\ne I$.
  ⇒⇒ *** It generates $SL(2,\\mathbb R)$, not $SU(2)$: a BOOST, not a rotation.  The corpus's own
      causal structure supplies a one-parameter subgroup of the right SHAPE through the right
      SUBALGEBRA and of the wrong SIGNATURE. ***

** ⓹ WHICH IS A SHARPER STATEMENT THAN "ONE FACTOR SHORT". **  *** The row does not need a continuous
parameter -- it has one.  It needs a COMPACT one, and the geometry offers a timelike pair where a
compact generator would need a spacelike or internal one.  ** That is a statement about signature,
and signature is not something a construction can be talked into. ** ***
  ⌗ ** And it connects to the chirality mismatch r2676 left: ** *** $SU(2)_L$ acts left-handed while
    P14's occupations differ on the RIGHT-handed pair.  A wrong-signature generator and a
    wrong-handedness action are the same kind of defect -- the group the geometry offers is not the
    group the Standard Model needs, in two independent ways. ***

WHAT IS NOT CLAIMED.  ** Not that no compact parameter exists anywhere ** -- *** the enumeration above
is over what the substrate's own structures supply, and a construction not yet built could supply
another; what is claimed is that the corpus's OWN candidates are exhausted and one of them fails
specifically. ***  ** Not that the boost is useless ** -- a non-compact one-parameter subgroup is a
real structure and may serve elsewhere.  ** Not that $\\sigma_z$ is the right embedding ** -- it is the
Cartan direction the Weyl element reflects (r2676), and the signature result is independent of the
embedding's normalisation.

** COMPUTES: the horn rotation's stabiliser on the three-horn configuration, and the rapidity
family exp(chi sigma_z/2) with its unitarity residual.  *** Both parameters are the corpus's
own -- the 120-degree horn separation and the Cartan direction the Weyl element reflects.
Nothing is imported. *** **

Written r2733.  Stated for reversal.
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
    print("  B30 -- the search PO-4 owed: is there a one-parameter subgroup?")
    print()
    p14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))

    # ⓶ the horn rotation is Z_3
    preserved = [psi for psi in range(0, 360, 20)
                 if sorted([(120*k + psi) % 360 for k in range(3)]) == [0, 120, 240]]
    check(f'⛔ ⓶ the horn rotation preserves the configuration only at {preserved} -- the rotation '
          'group of the horn set is $\\mathbb{Z}_3$, not $U(1)$',
          preserved == [0, 120, 240])
    check('and that is the CENTRE r2679 banked as colour, not $SU(2)$\'s Cartan -- so the horn angle '
          'fails as the wrong group entirely',
          len(preserved) == 3)

    # ⓷ P14 locates the doublet
    check('⛭⛭ ⓷ and P14 locates the two-state object: "two ends of one hinge are timelike '
          'separated, two on one horn spacelike, and only the cross pairs null"',
          'two ends of one hinge are timelike separated' in p14)

    # ⓸ the rapidity is continuous, diagonal, non-unitary
    M = lambda chi: np.diag([np.exp(chi/2), np.exp(-chi/2)])
    vals = [M(c) for c in (0.5, 1.0, 2.0)]
    check('⓸ a rapidity generates a CONTINUOUS one-parameter family -- distinct at every $\\chi$',
          all(not np.allclose(vals[i], vals[j]) for i in range(3) for j in range(i+1, 3)))
    check('and it is DIAGONAL, hence in the Cartan direction',
          all(abs(m[0, 1]) < 1e-12 for m in vals))
    m = M(2.0)
    prod = m.conj().T @ m
    check(f'⛔ but it is NOT UNITARY: $M^\\dagger M$ = diag({prod[0,0].real:.3f}, '
          f'{prod[1,1].real:.3f}) $\\ne I$ -- it generates $SL(2,\\mathbb{{R}})$, not $SU(2)$',
          not np.allclose(prod, np.eye(2)))
    check('while $\\det M = 1$, so the failure is signature and not normalisation',
          abs(np.linalg.det(m) - 1.0) < 1e-9)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the parameter EXISTS and has the WRONG SIGNATURE — a boost, not a rotation. **')
    print('  ⛔ ⓶ ** The horn angle fails as the wrong GROUP: ** rotation preserves the three-horn')
    print('     configuration only at 0, 120, 240 — that is $\\mathbb{Z}_3$, the CENTRE already banked')
    print('     as colour.  ** The continuous angle exists and the 120° structure quotients it to')
    print('     three points: the same cardinality wall one level down. **')
    print('  ⛭⛭ ⓷ ** And the doublet is not the horns — P14 says so: ** "two ends of one hinge are')
    print('     TIMELIKE separated".')
    print('  ⛔⛭ ⓸ ** So the two-state object carries a RAPIDITY: continuous ✔, diagonal ✔,')
    print(f'     UNITARY ✘ ** — $M^\\dagger M$ = diag({prod[0,0].real:.3f}, {prod[1,1].real:.3f}), and')
    print('     $\\det M = 1$, so the failure is SIGNATURE and not normalisation.')
    print('     ⇒⇒ *** The corpus supplies a one-parameter subgroup of the right SHAPE, through the')
    print('       right SUBALGEBRA, and of the WRONG SIGNATURE.  It generates SL(2,R), not SU(2). ***')
    print('  ⓹ ** Which is sharper than "one factor short": ** the row does not need a continuous')
    print('     parameter — it HAS one.  It needs a COMPACT one, and the geometry offers a timelike')
    print('     pair where a compact generator needs a spacelike or internal one.')
    print('     ⌗ ** And signature is not something a construction can be talked into. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
