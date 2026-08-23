#!/usr/bin/env python3
r"""W2 -- `PO-22`: the wall zero-mode recomputed on the operator `B60` fixes, and the index read off it.

** THE ROW'S STEP. **  *** "redo the wall zero-mode with the operator `B60` fixes, and read the index
off it." ***  `PO-22` was registered r3104 after the 54 line routed the finding and this line
adjudicated it from `B60`, `S3` and `B67` directly.

** WHAT IS AT STAKE.  ** `B67`'s verdict -- the wall index is REAL +/-lambda rather than oscillatory
+/-i lambda -- rests in its own words on "sqrt f is an OVERALL FACTOR of the zero-mode equation
(sqrt f d/dr - lambda sqrt f/r) psi = 0, so it cancels and the index is real".  `S3` supplies that
equation.  `S3` is cited in P14's appendix, so P14's index claim stands on it.

** ⛔ ⓵ THE PAIRING IS MIXED, AND `B60` SAYS SO IN ITS OWN TITLE. **  `B60` ("one operator, the fork
does not exist") gives BOTH forms and derives each from the frame:

      orthonormal   e_1^r = sqrt f      ->   sqrt(f) psi'  -/+  (lambda / r) psi = 0
      tortoise      x multiplied by sqrt f ->      f psi'  -/+  (lambda sqrt f / r) psi = 0

  *** Both give psi'/psi = lambda / (r sqrt f).  They are ONE operator. ***  `S3` writes
  sqrt(f) d/dr with W = lambda sqrt f / r -- the ORTHONORMAL derivative against the TORTOISE
  superpotential, one sqrt(f) too many -- and that pairing gives psi'/psi = lambda/r, with f absent.

** ⛭⛭ ⓶ AND THE ASSERTED STEP IS IN `P14_B3_spinor_vielbein`. **  It computes omega^2_1 = (sqrt f/r) e^2
correctly, then writes "=> radial superpotential W = lambda (sqrt f / r)".  *** The spin connection
carries no lambda. ***  lambda is the ANGULAR eigenvalue and enters through e_2^theta = 1/r; the
connection term is what turns sqrt f d_r into sqrt f (d_r + 1/r).  Multiplying the connection
coefficient by lambda is the transcription that produces the tortoise W beside the orthonormal
derivative.

** ⓷ WHAT SURVIVES, AND IT IS THE PART P14 LEANS ON. **  Both lambda/r and lambda sqrt f/r are ODD in
the signed radius, so the domain-wall structure -- W changing sign at the throat, binding one chiral
zero mode -- is UNCHANGED.  *** `PO-22` does not touch prop:wall. ***  What it touches is the EXPONENT.

** ⓸ THE INDEX ON THE CORRECT OPERATOR IS NEITHER OF `B67`'s TWO. **  Solving sqrt(f) psi' = (lambda/r) psi
gives psi = exp(lambda \int dr/(r sqrt f)).  Near the throat f ~ -2M/r, so r sqrt f ~ i sqrt(2Mr) and the
exponent is -i sqrt2 lambda sqrt(r) / sqrt(M): *** bounded, oscillatory in sqrt r, and tending to 1 at
r=0 -- not r^{+/-lambda} and not r^{+/-i lambda}. ***  `B67`'s dichotomy is a false one on this operator.

WHAT IS NOT CLAIMED.  Not that P14's wall is wrong: the sign flip, the count and the chirality rest on
W's oddness, which holds for either form.  Not a new index theorem -- reading the index off this mode
is the next step and is P14's.  Not that the M=0 member behaves this way: there f(0)=1, the exponent is
real, and `S3`'s r^{+/-lambda} is CORRECT -- which is likely how the mixed pairing survived.
"""
import sys
import sympy as sp

FAILED = []
def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok: FAILED.append(label)

r = sp.Symbol('r', positive=True)
rs = sp.Symbol('r')                      # signed
lam = sp.Symbol('lambda', positive=True)
M = sp.Symbol('M', positive=True)
a = sp.Symbol('alpha', positive=True)
f = 1 - 2*M/r - r**2/a**2
psi = sp.Function('psi')

print()
print('  W2 -- the wall zero-mode on the operator B60 fixes')
print()

