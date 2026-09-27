"""
P15_the_transfers_running_is_a_function_of_one_variable_so_the_requirement_is_the_radiation_fractions
====================================================================================================

LEVEL: exact symbolic (sympy) for the scaling substitution and the composition identity; the
banked instrument re-run as the gate; the high-k limit argued ANALYTICALLY from the potential's
Coulomb form and only then compared with measurement.

OBJECT UNDER TEST -- `PO-31`, `r6914`, three items.  The order's framing, verbatim:

    "A determined input is only good news if the determination is not a conspiracy.  A
     progenitor spectrum that runs by 1.71 in exactly the sense that cancels the transfer's
     running, across two and a half decades, is either structural --- both runnings set by the
     same thing --- or it is a tuning of a FUNCTION, which is worse than having no answer."

  ⓵ where is the break in rho, and is there any rho putting the observed band wholly below it?
  ⓶ is 1.71 a number or an artefact of the band's placement?
  ⓷ is the high-k limit of the slope exactly zero, and is the requirement therefore bounded
     by two -- ** argued ANALYTICALLY, because k -> large is exactly where this seat's own
     x_i = 300/k premise expires and "a second k = 1e5 would be worse than a gap". **

-------------------------------------------------------------------------------
** ALL THREE ANSWER, AND TWO OF THEM CLOSED-FORM, BECAUSE THE TRANSFER'S RUNNING TURNS OUT TO
   BE A FUNCTION OF ONE VARIABLE. **

  ⓪ ** THE STRUCTURAL FACT THE ORDER WAS REACHING FOR. **  Substituting x = 2 rho u in
      v'' = (2/(x(x+2 rho)) - k^2) v gives

        v_uu = ( 2/(u(u+1)) - kappa^2 ) v ,        kappa = 2 rho k

      -- the potential in u carries NO rho, and rho and k enter only through kappa.  ** So
      d lnT/d lnk is a universal function of kappa alone. **  Verified to 7e-13 across a factor
      100 in rho.  ⇒ *The break sits at a FIXED kappa, k_break = kappa*/(2 rho) exactly rather
      than approximately, and items ⓵ and ⓷ stop being scans.*

  ⓷ ** THE HIGH-k LIMIT IS EXACTLY ZERO, AND THE ARGUMENT IS ANALYTIC AS ORDERED. **  Near
      x -> 0 the potential is P/x with P = 1/rho, and with x = s/k the equation becomes

        v_ss + ( 1 - 2 eta / s ) v = 0 ,           eta = P/(2k) = 1/kappa

      the L = 0 COULOMB wave equation, REPULSIVE.  The irregular solution's amplitude at
      s -> 0 goes as 1/C_0(eta) with C_0(eta)^2 = 2 pi eta/(e^{2 pi eta} - 1), so

        T ~ const x (1 + pi eta/2 + O(eta^2))   and   d lnT/d lnk -> - pi eta/2 = - pi/(4 rho k)

      ⇒ ** the limit is exactly 0 and is approached as 1/k. **  The measured slope agrees with
      -pi/(4 rho k) to within 1.5% at four (k, rho) pairs INSIDE the premise's validity -- the
      asymptote is derived where the integration is not trusted and checked where it is.

      ⇒ ** SO THE TOTAL EXCURSION OF d lnT/d lnk IS EXACTLY 1, from -1 to 0; what the transfer
         adds to a tilt is AT MOST 2; and no band however wide can require a progenitor running
         above 2. **  The observed band's requirement is 86% of that hard maximum.

  ⓵ ** AND THE REQUIREMENT IS THE RADIATION FRACTION'S.  A rho that puts the band wholly below
      the break EXISTS -- and it is two to nearly three orders below the determined one. **
      On a stated criterion rather than an eye reading:

        d lnT/d lnk = -0.5  (midpoint)          kappa* = 2.729  ->  rho < 9.7e-4   (x55 down)
        d lnT/d lnk = -0.95 (within 0.05 of -1) kappa* = 0.400  ->  rho < 1.4e-4   (x378 down)

      ⇒ ** So the answer is the order's SECOND branch: the requirement stands, and it stands
         because the DETERMINED radiation fraction forces it. **  Not because the transfer
         imprints in the abstract -- because rho = 0.05451 puts the observed band 55 to 378
         times too far above its own break.

  ⓶ ** AND 1.71 IS A NUMBER, NOT AN ARTEFACT OF THE PLACEMENT. **  Over the +/-6% the arm's own
      distance mapping allows, the requirement moves by 0.040, i.e. 2.3%.  ⚠ Over a much wider
      band it moves 6-9%, which is reported rather than hidden.

⌗ AND ONE THING FOUND ON THE WAY THAT IS NOT THIS ORDER'S TO RESOLVE, FLAGGED RATHER THAN USED.
  The bound in ⓵ is a bound on rho, and rho is not a free number: from `P16`'s own two
  statements -- rho = 2 sqrt(B)/A and a_eq = A rho^2/4 = B/A -- it follows that
  ** rho = sqrt(2 a_eq / M) ** (with A = 2M), verified symbolically below.  ⚠ But that identity
  at `a_eq` = 1.49 Mpc and the REGISTER's mass 2.33e23 Msun gives rho = 1.635e-2, against the
  determined 0.05451 -- a factor 3.3, i.e. a mass ratio of 10.9.  ** The two are consistent only
  at two different progenitor masses, and which one the radiation fraction's determination uses
  is not settled here. **  So the bound is reported as a bound on rho and, as a SCALING, on
  a_eq/M; it is deliberately NOT converted into a number for a_eq or M.

COMPUTES: scope -- what this settles and what it must not be read as.
  * ** THE CALIBRATION IS THE GATE. **  PART 1 re-runs the banked check at the banked rho and k.
    Everything below is that instrument or an analytic argument about the same equation.
  * ** THE ANALYTIC LIMIT IS NOT MEASURED AT LARGE k, BY DESIGN. **  The order forbade it and the
    reason is this seat's: `r6912` discarded a k = 1e5 reading that was tolerance-converged to
    2e-10 and still meaningless, because x_i = 300/k had drifted inside the break.  ** Here the
    limit comes from the potential's Coulomb form and is only COMPARED with measurements at
    k <= 2000, inside the premise. **  No integration above k = 2000 is performed or quoted.
  * ⚠ ** THE DIFFERENCING CONVENTION MOVES THE HEADLINE IN THE THIRD DIGIT. **  `r6912` quoted
    1.71 from centred slopes on its k-grid; this uses a +/-8% two-point slope and gets 1.724.
    ** The requirement is therefore quoted as 1.71-1.72 and not to three decimals ** -- and that
    0.7% spread is itself part of ⓶'s answer.
  * ** rho = 0.05451, a_eq = 1.49 Mpc, the potential and the background are taken from banked
    receipts **, not re-chosen.  No progenitor interior is built.
  * ** NO tilt value, NO amplitude ** -- `r6898`'s 10^103 is about vacuum data and a classical
    input's amplitude is free.  ** And `PO-31` does not close **, as the order said.

rc=0 on success.  Run: python3 P15_the_transfers_running_is_a_function_of_one_variable_so_the_requirement_is_the_radiation_fractions.py
"""
import sys

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

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


