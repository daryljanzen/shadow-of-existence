#!/usr/bin/env python3
"""
RECEIPT -- P15: ** THE GROWTH SECTOR IS PARAMETER-FREE, AND THE NORMALISATION ROOT
IS A GROWTH-WEIGHTED MOMENT OF Om_m ABOUT ITS VALUE AT THE NARIAI RADIUS. **

*The published note records that the flat-LambdaCDM growth normalisation
J(Om_m) = int_0^inf dz (1+z)/[Om_m(1+z)^3 + (1-Om_m)]^(3/2) crosses unity once, at
Om* = 0.315162, and asserts no explanation.  Written in this construction's own
variables the crossing is not a coincidence between an integral and a fitted density:
it is a condition on the clock, determined by an equation with no parameters in it,
pivoting on the one epoch the geometry marks.*

** STEP 1 -- THE GROWTH EQUATION LOSES ITS PARAMETERS. **  On the Nariai member the
mass is fixed by Lambda, so the whole scale factor is one function of it:
r = A sinh^(2/3)(u) with u = (3c/2 alpha) tau and A = 2^(1/3)/sqrt(Lambda).  Then
H = (c/alpha) coth u, and the Friedmann readout H^2 = (8 pi G/3) rho + Lambda c^2/3
gives 4 pi G rho = (3/2)(c/alpha)^2 csch^2 u.  Substituting both into

    D_tautau + 2 H D_tau - 4 pi G rho D = 0

and changing variable to u, every factor of (c/alpha)^2 divides out:

    ** 3 D'' + 4 coth(u) D' - 2 csch^2(u) D = 0 **

** alpha does not merely fail to appear -- it CANCELS **, because the source is fixed
by the Nariai-constrained geometry and the time variable carries alpha too.  So growth
in this construction is a universal function of the clock, with no parameters at all.

** STEP 2 -- BOTH MODES ARE EXACT. **  D_minus = coth u = H alpha / c: the decaying
mode IS the rate.  Reduction of order (Wronskian ~ sinh^(-4/3)) then gives

    D_plus(u) = coth(u) * F(u),    F(u) = int_0^u sinh^(2/3)(v) sech^2(v) dv.

** STEP 3 -- Om_m IS A CLOCK READING. **  cosh^2(u) = 1/Om_m exactly, so Om_m =
sech^2(u).  It is not a parameter of anything; it is sech-squared of the time.

** STEP 4 -- J RE-EXPRESSED. **  With a = sinh^(2/3)(u) the scale factor,
J = (2/3) cosh^2(u_0) (D_plus/a)|_0, whose matter-domination limit reproduces the
analytic endpoint J -> 2/5 (since D_plus/a -> 3/5 there).  Setting J = 1 gives
F(u_0) = G(u_0) with G(u) = (3/2) sinh^(5/3)(u)/cosh^3(u).

** STEP 5 -- THE CONDITION IS A MOMENT BALANCE, AND THE PIVOT IS THE NARIAI RADIUS. **
Differentiating gives the exact identity G'/F' = (9/2) Om_m - 2, so
d(F-G)/du = F' [3 - (9/2) Om_m].  Since F(0) = G(0) = 0, the condition integrates to

    ** int_0^{u_0}  a(v) Om_m(v) [ Om_m(v) - 2/3 ]  dv  =  0 **

-- the growth-weighted history of Om_m balanced about 2/3.  ** And Om_m = 2/3 is
rho_m / rho_Lambda = 2 exactly, the deceleration-to-acceleration turnover, at which
the areal radius is alpha/sqrt3 = r_N: the Nariai radius, the front seam, the merged
double root. **

** WHAT IS ESTABLISHED. **  Om* is determined by an equation with nothing free in it.
** What remains contingent is that we observe near that epoch -- a why-now, not a
why-this-density, and the density was never free. **

** TWO SCOPE STATEMENTS, AND BOTH NARROW THE CLAIM.  Each is checked below rather
than merely stated. **

  (a) ** THE TURNOVER IS NOT THIS CONSTRUCTION'S PROPERTY. **  Om_m = 2/3 is
      rho_m/rho_Lambda = 2 in ANY flat matter-and-Lambda rate; LambdaCDM has the same
      turnover and no Nariai radius anywhere.  What is this construction's is the
      IDENTIFICATION of that turnover with a geometric locus -- the areal radius there
      being alpha/sqrt3 = r_N.  ** So the balance pivots on the turnover, and the
      geometry is what makes the turnover a place. **  The receipt checks the pivot in
      both readings so the split is visible.

  (b) ** THE RATE USED IS THE STACKING ONE. **  The published normalisation is a
      matter-and-Lambda integral, and the stacking rate written in the fitted pair IS
      that rate -- which is why the derivation reproduces it.  But the corpus's own
      rate rule assigns perturbations to the LEAF, and on the leaf rate the same
      integral returns 0.99934 rather than unity, moving the root slightly.  ** So what
      is derived is the root of the STANDARD normalisation, not this construction's own
      growth root. **

** WHAT IS NOT CLAIMED. **  That the balance has a closed-form solution; it is solved
numerically here.  And no claim is made that the standard model's growth factor is
wrong -- the function is the same function.  What differs is that in these variables
its root is derived rather than observed.
"""
import math
import sys
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

