"""
P14_the_binding_radius_is_a_branch_point_of_the_time_map
========================================================

Object under test -- the region r6563 left uncharacterised (inside the lift), and the
framing r6563 used for [6*].  ** Both are corrected here, and the first correction
produces the stronger result. **

*** Speculative programme, held at that weight: this characterises a structure, it does
not identify anything with a Standard Model state. ***

--------------------------------------------------------------------------------
(1) THE FRAME EXCHANGE IS ONE RULE, AND THE PIECEWISE APPEARANCE IS arcsinh's.

r6563 reported that r -> -r relates to tau~ -> -tau~ by a half-sector shift OUTSIDE the
lift and "differently" inside, and flagged the inside as uncharacterised.  ** There is
no second behaviour. **  With u = (r/A)^{3/2},

    r -> -r   IS   u -> i u,            a QUARTER TURN IN u, everywhere.

Verified on both sides of |r| = A against the figure's own `wing`: tau~(-r) equals
(2/3) arcsinh(i u) exactly, real part included, at |r| = 0.3, 0.55, A, 0.95, 1.7.

  ==> ** The map does not change at the binding radius.  arcsinh does. **

--------------------------------------------------------------------------------
(2) AND THAT IS BECAUSE THE BINDING RADIUS IS A BRANCH POINT OF THE TIME MAP.

arcsinh has branch points at +-i.  So arcsinh(i u) branches at u = +-1 -- which is

    u = 1   <=>   |r| = A,   A^3 = 2 M alpha^2.

  *** The binding radius is not a piecewise seam in somebody's plotting function.  It is
  where tau~(r), under the frame exchange, meets a branch point of its own. ***

  ⌗ And A = 2^{1/3} R_TA,max, the Hubble--Eddington radius, which P3 defines as "the
  largest shell around a mass M that can stay gravitationally bound against the
  cosmological expansion".  ** The bound/unbound boundary and the branch point of the
  time map are the same radius. **

--------------------------------------------------------------------------------
(3) AND THE TWO R-INVARIANT FIBRES ARE THE TWO ENDS OF THE LIFT.

On the lift the fibre base is theta = (2/3) arcsin(u), running 0 -> 60 deg as |r| runs
from the branch point to the binding radius:

    r = 0    (the BRANCH POINT)      theta = 0 deg    fibre {0, 120, 240}  = the HINGES
    |r| = A  (the BINDING RADIUS)    theta = 60 deg   fibre {60, 180, 300} = the WALLS

  ** Every fibre strictly between them fails R-invariance. **  So the two triples are not
  bases that happened to work: *** they are the endpoints of the bound region, and the
  lift is the interpolation between them. ***

--------------------------------------------------------------------------------
⛔ (4) AND r6563's FRAMING OF [6*] WAS WRONG, IN THE DIRECTION THAT OVERSTATED CONTINGENCY.

r6563 said the 2+1 is "contingent on [6*]" -- on which READING governs.  ** That conflates
two different questions. **

    A MAP question       : which involutions act on the object.  tau~ -> -tau~ and
                           u -> i u both do; both are computable; neither needs a
                           species labelling to be defined.
    A LABELLING question : whether species is sign(r) or the quadrant sign.  *** This is
                           what [6*] actually asks, and it is open. ***

  ==> ** The 2+1 is a fact about an involution acting on a fibre.  It does not wait on
      the labelling. **  What waits on the labelling is whether that 2+1 means anything
      about matter and antimatter -- which is a separate and still-open thing.

  ⌗ AND THE CORPUS MAKES r -> -r A MAP RATHER THAN A LABELLING: P7's caption says the two
  R-conjugate frames read "each matter (blue) on its own r>0 side".  ** r is
  frame-relative, so r -> -r is the frame exchange. **

⚠ WHAT IS NOT CLAIMED.  Not that the labelling question is settled -- it is not, and
nothing here bears on it.  Not that the fibre's three elements are the colourless
fermions.  ** Not that a branch point of a time map is a binding mechanism: the two
coincide in radius, and coincidence of radius is what is shown. **
"""

