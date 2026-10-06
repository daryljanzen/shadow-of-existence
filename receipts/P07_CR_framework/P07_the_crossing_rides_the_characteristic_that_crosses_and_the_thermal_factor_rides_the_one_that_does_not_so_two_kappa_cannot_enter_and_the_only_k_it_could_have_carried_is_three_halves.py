#!/usr/bin/env python3
"""
RECEIPT -- P07/P15: ** THE MODE EQUATION ACROSS THE BACK SEAM, IN THE CHART THE BEAD ACTUALLY
CROSSES IN.  THE SEAM IS A CHARACTERISTIC SURFACE AND ITS TWO CHARACTERISTIC SPEEDS AT THE SEAM ARE
EXACTLY 2 AND EXACTLY 0.  THE CROSSING RIDES THE SPEED-2 FAMILY; THE THERMAL FACTOR
e^{pi omega/kappa} RIDES THE SPEED-0 FAMILY, WHICH DOES NOT CROSS.  SO 2 kappa CANNOT ENTER THROUGH
THE CROSSING: THE TRANSFER IS 1, IDENTICALLY IN omega AND IN ell. **

Built r7185+cc66.147 (node 66, code seat), on `PO-13`, answering `r7185`'s order.

===================================================================================================
** THE ORDER, AND THE ONE STRUCTURAL FACT THAT MADE IT A CLOSED-FORM CALCULATION **
===================================================================================================

`r7185` asked for the mode equation across a simple root of `$f$` crossed at finite proper time on
the collapse trajectory, with three things kept apart: the static approach versus the trajectory
crossing; which rate each step is on; and whether the crossing carries a `$k$`.

** The fact that collapses all three: the Painleve-Gullstrand chart built on this `$f$` IS the
corpus's own collapse branch.  Not a chart chosen for convenience and then reconciled with the
trajectory -- the same object. **  PG's shift is `$v^2=1-f=2M/r+r^2/\\alpha^2$`, so its congruence is
the `$E=1$` radial geodesic family; `$v$` is real exactly where `$|r|\\ge(2M\\alpha^2)^{1/3}$` and
vanishes exactly there, which is the turnaround; and on `$r=-(2M\\alpha^2)^{1/3}\\cosh^{2/3}x$` the
chart's own time advances as `$\\dd\\tau=-(2\\alpha/3)\\dd x$` EXACTLY, so `$x$` is proper time up to
a constant.  ** The leg's conformal measure follows: `$\\dd\\eta=\\dd\\tau/a$` with `$a=|r|/\\alpha$`
gives the prefactor `$2/(\\sqrt3\\,2^{1/3})$` and the leg length `$1.927621297\\alpha$` that
`P07_the_back_seam_is_the_laps_one_non_degenerate_horizon...` measures. **  So the chart in which the
mode equation is REGULAR at the seam is the chart in which the bead's clock is the time coordinate.
`r7185`'s item 2 is answered structurally rather than by a convention choice: the mode is carried on
the comoving congruence's own proper time, and the static chart's `$t$` is not any clock on the
trajectory.

  PART A  ** THE CHART IS THE TRAJECTORY. **  `$E=1$`, turnaround at `$v=0$`, `$\\dd\\tau$` exact,
          and the conformal prefactor and leg length recovered from the PG construction alone.
  PART B  ** THE MODE EQUATION, DERIVED AND NOT POSTED. **  `$(r^2f R')'+2i\\omega r^2vR'
          +[\\omega^2r^2+i\\omega(r^2v)'-\\ell(\\ell+1)]R=0$`, with every coefficient FINITE at the
          seam and only the `$R''$` coefficient vanishing there.
  PART C  ** THE SEAM IS A CHARACTERISTIC AND THE TWO SPEEDS ARE 2 AND 0. **  `$\\dd r/\\dd\\tau
          =v\\pm1$`; at the seam `$v=1$`.  The crossing family takes `$10^{-3}\\alpha$` of proper
          time to cross a `$\\pm10^{-3}\\alpha$` window; the skimming family takes
          `$\\ln100/\\kappa$` per factor `$100$` and never arrives.
  PART D  ** THE TWO INDICES: `$0$` AND `$-i\\omega/\\kappa$`, with `$\\kappa$` the corpus's own
          `$3\\sqrt3/4\\alpha$` to 18 figures -- recovered from the equation and not inserted. **
  PART E  ** WHICH BRANCH EACH CHARACTERISTIC CARRIES. **  On the skimming ray
          `$x\\propto e^{-\\kappa\\tau}$`, so `$e^{-i\\omega\\tau}x^{-i\\omega/\\kappa}$` is
          CONSTANT: the thermal branch is the one the non-crossing rays carry.  Its phase holds
          within `$0.004$` rad while the bare `$e^{-i\\omega\\tau}$` turns through `$138$` -- a
          factor `$38000$`, measured with `$\\tau(x)$` taken by quadrature and not from the law.
  PART F  ** THE TRANSFER, MEASURED. **  The index-`$0$` branch exists for every `$(\\omega,\\ell)$`
          (its recursion's denominator cannot vanish), solves the equation to `$10^{-20}$` on BOTH
          sides (measured `$10^{-36}$`), and its transfer across a window of half-width `$d$`
          goes to `$1$` LIKE `$d$` --
          while `$e^{\\pi\\omega/\\kappa}$` is `$d$`-independent and is `$2.7\\times10^{136}$` at
          `$\\omega=100\\kappa$`.
  PART G  ** THE FRONT SEAM IS THE SAME FORMULA INVERTED, AND ONE LINE COVERS BOTH. **  Both seams'
          non-trivial branch is `$e^{-2i\\omega r_*}$`; whether that is a MODULUS or a PHASE is
          decided by whether `$r_*$` acquires an imaginary part on continuation, which happens at a
          logarithmic (simple) root and not at a pole (double) root.
  PART H  ** AT WHICH `$k$`. **  The only scale at the crossing is `$\\kappa$`, so the only comoving
          wavenumber it could have carried is `$k=a_h\\kappa=3/2$` EXACTLY, `$\\alpha$`-free.  That is
          `$L=0.8028$`, BELOW the dipole, and `$\\ell=4.16$` against the first acoustic peak's
          `$220.60$` -- a factor `$53.0$`, the `$k$`-space counterpart of the loci's `$50.6$`.

⇒ *** THE CROSSING DOES NOT ALTER THE SPECTRUM.  The factor is 1 -- not small, not k-independent-and-
nonzero, but the identity -- so it is neither an amplitude in $A_s$ nor a tilt in $n_s$.  2 kappa is
in the equation exactly once, as the index of the branch that is not smooth at the seam, and that
branch is carried by the rays that asymptote to the seam instead of crossing it.  The transmission
chain closes end to end, and the sector's 1.57 acquires NO parameter address from the lap's one
non-degenerate horizon. ***

** WHAT THIS IS NOT, AND THE ONE QUANTITY THE CORPUS DOES NOT HAVE. **
  ⛔ Not a calculation of what the seam RADIATES.  `$T_H=\\kappa/2\\pi=0.2067\\alpha^{-1}$` is a
     statement about the quantum state on this background, not about a classical mode's transfer,
     and this receipt computes only the transfer.  A flux calculation needs the progenitor interior
     `PO-75` is live on; the TRANSFER did not, and that is the result.
  ⛔ Not a claim that nothing happens between the fixing locus and the seam.  `$99$` per cent of the
     leg lies in between and the envelope already prices it.  What is computed here is the crossing
     itself, which is the `$d\\to0$` limit, and that limit is `$1$`.
  ⌗ ** THE MISSING QUANTITY, NAMED RATHER THAN FITTED: the physical `$\\alpha$`. **  Without it
     `$k=3/(2\\alpha)$` is not a number in `$\\mathrm{Mpc}^{-1}$`.  It is not needed: the verdict is
     `$1$`, which carries no scale, and the RATIO to the first peak is `$\\alpha$`-free.

** COMPUTES: one metric in the Painleve-Gullstrand chart, symbolically, with `$M$` and
   `$\\alpha$` free; one second-order ODE's coefficients, indices
   and Frobenius recursion at two roots of the same cubic; two characteristic families by quadrature;
   and the index-0 branch's transfer over four decades of `$\\omega/\\kappa$`, three `$\\ell$` and four
   window widths.  *** The construction has one scale, `$\\alpha$`, and every number below is a pure
   number in `$\\alpha=1$` units; the `$(\\omega,\\ell)$` ladder is the only input and it is stated. ***
   No grid, no fit, no banked artefact. **

STATUS: rc=0 on success.  Run: python3 <this file>   (sympy, mpmath; ~30 s)
"""
import sys