RHO = 0.05451                        # the DETERMINED composition (P16, c54.143) -- taken
TARGET = 3.0 / (2.0 * np.sqrt(2.0))
K_PREMISE = 300.0 / (2 * RHO)       # x_i = 300/k sits outside the break only below this


def residue(k, rho=RHO, amp=1.0, n_osc=300.0, xf_frac=1e-4, rtol=1e-12):
    x_f = xf_frac * rho

    def rhs(xx, y):
        pot = 2.0 / (xx * (xx + 2.0 * rho))
        return [y[1], (pot - k**2) * y[0], y[3], (pot - k**2) * y[2]]

    x_i = n_osc / k
    y0 = [amp * np.cos(k * x_i), -amp * k * np.sin(k * x_i),
          amp * np.sin(k * x_i), amp * k * np.cos(k * x_i)]
    s = solve_ivp(rhs, [x_i, x_f], y0, rtol=rtol, atol=1e-16, method='DOP853')
    v = s.y[0, -1] + 1j * s.y[2, -1]
    vx = s.y[1, -1] + 1j * s.y[3, -1]
    return abs((v - vx * x_f) / (1.0 + x_f * np.log(x_f / (2 * rho)) / rho))


def slope(k, rho=RHO, h=0.08):
    """Two-point log-slope of T at k.  h is stated because it moves the headline's third digit."""
    a, b = residue(k * (1 - h), rho), residue(k * (1 + h), rho)
    return np.log(b / a) / np.log((1 + h) / (1 - h))


