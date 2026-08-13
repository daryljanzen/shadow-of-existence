#!/usr/bin/env python3
"""
RECEIPT -- P1: ** ITEM 50 WORKED, AND THE SCOPING IS THE WHOLE CONTENT.  THE STATIC-FRAME BLUESHIFT AT
A STILL-COLLAPSING SURFACE IS FINITE AT EACH FINITE EXTERIOR TIME AND ** *** NOT UNIFORMLY BOUNDED *** **
-- IT GROWS AS e^{kappa t}, WITH THE SAME kappa THAT IS THE MECHANISM OF THERMALITY, AND THE PLANCK
VALUE IS REACHED IN ** MILLISECONDS ** FOR A STELLAR-MASS BODY. **

Built r2566+c54.207, lead `L-531`.  VEIN: `L-165` (PO-6, what a quantum of this geometry is).

===================================================================================================
** WHY THIS IS A SCOPING AND NOT A DEFENCE **
===================================================================================================

`FOR_54` item 50 routed a PARTIAL answer and said so: *"the claim available is 'finite at each finite
time', NOT 'bounded' -- and that difference is exactly what a referee in this area will press.  If it
goes in the paper it has to go in with the scoping attached, or it is an overclaim wearing a result's
clothes."*  ** This file is that scoping, computed. **

  ** ⓵ THE OBJECTION AS USUALLY POSED DOES NOT TRANSFER. **  The trans-Planckian problem is an
     objection to the BOGOLIUBOV construction -- late-time quanta traced backward to arbitrarily high
     frequency.  *P1 does not perform that construction; §Hawking's argument is causal and computes no
     mode functions.*  ⇒ ** So the transfer has to be made on other grounds or not at all. **

  ** ⓶ AND THERE IS A VERSION THAT NEEDS NO MODE-TRACING. **  A static observer outside a
     still-collapsing surface measures omega_loc = omega_inf / sqrt(f).  Near a simple root
     f ~ 2 kappa delta, so the factor goes as delta^{-1/2} and *diverges only AS the surface is
     reached* -- which §5 says never happens at finite exterior time.

  ** ⓷ ⛔ BUT NOT UNIFORMLY, AND THAT IS THE PART THAT IS EASY TO SKIP. **
     Radial infall at unit energy: dr/dt = -f sqrt(r_h/r) ~ -2 kappa delta
       ⇒  delta(t) ∝ e^{-2 kappa t}   ⇒   omega_loc/omega_inf ∝ ** e^{+kappa t} **
     ⇒ *** sup over exterior time is INFINITE.  "Finite at each finite t" and "bounded" are different
         statements and only the first is available. ***

  ** ⓸ ⛭⛭ AND THE RATE IS THE SAME kappa `L-526` CALLED THE MECHANISM OF THERMALITY. **
     *One exponential seen twice: once as what carries a mode's positive frequencies into a Planck
     spectrum, once as what carries the collapsing surface into the ultraviolet.*  ⇒ ** So the
     logarithm suppresses nothing: t_Planck-blueshift = kappa^{-1} ln(kappa^{-1}/t_P), which is
     MILLISECONDS at a stellar mass. **  *A "finiteness" reached in milliseconds is not a shield.*

===================================================================================================
** ⛔ WHAT IS NOT CLAIMED **
===================================================================================================

** Not that the blueshift is bounded ** -- the file exists to deny exactly that.  ** Not that the
framework is free of trans-Planckian sensitivity ** -- the late-time surface is not, and P1 now says
so in print rather than leaving the prior sentence ("needs no ultraviolet completion of gravity") to
be read as the stronger thing.  ** Not that the ultraviolet regime is benign **, which is not settled
here.  ** And not a temperature at either root ** -- `L-519` stays refused.

⚠ ** THE ONE SENTENCE THIS CLAUSE QUALIFIES IS PRE-EXISTING AND MUST SURVIVE. **  *If §Hawking's
"needs no ultraviolet completion of gravity and no modification of quantum theory" were ever deleted,
the new paragraph would be qualifying nothing and would read as a free-standing concession.*  PART 4
pins it present.

SETTINGS: none -- no instrument, no spectra.  Symbolic expansion of the Schwarzschild metric function
and the radial-infall coordinate speed, one ODE solved rather than quoted, an arithmetic of the
Planck-blueshift time from CODATA constants, and source checks.

rc=0 on success.  Run: python3 P1_the_transplanckian_claim_is_finite_at_each_finite_time_and_it_is_not_bounded.py
                        (sympy; ~6 s)
"""
import math
import os
import re
import sys