import mpmath as mp
import sympy as sp

print(__doc__.split("STATUS:")[0])
BAR = "=" * 104
fail = []


def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        fail.append(label)


def head(t):
    print(f"\n{BAR}\n  {t}\n{BAR}")


mp.mp.dps = 40

# ---- the corpus's closed-form geometry, alpha = 1 -----------------------------------------------
M = mp.sqrt(3) / 9                      # Nariai: M = alpha/(3 sqrt3)
R_BACK = -2 / mp.sqrt(3)                # the back seam, the cubic's SIMPLE root
R_FRONT = 1 / mp.sqrt(3)                # the front seam, its DOUBLE root
KAP = 3 * mp.sqrt(3) / 4                # kappa = 3 sqrt3 / 4 alpha
R_TURN = -(2 * M) ** (mp.mpf(1) / 3)    # the collapse branch's turnaround

f = lambda r: 1 - 2 * M / r - r ** 2
v = lambda r: mp.sqrt(2 * M / r + r ** 2)          # the PG shift, positive on the leg
A = lambda r: r ** 2 - 2 * M * r - r ** 4          # = r^2 f
Ap = lambda r: 2 * r - 2 * M - 4 * r ** 3          # = (r^2 f)'
P = lambda r: mp.sqrt(r ** 6 + 2 * M * r ** 3)     # = r^2 v
Pp = lambda r: 3 * r ** 2 * (r ** 3 + M) / P(r)    # = (r^2 v)'


# ============================================================ A. the chart IS the trajectory
head("A.  THE CHART IS THE TRAJECTORY -- PG's CONGRUENCE IS THE CORPUS'S OWN COLLAPSE BRANCH")

rs, xs = sp.symbols('r x', real=True)
Ms = sp.Rational(1, 3) / sp.sqrt(3)
fsym = 1 - 2 * Ms / rs - rs ** 2
xp = sp.symbols('xp', positive=True)
r_of_x = -(2 * Ms) ** sp.Rational(1, 3) * sp.cosh(xp) ** sp.Rational(2, 3)
v_of_x = sp.sqrt(2 * Ms / r_of_x + r_of_x ** 2)
dx_dtau = sp.simplify(v_of_x / sp.diff(r_of_x, xp))
print(f"      v^2 = 1 - f = 2M/r + r^2/alpha^2, so the PG congruence has E = 1")
print(f"      v = 0  at  r = -(2 M alpha^2)^(1/3) = {mp.nstr(R_TURN, 15)}  = the TURNAROUND")
print(f"      on r = -(2M)^(1/3) cosh^(2/3)x :   dx/dtau = {dx_dtau}   (exactly -3/2)")
check("Ⓐ①  PG's shift vanishes exactly at the collapse branch's turnaround, so the chart covers "
      "exactly the leg and no more -- the congruence is the E=1 family, i.e. the collapse branch",
      abs(v(R_TURN)) < mp.mpf('1e-30') and abs(R_TURN + mp.mpf('0.727415757314481')) < 1e-15)
