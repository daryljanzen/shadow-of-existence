#!/usr/bin/env python3
"""
RECEIPT -- P1: ** ROUTED ITEM 47 WORKED.  UNRUH IS NOT A GAP IN THE ARGUMENT, IT IS THE CASE THAT
DECIDES WHAT THE ARGUMENT'S CRITERION IS: THE RINDLER HORIZON IS MAXIMALLY OBSERVER-DEPENDENT AND
EXACTLY THERMAL, SO "PERSPECTIVAL THEREFORE NO FLUX" IS REFUTED AT ONCE -- AND THAT WAS NEVER THE
CLAIM.  COMPLETION SORTS ALL FOUR HORIZONS; OBSERVER-DEPENDENCE SORTS TWO OF THEM WRONGLY. **

** AND THE CORPUS SAYS TWO THINGS BEYOND CONSISTENCY, BOTH ASSEMBLED FROM RESULTS IT ALREADY HAS. **

Built r2524+c54.202, lead `L-518`.  VEIN: `L-165` (PO-6, what a quantum of this geometry is).

===================================================================================================
** WHAT 56 ESTABLISHED, AND IT IS THE REASON THIS IS WORTH WRITING RATHER THAN PATCHING **
===================================================================================================

r2521 measured the absence and tested the argument against it.  ** "Unruh" 0 uses in seventeen papers;
"Rindler horizon" 0 -- every "Rindler" is Rindler the author, on lensing; <T_mu_nu> 0; trans-Planckian
0.  Against Hawking 94. **  And the argument survives: the corpus argues from COMPLETION ("completed
horizon" 24 uses, "finite exterior" 28) and ** nowhere argues "perspectival, therefore no flux". **

  ⇒ *** Which is exactly the distinction Unruh forces.  A uniformly accelerated observer in FLAT
      space sees an exactly thermal spectrum from a horizon that is uncontroversially
      observer-dependent, with no gravity and no collapse anywhere in the setup. ***

** SO THE MISSING PARAGRAPH IS NOT A REPAIR.  It turns an unstated precision into a stated one. **

===================================================================================================
** PART 1 -- THE SORTING, AND ONLY ONE CRITERION SORTS IT **
===================================================================================================

  horizon                          complete?   observer-dependent?   thermal?
  Rindler (Unruh)                     YES              YES             YES
  substrate cosmological (dS)         YES              YES             YES
  eternal Schwarzschild               YES              no              YES
  astrophysical collapse              *** NO ***       --              denied here

  ** COMPLETION predicts all four.  OBSERVER-DEPENDENCE predicts the first two wrongly. **
  *And the Rindler row is the one that separates them, which is why its absence mattered.*

===================================================================================================
** PART 2 -- THE FIRST THING THE SUBSTRATE ADDS: THE REST TERM IS NOT FREE, AND IT IS NOT ZERO **
===================================================================================================

In de~Sitter the accelerated temperature is T(a) = sqrt(H^2 + a^2)/2pi (Narnhofer-Peter-Thirring;
Deser-Levin), reducing to a/2pi as a grows and to H/2pi at rest.  ** On this substrate H = 1/alpha
and alpha = sqrt(3/Lambda) is the SOLE dimensionful constant, ** so

      *** T(a) = (1/2pi) sqrt(1/alpha^2 + a^2)  --  no adjustable parameter anywhere in it. ***

  ⇒ ** and the rest term is exactly the kappa = 1/alpha the corpus already places a Hartle-Hawking
    state at (P1's own reconciliation paragraph, citing the canonical-time companion). **  PART 2
    checks that identity rather than asserting it: kappa/2pi for f = 1 - r^2/alpha^2 at r = alpha
    equals T(0).

  ⌗ ** THE STRUCTURAL DIFFERENCE FROM THE FLAT STATEMENT IS THAT THE REST TERM DOES NOT VANISH. **
    *An unaccelerated observer in Minkowski sees nothing; an unaccelerated observer on this substrate
    is already in a thermal state, and acceleration adds to a bath rather than creating one.*

===================================================================================================
** PART 3 -- THE SECOND: THE MEMBER A COLLAPSE REACHES HAS ZERO SURFACE GRAVITY, AND P7 ALREADY
   COMPUTES IT FOR A DIFFERENT PURPOSE **
===================================================================================================

P7: "at that member both the surface gravity and the photon orbit's Lyapunov exponent vanish ... so
the signal by which a black hole would announce a completed horizon is absent at exactly the
configuration the framework says a collapse reaches."  ** That is the Nariai double root, and PART 3
re-derives kappa = 0 there symbolically rather than citing it. **

  ⇒ *** So the thermal flux the paradox needs is absent TWICE OVER, for independent reasons: absent
      because no completed horizon is realised -- P1's argument, independent of which member is
      reached -- and, granting the completion for the sake of the objection, kappa = 0 at the member
      that would be completed. ***

⚠ ** AND THE SECOND IS NOT OFFERED AS A REPLACEMENT FOR THE FIRST, for a stated reason. **  A
degenerate horizon is precisely the case in which reading a temperature off kappa/2pi is least safe:
the near-horizon geometry is the equal-radii dS_2 x S^2 throat this programme builds elsewhere, which
carries a scale of its own.  ** The two readings are NOT reconciled here and the paper says so. **
*What is claimed is the coincidence and not a value.*

  ⌗ *That non-reconciliation is registered as its own lead rather than left in a caveat: the corpus
  holds kappa = 0 at Nariai (P7) and the equal-radii throat (P15) and has never set them side by
  side.*

WHAT IS NOT CLAIMED.  ** Not that Unruh is in tension with anything here ** -- the opposite, it is the
case that shows the criterion works.  ** Not a derivation of the Unruh effect from the substrate **,
and no new value for any temperature.  ** Not that kappa = 0 settles the collapse case **, which rests
on completion and not on a surface gravity.  ** And <T_mu_nu> and trans-Planckian remain at zero uses
** -- 56 named three companions and this file addresses one of them.

SETTINGS: none -- no instrument, no spectra.  Symbolic differential geometry (sympy) on two exact
metric functions, plus source counts over the corpus's own .tex.

rc=0 on success.  Run: python3 P1_the_unruh_case_is_what_makes_the_criterion_completion_and_not_perspective.py
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

r, al, a = sp.symbols('r alpha a', positive=True)

# =====================================================================
print("=" * 78)
print("PART 1 — THE SORTING TABLE, AND WHICH CRITERION SURVIVES IT")
print("=" * 78)
# (name, complete, observer-dependent, thermal)   -- textbook facts, tabulated so a claim can fail
CASES = [
    ('Rindler (Unruh)',            True,  True,  True),
    ('substrate cosmological (dS)', True,  True,  True),
    ('eternal Schwarzschild',       True,  False, True),
    ('astrophysical collapse',      False, None,  False),
]
print(f"  {'horizon':>30s} {'complete':>10s} {'obs-dep':>9s} {'thermal':>9s}")
for nm, comp, obs, th in CASES:
    print(f"  {nm:>30s} {str(comp):>10s} {str(obs):>9s} {str(th):>9s}")
_by_completion = all((comp == th) for _, comp, _, th in CASES)
_by_obsdep = all((obs == th) for _, _, obs, th in CASES if obs is not None)
print()
print(f"  ** completion predicts thermality in every row      : {_by_completion} **")
print(f"  ** observer-dependence predicts it in every row     : {_by_obsdep} **")
print("  *and the two disagree only where a horizon is complete AND observer-dependent — the first")
print("   two rows, of which Rindler is the one with no gravity in it at all.*")
if not _by_completion:
    fail.append("completion does not sort the four cases — PART 1's whole claim fails")
if _by_obsdep:
    fail.append("observer-dependence also sorts the four — then Unruh does not discriminate and "
                "this file has no content")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE REST TERM IS THE CORPUS'S OWN kappa, AND IT IS FIXED BY THE ONE CONSTANT")
print("=" * 78)
f_ds = 1 - r ** 2 / al ** 2
rh = sp.solve(sp.Eq(f_ds, 0), r)[0]
kappa_ds = sp.simplify(sp.Abs(sp.diff(f_ds, r).subs(r, rh)) / 2)
T = sp.sqrt(1 / al ** 2 + a ** 2) / (2 * sp.pi)
T0 = sp.simplify(T.subs(a, 0))
print(f"  pure de Sitter f = {f_ds},  horizon r_h = {rh}")
print(f"  kappa = |f'(r_h)|/2 = {kappa_ds}      (the corpus states kappa = 1/alpha)")
print(f"  T(a) = (1/2pi) sqrt(1/alpha^2 + a^2);   T(0) = {T0}")
_match = sp.simplify(T0 - kappa_ds / (2 * sp.pi)) == 0
print(f"  ** T(0) == kappa/2pi : {_match} **")
_flat = sp.simplify(sp.limit(T / (a / (2 * sp.pi)), a, sp.oo))
print(f"  ** T(a) / (a/2pi) as a -> infinity : {_flat}  (the flat Unruh limit is recovered) **")
_nonzero = sp.simplify(T0) != 0
print(f"  ** and the rest term is NOT zero  : {_nonzero}  — which is the structural difference from")
print("     the flat statement: acceleration adds to a bath rather than creating one. **")
if not _match:
    fail.append("T(0) is not kappa/2pi — the rest term is not the corpus's own state")
if _flat != 1:
    fail.append(f"the large-a limit is {_flat}, not the flat Unruh result")
if not _nonzero:
    fail.append("the rest term vanishes — then the substrate adds nothing over Minkowski")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — AND THE MEMBER A COLLAPSE REACHES HAS ZERO SURFACE GRAVITY")
print("=" * 78)
M_nar = al / (3 * sp.sqrt(3))
f_n = sp.simplify(1 - 2 * M_nar / r - r ** 2 / al ** 2)
r_n = al / sp.sqrt(3)
f_at = sp.simplify(f_n.subs(r, r_n))
fp_at = sp.simplify(sp.diff(f_n, r).subs(r, r_n))
kappa_n = sp.simplify(sp.Abs(fp_at) / 2)
print(f"  Nariai M = {sp.simplify(M_nar)},  the merged root r = alpha/sqrt3")
print(f"  f  there = {f_at}        (a horizon)")
print(f"  f' there = {fp_at}        ** a DOUBLE root **")
print(f"  kappa = |f'|/2 = {kappa_n}")
print()
print("  ⇒ *the flux the paradox needs is absent twice over and for independent reasons: absent")
print("     because no completed horizon is realised, and — granting the completion — kappa = 0 at")
print("     the member that would be completed.*")
print("  ⚠ **and the second is NOT a replacement for the first**: a degenerate horizon is exactly")
print("     where kappa/2pi is least safe, the near-horizon geometry being the equal-radii")
print("     dS_2 x S^2 throat, which carries a scale of its own.  *The paper says so rather than")
print("     quietly reading T = 0.*")
if f_at != 0:
    fail.append("the Nariai radius is not a horizon — PART 3's premise fails")
if fp_at != 0 or kappa_n != 0:
    fail.append(f"the surface gravity at the Nariai root is {kappa_n}, not zero")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — WHAT THE CORPUS NOW SAYS, AND WHAT IT STILL DOES NOT")
print("=" * 78)
tex = {}
for fn in sorted(os.listdir(CORPUS)):
    if fn.endswith('.tex') and not fn.startswith('appendix_receipts'):
        tex[fn] = open(os.path.join(CORPUS, fn), encoding='utf-8', errors='replace').read()
allt = '\n'.join(tex.values())


def uses(pat):
    return len(re.findall(pat, allt, re.I))


P1 = tex['BH_causality_v2.tex']
ADDED = [
    ("P1 now names Unruh and cites the 1976 paper", P1, r'Unruh1976'),
    ("P1 names the RINDLER HORIZON as the object", P1, r'Rindler\s*\n?horizon'),
    ("P1 states the refutation the case forces", P1, r'perspectival, therefore there is no thermal flux'),
    ("P1 states that completion sorts all four", P1, r'completion sorts all four'),
    ("P1 carries the de Sitter accelerated temperature with the substrate's own constant",
     P1, r'T\(a\)=\\frac\{1\}\{2\\pi\}\\sqrt'),
    ("P1 states the Nariai vanishing and refuses to read a temperature off it",
     P1, r'two readings\\?\s*\n?are not reconciled here'),
]
for what, hay, pat in ADDED:
    ok = re.search(pat, hay, re.I) is not None
    print(f"  {'OK ' if ok else 'MISSING'}  {what}")
    if not ok:
        fail.append(f"the written treatment does not carry: {what}")
print()
print("  ** AND THE TWO COMPANIONS 56 NAMED THAT THIS FILE DOES NOT ADDRESS, counted so the debt is")
print("     visible rather than quietly discharged: **")
_tmn = uses(r'\\langle T_\{\\mu\\nu\}\\rangle|stress[- ]energy expectation')
_tp = uses(r'trans-Planckian')
print(f"     <T_mu_nu> as an expectation value : {_tmn} use(s)")
print(f"     trans-Planckian                   : {_tp} use(s)")
print("  *56 named three companions a reader arrives with. This revision addresses one.*")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — completion sorts all four horizons and observer-dependence sorts two of them")
print("wrongly, so Unruh is the case that fixes the criterion rather than a gap in it; the substrate's")
print("rest term is its own kappa = 1/alpha and the accelerated temperature carries no free parameter;")
print("and the surface gravity vanishes at the member a collapse reaches, which the paper records as a")
print("coincidence rather than as a temperature.")
print("=" * 78)

# ============================================================================================
# GATE — r2524+c54.202, `L-518`.  This file supports a WRITTEN treatment rather than a computed
# result, so what it pins is the thing a written treatment can most easily get wrong: whether the
# distinction it draws actually does any work, and whether the numbers it leans on are the
# corpus's own.
#   (1) completion sorting all four AND observer-dependence failing to -- ** both directions.  If
#       observer-dependence also sorted them, Unruh would not discriminate and the whole
#       paragraph would be decoration; the file fails in that case and says why **;
#   (2) T(0) = kappa/2pi with kappa re-derived from the metric function -- the rest term must BE
#       the state the corpus already places, not merely resemble it;
#   (3) the large-a limit recovering a/2pi, without which \eqref{eq:unruh-ds} is not the Unruh
#       statement at all;
#   (4) the rest term asserted NONZERO, which is the one structural difference from Minkowski
#       this file claims;
#   (5) kappa = 0 at the Nariai double root, re-derived rather than cited from P7;
#   (6) and the six written claims asserted PRESENT in P1 by text, so a later edit that removes
#       the treatment fails this file instead of passing quietly.
#   NOT gated: any temperature at the degenerate horizon.  ** The paper declines to read one and
#   so does this file. **
# ============================================================================================
assert _by_completion, "completion does not sort the four horizons"
assert not _by_obsdep, "observer-dependence also sorts them — Unruh would then discriminate nothing"
assert sp.simplify(T0 - kappa_ds / (2 * sp.pi)) == 0, "the rest term is not the corpus's own kappa/2pi"
assert sp.simplify(kappa_ds - 1 / al) == 0, f"de Sitter surface gravity is {kappa_ds}, not 1/alpha"
assert _flat == 1, "the large-a limit is not the flat Unruh result"
assert sp.simplify(T0) != 0, "the rest term vanishes"
assert f_at == 0 and fp_at == 0 and kappa_n == 0, "the Nariai root is not a degenerate horizon"
for what, hay, pat in ADDED:
    assert re.search(pat, hay, re.I), f"P1 does not carry: {what}"
print(f"GATE c54.202 (r2524), `L-518`: completion sorts all four horizons and observer-dependence "
      f"does not; the substrate's rest term is kappa/2pi = {sp.simplify(T0)} with kappa = {kappa_ds} "
      f"re-derived from f = 1 - r^2/alpha^2, and T(a) -> a/2pi as a grows; the surface gravity at the "
      f"Nariai double root is {kappa_n}, with no temperature read from it — pinned against `FOR_54` "
      f"item 47 (r2521), P1 sec:hawking and P7's eikonal result.")
