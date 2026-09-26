"""
P03_the_third_regime_is_the_boundary_of_admissible_data_and_not_a_behaviour_of_the_lap
=====================================================================================

LEVEL: exact symbolic (sympy) for the turning-point structure; the struck row's own scored
numbers reproduced first as the calibration.

OBJECT UNDER TEST -- `PO-49`, `r6911` item ⓶, open since `r6861`.  The order, verbatim:

    "The charged interior's third regime --- over-extremality --- was found by the verification
     that struck `PO-25` and is carried by nothing.  What the lap does there, on the same exact
     interior, and whether the regime is reachable on a progenitor of the mass this cosmology
     requires.  ⌗ The struck row's own scoring puts the charge-to-mass threshold near 1e-2, so
     reachability is a question about astrophysical charge and not about the geometry --- say
     which of the two you are answering."

-------------------------------------------------------------------------------
** THE ROW CLOSES, AND ON THE FIRST HALF RATHER THAN THE SECOND. **  Both questions are
answered and labelled as the order demands, but the load is carried by the geometry.

  ⓵ ** (GEOMETRY) THE LAP DOES NOTHING THERE, BECAUSE THERE IS NOTHING TO DO. **  With
      beta = B sin^4 chi - Q^2, the third regime is -beta > A^2 sin^4 chi / 4, i.e. the
      turning-point quadratic has no real root.  Its leading coefficient is -sin^2 chi < 0, so
      no real root means it never changes sign:

        (dR/dtau)^2 < 0  at EVERY R > 0,  not merely at small R

      -- checked over sixteen decades in R.  ** So no shell exists at any radius with that
      data.  The third 'regime' is not a third behaviour of the motion at all: it is the
      boundary of ADMISSIBLE INITIAL DATA. **  The other two are statements about a
      trajectory -- beta > 0 reaches R = 0, and 0 < -beta < A^2 sin^4 chi/4 bounces at finite R
      -- and this one is a statement about what can be specified:

        admissible  <=>  Q^2  <=  (B + A^2/4) sin^4 chi

  ⓶ ** AND NO SHELL CAN ENTER OR LEAVE IT DURING THE LAP. **  A, B, Q and sin chi are all
      constants of a comoving shell, so the regime is fixed per shell for all time.  ** That
      closes the dynamical reading of "reachable" as well as the parametric one: ** the regime
      is not somewhere the lap goes, on any shell, ever.

  ⓷ ** (SCORING) AND IT IS UNREACHABLE, BY A MARGIN THAT IS NOT CLOSE. **  At the edge
      (sin chi = 1, A = 2M, B = 2 M a_eq) the window closes at Q^2 = 2 M a_eq + M^2, so

        (Q/M)_third = sqrt(2 a_eq/M + 1) = 1.000134        against
        (Q/M)_obstr = sqrt(2 a_eq/M)     = 1.635e-2

      -- a ratio of 61.2.  The struck row's worst case, the EXTENSIVE reading, has
      Q/M = 4.01e-4: short of the obstruction by 40.7 (the struck row's own "factor 40",
      reproduced) and short of the third regime by ** 2.49e3 **.  On the intensive reading,
      by 2.49e62.

⛔ ** AND THAT IS WHERE THE ORDER'S HINT NEEDS CORRECTING, WHICH IS THE ONE SUBSTANTIVE THING
   THIS ADDS TO IT. **  The order attributes the near-1e-2 charge-to-mass threshold to this
   regime and concludes that reachability is therefore an astrophysical-charge question.
   ** The 1e-2 is the OBSTRUCTION threshold -- the boundary of the SECOND regime -- and this
   regime's threshold is 1.000134, which is over-extremality. **  Since 2 a_eq/M = 2.67e-4 << 1,
   the dust-and-radiation term is negligible against M^2 and the boundary is Q > M to four
   decimal places.  ⇒ *So reachability here is NOT a question about how much charge a star can
   hold: it is settled by over-extremality alone, and needs no astrophysical bound at all.*
   ** Which is the cleaner answer, and it is the geometry's, not the astrophysics'. **

COMPUTES: scope -- what this settles and what it must not be read as.
  * ** THE CALIBRATION IS THE GATE. **  PART 1 reproduces the struck row's own scored figures
    -- (Q/M)_crit = 1.6e-2, short by 40 extensive and 1e60 intensive -- from the constants
    here.  If those do not come back, nothing below may be read, because every number below
    is built on the same conversion.
  * ** PER-SHELL, AS IT HAS TO BE. **  A radial electric field makes the stress anisotropic, so
    exact homogeneity is broken and every statement here is per-shell -- exactly the scope the
    striking receipt set, quoted rather than re-derived.
  * ** NOT that the branch point is reached. **  `r6405` left what replaces the Cauchy horizon
    as a numerical-relativity question and that stands; this says the third regime is not a
    motion, not that any other motion is smooth.
  * ** NOT a statement about the obstruction. **  `PO-25` is struck and stays struck; the
    second regime's threshold is quoted here only to put the third's beside it.
  * ** NO NEW INTERIOR. **  The background, a_eq = 1.49 Mpc, the masses and both charge readings
    are taken from the banked receipt, not re-chosen.

rc=0 on success.  Run: python3 P03_the_third_regime_is_the_boundary_of_admissible_data_and_not_a_behaviour_of_the_lap.py
"""
import sys