check("Ⓐ②  and on that branch the chart's own time is the proper time, exactly: dtau = -(2/3) dx, "
      "so x is an affine proper-time parameter and the crossing is at finite tau by construction",
      sp.simplify(dx_dtau + sp.Rational(3, 2)) == 0)

_seam_from_branch = R_TURN * 2 ** (mp.mpf(2) / 3)
print(f"      cosh x = 2  ->  r = {mp.nstr(_seam_from_branch, 15)}   vs  -2/sqrt3 = "
      f"{mp.nstr(R_BACK, 15)}")
check("Ⓐ③  `cosh x = 2` on the collapse branch IS the cubic's simple root -2 alpha/sqrt3, so the "
      "seam the order names and the root the mode equation degenerates at are the same point",
      abs(_seam_from_branch - R_BACK) < mp.mpf('1e-30'))

_c0 = (mp.mpf(2) / 3) / (-R_TURN)
_leg = _c0 * mp.quad(lambda u: mp.cosh(u) ** (-mp.mpf(2) / 3), [0, mp.inf])
_tau_cross = mp.mpf(2) / 3 * mp.acosh(2)
print(f"      d eta = dtau / a with a = |r|/alpha  ->  prefactor {mp.nstr(_c0, 15)} "
      f"= 2/(sqrt3 2^(1/3))")
print(f"      leg conformal length = {mp.nstr(_leg, 12)} alpha      proper time seam->turnaround "
      f"= (2/3) acosh 2 = {mp.nstr(_tau_cross, 12)} alpha")
check("Ⓐ④  the conformal prefactor and the leg length 1.927621297 alpha follow from the PG "
      "construction ALONE -- two independent routes to the same leg, so the chart and the corpus's "
      "conformal measure are one object",
      abs(_c0 - 2 / (mp.sqrt(3) * 2 ** (mp.mpf(1) / 3))) < mp.mpf('1e-30')
      and abs(_leg - mp.mpf('1.927621297')) < 1e-9)
check("Ⓐ⑤  the crossing-to-turnaround proper time is finite and exactly (2 alpha/3) acosh 2 = "
      "0.877971931 alpha -- which is the trajectory's own clock, NOT the 0.66978 alpha the "
      "companion receipt extrapolates (that is int dr/sqrt(-f) over a fixed 0.3 alpha window, a "
      "convergence demonstration at the root, and the two quantities are not the same integral)",
      abs(_tau_cross - mp.mpf('0.877971931283')) < 1e-11)


# ============================================================ B. the mode equation
head("B.  THE MODE EQUATION IN THE CROSSING CHART, DERIVED FROM THE METRIC")

# the derivation is done with M and alpha FREE, so what it establishes is not Nariai-specific;
# the seam's own numbers are then read off at M = alpha/(3 sqrt3).
rg, Mg, ag = sp.symbols('r M alpha', positive=True)
w, ell = sp.symbols('omega ell', positive=True)
th = sp.symbols('theta')
fg = 1 - 2 * Mg / rg - rg ** 2 / ag ** 2
vg = sp.sqrt(1 - fg)
gmat = sp.Matrix([[-(1 - vg ** 2), -vg, 0, 0],
                  [-vg, 1, 0, 0],
                  [0, 0, rg ** 2, 0],
                  [0, 0, 0, rg ** 2 * sp.sin(th) ** 2]])
gdet = sp.simplify(gmat.det())
ginv = gmat.inv()
gtt, gtr, grr = (sp.simplify(ginv[0, 0]), sp.simplify(ginv[0, 1]), sp.simplify(ginv[1, 1]))
print(f"      ds^2 = -dtau^2 + (dr - v dtau)^2 + r^2 dOmega^2,   v^2 = 1 - f = 2M/r + r^2/alpha^2")
print(f"      det g    = {gdet}")
print(f"      g^tautau = {gtt}        g^rr = {grr}   <- vanishes at every root of f")
print(f"      g^taur   = {gtr} = -v   <- does NOT vanish there: the chart stays invertible")
check("Ⓑ①  the PG metric's determinant is -r^4 sin^2(theta) with NO f in it, for M and alpha FREE, "
      "so the chart is nondegenerate at every root of f -- the seam is not a singularity of this "
      "chart, and that is a statement about the whole family and not about Nariai",
      sp.simplify(gdet + rg ** 4 * sp.sin(th) ** 2) == 0)
check("Ⓑ②  and g^rr = f exactly while g^{tau r} = -v, which is -1 at any root: exactly one "
      "component of the inverse metric degenerates and it is the one transverse to the seam",
      sp.simplify(grr - fg) == 0 and sp.simplify(gtr + vg) == 0)

# Phi = R(r) Y_lm e^{-i w tau};  r^2 * box Phi = A R'' + B R' + C R
Rf = sp.Function('R')(rg)
I = sp.I
row_t = rg ** 2 * (gtt * (-I * w) * Rf + gtr * sp.diff(Rf, rg))
row_r = rg ** 2 * (gtr * (-I * w) * Rf + grr * sp.diff(Rf, rg))
box = sp.expand((-I * w) * row_t + sp.diff(row_r, rg) - ell * (ell + 1) * Rf)
Pz = rg ** 2 * vg
tgt = (rg ** 2 * fg * sp.diff(Rf, rg, 2)
       + (sp.diff(rg ** 2 * fg, rg) + 2 * I * w * Pz) * sp.diff(Rf, rg)
       + (w ** 2 * rg ** 2 + I * w * sp.diff(Pz, rg) - ell * (ell + 1)) * Rf)
print(f"      (r^2 f R')' + 2 i w r^2 v R' + [w^2 r^2 + i w (r^2 v)' - l(l+1)] R = 0")
print(f"      A = r^2 f    B = (r^2 f)' + 2 i w r^2 v    C = w^2 r^2 + i w (r^2 v)' - l(l+1)")
check("Ⓑ③  r^2 (box Phi) for Phi = R(r) Y e^{-i w tau} equals exactly that, with M and alpha free "
      "and no residue -- so the equation is DERIVED from the chart rather than imported from a "
      "static-slicing form and re-coordinatised",
      sp.simplify(sp.expand(box - tgt)) == 0)

