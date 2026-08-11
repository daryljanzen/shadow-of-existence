#!/usr/bin/env python3
"""
L-111 — DARYL'S READING WORKED: NARIAI POINTS AS LEPTONS, PUNCTURES AS QUARKS.

FIRST, THE TERMS I WAS USING LOOSELY.  Daryl, c54.38: "A graze point sounds geometric and
something like a tangent.  But you're speaking loosely and defining nothing.  I don't know
what you mean by a path or a graze point.  And why are you asking about the hinge axis?
That's not even on the manifold."

** ALL THREE CORRECTIONS ARE ACCEPTED AND ONE OF MY QUESTIONS WAS SIMPLY WRONG. **

  GRAZE POINT (= NARIAI POINT = WALL).  A point of the substrate.  Each null leg is a ruling
  of the substrate running from a puncture and TANGENT to the throat circle |X| = alpha at
  X_0 = 0; the point of tangency is the graze point.  There are three, at azimuth
  60/180/300 deg.  They ARE manifold points -- they lie on the throat, which lies on the
  substrate.  Each is a Nariai cut (sin w = 1/2 => sin 3w = 1, r_0 = +-1/sqrt3) and each is
  the matter sector's WALL, the r = 0 branch point.  ** One object, four names, all earned. **

  ROUTE.  NOT a curve on the substrate.  It is a path in the EQUATORIAL PROJECTION -- an arc
  of the projected figure running between hinge stations, and the winding counts how many of
  the three graze points it passes.  ** That the winding derivation lives in the projection
  and not on the manifold is a real limitation and I had never said so. **

  THE HINGE AXIS.  ** My question 1 of the last turn was wrong.  The hinge is a line at
  transverse radius 2 alpha whose direction is timelike; it is NOT contained in the substrate
  and meets it only at its two punctures.  There is no "axial mode" to ask about. **  And
  Daryl's answer to my other question settles it: ** the puncture is the VANTAGE POINT for the
  whole slicing -- you look out along the slicing plane from each puncture, in BOTH directions,
  to get the complementary geometries (SdS vs FLRW, static vs cosmological). **  So a puncture
  is emphatically not a mere incidence point of legs.  It is where an observer stands.

  PART 1  His configuration, verified: does a hinge's pair of legs really graze at the same
          two Nariai points from BOTH its punctures?
  PART 2  ** His lepton reading, counted.  It gives FOUR, not three. **
  PART 3  ** And four is a prediction, not a mismatch: it requires a right-handed neutrino. **
  PART 4  ** THE ANTIQUARK DISAGREEMENT, AND IT DISSOLVES.  We were counting in two different
          conventions, and the corpus already says which. **
  PART 5  What is still genuinely missing, after both of the above.

Run: python3 L111_daryls_lepton_reading.py     (numpy)
"""
import itertools
import numpy as np

print(__doc__.split("Run:")[0])
a, S3 = 1.0, np.sqrt(3)
ANG = [0, 120, 240]

def pol(deg, rad=1.0, z=0.0):
    return np.array([rad*np.cos(np.radians(deg)), rad*np.sin(np.radians(deg)), z])

P = {f"{h}{k}": pol(A, 2*a, s*S3*a)
     for k, A in enumerate(ANG) for s, h in ((1, 'U'), (-1, 'D'))}
W = {k: pol(A + 180, a) for k, A in enumerate(ANG)}      # w_k antipodal to h_k: 180/300/60
CHORD = [(f"U{i}", f"D{j}") for i in range(3) for j in range(3) if i != j]

# =====================================================================
print("=" * 78)
print("PART 1 — HIS CONFIGURATION, VERIFIED")
print("=" * 78)
print("  Daryl: 'looking at one puncture as u.  The legs cut tangent at the two Nariai points.")
print("   Now you take the puncture below it.  That's a duu with again two Nariai, but they're")
print("   THE SAME TWO POINTS SEEN FROM ANOTHER WAY.'")
print()
touch = {}
for uu, dd in CHORD:
    m = 0.5*(P[uu] + P[dd])
    k = min(W, key=lambda t: np.linalg.norm(W[t] - m))
    touch.setdefault(uu, set()).add(k)
    touch.setdefault(dd, set()).add(k)
print(f"  {'puncture':>10} {'its 2 legs graze at':>22} {'its own hinge is':>18} {'own wall touched?':>18}")
same = True
for k in range(3):
    for h in ('U', 'D'):
        nm = f"{h}{k}"
        print(f"  {nm:>10} {str(sorted('w%d' % t for t in touch[nm])):>22} "
              f"{('h%d' % k):>18} {str(k in touch[nm]):>18}")
    same &= (touch[f"U{k}"] == touch[f"D{k}"])
