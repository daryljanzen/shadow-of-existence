#!/usr/bin/env python3
"""RECEIPT — functional-analysis bake `F16`: ** P08 DESCRIBES ITS OPERATOR BY KERNEL, IMAGE,
INJECTIVITY AND SURJECTIVITY — THE FOUR INVARIANTS OF A LINEAR MAP — AND THE MATTER FUNCTIONAL IS
AFFINE.  THE VACUUM SECTOR IS A COSET OF THE KERNEL, NOT THE KERNEL, AND M IS THE COSET'S AFFINE
COORDINATE. **

LEVEL: NO RATE — linear versus affine maps.

WHY THIS PROBE.  P08 was estimated MEDIUM, and F13 had already opened half of it by verifying that the
  "vacuum kernel" is an operator null space of dimension one.  Reading the rest, P08 describes the
  slicing operator in the vocabulary of linear algebra throughout: it is "SURJECTIVE onto its image by
  construction", it is "NOT INJECTIVE on arrows" (three distinct cuts return one geometry), and "the
  vacuum sector is exactly the KERNEL of the matter functional, derived, not matched".

  ** Four invariants of a linear map, applied to two different objects.  So: is the matter functional
  linear? **

IT IS NOT.  Testing additivity on f = g + h:

      T[g+h] - (T[g] + T[h])  =  1 - Lambda r^2   != 0

  ** The functional is AFFINE: T[f] = L[f] - b with L[f] = r f' + f linear and b = 1 - Lambda r^2
  constant. **

SO THE VACUUM SECTOR IS A COSET, NOT A KERNEL.  The kernel of the LINEAR part is f = C/r, dimension
  one.  The preimage of zero of the AFFINE map is f = C/r + 1 - Lambda r^2 / 3 -- ** the kernel
  translated by a particular solution.  A coset. **  And the physics is exactly right either way: M is
  the single free constant, and the vacuum set is one-dimensional AS AN AFFINE SPACE, with M its
  affine coordinate.

WHAT THIS ADDS TO F13.  F13 found `kernel` x147 carrying four senses across the corpus.  ** Here is a
  fifth distinction inside the largest of those senses: the "vacuum kernel" is an affine preimage, and
  calling it a kernel is right only once the inhomogeneity is absorbed.  Not an error -- the
  translated set is what the physics needs -- but the word is doing affine duty in the corpus's
  most-used technical term. **

  And it sharpens P08's own sentence: "the vacuum sector is exactly the kernel of the matter
  functional" is exact for the LINEAR PART and a coset for the functional as written.

VERDICTS ARE ASSERTS.
"""
import sympy as sp

r, Lam = sp.symbols('r Lambda', positive=True)
f, g, h = sp.Function('f'), sp.Function('g'), sp.Function('h')

print("=" * 78)
print("  F16 — the matter functional is affine, so the vacuum sector is a coset")
print("=" * 78)

print("\n  P08's matter functional:  T[f] = r f' + f - 1 + Lambda r^2")

lhs = r * sp.diff(g(r) + h(r), r) + (g(r) + h(r)) - 1 + Lam * r**2
rhs = (r * sp.diff(g(r), r) + g(r) - 1 + Lam * r**2) + (r * sp.diff(h(r), r) + h(r) - 1 + Lam * r**2)
defect = sp.simplify(lhs - rhs)
print(f"\n  additivity test:  T[g+h] - (T[g] + T[h]) = {defect}")
assert defect != 0, "the functional must fail additivity"
assert sp.simplify(defect - (1 - Lam * r**2)) == 0, "and the defect is exactly the constant term"
print("  ** VERDICT 1: nonzero, and equal to the constant term.  The functional is AFFINE:")
print("     T[f] = L[f] - b with L[f] = r f' + f linear and b = 1 - Lambda r^2. **")

ker = sp.dsolve(sp.Eq(r * sp.Derivative(f(r), r) + f(r), 0), f(r))
pre = sp.dsolve(sp.Eq(r * sp.Derivative(f(r), r) + f(r) - 1 + Lam * r**2, 0), f(r))
C1 = sp.Symbol('C1')
print(f"\n  kernel of the LINEAR part L : {ker}")
print(f"  preimage of 0 of the AFFINE T: {pre}")
assert sp.simplify(ker.rhs - C1 / r) == 0
assert sp.simplify(pre.rhs - (C1 / r + 1 - Lam * r**2 / 3)) == 0
diff = sp.simplify(pre.rhs - ker.rhs)
print(f"  their difference             : {diff}   (a fixed particular solution)")
assert diff.free_symbols <= {r, Lam}, "the difference must not contain the free constant"
print("  ** VERDICT 2: the preimage is the kernel TRANSLATED by a particular solution -- a")
print("     COSET, not a linear subspace.  One-dimensional as an AFFINE space, with M its")
print("     affine coordinate. **")

print("\n  ** VERDICT 3: and the physics is right either way -- M is the single free constant.")
print("     What this adds to F13 is a fifth distinction INSIDE its largest sense: the")
print("     'vacuum kernel' is an affine preimage, and the word is doing affine duty in the")
print("     corpus's most-used technical term (x147, four senses). **")

print("\n  ** VERDICT 4: so P08's 'the vacuum sector is exactly the kernel of the matter")
print("     functional' is exact for the LINEAR PART, and a coset for the functional as")
print("     written. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
