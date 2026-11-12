# `r7743+71.1` — PRE-REGISTRATION: campaign 132, **P15's last rows: 2, 3a, 3b (the arithmetic) and 5 (the flat slice), closing P15 at 11 of 11**. ⌗ `520` new lines (band 450–650), p `0.85`, of which `424` are a verbatim copy. **Expected stop:** none serious; the risk is real-number `norm_num` on powers like `(5.45×10⁻²)⁻⁶`

*Registered before any Lean. A trial build of the copied sections, standalone on Mathlib, compiled with no errors
before this registration.*
- **Everything goes into `probes/Cosmology.lean`,** P15's citable file.
- **The copy.** `StaticEinstein.lean`'s sections `KrCurvature` (91 lines, with `KrTrig` nested) and `LfLeaves` (333
  lines) are copied verbatim into namespace `ShadowProbe.StaticEinsteinProbe`, with every name kept.

## Rows

| Row | Statement | Lines | p |
|---|---|---|---|
| 2 | `10¹¹² < 2×10⁻⁹ / 3×10⁻¹²² < 10¹¹³`: the stated vacuum power is about `10¹¹³` below `A_s` | 10–20 | 0.95 |
| 3a | `0 < M ≤ α/(3√3)` ⟹ `(ℓ_P/M)² ≥ 27(ℓ_P/α)²` | 15–30 | 0.95 |
| 3b | `10⁻¹¹³ < 9 × 2.6×10⁻¹²¹ × (5.45×10⁻²)⁻⁶ < 10⁻¹¹²`. Run backwards, `9 × 2.6×10⁻¹²¹ × ρ⁻⁶` reaches `2×10⁻⁹` for `ρ` between `3×10⁻¹⁹` and `3.5×10⁻¹⁹`. Also the tensor floor: `144π × 2.6×10⁻¹²¹ × (5.45×10⁻²)⁻⁶ < 10⁻¹¹⁰` | 30–60 | 0.85 |
| 5 | `cm_flat_slice`: `lf_g 1 id = diag(1, r², r² sin²θ)` (the induced metric `dr² + r²dΩ²`), and every `R_{abcd} = 0` at `r ≠ 0`, `sin θ ≠ 0`. This is `lf_curv` with `R = 1`, `S = id`, `S′ = 1`, `k = 0` | 30–60 | 0.9 |

**Non-vacuity:** row 5 at a concrete point; rows 2 and 3 are strict two-sided bounds.

**Cited, not formalised:**
- the inputs `Λℓ_P² ≈ 3×10⁻¹²²`, `ρ ≃ 5.45×10⁻²` and `ℓ_P/α`;
- the transfer law, eq. `transfer-law`.

**An open question, not a flag.** "Thirteen orders below what nucleosynthesis permits" (l.2486) depends on a lower
bound on `ρ` that P15 does not state. Against the paper's own `ρ ≃ 5.45×10⁻²`, the gap to `3×10⁻¹⁹` is 17 orders.
I will put this to 60.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
