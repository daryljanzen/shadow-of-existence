# Survey for the fifth paper to formalise, and its inventory: `r7733+71.1`

*A survey and inventory, not a campaign. It reads the corpus at `341a1034` (r7733) and the probes through campaign
126 (`StaticEinstein.lean`). The marking rule is the one used for P1–P3 and P8: **BUILT**, **BUILT IN PART** (gap
named), **NOT BEGUN**. Every Lean name below was grepped for its declaration. Cite counts are recounted at this
revision.*

**Choice: P5, `corpus/groupoid_paper.tex`.** First campaign (127): the dihedral core, which is rows 2a, 2c, 3, 4,
7b, 8 and 13. It is registered in `r7733_71_campaign127/PREDICTION.md`.

## The re-weighing after P3 and P8

| P | key | cites | stmts | fit | now |
|---|---|---|---|---|---|
| 7 | `JanzenCRframework` | 263 | 20 | Low | Unchanged. Its statements are about "ontological layers" and "projections", which are undefined |
| 14 | `JanzenMatter` | 178 | 2 | Low | Unchanged |
| 15 | `JanzenCRcosmology` | 163 | 7 | Low–medium | **Up a little.** P8's kit fits `prop:throat` (`dS₂ × S²`) and `prop:flat`. The other five are amplitudes and transmission estimates |
| 13 | `JanzenBoundary` | 144 | 4 | Low | Unchanged. Standard Model gauge groups |
| 17 | `JanzenGeometricCore` | 133 | 2 | Low | Unchanged |
| 10 | `JanzenCanonicalTime` | 113 | 0 | — | No stated results |
| 16 | `JanzenCosmogenesis` | 112 | 0 | — | No stated results |
| **5** | `JanzenGroupoid` | 109 | 13 | **Medium–high** | **Up, and chosen.** See below |
| 9 | `JanzenRange` | 107 | 11 | Low | Unchanged. It needs Kerr–de Sitter and the Petrov classification |
| 6 | `JanzenShadowExistence` | 92 | 2 | Low | No formal core |
| 4 | `JanzenModernParallax` | 90 | 1 | Low | One statement, observational |
| 12 | `JanzenAlgebroid` | 103 | 1 | Low | One statement |
| 11 | `JanzenDynamics` | 70 | 3 | Low | Unchanged |

**Why P5, and why it moved up.**
- **P3's closure built its precise core.** `SlicingCurvature.lean` has σ (`sl_σ`, `sl_σ_σ`, `sl_σ_fixed`,
  `sl_σ_sin`), the Nariai member (`sl_nariai`) and the seam flip (`sl_flip`). `Row18Monodromy.lean`, which imports
  only Mathlib, proves that the cover is a covering map, that each Nariai loop swaps two sheets (`swap_plus`,
  `swap_minus`), and that the monodromy group is all of `S₃` (`monodromy_surjective`).
- **What remains is precise.** The relations, `D₃ ≅ S₃`, the root permutation, `Aut(A₂) ≅ D₆` and the deck group
  are finite group theory on the sky-angle circle `ℝ/2πℤ`, all in Mathlib. `prop:completeness` is a classification
  of continuous bijections of the circle, which is real but bounded topology.
- **It is load-bearing.** P2, P3, P7, P8 and P15 cite σ, the Nariai fixed point and the `S₃`.
- **Why not P15** with more citations: only two of its seven statements have a formal core.

**60's offered declaration joining `thm:kernel`'s two halves (P8) is left for now.** It is a small campaign that
can be taken between P5's campaigns if 69 wants P8 to cite one statement.

---

# Inventory of P5 (`corpus/groupoid_paper.tex`)

The grep for `\begin{theorem|proposition|lemma|corollary}` finds **13** statements. They are split into **18 rows**.
- **The sky angle:** `w ∈ ℝ/2πℤ`, with `r₀ = (2/√3) sin w` and `2M = (2/3√3) sin 3w` (gauge `α = 1`).
- **The cubic's roots:** `rₖ(w) = (2/√3) sin(w + 2πk/3)` for `k ∈ ℤ/3`. Each solves `r³ − r + 2M = 0`.
- **Other-probe work counts as BUILT IN PART.** The gap is that it is not yet in P5's file.

## 1. `prop:groupoid` (l.188)

**1.** The maps `ĝ` of the circle that are continuous bijections with `sin 3ĝ(w) = sin 3w` form a group under
composition.
- **Mark: NOT BEGUN.** 60–120 lines, p 0.85.
- **Interpretive:** "the single invariant of `G` is the SdS geometry".

## 2. `prop:sigma` (l.212)

- **2a.** `σ : w ↦ π/3 − w` on `ℝ/2πℤ`, with `σ² = 1`.
  - **Mark: NOT BEGUN.** 10–20 lines, p 0.98.
- **2b.** In the slicing parameter, `σ` is `r₀ ↦ (−r₀ + √(4 − 3r₀²))/2`.
  - **Kit:** `sl_σ_sin` (`SlicingCurvature.lean`). **Mark: BUILT IN PART.** 30–60 lines (copy), p 0.95.
- **2c.** `σ` exchanges the two non-fixed positive roots: `rₖ(σw) = r₁₋ₖ(w)`, so labels 0 and 1 swap and label 2 is
  fixed. Both `r₀` and `r₁` are positive for `w ∈ (0, π/3)`.
  - **Mark: NOT BEGUN.** 80–160 lines, p 0.8.

## 3. `prop:tau` (l.234)

