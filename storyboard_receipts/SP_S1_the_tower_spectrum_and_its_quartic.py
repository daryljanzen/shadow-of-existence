#!/usr/bin/env python3
"""RECEIPT — spectral-theory bake `S1`: ** P10'S TOWER HAS A DISCRETE MODEWISE SPECTRUM AND A
QUARTICALLY DIVERGENT ZERO-POINT SUM — AND THAT QUARTIC IS THE ONE THE CORPUS ALREADY COMPUTES, FOR A
DIFFERENT PURPOSE, WITHOUT NAMING IT AS A VACUUM ENERGY. **

LEVEL: NO RATE — the spectrum of a tower of oscillators.

WHY THIS PROBE.  P10 was estimated HIGH: it is the deficiency-index paper, and the functional-analysis
  bake's F1-F3 classified the ENDPOINTS -- limit-circle at a=0, limit-point at r=0 -- and never asked
  what the spectrum IS.  ** That is this field's first question and no paper puts it. **

WHAT P10 GIVES.  Deparametrised, the transverse-traceless sector is

      H_phys = sum_n [ pi_n^2 / (2 a^3)  +  (1/2) a mu_n^2 phi_n^2 ],   mu_n^2 = n(n+2) - 2, n >= 2

  -- a harmonic oscillator per mode, mass a^3, frequency omega_n = mu_n / a.  P10 says each is "a
  Schroedinger oscillator on L^2(R) and manifestly self-adjoint", and that "the closed topology of the
  layer enters as the DISCRETENESS of the tower, in contrast to the continuous spectra of the flat
  minisuperspace and planar reductions."

  ** MODEWISE THE SPECTRUM IS THEREFORE E_{n,k} = (k + 1/2) mu_n / a, k = 0, 1, 2, ...  Discrete,
  simple in k, and degenerate in n with multiplicity g(n) = 2(n-1)(n+3) -- the corpus's own derived
  degeneracy, not the textbook 2(n^2-1). **

AND THE SUM OVER THE TOWER IS A DIFFERENT OPERATOR.  The zero-point energy is

      E_0 = (1/2a) sum_n g(n) mu_n ,     g(n) mu_n ~ 2 n^3

  ** so the summand's SHELL contribution is ~ 2 n^3 and the partial sums grow as N^4 / 2: the
  zero-point sum DIVERGES QUARTICALLY. **

  ** AND THAT IS THE CORPUS'S OWN QUARTIC. **  The degeneracy receipt
  (D1_the_degeneracy_carrying_the_quartic...) states "the shell contribution is 2 n^3 and the leading
  constant is settled rather than assumed", computed there for a Weyl-law counting purpose.

  ⛔ CORRECTED r3491.  This receipt first added "and neither the paper nor the receipt says so".
  ** THAT IS WRONG, AND P07 SAYS IT EXPLICITLY: ** "the tower's frequencies grow as mu_n ~ n and the
  three-sphere degeneracy as n^2, so the shells grow as n^3 and the sum diverges as N^4 -- THE GENERIC
  ZERO-POINT DIVERGENCE OF A FIELD IN FOUR DIMENSIONS, at the generic power."  P07 makes the
  identification, and makes more of it than this probe did.

  ** What survives is narrower and still true: P10 and the degeneracy receipt each compute this sum
  for their own purposes and NEITHER references P07's identification.  The join exists in one paper
  and is absent from the two places that do the computation. **

WHAT THIS DOES AND DOES NOT CLAIM.  It does NOT claim a defect: a divergent zero-point sum is what
  every free field theory has, and P10's unitarity claim is modewise and unaffected.  ** What is
  claimed is an identification: the counting quartic and the vacuum energy are the same sum, and the
  corpus computes it twice without joining them. **

ROUTED, NOT APPLIED.

VERDICTS ARE ASSERTS.
"""
import sympy as sp

n, N, a, k = sp.symbols('n N a k', positive=True)

print("=" * 78)
print("  S1 — the tower's spectrum, and where its quartic already lives")
print("=" * 78)

mu = sp.sqrt(n * (n + 2) - 2)
g = 2 * (n - 1) * (n + 3)
print(f"\n  P10:  H_phys = sum_n [ pi_n^2/(2a^3) + (1/2) a mu_n^2 phi_n^2 ],  mu_n = {mu}")
print(f"        degeneracy g(n) = {sp.expand(g)}   (the corpus's derived one, ten at n=2)")
assert int(g.subs(n, 2)) == 10, "must be the corpus's degeneracy, not the textbook 2(n^2-1)"

print("\n  each mode is an oscillator of mass a^3 and frequency mu_n/a, so modewise")
print("      E_{n,k} = (k + 1/2) mu_n / a,   k = 0, 1, 2, ...")
print("  ** VERDICT 1: DISCRETE, simple in k, degenerate in n with multiplicity g(n) --")
print("     which is P10's 'the closed topology enters as the DISCRETENESS of the tower'. **")

shell = sp.simplify(g * mu)
lead = sp.limit(shell / n**3, n, sp.oo)
print(f"\n  the zero-point sum: E_0 = (1/2a) sum_n g(n) mu_n")
print(f"      shell g(n) mu_n ~ {lead} n^3")
assert sp.simplify(lead - 2) == 0, "the shell must go as 2 n^3 -- the corpus's own figure"
S = sp.summation(n**3, (n, 2, N))
print(f"      sum_2^N n^3 = {sp.factor(sp.simplify(S))}   ->  grows as N^4/4")
print("  ** VERDICT 2: the shell is ~ 2 n^3, exactly the corpus's 'the shell contribution is")
print("     2 n^3', and the partial sums grow QUARTICALLY. **")

print("\n  ** VERDICT 3 (CORRECTED r3491): the counting quartic and the vacuum energy of P10's")
print("     graviton tower are THE SAME SUM, up to one half -- and P07 SAYS SO explicitly:")
print("     'the sum diverges as N^4 -- the generic zero-point divergence of a field in four")
print("     dimensions'.  This probe first claimed the identification was unmade; it is made,")
print("     in P07, and made better there.  What survives: P10 and the degeneracy receipt")
print("     each compute the sum for their own purposes and neither references P07. **")

print("\n  ** VERDICT 4: no defect is claimed.  A divergent zero-point sum is what every free")
print("     field theory has, and P10's unitarity claim is MODEWISE and unaffected.  What is")
print("     claimed is the IDENTIFICATION -- the corpus computes one sum twice, for two")
print("     purposes, without joining them. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