import numpy as np
import sympy as sp

print(__doc__.split("\n", 1)[1].split("COMPUTES:")[0].rstrip())
print("COMPUTES:" + __doc__.split("COMPUTES:")[1].split("rc=0")[0].rstrip())

FAILED = []


def check(ok, msg):
    print(f"    {'OK  ' if ok else 'FAIL'}  {msg}")
    if not ok:
        FAILED.append(msg)


def head(title):
    print()
    print("=" * 94)
    print(title)
    print("=" * 94)


Msun, Mpc = 1.98847e30, 3.0857e22
G, c, eps0, e_C = 6.67430e-11, 2.99792458e8, 8.8541878128e-12, 1.602176634e-19
gm = lambda M_kg: G * M_kg / c**2                              # mass in metres
gq = lambda Q_C: np.sqrt(G / (4 * np.pi * eps0)) * Q_C / c**2  # charge in metres
A_EQ = 1.49 * Mpc                       # P16 sec:interior, DETERMINED (taken, not chosen)
M_REG = gm(2.33e23 * Msun)              # the register's progenitor mass
Q_EXT = gq(1e-21 * e_C * 1e80)          # extensive reading: 1e-21 e per baryon, 1e80 baryons
Q_INT = gq(e_C)                         # intensive reading: one electron charge

# =============================================================================================
head("PART 1 (C1) -- THE STRUCK ROW'S OWN SCORED FIGURES, REPRODUCED FIRST")

QM_obstr = np.sqrt(2 * A_EQ / M_REG)
print(f"  a_eq                              = {A_EQ:.4e} m   (= 1.49 Mpc, determined)")
print(f"  M (register, 2.33e23 Msun)        = {M_REG:.4e} m")
print(f"  (Q/M)_crit = sqrt(2 a_eq / M)     = {QM_obstr:.4e}")
print(f"  r_inner extensive = Q^2 / 2M      = {Q_EXT**2/(2*M_REG):.3e} m   (banked: 2.8e19 m)")
print(f"  r_inner intensive = Q^2 / 2M      = {Q_INT**2/(2*M_REG):.3e} m   (banked: 2.8e-99 m)")
short_ext = QM_obstr / (Q_EXT / M_REG)
short_int = QM_obstr / (Q_INT / M_REG)
print(f"  short of the obstruction, extensive = {short_ext:.1f}      (banked: 'a factor 40')")
print(f"  short of the obstruction, intensive = {short_int:.2e}   (banked: '10^60')")
check(abs(QM_obstr / 1.635e-2 - 1) < 0.02, f"(Q/M)_crit reproduces at {QM_obstr:.4e} vs 1.6e-2")
check(abs(Q_EXT**2 / (2 * M_REG) / 2.8e19 - 1) < 0.1, "r_inner extensive reproduces 2.8e19 m")
check(10 < short_ext < 100, f"the extensive shortfall reproduces the banked factor 40 ({short_ext:.1f})")
check(1e59 < short_int < 1e61, f"the intensive shortfall reproduces the banked 10^60 ({short_int:.1e})")

