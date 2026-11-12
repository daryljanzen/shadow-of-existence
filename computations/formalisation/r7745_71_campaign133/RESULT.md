# `r7745+71.2` — RESULT: campaign 133, **P9's reachable rows are BUILT: the Kantowski–Sachs Einstein tensor and its vacuum kernel (3a–c), and the pp-wave's Ricci (8a).** ⌗ `448` lines, a new file, inside the registered band of 400–850 (point `600`). `91` of them are the copied `KrCurvature`. ⌗ p `0.6` came true. The expected stop, the KS Christoffel table, fell on the first build, and no fallback was used

*Against `PREDICTION.md` (`r7745+71.1`). 71 ran `lake env lean probes/Range.lean`. It exits 0 with no errors and no
warnings. All `14` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`. The forbidden-token grep is
clean, the probe imports only Mathlib, and `check_no_sorry.py` reads ALL 29 THEOREMS COMPILE. The copied
`KrCurvature` section is byte-identical to `StaticEinstein.lean`'s.*

**The file** is `probes/Range.lean`, prefix `rn_`, and it is P9's citable file. `rn_Ric`, `rn_scal` and `rn_G` repeat
P8's definitions.

## Row 3, `prop:ksvac` — BUILT

- **3a:** for `−dτ² + X(τ)²dχ² + Y(τ)²dΩ²`, the Einstein tensor is computed from the coordinate Riemann tensor.
  - `rn_ks_Γ`: the Christoffel table.
  - `rn_ks_Ric_diag`: the Ricci diagonal.
  - `rn_ks_einstein`: P9 eq. `ksrho` and its partners exactly:
    - `−G^τ_τ = (Y′/Y)² + 1/Y² + 2X′Y′/(XY)`;
    - `G^χ_χ = −2Y″/Y − (Y′/Y)² − 1/Y²`;
    - `G^θ_θ = G^φ_φ = −Y″/Y − X″/X − X′Y′/(XY)`.
  - `rn_ks_Ric_offdiag` and `rn_ks_G_offdiag`: the off-diagonal components vanish.
- **3b, `rn_ks_sds_vacuum`:** the SdS interior is vacuum. If `Y′ = X`, `X′ = −f′(Y)/2`, `X″ = −f″(Y)X/2` and
  `X² = −f(Y)`, then all sixteen components of `G^μ_ν + Λδ^μ_ν` vanish.
  - `rn_ks_witness` is the explicit member `M = 0`, `Λ = 3`, `Y = cosh τ`, `X = sinh τ`.
- **3c, `rn_ks_nariai`:** the Nariai member `Y = 1/√Λ`, `X = e^{√Λτ}` is vacuum in all sixteen components.

## Row 8a, `prop:radiative`'s pp-wave — BUILT

- **`rn_pp_inv`:** the inverse of the non-diagonal `H du² − 2du dv + dx² + dy²`.
- **`rn_pp_Γ`:** the Christoffel table. It holds at every point, since the metric needs no division.
- **`rn_pp_Ric`:** `R_uu = −½(∂²_x H + ∂²_y H)`, and every other `R_μν = 0`.
- **`rn_pp_vacuum_iff`:** the wave is vacuum iff `H` is harmonic in `(x, y)`.
- **`rn_pp_witness`:** `H = x² − y²` is vacuum.
- **Not built (8b):** type N, with the Weyl tensor non-zero and `I = J = 0`.

## Marks (P9's inventory, `r7745_71_survey/SURVEY.md`)

- **Built (4):** 3a, 3b, 3c and 8a.
- **Not begun (5):** 4a–e, 5, 7a, 7b and 8b.
- **No formal core (7).**

**Next (campaign 134):** the cheap Kerr rows (4b, 4d, 4e) and the registered attempt at Kerr–de Sitter (4a). It is
priced at 1500–4000 lines, p 0.3, with the stop at `field_simp`/`ring` on the rational Ricci components.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
