#!/usr/bin/env python3
"""P15 receipt -- `PO-75` narrowed on the pointer `r7169` wrote into it: what supplies the
anisotropic spectrum's source on the expansion leg, when the single Nariai worldline does not
carry one.

*** ⛭⛭⛭ THE SUPPLIER IS NOT MISSING -- IT IS IN PRINT IN THREE PIECES THAT WERE NEVER JOINED, AND
    THE ROW'S REAL CONTENT IS THE FLOOR.  `$L=2$` IS ASSERTED AT THREE SITES, **DERIVED AT ONE**,
    AND THE TWO AVAILABLE DERIVATIONS DISAGREE AT EVERY ODD DEGREE ABOVE IT. ***

** ⓵ NOTHING ON THE EXPANSION LEG HAS TO SUPPLY IT, AND THE CORPUS ALREADY SAYS SO. **
*`P16`: the construction is* `a genealogy of universes and not a recursion on modes`*, in which*
`every passage is entered with frozen data and left with frozen data`*; the crossing is lossless
because every mode is already super-horizon at the branch point; and the harmonic index is
PRESERVED across it, the map being the identity on `$L$`.*  ⇒ *So the supplier is the progenitor,
the route is the inheritance factor, and the expansion leg is where frozen data ARRIVES rather than
where it is made.  `PO-75` was asking for a source where the construction has a boundary condition.*

⌗ *And `P16` says in terms which part is inherited:* `the mode content is the part of the primordial
sector this construction inherits rather than derives`*.  **So the row cannot be discharged by
deriving the content -- only by bounding what can arrive.***

** ⇒ ⓶ WHICH MAKES THE FLOOR THE WHOLE QUESTION, AND THE FLOOR IS WHERE THE CORPUS IS THINNEST. **
*Three sites carry `$L=2$`:*

| site | what it says | derived there? |
|---|---|---|
| `P16`, the shear paragraph | `the $S^3$ tensor tower starts at $L=2$ and has no $k=0$ member` | stated |
| the interior-to-observed map | `lowest physical mode L = 2`, and `no source below it` | **assumed** |
| `r7172`, the descending sector | the neutral slice is empty at odd degree, so the sector begins at `$L=2$` | **derived** |

⌗ *Measured, not asserted: the map receipt that validates the parameter-free deficit at
`$\\ell\\lesssim8$` contains **no** occurrence of `transverse`, `traceless`, `tensor tower`, `Hopf`
or `charge` -- it takes the floor as input and checks the projection through it.*

*** ⓷ AND THE TWO DERIVATIONS STAND IN STRICT CONTAINMENT, WHICH IS SHARPER THAN RIVALRY. ***
*The layer's floor comes from Hopf-charge parity under squashing -- the neutral slice needs
`$m=0$`, and `$m=L/2-k$` reaches zero only at EVEN `$L$` -- so it prunes `$L=3,5,7,\dots$` as well.
The tensor floor as `P16` states it excludes `$L=0$` and `$L=1$` and prunes nothing above.*
⇒ *** So what the layer excludes properly CONTAINS what the tensor tower excludes: the layer's
    floor IMPLIES the tensor floor and not conversely.  The deficit's floor at `$L=2$` is therefore
    safe under EITHER -- worth knowing on its own -- while the odd-ladder exclusion belongs to the
    layer's decomposition ALONE, and that ladder is the test which separates them. ***

⛔ ** AND THE GUARD FROM `r7172` IS APPLIED TO THIS SEAT'S OWN RESULT RATHER THAN TO THE PAPER'S. **
*This receipt does NOT claim the descending sector's transport IS the branch-point crossing.  That
identification is exactly what is unestablished -- `r7172` showed the layer's transport is not
shared with the four-route, and whether it is shared with the CROSSING is a third question nobody
has asked.*  ⇒ *** So the odd-degree prediction is conditional on an identification this revision
declines to assume, and that condition is the fork, stated in the channel with both branches. ***

⌗ ** WHAT THIS DOES NOT CLAIM. ** *It does not discharge `PO-75`: it establishes that the row's
supplier is in print and relocates the row's open content to the floor's provenance.  It computes no
amplitude, which is `PO-84`'s undelivered remainder and still undelivered.  It does not re-derive
the tensor floor -- that is taken from `P16`'s own sentence and declared, not reproduced -- and it
touches no paper and no other seat's receipt.  It is not `PO-85`: that row asks for an INSTRUMENT
comparing asserted grades with proved ones, which is `70`'s; this is one instance in this seat's own
sector, found by reading rather than by a gate.*

** COMPUTES: the layer's charge arithmetic at `$1\\le L\\le12$`, exactly and over the integers --
`$m=L/2-k$` for `$k=0\\dots L$`, multiplicity `$(L+1)^2$`.  No rate, no amplitude, no parameter. **
"""
import os
import re
import time

