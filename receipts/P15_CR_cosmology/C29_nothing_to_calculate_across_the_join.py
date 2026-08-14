#!/usr/bin/env python3
"""C29 -- `PO-12`'s remaining half DISSOLVES: the pre-onset stretch is pressureless, its potential
equation contains no $k$, and the residue P15 names is `PO-7`'s question, not this row's.

** WHAT r2663 LEFT AND NOTHING HAS TOUCHED. **  "The acoustic evolution from the branch point to
recombination is what the instrument already runs; ** joining the two as a single calculation is unrun
**."  *** This row has carried that sentence for forty revisions. ***

** ⛭⛭ ⓵ AND P15 ANSWERS IT IN ITS OWN VOICE. **  "On the radiation-free rate the crossing occurs under
pressureless matter to better than a part in $10^4$, and the potential equation for a pressureless
component, $\\Phi''+3\\mathcal H(1+w)\\Phi'+[2\\mathcal H'+(1+3w)\\mathcal H^2]\\Phi+wk^2\\Phi=0$, ** contains
no $k$ at all once $w=0$ **---the wavenumber enters only through the pressure term."

  ** Verified symbolically: ** setting $w=0$ leaves

      *** Phi'' + 3H Phi' + (H^2 + 2H') Phi = 0     ->  k ABSENT ***

  ⇒ *** Every mode's potential obeys the SAME equation on that stretch, whatever its wavenumber.  There
      is no scale-dependent evolution to compute, so there is nothing for a "single calculation across
      the join" to calculate. ***

** ⓶ AND THE GEOMETRY AGREES FROM BOTH ENDS. **
  * ** branch point: ** the comoving horizon $\\to0$, so ** every mode is outside ** (r2662).
  * ** onset: ** $k_{\\rm hor}=0.010$ Mpc$^{-1}$ against peaks at $0.022$ and above -- ** inside by a
    factor $2.2$ ** (`prop:subhorizon`).
  ⇒⇒ ** So every acoustic mode crosses in between them ** -- and P15 names the boundary mode,
  $k=0.0111$ Mpc$^{-1}$, $\\ell\\simeq144$: "** every mode at and above the acoustic peaks crossed before
  the plasma began **".  *** The crossing happens where there is no plasma to record it. ***

** ⓷ SO WHAT REMAINS IS NOT THIS ROW'S. **  P15 states the residue exactly: "the open question is now
sharp: ** on this rate nothing before the onset can imprint an acoustic phase **, so whatever sets it
must act on modes ** already inside the sound horizon when the plasma begins **."
  ⇒ *** That is the first peak's position -- `PO-7`'s question, and cc54's `L-812` held at the
      turnaround obstacle.  `PO-12`'s own remaining half is empty. ***

WHAT IS NOT CLAIMED.  ** Not that `PO-12` closes ** -- *** that is a verdict on a protected row and `F5`
reserves the strike; what is established is that the sentence this row has carried since r2663 names a
calculation with no content. ***  ** Not that the $10^{-4}$ is re-derived ** -- it is P15's, with its own
receipt.  ** Not that `PO-7` is thereby easier ** -- it inherits a sharper statement, not a smaller
problem.

Written r2701.  Stated for reversal.
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
    print("  C29 -- is there anything to calculate across the join?")
    print()
    p15 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')))

    # ⓵ the paper's clause
    check('⛭⛭ ⓵ P15: the potential equation for a pressureless component "contains no $k$ at all once '
          '$w=0$---the wavenumber enters only through the pressure term"',
          'the wavenumber enters only through the pressure te' in p15)
    check('on a stretch that is pressureless: "the crossing occurs under pressureless matter to better '
          'than a part in $10^{4}$"',
          'the crossing occurs under pressureless matter to better than a part in' in p15)

    # verify it
    Phi = sp.Function('Phi')
    eta, k, w = sp.symbols('eta k w')
    H = sp.Function('H')
    eq = (sp.diff(Phi(eta), eta, 2) + 3*H(eta)*(1+w)*sp.diff(Phi(eta), eta)
          + (2*sp.diff(H(eta), eta) + (1+3*w)*H(eta)**2)*Phi(eta) + w*k**2*Phi(eta))
    check('and $k$ IS in the general equation, so the check is not vacuous', k in eq.free_symbols)
    check('while at $w=0$ it becomes $\\Phi\'\'+3\\mathcal H\\Phi\'+(\\mathcal H^2+2\\mathcal H\')\\Phi=0$ -- '
          '$k$ ABSENT',
          k not in sp.simplify(eq.subs(w, 0)).free_symbols)

    # ⓶ the two ends
    check('⓶ and the geometry agrees: P15 names the boundary mode, "the mode whose crossing coincides '
          'with the onset is $k=0.0111$"',
          'the mode whose crossing coincides with the onset is' in p15)
    check('with "every mode at and above the acoustic peaks crossed before the plasma began"',
          'crossed before the plasma began' in p15)

    # ⓷ the residue is PO-7's
    check('⓷ and P15 states the residue: "on this rate nothing before the onset can imprint an acoustic '
          'phase, so whatever sets it must act on modes already inside the sound horizon when the plasma '
          'begins"',
          'nothing before the onset can imprint an acoustic phase' in p15
          and 'already inside the sound horizon when the plasma begins' in p15)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** PO-12's remaining half has NO CONTENT. **")
    print('  ⛭⛭ ⓵ ** The pre-onset stretch is pressureless, and at w = 0 the potential equation loses')
    print('     k entirely: ** Φ\'\' + 3ℋΦ\' + (ℋ² + 2ℋ\')Φ = 0.  ** Verified symbolically, and k IS present')
    print('     in the general equation, so the check is not vacuous. **')
    print('     ⇒ *** Every mode obeys the SAME equation there.  There is no scale-dependent evolution,')
    print('       so there is nothing for a "single calculation across the join" to calculate. ***')
    print('  ⓶ ** The geometry agrees from both ends: ** the comoving horizon → 0 at the branch point')
    print('     (every mode outside, r2662), against peaks inside by 2.2 at the onset — so every')
    print('     acoustic mode crosses in between, ** "before the plasma began". **')
    print('  ⓷ ** And P15 states the residue exactly: ** "nothing before the onset can imprint an')
    print('     acoustic phase, so whatever sets it must act on modes ** already inside the sound horizon')
    print('     when the plasma begins **".')
    print('     ⇒ *** That is the first peak\'s position — PO-7\'s question. PO-12\'s own remaining half')
    print('       is empty. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
