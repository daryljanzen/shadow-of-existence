"""K8 — THE STRATIFIED GROUPOID'S INVARIANTS.
CONFIRMATION 4: the object is the SO(5,1)-action on the space of cuts C, stratified by orbit type.
The standard invariants of such an action are: the isotropy at each stratum, the orbit dimension
(orbit-stabiliser), and which stratum is PRINCIPAL (smallest isotropy, open and dense).
P12 supplies isotropies; the rest follows and is computed here."""
import numpy as np, itertools
def dso(n): return n*(n-1)//2
G=dso(6); print("="*80); print("K8 — THE ORBIT-TYPE STRATIFICATION OF THE ACTION ON C"); print("="*80)
print(f"\n  dim SO(5,1) = {G}.  Orbit-stabiliser: dim(orbit) = {G} - dim(isotropy).\n")
strata=[("Type O (pure de Sitter)","SO(4,1)",10,"symmetric"),
        ("Nariai","SO(2,1) x SO(3)",6,"symmetric"),
        ("generic SdS","R_t x SO(3)",4,"non-symmetric"),
        ("(P12's list, unnamed)","-",3,"non-symmetric"),
        ("(P12's list, unnamed)","-",2,"non-symmetric"),
        ("(P12's list, unnamed)","-",0,"non-symmetric")]
print(f"   {'stratum':26s} {'isotropy':18s} {'dim h':>6s} {'dim orbit':>10s}   grading")
print("   "+"-"*78)
for lab,iso,d,g in strata:
    print(f"   {lab:26s} {iso:18s} {d:>6d} {G-d:>10d}   {g}")
print("""
  READ IT.  The MOST symmetric cut has the SMALLEST orbit: Type O, isotropy 10, orbit 5.  The
  PRINCIPAL stratum -- smallest isotropy, hence open and dense -- is the isotropy-zero one, orbit 15.
  So pure de Sitter is the most DEGENERATE point of the stratification, not a generic one, and the
  ordering 10 > 6 > 4 > 3 > 2 > 0 is a filtration by how much symmetry the cut retains.
""")
print("STEP 2 — AND NOW THE INVARIANT THAT SURFACES A NUMBER THE CORPUS NAMES AND DOES NOT USE.")
print("  P12: 'the symmetric-pair isotropy dimensions of so(5,1) are {6,7,10}'.")
print("  Enumerate the symmetric pairs of so(5,1) directly -- so(p',q') + so(p'',q'') with")
print("  p'+p''=5, q'+q''=1 -- and take their dimensions:\n")
seen={}
for pp in range(0,6):
    for qq in (0,1):
        p2,q2=5-pp,1-qq
        d=dso(pp+qq)+dso(p2+q2)
        lab=f"so({pp},{qq}) + so({p2},{q2})"
        seen.setdefault(d,[]).append(lab)
for d in sorted(seen):
    if d>0: print(f"     dim h = {d:>2d} :  {' | '.join(sorted(set(seen[d])))}")
print("""
  *** {6, 7, 10} IS CONFIRMED, AND THE CORPUS USES 10 (Type O) AND 6 (Nariai) AND NOT 7. ***
  The dim-7 pairs are so(4)+so(1,1) and so(3,1)+so(2).  P12 lists the dimension and identifies no
  stratum at it.  So either no cut has that isotropy, or the stratum was not checked --
  *** AND P12's OWN WORDING DOES NOT DISTINGUISH THOSE: 'the grading survives at EXACTLY TWO strata'
      is a result about what was tested, while '{6,7,10}' is a fact about the algebra. ***
  That gap is the invariant's find: A THIRD ADMISSIBLE SYMMETRIC DIMENSION, NAMED AND UNOCCUPIED.
""")
print("="*80)

print("\nSTEP 3 — AND THE FILTRATION IS P9's OWN AXIS, READ AS ORBIT TYPE.")
print("  P9: 'the reachable sector runs along the NULL-DEGENERACY (Petrov) AXIS... Nariai pins to the")
print("       SEAM, not the wall -- they are OPPOSITE ENDS of the one null-degeneracy axis.'")
print("  And the isotropy filtration runs:")
for lab,d in [("Type O (pure de Sitter)",10),("Nariai -- P9's INNER end",6),
              ("generic SdS",4),("...",3),("...",2),("the wall -- P9's OUTER end, isotropy 0",0)]:
    print(f"     dim h = {d:>2d}   orbit = {15-d:>2d}   {lab}")
print("  *** SO P9's 'ONE NULL-DEGENERACY AXIS FROM THE SEAM TO THE WALL' IS THE ORBIT-TYPE")
print("      FILTRATION OF THE ACTION, ordered by isotropy dimension, with Nariai and the wall at")
print("      dim 6 and dim 0.  P9 orders the axis by PETROV TYPE; this orders it by ISOTROPY, and")
print("      the two orderings agree on the ends P9 names. ***")
print("  CAUTION, held: agreement at the two named ends is not agreement everywhere.  P9's middle is")
print("  ordered by algebraic type and this by isotropy dimension, and no check has been run that")
print("  those coincide on the Type-I classes.  Stated for the ends only.")

# r2376+c54.158 -- pins the two tables this receipt computes, which are its whole content.
# (1) THE ORBIT-STABILISER COLUMN.  dim SO(5,1) = 15, so the six isotropy dimensions
# 10, 6, 4, 3, 2, 0 give orbits 5, 9, 11, 12, 13, 15.  The DIRECTION is the claim: the most
# symmetric cut (Type O, isotropy 10) has the SMALLEST orbit, 5, and the principal -- open and
# dense -- stratum is the isotropy-zero one at orbit 15, so pure de Sitter is the most DEGENERATE
# point of the stratification rather than a generic one.
# (2) STEP 2's ENUMERATION.  The proper symmetric pairs so(p',q') + so(p'',q'') of so(5,1) have
# dimensions exactly {6, 7, 10} -- P12's own set, confirmed by direct enumeration rather than
# quoted -- and the dimension-7 entry is realised by so(1,1)+so(4) and so(2)+so(3,1), the two
# pairs P12 names no stratum at.  That gap is what K8b then settles.
assert G == 15, G
assert [G - d for _, _, d, _ in strata] == [5, 9, 11, 12, 13, 15]
assert [d for _, _, d, _ in strata] == sorted((d for _, _, d, _ in strata), reverse=True)
assert sorted(d for d in seen if 0 < d < G) == [6, 7, 10], sorted(seen)
assert set(seen[7]) == {'so(1,1) + so(4,0)', 'so(4,0) + so(1,1)',
                        'so(2,0) + so(3,1)', 'so(3,1) + so(2,0)'}, seen[7]
print("="*80)
