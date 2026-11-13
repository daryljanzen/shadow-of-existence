# Survey for the eighth paper to formalise, and its inventory: `r7755+71.1`

*A survey and inventory, not a campaign. It reads the corpus at `968993e6` (r7755) and the probes through campaign
136. The criterion is 69's, as in r7741: **the largest formal core within reach of Mathlib and the files already
built.** Already formalised: P1, P2, P3, P8, P5, P15, P9. Statement counts are `theorem`, `proposition`, `lemma` and
`corollary` environments, recounted at this revision.*

**Choice: P7, `corpus/CR_framework.tex` (263 cites, the most cited companion).**
- **Rows:** 20 statements. 6 of them carry a formal core, split into **15 cored rows**.
- **Reach:** **14** of the 15 are within reach. The 15th (7c) is priced with a named stop.
- **Price:** 2 campaigns, **700–1200 lines in total, p(14 of 15 BUILT) 0.6.**

## The candidates

| P | file | cites | stmts | cored rows | reach | stop / why not |
|---|---|---|---|---|---|---|
| **7** | `CR_framework` | **263** | **20** | **15** | **14** | 7c, the bound `|Im τ̃| ≤ πα/3` along the whole lap, a branch analysis of a complex integral. The 14 statements without a core are about "ontological layers", "projections" and "augmentation", which are undefined |
| 13 | `boundary_paper` | 144 | 4 | 6 | 5 | `prop:boundary`: that the SM algebra does not embed in `so(5,1)` needs a rank or maximal-compact argument, which needs Lie theory Mathlib lacks. The parity and conjugation rows are algebra |
| 12 | `algebroid_paper` | 103 | 1 | 4 | 4 | None: the `so(5,1) = so(4,1) ⊕ m` brackets are matrix algebra. But it is small (one statement) |
| 11 | `dynamics_paper` | 70 | 3 | 3 | 2 | `prop:twoKV`'s "exactly two" needs the full Killing equation. Its Petrov type I is now reachable with campaign 136's `ij_I`/`ij_J`, and the wall's regularity reuses `pw_IJ` |
| 17 | `geometric_core_paper` | 133 | 2 | 2 | 1 | `prop:unique` is a classification. `prop:tangentnull` (tangent–secant equals null) is algebra |
| 14 | `matter_sector_paper` | 178 | 2 | 1 | 0–1 | "Exactly one normalisable zero-mode" is spinor ODE uniqueness |
| SYN | `CR_synthesis` | — | 1 | 1 | 0 | P17's `prop:unique` restated |
| 4, 6 | parallax, shadow | 90, 92 | 1, 2 | 0 | 0 | Philosophical theorems, no formal core |
| 10, 16 | canonical time, cosmogenesis | 113, 112 | 0 | — | — | No stated results |

**Why P7.**
- **It has the largest reachable core:** 14 rows, against P13's 5.
- **It is the most cited paper in the corpus,** and P8, P15, P9 and P13 all lean on its bead, two-turnings and
  null-boundary statements.
- **Its precise content sits inside theorems whose framing is interpretive.** `thm:null-boundary`, `thm:bead` and
  `lem:twoturnings` each make exact claims (null hypersurfaces, horizon areas, surface gravities, root
  configurations, affine inequivalence, a complex turnaround time) that are separable from the ontology. The
  inventory splits them out row by row.
- **Several rows reuse files already built.** These would be copied verbatim into P7's own citable file:
  - `sr_future_diverges` (P2, `CircleChart.lean`) for row 1;
  - `cm_throat_root` (P15) for row 7a;
  - the `sinh^{2/3}` law `rExp` (`LimitNariai.lean`) for row 6.
- **Why not P13:** its headline (`prop:boundary`) is out of reach, and its reachable rows are a handful of parity
  identities.

---

# Inventory of P7 (`corpus/CR_framework.tex`)

`f = 1 − 2M/r − r²/α²`, `α = √(3/Λ)`. Marks: **NOT BEGUN** throughout. Prices are new lines, and p is the chance of
success.

## 1. Asymptotic non-intersection (l.402)
- **1.** For the exterior static time, a radial infall reaches `r = 2M` only as `t → ∞`. Status:
  - **Exists** as `sr_future_diverges` (P2), so the row is a verbatim port plus a statement in P7's form.
  - 60–150, p 0.8. **Stop:** whether the P2 section copies standalone.

## 2. Interpretive statements (no formal core)
- **l.354** (lapse and shift), **l.408**, **l.418**, **l.440**, **l.450**, **l.460**, **l.478**, **l.500**, **l.508**,
  **l.562**, **l.570**, **l.1508** (`thm:augmentation-p7`), **l.1664** (`thm:cosmogenesis`) and **l.1676**
  (`cor:nonspherical`). They state ontology; "layer", "projection" and "augmentation" have no mathematical
  definition in the paper.

