"""
P03_the_interior_mass_function_is_p_equals_one_along_the_shell_and_the_charge_falls_short_of_the_equality_radius
===============================================================================================================

LEVEL: exact symbolic (sympy), with the numbers scored on the corpus's own progenitor.

OBJECT UNDER TEST -- the four-line derivation routed at `r6841`, which proposes to answer
`PO-25` by putting `P16` sec:interior's exact closed dust-plus-radiation ball together with
`P03` sec:charge's sharpened criterion.  The routed claim, verbatim:

    "For the closed interior, 2m/r = (adot^2 + 1) sin^2 chi and adot^2 + 1 = (Aa + B)/a^2,
     so m = (Aa + B) sin^3 chi / 2a.  Substituting r = a sin chi:
         m(r) = (1/2) A sin^3 chi  +  (1/2) B sin^4 chi / r.
     So p = 1 identically, the constant being the dust and the 1/r being the radiation ...
     and the obstruction survives exactly when Q^2 > B sin^4 chi -- a scale-free
     competition between the charge and the shell's radiation content, with the dust
     dropping out of the comparison entirely."

The order was: check the algebra, then ATTACK it, then report the physical reading either
way.  It was explicitly NOT a licence to land it.

-------------------------------------------------------------------------------
WHAT THIS PROBE FINDS, IN ONE PARAGRAPH.

** THE ALGEBRA IS CORRECT -- every step of it, including the sign conventions and the
Misner--Sharp definition, which are re-derived here from the metric rather than quoted. **
But the derivation is silent on WHICH r -> 0 limit it takes, and the two available limits
give different exponents: across a constant-time slice m(r) goes as r^3 (p = -3, the
regular FRW centre), and along a comoving shell m(R) goes as 1/R (p = 1).  The criterion
`PO-25` needs is the second, and the routed reading takes it -- correctly, but without
saying so, and the row's own wording ("the interior mass function at the origin") reads as
the first.  ** Two of the three attacks the order named fail to break it and one lands. **
The exponent survives charge (Gauss's law and radiation redshift are both exactly R^-2)
and survives a non-uniform profile at leading order, but ** the comparison is NOT
scale-free in chi: the charge enclosed vanishes as chi^3 while B sin^4 chi vanishes as
chi^4, so Q^2 / (B sin^4 chi) ~ chi^2 -> 0 and the obstruction ALWAYS fails on a central
core, whatever the total charge. **  And "the dust drops out" is true only while A and B
are read as independent: the corpus DETERMINES B = A a_eq, so the criterion is

        Q^2 > 2 M(chi) a_eq sin chi        i.e.        r_inner(chi) > a_eq sin chi

-- the Reissner--Nordstroem inner-horizon radius against the progenitor's matter-radiation
equality radius, with the dust mass squarely in it.  ** Scored on the corpus's own
progenitor the charge falls short of that threshold by a factor 40 in Q on the EXTENSIVE
reading and by 10^60 on the INTENSIVE one, so the obstruction is destroyed on both -- which
decouples `PO-25` from the datum fork the same way `r6405` did, and this time answers it. **

-------------------------------------------------------------------------------
WHAT IS CLAIMED.

 (1) The Misner--Sharp identity 2m/R = (adot^2 + 1) sin^2 chi is derived, not assumed, from
     the closed FRW metric and the corpus's own m_MS = (R/2)(1 - (grad R)^2).
 (2) (a')^2 + a^2 = A a + B is the first integral of `P16`'s a'' + a = A/2, and the routed
     substitution returns m(R) = (1/2) A sin^3 chi + (1/2) B sin^4 chi / R exactly.
 (3) The r -> 0 limit is ambiguous and the two readings differ: SPATIAL (fixed time,
     chi -> 0) gives m ~ r^3 with the FRW density as coefficient; COMOVING (fixed shell,
     a -> 0) gives p = 1.  The dynamical criterion needs the comoving one.
 (4) ATTACK (a) FAILS TO BREAK IT.  Charge does not move the exponent: the electromagnetic
     contribution to m is -Q^2/2R identically (verified off the RN metric) and the
     radiation contribution is +const/R identically (verified off dm/dt = -4 pi p R^2 dR/dt
     with p = rho/3), so both terms are exactly R^-2 in 2m/R and p = 1 is charge-blind.
 (5) ATTACK (b) FAILS AT LEADING ORDER AND LEAVES A NAMED GAP.  The per-shell derivation of
     (4) uses only the equations of state and needs no homogeneity, so a non-uniform dust
     profile does not move p.  It DOES need rho_r ~ R^-4 at fixed shell, which is the
     top-hat's behaviour; off it the radial/tangential split of the expansion moves the
     radiation exponent and there is no exact statement.  That is a gap, not a refutation.
 (6) ATTACK (c) LANDS.  The criterion is chi-dependent and degenerates at the centre:
     Q(chi)^2 / (B sin^4 chi) ~ chi^2 -> 0 for any charge distribution with finite comoving
     density, so there is always a critical shell chi_* inside which the collapse reaches
     R = 0.  ** The obstruction can never be total, which contradicts the row's landed
     "obstructed TOTALLY at any Q > 0". **
 (7) The turning-point structure is exhibited, and it has THREE regimes where the routed
     reading states two.  Writing beta = B sin^4 chi - Q^2 in
     dR/dtau^2 = -sin^2 chi + A sin^3 chi / R + beta / R^2:  beta > 0 gives one positive root
     and R = 0 is reached; 0 < -beta < A^2 sin^4 chi / 4 gives two and the shell bounces at
     finite R -- that is the obstruction; -beta > A^2 sin^4 chi / 4 gives none at all, so the
     shell does not exist with that energy.  The third is over-extremality (Q > M at the edge)
     and is outside the problem, but the clean binary owes the clause.
 (8) In corpus units the criterion is r_inner > a_eq sin chi, and at the edge the threshold
     is a charge-to-mass ratio (Q/M)_crit = sqrt(2 a_eq / M).  Both of the row's charge
     readings fall below it.

WHAT IS NOT CLAIMED.

 * NOT that the branch point is thereby reached.  `r6405` established that what replaces the
   Cauchy horizon is a numerical-relativity question; this probe says the CHARGE term does
   not stop the collapse, not that the collapse is smooth.
 * NOT that the charged interior IS `P16`'s ball.  A radial electric field makes the stress
   anisotropic, so exact homogeneity is broken; every statement here is per-shell, which is
   where it has to live anyway.
 * NOT a value for the progenitor's charge.  The two readings are the row's own and the
   verdict is reported on both, because it does not depend on which is right.

** COMPUTES: the progenitor of `P16` sec:interior and `P03` sec:lap, at the determined
composition -- a_eq = A rho^2 / 4 = B/A = 1.49 Mpc with rho = 5.4e-2 -- scored at BOTH masses the
corpus carries (M = 2.33e23 Msun from THE_REGISTER's charge computation, M = 4.3e52 kg from P16's
own determination) and at BOTH of the row's charge readings (intensive, one e; extensive,
1e-21 e per baryon over 1e80 baryons).  The symbolic parts are parameter-free and hold for any
(A, B, Q, chi).  Lambda = 0 throughout, as in P16's interior; the verdict is a comparison of two
lengths and a Lambda term enters m_MS only at O(R^3), which PART 1 gates. **

WHAT WOULD FALSIFY IT.  The Misner--Sharp identity failing off the metric; the substitution
not returning the routed m(R); the chi^2 scaling of the central degeneracy not appearing;
or the scored shortfall reversing on either charge reading.
"""
import numpy as np
import sympy as sp
from scipy.optimize import brentq

