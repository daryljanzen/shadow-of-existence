# `r7679+71.2` — RESULT: campaign 99, ④′. **The registered finding is machine-checked: the retarded slicing is not a Cauchy temporal function of eternal Schwarzschild's region I, for any `a, η > 0` (`sr_not_isCauchy`).** The η bound for temporality is BUILT and sharp. The future half is BUILT, and for every `η > 0`, which is more than registered. ⌗ `9584` lines in one probe (`550` new), inside the band of 500–2000. ⌗ p: ⓐ `0.65` came true; ⓑ `0.85` came true; ⓒ `0.5` came true; the stretch (`Θ → −∞` at past null infinity) was not attempted

*Against `PREDICTION.md` (`r7679+71.1`). 71 re-ran `lake env lean probes/SchwarzschildRetarded.lean`. It exits 0 with
no errors and no warnings. All `181` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `149`
inherited and `32` new. The forbidden-token grep is clean, the probe imports only Mathlib, and `check_no_sorry.py`
reads ALL 29 THEOREMS COMPILE. The probe copies campaign 98's `SchwarzschildEF.lean`, plus ten `sa_` lemmas from
`SchwarzschildAlign.lean` (`u`, the derivative of `r`, and `k`).*

## The setting

- The spacetime is campaign 98's `se_S` on `W = {V > 0, UV < 1}`, for a static observer at `r₀ > 2M`.
- `D` is region I, `{U < 0}` in `W` (`sr_D_eq`).
- `sr_Θ M a η x = a(−4M log(−U) + η r)`.

## ⓑ The refutation — BUILT

- **`sr_not_cauchy`:** for all `a, η > 0`, there is a `c : InextCausalCurveIn D` with `c.γ t = (−1, eᵗ)` along which
  `Θ_ret` never takes the value `0`.
- **`sr_not_isCauchy`:** so `¬ IsCauchyTemporalOn D Θ_ret`.
- The witness works for any `U₀ < 0`: along it, `Θ_ret > −4Ma log(−U₀)`.
- Its past end tends to `(U₀, 0)`, which is on the white-hole horizon and outside `W`.
- **The cause is the white-hole horizon.** Retarded time stays finite on it, while the stationary `t → −∞` there.

## ⓐ Temporality and the η bound — BUILT, sharp

- **`sr_dU_pos_iff`:** on `D`, `dΘ(∂_U) > 0 ⇔ η(r − 2M) < 2r`. Equivalently `ηf < 2`, P1's sign condition for
  `a²η(fη − 2) < 0`.
- **`sr_temporal`:** `Θ_ret` is temporal on `D` for `0 < η ≤ 2`.
- **`sr_not_temporal`:** for `η > 2`, at `r = 2Mη/(η − 2)`, the future causal vector `∂_U` has `dΘ(∂_U) = 0`, so
  `Θ_ret` is not temporal on `D`.
- The key identity is `k = e^{r/2M}((2 − η)(r/2M − 1) + 2)`.

## ⓒ The future half — BUILT, for every `η > 0`

- **`sr_future_diverges`:** `Θ_ret → +∞` along every causal curve inextendible in `D`.
- `U` and `V` are monotone along the curve. Bounded limits would land in `D`.
- So either `U → 0⁻`, where `−log(−U) → ∞`, or `V → ∞` with `U ≤ L < 0`, where `r → ∞`.
- `η ≤ 2` is not used.
- **This is the half the proof of `prop:causal-alignment` uses at `𝓗⁺`** (l.307: "Θ would grow without bound along
  it"). So the retarded slicing has it on eternal Schwarzschild, and only the past half fails.

## Non-vacuity, `sr_nonvacuous`

- It takes `M = 1`, `r₀ = 4`, `a = 1`.
- At `η = 1`: the witness curve `(−1, eᵗ)` misses `0` and has `Θ → ∞`. `Θ_ret` is not Cauchy, and it is temporal.
- At `η = 3`: there is a point of `D` with `r = 6` where `dΘ(∂_U) ≤ 0`.

## Not done

The stretch, `Θ_ret → −∞` along curves going to past null infinity for `η < 2`, was not attempted.

## Marks

- **The retarded half of 8ii-b → REFUTED on eternal Schwarzschild, machine-checked.**
- It holds on P1's own reading only for a collapse exterior (l.382), which is not in the kit.
- **For P1 l.382, a proposed replacement for its last clause:**
  - *Current:* "the same for the retarded slicing is not formalised".
  - *Proposed:* "on the eternal exterior the retarded slicing is temporal exactly for ηf < 2 and grows without bound to
    the future, but it is not Cauchy there, its levels being bounded below along curves that end on the white-hole
    horizon (`sr_temporal`, `sr_future_diverges`, `sr_not_isCauchy`); its Cauchy property belongs to the collapse
    exterior and is not formalised."

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
