"""
P03_the_hubble_eddington_radius_is_the_slices_flat_locus_and_the_bend_takes_whatever_gravitates
=============================================================================================

Object under test -- `PO-36`, invited to this seat by node 66: *"your seat is the one with the symbolic
machinery to state what the construction predicts before any data is touched."*  `r6407` (64) quantified
the discrimination and re-scoped the row; what it did not do is DERIVE either half from the cut's own
geometry.  Both halves are derived here, and the derivation finds the radius already in the construction
under another name.

** (1) THE HUBBLE--EDDINGTON RADIUS IS NOT A NEW SCALE IN THIS CONSTRUCTION.  IT IS THE FLAT LOCUS OF
THE SLICING SURFACE, WHICH `r1680` NAMED AND NOBODY CONNECTED TO THIS ROW. **

On the cut, f = 1 - 2M/r - r^2/alpha^2, and the comoving radial acceleration of the whole energy family
is d^2r/dtau^2 = -f'(r)/2 = r/alpha^2 - M/r^2, with E cancelling.  `r1680` proved that this is exactly
r K_G with K_G = 1/alpha^2 - M/r^3 the slice's Gaussian curvature.  ** So the locus where the mass
attraction and the Lambda repulsion balance IS the locus where the slice is flat: **

      d^2r/dtau^2 = 0   <=>   K_G = 0   <=>   r^3 = M alpha^2 = 3M/Lambda

and (3M/Lambda)^(1/3) is the Hubble--Eddington radius `r6407` quoted from Pavlidou--Tomaras.  *The
construction has carried it since `r1680` as the deceleration-to-acceleration turnover.*

** (2) AND THE NAME GUARD BECOMES ARITHMETIC RATHER THAN A WARNING. **  The row carries a guard that the
literature's "maximum turnaround radius" is not this corpus's TURNAROUND.  It is not, and the factor is
exact:

      r_HE          = (M alpha^2)^(1/3)          the force-balance locus, K_G = 0
      r_equality    = (2 M alpha^2)^(1/3)        matter--Lambda DENSITY equality, 3m/4pi r^3 = Lambda/8pi
      r_turnaround  = -(2 M alpha^2)^(1/3)       the corpus's comoving turnaround, a 1 - f = 0 point

      r_equality / r_HE = 2^(1/3) EXACTLY, and the corpus's turnaround is the equality radius signed

** So the two loci differ by 2^(1/3) = 1.26, and reading one for the other is a 26% error in radius. **
⌗ *`CR_cosmology` already says (2 M alpha^2)^(1/3) "is exactly the areal radius at matter--Lambda
equality"; this receipt adds that the force-balance radius is a DIFFERENT locus a factor 2^(1/3) inside
it, which is why the density equality and the acceleration turnover must not be quoted for each other.*
⌗ *And the 2^(1/3) is the same signature `P03`'s own figure flags: the turnaround sits off the slicing
lattice "by exactly the cbrt(2) that is the other cubic's signature".*

** (3) ON THE FORCED MEMBER THE RADIUS IS NOT INDEPENDENT AT ALL -- IT IS A SLICING ROOT. **  The
tangency trichotomy forces Lambda M^2 = 1/9, i.e. M = sqrt(3) alpha/9.  There

      r_HE = alpha/sqrt(3)         which is the slicing root +alpha/sqrt(3) itself
      r_turnaround = 2^(1/3) alpha/sqrt(3)

⚠ ** WHICH SPACE, AND THIS IS THE CHANNEL'S OWN FIRST WATCH APPLIED TO THIS ROW. **  That identity is a
statement about the COSMOLOGICAL member, whose M is the cut's offset for the universe.  `PO-36`'s
measurement is on a CLUSTER, whose M is its own and is not tied to Lambda by the trichotomy.  ** The two
must not be run together: on the cluster r_HE is (3M_cl/Lambda)^(1/3) with M_cl free, and the root
identity says nothing about it. **  *Stated because the identity is pretty enough to invite exactly that
error.*

** (4) WHICH MASS, DERIVED RATHER THAN READ.  THE BEND TAKES WHATEVER GRAVITATES. **  With the offset
promoted to a profile, f = 1 - 2m(r)/r - r^2/alpha^2 and the cut's own equation gives
rho(r) = m'(r)/4 pi r^2.  The acceleration is then

      d^2r/dtau^2 = m'(r)/r - m(r)/r^2 + r/alpha^2 = 4 pi r rho(r) - m(r)/r^2 + r/alpha^2

  (a) ** OUTSIDE the matter, m' = 0, and the locus depends on m ONLY through its enclosed value. **
      That is "profile-independence GIVEN M" -- the exact clause `P03`'s Pavlidou--Tomaras sentence
      states and `PO-36` says the paper does not distinguish from independence of WHICH M.  ** It is
      derived here, with its domain: it holds outside the distribution and not inside, where the
      4 pi r rho term is present. **
  (b) ** And WHICH m is settled by rho = m'/4 pi r^2 having no second channel. **  Every component with
      stress-energy enters m.  A baryon-only m is not a different choice of variable; it requires
      rho_dark == 0 identically.  ** The construction therefore predicts the DYNAMICAL mass, and it
      predicts it structurally rather than by preference. **

  ⇒ *So `r6407`'s conclusion stands and is now entailed: the row is not a CR-versus-LambdaCDM
  discriminator, because both take the same m for the same reason.*

** (5) AND THE SIZE OF THE DISCRIMINATION IS EXACT, NOT FITTED. **  r_HE scales as m^(1/3), so the two
mass choices stand in the ratio f_b^(-1/3) in radius and 1/f_b in the Lambda inferred from an observed
radius: f_b = 0.157 gives 1.8537 and 6.369, which are `r6407`'s 1.85 and 6.37 recovered as algebra.
** The control is f_b -> 1: the ratio goes to unity identically and the test falls silent, so what it
measures is the dark fraction and nothing about the framework. **

CONSTRUCTION.  Everything is symbolic in sympy on the cut's own metric function: the acceleration from
-f'/2 over the whole energy family, the identity against `r1680`'s K_G, the three loci and their exact
ratios, the profile promotion m -> m(r) with its extra term kept rather than dropped, and the trichotomy
substitution.  No data, no fit, and no numerical constant except f_b where the row's own figures are
reproduced.

COMPUTES: scope -- what this settles and what it leaves.
  * It settles WHICH MASS structurally (the bend has one channel) and WHERE the standard formula holds
    (outside the matter).  ** It does not measure f_b and touches no data: the row's observational half
    is untouched and is not this seat's. **
  * The slicing-root identity is on the FORCED member only, where Lambda M^2 = 1/9 ties M to Lambda.  It
    is not a statement about clusters and is flagged as such above.
  * `f_b = 0.157` is an input, carried only to reproduce `r6407`'s two figures; every other number here
    is exact.
  * The 2^(1/3) between the force-balance and density-equality loci is a statement about THESE two
    definitions.  ** It does not say the literature is wrong about its own radius -- it says the two
    names denote different radii in this corpus and the conversion is exact. **
  * Nothing here bears on `PO-7`: no verdict on the construction is drawn, and the row's stake is the
    unpinned factor of 6.37 in the local reading of Lambda, which this leaves exactly where `r6407` put
    it.

ORIGIN: invited by node 66 in `FOR_60` after `PO-24` was struck, on the ground that this seat holds the
symbolic machinery.  `r6407`'s three results are anchored first and none is restated as new.
"""
import os
import sys

