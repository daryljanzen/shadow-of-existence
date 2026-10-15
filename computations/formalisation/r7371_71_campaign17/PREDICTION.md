# `r7371+71.4` — PRE-REGISTRATION: campaign 17, row 7's half, the receipt's count claims. ⌗ `70` lines (band 35–160), ⛔ stop `200`. ⌗ p `0.7`. ⌗ With the price list for the last three halves, cheapest first: 7, 108, 77

*Orders: `FOR_71.md` §`r7371` ③ (the remaining halves, cheapest first by my own price list, a band before each).
Campaign 16 (row 35) landed at `r7371+71.3`. ***No pre-opening reading:*** all three receipts were opened before
this registration and are priced from what they compute, which is said here.*

## ⓪ The price list (what each receipt COMPUTES, not what its prose says)

| row | receipt | what it computes | price | order |
|---|---|---|---|---|
| 7 | `L174_general_matter_dynamics/I3_…_shear_count_is_the_gap.py` | a trace-free symmetric `3 × 3` `σ` has FIVE free components (it counts symbols); `ρ = R₃/2 + θ²/3 − σ²/2` with `∂ρ/∂σ² < 0` | linear algebra, `70` lines | ***1st*** |
| 108 | `P17_…/P17_the_cut_is_planar_only_at_M_zero.py` (4)–(5) | inside ONE ansatz, `X = (F sinh κt, F cosh κt, G, r n)`: the two determinations of `G′²` disagree, the defect has an overall factor `M`, and no constant `κ` closes it at `M ≠ 0` | rational-function algebra plus "vanishes on an interval ⇒ `M = 0`", `≈ 150` lines | 2nd |
| 77 | `P11_dynamics_paper/P11_twoKV.py` | `∂_z`, `∂_t` fail the Killing equation when `ψ_z`, `ψ_t ≠ 0`; the `x ↔ y` rotation fails when `g_xx ≠ g_yy` | the rotation is NOT a constant field, so THE connection must act on a linear field; `≈ 200` lines | 3rd |

- ***Neither 108 nor 77 is real-end on what its receipt computes.*** 108's receipt proves nonexistence INSIDE its
  ansatz, not over all hypersurfaces. 77's receipt tests three named candidates, not the whole Killing algebra.
  Each would be built as what it computes, and the row's text would say what is not claimed.
- Each gets its own band before it is built.

## ① The piece (row 7)

- ***The count:*** the trace-free symmetric `3 × 3` real matrices form a subspace of dimension ***`5`***
  (`Module.finrank`). The receipt counts symbols; this is the statement the count stands for.
- ***The sign:*** with the Hamiltonian constraint `R₃ + K² − K_ijK^ij = 2ρ` and `K = (θ/3)g + σ`, `σ` trace-free,
  `ρ = R₃/2 + θ²/3 − (σ·σ)/2`, using `adm_trace_split` (`r7351+71.3`). Then `ρ` strictly decreases in `σ·σ` at
  fixed `R₃` and `θ`.
- ***What it will not build:*** the receipt's other count, that a polarized Gowdy leaf's shear is ONE function.
  The receipt pins that from the paper's text and computes nothing for it. It is said in the row and not built.

***Failable:*** BUILT, BUILT IN PART (count or sign), or REPORTED. p `0.7` under the stop.
- ***Risk:*** the `finrank` statement needs an explicit basis, or a linear equivalence with `Fin 5 → ℝ`, of the
  trace-free symmetric submodule. Mathlib may have no ready lemma for it.

***Census if BUILT:*** row 7 moves `DONE (chartable half)` → `DONE`. Then DONE `54` and halves `2` (77, 108).

## ② Compile

Priced under `1` minute: no curvature contraction.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
