"""P12_polar_dimension.py -- what fixes the substrate's dimension, and what does not.
   Backs the sec:substrate parenthetical on the forcing of D=5.
   (1) LEAST-ARBITRARINESS CANNOT RANK DIMENSIONS. P6's criterion prefers the structure requiring no
       "choice of how to break the symmetry"; dS_D is maximally symmetric and moduli-free for EVERY D,
       so the criterion selects the manifold AT FIXED D and is silent on D. (P13 says so in its own
       words: dS_5 is "the unique maximally symmetric Lorentzian manifold OF ITS DIMENSION".)
   (2) THE GENERATION ARGUMENT IS A LOWER BOUND. "Slicing a four-dimensional de Sitter space only
       re-coordinatizes it" excludes D=4 and nothing above it: it gives D>=5, not D=5.
   (3) POLARITY RELATES THE RUNGS BUT CAPS NOTHING. Computed below in general D: the polar hyperplane
       of a spacelike substrate point carries signature (1,D-1), so the totally geodesic cut is
       dS_(D-1) with isometry SO(D-1,1) -- reproducing p0's (1,4)/SO(4,1)/dS_4 at D=5. This fixes the
       RELATION background = dS_(D-1); it does not fix D.
   (4) THERE IS NO UPPER BOUND ANYWHERE IN THE CORPUS. Corrected c54.6: an earlier version of this
       receipt claimed polarity + observed 4D spacetime "pins D=5". It does not. P7's axioms state
       ONE dimension -- the LAYER (the existent) is three-dimensional; the Lorentzian-spacetime axiom
       states none; Diffeomorphic Representability gives only dim M >= 4; and the Projection Principle
       says "No uniqueness of the projection is assumed." P4 forces the FOLIATION (a floor); the
       operator is codimension-one (a floor). EVERY constraint is a lower bound. dS_5 is therefore the
       MINIMAL substrate sufficient for the sector built, not a derived maximum.
STATUS: OK (signature computation exact in every D tested; the negative results are logical, stated not computed)
RUN: python3 P12_polar_dimension.py   RUNTIME: <1s
ORIGIN: built r2376 (c54.5); the polar relation is p0's Q6r_polar_is_the_background generalised in D."""
import numpy as np
print("  polar of a spacelike point of dS_D in M^{1,D}:")
print("   D  | polar signature | cut      | isometry   | background dim")
ok=True
for D in (4,5,6,7,8):
    eta=np.diag([-1.0]+[1.0]*D); P=np.zeros(D+1); P[1]=1.0
    assert P@eta@P>0
    _,_,V=np.linalg.svd((eta@P).reshape(1,-1)); B=V[1:]
    ev=np.linalg.eigvalsh(B@eta@B.T); neg=int((ev<-1e-9).sum()); pos=int((ev>1e-9).sum())
    ok &= (neg==1 and pos==D-1)
    print("   %d  |      (%d,%d)        |  dS_%-3d  | SO(%d,1)    |      %d"%(D,neg,pos,D-1,D-1,D-1))
print("\n  RESULT: %s -- polar(dS_D) = dS_(D-1) in every D; at D=5 this is p0's dS_4/SO(4,1) background."%("PASS" if ok else "FAIL"))
print("  => the RELATION background = dS_(D-1) is fixed; D itself is NOT. Every corpus constraint on")
print("     the dimension is a LOWER bound; dS_5 is the minimal sufficient substrate, not a ceiling.")