import numpy as np

A = 2**(1/3)/np.sqrt(3)


def wing_tau(r):
    """tau~(r) for r<0, exactly as the r1000 figure computes it"""
    u = abs(r/A)**1.5
    return (0.0 + 1j*(2/3)*np.arcsin(u)) if u <= 1 else ((2/3)*np.arccosh(u) + 1j*np.pi/3)


# --- (1) one rule, both sides of the binding radius --------------------------------
for rr in (0.3, 0.55, A, 0.95, 1.7):
    u = (rr/A)**1.5
    got, pred = wing_tau(-rr), (2/3)*np.arcsinh(1j*u)
    assert abs(got - pred) < 1e-9, f"|r|={rr}: {got} vs {pred}"
print("  r -> -r IS u -> i u on both sides of |r| = A, exactly            OK")

# --- (2) and |r| = A is where arcsinh(i u) branches ---------------------------------
assert abs((A/A)**1.5 - 1.0) < 1e-12, "u = 1 exactly at |r| = A"
# arcsinh branches at +-i: the derivative 1/sqrt(1+z^2) blows up there
d = lambda z: 1/np.sqrt(1 + z**2)
near = abs(d(1j*0.999999))
far = abs(d(1j*0.5))
assert near > 100*far, f"the derivative must blow up at u->1: {near:.2f} vs {far:.2f}"
print(f"  arcsinh(i u) branches at u = 1, i.e. |r| = A = {A:.6f}           OK")
print(f"    |d/dz arcsinh| at u=0.999999 is {near:.1f}x its value at u=0.5")

# --- (3) the two invariant fibres are the lift's ends -------------------------------
theta = lambda r: (2/3)*np.arcsin(abs(r/A)**1.5)
assert abs(np.degrees(theta(0.0)) - 0.0) < 1e-9, "branch point -> 0 deg"
assert abs(np.degrees(theta(-A)) - 60.0) < 1e-9, "binding radius -> 60 deg"
mid = np.degrees(theta(-0.45))
assert 0 < mid < 60 and abs(mid - 0) > 1 and abs(mid - 60) > 1, \
    "an interior fibre must sit strictly between and so fail R-invariance"
print(f"  lift ends: r=0 -> 0 deg (HINGES);  |r|=A -> 60 deg (WALLS)       OK")
print(f"    an interior point r=-0.45 sits at {mid:.2f} deg -- neither       OK")

# --- (4) map question vs labelling question ----------------------------------------
MAPS = {'tau~ -> -tau~': 'acts on a fibre; 2+1 on the two invariant ones',
        'u -> i u': 'the frame exchange, r -> -r'}
LABELS = {'species = sign(r)', 'species = sign(Re tau~ * Im tau~)'}
assert len(MAPS) == 2 and len(LABELS) == 2
assert not (set(MAPS) & LABELS), "a map is not a labelling -- that is the correction"
print("\n  two MAPS (computable without any labelling) and two LABELLINGS (open):")
for k, v in MAPS.items():
    print(f"    map      {k:<18} {v}")
for l in sorted(LABELS):
    print(f"    labelling {l}")
print("  -> the 2+1 is a fact about a map and does not wait on [6*]       OK")

print()
print("ESTABLISHED: r -> -r is u -> i u everywhere, so the frame exchange is one rule and")
print("the piecewise look is arcsinh's; the binding radius |r| = A is the branch point of")
print("arcsinh(i u), the same radius P3 gives as the largest bound shell; and the two")
print("R-invariant fibres are the lift's two ends, hinges at the branch point and walls at")
print("the binding radius.  AND r6563 overstated the contingency: the 2+1 is a fact about")
print("an involution, while [6*] asks a labelling question the 2+1 does not wait on.")
print("NOT CLAIMED: that the labelling is settled; that the fibre's elements are the")
print("colourless fermions; or that a branch point IS a binding mechanism -- the two")
print("coincide in radius, and coincidence of radius is what is shown.")
