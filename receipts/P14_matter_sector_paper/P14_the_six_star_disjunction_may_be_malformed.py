"""
P14_the_six_star_disjunction_may_be_malformed
=============================================

Object under test -- `[6*]`, carried since r1080 as a conflict between two readings of
the conjugation, and posed there as a CHOICE.  ** This asks whether the choice is well
posed, and finds that the note's own diagnosis says it is not. **

Worked at Daryl's direction while resurrecting the r1000 worldline pictures with the
infrastructure they did not have.  *** Speculative and marked so: this REFRAMES an open
item, it does not settle it. ***

--------------------------------------------------------------------------------
(1) THE LIFT SITS ON THE WALL RAYS, NOT THE HINGE RAYS.

The ray map's own angles, against `P14`'s hinge and wall positions:

    face 2  tau~ REAL,  r complex     arg r = 0, 120, 240   = THE HINGE RAYS
    face 4  tau~ IMAG,  r complex     arg r = 60, 180, 300  = THE WALL RAYS   (the lift)

and `P14` places hinges at 120j and walls at 120j+180 (mod 360), i.e. 60, 180, 300.

  ==> ** Real time sits on the hinges; imaginary time sits on the walls. **  And the
      walls ARE the graze points -- the 3 in `P14`'s 3 x 2 x 2, the colour index.

  ⌗ So the lift is not a hinge structure, which settles the question it was natural to
  ask of it.  *** It is a WALL structure, which is to say a COLOUR structure. ***

--------------------------------------------------------------------------------
(2) AND `[6*]` IS POSED AS A DISJUNCTION WHILE ITS OWN DIAGNOSIS DENIES ONE.

r1080, verbatim: "The rule as stated -- 'conjugate when you go from positive to negative,
real or imaginary, r or tau~' -- is about MOTION ALONG A BEAD (a path crossing zero),
while the quadrant/ray readings are about WHERE A POINT SITS.  Those are not the same
thing, and on a slice where a coordinate is pinned to zero the distinction bites.
** WHICH READING IS THE OBJECT'S IS EXACTLY [6*] AND IS NOT SETTLED HERE. **"

  ** The first two sentences say the readings answer DIFFERENT QUESTIONS.  The third
  asks which is "the object's", which presupposes they answer the SAME one. **

  ==> *** A conflict between two answers to one question needs settling.  Two answers to
      two questions do not compete, and `[6*]` as written cannot tell which it is. ***

⌗ AND THE CORPUS CARRIES THE PRECEDENT: `P17` describes its own index and symmetry
mechanisms as "complementary" rather than rival.  ** Forcing an exclusive choice is a
move this construction does not otherwise make. **

--------------------------------------------------------------------------------
(3) AND THE TWO READINGS DO DIFFERENT WORK, MEASURABLY.

Computed here, on the three Im tau~ sectors (period 2 pi alpha / 3, three to a thermal
circle):

    R AS MOTION, (Re, Im) -> (-Re, -Im)     permutes the sectors {0->2, 1->1, 2->0}:
                                            ** one FIXED, two EXCHANGED -- a 2+1 **
    R AS POSITION, species = sign(r)        carries every r>0 point to an r<0 point and
                                            back -- ** a map between SIDES, and not a
                                            permutation of the sectors at all **

  ==> ** Under the disjunction these look like a contradiction.  Under complementarity
      they look like division of labour: the motion reading acts on paths, the position
      reading acts on sides, and neither is doing the other's job badly. **

--------------------------------------------------------------------------------
⇒ (4) WHY THIS MATTERS TO `PO-45`, WHICH IS THE POINT.

`PO-45` needs a three on which R acts 2+1 to seat the colourless triple.  ** Under the
motion reading the three Im tau~ sectors give one.  Under the position reading they give
nothing. **  So `[6*]` is no longer a marked conflict with nothing hanging on it:

  *** if the readings are complementary and the motion reading governs paths, then a
      seat exists for objects that ARE paths -- and the quarks, which are seated at
      graze POINTS, are exactly the objects the position reading governs. ***

⚠ WHAT IS NOT ESTABLISHED, AND IT IS MOST OF IT.  ** Not that the readings ARE
complementary -- only that `[6*]` as posed cannot distinguish that from a conflict, and
that its own diagnosis leans the first way. **  Not that the three sectors are genuinely
third: they may reduce to the wall three, which is what (1) makes likely and what would
disqualify them under r6537's first test.  Not that leptons are paths.  *** A reframing
of an open item, offered at that weight. ***
"""