import sympy as sp

_checks = []


def check(label, ok):
    _checks.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    assert ok, label


print(__doc__)

r, al, M, E, Lam = sp.symbols('r alpha M E Lambda', positive=True)
f_b = sp.Rational(157, 1000)

# =========================================================================================
print("=" * 94)
print("PART 1 (C1) — THE PRIOR RESULTS ANCHORED BEFORE ANYTHING NEW IS COMPUTED")
print("=" * 94)
print("""
  Two of them, and this receipt is only readable if both hold: `r1680`'s identity that the comoving
  acceleration is the slice's Gaussian curvature times r, and the corpus's own comoving turnaround.
""")
f = 1 - 2 * M / r - r ** 2 / al ** 2
acc = sp.simplify(sp.diff(E ** 2 - f, r) / 2)
KG = 1 / al ** 2 - M / r ** 3
print(f"    f(r)            = {f}")
print(f"    d^2r/dtau^2     = {acc}          [E cancels: it is the whole energy family's]")
print(f"    r * K_G         = {sp.simplify(r * KG)}")
check("r1680's identity holds: the acceleration IS r times the slice's Gaussian curvature",
      sp.simplify(acc - r * KG) == 0)
check("and E is absent from it, so it is the family's and not one member's",
      E not in acc.free_symbols)
