# `r7725+71.2` — RESULT: campaign 123, **P8's vacuum kernel is BUILT: rows 1b, 1c, 1d, 1e and 2.** ⌗ `223` lines, a new standalone file, **below** the registered band of 250–650 (point `400`). ⌗ p `0.8` came true. The expected stop did not occur, and no fallback was used

*Against `PREDICTION.md` (`r7725+71.1`). 71 ran `lake env lean probes/OperatorKernel.lean`. It exits 0 with no
errors and no warnings. All `11` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`. The
forbidden-token grep is clean, the probe imports only Mathlib, and `check_no_sorry.py` reads ALL 29 THEOREMS COMPILE. It is a new file that copies no earlier probe,
with everything prefixed `ok_`.*

## Why the line count is low

**The expected stop, the preimage at the interval's ends, did not occur.** With `g` continuous on `ℝ`, Mathlib's
`intervalIntegral.integral_hasDerivAt_right` gives `(r · (1/r)∫_{r₁}^r g)′ = g(r)` at every `r > 0`, endpoints
included. The kernel and the general solution are both `IsOpen.exists_is_const_of_deriv_eq_zero`.

## `thm:kernel` (P8 l.206)

- **1b, `ok_vacuum_iff_ode`:** on an open interval in `(0, ∞)`, with `f` twice differentiable there, every
  component of `T` vanishes ⟺ `rf′ + f − 1 + Λr² = 0` there.
  - `T^t_t = T^r_r` is the ODE over `r²`.
  - `2r·T^θ_θ` is the ODE's derivative, which vanishes because the ODE holds on a neighbourhood.
- **1c:**
  - **`ok_general_solution`:** on an open interval in `(0, ∞)`, with `f` differentiable, `f` solves the ODE ⟺
    `f = 1 − 2M/r − Λr²/3` for a single `M`. The constant of integration is `−2M`, since `rf − r + Λr³/3` is
    constant.
  - **`ok_sds_solves`** (non-vacuity): every SdS profile solves it on all of `(0, ∞)`.
- **1d, the operator `Lf = (rf)′`:**
  - **`ok_L_bound`:** `|Lf| ≤ |f| + r₂|f′|` on `[r₁, r₂]`, so `L` is bounded `C¹ → C⁰`.
  - **`ok_kernel`:** on `(r₁, r₂)`, `Lf = 0 ⟺ f = c/r`.
  - **`ok_onto`:** `f = (1/r)∫_{r₁}^r g` has `Lf = g` at every `r > 0`, so on all of `[r₁, r₂]`.
  - **`ok_index_one`:** `1/r` is in the kernel, is non-zero, and spans it; and `L` is onto. One-dimensional kernel,
    zero cokernel: index 1.
  - "The index is the mass", and its stability along Fredholm paths, stay interpretive or cited.
- **1e, `ok_matter_onto`:** for every continuous `ρ`, `m(r) = ∫_{r₁}^r 4πs²ρ` gives a cut
  `f = 1 − 2m/r − Λr²/3` with `8πT^t_t = −8πρ` at every `r > 0`. Every density is realised.

## `prop:bend` (P8 l.237)

- **2, `ok_bend`:** with `f = 1 − 2m/r − Λr²/3` and `m` differentiable at `r ≠ 0`,
  `8πT^t_t = (rf′ + f − 1)/r² + Λ = −2m′/r²`. So `ρ = m′/4πr²`.

## Reading

**No flags.** `thm:kernel` is exact as stated: the ODE, its one-parameter solution set, and index 1 =
`dim ker − codim range = 1 − 0`.

## Marks (P8's inventory, `r7725_71_survey/SURVEY.md`)

- **Built (5):** 1b, 1c, 1d, 1e and 2.
- **Built in part (6):** 1a, 3a, 3b, 4b, 5b and 5c, all in the other engine.
- **Not begun (4):** 3c, 4a, 4c and 5a.
- **No formal core (1):** 5d.

**Next (campaign 124):** 1a and 3a–c, the static Einstein tensor `diag(−A, 1/F, r², r² sin²θ)` from the chain's
coordinate Riemann tensor. It copies the chain, because it needs `kr_Riem`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
