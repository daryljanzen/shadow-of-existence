# `r7655+71.2` — RESULT: campaign 87, route (b)'s assembly, **BUILT**. P1's headline, the accumulation clause of `prop:causal-alignment`, now holds in Lean on **any Mathlib manifold** whose metric is C¹ in charts (`mh_causal_alignment_gh_N`). It is witnessed end to end, with the two-sided Cauchy hypothesis campaign 85 deferred now discharged. Neither registered stop was hit. The flat-cylinder stretch is REPORTED. ⌗ `4535` lines in one probe (about `385` new, against the registered `1200`, so the estimate was badly over-priced, because campaigns 84–86 had already built the pieces). ⌗ p: headline `0.45`, witness `0.5`: both came true; the stretch `0.15` was not attempted

*Against `PREDICTION.md` (`r7655+71.1`). 71 re-ran `lake env lean probes/ManifoldHeadline.lean`. It exits 0 with no
errors. All `22` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`. The forbidden-token grep is
clean. Campaigns 84–86 are copied in, about 4150 lines, with about 400 lines of unused end-consumers trimmed.*

## The assembly — all BUILT

1. **Temporal increase.** `mh_temporalD_chr`: `Θ` strictly increases along `Chr_N` into `D`. It goes through `DspN`,
   which is open by `mk_isOpen_D`, and through `mh_tstep_DspN`.
2. **`hint` and `hcl` on `N`.** `mh_hint` and `mh_hcl`, by campaign 86's short steps and push-up.
3. **Properness.** `mh_blowup` and `mh_sublevelProper`, by `mk_curve_inext_D`, then `me_futCauchy_of_cauchy_N` at
   `U = D J`, then the openness of `I⁺(r)`. This was the registered second-likeliest stop.
4. **The slice lower limit.** `mh_slice_lower_limit`, from the curve's tail.
5. **The upper limit and Kuratowski.** `mh_slice_upper_limit` and `mh_slice_kuratowski`. This was the registered
   expected stop, and it was not hit: campaign 81's argument uses no vector-space structure, only `I⁻(Oσ)` open,
   `D ⊆ J⁻(J)`, and step 1.
6. **`mh_causal_alignment_gh_N`.**

***The witness.***
- `NModel.mh_witness_hypotheses` discharges every hypothesis on the two-chart `Pt`, including
  `IsCauchyTemporalOn (D J) Θ`. That hypothesis is transported from campaign 81's two-sided model through `Pt`'s
  covering chart.
- `mh_witness_headline` gives properness and `KLi = KLs = 𝓗⁺ = {U = 0}`, a non-empty set, for `Θ₀∘φ` and `Θf∘φ`.
- **The registered limit stands.** One chart covers all of `Pt`. The flat cylinder, which no single chart covers, is
  REPORTED: it needs a new charted space and a Cauchy proof on `N` with no global chart to transport through.

## The headline set against P1, clause by clause

`theorem mh_causal_alignment_gh_N (hL : S.LocallyOneChart) [T2Space N] (hOD : S.IpastSet (range O) = S.D J) (hmono : ∀ s t, s < t → S.Chr (O s) (O t)) (hJM : J ⊆ S.M) (hHM : S.H J ⊆ S.M) (hΘ : S.IsCauchyTemporalOn (S.D J) Θ) (hadapt : ∀ τ, Θ (O τ) = τ + c) : S.SublevelProper J Θ ∧ KLi (S.slice J Θ) = S.H J ∧ KLs (S.slice J Θ) = S.H J`

| P1's `prop:causal-alignment` | in the Lean | status |
|---|---|---|
| `(M, g)` a spacetime, `g` smooth, time-oriented | `S : MSpacetime E N` on a Mathlib manifold `N`, with a time-orientation field `T`; `LocallyOneChart` (`g` C¹ and `T` continuous in charts); `T2Space N` | **weaker than P1**: smooth implies C¹; spacetimes are Hausdorff |
| `D = I⁻(𝒥⁺)`, globally hyperbolic, with `Θ` a smooth Cauchy temporal function of `D` | `D = I⁻(J)` for a set `J ⊆ M`; `IsCauchyTemporalOn (D J) Θ` (C¹ on `D`, increasing on causal vectors, every inextendible causal curve of `D` meets each level once) | matches. P1 takes `Θ` Cauchy temporal as its premise, and so does the Lean |
| `O` future-complete in `D` with `I⁻(O) = D` | `hmono` (`O` chronological, parametrised over all of `ℝ`) and `hOD : I⁻(range O) = D` | matches |
| `Θ` adapted to `O`: `Θ(O(τ)) = τ + const` | `hadapt` | matches |
| `𝓗⁺ = ∂J⁻(𝒥⁺)` | `H = frontier_N J⁻(J)`, with `hJM : J ⊆ M` and `hHM : 𝓗⁺ ⊆ M` | **see below** |
| **the slices accumulate on `𝓗⁺`** | `KLi(S_τ) = KLs(S_τ) = 𝓗⁺`, plus properness (`SublevelProper`) | **BUILT on any such manifold** |
| each finite slice lies in `D` | `slice J Θ τ ⊆ D J` by definition | BUILT (definitional) |
| the past cones `∂J⁻(O(τ))` converge to `𝓗⁺` | campaign 72's `hc_kuratowski` | BUILT **in one chart only**, not lifted to `N` |
| tangency, under the stated rate condition | campaign 80, frame-free and in the Kruskal plane | BUILT **pointwise in a vector space**, not stated on `N` |

***The one point of reading, `J` and `𝒥⁺`.***
- P1's `𝒥⁺` sits on a conformal boundary, outside `M`, while the Lean's `J` must lie in `M`. The way P1 itself
  supplies a `J` inside `M` is `I⁻(O) = D`: take `J` = the worldline, as the witness does.
- Then the Lean's `𝓗⁺` is the frontier of `J⁻(O)`. Identifying that with P1's `∂J⁻(𝒥⁺)`, given `I⁻(O) = I⁻(𝒥⁺)`, is
  the standard step. **It is not formalised.**

***In plain words, for 69.*** On any smooth, Hausdorff spacetime manifold, take a region `D` that is the chronological
past of an observer's worldline and carries an adapted Cauchy time function. Then that time function's slices
accumulate exactly on the boundary of `D`'s causal past, in both Kuratowski limits, and the time function is proper.
This is proved in Lean from those hypotheses alone. Three things are not on the manifold yet:
- the identification of that boundary with `∂J⁻(𝒥⁺)`;
- the cone-convergence clause, which is built in one chart;
- the tangency clause, which is built in a vector space.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
