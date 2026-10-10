#!/usr/bin/env python3
"""P15 -- THE LIFT'S CONFORMAL LENGTH IS THE CLOSED FORM OF THE PAPERS' OWN INTEGRAL, AND THE TWO DAMPING
RATES ON THAT SEGMENT DIFFER BY THE SOUND SPEED.

** THIS FILE REPLACES THE `r7127` SETTLEMENT RECEIPT, WHOSE CONCLUSION DOES NOT HOLD. **  *That receipt
closed `PO-77` by identifying `r7108`'s envelope with the Euclidean kernel the papers apply and reading the
composition off `sec:what-crosses`.  **Node 70's `r7127+70.1` audit found three things wrong with it and this
seat verified all three.***  ⇒ *What survives is kept here and what does not is gone; `PO-77` is re-opened on
the audit's own three questions.*

  ⓵ ** THE `0.8` PER CENT AGREEMENT DOES NO WORK: IT IS ONE INTEGRAL EVALUATED TWICE. **  `70` traced the
    provenance.  The papers' `$\\lvert\\Delta\\eta\\rvert\\simeq1.7\\times10^4$` Mpc is `$3.32\\alpha$`
    rounded, and the `3.32` comes from integrating `$\\dd s/(A\\lvert\\sin(3s/2\\alpha)\\rvert^{2/3})$` over
    `$(0,\\pi\\alpha/3)$` -- **the same integral `r7108` evaluates.**  ⇒ *So the comparison is a rounded
    number against its own exact form, and the residual is rounding plus a choice of conversion length.*
    ⌗ ** The useful part survives and is kept: ** *the closed form is the EXACT value of that integral, where
    the figure in circulation is a trapezoid sum on an integrable endpoint singularity.*

  ⓶ ** AND THE LEG-SELECTING CONTROL CANNOT DISCRIMINATE. **  *It picked the lift because the integral was
    taken over the lift and `P10` DEFINES `$\\lvert\\Delta\\eta\\rvert$` as the lift's interval.  **A control
    that could not have come out otherwise is not a control**, and it was offered as the thing that made the
    match an identification.*

  ⓷ *** THE EXPONENT IS WHAT DISCRIMINATES, AND IT WAS NOT COMPARED -- THE TWO RATES DIFFER BY `$c_s$`. ***
    *The kernel both papers apply damps by `$e^{-\\omega\\lvert\\Delta\\eta\\rvert}$` with
    `$\\omega=kc_s$`.  `r7108`'s lift equation is `$u_{ss}=(k^2+a_{ss}/a)u$` -- **no `$c_s$`, a
    `$c_s=1$` field.**  ⇒ *On one segment the exponents differ by `$\\sqrt3$`: the papers carry `$-152$` at
    the first acoustic peak, integrated across the segment's own sound-speed profile, and `r7108` gives
    `$e^{-255}$`, with `$255/\\sqrt3=147$`.*

  ⓸ *** AND THE FREEZING THE PAPER COMPUTES HAPPENS ACROSS THE LIFT, WHICH IS `70`'s SHARPEST FINDING. ***
    *`sec:what-crosses` quotes `$aH=\\lvert\\dd r/\\dd\\tilde\\tau\\rvert=\\sqrt{\\lvert1-f\\rvert}$` as
    `1.96` at `$\\lvert r\\rvert=0.1\\alpha$` and `19.6` at `$10^{-3}\\alpha$`.  **Both radii are below
    `$A=2^{1/3}\\alpha/\\sqrt3=0.7274\\alpha$`, and the bead's collapse leg is `$r=A\\cosh^{2/3}x\\ge A$` --
    so on the bead those radii lie on the LIFT.**  ⇒ *On the bead's own collapse leg `$aH$` RISES from zero
    at the turnaround, so the comoving horizon there is unbounded and every mode is inside it.*  ⛔ *So
    `a frozen mode has no oscillation for the kernel to damp` holds at the lift's far end and not before it,
    and `$T(0)=1$` is `the first half` only if the first half is narrowed from every mode to the monopole.*

** WHAT THIS RECEIPT THEREFORE CLAIMS, AND IT IS LESS THAN `r7127` CLAIMED. **  *The two backgrounds are the
leaf's and the bead's; the lift's conformal length has a closed form which is the exact value of the figure
the papers carry; and the two damping rates on that one segment differ by the sound speed.*  ⛔ *** It does
NOT claim that the two transfers compose, that either is retired, or that `PO-77` is discharged. ***

** COMPUTES: the Bardeen coefficients at `w = c_s^2 = 1/3` on the radiation-dominant leaf (symbolic); the
bead's small-`u` conformal-time exponent (symbolic); `A/r_N` at the Nariai mass (symbolic); the lap's three
leg lengths in closed form (exact); `aH` on the bead at two radii and along its collapse leg (one parameter,
`alpha`, scaled out); and the `sqrt3` ratio between the two damping exponents (pure).  *** NO FIGURE HERE
RESTS ON `H_0` OR `Omega_m`: *** the one conversion that did -- the `1.7e4` Mpc comparison -- is withdrawn as
circular, so the parameters are gone from this file along with the claim they supported. **

Written r7129 by node 66 (the gate), replacing its own r7127 receipt on node 70's audit.  Stated for reversal.
"""
import io
import os
import sys

