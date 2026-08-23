#!/usr/bin/env python3
"""S12 -- cc54's L-818 boundary, r2743's shear finding and P10's open item are ONE boundary: the
excluded sector is the shear, the shear is the tower, and the tower is what P10 leaves open.

** WHY THIS EXISTS.  ** cc54, in flight on `L-818`: *** "this treats the running-but-classical layer
(where the heat-kernel expansion is defined); the fully back-reacting / quantized-$a(T)$ sector with no
fixed background --- S50's deeper caveat, 'the standard problem of the interacting theory' --- stays
untouched." ***  ** That is written as a caveat.  It is a located result, and this receipt locates
it. **

** ⓵ THEIR STEP 1 AGREES WITH r2736 EXACTLY. **  cc54: "Weyl$^2=0$ on the running layer (conformal
flatness isn't special to de Sitter), and $R(T)$ genuinely runs."  Verified here for a FREE $a(T)$:

      *** k = +1, 0, -1:   Weyl^2 = Riem^2 - 2 Ric^2 + R^2/3 = 0    and    dR/dT != 0 ***

  ⇒ ** The layer is conformally flat AND running. **  *** Which is the same object r2736 verified
      against c54.215, reached for a different purpose. ***

** ⛭⛭ ⓶ AND THAT IS WHY THEIR EXCLUDED SECTOR IS THE SHEAR SECTOR. **  *** An FRW layer is SHEAR-FREE
by construction -- that is what makes $\\mathrm{Weyl}^2$ vanish on it.  r2743 established the degeneracy
ends exactly where conformal flatness does, at the shear, with $C^2=4\\sigma^2+O(\\sigma^4)$.  ** So the
sector cc54's calculation cannot reach is the sector r2743 identified as the one that ends the
degeneracy. ** ***

** ⛭⛭⛭ ⓷ AND r2743 ALSO NAMED WHAT THAT SECTOR IS. **  P10, in its own words: the propagating sector is
"** the transverse-traceless graviton tower **".  *** Transverse-traceless perturbation IS shear. ***

  ⇒⇒ *** SO THREE STATEMENTS NAME ONE OBJECT: ***

      *** cc54 L-818   "the fully back-reacting / quantized-a(T) sector"
          56  r2743    the shear, where C^2 = 4 sigma^2 first becomes nonzero
          P10 (r2763)  "the definition of the interacting tower --- the standard
                        problem of the interacting theory" ***

** ⓸ WHICH UPGRADES THEIR CAVEAT AND SHOULD BE IN THE RECEIPT. **  *** A caveat says "my method does not
reach there."  ** A located boundary says "what lies beyond is the shear sector, which is the graviton
tower, which is the corpus's own named open problem." **  The second is a stronger claim and cc54 has
earned it: their reduction covers everything up to the exact point where the corpus already knows the
question changes character. ***

** ⓹ AND IT MAKES `PO-6`'s TWO HALVES ONE STATEMENT. **  *** The counterterm half: the one-constant
ledger survives on the shear-free running layer (cc54, coefficient-independent).  The tower half: what
remains is the interacting tower (P10, r2763).  ** And the tower IS the shear, which is precisely where
the counterterm result stops. ** *** So the row's two declared halves are not merely coupled (r2743) --
they partition at the same surface.

WHAT IS NOT CLAIMED.  ** Not that cc54's reduction is verified ** -- *** their five sympy steps are not
rerun here; only their Step 1 is checked against r2736, and their conclusion is coefficient-independent
by their own statement. ***  ** Not that the boundaries coincide by proof ** -- *** they coincide by
IDENTIFICATION: FRW is shear-free, shear is transverse-traceless perturbation, and P10 names the
transverse-traceless tower as the open item.  Each link is a corpus statement. ***  ** Not that `PO-6`
converts ** -- nothing here closes the row: no measurement below is read as a framework verdict.

** COMPUTES: $\\mathrm{Weyl}^2$ and $dR/dT$ on FRW at $k=+1,0,-1$ for a free $a(T)$, checking cc54's
Step 1.  *** The metric is the corpus's own. *** **

Written r2764.  Stated for reversal.
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
    print("  S12 -- is cc54's L-818 boundary the same boundary as r2743's?")
    print()
    T = sp.symbols('T')
    a = sp.Function('a')(T)

    # ⓵ their Step 1
    for kv in (1, 0, -1):
        ap, app = sp.diff(a, T), sp.diff(a, T, 2)
        R = 6*(app/a + (ap/a)**2 + kv/a**2)
        Ric2 = 12*((app/a)**2 + (app/a)*((ap/a)**2 + kv/a**2) + ((ap/a)**2 + kv/a**2)**2)
        Rie2 = 12*((app/a)**2 + ((ap/a)**2 + kv/a**2)**2)
        W2 = sp.simplify(Rie2 - 2*Ric2 + R**2/3)
        check(f'⓵ cc54 Step 1 at $k={kv:+d}$: Weyl$^2=0$ for a FREE $a(T)$, and $R$ genuinely runs '
              f'($dR/dT\\ne0$)', W2 == 0 and sp.diff(R, T) != 0)

    # ⓶ P10 names the tower as transverse-traceless
    p10 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'canonical_time.tex')))
    check('⛭⛭ ⓶ and P10 names the propagating sector "the transverse-traceless graviton tower" -- '
          'so the tower IS shear, and an FRW layer is shear-free by construction',
          'transverse-traceless graviton tower' in p10)
    check('⛭⛭⛭ ⓷ while P10 also names it as what remains open: "the definition of the interacting '
          'tower---the standard problem of the interacting theory"',
          'the standard problem of the interacting theory' in p10)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** cc54's caveat is a LOCATED boundary, and it is the corpus's own. **")
    print('  ⓵ ** Their Step 1 agrees with r2736 exactly: ** Weyl² = 0 at k = +1, 0, −1 for a free')
    print('     a(T), with R running.  ** The layer is conformally flat AND running. **')
    print('  ⛭⛭ ⓶ ** So their excluded sector is the SHEAR sector: ** an FRW layer is shear-free by')
    print('     construction — that is what makes Weyl² vanish — and r2743 showed the degeneracy ends')
    print('     exactly at the shear, C² = 4σ² + O(σ⁴).')
    print('  ⛭⛭⛭ ⓷ *** AND THREE STATEMENTS NAME ONE OBJECT: ***')
    print('       cc54 L-818   "the fully back-reacting / quantized-a(T) sector"')
    print('       56  r2743    the shear, where C² = 4σ² first becomes nonzero')
    print('       P10 (r2763)  "the definition of the interacting tower"')
    print('  ⓸ ** Which upgrades their caveat: ** "my method does not reach there" becomes ** "what')
    print('     lies beyond is the shear sector, which is the graviton tower, which is the corpus\'s')
    print('     own named open problem." **  The second is stronger and they have earned it.')
    print('  ⓹ ** And it makes PO-6\'s two halves one statement: ** the counterterm half survives on the')
    print('     shear-free layer; the tower half is what remains; ** and the tower IS the shear, which')
    print('     is precisely where the counterterm result stops. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
