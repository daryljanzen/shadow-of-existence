#!/usr/bin/env python3
"""
THE FOLD LEAKED, AND P7's FRONTIER ITEM 4 IS WHERE IT SHOWS.  THREE LIVE MAP ITEMS WERE NEVER
FOLDED INTO THE REGISTER -- AND ONE OF THEM IS THE CORPUS'S QUANTUM FRONTIER.

`OPEN_PROBLEMS_MAP` carries this sentence at its head (c54.90, Daryl-directed):

    "Every live item below has been FOLDED INTO `THE_LIVE_ARC`'s lead register and carries its
     lead ID inline as `[L-nnn]`. ... Closed items are NOT folded and are left exactly in place
     as the record."

** IT IS NOT TRUE, AND THE EXCEPTIONS ARE NOT SMALL. **  `P07_frontier_currency` found the first of
them the same way it found `A·5` a revision earlier: every frontier item mapped to a lead and this
one mapped to nothing.  The check below asks the map's own claim of the map, mechanically.

  PART 1  ** WHICH MAP ITEMS ARE IN THE REGISTER, PARSED FROM BOTH DOCUMENTS. **
  PART 2  ** THE THREE THAT ARE NOT -- and which of them are legitimately unfolded. **
  PART 3  ** B·1's CONTENT, CHECKED: the boundary coefficient $\\hat\\Gamma$ is asserted bounded
          below where the structure is built and listed as UNKNOWN where the frontier is stated,
          inside one paragraph. **
  PART 4  ** WHAT THE STRADDLE ARGUMENT ACTUALLY NEEDS -- and it is not boundedness below. **
  PART 5  What the three rows are.

Run: python3 L165_the_quantum_completion_was_never_folded.py      (numpy)
"""
import os
import re

import numpy as np

print(__doc__.split("Run:")[0])
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
MAP = open(os.path.join(ROOT, 'OPEN_PROBLEMS_MAP.md'), encoding='utf-8').read()
ARC = open(os.path.join(ROOT, 'THE_LIVE_ARC.md'), encoding='utf-8').read()
P10 = open(os.path.join(ROOT, 'corpus', 'canonical_time.tex'), encoding='utf-8').read()

# =====================================================================
print("=" * 78)
print("PART 1 — WHICH MAP ITEMS ARE IN THE REGISTER")
print("=" * 78)
# A map ITEM is a top-level bullet declaring a cluster-local code.  Take the first code on the
# bullet: a strike banner names the code it strikes, and that is the same item.
items = []
for line in MAP.split('\n'):
    if not line.startswith('- **'):
        continue
    mm = re.search(r'([A-J])(·|\b)(\d+)', line)
    if not mm:
        continue                      # prose bullets in the runway/priority sections
    code = f"{mm.group(1)}·{mm.group(3)}"
    if code not in [c for c, _, _ in items]:
        # the map writes cluster A's second item as BOTH `A2` and `A·2`; one item, two spellings,
        # and that ALIAS is the only one -- no general de-interpuncting, which would match noise.
        inreg = (code in ARC) or (code == 'A·2' and re.search(r'\bA2\b', ARC) is not None)
        items.append((code, line, inreg))
print(f"  the map declares {len(items)} items")
missing = [(c, ln) for c, ln, ir in items if not ir]
print(f"  ** {len(items) - len(missing)} of them name a lead in the register. "
      f"{len(missing)} do not: {[c for c, _ in missing]} **")
assert len(items) >= 30

# =====================================================================
print()
print("=" * 78)
print("PART 2 — WHICH OF THE UNFOLDED ARE LEGITIMATELY UNFOLDED")
print("=" * 78)
# ** NO HEURISTIC HERE.  The map's rule is that a CLOSED item is not folded, and the map states a
# closure in one of exactly two shapes, each carrying its revision.  Anything else is LIVE, and
# the evidence is printed so the classification can be checked by eye rather than trusted. **
CLOSURE = re.compile(r'(\[r\d+\s*[—–-]\s*(?:RESOLVED|CLOSED)|(?:RESOLVED|CLOSED)\s*\(r\d+\))')
gap, closed_unfolded = [], []
for c, ln in missing:
    ev = CLOSURE.search(ln)
    if ev:
        closed_unfolded.append(c)
        print(f"  {c:>5}  closed at map level — evidence: “{ev.group(0)}”")
    else:
        gap.append(c)
        print(f"  {c:>5}  ⛔ NO CLOSURE MARKER — LIVE AND UNFOLDED")
