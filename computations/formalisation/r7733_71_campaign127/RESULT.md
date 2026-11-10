# `r7733+71.2` — RESULT: campaign 127, **P5's dihedral core is BUILT: rows 2a, 2c, 3, 4, 7b, 8 and 13.** ⌗ `504` lines, a new standalone file, inside the registered band of 450–1200 but below the point (`750`). ⌗ p `0.5` came true. The expected stop, `⟨σ, τ⟩ = range`, fell, and no fallback was used

*Against `PREDICTION.md` (`r7733+71.1`). 71 ran `lake env lean probes/Groupoid.lean`. It exits 0 with no errors and no
warnings. All `30` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`. The forbidden-token grep
is clean, the probe imports only Mathlib, and `check_no_sorry.py` reads ALL 29 THEOREMS COMPILE.*

**The file** is `probes/Groupoid.lean`, prefix `gp_`, and it is P5's citable file. The sky-angle circle is
`gp_T = AddCircle (2π)`. `σ`, `τ` and `R` are elements of `Equiv.Perm gp_T`.

## Why the line count is low

One construction serves `D₃` on the circle, `D₃` on the root labels and `D₆` on the circle. The root permutation,
priced as up to 18 trigonometric cases, came out as two cases through a congruence mod 3 (`gp_val_lift`).

## The construction

- **`gp_act e d : DihedralGroup n →* Perm A`** sends `r i ↦ (w ↦ w + e i)` and `sr i ↦ (w ↦ −w + (d − e i))`.
- **`gp_act_injective`:** it is injective if `e i = 0` forces `i = 0` and some `a` has `a + a ≠ 0`.
- **`gp_act_range`:** its range is the closure of the image of a generating set. `gp_closure_top` gives
  `⟨r 1, sr 0⟩ = ⊤`.

## Rows — BUILT

- **2a, `gp_σ_sq`:** `σ = (w ↦ π/3 − w)` has `σ² = 1` and `σ ≠ 1`.
- **3, `gp_τ_order`:** `τ = (w ↦ w + 2π/3)` has `orderOf τ = 3` on `ℝ/2πℤ`. **`gp_τ_short`:** on `ℝ/(2π/3)ℤ`
  the same translation is the identity, which is `prop:tau`'s caveat.
- **4:**
  - `gp_relations`: `σ² = τ³ = (στ)² = 1`.
  - `gp_D3`: `⟨σ, τ⟩ ≃* DihedralGroup 3`, through the injective `gp_φ` with range `closure {σ, τ}`
    (`gp_φ_range`).
  - `gp_D3_card`: the group has order 6.
  - `gp_S3`: `DihedralGroup 3 ≃* Perm (ZMod 3)`, which is `S₃`.
- **2c:**
  - `gp_root_cubic`: each `rₖ(w) = (2/√3) sin(w + 2πk/3)` solves `r³ − r + (2/3√3) sin 3w = 0`.
  - `gp_root_perm`: `r_{ψ(g)k}(g w) = rₖ(w)` for every `g ∈ D₃`. Here `g w` is the action lifted to `ℝ`
    (`gp_lift_coe`), and `ψ` is the label action, a push-forward.
  - `gp_σ_roots`: `σ` swaps labels 0 and 1 and fixes 2.
  - `gp_roots_pos`: the swapped roots are positive on `(0, π/3)`.
- **7b, `gp_σ_fixed`:** on the full circle `σ w = w ⟺ w ∈ {π/6, 7π/6}`. There `r₀ = 1/√3` and `−1/√3`.
- **8, `gp_nariai_mass`:** at `w = π/6`, `2M = 2/(3√3)`. With `M = α/(3√3)` and `Λ = 3/α²`, `ΛM² = 1/9`.
- **13:**
  - `gp_R_mass`: `R = (w ↦ −w)` sends `sin 3w ↦ −sin 3w`, swaps the Nariai vantages `±π/6`
    (`2M = ±2/(3√3)`), and fixes `0`.
  - `gp_D6` and `gp_D6_card`: `⟨σ, τ, R⟩ ≃* DihedralGroup 6`, of order 12.
  - `gp_D3_le_D6`: `⟨σ, τ⟩` sits inside it with index 2.
  - `gp_half_turn`: `w ↦ w + π` has order 2, lies in `⟨σ, τ, R⟩`, is central there, and is not in `⟨σ, τ⟩`. So
    `Aut(A₂) = S₃ × ℤ₂ ≅ D₆`.

**Non-vacuity** is in the statements: `σ ≠ 1`, `orderOf τ = 3`, and the orders 6 and 12.

**The sign.** The roots transform by an anti-homomorphism under the circle action, so the label action that is a
homomorphism is the push-forward: `ψ(r i) = (k ↦ k − i)` and `ψ(sr i) = (k ↦ −k + 1 + i)`. `σ`'s swap of labels 0
and 1 is unaffected.

## Marks (P5's inventory, `r7733_71_survey/SURVEY.md`)

- **Built (7):** 2a, 2c, 3, 4, 7b, 8 and 13.
- **Built in part (6):** 2b, 7a, 9, 10, 11b and 12a, in other probes.
- **Not begun (4):** 1, 5, 11a and 12b.
- **No formal core (1):** 6.

**Next (campaign 128):** 1 and 5, the morphism group and the completeness of `⟨σ, τ⟩`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
