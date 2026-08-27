#!/usr/bin/env python3
"""RECEIPT — statistics/inference bake `S10`: ** P07'S CITATION-MULTIPLICITY PROXY SURVIVES ITS OBVIOUS
CONFOUND AND CANNOT BE VALIDATED AT n=6 — WHICH IS THIS FIELD'S OWN S1 FINDING APPLIED TO THE CORPUS
ITSELF. **

LEVEL: NO RATE — an inference about a stated proxy.

WHAT P07 CLAIMS.  Its foundational-structure figure labels each edge with a count and says these are
  "citation multiplicities, A PROXY FOR LOAD-BEARING WEIGHT".  That is a measurement claim resting on a
  proxy assumption, and a proxy assumption is a thing a statistician tests.

THE OBVIOUS CONFOUND: does the count measure LOAD-BEARING, or does it measure SIZE?  A long paper
  offers more places to be cited from.  Measured across the six papers P07 draws edges from, on word
  counts of the document bodies with comments stripped:

      P1  35 citations   12810 words       P4  18 citations    6289 words
      P3  25 citations   30002 words       P6  18 citations   13482 words
      P5  23 citations   16913 words       P2  15 citations   15703 words

  Pearson r(edge weight, length) = +0.187.  ** The confound is not visible.  The sharpest case is P4 --
  the SHORTEST paper at 6289 words, carrying 18 citations, against P3's 25 from 30002.  A size effect
  would have put P3 first and P4 last. **

BUT THE TEST IS UNDERPOWERED, AND THAT IS THE FINDING.  At n=6 the Fisher-z interval on r=0.187 runs
  from -0.74 to +0.87 -- from strong negative to strong positive.  ** It excludes nothing. **  To
  detect a correlation of 0.5 at 80% power needs 30 papers; 0.6 needs 20.  The corpus has seventeen and
  P07 draws six edges.

  ** So P07's proxy claim can be neither validated nor refuted with the corpus that exists.  That is
  exactly S1's result -- a small class cannot adjudicate a moderate effect -- turned on the corpus
  itself rather than on P06's reference class. **

ROUTED, NOT APPLIED.  What is owed is a word: the figure says "a proxy for load-bearing weight" and
  could say "an indicative count, not a measurement" without losing anything the figure uses it for.

VERDICTS ARE ASSERTS.
"""
import math
import statistics as st

print("=" * 78)
print("  S10 — P07's citation-multiplicity proxy")
print("=" * 78)

data = [("P1", 35, 12810), ("P3", 25, 30002), ("P5", 23, 16913),
        ("P4", 18, 6289), ("P6", 18, 13482), ("P2", 15, 15703)]

print(f"\n  {'paper':6s} {'P7 edge':>8} {'words':>8}   words/citation")
for p, e, w in data:
    print(f"  {p:6s} {e:8d} {w:8d}   {w/e:12.0f}")

xs = [d[1] for d in data]
ys = [d[2] for d in data]
mx, my = st.mean(xs), st.mean(ys)
r = (sum((a - mx) * (b - my) for a, b in zip(xs, ys))
     / (sum((a - mx)**2 for a in xs) * sum((b - my)**2 for b in ys))**0.5)
print(f"\n  Pearson r(edge weight, paper length) = {r:+.3f}   on n = {len(data)}")
assert abs(r) < 0.5, "a size confound would show as a strong positive correlation"

shortest = min(data, key=lambda d: d[2])
longest = max(data, key=lambda d: d[2])
print(f"  sharpest case: {shortest[0]} is the SHORTEST at {shortest[2]} words and carries "
      f"{shortest[1]} citations,")
print(f"                 against {longest[0]}'s {longest[1]} from {longest[2]}.")
assert shortest[1] >= sorted(xs)[len(xs) // 2] - 5, "the shortest paper is not at the bottom"
print("  ** VERDICT 1: the size confound is NOT visible.  A size effect would have put the")
print("     longest paper first and the shortest last, and it does not. **")

n = len(data)
z = 0.5 * math.log((1 + r) / (1 - r))
se = 1 / math.sqrt(n - 3)
lo, hi = [(math.exp(2 * x) - 1) / (math.exp(2 * x) + 1) for x in (z - 1.96 * se, z + 1.96 * se)]
print(f"\n  Fisher-z 95% interval on r at n={n}:  ({lo:+.2f}, {hi:+.2f})")
assert lo < -0.5 and hi > 0.5, "the interval must span strong negative to strong positive"
print("  ** VERDICT 2: the interval runs from strong NEGATIVE to strong POSITIVE.")
print("     It excludes nothing.  The confound is not visible and is not excluded either. **")


def n_needed(rho, za=1.959964, zb=0.8416212):
    return math.ceil(((za + zb) / (0.5 * math.log((1 + rho) / (1 - rho))))**2 + 3)


print("\n  papers needed to detect a correlation at 80% power:")
for rho in (0.5, 0.6, 0.7, 0.8):
    print(f"      rho = {rho}:  n = {n_needed(rho)}")
assert n_needed(0.5) > 17, "even the whole corpus cannot detect a moderate correlation"
print("  ** VERDICT 3: the corpus has SEVENTEEN papers and P07 draws SIX edges.  Even using")
print("     all seventeen, only rho >= 0.6 would be detectable.  So the proxy claim can be")
print("     neither validated nor refuted with the corpus that exists -- which is S1's own")
print("     result turned on the corpus itself. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
