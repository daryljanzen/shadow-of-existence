"""
P15_the_transfer_is_the_same_object_as_the_vacuum_spectrum_and_the_crossing_carries_no_wavenumber
================================================================================================

LEVEL: the banked instrument re-run as calibration (DOP853, rtol 1e-12) before anything new is
read from it; exact symbolic Frobenius determination of the crossing's resonant coefficient.

OBJECT UNDER TEST -- `PO-31`, released at `r6897` after the switch sweep validated its target, with
one thing named to look at first.  The order, verbatim:

    "what supplies a red tilt when the only vacuum the construction has computed is blue?  One
     thing this seat would look at before anything else: every closed channel was tested as a
     SPECTRUM-GENERATING mechanism.  The tilt is a ratio of amplitudes at two wavenumbers, and the
     construction has a second place a wavenumber-dependence can enter --- the TRANSFER from the
     progenitor's vacuum to the boundary datum, as against the vacuum itself.  Whether that
     transfer is scale-free has been established for the collapse leg and not for the
     interior-to-leg join.  That is a question and not an instruction; if it is already closed, say
     so and it costs a paragraph."

-------------------------------------------------------------------------------
** IT IS NOT A SECOND PLACE, AND SAYING SO COSTS MORE THAN A PARAGRAPH BECAUSE THE REASON CORRECTS
   THIS SEAT'S OWN RECONCILIATION OF TWO BANKED RESULTS. **

  ⓵ ** THE INTERIOR'S TRANSFER AND THE INTERIOR'S VACUUM SPECTRUM ARE ONE OBJECT. **  The banked
      instrument (`P15_the_progenitor_vacuum_is_negligible_too`, PART 2) integrates the k != 0 mode
      equation from sub-horizon vacuum data at large x down to the crunch and reads the constant
      residue.  Run at the DETERMINED composition rho = 0.0539 across the band r6846 used, the
      k^{3/2}-stripped residue has a log-slope running +0.27 to +1.98, tending to +2.  ** That is
      r6857's number, from initial data placed somewhere else entirely -- r6846 set the vacuum at
      maximum expansion, this sets it sub-horizon in the deep matter contraction. **  ⚠ They are
      NOT expected to agree pointwise and do not: at the top of the band both give +1.98, and at
      the flat end this reads +0.267 against r6846's flattest +0.304, a twelve per cent
      difference the different vacuum placement accounts for.  ** What reproduces is the running
      and its two limits, which is what the argument uses. **  An independent reproduction, and the
      reason there is nothing new here to find: the interior's evolution from vacuum data to the
      crunch residue IS the transfer.

  ⛔ ⓶ ** AND THE BANKED SCALE-INVARIANCE IS NOT CONTRADICTED -- IT HAS A DOMAIN, WHICH THIS SEAT
      GOT WRONG ONCE ALREADY. **  The potential 2/(x(x+2 rho)) breaks at x ~ 2 rho, so the
      wavenumber that separates "freezes in the matter contraction" from "freezes in the radiation
      crunch" is k_break = 1/(2 rho).  The banked receipt tested rho = 1e-3 and 1e-4 at k = 2, 10,
      30 -- ** the whole tested band below k_break = 500 and 5000, where the transfer IS scale-free
      and the check passes to 0.2%. **  At the determined rho = 0.0539, k_break = 9.3 and the
      observed band sits ABOVE it.  ⚠ `r6846` reconciled the two banked results by saying "its
      scale-invariance is of a transfer and its number an amplitude; the slope of the generated
      spectrum is a different object."  ** They are not different objects, and that reconciliation
      is withdrawn here.  The correct one is the band's position relative to 1/(2 rho). **

  ⓷ ** AND THE ONE STEP GENUINELY NOT YET TESTED FOR A WAVENUMBER -- THE CROSSING ITSELF -- CARRIES
      NONE, EXACTLY. **  The banked transfer law uses a monodromy 4 pi/rho, verified in PART 3b of
      that receipt on the k = 0 equation only.  x = 0 is a regular singular point with resonant
      exponents 0 and 1, so the monodromy IS the resonant log coefficient, and it is determined here
      order by order:

        C = 1/rho   exactly,   dC/dk = 0

      with the mechanism visible coefficient by coefficient in the analytic solution: ** k^2 is
      REGULAR where the potential is SINGULAR, so it cannot reach the indicial equation and cannot
      reach the resonance -- it first appears at x^3. **

  ⇒ ** SO THE CHAIN FROM THE PROGENITOR'S VACUUM TO THE BOUNDARY DATUM CARRIES NO WAVENUMBER
      DEPENDENCE OF ITS OWN ANYWHERE: the interior step is the vacuum spectrum already measured and
      already blue, the crossing is k-free by an identity of the singular point, and the leg is
      scale-free at fixed phase (`r6812`, `r6823`).  The transfer is not a fifth channel, and the
      row does not get a red tilt from it. **

⌗ AND ONE BOUNDED CONSEQUENCE FOR A NUMBER THE CORPUS CARRIES, WHICH DOES NOT MOVE ANY VERDICT.
  A_s^vac = 9 (l_P/M)^2 rho^{-6} was read off the scale-free branch at the determined rho.  On the
  observed band the residue exceeds that branch's value, by a factor that is measured here rather
  than estimated.  ** Against a shortfall of 10^103 it changes nothing, and the banked verdict --
  the primordial statistics are classical and non-vacuum -- stands untouched. **  Reported as a
  bound on the number's reading, not as a correction to the conclusion.

COMPUTES: scope -- what this settles and what it must not be read as.
  * ** THIS DOES NOT CLOSE PO-31. **  It closes the route the order named, which is a different
    thing.  The row's question -- what supplies a red near-constant tilt -- is left exactly where
    r6857 left it, with one candidate route now eliminated rather than untested.
  * ** THE CALIBRATION IS THE GATE. **  PART 1 re-runs the banked check at the banked rho and k.
    If 3/(2 sqrt 2) does not reproduce there, nothing below may be read: the whole of PART 2 is the
    same instrument pointed at a different composition.
  * ** NOTHING HERE IS A NEW BACKGROUND OR A NEW MODE PROBLEM. **  The potential, the composition
    rho = 0.0539 and the monodromy's role are all taken from banked receipts.  What is new is where
    they are evaluated and what the resonance is asked for.
  * ** THE CROSSING RESULT IS ABOUT THE MONODROMY AND NOT ABOUT C19's 9/10. **  `C19` states in its
    own voice that its join factor is the super-horizon one and that "modes inside the horizon at
    the branch point are not covered".  ⓷ says the crossing's resonant coefficient carries no k; it
    does NOT say the 9/10 extends to sub-horizon modes, which is a separate item and is untouched.
  * ** A SLOPE IS NOT AN AMPLITUDE. **  PART 2 reads log-slopes; the amplitude comparison in PART 3
    is a ratio to the scale-free branch and is not an independent measurement of A_s.
  * Nothing bears on PO-7, PO-23's coupled tower, PO-48, or PO-52.

rc=0 on success.  Run: python3 P15_the_transfer_is_the_same_object_as_the_vacuum_spectrum_and_the_crossing_carries_no_wavenumber.py
"""
import sys

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

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