print()
print(f"  ** live and NOT in the register: {gap} **")
print(f"  closed before the fold and correctly left in place: {closed_unfolded}")
assert gap == ['B·1', 'B·2', 'G·1'], gap
assert closed_unfolded == ['C·1', 'C·2'], closed_unfolded
print()
for s in [
 "⇒⇒ ** SO THE MAP'S HEADER SENTENCE IS FALSE FOR EXACTLY THREE ITEMS, AND THE WHOLE OF CLUSTER B",
 "   IS TWO OF THEM. **  *`C·1` (r547) and `C·2` (r561) were both closed BEFORE the fold and are",
 "   correctly left in place as the record -- the map's stated rule.  `B·1`, `B·2` and `G·1` are",
 "   live, and no gate has been able to see them: not `check_burndown`, not `check_supersession`,",
 "   not `check_grains`.*",
 "",
 "⌗ ** AND THE CONSEQUENCE IS EXACTLY THE ONE `A·5` HAD A REVISION EARLIER: a frontier item in a",
 "   PAPER pointing at open work that the corpus's own tracking cannot reach. **  *P7",
 "   `sec:frontiers` item 4 -- 'the quantum sector: the deparametrized content in hand, the",
 "   interacting theory's definition open' -- IS `B·1`.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — B·1's CONTENT, CHECKED AGAINST P10")
print("=" * 78)
para = P10[P10.find('It is worth naming what kind of closure'):]
para = para[:para.find('\n\n')] if '\n\n' in para[:60000] else para[:60000]
a = re.search(r'promoted from the c-number.{0,200}?threshold\.', para, re.S)
b = re.search(r'the spectrum of \$\\hat\\Gamma\$[^.]{0,160}', para, re.S)
print("  where the structure is BUILT, the paragraph says:")
print(f"    “…{a.group(0)}”")
print()
print("  where the frontier is STATED, the same paragraph says:")
print(f"    “…{b.group(0)}…”")
print()
built_claims_bb = 'bounded below by $\\gamma$' in a.group(0)
front_calls_open = 'bounded below' in b.group(0)
print(f"  ** the first asserts boundedness below: {built_claims_bb} **")
print(f"  ** the second lists boundedness below as OPEN: {front_calls_open} **")
assert built_claims_bb and front_calls_open
print()
for s in [
 "⚠ ** THE TWO ARE IN TENSION AS WRITTEN, AND THE TENSION IS A SCOPE SLIP RATHER THAN AN ERROR. **",
 "   *The paragraph proves boundedness below for the LEADING-ORDER operator, two sentences later:*",
 "   *$\\hat\\Gamma=\\gamma+c\\sum_n\\hat\\pi_n^{2}$, a sum of squares over a positive coefficient,*",
 "   *whose spectrum is contained in $[\\gamma,\\infty)$.*  ** But the assertion is made of",
 "   $\\hat\\Gamma$ unqualified, and the COMPLETE $\\hat\\Gamma$ -- the singular part of the",
 "   INTERACTING graviton Hamiltonian, cubic and higher included -- is the very object the same",
 "   paragraph then declares unknown. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — WHAT THE STRADDLE ARGUMENT ACTUALLY NEEDS")
print("=" * 78)
print("  Model the boundary coefficient on a truncated tower in the momentum representation, where")
print("  pi_n^2 is diagonal with eigenvalues k_n^2 >= 0.  gamma <= 1/4 is the free scale factor's.")
GAM, C = 0.25, 1.0
K = np.linspace(0.0, 2.0, 400)                      # one mode's momentum grid
lead = GAM + C * K**2
print(f"     leading order:  Gamma-hat = gamma + c * pi^2,  c = {C}")
print(f"     {'min spec':>28} {lead.min():.6f}   (= gamma = {GAM})")
print(f"     {'max spec':>28} {lead.max():.6f}   (unbounded as the grid extends)")
assert abs(lead.min() - GAM) < 1e-12
print(f"     ** bounded below by gamma: {bool(lead.min() >= GAM - 1e-12)} **")
print(f"     ** straddles 3/4:  some below {bool((lead < 0.75).any())} · some above "
      f"{bool((lead >= 0.75).any())} **")
