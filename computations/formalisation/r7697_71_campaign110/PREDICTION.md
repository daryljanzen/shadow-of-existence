# `r7697+71.1` — PRE-REGISTRATION: campaign 110, `r7697`, **7c staged: the curvature singularity of Schwarzschild lies in the black-hole region and on no finite exterior slice. The stages go from the locus (cheap and certain) to the Kretschmann scalar by hand (expensive).** ⌗ `2200` new lines for the whole (band 1200–4000), p `0.2` for the whole. **Each stage carries its own price and p,** so a stop leaves the stages before it BUILT

*Registered before any Lean. The new probe is `probes/Kretschmann.lean`, a copy of campaign 107's `NullGeodesic.lean`
(which has `se_` on `W`, `sx_` with `𝓗⁺ = ∂J⁻(𝒥⁺)`, the copied `sa_` derivatives of `r`, and `ng_Γ`). Everything new
is prefixed `kr_`. The stages are built in the order below, cheapest and most certain first.*

## Stage ① — the locus and the slices: `200` lines, p `0.85`

The singular locus is `Σ = {UV = 1}`, where `r → 0`. It is not in `W`.
- **`kr_locus_BH`:** `Σ` lies in the closure, in `P`, of the black-hole region `W ∖ J⁻(𝒥⁺) = {U ≥ 0} ∩ W`. On `Σ`,
  `U > 0`.
- **`kr_slice_far`:** no finite exterior slice has `Σ` in its closure. Slices lie in `D = {U < 0}`, whose closure has
  `UV ≤ 0 < 1`.
- **`kr_r_to_zero`:** `r → 0⁺` exactly as `UV → 1⁻` within `W`.

This is the locus reading of 7c. Taken alone it is interpretive, since nothing yet says `Σ` is singular. Stages ② to
⑤ supply that.

## Stage ② — curvature in coordinates: `450` lines, p `0.65`

- **Definitions:** for a `C²` metric field `G : ℝⁿ → (ℝⁿ →L ℝⁿ →L ℝ)`, define:
  - the Christoffel map, through `ng_kos` and the inverse of `G`;
  - the Riemann tensor `R(X, Y)Z`, from the derivative of the Christoffel map plus its products;
  - the Kretschmann scalar `K = R_{abcd} R^{abcd}`, contracted with `G⁻¹` in a basis.
- **Sanity checks, which are the non-vacuity of the definitions:**
  - a constant `G` has `K = 0`;
  - the round 2-sphere of radius `ρ` (in `θ, φ`) has Gaussian curvature `1/ρ²` and `K = 4/ρ⁴`.

## Stage ③ — Kretschmann of a warped product: `900` lines, p `0.3`. **This is the expected stop**

- **The metric:** `g = −F(U, V) dU dV + R(U, V)²(dθ² + sin²θ dφ²)` on `ℝ² × (0, π) × ℝ`.
- **`kr_warped`:** compute `K` in terms of `F`, `R` and their first and second derivatives. The classical result is
  `K = k₂² + 8|∇∇R|²/R² + 4(1 − |∇R|²)²/R⁴`, with `k₂` twice the Gauss curvature of `−F dU dV`.
- The `sin θ` dependence cancels from `K`. Proving that, component by component, is the bulk of the work.

## Stage ④ — the Schwarzschild value: `350` lines, p `0.6` given ③

**`kr_schwarzschild`:** with `F = (32M³/r) e^{−r/2M}` and `R = r(UV)`, the Kretschmann scalar is
**`K = 48M²/r⁶`** on `W` and on `{UV < 1}`. It uses the `r_U`, `r_V` identities from `hK`.

## Stage ⑤ — blow-up: `100` lines, p `0.9` given ④

**`kr_blowup`:** `K → +∞` as `UV → 1⁻`, combining `kr_r_to_zero` and `48M²/r⁶`. With ①, this gives **7c**: the locus
where the curvature invariant diverges lies in the black-hole region's closure, and in no finite exterior slice's
closure.

## Fallback at ③

**The 2D-plus-sphere reduction.** Compute only the 2D curvature `k₂` and the Hessian of `R` with stage ②'s machinery.
Use the classical warped-product formula for `K` as a stated identity. Its mark would be IN PART: the formula cited,
not proved. ④ and ⑤ would then rest on it, as they say.

*6b-ii waits, as ruled. Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