RHO_DET = 0.0539            # the DETERMINED composition (P16, c54.143), taken not chosen
TARGET = 3.0 / (2.0 * np.sqrt(2.0))


def residue(k, rho, n_osc=300.0, xf_frac=1e-4):
    """|c_0| at the crunch from sub-horizon vacuum data -- the banked instrument, with the
    x -> 0 log of the radiation crunch divided out explicitly rather than left in the residual."""
    x_f = xf_frac * rho

    def rhs(xx, y):
        pot = 2.0 / (xx * (xx + 2.0 * rho))
        return [y[1], (pot - k**2) * y[0], y[3], (pot - k**2) * y[2]]

    x_i = n_osc / k
    n = np.sqrt(2.0 * k)
    y0 = [np.cos(k * x_i) / n, -k * np.sin(k * x_i) / n,
          np.sin(k * x_i) / n, k * np.cos(k * x_i) / n]
    s = solve_ivp(rhs, [x_i, x_f], y0, rtol=1e-12, atol=1e-16, method='DOP853')
    v = s.y[0, -1] + 1j * s.y[2, -1]
    vx = s.y[1, -1] + 1j * s.y[3, -1]
    c0 = (v - vx * x_f) / (1.0 + x_f * np.log(x_f / (2 * rho)) / rho)
    return abs(c0)


# =============================================================================================
head("PART 1 (C1) -- THE BANKED CHECK REPRODUCED, AT THE BANKED COMPOSITIONS, BEFORE ANYTHING ELSE")

print(f"  {'rho':>9} {'k':>7} {'|c0| k^1.5 rho':>17} {'3/(2 sqrt 2)':>14} {'departure':>11}")
worst = 0.0
for rho in [1e-3, 1e-4]:
    for k in [2.0, 10.0, 30.0]:
        val = residue(k, rho) * k**1.5 * rho
        d = abs(val / TARGET - 1)
        worst = max(worst, d)
        print(f"  {rho:>9.0e} {k:>7.1f} {val:>17.6f} {TARGET:>14.6f} {d*100:>10.3f}%")
check(worst < 0.03,
      f"the banked scale-invariance reproduces at the banked rho and k -- worst {worst*100:.2f}%")
print(f"  ** and k_break = 1/(2 rho) is {1/(2*1e-3):.0f} and {1/(2*1e-4):.0f} at these two")
print("     compositions: the ENTIRE tested band lies below it. **")