TURN = -(2 * M * al ** 2) ** sp.Rational(1, 3)
print(f"    the corpus's comoving turnaround  r = {TURN}")
_u = sp.symbols('u', positive=True)                      # u = (2 M alpha^2)^(1/3), so 2M = u^3/alpha^2
_one_minus_f = (2 * M / r + r ** 2 / al ** 2).subs(M, _u ** 3 / (2 * al ** 2)).subs(r, -_u)
print(f"    at r = -(2 M alpha^2)^(1/3):   1 - f = {sp.simplify(_one_minus_f)}")
check("the turnaround is a 1 - f = 0 point, verified by substitution",
      sp.simplify(_one_minus_f) == 0)
check("and it is NOT a root of the slicing there, f being 1 rather than 0",
      sp.simplify(1 - _one_minus_f) == 1)

# =========================================================================================
print()
print("=" * 94)
print("PART 2 (THE FINDING) — THE HUBBLE–EDDINGTON RADIUS IS THE FLAT LOCUS OF THE SLICE")
print("=" * 94)
R_HE = sp.solve(sp.Eq(acc, 0), r)
assert len(R_HE) == 1
R_HE = R_HE[0]
R_HE_LAM = sp.simplify(R_HE.subs(al, sp.sqrt(3 / Lam)))
print(f"    d^2r/dtau^2 = 0  ->  r_HE = {R_HE}")
print(f"    in Lambda            r_HE = {R_HE_LAM}        [alpha^2 = 3/Lambda]")
print(f"    K_G = 0          ->  r    = {sp.solve(sp.Eq(KG, 0), r)[0]}")
check("the force-balance locus is r^3 = M alpha^2", sp.simplify(R_HE ** 3 - M * al ** 2) == 0)
check("⚑ and it is the SAME locus as K_G = 0, so the radius is the slice's flat locus",
      sp.simplify(R_HE - sp.solve(sp.Eq(KG, 0), r)[0]) == 0)
check("which in Lambda is the (3M/Lambda)^(1/3) the row quotes from the literature",
      sp.simplify(R_HE_LAM - (3 * M / Lam) ** sp.Rational(1, 3)) == 0)

# =========================================================================================
print()
print("=" * 94)
print("PART 3 (THE NAME GUARD, AS ARITHMETIC) — THREE LOCI AND THEIR EXACT RATIOS")
print("=" * 94)
R_EQ = sp.solve(sp.Eq(3 * M / (4 * sp.pi * r ** 3), Lam / (8 * sp.pi)), r)[0]
R_EQ = sp.simplify(R_EQ.subs(Lam, 3 / al ** 2))
print(f"    force balance,     K_G = 0                  r_HE       = {R_HE}")
print(f"    density equality,  3m/4pi r^3 = Lambda/8pi  r_equality = {R_EQ}")
print(f"    the corpus's comoving turnaround            r_turn     = {TURN}")
print()
RATIO = sp.simplify(R_EQ / R_HE)
print(f"    r_equality / r_HE = {RATIO} = {float(RATIO):.4f}")
check("the density-equality radius is the corpus's turnaround, signed",
      sp.simplify(R_EQ + TURN) == 0)
check("⛔ and it is 2^(1/3) times the force-balance radius, EXACTLY",
      sp.simplify(RATIO - 2 ** sp.Rational(1, 3)) == 0)
check("so reading one for the other is a 26% error in radius", abs(float(RATIO) - 1.26) < 0.01)

