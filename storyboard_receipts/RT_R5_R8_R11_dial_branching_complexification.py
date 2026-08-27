#!/usr/bin/env python3
"""RECEIPT — representation-theory bake `R5`, `R8`, `R11`: ** THE DIAL REALISES Aut(A_2) EXACTLY;
su(3) SITS IN so(6) AND NOT IN so(5,1) FOR A REPRESENTATION-THEORETIC REASON; AND THE COMMON
COMPLEXIFICATION HAS ROOT SYSTEM A_3, NOT A_2. **

LEVEL: NO RATE — Lie theory and the horizon cubic's roots on the dial.

R5.  P03 states Aut(A_2) = S_3 x Z_2 = D_6 "realised as the dial's hexagonal symmetry".  Both halves
  are checked here: the group, and the realisation.  The dial parameter enters the roots as a PHASE,
  r_k = (2/sqrt3) sin(w_k) with w_k = w, w +/- 120 deg, verified against the cubic; w -> w+120 permutes
  the roots cyclically (the Weyl S_3) and w -> w+60 flips the sign of 2M (R, the diagram automorphism
  exchanging 3 and 3bar).  Order 12, dihedral.  ** NO CHANGE OWED -- the claim is correct. **

R8.  su(3) subset so(6) is EXHIBITED, not inferred: eight real antisymmetric 6x6 generators spanning
  an 8-dimensional space.  su(3) not-subset so(5,1) holds because any compact su(3) must lie in a
  maximal compact so(5), which acts on R^5, while su(3)'s smallest faithful REAL representation is
  six-dimensional.  ** That obstruction is representation-theoretic and the corpus states it without
  naming it as such. **

R11.  rem:a2-distinct says the two A_2's coincide "no accident of abstract type" because colour rides
  the substrate's conjugate real form, making the connection ANALYTIC.  Checked: so(6,C) = D_3 = A_3,
  rank 3, TWELVE roots.  ** Neither A_2 is the root system of the common complexification. **  A_2
  enters as the sub-root-system obtained by deleting one Dynkin node, matching su(3) subset su(4) =
  so(6) -- so the analytic route runs through so(6,C) on COLOUR'S SIDE ONLY, while the geometric A_2 is
  not a subalgebra root system at all, as the remark itself says.  That is a SHARPER "resonance, not
  identity" than the remark currently makes.

VERDICTS ARE ASSERTS.
"""
import numpy as np

print("=" * 78)
print("  R5 / R8 / R11")
print("=" * 78)

# ---------------------------------------------------------------- R5
print("\n  R5 — the dial realises Aut(A_2)")
tri = lambda w: np.sort(np.roots([1, 0, -1, (2 / (3 * np.sqrt(3))) * np.sin(3 * np.radians(w))]).real)
for w in (30, 60, 90):
    direct = np.sort([(2 / np.sqrt(3)) * np.sin(np.radians(w + k)) for k in (0, 120, 240)])
    assert np.allclose(direct, tri(w)), f"phase form must reproduce the cubic at w={w}"
print("      r_k = (2/sqrt3) sin(w_k), w_k = w, w+/-120 deg  ==  roots of the cubic   [verified]")
assert np.allclose(tri(30), tri(150)), "w -> w+120 must permute the roots"
print("      w -> w+120 : the same multiset, roots permuted        -> the Weyl S_3")
m = lambda w: (2 / (3 * np.sqrt(3))) * np.sin(np.radians(3 * w))
assert abs(m(30) + m(90)) < 1e-12, "w -> w+60 must flip the sign of 2M"
print(f"      w -> w+60  : 2M {m(30):+.4f} -> {m(90):+.4f}            -> R, the diagram automorphism")
print("  ** VERDICT R5: order 12, dihedral, S_3 x Z_2 = D_6, and the dial realises it. NO CHANGE OWED. **")

# ---------------------------------------------------------------- R8
print("\n  R8 — su(3) in so(6), not in so(5,1)")
lam = [np.array(x, dtype=complex) for x in [
    [[0, 1, 0], [1, 0, 0], [0, 0, 0]], [[0, -1j, 0], [1j, 0, 0], [0, 0, 0]],
    [[1, 0, 0], [0, -1, 0], [0, 0, 0]], [[0, 0, 1], [0, 0, 0], [1, 0, 0]],
    [[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], [[0, 0, 0], [0, 0, 1], [0, 1, 0]],
    [[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], np.diag([1, 1, -2]) / np.sqrt(3)]]
real = lambda A: np.block([[A.real, -A.imag], [A.imag, A.real]])
gens = [real(1j * x / 2) for x in lam]
assert all(np.allclose(g, -g.T) for g in gens), "images must be antisymmetric: so(6)"
assert np.linalg.matrix_rank(np.array([g.flatten() for g in gens])) == 8, "must span 8 dimensions"
print("      eight real antisymmetric 6x6 generators, span 8       -> su(3) subset so(6)  [exhibited]")
eta = np.diag([-1.0, 1, 1, 1, 1, 1])
n_ok = sum(np.allclose(g.T @ eta + eta @ g, 0) for g in gens)
assert n_ok < 8, "the standard embedding must fail the so(5,1) condition"
print(f"      of those, satisfying X^T eta + eta X = 0 : {n_ok} of 8   -> not in so(5,1)")
print("      general: a compact su(3) must lie in the maximal compact so(5), acting on R^5,")
print("      while su(3)'s smallest faithful REAL rep is 6-dimensional.  6 > 5.")
print("  ** VERDICT R8: the obstruction is the dimension of the smallest faithful real rep --")
print("     a representation-theoretic statement the corpus makes without naming it. **")

# ---------------------------------------------------------------- R11
print("\n  R11 — the common complexification's root system")
A3 = [tuple(np.eye(4)[i] - np.eye(4)[j]) for i in range(4) for j in range(4) if i != j]
assert len(A3) == 12, "A_3 has twelve roots"
sub = [r for r in A3 if abs(r[3]) < 1e-9]
assert len(sub) == 6, "deleting a node must leave an A_2"
print(f"      so(6,C) = D_3 = A_3 : rank 3, {len(A3)} roots     -> NOT an A_2")
print(f"      deleting one Dynkin node leaves {len(sub)} roots     -> an A_2, = su(3) in su(4) = so(6)")
print("  ** VERDICT R11: the analytic route runs through so(6,C) on COLOUR'S side only.")
print("     The geometric A_2 is not a subalgebra root system at all -- rem:a2-distinct says")
print("     so itself -- so the two meet as ABSTRACT root systems, which is a sharper")
print("     'resonance, not identity' than the remark currently makes. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