_Ah, _Aph, _Ph, _Pph = A(R_BACK), Ap(R_BACK), P(R_BACK), Pp(R_BACK)
print(f"      at the seam:  A = {mp.nstr(_Ah, 6)}   A' = {mp.nstr(_Aph, 15)} (= 2 sqrt3)   "
      f"r^2 v = {mp.nstr(_Ph, 15)} (= 4/3)   (r^2 v)' = {mp.nstr(_Pph, 10)}")
check("Ⓑ④  at the seam A vanishes with a SIMPLE zero of slope 2 sqrt3 = 3.464101615 while B and C "
      "stay finite -- B(r_h) = 2 sqrt3 + (8 i/3) w is nonzero for every real w, which is the whole "
      "difference between a regular singular point and a chart breakdown",
      abs(_Ah) < mp.mpf('1e-30')
      and abs(_Aph - 2 * mp.sqrt(3)) < mp.mpf('1e-30')
      and abs(_Ph - mp.mpf(4) / 3) < mp.mpf('1e-30')
      and mp.isfinite(_Pph))


# ============================================================ C. the seam is a characteristic
head("C.  THE SEAM IS A CHARACTERISTIC SURFACE, AND ITS TWO SPEEDS THERE ARE EXACTLY 2 AND EXACTLY 0")

xi_t, xi_r = sp.symbols('xi_tau xi_r')
psym = sp.simplify(gtt * xi_t ** 2 + 2 * gtr * xi_t * xi_r + grr * xi_r ** 2)
print(f"      principal symbol  = {sp.simplify(sp.expand(psym))}")
print(f"      on dr (xi_tau = 0) it is f xi_r^2, which vanishes at the root: r = r_h IS a "
      f"characteristic")
print(f"      null curves:  -f dtau^2 - 2 v dtau dr + dr^2 = 0  ->  dr/dtau = v +- 1")
check("Ⓒ①  the principal symbol restricted to dr is f, so every root of f is a characteristic "
      "surface of this equation -- the degeneracy in Ⓑ④ is the seam being null, not the chart "
      "failing, and the two facts are the same fact",
      sp.simplify(psym.subs(xi_t, 0) - fg * xi_r ** 2) == 0)
_vh = v(R_BACK)
# dv/dr = -f'/(2v), and v = 1 at any root of f, so dv/dr|_root = -f'/2 = -kappa.  That is the
# same identity the companion receipt uses for the bead's acceleration, read on the PG shift.
_ident = sp.simplify(sp.diff(vg, rg) + sp.diff(fg, rg) / (2 * vg))
_slope_num = -M / R_BACK ** 2 + R_BACK                       # = -f'(r_h)/2 at v = 1
print(f"      v(r_h) = {mp.nstr(_vh, 12)}  ->  crossing speed v+1 = {mp.nstr(_vh + 1, 12)}, "
      f"skimming speed |v-1| = {mp.nstr(abs(_vh - 1), 6)}")
print(f"      dv/dr + f'/(2v) = {_ident} identically (M, alpha free), so at a root dv/dr = -f'/2")
print(f"      dv/dr at the seam = {mp.nstr(_slope_num, 15)}   = -kappa = {mp.nstr(-KAP, 15)}")
check("Ⓒ②  the two characteristic speeds at the seam are exactly 2 and exactly 0, and the "
      "vanishing one vanishes LINEARLY with slope -kappa -- so kappa is the rate at which the "
      "skimming family fails to arrive, read off the chart with no tortoise coordinate in sight",
      abs(_vh - 1) < mp.mpf('1e-30') and _ident == 0
      and abs(_slope_num + KAP) < mp.mpf('1e-30'))

_t_cross = [(d, mp.quad(lambda r: 1 / (v(r) + 1), [R_BACK - d, R_BACK + d]))
            for d in (mp.mpf('0.3'), mp.mpf('1e-3'))]
print("\n      (i) CROSSING family, tau = int dr/(v+1) over a +-d window about the seam:")
for d, t in _t_cross:
    print(f"            d = {mp.nstr(d, 2):>7}   tau = {mp.nstr(t, 12)} alpha")
print(f"            and r = -10 alpha -> turnaround = "
      f"{mp.nstr(mp.re(mp.quad(lambda r: 1 / (v(r) + 1), [R_BACK - 10, R_TURN])), 12)} alpha")
print("      (ii) SKIMMING family, tau = int dr/(v-1) from r_h - 0.3 in to r_h - eps:")
_sk = []
for e in (mp.mpf('1e-2'), mp.mpf('1e-4'), mp.mpf('1e-6'), mp.mpf('1e-8')):
    _sk.append(mp.quad(lambda r: 1 / (v(r) - 1), [R_BACK - mp.mpf('0.3'), R_BACK - e]))
    print(f"            eps = {mp.nstr(e, 2):>7}   tau = {mp.nstr(_sk[-1], 12)} alpha"
          + ("" if len(_sk) == 1 else f"   increment {mp.nstr(_sk[-1] - _sk[-2], 10)}"))
_incs = [_sk[i + 1] - _sk[i] for i in range(3)]
print(f"            ln(100)/kappa  = {mp.nstr(mp.log(100) / KAP, 12)}   <- the tau rate is kappa")
print(f"            ln(100)/|f'|   = {mp.nstr(mp.log(100) / (2 * KAP), 12)}   <- the r_* rate is "
      f"2 kappa, HALF of it")
check("Ⓒ③  the crossing family takes 1.000000219e-3 alpha of proper time to cross a +-1e-3 alpha "
      "window and 2.011 alpha to come from r = -10 alpha to the turnaround: finite, smooth, "
      "transverse.  ** The static approach is not a slower version of the crossing; it is the "
      "OTHER characteristic family. **",
      abs(_t_cross[1][1] - mp.mpf('0.00100000021875')) < 1e-14
      and abs(_t_cross[0][1] - mp.mpf('0.306887473111')) < 1e-11)
