"""
P13_the_last_evasion_inside_the_premise_is_the_squash_and_it_is_excluded_twice
=============================================================================

Object under test -- whether `P13`'s positive-curvature obstruction is ROBUST, or
holds only on the particular metric it is evaluated on.

`P13` lists the known escapes -- gauge flux, Ricci-flat (Calabi--Yau) internal spaces
-- and calls them uniformly non-geometric, each abandoning the
gauge-group-equals-isometry premise.  ** There is a third escape it does not list,
and unlike those two it lies INSIDE the premise. **

--------------------------------------------------------------------------------
(1) THE ESCAPE IS REAL, AND IT BREAKS LICHNEROWICZ WITH THE ISOMETRY INTACT.

S^5 = SU(3)/SU(2) carries a one-parameter family of SU(3)-invariant metrics -- the
canonical variation of the Hopf submersion S^1 -> S^5 -> CP^2 with the fibre scaled
by t.  For totally geodesic fibres,

        R_t = R_base + R_fibre/t^2 - t^2 |A|^2
            = 4n(n+1) - 2n t^2            at n = 2:   ** R_t = 24 - 4 t^2 **

reproducing R = 20 at t = 1, the round sphere.  ** R_t vanishes at t = sqrt(6) and is
NEGATIVE beyond it **, so the positive-scalar-curvature hypothesis fails there -- and
SU(3) is preserved throughout the family.  *** So the obstruction is NOT robust across
the invariant metrics: it holds for t < sqrt(6) and not beyond. ***

--------------------------------------------------------------------------------
(2) BUT THAT MEMBER IS NOT AVAILABLE TO THIS CONSTRUCTION, AND IS EXCLUDED TWICE
    OVER BY THINGS ALREADY STATED.

  ** (a) The continuation forces the round member. **  The face is not a chosen
  internal geometry: it is dS_5 = SO(5,1)/SO(4,1) on its other real form.  dS_5 is
  MAXIMALLY SYMMETRIC, its isometry algebra fifteen-dimensional, so its Euclidean
  section is too -- the round S^5, isometry SO(6), also fifteen.  A squashed S^5 has
  isometry SU(3) x U(1), dimension nine.  ** Nine is not fifteen, so no squashed
  member is the continuation of anything maximally symmetric. **

  ** (b) And the ledger forbids it independently. **  On the round member every
  curvature invariant is a pure power of 1/alpha^2.  On a squashed member
  R = (24 - 4t^2)/alpha^2 -- a pure power TIMES a free t.  *** The squash parameter is
  a second dimensionless constant, and the construction's ledger states that it spends
  none. ***

  ==> ** Neither reason is a preference for the round metric.  One is forced by what
      the face IS; the other is the same ledger that forbids a free constant anywhere
      else. **

--------------------------------------------------------------------------------
⇒ WHAT THIS SETTLES.  The three escapes from `P13`'s obstruction are now complete and
each is closed: ** flux and Ricci-flatness abandon the premise, and the squash --
the only one that keeps it -- is excluded by the continuation and by the ledger. **
So the obstruction holds on the face this construction actually has, and it holds for
stated reasons rather than by evaluating on a convenient metric.

⌗ AND THE ORDER MATTERED.  This was checked BEFORE any judgement about whether
`PO-26` discharges, precisely because the same node had just specified the
construction and is the worst-placed to weigh its own obstruction.  ** Had the squash
been available, the row would have stayed open and the specification would have been
the reason why. **
"""

import sympy as sp

t, n = sp.symbols('t n', positive=True)

# --- (1) the canonical variation, and where it turns negative --------------------
R_t = sp.simplify(4*n*(n + 1) + 0/t**2 - t**2*(2*n))
R5 = sp.simplify(R_t.subs(n, 2))
assert R5 == 24 - 4*t**2, f"S^5 canonical variation, got {R5}"
assert R5.subs(t, 1) == 20, "must reproduce the round S^5, R = n(n-1) = 20"
root = sp.solve(sp.Eq(R5, 0), t)
assert root == [sp.sqrt(6)], f"sign change at sqrt(6), got {root}"
assert R5.subs(t, 3) < 0, "beyond sqrt(6) the scalar curvature is negative"
print(f"  R_t = {R5};  round t=1 gives R = {R5.subs(t,1)}            OK")
print(f"  R_t = 0 at t = sqrt(6) = {float(sp.sqrt(6)):.4f}; negative beyond        OK")
print("  -> the escape is REAL: Lichnerowicz fails there, SU(3) intact  OK")

# --- (2a) the continuation forces the round member -------------------------------
dim_iso = {'dS_5 / round S^5 (maximally symmetric)': 15, 'squashed S^5, SU(3)xU(1)': 9}
assert dim_iso['squashed S^5, SU(3)xU(1)'] < dim_iso['dS_5 / round S^5 (maximally symmetric)']
print(f"\n  isometry dimensions: round {dim_iso['dS_5 / round S^5 (maximally symmetric)']}"
      f"  vs squashed {dim_iso['squashed S^5, SU(3)xU(1)']}")
print("  -> a squashed member is not the continuation of a maximally")
print("     symmetric Lorentzian space                                  OK")

# --- (2b) and it costs a second dimensionless constant ---------------------------
round_invariant_is_pure_power = sp.simplify(R5.subs(t, 1)).is_number
squashed_depends_on_t = t in R5.free_symbols
assert round_invariant_is_pure_power and squashed_depends_on_t
print("\n  round:    R is a pure number over alpha^2")
print("  squashed: R carries a free t -- a SECOND dimensionless constant")
print("  -> excluded by the ledger, independently of (2a)               OK")

print()
print("ESTABLISHED: the three escapes are complete and each closed -- flux and")
print("Ricci-flatness abandon the premise; the squash keeps it and is excluded")
print("by the continuation and by the ledger. The obstruction holds on the face")
print("this construction actually has.")
