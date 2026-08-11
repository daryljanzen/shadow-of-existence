#!/usr/bin/env python3
"""
L-149w — `E·4`, "THE RADIATION-FREE RATE AS THE STANDING DISCRIMINATOR (THE KNOB-FREE-NESS TEST)".
BOTH THINGS IT OWES ARE DELIVERED.  ITS SHARP QUESTION -- *is $\\rho_r/\\rho_m\\approx2$ a measured datum
like $\\eta$, or a hidden knob?* -- HAS A THIRD ANSWER, AND IT IS THE RIGHT ONE.

** IT IS NEITHER.  $\\rho_r/\\rho_m\\approx2$ IS A RE-EXPRESSION OF THE ONE FITTED QUANTITY,
$z_{\\mathrm{onset}}$, IN UNITS OF A MATTER DENSITY THIS CONSTRUCTION DOES NOT DETERMINE. **

The knob-freeness -- the load-bearing half -- survives untouched: $z_{\\mathrm{onset}}$ does not move
with $H_0$, so it cannot be absorbing the Hubble tension.  ** What does not survive is the EXACTNESS
of "about twice matter--radiation equality": that factor is $2.00$ at $h\\simeq0.68$ and $1.71$ at
$h=0.73$, and the papers quote the first while arguing the cosmology fits at the second. **

  PART 1  What `E·4` owes, and where each half was delivered.
  PART 2  ** THE KNOB-FREE HALF: $z_{\\mathrm{onset}}$ does not move.  Confirmed, and it is exact. **
  PART 3  ** THE RATIO IS NOT A SECOND DATUM: it is $z_{\\mathrm{onset}}$ divided by something CR
          does not compute. **
  PART 4  ** THE $14\\%$, AND WHICH $H_0$ THE CORPUS'S "TWICE EQUALITY" IS READ AT. **
  PART 5  What `L-149` becomes, and what `F·1` inherits.

Run: python3 L149w_the_factor_of_two_is_a_unit.py       (numpy, scipy)
"""
import os

import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

print(__doc__.split("Run:")[0])
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))

c = 299792.458
Om = 0.3066            # the corpus's own DESI DR2 best fit, dimensionless
wb, wg = 0.02237, 2.47e-5
wr = 4.15e-5           # photons + three massless neutrinos, physical, fixed by T_CMB
wm_planck = 0.1430     # the CMB-inferred PHYSICAL matter density
zrec = 1090.0
THETA = 0.0104085
R0 = 3*wb/(4*wg)


def cs(z):
    return c/np.sqrt(3*(1+R0/(1+z)))


def H(z, H0):
    return H0*np.sqrt(Om*(1+z)**3 + (1-Om))        # RADIATION-FREE


def DM(H0):
    return quad(lambda z: c/H(z, H0), 0, zrec, limit=400)[0]


def rs(H0, z_on):
    return quad(lambda u: cs(np.exp(u)-1)/H(np.exp(u)-1, H0)*np.exp(u),
                np.log(1+zrec), np.log(1+z_on), limit=400)[0]


def z_onset_of(H0):
    return brentq(lambda z: rs(H0, z)/DM(H0) - THETA, 2000., 40000., xtol=1e-3)


# =====================================================================
print("=" * 78)
print("PART 1 — WHAT E·4 OWES, AND WHERE EACH HALF WAS DELIVERED")
print("=" * 78)
idx = open(os.path.join(ROOT, 'receipts', 'INDEX.md'), encoding='utf-8').read()
OWED = [
    ("the rate confronted against the expansion history",
     'P15_desi_dr2_confrontation', "DESI DR2, 13 measurements / 7 tracers, chi2/dof = 1.00"),
    ("the knob-free-ness test (z_onset vs H0)",
     'P15_zonset_determinations', "the angle-pinned determination, H0-independent to 5 digits"),
]
print(f"  {'what E-4 owes':>46} {'registered?':>12} {'as':>44}")
for what, stem, how in OWED:
    print(f"  {what:>46} {('** yes **' if stem in idx else 'NO'):>12} {how:>44}")
assert all(stem in idx for _, stem, _ in OWED)
print()
for s in [
 "⌗ ** BOTH HALVES ARE BUILT AND REGISTERED, so `E·4` is not waiting on a computation. **  *What it",
 "   is waiting on is its own sharp question, which the register carries in capitals and the papers",
 "   answer only in passing.*",
 "",
 "⚠ *One bookkeeping note that belongs in the strike: the knob-free test's own script,",
 "`hubble_build/verify_rate_knobfree.py`, is **not a registered receipt and is cited nowhere**.  The",
 "claim it carries IS receipted -- by `P15_zonset_determinations`, whose declared scope is the",
 "`sec:tensions` second-check paragraph -- so nothing is unbacked.  ** But the two hold DIFFERENT",
 "quantities fixed, and that is the whole of what follows. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE KNOB-FREE HALF, CONFIRMED FROM THE RATE ITSELF")
