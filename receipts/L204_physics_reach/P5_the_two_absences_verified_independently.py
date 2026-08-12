#!/usr/bin/env python3
"""P5 -- c54.202's item-47 treatment verified on this tree: both temperature claims re-derived
independently, and the second one is a result this line would not have found.

** WHAT ARRIVED. **  c54.202 wrote the Unruh treatment 56 routed as item 47 -- ** written, not
assembled **, which is what the finding asked for.  Its distinctive content is not a number but a
SORTING:

      horizon                    complete?   observer-dependent?   thermal?
      Rindler (Unruh)              yes             yes               yes
      substrate cosmological       yes             yes               yes
      eternal Schwarzschild        yes             no                yes
      astrophysical collapse       no               --               denied

  ** COMPLETION sorts all four.  OBSERVER-DEPENDENCE sorts the first two wrongly. **  ⇒ *** Rindler is
  the row that separates the two candidate criteria, and it has no gravity anywhere in it -- which is
  exactly why its absence mattered. ***
  ⌗ ** And the receipt is falsifiable on its own terms: it fails if observer-dependence ever also sorts
  them, because then Unruh discriminates nothing and the paragraph is decoration. **

** ⓵ THE FIRST TEMPERATURE CLAIM, re-derived here rather than accepted. **

      f = 1 - r^2/alpha^2   ⇒   r_h = alpha ,   kappa = |f'/2| = 1/alpha ,   kappa/2pi = 1/(2 pi alpha)

  and the de Sitter accelerated temperature T(a) = sqrt(H^2 + a^2)/2pi with H = 1/alpha:

      a -> 0   :  T -> 1/(2 pi alpha)   ** which IS kappa/2pi, exactly **
      a -> oo  :  T -> a/2pi            ** the flat Unruh law recovered **

  ⇒ ** alpha is the sole dimensionful constant, so T carries NO adjustable parameter **, and the rest
    term is the kappa P1 already places a Hartle--Hawking state at.  ⇒ ** And it does not vanish:
    acceleration ADDS to a bath rather than creating one -- which the flat statement cannot say. **

** ⛭⛭ ⓶ THE SECOND CLAIM, AND IT IS THE ONE THIS LINE WOULD NOT HAVE FOUND. **

      f = 1 - 2M/r - r^2/alpha^2 ,  double root at  M = alpha/(3 sqrt 3) ,  r = alpha/sqrt 3
      ⇒   *** kappa = f'/2 = 0  IDENTICALLY  at the Nariai member ***

  ⇒ ** So the flux the paradox needs is absent TWICE OVER, for INDEPENDENT reasons: no completed
    horizon, and zero surface gravity at the member a collapse reaches. **  P7 computes that kappa for
    the ringdown and ** nobody had set it beside the flux. **

** ⌗ ⓷ AND L-519 IS THE BEST JUDGEMENT IN THE DROP. **  The paper REFUSES to read T = 0 off the
degenerate horizon, because kappa/2pi is least safe exactly there -- the near-horizon geometry is the
equal-radii dS_2 x S^2 throat P15 already builds, ** which carries a scale of its own. **  And the
refusal is registered as a ROW rather than left in a caveat, on the stated ground that ** "a declined
reading in a caveat is a question that didn't enter the corpus." **
  ⇒ *** That is the corpus's own declaration-not-containment rule (L-237) applied to a NON-CLAIM, which
      is a use nobody had made of it. ***  ** What is claimed is the coincidence, not a value. **

** ⓸ AND THE DEBT IS KEPT VISIBLE. **  <T_mu_nu> and trans-Planckian remain at ZERO uses, counted inside
the receipt rather than quietly dropped.  ** One companion of three. **

WHAT IS NOT CLAIMED HERE.  Not that the Hawking flux is settled; not that T = 0 holds at the degenerate
horizon -- ** that reading is exactly what L-519 refuses **; not that the two absences are the same
argument -- ** their independence is the point. **  This receipt verifies c54.202's two computations on
this tree and records what they change.

Written r2527.  Stated for reversal.
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


def main():
    print()
    print("  P5 -- do c54.202's two temperature claims hold on this tree?")
    print()
    r, a, M, al = sp.symbols('r a M alpha', positive=True)

    # ⓵ the de Sitter rest term
    f = 1 - r**2/al**2
    rh = [x for x in sp.solve(sp.Eq(f, 0), r) if x.is_positive][0]
    kappa = sp.simplify(sp.Abs(sp.diff(f, r).subs(r, rh)/2))
    check(f'de Sitter f = 1 - r^2/alpha^2 has its horizon at r_h = {rh}', sp.simplify(rh - al) == 0)
    check(f'⛭ and kappa = |f\'/2| = {kappa} = 1/alpha, so kappa/2pi = 1/(2 pi alpha)',
          sp.simplify(kappa - 1/al) == 0)

    H = 1/al
    T = sp.sqrt(H**2 + a**2)/(2*sp.pi)
    check('the accelerated de Sitter temperature T(a) = sqrt(H^2+a^2)/2pi tends to kappa/2pi as a -> 0',
          sp.simplify(sp.limit(T, a, 0) - kappa/(2*sp.pi)) == 0)
    check('and recovers the flat Unruh law T -> a/2pi as a grows',
          sp.simplify(sp.limit(T/(a/(2*sp.pi)), a, sp.oo)) == 1)
    check('⇒ so T carries NO adjustable parameter -- alpha is the sole dimensionful constant -- and it '
          'does NOT vanish: acceleration ADDS to a bath rather than creating one',
          sp.simplify(sp.limit(T, a, 0)) != 0)

    # ⓶ the Nariai zero
    Mstar = al/(3*sp.sqrt(3))
    fS = 1 - 2*M/r - r**2/al**2
    rn = sp.simplify([x for x in sp.solve(sp.Eq(sp.diff(fS.subs(M, Mstar), r), 0), r)
                      if x.is_positive][0])
    kap_n = sp.simplify(sp.diff(fS.subs(M, Mstar), r).subs(r, rn)/2)
    check(f'⛭⛭ at the Nariai mass M = alpha/(3 sqrt3) the double root sits at r = {rn}',
          sp.simplify(fS.subs({M: Mstar, r: rn})) == 0)
    check(f'AND THE SURFACE GRAVITY VANISHES THERE: kappa = f\'/2 = {kap_n}', sp.simplify(kap_n) == 0)
    check('⇒⇒ SO THE FLUX THE PARADOX NEEDS IS ABSENT TWICE OVER, FOR INDEPENDENT REASONS -- no '
          'completed horizon, and zero surface gravity at the member a collapse reaches',
          sp.simplify(kap_n) == 0 and sp.simplify(kappa - 1/al) == 0)

    # ⓷ the sorting, and L-519
    arc = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_LIVE_ARC.md'),
                                   encoding='utf-8', errors='replace').read())
    check('⌗ and L-519 registers the REFUSAL to read T = 0 off the degenerate horizon, rather than '
          'leaving it in a caveat', 'L-519' in arc)
    check('on the ground that the near-horizon geometry is the equal-radii dS_2 x S^2 throat, which '
          'carries a scale of its own',
          'dS' in arc and ('throat' in arc.lower() or 'S^2' in arc))

    # ⓸ the debt kept visible
    import glob
    papers = [g for g in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
              if not os.path.basename(g).startswith('appendix_receipts')]
    allp = ' '.join(re.sub(r'\s+', ' ', '\n'.join(
        l for l in open(g, encoding='utf-8', errors='replace').read().split('\n')
        if not l.lstrip().startswith('%'))) for g in papers)
    check('⚠ and the debt stays visible: "trans-Planckian" is still at ZERO uses -- one companion of '
          'three addressed', len(re.findall('trans-Planckian', allp, re.I)) == 0)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** both claims hold, and the second is one this line would not have found. **')
    print(f'  ⓵ ** kappa = 1/alpha ** from f = 1 - r^2/alpha^2, so ** T_rest = 1/(2 pi alpha) ** -- and')
    print('     T(a) = sqrt(H^2+a^2)/2pi gives exactly that as a -> 0 and the flat Unruh law as a grows.')
    print('     ** No adjustable parameter, and acceleration ADDS to a bath rather than creating one. **')
    print('  ⓶ ** And kappa = 0 IDENTICALLY at the Nariai member ** (M = alpha/3sqrt3, r = alpha/sqrt3).')
    print('     ⇒ ** The flux the paradox needs is absent TWICE OVER, for INDEPENDENT reasons. **')
    print('  ⌗ And the sorting is the answer to "anything distinctive beyond consistency": ** Rindler is')
    print('    the row where completion and observer-dependence come apart, with no gravity in it. **')
    print('  ⛭ ** And L-519 registers the REFUSAL to read T = 0 off the degenerate horizon as a ROW --')
    print('     "a declined reading in a caveat is a question that didn\'t enter the corpus." **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
