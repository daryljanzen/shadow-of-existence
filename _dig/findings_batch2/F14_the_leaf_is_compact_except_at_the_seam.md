# F14 — P14's leaf-compactness claim, which carries the generation index, holds on every sub-Nariai member and fails at the Nariai member — and the paper does not say which one it is on

*status: BOUNDED NEGATIVE (scope of a stated hypothesis) + a question I cannot settle from here.*
*receipt: `DRAFT_P14_the_leaf_is_compact_except_at_the_seam.py`, rc=0.*
*touches: P14 `sec:count`, the sentence citing [AtiyahSinger1968]; `P14_leaf_compactness.py`.*

---

## The sentence

P14 offers leaf compactness in place of the bulk index P13's non-compactness obstructs:

> *In the leaf's proper measure dℓ = dr/√|f| the closed slicing has **finite** total length — the
> horizon turning points at finite proper distance, the r=0 crossing an integrable √-singularity —
> so **the leaf is compact and the Dirac operator on it carries a well-defined analytical index
> dim ker**, exactly where the bulk index on the non-compact spacetime is obstructed.*

`P14_leaf_compactness.py` verifies it, and verifies it well — five checks, an exponent test, and a
control that fabricates a simple-pole measure to show the test has teeth. **It runs at M = 0.12α.**

The Nariai mass is M_N = α/(3√3) = 0.19245, so the receipt runs at **0.62 M_N**, where f has three
**simple** roots. Reproduced exactly: between-horizon leaf length **1.7671**, matching the
receipt's printed value.

## At the Nariai member the exponent changes

There the two positive roots **merge** at r₀ = α/√3 — P14's own `sec:cosmogenesis` says so
(*"the Nariai crest is the fixed point of the root-permutation, where two of the three roots
merge"*). Verified: f(r₀) = −5.6×10⁻¹⁷, f′(r₀) = −5.6×10⁻¹⁰, **f″(r₀) = −6.0000** = −6/α² exactly.
So

> |f| ~ 3(r−r₀)²/α² ⟹ **1/√|f| ~ α/(√3 |r−r₀|)** — a simple **pole**, not a square root.

| cutoff d | ∫ from r₀+d | (α/√3)·ln(0.05/d) |
|---|---|---|
| 10⁻² | 0.9422 | 0.9292 |
| 10⁻³ | 2.2746 | 2.2586 |
| 10⁻⁴ | 3.6043 | 3.5880 |
| 10⁻⁶ | 6.2631 | 6.2468 |

**Logarithmically divergent, at exactly the rate α/√3 per e-fold.** And that is the very exponent
`P14_leaf_compactness`'s own control identifies as non-integrable — the control fabricates a simple
pole to prove the test discriminates, and the Nariai member supplies one for free.

## A discontinuity, not a limit

| M/M_N | ∫_{r_b}^{r_c} dr/√f |
|---|---|
| 0.500 | 1.74631 |
| 0.900 | 1.80320 |
| 0.999 | 1.81370 |
| 0.99999 | 1.81380 |
| — | **πα/√3 = 1.81380** |

The between-horizon length tends to a clean closed form **πα/√3** as the roots merge, and the
outside pieces stay integrable at each simple root. **But at M = M_N the f > 0 region has closed
up**, both approaches to r₀ run through f < 0, and the divergence above is what is left.

> The leaf's total proper length is **finite on the whole open family and infinite at its
> endpoint**.

## Why the endpoint is not an exotic corner

**It is the seam.** P16's spine has the beginning as a collapse *"through the finite-curvature
degenerate (κ = 0) Nariai seam"*; P7's lap is drawn on the Nariai member and names its two seams as
r = −2α/√3 and **r = +α/√3**, the second of which *is* the double root; P3's dial peaks there.

## And the walls themselves are fine, at every member

P14's three zero-modes sit at **r = 0** on the throat circle. Near r = 0, |f| ~ 2M/|r|, so
1/√|f| ~ √(|r|/2M) → 0 — integrable, and integrable at **every** member including Nariai (verified:
converges at both M = 0.5 M_N and M = M_N).

**So the modes' own locus is not where the trouble is.** This is about the front seam at the far
end of the same closed slicing.

## The question

> **On which member is P14's leaf?** The sentence does not say, and the answer decides whether this
> is a clause or a repair.

- **Generic member** (the receipt's reading): everything is right, and what is owed is a clause —
  the claim holds for M < M_N and fails at the degenerate member, so the index is a statement about
  the open family.
- **Nariai member**: *"the leaf is compact"* is false there, and with it *"the Dirac operator on it
  carries a well-defined analytical index dim ker."* The argument would need a different measure, a
  regularisation at the double root, or an explicit restriction to M < M_N.

This is not a small matter of wording: the count of three generations is stated as a wall-localised
index, and leaf compactness is precisely what P14 offers where the bulk index is obstructed. **The
load-bearing sentence should name its member.**

## Not claimed

- **No claim that the generation count is wrong.** The three walls are at r = 0, integrable at every
  member.
- **No claim that `P14_leaf_compactness` is wrong.** It is a good receipt and every check in it
  passes at the member it runs — including the control, which is what made the Nariai case legible.
- No claim about which member the corpus *intends*. The receipt and the surrounding papers point
  different ways, and that is the whole of the finding.
- No closure on any registered item.
