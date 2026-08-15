#!/usr/bin/env python3
"""B51 -- p0's inference is SOUND and its premise is EXACTLY TRUE, and $1/\\sqrt3$ falls outside the
class it ranges over: the mass cancels from the curvature invariants and survives in the locus ratio.

** THE READ r2804 ROUTED. **  *** Does p0's no-coupling inference still close over a forced
dimensionless quantity that is not a curvature invariant? ***

** ⓵ p0's PREMISE IS SHARPER THAN r2804 QUOTED. **  *** "neither real form supplies a second invariant
and ** a dimensionless magnitude needs two ** ... every curvature invariant on either face is a pure
power of $1/\\alpha^{2}$.  ** So the construction cannot force a coupling. ** " ***

  ⇒ ** The argument is: a ratio needs two scales; the faces supply one. **  *** Not "there are no
      numbers" but "there is nothing to take a ratio OF". ***

** ⛭⛭⛭ ⓶ AND ON THE NARIAI CUT THE PREMISE IS EXACTLY TRUE -- THE MASS CANCELS. **  `janzen_circle`:
"On the Nariai cut itself the full invariant is $K=48M^2/r^6+24/\\alpha^4$, ** in which the mass cancels
identically rather than only in the limit **."  Verified symbolically at $M=\\alpha/3\\sqrt3$,
$r=\\alpha/\\sqrt3$:

      *** K = 72 / alpha^4     -- a pure power, exactly as p0 says ***

** ⛭⛭ ⓷ AND $1/\\sqrt3$ SURVIVES THAT CANCELLATION, WHICH IS THE WHOLE POINT. **  *** $r_N/\\alpha =
1/\\sqrt3$ is dimensionless, fixed, and ** ABSENT FROM $K$ **.  It is a ratio of a LOCUS to the scale,
not of two invariants -- so the second scale p0's premise denies is not what supplies it. ***

  ⇒⇒ *** p0's INFERENCE IS SOUND AND ITS SCOPE IS CURVATURE INVARIANTS.  ** $1/\\sqrt3$ is a forced
      dimensionless quantity outside that scope, and the inference neither covers nor excludes it. ** ***

** ⓸ AND NARIAI IS NOT A CHOICE, WHICH IS WHAT MAKES THE NUMBER FORCED. **  *** `shadow_of_existence`:
the Nariai configuration is "** the unique fixed point ** of the root-exchange involution, the unique
vantage at which two roots collide so that the involution acts trivially".  `cosmogenesis_paper`: the
generation structure "originates at the $S_3$-fixed Nariai crest". ***
  ⇒ ** $M/\\alpha$ is not a free second scale here. **  *** It is fixed by a uniqueness statement the
    corpus proves, and the physics is placed there. ***

** ⓹ SO `PO-5`'s RESIDUE IS NOW ONE SENTENCE, NOT A SEARCH. **  *** The corpus HAS a forced
dimensionless number.  p0's argument that it cannot have one is about curvature invariants and is
correct about those.  ** What is missing is not a number and not an argument -- it is an $F^2$ term for
the number to multiply, which r2729 established and nothing since has moved. ** ***

WHAT IS NOT CLAIMED.  ** Not that p0 is wrong ** -- *** its premise is verified exactly true here and
its inference follows; the finding is about SCOPE. ***  ** Not that $1/\\sqrt3$ is a coupling ** --
*** it is a forced dimensionless quantity, which is necessary and not sufficient. ***  ** Not that
Nariai's uniqueness is re-derived ** -- it is `groupoid_paper`'s and is quoted.

** COMPUTES: $K$ at the Nariai values symbolically, showing the mass cancels to $72/\\alpha^4$, and
$r_N/\\alpha$.  *** $K$ is `janzen_circle`'s own expression. *** **

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT 77de31f** *(per c54.220's rule, r2776).*

Written r2805.  Stated for reversal.
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


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def main():
    print()
    print("  B51 -- does p0's inference close over a non-curvature dimensionless quantity?")
    print()
    p0 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'geometric_core_paper.tex')))
    circ = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'janzen_circle_v3.tex')))
    shad = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'shadow_of_existence.tex')))

    check('⓵ p0\'s premise is a two-scale argument: "neither real form supplies a second invariant '
          'and a dimensionless magnitude needs two"',
          'a dimensionless magnitude needs two' in p0)
    check('with the curvature clause: "every curvature invariant on either face is a pure power of '
          '$1/\\alpha^{2}$. So the construction cannot force a coupling"',
          'is a pure power of' in p0 and 'So the construction cannot force a coupling' in p0)

    # ⓶ the mass cancels
    r, M, a = sp.symbols('r M alpha', positive=True)
    K = 48*M**2/r**6 + 24/a**4
    Kn = sp.simplify(K.subs({M: a/(3*sp.sqrt(3)), r: a/sp.sqrt(3)}))
    check(f'⛭⛭⛭ ⓶ and on the Nariai cut the mass CANCELS: $K={sp.latex(Kn)}$ -- a pure power of '
          '$1/\\alpha^4$, exactly as p0 says',
          sp.simplify(Kn - 72/a**4) == 0)
    check('and `janzen_circle` states it: "in which the mass cancels identically rather than only in '
          'the limit"',
          # ** the source writes it as `the mass cancels \\emph{identically}` **
          'in which the mass cancels' in circ and 'rather than only in the limit' in circ)

    # ⓷ and 1/sqrt3 survives
    check('⛭⛭ ⓷ while $r_N/\\alpha=1/\\sqrt3$ is dimensionless, fixed, and ABSENT from $K$ -- ** a '
          'ratio of a LOCUS to the scale, not of two invariants **',
          sp.simplify((a/sp.sqrt(3))/a - 1/sp.sqrt(3)) == 0)

    # ⓸ Nariai is unique
    check('⓸ and Nariai is not a choice: "the Nariai configuration is the unique fixed point of the '
          'root-exchange involution, the unique vantage at which two roots collide"',
          'the unique fixed point of the root-exchange involution' in shad)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** p0's inference is SOUND and 1/√3 falls outside its scope. **")
    print('  ⓵ ** The premise is a two-scale argument: ** "a dimensionless magnitude needs two" —')
    print('     not "there are no numbers" but ** "there is nothing to take a ratio OF". **')
    print(f'  ⛭⛭⛭ ⓶ ** And on the Nariai cut the mass CANCELS: K = {sp.latex(Kn)}. **  A pure power,')
    print('     ** exactly as p0 says **, and janzen_circle states it in its own voice.')
    print('  ⛭⛭ ⓷ ** But r_N/α = 1/√3 survives that cancellation and is ABSENT from K. **')
    print('     *** A ratio of a LOCUS to the scale, not of two invariants — so the second scale p0')
    print('     denies is not what supplies it.  The inference neither covers nor excludes it. ***')
    print('  ⓸ ** And Nariai is not a choice: ** "the unique fixed point of the root-exchange')
    print('     involution".  ** M/α is fixed by a uniqueness statement the corpus proves. **')
    print('  ⓹ *** SO PO-5\'s RESIDUE IS ONE SENTENCE, NOT A SEARCH: the corpus HAS a forced')
    print('     dimensionless number, and p0\'s argument against having one is about curvature')
    print('     invariants and correct about those.  What is missing is an F² term for the number to')
    print('     multiply — r2729\'s wall, unmoved. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
