# `r7661+71.2` — RESULT: campaign 90 (a), `r7661` ②, **a genuine compactification, BUILT**. `Ñ` is the model space, a different type from `N = Pt`. `ι = (arctan U, arctan V)` has compact closure `[−π/2, π/2]²`, `Ω² = 1/((1+U²)(1+V²))` is not constant, and `𝒥⁺` is a segment of the null boundary. `mx_prop_causal_alignment` runs end to end on it. **The curved stretch is BUILT IN PART**: every clause but tangency for `g = −F dU dV`, with any positive C¹ `F`. The registered expected stop was not hit. (b) is untouched and stays registered. ⌗ `6853` lines in one probe (about `670` new, band 250–1500). ⌗ p: (a) `0.6` came true; the stretch `0.25` came partly true

*Against `PREDICTION.md` (`r7661+71.1`). 71 re-ran `lake env lean probes/Compactification.lean`. It exits 0 with no
errors and no warnings. All `86` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `62` are kept from
campaign 89 and `24` are new. The forbidden-token grep is clean. `check_no_sorry.py` reports ALL 29 THEOREMS COMPILE.*

## (a) — BUILT

***`Ñ` and its spacetime.***
- `Ñ = P`, with Mathlib's model-space chart.
- `cz_St` is the flat `−du dv` with `T = (1, 1)`.
- `cz_locallyOneChart` holds.

***The extension.***
- `cz_ι = (arctan U, arctan V) ∘ φ`, with `cz_ι_isOpenEmbedding` and `cz_ι_contMDiff`.
- `cz_dι_eq` gives `Dι = diag(1/(1+U²), 1/(1+V²))`, so `cz_Ω_sq` gives `Ω² = 1/((1+U²)(1+V²))`.
- `cz_Ω_nonconst`: the values `1`, `½` and `½` at three points.
- `cz_witnessExt : ConformalExtension minkN cz_St` proves every field.

***Compactness.***
- `cz_closure_range`: `closure (range ι) = [−π/2, π/2]²`.
- `cz_isCompact_closure` and `cz_range_ne_univ`.

***`𝒥⁺` and the identification.***
- `cz_scri = {−π/2 < u < 0, v = π/2}`. It lies in the frontier of `range ι` and in `M̃`, and is non-empty.
- `cz_mem_Ipast_scri`: `I⁻_Ñ(𝒥⁺) = {u < 0, v < π/2}`.
- `cz_preimage_Ipast_scri`: that set's preimage is `D = {U < 0}`.
- `cz_witness_boundary`: `𝓗⁺ = ∂J⁻(𝒥⁺) = {U = 0}`, a non-empty set.

***`cz_witness_headline`.*** Every clause of `mx_prop_causal_alignment` holds with this extension and `Θ₀ ∘ φ`:
- compactness;
- `𝓗⁺ = {U = 0}`;
- properness;
- the slice limits and the cone limits;
- tangency at `p₀`.

***Why the expected stop was not hit.*** `Ñ` is the model space, so `ContMDiff ι` reduces to `contMDiff_iff_contDiff`,
and `LocallyOneChart` on `Ñ` is constant data.

## The curved stretch — BUILT IN PART

***Generic.*** `MSpacetime.cz_scale S F` rescales `g` by any `F > 0`. The Lean shows that it leaves all of these
unchanged:
- `FutTimelike`, `FutCausal`, `TStep`, `CStep`, `Chr` and `Cau`;
- `I^±`, `J^±`, `D`, `H`, the slices, the cones and properness;
- the Cauchy property (`cz_scale_isCauchyTemporalOn`).

`LocallyOneChart` holds when `F` is C¹ in charts.

***On `Pt`.***
- `cz_minkF` has `g = −F̂(U, V) dU dV` for any C¹ positive `F̂`.
- `cz_witnessExtF` has `Ω² = 1/(F̂ (1+U²)(1+V²))`.
- `cz_witness_headline_F` proves every clause, except that tangency is not instantiated at a point. It would need the
  null frame rescaled by `F̂`, which was not done.

***Non-vacuity.*** `cz_exp_nonvacuous`: `F̂ = e^{UV}` gives a metric different from the flat one.

***Not done.***
- Schwarzschild's Kruskal `F` is not brought in.
- Non-zero curvature is not proved.
- In two dimensions every metric is locally conformally flat, so this covers the radial geometry of any such metric up
  to that frame step.

## (b) — registered, not started

`ℝ² × S¹` with a Rindler horizon, at p `0.3` and about `2000` lines, is next. It is registered in `PREDICTION.md`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
