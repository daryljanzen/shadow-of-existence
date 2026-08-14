#!/usr/bin/env python3
"""B16 -- `PO-5`'s coupling cannot come from the colour bundle, and the reason is structural: the
branch-point holonomy is non-trivial while the curvature is identically zero, and force needs curvature.

** WHERE `PO-5` STANDS. **  r2609 found the OBJECT delivered -- $SU(3)$ generated, channels computed --
and left the COUPLING: "the bundle above is flat, so the construction supplies colour's exact selection
rules and no force---** the geometry quantises and does not couple **."

** ⓵ AND THE BUNDLE IS NOT TRIVIAL, WHICH IS WHY THE QUESTION SURVIVED. **  P14 records "two further
facts about the sector's discrete group": it is larger than $D_6$, because "** the residue pairing the
horizon roots' surface gravities carry has a holonomy about the branch points ** which, adjoined to the
walls' $S_3$, ** closes the Weyl group of the substrate's own complexified isometry algebra **---so the
excess is substrate-derived rather than assumed."

  ⇒ *** So there IS a holonomy.  A flat bundle over a punctured base carries non-trivial holonomy about
      the punctures while its curvature vanishes identically -- which is exactly the situation described,
      and exactly why "flat" and "has a group" are not in tension. ***

** ⛭⛭ ⓶ BUT HOLONOMY IS NOT CURVATURE, AND FORCE NEEDS CURVATURE. **  For a connection
$A=c\\,T\\,d\\varphi$ on a punctured base with $c$ constant and $T$ fixed:

      *** dA      = c T d(dphi) = 0        (dphi is closed away from the puncture)
          A ^ A   = c^2 (T^T) dphi^dphi = 0  (a 1-form wedged with itself)
          ⇒ F = dA + A^A = 0  EVERYWHERE off the puncture ***

  while the holonomy around a loop enclosing it is $\\exp(2\\pi i c)$ -- ** non-trivial, and for $c=1/3$
  exactly the generator of a $\\mathbb Z_3$. **

  ⇒⇒ *** A force on a charge requires $F_{\\mu\\nu}\\ne0$ (Lorentz: $f=qF v$).  $F=0$ everywhere the
      particle can be, so there is NO FORCE AT ANY SEPARATION.  What survives is a PHASE -- Aharonov--Bohm
      -- which is interference, not attraction. ***

** ⓷ SO `PO-5`'s COUPLING CANNOT COME FROM THIS BUNDLE. **  *** Not "has not yet been extracted from it"
-- CANNOT.  The bundle's holonomy is what delivers the selection rules and the group, and the same
flatness that makes those exact makes a force impossible.  The two are the same fact read twice. ***
  ⌗ ** Which is a determinate NEGATIVE and worth a positive: ** *** it tells the row where not to look.  A
    coupling, if the programme has one, must come from a structure OTHER than the colour bundle -- and
    P14 already names the candidate class by exclusion when it says the geometry "quantises and does not
    couple". ***

WHAT IS NOT CLAIMED.  ** Not that CR has no route to a coupling ** -- *** only that this bundle is not
it.  Where one would come from is not addressed here. ***  ** Not that the holonomy is unimportant ** --
it closes the Weyl group and is substrate-derived, which is P14's point and stands.  ** Not that the
model connection is CR's ** -- *** it is the general form of a flat connection on a punctured base, used
to show that flatness and non-trivial holonomy coexist; the conclusion needs only $F=0$, which P14
states. ***

Written r2666.  Stated for reversal.
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
    print("  B16 -- can PO-5's coupling come from the colour bundle?")
    print()
    p14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))

    # ⓵ the paper's two statements
    check('⓵ P14 states the flatness: "Flat holonomy supplies exact selection rules and no curvature, so '
          'the construction delivers the discrete content of colour and supplies no force"',
          'Flat holonomy supplies exact selection rules and no curvature' in p14)
    check('and the geometry\'s role: "the geometry quantises and does not couple"',
          'the geometry quantises and does not couple' in p14)
    check('⛭ and there IS a holonomy: "the residue pairing the horizon roots\' surface gravities carry '
          'has a holonomy about the branch points"',
          "has a holonomy about the branch points" in p14)
    check('which closes a group: "adjoined to the walls\' $S_3$, closes the Weyl group of the '
          "substrate's own complexified isometry algebra\"",
          "closes the Weyl group of the substrate's own complexified isometry algebra" in p14)

    # ⓶ flatness with non-trivial holonomy
    for c in (1/3, 2/3):
        hol = complex(np.exp(2j * np.pi * c))
        check(f'⓶ a flat connection $A=c\\,T\\,d\\varphi$ has holonomy $\\exp(2\\pi i c)$ = '
              f'{hol.real:+.3f}{hol.imag:+.3f}i at $c={c:.3f}$ -- NON-trivial',
              abs(hol - 1) > 0.5)
    hol3 = complex(np.exp(2j * np.pi * 1.0))
    check('and returns to the identity at winding 3, so it generates a $\\mathbb{Z}_3$',
          abs(hol3 - 1) < 1e-9)
    # ** compute the curvature rather than asserting it.  A = c T dphi in polar coordinates is
    # A_phi = c T, A_r = 0, both independent of r and phi, so every component of
    # F_{mu nu} = d_mu A_nu - d_nu A_mu + [A_mu, A_nu] vanishes. **
    import sympy as sp
    r, phi, c = sp.symbols('r varphi c', positive=True)
    A_r, A_phi = 0, c                       # T factored out; [A_r, A_phi] = 0 since A_r = 0
    F = sp.simplify(sp.diff(A_phi, r) - sp.diff(A_r, phi))
    check(f'while its curvature vanishes identically: $F_{{r\\varphi}} = \\partial_r A_\\varphi - '
          f'\\partial_\\varphi A_r = {F}$, and $A\\wedge A=0$ (a 1-form wedged with itself)',
          F == 0)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** PO-5's coupling CANNOT come from this bundle. **")
    print('  ⓵ ** The bundle is flat AND has a non-trivial holonomy, ** which is not a tension: a flat')
    print('     bundle over a PUNCTURED base carries holonomy about the punctures while its curvature')
    print('     vanishes identically.  ** P14 records exactly that: "a holonomy about the branch points"')
    print('     that "closes the Weyl group of the substrate\'s own complexified isometry algebra". **')
    print('  ⛭⛭ ⓶ ** But holonomy is not curvature, and force needs curvature: **')
    print('       dA = cT d(dφ) = 0,   A∧A = 0   ⇒   ** F = 0 everywhere off the puncture **')
    print('       while the holonomy exp(2πic) is non-trivial, generating a Z₃ at c = 1/3.')
    print('     ⇒⇒ ** A force needs F ≠ 0 (Lorentz: f = qFv).  F = 0 everywhere the particle can be, so')
    print('       there is NO FORCE AT ANY SEPARATION. **  *** What survives is a PHASE -- Aharonov-Bohm')
    print('       -- which is interference, not attraction. ***')
    print('  ⓷ ** So it is not "not yet extracted" but CANNOT: ** the same flatness that makes the')
    print('     selection rules EXACT makes a force IMPOSSIBLE.  ** The two are one fact read twice. **')
    print('  ⌗ ** A determinate negative, and worth a positive: ** *** it tells the row where not to look.')
    print('    A coupling, if the programme has one, must come from a structure OTHER than the colour')
    print('    bundle. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
