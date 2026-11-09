# Survey for the third paper to formalise, and its inventory: `r7717+71.1`

*A survey and inventory, not a campaign. No Lean was written for it. It reads the corpus at `f14d2e51` (r7717) and
the probes through campaign 118 (`CircleConic.lean`). The marking rule is the one used for P1 and P2: **BUILT**,
**BUILT IN PART** (gap named), **NOT BEGUN**. Every Lean name below was grepped for its declaration. Prices are new
lines in a probe; p is the chance of success.*

**Choice: P3, `corpus/SdS-slicing-curve_v2.tex`.** First campaign (119): the cubic chain, which is `prop:factor`,
`prop:r0zero`, `prop:readingswap`, `prop:involution`, `prop:locus` and `cor:nariai-locus`. It is registered in
`r7717_71_campaign119/PREDICTION.md`.

**Close second: P8** (`slicing_operator`). It is the better choice only if using the Lorentzian kit matters more than
how much the corpus leans on the paper.

## The weighing

Load-bearing is measured by `\cite` counts across `corpus/*.tex`. Fit is how well Mathlib, as it stands, covers the
paper's statements.

| P | file | key | cites | stmts | fit | verdict |
|---|---|---|---|---|---|---|
| **3** | `SdS-slicing-curve_v2` | `JanzenSlicing` | **222** | 15 | **High** | Chosen. 11 of the 15 have precise formal content; it is cubic algebra, trig and Euclidean geometry, all in Mathlib |
| 17 | `geometric_core_paper` | `JanzenGeometricCore` | 114 | 2 | Low | `prop:tangentnull` is a one-line identity. `prop:unique` is a classification of maximally symmetric pseudo-Riemannian manifolds; Mathlib has no such classification. Read plainly it is also too strong: anti-de Sitter is maximally symmetric and Lorentzian, so the uniqueness rests on the undefined "requisite causal structure" |
| 8 | `slicing_operator` | `JanzenOperator` | 95 | 5 | Medium–high | All five are precise, and `thm:kernel` and `prop:cosmo` suit the kit (Einstein tensor from the coordinate Riemann tensor, `ng_energy_const`). It is cited less than half as often as P3. The Ricci contraction of `kr_`'s Riemann tensor is new work |
| 5 | `groupoid_paper` | `JanzenGroupoid` | 91 | 13 | Low–medium | "The groupoid of observer descriptions" is never defined. The precise parts (D₃ relations, S₃ monodromy, Aut(A₂)) are largely built (`Row18Monodromy.lean`) |
| 6 | `shadow_of_existence` | `JanzenShadowExistence` | 72 | 2 | Low | Philosophy of science; no formal core |

**Why P3.**
- **It is the most cited companion paper in the corpus**, second only to the framework paper P7, whose statements
  are mostly about undefined "ontological layers". The horizon cubic, the root-exchange involution `σ` and the Nariai
  member it fixes are used by P5, P7, P8, P15 and P16.
- **It is the most formalisable.** Its precise content is polynomial identities, square roots, the triple-angle
  formula, `arcsin`, and Euclidean facts about an equilateral triangle. Every row below has p ≥ 0.75 except the
  turning-point dynamics.
- **Part of it already exists**, in other engines: `ShadowFormal/Nariai.lean`, `Row18Cubic.lean`,
  `ShadowEngine.lean` (`slice_gauss`, `sds_slice_gauss`) and `NoConnectionSweep.lean` (`throat_join`,
  `hinge_interval`). Bringing these onto one probe is cheap.

**Why not P8.** It suits the kit better, but the corpus leans on it less than half as much as on P3, and most of its
kernels are already built at the receipt level (`SecondSeatStatic.lean`, `CurvatureInstances.lean`). It is the
natural fourth paper.

---

# Inventory of P3 (`corpus/SdS-slicing-curve_v2.tex`)

The grep for `\begin{theorem|proposition|lemma|corollary}` finds **15** statements. They are split into **24 rows**.
Gauge `α = 1` throughout, as in the paper; `f(r) = 1 − 2M/r − r²`, `g(t) = t − t³`, `2M = g(r₀)`, and
`σ(x) = (−x + √(4 − 3x²))/2`.

**Other-engine work counts as BUILT IN PART.** The gap is the same each time: it is not in the probe chain.

## 1. `prop:turning` (l.277)

**1a.** `r f(r) = 0 ⟺ r³ − r + 2M = 0` for `r ≠ 0`, and `dr/dl = √|f|` vanishes exactly there.
- **Mark: NOT BEGUN.** 20–40 lines, p 0.98. **Interpretive:** no.

