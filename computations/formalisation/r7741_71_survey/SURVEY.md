# Survey for the sixth paper to formalise, and its inventory: `r7741+71.1`

*A survey and inventory, not a campaign. It reads the corpus at `ec0f6925` (r7741) and the probes through campaign
130 (`Groupoid.lean`, `StaticEinstein.lean`). The criterion is 69's: **the largest formal core within reach of
Mathlib and the files already built.** Marks as before: **BUILT**, **BUILT IN PART** (gap named), **NOT BEGUN**.*

**Choice: P15, `corpus/CR_cosmology.tex`.** First campaign (131): rows 1, 4, 6 and 7. It is registered in
`r7741_71_campaign131/PREDICTION.md`.

## The candidates

Each candidate is listed with its rows: a statement is split where it makes more than one claim. **Core** counts
rows with a precise statement. **Reach** counts rows buildable with Mathlib and the files already built.

| P | file | cites | stmts | rows | core | reach | stops |
|---|---|---|---|---|---|---|---|
| **15** | `CR_cosmology` | 163 | 7 | **12** | **11** | **11** | Row 7's integrability of `1/f` at `r = 0`. Everything else is SdS calculus, P8's `lf_curv` and arithmetic |
| 9 | `range_paper` | 107 | 11 | 14 | 7 | 2–3 | `prop:kerr` (`R_{μν} = Λg_{μν}` for Kerr–dS, a non-diagonal `Fin 4` metric) and `thm:pd` (the Type-D "iff quartics"): the coordinate Riemann tensor of a non-diagonal metric, at a scale not yet attempted. `prop:typeI` and `prop:radiative` need the Weyl invariants `I` and `J`. Reachable: `prop:ksvac` (diagonal) and the pp-wave's Ricci |
| 13 | `boundary_paper` | 144 | 4 | 6 | 3 | 3 | `prop:boundary` (`su(3)` is not an isometry of the substrate) needs Lie-algebra embedding theory Mathlib lacks. The parity rows are algebra |
| 12 | `algebroid_paper` | 103 | 1 | 3 | 3 | 3 | None: the `so(5,1)` brackets are matrix algebra. But it is one statement |
| 11 | `dynamics_paper` | 70 | 3 | 4 | 2 | 1 | `prop:twoKV`'s "exactly two" needs the full Killing equation |
| 17 | `geometric_core_paper` | 133 | 2 | 2 | 2 | 1 | `prop:unique` is a classification Mathlib lacks |
| 7 | `CR_framework` | 263 | 20 | — | low | low | Unchanged: "ontological layers" are undefined |
| 14 | `matter_sector_paper` | 178 | 2 | 2 | 1 | 0 | Spinor zero-modes |
| 4, 6 | parallax, shadow | 90, 92 | 1, 2 | — | 0 | 0 | No formal core |
| 10, 16 | canonical time, cosmogenesis | 113, 112 | 0 | — | — | — | No stated results |

**Why P15.**
- **11 of its 12 rows are within reach,** more than any other paper.
- **They are SdS calculus:** the Nariai double root, the tortoise integrals and the comoving Hubble scale. The flat
  slice is P8's `lf_curv` with `k = 0`.
- **It is the second most cited companion** after P7.
- **The only real stop** is the finite tortoise length at the branch point, which needs `1/f` integrable at `r = 0`.
- **Why not P9:** its headline results are the hardest computations in the corpus.
- **No reading flags so far.** I checked P15's stated numbers:
  - `9 × 2.6×10⁻¹²¹ × (5.45×10⁻²)⁻⁶ = 8.9×10⁻¹¹³ ~ 10⁻¹¹²`;
  - `2×10⁻⁹ / 3×10⁻¹²² = 6.7×10¹¹² ~ 10¹¹³`;
  - run backwards, `ρ = 3.2×10⁻¹⁹`;
  - `0.4835² = 0.2338`.

---

# Inventory of P15 (`corpus/CR_cosmology.tex`)

The grep finds **7** statements, split into **12 rows**. `f(r) = 1 − 2M/r − r²/α²`, `Λ = 3/α²`, `G = c = 1`.

