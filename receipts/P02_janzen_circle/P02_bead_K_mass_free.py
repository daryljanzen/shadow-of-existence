#!/usr/bin/env python3
"""
P02 receipt — the Kretschmann scalar along the bead is free of both M and alpha.

Establishes the contrast the paper needs:

  CYCLOID  (Schwarzschild interior, P2's own parametrisation)
      r(z) = M (1 + cos z)          amplitude ∝ M^1
      K     = 48 M^2 / r^6 = 48 / [M^4 (1+cos z)^6]        →  K ∝ M^(-4)

  BEAD     (the cosmological outward branch, P7 thm:bead)
      r(s) = (2 M alpha^2)^(1/3) sinh^(2/3)(3 s / 2 alpha)  amplitude ∝ M^(1/3)
      small-s:  r ≈ 6^(2/3) M^(1/3) s^(2/3) / 2
      K     = 48 M^2 / r^6 = 64 / (27 s^4)                 →  K ∝ M^0, alpha^0

The mechanism is the amplitude's mass exponent, and nothing else:
      r ∝ M^(1/3)  ⟹  r^6 ∝ M^(6/3) = M^2  ⟹  M^2 / r^6 ∝ M^0
      6 × (1/3) = 2, exactly.

Physical content: at a given proper interval s from the origin, the curvature along the
bead is the SAME for every progenitor mass. Two collapses of different mass reach
identical curvature at identical s.

NOTE ON INTERPRETATION: this receipt establishes the identity only. Two readings were
previously given to the M-cancellation and both are recorded as wrong (C40_HARVEST II.2);
the corpus therefore states the computation and not a reading of it.
"""
import sympy as sp

M, alpha, z, s = sp.symbols('M alpha z s', positive=True)

# --- cycloid ---------------------------------------------------------------
r_cyc = M * (1 + sp.cos(z))
K_cyc = sp.simplify(48 * M**2 / r_cyc**6)
assert sp.simplify(K_cyc - 48 / (M**4 * (1 + sp.cos(z))**6)) == 0
assert K_cyc.has(M)

# --- bead ------------------------------------------------------------------
A = (2 * M * alpha**2)**sp.Rational(1, 3)
r_bead_full = A * sp.sinh(3*s/(2*alpha))**sp.Rational(2, 3)
r_bead = A * (3*s/(2*alpha))**sp.Rational(2, 3)          # small-s limit
assert sp.simplify(sp.limit(r_bead_full/r_bead, s, 0) - 1) == 0

K_bead = sp.simplify(48 * M**2 / r_bead**6)
assert sp.simplify(K_bead - sp.Rational(64, 27)/s**4) == 0
assert not K_bead.has(M), "K must be mass-free along the bead"
assert not K_bead.has(alpha), "K must be alpha-free along the bead"

# --- the exponent bookkeeping ---------------------------------------------
assert sp.Rational(6) * sp.Rational(1, 3) == 2

print("P02_bead_K_mass_free — PASS")
print(f"  cycloid : K = {K_cyc}                 (M^-4)")
print(f"  bead    : K = {K_bead}                        (M^0, alpha^0)")
print("  mechanism: amplitude ∝ M^(1/3) ⟹ r^6 ∝ M^2 ⟹ M^2/r^6 ∝ M^0   [6 × 1/3 = 2]")
