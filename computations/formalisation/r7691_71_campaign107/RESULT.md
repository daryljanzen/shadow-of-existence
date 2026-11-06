# `r7691+71.2` — RESULT: campaign 107, **2iii BUILT on `N`: along any geodesic, `g(γ̇, γ̇)` is constant, so a geodesic segment null at one point is null along the whole segment. The witness is Schwarzschild's horizon generator in `∂J⁻(𝒥⁺)`, an affinely parametrised geodesic.** ⌗ `14094` lines in one probe (`426` new, band 200–900). ⌗ p `0.65` came true, all four parts on `W`, with no fallback. The expected stop (the chart identity for `g(γ̇, γ̇)`) was not hit

*Against `PREDICTION.md` (`r7691+71.1`). 71 re-ran `lake env lean probes/NullGeodesic.lean`. It exits 0 with no
errors and no warnings. All `420` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `401` inherited
and `19` new. The forbidden-token grep is clean, the probe imports only Mathlib, and `check_no_sorry.py` reads ALL 29
THEOREMS COMPILE. The probe copies campaign 106's `StationaryHorizon.lean`.*

## ① Geodesics on `N` — BUILT

- **`ng_kos`:** the Koszul form of a `C¹` bilinear-form field.
- **`ng_Γ`:** the Christoffel map.
  - `ng_Γ_exists`: it exists in finite dimension for a non-degenerate `g`.
  - `ng_Γ_unique`: it is unique.
  - `ng_geod_iff`: the Koszul form of the geodesic equation is equivalent to `c″ = −Γ(c′, c′)`.
- **`MSpacetime.IsGeodesicOn γ a b`:** about each `t ∈ [a, b]`, in the preferred chart at `γ t`, the chart curve is `C²`
  on an open interval and satisfies `g(c″, w) = −kos(c′, c′, w)` for every `w`.
  - The equation is stated in Koszul form, so `g` is never inverted.
  - The interval is open, so a segment on `[a, b]` is a geodesic slightly beyond its ends.

## ② Energy conservation — BUILT

- **`ng_energy_const`:** under `LocallyOneChart`, along `IsGeodesicOn`, `g(γ t)(γ̇, γ̇)` is constant on `[a, b]`.
- **The proof:**
  - In the chart, `(G(c)(c′, c′))′ = DG(c′)(c′, c′) + 2G(c″, c′) = 0`, by Koszul at `w = c′` (`ng_chart_energy_deriv`).
  - The intrinsic value equals the chart value, through `ld_h_eq_hRep` (`ng_energy_hasDerivAt`).
  - A function with zero derivative is constant.

## ③ 2iii — BUILT

**`ng_cor_threefold_iii`:** a geodesic on `[a, b]` that is null at one `t₀` is null at every `t ∈ [a, b]`. That is P1's
"`g(γ̇, γ̇) = 0` along the entire segment".

## ④ The witness — BUILT, on `W`

**`ng_witness`:** on Schwarzschild on `W`, take `γ(s) = (0, V₀ + s)`, `s ∈ [0, b]`. It satisfies:
- `𝓗⁺ = ∂J⁻(𝒥⁺)`, and `γ` lies in it;
- `IsGeodesicOn`, with `c″ = 0 = −Γ(c′, c′)` in every chart. The key step is `ng_FS_dV`: `∂_V F = 0` on `U = 0`, since
  `F` depends on `UV`;
- null throughout.

***Stated plainly:*** on this witness, nullness also follows directly, because `g(∂_V, ∂_V) = 0` in Kruskal form. The
witness's content is that the horizon generator is an affinely parametrised geodesic, so ②'s hypotheses are met
non-vacuously. ②'s content is general: it holds along any geodesic on `N`.

## Marks

- **2iii → BUILT.**
- `cor:threefold` is now whole apart from 2iv-b.
- The inventory is now **28 / 3 / 3**.
- **Left in part:** 2iv-b, 6b-ii and 7c.
- **Not begun:** 3c and 7e, which are interpretive, and 8ii-e, which is priced at 300–500 lines, p 0.65, by conformal
  invariance.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