import sympy as sp

print(__doc__.split("rc=0")[0])

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
CORPUS = os.path.join(ROOT, 'corpus')
fail = []

r, rh, d, t, C1 = sp.symbols('r r_h delta t C1', positive=True)

# =====================================================================
print("=" * 78)
print("PART 1 — THE BLUESHIFT EXPONENT AT A SIMPLE ROOT, EXPANDED RATHER THAN QUOTED")
print("=" * 78)
f = 1 - rh / r
_ser = sp.expand(sp.series(f.subs(r, rh + d), d, 0, 3).removeO())
_lin = sp.simplify(sp.limit(_ser / d, d, 0))
_kappa = sp.simplify(_lin / 2)           # f ~ 2 kappa delta  =>  kappa = coeff/2
print(f"  f(r_h + delta) = {_ser}")
print(f"  linear coefficient = {_lin}    ** nonzero => SIMPLE root, and f ~ 2 kappa delta **")
print(f"  so kappa = {_kappa}            ( = 1/4M for Schwarzschild )")
_blue = sp.simplify(1 / sp.sqrt(_lin * d))
_exp = sp.simplify(sp.log(_blue.subs(rh, 1)) / sp.log(d))
print(f"  blueshift 1/sqrt(f) ~ {_blue}   ** power of delta = {_exp} **")
if _lin == 0:
    fail.append("the Schwarzschild horizon came out degenerate — PART 1's premise fails")
if sp.simplify(_exp + sp.Rational(1, 2)) != 0:
    fail.append(f"the blueshift power is {_exp}, not -1/2 — the routed scaling does not reproduce")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — AND THE APPROACH IN EXTERIOR TIME, SOLVED RATHER THAN ASSERTED")
print("=" * 78)
_drdt = sp.simplify(sp.series((-f * sp.sqrt(rh / r)).subs(r, rh + d), d, 0, 2).removeO())
print(f"  dr/dt = -f sqrt(r_h/r)  ->  near the root:  ddelta/dt = {_drdt}")
D = sp.Function('D')
_sol = sp.dsolve(sp.Eq(sp.Derivative(D(t), t), _drdt.subs(d, D(t))), D(t))
print(f"  {_sol}")
_rate = sp.simplify(sp.log(_sol.rhs / sp.Symbol('C1')) / t)
print(f"  ** delta(t) decays at rate {_rate} = -2 kappa **")
_blue_t = sp.simplify(1 / sp.sqrt(_lin * _sol.rhs.subs(sp.Symbol('C1'), rh)))
_grow = sp.simplify(sp.log(sp.simplify(_blue_t / _blue_t.subs(t, 0))) / t)
print(f"  ** so omega_loc/omega_inf grows at rate {_grow} = +kappa **")
print()
print("  *** SAME kappa AS THE THERMALITY EXPONENTIAL OF `L-526`.  One exponential, two readings. ***")
_ok_rate = sp.simplify(_rate + 2 * _kappa) == 0
_ok_grow = sp.simplify(_grow - _kappa) == 0
print(f"  decay rate is exactly -2 kappa : {_ok_rate}")
print(f"  growth rate is exactly +kappa  : {_ok_grow}")
if not _ok_rate:
    fail.append("delta does not decay at 2 kappa — the exponential identification fails")
if not _ok_grow:
    fail.append("the blueshift does not grow at kappa — the 'one exponential twice' claim fails")

print()
print("  ⛔ AND THE SUPREMUM, which is the whole scoping:")
_sup = sp.limit(_blue_t, t, sp.oo)
print(f"     lim_{{t->oo}} omega_loc/omega_inf = {_sup}")
print("     *** so the quantity is FINITE AT EACH FINITE t AND UNBOUNDED OVER t.  'Bounded' is NOT")
print("         the available claim, and the difference is not a technicality. ***")
if _sup != sp.oo:
    fail.append(f"the supremum came out {_sup} — the 'not uniformly bounded' scoping would be wrong")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — AND THE LOGARITHM SUPPRESSES NOTHING: THE PLANCK-BLUESHIFT TIME, IN SECONDS")
