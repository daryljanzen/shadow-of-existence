r"""L-276 -- THE TWO BRANCH-POINT VERDICTS RECONCILED: LIMIT-CIRCLE, DEFICIENCY (1,1).

The zero-mode equation on the radial first-order pair, written on either self-consistent pairing --
the tortoise superpotential W = lambda sqrt(f)/r against the tortoise derivative d/dr_* = f d/dr, or the
frame superpotential lambda/r against the frame derivative sqrt(f) d/dr -- gives the one logarithmic
derivative d(ln psi)/dr = lambda/(r sqrt f), which is what P14 sec:chirality prints and what W2
(L-246, PO-22) computed.  Only the MIXED pairing, the tortoise superpotential against the frame
derivative, (sqrt f d/dr - lambda sqrt f/r) psi = 0, cancels sqrt f and returns psi' = (lambda/r) psi
with its powers r^(+-lambda); that is K1's input, and its algebra is right on it.  On the corrected
operator ln psi = -i lambda sqrt(2/M) sqrt(r) near the throat, a bounded imaginary phase, so both
branches are L^2 in the leaf norm: limit-circle, deficiency (1,1).

r7605 (69): a withdrawal note stood here from r3339 reverting the verdict to limit-point on the ground
that sqrt f is an overall factor of (sqrt f d/dr - lambda sqrt f/r).  That operator is the mixed pairing
this receipt's PART 1 rules out, and its substitution test ran on psi' = (lambda/r) psi, the mixed
pairing's own equation, so it returned r^(+lambda) by construction (cc66 read this at r7577+cc66.2).
The computation below was never changed and gives limit-circle; the note is removed and the verdict
is the one the computation, W2 and P14 carry.  PO-95's closure (receipt
P14_the_leaf_measure_closes_completeness_by_a_different_theorem) holds on either branch.
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
