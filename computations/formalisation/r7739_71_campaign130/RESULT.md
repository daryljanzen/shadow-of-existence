# `r7739+71.2` — RESULT: campaign 130, **P5's last four rows are BUILT by copy (2b, 7a, 9, 10). P5 is closed: 17 of 18 rows BUILT, and row 6 has no formal core.** ⌗ `+1528` lines, inside the registered band of 1450–1700 (point `1550`). About `1480` of them are the verbatim copy. ⌗ p `0.85` came true. There was no stop

*Against `PREDICTION.md` (`r7739+71.1`). 71 ran `lake env lean probes/Groupoid.lean`. It exits 0 with no errors and no
warnings. All `65` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `57` from campaigns
127–129, `7` for the copied names cited, and `1` new. The forbidden-token grep is clean, the probe imports only
Mathlib, and `check_no_sorry.py` reads ALL 29 THEOREMS COMPILE.*

**The copy.** `SlicingCurvature.lean`'s sections `KrCurvature`, `SlCubic`, `SlSky`, `SlHinge` and `SlCurv` are copied
into `Groupoid.lean` under namespace `ShadowProbe.SlicingCurvatureProbe`, with every name kept. Each of the five
sections is byte-identical to its source. One correction to the registration: it gave `KrCurvature` as 462 lines,
but that count included `KrTrig`, which is nested inside it.

## Rows — BUILT

- **2b, `sl_σ_sin`:** for `cos b ≥ 0`, `σ((2/√3) sin b) = (2/√3) sin(π/3 − b)`. This is the involution in the
  slicing parameter as the reflection of the sky angle.
- **7a, `sl_σ_fixed` and `sl_nariai`:** on the admitted range, `σ(r₀) = r₀ ⟺ r₀ = 1/√3`. There the cubic is
  `(r − a)²(r + 2a)`, so the two non-fixed roots collide.
- **9, `sl_flip`:** `θ = π/2 + iψ` has `dθ/dψ = i`, `i² = −1` and `sin(π/2 + iψ) = cosh ψ`. That is the signature flip.
- **10:**
  - `sl_curvature_static`: from the coordinate Riemann tensor, the static slicing surface has
    `K_G = 1 − (m/2)/r³`, with `α = 1` and `m = 2M`.
  - `sl_curvature_witness`: the non-vacuity witness.
  - **New, `gp_KG_diverges`:** `K_G → −∞` as `r → 0⁺` for `M > 0`.
- **Interpretive, not formalised:**
  - row 9's "`ξ² = id` as a swap of two descriptions";
  - row 10's "pivot", "artefact" and "identical through first order".

## Marks (P5's inventory, `r7733_71_survey/SURVEY.md`) — CLOSED

- **Built (17):** 1, 2a, 2b, 2c, 3, 4, 5, 7a, 7b, 8, 9, 10, 11a, 11b, 12a, 12b and 13.
- **No formal core (1):** 6.

**Five papers are now formalised:** P1, P2, P3, P5 and P8. **Next:** the sixth paper's survey, on 69's order.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