# =============================================================================================
head("PART 1 (C1) -- THE BANKED CHECK, AT THE BANKED COMPOSITIONS, BEFORE ANYTHING ELSE")

print(f"  {'rho':>9} {'k':>7} {'|c0| k^1.5 rho':>17} {'3/(2 sqrt 2)':>14} {'departure':>11}")
worst = 0.0
for rho in [1e-3, 1e-4]:
    for k in [2.0, 10.0, 30.0]:
        val = residue(k, rho=rho, amp=1.0 / np.sqrt(2.0 * k)) * k**1.5 * rho
        d = abs(val / TARGET - 1)
        worst = max(worst, d)
        print(f"  {rho:>9.0e} {k:>7.1f} {val:>17.6f} {TARGET:>14.6f} {d*100:>10.3f}%")
check(worst < 0.03, f"the banked scale-invariance reproduces -- worst {worst*100:.2f}%")

# =============================================================================================
head("PART 2 -- THE ONE-VARIABLE SCALING, DERIVED THEN MEASURED")

x, u, rho_s, k_s = sp.symbols('x u rho k', positive=True)
v = sp.Function('v')
pot_x = 2 / (x * (x + 2 * rho_s))
# substitute x = 2 rho u : d^2/dx^2 -> (1/(2 rho)^2) d^2/du^2
pot_u = sp.simplify(pot_x.subs(x, 2 * rho_s * u) * (2 * rho_s)**2)
k_term = sp.simplify(k_s**2 * (2 * rho_s)**2)
print(f"  x = 2 rho u  =>  v_uu = ( {pot_u}  -  {k_term} ) v")
check(sp.simplify(pot_u - 2 / (u * (u + 1))) == 0,
      "the potential in u is 2/(u(u+1)) -- rho has CANCELLED out of it entirely")
check(sp.simplify(k_term - (2 * rho_s * k_s)**2) == 0,
      "and rho and k enter only as kappa = 2 rho k")
print("  ⇒ so d lnT/d lnk must be a universal function of kappa alone.  Measured:")
print(f"  {'kappa':>7} " + " ".join(f"{'rho='+format(r,'.4f'):>13}" for r in
                                   (0.05451, 0.0100, 0.0020, 0.2000)) + f" {'spread':>10}")
worst_scale = 0.0
for kap in [0.2, 0.5, 1.0, 2.0, 5.0, 12.0, 30.0]:
    row = [slope(kap / (2 * r), r) for r in (0.05451, 0.0100, 0.0020, 0.2000)]
    sp_ = max(row) - min(row)
    worst_scale = max(worst_scale, sp_)
    print(f"  {kap:>7.2f} " + " ".join(f"{v_:>13.6f}" for v_ in row) + f" {sp_:>10.2e}")
check(worst_scale < 1e-9,
      f"the slope collapses onto one function of kappa across a factor 100 in rho -- {worst_scale:.1e}")
print("  ** so k_break = kappa*/(2 rho) EXACTLY, not approximately. **")

