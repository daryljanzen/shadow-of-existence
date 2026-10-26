# `r7613+71.5` — RESULT: campaign 57, `r7613` ①, BUILT, all four pieces. ⌗ `164` lines in one probe (registered `300`, band 120–700). ⌗ both registered p came true (`0.9`, `0.7`); the reachable negative did not occur

*Against `PREDICTION.md` (`r7613+71.1`). 71 re-ran `lake env lean probes/MetricSingularity.lean`. It exits 0 with
no errors. All `8` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`. A grep for `sorry`,
`admit`, `axiom`, `native_decide`, `unsafe`, `implemented_by` and `elab` is empty.*

## `thm:metric-singularity`
- **`ms_metric_singularity_scalar`, `ms_metric_singularity_vec`.** From `Δs² = Δx² − Δτ²`, `Δs² = 0` and `Δx = 0`
  it follows that `Δτ = 0`. The vector form uses `Δx : EuclideanSpace ℝ (Fin n)` with `‖Δx‖²`.
- **`ms_metric_singularity_along`, the remark's form.** For `τ`, `x` with derivatives at every point of `[0,1]`,
  with `‖x′‖² − τ′² = 0` and (b) `x′ = 0` on the whole segment:
  - `τ′ = 0` on `[0,1]`;
  - `τ(1) = τ(0)`;
  - `x(1) = x(0)`.

## `cor:threefold`
- **(iii): `ms_threefold_iii`, `ms_threefold_iii_of_b`.** `g(γ̇, γ̇) = 0` at every parameter. It is also derived
  from (b) and `τ′ = 0` alone.
- **(iv), second half: `ms_threefold_iv_noninvariance`.** Take a `C^k` temporal `τ` (`k ≥ 1`) with
  `∂_t τ ≥ c > 0`, points `p ≠ q`, and `ε > 0`. Then there is a `C^∞` function `φ` with:
  - `|φ| ≤ ε`;
  - support inside the ball `B(q, d(p,q)/2)`, which does not contain `p`;
  - `τ + φ` still `C^k` and still temporal, with `∂_t(τ + φ) ≥ c/2`;
  - `(τ+φ)(q) − (τ+φ)(p) ≠ τ(q) − τ(p)`.

  The construction is `φ = δ·b`, with `b` a `ContDiffBump`. Its derivative bound comes from compact support.

***Scope.***
- "Temporal" is a uniform bound in one global chart on `ℝ^{n+1}`. The theorem is not stated on a manifold.
- The relation `Δs² = Δx² − Δτ²` is a hypothesis, as the paper states it. The adapted frame is not constructed.
- No census row moves.