FAILS = []


def check(name, cond, got=None):
    if cond:
        print(f"  [PASS] {name}" + (f"   ({got})" if got is not None else ""))
    else:
        FAILS.append(name)
        print(f"  [FAIL] {name}" + (f"   (got {got})" if got is not None else ""))


print(__doc__)
print("=" * 100)

eta, chi = sp.symbols('eta chi', real=True)
t = sp.Symbol('t', real=True)
A, B, a, R, Q, k, rho0 = sp.symbols('A B a R Q k rho_0', positive=True)

# ---------------------------------------------------------------------------------
print("\nPART 1 -- THE MISNER--SHARP IDENTITY, DERIVED OFF THE METRIC AND NOT QUOTED.")
print("-" * 100)
print("  closed FRW:  ds^2 = -dt^2 + a(t)^2 [ dchi^2 + sin^2 chi dOmega^2 ],  R = a sin chi")
print("  corpus definition (SdS-slicing-curve_v2 sec 8.4):  m_MS(R) = (R/2)(1 - f),")
print("  with f = (grad R)^2 = g^{mu nu} d_mu R d_nu R.")

af = sp.Function('a')(t)
Rr = af * sp.sin(chi)
grad2 = -sp.diff(Rr, t) ** 2 + sp.diff(Rr, chi) ** 2 / af ** 2   # g^tt = -1, g^chichi = 1/a^2
m_MS = sp.simplify(Rr * (1 - grad2) / 2)
two_m_over_R = sp.simplify(2 * m_MS / Rr)
print(f"\n  (grad R)^2 = {sp.simplify(grad2)}")
print(f"  2 m / R    = {two_m_over_R}")

target_id = (sp.Derivative(af, t) ** 2 + 1) * sp.sin(chi) ** 2
check("2m/R = (adot^2 + 1) sin^2 chi  -- the routed identity, derived",
      sp.simplify(two_m_over_R - target_id) == 0)