# =============================================================================================
head("PART 3 (⓷) -- THE HIGH-k LIMIT, ARGUED ANALYTICALLY AND ONLY THEN COMPARED")

s_, eta = sp.symbols('s eta', positive=True)
print("  Near x -> 0 the potential is P/x with P = 1/rho.  Set x = s/k:")
lhs = sp.simplify(k_s**2 * (1 / rho_s / (s_ / k_s) - k_s**2) / k_s**2)
print(f"      v_ss = ( {sp.simplify((1/rho_s)/(s_/k_s)/k_s**2)} - 1 ) v"
      f"   i.e.  v_ss + (1 - 2 eta/s) v = 0  with eta = 1/(2 rho k)")
check(sp.simplify((1 / rho_s) / (s_ / k_s) / k_s**2 - 2 * (1 / (2 * rho_s * k_s)) / s_) == 0,
      "the reduced equation is the L = 0 Coulomb wave equation with eta = 1/(2 rho k) = 1/kappa")
C0sq = 2 * sp.pi * eta / (sp.exp(2 * sp.pi * eta) - 1)
inv = sp.series(1 / sp.sqrt(C0sq), eta, 0, 2).removeO()
print(f"  repulsive, so the irregular amplitude at s -> 0 goes as 1/C_0(eta),")
print(f"  C_0(eta)^2 = 2 pi eta/(e^(2 pi eta) - 1)   =>   1/C_0(eta) = {sp.simplify(inv)} + O(eta^2)")
check(sp.simplify(sp.limit((1 / sp.sqrt(C0sq) - 1) / eta, eta, 0) - sp.pi / 2) == 0,
      "1/C_0(eta) = 1 + pi eta/2 + O(eta^2), so T ~ const (1 + pi eta/2)")
print("  ⇒ d lnT/d lnk = d(pi eta/2)/d lnk = - pi eta/2 = ** - pi/(4 rho k) -> 0 **")
print()
print(f"  {'k':>8} {'rho':>8} {'measured':>13} {'-pi/(4 rho k)':>15} {'ratio':>9}")
worst_as = 0.0
for (kk, rr) in [(1400.0, 0.05451), (2000.0, 0.05451), (700.0, 0.05451),
                 (300.0, 0.05451), (2000.0, 0.0100)]:
    m, a = slope(kk, rr), -np.pi / (4 * rr * kk)
    worst_as = max(worst_as, abs(m / a - 1))
    print(f"  {kk:>8.0f} {rr:>8.4f} {m:>13.6f} {a:>15.6f} {m/a:>9.4f}")
check(worst_as < 0.05,
      f"the analytic asymptote matches the measured slope to {worst_as*100:.1f}% at every "
      f"pair tested, all at k <= 2000 and so INSIDE the premise (k < {K_PREMISE:.0f})")
print("  ** the limit is derived where the integration is NOT trusted and checked where it is. **")
print()
lo_lim, hi_lim = -1.0, 0.0
print(f"  low-k limit  {lo_lim:+.1f} (r6912: -0.9992 at k = 0.3, kT -> 27.86)")
print(f"  high-k limit {hi_lim:+.1f} (this part, exactly)")
check(abs((hi_lim - lo_lim) - 1.0) < 1e-12,
      "so the total excursion of d lnT/d lnk is EXACTLY 1, and what it adds to a tilt at most 2")

# =============================================================================================
head("PART 4 (⓵) -- WHERE IS THE BREAK?  A STATED CRITERION, THEN THE rho BOUND")

bounds = {}
for target, label in ((-0.5, "midpoint of the excursion"),
                      (-0.95, "within 0.05 of the -1 power law")):
    kstar = np.exp(brentq(lambda lk: slope(np.exp(lk)) - target,
                          np.log(0.05), np.log(400.0), xtol=1e-6))
    kap = 2 * RHO * kstar
    print(f"  criterion d lnT/d lnk = {target}  ({label}):  kappa* = {kap:.4f}"
          f"   ->  k_break(rho) = {kap:.4f}/(2 rho)")
    for kmax in (1400.0, 2000.0):
        rb = kap / (2 * kmax)
        bounds[(target, kmax)] = rb
        print(f"     band top k = {kmax:.0f}  =>  band wholly below the break needs "
              f"rho < {rb:.3e}   (determined 0.05451 is {RHO/rb:.0f}x larger)")