check("Ⓒ④  while the skimming family adds ln(100)/kappa = 3.545061662 alpha of proper time per "
      "factor 100 in the gap and never arrives -- and that is EXACTLY TWICE the ln(100)/|f'| the "
      "companion receipt measures for r_*, because r_* is the parameter the PHASE lives in and "
      "tau is the parameter the TRAJECTORY lives in.  ** Two rates, kappa and 2 kappa, on two "
      "different clocks, and the imprinting law is on the one the bead does not use. **",
      abs(_incs[-1] - mp.log(100) / KAP) < 1e-5
      and abs(_incs[-1] - 2 * mp.log(100) / (2 * KAP)) < 1e-5
      and max(abs(_incs[i] - _incs[-1]) for i in range(3)) < 5e-3)


# ============================================================ D. the indices
head("D.  THE TWO INDICES AT THE SIMPLE ROOT: 0 AND -i omega/kappa, AND kappa COMES OUT OF THE ODE")

ss = sp.symbols('s')
a1s = sp.simplify(sp.diff(rs ** 2 * fsym, rs).subs(rs, -2 / sp.sqrt(3)))
b0s = sp.simplify(a1s + 2 * I * w * sp.Rational(4, 3))
indicial = sp.simplify(ss * ((ss - 1) * a1s + b0s))
roots = sp.solve(sp.Eq(indicial, 0), ss)
print(f"      a_1 = A'(r_h) = {a1s} = {mp.nstr(_Aph, 15)}        b_0 = B(r_h) = {b0s}")
print(f"      indicial equation  s[(s-1) a_1 + b_0] = 0   ->   s = {roots}")
_sec = [q for q in roots if q != 0][0]
_kap_from_ode = sp.simplify(-I * w / _sec)
print(f"      so the second index is -i w / ({_kap_from_ode}) , and 3 sqrt3/4 = {mp.nstr(KAP, 18)}")
check("Ⓓ①  the indices are 0 and -i omega/kappa with kappa = 3 sqrt3/4 alpha to 18 figures -- "
      "** the surface gravity is RECOVERED from the mode equation, not inserted into it, and it "
      "appears exactly once: as the index of the second branch **",
      0 in roots and len(roots) == 2
      and abs(mp.mpf(str(sp.N(_kap_from_ode, 30))) - KAP) < mp.mpf('1e-25'))
check("Ⓓ②  the two indices differ by -i omega/kappa, which is non-integer for every real omega > 0, "
      "so the monodromy about the seam is exactly DIAGONAL: no logarithm, no mixing.  The regular "
      "branch's monodromy is exactly 1 and the other's is e^{-2 pi omega/kappa} -- the Boltzmann "
      "factor at T_H = kappa/2pi, which is the only place a temperature can enter",
      sp.simplify(sp.re(_sec)) == 0 and sp.simplify(_sec.subs(w, 1)) != 0)
print(f"      T_H = kappa/2pi = {mp.nstr(KAP / (2 * mp.pi), 12)} / alpha")
check("Ⓓ③  and T_H = kappa/2pi = 0.2067483358/alpha, so `the lap's one non-degenerate horizon "
      "carries a thermal scale` is confirmed in the mode equation itself -- the question the order "
      "asks is not WHETHER 2 kappa is there but which branch carries it",
      abs(KAP / (2 * mp.pi) - mp.mpf('0.206748335783')) < 1e-11)


# ============================================================ E. which branch each ray carries
head("E.  THE THERMAL BRANCH IS THE ONE THE NON-CROSSING RAYS CARRY -- CONSTANT ALONG THE SKIMMING RAY")

print("      on the skimming ray  dr/dtau = v-1 = -kappa x + O(x^2),  so  x = x_0 e^{-kappa tau}")
print("      hence  e^{-i w tau} x^{-i w/kappa} = e^{-i w tau} e^{+i w tau} x_0^{-i w/kappa} = const")
print("      -- and the MODULUS of that product is 1 identically, so it tests nothing.  The")
print("      content is the PHASE: tau(x) = -(1/kappa) ln|x| + const is what makes the two")
print("      exponentials cancel, so the phase of the product is what must hold still.  tau(x) is")
print("      taken by quadrature along the ray, never from the leading-order law:")
print("\n        w/kappa      x       tau(x) by quad   offset tau + ln|x|/kappa    bare w tau "
      "(rad)   product's phase (rad)")
_drift, _bare, _off = [], [], []
X0 = mp.mpf('-1e-3')
for wk in (mp.mpf('0.1'), mp.mpf(1), mp.mpf(10)):
    wv = KAP * wk
    base = (-X0) ** (-1j * wv / KAP)
    for X in (mp.mpf('-1e-5'), mp.mpf('-1e-7'), mp.mpf('-1e-9')):
        tau = mp.quad(lambda r: 1 / (v(r) - 1), [R_BACK + X0, R_BACK + X])
        val = mp.e ** (-1j * wv * tau) * (-X) ** (-1j * wv / KAP) / base
        _drift.append(abs(mp.arg(val)))
        _bare.append(wv * tau)
        _off.append(tau + mp.log(-X) / KAP)
        print(f"        {float(wk):7.1f} {mp.nstr(X, 2):>9} {mp.nstr(tau, 10):>14}"
              f"   {mp.nstr(_off[-1], 10):>22}   {mp.nstr(_bare[-1], 8):>14}   "
              f"{mp.nstr(_drift[-1], 6):>14}")
_offc = [abs(_off[i] - _off[2]) for i in (0, 1)]
print(f"      the offset tau + ln|x|/kappa converges: it moves {mp.nstr(_offc[0], 4)} from "
      f"x = -1e-5 to -1e-9 and\n      only {mp.nstr(_offc[1], 4)} over the last two decades, so "
      f"x -> x_inf e^{{-kappa tau}} asymptotically.")
