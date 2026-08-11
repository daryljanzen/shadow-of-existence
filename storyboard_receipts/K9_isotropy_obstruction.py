"""K9 — IS THE ISOTROPY=ISOMETRY EQUALITY GENERAL, OR STRATUM-BY-STRATUM?
I hedged this twice (K6 in P8, K7 in P9) and proposed the hedge could be removed by a general
argument: 'a cut's isotropy is by construction the subgroup preserving it, and the geometry read
off it inherits exactly those.'  TEST THAT ARGUMENT HONESTLY, BOTH DIRECTIONS."""
def dso(n): return n*(n-1)//2
print("="*80); print("K9 — TESTING MY OWN PROPOSED GENERAL ARGUMENT"); print("="*80)
print("""
  THE OBJECTS.  Isotropy(c) = { g in SO(5,1) : g.c = c }.  Isom(Psi(c)) = the isometry group of the
  four-geometry read off c.  A cut is a four-geometry in a five-manifold: CODIMENSION ONE.

DIRECTION 1 — Isotropy(c) -> Isom(Psi(c)).  DOES IT HOLD?  YES, and it is injective.
  * Well-defined: g is an ambient isometry with g(c) = c, so g restricted to c preserves the INDUCED
    metric.  So there is a homomorphism.
  * Injective: an element of the kernel fixes c POINTWISE.  At a point of c it fixes four independent
    tangent directions; the only remaining direction is the 1-dimensional normal.  It must fix the
    normal line, and either fixes it (identity) or reverses it -- and a reversal has det = -1, so it
    is not in the connected SO_0(5,1).
    *** SO IN THE CONNECTED GROUP THE POINTWISE STABILISER OF A CODIM-1 CUT IS TRIVIAL: INJECTIVE. ***

DIRECTION 2 — Isom(Psi(c)) -> Isotropy(c).  SURJECTIVITY.  *** AND HERE MY ARGUMENT FAILS. ***
  An abstract isometry of the INDUCED metric on c need not extend to the ambient at all.  By the
  rigidity (Bonnet-type) statement, an isometry of a submanifold extends to an ambient isometry
  precisely when it ALSO PRESERVES THE SECOND FUNDAMENTAL FORM -- the extrinsic curvature.
  *** SO WHAT IS ACTUALLY TRUE IS: ***
        Isotropy(c)  ~=  { phi in Isom(Psi(c)) : phi preserves the second fundamental form } ,
    which is a SUBGROUP of Isom(Psi(c)), and may be PROPER.
  My proposed general argument silently assumed the intrinsic geometry determines the extrinsic one.
  IT DOES NOT.
""")
print("STEP 3 — AND THAT EXPLAINS THE PATTERN P12's TABLE SHOWS, which is the useful part.")
rows=[("Type O (pure de Sitter)", "the cut is TOTALLY GEODESIC -- second fundamental form VANISHES,", "so every isometry preserves it trivially.  EQUALITY FORCED."),
      ("Nariai", "isotropy SO(2,1) x SO(3): the cut's extrinsic curvature is invariant", "under both factors by the product structure.  EQUALITY."),
      ("generic SdS", "R_t x SO(3): staticity and spherical symmetry leave the extrinsic", "curvature invariant.  EQUALITY.")]
for a,b,c in rows:
    print(f"   {a:26s} {b}")
    print(f"   {'':26s} {c}")
print("""
  *** SO THE EQUALITY HOLDS AT EXACTLY THE STRATA WHERE THE SYMMETRY IS LARGE ENOUGH TO FIX THE
      EXTRINSIC CURVATURE TOO -- and P12 tabulates precisely the high-symmetry strata. ***
  AND THE UNTABULATED ONES ARE THE LOW-SYMMETRY ONES: the Type-I classes, the wall.  Those are
  exactly where an isometry of the induced metric is least likely to preserve the second fundamental
  form, so exactly where the equality is least likely to hold.
""")
print("="*80)
print("RESULT K9: my proposed general argument is WRONG, and the hedge I wrote twice was RIGHT --")
print("  for a reason I had not identified.  The hedge does not come out; it gets its reason:")
print("  *** Isotropy(c) is the subgroup of Isom(Psi(c)) preserving the SECOND FUNDAMENTAL FORM, and")
print("      the equality at the tabulated strata holds because those cuts are symmetric enough to")
print("      fix the extrinsic curvature as well as the intrinsic one. ***")
print("  A scoped claim with a stated obstruction is stronger than the same claim scoped by 'we only")
print("  checked these'.")
print("="*80)

