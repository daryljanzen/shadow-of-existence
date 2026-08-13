#!/usr/bin/env python3
"""B4 -- the radial operator DOES carry a real structure: $A=\\sigma_z\\circ\\overline{\\phantom{x}}$ commutes
with it, squares to $+1$, and preserves the eigenspace the zero mode lives in.  The mod-2 index's
condition is met.

** THE ROUTE HERE, AND IT TOOK THREE CORRECTIONS. **
  * r2568 asked whether the discrete parity $R$ carries a mod-2 index, noting `mod 2`, `Witten anomaly`
    and `eta invariant` at ZERO across the corpus.
  * r2604 found the ** prerequisite present and realised on the built zero-modes ** -- $R\\circ K$ acting
    on them as charge conjugation's kinematic face.
  * r2605 computed $S=\\gamma^{0}\\gamma^{1}\\gamma^{3}$, found $S^2=-\\mathbb 1$, and concluded the route
    was CLOSED.
  * ⛔ r2606 corrected that: ** $S$ is a lift in the FOUR-dimensional spacetime algebra **, and the
    operator whose kernel is counted is the ** RADIAL ** one.

** ⇒⇒ SO THIS RECEIPT ASKS THE CORRECTED QUESTION ON THE CORRECTED OPERATOR, AND THE CORPUS SUPPLIES BOTH
EXPLICITLY. **  P14 gives the reduction in full: "The zero-mode equation $H\\psi=0$ for ** $H=-i\\sigma_x
\\partial_x+m(x)\\sigma_z$ **, with $m(x)$ the wall profile crossing zero at the throat", and the solution
"$\\psi(x)=\\exp(-\\int_0^x m\\,dx')\\chi_{+}$, with ** $\\chi_+$ the $\\sigma_y=+1$ eigenspinor **".

** ⓵ THE ANTILINEAR SYMMETRY IS UNIQUE AMONG THE FOUR CANDIDATES. **  Writing $A=U\\circ\\overline{\\;}$ and
requiring $AHA^{-1}=H$:

      *** U = 1   does not commute
          U = σx  does not commute
          U = σy  does not commute
          U = σz  COMMUTES ***

  ⌗ ** By hand: ** $\\overline{-i\\sigma_x\\partial_x}=+i\\sigma_x\\partial_x$ since $\\sigma_x$ is real, and
  $\\sigma_z(i\\sigma_x)\\sigma_z=-i\\sigma_x$; while $\\overline{m\\sigma_z}=m\\sigma_z$ and
  $\\sigma_z\\sigma_z\\sigma_z=\\sigma_z$.  ** Both terms are returned. **

** ⛭⛭ ⓶ AND IT SQUARES TO $+1$. **  $A^2=\\sigma_z\\overline{\\sigma_z}=\\sigma_z^2=+\\mathbb 1$.
  ⇒ *** A REAL structure, not a quaternionic one -- the opposite of what the 4D lift gives, and it is the
      radial operator's that governs the count. ***

** ⓷ AND IT PRESERVES THE EIGENSPACE THE MODE LIVES IN. **
$A\\sigma_yA^{-1}=\\sigma_z\\overline{\\sigma_y}\\sigma_z=\\sigma_z(-\\sigma_y)\\sigma_z=+\\sigma_y$.
  ⇒ ** So $A$ maps the $\\sigma_y=+1$ eigenspace to itself ** -- the space in which the corpus's $\\chi_+$
    sits.

** ⇒⇒⇒ TWO CONSEQUENCES, AND THE FIRST DISSOLVES A TENSION THIS LINE RAISED AT r2606. **
  * ** NO KRAMERS DOUBLING. **  Kramers requires an antiunitary squaring to $-1$; this squares to $+1$.
    *** So `prop:wall`'s "each throat wall binds exactly one normalizable chiral zero-mode" is consistent
    with the reality structure, and the worry that two would be forced does not arise. ***
  * ** AND THE MOD-2 INDEX'S CONDITION IS MET. **  A real structure commuting with the operator and
    preserving the counted space is exactly what makes $\\dim\\ker$ a mod-2 deformation invariant.
    *** `PO-5`'s mod-2 route is OPEN, and the structure supporting it is one the corpus already wrote
    down. ***

WHAT IS NOT CLAIMED.  ** Not that the mod-2 index is COMPUTED **: its value, and whether it is the object
that grades the three walls, are untouched.  ** Not that $A$ is $R\\circ K$ ** -- $A$ acts on the radial
2-spinor and $R\\circ K$ on the 4-component cut spinor; whether they are the same structure in two frames
is a question this opens.  ** Not that a mod-2 index would deliver the bridge **: r2568's standing limit
holds -- *** a $\\mathbb{Z}_2$ invariant can obstruct or permit but cannot by itself deliver four
states. ***

Written r2607.  Stated for reversal.
"""
import glob
import os
import re

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