print("=" * 78)
print(f"  the radiation-free rate: H(z) = H_0 sqrt(Om (1+z)^3 + 1 - Om), Om = {Om}")
print(f"  {'H_0':>8} {'z_onset from the measured angle':>34} {'100 theta_* there':>20}")
zs = []
for H0 in (67.4, 70.0, 73.0, 74.0):
    z = z_onset_of(H0)
    zs.append(z)
    print(f"  {H0:>8.1f} {z:>34.1f} {100*rs(H0, z)/DM(H0):>20.5f}")
print()
print(f"  ** spread in z_onset across H_0 = 67.4..74: {max(zs)-min(zs):.2f} in {np.mean(zs):.0f} "
      f"-- i.e. NONE **")
assert max(zs) - min(zs) < 1.0
print()
for s in [
 "⇒ ** SO THE FITTED QUANTITY CANNOT BE ABSORBING THE HUBBLE TENSION: it does not move between the",
 "   two values of $H_0$ the tension is between. **  *$H_0$ is a common factor in both $\\rs$ and",
 "   $D_M$ once radiation leaves the rate, so it cancels from $\\theta_*=\\rs/D_M$ exactly.*",
 "",
 "✔ ** THAT IS `E·4`'s LOAD-BEARING CLAIM AND IT STANDS, unqualified, at every $H_0$ in the range. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE RATIO IS NOT A SECOND DATUM")
print("=" * 78)
z_on = zs[0]
print("  WHAT THE CONSTRUCTION ACTUALLY USES, quantity by quantity:")
print(f"  {'quantity':>26} {'enters through':>30} {'H_0-free?':>12}")
for a, b, d in [
    ("Omega_m (dimensionless)", "the rate H(z); fitted to BAO", "by construction"),
    ("omega_b, omega_gamma", "the sound speed c_s(z)", "yes -- physical"),
    ("z_onset", "the lower limit of the r_s integral", "** yes -- shown above **"),
    ("omega_m (physical)", "** NOTHING **", "--"),
]:
    print(f"  {a:>26} {b:>30} {d:>12}")
print()
for s in [
 "⇒⇒ ** THE PHYSICAL MATTER DENSITY $\\omega_m=\\Omega_m h^2$ ENTERS NO PREDICTION THIS COSMOLOGY MAKES.",
 "   The rate carries $\\Omega_m$; the sound speed carries $\\omega_b$ and $\\omega_\\gamma$, both measured",
 "   directly and framework-free; and that is the whole list. **",
 "",
 "⌗ ** BUT $\\rho_r/\\rho_m$ AT ONSET IS $\\omega_r(1+z_{\\mathrm{onset}})/\\omega_m$, AND EQUALITY IS",
 "   $1+z_{\\mathrm{eq}}=\\omega_m/\\omega_r$. **  *Both divide by the one quantity the construction does",
 "   not determine.*  ⇒ ***So \"$\\rho_r/\\rho_m\\approx2$\" is not a second inherited number standing",
 "   beside $z_{\\mathrm{onset}}$: it is $z_{\\mathrm{onset}}$ itself, re-expressed in units of an",
 "   imported density.  There is ONE fitted quantity, and the paper says so; the ratio is its",
 "   restatement, and the paper does not say that.***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE 14%, AND WHICH H_0 'TWICE EQUALITY' IS READ AT")
print("=" * 78)
print(f"  z_onset = {z_on:.0f}, fixed and H_0-free.  Now divide it by equality, two ways:")
print()
print("  (a) using the CMB-INFERRED physical density omega_m = %.4f (h-free, but derived in a"
      % wm_planck)
print("      radiation-included analysis):")
zeq_p = wm_planck/wr - 1
print(f"        1+z_eq = omega_m/omega_r = {zeq_p+1:.0f} ;  "
      f"rho_r/rho_m at onset = {(1+z_on)/(1+zeq_p):.3f}")
print()
print(f"  (b) using THIS cosmology's own densities -- Omega_m = {Om} at each H_0, so"
      " omega_m = Om h^2:")