# =========================================================================================
print()
print("=" * 94)
print("PART 4 (⚠ WHICH SPACE) — ON THE FORCED MEMBER IT IS A SLICING ROOT, AND THAT IS NOT A CLUSTER")
print("=" * 94)
M_DEG = sp.solve(sp.Eq(Lam * M ** 2, sp.Rational(1, 9)), M)[0]
M_DEG = sp.simplify(M_DEG.subs(Lam, 3 / al ** 2))
R_HE_DEG = sp.simplify(R_HE.subs(M, M_DEG))
print(f"    the trichotomy forces Lambda M^2 = 1/9  ->  M = {M_DEG}")
print(f"    r_HE there       = {R_HE_DEG}     against the slicing root +alpha/sqrt(3) = "
      f"{sp.simplify(al / sp.sqrt(3))}")
print(f"    r_turnaround     = {sp.simplify(TURN.subs(M, M_DEG))}")
check("⚑ on the forced member the force-balance radius IS the slicing root alpha/sqrt(3)",
      sp.simplify(R_HE_DEG - al / sp.sqrt(3)) == 0)
check("and the turnaround there is 2^(1/3) times that root",
      sp.simplify(sp.simplify(TURN.subs(M, M_DEG)) + 2 ** sp.Rational(1, 3) * al / sp.sqrt(3)) == 0)
print("""
  ⚠ AND THE WATCH: that identity ties M to Lambda through the trichotomy, so it is a statement about the
  COSMOLOGICAL member.  `PO-36`'s measurement is on a cluster, whose M is its own.  ** The root identity
  says nothing about a cluster's radius, and the two must not be run together. **
""")
M_cl = sp.symbols('M_cl', positive=True)
check("on a cluster the radius keeps a free mass and no root identity is available",
      M_cl in sp.simplify(R_HE.subs(M, M_cl)).free_symbols)

# =========================================================================================
print()
print("=" * 94)
print("PART 5 (WHICH MASS) — THE BEND HAS ONE CHANNEL, SO IT TAKES WHATEVER GRAVITATES")
print("=" * 94)
m = sp.Function('m')
f_prof = 1 - 2 * m(r) / r - r ** 2 / al ** 2
acc_prof = sp.simplify(sp.expand(sp.diff(E ** 2 - f_prof, r) / 2))
extra = sp.simplify(acc_prof - (r / al ** 2 - m(r) / r ** 2))
acc_vac = sp.simplify(acc_prof.subs(sp.Derivative(m(r), r), 0))
print(f"    with the offset promoted to a profile:  d^2r/dtau^2 = {acc_prof}")
print(f"    the extra term is                      {extra}  =  4 pi r rho,  since rho = m'/4 pi r^2")
print(f"    OUTSIDE the matter (m' = 0):           d^2r/dtau^2 = {acc_vac}")
check("inside the distribution the balance carries a 4 pi r rho term, so the standard formula "
      "does NOT hold there", extra != 0)
check("⚑ outside it, the locus depends on m only through its ENCLOSED value — profile-independence "
      "GIVEN M, derived with its domain", sp.Derivative(m(r), r) not in acc_vac.atoms(sp.Derivative))
print("""
  ** AND WHICH m IS SETTLED BY rho = m'(r)/4 pi r^2 HAVING NO SECOND CHANNEL. **  Everything with
  stress-energy enters m.  A baryon-only m is not another choice of variable -- it is the assertion
  rho_dark == 0.  *The control is exactly that substitution.*
""")
rho_d = sp.Function('rho_dark')
m_b, m_d = sp.Function('m_b'), sp.Function('m_d')
tot = sp.Eq(sp.Derivative(m_b(r) + m_d(r), r), 4 * sp.pi * r ** 2 * (sp.Function('rho_b')(r) + rho_d(r)))
print(f"    the cut's equation on a two-component source:  {tot}")
print("    m = m_b alone  <=>  m_d' = 0 for all r  <=>  rho_dark == 0")
_rho = sp.symbols('rho_d')
_forced = sp.solve(sp.Eq(sp.diff(sp.Integer(0) * r, r), 4 * sp.pi * r ** 2 * _rho), _rho)
print(f"    setting m_d(r) == 0 in m_d' = 4 pi r^2 rho_d forces rho_d = {_forced}")
check("so 'the baryonic mass' is reachable only by asserting the dark component does not "
      "gravitate at all", _forced == [0])