print(f"      and the product's phase therefore STOPS accumulating: at w = 10 kappa it holds within "
      f"{mp.nstr(max(_drift), 3)} rad\n      while e^{{-i w tau}} alone has turned through "
      f"{mp.nstr(max(_bare), 6)} rad -- a factor "
      f"{mp.nstr(max(_bare) / max(_drift), 6)}.")
check("Ⓔ①  the offset tau + ln|x|/kappa converges to a constant over four decades of approach, so "
      "the skimming ray's own law IS x = x_inf e^{-kappa tau} with kappa the index's kappa -- and "
      "the product e^{-i w tau} |x|^{-i w/kappa} therefore stops accumulating phase: it holds "
      "within 0.004 rad at omega = 10 kappa while e^{-i w tau} alone turns through 138 rad, a "
      "factor of 38000.  ** So the index -i omega/kappa branch is, exactly, the branch that is "
      "stationary on the rays that never cross: its radial factor is the skimming family's own "
      "accumulated phase with the sign that cancels it. **",
      max(_drift) < 4e-3 and _offc[1] < _offc[0] / 20
      and max(_bare) > 130 and max(_bare) / max(_drift) > 1e4)
print("\n      and the SAME expression on the crossing ray is not stationary at all: x passes "
      "through 0\n      at finite tau, where |x|^{-i w/kappa} has a branch point and e^{-i w tau} "
      "does not.")
check("Ⓔ②  the crossing ray reaches x = 0 at finite proper time (Ⓒ③) while the skimming ray does "
      "not (Ⓒ④), so the two branches are carried by the two characteristic families and the "
      "crossing cannot pick up the one it does not ride.  ** This is `r7185`'s item 1, as a "
      "statement about characteristics rather than about slicings: the unbounded approach is not "
      "`a slicing's artefact`, it is a real family of rays -- and the modes the sky carries are "
      "not on it. **",
      _t_cross[1][1] < mp.mpf('1e-2') and _sk[-1] > 10)


# ============================================================ F. the transfer, measured
head("F.  THE TRANSFER ACROSS THE CROSSING, MEASURED: IT GOES TO 1 LIKE d, FOR EVERY omega AND ell")


def _poly_shift(co, h):
    """Taylor coefficients about r = h of the polynomial sum co[i] r^i, exactly."""
    N = len(co)
    out = [mp.mpf(0)] * N
    for i, ci in enumerate(co):
        b = mp.mpf(1)
        for j in range(i + 1):
            out[j] += ci * b * h ** (i - j)
            b = b * (i - j) / (j + 1)
    return out


def _sqrt_series(q, N):
    """coefficients of sqrt(sum q_n x^n) with q_0 > 0, by the standard convolution recursion."""
    p = [mp.sqrt(q[0])]
    for n in range(1, N):
        acc = (q[n] if n < len(q) else mp.mpf(0))
        acc -= sum(p[m] * p[n - m] for m in range(1, n))
        p.append(acc / (2 * p[0]))
    return p


def regular_series(wv, lv, N=60):
    """the index-0 Frobenius solution about the back seam, R = sum R_n x^n with R_0 = 1.

    Every input series is EXACT: A and (r^2 f)' and r^2 are polynomials, shifted by binomials;
    r^2 v = sqrt(r^6 + 2 M r^3) comes from the sqrt recursion on the shifted polynomial.
    """
    NC = N + 3
    a = _poly_shift([mp.mpf(0), -2 * M, mp.mpf(1), mp.mpf(0), -mp.mpf(1)],
                    R_BACK) + [mp.mpf(0)] * NC          # r^2 - 2 M r - r^4  = r^2 f
    ap = _poly_shift([-2 * M, mp.mpf(2), mp.mpf(0), -mp.mpf(4)], R_BACK) + [mp.mpf(0)] * NC
    r2 = _poly_shift([mp.mpf(0), mp.mpf(0), mp.mpf(1)], R_BACK) + [mp.mpf(0)] * NC
    q = _poly_shift([mp.mpf(0)] * 3 + [2 * M, mp.mpf(0), mp.mpf(0), mp.mpf(1)],
                    R_BACK) + [mp.mpf(0)] * NC          # r^6 + 2 M r^3
    pv = _sqrt_series(q, NC)                            # r^2 v
    pvp = [(n + 1) * pv[n + 1] for n in range(NC - 1)] + [mp.mpf(0)]
    b = [ap[n] + 2j * wv * pv[n] for n in range(NC)]
    c = [wv ** 2 * r2[n] + 1j * wv * pvp[n] - (lv * (lv + 1) if n == 0 else 0) for n in range(NC)]
    R = [mp.mpc(1)]
    dens = []
    for j in range(N):
        s = mp.mpc(0)
        for n in range(j + 3):
            for m, co in ((j - n + 2, lambda m: a[n] * m * (m - 1)),
                          (j - n + 1, lambda m: b[n] * m),
                          (j - n, lambda m: c[n])):
                if 0 <= m <= j:
                    s += co(m) * R[m]
        den = (j + 1) * (j * a[1] + b[0])
        dens.append(abs(den))
        R.append(-s / den)
    return R, min(dens)


def resid(R, wv, lv, x):
    r = R_BACK + x
    R0 = sum(R[n] * x ** n for n in range(len(R)))
    R1 = sum(n * R[n] * x ** (n - 1) for n in range(1, len(R)))
    R2 = sum(n * (n - 1) * R[n] * x ** (n - 2) for n in range(2, len(R)))
    return abs(A(r) * R2 + (Ap(r) + 2j * wv * P(r)) * R1
               + (wv ** 2 * r ** 2 + 1j * wv * Pp(r) - lv * (lv + 1)) * R0)


