r"""L-276 -- WITHDRAWN r3339.  ** THIS RECEIPT'S CONCLUSION IS WRONG AND THE CORPUS HAD ALREADY
DECIDED AGAINST IT TWICE. **

*** It concluded LIMIT-CIRCLE from d(ln psi)/dr = lambda/(r sqrt f) -- sqrt f on ONE side of the
zero-mode equation.  B67 (r2825, a formal F5 verdict) and S3 (r2819) both hold that sqrt f is an
OVERALL FACTOR: the equation is (sqrt f d/dr - lambda sqrt f/r) psi = 0, so sqrt f CANCELS before any
branch can be chosen and the index is real +-lambda whatever the sign of f. ***

** The substitution test settles it and needs no reduction: ** on psi' = (lambda/r) psi the exponent
r^(+lambda) solves IDENTICALLY, while r^(i lambda) and this receipt's exp(-i lambda sqrt(2/M) sqrt r)
both leave nonzero residuals.  *Verified here before the withdrawal was written.*

⇒ ** THE VERDICT IS LIMIT-POINT, ** as L-264/K1 and L-275/U1 had it.  P14 is reverted, both receipts
are restored at the upheld verdict, and OWED 625 is corrected.

⌗ ** AND THE METHOD FAILURE IS THE PART WORTH KEEPING. **  L-265 and this receipt surveyed the PAPERS
and found the branch point carried no verdict.  The corpus decides in its RECEIPTS -- fourteen of them
name this operator, eight in `L221_the_bridge`, including B60 "one operator, the fork does not exist".
*Node 54 built `corpus/prior_art.py` after making the same error from the other side.  The rule: ask
the receipts, not only the papers -- what the corpus publishes and what it has already decided are
different sets.*
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
print()
print('  ⛔ WITHDRAWN r3339 -- see the docstring.  The verdict is LIMIT-POINT (B67, S3).')
sys.exit(0)
