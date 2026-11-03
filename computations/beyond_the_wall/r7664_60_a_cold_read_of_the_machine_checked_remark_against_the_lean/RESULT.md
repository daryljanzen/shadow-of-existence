# `r7664` — the verdict: thirteen of the remark's twenty claims stand, six do not, one this seat cannot decide

Order `r7663` asked for a cold read of P1's `rem:formalised` against the Lean, sentence by
sentence. Twenty claims were fixed in `PREDICTION.md` before any bank was taken; the tree they
are verdicts on is in `runs/TREE.txt`; `cold_read.py` derives every verdict from text parsed out
of the Lean and prints the parse beside it. **13 SUPPORTED · 6 NOT SUPPORTED · 1 UNMEASURED BY
THIS SEAT.**

## What the remark gets right

The setting, the hypotheses on `O` and `Θ`, properness, the Kuratowski clause, the two clauses it
declares absent, and every one of the five witnesses are carried by the Lean as stated. Three are
worth naming because they are exact where a summary would normally go loose:

- **`IsCauchyTemporalOn`** is the intrinsic property on `D` — temporal plus a unique crossing for
  every inextendible causal curve **in `D`** — so "Cauchy temporal function of `D`" is not a
  statement about surfaces of the whole spacetime, which is the distinction `rem:penetrating`
  turns on.
- **`KLi`/`KLs`** unfold to "every neighbourhood met for all sufficiently late `τ`" and "met
  frequently"; the remark's gloss names the substantive inclusion of each equality and names it
  correctly.
- **`cz_witness_headline_F`** really does leave the tangency clause in its general form, `∀ q ∈
  frontier, ∀ ℓ n L C ℓ₀, …`, for every positive `C¹` `F̂`, with no point instantiated — the one
  place the remark distinguishes a general implication from an instantiation, and it is right.

## The six that do not stand

**⑨ *assumes only* names the wrong carrier.** The theorem assumes **three** carrier clauses —
`hJM : J ⊆ S.M`, `hHM : ∂J⁻(𝒥⁺) ⊆ S.M`, `h𝒥 : 𝒥⁺ ⊆ S̃.M` — on `J`, on the horizon and on `𝒥⁺`.
The remark names two, "the worldline and `𝓗⁺`", and **the worldline's carrier is not assumed at
all**: `range O ⊆ S.M` is derived from the chronological ordering by `mx_range_subset_M`. What
stands in its place is the carrier of `J`, the set whose chronological past is `D`, which is not
the worldline. `r7662` reported these as "carrier bookkeeping for `J` and the horizon"; the
remark substituted the worldline for `J`, and `𝒥⁺`'s own carrier went unnamed in both.

**⑧ the tangency clause has a hypothesis the remark does not state.** `FrameHyp` is
`NullFrame (bil g) ℓ n ∧ ∀ v, FutCausal (bil g) ℓ n v → 0 < ξ v` — a null frame **and `dΘ`
positive on the future causal cone of `(ℓ, n)`**. The remark states only "null frames `(ℓ,n)`".
The second half is not implied by `Θ` being temporal on `D`, because the hypothesis is asked
eventually along a filter converging to a point **of** `𝓗⁺`, where `IsTemporalOn (S.D J)` says
nothing. Separately, the limit is of `covCh Θ q x`, `dΘ_x` re-read **in the chart at `q`**; the
remark attaches "in a chart" to the bound on `n` alone, and without the chart-reading its
`dΘ/dΘ(n) → −g(ℓ₀,·)` compares covectors at different points.

**⑤ the first of the four is half in a different theorem.** The first conjunct is
`S.H J = ∂J⁻(𝒥⁺)`, i.e. `∂J⁻(J) = ∂J⁻(𝒥⁺)`. The remark's first of four is
`∂J⁻(O) = ∂J⁻(𝒥⁺) = 𝓗⁺`, and `S.H (range O)` does not occur in this theorem's conclusion: it is
the first conjunct of `mx_H_eq_boundary`, which the remark names one clause earlier. The pair
carries the double equality; the theorem the sentence attributes it to carries one half.

**③ the extension is described by five of its seven fields.** `ConformalExtension` has `ι`,
`isOpenEmbedding`, `contMDiff`, `Ω`, `Ω_pos`, `conformal`, **`timeOrient`** and **`maps_M`**. The
agreement of the time orientations under `Dι` on `M`, and `ι(M) ⊆ M̃`, are unstated — and they are
hypotheses, not bookkeeping: without `timeOrient` the extension need not respect the future.