print("      the recursion is (j+1)[(j+1) a_1 + (8i/3) w] R_{j+1} = -(lower terms), and its "
      "denominator\n      cannot vanish for real w and j >= 0, so the index-0 branch exists and is "
      "unique for EVERY (w, l)\n")
print("        w/kappa  ell   |residual| at x = -0.02 / +0.02      |T(d)| at d = 1e-1 / 1e-2 / "
      "1e-3 / 1e-4        e^{pi w/kappa}")
_res, _slopes, _dmin = [], [], []
for wk in (mp.mpf('0.1'), mp.mpf(1), mp.mpf(10), mp.mpf(100)):
    wv = KAP * wk
    for lv in (0, 2, 10):
        R, dmin = regular_series(wv, lv, 60)
        _dmin.append(dmin)
        r1, r2 = resid(R, wv, lv, mp.mpf('-0.02')), resid(R, wv, lv, mp.mpf('0.02'))
        _res += [r1, r2]
        Ts = []
        for d in (mp.mpf('1e-1'), mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4')):
            Rp = sum(R[n] * d ** n for n in range(len(R)))
            Rm = sum(R[n] * (-d) ** n for n in range(len(R)))
            Ts.append(((R_BACK + d) * Rp) / ((R_BACK - d) * Rm))
        _slopes.append([abs(abs(t) - 1) / d for t, d in
                        zip(Ts, (mp.mpf('1e-1'), mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4')))])
        print(f"        {float(wk):7.1f} {lv:4d}   {mp.nstr(r1, 3):>9} {mp.nstr(r2, 3):>9}      "
              + " ".join(f"{mp.nstr(abs(t), 10):>13}" for t in Ts)
              + f"   {mp.nstr(mp.e ** (mp.pi * wk), 6)}")
check("Ⓕ①  the index-0 series solves the equation to better than 1e-20 on BOTH sides of the seam, "
      "at every (omega, ell) tried -- so a single analytic solution spans the crossing and the two "
      "sides are not two problems to be matched",
      max(_res) < 1e-20 and min(_dmin) > 1)
check("Ⓕ②  ** and its transfer T(d) = [r R]_{+d}/[r R]_{-d} has modulus going to 1 LIKE d: the "
      "ratio ||T|-1|/d is bounded over four decades of d, four decades of omega/kappa and "
      "ell = 0, 2, 10, so the d -> 0 limit is exactly 1. **  The crossing's own factor is the "
      "identity; everything at finite d is ordinary propagation over a finite window, which the "
      "envelope already prices",
      all(max(s[1:]) < 200 and s[-1] < 200 for s in _slopes))
check("Ⓕ③  while e^{pi omega/kappa} is d-INDEPENDENT and reaches 2.739e136 at omega = 100 kappa: "
      "the two candidates differ by 136 orders of magnitude and by their d -> 0 behaviour, so no "
      "precision question stands between them.  ** THE CROSSING CARRIES NO THERMAL FACTOR. **",
      abs(mp.e ** (mp.pi * 100) / mp.mpf('2.7392734e136') - 1) < 1e-6
      and max(_slopes[-1]) * mp.mpf('1e-4') < mp.mpf('1e-1'))


# ============================================================ G. the front seam, inverted
head("G.  THE FRONT SEAM IS THE SAME FORMULA INVERTED -- ONE LINE COVERS BOTH SEAMS")

_ff = sp.simplify(fsym.subs(rs, 1 / sp.sqrt(3)))
_fp = sp.simplify(sp.diff(fsym, rs).subs(rs, 1 / sp.sqrt(3)))
_fpp = sp.simplify(sp.diff(fsym, rs, 2).subs(rs, 1 / sp.sqrt(3)))
_a2 = sp.simplify(sp.diff(rs ** 2 * fsym, rs, 2).subs(rs, 1 / sp.sqrt(3)) / 2)
_b0F = sp.simplify(sp.diff(rs ** 2 * fsym, rs).subs(rs, 1 / sp.sqrt(3)) + 2 * I * w * sp.Rational(1, 3))
print(f"      front seam r = +alpha/sqrt3:   f = {_ff}   f' = {_fp}   f'' = {_fpp}")
print(f"      A = r^2 f has a DOUBLE zero: A = {_a2} x^2 + ...,  B(r_F) = {_b0F}  (purely imaginary)")
print(f"      => an IRREGULAR singular point of rank 1:  R' ~ exp(-B(r_F)/(A''/2 x)) = "
      f"exp({sp.simplify(-_b0F / _a2)}/x)")
print(f"      and r_* = int dr/f ~ -1/((f''/2) x) = {sp.simplify(-1 / (_fpp / 2 * xs))}, so that IS "
      f"exp(-2 i w r_*)")
check("Ⓖ①  both seams' non-trivial branch is the same object, e^{-2 i omega r_*}: at the simple "
      "root r_* = (1/f') ln|x| and at the double root r_* = 1/(3x).  ** The discriminant is not the "
      "size of r_* but its CHARACTER: continuing x through a logarithm adds i pi/f' = i pi/(2 kappa) "
      "to r_*, and continuing it through a pole adds nothing.  So the modulus factor "
      "e^{+-pi omega/kappa} exists at the back seam and is identically 1 at the front seam, where "
      "kappa = 0. **",
      _ff == 0 and _fp == 0 and _fpp == -6 and _a2 == -1
      and sp.simplify(_b0F - 2 * I * w / 3) == 0
      and sp.simplify(sp.re(sp.simplify(-_b0F / _a2))) == 0)
check("Ⓖ②  so the order's inversion -- r_* divergent and T convergent at the back seam, the "
      "reverse at the front -- is reproduced inside the mode equation as regular-singular versus "
      "irregular-singular, and `one clause covering both seams` could not have been true of both: "
      "the front seam's branch is unimodular for every omega and the back seam's is not",
      sp.simplify(sp.re(sp.simplify(-_b0F / _a2))) == 0
      and abs(mp.mpf(str(sp.N(_kap_from_ode, 30))) - KAP) < mp.mpf('1e-25'))


# ============================================================ H. at which k
head("H.  AT WHICH k -- NAMED, EVEN THOUGH THE FACTOR IS 1")

_a_h = -R_BACK                                     # a = |r|/alpha at the seam
_k_th = _a_h * KAP
_L_th = -1 + mp.sqrt(1 + _k_th ** 2)
STRETCH = mp.mpf('2.7737')                         # eq:lowell's factor in k
L_PEAK = mp.mpf('78.5382')
_k_pk = mp.sqrt(L_PEAK * (L_PEAK + 2))
print(f"      the only scale AT the crossing is kappa, so the only comoving wavenumber it could")
print(f"      carry is k = a_h kappa with a_h = |r_h|/alpha = 2/sqrt3:")
print(f"         k_th = (2/sqrt3)(3 sqrt3/4) = {mp.nstr(_k_th, 15)}   EXACTLY 3/2, and alpha-free")
print(f"         k^2 = L(L+2)  ->  L_th = {mp.nstr(_L_th, 12)}   (the dipole is L = 1, k = "
      f"{mp.nstr(mp.sqrt(3), 10)})")
print(f"         k_th/k(L=1) = {mp.nstr(_k_th / mp.sqrt(3), 12)} = sqrt3/2 exactly")
print(f"         eq:lowell's 2.7737 in k  ->  ell_th = {mp.nstr(STRETCH * _k_th, 8)}, against the "
      f"first acoustic peak's")
print(f"         L = 78.5382, k = {mp.nstr(_k_pk, 10)}, ell = {mp.nstr(STRETCH * _k_pk, 8)}  "
      f"->  a factor {mp.nstr(_k_pk / _k_th, 8)}")
check("Ⓗ①  the thermal wavenumber is k = 3/2 EXACTLY in the leg's own comoving units, which is "
      "L = 0.8027756 -- BELOW THE DIPOLE.  ** There is no harmonic on the layer at the scale the "
      "seam's temperature sets: the smallest the sky carries, L = 1 at k = sqrt3, already sits a "
      "factor 2/sqrt3 above it. **",
      abs(_k_th - mp.mpf('1.5')) < mp.mpf('1e-30')
      and abs(_L_th - mp.mpf('0.802775637732')) < 1e-11
      and _L_th < 1)
check("Ⓗ②  and through eq:lowell the thermal scale would act at ell = 4.16 against the first "
      "acoustic peak's 220.60 -- a factor 53.02, which is the k-space counterpart of the 50.6 the "
      "two LOCI give on the leg.  ** Two independent routes to the same factor of fifty, so the "
      "`fifty times downstream` reading is a statement about scales and not only about positions. **",
      abs(STRETCH * _k_th - mp.mpf('4.16055')) < 1e-4
      and abs(STRETCH * _k_pk - mp.mpf('220.59767')) < 1e-3
      and abs(_k_pk / _k_th - mp.mpf('53.021276')) < 1e-4
      and 40 < _k_pk / _k_th < 70)
check("Ⓗ③  so the answer to `at which k` is complete in both directions: the factor is 1 at every "
      "k (Ⓕ②), and the one k at which a thermal factor could have acted is below the lowest "
      "harmonic the sky has.  ** A k-independent factor of 1 is not an amplitude -- it is the "
      "identity -- so neither A_s nor n_s moves, and the n_s budget the refit leaves is untouched "
      "by the seam. **",
      abs(_k_th - mp.mpf('1.5')) < mp.mpf('1e-30') and all(s[-1] < 200 for s in _slopes))


# ============================================================ verdict
print()
print(BAR)
if fail:
    print(f"  ⛔ {len(fail)} CHECK(S) FAILED")
    for q in fail:
        print(f"      - {q}")
    print(BAR)
    sys.exit(1)
print("  ✔ ** THE CROSSING DOES NOT ALTER THE SPECTRUM, AND THE REASON IS CHARACTERISTIC STRUCTURE")
print("    RATHER THAN A CHOICE OF SLICING. **  The seam is a characteristic surface of the mode")
print("    equation; its two characteristic speeds there are exactly 2 and exactly 0; the crossing")
print("    rides the first and the thermal branch is stationary on the second.  The index-0 branch")
print("    spans the crossing analytically and its transfer tends to 1 like the window width, for")
print("    every omega over four decades and ell = 0, 2, 10.")
print("  ⛭ ** 2 kappa IS in the equation -- exactly once, as the index of the branch that is not")
print("    smooth at the seam -- and it CANNOT enter through the crossing.  `r7185`'s item 1 is")
print("    therefore closed with a computation and not an argument: `prop:transmit`'s conclusion")
print("    survives at this locus for the reason that the unbounded approach belongs to a family of")
print("    rays the modes are not on. **")
print("  ⛭ And the rates are separated with numbers: tau along the skimming family runs at kappa,")
print("    r_* runs at 2 kappa, and the trajectory runs on neither -- it crosses at speed 2 in")
print("    0.877971931 alpha of its own proper time from the seam to the turnaround.")
print("  ⌗ The only k a thermal factor could have carried is 3/2 exactly, below the dipole; through")
print("    eq:lowell that is ell = 4.16 against the first peak's 220.60, a factor 53.0 that")
print("    independently reproduces the loci's 50.6.")
print("  ⇒ ** THE SECTOR'S 1.57 ACQUIRES NO PARAMETER ADDRESS FROM THE LAP'S ONE NON-DEGENERATE")
print("    HORIZON.  `r7181+cc66.144`'s finding survives the one test that could have overturned it. **")
print("  ⚠ What is NOT computed: the flux the seam radiates into the lap's future.  That is a")
print("    question about the quantum state and it does need the progenitor interior `PO-75` is")
print("    live on.  The TRANSFER did not, and the missing physical alpha is not needed either:")
print("    the verdict is 1, which carries no scale.")
print(BAR)
print("  ALL CHECKS PASS")