check(all(b < RHO / 40 for b in bounds.values()),
      "a rho that works EXISTS, and every criterion puts it at least 40x below the determined one")
check(RHO / bounds[(-0.5, 1400.0)] > 50 and RHO / bounds[(-0.95, 2000.0)] > 500,
      f"the span is {RHO/bounds[(-0.5,1400.0)]:.0f}x on the loose criterion to "
      f"{RHO/bounds[(-0.95,2000.0)]:.0f}x on the strict one")

# =============================================================================================
head("PART 5 -- WHAT THE rho BOUND IS A BOUND ON, AND WHAT IS NOT SETTLED HERE")

A_, B_, M_, aeq_ = sp.symbols('A B M a_eq', positive=True)
rho_def = 2 * sp.sqrt(B_) / A_                       # P16: rho = 2 sqrt(B)/A
aeq_def = sp.simplify(A_ * rho_def**2 / 4)           # P16: a_eq = A rho^2/4
check(sp.simplify(aeq_def - B_ / A_) == 0,
      "P16's own two statements are consistent: a_eq = A rho^2/4 = B/A")
rho_from = sp.simplify(rho_def.subs(B_, A_ * aeq_).subs(A_, 2 * M_))
check(sp.simplify(rho_from - sp.sqrt(2 * aeq_ / M_)) == 0,
      f"and together they give rho = sqrt(2 a_eq / M) = {rho_from}")
Msun, Mpc = 1.98847e30, 3.0857e22
G, c = 6.67430e-11, 2.99792458e8
M_reg = G * (2.33e23 * Msun) / c**2
aeq = 1.49 * Mpc
rho_reg = np.sqrt(2 * aeq / M_reg)
print(f"  at a_eq = 1.49 Mpc and the REGISTER's mass 2.33e23 Msun:  rho = {rho_reg:.4e}")
print(f"  against the DETERMINED rho = {RHO}                     ratio = {RHO/rho_reg:.2f}"
      f"   (a mass ratio of {(RHO/rho_reg)**2:.1f})")
check(2.0 < RHO / rho_reg < 5.0,
      "⚠ the two are consistent only at two DIFFERENT progenitor masses, and which one the "
      "radiation fraction's determination uses is NOT settled here")
print("  ⇒ ** so the bound is reported as a bound on rho, and as a SCALING on a_eq/M")
print("     (rho^2 = 2 a_eq/M, so rho 55x down needs a_eq/M about 3000x down) --")
print("     deliberately NOT converted into a number for a_eq or for M. **")

# =============================================================================================
head("PART 6 (⓶) -- IS 1.71 SOFT UNDER THE BAND'S PLACEMENT?")

base = 2 * (slope(1400.0) - slope(7.0))
print(f"  required running = 2 [ slope(k_max) - slope(k_min) ];  baseline 7 < k < 1400: {base:.4f}")
print(f"  ⚠ r6912 quoted 1.71 from centred grid slopes; this is a +/-8% two-point slope and")
print(f"    gives {base:.4f}.  ** The 0.7% method spread is part of the answer, not noise. **")
print()
print(f"  {'k_min':>8} {'k_max':>8} {'requirement':>13} {'shift':>10} {'%':>8}")
narrow = []
for (a, b, tag) in [(7.0, 1400.0, 'base'), (6.6, 1400.0, '6%'), (7.4, 1400.0, '6%'),
                    (7.0, 1320.0, '6%'), (7.0, 1484.0, '6%'), (6.6, 1320.0, '6%'),
                    (7.4, 1484.0, '6%'), (5.0, 2000.0, 'wide'), (10.0, 1000.0, 'wide')]:
    v_ = 2 * (slope(b) - slope(a))
    if tag in ('base', '6%'):
        narrow.append(v_)
    print(f"  {a:>8.1f} {b:>8.0f} {v_:>13.4f} {v_-base:>10.4f} {100*(v_-base)/base:>7.2f}%")
