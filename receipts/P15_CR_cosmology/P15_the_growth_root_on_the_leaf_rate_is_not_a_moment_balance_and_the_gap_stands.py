#!/usr/bin/env python3
r"""
RECEIPT -- P15 / PO-38: ** THE MOMENT-BALANCE FORM DOES NOT SURVIVE ON THE LEAF RATE, THE ROOT
BARELY MOVES, AND IT MOVES THE OPPOSITE WAY FROM WHAT THE CONTINUED INTEGRAL IMPLIES. **

`PO-38` asks for the growth normalisation root re-solved on the LEAF rate -- the rate the corpus's
own three-level rule assigns the perturbations to -- and warns that adding radiation may break the
cancellation that made the growth equation parameter-free.  ** It does, and the break is exact
rather than numerical. **

===================================================================================================
** THE JUDGEMENT, MADE BEFORE THE ARITHMETIC AND CHECKED SYMBOLICALLY. **
===================================================================================================

`P15_the_growth_root_is_a_moment_balance_pivoting_on_the_nariai_radius`'s STEP 2 rests on one
sentence: *"D_minus = coth u = H alpha / c: the decaying mode IS the rate."*  Apply the growth
operator to D = H with radiation present, using only the flat Friedmann/Raychaudhuri pair
Hdot = -4 pi G (rho + p) and the two continuity equations:

    ** L[H]  =  Hddot + 2 H Hdot - 4 pi G rho_m H  =  (32/3) pi G H rho_r **

-- which vanishes if and only if rho_r = 0.  ⇒ *** THE DECAYING MODE STOPS BEING THE RATE THE
INSTANT RADIATION GRAVITATES. ***  Everything downstream rests on it: the reduction of order that
gives D_plus = coth(u) F(u), the identity G'/F' = (9/2) Om_m - 2, and therefore the moment balance
itself.  ** So the balance is a matter-and-Lambda theorem, not a growth theorem. **

⌗ *And alpha still cancels.*  Radiation enters the rate as a DIMENSIONLESS function of the clock,
so the equation stays scale-free -- but it acquires Om_r, which the geometry does not fix.
** The loss is not scale-freedom.  It is parameter-freedom: a parameter-free equation becomes a
one-parameter family. **

===================================================================================================
** WHAT REPLACES IT, AND HOW THE REPLACEMENT IS NORMALISED. **
===================================================================================================

The growth ODE integrated directly, in x = ln a:

    D_xx + [2 + dlnE/dx] D_x - (3/2) Om_m(a) D = 0,     Om_m(a) = Om_m a^-3 / E^2(a)

with the LEAF rate E^2 = Om_m a^-3 + Om_r a^-4 + (1 - Om_m - Om_r), flatness kept.  The initial
condition is the Meszaros growing mode D = 1 + (3/2) y, y = a/a_eq -- ** which this receipt checks
is EXACT for the matter+radiation problem, so the attractor amplitude is analytic and no window
has to be fitted. **  The solution is then normalised by the same convention the published integral
carries, D -> (2/5) a / Om_m in matter domination, and J is its value today.

⌗ ** The (2/5) is checked rather than asserted: ** with radiation off, the ODE under that convention
reproduces the published integral J = int_0^1 da/(a^3 E^3) to 2e-12.

===================================================================================================
** THE RESULT.  OUTCOME 3, WITH A SIGN. **
===================================================================================================

                                          Om*            u_0          x_0    vs 1.6648    sigma
    stacking (the published root)   0.315162424    1.180309372     1.631903     -1.976%   -0.704
    ** leaf, growing mode SOLVED    0.315303543    1.180038880     1.631480     -2.001%   -0.713 **
    leaf, published integral CONTINUED
                                    0.314917676    1.180778715     1.632453     -1.943%   -0.693
    -- corpus measured --                               1.2052    1.6648 +/- 0.0467

** THE ROOT BARELY MOVES: ** du_0 = -2.70e-04, which is 1.1% of the 0.0249 gap; the offset goes
0.704 sigma -> 0.713 sigma, a change of 0.009 sigma on a 0.70 sigma gap.  ⇒ *** The 2% is NOT an
artefact of the rate.  The gap stands and wants a mechanism -- outcome 3 as PO-38 framed it. ***
** And it moves FURTHER from the measurement, not closer. **

⛔ ** AND THE CONTINUED INTEGRAL GETS THE SIGN WRONG, WHICH IS THE SHARPER FINDING. **  Continuing
the published closed form onto the leaf rate -- the route behind the recorded 0.99934 -- moves the
root the OTHER way (0.704 -> 0.693 sigma), and by 1.7x the magnitude in u_0 (4.69e-04
against 2.70e-04) or 1.3x in sigma.  *That integral is the growing
mode only when the closed form solves the rate, and on the leaf rate it does not.*  ⇒ ** 0.99934 is
not a measure of how far the root moves.  It measures a closed form failing on a rate it does not
solve, and reading it as a direction gives the wrong one. **

⌗ ** A FLATNESS SLIP IN THE EXISTING SCOPE-(b) CHECK, REPORTED BECAUSE IT IS THE SIZE OF THE
EFFECT. **  Its leaf integrand carries Om_Lambda = 1 - Om, not 1 - Om - Om_r, so the three
fractions sum to 1 + Om_r.  Corrected, its own figure moves 0.99934 -> 0.99940, and the slip alone
accounts for 10.4% of the shift that figure reports.

===================================================================================================
** WHERE THE PIVOT LANDS: IT DOES NOT MOVE, IT SPLITS. **
===================================================================================================

    stacking:  Om_m = 2/3            u = 0.658478948    r/r_N = 1.000000000  (exactly the Nariai radius)
    leaf:      Om_m = 2/3            u = 0.658260700    r/r_N = 0.999747989
    leaf:      q = 0, the TURNOVER   u = 0.658768578    r/r_N = 1.000334436

** Om_m = 2/3 is the acceleration turnover only when matter and Lambda are the whole content. **
Radiation decelerates too, so q = 0 requires Om_m + 2 Om_r = 2 Om_Lambda.  ⇒ *** On the leaf rate
the pivot and the turnover are two different epochs, separated by du = 5.08e-04, and the Nariai
radius sits BETWEEN them. ***  The identification of the turnover with r_N is exact on the stacking
rate and approximate on the leaf one -- which is the correct status for an L1 statement read on L2.

** WHAT IS NOT CLAIMED. **  That the leaf rate is the right rate for this object -- the corpus's
rule assigns it, and this receipt computes the consequence rather than re-litigating the
assignment.  That Om_r is anything but an inherited datum: it is held FIXED at 8.5e-5 throughout
and nothing here is tuned.  And no mechanism for the residual 2% is offered; the row asked whether
the rate explains it, and the answer is that it does not.

STATUS: OK
RUN: python3 P15_the_growth_root_on_the_leaf_rate_is_not_a_moment_balance_and_the_gap_stands.py
RUNTIME: ~20 s
ORIGIN: built r4394 (node 60) discharging PO-38's computation.
"""
import math
import sys