print(f"  {'H_0':>8} {'omega_m = Om h^2':>18} {'1+z_eq':>10} {'rho_r/rho_m at onset':>22}")
rows = []
for H0 in (67.4, 68.0, 70.0, 73.0):
    wm = Om*(H0/100.0)**2
    ratio = (1+z_on)/(wm/wr)
    rows.append((H0, wm, ratio))
    print(f"  {H0:>8.1f} {wm:>18.4f} {wm/wr:>10.0f} {ratio:>22.3f}")
h_star = np.sqrt(wm_planck/Om)*100
print()
print(f"  ** the two readings coincide at H_0 = {h_star:.1f}, where Om h^2 reproduces the "
      f"CMB-inferred omega_m **")
print(f"  ** and at the DIRECTLY measured H_0 = 73 the ratio is {rows[-1][2]:.2f}, "
      f"{100*(1-rows[-1][2]/2.0):.0f}% below two **")
assert abs(rows[-1][2] - 1.72) < 0.05 and 67 < h_star < 69
print()
for s in [
 "⇒⇒ ** SO THE FACTOR OF TWO IS EXACT ONLY WHERE THIS COSMOLOGY'S OWN $(\\Omega_m,H_0)$ REPRODUCE THE",
 f"   CMB-INFERRED $\\omega_m$, WHICH IS AT $H_0\\simeq{h_star:.0f}$ -- and the papers' headline is that the",
 f"   cosmology fits at the DIRECTLY measured $H_0=73$, where the same ratio is ${rows[-1][2]:.2f}$. **",
 "",
 "⌗ ** WHAT IS AND IS NOT DAMAGED, and the distinction is the whole disposal. **",
 "   ✔ *knob-freeness*: untouched -- $z_{\\mathrm{onset}}$ is $H_0$-free, shown in PART 2.",
 "   ✔ *the $\\eta$-analogy*: untouched -- one inherited number, and it is $O(1)$ rather than tuned,",
 "     which is the comparison the papers actually draw against $\\eta\\sim6\\times10^{-10}$.",
 "   ✔ *the DESI confrontation*: untouched -- it uses $\\Omega_m$ and BAO ratios and never $\\omega_m$.",
 "   ⚠ *the exactness*: **\"about twice matter--radiation equality\" and \"$1+z_{\\mathrm{eq}}=3399$ is a",
 "     consequence and a check\" are statements at $h\\simeq0.68$**, and should say so.",
 "",
 "⌗⌗ ** AND THE CHECK IS WORTH MORE ONCE IT IS STATED PROPERLY, NOT LESS. **  *Read honestly it says:",
 "   the acoustic angle's $z_{\\mathrm{onset}}$ agrees with twice the CMB-inferred equality to better",
 "   than a per cent IF the two frameworks' matter densities agree -- so it is a CONSISTENCY between",
 "   an $H_0$-free CR quantity and a $\\Lambda$CDM-analysis quantity, and its residual is a measure of",
 "   how far the two analyses' $\\omega_m$ have to differ.  ** That is a sharper object than a",
 "   coincidence, and it is a place the construction could be pushed on. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — WHAT `L-149` BECOMES, AND WHAT `F·1` INHERITS")
print("=" * 78)
for s in [
 "✔ ** THE CONFRONTATION: delivered (DESI DR2, $\\chi^2/\\mathrm{dof}=1.00$, registered). **",
 "✔ ** THE KNOB-FREE TEST: delivered, and re-run here from the rate itself rather than trusted. **",
 "✔ ** THE SHARP QUESTION: answered, and with a third answer -- not a knob, not a second measured",
 "   datum, but the one fitted quantity in imported units. **",
 "⇒ ** `L-149` STRIKES. **",
 "",
 "⌗ ** WHAT `F·1` (`L-150`) INHERITS, RESTATED. **  *`F·1` asks the progenitor collapse to DERIVE",
 "   $\\rho_r/\\rho_m\\approx2$ rather than measure it.*  ** Its target is not the number two.  It is",
 f"   an $O(1)$ number in the band $1.7$--$2.0$, and the band is not a computational uncertainty --",
 "   it is the range the same $z_{\\mathrm{onset}}$ takes as the matter density is read at different",
 "   $H_0$. **  *A derivation landing at $1.8$ would be as much a success as one landing at $2.0$,",
 "   and a derivation quoted to two figures would be claiming a precision the target does not have.*",
 "",
 "⌗ *And the second thing `F·1` inherits is the sharper form of the check: what a collapse-energetics",
 "derivation would really be testing is whether $z_{\\mathrm{onset}}$ -- the angle-fixed, $H_0$-free",
 "quantity -- comes out right, since that is the thing the construction actually determines.*",
]:
    print("  " + s)
