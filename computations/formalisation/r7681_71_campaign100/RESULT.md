# `r7681+71.2` — RESULT: campaign 100, **`ConformalExtension` on `W` BUILT; `cd_prop_causal_alignment` instantiated on Schwarzschild as such, with `𝓗⁺ = ∂J⁻(𝒥⁺)` and `𝒥⁺` Schwarzschild's future null infinity.** ⌗ `9855` lines in one probe (`271` new, band 200–1000). ⌗ p `0.75` came true; ①②③ all BUILT. The expected stop (`Dι` on the `Opens` subtype) was not hit. The optional instantiation of the tangency clause at a point was not done

*Against `PREDICTION.md` (`r7681+71.1`). 71 re-ran `lake env lean probes/SchwarzschildConformal.lean`. It exits 0
with no errors and no warnings. All `195` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `181`
inherited and `14` new. The forbidden-token grep is clean, the probe imports only Mathlib, and `check_no_sorry.py`
reads ALL 29 THEOREMS COMPILE. The probe copies campaign 99's `SchwarzschildRetarded.lean`, and
`cd_prop_causal_alignment` is copied verbatim from `ConeDisjoint.lean`.*

## ① The extension — BUILT

- **`sx_ext (hM) : ConformalExtension (se_S hM) cz_St`**, with every field proved.
  - The map is `ι = cz_fB ∘ val`, `(U, V) ↦ (arctan U, arctan V)`, into flat `−du dv` on `ℝ²`.
  - `sx_ι_isOpenEmbedding`: the open inclusion of `W` composed with `cz_fB`'s open embedding.
  - `sx_ι_contMDiff` holds, via `contMDiff_subtype_val`.
- **The derivative.** `sx_dι_eq : mx_dι sx_ι x v = cz_DfB x.1 v`, which is `diag(1/(1+U²), 1/(1+V²))`. It comes from
  `mfderiv_comp` and campaign 98's `se_dchart`.
- **The conformal factor.** `sx_Ω_sq` gives `Ω² = 1/(F(r)(1+U²)(1+V²))`.
- **Time orientation.** `sx_dι_T`: `Dι(T)` is future timelike.

## ② `𝒥⁺` and `hI` — BUILT

- `𝒥⁺ = cz_scri = {(u, π/2) : −π/2 < u < 0}`. This is `V → ∞` at `U < 0`, which is `r → ∞`: Schwarzschild's future
  null infinity in the radial plane.
- **`sx_hI`:** `I⁻(O) = ι⁻¹ Ĩ⁻(𝒥⁺)`, both being region I.

## ③ The headline — BUILT

`sx_prop_causal_alignment hM hr₀` gives, for the static observer at `r₀ > 2M` and `Θ = √(1 − 2M/r₀) t`:
- **`S.H J = ∂J⁻(𝒥⁺)`** (P1's `𝓗⁺`), with `∂J⁻(𝒥⁺)` pulled back `= {U = 0, V > 0}` and `r = 2M` on it;
- properness, and `KLi = KLs = ∂J⁻(𝒥⁺)` for the slices and for the cones;
- the tangency clause, in its general form;
- `cone(τ) ∩ ∂J⁻(𝒥⁺) = ∅`.

This is `cd_prop_causal_alignment` itself, so **campaign 98's stated difference is removed**. `𝓗⁺` is now P1's
`∂J⁻(𝒥⁺)`, not a set identified by hand.

## Non-vacuity, `sx_nonvacuous`

- It takes `M = 1`, `r₀ = 4`.
- `(0, 1) ∈ ∂J⁻(𝒥⁺)`.
- `Ω` differs between `(0, 1)` and `(0, 2)`.
- `g` is not flat at `(0, 1)`.

## Limits, as registered

- **This is the radial plane.** In four dimensions `Ω² r²` would also have to stay finite at `𝒥⁺`, and that is not in
  the kit.
- **The target `S̃` is flat `ℝ²`,** not Penrose's compactified Schwarzschild.
- **The tangency clause is not instantiated at a point** in this probe. Campaign 98's `sa_stationary_aligns`, in
  `SchwarzschildAlign.lean`, discharges it at every horizon point on the same metric.

## Marks

- **8i on Schwarzschild is now BUILT with P1's own `𝓗⁺ = ∂J⁻(𝒥⁺)`,** by `cd_prop_causal_alignment` itself.
- For `rem:formalised`'s seventh family, "identified as a set" can become "identified as `∂J⁻(𝒥⁺)` through a conformal
  extension of the radial plane (`sx_prop_causal_alignment`)".

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
