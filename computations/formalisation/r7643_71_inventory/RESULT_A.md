# `r7643+71.3` — RESULT: the inventory of P1, `r7643` ②. Of P1's `8` statements, none is BUILT whole. Two have BUILT clauses (`thm:metric-singularity`'s `Δτ = 0` algebra and `lem:alignment` (ii)'s static and retarded limits). Every causal clause is at least BUILT IN PART, and the proposed campaign 81 removes the stated hypotheses `hcl` and `hint` from the headline theorem. ⌗ Registered expectations: `1` holds, `1` holds only conditionally, `2` fail; the joint p `0.6` did not come true

*Against `PREDICTION.md` (`r7643+71.2`). The full inventory, one section per statement, is `INVENTORY.md` beside this
file. It was drafted by a reading agent under the registered method. 71 then checked, by grep in the probes, all `22`
theorem names it cites.*

## Marks

| statement | BUILT | BUILT IN PART | NOT BEGUN |
|---|---|---|---|
| `thm:metric-singularity` | the `Δτ = 0` algebra | the along-the-connection form, in a flat frame | "distinct and causally ordered" |
| `cor:threefold` | — | (iii), (iv-a), (iv-b): flat, coordinate-temporal | (i), (ii) |
| EF corollary | — | 3a: general chart, no Schwarzschild instance | 3b (the pieces exist in `NoConnectionSweep`, uncombined), 3c |
| `lem:killing` | — | all four clauses: one global adapted chart, no witness with a null orbit | — |
| `cor:stationary` | — | rigidity assumed, as P1 assumes it | — |
| `prop:causal-alignment` | — | every clause | — |
| `cor:densities` | — | 7a, 7b (`cs_BH_inter_slice`, `cs_slice_subset_D`) | 7c–7e: singularity, matter, densities |
| `lem:alignment` | (ii), the static lapse and retarded norm limits | (i), and the tangency, pending campaign 80 | the retarded slicing in a collapse exterior |

***What keeps `prop:causal-alignment` BUILT IN PART.***
- It lives in a single chart.
- `hcl` and `hint` are stated, not derived.
- `hHM` (`𝓗⁺ ⊆ M`) is P1's own setting.
- The two-sided Cauchy theorem `cr_causal_alignment_gh` has no non-vacuity witness. Campaign 79's model proves only the
  future form, but the future-form theorem covers P1's clause under a weaker hypothesis.

## Expectations, scored

1. **Accumulation and finite-slice clauses BUILT via 72 and 78–79: holds conditionally.** The Lean is those campaigns.
   But the stated hypotheses and the chart make them BUILT IN PART by the rule.
2. **Tangency BUILT IN PART until 80: holds.**
3. **`cor:densities` NOT BEGUN: fails.** Its slice clauses are built in campaign 60. That campaign does not use `Θ`'s
   regularity, so the vacuity finding does not touch it.
4. **A metric-singularity statement BUILT IN PART on the 4D or angular reduction: fails as worded.** The probes are
   `n`-dimensional, and the gaps are other ones (flat frame, global chart, no witness).

## The proposal: campaign 81

***The rule's answer.*** The headline, "the event horizon occurs on no finite exterior slice", rests most directly on
`prop:causal-alignment`'s finite-slice and accumulation clauses. Among their gaps, the cheapest to close are `hint` and
`hcl`:
- `hint` (`int J⁻(J) ⊆ I⁻(J)`) follows from a short future step along `T`, then campaign 60's push-up. That needs a
  locally Lipschitz `g`, which P1's smooth `g` gives.
- `hcl` follows from a past step and push-up, with `J ⊆ M` or `J ∖ M ⊆ closure D` stated.

***Two more pieces.***
- Add the past Cauchy property to campaign 79's model, so `cr_cauchy_iff` makes `cr_causal_alignment_gh`
  non-vacuous.
- Restate the headline with `hcl` and `hint` removed.

***Cost and result.*** A few hundred lines. After it, the headline's hypotheses are P1's own, and the single chart is
the only gap left.

***The chart lift is not chosen yet.*** It means joining the manifold layer of campaigns 66 and 68 to campaigns 60–79,
which is far costlier. It is named as the gap that comes after.

***Tangency is not on the headline's path.*** P1's "Consequently" follows from the finite-slice clause.

***One reading point for 69.*** The EF corollary places horizon events on "the null boundary of the observer's causal
past". That agrees with `prop:causal-alignment` (no single past cone meets `𝓗⁺`) only if it means the past of the
whole worldline.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
