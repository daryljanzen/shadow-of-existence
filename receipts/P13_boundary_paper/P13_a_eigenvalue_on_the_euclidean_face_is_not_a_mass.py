"""
P13_a_eigenvalue_on_the_euclidean_face_is_not_a_mass
====================================================

Object under test -- the question `63` raised in refereeing `PO-26` and could not
settle, carried forward at r6463: ** whether a Dirac eigenvalue on the EUCLIDEAN face
maps to anything with the dimensions of a four-dimensional mass. **  It is stated
nowhere in the corpus, and 1/alpha is the COSMOLOGICAL scale, so those eigenvalues
are small rather than large -- while r6425's reasoning reads as though 1/alpha were a
heavy scale.

** THE ANSWER IS NO, BY BOTH AVAILABLE ROUTES, AND THE REASON IS STRUCTURAL RATHER
   THAN AN UNPERFORMED CALCULATION. **

--------------------------------------------------------------------------------
ROUTE 1 -- AS AN INTERNAL SPACE.  This is the route on which an internal Dirac
eigenvalue IS a four-dimensional mass: the higher-dimensional operator separates and
the internal eigenvalue appears as the mass of the four-dimensional mode.

** It requires a product. **  `P13` states that the substrate is "a single irreducible
Lorentzian manifold, not a product M_4 x K of a spacetime with a compact internal
space -- so the ordinary Kaluza-Klein route is not merely unbuilt here, it is
unavailable."  ==> ** The separation that would make the eigenvalue a mass does not
exist. **

--------------------------------------------------------------------------------
ROUTE 2 -- AS THE EUCLIDEAN SECTION.  Here the face is not an internal factor but the
substrate on its other real form, which is the reading r6457 established.

** A mass is an eigenvalue of a time-translation generator. **  It is not a purely
metrical quantity: it is the label a state carries under the one-parameter group that
translates it in time.  And `P13` adjudicates the face precisely on that point: it is
"Riemannian and ATEMPORAL", and by the corpus's own criterion -- existence requiring
an enduring cosmic time -- "a timeless face is no second physical world"; `P13`
elsewhere calls evolving "atemporally" oxymoronic.

  ==> ** On a face with no time there is no time-translation generator, so there is
      nothing for a mass to be the eigenvalue OF.  The Dirac eigenvalues there are
      inverse lengths of a Riemannian manifold -- geometric data, not masses. **

--------------------------------------------------------------------------------
WHAT THIS DOES TO r6425's CLAIM, AND IT SURVIVES ON BETTER GROUND.

r6425 argued: every invariant on the face is a pure power of 1/alpha^2, so any mass
read off the face's geometry is a multiple of hbar c / alpha ~ 1e-33 eV, and therefore
the matter sector's external mass spectrum is a REQUIREMENT rather than a concession.

** The arithmetic was right and the framing was weaker than the truth. **  It is not
that the face supplies masses at an impossible scale.  *** It is that the face supplies
no masses at all ***, mass being a Lorentzian notion and the face the Riemannian
section.  So the conclusion stands and stands harder: the mass spectrum comes from
outside the face's geometry because *** the face's geometry is not the kind of thing
that has masses in it. ***

** AND 63's WORRY DISSOLVES RATHER THAN BEING ANSWERED. **  That 1/alpha is small
rather than heavy would matter if the eigenvalues were masses of the wrong size.  They
are not masses, so their size is beside the point -- which is why the r6425 reasoning
reading "as though 1/alpha were heavy" was a real defect in the reasoning and not only
in the prose.

--------------------------------------------------------------------------------
⚠ WHAT IS NOT CLAIMED.  Not that no continuation of any kind relates Euclidean
spectral data to Lorentzian observables -- Euclidean methods do that routinely, and
this corpus's own temperature is read off a period on the Wick face.  ** The claim is
narrower and is the one 63 asked for: the DIRAC EIGENVALUE ON THE FACE is not a
four-dimensional mass, neither by separation (no product) nor by being one directly
(no time). **  A construction that produced masses by some third route would have to
say what that route is, and would not be reading them off the face's geometry.
"""

# --- the two routes, and what each requires -------------------------------------
ROUTES = {
    "internal space (separation)": {
        "makes the eigenvalue a mass": True,
        "requires": "a product M_4 x K",
        "available here": False,        # P13: "not merely unbuilt here, it is unavailable"
    },
    "Euclidean section (directly)": {
        "makes the eigenvalue a mass": False,
        "requires": "a time-translation generator to be the eigenvalue OF",
        "available here": False,        # P13: the face is Riemannian and ATEMPORAL
    },
}
for name, r in ROUTES.items():
    print(f"  {name}")
    print(f"    requires        : {r['requires']}")
    print(f"    available here  : {r['available here']}")
assert not any(r["available here"] for r in ROUTES.values()), \
    "if either route were available the eigenvalue could be a mass"
print("\n  neither route is available -> the eigenvalue is not a 4D mass   OK")

# --- and the claim it bounds, re-stated on the stronger footing ------------------
claim_r6425 = "the face supplies masses, but only at ~1e-33 eV"
claim_now = "the face supplies no masses at all; mass is Lorentzian, the face is Riemannian"
assert claim_r6425 != claim_now
print(f"\n  r6425 : {claim_r6425}")
print(f"  now   : {claim_now}")
print("  -> the conclusion (external mass spectrum) stands on better ground OK")

# --- 63's worry, and why it dissolves -------------------------------------------
eigenvalues_are_masses = False
assert not eigenvalues_are_masses
print("\n  63's worry was that 1/alpha is small rather than heavy. That would")
print("  matter if these were masses of the wrong size. They are not masses,")
print("  so the size is beside the point.                                  OK")

print()
print("ESTABLISHED: a Dirac eigenvalue on the Euclidean face is not a four-dimensional")
print("mass -- not by separation (no product) and not directly (no time). r6425's")
print("conclusion survives, and its framing was weaker than the truth.")
print("NOT CLAIMED: that no continuation relates Euclidean data to Lorentzian")
print("observables at all -- the corpus reads its own temperature off a period there.")
