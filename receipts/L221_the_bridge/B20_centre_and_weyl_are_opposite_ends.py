#!/usr/bin/env python3
"""B20 -- the two gauge debts sit at OPPOSITE ends of the subgroup lattice: colour arrives at the CENTRE,
isospin at the WEYL element -- and that predicts the debts differ in kind, which they do.

** HOW THIS SURFACED. **  `scripts/unbanked.py` (r2678) surfaced `pushforward` at 30 uses across receipts
and ** zero across all seventeen papers **.  Reading its carriers found an unbanked statement in
`P14_leg_count_equals_arc_count`:

  "** the corpus's colour is the CENTRE and its structure group, reached three independent ways -- the
   winding's $\\mathbb Z_3$, the pushforward's holonomy, and the vantage triple's selection rule -- and
   each time the thing that arrives is a discrete label and the thing that does not is a coupling.
   Three routes agreeing on both halves is stronger evidence about where the boundary sits **"

** ⓵ AND THAT LOCATES COLOUR EXACTLY WHERE r2666/r2667 LEFT IT. **  The centre of $SU(3)$ is
$\\mathbb Z_3=\\{I,\\omega I,\\omega^2I\\}$, $\\omega=e^{2\\pi i/3}$; verified central against non-commuting
generators, and its adjoint action is ** trivial **:

      *** g T g^-1 = T  for every generator T,  g in the centre ***

  ⇒ ** Which is the same computation r2666 ran for $SU(2)$'s centre, one rank up. **  *** A centre supplies
    a LABEL and cannot generate the group -- so the coupling is not merely unbuilt but excluded on that
    route, which is P14's own verdict. ***

** ⛭⛭ ⓶ BUT r2676 PUT ISOSPIN AT THE OTHER END. **  A "discrete horn swap" has the ** WEYL ** element's
adjoint action -- $i\\sigma_x$ FLIPS $\\sigma_z$ -- ** not the centre's **.

  ⇒⇒ *** So the two sectors arrive at OPPOSITE ends of the subgroup lattice:

          COLOUR   ->  the CENTRE Z_3 of SU(3)    adjoint-TRIVIAL   a pure LABEL
          ISOSPIN  ->  the WEYL element of SU(2)  adjoint-NON-triv  a REFLECTION ***

** ⓷ AND THAT PREDICTS THE TWO DEBTS DIFFER IN KIND, WHICH THEY DO. **
  * ** `PO-5` (colour): ** a centre carries no adjoint information, so *** no deformation of it reaches a
    coupling -- P14 walls the route and names the residue "no third mechanism has been named". ***
  * ** `PO-4` (isospin): ** a Weyl element is HALF the generating data of $SU(2)$, which is the torus plus
    the reflection, so *** what is missing is one factor and the debt is a continuous $U(1)$. ***

  ⌗ *** The corpus has been treating these as one frontier -- "the gauge group and the multiplet
      structure" (P14) -- and they are two problems of different shape.  One is walled; one is one factor
      short. ***

WHAT IS NOT CLAIMED.  ** Not that isospin's $T$ IS the Weyl element ** -- *** r2676 showed a swap has the
Weyl adjoint action and not the centre's; whether P14's $T$ realises it needs `sec:whichthree`'s
construction read, which neither receipt does. ***  ** Not that the $U(1)$ is available ** -- it is the
same continuous-from-discrete problem, and this receipt says only that the two debts are not the same
size.  ** Not that the three colour routes are re-derived ** -- they are P14's, quoted from an unbanked
receipt and used, not re-proved.

Written r2679.  Stated for reversal.
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


def main():
    print()
    print('  B20 -- where do the two gauge debts sit in the subgroup lattice?')
    print()
    src = os.path.join(ROOT, 'receipts', 'P14_matter_sector_paper',
                       'P14_leg_count_equals_arc_count.py')
    # ** the carrier is a print-block receipt: its prose is split across Python string literals,
    # so a whitespace flatten leaves `colour is",\n            "the CENTRE`.  *** Join across the
    # quote-comma-newline-quote seams first, then flatten. *** **
    raw = open(src, encoding='utf-8', errors='replace').read()
    d = re.sub(r'"\s*,?\s*\n\s*"', '', raw)
    d = re.sub(r'\s+', ' ', d)

    check("⓵ the unbanked statement is there: \"the corpus's colour is the CENTRE and its structure "
          'group, reached three independent ways"',
          "the corpus's colour is the CENTRE and its structure group" in d
          and 'reached three independent ways' in d)
    check('naming them: "the winding\'s Z_3, the pushforward\'s holonomy, and the vantage triple\'s '
          'selection rule"',
          "the pushforward's holonomy" in d and "the vantage triple's selection rule" in d)
    check('and the pattern: "each time the thing that arrives is a discrete label and the thing that '
          'does not is a coupling"',
          'the thing that arrives is a discrete label and the thing that does not is a coupling' in d)

    # ⓵ the centre of SU(3)
    w = np.exp(2j*np.pi/3)
    def z(k):
        return (w**k) * np.eye(3, dtype=complex)

    A = np.diag([1, -1, 0]).astype(complex)
    B = np.eye(3, k=1) + 0j
    check('⓶ the centre of $SU(3)$ is $\\mathbb{Z}_3=\\{I,\\omega I,\\omega^2 I\\}$: each has unit '
          'determinant and commutes with non-commuting generators',
          # ** `@` binds tighter than `*`, so `A @ (w**k)*np.eye(3)` parsed as `(A @ w**k) * I`
          # and raised.  *** Bind the centre element first. *** **
          all(abs(np.linalg.det(z(k)) - 1) < 1e-9
              and np.allclose(z(k) @ A, A @ z(k))
              and np.allclose(z(k) @ B, B @ z(k)) for k in (0, 1, 2)))
    g = w*np.eye(3)
    check('and its adjoint action is TRIVIAL: $gTg^{-1}=T$ -- the same computation r2666 ran one rank '
          'down', np.allclose(g @ A @ np.linalg.inv(g), A))
    check('with $A$ and $B$ genuinely non-commuting, so the centrality is not vacuous',
          not np.allclose(A @ B, B @ A))

    # ⓶ the Weyl element at the other end
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sz = np.diag([1, -1]).astype(complex)
    weyl = 1j*sx
    check('⛭⛭ ⓷ while the WEYL element of $SU(2)$ has NON-trivial adjoint action: $i\\sigma_x$ flips '
          '$\\sigma_z$ (r2676)',
          np.allclose(weyl @ sz @ np.linalg.inv(weyl), -sz))

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the two gauge debts sit at OPPOSITE ends of the subgroup lattice. **')
    print('       COLOUR   ->  the CENTRE Z₃ of SU(3)     adjoint-TRIVIAL      a pure LABEL')
    print('       ISOSPIN  ->  the WEYL element of SU(2)  adjoint-NON-trivial  a REFLECTION')
    print()
    print('  ⓵ ** Colour arrives at the centre by THREE independent routes ** -- the winding\'s Z₃, the')
    print("     pushforward's holonomy, the vantage triple's selection rule -- and P14's own note:")
    print('     ** "each time the thing that arrives is a discrete label and the thing that does not is a')
    print('     coupling". **  *** That statement is UNBANKED: `pushforward` is at 30 uses in receipts and')
    print('     ZERO across all seventeen papers. ***')
    print('  ⛭⛭ ⓶ ** And that predicts the debts differ in KIND, which they do: **')
    print('     ** PO-5 (colour) ** -- a centre carries no adjoint information, so no deformation reaches')
    print('     a coupling; P14 walls the route and names the residue.')
    print('     ** PO-4 (isospin) ** -- a Weyl element is HALF the generating data of SU(2), so what is')
    print('     missing is ONE FACTOR, the torus.')
    print('  ⌗ *** The corpus treats these as one frontier -- "the gauge group and the multiplet')
    print('     structure" -- and they are two problems of different shape.  One is WALLED; one is ONE')
    print('     FACTOR SHORT. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