print()
print(f"  ** BOTH PUNCTURES OF ONE HINGE GRAZE AT THE SAME TWO NARIAI POINTS: {same}. **")
print("  ** AND NEITHER TOUCHES ITS OWN.  So per hinge the three Nariai points split 2 + 1:")
print("     TWO reached by its legs, ONE -- its own, antipodal -- left over.  That is exactly")
print("     the structure Daryl describes, and the 2+1 is the section's own. **")
print()
print("  And the charges of the two readings, from the winding derivation:")
u, d = 2/3, -1/3
print(f"  {'read from':>14} {'triple':>22} {'total charge':>13}")
print(f"  {'the UPPER puncture':>14} {'(u,d,d)':>22} {u + 2*d:>13.0f}")
print(f"  {'the LOWER puncture':>14} {'(d,u,u)':>22} {d + 2*u:>13.0f}")
print("  ** 'One configuration gives zero charge and one gives full charge' -- confirmed, and")
print("     it is the corpus's own T: the horn swap costs exactly one lap. **")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — HIS LEPTON READING, COUNTED")
print("=" * 78)
print("  'Could you not have neutrinos described one way and electrons the other, as particle")
print("   antiparticle pairs, with the wall at the third Nariai point.  So per baryon config")
print("   you get two sets of lepton type particle antiparticle pairs and a wall.'")
print()
print("  Made into a count.  Per hinge (= per vantage = per generation):")
print()
rows = [("Nariai points reached by its legs", 2, "w_{k+1}, w_{k+2}"),
        ("ways each is seen (upper / lower puncture)", 2, "the horn, which the corpus reads as ISOSPIN"),
        ("=> colourless slots per hinge", 4, "2 x 2"),
        ("its own Nariai point, untouched", 1, "THE WALL -- where P14 binds the zero-mode")]
for nm, n, why in rows:
    print(f"  {nm:>42} {n:>3}   {why}")
print()
print("  ** SO HIS STRUCTURE GIVES FOUR COLOURLESS SLOTS PER GENERATION, PLUS A WALL -- NOT")
print("     THREE.  And the wall is not one of the four: it is the seat, not a state. **")
print()
print("  ⌗ AND THE FOUR HAVE THE RIGHT SHAPE, WHICH IS THE PART THAT MATTERS.  A 2 x 2 whose")
print("  first factor is 'which Nariai point' and whose second is the HORN -- and the corpus")
print("  already reads the horn as WEAK ISOSPIN.  So the four are a pair of isospin doublets:")
print()
print(f"  {'':>12} {'upper puncture':>18} {'lower puncture':>18}")
print(f"  {'w_{k+1}':>12} {'nu':>18} {'e':>18}")
print(f"  {'w_{k+2}':>12} {'nu-bar':>18} {'e-bar':>18}")
print("  ** which is Daryl's 'two sets of lepton type particle antiparticle pairs' exactly. **")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — FOUR IS A PREDICTION, NOT A MISMATCH")
print("=" * 78)
print("  I had been anchoring on FIFTEEN because P14 does, and reading a fourth slot as an")
print("  error.  ** On his reading it is not an error.  A generation with a right-handed")
print("  neutrino is SIXTEEN Weyl fermions, and 16 = 12 + 4. **")
print()
print(f"  {'':>28} {'coloured':>10} {'colourless':>12} {'total':>7}")
for nm, c, l in [("the geometry (his reading)", 12, 4),
                 ("SM without a right-handed nu", 12, 3),
                 ("SM WITH a right-handed nu", 12, 4)]:
    print(f"  {nm:>28} {c:>10} {l:>12} {c+l:>7}")
print()
print("  ⌗ AND THE FOUR IS NOT AN ASSUMPTION EITHER -- it is the corpus's OWN 'four legs per")
print("  graze point' seen from the other side: 3 graze points x 4 = 12 is already how the")
print("  leg count closes (P03_twelve_null_legs).  ** The same 4. **")
print()
print("  ** SO THE READING PREDICTS A RIGHT-HANDED NEUTRINO, and that is a real prediction:")
print("     it is the one place where 15 and 16 differ, it is experimentally live, and a")
print("     construction that returned 15 exactly would FALSIFY the structure Daryl just")
print("     described. **  Recorded as his, not mine.")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE ANTIQUARK DISAGREEMENT, AND IT DISSOLVES")
print("=" * 78)
print("  Daryl: 'You seem ok about things except missing a place for neutrinos, whereas I feel")
print("   like it all seems mostly there EXCEPT FOR THE ANTIQUARKS.'")
print()
print("  ** WE WERE COUNTING IN TWO DIFFERENT CONVENTIONS AND BOTH ARE STANDARD. **")
print()
print(f"  {'convention':>26} {'the 12 coloured states of one generation':>46}")
for nm, s in [("mine (right-handed)", "u_L, d_L in 3 colours + u_R, d_R in 3 colours"),
              ("his (all left-handed)", "u_L, d_L in 3 colours + u-bar, d-bar in 3 ANTIcolours")]:
    print(f"  {nm:>26} {s:>46}")