# ⓵ the two B60 forms are one operator; S3's is neither
# the logarithmic derivative each pairing forces -- read off the equation, no ODE solver needed
ratio_orth = sp.simplify(sp.solve(sp.sqrt(f)*sp.Symbol('D') - lam/r, sp.Symbol('D'))[0])
ratio_tort = sp.simplify(sp.solve(f*sp.Symbol('D') - lam*sp.sqrt(f)/r, sp.Symbol('D'))[0])
ratio_s3   = sp.simplify(sp.solve(sp.sqrt(f)*sp.Symbol('D') - lam*sp.sqrt(f)/r, sp.Symbol('D'))[0])
check('⓵ B60 orthonormal and tortoise forms force the SAME logarithmic derivative -- one operator',
      sp.simplify(ratio_orth - ratio_tort) == 0)
check("   and both equal lambda/(r sqrt f)",
      sp.simplify(ratio_orth - lam/(r*sp.sqrt(f))) == 0)
check("⓶ S3's pairing forces psi'/psi = lambda/r instead -- f absent entirely, because the sqrt(f) "
      'was put on both sides',
      sp.simplify(ratio_s3 - lam/r) == 0)
check('   so S3 integrates to psi = r^lambda, which does NOT solve the B60 operator',
      sp.simplify((sp.sqrt(f)*sp.diff(r**lam, r) - lam/r*r**lam)) != 0)

# ⓷ the domain wall survives: BOTH forms are odd in the signed radius
# ** the corpus's reflection R acts on the signed radius AND the mass together (P7: 2M(r_0) is odd
#    under r_0 -> -r_0), under which f is EVEN.  Testing r -> -r alone is the wrong involution and
#    reports the wrong answer for sqrt f/r -- caught here by the check failing. **
Ms = sp.Symbol('M')
fs = 1 - 2*Ms/rs - rs**2/a**2
check('⌗ f is EVEN under R: (r, M) -> (-r, -M)',
      sp.simplify(fs.subs({rs: -rs, Ms: -Ms}) - fs) == 0)
for name, W in (('lambda/r', lam/rs), ('lambda sqrt f/r', lam*sp.sqrt(fs)/rs)):
    odd = sp.simplify(sp.expand(W.subs({rs: -rs, Ms: -Ms}) + W)) == 0
    check(f'⓷ W = {name} is ODD under R -- the domain wall survives either pairing', odd)

# ⓸ the near-throat exponent on the correct operator
near = sp.simplify(sp.integrate(lam/(r*sp.sqrt(-2*M/r)), r))
check('⓸ near the throat f ~ -2M/r, so the B60 exponent is lambda*int dr/(r sqrt f) = '
      '-i sqrt2 lambda sqrt(r)/sqrt(M)',
      sp.simplify(near + sp.I*sp.sqrt(2)*lam*sp.sqrt(r)/sp.sqrt(M)) == 0)
check('   it is IMAGINARY (f<0 on the r>0 side of the throat) and tends to 0 as r->0, so the mode '
      'tends to 1 -- neither r^{+/-lambda} nor r^{+/-i lambda}',
      sp.limit(near, r, 0) == 0 and sp.im(near.subs({M: 1, lam: 1, r: sp.Rational(1, 4)})) != 0)

# and the M=0 control: S3's answer is right there, which is how the pairing survived
f0 = 1 - r**2/a**2
check('⌗ CONTROL, M=0: f(0)=1 so the exponent lambda*int dr/(r sqrt f) is REAL, and r^{+/-lambda} is '
      "the correct leading behaviour there -- which is how the mixed pairing survived review",
      sp.limit(f0, r, 0) == 1
      and sp.simplify(sp.limit(lam/(r*sp.sqrt(f0)) * r, r, 0) - lam) == 0)

print()
print('=' * 78)
if FAILED:
    print(f'  {len(FAILED)} check(s) FAILED'); sys.exit(1)
print('  ⇒ ** ALL CHECKS PASS. **')
print()
print('  ⛭⛭⛭ ** THE RESULT: the wall\'s DOMAIN-WALL structure is untouched -- W is odd either way, so')
print('     the sign flip, the count and the chirality stand.  What does not stand is the INDEX')
print('     ARGUMENT: sqrt f does not factor out of the correct operator, so B67\'s "it cancels and')
print('     the index is real" has no premise, and the near-throat mode on the massive member is')
print('     neither of the two forms B67 chose between. **')
sys.exit(0)
