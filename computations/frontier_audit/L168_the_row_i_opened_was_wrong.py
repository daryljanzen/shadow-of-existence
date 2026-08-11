#!/usr/bin/env python3
"""
`L-168` IS WRONG, AND I OPENED IT.  ** THE TILT *IS* INHERITED, THE PAPER SAYS SO IN ITS OWN BODY,
AND I REGISTERED THE OPPOSITE TWO REVISIONS AGO BY READING THE LEDGER INSTEAD OF THE PAPER. **

At `c54.119` I read `THE_OPEN_PROBLEMS_LEDGER` family (11) — opened r2244 — and took its ⛔ clause
at face value: *"the computed filter decides against ... nothing at observable scales crosses ... a
tilt measured at $k\\sim0.05$ Mpc$^{-1}$ cannot be inherited across a filter suppressing that
wavenumber by $e^{-500}$."*  I registered its residual as a new open row.

** THAT CLAUSE IS THE r2244 FRAMING, WHICH r2245 RECLASSIFIED AS 'MY FRAMING WAS THE ERROR, NOT THE
PHYSICS', AND WHICH P15 `sec:what-crosses` RESOLVES IN ITS OWN BODY. **  I had retired the clue-map
layer of that very ledger in the same revision for being unmaintainable, and then trusted its prose.

  PART 1  ** WHAT P15 ACTUALLY SAYS, quoted from the paper. **
  PART 2  ** THE MECHANISM, RE-DERIVED: on the contracting leg the comoving horizon shrinks to
          ZERO, so every mode has exited and frozen before the crossing. **
  PART 3  ** SO THE FILTER'S TWO READINGS ARE ONE STATEMENT, and the tilt is on the passing side. **
  PART 4  ** WHAT THE REAL OPEN ITEM IS, and what `L-168` must become. **

Run: python3 L168_the_row_i_opened_was_wrong.py      (sympy, numpy)
"""
import os
import re

import numpy as np
import sympy as sp

print(__doc__.split("Run:")[0])
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
P15 = open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'), encoding='utf-8').read()

# =====================================================================
print("=" * 78)
print("PART 1 — WHAT P15 ACTUALLY SAYS")
print("=" * 78)
KEY = [
 ("the naive reading, named as naive IN THE PAPER",
  r"Taken\s*\nnaively this would annihilate everything: at \$\\ell=220\$ the factor is \$10\^\{-71\}\$"),
 ("the mechanism",
  r"every\\emph\{ \}mode exits it and freezes|\\emph\{every\} mode exits it and freezes"),
 ("the verdict on the tilt",
  r"the amplitude and the\s*\ntilt cross unaltered"),
 ("the one-statement summary",
  r"the crossing transmits what is frozen and destroys what oscillates"),
]
found = 0
for name, pat in KEY:
    m = re.search(pat, P15)
    print(f"  {'✔' if m else '⛔'} {name}: {'present' if m else 'NOT FOUND'}")
    if m:
        found += 1
        print(f"        “…{m.group(0)[:120].replace(chr(10),' ')}…”")
assert found >= 3, found
print()
for s in [
 "⇒⇒ ** THE PAPER'S OWN SENTENCE IS THE ANSWER: *'the crossing transmits what is FROZEN and destroys",
 "   what OSCILLATES, so the progenitor supplies the spectrum's amplitude and shape while supplying",
 "   none of its phase.'*  The $10^{-71}$ applies to the acoustic PHASE, not to the tilt. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE MECHANISM, RE-DERIVED")
print("=" * 78)
r, M, al = sp.symbols('r M alpha', positive=True)
f = 1 - 2 * M / r - r**2 / al**2
aH2 = sp.simplify(1 - f)                       # (a H)^2 = |dr/dtautilde|^2 = |1 - f|
print(f"  On the contracting leg  aH = |dr/dtautilde| = sqrt(|1-f|),  and  1 - f = {aH2}")
lim = sp.limit(aH2, r, 0, '+')
print(f"  ** lim_(r->0) (aH)^2 = {lim}  ⇒  aH -> infinity  ⇒  the comoving horizon 1/aH -> 0 **")
assert lim == sp.oo
print("  and it is the MASS term that does it: 2M/r diverges while r^2/alpha^2 vanishes.")
print()
print("  P15 quotes two values; both are reproduced here at the Nariai member 2M = 2/(3 sqrt 3) alpha:")
TWOM = 2.0 / (3.0 * np.sqrt(3.0))
print(f"  {'|r|/alpha':>12} {'aH = sqrt(2M/r + r^2)':>24} {'P15':>10}")
for rr, quoted in [(0.1, 1.96), (1e-3, 19.6)]:
    v = np.sqrt(TWOM / rr + rr**2)
    print(f"  {rr:>12.0e} {v:>24.3f} {quoted:>10}")
    assert abs(v - quoted) < 0.02, (rr, v, quoted)