I2 = np.eye(2)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]])
SZ = np.array([[1, 0], [0, -1]], dtype=complex)


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def commutes(U):
    """Does A = U∘conj return both terms of H = -i σx ∂ + m σz ?"""
    Ui = np.linalg.inv(U)
    kin = U @ np.conj(-1j * SX) @ Ui
    mass = U @ np.conj(SZ) @ Ui
    return np.allclose(kin, -1j * SX) and np.allclose(mass, SZ)


def main():
    print()
    print("  B4 -- does the RADIAL operator carry a real structure?")
    print()
    p14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))

    # the corpus supplies the operator and the eigenspace
    check('⌗ P14 gives the reduction: "$H=-i\\sigma_x\\partial_x+m(x)\\sigma_z$, with $m(x)$ the wall '
          'profile crossing zero at the throat"',
          'H=-i\\sigma_x\\partial_x+m(x)\\sigma_z' in p14.replace(' ', ''))
    check('and the eigenspace: "$\\chi_+$ the $\\sigma_y=+1$ eigenspinor"',
          '\\chi_{+}$ the $\\sigma_y=+1$ eigenspinor' in p14 or
          '\\sigma_y=+1$ eigenspinor' in p14)
    check('and the superpotential it came from: $W(r)=\\lambda\\sqrt f/r$ with $\\lambda=j+\\tfrac12$',
          'W(r)=\\frac{\\lambda\\sqrt{f}}{r}' in p14.replace(' ', ''))

    # ⓵ uniqueness among the four
    for name, U in (('1', I2), ('sigma_x', SX), ('sigma_y', SY), ('sigma_z', SZ)):
        c = commutes(U)
        if name == 'sigma_z':
            check(f'⓵ A = {name}∘conj COMMUTES with H', c)
        else:
            check(f'   A = {name}∘conj does NOT commute', not c)

    # ⓶ the square
    A2 = SZ @ np.conj(SZ)
    check('⛭⛭ ⓶ and it squares to +1: $A^2=\\sigma_z\\overline{\\sigma_z}=+\\mathbb 1$ -- a REAL structure',
          np.allclose(A2, I2))
    # ** the contrast is asserted against the 4D lift itself, not stated: S = g0 g1 g3 really does
    # square to -1, and the point is that the two operators disagree. **
    K4 = np.kron
    g0 = K4(SZ, I2); g1 = K4(1j*SX, SX); g2 = K4(1j*SX, SY); g3 = K4(1j*SX, SZ)
    S4 = g0 @ g1 @ g3
    check('   and the contrast with the 4D lift is real, not rhetorical: $S=\\gamma^0\\gamma^1\\gamma^3$ '
          'squares to $-1$ while this squares to $+1$ -- two operators, two structures',
          np.allclose(S4 @ S4, -np.eye(4)) and np.allclose(A2, I2))

    # ⓷ preserves the eigenspace
    act = SZ @ np.conj(SY) @ np.linalg.inv(SZ)
    check('⓷ and it preserves the counted eigenspace: $A\\sigma_yA^{-1}=+\\sigma_y$',
          np.allclose(act, SY))

    # consequences
    check('⇒ NO KRAMERS DOUBLING: Kramers needs an antiunitary squaring to -1, and this squares to +1 -- '
          "so prop:wall's \"exactly one normalizable chiral zero-mode\" is consistent",
          np.allclose(A2, I2))
    check('⇒⇒ AND THE MOD-2 INDEX CONDITION IS MET: a real structure commuting with the operator and '
          'preserving the counted space makes dim ker a mod-2 deformation invariant',
          commutes(SZ) and np.allclose(A2, I2) and np.allclose(act, SY))

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the radial operator carries a REAL structure, and the mod-2 condition is met. **')
    print('  ⓵ ** A = σz∘conj is the ONLY one of the four candidates that commutes with')
    print('     H = -i σx ∂ + m σz. **')
    print('  ⓶ ** A² = +1 ** -- a REAL structure, ** the opposite of the 4D lift\'s S² = -1 **, and it is')
    print('     the radial operator\'s that governs the count.')
    print('  ⓷ ** A σy A⁻¹ = +σy ** -- it preserves the σy = +1 eigenspace where the corpus puts χ₊.')
    print('  ⇒ ** NO KRAMERS DOUBLING **, so prop:wall\'s "exactly one" is consistent and r2606\'s worry')
    print('    does not arise.')
    print('  ⇒⇒ ** AND PO-5\'s MOD-2 ROUTE IS OPEN: ** the structure supporting it is one the corpus')
    print('     already wrote down, two sentences from the operator it wrote it for.')
    print('  ⚠ NOT claimed: the index\'s VALUE, that A is R∘K in another frame, or that a Z2 invariant')
    print('    could deliver four states.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