print("=" * 78)
G, c_l, hbar, Msun = 6.67430e-11, 2.99792458e8, 1.054571817e-34, 1.98892e30
tP = math.sqrt(hbar * G / c_l ** 5)
print(f"  t_P = {tP:.4e} s   (from CODATA G, c, hbar — not quoted)")
print()
print(f"  {'body':>34s} {'1/kappa (s)':>13s} {'ln(1/kappa/t_P)':>16s} {'t to Planck (s)':>17s}")
ROWS = [("one solar mass", 1.0), ("ten solar masses", 10.0),
        ("a 10^6 Msun nucleus", 1e6), ("M87*, 6.5x10^9 Msun", 6.5e9)]
_times = {}
for what, mr in ROWS:
    kinv = 4 * G * mr * Msun / c_l ** 3
    lnB = math.log(kinv / tP)
    tt = kinv * lnB
    _times[what] = tt
    print(f"  {what:>34s} {kinv:>13.3e} {lnB:>16.1f} {tt:>17.3e}")
print()
print("  ** MILLISECONDS at a stellar mass; MONTHS at the heaviest resolved hole. **  *The logarithm")
print("     is ~90 and the prefactor is kappa^{-1}, so nothing is suppressed: the regime the objection")
print("     is about is entered on a timescale short by every astrophysical measure.*")
print("  ⇒ *** WHICH IS WHY 'finite at each finite exterior time' CANNOT BE OFFERED AS A DEFENCE. ***")
if not (1e-3 < _times["one solar mass"] < 1e-2):
    fail.append(f"the solar-mass Planck-blueshift time is {_times['one solar mass']:.3e} s, "
                "outside the millisecond band the paper states")
if not (1e-2 < _times["ten solar masses"] < 1e-1):
    fail.append(f"the ten-solar-mass time is {_times['ten solar masses']:.3e} s, "
                "outside the band the paper states")
if not (1e6 < _times["M87*, 6.5x10^9 Msun"] < 3.2e7):
    fail.append(f"the M87* time is {_times['M87*, 6.5x10^9 Msun']:.3e} s — 'of order months' is wrong")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — AND WHAT P1 NOW SAYS, INCLUDING THE SENTENCE THE NEW CLAUSE EXISTS TO QUALIFY")
print("=" * 78)
P1 = open(os.path.join(CORPUS, 'BH_causality_v2.tex'), encoding='utf-8').read()
WRITTEN = [
    ("the topic is named at all — it was at ZERO uses before this revision",
     r'trans-Planckian'),
    ("the objection is placed on the Bogoliubov construction, which P1 does not perform",
     r'targets the\s*\n?Bogoliubov construction, which is not carried out here'),
    ("the local frequency and the delta^{-1/2} scaling are stated",
     r'omega_\{\\mathrm\{loc\}\}=\\omega_\{\\infty\}/\\sqrt\{f\}'),
    ("the finite-at-each-finite-time claim is made",
     r'finite at every finite exterior time'),
    ("⛔ and the NON-boundedness is stated in the same breath",
     r'not that the blueshift is\s*\n?bounded'),
    ("the supremum is called infinite explicitly",
     r'supremum over\s*\n?exterior time is infinite'),
    ("the two phrasings are set against each other as non-interchangeable",
     r'``finite at each finite exterior time.. and not\s*\n?``bounded'),
    ("the growth rate is identified with the thermality kappa",
     r'same \$\\kappa\$\s*\n?the preceding paragraph identified as the mechanism of thermality'),
    ("the millisecond timescale is in print rather than left implicit",
     r'2\\times10\^\{-3\}\$\s*seconds at a solar mass'),
    ("and the paper states plainly that the surface is NOT free of ultraviolet physics",
     r'not a claim that the late-time collapsing surface is free of ultraviolet\s*\n?physics'),
]
for what, pat in WRITTEN:
    ok = re.search(pat, P1, re.I | re.S) is not None
    print(f"  {'OK ' if ok else 'MISSING'}  {what}")
    if not ok:
        fail.append(f"the written clause does not carry: {what}")

print()
QUALIFIED = ("the PRE-EXISTING sentence the clause qualifies is still present",
             r'It needs no ultraviolet completion of gravity and no modification of quantum theory')
_ok_q = re.search(QUALIFIED[1], P1) is not None
print(f"  {'OK ' if _ok_q else 'MISSING'}  {QUALIFIED[0]}")
print("     ⚠ *without it the new paragraph qualifies nothing and reads as a free-standing concession*")
if not _ok_q:
    fail.append("the sentence the clause exists to qualify has been removed")

