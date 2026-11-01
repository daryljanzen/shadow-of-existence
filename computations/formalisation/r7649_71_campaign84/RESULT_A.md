# `r7649+71.2` — RESULT: campaign 84, route (c), **BUILT in full**. The headline holds on any Mathlib manifold whose spacetime region lies in one chart (`ch_causal_alignment_gh_N`), stated in the manifold's own terms and proved by transport to campaign 81's theorem. Neither registered stop was hit: the `TStep` chart transfer and the localisation of `𝓗⁺` are both BUILT. Non-vacuity is shown on a manifold whose chart, and whose chart derivative, are not the identity. ⌗ `3622` lines in one probe (about `1400` new, band 700–2200). ⌗ p: c1 `0.75`, c2 `0.4`, whole `0.35`: all came true

*Against `PREDICTION.md` (`r7649+71.1`). 71 re-ran `lake env lean probes/ChartHeadline.lean`. It exits 0 with no
errors. All `30` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`. The forbidden-token grep is
clean.*

## c1, the `V` side — BUILT

- **The fields.** `Spacetime`'s `cont_g` and `cont_T` are now `ContinuousOn … M`, and every `LocallyLipschitz g` is
  `LocallyLipschitzOn M g`.
- **The re-check.** The chain re-checks with continuity used only at points of `M`: `isOpen_timelikePairs`,
  `local_pushup`, `safe_uniform` and the past extension.
- **The model.** `Model.hl_model_headline` builds with its statement unchanged.
- **The localised headline.** `ch_causal_alignment_gh_loc` uses `𝓗⁺ ∩ W ⊆ M` for any `W`, and its conclusions are
  intersected with `W`. The proof uses `hHM` only at horizon points of `W`. `ch_causal_alignment_gh_univ` recovers the
  global form.

## c2, the manifold side — BUILT

***Intrinsic definitions on `N`.***
- `MSpacetime`, with sections `g` and `T`.
- `TStep` and `CStep`: `ContMDiff 1` curves `ℝ → N` with future-timelike or causal `mfderiv` velocity.
- `Chr`, `Cau`, `D`, `𝓗⁺ = frontier_N J⁻(J)`, slices, `SublevelProper`, and `KLi`/`KLs` in any topological space.
- `IsTemporalOn` (`ContMDiffOn` plus `mfderiv`) and `IsCauchyTemporalOn`.

***Chart-defined, and only this.*** `OneChart S p₀`: `M ⊆ (chartAt p₀).source`, `hRep g p₀` C¹ on `φ(M)`, and
`chartRep T p₀` continuous there.

***The transfer.***
- `ch_squash`, an arctan reparametrisation.
- `ch_tstep_iff`: `TStep_N x y ↔ TStep_V (φx) (φy)`, through `mfderiv_comp` and `mfderiv_eq_fderiv`.
- Then the rest transfers: `ch_chr_iff`, `ch_cau_iff`, `D`, `J⁻(J)`, closure, frontier and `KLi`/`KLs` through the
  chart, `ch_mem_H_iff` (`𝓗⁺` inside the chart), and the Cauchy property both ways (`ch_isCauchy_NV`/`_VN`).

***`ch_causal_alignment_gh_N`.***
- Hypotheses: `OneChart`, `hOD`, `hmono`, `J ⊆ M`, `𝓗⁺ ⊆ M`, `IsCauchyTemporalOn (D J) Θ` and `hadapt`.
- Conclusion: properness, and `KLi(S_τ) = KLs(S_τ) = 𝓗⁺`.
- Everything is read in `N`. `LocallyLipschitz` has disappeared as a separate hypothesis, because it follows from
  `hRep g` being C¹ on the open `φ(M)`.

## Non-vacuity — BUILT, on a non-identity chart

- **The manifold.** `NModel.Pt` is a copy of `ℝ²` as its own type, with the atlas `{id, (t,x) ↦ (t−x, t+x)}`.
  - At `p₀ = (0,0)` the chart is the null-coordinate map. `ch_chart_ne_id` shows it is not the identity, and
    `ch_dchart_ne_id` shows its derivative is not the identity, so `hRep` and `chartRep` really change components.
- **The chart spacetime.** `ch_chartSp_eq` shows it is campaign 81's `mink`.
- **The hypotheses.** `ch_witness_hypotheses` discharges every hypothesis of `ch_causal_alignment_gh_N`.
- **The conclusion.** `ch_witness_headline` gives it for `Θ₀∘φ` and for `Θf∘φ`, with `𝓗⁺_N` non-empty and
  `x ∈ 𝓗⁺_N ↔ (φx).1 = 0`.

## What separates P1's headline from the Lean now

- **The one-chart hypothesis.** P1's exemplars, the Kruskal and Oppenheimer–Snyder exteriors, are open subsets of `ℝ⁴`
  and so satisfy it. That fact is not formalised; it needs Schwarzschild in 4D coordinates.
- **The fully general clause, "any asymptotically flat spacetime".** It needs route (b). Its first missing piece is the
  inextendible-curve extension on a multi-chart `N`, as campaign 84's scoping named.

**For 69: nothing in P1's statement needs to change.** One caution if P1 ever cites the formalisation for the general
clause: the Lean covers spacetimes whose region lies in one chart, which includes its exemplars, and not arbitrary
multi-chart manifolds.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
