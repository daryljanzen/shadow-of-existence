# `r7663+71.3` — RESULT: campaign 91, all three pieces **BUILT**, and no registered stop was hit. ① no past light cone meets `𝓗⁺` (`RESULT_1.md`); ② a four-dimensional witness carrying every conclusion and tangency; ③ tangency on the curved `−F dU dV` at every horizon point, with an instance where the limit differs from the flat one. ⌗ ① `187`, ② about `730`, ③ `391` new lines, all inside their bands. ⌗ p `0.8`, `0.6`, `0.75`: all came true

*Against `PREDICTION.md` (`r7663+71.1`). 71 re-ran each probe. Each exits 0 with no errors and no warnings, and every
`#print axioms` line reads `[propext, Classical.choice, Quot.sound]`:
- `ConeDisjoint.lean`: `70` prints;
- `FourDWitness.lean`: `71` prints;
- `CurvedTangency.lean`: `95` prints.

The forbidden-token grep is clean, and `check_no_sorry.py` reports ALL 29 THEOREMS COMPILE.*

## ① — see `RESULT_1.md`

`cd_cone_disjoint` and `cd_prop_causal_alignment`, the eighth conjunct, need no new hypothesis. The clause rests on the
Cauchy property.

## ② The four-dimensional witness — BUILT

***The space.***
- `N = E = (ℝ × ℝ) × (ℝ × ℝ)` is the model space, with its single chart (`fd_chart_univ`). `finrank E = 4`.
- `g = −dU dV + dy² + dz²` and `T = ∂_U + ∂_V`.
- The probe copies (b)'s general theory and drops (b)'s `Cylinder` witness.

***The Cauchy property on a non-compact fibre*** — the registered stop, not hit.
- `fd_mono`: a functional that is non-negative on the causal cone is non-decreasing along causal curves.
- `fd_lip`: `|Δy|, |Δz| ≤ Δ(U+V)/2` along causal curves.
- `fd_converge`: each coordinate is Cauchy in `ℝ`.
- `hl_cauchy_Θ₀` then applies through the projection.

***`fd_witness_headline`.***
- **Hypotheses discharged:** `finrank 4`, `LocallyOneChart`, `hOD`, `hmono`, `hJM`, and `IsCauchyTemporalOn (D J) Θ` with
  `Θ = −log(−U) + V`.
- **Facts established:** `D = {U < 0}`, and `𝓗⁺ = {U = 0}`, a null hyperplane that is non-empty and lies in `M`.
- **Conclusions:** adaptation, properness, `KLi = KLs = 𝓗⁺` for the slices and for the cones, and every slice
  non-empty.

***`fd_witness_tangency q`, at every horizon point.***
- The frame is `ℓ = ∂_V` and `n = 2∂_U`, and `W = {ℓ, n}^⊥` is exactly the transverse plane, where `g = dy² + dz²`.
- The rate is `→ 0`, and the limit is `½ dU = −g(ℓ, ·)`.
- `fd_tangency_origin` instantiates it at the origin.

***Not exercised, as registered.*** `∂J⁻(𝒥⁺)` in 4D, because `(arctan U, arctan V, y, z)` is not conformal for the
product metric. The witness also has a single chart; the multi-chart witness is (b).

## ③ Tangency on `−F̂ dU dV` — BUILT

***The frame.***
- `ℓ = ∂_V` and `n = ct_nN = (2/F̂)∂_U`, so `g_F(ℓ, n) = −1`.
- `ct_Tq q` is the constant coordinate change into `q`'s preferred chart.

***`ct_witness_tangency_F q`, at every horizon point, for any C¹ positive `F̂`.***
- `𝓝[D] q` is non-trivial.
- The frame hypotheses hold eventually.
- The rate `(−U/2) F̂ → 0` (`ct_ratio`).
- `‖n^q‖` is bounded (`ct_bound`). This was the registered stop, and it was not hit: continuity and positivity of `F̂`
  suffice.
- The limit is `−g_q(ℓ, ·)` in `q`'s chart, which is `(F̂(q)/2) dU` in `φ`'s chart.

***`ct_witness_headline_F`.*** It is campaign 90's `cz_witness_headline_F` with the tangency clause instantiated at every
point of `∂J⁻(𝒥⁺)`. This removes its last caveat.

***Non-vacuity.***
- `ct_exp`, with `F̂ = e^{UV}`: the rescaled frame differs from the flat one. The limit at `p₀` is still `½ dU`, because
  `F̂ = 1` on `U = 0`.
- **`ct_expV_differs`**, with `F̂ = e^V`: at `ψ(0, 1) ∈ 𝓗⁺` the limit is `(e/2) dU`, which is not `½ dU`. The curved
  limit is genuinely different from the flat one.

## What the remark can now lose

1. "No cone meets `𝓗⁺`" becomes a conclusion, with the note that it rests on the Cauchy property.
2. "A four-dimensional witness" can go, with the note that the 4D witness does not exercise the `𝒥⁺` identification
   and has one chart.
3. The caveat on the curved witness's tangency can go.

The unbounded-stretch clause remains the one clause not in the formal statement.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
