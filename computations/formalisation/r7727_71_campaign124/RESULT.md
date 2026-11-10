# `r7727+71.2` — RESULT: campaign 124, **P8's static Einstein tensor is BUILT from the coordinate Riemann tensor: rows 1a and 3a–c. It delivers eq. `Ttt`, `Ttheta`, `rho-B` and `prho`, and the SdS vacuum from the metric itself.** ⌗ `361` lines added: `244` new (`es_`), `90` copied verbatim (`kr_`), and the header. That is **below** the registered band of 450–1000 (point `650`). ⌗ p `0.55` came true. The expected stop, the Christoffel table, fell on the first build, and no fallback was used

*Against `PREDICTION.md` (`r7727+71.1`). 71 ran `lake env lean probes/StaticEinstein.lean`. It exits 0 with no errors
and no warnings. All `21` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `11` inherited from
campaign 123 and `10` new. The forbidden-token grep is clean, the probe imports only Mathlib, and `check_no_sorry.py`
reads ALL 29 THEOREMS COMPILE.*

**The file.** `StaticEinstein.lean` is campaign 123's `OperatorKernel.lean`, plus campaign 110's `KrCurvature` and
`KrTrig` sections copied verbatim from `SlicingCurvature.lean`, plus `section EsStatic`. P8's names are in one file.

**The Einstein tensor**, from `kr_Riem`:
- Ricci `R_{bd} = Σ_a R^a_{bad}` (`es_Ric`);
- scalar `R = Σ g^{bd} R_{db}` (`es_scal`);
- mixed `G^b_c = Σ_d g^{bd} R_{dc} − ½δ^b_c R` (`es_G`).

## Row 1a — BUILT

- **`es_Γ`:** the 64-entry Christoffel table of `g = diag(−A(r), 1/F(r), r², r² sin²θ)`, at any point where
  `A, F, r, sin θ ≠ 0` and `F` is differentiable.
- **`es_Ric_diag`:** the Ricci diagonal, from `kr_Riem`:
  - `R_tt = FA″/2 − FA′²/4A + F′A′/4 + FA′/r`;
  - `R_rr = −A″/2A + A′²/4A² − A′F′/4AF − F′/rF`;
  - `R_θθ = 1 − F − rFA′/2A − rF′/2`;
  - `R_φφ = sin²θ · R_θθ`.
- **`es_einstein`:**
  - `G^t_t = (rF′ + F − 1)/r²`;
  - `G^r_r = (rFA′/A + F − 1)/r²`;
  - `G^θ_θ = G^φ_φ = FA″/2A − FA′²/4A² + F′A′/4A + FA′/2rA + F′/2r`.
- **`es_construction_gauge` (`A = F = f`):**
  - **eq. `Ttt`:** `G^t_t = G^r_r = (rf′ + f − 1)/r²`;
  - **eq. `Ttheta`:** `G^θ_θ = G^φ_φ = f″/2 + f′/r`.
  - With `+Λ`, these are P8's `8πT^t_t = 8πT^r_r` and `8πT^θ_θ = 8πT^φ_φ`.
- **The hypotheses** (`es_Hyp`), at the point:
  - `A, F, r, sin θ ≠ 0`;
  - `A` differentiable, and `F` differentiable on a neighbourhood;
  - `A′` differentiable, with derivative `A″`.

## Rows 3a–3c, `prop:lapse` — BUILT

- **`es_lapse`:**
  - **eq. `rho-B`:** `G^t_t` is the same for every lapse `A`.
  - **eq. `prho`:** `G^r_r − G^t_t = (F/r)(A′/A − F′/F)`, which equals `(F/r)(ln(A/F))′` where `A/F > 0`.
  - **The lock** `A = F` gives `G^r_r = G^t_t`, so `p_r + ρ = 0`.

## Non-vacuity, and the vacuum from the metric — BUILT

- **`es_sds_vacuum`:** SdS (`A = F = 1 − 2M/r − Λr²/3`), at any point with `r > 0`, `f ≠ 0` and `sin θ ≠ 0`, meets
  the hypotheses. There `G^μ_μ + Λ = 0` for all four diagonal components. That is the vacuum computed from the
  Riemann tensor, not assumed.
- **`es_sds_witness`:** a concrete point, `M = 1`, `Λ = 3/100`, `r = 4`, `θ = π/2`.

## Why the line count is low

The plan to name each Christoffel entry as a function of one variable made every `kr_pd` a single `deriv` with a
supplied value. The 64-entry table then closed by `simp` and `field_simp` on the first build.

## For the landing: what comes off "given the matter functional"

- **P8 eq. `Ttt` and eq. `Ttheta` are now theorems from the metric** (`es_construction_gauge`), where
  `ok_vacuum_iff_ode` (campaign 123) took them as input.
- **Eq. `rho-B` and eq. `prho`** (`prop:lapse`) are `es_lapse`.
- **Scope:** only the diagonal mixed components are proved, which is what eq. `Ttt`–`Ttheta` list. That the
  off-diagonal components vanish is not claimed.

## Marks (P8's inventory, `r7725_71_survey/SURVEY.md`)

- **Built (9):** 1a, 1b, 1c, 1d, 1e, 2, 3a, 3b and 3c.
- **Built in part (3):** 4b, 5b and 5c, in the other engine.
- **Not begun (3):** 4a, 4c and 5a.
- **No formal core (1):** 5d.

**Next (campaign 125):** 4a–c, the radial geodesics and their exact solutions.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