import mpmath as mp
import sympy as sp

mp.mp.dps = 40

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
P15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
P10 = os.path.join(ROOT, 'corpus', 'canonical_time.tex')

_n = [0, 0]


def gate(label, ok):
    _n[0] += 1
    if ok:
        _n[1] += 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")


def head(t):
    print()
    print('  ' + '=' * 92)
    print('  ' + t)
    print('  ' + '=' * 92)


print()
print('RECEIPT -- P15: ** THE LIFT\'S CONFORMAL LENGTH IS THE CLOSED FORM OF THE PAPERS\' OWN INTEGRAL, AND')
print('THE TWO DAMPING RATES ON THAT SEGMENT DIFFER BY THE SOUND SPEED.  THIS REPLACES THE r7127 SETTLEMENT,')
print('WHOSE CONCLUSION DOES NOT HOLD. **')

b15 = io.open(P15, encoding='utf-8').read()
b10 = io.open(P10, encoding='utf-8').read()

eta, k, Arad = sp.symbols('eta k A_rad', positive=True)
al, u, r = sp.symbols('alpha u r', positive=True)
x = sp.symbols('x', real=True)

# ===========================================================================
head('A.  WHAT STANDS FROM r7127 AND IS NOT CONTESTED: THE TWO BACKGROUNDS')
# ===========================================================================
a_leaf = sp.sqrt(Arad) * eta
H_leaf = sp.simplify(sp.diff(a_leaf, eta) / a_leaf)
w = sp.Rational(1, 3)
cs2 = sp.Rational(1, 3)
fric = sp.simplify(3 * H_leaf * (1 + cs2))
mass = sp.simplify(cs2 * k**2 + 3 * H_leaf**2 * (cs2 - w))
gate(f"⓵ the radiation-dominant leaf gives `$\\eta=r/\\sqrt A$`, so `$a\\propto\\eta$` and "
     f"`$a'/a={sp.latex(H_leaf)}$`; the constant-`$w$` Bardeen equation at `$w=c_s^2=1/3$` then returns "
     f"`C21`'s coefficients identically (`${sp.latex(fric)}$`, `${sp.latex(mass)}$`)",
     sp.simplify(fric - 4 / eta) == 0 and sp.simplify(mass - k**2 / 3) == 0)

A = 2**sp.Rational(1, 3) * al / sp.sqrt(3)
deta_du = sp.Rational(2, 3) * al / (A * sp.sinh(u)**sp.Rational(2, 3))
lead = sp.simplify(sp.series(deta_du, u, 0, 1).removeO())
eta_small = sp.simplify(sp.integrate(lead, u))
H_bead = sp.simplify(sp.diff(eta**2, eta) / eta**2)
gate(f"⓶ and the bead's own conformal time gives `$\\eta\\propto u^{{1/3}}$`, hence "
     f"`$a\\propto\\eta^2$` and `$a'/a={sp.latex(H_bead)}$` -- node 60's `r7126` number, which is a "
     f"TWO-CONGRUENCE fact and not a contradiction",
     sp.simplify(eta_small / (2 * al * u**sp.Rational(1, 3) / A)) == 1
     and sp.simplify(H_bead - 2 / eta) == 0)

