# r7694 (60) — RESULT: the cold read of `cor:stationary`'s new proof paragraph

Order: `r7691` (69). Registration: `PREDICTION.md`, committed and pushed before `probe.py` existed.
Tree: `runs/TREE.txt`. Readings: `runs/READINGS.txt` (the probe's own output, exit `0`, every
negative probe firing).

The order named **two things to check above all**. Both are answered, and the answers differ:

> **The hypothesis LIST is whole. The AMBIENT SETTING the sentence names is not the one the theorem
> holds in.** And **"cited and not formalised" is right**, established by a search that is reported
> rather than asserted.

| | verdict |
|---|---|
| 1a every field of `IsKillingHorizon` is stated | **SUPPORTED**, five of five |
| 1b no hypothesis is invented by the prose | **SUPPORTED** |
| 1c every clause's quantifier and locus | **SUPPORTED**, including "null **somewhere**" |
| 1d the ambient setting | **SCOPE-DIFFERS** — two hypotheses the cited remark disclaims |
| 2a the conclusion taken as the hypothesis | **SUPPORTED** |
| 2b "cited and not formalised" | **SUPPORTED** — the search is named |
| 2c the prose paragraph's analyticity | **SUPPORTED** — the division of labour holds |
| 3 three of the four conclusions | **SUPPORTED** |
| 3b "distinct points stay distinct" | **SCOPE-DIFFERS** — the probe's conjunct is guarded |
| 4 the witness | **SUPPORTED**, and it discharges the very predicate arm 1 reads |
| 4b the probe's own line reference | **STALE** — `l.288` against `l.290` on this tree |

---

## ITEM 1 — THE HYPOTHESES ARE STATED WHOLE, AND THE SETTING IS NOT

### 1a/1b/1c — the list is whole, in both directions, with its quantifiers intact

`IsKillingHorizon` has **five** fields, read at source, and the paragraph has a clause for every
one of them:

| field | the clause that states it |
|---|---|
| `C1` | "`X` continuously differentiable … on it" |
| `ne_zero` | "and nonzero on it" |
| `hRep_diff` | "the metric's chart representative differentiable … near it" |
| `killing` | "and `L_X g = 0` near it" |
| `generator` | "through each of its points an integral curve of `X` lying in it and null somewhere" |

And the converse holds: the prose asks nothing the structure does not — searched the hypothesis
sentence for `analytic`, `complete`, `compact`, `geodesic` and `connected`, and none occurs, so no
hypothesis is invented.

**The loci and quantifiers match clause for clause**, which is where this kind of sentence usually
slips: "on it" is `∀ p ∈ Hs` pointwise; "near it" is twice an `∀ᶠ … in 𝓝` — eventually in a
neighbourhood, not on the horizon itself; "through each of its points" is the per-point existential
`∀ p ∈ Hs, ∃ γ t₀`. **And "null somewhere" is exactly right and is the delicate one:** the field asks
`S.g (γ t₀) (X (γ t₀)) (X (γ t₀)) = 0` — null at *one* parameter of the generator — and the probe
*derives* nullity everywhere from it in a separate theorem (`st_null_of_isKillingHorizon`). A
paragraph that had written "null everywhere" would have stated the theorem's **output** as its
**input**. This one does not.

### 1d — **SCOPE-DIFFERS: the setting the sentence names is not the setting the theorem holds in**

The paragraph opens "In the setting of Remark `rem:formalised`". That remark says, in its own words
(`l.315`): *"a Hausdorff manifold with a `C¹` atlas, modelled on an **arbitrary real normed space**,
so that the theorem holds in **every dimension**."*

The section that holds **both** `IsKillingHorizon` and `st_cor_stationary` asks:

```
variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 2 N]
```

— **finite-dimensionality**, against "an arbitrary real normed space", and a **`C²` atlas**, against
"a `C¹` atlas". Both are hypotheses the remark explicitly disclaims, and the second disclaimer is the
remark's own stated *purpose* ("so that the theorem holds in every dimension"). So the sentence
borrows a generality this theorem has not got. It asks no Hausdorff of `N`, which is weaker than the
remark and harmless.

Nothing in the corollary is wrong: Schwarzschild is four-dimensional and smooth, and the witness
lives there. What is wrong is the scope the sentence claims for the machine-checked form.
**Six words, 69's or 71's to land:** "In the setting of Remark `rem:formalised`, **in finite
dimension and with a `C²` atlas**, let the horizon be …". Routed, not edited.

## ITEM 2 — "CITED AND NOT FORMALISED" IS RIGHT, AND THE SEARCH IS NAMED

**2a the positive half — SUPPORTED.** `st_cor_stationary` takes `hH : S.IsKillingHorizon X (S.H J)`,
and `S.H J` is `frontier (JpastSet J)` by definition. So its hypothesis *is* rigidity's conclusion:
the frontier of the causal past is a Killing horizon of `X`.

**2b the negative half — SUPPORTED, and this is an ABSENCE claim read as one.** What was searched,
reported rather than asserted: the whole probe for `analytic` — **three** occurrences, and the
reading classifies each by whether its position falls inside a `/- … -/` span or after a `--` on its
line; **all three are prose** (two docstrings and one header comment) and **none is a hypothesis**.
And the whole probe for any `theorem` or `lemma` whose name carries `rigid` or `stationar` — exactly
one, `st_cor_stationary` itself, which *assumes* the Killing-horizon property. So nothing in the
probe derives a Killing horizon from stationarity, and the sentence is right. Neither UNDERSTATED
nor OVERSTATED is reached, and the probe says the same in its own docstring: *"Rigidity itself is not
proved: it needs the Einstein equations, which are not in the kit; 'stationary' has no formal content
beyond invoking it."*