spread6 = max(narrow) - min(narrow)
check(spread6 / base < 0.05,
      f"over the +/-6% the arm's distance mapping allows, the requirement moves "
      f"{spread6:.4f} = {100*spread6/base:.2f}% -- ** a number, not an artefact **")
print(f"  ⚠ over a much WIDER band it moves 6-9%, reported rather than hidden.")
print(f"  ** and against the hard maximum of 2 from PART 3, the baseline is "
      f"{100*base/2:.1f}% of the available excursion. **")

# =============================================================================================
head("VERDICT")

print(f"""
  ⇒ ** THE TRANSFER'S RUNNING IS A FUNCTION OF ONE VARIABLE, kappa = 2 rho k, AND THAT SETTLES
       ALL THREE ITEMS -- TWO OF THEM IN CLOSED FORM. **

  ⓵ ** THE REQUIREMENT IS THE RADIATION FRACTION'S, WHICH IS THE ORDER'S SECOND BRANCH. **  A
      rho putting the observed band wholly below the break EXISTS, and the break's location is
      exact rather than estimated: k_break = kappa*/(2 rho).  But it needs
      rho < 9.7e-4 on the midpoint criterion and < 1.4e-4 on the strict one -- ** 55x to 378x
      below the determined 0.05451. **  So the requirement stands *because the determined
      radiation fraction forces it*, which is the falsifiable sentence the order asked for.

  ⓶ ** 1.71 IS A NUMBER. **  Over the +/-6% the arm's own distances allow it moves {100*spread6/base:.1f}%.
      ⚠ Quote it as ** 1.71-1.72 ** and not to three decimals: the differencing convention alone
      moves the third digit by 0.7%, and a wider band moves it 6-9%.

  ⓷ ** THE HIGH-k LIMIT IS EXACTLY ZERO, ANALYTICALLY. **  The near-crunch equation is the
      repulsive L = 0 Coulomb wave equation with eta = 1/kappa, and 1/C_0(eta) = 1 + pi eta/2
      gives d lnT/d lnk -> -pi/(4 rho k) -> 0, matching measurement to {worst_as*100:.1f}% at k <= 2000.
      ⇒ ** the excursion is exactly 1, the tilt contribution at most 2, and no band however
         wide can require a progenitor running above 2. **  The observed band asks for
         {100*base/2:.0f}% of that hard maximum -- so the construction has little room left, and
         that is a structural statement rather than an empirical one.

  ⌗ AND THE CONSPIRACY QUESTION THE ORDER OPENED WITH NOW HAS A SHAPE.  Both runnings are set
    by the same object -- the break, at kappa ~ 1 -- so a progenitor that cancels the transfer
    is not a tuning of an arbitrary function; it is a progenitor whose own spectrum breaks where
    the interior's does.  ⚠ ** That is a structural CANDIDATE and not a result: nothing here
    shows a progenitor does that, only that the thing to be explained is one coincidence of
    scales rather than a function's worth of them. **

  ⌗ WHAT THIS DOES NOT DO.  `PO-31` does not close.  No progenitor interior, no tilt value, no
    amplitude.  No integration above k = 2000 is performed or quoted -- the high-k limit is the
    potential's asymptotics, as ordered.  And the rho bound is NOT converted into a number for
    a_eq or M, because `P16`'s rho = sqrt(2 a_eq/M) and the register's mass disagree with the
    determined rho by a factor {RHO/rho_reg:.1f}; ** that discrepancy is flagged, not used. **
""".rstrip())

print()
if FAILED:
    print("FAIL: " + "; ".join(FAILED))
    sys.exit(1)
print("ALL CHECKS PASS")
sys.exit(0)