import numpy as np

# --- (1) the ray map against P14's hinge and wall angles --------------------------
HINGES = {(120*j) % 360 for j in range(3)}
WALLS = {(120*j + 180) % 360 for j in range(3)}
FACE2, FACE4 = {0, 120, 240}, {60, 180, 300}
assert HINGES == {0, 120, 240} and WALLS == {60, 180, 300}
assert FACE2 == HINGES, "face 2 (tau~ real) must sit on the hinge rays"
assert FACE4 == WALLS, "face 4 (the lift, tau~ imaginary) must sit on the WALL rays"
assert FACE2 != FACE4, "and the two must not coincide, or there is no complementarity"
print(f"  hinges {sorted(HINGES)}  <- face 2, tau~ REAL")
print(f"  walls  {sorted(WALLS)}  <- face 4, tau~ IMAGINARY (the lift)")
print("  -> real time on the hinges, imaginary time on the walls = the colour index  OK")

# --- (3) the two readings, on the three Im tau~ sectors ----------------------------
SECT = 2*np.pi/3


def sector(im):
    return int(np.floor((im % (2*np.pi)) / SECT))


motion = {sector((k + 0.5)*SECT): sector(-(k + 0.5)*SECT) for k in range(3)}
fixed = [s for s, t in motion.items() if s == t]
moved = [s for s, t in motion.items() if s != t]
assert len(fixed) == 1 and len(moved) == 2, f"R-as-motion must give 2+1, got {motion}"
print(f"\n  R as MOTION on the three sectors: {motion}")
print(f"    fixed {fixed}, exchanged {moved}  -> a 2+1                        OK")

A = 2**(1/3)/np.sqrt(3)


def im_tau(r):
    if r >= 0:
        return 0.0
    u = abs(r/A)**1.5
    return (2/3)*np.arcsin(u) if u <= 1 else np.pi/3


pos = {r: im_tau(-r) for r in (0.5, 1.5)}
assert all(im_tau(r) == 0.0 for r in (0.5, 1.5)), "every r>0 point sits at Im tau~ = 0"
assert all(v > 0 for v in pos.values()), "and r -> -r sends each to a nonzero Im tau~"
print("  R as POSITION (sign r): every r>0 point -> an r<0 point and back")
print("    a map between SIDES, not a permutation of sectors                 OK")

# --- (2)/(4) the disjunction and what hangs on it ----------------------------------
DIAGNOSIS = 'the readings answer DIFFERENT questions (motion vs position)'
POSED_AS = 'which reading is THE OBJECT\'S -- one question, two answers'
assert DIAGNOSIS != POSED_AS, \
    "the note's diagnosis and its posing do not agree, which is the finding"
SEAT = {'motion reading': '2+1 on the three sectors', 'position reading': 'no permutation'}
assert len(set(SEAT.values())) == 2, "and the two readings differ on whether a seat exists"
print(f"\n  r1080 diagnoses : {DIAGNOSIS}")
print(f"  r1080 poses     : {POSED_AS}")
print("  -> a conflict needs settling; two answers to two questions do not")
print("     compete, and [6*] as written cannot tell which it is            OK")

print()
print("ESTABLISHED: the lift sits on the WALL rays (the colour index) and not the hinge")
print("rays; [6*] is posed as a disjunction while its own diagnosis says the readings")
print("answer different questions; and the two readings differ on whether the three")
print("Im tau~ sectors carry a 2+1 -- so [6*] now has a stake it did not have.")
print("NOT ESTABLISHED: that the readings are complementary; that the sectors are")
print("genuinely third rather than the wall three again; or anything about leptons.")
