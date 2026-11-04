# `r7669+71.2` — RESULT: campaign 94 ②, **`lem:killing` stage 1 BUILT**: the local lemma on a derived `LocalKillingChart`, with a null-translation witness that has distinct coincident points. 4b–4d stay BUILT IN PART, and the gap is now one flow box. Stage 2 is not attempted. ⌗ `2496` lines in one probe (`436` new, band 250–1000). ⌗ p `0.75` came true

*Against `PREDICTION.md` (`r7669+71.1`). 71 re-ran `lake env lean probes/KillingLocal.lean`. It exits 0 with no errors
and no warnings. All `125` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `96` are copied and
`29` are new. The forbidden-token grep is clean. The probe copies campaigns 66–68's `LieDerivManifold.lean`, and
imports only Mathlib.*

## `kl_lemma_killing_local`

***Hypotheses*** — exactly `ld_manifold_killingChart_lieDeriv`'s, plus `g_p(X p, X p) = 0`:
- `N` is a C² manifold;
- `X` is a C¹ vector field with `X p ≠ 0`;
- `g` is differentiable in the chart near `p`;
- `L_X g = 0` near `p`.

***Conclusion.*** A `LocalKillingChart K` at `p` and an `ε > 0` such that, for `|a|, |b| < ε`,
`kl_MetricallyCoincidentLocal g K a b` holds. Writing `ψ = (extChartAt p)⁻¹ ∘ K.Φ`, that means:
- **the orbit:** `ψ(t, 0)` has velocity `X`;
- **(a):** `g(X, X) = 0` at every `ψ(t, 0)`, and `ds² = |X|² dλ² = 0` on the segment;
- **(b), and (b) between:** every transverse invariant, which is any function of the adapted chart's components on
  the slice, is equal at `a`, at `b`, and at any `t` between them;
- **the separations:** `Δx = 0`, and `Δτ = 0` in `kh`'s adapted-frame sense;
- **distinctness:** `a ≠ b` implies `ψ(a, 0) ≠ ψ(b, 0)`.

***Supporting lemmas.***
- `kl_lambda_indep_N`: the components depend only on the transverse coordinate.
- `kl_normSq_orbit_const` and `kl_null_along_orbit`: the local versions of 4b.
- `kl_lemma_killing_chart`: the same conclusion for any given chart.

***Why the registered stop was not hit.*** Within one box, `LocalKillingChart.metric_eq` already makes the components
`λ`-independent. So (b) is component equality in the adapted chart, and no flow map on `N` is needed.

## The witness, `kl_witness`

***The setting.*** `ℝ × ℝ` with `g = 2 dλ dx` (`v₁w₂ + v₂w₁`) and `X ≡ (1, 0)`, a null translation.
- `kl_w_lorentzian`: `g` is symmetric and non-degenerate, with a timelike and a spacelike vector.
- `kl_w_lieDeriv`: `L_X g = 0`, through the registered `lieDeriv`.

***What it shows.***
- Every hypothesis is discharged.
- `ψ(t, 0) = (t, 0)` is proved by integrating the velocity (`kl_model_orbit`).
- The points `ψ(0, 0)` and `ψ(ε/2, 0)` are metrically coincident **and distinct**.

## What remains

***4b–4d: BUILT IN PART.***
- Stage 2, gluing flow boxes along a whole generator, is not attempted.
- `Δx` and `Δτ` are in `kh`'s algebraic adapted-frame sense.
- The witness's chart `K` is existential. Only `ψ` on the orbit is explicit.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