# =============================================================================================
head("PART 2 (a, GEOMETRY) -- IS THE THIRD REGIME A REGIME OF THE MOTION AT ALL?")

R, Q, A, B = sp.symbols('R Q A B', positive=True)
s = sp.Symbol('s', positive=True)                      # s = sin chi
Rdot2 = -s**2 + A * s**3 / R + (B * s**4 - Q**2) / R**2
poly = sp.expand(sp.simplify(Rdot2 * R**2))
disc = sp.factor(sp.expand((A * s**3)**2 - 4 * (-s**2) * (B * s**4 - Q**2)))
print(f"  (dR/dtau)^2 R^2 = {poly}")
print(f"  discriminant    = {disc}")
check(sp.simplify(disc - s**2 * (A**2 * s**4 + 4 * B * s**4 - 4 * Q**2)) == 0,
      "the discriminant is s^2 (A^2 s^4 + 4 B s^4 - 4 Q^2), so disc < 0 is Q^2 - B s^4 > A^2 s^4/4")
print("  the leading coefficient in R is -s^2 < 0, so with NO real root the quadratic")
print("  cannot change sign -- it is negative for every R.  Measured, not argued:")
print(f"  {'A':>5} {'s':>5} {'B':>5} {'Q':>9} {'disc':>11} {'max over R>0':>16}")
allneg = True
for (Av, sv, Bv, mult) in [(1.0, 0.8, 1.0, 4.0), (1.0, 0.8, 1.0, 9.0),
                           (2.0, 0.5, 3.0, 4.0), (0.7, 1.0, 0.2, 25.0)]:
    win = Av**2 * sv**4 / 4
    Qv = np.sqrt(Bv * sv**4 + mult * win)
    d = (Av * sv**3)**2 - 4 * (-sv**2) * (Bv * sv**4 - Qv**2)
    Rg = np.logspace(-8, 8, 20001)
    mx = float((-sv**2 * Rg**2 + Av * sv**3 * Rg + (Bv * sv**4 - Qv**2)).max())
    allneg &= mx < 0
    print(f"  {Av:>5.2f} {sv:>5.2f} {Bv:>5.2f} {Qv:>9.5f} {d:>11.5f} {mx:>16.6e}")
check(allneg,
      "(dR/dtau)^2 < 0 at EVERY radius over sixteen decades, not merely at small R")
print()
print("  ⇒ ** so no shell exists at any radius with that data, and the lap does NOTHING")
print("       there because there is no motion to do.  The third 'regime' is the boundary")
print("       of ADMISSIBLE INITIAL DATA and not a third behaviour of the lap. **")
adm = sp.simplify(sp.factor(B * s**4 + A**2 * s**4 / 4))
check(sp.simplify(adm - (B + A**2 / 4) * s**4) == 0,
      f"and the admissibility condition is Q^2 <= (B + A^2/4) sin^4 chi")

# =============================================================================================
head("PART 3 -- AND NO SHELL ENTERS OR LEAVES IT DURING THE LAP")

print("  A, B and Q are constants of the shell and sin chi is its comoving label, so the")
print("  regime indicator depends on no dynamical variable.  R does not appear in it:")
ind = sp.simplify((B + A**2 / 4) * s**4 - Q**2)
print(f"      regime indicator = {ind}")
check(sp.diff(ind, R) == 0 and R not in ind.free_symbols,
      "the indicator is independent of R, so a shell cannot evolve across the boundary")
print("  ⇒ ** which closes the DYNAMICAL reading of 'reachable' as well as the parametric")
print("       one: the regime is not somewhere the lap goes, on any shell, ever. **")