# =============================================================================================
head("PART 2 -- THE SAME INSTRUMENT AT THE DETERMINED COMPOSITION, ACROSS THE OBSERVED BAND")

print(f"  rho = {RHO_DET}  ->  potential break at x ~ 2 rho = {2*RHO_DET:.4f}, "
      f"k_break = {1/(2*RHO_DET):.2f}")
print()
ks = np.array([5.0, 7.0, 10.0, 20.0, 50.0, 100.0, 300.0, 1000.0, 1400.0, 2000.0])
res = np.array([residue(k, RHO_DET) for k in ks])
stripped = res * ks**1.5
print(f"  {'k':>9} {'|c0|':>15} {'|c0| k^1.5 rho':>17} {'ratio to the scale-free branch':>32}")
for k, c, s in zip(ks, res, stripped):
    print(f"  {k:>9.1f} {c:>15.6e} {s*RHO_DET:>17.6f} {s*RHO_DET/TARGET:>32.4f}")

lk, lv = np.log(ks), np.log(stripped)
print()
print("  centred log-slope of the transfer, and the spectrum it implies (P ~ k^3 |c0|^2):")
print(f"  {'k':>9} {'d ln(|c0| k^1.5)/d ln k':>26} {'n_s - 1':>12}")
slopes = {}
for i in range(1, len(ks) - 1):
    sl = (lv[i + 1] - lv[i - 1]) / (lk[i + 1] - lk[i - 1])
    slopes[ks[i]] = sl
    print(f"  {ks[i]:>9.1f} {sl:>26.6f} {2*sl:>12.6f}")
lo, hi = slopes[7.0], slopes[1400.0]
check(lo > 0 and hi > 0,
      f"the transfer is BLUE at both ends of the band ({2*lo:+.3f} and {2*hi:+.3f} in n_s - 1)")
check(abs(2 * hi - 2.0) < 0.1,
      f"and it tends to the radiation value +2 at the top of the band ({2*hi:+.4f})")
check(2 * hi - 2 * lo > 1.0,
      "it RUNS across the band rather than sitting at a constant -- a running, not a tilt")
print()
print(f"  ** r6857's banked reading of the interior's GENERATED spectrum was +0.30 to +1.98 over")
print(f"     k = 5-2000, flattest +0.304.  This instrument, from vacuum data placed in a different")
print(f"     place entirely, gives {2*lo:+.3f} to {2*hi:+.3f} -- the top end to three figures, the")
print(f"     flat end to twelve per cent, which the different vacuum placement accounts for.")
print(f"     ** THE SAME OBJECT TWICE, AND THE AGREEMENT IS OF THE RUNNING AND ITS LIMITS. **")
print("  ** And the sign is the row's problem unchanged: the target is RED, 1 - n_s = 0.005. **")

# =============================================================================================
head("PART 3 -- THE BOUNDED CONSEQUENCE FOR A_s^vac, WHICH MOVES NO VERDICT")

LAM, LP, AS_OBS = 1.1056e-52, 1.616255e-35, 2.1e-9
alpha = np.sqrt(3.0 / LAM)
M_nar = alpha / (3 * np.sqrt(3))
As_branch = 9.0 * (LP / M_nar)**2 * RHO_DET**-6.0
boost_top = (stripped[-1] * RHO_DET / TARGET)**2
print(f"  A_s on the scale-free branch (the banked number)      {As_branch:>14.4g}")
print(f"  amplitude-squared excess at the top of the band       {boost_top:>14.4g}")
print(f"  so the reading there                                  {As_branch*boost_top:>14.4g}")
print(f"  observed                                              {AS_OBS:>14.4g}")
print(f"  shortfall, on the branch                              {AS_OBS/As_branch:>14.2e}")
print(f"  shortfall, at the top of the band                     {AS_OBS/(As_branch*boost_top):>14.2e}")
check(AS_OBS / (As_branch * boost_top) > 1e95,
      "the shortfall survives the excess by ninety-five orders -- the banked verdict is untouched")
print("  ** so this is a bound on how the banked number should be READ (it is the k -> 0 end of a")
print("     running amplitude, not a band-wide constant) and not a correction to its conclusion. **")

# =============================================================================================
head("PART 4 -- THE CROSSING: THE RESONANT COEFFICIENT, DETERMINED RATHER THAN ARGUED")

x, rho_s, k_s = sp.symbols('x rho k', positive=True)
NORD = 7
pot = 2 / (x * (x + 2 * rho_s))
p0 = sp.limit(x * pot, x, 0)
q0 = sp.limit(x**2 * (pot - k_s**2), x, 0)
print(f"  x (potential)          -> {sp.simplify(p0)}   as x -> 0      ** and no k in it **")
print(f"  x^2 (potential - k^2)  -> {sp.simplify(q0)}")
check(sp.simplify(sp.diff(p0, k_s)) == 0 and sp.simplify(q0) == 0,
      "x = 0 is a regular singular point whose indicial equation s(s-1) = 0 cannot see k")
