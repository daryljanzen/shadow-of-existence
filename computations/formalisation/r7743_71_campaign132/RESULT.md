# `r7743+71.2` — RESULT: campaign 132, **P15's last rows are BUILT (2, 3a, 3b, 5). P15 is closed: 11 of 11 rows BUILT.** ⌗ `+502` lines, inside the registered band of 450–650 (point `520`). `424` of them are the verbatim copy. ⌗ p `0.85` came true. There was no stop

*Against `PREDICTION.md` (`r7743+71.1`). 71 ran `lake env lean probes/Cosmology.lean`. It exits 0 with no errors and no
warnings. All `17` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `11` from campaign 131,
`1` for the copied `lf_curv`, and `5` new. The forbidden-token grep is clean, the probe imports only Mathlib, and
`check_no_sorry.py` reads ALL 29 THEOREMS COMPILE.*

**The copy.** `StaticEinstein.lean`'s `KrCurvature` (with `KrTrig` nested) and `LfLeaves` are copied into
`Cosmology.lean` under namespace `ShadowProbe.StaticEinsteinProbe`, with every name kept. Both sections are
byte-identical to their source.

## Rows — BUILT

- **2, `cm_substrate_ratio`:** `10¹¹² < 2×10⁻⁹ / 3×10⁻¹²² < 10¹¹³`.
- **3a, `cm_mass_cap`:** `0 < M ≤ α/(3√3)` gives `(ℓ_P/M)² ≥ 27(ℓ_P/α)²`.
- **3b, `cm_progenitor_arith`:**
  - `10⁻¹¹³ < 9 × 2.6×10⁻¹²¹ × (5.45×10⁻²)⁻⁶ < 10⁻¹¹²`;
  - the observed `2×10⁻⁹` is reached only for `ρ` between `3×10⁻¹⁹` and `3.5×10⁻¹⁹`;
  - the tensor floor `144π × 2.6×10⁻¹²¹ × (5.45×10⁻²)⁻⁶ < 10⁻¹¹⁰` (paper: `≃ 5×10⁻¹¹¹`).
- **5, `cm_flat_slice`:** the slice's induced metric `dr² + r²dΩ²` is `lf_g 1 id`, and every `R_{abcd}` vanishes.
  This is the copied `lf_curv` with `k = 0`. `cm_flat_witness` gives the same at `r = 1`, `θ = π/2`.
- **Cited, not formalised:**
  - the inputs `Λℓ_P² ≈ 3×10⁻¹²²`, `ρ ≃ 5.45×10⁻²` and `ℓ_P/α`;
  - the transfer law.

## An open question for 60, not a flag

`prop:progenitor-amplitude`'s argument (l.2486) says `ρ ~ 3×10⁻¹⁹` is "thirteen orders below what nucleosynthesis on
the same leg permits".
- P15 does not state the nucleosynthesis bound on `ρ`.
- Against the paper's own `ρ ≃ 5.45×10⁻²`, the gap is 17 orders.
- If the permitted lower bound is about `10⁻⁶`, then 13 is right. I can't check which from P15.

## Marks (P15's inventory, `r7741_71_survey/SURVEY.md`) — CLOSED

- **Built (11):** 1a, 1b, 2, 3a, 3b, 4a, 4b, 5, 6a, 6b and 7.

**Six papers are formalised:** P1, P2, P3, P5, P8 and P15. **Next:** P9, per 69's order.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
