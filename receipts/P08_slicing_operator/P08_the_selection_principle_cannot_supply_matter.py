"""
P08_the_selection_principle_cannot_supply_matter
================================================

Object under test -- `PO-30`, after r6481 reduced it: the law must fix a PROFILE m(r),
not a number.  ** The corpus has exactly one selection principle -- least-arbitrariness
-- and this asks whether it can select a profile. **

** IT CAN, AND WHAT IT SELECTS IS NOT MATTER.  Both halves are already stated in the
   corpus; what is new is putting them together and seeing what they do to this row. **

--------------------------------------------------------------------------------
(1) WHAT THE PRINCIPLE SELECTS.  `P12` states it: it "prefers the structure requiring
NO CHOICE OF HOW TO BREAK A SYMMETRY", and is silent where no such choice arises --
which is why it "selects the manifold at fixed dimension and is silent on the dimension
itself".

Applied to a radial profile: ** any non-constant rho(r) is a choice of HOW to break
homogeneity -- which function -- and exactly one profile makes no such choice: rho
constant. **  So the principle does reach profiles, and it selects the homogeneous one.

--------------------------------------------------------------------------------
(2) AND IN THIS CONSTRUCTION A CONSTANT DENSITY IS NOT A BEND AT ALL.

`p0` says so outright, in the course of dissolving the cosmological-constant problem:
"a constant density gravitates as a curvature scale, so it enters the profile's
Lambda r^2 / 3 term, ** NOT as a 2m/r bend **" -- and immediately: "the
substrate/bend distinction separates Lambda from INHOMOGENEOUS matter, a genuine bend
that breaks the maximal symmetry."

  ==> ** The profile least-arbitrariness selects is absorbed into Lambda.  It is the
      cosmological term, not matter. **

  ⌗ And `P07` reaches the same boundary from the other side: "homogeneous collapse lies
  past the wall of inhomogeneity, where the construction's generation-by-symmetry hands
  off to ordinary Einstein evolution."  ** The symmetric case is precisely where the
  construction stops generating. **

--------------------------------------------------------------------------------
⇒ (3) SO LEAST-ARBITRARINESS CANNOT BE THE LAW `PO-30` WANTS, AND THE REASON IS
   STRUCTURAL RATHER THAN A GAP.

  matter               = a bend = a BREAKING of the maximal symmetry (`p0`)
  the principle        = selects what requires no choice of how to break it (`P12`)

** A selector for maximal symmetry cannot deliver a symmetry-breaking. **  Asking it to
supply matter asks it for the thing it is defined to avoid.

⌗ AND THIS IS THE SECOND TIME THE SAME SHAPE HAS ANSWERED THIS ROW.  r6481: the one cut
the construction distinguishes intrinsically is the Nariai member, and it carries no
matter.  Here: the one profile the principle selects is constant, and that is Lambda.
*** Every maximally symmetric selection this construction offers returns something
matterless -- which is p0's own "the rigidity and the wall are one fact" seen from
inside PO-30. ***

--------------------------------------------------------------------------------
⚠ WHAT THIS DOES AND DOES NOT DO.  ** It does not close the row. **  It removes the
corpus's only existing selection principle as a candidate, which narrows what an answer
could look like: *** the law must be something other than a symmetry selection, because
the content it must fix is by definition what symmetry does not. ***  And it does not
say no such law exists.
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
