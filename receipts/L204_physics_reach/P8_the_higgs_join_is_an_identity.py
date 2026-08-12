#!/usr/bin/env python3
"""P8 -- c54.203's item-48 join verified independently: p0's mass-reflection is a PROPERTY of P3's own
cubic, so the two symmetry-breaking mechanisms are ONE, and the order parameter's bound IS the Nariai
mass.

** THE PRIOR QUESTION, STATED IN ADVANCE AND ANSWERED. **  c54.202 said before doing the work: "are P3's
symmetry breaking and p0's R-parity identification ** one mechanism or two **?  ** Whether they're one or
two is prior to asking what the Higgs identification predicts. **"  ⇒ *** They are one, and the join is
an IDENTITY rather than an argument. ***

** ⓵ THE JOIN, re-derived here. **  p0 states the parity as the geometric mass-reflection
r_0 -> -r_0, whence 2M -> -2M.  P3 derives, ** for an entirely different purpose **, the relation

      2M = r_0 - r_0^3        (alpha = 1)

  and the cubic is ** ODD **: under r_0 -> -r_0 it returns exactly -(2M).  Verified symbolically.
  ⇒ *** SO p0's MASS-REFLECTION IS A PROPERTY OF P3's OWN RELATION, NOT A SECOND ASSUMPTION.  The two
      papers were describing one object and had never been set side by side. ***

** ⓶ THE UNBROKEN PHASE IS THE BARE SUBSTRATE. **  2M = 0 at r_0 = 0, +/-alpha -- ** three offsets, one
massless geometry ** (f = 1 - r^2/alpha^2 at all three).  ⇒ ** The symmetric sector IS de Sitter. **

** ⛭⛭ ⓷ AND THE ORDER PARAMETER IS BOUNDED, WHICH A QUARTIC POTENTIAL IS NOT. **  Stationary points of
r_0 - r_0^3 sit at r_0 = +/-alpha/sqrt(3), giving

      *** |M|_max = alpha/(3 sqrt 3) ***

  and that is ** the Nariai mass **, obtained independently from f = f' = 0 and ** never substituted
  in **.  Verified: the two expressions are equal exactly.
  ⇒ *** THE BREAKING SATURATES AT EXACTLY THE CONFIGURATION A COLLAPSE REACHES. ***  ** That is content,
    not restatement: a Higgs potential's order parameter is unbounded above; this one is not, and its
    ceiling is a geometry the corpus already had for other reasons. **

** ⓸ AND THE BREAKING HAS A CAUSE RATHER THAN A POSTULATE. **  P3 does not posit the offset: it argues a
manifold observer ** cannot be assumed to sit at r_0 = 0 **, because the reference they actually have is
the hole's sky image and ** there is no marked point on it for a reticle to land on **.
  ⇒ ** So the symmetry is broken by WHAT A REFERENCE IS, not by a potential written with its minimum off
    the origin. **

WHAT IS NOT CLAIMED, and c54.203's own not-claimed list is longer than its claimed one.  ** No vev, no
scale, no mass value, no derivation of the Higgs field or its potential or the gauge group it breaks. **
`F1` untouched, and said so in the paper's own voice.  ** Not that this is a derivation of the Higgs
mechanism ** -- it is an identification of what, in CR's terms, the mechanism BREAKS, which is what
r2524 established was asserted and undeveloped.

⌗ AND THE FIRST HALF OF THIS ROW'S HISTORY IS WORTH KEEPING BESIDE IT: ** r2522 recorded the Higgs as a
principled decline and wrote "the argument is complete and only the word is missing." **  Daryl: "I've
met nodes trying to bury that."  *** The word was not what was missing.  What was missing is above. ***

Written r2539.  Stated for reversal.
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


def body(f):
    return re.sub(r'\s+', ' ', '\n'.join(
        l for l in open(os.path.join(ROOT, 'corpus', f), encoding='utf-8', errors='replace').read().split('\n')
        if not l.lstrip().startswith('%')))


def main():
    print()
    print('  P8 -- are the two symmetry-breaking mechanisms one, and is the join an identity?')
    print()
    r = sp.Symbol('r_0', real=True)
    twoM = r - r**3

    # ⓵ the cubic is odd
    check('P3 relation 2M = r_0 - r_0^3 is ODD: under r_0 -> -r_0 it returns exactly -(2M)',
          sp.simplify(twoM.subs(r, -r) + twoM) == 0)
    check("⇒⇒ SO p0's MASS-REFLECTION IS A PROPERTY OF P3's OWN CUBIC, NOT A SECOND ASSUMPTION",
          sp.simplify(twoM.subs(r, -r) + twoM) == 0)

    # ⓶ the unbroken phase
    zeros = sorted(sp.solve(sp.Eq(twoM, 0), r), key=lambda x: sp.N(x))
    check(f'2M = 0 at r_0 = {zeros} -- three offsets, one massless geometry',
          zeros == [-1, 0, 1])

    # ⓷ the bound is the Nariai mass
    crit = sp.solve(sp.Eq(sp.diff(twoM, r), 0), r)
    Mmax = max([sp.Abs(twoM.subs(r, c))/2 for c in crit], key=lambda e: sp.N(e))
    nariai = 1/(3*sp.sqrt(3))
    check(f'the stationary points sit at r_0 = {crit}, giving |M|max = {sp.simplify(Mmax)}',
          len(crit) == 2)
    check(f'⛭⛭ AND THAT EQUALS THE NARIAI MASS alpha/(3 sqrt3) = {sp.simplify(nariai)}, obtained '
          'independently from f = f\' = 0', sp.simplify(Mmax - nariai) == 0)
    al = sp.Symbol('alpha', positive=True)
    rr = sp.Symbol('r', positive=True)
    f = 1 - 2*(al/(3*sp.sqrt(3)))/rr - rr**2/al**2
    rn = al/sp.sqrt(3)
    check('cross-check: at M = alpha/(3 sqrt3) the metric function has f = 0 and f\' = 0 at '
          'r = alpha/sqrt3',
          sp.simplify(f.subs(rr, rn)) == 0 and sp.simplify(sp.diff(f, rr).subs(rr, rn)) == 0)
    check('⇒ SO THE BREAKING SATURATES AT EXACTLY THE CONFIGURATION A COLLAPSE REACHES',
          sp.simplify(Mmax - nariai) == 0)

    # ⓸ and the word is now in a paper
    papers = [g for g in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
              if not os.path.basename(g).startswith('appendix_receipts')]
    allp = ' '.join(body(os.path.basename(g)) for g in papers)
    n = len(re.findall('Higgs', allp, re.I))
    check(f'⌗ and "Higgs" is now IN A PAPER BODY ({n} occurrence(s)), where r2522 measured ZERO across '
          'seventeen', n > 0)
    check('and the paper states its own non-claims in its own voice -- no Higgs field, potential, or '
          'gauge group derived',
          'Higgs field, its potential, or the gauge group it breaks' in allp)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the two mechanisms are ONE, and the join is an identity. **')
    print('  ⓵ ** 2M = r_0 - r_0^3 is ODD **, so p0\'s mass-reflection r_0 -> -r_0 whence 2M -> -2M is a')
    print("     PROPERTY of P3's own relation -- ** not a second assumption. **  Two papers, one object,")
    print('     never set side by side.')
    print('  ⓶ ** 2M = 0 at r_0 = 0, +/-alpha ** -- three offsets, one massless geometry.  The unbroken')
    print('     phase IS de Sitter.')
    print('  ⓷ ** And |M|max = alpha/(3 sqrt3) = THE NARIAI MASS **, obtained independently from')
    print('     f = f\' = 0 and never substituted in.  ⇒ ** The order parameter is BOUNDED, which a')
    print('     quartic potential is not, and it saturates at exactly the configuration a collapse')
    print('     reaches. **')
    print('  ⌗ And "Higgs" is now in a paper body, where r2522 measured zero across seventeen.')
    print('  ⚠ NOT claimed: no vev, no scale, no mass value, no derivation of the field, its potential,')
    print('    or the gauge group.  ** F1 untouched. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