FAILED = []


def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        FAILED.append(label)


# ---------------------------------------------------------------- the objects
def a_of(u):
    """Scale factor, up to the amplitude: a ~ sinh^(2/3) u."""
    return math.sinh(u) ** (2.0 / 3.0)


def Om_of(u):
    """Matter fraction as a clock reading."""
    return 1.0 / math.cosh(u) ** 2


def F(u):
    return quad(lambda v: math.sinh(v) ** (2 / 3) / math.cosh(v) ** 2, 0, u,
                limit=400)[0]


def G(u):
    return 1.5 * math.sinh(u) ** (5 / 3) / math.cosh(u) ** 3


def D_plus(u):
    return F(u) / math.tanh(u)


def D_minus(u):
    return 1.0 / math.tanh(u)


def J_of_Om(Om):
    """The published normalisation integral, in its original variables."""
    return quad(lambda z: (1 + z) / (Om * (1 + z) ** 3 + (1 - Om)) ** 1.5,
                0, np.inf, limit=500)[0]


def u_of_Om(Om):
    return math.acosh(1.0 / math.sqrt(Om))


print()
print("  THE GROWTH NORMALISATION ROOT, DERIVED")
print("  " + "=" * 68)
print()

# ------------------------------------------------- STEP 1/2: the ODE and its modes
def ode_residual(D, u, h=1e-5):
    d1 = (D(u + h) - D(u - h)) / (2 * h)
    d2 = (D(u + h) - 2 * D(u) + D(u - h)) / h ** 2
    return 3 * d2 + 4 / math.tanh(u) * d1 - 2 * D(u) / math.sinh(u) ** 2


print("  step 1-2: 3 D'' + 4 coth(u) D' - 2 csch^2(u) D = 0")
res_minus = max(abs(ode_residual(D_minus, u)) for u in (0.4, 0.8, 1.5, 2.5))
res_plus = max(abs(ode_residual(D_plus, u)) for u in (0.4, 0.8, 1.5, 2.5))
print(f"      decaying  D = coth u : max residual {res_minus:.2e}")
print(f"      growing   D = coth u F(u) : max residual {res_plus:.2e}")
# coth u satisfies the ODE identically; what is measured here is the
# finite-difference floor, so the tolerance is the discretisation error and
# the analytic check is done separately below at machine precision.
check("the decaying mode coth u -- the rate itself -- solves it",
      res_minus < 1e-4)
_ex = max(abs(3 * (2 * math.cosh(u) / math.sinh(u) ** 3)
              + 4 / math.tanh(u) * (-1 / math.sinh(u) ** 2)
              - 2 * (1 / math.tanh(u)) / math.sinh(u) ** 2)
          for u in (0.4, 0.8, 1.5, 2.5))
check("and does so ANALYTICALLY, to machine precision, differentiated by hand",
      _ex < 1e-13)
check("the growing mode from reduction of order solves it",
      res_plus < 1e-4)

print()
# ------------------------------------------------------ STEP 3: Om_m is the clock
print("  step 3: cosh^2(u) = 1/Om_m")
ok = True
for u in (0.5, 1.0, 1.1803, 1.5, 2.0):
    x0 = (2 * math.sinh(u) ** 2) ** (1 / 3)
    ok &= abs(Om_of(u) - 2.0 / (x0 ** 3 + 2)) < 1e-12
check("Om_m = sech^2(u) matches the dictionary Om_m = 2/(x_0^3+2) at every epoch", ok)

print()
# ------------------------------------------------------------ STEP 4: J rewritten
print("  step 4: J = (2/3) cosh^2(u_0) (D_plus/a)|_0")
ok = True
for Om in (0.2, 0.315162, 0.45, 0.7):
    u = u_of_Om(Om)
    ok &= abs(J_of_Om(Om) - (2 / 3) * math.cosh(u) ** 2 * D_plus(u) / a_of(u)) < 1e-7
check("the rewrite reproduces the published integral at every density tested", ok)

md = D_plus(1e-5) / a_of(1e-5)
print(f"      matter-domination limit D_plus/a = {md:.6f}   (3/5 = 0.6)")
check("D_plus/a -> 3/5 in matter domination", abs(md - 0.6) < 1e-5)
check("so J -> (2/3)(3/5) = 2/5 as Om_m -> 1, the analytic endpoint",
      abs(J_of_Om(0.999999) - 0.4) < 1e-5)