# =============================================================================================
head("PART 4 (b, SCORING) -- IS IT REACHABLE ON THE PROGENITOR THIS COSMOLOGY REQUIRES?")

QM_third = np.sqrt(2 * A_EQ / M_REG + 1.0)
print(f"  at the edge (sin chi = 1, A = 2M, B = 2 M a_eq) the window closes at Q^2 = 2 M a_eq + M^2")
print(f"  (Q/M)_third = sqrt(2 a_eq/M + 1) = {QM_third:.6f}")
print(f"  (Q/M)_obstr = sqrt(2 a_eq/M)     = {QM_obstr:.4e}")
print(f"  ratio third / obstruction        = {QM_third/QM_obstr:.2f}")
print(f"  2 a_eq / M                       = {2*A_EQ/M_REG:.3e}  << 1")
check(abs(QM_third - 1.0) < 1e-3,
      f"the third regime's threshold is OVER-EXTREMALITY: Q/M > 1 to within {QM_third-1:.2e}")
check(50 < QM_third / QM_obstr < 70,
      f"it sits {QM_third/QM_obstr:.1f}x above the obstruction threshold the struck row scored")
print()
print(f"  {'charge reading':<44} {'Q/M':>12} {'short of obstr':>15} {'short of third':>15}")
rows = []
for lbl, Qv in (("intensive  (one e)", Q_INT),
                ("extensive  (1e-21 e/baryon, 1e80 baryons)", Q_EXT)):
    qm = Qv / M_REG
    rows.append(QM_third / qm)
    print(f"  {lbl:<44} {qm:>12.4e} {QM_obstr/qm:>15.3e} {QM_third/qm:>15.3e}")
check(min(rows) > 1e3,
      f"both readings fall short of the third regime, the worst case by {min(rows):.2e}")

# =============================================================================================
head("VERDICT")

print(f"""
  ⇒ ** `PO-49` CLOSES, AND ON THE GEOMETRY RATHER THAN ON THE SCORING. **

  (a) ** WHAT THE LAP DOES THERE: NOTHING, BECAUSE THERE IS NO THERE. **  The turning-point
      quadratic has negative leading coefficient, so no real root makes it negative at EVERY
      radius -- verified over sixteen decades.  No shell exists with that data at any R, so
      the third case is the boundary of admissible initial data and not a third behaviour of
      the motion.  And its indicator contains no dynamical variable, so no shell crosses the
      boundary during the lap either.  ** The clean binary the struck row stated is a binary
      about TRAJECTORIES, and it was right to be: the third case is a constraint on
      specification, which is a different kind of object. **

  (b) ** WHETHER IT IS REACHABLE: NO, by {min(rows):.1e} in Q on the row's own worst case. **
      (Q/M)_third = {QM_third:.6f} against (Q/M)_obstr = {QM_obstr:.3e}, a factor {QM_third/QM_obstr:.1f}.

  ⛔ ** AND THE ORDER'S HINT IS THE ONE THING WORTH CORRECTING. **  It puts this regime's
    threshold near 1e-2 and concludes reachability is an astrophysical-charge question.
    ** The 1e-2 belongs to the OBSTRUCTION -- the second regime's boundary -- and this
    regime's is 1.000134. **  Because 2 a_eq/M = {2*A_EQ/M_REG:.2e} is tiny, the matter terms are
    negligible against M^2 and the boundary is over-extremality to four decimals.  ⇒ *So
    reachability is settled without any bound on astrophysical charge, and the answer to
    "which of the two are you answering" is: the geometry, for both halves.*

  ⌗ WHAT THIS DOES NOT DO.  `PO-25` stays struck and is not reopened; nothing here says the
    branch point is reached or that any other motion is smooth (`r6405` stands); and every
    statement is per-shell, because a radial electric field breaks exact homogeneity.
""".rstrip())

print()
if FAILED:
    print("FAIL: " + "; ".join(FAILED))
    sys.exit(1)
print("ALL CHECKS PASS")
sys.exit(0)
