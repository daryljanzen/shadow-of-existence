# `r7697+71.2` — RESULT: campaign 110, **7c BUILT, all five stages. The Kretschmann scalar of Schwarzschild in Kruskal coordinates is `48M²/r⁶`, proved by hand from the coordinate Riemann tensor. It diverges as `UV → 1`, and that locus lies in the black-hole region's closure and in no finite exterior slice's closure.** ⌗ `15093` lines in one probe (`999` new, under the registered `2200`). ⌗ p `0.2` for the whole came true. The expected stop at ③ was not hit, and no fallback was used

*Against `PREDICTION.md` (`r7697+71.1`). 71 re-ran `lake env lean probes/Kretschmann.lean`. It exits 0 with no errors
and no warnings. All `482` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `420` inherited and
`62` new. The forbidden-token grep is clean, the probe imports only Mathlib, and `check_no_sorry.py` reads ALL 29
THEOREMS COMPILE. The probe copies campaign 107's `NullGeodesic.lean`. A container restart interrupted the build after
④, and the agent resumed it.*

## ① The locus and the slices — BUILT

- **The sets:** `Σ = {UV = 1}`. The black-hole region is `kr_BH = W ∖ J⁻(O)`, and `kr_BH_eq` gives `kr_BH = {U ≥ 0}`.
- **`kr_locus_BH`:** `Σ ∩ {V > 0}` lies in the closure of the black-hole region, and `U > 0` on it.
- **`kr_slice_far`:** for every `Θ` and `τ`, `Σ` misses the closure of the slice.
- **`kr_r_to_zero`:** `r → 0⁺` as `UV → 1⁻`, and conversely.

## ② Curvature in coordinates — BUILT

- **The definitions are the standard ones.** For `g : ℝⁿ → Matrix`:
  - `kr_Γ^a_{bc} = ½ g^{ad}(∂_b g_{dc} + ∂_c g_{db} − ∂_d g_{bc})`;
  - `kr_Riem^a_{bcd} = ∂_cΓ^a_{db} − ∂_dΓ^a_{cb} + ΓΓ − ΓΓ`;
  - `kr_K = R_{abcd}R^{abcd}`.
- **Sanity checks:**
  - `kr_K_const`: a constant metric has `K = 0`.
  - `kr_K_sphere`: the round 2-sphere of radius `ρ` has `K = 4/ρ⁴`.

## ③ The warped product — BUILT, with no fallback

- **The metric:** `g = −F dU dV + R²(dθ² + sin²θ dφ²)`.
- **The computation:** the inverse, all `64` Christoffel symbols and all `256` Riemann components (`40` of them non-zero)
  are computed one by one.
- **`kr_warped`:** `K = k₂² + 8 Hess(R)²/R² + 4(1 − |∇R|²)²/R⁴`, where:
  - `k₂ = 4(F F_UV − F_U F_V)/F³`;
  - `|∇R|² = −(4/F) R_U R_V`;
  - `Hess(R)² = (8/F²)((R_UU − (F_U/F) R_U)(R_VV − (F_V/F) R_V) + R_UV²)`.

## ④ The Schwarzschild value — BUILT

**`kr_schwarzschild`:** with `F = (32M³/r)e^{−r/2M}` and `R = r(UV)`, **`K = 48M²/r⁶`** on all of `{UV < 1}`, and so on
`W`.

## ⑤ Blow-up, and 7c — BUILT

- **`kr_blowup`:** `K → +∞` as `UV → 1⁻`.
- **`kr_cor_densities_c`:**
  - `K = 48M²/r⁶` on `W`;
  - `K → ∞` toward `Σ`;
  - every point of `Σ` in `W`'s closure is approached from `W`, with `K → ∞` there, and lies in the black-hole region's
    closure, with `U > 0`;
  - `Σ` misses the closure of every finite exterior slice.

## Limits

- **The curvature is computed on the coordinate chart `(U, V, θ, φ)`.** It is not tied to the manifold `seW` or to
  campaign 107's `ng_Γ`.
- **The sphere factor is added to the metric by hand.** It is not a product manifold.
- `K` is evaluated where `sin θ ≠ 0`.
- **"The curvature singularity" is read as the locus where the Kretschmann invariant diverges.** That is standard.
  `Σ` is not a set of points of the spacetime.

## Marks

- **7c → BUILT.**
- `cor:densities` is now whole apart from 7e, which is interpretive.
- The inventory is now **31 / 1 / 2**.
- **Left in part:** 6b-ii, which waits by ruling.
- **Not begun:** 3c and 7e, both interpretive.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