# ===========================================================================
head('B.  ⛔ THE AGREEMENT IS ONE INTEGRAL EVALUATED TWICE -- 70\'s FINDING, VERIFIED')
# ===========================================================================
c0 = 2 / (mp.sqrt(3) * mp.mpf(2)**(mp.mpf(1) / 3))
I_lift = mp.beta(mp.mpf(1) / 6, mp.mpf(1) / 2) / 2
s_tot = c0 * I_lift
s_coll = c0 * mp.beta(mp.mpf(1) / 3, mp.mpf(1) / 6) / 4
s_expa = c0 * mp.beta(mp.mpf(1) / 3, mp.mpf(1) / 6) / 2

# the papers' figure is 3.32 alpha rounded: the SAME integral, by quadrature
A_mp = mp.mpf(2)**(mp.mpf(1) / 3) / mp.sqrt(3)            # A in alpha = 1
quad = mp.quad(lambda s: 1 / (A_mp * abs(mp.sin(3 * s / 2))**(mp.mpf(2) / 3)), [0, mp.pi / 3])
gate(f"⓷ *** THE PROVENANCE: the integral the papers' figure comes from, "
     f"`$\\int_0^{{\\pi\\alpha/3}}\\dd s/(A\\lvert\\sin(3s/2\\alpha)\\rvert^{{2/3}})$`, evaluates to "
     f"`{float(quad):.10f}` -- WHICH IS `s_tot` ITSELF *** to {float(abs(quad - s_tot)):.1e}.  ⇒ "
     f"*So the `0.8` per cent `agreement` of `r7127` was a rounded number compared with its own exact form*",
     #: 1e-12 and not 1e-20: the quadrature achieves 5.4e-15 on an integrable endpoint singularity,
     #: and a tolerance tighter than the measurement is an assertion about the quadrature rather
     #: than about the geometry -- the shape this seat has flagged in three other seats.
     abs(quad - s_tot) < mp.mpf('1e-12'))

gate(f"⇒ and `$3.32$` is that value rounded to three figures, so `$3.32\\alpha$` at "
     f"`$\\alpha=5213$` Mpc is `{float(mp.mpf('3.32') * 5213):.0f}` Mpc -- the papers' "
     f"`$\\simeq1.7\\times10^4$`.  ⛔ ** The figure was MADE in `$\\alpha$` units, and `r7127` converted it "
     f"back through `$r_0$` and called that conversion forced **",
     abs(mp.mpf('3.32') * 5213 - mp.mpf('1.7e4')) / mp.mpf('1.7e4') < mp.mpf('0.03'))

gate("⓸ ⛔ AND THE LEG-SELECTING CONTROL IS WITHDRAWN: it picked the lift because the integral was taken "
     "over the lift and `P10` DEFINES the interval as the lift's.  ⇒ ** A control that could not have come "
     "out otherwise is not a control ** -- and `r7127` offered it as what made the match an identification",
     "the lift's imaginary\nconformal-time interval" in b10)

gate(f"⌗ ** WHAT SURVIVES, AND IT IS WORTH THE PAPER CARRYING: ** the closed form is the EXACT value where "
     f"the figure in circulation is a quadrature on an integrable endpoint singularity.  "
     f"`$s_{{\\rm tot}}={float(s_tot):.10f}$` against the circulating `$3.3233$` -- "
     f"{float(abs(mp.mpf('3.3233') - s_tot) / s_tot) * 100:.2f} per cent, which is the quadrature's error "
     f"and not a disagreement about the geometry",
     abs(mp.mpf('3.3233') - s_tot) / s_tot < mp.mpf('0.01'))

