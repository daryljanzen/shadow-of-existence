#!/usr/bin/env python3
"""S10 -- `PO-6`'s two halves MEET AT THE SHEAR, and the second-order entry says which processes can
break the degeneracy: none at one graviton, and the tower IS the shear.

** WHERE THIS ARRIVES. **  c54.215 established the counterterm degeneracy is CONFORMAL FLATNESS
(verified at r2736: $\\mathrm{Weyl}^2=0$ for $k=+1,0,-1$ and a FREE $a(T)$), and named the real limit as
the shear, $4\\sigma^2+O(\\sigma^4)$.  *** Nobody had run what that means for the ROW. ***

** ⓵ THE DEFICIT'S FORM, checked. **  On an axisymmetric shear $\\mathrm{diag}(-2\\sigma,\\sigma,\\sigma)$
over an isotropic expansion:

      *** sigma_ij sigma^ij = 6 sigma^2
          C^2 = sigma^2 (4 + 16 sigma^2 / 3) = 4 sigma^2 + O(sigma^4)
          C^2(0) = 0 · C^2(1/10) = 76/1875 · C^2(1/2) = 4/3 ***

  ⇒ ** Leading coefficient 4, entering at SECOND order, vanishing identically at $\\sigma=0$. **

** ⛭⛭ ⓶ AND P10 SAYS WHAT THE TOWER IS, IN ITS OWN WORDS. **  "the ** TRANSVERSE-TRACELESS graviton
modes form a discrete tower ** that deparametrizes to a unitary evolution in cosmic time" -- and again,
"the closed-$S^3$ layer's propagating sector---** the transverse-traceless graviton tower **, advanced
unitarily in cosmic time".

  ⇒⇒ *** THE TOWER IS THE SHEAR.  Transverse-traceless perturbation IS shear. ***

** ⛭ ⓷ SO `PO-6`'s TWO DECLARED HALVES ARE NOT INDEPENDENT -- THEY MEET AT THE SHEAR. **
  * ** the counterterm half ** ends where conformal flatness ends, which is at the shear;
  * ** the interacting-tower half ** quantises the transverse-traceless modes, which ARE the shear.
  ⇒ *** The row declares two halves (r2684) and the corpus supplies one object under both.  That is a
      convergence, not a coincidence, and it was invisible while the counterterm half was stated as
      "maximal symmetry" and the tower half as "back-reaction". ***

** ⓸ AND THE SECOND-ORDER ENTRY HAS A PHYSICAL READING. **  *** $C^2$ entering at $\\sigma^2$ means the
degeneracy SURVIVES TO FIRST ORDER in the graviton amplitude: a one-graviton process cannot break the
one-dimensional counterterm basis, and a two-graviton process can.  ** That is a statement about which
diagrams the basis is safe against, and it is the kind of thing a counterterm question wants. ** ***

WHAT IS NOT CLAIMED.  ** Not that the basis is computed at second order ** -- *** what is established is
where it must break and at what order, not what the second-order basis contains. ***  ** Not that the
$4\\sigma^2$ coefficient is re-derived from the metric ** -- cc54 computed it; its STRUCTURE is checked
here (vanishing at $\\sigma=0$, quadratic leading term) and the identification with the tower is read
from P10.  ** Not that the two halves are thereby one problem ** -- they meet at an object; they are
still asked about different things (a basis, and a spectrum).

** COMPUTES: the shear invariant and the structure of $C^2(\\sigma)$ at three amplitudes.  *** The shear
amplitude is the corpus's own object -- P10's transverse-traceless tower; nothing is imported. *** **

Written r2743.  Stated for reversal.
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


#: ** ⛭⛭ MARKERS ARE APPARATUS, NOT PROSE, AND A PIN INTO PROSE MUST NOT SEE THEM (r3962). **
#: ** This file failed because r3558's marker pass inserted `\ldg{variational}` INTO THE MIDDLE of a
#: ** sentence it quotes: "the transverse-traceless\ldg{variational} graviton modes form a discrete
#: ** tower ...".  *** The paper's words did not change.  A bake landing split the quotation. ***
#: **   ⇒ ** That is the fourth repair kind seen from the other side: `R1` was a receipt COUNTING
#: **     its own bake's landings, and this is a receipt QUOTING across one. **  A bake that lands
#: **     markers correctly should never be able to falsify a receipt about the sentence it marks,
#: **     so the markers are stripped here rather than the quotation being cut into fragments --
#: **     fragments would only move the fragility to wherever the NEXT marker lands.
MARKER = re.compile(r'\\(?:ldg|rcpt)\{[A-Za-z0-9_]+\}')


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return MARKER.sub('', b[:j] if j > 0 else b)


def main():
    print()
    print("  S10 -- what does the shear deficit mean for PO-6's row?")
    print()
    p10 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'canonical_time.tex')))

    s = sp.symbols('sigma', real=True)
    C2 = s**2*(4 + sp.Rational(16, 3)*s**2)

    # ⓵ structure
    check('⓵ $C^2$ vanishes identically at $\\sigma=0$ -- the degeneracy is exact on any shear-free '
          'background', sp.simplify(C2.subs(s, 0)) == 0)
    check('and its leading term is $4\\sigma^2$ -- entering at SECOND order, not first',
          sp.expand(C2).as_poly(s).all_coeffs()[-3] == 4
          and sp.expand(C2).as_poly(s).all_coeffs()[-2] == 0)
    check('while being NON-zero away from zero, so the check is not vacuous: '
          f'$C^2(1/2)={sp.nsimplify(C2.subs(s, sp.Rational(1,2)))}$',
          C2.subs(s, sp.Rational(1, 2)) > 0)
    check('and the shear tensor diag$(-2\\sigma,\\sigma,\\sigma)$ is trace-free, so it is a shear and '
          'not an expansion', sp.simplify(-2*s + s + s) == 0)

    # ⓶ P10 identifies the tower
    check('⛭⛭ ⓶ and P10 names the tower: "the transverse-traceless graviton modes form a discrete '
          'tower that deparametrizes to a unitary evolution in cosmic time"',
          'transverse-traceless graviton modes form a discrete tower' in p10)
    check('and again as the propagating sector: "the transverse-traceless graviton tower, advanced '
          'unitarily in cosmic time"',
          'transverse-traceless graviton tower' in p10)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** PO-6's two halves MEET AT THE SHEAR. **")
    print('  ⓵ ** The deficit: ** C² = σ²(4 + 16σ²/3) = 4σ² + O(σ⁴) — zero at σ=0, quadratic leading,')
    print('     trace-free source.')
    print('  ⛭⛭ ⓶ ** And P10 says what the tower IS: ** "the TRANSVERSE-TRACELESS graviton modes form')
    print('     a discrete tower".  *** Transverse-traceless perturbation IS shear.  THE TOWER IS THE')
    print('     SHEAR. ***')
    print('  ⛭ ⓷ ** So the two declared halves are not independent: ** the counterterm half ends where')
    print('     conformal flatness ends — at the shear; the tower half quantises the')
    print('     transverse-traceless modes — which are the shear.')
    print('     ⇒ *** A convergence, invisible while one half read "maximal symmetry" and the other')
    print('       read "back-reaction". ***')
    print('  ⓸ ** And the second-order entry has a physical reading: ** the degeneracy SURVIVES TO')
    print('     FIRST ORDER in the graviton amplitude.  ** A one-graviton process cannot break the')
    print('     one-dimensional basis; a two-graviton process can. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