print("\n" + "="*80)
print("STEP 4 — AND A TEMPTING IDENTIFICATION THAT IS FALSE, CHECKED BEFORE USE.")
print("="*80)
print("""
  The obstruction is the SECOND FUNDAMENTAL FORM.  The corpus has 'the bend of the cut' x26 and
  'matter is the curvature of the cut'.  It is tempting to say these are the same object and dress
  the result in the corpus's own language.  THEY ARE NOT.
    * THE BEND (P8 prop:bend):  writing f = 1 - 2m(r)/r - Lambda r^2/3, the bend is m'(r) != 0 and
      rho = m'(r)/4 pi r^2 -- THE SLICING CURVE'S DEPARTURE FROM THE CONSTANT-M VACUUM PROFILE.
      A statement about the shape of a CURVE in the construction's own plane.
    * THE SECOND FUNDAMENTAL FORM:  how the FOUR-GEOMETRY sits inside dS_5 -- a statement about the
      embedding of a hypersurface, not about a curve.
  *** DIFFERENT OBJECTS.  The result may NOT be written in the bend's language. ***

  AND THE CHECK TURNS UP SOMETHING ELSE WORTH RECORDING: the corpus carries NO extrinsic-curvature
  vocabulary at all -- 'second fundamental form' x0, 'extrinsic curvature' x0, 'K_{ab}' x0 -- in a
  programme built on CUTS of a substrate.  So K9's obstruction is stated in terms the corpus does
  not carry, and that is part of the finding rather than a defect in it.
""")
print("="*80)

# ** r2376+c54.161 -- DIRECTION 1, ASSERTED (it was argued in prose and never computed). **
#   The claim: in the CONNECTED group the pointwise stabiliser of a CODIMENSION-ONE cut is TRIVIAL,
#   so Isotropy(c) -> Isom(Psi(c)) is injective.  Computed here in the ambient R^{5,1} that carries
#   the substrate hyperboloid: an element fixing the cut pointwise fixes five directions (the four
#   tangent to the cut plus the position vector) and can only send the remaining unit spacelike
#   normal to +/- itself.  Both choices are isometries of eta; their determinants are +1 and -1;
#   so the reversal sits in O(5,1) and NOT in SO_0(5,1), and the kernel is the identity alone.
import numpy as _np
_eta6 = _np.diag([-1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
_dets = {}
for _s in (1.0, -1.0):
    _gm = _np.diag([1.0, 1.0, 1.0, 1.0, 1.0, _s])
    assert _np.allclose(_gm.T @ _eta6 @ _gm, _eta6), _s      # both preserve the ambient metric
    _dets[_s] = float(_np.linalg.det(_gm))
assert abs(_dets[1.0] - 1.0) < 1e-12, _dets                  # the identity: kernel element
assert abs(_dets[-1.0] - (-1.0)) < 1e-12, _dets              # the normal reversal: det = -1
assert _np.allclose(_np.diag([1.0, 1.0, 1.0, 1.0, 1.0, 1.0]), _np.eye(6))
assert _dets[-1.0] < 0.0 < _dets[1.0]                        # only one of the two is in SO_0(5,1)
#   and the dimension bookkeeping the step-3 table leans on, pinned to P12's numbers:
#   so(5,1) is FIFTEEN, SO(4,1) is TEN, SO(2,1) x SO(3) is SIX, R_t x SO(3) is FOUR -- and the
#   codimension of a four-geometry in the five-manifold is ONE, which is what makes the normal
#   line one-dimensional and the argument above go through at all.
assert dso(6) == 15, dso(6)
assert dso(5) == 10 and dso(3) + dso(3) == 6 and 1 + dso(3) == 4
_dim_ambient = len(_np.diag(_eta6))                          # R^{5,1}
_dim_substrate = _dim_ambient - 1                            # the hyperboloid, a level set in it
_codim = _dim_substrate - 4                                  # a four-geometry sits in it
assert _dim_ambient == 6 and _dim_substrate == 5 and _codim == 1, (_dim_ambient, _codim)
assert float(_np.linalg.det(_eta6)) < 0.0                    # Lorentzian ambient, signature (5,1)
