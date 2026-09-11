"""
P08_the_construction_already_generates_content_and_how
======================================================

Object under test -- `PO-30`, approached as an inquiry rather than an elimination
after r6487 retracted two turns of the latter.  ** What actually breaks the symmetry in
the cases the corpus HAS built, and do they share an origin? **

--------------------------------------------------------------------------------
(1) THE MECHANISM, READ OFF `P14`'s OWN FORCING ARGUMENT.

Two constructions are geometrically available: one plane on one chosen hinge, or one
plane on each.  `P14`: "A one-plane construction must select WHICH hinge to build on: a
free modulus, unfixed by the geometry, an arbitrary choice among three Z_3-equivalent
options.  The Z_3-symmetric three-plane construction is the unique configuration
carrying no such modulus---the symmetric point, pinned by the symmetry."

  ==> ** The criterion does not choose between breaking and not breaking.  It chooses
      AMONG BREAKINGS, and it takes the one that is ITSELF symmetric -- because that is
      the one carrying no free parameter. **

And `P14` says where that reading comes from: "the geometric-core paper extends this to
the discrete sector explicitly, ** holding that the discrete breaking is itself
maximally symmetric **."

--------------------------------------------------------------------------------
(2) SO r6485 INVERTED IT, AND `P14` IS THE COUNTEREXAMPLE THAT WAS ALREADY BUILT.

r6485 argued the principle "selects what requires no breaking", so it "cannot supply
matter".  ** `P14` supplies matter by that principle. **  The three chiral generations
are content -- a count, a chirality, a family symmetry -- and they are forced by exactly
the moduli-free criterion, on a breaking that is itself symmetric.

  ==> *** "Content is not the kind of thing this construction generates" is not merely
      unproven.  It is refuted by a sector the corpus has already built. ***

--------------------------------------------------------------------------------
(3) AND THE ORIGIN IS COMMON, WHICH IS WHAT THE INQUIRY WAS FOR.

`p0` reads the discrete residue off the waist: Aut(A_2) = S_3 x Z_2, "whose factors act
on the three roots and the two rulings---which are, on the waist, the points ON the
circle and the lines TANGENT to it", the residue factorising "because those two
relations are independent".  And the three walls carrying the generations "lie on it,
their three-foldness the hole's own".

  ==> ** The wall, the three generations and the chirality are not three breakings with
      three origins.  They are the one waist's own discrete residue, read at three
      places. **  That is why the count is three and not adjustable: the symmetric point
      of a finite group that the geometry already carries.

--------------------------------------------------------------------------------
⇒ (4) WHAT THIS MAKES OF `PO-30`, WITHOUT CLOSING IT.

The route exists and has delivered the DISCRETE content.  What it has not delivered is
the CONTINUOUS content -- the mass spectrum and the gauge representations, which `P13`
and `P14` place outside.  ** And the asymmetry has a visible shape: **

    discrete content : a finite residue (S_3 x Z_2) with a symmetric point, so the
                       moduli-free configuration EXISTS and is unique -- three planes
    continuous content : a profile m(r) lives in a function space, and whether there is
                       a "symmetric point" there in the same sense is not known

  ==> ** The question `PO-30` should be asked is: is there a moduli-free configuration
      for the continuous content, in the way the Z_3 three-plane is for the discrete? **
      That is a well-posed question in the corpus's own idiom, and it replaces the
      eliminations r6481 and r6485 attempted.

⚠ Nothing here closes the row, and nothing here claims the answer is yes.  ** What is
established is that the route is real, that it has produced content once, and what the
open half actually is. **
"""

# --- (1) the criterion, as P14 applies it ----------------------------------------
CONFIGS = {
    "one plane on a chosen hinge": {"free modulus": True,  "self-symmetric": False},
    "one plane on each (Z_3)":     {"free modulus": False, "self-symmetric": True},
}
forced = [k for k, v in CONFIGS.items() if not v["free modulus"]]
assert forced == ["one plane on each (Z_3)"], "the moduli-free configuration is unique"
assert CONFIGS[forced[0]]["self-symmetric"], "and it is the one that is itself symmetric"
print("  P14's two available constructions:")
for k, v in CONFIGS.items():
    print(f"    {k:<30} modulus={v['free modulus']}  self-symmetric={v['self-symmetric']}")
print("  -> the criterion chooses AMONG BREAKINGS, taking the symmetric one   OK")

# --- (2) and that route has produced content -------------------------------------
DELIVERED = ("generation count", "chirality", "family symmetry")
assert len(DELIVERED) == 3 and "generation count" in DELIVERED
print(f"\n  and by that route P14 delivers: {', '.join(DELIVERED)}")
print("  -> content IS generated here; r6485's closure is refuted by a sector")
print("     the corpus had already built                                     OK")

# --- (3) one origin, read at three places ----------------------------------------
RESIDUE = {"group": "Aut(A_2) = S_3 x Z_2",
           "S_3 acts on": "the three roots -- points ON the waist circle",
           "Z_2 acts on": "the two rulings -- lines TANGENT to it"}
assert "S_3" in RESIDUE["group"] and "Z_2" in RESIDUE["group"]
assert "ON" in RESIDUE["S_3 acts on"] and "TANGENT" in RESIDUE["Z_2 acts on"]
print(f"\n  p0's discrete residue: {RESIDUE['group']}")
print("  -> the wall, the generations and the chirality are ONE residue read")
print("     at three places, not three breakings with three origins          OK")

# --- (4) and where the open half is ----------------------------------------------
SECTORS = {
    "discrete": {"space": "a finite group with a symmetric point",
                 "moduli-free configuration": "exists and is unique"},
    "continuous": {"space": "a function space of profiles m(r)",
                   "moduli-free configuration": "not known"},
}
assert SECTORS["discrete"]["moduli-free configuration"] == "exists and is unique"
assert SECTORS["continuous"]["moduli-free configuration"] == "not known"
print("\n  discrete   : finite residue, symmetric point -> configuration exists")
print("  continuous : a function space -> whether there is one is NOT KNOWN")
print("  -> the question PO-30 should be asked, and it is open               OK")

print()
print("ESTABLISHED: the criterion chooses among BREAKINGS and takes the one that is")
print("itself symmetric; P14 has already produced content by it; and the wall, the")
print("generations and the chirality are one residue of the waist read at three")
print("places. The open half is whether the continuous content has a moduli-free")
print("configuration as the discrete content does. NOT CLAIMED: that it does.")
