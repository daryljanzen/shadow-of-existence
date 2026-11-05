# `r7681+71.1` — PRE-REGISTRATION: campaign 100, `r7681`. **A `ConformalExtension` on `W`, so that `𝓗⁺ = ∂J⁻(𝒥⁺)` runs on Schwarzschild and `cd_prop_causal_alignment` is instantiated as such.** ⌗ `400` new lines (band 200–1000), p `0.75` for the whole. **Expected stop:** the derivative of `ι` on the `Opens` subtype

*Registered before any Lean. The new probe is `probes/SchwarzschildConformal.lean`, a copy of campaign 99's
`SchwarzschildRetarded.lean`, which already carries every needed piece. These are campaign 89's `ConformalExtension`
and `mx_prop_causal_alignment`; campaign 90's flat target `cz_St`, arctan map `cz_fB`, `cz_witnessExtF` and
`cz_mem_Ipast_scri`; campaign 98's `se_S`, `se_dchart` and `se_headline`; and campaign 91's `cd_cone_disjoint`.
`cd_prop_causal_alignment` (about 30 lines, `ConeDisjoint.lean`) is copied in. Everything new is prefixed `sx_`.*

## ① The extension — `200` lines, p `0.8`

- **The target is `S̃ = cz_St`:** `Ñ = P`, `g̃ = −du dv`, `M̃ = P`, `T̃ = (1, 1)`.
- **The map is `ι = cz_fB ∘ val : W → P`, `(U, V) ↦ (arctan U, arctan V)`.**
  - It is an open embedding, as the composition of an open inclusion and a homeomorphism onto `(−π/2, π/2)²`.
  - It is `C¹`.
  - `Dι = diag(1/(1+U²), 1/(1+V²))`, through `se_dchart`.
- **The conformal factor:** with `g = −F(r) dU dV`, `Ω² = 1/(F (1+U²)(1+V²))`. This is `cz_witnessExtF`'s factor with
  `F̂ = FS M`.
- **`sx_ext : ConformalExtension (se_S hM) cz_St`**, with every field proved.
- **Expected stop:** `mx_dι` for `ι` on the `Opens` subtype. It is `mfderiv` through the subtype's chart, where
  campaign 98's `se_dchart` gives the identity.

## ② `𝒥⁺` and `hI` — `100` lines, p `0.8`

- `𝒥⁺ = cz_scri = {(u, π/2) : −π/2 < u < 0}`, in the frontier of `ι(W)`.
- **It is Schwarzschild's own future null infinity.** `v = π/2` is `V → ∞`, and at fixed `U < 0` that is `−UV → ∞`,
  so `r → ∞`.
- `Ĩ⁻(𝒥⁺) = {u < 0, v < π/2}`, by `cz_mem_Ipast_scri`.
- Its preimage in `W` is `{U < 0} ∩ W`, which is region I, which is `D`. That is `hI`.
- `hHM` holds because `M = univ`.

## ③ The headline — `100` lines, p `0.75`

- **`sx_prop_causal_alignment`:** `cd_prop_causal_alignment` for `sx_ext`, with the static observer and
  `Θ = √(1 − 2M/r₀) t` (`se_headline`'s Cauchy property, `c = 0`). It gives:
  - `S.H J = ∂J⁻(𝒥⁺)`, together with `∂J⁻(𝒥⁺)` pulled back `= {U = 0, V > 0}` (`r = 2M`);
  - properness;
  - `KLi = KLs = ∂J⁻(𝒥⁺)` for the slices and for the cones;
  - the tangency clause in its general form;
  - `cone(τ) ∩ ∂J⁻(𝒥⁺) = ∅`.
- **Non-vacuity, `sx_nonvacuous`:** `M = 1`, `r₀ = 4`. `∂J⁻(𝒥⁺)` is non-empty, `Ω` is not constant, and `g` is not
  flat.
- **Optional, p `0.5`:** the tangency clause instantiated at a horizon point, from campaign 98's `sa_stationary_aligns`
  read on `W`.

## Limits stated in advance

- **This is the radial plane.** In two dimensions every metric is conformally flat. In four dimensions the sphere's
  `Ω² r²` would also have to stay finite at `𝒥⁺`, and that is not in the kit.
- **The target `S̃` is flat `ℝ²`, not Penrose's compactified Schwarzschild.** `𝒥⁺` lies in `S̃`'s `M`, as the
  definition requires, and `∂J⁻(𝒥⁺)` is computed in `S̃`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