**1b.** At a root of the cubic, it is simple iff `f′(r_h) ≠ 0`, and double iff `f′(r_h) = 0` (Nariai).
- **Kit:** `discr_horizon`, `discr_horizon_eq_zero_iff`, `nariai_double_root` (`ShadowFormal/Nariai.lean`),
  `no_triple_root` (`Row18Cubic.lean`). **Mark: BUILT IN PART.** 60–120 lines, p 0.9.

**1c.** At a simple root the turning point is non-degenerate: `d²r/dl² = ±½ f′(r_h) ≠ 0`.
- **Reading flag:** `dr/dl = +√|f|` never turns; the curve turns only on `(dr/dl)² = |f|`. Then `r″ = ½ |f|′(r)`
  where `f ≠ 0`, and at a simple root the one-sided limits are `±½ f′(r_h)`.
- **Remains:** a `C²` solution of `(r′)² = |f(r)|` reaching `r_h` has `r′ = 0` and `r″ = ±½ f′(r_h)` there.
- **Mark: NOT BEGUN.** 150–300 lines, p 0.75. **Stop:** `|f|` is not differentiable at `r_h`; work on each side and
  take the one-sided limit.

## 2. `prop:factor` (l.310)

**2.** `r³ − r + g(r₀) = (r − r₀)(r² + r r₀ + r₀² − 1)`. The roots are `r₀` and `(−r₀ ± √(4 − 3r₀²))/2` when
`4 − 3r₀² ≥ 0`, and they sum to zero.
- **Kit:** `factor_general` (the double-root case only). **Mark: BUILT IN PART.** 40–80 lines, p 0.97.

## 3. `prop:r0zero` (l.363)

**3.** At `r₀ = 0`: `f = 1 − r²` and the roots are `{0, 1, −1}`.
- **Mark: NOT BEGUN.** 20–40 lines, p 0.98.
- **Interpretive:** "two readings of one slicing" is a reading; its formal core is the identity.

## 4. `prop:readingswap` (l.373)

**4.** `g(σ(r₀)) = g(r₀)` wherever `4 − 3r₀² ≥ 0`, so `f` is unchanged.
- **Mark: NOT BEGUN.** 40–80 lines, p 0.95.

## 5. `prop:involution` (l.388)

**5a.** `σ(σ(x)) = x`.
- **Reading flag** (from `r7699_71_survey`): it holds on `[0, 2/√3]`, but `σ` maps that interval onto
  `[−1/√3, 1]`, not into itself. `σ` is an involution of `[−1/√3, 2/√3]`. Both are stated.
- **Mark: NOT BEGUN.** 60–120 lines, p 0.9. **Stop:** the nested square root. The plan is the identity
  `4 − 3σ(x)² = ((3x + √(4 − 3x²))/2)²`, whose root is non-negative on `[−1/√3, 2/√3]`.

**5b.** `σ(r₀)` is the second positive root of `r₀`'s cubic.
- **Reading flag:** only for `r₀ ∈ [0, 1]`. For `r₀ ∈ (1, 2/√3]`, `σ(r₀) < 0`.
- **Mark: NOT BEGUN.** 40–80 lines, p 0.9.

**5c.** `σ(1/√3) = 1/√3`, `σ(0) = 1`, `σ(1) = 0`.
- **Mark: NOT BEGUN.** 20–40 lines, p 0.98.

## 6. `prop:locus` (l.441)

**6a.** `g(r) = g(r₀) ⟺ (r − r₀)(r² + r r₀ + r₀² − 1) = 0`.
- **Mark: NOT BEGUN.** 20–40 lines, p 0.98.

**6b.** The conic is an ellipse tilted at 45°. Its major axis lies along `r = −r₀`, with semi-axis `√2`, and its
minor axis along `r = r₀`, with semi-axis `√(2/3)`.
- **Formal content:** in `u = (r + r₀)/√2`, `v = (r − r₀)/√2`, `r² + r r₀ + r₀² = (3/2)u² + (1/2)v²`.
- **Mark: NOT BEGUN.** 60–120 lines, p 0.9.
- **Interpretive:** "the fundamental ellipse of the 2012 dissertation" is a citation.

## 7. `cor:nariai-locus` (l.457)

**7.** The line and the conic meet exactly at `r₀ = r = ±1/√3`. There the cubic has a double root and the third root
is `∓2/√3`. These two points are the endpoints of the minor axis.
- **Kit:** `nariai_factorisation`, `nariai_double_root` (the `+` sign). **Mark: BUILT IN PART.** 60–120 lines,
  p 0.95.

## 8. `prop:gnomonic` (l.530)

**8.** Interpretive. "A faithful planar chart" is undefined. The relation it supplies, `sin u = (2/√3) sin w`
(eq. `wdef`), is a definition. **No formal core.**

## 9. `prop:triple` (l.552)

**9a.** With `r₀ = (2/√3) sin w`, `g(r₀) = (2/(3√3)) sin 3w`.
- **Mark: NOT BEGUN.** 30–60 lines, p 0.97.