# Lambda rides as r^3 and cannot matter at the origin (corpus: m_MS = M + r^3/2 alpha^2)
al = sp.Symbol('alpha', positive=True)
check("a Lambda term enters m_MS as R^3/2alpha^2, so it is O(R^3) at the origin and cannot compete",
      sp.limit((R ** 3 / (2 * al ** 2)) * R, R, 0, '+') == 0)

# ---------------------------------------------------------------------------------
print("\nPART 2 -- THE FIRST INTEGRAL AND THE SUBSTITUTION.  IS THE ROUTED m(R) RIGHT?")
print("-" * 100)

a_sol = A / 2 * (1 - sp.cos(eta)) + sp.sqrt(B) * sp.sin(eta)      # P16 sec:interior
print(f"  P16:  a(eta) = {a_sol}")

check("a'' + a = A/2  -- P16's driven oscillator (conformal time)",
      sp.simplify(sp.diff(a_sol, eta, 2) + a_sol - A / 2) == 0)
check("(a')^2 + a^2 = A a + B  -- its first integral, so A is the dust and B the radiation",
      sp.simplify(sp.diff(a_sol, eta) ** 2 + a_sol ** 2 - A * a_sol - B) == 0)

# adot = a'/a because dt = a d(eta).  Two derivatives, two conventions -- both routed lines
# are right in their own, and this is the sign check the order asked for.
adot2 = (A * a + B - a ** 2) / a ** 2
check("adot^2 + 1 = (Aa + B)/a^2  with adot = d/dt and a' = d/deta  (the conventions differ "
      "between the two routed lines and both are correct)",
      sp.simplify((adot2 + 1) - (A * a + B) / a ** 2) == 0)

m_of_R = sp.simplify(sp.expand(sp.simplify((adot2 + 1) * sp.sin(chi) ** 2 * R / 2).subs(a, R / sp.sin(chi))))
routed = A * sp.sin(chi) ** 3 / 2 + B * sp.sin(chi) ** 4 / (2 * R)
print(f"\n  substituting a = R / sin chi:   m(R) = {m_of_R}")
print(f"  routed claim                  :   m(R) = {routed}")
check("the routed m(R) = (1/2) A sin^3 chi + (1/2) B sin^4 chi / R is EXACT",
      sp.simplify(m_of_R - routed) == 0)
print("\n  => THE ALGEBRA IS CORRECT.  Nothing in PART 1 or PART 2 is wrong.")

# ---------------------------------------------------------------------------------
print("\nPART 3 -- BUT WHICH r -> 0?  THE TWO LIMITS GIVE DIFFERENT EXPONENTS.")
print("-" * 100)
print("  m(R) above holds chi FIXED and lets R vary, i.e. it is a statement along a comoving")
print("  shell as the collapse proceeds.  The row's wording -- 'the interior mass function at")
print("  the origin' -- descends from the STATIC f(r) and reads as a spatial profile.  They")
print("  are not the same limit and they do not give the same p.")

lead_comoving = sp.limit(routed * R, R, 0, '+')
check("COMOVING (chi fixed, R -> 0):  R m(R) -> B sin^4 chi / 2, so p = 1 and 2k = B sin^4 chi",
      sp.simplify(lead_comoving - B * sp.sin(chi) ** 4 / 2) == 0, sp.simplify(lead_comoving))

m_spatial = sp.simplify(routed.subs(sp.sin(chi), R / a))          # fixed a, chi -> 0
coef = sp.simplify(m_spatial / R ** 3)
check("SPATIAL (a fixed, chi -> 0):  m(R) = R^3 (A a + B) / 2 a^4, so p = -3, not 1",
      sp.simplify(m_spatial - R ** 3 * (A * a + B) / (2 * a ** 4)) == 0, coef)
# and that coefficient is the FRW density, which is what a regular centre must give
check("...and its coefficient is (4 pi/3) rho with rho the closed-FRW density "
      "(H^2 + 1/a^2 = 8 pi rho/3), i.e. the SPATIAL reading is just centre regularity",
      sp.simplify(coef - sp.Rational(4, 3) * sp.pi * sp.Rational(3, 8) / sp.pi * (A * a + B) / a ** 4) == 0)

print("\n  => The routed derivation takes the COMOVING limit.  That is the right one for")
print("     PO-25 -- the criterion is about whether a collapsing shell REACHES R = 0, and")
print("     there is no static f in a dynamical interior to read a spatial profile off.")
print("     ** But the row's own wording does not say so, and read spatially the answer is")
print("     the trivial p = -3.  That is a wording debt on the row, not an error here. **")

# ---------------------------------------------------------------------------------
print("\nPART 4 -- ATTACK (a): DOES THE CHARGED BALL'S OWN DYNAMICS MOVE THE EXPONENT?")
print("-" * 100)
print("  The order asks whether the charge, which alters the evolution, alters the r-scaling")
print("  of the radiation term.  It does not, and the reason is that BOTH terms are pinned by")
print("  conservation laws rather than by the background.")

