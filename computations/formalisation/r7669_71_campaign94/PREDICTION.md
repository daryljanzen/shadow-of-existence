# `r7669+71.1` — PRE-REGISTRATION: campaign 94, `r7669`, in 69's order. ① `thm:metric-singularity` 1b and `cor:threefold` 2iv-a on ruling 2: the along-the-connection theorem with `Δτ = ∫ N |dt(γ′)|`, its `N > 0` companion, and a Rindler-horizon witness with `p ≠ q`. ② `lem:killing` stage 1: the local lemma on a `LocalKillingChart`, with a Minkowski witness. ⌗ ① `300` new lines (band 120–800), p `0.85`. ② `400` new lines (band 250–1000), p `0.75`. **Expected stops:** ① going from `Δx = 0` to `h(γ′, γ′) = 0` pointwise, which needs continuity of the integrand; ② the `LocalKillingChart` orbit and flow-isometry transport, which the global-chart proof gets for free

*Under `r7669`. Two new probes, built in parallel: `probes/AlongConnection.lean` for ①, from campaign 92's
`HorizonStretch.lean`, and `probes/KillingLocal.lean` for ②, from campaigns 66–68's `LieDerivManifold.lean` with
campaign 59/82's `KillingHorizon` and `KillingWitness` material. No Lean was written before this registration.*

## ① The along-the-connection form, on 69's ruling

***The splitting along `γ`.*** Take `γ : ℝ → N`, C¹ on `[0, 1]`, with velocity `γ′ = S.vel γ`. Along it, take:
- `h s`, a bilinear form;
- `n s ≥ 0`, the lapse, which may vanish;
- `dt s`, a linear form;

such that `S.gE (γ s) = h s − (n s)² · dt s ⊗ dt s` and `h s (γ′ s, γ′ s) ≥ 0`. Then:
- `Δx := ∫₀¹ √(h(γ′, γ′))`;
- `Δτ := ∫₀¹ n |dt(γ′)|`.

***`ac_metric_singularity_along`.***
- **Hypotheses:**
  - (a) `g(γ′, γ′) = 0` on `[0, 1]`;
  - (b) `Δx = 0`;
  - the integrands are continuous on `[0, 1]`.
- **Conclusion:** `Δτ = 0`, and `n s · dt s (γ′ s) = 0` on `[0, 1]`.
- **Route.** (b) and continuity with non-negativity give `h(γ′, γ′) = 0` pointwise (the expected stop). Then (a) gives
  `n² dt(γ′)² = 0`.

***`ac_lapse_pos_forces_point`, the companion.*** If `n > 0` on `[0, 1]`, and each `h s` is positive definite on
`ker dt s`, then (a) and (b) force `γ′ = 0`, so `γ 1 = γ 0` and `p = q`.
- This is why the flat-frame `ms_metric_singularity_along` has no witness with `p ≠ q`. It is P1's point that metric
  coincidence of distinct events needs the adapted lapse to degenerate.

***`ac_witness`, on the Rindler horizon.***
- **The space:** 2D Minkowski in null coordinates, `g = −dU dV`.
- **The curve:** `γ(s) = (0, e^s)` on `U = 0`, so `p = (0, 1) ≠ q = (0, e)`.
- **The boost field:** `χ = V∂_V − U∂_U`.
  - It is Killing, by a constant linear flow.
  - `g(χ, χ) = UV`, so `|χ| = √(−UV)` in region I and `0` on `U = 0`.
  - Along `γ`, `χ = γ′`, which is null and non-zero.
- **The splitting:** `dt = dV/V`, which is `dλ` with `λ = log V`; the lapse `n = |χ| = 0`; and `h = g`.
- **The result:** (a) and (b) hold, `Δτ = 0`, and `p ≠ q`.

***Setting.*** 69's ruling is pointwise along `γ`, so ① is stated for an `MSpacetime` on any manifold, and witnessed
on the model space.

## ② `lem:killing` stage 1

***`kl_lemma_killing_local`.***
- **Hypotheses:** `ld_manifold_killingChart_lieDeriv`'s (`L_X g = 0` on `N`, with `X(p) ≠ 0`), together with
  `g_p(X p, X p) = 0`.
- **Conclusion:** there are a `LocalKillingChart` at `p` and an `ε > 0` such that, for `|a|, |b| < ε`, the points
  `ψ(a, 0)` and `ψ(b, 0)` on `X`'s orbit are:
  - metrically coincident in the local form of `MetricallyCoincident`: `ds² = |X|² dλ² = 0` along the orbit, and the
    transverse invariants are equal by the local flow isometry;
  - distinct when `a ≠ b`.

***Witness.*** Minkowski with a constant null `X`: `g = 2 dλ dx`, a null translation, on the model space, with
explicit distinct orbit points.

***What stays open.*** 4b–4d stay BUILT IN PART, with the gap narrowed to "one flow box". Gluing flow boxes along a
whole generator is stage 2 and is not attempted.

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED. Non-vacuity is mandatory.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
