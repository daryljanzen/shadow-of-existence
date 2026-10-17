# `r7443+71.11` — PRE-REGISTRATION: campaign 33, step 4's cheapest five library-gap rows: 23 (cited), 24, 82, 84, 46. ⌗ `300` lines (band 160–600), ⛔ stop `900`. ⌗ p `0.65`

*Under `r7443` ②, step 4, in the easiest-first order of `r7443_71_pricing/PRICING.md` (`r7443+71.10`). The five
receipts were read there for what they compute. No Lean was written before this registration.*

## ① The pieces: `probes/LibGap5.lean`

- ***Row 23*** (`L818_po6_running_layer/S1`). It is the same receipt row 19's campaign 12 formalised. Its five
  computed items are `probes/RunningLayer.lean`'s `frw_invariants`, `tv_identity`, `ledger_general`, `ledger_layer`
  and `ledger_ds_point`. ***Cited, not rebuilt.*** Only its paper-text check is left, and that is a pin, not
  mathematics.
- ***Row 24*** (`L819…/S1`):
  - `b4_rewrite`: with `Ric² = ½W − ½GB + ⅓R²`, `b₄ = (7/40)W + (149/360)GB + (1/8)R²`;
  - `trace_relation`: `4ΛR − R·E_tr − R² = 0` at `E_tr = −R + 4Λ`;
  - `shear_onset`: `12σ²(H − 2σ)²`, the Weyl² `row1_shear` (`BianchiI.lean`) proves on the receipt's family, is `0` at
    `σ = 0`, has `σ¹` coefficient `0`, and has `σ²` coefficient `12H² ≠ 0` for `H ≠ 0`. `row1_shear` is cited.
- ***Row 82*** (`P13_the_compact_face_is_odd_dimensional`). With `R(n) = n(n−1)/a²` and the spectrum
  `λ(n,k) = (n/2 + k)/a`, which is a definition in the receipt, imported and labelled so here:
  - Friedrich saturation `λ_min² = nR/(4(n−1))` at `n = 4, 5`;
  - `λ_min(5) = 5/(2a) > 0`, with no `k ≥ 0` giving zero;
  - `R(5)/4 = 5/a²`.
- ***Row 84*** (`P13_the_one_scale_forbids_the_isometry_route`):
  - `α = √(3/Λ)` gives `R = 20Λ/3` and `λ_min = (5/2)/α`;
  - the decimal bounds `m_min < 10⁻³⁰ eV` and `m_e/m_min > 10³⁰` as exact rational inequalities, with `√0.7`
    bracketed.
- ***Row 46*** (`P07_the_double_root_removes_the_first_law`):
  - the photon sphere is the unique stationary point `3M` of `f/r²`, with no `α`;
  - Nariai `3M_N = r_N` with `f = f′ = 0` there, and `λ² = 0` there;
  - the area and entropy algebra (`16πM² = 4πα²` only at `M = α/2 ≠ M_N`, the ratio `1/3`, and the entropy ratios
    `3/8` and `1/8`).

***Caveats, registered.***
- ***The imported data stay imported***, as the receipts take them:
  - the `b₄` coefficients (rows 23 and 24);
  - the Dirac spectrum on spheres and the Friedrich bound (82 and 84);
  - the area formula `4πr²` and `S = A/4` (46);
  - the physical constants (84).

  None is derived. Each is named in the row as belonging to its library, not to the row, as at rows 59 and 67.
- Paper-text checks are pins, not mathematics, and are not formalised.

***Failable:*** BUILT, BUILT IN PART (per row), or REPORTED. p `0.65`.
- ***Risk:*** row 84's decimal bounds.

***Census if BUILT:*** rows 23, 24, 82, 84 and 46 → `DONE`, each with `decl` filled in the same push. That gives
library gap `17 → 12`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