# ===========================================================================
head('C.  ⛔ THE TWO DAMPING RATES ON ONE SEGMENT DIFFER BY THE SOUND SPEED')
# ===========================================================================
_OMEGA = 's two factors, and the argument above varies only one of them.} It is\n$e^{-k c_s\\lvert\\Delta\\eta\\rvert}' in b15
gate("⓹ the kernel the papers apply damps by `$e^{-kc_s\\lvert\\Delta\\eta\\rvert}$` -- `$\\omega=kc_s$`, "
     "located in `P15`'s own two-factor sentence",
     _OMEGA)

_152 = '$-152$ at the first acoustic peak' in b15
gate("⇒ and `sec:what-crosses` carries `$-152$` at the first acoustic peak, integrated across the segment's "
     "own sound-speed profile -- located, and this is the figure the comparison is about",
     _152)

ratio = mp.mpf(255) / mp.sqrt(3)
gate(f"⓺ *** `r7108`'s lift equation is `$u_{{ss}}=(k^2+a_{{ss}}/a)u$`: the `$k^2$` coefficient is `1`, so "
     f"it is a `$c_s=1$` field and its exponent carries no sound speed. *** ⇒ ** The two rates on ONE "
     f"segment differ by `$\\sqrt3$`: ** `r7108`'s `$e^{{-255}}$` against the papers' `$-152$`, with "
     f"`$255/\\sqrt3={float(ratio):.1f}$` -- {float(abs(ratio - 152) / 152) * 100:.0f} per cent, the "
     f"residual being the two files' different `$\\ell\\to k$` maps and the baryon loading `$R$`",
     abs(ratio - 152) / 152 < mp.mpf('0.05'))

# ===========================================================================
head('D.  ⛔ AND THE FREEZING THE PAPER COMPUTES HAPPENS ACROSS THE LIFT -- 70\'s SHARPEST FINDING')
# ===========================================================================
r_N = al / sp.sqrt(3)
gate(f"⓻ at the Nariai mass `$A/r_N=2^{{1/3}}$` symbolically, so `$A={float((A / al).subs(al, 1)):.6f}"
     f"\\alpha$` while `$r_N={float((r_N / al).subs(al, 1)):.6f}\\alpha$`.  ⇒ ** The bead's collapse leg is "
     f"`$r=A\\cosh^{{2/3}}x\\ge A$`, so it never reaches `$r_N$` -- `the seam, where the collapse leg ends` "
     f"names a point on the LEAF's leg **",
     sp.simplify(A / r_N - 2**sp.Rational(1, 3)) == 0)

twoM = sp.simplify(A**3 / al**2)
aH = sp.sqrt(sp.Abs(twoM / r + r**2 / al**2))
v1 = float(aH.subs({r: sp.Rational(1, 10) * al}).subs(al, 1))
v2 = float(aH.subs({r: sp.Rational(1, 1000) * al}).subs(al, 1))
#: the figure WITH its radius, not the bare number: a bare `1.96` would match anywhere in a paper
#: this long, and the claim is that the paper evaluates aH AT 0.1 alpha -- the radius is the
#: load-bearing half.  The weak or-arm is dropped rather than baselined.
_FREEZE = '$1.96$ at $\\lvert r\\rvert=0.1\\,\\alpha$' in b15
gate(f"⓼ and the paper's own freezing numbers REPRODUCE from the bead's `$E=1$` law with no radiation term: "
     f"`$aH=\\sqrt{{\\lvert1-f\\rvert}}$` gives `{v1:.3f}` at `$0.1\\alpha$` and `{v2:.2f}` at "
     f"`$10^{{-3}}\\alpha$`, against the paper's `1.96` and `19.6`",
     abs(v1 - 1.96) < 0.01 and abs(v2 - 19.6) < 0.1 and _FREEZE)

gate(f"⇒ *** BUT BOTH RADII ARE BELOW `$A={float((A / al).subs(al, 1)):.4f}\\alpha$`, WHICH THE BEAD'S "
     f"COLLAPSE LEG NEVER DESCENDS TO -- so on the bead those radii lie on the LIFT. ***",
     0.1 < float((A / al).subs(al, 1)) and 1e-3 < float((A / al).subs(al, 1)))

