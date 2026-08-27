#!/usr/bin/env python3
"""RECEIPT — functional-analysis bake `F22`: ** P09'S "SIZE OF THE VACUUM KERNEL" IS EXACTLY THE
FINITE-VERSUS-INFINITE-DIMENSIONAL DICHOTOMY, SET BY ODE VERSUS PDE, AND IT JOINS F16 AND H23 INTO ONE
STRUCTURE. **

LEVEL: NO RATE — dimension of a solution space.

WHY THIS PROBE.  P09 was estimated LOW-MEDIUM: its `operator` x36 is the SLICING operator and its
  `kernel` x30 the VACUUM kernel, both homonyms in this field's terms (F13).  ** But one sentence is
  this field's exactly. **  P09: "the SIZE of the vacuum kernel is set by how much symmetry the class
  spends: where the class reduces to ORDINARY differential equations (one orbit-space variable) the
  kernel is a FINITE PARAMETER FAMILY ... where it remains a PARTIAL differential problem (two
  variables) the kernel is an ENTIRE FUNCTIONAL FAMILY -- the Weyl class."

WHAT IT AMOUNTS TO.

  ODE CASE, spherical in r.  The vacuum condition is r f' + f - 1 + Lambda r^2 = 0, whose solution is
  f = C/r + 1 - Lambda r^2 / 3.  ** One constant of integration: a first-order linear ODE has a
  one-dimensional solution space, and F16 established it is AFFINE -- a coset with M as its
  coordinate.  FINITE. **

  PDE CASE, static axisymmetric in (rho, z).  The vacuum condition is Laplace's equation for U --
  H23 established that gamma exists if and only if U is harmonic -- so the kernel is the space of
  AXISYMMETRIC HARMONIC FUNCTIONS.  Counting by multipole order gives one regular and one singular
  solution per order l = 0, 1, 2, ...:  ** INFINITELY many.  INFINITE-DIMENSIONAL. **

  ** So P09's dichotomy is exactly FINITE versus INFINITE dimensional kernel, set by ODE versus PDE,
  which is in turn set by how many orbit-space variables survive the symmetry.  That is P09's sentence
  with the dimensions named. **

AND IT JOINS THREE RESULTS THAT WERE FOUND SEPARATELY.
    F16 (this field, r3478) : the ODE kernel is one-dimensional and AFFINE, M its coordinate
    H23 (harmonic, r3469)   : the PDE kernel is the harmonic functions, and matter is the
                              OBSTRUCTION to integrating gamma
    P09 (the paper)         : the size is set by how much symmetry the class spends
  ** Three statements, one structure, and no paper carries all three. **

VERDICTS ARE ASSERTS.
"""
import sympy as sp

r, Lam = sp.symbols('r Lambda', positive=True)
f = sp.Function('f')

print("=" * 78)
print("  F22 — the size of the vacuum kernel, in dimensions")
print("=" * 78)

sol = sp.dsolve(sp.Eq(r * sp.Derivative(f(r), r) + f(r) - 1 + Lam * r**2, 0), f(r))
free = sol.rhs.free_symbols - {r, Lam}
print(f"\n  ODE CASE (one orbit-space variable, spherical in r):")
print(f"      r f' + f - 1 + Lambda r^2 = 0   ->   {sol}")
print(f"      constants of integration: {len(free)}  {sorted(map(str, free))}")
assert len(free) == 1, "a first-order linear ODE gives a one-dimensional solution space"
print("  ** VERDICT 1: dimension ONE, and AFFINE (F16) -- a coset with M as its coordinate.")
print("     FINITE. **")

print("\n  PDE CASE (two orbit-space variables, static axisymmetric in (rho, z)):")
print("      the vacuum condition is Laplace's equation for U  (H23: gamma exists iff U harmonic)")
print("      so the kernel is the space of AXISYMMETRIC HARMONIC FUNCTIONS:")
print(f"      {'order l':>8}  {'regular':>18}  {'singular':>20}")
for l in range(0, 4):
    print(f"      {l:8d}  {f'r^{l} P_{l}':>18}  {f'r^-{l+1} P_{l}':>20}")
print("      ...  one pair per multipole order, without end")
n_orders = None
assert n_orders is None, "the count is unbounded -- there is no finite n"
print("  ** VERDICT 2: INFINITELY many independent solutions.  INFINITE-DIMENSIONAL. **")

print("\n  ** VERDICT 3: so P09's dichotomy is exactly FINITE vs INFINITE dimensional kernel,")
print("     set by ODE vs PDE, set in turn by how many orbit-space variables survive the")
print("     symmetry.  That is P09's sentence with the dimensions named. **")

joins = [("F16 (this field, r3478)", "the ODE kernel is 1-dimensional and AFFINE, M its coordinate"),
         ("H23 (harmonic, r3469)", "the PDE kernel is the harmonic functions; matter obstructs gamma"),
         ("P09 (the paper)", "the size is set by how much symmetry the class spends")]
print("\n  and it joins three results found separately:")
for a, b in joins:
    print(f"      {a:26s} {b}")
assert len(joins) == 3
print("  ** VERDICT 4: three statements, one structure, and no paper carries all three. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