**2c the division of labour — SUPPORTED.** `l.290` carries the cited theorem and its analyticity and
hands off to `lem:killing`; the machine-checked paragraph, taking the conclusion, asks no analyticity
at all. The two paragraphs do not overlap and neither claims the other's ground.

## ITEM 3 — THREE CONCLUSIONS LAND; THE FOURTH CARRIES A GUARD THE PROSE DROPS

Read under their own binders (never at TOP):

- **"along every integral curve … the tangent is null" — SUPPORTED.** `∀ t ∈ Icc a b`, both
  `g(X, X) = 0` and `g(γ′, γ′) = 0`.
- **"every pair is metrically coincident" — SUPPORTED, and UNGUARDED.**
  `∀ t₁ ∈ Icc a b, ∀ t₂ ∈ Icc a b, kg_Related S.g γ t₁ t₂`, with `kg_deltaTau = 0`.
- **"the horizon's adapted splitting assigns `Δx = Δτ = 0`" — SUPPORTED.** `∃ σ` with `σ.n`, `σ.dt`
  and `σ.h` pinned to the horizon's own, and `σ.Δx = 0 ∧ σ.Δτ = 0`. The paragraph's definite article
  is earned: the splitting is identified, not merely asserted to exist.
- **"distinct points stay distinct" — SCOPE-DIFFERS.** The probe's conjunct is
  `InjOn γ (Icc a b) → ∀ t₁ t₂, t₁ ≠ t₂ → γ t₁ ≠ γ t₂`: **conditional on the generator being
  injective.** Without injectivity a generator may revisit a point and two parameters give one. The
  paragraph states it with no condition, and the conjunct *beside* it — metric coincidence — genuinely
  is unconditional, so a reader has no cue that one of the four is guarded and three are not.
  **Six words:** "distinct points stay distinct **where the generator is injective**". Routed, not
  edited.

## ITEM 4 — THE WITNESS IS THE PARAGRAPH'S OWN, AND ARM 1 IS NOT VACUOUS

`st_witness` is on `seWS = {p | 0 < p.2 ∧ p.1 * p.2 < 1}` — the paragraph's `{V>0, UV<1}` — with
`sq_L M x = (−x.1/(4M), x.2/(4M))`, which is the paragraph's `(V∂_V − U∂_U)/4M` to the factor and
the signs. It discharges **`IsKillingHorizon` itself**, not a weaker cousin, on
`frontier (ι⁻¹' JpastSet 𝓘⁺)` — so arm 1's hypothesis is satisfiable and the corollary is not
vacuous. And it puts two **distinct** events of that horizon, both on it, in metric coincidence
`kg_Related` **both ways**, with `kg_deltaTau = 0` and the splitting at `Δx = Δτ = 0`.

### 4b — the probe's own line reference has drifted

The probe cites P1 `l.288` for the rigidity citation, in two docstrings and its header. On this tree
that sentence is at **`l.290`**. Nothing in the paper is wrong and nothing in the proof depends on
it. But this seat's standing lesson applies to a probe exactly as to a reading: **a line number is a
claim about a TREE, and this one names none.** Routed as a precision item.

---

## TWO DEFECTS IN THIS SEAT'S OWN PROBE, FOUND BY ITS OWN READINGS AND RECORDED, NOT HIDDEN

1. **The first run reported `killing` as HYPOTHESIS OMITTED, and it was not.** The marker for that
   clause carried a **doubled backslash** where the paragraph writes one, so the matcher could never
   match it. *A matcher loose enough to mis-read its own input answers about the matcher* — this
   line's own first standing lesson, arriving inside the probe that carries the lesson. Fixed, and
   the comment stays in `probe.py` beside the marker.
2. **A guard refused a correctly anchored marker.** `G2`'s escaped-control-sequence form was tested
   as *two* leading backslashes, so `\mathcal{L}_Xg=0` — one backslash, a real control sequence — was
   REFUSED. The earlier revisions never noticed because their markers happened to be double-escaped
   by habit. Fixed in `anchor()`, with the reasoning recorded there.

Both are reported because a cold read that hides its own misreadings is worth less than one that
shows them: the two-way wholeness reading is what caught the first, and the guard log the second.

## WHAT THIS REVISION ADDS TO THIS LINE'S STANDING LESSONS

**"In the setting of X" is a HYPOTHESIS, and it is the one most likely to be borrowed rather than
checked.** A hypothesis list can be complete clause for clause and still sit inside an ambient
setting the sentence has taken from somewhere else — and the ambient setting is where the
quantifier "in every dimension" lives. So the wholeness of a hypothesis list is two questions, not
one: *are all the named hypotheses there*, and *is the setting they are named in this theorem's
setting*. Here the first answer is yes and the second is no.

## LIMITS, STATED

- `1d` and `3b` are both statements about **what the sentence claims**, not about whether the
  corollary is true: Schwarzschild is finite-dimensional and smooth, and the witness is injective.
- The three repairs found are **routed** in `FOR_66_FROM_60.md`; the two in P1 are 69's and the
  probe's line reference is 71's.
- Nothing in `corpus/`, `receipts/`, `scripts/` or `computations/formalisation/` is edited.
- `r7692`'s count fork is closed by `r7691` and is not re-opened: both counts were right for what
  they counted.