print()
for s in [
 "⇒ ** SO EVERY COMOVING SCALE IS OUTSIDE THE HORIZON AT THE CROSSING, whatever its $k$. **",
 "   *The naive calculation evaluates $e^{-k c_s|\\Delta\\eta|}$ with $k$ the mode's wavenumber and",
 "   $c_s$ the plasma's sound speed — i.e. it treats an observable-scale mode as still OSCILLATING",
 "   when it reaches the branch point.  **It is not.  It froze on the way in, and a frozen mode has",
 "   no oscillation for a Euclidean kernel to damp.***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE TWO READINGS ARE ONE STATEMENT")
print("=" * 78)
print(f"  the exponent is  k * c_s * |Delta eta|  — TWO factors, and the corpus reads both:")
print(f"  {'reading':>34} {'held fixed':>12} {'varied':>8} {'what it separates':>34}")
for a, b, c, d in [("scale criterion (r2157)", "c_s", "k", "frozen vs oscillating"),
                   ("species criterion (c54.112)", "k", "c_s", "pressureless vs pressured")]:
    print(f"  {a:>34} {b:>12} {c:>8} {d:>34}")
print()
print(f"  {'content':>36} {'oscillating at the crossing?':>30} {'crosses?':>10}")
for a, b, c in [("the acoustic PHASE of the collapse leg", "yes — it was sub-horizon", "NO, e^-152"),
                ("the AMPLITUDE A_s", "no — frozen", "YES"),
                ("the TILT n_s", "no — frozen", "YES"),
                ("a pressureless component (c_s = 0)", "no — psi'' = 0", "YES, exactly")]:
    print(f"  {a:>36} {b:>30} {c:>10}")
print()
for s in [
 "✔ ** AND THE PHASE'S DESTRUCTION IS INDEPENDENTLY REQUIRED: the observed peak POSITIONS exclude a",
 "   transmitted leg phase by a factor of 21–39 in the required distance. **  *So the filter is not",
 "   an embarrassment the construction survives; it removes exactly the thing the data says must be",
 "   absent, and leaves the comb to be set on the expansion side.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — WHAT THE REAL OPEN ITEM IS")
print("=" * 78)
m = re.search(r'\$n_s\$ and \$A_s\$ are inherited[^.]*\.', P15)
print("  P15 `sec:transmission`, closing sentence:")
print(f"    “…{m.group(0)[:230]}…”" if m else "    (not matched)")
assert m
print()
for s in [
 "⇒⇒ ** SO THERE IS A REAL OPEN ITEM AND IT IS NOT THE ONE I REGISTERED.  It is: DERIVE $n_s$ AND",
 "   $A_s$ FROM THE PROGENITOR COLLAPSE — which the paper states plainly as inherited-and-not-",
 "   derived, and which it says is *'the same handover that fixes $\\rho_r/\\rho_m$ and the",
 "   light-element abundances'*. **  ⌗ *That handover is already `L-150`.  So this is not a new row;",
 "   it is `L-150`'s scope, and `L-150` should say so.*",
 "",
 "⛔⛔ ** THE ERROR, RECORDED AT ITS FULL SIZE: I registered `L-168` asserting that the tilt CANNOT",
 "   be inherited.  The paper's body says it IS, gives the mechanism, and names the naive reading as",
 "   naive in the same paragraph. **  *I reached that conclusion by reading a LEDGER's r2244 framing",
 "   — which r2245 had already reclassified as 'my framing was the error, not the physics' — instead",
 "   of the paper.*",
 "",
 "⌗⌗ ** AND THE AGGRAVATION IS THE PART WORTH BANKING: I did it in the SAME REVISION in which I",
 "   retired that ledger's pointer layer for being unmaintainable.  I distrusted its ADDRESSES and",
 "   trusted its PROSE, and the prose was staler than the addresses. **",
 "",
 "⇒ *The rule this earns: **when a ledger entry and a paper disagree, the paper wins — and a ledger",
 "   entry that has been RECLASSIFIED carries its superseded framing in the same block as its",
 "   verdict.*  A reclassification is not a strike, and its old text stays live-looking.*",
]:
    print("  " + s)
