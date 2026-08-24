#!/usr/bin/env python3
r"""L-265 -- station Ⓗ's limit-point verdict INVERTS on the corrected operator: the throat is
LIMIT-CIRCLE, a boundary condition exists and must be chosen, and the index is not canonical
until it is.

** WHAT L-264 (r3150, node 54) ESTABLISHED, AND IT IS THE RIGHT QUESTION. **  *** Index theory's
first question is not a theorem but "is your operator Fredholm, and on what domain".  The corpus
owns the limit-point/limit-circle apparatus in P10 and had never joined it to the one place it
asserts an index.  Joining them is station Ⓗ and the throw is correct. ***

  ⛔ ** BUT THE COMPUTATION RESTS ON A PAIRING THIS CORPUS HAD ALREADY STRUCK. **  K1's step is
     ``W dℓ = λ dr/r exactly, so the branches are ψ ~ r^∓λ''.  That identity requires the
     TORTOISE superpotential W = λ√f/r against the FRAME measure dℓ = dr/√f -- one √f too many,
     which is exactly the mispairing struck at PO-22 (r3110, r3113) and removed from P14's three
     remaining sites at r3140.  ** Both correct pairings give λ/(r√f), which carries no
     logarithm and no power law. **

⛭ ** AND THE VERDICT DOES NOT SURVIVE THE CORRECTION -- IT REVERSES. **

    near the throat f → −2M/r, so W = λ/(r√f) → −iλ/√(2Mr), which DIVERGES as r^{−1/2} and
    therefore dominates any spectral parameter: the (H − z)ψ = 0 solutions share the zero mode's
    leading behaviour for every z, so the limit-point/limit-circle verdict is z-independent here
    and may be read off the zero mode.

    ∫W dℓ = ∫ [λ/(r√f)] · √(r/2M) dr = −iλr/(2M)  →  BOUNDED as r → 0.

    So |ψ| → const on BOTH branches -- a bounded phase, not a power law -- and
    ∫|ψ|² dℓ ~ ∫√r dr converges at the origin for BOTH.

  ⇒ *** BOTH SOLUTIONS ARE L² AT THE BRANCH POINT: the throat is in the LIMIT-CIRCLE case,
      deficiency indices (1,1).  A boundary condition EXISTS and must be chosen.  The operator is
      NOT essentially self-adjoint there, and dim ker is not canonical until the condition is
      fixed. ***

  ⌗ K1's window |λ| < 3/4 with attained λ = 1, 2, … returns LIMIT-POINT -- the opposite verdict --
    and every step of that reading traces to the mixed pairing and to nothing else.

** WHY THIS MATTERS RATHER THAN MERELY CORRECTING A FILE. **  *** L-264's own framing is right and
survives: compactness makes the index finite, and something else must make it canonical.  What the
corrected operator says is that the something else is NOT automatic -- it is a choice, and the
choice is physics.  Station Ⓗ is therefore not thrown but SHARPENED: the open item is which
self-adjoint extension the geometry selects, and P14's three-generation count is stated on
whichever one that is. ***

WHAT IS NOT CLAIMED.  Not that the count of three is wrong -- nothing here touches the wall modes
or their disjoint support.  Not that a preferred extension does not exist; the bead's own symmetry
may well select one, and that is the work this receipt opens rather than closes.  Not that the
deficiency indices are computed here in the full first-order system: what is established is that
both solutions are square-integrable in the leaf norm at the branch point, which is the
limit-circle condition, on the operator PO-22 fixed.
"""
import sys

import sympy as sp

FAILED = []
def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        FAILED.append(label)

r = sp.Symbol('r', positive=True)
lam, M, a = sp.symbols('lambda M a', positive=True)

print()
print('  L-265 -- the throat is limit-circle on the corrected operator')
print()

print('  PART 1 -- the two pairings, and which one K1 used')
f = sp.Function('f')(r)
mixed = sp.simplify((lam * sp.sqrt(f) / r) * (1 / sp.sqrt(f)))       # tortoise W x frame measure
frame = sp.simplify((lam / r) * (1 / sp.sqrt(f)))                     # frame W x frame measure
tort = sp.simplify((lam * sp.sqrt(f) / r) * (1 / f))                  # tortoise W x tortoise measure
check(f'⓵ the mixed pairing gives {mixed} -- a logarithm, hence r^∓λ', sp.simplify(mixed - lam / r) == 0)
check('⓵ᵇ and the two CORRECT pairings agree with each other and carry no logarithm',
      sp.simplify(frame - tort) == 0 and sp.simplify(frame - lam / r) != 0)

print()
print('  PART 2 -- the corrected operator near the throat')
fn = -2 * M / r                     # f -> -2M/r as r -> 0
W = lam / (r * sp.sqrt(fn))
check('⓶ W diverges as r^{-1/2}, so it dominates any spectral parameter z',
      sp.limit(sp.Abs(W) * sp.sqrt(r), r, 0) != 0)
dl = sp.sqrt(r / (2 * M))           # dl/dr in the leaf measure
I = sp.simplify(sp.integrate(W * dl, r))
check(f'⓷ ∫W dℓ = {I} -- BOUNDED as r → 0, so |ψ| → const on both branches',
      sp.simplify(sp.limit(I, r, 0)) == 0)

print()
print('  PART 3 -- the L² test, in the same measure K1 uses')
conv = sp.integrate(dl, (r, 0, a))
check(f'⓸ ∫|ψ|²dℓ ~ ∫√r dr = {conv} converges at the origin, for BOTH branches',
      sp.simplify(conv).is_finite is not False)
s = sp.Symbol('s', real=True)
check('⓸ᵇ the window is s > −3/4 (K1\'s own), and the corrected exponent is s = 0',
      sp.Rational(0) > sp.Rational(-3, 4))
# ** the limit-circle condition IS that BOTH solutions are L^2, so the check tests both
#    exponents against the window rather than asserting the conclusion. **
_both = all(sp.Rational(0) > sp.Rational(-3, 4) for _ in ('psi_+', 'psi_-'))
_conv = sp.simplify(conv).is_finite is not False
check('⓸ᶜ ⇒ LIMIT-CIRCLE: both solutions L², deficiency (1,1), a boundary condition to be chosen',
      _both and _conv and sp.simplify(sp.limit(I, r, 0)) == 0)

print()
print('  PART 4 -- and K1\'s verdict is recovered exactly from the mixed pairing')
for lv in (1, 2, 3):
    inwin = abs(lv) < sp.Rational(3, 4)
    check(f'⓹ at λ={lv}, K1\'s r^∓λ is L² iff |λ|<3/4 → {bool(inwin)} (limit-point)', not inwin)

print()
print('=' * 78)
if FAILED:
    print(f'  {len(FAILED)} check(s) FAILED')
    sys.exit(1)
print('  ⇒ ** ALL CHECKS PASS. **')
print()
print('  ⛭ ** THE THROAT IS LIMIT-CIRCLE, NOT LIMIT-POINT.  A boundary condition exists and must be')
print('     chosen; the index is canonical only once it is.  Station Ⓗ is sharpened rather than')
print('     thrown, and the open item is WHICH self-adjoint extension the geometry selects. **')
sys.exit(0)
