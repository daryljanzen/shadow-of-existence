"""K8b — SETTLING THE DIMENSION-SEVEN STRATUM, rather than leaving it dangling.
P9's necessary bound is the constraint, and it is SHARPER than 'a subgroup of so(5,1)':
   'a geometry swept by H <= SO(4,1) INHERITS H' -- THE SWEEP SUBGROUP LIES IN SO(4,1), not in the
   whole of SO(5,1).  dim so(4,1) = 10.
So the question is not 'does a dim-7 symmetric pair exist in so(5,1)' -- it does, twice -- but
'does either EMBED IN so(4,1)'.  Checked directly.
ORIGIN: storyboard_receipts/K8b_dim_seven_empty.py -- registered r2376 (c54); edit the origin, not this copy."""
import numpy as np, itertools
def dso(n): return n*(n-1)//2
print("="*80); print("K8b — IS THE DIMENSION-SEVEN STRATUM EMPTY, OR UNEXAMINED?"); print("="*80)
print(f"\n  P9's bound: the sweep subgroup H satisfies H <= SO(4,1), dim = {dso(5)}.")
print("  The two dim-7 symmetric pairs of so(5,1) are so(4)+so(1,1) and so(3,1)+so(2).")
print("  Do they embed in so(4,1)?  so(4,1) has signature (4,1): four spacelike, one timelike.\n")
print("  CANDIDATE A — so(4) + so(1,1), dim 6 + 1 = 7.")
print("    so(4) must rotate FOUR spacelike directions -- and so(4,1) has exactly four, so so(4)")
print("    uses ALL of them, as the maximal compact.")
print("    so(1,1) is a boost: it mixes one spacelike with the timelike direction.")
print("    But that spacelike direction is already carried by so(4), and a boost on it does NOT")
print("    commute with the rotations that move it.  A DIRECT SUM requires commuting factors.")
print("    *** so(4) + so(1,1) DOES NOT EMBED IN so(4,1). ***")
print()
print("  CANDIDATE B — so(3,1) + so(2), dim 6 + 1 = 7.")
print("    so(3,1) uses three spacelike and the one timelike direction.  Of so(4,1)'s five")
print("    directions that leaves exactly ONE spacelike.")
print("    so(2) is a rotation and needs TWO directions to rotate.  Only one remains.")
print("    *** so(3,1) + so(2) DOES NOT EMBED IN so(4,1). ***")
print()
print("  DIMENSION CHECK, as a cross-check on the counting rather than the argument:")
for lab,need,have in [("so(4)+so(1,1)","4 spacelike for so(4), plus a boost on a FIFTH independent spacelike","4 spacelike available"),
                      ("so(3,1)+so(2)","3 spacelike + 1 time for so(3,1), plus 2 more spacelike for so(2)","4 spacelike + 1 time available")]:
    print(f"    {lab:16s} needs {need}")
    print(f"    {'':16s} has   {have}   -> FAILS")
print("""
  *** SO THE DIMENSION-SEVEN STRATUM IS EMPTY IN THE REACHABLE CLASS, AND THE REASON IS P9's OWN
      BOUND: the sweep subgroup lies in SO(4,1), and NEITHER dim-7 symmetric pair of so(5,1) fits
      inside SO(4,1). ***
  The pairs exist in so(5,1); they are not available to a SWEPT geometry.  P12's '{6,7,10}' is a
  fact about the algebra and P12's 'exactly two strata' is a fact about the reachable class, and
  they are consistent: the third admissible dimension is ruled out by the range paper's bound, not
  merely untested.
""")

# r2376+c54.158 -- this receipt argued in prose and computed nothing but two dimensions.  The block
# below computes the steps it states and pins them.
#   (1) P9's BOUND, as a number: dim so(4,1) = 10 inside dim so(5,1) = 15; and the dimension-7
#       symmetric pairs of so(5,1) are exactly the two the text names, so(1,1)+so(4) and
#       so(2)+so(3,1) (K8's enumeration, redone here so this receipt does not merely quote it).
#   (2) THE ARGUMENT ITSELF -- "a DIRECT SUM requires COMMUTING FACTORS".  Build so(4,1)
#       explicitly as the 10 eta-antisymmetric generators of eta = diag(+,+,+,+,-) and solve, as a
#       linear system in all 10 unknowns, for everything commuting with the so(4) block: the
#       CENTRALISER IS ZERO-DIMENSIONAL, so there is no room beside so(4) for the so(1,1) it needs
#       -- candidate A is out.  Same for the standard so(3,1) block: centraliser 0, so no so(2)
#       beside it -- candidate B is out.  CONTROL: the centraliser of a single so(2) generator is
#       4-dimensional, so the method finds room where room exists and the two zeros are content.
#   (3) Cross-check from the other side: NO symmetric pair of so(4,1) itself has dimension 7 --
#       its symmetric-pair dimensions are {4, 6, 10}.
assert dso(5) == 10 and dso(6) == 15
pairs7 = sorted({f"so({pp},{qq}) + so({5-pp},{1-qq})" for pp in range(6) for qq in (0, 1)
                 if dso(pp+qq) + dso((5-pp)+(1-qq)) == 7})
assert pairs7 == ['so(1,1) + so(4,0)', 'so(2,0) + so(3,1)',
                  'so(3,1) + so(2,0)', 'so(4,0) + so(1,1)'], pairs7

eta41 = np.diag([1., 1., 1., 1., -1.])          # so(4,1): directions 0-3 spacelike, 4 timelike
def Mg(i, j):
    X = np.zeros((5, 5))
    for A in range(5):
        for B in range(5):
            X[A, B] = (A == i)*eta41[j, B] - (A == j)*eta41[i, B]
    return X
basis41 = [Mg(i, j) for i in range(5) for j in range(i+1, 5)]
def centraliser_dim(sub):
    cols = [np.concatenate([(X@Y - Y@X).flatten() for Y in sub]) for X in basis41]
    return len(basis41) - np.linalg.matrix_rank(np.array(cols).T, tol=1e-9)
so4  = [Mg(i, j) for i in range(4) for j in range(i+1, 4)]                    # maximal compact
so31 = [Mg(i, j) for (i, j) in [(0,1), (0,2), (0,4), (1,2), (1,4), (2,4)]]    # standard so(3,1)
assert len(basis41) == 10 and len(so4) == 6 and len(so31) == 6
assert centraliser_dim(so4) == 0, centraliser_dim(so4)
assert centraliser_dim(so31) == 0, centraliser_dim(so31)
assert centraliser_dim([Mg(0, 1)]) == 4, centraliser_dim([Mg(0, 1)])     # CONTROL: room exists
assert sorted({dso(pp+qq) + dso((4-pp)+(1-qq))
               for pp in range(5) for qq in (0, 1)}) == [4, 6, 10]
print("="*80)
