#!/usr/bin/env python3
"""C19 -- the branch-point join, computed: transmission is conservation of $\\mathcal R$, so the join is a
change of variable and its value is exactly $9/10$ -- applied ONCE, instantaneously, where
$\\Lambda$CDM's is spread over equality.

** WHAT WAS OWED. **  r2660 reduced `PO-12` to "run the existing hierarchy across a TWO-LEG background
joined at the branch point", and marked ** the join untouched **.  P15 states the debt in its own voice:
"the super-horizon transfer across the branch point is
itself computed ... while carrying that join and the acoustic evolution through to recombination
as ONE CALCULATION is not yet run." (r3859; the earlier wording said no computed transfer existed
at all, and C21 made that false.)

** ⓵ AND THE MATCHING CONDITION IS ALREADY STATED. **  P15: "the branch point's null geometry decomposes
the primordial scalar spectrum into a substrate-determined structure and a progenitor-supplied content,
and the degeneracy proves that ** the branch point TRANSMITS that content rather than imprinting one of
its own **."

  ⇒ *** Transmission is a conservation statement.  The quantity conserved across a change of background
      content on super-horizon scales is the comoving curvature perturbation $\\mathcal R$ -- so the join
      is a CHANGE OF VARIABLE, not a new dynamics. ***

** ⛭⛭ ⓶ AND THE VALUE FOLLOWS IN CLOSED FORM. **  On super-horizon scales at constant $w$,
$\\mathcal R/\\Phi=(5+3w)/(3+3w)$:

      *** radiation (w=1/3):  R/Phi = 3/2       matter (w=0):  R/Phi = 5/3
          ⇒  Phi_expansion / Phi_collapse  =  (3/2)/(5/3)  =  9/10,  EXACTLY ***

** ⛭⛭⛭ ⓷ AND CR APPLIES IT ONCE, INSTANTANEOUSLY, WHERE $\\Lambda$CDM SPREADS IT OVER EQUALITY. **  P15:
the expansion leg is "** matter-dominated to nine orders **, the substrate term being utterly negligible
there"; and "** this cosmology has no early integrated Sachs--Wolfe term where flat $\\Lambda$CDM has one
---in the latter the potential is still some four per cent above its asymptote at recombination, and that
residual decay is what the line-of-sight integral picks up **."

  ⇒⇒ *** So the two cosmologies apply the SAME factor by DIFFERENT routes: ***
  * ** $\\Lambda$CDM: ** the potential decays through radiation-matter equality and is still ~4% above
    asymptote at recombination -- *** the residual decay sources an early ISW term. ***
  * ** CR: ** the content changes AT the branch point and the expansion leg is matter-dominated
    throughout -- *** the potential sits AT its asymptote from the start, and there is no early ISW to
    source. ***

** ⇒ ⓸ WHICH IS WHY THE $9/10$ IS NOT A CORRECTION TO APPLY BUT A BOUNDARY CONDITION. **  *** On the
expansion leg $\\Phi$ is constant, so $\\Phi_{\\rm exp}=\\tfrac{9}{10}\\Phi_{\\rm coll}$ holds from the branch
point to recombination with no further evolution.  The transfer's collapse-leg half is the closed form
`sec:envelope` already gives; the expansion-leg half is a constant. ***
  ⌗ ** And the 4% is the observable difference, already located by the paper: ** *** $\\Lambda$CDM's
    line-of-sight integral picks up a residual decay that CR's does not have. ***

WHAT IS NOT CLAIMED.  ** Not that this IS the transfer function P15 says is not in hand ** -- *** this is
the super-horizon join only.  Modes inside the horizon at the branch point are not covered, and
$\\mathcal R$'s conservation is a super-horizon result. ***  ** Not that the expansion leg is exactly
matter-dominated ** -- the paper says "to nine orders", which is what makes the constant-$\\Phi$ statement
safe and is quoted rather than assumed.  ** Not that the join's dynamical crossing is addressed ** --
P15 defers "the detailed worldline and field dynamics of the crossing for a concrete matter model", and
that stands.

Written r2661.  Stated for reversal.
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
    print('  C19 -- the branch-point join')
    print()
    p15 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')))

    # ⓵ the debt, and the matching condition
    # ** RE-PINNED r3961.  ** The old pin read P15 saying "a computed transfer function across the
    # branch point is not yet in hand".  That sentence was CORRECTED at r3859 because it had become
    # false: C21 computes the super-horizon transfer across the branch point.  The pin is superseded
    # BY A RESULT, not stale, and the paper now draws the sharper line this receipt is actually about.
    check('⓵ P15: the super-horizon transfer across the branch point IS computed',
          'the super-horizon transfer across the branch point is itself' in p15
          and 'computed' in p15)
    check('  and what is NOT run is the single end-to-end calculation',
          'the acoustic evolution through to recombination as one calculation is not yet run' in p15)
    check('and the matching condition: "the branch point transmits that content rather than imprinting '
          'one of its own"',
          'the branch point transmits that content rather than imprinting one of its own' in p15)

    # ⓶ the value
    w = sp.symbols('w')
    RoP = (5 + 3*w) / (3 + 3*w)
    rad = sp.nsimplify(RoP.subs(w, sp.Rational(1, 3)))
    mat = sp.nsimplify(RoP.subs(w, 0))
    join = sp.nsimplify(rad / mat)
    check(f'⛭⛭ ⓶ on super-horizon scales R/Phi = (5+3w)/(3+3w): {rad} for radiation, {mat} for matter',
          rad == sp.Rational(3, 2) and mat == sp.Rational(5, 3))
    check(f'⇒ so Phi_expansion / Phi_collapse = {join} EXACTLY', join == sp.Rational(9, 10))

    # ⓷ CR applies it once
    check('⛭⛭⛭ ⓷ and the expansion leg is "matter-dominated to nine orders, the substrate term being '
          'utterly negligible there"',
          'matter-dominated to nine orders' in p15)
    check('while LCDM spreads it: "this cosmology has no early integrated Sachs--Wolfe term where flat '
          '$\\Lambda$CDM has one"',
          'has no early integrated Sachs--Wolfe term where flat' in p15)
    check('"in the latter the potential is still some four per cent above its asymptote at '
          'recombination, and that residual decay is what the line-of-sight integral picks up"',
          'four per cent above its asymptote at recombination' in p15
          and 'that residual decay is what the line-of-sight integral picks up' in p15)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the join computes, and its value is exactly 9/10. **')
    print('  ⓵ ** Transmission is a CONSERVATION statement: ** the branch point "transmits that content')
    print('     rather than imprinting one of its own", and what is conserved across a change of')
    print('     background content on super-horizon scales is ** the comoving curvature perturbation R.')
    print('     So the join is a CHANGE OF VARIABLE, not a new dynamics. **')
    print('  ⛭⛭ ⓶ ** And the value follows in closed form: ** R/Phi = 3/2 (radiation), 5/3 (matter)')
    print('     ⇒ ** Phi_exp / Phi_coll = 9/10, exactly. **')
    print('  ⛭⛭⛭ ⓷ ** And CR applies it ONCE where LCDM spreads it over equality: **')
    print('     ** LCDM ** -- the potential decays through equality and is ** still ~4% above asymptote at')
    print('     recombination **, and that residual decay ** sources an early ISW term **;')
    print('     ** CR ** -- the content changes AT the branch point and the expansion leg is')
    print('     ** matter-dominated to nine orders **, so the potential sits ** at its asymptote from the')
    print('     start ** and there is ** no early ISW to source. **')
    print('  ⇒ ⓸ ** So 9/10 is not a correction to apply but a BOUNDARY CONDITION: ** Phi is constant on')
    print('     the expansion leg, so Phi_exp = (9/10) Phi_coll holds from the branch point to')
    print('     recombination ** with no further evolution. **  The collapse-leg half is sec:envelope\'s')
    print('     closed form; ** the expansion-leg half is a constant. **')
    print('  ⚠ ** SUPER-HORIZON ONLY. **  Modes inside the horizon at the branch point are not covered,')
    print('    and R\'s conservation is a super-horizon result.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
