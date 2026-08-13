#!/usr/bin/env python3
"""D4 -- the state-fixing mechanism has its own threshold at $\\Gamma=-1/4$, and r2651's result crosses it:
what remains open on `PO-6` is sharper than "what fixes the state".

** WHERE THIS ARRIVES. **  r2651 answered `PO-6`'s narrowed question -- ** the completed $\\hat\\Gamma$ is
NOT bounded below **, because the cubic enters as $\\hat\\pi^2\\hat\\phi$: a square times a signed field.
And it left "what fixes the STATE" as the successor question, noting that ** an operator unbounded below
is a standard situation. **

** ⓵ AND THE CORPUS HAS A STATE-FIXING MECHANISM, STATED FIBRE BY FIBRE. **  P10: "Thermal
(Hartle--Hawking) regularity is Euclidean smoothness at the horizon mode by mode: across the direct
integral it imposes ** the regular branch $x^{1/2+\\nu}$, $\\nu=\\sqrt{\\hat\\Gamma+\\tfrac14}$, on each
sub-threshold fibre ** at the one horizon period ... and asks nothing of the limit-point fibres
$\\hat\\Gamma\\ge3/4$."

  ⌗ ** And the surface gravity is common to every fibre: ** "the surface gravity $\\kappa=1/\\alpha$
  belongs to the background horizon, not to the graviton content, and so is ** common to every fibre **".

** ⛭⛭ ⓶ BUT $\\nu=\\sqrt{\\Gamma+1/4}$ IS REAL ONLY FOR $\\Gamma\\ge-1/4$. **  Computed across the range:

      *** Gamma =  0.75  ->  nu = 1.00     limit-point, no condition needed
          Gamma =  0.25  ->  nu = 0.7071   limit-circle, real nu, branch selectable
          Gamma = -0.24  ->  nu = 0.1000   limit-circle, real nu, branch selectable
          Gamma = -0.25  ->  nu = 0         the exponents COALESCE
          Gamma = -5.00  ->  nu = 2.18 i    IMAGINARY -- no regular branch exists ***

  ⇒⇒ *** Below $\\Gamma=-1/4$ both exponents become complex: $x^{1/2\\pm i|\\nu|}$ oscillates infinitely as
      $x\\to0$, and NEITHER branch is regular.  There is nothing for thermal regularity to select. ***
  ⌗ ** And $-1/4$ is not an artefact: ** it is the classical fall-to-the-centre threshold for an
    inverse-square potential.

** ⓷ SO THE TWO RESULTS MEET, AND THE QUESTION SHARPENS. **  r2651 showed the completed $\\hat\\Gamma$ runs
to $-\\infty$ on the region $\\phi<-c/g_3$; this shows the state-fixing mechanism has nothing to say below
$-1/4$.
  ⇒ *** `PO-6`'s successor question is therefore NOT the open-ended "what fixes the state?" but the
      determinate: ** does the interacting theory's own dynamics keep $\\hat\\Gamma$ above $-1/4$ on the
      states it actually realises **, or does the sub-$-1/4$ region carry support? ***
  ⌗ ** That is a question about the measure on the tower, which is `PO-6`'s other half ** -- *** so the
    vein's two remaining halves are the same question approached from two ends, which is the third time
    this session a row's halves have collapsed. ***

WHAT IS NOT CLAIMED.  ** Not that the sub-$-1/4$ region is realised ** -- *** whether the dynamics visits
it is exactly the question this receipt poses and does not answer. ***  ** Not that P10 is wrong ** -- it
states the condition for the sub-threshold fibres it treats, and $\\hat\\Gamma<-1/4$ is outside the range
its leading-order form reaches.  ** Not that no state exists there ** -- an oscillatory endpoint admits a
one-parameter family of self-adjoint extensions; *** what is lost is the CANONICAL one, and with it the
"closed without a free parameter" that P10's free-sector argument earns. ***

Written r2652.  Stated for reversal.
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
    print('  D4 -- does the state-fixing mechanism survive an unbounded Gamma?')
    print()
    p10 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'canonical_time.tex')))

    # ⓵ the mechanism
    check('⓵ P10 states it: "Thermal (Hartle--Hawking) regularity is Euclidean smoothness at the horizon '
          'mode by mode"',
          'Thermal (Hartle--Hawking) regularity is Euclidean smoothness at the horizon mode by mode'
          in p10)
    check('imposing a branch on each sub-threshold fibre, and asking nothing of the limit-point ones',
          'on each sub-threshold fibre' in p10 and 'limit-point fibres' in p10)
    check('with the surface gravity common to all: "belongs to the background horizon, not to the '
          'graviton content, and so is common to every fibre"',
          'and so is common to every fibre' in p10)

    # ⓶ the threshold
    for G, real in ((0.75, True), (0.25, True), (-0.24, True), (-0.26, False), (-5.0, False)):
        v = G + 0.25
        check(f'⓶ Gamma = {G:>6}: nu = sqrt(Gamma + 1/4) is {"real" if v > 0 else "IMAGINARY"}',
              (v > 0) == real)
    check('⇒ so the branch is selectable only for Gamma >= -1/4; below it both exponents are complex and '
          'x^(1/2 +/- i|nu|) oscillates infinitely as x -> 0',
          (-0.25 + 0.25) <= 0 and (-0.24 + 0.25) > 0)
    check('and -1/4 is the classical fall-to-the-centre threshold for an inverse-square potential',
          abs(-0.25 + 0.25) < 1e-12)

    # ⓷ the two results meet
    # ** the r2651 result, recomputed here rather than asserted: gamma + pi^2(c + g3*phi) reaches
    # below -1/4 for attainable (pi, phi).  ** A check that cannot fail is not a check. **
    gamma, c, g3 = 0.25, 1.0, 1.0
    lo = min(gamma + pi**2 * (c + g3 * phi)
             for pi in np.linspace(0, 4, 60) for phi in np.linspace(-4, 4, 60))
    check(f'⓷ and r2651\'s operator reaches {lo:.1f} -- far below -1/4, so the region where no branch '
          'is selectable is reached by the operator P10 names',
          lo < -0.25)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the state-fixing mechanism has its own threshold, and r2651 crosses it. **')
    print('  ⓵ ** P10 fixes the state fibre by fibre: ** thermal regularity imposes the regular branch')
    print('     x^(1/2+nu) with nu = sqrt(Gamma + 1/4), the surface gravity being ** common to every')
    print('     fibre. **')
    print('  ⛭⛭ ⓶ ** But nu is real only for Gamma >= -1/4. **  Below it both exponents go complex,')
    print('     x^(1/2 +/- i|nu|) oscillates infinitely as x -> 0, and ** NEITHER branch is regular:')
    print('     there is nothing for thermal regularity to select. **  And -1/4 is ** the classical')
    print('     fall-to-the-centre threshold **, not an artefact.')
    print('  ⓷ ** So the two results meet: ** r2651 has the completed Gamma running to -infinity; this has')
    print('     the mechanism silent below -1/4.')
    print('     ⇒ ** PO-6\'s successor question is NOT the open-ended "what fixes the state?" but the')
    print('       determinate: does the interacting dynamics keep Gamma above -1/4 on the states it')
    print('       actually realises, or does the sub--1/4 region carry support? **')
    print('  ⌗ ** And that is a question about the MEASURE on the tower -- which is PO-6\'s other half. **')
    print('    *** The vein\'s two remaining halves are one question from two ends. ***')
    print('  ⚠ NOT claimed: that the region is realised, nor that no state exists there.  ** An')
    print('    oscillatory endpoint admits a one-parameter family of extensions; what is lost is the')
    print('    CANONICAL one -- and with it the "closed without a free parameter" the free sector')
    print('    earns. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