**9b.** Uniqueness: if `c > 0` and `g(c sin w) = k sin 3w` for all `w`, then `c = 2/√3`.
- **Mark: NOT BEGUN.** 60–100 lines, p 0.9.

## 10. `prop:conjugacy` (l.616)

**10.** `χ(g₁(x)) = σ(χ(x))`, where `g₁(x) = √(1 − x²)` and `χ(x) = (2/√3) sin((2/3) arcsin x)`.
- **Reading flag:** the paper states no domain. The identity holds on `[0, 1]` and fails on `[−1, 0)`: at `x = −1`
  the left side is `0` and the right side is `1`.
- **Mark: NOT BEGUN.** 100–200 lines, p 0.85. **Stop:** `arcsin √(1 − x²) = π/2 − arcsin x` on `[0, 1]`.

## 11. `prop:twoalpha` (l.682)

**11a.** (i) ⟺ (ii) ⟺ (iii), for `α > 0` and `R ≥ α`: `R = 2α`, `arcsin(α/R) = π/6`, and the equilateral triangle
with circumradius `R` has inradius `α`.
- **Mark: NOT BEGUN.** 80–150 lines, p 0.9.

**11b.** (iv): the nine-point circle of that triangle is the throat iff `R = 2α`.
- **Mark: NOT BEGUN.** 150–250 lines, p 0.8. **Stop:** Mathlib has no nine-point circle; it is built in coordinates.

**11c.** (v) and (vi).
- **Kit:** `hinge_interval` (`NoConnectionSweep.lean`) gives (vi): `s² = 4α² − ρ²`, vanishing at `ρ = 2α`.
- **Reading flag on (v):** the hinge sits on the hyperboloid at height `X₀ = √(R² − α²)`, which equals the tangent
  length at every `R`. That is P17's `prop:tangentnull`. So (v) is an equivalence only as "the common value is
  `√3α`".
- **Mark: BUILT IN PART.** 60–120 lines, p 0.9.

## 12. `prop:flip` (l.835)

**12.** Under `θ = π/2 + iψ`: `sin²θ = cosh²ψ`, `dθ² = −dψ²`, and the result is Lorentzian.
- **Kit:** `throat_join` (`NoConnectionSweep.lean`). **Mark: BUILT IN PART.** 30–60 lines, p 0.97.
- **Interpretive:** "the flip is not imposed" is a reading of `i² = −1`.

## 13. `prop:curvature` (l.960)

**13a.** The surface `dl² + r(l)² dφ²` has Gaussian curvature `K_G = −f′(r)/2r`.
- **Kit:** `slice_gauss` (`ShadowEngine.lean`) gives `−f′/2r` for the Levi-Civita connection of `dr²/f + r² dφ²`.
- **Reading flag** (from `r7699_71_survey`): the paper's surface is `dr²/|f| + r² dφ²`. Its curvature is
  `−|f|′/2r`, which is `+f′/2r` where `f < 0`. So the formula holds where `f > 0` and flips sign outside it.
- **Mark: BUILT IN PART.** The gaps are the other engine and the `f < 0` side. 200–400 lines, p 0.7.

**13b.** `−f′(r)/2r = 1 − M/r³` (with `α = 1`; `1/α² − M/r³` in general).
- **Kit:** `sds_slice_gauss`. **Mark: BUILT IN PART.** 20–40 lines, p 0.98.

## 14. `prop:rigidity` (l.1104)

**14.** Interpretive. "Placement of the charting observer" is undefined. The formal content, that `g(r₀)` depends on
`r₀` alone, is row 2. **No formal core.**

## 15. `prop:morphism-generation` (l.1120)

**15.** Interpretive. "The groupoid of observer descriptions" is undefined, and the proposition defers its
classification to P5. **No formal core.**

## Totals

- **24 rows.** 3 have no formal core (8, 14, 15). 3 more carry an interpretive clause around a formal core (3, 6b,
  12).
- **Marks:** 0 BUILT; 7 BUILT IN PART (1b, 2, 7, 11c, 12, 13a, 13b); 14 NOT BEGUN.
- **Flags:** 1c (the sign of `dr/dl`), 5a and 5b (domains), 10 (domain), 11c (v), and 13a (the sign where `f < 0`).
  None of them makes a stated identity false on the domain where the paper uses it.
- **Whole paper:** about 1,500–2,800 new lines, most at p ≥ 0.85. The expensive rows are 1c, 11b and 13a.

## Campaign order

- **119:** the cubic chain: rows 2, 3, 4, 5a–c, 6a–b and 7.
- **120:** rows 9a–b, 10 and 1a–b, the sky angle and the turning points.
- **121:** rows 11a–c and 12, the hinge and the flip.
- **122:** rows 13a–b and 1c, the curvature and the turning-point dynamics.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