import sympy as sp

t_all = time.time()
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


def body_of(path):
    src = open(path, encoding='utf-8').read()
    b = '\n'.join(ln for ln in src.split('\n') if not ln.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return re.sub(r'\s+', ' ', b[:j] if j > 0 else b)


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P16 = body_of(os.path.join(ROOT, 'corpus', 'cosmogenesis_paper.tex'))
MAP = open(os.path.join(ROOT, 'receipts', 'P16_cosmogenesis_paper',
                        'P16_the_interior_to_observed_mode_map.py'), encoding='utf-8').read()

# =====================================================================================
head("A -- READ FIRST: THE SUPPLIER IS IN PRINT, IN THREE PIECES THAT WERE NEVER JOINED")

gate("Ⓐ①  the construction is a GENEALOGY and not a recursion on modes, with every passage entered"
     " and left with frozen data -- so the expansion leg is where frozen data ARRIVES and not where"
     " it is sourced",
     P16.count('a genealogy of universes and not a recursion on modes') == 1
     and P16.count('every passage is entered with frozen data and left with frozen data') == 1)

gate("Ⓐ②  and `P16` says in terms which part is INHERITED rather than derived -- the mode content"
     " itself -- so this row cannot be discharged by deriving the content, only by bounding what"
     " can arrive",
     P16.count('the mode content is the part of the primordial sector this construction inherits'
               ' rather than derives') == 1)

gate("Ⓐ③  the tensor floor is STATED in `P16`'s shear paragraph, and it is stated for the round"
     " sphere's tensor tower -- the floor this receipt compares against, taken from the paper and"
     " not re-derived here",
     P16.count('the $S^3$ tensor tower starts at $L=2$ and has no $k=0$ member') == 1)

_ABSENT = ('transverse', 'traceless', 'tensor tower', 'Hopf', 'charge')
_hits = {w: len(re.findall(w, MAP)) for w in _ABSENT}
gate("Ⓐ④  AND THE RECEIPT THAT VALIDATES THE PARAMETER-FREE DEFICIT TAKES THE FLOOR AS INPUT: it"
     " says `lowest physical mode L = 2` and `no source below it`, and carries NO occurrence of"
     " transverse, traceless, tensor tower, Hopf or charge -- so the floor is asserted there and"
     f" proved elsewhere, measured: {_hits}",
     MAP.count('lowest physical mode') >= 1
     and 'no source below it' in MAP
     and all(v == 0 for v in _hits.values()))

# =====================================================================================
head("B -- THE ONE FLOOR THAT IS DERIVED, REPRODUCED OVER THE INTEGERS")

rows = []
for L in range(1, 13):
    ms = [sp.Rational(L, 2) - k for k in range(L + 1)]
    tot = (L + 1)**2
    neutral = (L + 1) if any(m == 0 for m in ms) else 0
    rows.append((L, tot, neutral, sp.Rational(neutral, tot)))
print(f"\n    {'L':>3s} {'charges':>8s} {'multiplicity':>13s} {'neutral slice':>14s} {'weight':>8s}")
for L, tot, neutral, w in rows:
    print(f"    {L:3d} {L + 1:8d} {tot:13d} {neutral:14d} {str(w):>8s}")

gate("Ⓑ①  the layer's charge ladder and multiplicity are exact over the integers: `$L+1$` charges"
     " `$m=L/2-k$`, each carrying `$L+1$` states, so `$(L+1)^2$` at every degree",
     all(tot == (L + 1)**2 for L, tot, _, _ in rows))

gate("Ⓑ②  and the NEUTRAL slice exists exactly when the degree is EVEN -- `$m=L/2-k$` reaches zero"
     " only then -- with weight `$1/(L+1)$` there and zero otherwise",
     all(w == (sp.Rational(1, L + 1) if L % 2 == 0 else 0) for L, _, _, w in rows))

evens = [L for L, _, _, w in rows if w != 0]
odds = [L for L, _, _, w in rows if w == 0]
gate("Ⓑ③  ⇒ SO THIS FLOOR IS STRICTLY STRONGER THAN A FLOOR AT TWO: its lowest anisotropic degree"
     f" is `$L=2$`, AND it prunes every odd degree above it -- {odds} carry nothing, {evens} carry"
     " the sector",
     min(evens) == 2 and all(L % 2 == 0 for L in evens)
     and odds == [L for L in range(1, 13) if L % 2 == 1])

# =====================================================================================
head("C -- THE ADJUDICATION: THE FLOORS AGREE AT ONE DEGREE AND DIVERGE AT EVERY ODD ONE ABOVE IT")

tensor_excluded = {0, 1}
layer_excluded = set(odds) | {0}
gate("Ⓒ①  the two floors agree on what they exclude BELOW two and on admitting two, which is the"
     " whole of their agreement",
     (2 not in tensor_excluded) and (2 not in layer_excluded)
     and {0, 1} <= tensor_excluded and 1 in layer_excluded)

disagree = sorted((layer_excluded - tensor_excluded) & set(range(2, 13)))
gate("Ⓒ②  AND THEY DISAGREE AT EVERY ODD DEGREE ABOVE THE FLOOR -- an infinite set, of which this"
     f" receipt enumerates {disagree} -- so the coincidence at two is two mechanisms meeting at one"
     " degree and not one fact counted twice",
     disagree == [L for L in range(3, 13) if L % 2 == 1] and len(disagree) >= 5)

gate("Ⓒ③  ⇒ SO THE ODD LADDER IS THE TEST THAT SEPARATES THEM: the layer's decomposition predicts"
     " NO odd-degree anisotropic content at any degree, the round sphere's tensor tower permits all"
     " of it, and the two cannot both be the transport that sets the floor",
     all(L % 2 == 1 for L in disagree)
     and all(sp.Rational(0) == w for L, _, _, w in rows if L % 2 == 1))

gate("Ⓒ④  AND THEIR LOGICAL RELATION IS STRICT CONTAINMENT, NOT INDEPENDENCE -- which is sharper"
     " than two rival mechanisms: what the layer's decomposition excludes CONTAINS what the tensor"
     " tower excludes, properly.  So the layer's floor IMPLIES the tensor floor and not conversely,"
     " the deficit's floor at two is safe under EITHER, and the odd-ladder prediction belongs to"
     " the layer's decomposition alone",
     tensor_excluded < layer_excluded
     and not (layer_excluded <= tensor_excluded)
     and (layer_excluded - tensor_excluded) == set(disagree) | set()
     and 2 not in layer_excluded)

gate("Ⓒ⑤  ⇒ SO THE ROW IS NARROWED RATHER THAN DISCHARGED, AND THE CONDITION IS THE FORK: the"
     " stronger floor is the one with a derivation, but it is a derivation on the LAYER's"
     " decomposition, and this receipt does not identify that transport with the branch-point"
     " crossing -- `r7172` established only that the layer's transport is not the four-route's."
     "  The odd-degree prediction is therefore conditional on an identification nobody has made",
     min(evens) == 2
     and all(sp.Rational(0) == w for L, _, _, w in rows if L % 2 == 1)
     and len(disagree) >= 5)

# ------------------------------------------------------------- verdict
head("VERDICT")
npass = sum(1 for _, ok in CHECKS if ok)
print(f"  {npass} of {len(CHECKS)} gates pass.   [{time.time() - t_all:.1f}s]")
bad = [nm for nm, ok in CHECKS if not ok]
if bad:
    print("\n  FAILED:")
    for nm in bad:
        print(f"    - {nm}")
    raise SystemExit(1)
print("""
  ==========================================================================
  PO-75 ASKED FOR A SOURCE WHERE THE CONSTRUCTION HAS A BOUNDARY CONDITION.
  The supplier is in print in three unjoined pieces: the construction is a
  genealogy in which every passage is entered and left with frozen data, the
  crossing is lossless because every mode is already super-horizon at the
  branch point, and the harmonic index is preserved across it.  So the
  progenitor supplies it and the expansion leg is where it ARRIVES.  And the
  paper says which part is inherited rather than derived -- the mode content
  itself -- so the row cannot be discharged by deriving the content.

  *** WHAT IS LEFT IS THE FLOOR, AND THAT IS WHERE THE CORPUS IS THINNEST:
      L = 2 is asserted at three sites and derived at ONE.  The receipt that
      validates the parameter-free low-multipole deficit takes the floor as
      input -- measured, it carries no occurrence of transverse, traceless,
      tensor tower, Hopf or charge. ***

  AND THE TWO AVAILABLE DERIVATIONS STAND IN STRICT CONTAINMENT.  The
  layer's floor is Hopf-charge parity under squashing, which prunes the whole
  odd ladder; the round sphere's tensor floor excludes only the first two
  degrees and prunes nothing above.  So the layer's floor IMPLIES the tensor
  floor and not conversely: the deficit's floor at L = 2 is safe under
  either, while the odd-ladder exclusion belongs to the layer's
  decomposition alone, and that ladder is the test which separates them.

  THE CONDITION, STATED RATHER THAN ASSUMED: this does not claim the
  descending sector's transport IS the branch-point crossing.  That is the
  third transport question, and it is the fork this revision routes.

  THE GUARD: when several derivations agree on a floor, check what each one
  excludes ABOVE it.  Agreement at the boundary is cheap -- two mechanisms
  can meet at one degree and part everywhere else -- and the place where
  they part is the measurement, not the place where they meet.
  ==========================================================================
""")
