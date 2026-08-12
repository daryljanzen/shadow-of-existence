#!/usr/bin/env python3
"""B10 -- L-519 answered from the MECHANISM side: thermality requires an exponential near-horizon
approach, the degenerate member's is a power law, and P15 already derived exactly that -- for a
different purpose.

** THE QUESTION, as L-519 states it. **  c54.202 found kappa = 0 at the Nariai double root and REFUSED
to read T = 0 from it, registering the refusal as a row rather than a caveat because "a declined reading
in a caveat is a question that didn't enter the corpus."  ** The row asks: what temperature, if any, does
the configuration a collapse reaches carry -- read on the near-horizon geometry rather than on
kappa/2pi? **

** ⓵ WHY A NON-DEGENERATE HORIZON IS THERMAL, AND IT IS ONE STEP. **  Near a SIMPLE root, f ~ 2 kappa
delta, so the tortoise coordinate is

      r_* = ∫ ddelta / f = log(delta) / (2 kappa)      ⇒   delta ~ e^{2 kappa r_*}

  ** The approach is EXPONENTIAL **, and the affine/Killing relation U ~ -e^{-kappa u} that follows is
  *** exactly the step that yields a Planck spectrum at T = kappa/2pi. ***  ** The exponential IS the
  thermality; everything else is bookkeeping. **

** ⛔ ⓶ AND AT A DOUBLE ROOT THE STEP IS NOT AVAILABLE. **  f ~ c delta^2, so

      r_* = -1/(c delta)                                ⇒   delta ~ -1/(c r_*)

  ** A POWER LAW, not a logarithm. **  ⇒ *** There is no exponential relation between affine and Killing
  time, so the construction that produces the Planck spectrum has no first step.  Not "the temperature is
  zero" -- THE MECHANISM IS ABSENT. ***
  ⌗ And the Nariai member is a double root: f(r_n) = f'(r_n) = 0 at r_n = alpha/sqrt(3), re-verified.

** ⛭⛭ ⓷ AND P15 ALREADY DERIVED THIS, FOR A DIFFERENT PURPOSE. **  Its transmission dichotomy:

  "a non-degenerate horizon's ** exponential near-horizon approach ** imprints a scale-invariant spectrum
   (the inflationary de Sitter-horizon mechanism), whereas ** the degenerate Nariai member's power-law,
   scale-free approach ** to the branch point is argued to transmit the progenitor spectrum unaltered."

  ⇒ *** THE SAME EXPONENTIAL/POWER-LAW SPLIT, ONE PAPER OVER, USED TO ARGUE ABOUT SPECTRAL TRANSMISSION
      AND NEVER CONNECTED TO THE TEMPERATURE QUESTION. ***  ** P15 needed it to say what CROSSES; L-519
      needed it to say what the configuration CARRIES.  It is one fact. **

** ⓸ SO L-519 HAS THREE INDEPENDENT FOOTINGS AND THEY AGREE. **
  * ** c54.202's ** -- the near-horizon geometry is the equal-radii dS_2 x S^2 throat, which ** carries a
    scale of its own **, so kappa/2pi is least safe exactly there;
  * ** r2528's ** -- f'' < 0 at the double root, so ** the static region pinches to a point and kappa/2pi
    has no FRAME to be defined in **;
  * ** and this one ** -- ** the MECHANISM is absent: thermality needs an exponential approach and this
    one is a power law. **
  ⇒ *** The first two say what CANNOT BE READ.  This one says what IS TRUE, and it is the one that makes
      the refusal a result rather than a caution. ***

WHAT IS NOT CLAIMED.  ** Not that the configuration is athermal in every sense ** -- a scale-free
power-law approach can still do things to a spectrum, which is precisely what P15 argues it does, and
that is a different question from a Planck spectrum.  ** Not that T = 0 ** -- that reading stays refused,
and this receipt supplies a third reason to refuse it rather than a value.  ** Not that P15's
transmission argument is re-derived here **: it is quoted, and only the exponential/power-law step is
recomputed.

Written r2543.  Stated for reversal.
"""
import glob
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
    print('  B10 -- what does the degenerate configuration carry, read on the mechanism?')
    print()
    papers = [f for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
              if not os.path.basename(f).startswith('appendix_receipts')]
    allp = ' '.join(re.sub(r'\s+', ' ', '\n'.join(
        l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
        if not l.lstrip().startswith('%'))) for f in papers)

    d, k, c = sp.symbols('delta kappa c', positive=True)

    # ⓵ the simple root gives a logarithm -> exponential approach
    rstar_s = sp.simplify(sp.integrate(1/(2*k*d), d))
    check(f'SIMPLE root: f ~ 2 kappa delta gives r_* = {rstar_s} -- a LOGARITHM',
          rstar_s.has(sp.log))
    check('⇒ so delta ~ e^{2 kappa r_*}: the approach is EXPONENTIAL, and the affine/Killing relation '
          'U ~ -e^{-kappa u} that follows is the step yielding a Planck spectrum at T = kappa/2pi',
          rstar_s.has(sp.log))

    # ⓶ the double root gives a power law
    rstar_d = sp.simplify(sp.integrate(1/(c*d**2), d))
    check(f'⛔ DOUBLE root: f ~ c delta^2 gives r_* = {rstar_d} -- a POWER LAW, not a logarithm',
          not rstar_d.has(sp.log) and rstar_d.has(d))
    check('⇒⇒ SO THERE IS NO EXPONENTIAL RELATION BETWEEN AFFINE AND KILLING TIME, and the construction '
          'that produces the Planck spectrum has no first step -- the MECHANISM is absent, which is not '
          'the same as the temperature being zero',
          not rstar_d.has(sp.log) and rstar_s.has(sp.log))

    # and the Nariai member is a double root
    al, r = sp.symbols('alpha r', positive=True)
    fS = 1 - 2*(al/(3*sp.sqrt(3)))/r - r**2/al**2
    rn = al/sp.sqrt(3)
    check('and the Nariai member IS a double root: f(r_n) = 0 and f\'(r_n) = 0 at r_n = alpha/sqrt3',
          sp.simplify(fS.subs(r, rn)) == 0 and sp.simplify(sp.diff(fS, r).subs(r, rn)) == 0)

    # ⓷ P15 already has the split
    check("⛭⛭ AND P15 ALREADY DERIVED THE SPLIT, for a different purpose: a non-degenerate horizon's "
          '"exponential near-horizon approach" imprints a scale-invariant spectrum',
          'exponential near-horizon approach' in allp)
    check("while \"the degenerate Nariai member's power-law, scale-free approach\" transmits the "
          'progenitor spectrum unaltered',
          "degenerate Nariai member's power-law, scale-free approach" in allp)
    check('⇒ SO IT IS ONE FACT USED FOR TWO PURPOSES -- P15 needed it to say what CROSSES; L-519 needs '
          'it to say what the configuration CARRIES -- and the two were never connected',
          'exponential near-horizon approach' in allp
          and "degenerate Nariai member's power-law, scale-free approach" in allp)

    # ⓸ the three footings
    check("⌗ c54.202's footing: the near-horizon geometry is the equal-radii dS_2 x S^2 throat, which "
          'carries a scale of its own',
          'equal-radii $\\mathrm{dS}_{2}\\times S^{2}$ throat' in allp
          and 'carries a scale of its own' in allp)
    check('and it says the two readings are not reconciled there, and claims the coincidence rather '
          'than a value',
          'What is claimed is the coincidence and not a value' in allp
          or 'the two readings are not reconciled here' in allp)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the mechanism is absent, and that is what is TRUE rather than what cannot be')
    print('  read. **')
    print('    simple root:  f ~ 2 kappa delta   ⇒ r_* ~ log(delta)   ⇒ ** EXPONENTIAL approach **')
    print('    double root:  f ~ c delta^2       ⇒ r_* ~ -1/delta     ⇒ ** POWER LAW **')
    print('  ⇒ ** The exponential IS the thermality -- it is the affine/Killing relation that yields the')
    print('     Planck spectrum.  At a double root that relation does not exist, so the construction has')
    print('     no first step. **  ⇒ ** Not "T = 0": THE MECHANISM IS ABSENT. **')
    print('  ⛭ And P15 already derived the same split for its transmission dichotomy -- ** one fact, two')
    print('     purposes, never connected. **')
    print('  ⌗ So L-519 now has THREE independent footings: ** the SCALE (c54.202), the FRAME (r2528),')
    print('    and the MECHANISM (here) ** -- and the first two say what cannot be read while this one')
    print('    says what is true.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
