#!/usr/bin/env python3
"""
RECEIPT -- P1: ** ITEM 54 WORKED.  `L-519`'s THIRD FOOTING, AND IT IS THE ONE THAT SAYS WHAT IS TRUE:
THERMALITY IS THE EXPONENTIAL RELATION BETWEEN THE AFFINE AND KILLING PARAMETERS, AND AT A DOUBLE ROOT
THAT RELATION IS A POWER LAW.  THE MECHANISM IS ABSENT, NOT THE TEMPERATURE ZERO. **

Built r2545+c54.205, lead `L-526`.  VEIN: `L-165` (PO-6, what a quantum of this geometry is).

===================================================================================================
** WHAT c54.202 LEFT AND WHY THIS COMPLETES IT **
===================================================================================================

c54.202 declined to read $T=0$ off the degenerate horizon and registered the refusal as `L-519`.
r2528 added a second footing (the FRAME: $f''<0$, the static region pinches to a point).  ** Both say
what CANNOT be read. **  This is the third and it is different in kind:

  ** near a SIMPLE root **   f ~ 2 kappa delta   =>   r_* = log(delta)/(2 kappa)   -- a LOGARITHM
                             so delta ~ e^{2 kappa r_*} and U ~ -e^{-kappa u}
  *** and THAT exponential relation between the affine and Killing parameters IS the step that
      carries a mode's positive frequencies into a Planck spectrum.  The exponential is the
      thermality. ***

  ** at a DOUBLE root **     f ~ c delta^2     =>   r_* = -1/(c delta)          -- a POWER LAW
  *** no exponential relation, so the construction that produces a thermal spectrum has no first
      step to take. ***

  ⇒ ** Not "T = 0".  THE MECHANISM IS ABSENT. **  *And those are different claims: the first is the
    one c54.202 refused to make and this file does not make either.*

===================================================================================================
** ⛭⛭ AND P15 DERIVED THIS SPLIT ALREADY, FOR ANOTHER PURPOSE **
===================================================================================================

P15, in its own words: *"For a mode approaching a horizon where the metric function behaves as
$f\\sim(r-r_h)^p$ ... At a non-degenerate horizon ($p=1$) the integral is logarithmic and the approach
exponential ... At the degenerate Nariai double root ($p=2$) ... the approach power-law."*

  ⇒ *** ONE FACT, TWO PURPOSES.  P15 needed it to say what CROSSES the branch point; `L-519` needed
      it to say what the configuration CARRIES.  Nobody had connected them. ***

PART 3 checks that sentence is in P15's source rather than quoting it from the routing slip.

⚠ ** WHAT IS NOT CLAIMED: ATHERMAL IN EVERY SENSE. **  A scale-free power-law approach can still act
on a spectrum -- which is exactly what P15 argues it does -- and that is a different question from
whether a PLANCK spectrum arises.  ** T = 0 stays refused; this file adds a positive statement beside
the refusal and does not replace it. **

SETTINGS: none -- no instrument, no spectra.  Symbolic integration of the tortoise coordinate in both
regimes, a series expansion of the Nariai metric function at its double root, and source checks.

rc=0 on success.  Run: python3 P1_thermality_is_the_exponential_and_a_double_root_has_no_exponential.py
                        (sympy; ~5 s)
"""
import os
import re
import sys

import sympy as sp

print(__doc__.split("rc=0")[0])

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
CORPUS = os.path.join(ROOT, 'corpus')
fail = []

d, k, c, r, al = sp.symbols('delta kappa c r alpha', positive=True)

# =====================================================================
print("=" * 78)
print("PART 1 — THE TORTOISE COORDINATE IN BOTH REGIMES, INTEGRATED RATHER THAN ASSERTED")
print("=" * 78)
_simple = sp.simplify(sp.integrate(1 / (2 * k * d), d))
_double = sp.simplify(sp.integrate(1 / (c * d ** 2), d))
print(f"  p = 1,  f ~ 2 kappa delta :  r_* = {_simple}")
print(f"  p = 2,  f ~ c delta^2     :  r_* = {_double}")
_is_log = _simple.has(sp.log)
_is_pow = (not _double.has(sp.log)) and _double.has(1 / d)
print()
print(f"  ** p = 1 gives a LOGARITHM : {_is_log} **   -> delta ~ exp(2 kappa r_*), and the exponential")
print("     relation between affine and Killing parameters is what a Planck spectrum is built from")
print(f"  ** p = 2 gives a POWER LAW : {_is_pow} **   -> no exponential, so no first step")
if not _is_log:
    fail.append("the simple-root tortoise integral is not logarithmic — PART 1's premise fails")
