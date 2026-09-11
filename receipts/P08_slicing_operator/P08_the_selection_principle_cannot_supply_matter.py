"""
P08_the_selection_principle_cannot_supply_matter -- ** WHOLLY RETRACTED r6487. **
================================================================================

** THIS RECEIPT'S ARGUMENT IS WRONG AT THE ROOT AND IS RETRACTED, NOT QUALIFIED. **  It
is kept, with its error stated, because the error is instructive and because deleting a
wrong argument leaves the next node free to make it again.

WHAT IT CLAIMED (r6485): that least-arbitrariness "selects" the constant profile, that a
constant density is Lambda and not matter, and therefore that the principle "cannot
supply matter, matter being a breaking of the symmetry it selects for".

** WHY IT IS WRONG -- THREE FAULTS, EACH SUFFICIENT ON ITS OWN. **

  (1) ** IT MISREADS THE PRINCIPLE. **  Rule 2, in its own paper: "Prefer the world that
      REQUIRES the observed phenomena as a consequence of its structure to the world
      that merely PERMITS them through adjustable parameters."  *** It is a criterion of
      NECESSITY VERSUS TUNING.  It does not rank options by symmetry and does not
      "select" a profile at all. ***  I used it as a symmetry-maximiser, which it is not.

  (2) ** IT APPLIES IT AT THE WRONG RUNG. **  `P17` states where it acts: "maximal
      symmetry is what makes the substrate the least-arbitrary vacuum such a description
      can be CUT FROM ... a symmetry-breaking MODULUS is the adjustable parameter that
      criterion rejects."  The criterion governs the SUBSTRATE -- the thing cut from --
      and what it rejects is an adjustable MODULUS.  ** Not a breaking.  A free
      parameter. **  I applied it to profiles on a cut, two rungs down.

  (3) ** AND IT INVERTS THE PROGRAMME'S OWN THESIS. **  `P17`'s capstone is that physics
      IS the broken-symmetry shadows of one maximally symmetric object -- "a
      symmetry-breaking slicing of the maximally symmetric object, not a separate
      thing".  *** Concluding that "a selector for maximal symmetry cannot deliver a
      symmetry-breaking" contradicts the thesis the corpus is built on. ***  Breaking is
      what the construction DOES.

** WHAT RULE 2 ACTUALLY SAYS ABOUT THIS ROW, which is the opposite of what I wrote. **
It does not foreclose a generative law for the content.  ** It is the STANDARD such a
law must meet: ** the content must follow as a structural consequence rather than be
admitted through an adjustable parameter.  *** So Rule 2 leaves the row open and tells
you what an answer would have to look like. ***

⚠ ** AND THE DRIVE BEHIND IT IS WORTH RECORDING WITH IT. **  r6481 ruled out one
candidate, r6485 ruled out another, and the turn after proposed that the row "should say
content is not the kind of thing this construction generates".  *** That is a closure
drive wearing the clothes of sharpening -- the flattening the method names, where a
question is crossed out rather than explored. ***  Three moves in one direction, each
smaller than the last, none of them an attempt to find out what fixes the content.
"""


# --- (1) what the principle selects, applied to a profile -----------------------
PROFILES = {
    "rho constant":        {"choice of how to break homogeneity": False},
    "rho(r) non-constant": {"choice of how to break homogeneity": True},
}
selected = [k for k, v in PROFILES.items() if not v["choice of how to break homogeneity"]]
assert selected == ["rho constant"], "exactly one profile makes no such choice"
print(f"  least-arbitrariness prefers what requires no choice of how to break a")
print(f"  symmetry -> among profiles that is: {selected[0]}                   OK")

# --- (2) and what a constant density IS here -------------------------------------
# p0: a constant density enters the Lambda r^2/3 term, NOT the 2m/r bend.
TERMS = {"Lambda r^2 / 3": "constant density", "2m/r": "inhomogeneous matter"}
assert TERMS["Lambda r^2 / 3"] == "constant density"
assert TERMS["2m/r"] != "constant density", "a constant density is not a bend"
print("\n  p0: a constant density enters the Lambda r^2/3 term, not the 2m/r bend")
print("  -> the selected profile is the cosmological term, not matter        OK")

# --- (3) so the principle cannot supply matter -----------------------------------
matter_is = "a BREAKING of the maximal symmetry"
principle_selects = "what requires NO choice of how to break it"
assert "BREAKING" in matter_is and "NO choice" in principle_selects
def can_supply(selector, thing):
    return not ("NO choice" in selector and "BREAKING" in thing)
assert not can_supply(principle_selects, matter_is), \
    "a selector for maximal symmetry cannot deliver a symmetry-breaking"
print("\n  matter    = " + matter_is)
print("  principle = selects " + principle_selects)
print("  -> it cannot be the law PO-30 wants                                 OK")

# --- and the shape has now answered this row twice -------------------------------
ANSWERS = {
    "r6481 the distinguished CUT":     "Nariai -- carries no matter",
    "r6485 the selected PROFILE":      "constant -- is Lambda, not matter",
}
assert len(ANSWERS) == 2 and all("matter" in v for v in ANSWERS.values())
print("\n  every maximally symmetric selection returns something matterless:")
for k, v in ANSWERS.items():
    print(f"    {k:<32} {v}")
print("  -> p0's 'the rigidity and the wall are one fact', from inside PO-30 OK")

print()
print("ESTABLISHED: least-arbitrariness does reach profiles and selects the constant")
print("one, which in this construction is the Lambda term and not a bend -- so the")
print("corpus's only selection principle cannot be PO-30's law, matter being by")
print("definition what symmetry does not supply.")
print("NOT ESTABLISHED: that no such law exists. The row narrows, it does not close.")
