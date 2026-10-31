# `r7643+71.1` — PRE-REGISTRATION: campaign 80, `r7643` ①. The sufficient condition for slice tangency, frame-free, as a pointwise inequality with a sequence corollary. Then the two slicings of `lem:alignment` checked against it in Schwarzschild's radial (Kruskal) plane, with what the setting lacks for 4D stated. ⌗ `800` new lines in one probe (band 300–3000 new), ⛔ stop `4000` total. ⌗ p: frame-free inequality and corollary `0.6`; stationary slicing in the Kruskal plane `0.45`; retarded slicing `0.3`; full 4D Schwarzschild `0.05` (expected REPORTED)

*Under `r7643` ①. A new probe, `probes/TangencyCondition.lean`. Its linear algebra is campaign 79's, generalised. Its
Kruskal part is new. No Lean was written before this registration.*

## ① Frame-free

***The setting.***
- `E` is a finite-dimensional real vector space with a symmetric bilinear `g`.
- `ℓ` and `n` are null, with `g(ℓ,n) = −1`.
- `W := {ℓ, n}^⊥` is assumed positive definite, which is what makes `g` Lorentzian.
- `ξ` is a covector positive on the closed future cone minus `0`.

***The statement*** (pointwise, no basis). For every `w ∈ E`,
`|ξ(w) − ξ(n)·(−g(ℓ,w))| ≤ ξ(ℓ)·|g(n,w)| + √(2 ξ(ℓ) ξ(n))·‖w_W‖_g`,
where `w_W = w + g(n,w)ℓ + g(ℓ,w)n`.

***The route.***
- Temporality gives `‖ξ|_W‖² ≤ 2ξ(ℓ)ξ(n)`. This is campaign 79's `st_null_frame_bound`, made basis-free by testing
  `ξ` on `αℓ + βn + e`.
- Expand `w` in the splitting `ℓ, n, W`.

***The corollary.*** Take sequences `ξ_m`, `ℓ_m → ℓ` and `n_m → n` (frames converging at a horizon point), with
`ξ_m(ℓ_m)` bounded and `ξ_m(n_m) → ∞`. Then `ξ_m/ξ_m(n_m) → −g(ℓ,·)` in operator norm. So `ker ξ_m → ℓ^⊥`, which is
tangency to the generator in direction.

***Non-vacuity.*** The hypotheses are instantiated by 2D Minkowski and by campaign 79's aligned `Θ₀`.

## ② The two slicings in Schwarzschild's Kruskal plane

***The setting.***
- `E = ℝ²` in Kruskal `(U, V)`, region I, with `g = −F(r) dU dV`.
- `F = (32M³/r) e^{−r/2M}`.
- `r` is defined by `(r/2M − 1) e^{r/2M} = −UV`. It is built as the inverse of a strictly increasing function, with
  its derivative from the inverse function theorem.
- `ℓ = ∂_V` and `n = (2/F)∂_U`, so `g(ℓ,n) = −1`.

***The slicings.***
- **Stationary** `t = 2M log(−V/U)`. Here `dt(ℓ) = 2M/V` is bounded near a horizon point `(0, V₀)`, `V₀ > 0`, and
  `dt(n) = (2/F)(2M/|U|) → ∞`. No `r` is needed beyond `F` being bounded.
- **Retarded** `Θ = a(u + ηr)` with `u = −4M log(−U)`. Here `dΘ(ℓ) = aη r_V` is bounded,
  `dΘ(n) = (2/F)·a(4M/|U| + η r_U) → ∞`, and `r_U, r_V` come from implicit differentiation.

***Conclusion.*** Both satisfy ①'s hypotheses at every horizon point, so both align.

***Non-vacuity.*** Both are temporal (`dΘ(ℓ), dΘ(n) > 0`) on a neighbourhood of `(0, V₀)` in region I.

## What the setting lacks for 4D (expected REPORTED)

- The causal chain lives in one chart, a normed space.
- 4D Schwarzschild needs the angular `S²`, which has no global chart. So the slicings are checked on the radial plane
  only.
- Lifting needs either the manifold setting of campaigns 66 and 68 joined to the causal chain, or a statement that the
  angular directions are `g`-orthogonal and `ξ`-null, which holds for spherically symmetric `Θ`. In that case ①'s `W`
  absorbs them.
- RESULT says which route, if either, was taken.

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED.

***Reachable negative.*** `r(U,V)`'s implicit derivative is the likely stop. If so, the retarded slicing is stated with
`r_U` and `r_V` as hypotheses (bounded near the horizon point), and RESULT names that gap.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