## 3. `thm:null-boundary` (l.909)
- **3a.** In the static de Sitter patch, `r = α` is a null hypersurface (`g^{rr} = 0` there, with a null normal).
  40–80, p 0.9.
- **3b.** Horizon areas:
  - `4πα²` for de Sitter;
  - at the Nariai mass the two positive roots coincide at `α/√3`, area `4πα²/3`. This rides on `cm_throat_root`.
  - 30–60, p 0.9.
- **3c.** Surface gravities: `κ = |f′(α)|/2 = 1/α ≠ 0` for de Sitter, and `f = f′ = 0` (`κ = 0`) for Nariai. 30–60,
  p 0.9.
- **3d.** In the embedding `ℝ^{1,4}`, `p ↦ ℋ_c⁺(p)` is injective on the waist `S³`, the oriented future horizon
  `{X₀ = X·n_p}` distinguishing `p` from `−p`. 100–200, p 0.7. **Stop:** fixing a definition of "oriented future
  horizon" that the paper's prose supports. Surjectivity is by the paper's own construction and is left
  interpretive.
- **Interpretive:** the correspondence `𝒩` and property (iv).

## 4. Corollary (l.949)
- **4 (row 6 in the totals).** `r = (2Mα²)^{1/3} sinh^{2/3}(3τ̃/2α)` solves `(dr/dτ̃)² = 2M/r + r²/α²`. **Exists** as
  `rExp` (`LimitNariai.lean`), so this is a port. 40–100, p 0.85.

## 5. `thm:bead` (l.965)
- **5a (row 7a).** The Nariai member's turning points are `+α/√3` (double) and `−2α/√3`, with branch point `0`. This
  is a port of `cm_throat_root`. 20–40, p 0.95.
- **5b (row 7b).** At `r = −(2Mα²)^{1/3}`, `τ̃ = −iπα/3` satisfies the bead `r³ = 2Mα² sinh²(3τ̃/2α)` (`ℂ`), and
  `1 − f = 0` there. 40–80, p 0.85.
- **5c (row 7c).** Along the lap, `|Im τ̃| ≤ πα/3`. 150–300, p 0.4. **Stop:** the branch analysis of
  `∫(2M/r + r²/α²)^{−1/2}dr` on `r < 0`.
- **Interpretive:** the closure on one smooth manifold (P3's slicing territory) and the two readings.

## 6. `lem:twoturnings` (l.998)
- **6a (row 8a).** `1 − f = 2M/r + r²/α²`, and `f = 1 ⇔ r³ = −2Mα²`. 10–20, p 0.95.
- **6b (row 8b).** The comoving roots of `r³ + 2M = 0` (`α = 1`) form an equilateral triangle, permuted by
  `r ↦ e^{2πi/3}r`. 40–80, p 0.9.
- **6c (row 8c).** For `0 < M < 1/(3√3)` the horizon cubic `r³ − r + 2M` has three distinct real roots (casus
  irreducibilis, discriminant `4 − 108M² > 0`). 60–120, p 0.85.
- **6d (row 8d).** Affine inequivalence: no `z ↦ az + b` (`a ≠ 0`, complex) maps the three colinear real roots onto
  the equilateral triple. Affine maps preserve collinearity. 60–120, p 0.85.
- **6e (row 8e).** At `E = 1`, `t = τ` at `f = 1`. This is the paper's "fixes the sign" claim, limited to the
  algebra. 20–40, p 0.8.
- **Interpretive:** "the locus that defines the fundamental rest frame".

## 7. `thm:antimatter-progenitor` (l.1140)
- **7 (row 9).** Under `R: (r, 2M) ↦ (−r, −2M)`, the action integrand `r(f − 1) = −2M − r³/α²` is odd. 10–30,
  p 0.95.
- **Interpretive:** "antimatter black hole", `3̄ = R(3)` (P5 carries the `D₆`).

## Totals
- **Statements:** 20. 6 carry a formal core (l.402, l.909, l.949, l.965, l.998, l.1140), and the 14 in §2 do not.
- **Cored rows (15):** 1, 3a, 3b, 3c, 3d, 6 (eq. 949), 7a, 7b, 7c, 8a, 8b, 8c, 8d, 8e and 9.
- **Reach:** 14 of 15 (all but 7c).

## Campaign plan
- **137:** 3a, 3b, 3c, 7a, 7b, 8a–8e, 9, in a new probe `probes/Framework.lean` (`fw_`). These are the algebraic and
  complex rows. About 400–650 lines.
- **138:** 1 and 6 (ports), 3d (embedding) and the registered attempt at 7c. About 300–550 lines.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
