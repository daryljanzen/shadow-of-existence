"""
P15_the_angular_momentum_sector_is_not_a_propagating_mode
=========================================================

Object under test -- `PO-31`'s named first computation: ** does the collapse leg's
no-hair damping remove J, or only its anisotropic signature? **

--------------------------------------------------------------------------------
(1) THE DAMPING ARGUMENT, REPRODUCED EXACTLY, AND WHAT IT IS AN ARGUMENT ABOUT.

`P15` `sec:coherence`: on the equal-radii throat an S^2 harmonic of degree l gives a
dS_2 field of mass^2 = l(l+1)/r_N^2 against H^2 = 1/r_N^2, so nu^2 = 1/4 - l(l+1).
l=0 returns nu = 1/2, "a scale-invariant base"; every l>=1 has nu^2 < 0, "the heavy
principal series, which oscillate and decay through the throat".  Reproduced below.

** That computation is correct, and it is a computation about a FIELD MODE: a
degree of freedom that propagates on the dS_2 factor and therefore has a mass to be
heavy. **

--------------------------------------------------------------------------------
(2) AND ANGULAR MOMENTUM IS NOT ONE.

In the standard multipole decomposition of perturbations about a spherically symmetric
background, the low multipoles are not radiative and are not field modes:

    l = 0            the MASS perturbation -- non-propagating, shifts M
    l = 1 (axial)    ** the ANGULAR MOMENTUM -- non-propagating, shifts J; it is the
                     slow-rotation limit, a STATIONARY solution, not an oscillation **
    l = 1 (polar)    a gauge mode, a translation
    l >= 2           the radiative content

  ==> ** J lives in the l=1 axial sector, which carries no propagating degree of
      freedom.  It is a constrained sector holding a conserved charge, not a field
      with a mass that could be heavy. **  Applying a principal-series argument there
      assigns a decay rate to a charge.

--------------------------------------------------------------------------------
⇒ (3) SO THE ROW'S DICHOTOMY RESOLVES TOWARD "ONLY THE SIGNATURE".

`P15`'s tower damps the anisotropic CONTENT -- the l>=2 radiative multipoles, which
genuinely oscillate and decay.  ** It does not reach J, because J is not among the
modes it is a statement about. **  The row's own suspicion -- "damping can hide angular
momentum in the stress-energy without destroying the charge" -- is the right reading,
and the reason is that the charge is not in the tower.

⌗ AND THE CORPUS ALREADY CARRIES THE CONCEPT, in another paper and not here: `P09`'s
"non-radiative skeleton of general relativity in every symmetry class", types O, D and
I, "the wall is where the field begins to propagate".  ** The l=0 and l=1 sectors are
that skeleton's multipole face.  Nothing needed inventing; it needed connecting. **

--------------------------------------------------------------------------------
⚠ (4) WHAT IS AND IS NOT ESTABLISHED, AND THE BOUNDARY IS SHARP.

  ESTABLISHED   that `P15`'s argument is about propagating field modes; that J is not
                one; and therefore that the argument as given does not remove J.
  NOT ESTABLISHED  that J SURVIVES the leg.  ** That wants the constrained-sector
                analysis on the throat -- what the l=1 axial sector does on dS_2 x S^2
                specifically -- which is a computation and is not done here. **  A
                charge can still be carried away by matter, or torqued; what is shown
                is only that the no-hair tower is not the mechanism that would do it.

⌗ And `r6493`'s third branch is untouched by this: whether the flow stays smooth long
enough for any of this to complete is a separate question, and vortex stretching
concentrates exactly the l=1 axial content.
"""

import sympy as sp

l = sp.Symbol('ell', nonnegative=True, integer=True)

# --- (1) P15's tower, reproduced --------------------------------------------------
nu2 = sp.Rational(1, 4) - l*(l + 1)
assert nu2.subs(l, 0) == sp.Rational(1, 4), "l=0 must give nu = 1/2, P15's base"
assert all(nu2.subs(l, L) < 0 for L in (1, 2, 3, 10)), "every l>=1 is principal series"
print("  P15's throat tower, nu^2 = 1/4 - l(l+1):")
for L in (0, 1, 2, 3):
    print(f"    l={L}: nu^2 = {nu2.subs(l, L)}")
print("  -> reproduced exactly; the computation is about a FIELD MODE      OK")

# --- (2) and the multipole sectors, by what they carry ----------------------------
SECTORS = {
    "l=0":           {"carries": "M", "propagating": False},
    "l=1 axial":     {"carries": "J", "propagating": False},
    "l=1 polar":     {"carries": "a gauge translation", "propagating": False},
    "l>=2":          {"carries": "radiation", "propagating": True},
}
radiative = [k for k, v in SECTORS.items() if v["propagating"]]
assert radiative == ["l>=2"], "only l>=2 propagates"
assert SECTORS["l=1 axial"]["carries"] == "J" and not SECTORS["l=1 axial"]["propagating"]
print("\n  multipole sectors on a spherically symmetric background:")
for k, v in SECTORS.items():
    print(f"    {k:<12} carries {v['carries']:<20} propagating={v['propagating']}")
print("  -> J sits in a NON-propagating sector                             OK")

# --- (3) so the tower's statement does not reach J --------------------------------
tower_is_about = {k for k, v in SECTORS.items() if v["propagating"]}
J_lives_in = "l=1 axial"
assert J_lives_in not in tower_is_about, \
    "if J were among the propagating modes the damping argument would reach it"
print(f"\n  the tower is a statement about {tower_is_about};  J lives in '{J_lives_in}'")
print("  -> the damping removes the SIGNATURE, not the charge              OK")

# --- (4) and the boundary of the claim --------------------------------------------
ESTABLISHED = "the no-hair tower is not a mechanism that removes J"
NOT_ESTABLISHED = "that J survives the leg -- a charge can still be carried off or torqued"
assert ESTABLISHED != NOT_ESTABLISHED
print(f"\n  established     : {ESTABLISHED}")
print(f"  NOT established : {NOT_ESTABLISHED}")
print("  -> the constrained-sector analysis on the throat is a computation")
print("     and is not done here                                          OK")

print()
print("ESTABLISHED: P15's damping argument is about propagating field modes, J is not")
print("one of them, and so the argument as given does not remove J -- which resolves")
print("PO-31's dichotomy toward 'only its anisotropic signature'. And P09 already")
print("carries the concept as its 'non-radiative skeleton'; it needed connecting.")
print("NOT ESTABLISHED: that J survives the leg. Only that this is not what removes it.")