# (i) the electromagnetic contribution to m_MS is -Q^2/2R identically -- read off RN
M_c = sp.Symbol('M_c', positive=True)
f_RN = 1 - 2 * M_c / R + Q ** 2 / R ** 2
m_from_f = sp.simplify(R * (1 - f_RN) / 2)
check("EM: m_MS = (R/2)(1-f) on Reissner--Nordstroem gives M - Q^2/2R, so the charge enters m "
      "as exactly -Q^2/2R (Gauss's law makes Q conserved, so this needs no stationarity)",
      sp.simplify(m_from_f - (M_c - Q ** 2 / (2 * R))) == 0, m_from_f)

# (ii) the radiation contribution is +const/R identically -- from dm/dt = -4 pi p R^2 Rdot
tau = sp.Symbol('tau', real=True)
Rf = sp.Function('R')(tau)
C = sp.Symbol('C', positive=True)
rho_r = C / Rf ** 4                                   # comoving radiation at fixed shell
m_rad_guess = 4 * sp.pi * C / (3 * Rf)
lhs = sp.diff(m_rad_guess, tau)
rhs = -4 * sp.pi * (rho_r / 3) * Rf ** 2 * sp.diff(Rf, tau)      # p = rho/3
check("RADIATION: with p = rho/3 and rho ~ R^-4 at fixed shell, the Misner--Sharp evolution "
      "dm/dtau = -4 pi p R^2 dR/dtau integrates to m_rad = 4 pi C / 3R exactly",
      sp.simplify(lhs - rhs) == 0)
m_dust_guess = sp.Symbol('M_d', positive=True)
check("DUST: p = 0 gives dm/dtau = 0, so the dust part is constant along the shell -- the "
      "'A sin^3 chi' term",
      sp.simplify(sp.diff(m_dust_guess, tau)) == 0)

print("\n  => Both the charge's -Q^2/2R and the radiation's +C/R are EXACT 1/R terms in m, so")
print("     they both appear at order R^-2 in 2m/R and compete at the same order at every R.")
print("     ** ATTACK (a) FAILS: p = 1 is charge-blind and the competition is genuinely")
print("     R-independent -- that part of the routed reading is right and is the good part. **")
print("\n  ONE THING THE ROUTED LINE DOES NOT SAY AND SHOULD.  A radial electric field makes")
print("  the stress anisotropic, so a charged ball is not exactly P16's homogeneous interior.")
print("  The two conservation laws above need no homogeneity, so the CONCLUSION survives -- but")
print("  it is a per-shell statement, not a statement about 'the interior mass function'.")

# ---------------------------------------------------------------------------------
print("\nPART 5 -- ATTACK (b): A NON-UNIFORM PROFILE, AND SHELL CROSSING.")
print("-" * 100)
print("  PART 4's derivation used only the equations of state and the Misner--Sharp evolution")
print("  equation, with no homogeneity anywhere, so A -> 2 M_d(chi) and B sin^4 chi -> 2C(chi)")
print("  shell by shell and p = 1 is untouched by a non-uniform DUST profile.")
Md_f, C_f = sp.Function('M_d')(chi), sp.Function('C')(chi)
m_profile = Md_f + 4 * sp.pi * C_f / (3 * Rf) - Q ** 2 / (2 * Rf)
rho_tot = C_f / Rf ** 4                                   # radiation only carries pressure
lhs_p = sp.diff(m_profile + Q ** 2 / (2 * Rf), tau)       # matter part of m only
rhs_p = -4 * sp.pi * (rho_tot / 3) * Rf ** 2 * sp.diff(Rf, tau)
check("p = 1 survives a chi-dependent profile: with M_d(chi) and C(chi) arbitrary functions "
      "of the shell label, dm/dtau = -4 pi p R^2 dR/dtau still integrates to M_d(chi) + "
      "4 pi C(chi)/3R, so 2m/R still carries an exact R^-2 term",
      sp.simplify(lhs_p - rhs_p) == 0)
check("...and the charge rides in the same R^-2 slot with the opposite sign, so the marginal "
      "competition is (8 pi C(chi)/3 - Q(chi)^2) shell by shell",
      sp.simplify(sp.limit(m_profile.subs(Rf, R) * R, R, 0, '+')
                  - (4 * sp.pi * C_f / 3 - Q ** 2 / 2)) == 0)