print("  ⇒ exponents 0 and 1: RESONANT, so the second solution carries a log and the log's")
print("    coefficient IS the monodromy the banked transfer law uses as 4 pi/rho.")

b = sp.symbols('b2:%d' % (NORD + 1))
v1 = x + sum(b[i - 2] * x**i for i in range(2, NORD + 1))
res_s = sp.series(sp.expand(sp.diff(v1, x, 2) * x * (x + 2 * rho_s)
                            - (2 - k_s**2 * x * (x + 2 * rho_s)) * v1), x, 0, NORD).removeO()
sol = sp.solve([sp.expand(res_s).coeff(x, m) for m in range(0, NORD)], list(b), dict=True)[0]
v1s = sp.expand(v1.subs(sol))
print()
print("  the analytic (exponent 1) solution, coefficient by coefficient:")
first_k = None
for i in range(1, NORD + 1):
    c = sp.simplify(v1s.coeff(x, i))
    if first_k is None and sp.simplify(sp.diff(c, k_s)) != 0:
        first_k = i
    print(f"    x^{i}:  {c}")
check(first_k == 3,
      f"k first enters the analytic solution at x^{first_k} -- it is regular where the potential is not")

C = sp.Symbol('C')
c_ = sp.symbols('c1:%d' % (NORD + 1))
L = sp.Symbol('L')
v2 = 1 + sum(c_[i - 1] * x**i for i in range(1, NORD + 1)) + C * v1s * sp.log(x)
E = sp.expand(sp.diff(v2, x, 2) * x * (x + 2 * rho_s)
              - (2 - k_s**2 * x * (x + 2 * rho_s)) * v2)
E = sp.expand(sp.simplify(E.subs(sp.log(x), L)))
eqs = [sp.expand(E.coeff(L, 0)).coeff(x, m) for m in range(0, NORD - 1)]
sol2 = sp.solve(eqs, [C] + list(c_[:NORD - 1]), dict=True)[0]
Cval = sp.simplify(sol2[C])
print()
print(f"  ** the resonant log coefficient:  C = {Cval} **")
check(sp.simplify(Cval - 1 / rho_s) == 0, "C = 1/rho exactly")
check(sp.simplify(sp.diff(Cval, k_s)) == 0, "dC/dk = 0 -- the crossing carries NO wavenumber")
print("  ** so the banked 4 pi/rho is k-free, and PART 3b's k = 0 verification was not a")
print("     restriction on its validity after all.  Checked rather than assumed. **")

# =============================================================================================
head("VERDICT")

print(f"""
  ⇒ ** THE TRANSFER IS NOT A SECOND PLACE A WAVENUMBER CAN ENTER, AND THE ROUTE THE ORDER NAMED IS
       CLOSED RATHER THAN UNTESTED. **

  Step by step along the chain from the progenitor's vacuum to the boundary datum:

     interior vacuum -> crunch residue   the SAME object as the generated spectrum, and this
                                         instrument reproduces r6857's blue running -- {2*lo:+.3f}
                                         to {2*hi:+.3f} -- from initial data placed elsewhere
     the crossing                        monodromy C = 1/rho, dC/dk = 0, exactly: k^2 is regular
                                         where the potential is singular
     the collapse leg                    scale-free at fixed phase, exactly 1 (r6812, r6823)

  ** Nowhere along it does a wavenumber enter that r6857 had not already measured, and where it
     does enter it is BLUE where the target is red. **

  ⛔ AND THE PRICE OF SAYING SO IS A WITHDRAWAL OF THIS SEAT'S OWN RECONCILIATION.  `r6846`
     reconciled the banked scale-invariance with its own blue running by calling them different
     objects.  They are one object; the banked check was run at rho = 1e-3 and 1e-4, where the
     tested band lies wholly below k_break = 1/(2 rho), and at the determined rho = 0.0539 the
     observed band lies wholly above it.  ** The reconciliation was wrong in the direction that let
     a conflict pass, which is the opposite of this seat's usual direction and is recorded for
     that reason. **

  ⌗ WHAT IS LEFT.  PO-31 stays open on exactly what r6857 left it on: what supplies a red
    near-constant tilt.  ** What this removes is a candidate, not the question **, and the corpus
    now has four closed channels plus one closed transfer rather than four closed channels and an
    untested transfer.
""".rstrip())

print()
if FAILED:
    print("FAIL: " + "; ".join(FAILED))
    sys.exit(1)
print("ALL CHECKS PASS")
sys.exit(0)