if not _is_pow:
    fail.append("the double-root tortoise integral is not a power law — the whole distinction fails")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — AND THE NARIAI MEMBER'S HORIZON IS A DOUBLE ROOT, EXPANDED HERE")
print("=" * 78)
M = al / (3 * sp.sqrt(3))
rh = al / sp.sqrt(3)
f = 1 - 2 * M / r - r ** 2 / al ** 2
_ser = sp.expand(sp.series(f.subs(r, rh + d), d, 0, 4).removeO())
_lead = sp.simplify(sp.limit(_ser / d ** 2, d, 0))
_lin = sp.simplify(sp.limit(_ser / d, d, 0))
print(f"  f(r_N + delta) = {_ser}")
print(f"  coefficient of delta^1 : {_lin}      ** zero => a DOUBLE root, so p = 2 **")
print(f"  coefficient of delta^2 : {_lead}")
print()
print("  *So the configuration a collapse reaches is exactly the p = 2 case, and the exponential the")
print("   thermal construction needs is not available at it.*")
if _lin != 0:
    fail.append(f"the Nariai expansion has a linear term {_lin} — it is not a double root")
if _lead == 0:
    fail.append("the quadratic coefficient vanishes too — the expansion is not p = 2")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — P15 ALREADY DERIVED THE SPLIT, AND P1 NOW CITES IT ACROSS")
print("=" * 78)
P15 = open(os.path.join(CORPUS, 'CR_cosmology.tex'), encoding='utf-8').read()
P1 = open(os.path.join(CORPUS, 'BH_causality_v2.tex'), encoding='utf-8').read()
CHECKS = [
    ("P15 states the p-dependence of the tortoise integral explicitly",
     P15, r'behaves as \$f\\sim\(r-r_h\)'),
    ("P15 gives p = 1 as logarithmic and exponential",
     P15, r'the integral is logarithmic and the approach exponential'),
    ("P15 gives the degenerate double root as power-law",
     P15, r'the approach power-law'),
    ("P1 now states that the exponential IS the thermality",
     P1, r'carries a mode.s positive frequencies into a Planck spectrum'),
    ("P1 states the double-root case has no first step",
     P1, r'has no first step to take'),
    ("P1 states the right conclusion is mechanism-absent and not T = 0",
     P1, r'not that the temperature is zero but that the\s*\n?mechanism is absent'),
    ("and P1 keeps the athermal-in-every-sense reading refused",
     P1, r'athermal in every sense'),
]
for what, hay, pat in CHECKS:
    ok = re.search(pat, hay, re.I | re.S) is not None
    print(f"  {'OK ' if ok else 'MISSING'}  {what}")
    if not ok:
        fail.append(f"not found in source: {what}")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — the simple-root tortoise integral is logarithmic and the double-root one a")
print("power law; the Nariai horizon is a double root by expansion; P15 already carried the split for")
print("its transmission dichotomy; and P1 now says the mechanism is absent rather than the temperature")
print("zero, with the athermal-in-every-sense reading still refused.")
print("=" * 78)

# ============================================================================================
# GATE — r2545+c54.205, `L-526`.  This adds a POSITIVE statement beside a refusal, which is the
# thing most easily over-read, so the pins are on the distinction holding and on the refusal
# surviving:
#   (1) the two integrals, computed rather than quoted -- ** the whole claim is that one is a
#       logarithm and the other is not, and if they were the same kind of function there would be
#       no distinction to draw **;
#   (2) the Nariai expansion having NO linear term and a nonzero quadratic one, so the p = 2 case
#       is the configuration a collapse reaches and not a generic remark;
#   (3) three source checks in P15 -- ** if P15 did not already carry the split, this would be a
#       new physics claim rather than a cross-citation, and P1 is not entitled to make one here **;
#   (4) and four in P1, including that the athermal-in-every-sense reading is explicitly refused.
#   NOT gated: any temperature, at either root.  ** c54.202 declined to read one and this file
#   does not read one either; what it adds is why there is nothing to read. **
# ============================================================================================
assert _is_log, "the p = 1 tortoise integral is not logarithmic"
assert _is_pow, "the p = 2 tortoise integral is not a power law"
assert _lin == 0 and _lead != 0, "the Nariai horizon is not a clean double root"
for what, hay, pat in CHECKS:
    assert re.search(pat, hay, re.I | re.S), f"source check failed: {what}"
print(f"GATE c54.205 (r2545), `L-526`: r_* = {_simple} at a simple root and {_double} at a double one, "
      f"so the exponential the thermal construction rests on exists at p = 1 and not at p = 2; the "
      f"Nariai expansion has no linear term and quadratic coefficient {_lead}; and P15's own "
      f"transmission split is cited across rather than re-derived as new — pinned against `FOR_54` "
      f"item 54 (r2543), `L-519` and P15 sec:transmission.")