import numpy as np
import sympy as sp
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq

print(__doc__.split("STATUS:")[0])
BAR = "=" * 78
FAILED = []


def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        FAILED.append(label)


OM_R = 8.5e-5                     # inherited datum, held fixed -- never tuned here
X0_MEAS, X0_SIG = 1.6648, 0.0467  # the corpus's own measured epoch and its width


# ------------------------------------------------------------------ the growth ODE
def rhs(x, y, Om, Orad, lam):
    a = math.exp(x)
    OL = (1.0 - Om - Orad) if lam else 0.0
    E2 = Om * a ** -3 + Orad * a ** -4 + OL
    D, Dx = y
    dlnE = 0.5 * (-3 * Om * a ** -3 - 4 * Orad * a ** -4) / E2
    return [Dx, -(2.0 + dlnE) * Dx + 1.5 * (Om * a ** -3 / E2) * D]


def _run(Om, Orad, lam, a_i, D0, Dx0):
    return solve_ivp(rhs, [math.log(a_i), 0.0], [D0, Dx0], args=(Om, Orad, lam),
                     rtol=1e-12, atol=1e-18, method='DOP853', dense_output=True)


def J_growmode(Om, Orad):
    """J from the growing mode actually solved on the rate, normalised D -> (2/5)a/Om."""
    if Orad == 0.0:
        a_i = 1e-7
        return _run(Om, 0.0, True, a_i, (2 / 5) * a_i / Om, (2 / 5) * a_i / Om).y[0, -1]
    a_eq = Orad / Om
    a_i = 1e-9
    y_i = a_i / a_eq
    s = _run(Om, Orad, True, a_i, 1.0 + 1.5 * y_i, 1.5 * y_i)
    return (((2 / 5) / Om) / (1.5 / a_eq)) * s.y[0, -1]