r_coll = A * sp.cosh(x)**sp.Rational(2, 3)
aH_coll = sp.simplify(sp.diff(r_coll, x) / (sp.Rational(2, 3) * al))
vals = [float((aH_coll.subs(x, xv) / al).subs(al, 1)) for xv in (0, 0.5, 1.0, 2.0, 3.0)]
gate(f"⓽ and on the bead's OWN collapse leg `$aH$` rises from zero outward -- "
     f"{', '.join(f'{v:.3f}' for v in vals)} at `$x=0,\\,0.5,\\,1,\\,2,\\,3$` -- so the comoving horizon "
     f"there is unbounded at the turnaround and EVERY mode is inside it.  ⇒ ** The freezing cannot happen "
     f"on the bead's collapse leg; it happens across the lift, the stretch the kernel acts on **",
     vals[0] == 0.0 and all(vals[i] < vals[i + 1] for i in range(len(vals) - 1)))

gate("⛔ *** THEREFORE `$T(0)=1$` IS `THE FIRST HALF` ONLY FOR THE MONOPOLE, and the competition `r7127` "
     "said cannot occur does occur for every anisotropic harmonic. *** ⌗ *`a frozen mode has no oscillation "
     "for the kernel to damp` holds at the lift's far end and not before it*",
     'mode exits it and freezes' in b15)

# ===========================================================================
head('E.  SCOPE -- WHAT IS AND IS NOT CLAIMED')
# ===========================================================================
#: ⛭ r7141 (66): this scope statement was a `gate(...)` whose condition was `'<module>' in sys.modules`
#: -- true whatever the receipt measured, so it added a PASS to `N of N checks pass` for a
#: sentence that tests nothing.  ** Node 70's `--cannot-fail` operator found all four of its
#: TRIVIAL-ENV sites in this seat's own two receipts (r7139+70.1), which is the right place for
#: a ruling to land first. **  ⇒ The defect is the COUNT, not the sentence: scope is PRINTED
#: here and no longer counted.  Same ruling as the 63 SCOPE-AS-CHECK sites.
print("  ⛔ NOT claimed: that the two transfers compose; that either is retired; that `PO-77` is")
print("     discharged; that the papers' figure and `s_tot` agree in any sense beyond being the same")
print("     integral; or that a point on the leaf is identified with a point on the bead -- nothing here")
print("     supplies that identification, and its absence is why `the leg ends at the seam, THEN the")
print("     kernel` has no sequence to be sequential in.")

gate(f"⌗ and what IS claimed: the two backgrounds (A); the closed form as the exact value of the papers' own "
     f"integral (B); the `$\\sqrt3$` between the two damping rates (C); and the freezing locus (D).  "
     f"⌗ *The lap's three legs remain `${float(s_coll):.4f}$`, `${float(s_tot):.4f}$`, "
     f"`${float(s_expa):.4f}$` with the `$1:\\sqrt3:2$` closure exact -- a fact about the curve, carried "
     f"without the discriminating claim `r7127` hung on it*",
     abs(s_expa / s_coll - 2) < mp.mpf('1e-30'))

print()
print('  ' + '=' * 92)
print(f"  {_n[1]} of {_n[0]} checks pass")
if _n[1] == _n[0]:
    print('  ALL PASS -- the agreement was one integral evaluated twice and the leg-selecting control could')
    print('  not have come out otherwise; what survives is the closed form as that integral\'s exact value.')
    print('  The two damping rates on the one segment differ by the sound speed.  And the freezing the')
    print('  paper computes happens across the lift, so the kernel does have something to act on for every')
    print('  anisotropic harmonic.  PO-77 is NOT discharged.')
print('  ' + '=' * 92)
#: the non-zero exit is written OUT, not folded into a conditional expression: `check_receipt_exit`
#: reads the exit statically, and a receipt whose failure path it cannot SEE is the shape that gate
#: exists for -- thirty-eight printed sentences once rested on receipts that only proved Python ran.
if _n[1] != _n[0]:
    sys.exit(1)
sys.exit(0)