print("\n  ** BUT TWO THINGS ARE GENUINELY LEFT OPEN AND ARE NAMED RATHER THAN CLOSED. **")
print("   (i) rho_r ~ R^-4 AT FIXED SHELL is the homogeneous (and self-similar) behaviour.  In")
print("       a Lemaitre--Tolman-like interior the radial and tangential expansion rates differ")
print("       and a comoving perfect fluid redshifts as (R^2 R')^{-4/3}; that reduces to R^-4")
print("       only when R' ~ R near the crunch.  Off that, the radiation exponent moves and")
print("       there is no exact statement.  This probe does not supply one.")
print("  (ii) Radiation has pressure, so on a non-uniform profile it does not stay comoving at")
print("       all -- pressure gradients drive flow between shells and C(chi) stops being")
print("       conserved.  The top-hat is the case in which the routed derivation is exact.")
print("  (iii) SHELL CROSSING is produced by the criterion's own verdict: if outer shells")
print("       bounce (PART 7) while inner ones do not, the comoving labelling degenerates and")
print("       the premises of the derivation fail behind the first crossing.")
print("\n  => ATTACK (b) does not break the exponent, and it does bound the claim's scope.")

# ---------------------------------------------------------------------------------
print("\nPART 6 -- ATTACK (c): IS sin chi THE RIGHT MEASURE AT THE CENTRE?  ** THIS ONE LANDS. **")
print("-" * 100)
print("  The routed criterion Q^2 > B sin^4 chi is called 'scale-free'.  It is R-free -- PART 4")
print("  -- but it is NOT chi-free, and PO-25's question is asked AT THE CENTRE.  The charge")
print("  enclosed within a comoving radius is itself a function of chi, and it vanishes faster.")

chi_s = sp.Symbol('chi', positive=True)
Vcom = sp.integrate(sp.sin(chi_s) ** 2, (chi_s, 0, chi))          # comoving charge volume
q_c = sp.Symbol('q_c', positive=True)
Q_chi = q_c * Vcom
ratio = sp.simplify(Q_chi ** 2 / (B * sp.sin(chi) ** 4))
ser = sp.simplify(sp.series(ratio, chi, 0, 3).removeO())
print(f"\n  Q(chi) = q_c INT_0^chi sin^2 = {sp.simplify(Q_chi)}")
print(f"  Q(chi)^2 / (B sin^4 chi)  ~  {ser}   as chi -> 0")
check("the criterion degenerates at the centre as chi^2: Q^2/(B sin^4 chi) -> 0 for ANY "
      "finite comoving charge density, so the obstruction ALWAYS fails on a central core",
      sp.limit(ratio, chi, 0, '+') == 0
      and sp.simplify(sp.diff(sp.simplify(ser / chi ** 2), chi)) == 0,
      f"leading term {ser}")

print("\n  numerical confirmation of the chi^2 scaling (uniform comoving charge, chi_b = pi/2):")
Vc = lambda x: (x - np.sin(x) * np.cos(x)) / 2
chib = np.pi / 2
prev = None
for xv in (1e-1, 1e-2, 1e-3, 1e-4):
    rr = (Vc(xv) / Vc(chib)) ** 2 / np.sin(xv) ** 4
    tag = "" if prev is None else f"   ratio to previous decade = {rr / prev:.4f}  (expect 1e-2)"
    print(f"    chi = {xv:.0e} :  Q^2/(B sin^4 chi) / (Q_tot^2/B) = {rr:.5e}{tag}")
    prev = rr
check("the decade-to-decade ratio is 1e-2, i.e. the degeneracy is exactly chi^2",
      abs(((Vc(1e-3) / Vc(chib)) ** 2 / np.sin(1e-3) ** 4) /
          ((Vc(1e-2) / Vc(chib)) ** 2 / np.sin(1e-2) ** 4) - 1e-2) < 1e-3)

print("\n  So there is always a CRITICAL SHELL chi_*, and the core inside it reaches R = 0:")
stars = []
for fac in (2.0, 10.0, 100.0, 1.0e4, 1.0e8):
    f = lambda x: fac * (Vc(x) / Vc(chib)) ** 2 - np.sin(x) ** 4
    xs = brentq(f, 1e-10, chib - 1e-12)
    stars.append((fac, xs))
    print(f"    Q_tot^2 / B = {fac:10.1f}  (edge criterion satisfied)  ->  chi_* = {xs:.6f} rad, "
          f"unobstructed core carries sin^3 chi_* = {np.sin(xs) ** 3:.4e} of the dust mass")
check("a critical shell exists strictly inside the ball for every total charge, and the core "
      "inside it is unobstructed -- against the row's landed 'obstructed TOTALLY at any Q > 0'",
      all(0.0 < x < chib for _, x in stars)
      and all(fac * (Vc(0.5 * x) / Vc(chib)) ** 2 < np.sin(0.5 * x) ** 4 for fac, x in stars),
      f"chi_* from {stars[-1][1]:.2e} to {stars[0][1]:.4f} rad over 8 decades in Q_tot^2")