print()
# ------------------------------------- STEP 5: the identity and the moment balance
print("  step 5: G'/F' = (9/2) Om_m - 2")
h = 1e-6
ok = True
for u in (0.4, 0.7, 1.0, 1.4):
    ratio = ((G(u + h) - G(u - h)) / (2 * h)) / ((F(u + h) - F(u - h)) / (2 * h))
    ok &= abs(ratio - (4.5 * Om_of(u) - 2)) < 1e-5
check("** the identity holds exactly, so d(F-G)/du = F'[3 - (9/2)Om_m] **", ok)

balance = lambda u: quad(
    lambda v: a_of(v) * Om_of(v) * (Om_of(v) - 2 / 3), 0, u, limit=400)[0]
u_root = brentq(balance, 0.3, 3.0, xtol=1e-13)
Om_root = Om_of(u_root)
print()
print(f"      moment balance  int a Om (Om - 2/3) du = 0   at u_0 = {u_root:.9f}")
print(f"      Om_m(u_0) = {Om_root:.9f}")

check("the balance reproduces the J = 1 root", abs(F(u_root) - G(u_root)) < 1e-9)
check("** and returns the published Om* = 0.315162 **",
      abs(Om_root - 0.315162) < 1e-6)

print()
# -------------------------------------------------- the pivot IS the Nariai radius
u_piv = brentq(lambda u: Om_of(u) - 2 / 3, 0.1, 2.0, xtol=1e-13)
rho_ratio = 1.0 / math.sinh(u_piv) ** 2
AMPL = 2 ** (1 / 3) / math.sqrt(3.0)          # amplitude in units of alpha, Nariai
r_piv = AMPL * a_of(u_piv)
R_N = 1.0 / math.sqrt(3.0)
print("  the pivot of the balance:")
print(f"      Om_m = 2/3 at u = {u_piv:.9f}")
print(f"      rho_m/rho_Lambda there = {rho_ratio:.9f}")
print(f"      areal radius there     = {r_piv:.9f} alpha")
print(f"      Nariai radius alpha/sqrt3 = {R_N:.9f} alpha")
print()
check("the pivot is rho_m/rho_Lambda = 2 exactly -- the acceleration turnover",
      abs(rho_ratio - 2.0) < 1e-9)
check("** and the areal radius there is the Nariai radius, alpha/sqrt3 **",
      abs(r_piv - R_N) < 1e-12)

print()
print("  " + "-" * 68)
print("  scope (a): the turnover is framework-neutral, the IDENTIFICATION is not")
# In any flat matter+Lambda rate, q = 0 where rho_m = 2 rho_Lambda, i.e. Om_m = 2/3.
# That statement needs no substrate and no Nariai radius.
check("Om_m = 2/3 is the turnover in ANY flat matter-and-Lambda rate, "
      "with no geometry invoked",
      abs((2 / 3) / (1 - 2 / 3) - 2.0) < 1e-12)
check("so the pivot itself is framework-neutral; what is this construction's is "
      "that the turnover sits at alpha/sqrt3",
      abs(r_piv - R_N) < 1e-12)

print()
print("  scope (b): the rate used is the STACKING rate, not the leaf rate")
OM_R = 8.5e-5
J_stack = quad(lambda z: (1 + z) / (Om_root * (1 + z) ** 3
                                    + (1 - Om_root)) ** 1.5, 0, np.inf, limit=600)[0]
J_leaf = quad(lambda z: (1 + z) / (Om_root * (1 + z) ** 3 + (1 - Om_root)
                                   + OM_R * (1 + z) ** 4) ** 1.5,
              0, np.inf, limit=600)[0]
print(f"      J on the stacking rate (the published object) = {J_stack:.8f}")
print(f"      J on the leaf rate (radiation gravitating)     = {J_leaf:.8f}")
print(f"      shift = {(J_leaf - J_stack) / J_stack * 100:+.4f}%")
check("the stacking rate reproduces the published normalisation at the root",
      abs(J_stack - 1.0) < 1e-5)
check("** the leaf rate does NOT, so the derived root is the STANDARD one **",
      abs(J_leaf - 1.0) > 1e-4)

print()
print("  " + "=" * 68)
if FAILED:
    print(f"  {len(FAILED)} check(s) FAILED")
    for f in FAILED:
        print(f"    - {f}")
    sys.exit(1)
print("  The growth equation has no parameters: alpha cancels because the source is")
print("  fixed by the Nariai-constrained geometry.  Om_m is sech^2 of the clock.  And")
print("  J = 1 is the growth-weighted history of Om_m balanced about 2/3 -- which is")
print("  rho_m/rho_Lambda = 2, the turnover, at the areal radius alpha/sqrt3 = r_N.")
print("  ** So Om* is determined by a parameter-free equation.  The pivot is the")
print("  ** turnover -- framework-neutral -- and the geometry is what makes that")
print("  ** turnover a place.  What stays contingent is that we look near it.")
print()
sys.exit(0)