## 1. `prop:subhorizon` (l.299)
- **1a.** On the `E = 1` leg (`a = r`, `ṙ² = 2M/r + r²/α²`), `aH = ṙ → ∞` as `r → 0⁺`. **NOT BEGUN.** 30–60, p 0.9.
- **1b.** Hence `k/(aH) → 0` for every `k`. **NOT BEGUN.** 10–20, p 0.95.
- **Interpretive:** "the frozen adiabatic state is handed over".

## 2. `prop:amplitude` (l.2466)
- **2.** Arithmetic on the stated inputs: `A_s/(Λℓ_P²) = 2×10⁻⁹/3×10⁻¹²² ∈ (10¹¹², 10¹¹³)`, which is `~10¹¹³`. **NOT
  BEGUN.** 10–20, p 0.95.
- **Interpretive:** the vacuum-power estimate itself.

## 3. `prop:progenitor-amplitude` (l.2478)
- **3a.** `M ≤ α/(3√3)` ⟹ `(ℓ_P/M)² ≥ 27(ℓ_P/α)²`. **NOT BEGUN.** 15–30, p 0.95.
- **3b.** Arithmetic: `9 × 2.6×10⁻¹²¹ × ρ⁻⁶` at `ρ = 5.45×10⁻²` is `~10⁻¹¹²`, and `2×10⁻⁹` needs `ρ ~ 3×10⁻¹⁹`.
  **NOT BEGUN.** 20–40, p 0.9.
- **Cited:** the transfer law, eq. `transfer-law`.

## 4. `prop:throat` (l.2502)
- **4a.** At `ΛM² = 1/9` (`M = α/(3√3)`), `r_N = α/√3` has `f = f′ = 0` and `f″ = −2Λ`. The two positive roots
  merge, and the cubic is `−(r − r_N)²(r + 2r_N)/(α² r)`.
  - **Kit:** `sl_nariai` (`α = 1`). **BUILT IN PART.** 60–120, p 0.85.
- **4b.** The `S²`'s two-Ricci is `2/r_N² = 2Λ`, and the `dS₂` radius² is `−2/f″(r_N) = 1/Λ`: equal radii.
  **NOT BEGUN.** 20–40, p 0.9.

## 5. `prop:flat` (l.2556)
- **5.** `dr² + r²dΩ²` has vanishing Riemann tensor: `lf_curv` with `R = 1`, `S = id`, `k = 0`.
  - **Kit:** `lf_curv` (`StaticEinstein.lean`). **BUILT IN PART.** Copy plus 20–40, p 0.9.

## 6. `prop:transmission` (l.2675)
- **6a.** `p = 1`: for `f = 2κ(r − r_h)`, `r* = ln(r − r_h)/(2κ)` has `dr*/dr = 1/f`, and `r − r_h = e^{2κ r*}`.
  **NOT BEGUN.** 30–60, p 0.9.
- **6b.** `p = 2`: for `f = −Λ(r − r_N)²`, `r* = 1/(Λ(r − r_N))` has `dr*/dr = 1/f`, and `r − r_N = 1/(Λr*)`.
  `r*` diverges as a power, not a logarithm. **NOT BEGUN.** 30–60, p 0.9.

## 7. `prop:transmit` (l.2763)
- **7.** At the branch point `f ~ −2M/r`. `1/f = r/(r − 2M − r³/α²)` extends continuously to `r = 0` with value `0`,
  so `r* = ∫₀^ε dr/f` is finite. **NOT BEGUN.** 60–150, p 0.75. **Stop:** integrability at `0`.
- **Interpretive:** "scale-free transmitter", and the `a″/a` constants.

## Totals
- **12 rows**, 11 with a formal core.
- **Marks:** 0 BUILT; 2 BUILT IN PART (4a, 5); 10 NOT BEGUN.
- **Whole paper:** about 400–800 new lines, plus the `lf_` copy for row 5.

## Campaign order
- **131:** rows 1, 4, 6 and 7, in a new standalone probe.
- **132:** rows 2, 3 and 5 (the `lf_` copy), which would close P15.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
