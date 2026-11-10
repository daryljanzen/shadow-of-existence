# `r7733+71.1` — PRE-REGISTRATION: campaign 127, **P5's dihedral core: rows 2a, 2c, 3, 4, 7b, 8 and 13**. ⌗ `750` new lines (band 450–1200), p `0.5`. **Expected stop:** `⟨σ, τ⟩ = range` of the map from `DihedralGroup 3`, and the `AddCircle` non-vanishing facts behind injectivity

*Registered before any Lean. The inventory is `r7733_71_survey/SURVEY.md`.*
- **The probe** is a new standalone file, `probes/Groupoid.lean`, prefix `gp_`. It imports only Mathlib. Later P5
  campaigns append to it, so it becomes P5's citable file.
- **The sky-angle circle** is `AddCircle (2π)`. `σ`, `τ` and `R` are elements of `Equiv.Perm (AddCircle (2π))`.

## One construction for both dihedral groups

| Item | Statement | Lines | p |
|---|---|---|---|
| `gp_act` | For an additive commutative group `A`, an additive map `e : ZMod n →+ A` and `d : A`: `r i ↦ (w ↦ w + e i)` and `sr i ↦ (w ↦ −w − e i + d)` is a group homomorphism `DihedralGroup n →* Perm A` | 80–150 | 0.8 |

## Rows

| Row | Statement | Lines | p |
|---|---|---|---|
| 2a | `σ = (w ↦ π/3 − w)`, `σ² = 1`, `σ ≠ 1` | 15–30 | 0.95 |
| 3 | `τ = (w ↦ w + 2π/3)` has `orderOf τ = 3` on `ℝ/2πℤ`; the same translation is `1` on `ℝ/(2π/3)ℤ` | 30–60 | 0.9 |
| 4 | `σ² = τ³ = (στ)² = 1`. `gp_act` with `n = 3`, `e i = i·(2π/3)` and `d = π/3` is injective, sends `sr 0 ↦ σ` and `r 1 ↦ τ`, and has range `closure {σ, τ}`. So `closure {σ, τ} ≃* DihedralGroup 3`, `Nat.card = 6`, and `≃* Perm (Fin 3)` (S₃) | 200–400 | 0.6 |
| 2c | `rₖ(w) = (2/√3) sin(w + 2πk/3)` solves `r³ − r + (2/3√3) sin 3w = 0` for each `k`. The action permutes the roots: `rₖ(g w) = r_{ψ(g) k}(w)` for every `g`, with `ψ` the same construction on `ZMod 3` (`d = 1`). `σ` swaps labels 0 and 1 and fixes 2, and `r₀, r₁ > 0` on `(0, π/3)`. `ψ` is the isomorphism onto `Perm (ZMod 3)` | 120–250 | 0.7 |
| 7b | `σ w = w ⟺ w ∈ {π/6, 7π/6}` on the circle, with `r₀ = 1/√3` and `−1/√3` there | 40–80 | 0.85 |
| 8 | At `w = π/6`: `2M = 2/(3√3)` and `ΛM² = 1/9` for `Λ = 3/α²`, with `M` scaled by `α` | 20–40 | 0.95 |
| 13 | `R = (w ↦ −w)` sends `sin 3w ↦ −sin 3w`, swaps `w = ±π/6` (`2M = ±2/(3√3)`) and fixes `w = 0`. `gp_act` with `n = 6`, `e i = i·(π/3)` and `d = 0` is injective with range `closure {σ, τ, R}`, so the group has order 12 and is `≃* DihedralGroup 6`. `closure {σ, τ}` has index 2 in it, and `w ↦ w + π` is central, of order 2, and not in `closure {σ, τ}` | 150–300 | 0.6 |

**Non-vacuity** is built into the statements: `σ ≠ 1`, `orderOf τ = 3` and the cardinalities 6 and 12.

**The expected stop** is row 4's closure equal to the range, and the facts that `↑(2π/3)`, `↑(4π/3)` and `↑π` are
non-zero in `AddCircle (2π)`. **The fallback** is to state the relations, the cardinality 6 of `closure {σ, τ}`
through the explicit list of six maps, and the injective homomorphism, without the `MulEquiv`s. Rows 4 and 13
would then be marked BUILT IN PART.

**Interpretive, not formalised:** "the within-single-geometry morphisms" as a category, which is row 1 (campaign 128).

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
