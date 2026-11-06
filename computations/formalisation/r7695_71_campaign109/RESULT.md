# `r7695+71.2` — RESULT: campaign 109, **2iv-b BUILT on `N`: for a causal chain from `p` to `q` and any open `V ∋ q`, every value in an open interval about `τ(q) − τ(p)` is the separation of a temporal function equal to `τ` outside `V`. It is built from a local bump on `N`.** ⌗ `7902` lines in one probe (`500` new, band 400–1300). ⌗ p `0.4` came true, on `N`, with no fallback. The expected stop (uniform cone positivity) was not hit

*Against `PREDICTION.md` (`r7695+71.1`). 71 re-ran `lake env lean probes/ThreefoldLocal.lean`. It exits 0 with no
errors and no warnings. All `138` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `120` inherited
and `18` new. The forbidden-token grep is clean, the probe imports only Mathlib, and `check_no_sorry.py` reads ALL 29
THEOREMS COMPILE. The probe copies campaign 104's `ThreefoldDistinct.lean`.*

*Hypotheses beyond the kit:*
- *`[FiniteDimensional ℝ E]`, for a compact unit sphere and a `ContDiffBump`;*
- *`[T2Space N]`, so the pulled-back bump is `C¹` across the chart's edge;*
- *`LocallyOneChart`;*
- *`U ⊆ M`.*

## ① The bump on `N` — BUILT

- **`tl_cone_bound_vs`**, in a vector space: on a compact `K`, there is `c > 0` with `D(w) ≥ c‖w‖` for every future causal
  `w`. The closed unit cone equals the strict one, because a non-zero vector `g`-orthogonal to a timelike `T` is
  spacelike.
- **`tl_cone_pos`:** for `τ` temporal on `U`, there is `c > 0` with `dτ(v) ≥ c‖Dφ_q v‖` for every future causal `v`,
  over a compact set in the chart at `q`. This was the expected stop, and it went through.
- **`tl_bump`:** `ψ = ContDiffBump ∘ φ_q`, extended by `0`. It is `C¹` on `N`, with `ψ(q) = 1`, support in a chart ball
  inside the given open set, and `|dψ(v)| ≤ C‖Dφ_q v‖`.
- **`tl_bump_temporal`:** if `|δ| C < c`, then `τ + δψ` is temporal on `U`.

## ② 2iv-b — BUILT

- **`tl_iv_b`:** for `τ` temporal on `U`, `q ∈ U` and `V ∋ q` open with `p ∉ V`, there is `δ₀ > 0` such that for
  every `δ ∈ (−δ₀, δ₀)` some `τ′` satisfies:
  - `τ′` is temporal on `U`;
  - `τ′ = τ` off `V`;
  - `τ′(q) − τ′(p) = τ(q) − τ(p) + δ`.
- **`tl_cor_threefold_iv_b`:** the same for a causal chain from `p` to `q` and any open `V ∋ q`, with no `p ∉ V`
  hypothesis. `V` is shrunk to `V ∖ {p}`, since `p ≠ q`.
- **`tl_separation_interval`:** the separations of such `τ′` fill an open interval about `τ(q) − τ(p)`.

## ③ The witness — BUILT

- **`tl_minkN_temporal`:** `U + V` is temporal on `minkN`. This was not proved in campaign 104.
- **`tl_witness`:** `to_cor_1c`'s null pair is `Cau` and `¬ Chr`. For any `r > 0`, two temporal functions agree off the
  chart ball of radius `r` about `q` and give different separations. It is an instance of the theorem on `N`.

## The reading, as flagged

**The Lean proves that the separation is not fixed by the geometry.** Smooth local deformations alter it through an
open interval, keeping `τ` temporal. It does not prove "arbitrarily": a deformation local to `V` can move the separation
only by a bounded amount. The registration has the argument and a suggested wording.

## Marks

- **2iv-b → BUILT,** on the reading "not fixed by the geometry".
- `cor:threefold` is now whole.
- The inventory is now **30 / 2 / 2**.
- **Left in part:** 6b-ii, which waits, and 7c, which needs curvature.
- **Not begun:** 3c and 7e, both interpretive.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