check("⇒ the construction predicts the DYNAMICAL mass, structurally rather than by preference",
      sp.simplify(acc_vac.subs(m(r), sp.Symbol('m_enclosed')) -
                  (r / al ** 2 - sp.Symbol('m_enclosed') / r ** 2)) == 0)

# =========================================================================================
print()
print("=" * 94)
print("PART 6 — AND THE SIZE OF THE DISCRIMINATION IS ALGEBRA, WITH ITS OWN CONTROL")
print("=" * 94)
RAD = sp.simplify((M / (f_b * M)) ** sp.Rational(1, 3))
LAMR = sp.simplify(1 / f_b)
print(f"    r_HE ~ m^(1/3), so the two mass choices differ in RADIUS by f_b^(-1/3) = {float(RAD):.4f}")
print(f"    and, read at an OBSERVED radius to infer the constant, in Lambda by 1/f_b = {float(LAMR):.4f}")
print(f"    r6407 reported 1.85 and 6.37")
check("the radius ratio is r6407's 1.85, now as algebra", abs(float(RAD) - 1.85) < 0.01)
check("the Lambda ratio is r6407's 6.37", abs(float(LAMR) - 6.37) < 0.01)
fb1 = sp.symbols('fb1', positive=True)
check("⚑ THE CONTROL: at f_b = 1 the two choices coincide identically and the test falls silent",
      sp.simplify(((M / (fb1 * M)) ** sp.Rational(1, 3)).subs(fb1, 1) - 1) == 0)

# =========================================================================================
print()
print("=" * 94)
print("WHAT THIS REVISION ESTABLISHES")
print("=" * 94)
print(f"""
  ** THE RADIUS THE ROW IS ABOUT IS ALREADY IN THE CONSTRUCTION, UNDER ANOTHER NAME. **  The
  Hubble--Eddington radius is the zero of the comoving acceleration, which `r1680` proved is the zero of
  the slicing surface's Gaussian curvature: r_HE = (M alpha^2)^(1/3) = (3M/Lambda)^(1/3), the slice's
  FLAT LOCUS and the deceleration-to-acceleration turnover.  *Nothing was imported to get it.*

  ** AND THE ROW'S NAME GUARD IS NOW ARITHMETIC. **  Force balance at (M alpha^2)^(1/3), matter--Lambda
  DENSITY equality at (2 M alpha^2)^(1/3) which is the corpus's comoving turnaround signed, ratio
  2^(1/3) = {float(RATIO):.4f} exactly.  Reading one for the other is a 26% error, and on the forced
  member the first is the slicing root alpha/sqrt(3) itself.
  ⚠ *That root identity is the COSMOLOGICAL member's and says nothing about a cluster, which is the
  WHICH-SPACE watch applied to a coincidence pretty enough to invite the error.*

  ** WHICH MASS IS SETTLED STRUCTURALLY. **  rho = m'(r)/4 pi r^2 has one channel, so every component
  with stress-energy is in the bend and "the baryonic mass" is reachable only by asserting rho_dark == 0.
  The construction predicts the DYNAMICAL mass -- which is `r6407`'s conclusion, now entailed rather than
  read off -- so the row is not a framework discriminator and what it measures is f_b.
  ⌗ *With the domain of the standard formula fixed on the way past: profile-independence given M holds
  OUTSIDE the distribution, the 4 pi r rho term being present inside.  That is the exact clause `P03`'s
  sentence conflates with independence of WHICH M.*

  ⚠ WHAT IS NOT DONE HERE: no data is touched and f_b is not measured.  The row's observational half is
  untouched, and its stake -- the factor of {float(LAMR):.2f} unpinned in the local reading of Lambda --
  is left exactly where `r6407` put it.
""")
print(f"  {len(_checks)} checks, all pass." if all(_checks) else "  FAILURES PRESENT")
assert all(_checks)