check("...and chi_* shrinks as Q_tot^(-1/2), the signature of the chi^2 degeneracy rather than "
      "of any scale in the problem",
      abs(np.log(stars[-1][1] / stars[-2][1]) / np.log(np.sqrt(stars[-2][0] / stars[-1][0])) - 1) < 0.02,
      f"exponent {np.log(stars[-1][1] / stars[-2][1]) / np.log(stars[-1][0] / stars[-2][0]):.4f} vs -1/2")

# ---------------------------------------------------------------------------------
print("\nPART 7 -- THE TURNING-POINT STRUCTURE, SO THE CRITERION IS A STATEMENT ABOUT MOTION.")
print("-" * 100)
print("  Along a comoving shell, with the charge's -Q^2/R^2 added to the generalised")
print("  Misner--Sharp relation (grad R)^2 = 1 - 2m/R + Q^2/R^2:")
print("      (dR/dtau)^2 = -sin^2 chi + A sin^3 chi / R + (B sin^4 chi - Q^2) / R^2 .")
s = sp.Symbol('s', positive=True)                # s = sin chi
Rdot2 = -s ** 2 + A * s ** 3 / R + (B * s ** 4 - Q ** 2) / R ** 2
poly = sp.simplify(sp.expand(Rdot2 * R ** 2))
roots = sp.solve(sp.Eq(poly, 0), R)
prod = sp.simplify(sp.expand((B * s ** 4 - Q ** 2) / (-s ** 2)))
check("the turning-point polynomial is -s^2 R^2 + A s^3 R + (B s^4 - Q^2), whose root PRODUCT "
      "is (Q^2 - B s^4)/s^2 and root SUM is A s > 0",
      sp.simplify(prod - (Q ** 2 - B * s ** 4) / s ** 2) == 0)
print("\n  ** AND THERE ARE THREE REGIMES, NOT TWO -- the routed reading states the binary and")
print("     the discriminant carries a third.  Writing beta = B sin^4 chi - Q^2: **")


def regimes(Av, sv, Bv, Qv):
    a2, a1, a0 = -sv ** 2, Av * sv ** 3, Bv * sv ** 4 - Qv ** 2
    return a1 ** 2 - 4 * a2 * a0, np.roots([a2, a1, a0])


Av, sv, Bv = 1.0, 0.8, 1.0
Bs4 = Bv * sv ** 4
win = Av ** 2 * sv ** 4 / 4                       # beta > -win is the disc > 0 window
for lbl, Qv in (("beta > 0  (Q^2 < B sin^4 chi)", np.sqrt(0.5 * Bs4)),
                ("beta < 0, disc > 0", np.sqrt(Bs4 + 0.4 * win)),
                ("beta < 0, disc < 0", np.sqrt(Bs4 + 4.0 * win))):
    d, rts = regimes(Av, sv, Bv, Qv)
    pos = np.sort(np.real(rts[np.isreal(rts)]))
    pos = pos[pos > 0]
    print(f"    {lbl:<32s} Q = {Qv:.5f}  disc = {d:+.5f}  positive roots = "
          f"{np.array2string(pos, precision=5)}")

d0, r0 = regimes(Av, sv, Bv, np.sqrt(0.5 * Bs4))
d1, r1 = regimes(Av, sv, Bv, np.sqrt(Bs4 + 0.4 * win))
d2, r2 = regimes(Av, sv, Bv, np.sqrt(Bs4 + 4.0 * win))
p0 = np.real(r0[np.isreal(r0)]); p0 = p0[p0 > 0]
p1 = np.real(r1[np.isreal(r1)]); p1 = p1[p1 > 0]
check("beta > 0: ONE positive root (the turnaround) -- the shell reaches R = 0, no obstruction",
      len(p0) == 1, f"root {p0[0]:.5f}")
check("0 < Q^2 - B sin^4 chi < A^2 sin^4 chi / 4: TWO positive roots -- the shell BOUNCES at "
      "finite R and never reaches the branch point.  ** THIS is the obstruction. **",
      d1 > 0 and len(p1) == 2, f"allowed band R in [{p1.min():.5f}, {p1.max():.5f}]")
check("Q^2 - B sin^4 chi > A^2 sin^4 chi / 4: NO real root, so (dR/dtau)^2 < 0 everywhere and "
      "the shell does not exist with that energy at all -- a re-specification, not a bounce",
      d2 < 0, f"disc = {d2:+.5f}")
print("\n  ** THE THIRD REGIME IS OVER-EXTREMALITY AND IS OUTSIDE THE PROBLEM. **  At the edge")
print("  (sin chi = 1, A = 2M) the window closes at Q^2 = B + M^2, and on the progenitor")
print("  M^2 = 1.2e53 m^2 against B = 3.2e49 m^2, so it is reached only for Q > M.  ** But the")
print("  routed line's clean binary is a statement about beta alone and does owe this clause. **")
check("Q^2 < B sin^4 chi  =>  product < 0  =>  ONE positive root (the turnaround) and "
      "(dR/dtau)^2 -> +oo as R -> 0: the shell REACHES R = 0",
      sp.limit(Rdot2.subs(Q, 0), R, 0, '+') == sp.oo)
