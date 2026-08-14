#!/usr/bin/env python3
"""S5 -- c54.210's counterterm degeneracy re-derived here, and its SCOPE shown necessary rather than
cautious: the substrate's invariants are one functional, and the layer's curvature runs.

** WHAT 54 CLAIMED (c54.210), folded per `INGESTION.md` -- re-derived, not transcribed. **  p0: "** every
curvature invariant on either face is a pure power of $1/\\alpha^2$ **" -- written to show the construction
cannot force a coupling.  ⇒ ** Read at the counterterm basis it is a SUFFICIENCY: ** the admitted
substrates are a one-parameter family, so the quadratic counterterms collapse.

** ⓵ RE-DERIVED, at $D=4,5,6$. **  On a maximally symmetric space,
$R_{abcd}=K(g_{ac}g_{bd}-g_{ad}g_{bc})$ with $K=1/\\alpha^2$:

      *** D=4:  R^2 = 144/a^4    Ric^2 = 36/a^4    Riem^2 = 24/a^4
          D=5:  R^2 = 400/a^4    Ric^2 = 80/a^4    Riem^2 = 40/a^4
          D=6:  R^2 = 900/a^4    Ric^2 = 150/a^4   Riem^2 = 60/a^4 ***

  ⇒⇒ *** Every one is a RATIONAL CONSTANT times $\\alpha^{-4}$.  So $\\int\\sqrt g\\,R^2$,
      $\\int\\sqrt g\\,R_{\\mu\\nu}R^{\\mu\\nu}$, $\\int\\sqrt g\\,R_{\\mu\\nu\\rho\\sigma}R^{\\mu\\nu\\rho\\sigma}$ and
      $\\int\\sqrt g$ are FOUR MULTIPLES OF ONE FUNCTIONAL on this family.  A divergence of any degree needs
      ONE counterterm where a generic theory needs three. ***

** ⛭⛭ ⓶ AND THE SCOPE 54 ATTACHED IS NECESSARY, NOT CAUTIOUS. **  A basis degeneracy is a property of
the BACKGROUND CLASS -- counterterms are told apart by how they respond to VARYING the background.  ** The
tower does not live on the substrate; it lives on the layer. **  Computing the layer's Ricci scalar for
$a\\sim\\sinh^{2/3}(3Ht/2)$:

      *** R(t) = H^2 (12 cosh(3Ht) - 6)/(cosh(3Ht) - 1)
          t -> 0+  :  R -> infinity        t -> infinity :  R -> 12 H^2 ***

  ⇒ *** The layer's curvature RUNS -- divergent early, $12H^2$ late -- where the substrate's does not.
      So a degeneracy proved on the substrate family does NOT transfer to the layer without argument. ***

** ⓷ SO `PO-6`'s DARK HALF IS NOW DETERMINATE. **  *** Does the one-dimensional basis survive on a
background whose curvature runs?  Stated object; known instrument (the sub-leading heat-kernel
coefficients); decidable answer. ***

WHAT IS NOT CLAIMED.  ** Not that the answer is known ** -- *** the successor question is 54's to run and
is registered `L-543`; this receipt establishes that both its premise and its scope hold. ***  ** Not that
the maximally-symmetric form is derived here ** -- it is the standard form for a constant-curvature space
and is used, not proved.  ** Not that the layer's $R$ is the only relevant invariant ** -- *** the running
of ONE invariant is enough to show the transfer needs argument, which is all the scope claims. ***

Written r2677.  Stated for reversal.
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
    print("  S5 -- is the counterterm basis one-dimensional, and does the scope hold?")
    print()
    p0 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'geometric_core_paper.tex')))
    p10 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'canonical_time.tex')))

    check("⓵ p0 supplies the premise: \"every curvature invariant on either face is a pure power of "
          '$1/\\alpha^{2}$"',
          'every curvature invariant on either face is a pure power of' in p0)
    check('⌗ and c54.210 banked the A7 verdict into P10 -- "counterterm" now appears there',
          'counterterm' in p10)

    # ⓵ the degeneracy, re-derived
    a, K, D = sp.symbols('alpha K D', positive=True)
    for Dv in (4, 5, 6):
        sub = {D: Dv, K: 1/a**2}
        r2 = sp.simplify(((D*(D-1)*K)**2).subs(sub))
        ric2 = sp.simplify((D*(D-1)**2*K**2).subs(sub))
        rie2 = sp.simplify((2*D*(D-1)*K**2).subs(sub))
        allpow = all(sp.simplify(x * a**4).is_number for x in (r2, ric2, rie2))
        check(f'⓶ D={Dv}: $R^2$={r2}, $Ric^2$={ric2}, $Riem^2$={rie2} -- each a rational constant times '
              '$\\alpha^{-4}$', allpow)

    # ⓶ the layer runs
    t, H = sp.symbols('t H', positive=True)
    sc = sp.sinh(sp.Rational(3, 2)*H*t)**sp.Rational(2, 3)
    R = sp.simplify(6*(sp.diff(sc, t, 2)/sc + (sp.diff(sc, t)/sc)**2))
    early = sp.limit(R, t, 0, '+')
    late = sp.simplify(sp.limit(R, t, sp.oo))
    check(f'⛭⛭ ⓷ and the layer\'s Ricci scalar RUNS: $R\\to${early} as $t\\to0^+$ and $\\to${late} as '
          '$t\\to\\infty$',
          early == sp.oo and late == 12*H**2)
    check('⇒ so a degeneracy proved on the substrate family does NOT transfer to the layer without '
          'argument -- the scope is necessary, not cautious',
          early != late)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** both halves hold -- the degeneracy is exact, and the scope is necessary. **")
    print('  ⓵ ** At D=4,5,6 every quadratic invariant is a RATIONAL CONSTANT times alpha^-4. **  So the')
    print('     three quadratic counterterms and the volume term are ** four multiples of one')
    print('     functional **: a divergence of any degree needs ONE counterterm where a generic theory')
    print('     needs three.')
    print('  ⛭⛭ ⓶ ** And the layer\'s curvature RUNS: ** R -> infinity early, 12H² late, for')
    print('     a ~ sinh^(2/3)(3Ht/2) -- where the substrate\'s does not.')
    print('     ⇒ *** A basis degeneracy is a property of the BACKGROUND CLASS, and the tower lives on')
    print('       the LAYER.  So the transfer needs argument -- the scope 54 attached is NECESSARY, not')
    print('       cautious. ***')
    print('  ⓷ ** PO-6\'s dark half is therefore determinate: ** does the one-dimensional basis survive')
    print('     on a background whose curvature runs?  ** Stated object, known instrument, decidable')
    print('     answer. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
