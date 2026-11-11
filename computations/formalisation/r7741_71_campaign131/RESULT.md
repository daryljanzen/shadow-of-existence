# `r7741+71.2` — RESULT: campaign 131, **P15's horizon rows are BUILT: 1a, 1b, 4a, 4b, 6a, 6b and 7.** ⌗ `240` lines, a new standalone file, **below** the registered band of 250–600 (point `380`). ⌗ p `0.7` came true. The expected stop, row 7's integrability, fell, and no fallback was used

*Against `PREDICTION.md` (`r7741+71.1`). 71 ran `lake env lean probes/Cosmology.lean`. It exits 0 with no errors and no
warnings. All `11` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`. The forbidden-token grep is
clean, the probe imports only Mathlib, and `check_no_sorry.py` reads ALL 29 THEOREMS COMPILE.*

**The file** is `probes/Cosmology.lean`, prefix `cm_`, and it is P15's citable file. `f(r) = 1 − 2M/r − r²/α²` is
`cm_f`. Its first two derivatives are `cm_f1` and `cm_f2`, with `cm_hasDeriv_f` and `cm_hasDeriv_f1`.

## Rows — BUILT

- **1a, `cm_aH_diverges`:** on the `E = 1` leg, `aH = ṙ = √(2M/r + r²/α²) → ∞` as `r → 0⁺`, for `M > 0`.
- **1b, `cm_horizon_exit`:** `k/(aH) → 0` for every `k`.
- **4a:**
  - `cm_throat`: at `M = α/(3√3)`, which is `ΛM² = 1/9`, the radius `r_N = α/√3` has `f = f′ = 0` and
    `f″ = −2Λ`.
  - `cm_throat_root`: `f = −(r − r_N)²(r + 2r_N)/(α² r)`, so `r_N` is the only positive root.
- **4b, `cm_throat_radii`:** `2/r_N² = 2Λ` and `−2/f″(r_N) = 1/Λ = r_N²`. Equal radii.
- **6a, `cm_tortoise_linear`:** for `f = 2κ(x − x_h)`, `r* = ln(x − x_h)/(2κ)` has `dr*/dx = 1/f`, with
  `x − x_h = e^{2κ r*}`, and `r* → −∞` logarithmically.
- **6b, `cm_tortoise_double`:** for `f = −Λ(x − x_N)²`, `r* = 1/(Λ(x − x_N))` has `dr*/dx = 1/f`, with
  `x − x_N = 1/(Λr*)`, and `r* → +∞` as a power.
- **7, `cm_tortoise_finite`:**
  - `1/f → 0` as `r → 0⁺`;
  - on `(0, ε]` with `ε ≤ M`, `|1/f| ≤ ε/M`;
  - `1/f` is `IntervalIntegrable` on `[0, ε]`, so the tortoise length at the branch point is finite.
  - The proof writes `1/f` as the continuous `r/(r − 2M − r³/α²)`, whose denominator is `≤ −M` there.
- **Non-vacuity, `cm_witness`:** the throat at `α = 3`, the exponential law at `κ = 1`, and the integrable tortoise
  at `M = 1`, `α = 3`, `ε = 1`.

**Why the line count is low.** Row 7 needed no horizon bound: `ε ≤ M` already keeps the denominator below `−M`.

**The survey's count is corrected.** P15 has 11 rows, all with a formal core, not 12 with 11 cores.
`r7741_71_survey/SURVEY.md` is amended to match.

## Marks (P15's inventory, `r7741_71_survey/SURVEY.md`)

- **Built (7):** 1a, 1b, 4a, 4b, 6a, 6b and 7.
- **Built in part (1):** 5, P8's `lf_curv`.
- **Not begun (3):** 2, 3a and 3b, the arithmetic rows.

**Next (campaign 132):** rows 2, 3 and 5, which would close P15.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
