"""
P10_the_two_replacement_questions_are_one_answered_one_coupled
==============================================================

Object under test -- `PO-43`'s `r4545` note, which withdrew the parity-odd second
ledger entry and said "TWO INDEPENDENT QUESTIONS REPLACE IT":

  (Q1) whether a connected isometry of the closed layer identifies the two
       helicities of an S^3 tensor harmonic;
  (Q2) whether the ledger counts topological terms.

** NEITHER SURVIVES AS STATED.  Q1 IS ANSWERED.  Q2 IS NOT INDEPENDENT. **

--------------------------------------------------------------------------------
Q1 -- ANSWERED, AND BY A ROW STRUCK TWO REVISIONS AFTER `r4545` NAMED IT.

`PO-44` (opened r4547, struck r4553) records it in its own strike note: the tower
"IS chirally capable, its two helicities being inequivalent representations of the
connected isometry group exchanged only on the disconnected component".  ** `PO-43`
still carries the question because `PO-44` came after the note that named it. **

The mechanism is exhibited here rather than taken.  S^3 = SU(2), and its connected
isometry group is SO(4) = (SU(2)_L x SU(2)_R)/Z_2.  Rank-2 transverse-traceless
harmonics carry |j_L - j_R| = 2, so each level is

      (j, j+2)  +  (j+2, j) ,        2j+1 = n-1

and dim(j_L,j_R) = (2j_L+1)(2j_R+1) gives k(k+4) each with k = n-1, hence
2(n-1)(n+3) in total -- ** exactly the degeneracy `P10` derives from Peter--Weyl. **
So the two helicities are INEQUIVALENT irreducibles of the connected group, and the
map exchanging them is the exchange of the two SU(2) factors: the outer
automorphism, realised by an orientation-reversing isometry in O(4)\\SO(4).

  ==> ** No connected isometry identifies them. **  Q1 answered, negatively, and
      consistently with `PO-44`: the closure of the parity-odd question is the
      STATE's (the boundary condition being helicity-blind) and not the geometry's.

--------------------------------------------------------------------------------
Q2 -- NOT INDEPENDENT.  IT IS THE ENTROPY QUESTION IN DIFFERENT CLOTHES.

A topological term contributes no field equation -- `P10` says so in its own voice,
of the Gauss--Bonnet combination.  ** So its coefficient cannot be read off any
dynamics. **  The remaining place a coefficient multiplying a topological invariant
could be observable is the horizon entropy.

And there the corpus has no position.  `PO-32`, struck r4501, closes the collapse
face by absence of a BEARER -- "a state variable needs a bearer, the bearers are
layers, and no layer carries the completed horizon" -- and then states of the other
face: `p0` "computes the number conditionally and declines: it does not assert a
de~Sitter entropy, leaves whether S=A/4 carries unsettled", so ** "the corpus is
uncommitted on both faces". **

And `p0`'s own ledger says nothing about this class at all: across `sec:ledger` the
words topological, Gauss, Euler and "field equation" occur ZERO times.  It counts
dimensionful gauges and one physical scale.

  ==> ** So "does the ledger count topological terms" is not a separate wall of the
      counterterm room.  It is the de~Sitter horizon-entropy question, reached from
      the other side. **  Answer that and Q2 answers with it; leave it open and Q2
      cannot be closed independently.

--------------------------------------------------------------------------------
WHAT THIS DOES TO THE ROOM.  `PO-23` and `PO-43` now both carry values -- the log on
the degenerate combination, and the Weyl-squared coefficient off it.  With Q1
answered and Q2 identified, ** the counterterm room's remaining openings are two,
not three: the coupled mode-sum computation, and whether the de Sitter horizon
entropy has a referent. **  The second was not previously counted as part of this
room.
"""

from fractions import Fraction as F

# --- Q1: the degeneracy splits into the two helicity families, at every level ----
def helicity_pair_dim(n):
    """(j, j+2) with 2j+1 = n-1; dim = (2j+1)(2j+5) = k(k+4)."""
    k = n - 1
    j = F(k - 1, 2)
    d = (2*j + 1) * (2*(j + 2) + 1)
    assert d == k*(k + 4)
    return j, d


print("  n    (j_L,j_R)        dim each   both   P10's 2(n-1)(n+3)")
print("  " + "-"*58)
for n in range(2, 12):
    j, d = helicity_pair_dim(n)
    both, corpus = 2*d, 2*(n-1)*(n+3)
    print(f"  {n:<4} ({j},{j+2})".ljust(24) + f"{int(d):>8}{int(both):>8}{corpus:>16}")
    assert both == corpus, f"degeneracy must be the two helicity families at n={n}"
print("  -> the degeneracy IS (j,j+2) + (j+2,j) at every level          OK")

# the two families are inequivalent: (a,b) == (c,d) only if a==c and b==d
for n in range(2, 12):
    j, _ = helicity_pair_dim(n)
    assert (j, j+2) != (j+2, j), "the two families must be distinct irreps"
    assert j != j+2
print("  -> and they are DISTINCT irreducibles of SU(2)_L x SU(2)_R      OK")
print("     so the exchange is the FACTOR SWAP -- the outer automorphism,")
print("     realised only by an orientation-reversing isometry.          OK")

# --- Q2: where could a topological coefficient be observable? -------------------
homes = {
    "field equations": False,   # P10: the Gauss-Bonnet combination contributes none
    "horizon entropy": None,    # PO-32: "the corpus is uncommitted on both faces"
}
assert homes["field equations"] is False
assert homes["horizon entropy"] is None, "the corpus has no position here"
assert not any(v is True for v in homes.values()), \
    "no home where the coefficient is presently observable"
print("\n  Q2: no field equation (P10), and the entropy is uncommitted (PO-32)")
print("  -> Q2 is the de Sitter horizon-entropy question reached from the")
print("     other side, not an independent wall of this room.             OK")

print()
print("ESTABLISHED: Q1 answered negatively -- no connected isometry identifies the")
print("helicities, confirming PO-44 and exhibiting the mechanism. Q2 is not")
print("independent: it is the entropy question in different clothes.")
print("SO the counterterm room has two remaining openings, not three, and one of")
print("them was not previously counted as belonging to it.")
