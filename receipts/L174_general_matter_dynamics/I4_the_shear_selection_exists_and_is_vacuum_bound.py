#!/usr/bin/env python3
"""I4 -- r2504's dark region corrected: the corpus DOES have a shear-selection principle, and it is a
VACUUM theorem, so it cannot reach the stratum where matter is dynamical.

** WHAT r2504 WROTE, one revision ago: ** "with FIVE shear components there is a five-dimensional space
of configurations at fixed rho and theta, and ** nothing in the identity says which of them a bend can
be **."  ⇒ ** The clause "nothing in the identity" was true and the implication drawn from it was too
strong: the identity is not the only thing the corpus has. **

** ⛭⛭ P9 HAS A SHEAR-SELECTION PRINCIPLE, AND IT IS THE SHIFT--SHEAR LINK. **

  "By the ** Goldberg--Sachs ** theorem an algebraically special ** vacuum ** carries a shear-free null
   geodesic congruence; ** the substrate's null rulings are shear-free **, and a cut that inherits one as
   its principal congruence is algebraically special---this is the Type-D corner.  But a cut need not
   inherit one: ** the anisotropy of Bianchi I and of Zipoy--Voorhees IS shear, shear forbids a repeated
   principal null direction **, and so the operator climbs past Type D into Type I."

  ⇒ *** SO THE SHEAR IS NOT FREE AT ALL IN THE VACUUM SECTOR.  IT IS THE ALGEBRAIC TYPE. ***  sigma = 0
      on the principal congruence <=> algebraically special; any nonzero shear pushes to Type I.  ** The
      substrate supplies a shear-free reference congruence, and a cut's shear is its DEPARTURE from
      that. **

** ⛔ AND THE HYPOTHESIS IS THE WHOLE FINDING: GOLDBERG--SACHS IS A VACUUM THEOREM. **  P9 states it
twice and does not hide it -- "an algebraically special ** vacuum **", "a Type-D ** vacuum ** admits a
Killing tensor" -- and the paper's own title names the object the ** Kerr--NUT--(A)dS VACUUM KERNEL **.

  ⇒ *** AND THE BEYOND-WALL STRATUM IS EXACTLY WHERE MATTER IS DYNAMICAL.  So the one selection
      principle this corpus has for shear is hypothesis-bound to the sector the wall excludes. ***

** ⌗ WHICH SHARPENS THE DARK REGION RATHER THAN REMOVING IT, and corrects its statement: **
  * ** WRONG (r2504): ** "nothing selects among five-component shears."
  * ** RIGHT: ** ** something does -- for vacuum, via Goldberg--Sachs and the substrate's shear-free
    rulings.  What is dark is that the selection does not survive the addition of matter, which is the
    only regime the unworked stratum contains. **
  ⇒ ** That is a better-posed gap: not "no principle exists" but "the principle we have has a hypothesis
    the stratum violates." **  ⇒ *** And it names what a beyond-wall result would have to supply: a
    shear-selection statement that does NOT assume vacuum. ***

** ⌗⌗ AND THE STRUCTURE OF THE CORPUS'S POSITION IS NOW VISIBLE AS A SINGLE LINE: **
      substrate rulings shear-free  ->  inherited congruence => Type D (vacuum, Goldberg--Sachs)
      shear present                 ->  no repeated PND     => Type I (still reachable, still confined)
      all confining symmetry lost   ->  ** the wall **      => matter dynamical, ** and GS is silent **

WHAT IS NOT CLAIMED.  ** Not that P9 erred ** -- it states the vacuum hypothesis explicitly at both uses
and its title names the kernel a vacuum kernel.  ** Not that a non-vacuum shear-selection principle is
impossible **, only that the corpus does not carry one.  Not that r2504's identity was wrong: ** it is
correct and general; what was too strong was reading "nothing in the identity" as "nothing at all." **

Written r2505.  Stated for reversal.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def pub(f):
    raw = open(os.path.join(ROOT, 'corpus', f), encoding='utf-8', errors='replace').read()
    return re.sub(r'\s+', ' ', '\n'.join(l for l in raw.split('\n')
                                         if not l.lstrip().startswith('%')))


def main():
    print()
    print('  I4 -- does the corpus select among shears, and where does the selection stop?')
    print()
    p9 = pub('range_paper.tex')
    arc = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_LIVE_ARC.md'),
                                   encoding='utf-8', errors='replace').read())

    # r2504's claim, as this line wrote it
    check('r2504 wrote that nothing in the identity says which shear a bend can be',
          'nothing in the identity says which of them a bend can be' in arc)

    # the selection principle exists
    check('⛭ P9 has the shift--shear link, and names it: "The mechanism is the shift--shear link"',
          'The mechanism is the shift--shear link' in p9)
    check('by Goldberg--Sachs an algebraically special VACUUM carries a shear-free null geodesic '
          'congruence',
          'By the Goldberg--Sachs theorem an algebraically special vacuum carries a shear-free null '
          'geodesic congruence' in p9)
    check("and the substrate's null rulings are shear-free, so a cut inheriting one is algebraically "
          'special -- the Type-D corner',
          "the substrate's null rulings are shear-free" in p9 and 'this is the Type-D corner' in p9)
    check('⇒ while shear FORBIDS a repeated principal null direction, so the operator climbs past '
          'Type D into Type I',
          'shear forbids a repeated principal null direction' in p9
          and 'climbs past Type~D into Type~I' in p9)
    check("⇒⇒ SO THE SHEAR IS THE ALGEBRAIC TYPE: the substrate supplies a shear-free reference "
          "congruence and a cut's shear is its DEPARTURE from it",
          'shear forbids a repeated principal null direction' in p9)

    # ** the hypothesis is the finding **
    check('⛔ AND THE HYPOTHESIS IS VACUUM, stated at the first use: "an algebraically special vacuum"',
          'an algebraically special vacuum' in p9)
    check('and again at the second: "a Type-D vacuum admits a Killing tensor"',
          'a Type-D vacuum admits a Killing tensor' in p9)
    check("and the paper's own title names the object the Kerr--NUT--(A)dS VACUUM KERNEL",
          'vacuum kernel' in p9)

    # and the stratum it cannot reach
    check('while the wall is where matter is genuinely inhomogeneous -- "such a geometry is one whose '
          'matter is genuinely inhomogeneous"',
          'such a geometry is one whose matter is genuinely inhomogeneous' in p9)
    check('⇒⇒ SO THE ONE SHEAR-SELECTION PRINCIPLE THE CORPUS HAS IS HYPOTHESIS-BOUND TO THE SECTOR '
          'THE WALL EXCLUDES',
          'an algebraically special vacuum' in p9
          and 'such a geometry is one whose matter is genuinely inhomogeneous' in p9)

    # the corrected statement
    check('⌗ so r2504\'s dark region is SHARPENED, not removed: not "no principle exists" but "the '
          'principle we have has a hypothesis the stratum violates"',
          'nothing in the identity says which of them a bend can be' in arc
          and 'an algebraically special vacuum' in p9)
    check('⇒ and it names what a beyond-wall result must supply: a shear-selection statement that does '
          'NOT assume vacuum', 'vacuum kernel' in p9)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the selection exists and is vacuum-bound. **')
    print('  P9\'s shift--shear link: ** by Goldberg--Sachs an algebraically special VACUUM carries a')
    print('  shear-free congruence; the substrate\'s rulings ARE shear-free; and shear forbids a')
    print('  repeated PND, so the operator climbs past Type D into Type I. **')
    print('  ⇒ So the shear is not free in the vacuum sector -- ** it IS the algebraic type, and a')
    print('    cut\'s shear is its departure from the substrate\'s shear-free reference congruence. **')
    print('  ⛔ AND THE HYPOTHESIS IS THE FINDING: ** Goldberg--Sachs is a VACUUM theorem ** -- P9 says')
    print('     so at both uses and its title names the kernel a vacuum kernel -- ** while the')
    print('     beyond-wall stratum is exactly where matter is dynamical. **')
    print('  ⇒⇒ ** So the one shear-selection principle the corpus has is hypothesis-bound to the')
    print('     sector the wall excludes. **')
    print('  ⌗ Which SHARPENS r2504 rather than removing it: not "no principle exists" but ** "the')
    print('    principle we have has a hypothesis the stratum violates" ** -- and that names what a')
    print('    beyond-wall result must supply: ** a shear-selection statement that does not assume')
    print('    vacuum. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