print("\n  => the routed criterion is confirmed as a statement about the shell's motion, which")
print("     is the only form it can take in a dynamical interior.")

# ---------------------------------------------------------------------------------
print("\nPART 8 -- 'THE DUST DROPS OUT' IS FALSE ONCE THE CORPUS'S OWN DETERMINATION IS USED.")
print("-" * 100)
print("  Q^2 > B sin^4 chi has no A in it while A and B are free.  They are not free here:")
print("  P16 sec:interior DETERMINES rho = 2 sqrt(B)/A from the progenitor's equality radius,")
print("  a_eq = A rho^2 / 4 = B / A = 1.49 Mpc.  Substituting B = A a_eq, with the enclosed")
print("  dust mass 2 M(chi) = A sin^3 chi:")
M_chi = sp.Symbol('M_chi', positive=True)
a_eq_s = sp.Symbol('a_eq', positive=True)
crit_B = B * sp.sin(chi) ** 4
crit_sub = sp.simplify(crit_B.subs(B, A * a_eq_s))
crit_M = sp.simplify(crit_sub.subs(A, 2 * M_chi / sp.sin(chi) ** 3))
check("B sin^4 chi = 2 M(chi) a_eq sin chi, so the criterion is Q^2 > 2 M(chi) a_eq sin chi "
      "-- the DUST MASS is in it",
      sp.simplify(crit_M - 2 * M_chi * a_eq_s * sp.sin(chi)) == 0, crit_M)
check("dividing by 2M(chi): the criterion is r_inner(chi) > a_eq sin chi, with "
      "r_inner = Q^2/2M the corpus's OWN quantity from PO13_WORKING_STATE",
      sp.simplify(crit_M / (2 * M_chi) - a_eq_s * sp.sin(chi)) == 0)
print("\n  ** THE CRITERION, IN THE CORPUS'S OWN UNITS: **")
print("        the obstruction survives  <=>  r_inner = Q^2/2M  >  a_eq sin chi .")
print("  The Reissner--Nordstroem inner-horizon radius against the progenitor's")
print("  matter-radiation equality radius.  ** Both are lengths the corpus has already. **")

# ---------------------------------------------------------------------------------
print("\nPART 9 -- SCORING IT ON THE PROGENITOR, ON BOTH CHARGE READINGS AND BOTH MASSES.")
print("-" * 100)
G, c = 6.67430e-11, 2.99792458e8
Msun, Mpc = 1.98892e30, 3.0856775814913673e22
lP, e_C, eps0, m_p = 1.616255e-35, 1.602176634e-19, 8.8541878128e-12, 1.67262192e-27
gm = lambda kg: G * kg / c ** 2
gq = lambda C_: np.sqrt(G / (4 * np.pi * eps0 * c ** 4)) * C_

a_eq = 1.49 * Mpc
print(f"  a_eq = 1.49 Mpc = {a_eq:.4e} m        (P16 sec:interior, determined not bounded)")

rows = []
for mlabel, Mkg in (("THE_REGISTER   M = 2.33e23 Msun", 2.33e23 * Msun),
                    ("P16 sec:interior M = 4.3e52 kg ", 4.3e52)):
    M = gm(Mkg)
    A_v, B_v = 2 * M, 2 * M * a_eq
    QcritM = np.sqrt(2 * a_eq / M)
    print(f"\n  {mlabel}:  M = {M:.4e} m,  A = {A_v:.4e} m,  B = A a_eq = {B_v:.4e} m^2")
    print(f"     threshold at the edge (sin chi = 1):  (Q/M)_crit = sqrt(2 a_eq / M) = {QcritM:.4e}")
    for rlabel, Q_C in (("intensive  (one e)", e_C),
                        ("extensive  (1e-21 e per baryon, 1e80 baryons)", 1e-21 * e_C * 1e80)):
        Qg = gq(Q_C)
        r_in = Qg ** 2 / (2 * M)
        print(f"     {rlabel:<46s} Q/M = {Qg / M:.3e}   r_inner = {r_in:.3e} m")
        print(f"       {'':<46s} r_inner / a_eq = {r_in / a_eq:.3e}"
              f"   -> shortfall {np.sqrt(B_v) / Qg:.3e} in Q, {B_v / Qg ** 2:.3e} in Q^2")
        rows.append((mlabel, rlabel, r_in / a_eq))

check("the corpus's own r_inner figures are reproduced (2.8e19 m extensive, 2.8e-99 m "
      "intensive, on M = 2.33e23 Msun with 1e80 baryons)",
      abs(gq(1e-21 * e_C * 1e80) ** 2 / (2 * gm(2.33e23 * Msun)) / 2.8e19 - 1) < 0.05 and
      abs(gq(e_C) ** 2 / (2 * gm(2.33e23 * Msun)) / 2.8e-99 - 1) < 0.05)