assert (lead < 0.75).any() and (lead >= 0.75).any()

print()
print("  Now add a cubic-order term of the kind the paragraph says enters at the SAME inverse-square")
print("  order.  A cubic self-interaction is not sign-definite and it does not act on every channel")
print("  alike, so the honest worst case is TWO CHANNELS: one the quadratic keeps, one the cubic")
print("  takes over.  The complete Gamma-hat is the union.")
LAM = 0.6
chA = GAM + C * K**2                     # untouched by the cubic
chB = GAM + C * K**2 - LAM * K**3        # the cubic wins at large momentum
full = np.concatenate([chA, chB])
print(f"     channel A:  gamma + c pi^2                 -> [{chA.min():.4f}, {chA.max():.4f}]")
print(f"     channel B:  gamma + c pi^2 - lambda pi^3   -> [{chB.min():.4f}, {chB.max():.4f}]"
      f"   (lambda = {LAM})")
print(f"     {'min of the union':>28} {full.min():.6f}")
print(f"     {'max of the union':>28} {full.max():.6f}")
print(f"     ** bounded below by gamma now?  {bool(full.min() >= GAM - 1e-12)} **")
assert not (full.min() >= GAM - 1e-12)
sub = (full < 0.75)
print(f"     ** but the SUB-THRESHOLD SPECTRAL SUBSPACE {{Gamma-hat < 3/4}} is still well defined: **")
print(f"        it carries {sub.sum()} of {len(full)} grid modes; its complement {(~sub).sum()}")
print(f"     ** and the straddle survives:  some below 3/4 {bool(sub.any())} · "
      f"some at or above {bool((~sub).any())} **")
assert sub.any() and (~sub).any()
print()
for s in [
 "⇒⇒ ** SO P10's STRUCTURE DOES NOT REST ON BOUNDEDNESS BELOW. **  *What the direct-integral",
 "   decomposition needs is that $\\hat\\Gamma$ commute with the radial part and that its spectrum",
 "   MEET BOTH SIDES of $\\tfrac34$ -- essential self-adjointness above, limit-circle below.  Both",
 "   survive an unbounded-below $\\hat\\Gamma$; the sub-threshold subspace is a spectral projection",
 "   and a spectral projection does not ask for a floor.*",
 "",
 "✔ ** THE REPAIR IS THEREFORE A QUALIFICATION AND NOT A RETRACTION: attach 'bounded below by",
 "   $\\gamma$' TO THE LEADING-ORDER OPERATOR, WHERE THE PARAGRAPH PROVES IT, and let the straddle",
 "   stand on what it actually uses. **  *Then the frontier sentence's 'including whether it is",
 "   bounded below' is asking about the complete operator only -- which is what it means.*",
 "",
 "⌗ *Small, and the reason it is worth the revision is the base rate it belongs to: **a paper states",
 "   a property where it needs one and questions the same property where it is being honest, and",
 "   the two sentences are 400 characters apart.**  This is the caption/body split of c54.107 with",
 "   both halves inside one paragraph.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — WHAT THE THREE ROWS ARE")
print("=" * 78)
print(f"  {'map item':>7} {'the row':>52} {'weight':>16}")
for x, y, z in [
    ("B·1", "the interacting tower as a defined theory", "OPEN, real"),
    ("B·2", "non-perturbative quantization / closed-form nonlinear", "OPEN, gated on A"),
    ("G·1", "does the empirical SM motivate the Wick face?", "OPEN, off-runway"),
]:
    print(f"  {x:>7} {y:>52} {z:>16}")
print()
for s in [
 "⇒ ** B·1 AND B·2 GO IN AS ONE ROW: they are the two faces of one frontier (the cosmological face",
 "   and the general dynamical face) and the map already says so. **  *`G·1` is its own row and",
 "   goes in at the weight the map assigns it -- exploratory, do-not-assert, gated on `A·5`'s",
 "   continuous side, which is `L-164`.*",
 "",
 "⌗⌗ ** AND THE STANDING ORDER THIS EARNS IS THE ONE THE `A·5` MISS ALREADY SHOULD HAVE: the fold",
 "   is not a one-time event, so the map's header claim gets CHECKED rather than asserted. **",
 "   *That is this file, and it is cheap to re-run.*",
]:
    print("  " + s)