print()
CROSS = ("and `L-526`'s thermality exponential is still in the text the new clause points back to",
         r'exponential relation between the affine and Killing parameters')
_ok_c = re.search(CROSS[1], P1) is not None
print(f"  {'OK ' if _ok_c else 'MISSING'}  {CROSS[0]}")
if not _ok_c:
    fail.append("the preceding paragraph's exponential is gone — 'the same kappa' has no referent")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — the blueshift goes as delta^{-1/2} at a simple root; delta decays at 2 kappa in")
print("exterior time so the factor grows at kappa and its supremum is infinite; the Planck value is")
print("reached in milliseconds at a stellar mass; and P1 states the finite-at-each-finite-time claim")
print("WITH its non-boundedness, its timescale, and the admission that the surface is not free of")
print("ultraviolet physics — against a qualified sentence that is still there to qualify.")
print("=" * 78)

# ============================================================================================
# GATE — r2566+c54.207, `L-531`.  ** A scoped partial answer is the single easiest thing in the
# corpus to over-read into a defence **, so every pin here is on the WEAKER half surviving:
#   (1) the delta^{-1/2} scaling from an expansion, not from the routing slip -- ** if the horizon
#       were degenerate the whole estimate would be a different function and the paragraph would be
#       about nothing **;
#   (2) the exterior-time approach SOLVED (dsolve, not quoted) and its rate checked to be exactly
#       2 kappa, with the growth rate exactly kappa -- ** the "same exponential twice" cross-claim to
#       `L-526` is a real identity or it is decoration **;
#   (3) *** the supremum asserted INFINITE ***.  ** This is the gate's centre.  If this ever came out
#       finite the paper would be entitled to say "bounded", and the fact that it does not is the
#       entire reason item 50 was routed as a scoping rather than as an answer **;
#   (4) the Planck-blueshift time bracketed in seconds for three masses -- ** a claim of finiteness
#       reached in milliseconds must not be presentable as a shield, so the number is pinned, not
#       just derived **;
#   (5) ten source checks on what is WRITTEN, four of them on the non-boundedness, the timescale and
#       the explicit admission that the late-time surface is not free of ultraviolet physics;
#   (6) and two ANCHOR checks: the pre-existing "needs no ultraviolet completion" sentence and
#       `L-526`'s exponential must both still be present -- ** the new paragraph is a qualification
#       and a back-reference, and each is void if its target is deleted **.
#   NOT gated: any statement about what happens in the t -> oo limit, or whether the ultraviolet
#   regime is benign.  ** Neither is claimed; the paper says both are unsettled. **
# ============================================================================================
assert _lin != 0, "the horizon came out degenerate"
assert sp.simplify(_exp + sp.Rational(1, 2)) == 0, "the blueshift power is not -1/2"
assert _ok_rate and _ok_grow, "the exterior-time exponents do not come out as +-kappa"
assert _sup == sp.oo, "THE SUPREMUM IS NOT INFINITE — the paper would then be entitled to say 'bounded'"
assert 1e-3 < _times["one solar mass"] < 1e-2, "the solar-mass Planck-blueshift time is not milliseconds"
assert 1e-2 < _times["ten solar masses"] < 1e-1, "the ten-solar-mass time is outside the stated band"
assert 1e6 < _times["M87*, 6.5x10^9 Msun"] < 3.2e7, "'of order months' is not what the arithmetic gives"
for what, pat in WRITTEN:
    assert re.search(pat, P1, re.I | re.S), f"source check failed: {what}"
assert _ok_q, "the sentence the clause qualifies has been removed"
assert _ok_c, "the exponential the clause points back to has been removed"
print(f"GATE c54.207 (r2566), `L-531`: 1/sqrt(f) ~ delta^({_exp}) at a simple root; delta decays at "
      f"{sp.simplify(-_rate)} and the blueshift grows at {_grow} in exterior time, with supremum "
      f"{_sup}; the Planck value is reached at {_times['one solar mass']:.2e} s for one solar mass and "
      f"{_times['M87*, 6.5x10^9 Msun']:.2e} s for M87*; and P1 carries the claim with its "
      f"non-boundedness, its timescale and its ultraviolet admission attached — pinned against "
      f"`FOR_54` item 50 (r2528), `L-526` and P1 sec:5.")