def J_integral(Om, Orad, flat=True):
    """The PUBLISHED closed form, continued onto whichever rate.  flat=False is the slip."""
    OL = (1.0 - Om - Orad) if flat else (1.0 - Om)
    return quad(lambda a: a ** -3 * (Om * a ** -3 + Orad * a ** -4 + OL) ** -1.5,
                0.0, 1.0, limit=800)[0]


x0_of = lambda Om, Orad: (2 * (1.0 - Om - Orad) / Om) ** (1 / 3)
u0_of = lambda Om: math.acosh(1 / math.sqrt(Om))

# =====================================================================================
print(BAR); print("PART 1 — THE JUDGEMENT: THE DECAYING MODE STOPS BEING THE RATE"); print(BAR)
t = sp.symbols('t')
G, pi = sp.symbols('G pi', positive=True)
rm, rr, H = sp.Function('rho_m')(t), sp.Function('rho_r')(t), sp.Function('H')(t)
Hdot = -4 * pi * G * (rm + sp.Rational(4, 3) * rr)
Hddot = sp.diff(Hdot, t).subs({sp.Derivative(rm, t): -3 * H * rm,
                               sp.Derivative(rr, t): -4 * H * rr})
L_H = sp.simplify(sp.expand(Hddot + 2 * H * Hdot - 4 * pi * G * rm * H))
print(f"      L[H] = {L_H}")
check("L[H] = (32/3) pi G H rho_r — NOT zero once radiation gravitates",
      sp.simplify(L_H - sp.Rational(32, 3) * pi * G * H * rr) == 0)
check("and it DOES vanish when rho_r = 0, so the stacking-rate identity is intact there",
      sp.simplify(L_H.subs(rr, 0)) == 0)
print("      ⇒ the reduction of order, the G'/F' identity and the moment balance all rest on this")

# =====================================================================================
print(); print(BAR); print("PART 2 — THE REPLACEMENT, AND ITS TWO CALIBRATIONS"); print(BAR)
Om0 = 0.315162424
a_i = 1e-7
J_ode = _run(Om0, 0.0, True, a_i, (2 / 5) * a_i / Om0, (2 / 5) * a_i / Om0).y[0, -1]
print(f"      radiation OFF:  ODE {J_ode:.9f}   published integral {J_integral(Om0, 0.0):.9f}")
check("the ODE under the D -> (2/5)a/Om convention reproduces the published integral to 1e-10",
      abs(J_ode - J_integral(Om0, 0.0)) < 1e-10)

a_eq = OM_R / Om0
s_mr = _run(Om0, OM_R, False, 1e-9, 1.0 + 1.5 * 1e-9 / a_eq, 1.5 * 1e-9 / a_eq)
worst = max(abs(s_mr.sol(math.log(a))[0] / (1 + 1.5 * a / a_eq) - 1)
            for a in (1e-6, 1e-4, 1e-3, 1e-2, 1e-1, 1.0))
print(f"      Lambda OFF:  max |D_num/(1 + 3y/2) - 1| over a = 1e-6..1 is {worst:.2e}")
check("the Meszaros growing mode 1 + (3/2)y is EXACT here, so the attractor is analytic",
      worst < 1e-9)