check("EVERY (mass, charge-reading) pair falls BELOW the threshold, so the verdict does not "
      "depend on which reading or which mass is right",
      all(v < 1.0 for _, _, v in rows), f"max r_inner/a_eq = {max(v for _, _, v in rows):.3e}")
check("the extensive reading -- the row's own worst case -- falls short by a factor of order "
      "40 in Q, not by orders of magnitude, so the margin is real but not extravagant",
      10 < np.sqrt(2 * gm(2.33e23 * Msun) * a_eq) / gq(1e-21 * e_C * 1e80) < 100,
      f"{np.sqrt(2 * gm(2.33e23 * Msun) * a_eq) / gq(1e-21 * e_C * 1e80):.1f}")

# ---------------------------------------------------------------------------------
print("\n" + "=" * 100)
print("THE PHYSICAL READING, WHICH IS WHAT THE ORDER ASKED FOR LAST.")
print("=" * 100)
print("""
  ** THE FOUR LINES ARE CORRECT AND THE CONCLUSION DRAWN FROM THEM IS NOT THE ONE TO LAND. **

  1. The algebra is exact, the Misner--Sharp identity is right, and p = 1 is right -- ALONG A
     COMOVING SHELL.  Read as a spatial profile at fixed time the same formula gives m ~ r^3,
     which is only centre regularity.  The row's wording points at the second and the
     derivation takes the first; the first is the one PO-25 needs, and the row should say so.

  2. The competition really is scale-free in R, and for a good reason the routed line does not
     give: Gauss's law pins the charge term at exactly R^-2 and the radiation's equation of
     state pins its term at exactly R^-2, neither by way of the background.  That is what
     makes the criterion a comparison of two CONSTANTS rather than a limit that could go
     either way, and it survives charge and survives a non-uniform dust profile.

  3. ** The dust does not drop out. **  It drops out only while A and B are independent, and
     the corpus determines B = A a_eq.  The criterion is r_inner > a_eq sin chi: the
     Reissner--Nordstroem inner-horizon radius against the progenitor's equality radius.

  4. ** On the corpus's own progenitor the obstruction is destroyed, on BOTH charge readings. **
     Extensive: r_inner = 2.8e19 m against a_eq = 4.6e22 m, short by a factor 1.6e3 in Q^2.
     Intensive: short by 1.7e121.  So PO-25 decouples from the datum fork exactly as r6405's
     strong-cosmic-censorship computation did -- and this time the decoupling ANSWERS the
     question rather than bounding it.

  5. ** And it is a condition on the progenitor, not a theorem -- which is what the routed
     reading anticipated, now with a number on it. **  The threshold is a charge-to-mass ratio,
     (Q/M)_crit = sqrt(2 a_eq / M) = 1.6e-2 on the register's mass: a progenitor within two
     orders of extremality WOULD keep the obstruction.  The corpus's progenitor is 40 times
     below that on the most generous charge reading it carries.

  6. ** But the obstruction could never have been TOTAL, and that is the part the row must
     change whatever else it says. **  Q(chi)^2 / (B sin^4 chi) ~ chi^2 at the centre for any
     finite comoving charge density, so a central core always reaches R = 0.  At Q_tot^2 = 100 B
     the core still carries a per cent of the dust; at the corpus's charge it is the whole ball.
     `P03` sec:charge's "at any Q > 0 the sign at the origin has switched" is a statement about
     a STATIONARY f with M constant, and dynamically it fails at the centre for every Q.

  ** WHAT IS STILL NOT DELIVERED, AND IT IS THE SAME CLAUSE r6405 LEFT. **  That the charge term
  does not stop the collapse is not that a spacelike r = 0 forms.  The differential bounce this
  criterion predicts for a supercritical charge produces shell crossings, and what the interior
  does behind the first one is a numerical-relativity question this probe does not touch.
""")

print("=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED -> " + "; ".join(FAILS))
    raise SystemExit(1)
print("GATES: ALL PASS.")
print("""
ESTABLISHED: the routed derivation's algebra is exact and p = 1 holds along a comoving shell,
charge-blind and profile-blind at leading order; the r -> 0 limit it takes is the comoving one
and must be said so; "the dust drops out" is false once P16's determination B = A a_eq is used,
and the criterion in corpus units is r_inner = Q^2/2M > a_eq sin chi; the obstruction is
destroyed on the corpus's progenitor on BOTH charge readings, short of threshold by 1.6e3 in
Q^2 (extensive) and 1.7e121 (intensive); and it can never be total, because the criterion
degenerates as chi^2 at the centre and a central core reaches R = 0 for any charge.
NOT CLAIMED: that a spacelike r = 0 forms; that the charged interior is P16's homogeneous
ball; any value for the progenitor's charge.
""")
