"""K1 — WHAT GROUPOID DOES P12's ALGEBROID INTEGRATE TO?
CONFIRMATION 4, from P12 at source:
  base    = the SPACE OF CUTS  C  of  dS_5 = SO(5,1)/SO(4,1)
  section = the cosmic clock (P10)
  structure function = the inverse spatial metric
  and the object P12 names in its own notation:  'what the continuous  so(5,1) |x C  realizes'
  connection = the leak of [m,m] into m, 'vanishing exactly at the two symmetric strata'
P5's groupoid, by contrast: objects = charting VANTAGES over ONE geometry; discrete; D_3 = S_3, +R -> D_6.
"""
import numpy as np
print("="*78); print("K1 — THE ALGEBROID IS AN ACTION ALGEBROID, SO IT INTEGRATES"); print("="*78)
print("""
STEP 1 — READ P12's OWN NOTATION.  'so(5,1) |x C' is the semidirect/action form: the Lie algebra
  so(5,1) acting on the base C.  A Lie algebroid of that form is an ACTION ALGEBROID -- the bundle is
  the trivial one g x C, the anchor is the infinitesimal action, and the bracket is the g-bracket
  twisted by the action.
STEP 2 — AND ACTION ALGEBROIDS ARE ALWAYS INTEGRABLE.  The integrability question (Crainic-Fernandes)
  has obstructions in general; for an action algebroid of a Lie algebra g on a manifold M by complete
  vector fields the obstructions vanish and the integrating object is the ACTION GROUPOID
       G |x M  ==>  M ,     objects = points of M,  arrows  m -> g.m .
  *** SO THE GROUPOID P12's ALGEBROID INTEGRATES TO IS  SO(5,1) |x C  ==>  C : ***
  *** OBJECTS ARE CUTS, AND ARROWS ARE THE SUBSTRATE ISOMETRIES CARRYING ONE CUT TO ANOTHER.        ***
STEP 3 — AND THAT IS NOT P5's GROUPOID, WHICH IS THE POINT.
  P5's objects are VANTAGES on ONE geometry; the action groupoid's objects are CUTS.
  The corpus already separates them, by dimension: P12's masthead --
     'the continuous algebroid IS THE SLICING STRUCTURE' (dimension-reducing, 5 -> 4);
     'REASSIGNMENT is DIMENSION-PRESERVING AND DISCRETE.'
  *** SO THE RELATION IS NOT 'SAME OBJECT AT TWO LEVELS'. IT IS ISOTROPY. ***
""")
print("STEP 4 — THE ISOTROPY, and P12 supplies the numbers.")
print("   In an action groupoid the arrows from an object to ITSELF form its ISOTROPY GROUP.")
print("   P12: 'the symmetric-space grading survives at EXACTLY two strata --")
print("         Type O (SO(4,1), dim 10) and Nariai (SO(2,1) x SO(3), dim 6)'.")
def dim_so(p,q=0): n=p+q; return n*(n-1)//2
print(f"     Type O   : SO(4,1)              dim = {dim_so(5)}")
print(f"     Nariai   : SO(2,1) x SO(3)      dim = {dim_so(3)} + {dim_so(3)} = {dim_so(3)+dim_so(3)}")
print(f"     generic  : R_time x SO(3)       dim = 1 + {dim_so(3)} = {1+dim_so(3)}")
print("   -> 10 > 6 > 4.  *** THE ISOTROPY ENHANCES AT EXACTLY THE TWO STRATA. ***")
# r2376+c54.158 -- pins STEP 4 against the numbers P12 records for the two surviving strata, which
# is the only external quantity K1 carries: dim SO(4,1) = 10 (Type O), dim SO(2,1) x SO(3) = 3+3 =
# 6 (Nariai), against the generic isotropy R_time x SO(3) = 1+3 = 4.  The strict chain 10 > 6 > 4
# IS the claim "the isotropy enhances at exactly the two strata"; if the generic value were not
# strictly smallest there would be no jump for the discrete and continuous faces to both read.
assert dim_so(5) == 10
assert dim_so(3) + dim_so(3) == 6
assert 1 + dim_so(3) == 4
assert dim_so(5) > dim_so(3) + dim_so(3) > 1 + dim_so(3)
print("""
STEP 5 — AND THAT IS WHY THE TWO FACES DEGENERATE TOGETHER, WHICH IS THE COINCIDENCE P5 NAMES.
  P12's connection is the leak of [m,m] into m -- it vanishes exactly where the coset grading is
  SYMMETRIC, and a grading is symmetric exactly when the isotropy makes a symmetric pair.
  *** SO 'THE CONNECTION VANISHES' AND 'THE ISOTROPY ENHANCES' ARE ONE STATEMENT ABOUT THE ACTION
      GROUPOID, NOT TWO FACTS THAT HAPPEN TO COINCIDE. ***
  And P5's deck branch point is the locus where sigma has its FIXED POINT -- where two designated
  roots merge, i.e. where the VANTAGE structure degenerates.  A vantage is a choice of designated
  root; the choices collapse exactly when the isotropy that permutes them grows.
  *** BOTH FACES ARE STATEMENTS ABOUT THE ISOTROPY OF ONE ACTION GROUPOID. ***
""")
print("="*78)
print("RESULT K1: the relation P5 identifies and does not develop is the ISOTROPY of the action")
print("  groupoid SO(5,1) |x C ==> C, which is what P12's algebroid integrates to -- automatically,")
print("  action algebroids being integrable.  The DISCRETE face (P5's deck group) lives in the")
print("  isotropy; the CONTINUOUS face (P12's connection) measures its failure to be symmetric.")
print("  They meet at Nariai because THAT IS WHERE THE ISOTROPY JUMPS, and both faces read the jump.")
print("="*78)