**3.** `τ : w ↦ w + 2π/3` has order exactly 3 on `ℝ/2πℤ`. It acts trivially on `ℝ/(2π/3)ℤ`, as the proof's caveat
says.
- **Mark: NOT BEGUN.** 20–40 lines, p 0.95.

## 4. `prop:relations` (l.263)

**4.** `σ² = τ³ = (στ)² = 1`. The subgroup of `Perm(ℝ/2πℤ)` they generate is isomorphic to `DihedralGroup 3`, has
order 6, and is isomorphic to `S₃`.
- **Mark: NOT BEGUN.** 200–400 lines, p 0.65. **Stop:** the closure equals the range of the map from
  `DihedralGroup 3`.

## 5. `prop:completeness` (l.275)

**5.** A continuous bijection `ĝ` of `ℝ/2πℤ` with `sin 3ĝ(w) = sin 3w` for all `w` is one of the six maps
`w ↦ ±w + c`, so it lies in `⟨σ, τ⟩`.
- **Mark: NOT BEGUN.** 300–700 lines, p 0.45. **Stop:** the branch argument. At each point one of
  `3ĝ(w) ∓ 3w` is in `2πℤ` (or `π + 2πℤ`), and continuity with injectivity rules out a switch. The lift to `ℝ`
  is the likely route.

## 6. `prop:dim-collapse` (l.337)

**6.** `r₀ ∈ (−2/√3, 2/√3)` parametrises, and the map to "the underlying manifold" is constant.
- **No formal core.** The map is constant by definition.

## 7. `prop:nariai-fixed` (l.365)

- **7a.** `σ(r₀) = r₀ ⟺ r₀ = 1/√3` on the admitted range, and the two non-fixed roots collide there.
  - **Kit:** `sl_σ_fixed`, `sl_nariai`. **Mark: BUILT IN PART.** 30–60 lines (copy), p 0.95.
- **7b.** On the full circle the reflection has exactly two fixed points, `π/6` and `7π/6`. The second gives
  `r₀ = −1/√3`.
  - **Mark: NOT BEGUN.** 40–80 lines, p 0.85.

## 8. `prop:single` (l.417)

**8.** At Nariai, `2M = 2/(3√3)`, equivalently `ΛM² = 1/9` with `Λ = 3/α²` (`G = c = 1`).
- **Kit:** `sl_nariai` for `2M`. **Mark: BUILT IN PART.** 20–40 lines, p 0.95.
- **Interpretive:** "the reassignment is unique".

## 9. `prop:partial` (l.468)

**9.** `ξ : θ ↦ π/2 + iψ` gives `dθ = i dψ`, so `dθ² = −dψ²` (the signature flip).
- **Kit:** `sl_flip` (`SlicingHinge.lean`). **Mark: BUILT IN PART.** 20–40 lines (copy), p 0.95.
- **Interpretive:** `ξ² = id` "as a swap of two descriptions".

## 10. `prop:sweep` (l.516)

**10.** `K_G = 1/α² − M/r³` on the static slicing surface, which diverges as `r → 0⁺`.
- **Kit:** `sl_curvature_static` (`SlicingCurvature.lean`). **Mark: BUILT IN PART.** 30–60 lines, p 0.9.
- **Interpretive:** "pivot", "artefact", and "identical through first order".

## 11. `prop:monodromy` (l.557)

- **11a.** The Nariai point is a simple zero of `Δ = 4 − 27(2M)²`, with `dΔ/d(2M) = −54(2M) ≠ 0`.
  - **Mark: NOT BEGUN.** 10–20 lines, p 0.98.
- **11b.** The monodromy about each Nariai point is a transposition of two sheets.
  - **Kit:** `swap_plus`, `swap_minus` (`Row18Monodromy.lean`). **Mark: BUILT IN PART.** Copy, 500–700 lines, p 0.8.

## 12. `prop:deck` (l.565)

- **12a.** The monodromy group is `S₃`.
  - **Kit:** `monodromy_surjective`, `fibre_card`. **Mark: BUILT IN PART** (with 11b's copy).
- **12b.** The deck group is trivial: the centraliser of `S₃` in `Sym(3)` is trivial, and a transitive degree-3
  cover with monodromy of order 6 is not normal.
  - **Mark: NOT BEGUN.** 40–100 lines, p 0.85.

## 13. `prop:autA2` (l.655)

**13.** `R : w ↦ −w` sends `2M ↦ −2M`, swaps the Nariai values `±2/(3√3)` and fixes `2M = 0`. `⟨σ, τ, R⟩` has
order 12 and is isomorphic to `DihedralGroup 6`. It contains `⟨σ, τ⟩` with index 2, and the half-turn
`w ↦ w + π` is central of order 2 and outside `⟨σ, τ⟩`. That is `S₃ × ℤ₂`.
- **Mark: NOT BEGUN.** 150–300 lines, p 0.65.

## Totals

- **18 rows.** 1 has no formal core (6).
- **Marks:** 0 BUILT; 7 BUILT IN PART (2b, 7a, 8, 9, 10, 11b, 12a); 10 NOT BEGUN.
- **Reading flags so far:** none. `prop:tau`'s domain caveat is stated in its own proof.
- **Whole paper:** about 1,800–3,200 new lines.

## Campaign order

- **127:** the dihedral core: 2a, 2c, 3, 4, 7b, 8 and 13, in a new standalone probe.
- **128:** 1 and 5, the morphism group and its completeness.
- **129:** 11 and 12, the monodromy (copying `Row18Monodromy`), and the deck group.
- **130:** the copies: 2b, 7a, 9 and 10, which would close P5.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
