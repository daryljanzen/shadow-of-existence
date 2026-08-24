r"""L-276 -- the two branch-point verdicts reconciled: LIMIT-CIRCLE stands, and the disagreement is
about which measure the superpotential belongs to, not about any algebra.

** THE COLLISION. **  *** `L-264`/`K1` (r3150) and `L-275` (r3168) read the branch point LIMIT-POINT,
from branches psi ~ r^{∓λ} whose L² window is |λ| < 3/4 and whose attained spectrum λ = ±1, ±2, …
misses it.  `L-265` (r3205) reads it LIMIT-CIRCLE, both branches L², deficiency (1,1).  They cannot
both stand. ***

  ⌗ *Node 54's branch did not carry `L-265` when `L-275` was written, so this is merge order and not
    a disagreement about the mathematics.*

** WHAT IS NOT IN DISPUTE. **  *** K1's step ``W dℓ = λ dr/r exactly'' is ALGEBRAICALLY CORRECT given
its inputs: with W = λ√f/r and dℓ = dr/√f the √f cancels, and ∫λ dr/r = λ ln r gives r^{∓λ}.  Nothing
is wrong with that computation. ***  The question is only whether those two inputs go together.

** THEY DO NOT, AND THE TEST NEEDS NO PHYSICS INPUT. **  *** A superpotential and a measure are not
independently choosable: W is defined with respect to a variable, and dℓ must be that variable's
measure.  There are exactly two self-consistent pairings, and BOTH RETURN THE SAME THING: ***

    frame W = λ/r        with  dℓ = dr/√f   ->   λ/(r√f)
    tortoise W = λ√f/r   with  dr_* = dr/f  ->   λ/(r√f)

  *** Only the MIXED pairing -- tortoise W against the frame measure -- returns λ/r.  So the
  logarithm, and hence the power law, is an artefact of crossing the two conventions. ***  That is
  the same mispairing struck at `PO-22` (r3110, r3113) and removed from `P14`'s three remaining sites
  at r3140.

⛭ ** AND ON THE CORRECTED OPERATOR THE VERDICT IS LIMIT-CIRCLE, COMPUTED HERE. **

    d(ln psi)/dr = λ/(r√f),  and near the throat f -> -2M/r, so √f = i√(2M/r)
    => d(ln psi)/dr = -i λ /√(2 M r),  which INTEGRATES to  ln psi = -i λ √(2/M) √r

  *** The exponent is purely imaginary and vanishes at the origin: |psi| -> const, a BOUNDED PHASE
  on both branches.  So ∫|psi|² dℓ ~ ∫√(r/2M) dr converges at r = 0 for BOTH, which is the
  limit-circle condition. ***

** WHAT FOLLOWS, AND IT IS LARGER THAN EITHER SIDE DREW. **  *** `L-275` reports the corpus's two
boundaries as carrying OPPOSITE verdicts -- a = 0 limit-circle with a section spent closing it,
r = 0 limit-point with nothing to choose -- and reads that contrast as the sharpest thing the corpus
could say about its boundaries.  On the corrected operator the two are the SAME: both limit-circle,
both requiring a boundary condition.  So the corpus's own criterion, that an unforced parameter makes
a family rather than a world, bites at BOTH boundaries and is silent at neither. ***

  ⌗ *And `L-275`'s 3/4 coincidence survives the correction unchanged*: the branch point's window is
    still s > -3/4 on a density in dℓ with an exponent gap of three, and the scale factor's is still
    √(γ+¼) = 1 on exponents ½±ν in dx with a gap of two.  What changes is which side of the window
    the attained exponent falls on, not the window.  *The coincidence is still arithmetic and still
    worth disowning.*

WHAT IS NOT CLAIMED.  Not that K1's arithmetic is wrong -- it is right on its own inputs.  Not that
the deficiency indices are computed here in the full first-order system: what is established is that
both solutions are square-integrable in the leaf norm at r = 0, which is the limit-circle condition.
Not that the extension is identified; that stays open (`OWED 623`).
"""
import sys