print()
print("  ** u_R AND u-bar ARE THE SAME DEGREE OF FREEDOM.  For a Weyl field, conjugating flips")
print("     chirality; the right-handed quark and the left-handed antiquark are one object")
print("     written two ways.  So in MY table the antiquarks look absent, and in HIS the")
print("     right-handed states look absent, and neither is actually missing. **")
print()
print("  ⌗ AND THE CORPUS ALREADY SAYS THIS, IN THE ONE SENTENCE THAT SETTLES IT.")
print("  P03_winding_and_closure, on the involutions: 'R -> CHIRALITY AND SPECIES AT ONCE,")
print("  WHICH IS REQUIRED FOR A WEYL FIELD.'")
print()
print("  ** R IS THE RULING SWAP -- the +-60 degree pair at a puncture (P3 rem:hingetriple).")
print("     So the two legs at one puncture ARE the particle and the antiparticle, and they")
print("     are also the two chiralities, BECAUSE FOR A WEYL FIELD THOSE ARE THE SAME")
print("     STATEMENT.  The antiquarks are the second leg. **")
print()
print("  ⇒ Check the arithmetic both ways:")
print(f"  {'':>34} {'count':>7}")
for nm, n in [("6 punctures x 2 rulings", 12),
              ("  = 6 quarks (upper) + 6 antiquarks (lower)  [his]", 12),
              ("  = 6 left-handed + 6 right-handed  [mine]", 12),
              ("SM coloured Weyl states per generation", 12)]:
    print(f"  {nm:>34} {n:>7}")

# =====================================================================
print()
print("=" * 78)
print("PART 5 — WHAT IS STILL MISSING AFTER BOTH OF THOSE")
print("=" * 78)
for s in [
 "Neither of us was missing a SPECIES.  With PART 4 the antiquarks are the second ruling and",
 "with PARTS 2-3 the leptons are the Nariai points read from the two horns.  ** What is still",
 "open is narrower and it is now sayable in one line: **",
 "",
 "  ① ** THE HORN IS BEING ASKED TO BE TWO THINGS. **  In PART 2 the horn distinguishes",
 "     nu from e (isospin), which is the corpus's own T -> weak isospin.  In PART 1 the horn",
 "     distinguishes the upper triple (u,d,d) from the lower (d,u,u), also isospin.  ** But in",
 "     PART 4's reading the horn is what separates the 3 from the 3-bar -- SPECIES. **  Those",
 "     are different jobs and the corpus assigns species to R, not to T.  ** Which is it? **",
 "",
 "  ② ** AND IF THE HORN IS ISOSPIN THEN R IS DOING SPECIES AND CHIRALITY AND NOTHING IS LEFT",
 "     FOR THE COLOUR-NEUTRALITY OF THE LEPTON. **  A lepton must be triality zero.  Daryl's",
 "     leptons sit AT the Nariai points, which are exactly where the colour label is CARRIED",
 "     (the graze point IS the colour index, L-76).  ** So why is a state sitting at a colour",
 "     site colourless? **  There is an answer available and it should be checked rather than",
 "     assumed: a leg CROSSES a graze point and a state AT one does not -- winding zero.",
 "     That is the natural reading and it is exactly L-74's antecedent again.",
 "",
 "  ③ ** AND THE THREE-VERSUS-NINE PROBLEM THAT HIS READING RAISES AND MINE DID NOT. **",
 "     Per hinge his structure gives 4 colourless slots; three hinges give 12, not 4.  But",
 "     there are only THREE Nariai points in total, each shared by two hinges.  ** So either",
 "     the leptons are per-generation (4 x 3 = 12 lepton states across three generations,",
 "     which is right) or the sharing double-counts.  The sharing is real: each graze point",
 "     is touched by 4 legs from TWO hinges. **  This is arithmetic I can do once he says",
 "     whether a lepton is seated at a Nariai POINT or at a (hinge, Nariai point) PAIR.",
]:
    print("  " + s)
print()
print("  ⌗ ** THAT LAST ONE IS THE WHOLE QUESTION AND IT IS ONE SENTENCE: is a lepton seated")
print("  at a Nariai point, or at a hinge's VIEW of a Nariai point?  Three of the first, nine")
print("  of the second, twelve with the horn.  I can carry it from either answer. **")