# =====================================================================================
print(); print(BAR); print("PART 3 — THE ROOT, THREE WAYS"); print(BAR)
r_stack = brentq(lambda O: J_growmode(O, 0.0) - 1, 0.2, 0.5, xtol=1e-14)
r_leaf = brentq(lambda O: J_growmode(O, OM_R) - 1, 0.2, 0.5, xtol=1e-14)
r_cont = brentq(lambda O: J_integral(O, OM_R) - 1, 0.2, 0.5, xtol=1e-14)
print(f"      {'':<36}{'Om*':>13}{'u_0':>13}{'x_0':>11}{'sigma':>9}")
out = {}
for lab, O, orad in (("stacking (the published root)", r_stack, 0.0),
                     ("leaf, growing mode SOLVED", r_leaf, OM_R),
                     ("leaf, published integral CONTINUED", r_cont, OM_R)):
    x = x0_of(O, orad)
    out[lab] = (O, u0_of(O), x, (x - X0_MEAS) / X0_SIG)
    print(f"      {lab:<36}{O:>13.9f}{u0_of(O):>13.9f}{x:>11.6f}{(x - X0_MEAS) / X0_SIG:>9.3f}")
print(f"      {'— corpus measured —':<36}{'':>13}{1.2052:>13.4f}{X0_MEAS:>11.4f}"
      f"  +/- {X0_SIG}")

check("the stacking root reproduces the published u_0 = 1.180309372",
      abs(out["stacking (the published root)"][1] - 1.180309372) < 1e-8)
du = out["leaf, growing mode SOLVED"][1] - out["stacking (the published root)"][1]
gap = 1.2052 - out["stacking (the published root)"][1]
print(f"\n      the leaf root moves du_0 = {du:+.3e}, which is {abs(du / gap):.2%} of the "
      f"{gap:.4f} gap")
check("** the root BARELY MOVES: under 2% of the gap — outcome 3 **", abs(du / gap) < 0.02)
s_st = out["stacking (the published root)"][3]
s_lf = out["leaf, growing mode SOLVED"][3]
s_ct = out["leaf, published integral CONTINUED"][3]
check(f"** and it moves FURTHER from the measurement, {s_st:.3f} -> {s_lf:.3f} sigma **",
      abs(s_lf) > abs(s_st))
check(f"** while the CONTINUED integral moves it CLOSER, {s_st:.3f} -> {s_ct:.3f} — "
      f"the opposite sign **", abs(s_ct) < abs(s_st))
print(f"      and by {abs(s_ct - s_st) / abs(s_lf - s_st):.1f}x the magnitude, so it is wrong in "
      f"size as well as direction")

# =====================================================================================
print(); print(BAR); print("PART 4 — THE FLATNESS SLIP IN THE EXISTING SCOPE-(b) CHECK"); print(BAR)
j_flat, j_slip = J_integral(Om0, OM_R, True), J_integral(Om0, OM_R, False)
print(f"      leaf J at the stacking root:  flatness kept {j_flat:.8f}   as written {j_slip:.8f}")
check("the recorded 0.99934 is the SLIPPED value; kept flat it is 0.99940",
      abs(j_slip - 0.99934) < 5e-6 and abs(j_flat - 0.99940) < 5e-6)
u_flat = u0_of(brentq(lambda O: J_integral(O, OM_R, True) - 1, 0.2, 0.5, xtol=1e-14))
u_slip = u0_of(brentq(lambda O: J_integral(O, OM_R, False) - 1, 0.2, 0.5, xtol=1e-14))
frac = abs(u_slip - u_flat) / abs(u_flat - out["stacking (the published root)"][1])
print(f"      the slip alone is {frac:.1%} of the shift that figure reports")
check("so the slip is comparable to the effect it is quoted for", 0.05 < frac < 0.3)

# =====================================================================================
print(); print(BAR); print("PART 5 — THE BALANCE, AND THE PIVOT THAT SPLITS"); print(BAR)
u0_l = out["leaf, growing mode SOLVED"][1]
Om_l = out["leaf, growing mode SOLVED"][0]
a_of = lambda v, u0: (math.sinh(v) / math.sinh(u0)) ** (2 / 3)
Om_leaf = lambda a, Om: Om * a ** -3 / (Om * a ** -3 + OM_R * a ** -4 + (1 - Om - OM_R))
Om_stack = lambda v: 1 / math.cosh(v) ** 2

dif = max(abs(Om_leaf(a_of(v, u0_l), Om_l) - Om_stack(v)) for v in (0.2, 0.4, 0.7, 1.0))
print(f"      max |Om_leaf(v) - sech^2 v| over v = 0.2..1.0 : {dif:.2e}")
check("Om_m = sech^2(u) is a STACKING-rate identity and fails on the leaf rate", dif > 1e-5)