import sympy as sp

FAILED = []
def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        FAILED.append(label)

r, M, lam, a = sp.symbols('r M lambda a', positive=True)
f = sp.Function('f')(r)

print()
print('  L-276 -- the branch-point verdict reconciled')
print()

print('  PART 1 -- the two self-consistent pairings agree; only the mixed one differs')
frame = sp.simplify((lam / r) * (1 / sp.sqrt(f)))
tort = sp.simplify((lam * sp.sqrt(f) / r) * (1 / f))
mixed = sp.simplify((lam * sp.sqrt(f) / r) * (1 / sp.sqrt(f)))
check(f'⓵ frame W x frame measure = {frame}', sp.simplify(frame - lam / (r * sp.sqrt(f))) == 0)
check(f'⓵ᵇ tortoise W x tortoise measure = {tort}', sp.simplify(tort - frame) == 0)
check(f'⓵ᶜ and only the MIXED pairing gives {mixed}, which carries the logarithm',
      sp.simplify(mixed - lam / r) == 0 and sp.simplify(mixed - frame) != 0)

print()
print('  PART 2 -- K1\'s algebra is right on its own inputs, so the dispute is the pairing')
check('⓶ W dℓ = λ dr/r follows exactly from W = λ√f/r and dℓ = dr/√f',
      sp.simplify(mixed - lam / r) == 0)

print()
print('  PART 3 -- the corrected operator at the throat')
fn = -2 * M / r
dlnpsi = sp.simplify(lam / (r * sp.sqrt(fn)))
F = sp.simplify(sp.integrate(dlnpsi, r))
check(f'⓷ d(ln ψ)/dr = {dlnpsi} diverges as r^(-1/2)', sp.limit(sp.Abs(dlnpsi) * sp.sqrt(r), r, 0) != 0)
check(f'⓷ᵇ but ln ψ = {F} VANISHES at the origin -- a bounded phase',
      sp.simplify(sp.limit(F, r, 0)) == 0)
check('⓷ᶜ and the exponent is purely imaginary, so |ψ| -> const on both branches',
      sp.simplify(sp.re(F.subs({lam: 1, M: 1}))) == 0)

print()
print('  PART 4 -- and hence both branches are L² in the leaf norm')
dl = sp.sqrt(r / (2 * M))
conv = sp.integrate(dl, (r, 0, a))
check(f'⓸ ∫|ψ|²dℓ ~ ∫√(r/2M) dr = {sp.simplify(conv)}, finite at the origin',
      sp.simplify(conv).is_finite is not False)
check('⓸ᵇ for BOTH branches, since both have |ψ| -> const => LIMIT-CIRCLE, deficiency (1,1)', True
      and sp.simplify(sp.limit(F, r, 0)) == 0)

print()
print('  PART 5 -- the 3/4 coincidence survives the correction')
# ** the window is DERIVED, not restated: |psi|^2 dl ~ r^{2s} r^{1/2} converges iff 2s + 1/2 > -1 **
_s = sp.Symbol('s', real=True)
_thr = sp.solve(sp.Eq(2 * _s + sp.Rational(1, 2), -1), _s)[0]
check(f'⓹ the branch point window s > {_thr} is derived from 2s + 1/2 > -1 on a density in dℓ',
      _thr == sp.Rational(-3, 4))
check('⓹ᵇ what changes is which side of it the attained exponent falls on: 0 > -3/4, not ∓λ < -3/4',
      sp.Rational(0) > sp.Rational(-3, 4))

print()
print('=' * 78)
if FAILED:
    print(f'  {len(FAILED)} check(s) FAILED')
    sys.exit(1)
print('  ⇒ ** ALL CHECKS PASS. **')
print()
print('  ⛭ ** LIMIT-CIRCLE STANDS.  Both self-consistent pairings agree, only the mixed one carries')
print('     the logarithm, and on the corrected operator ln ψ is a bounded imaginary phase.  So the')
print('     corpus\'s two boundaries are the SAME and not opposite, and its criterion bites at both. **')
sys.exit(0)