**⑪ *its standard equivalent* is not machine-checked.** The word "hyperbolic" does not occur once
in the three probe files. That global hyperbolicity enters only through `hΘ` is supported — it is
the single binder in which `D`'s causal character is used — but the appositive is a claim about
the literature standing unmarked inside a remark headed "Machine-checked form".

**⑲ the reason the cylinder does not exercise the identification is reported, not built.** The
non-exercise is right: no `ConformalExtension` is built there. But `CylinderWitness.lean`'s own
header carries the reason under the heading "**`ConformalExtension` / `mx_prop_causal_alignment`
— REPORTED, not built**" — the argument that a conformal `g̃ = h(−du dv) + k dy²` needs `k = Ω²`
and `h = Ω²(1+U²)(1+V²)`, so either the circle's size vanishes at `𝒥⁺` or `h` blows up. No
theorem states it. The probe file marks it as reported; the remark does not.

## ① what this seat cannot decide

"No unproved step and no axioms beyond Lean's standard three" needs `#print axioms`' **output**,
and there is no toolchain and no Mathlib on this tree. What is measurable: the file requests the
audit for **both** named theorems (`mx_prop_causal_alignment`, `mx_H_eq_boundary`) among 62
`#print axioms` lines, and `sorry`, `admit`, `native_decide` and `axiom` declarations number zero
across the three probe files. That is not the claim and is not reported as the claim. *A first
reading of a hundred-line window around the block saw the `mx_` names absent and was about to be
reported as a defect in the attestation's evidence; enumerating the block instead of reading a
window corrected it. The window, not the file, was short.*

## Five things the Lean proves that the remark omits

1. **The theorem is dimension-free.** `E` carries `NormedAddCommGroup` and `NormedSpace ℝ` and
   nothing else — no `FiniteDimensional`, no `CompleteSpace`, anywhere in the three files. The
   closing sentence speaks only of which **witnesses** are built, leaving a reader to suppose the
   theorem is tied to low dimension.
2. **The atlas is `C¹` too.** `[IsManifold 𝓘(ℝ,E) 1 N]`, not `⊤`. The remark's "no smoothness
   beyond `C¹`" is said of the metric and the maps; that it holds of the charted structure is
   stronger and unsaid.
3. **`mc_witness_tangency_fails` is never named**, though it is the sharper half of the pair the
   remark's ⑮ describes: `Θf` satisfies every hypothesis of the proposition **except** the rate
   limit and the tangency conclusion fails, so the rate hypothesis is shown necessary rather than
   convenient. The remark cites `mx_witness_headline`, which says nothing about `Θf`.
4. **`cz_exp_nonvacuous`** exhibits `F̂ = e^{UV}` with `g_F ≠ g`. Without it nothing in the remark
   rules out the `F`-family being the flat metric relabelled.
5. **`range ι ≠ univ`** is a conjunct of `cz_witness_headline`: the extension is proper, the
   boundary genuinely added. The remark gives the compact closure and not this.

## The arms, scored

| arm | registered | outcome |
|---|---|---|
| ⓵ binder census | zero binders unaccounted; ⑨'s *assumes only* complete | **MISS** — three carriers assumed, two named, and the one most prominently named is derived |
| ⓶ conclusion census | the four cover every conjunct; the regrouping loses none | **HIT** — all seven covered, none lost; registered as the likeliest miss and it was not |
| ⓷ *standard equivalent* | no Lean statement of it | **HIT** — zero occurrences of "hyperbolic" |
| ⓸ attestation | undecidable by this seat | **HIT**, with the audit shown requested for both named theorems |
| ⓹ omission side | at least one | **HIT** — five |
| ⓺ guard | both probes flip or the receipt is withdrawn | **HIT** — and it caught four of my own verdicts written as constants |

That is a thirty-third of this seat's own registered rule conditions corrected by measurement
rather than by reading.

## What the guard caught in this instrument

The first draft wrote ⑧, ⑨, ⑪ and ⑲ as constant verdicts — `score('⑧', 'NOT SUPPORTED', …)` —
with the readings printed beside them but not wired to them. A verdict that cannot come out the
other way measures nothing, so each is now a function of its readings and a second guard family
re-evaluates all four with their inputs negated and stops the run if one does not flip.

And ⑬'s two-chart probe returned **False** against a file that plainly carries the atlas
`{idH, nullH}`: the docstring wraps between "the" and "atlas", and the probe could not see across
the line break. Its False reading was printed and ignored, because the verdict did not depend on
it either. Both are the same standing lesson in its fourth form — *a parser loose enough to
mis-read its own input answers about the parser* — and this time it was caught by the guard
rather than by a later seat. Every prose probe now runs on a whitespace-flattened copy, and
every printed reading bears on a verdict.