bal_s = quad(lambda v: math.sinh(v) ** (2 / 3) * Om_stack(v) * (Om_stack(v) - 2 / 3),
             0, out["stacking (the published root)"][1], limit=400)[0]
bal_l = quad(lambda v: math.sinh(v) ** (2 / 3) * Om_leaf(a_of(v, u0_l), Om_l)
             * (Om_leaf(a_of(v, u0_l), Om_l) - 2 / 3), 1e-9, u0_l, limit=400)[0]
print(f"      moment balance at its own root:  stacking {bal_s:+.2e}   leaf {bal_l:+.2e}")
check("the balance vanishes on the stacking rate — the theorem", abs(bal_s) < 1e-9)
check("** and does NOT vanish on the leaf rate: the form does not survive **", abs(bal_l) > 1e-5)

v_ps = brentq(lambda v: Om_stack(v) - 2 / 3, 0.1, 2.0, xtol=1e-14)
v_pl = brentq(lambda v: Om_leaf(a_of(v, u0_l), Om_l) - 2 / 3, 0.1, 2.0, xtol=1e-14)


def q_of(a, Om):
    E2 = Om * a ** -3 + OM_R * a ** -4 + (1 - Om - OM_R)
    return 0.5 * (Om * a ** -3 + 2 * OM_R * a ** -4) / E2 - (1 - Om - OM_R) / E2


v_ql = brentq(lambda v: q_of(a_of(v, u0_l), Om_l), 0.1, 2.0, xtol=1e-14)
AM, RN = 2 ** (1 / 3) / math.sqrt(3.0), 1 / math.sqrt(3.0)
r_of = lambda v: AM * math.sinh(v) ** (2 / 3) / RN
print()
for lab, v in (("stacking: Om_m = 2/3", v_ps), ("leaf: Om_m = 2/3", v_pl),
               ("leaf: q = 0, the turnover", v_ql)):
    print(f"      {lab:<28} u = {v:.9f}   r/r_N = {r_of(v):.9f}")
check("on the stacking rate the pivot IS the Nariai radius, exactly",
      abs(r_of(v_ps) - 1.0) < 1e-12)
check("** on the leaf rate Om_m = 2/3 and q = 0 are two different epochs **",
      abs(v_pl - v_ql) > 1e-5)
check("** and the Nariai radius sits BETWEEN them **",
      r_of(v_pl) < 1.0 < r_of(v_ql))

# =====================================================================================
print(); print(BAR)
if FAILED:
    print(f"⛔ {len(FAILED)} CHECK(S) FAILED")
    for f in FAILED:
        print("   - " + f)
    print(BAR)
    sys.exit(1)
print("""VERDICT.  ** The moment-balance form does not survive on the leaf rate, and the reason is
exact: the decaying mode is the rate only while radiation does not gravitate.  L[H] = (32/3) pi G H
rho_r. **  With that gone the reduction of order, the G'/F' identity and the balance all go with it;
alpha still cancels, so the equation stays scale-free, but it acquires Om_r and stops being
parameter-free.

** What replaces it is the growth ODE solved on the rate **, with the Meszaros mode as an exact
initial condition and the published (2/5)a/Om convention checked against the closed form where the
closed form is valid.

*** THE ANSWER IS OUTCOME 3, WITH A SIGN. ***  The leaf root sits at u_0 = 1.180038880 against the
stacking 1.180309372 -- a move of 1.1% of the gap, taking the offset from 0.704 to 0.713 sigma.
** The 2% is not an artefact of the rate: the gap stands and wants a mechanism. **  And what shift
there is goes the WRONG way -- further from the measurement, not closer.

⛔ ** The continued integral, which is where 0.99934 comes from, gets the direction backwards. **
It moves the root toward the measurement where solving the equation moves it away, and by 1.7x
the size in u_0.  That number does not measure how far the root moves; it measures a closed form failing on a
rate it does not solve.

⌗ ** And the pivot does not move -- it SPLITS. **  Om_m = 2/3 is the acceleration turnover only
when matter and Lambda are the whole content; radiation decelerates too.  On the leaf rate the two
loci separate and the Nariai radius sits between them, which is the right status for an L1
identification read on L2.""")
print(BAR)
sys.exit(0)
