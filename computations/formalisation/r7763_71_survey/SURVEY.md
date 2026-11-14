# Survey for the ninth paper to formalise, and its inventory: `r7763+71.1`

*A survey and inventory, not a campaign. It reads the corpus at `07d109de` (r7763) and the probes through campaign
138. The criterion is r7741's: **the largest formal core within reach of Mathlib and the files already built.**
Already formalised: P1, P2, P3, P8, P5, P15, P9, P7.*

*Per r7763, rows in passages about to be rewritten are avoided: P15, P7's rate remark, P10 and P16. None of the rows
below lies there.*

**Choice: P13, `corpus/boundary_paper.tex` (144 cites).**
- **Rows:** 4 statements, split into **10 cored rows**. **9 are within reach.**
- **The 10th** is `prop:boundary`'s embedding claim, priced as beyond (Lie theory Mathlib lacks).
- **Price:** one campaign, **350–650 lines, p(9 of 10 BUILT) 0.75.**

## The candidates

| P | file | cites | stmts | cored rows | reach | stop / why not |
|---|---|---|---|---|---|---|
| **13** | `boundary_paper` | **144** | **4** | **10** | **9** | `prop:boundary`: that the SM gauge algebra is not a continuous isometry of the substrate needs a rank or maximal-compact argument for real forms, which needs Lie theory Mathlib lacks. Every other row is elementary algebra, complex conjugation or `2×2` linear algebra |
| 12 | `algebroid_paper` | 103 | 1 | 4 | 4 | None: the `so(5,1) = so(4,1) ⊕ m` grading and `[M₀₅, M₁₅] = −M₀₁` are matrix algebra. But it is one statement and 4 rows; a good second |
| 11 | `dynamics_paper` | 70 | 3 | 5 | 3 | `prop:twoKV`'s "exactly two" needs the full Killing equation. Its type I is reachable with campaign 136's `ij_I`/`ij_J`, but it is a two-variable Weyl computation (heavy). The wall's non-degeneracy and type N reuse `pw_IJ` |
| 17 | `geometric_core_paper` | 133 | 2 | 2 | 1 | `prop:unique` is a classification. `prop:tangentnull` is one algebraic row |
| 14 | `matter_sector_paper` | 178 | 2 | 1 | 0–1 | "Exactly one normalisable zero-mode" is spinor ODE uniqueness |
| 4, 6, SYN | parallax, shadow, synthesis | — | 1, 2, 1 | 0–1 | 0 | Philosophical theorems, or P17's `prop:unique` restated |
| 10, 16 | canonical time, cosmogenesis | — | 0 | — | — | No stated results, and under rewrite (r7763) |

**Why P13.**
- **It has the largest reachable core left:** 9 rows, against P12's 4 and P11's 3.
- **Its rows are exact and short:** a parity split, an isometry, a complex-conjugation symmetry of the bead, a
  weight-set identity and a `2×2` Lorentz fact.
- **It joins two papers already formalised:**
  - P7's bead (`fw_τ`) supplies 3c's wings;
  - P5's `D₆` supplies the setting for 4i.
- **Its one stop is its headline** (`prop:boundary`). The inventory names it, and the rest does not depend on it.

---

# Inventory of P13 (`corpus/boundary_paper.tex`)

`f(r) = 1 − 2M/r + Q²/r² − Λr²/3`; `R: (r, M) ↦ (−r, −M)`; `K: (r, τ̃) ↦ (r̄, τ̃̄)`. Marks: **NOT BEGUN** throughout.

## 1. `prop:boundary` (l.234)
- **1.** The SM gauge algebra is not contained in the substrate's continuous symmetry `so(5,1)` as an isometry
  algebra of the real substrate. **Beyond:** Mathlib has no classification of the real forms of compact
  subalgebras, nor of their ranks. The rest of the statement (the cascade, the Wick face, "escapes") is interpretive.

## 2. `prop:conjugation-parity` (l.312)
- **2a.** `f = f_even + f_odd` in `r`, with `f_even = 1 + Q²/r² − Λr²/3` and `f_odd = −2M/r`. So the mass term is
  `R`-odd and the de Sitter and charge terms are `R`-even, and `f(−r; −M) = f(r; M)`. 20–40, p 0.95.
- **2b.** `f` depends on `Q` only through `Q²` (`f(Q) = f(−Q)`), while the Maxwell potential `A_t = −Q/r` is odd in
  `Q`. So the charge sign is carried by `A` alone. 15–30, p 0.95.
- **Interpretive:** "`P` and `T` stay geometric", "a geometric `CPT` is not auto-yielded".

## 3. `prop:conjugation-closure` (l.327)
- **3a.** `R` is a linear isometry of the charged metric `diag(−f, 1/f, r², r² sin²θ)`. The map `r ↦ −r` with
  `M ↦ −M` pulls the metric back to itself, and is blind to `Q`. 60–120, p 0.85.
- **3b.** `K` is a symmetry of the bead: `r³ = 2Mα² sinh²(3τ̃/2α)` ⟹ `r̄³ = 2Mα² sinh²(3τ̃̄/2α)` for real `M, α`.
  `K` is antilinear and an involution. 30–60, p 0.9.
- **3c.** `K` fixes the real axis, and swaps the two `r < 0` wings: the conjugate of P7's `fw_τ` (`Im τ̃ = −πα/3`
  beyond the turnaround) is the other wing (`Im = +πα/3`), and also solves the bead. 40–80, p 0.85. It reuses
  `fw_τ`'s definition by verbatim copy.
- **3d.** `R ∘ K = K ∘ R`, and it is an antilinear involution. 15–30, p 0.95.
- **Interpretive:** the factorisation `C = (Q ↦ −Q)_field ∘ (R∘K)_geometric` as a statement about charge
  conjugation.

## 4. `prop:residue-is-the-bead` (l.353)
- **4i.** `3̄ = R(3)` on the `A₂` weight lattice:
  - the diagram automorphism (`ω₁ ↔ ω₂`) maps the weights of `𝟑`, `{ω₁, ω₂ − ω₁, −ω₂}`, onto those of `𝟑̄`;
  - `−1 ∉ W(A₂)`, so it is not a Weyl reflection.
  - 60–120, p 0.8.
- **4ii.** Mass reversal, `2M ↦ −2M`. This is 2a's content and is counted there.
- **4iii.** Every orientation-reversing linear isometry of `ℝ^{1,1}` swaps the two null lines `u = 0` and `v = 0`.
  This is the paper's "generic face". 60–120, p 0.85.
- **4iv.** `R` fixes exactly `r = 0` (the bead's branch point) and exchanges `r > 0` with `r < 0`. 10–20, p 0.95.
- **Interpretive:** "one `ℤ₂`, four faces", "matter/antimatter skeleton".

## Totals
- **Statements:** 4.
- **Cored rows (10):** 1, 2a, 2b, 3a, 3b, 3c, 3d, 4i, 4iii, 4iv. 4ii is folded into 2a.
- **Reach:** 9 of 10 (all but 1).

## Campaign plan
- **139:** the nine reachable rows, in a new probe `probes/Boundary.lean` (`bd_`), copying P7's `fw_τ` (and its
  lemmas) verbatim for 3c. About 350–650 lines.
- **Row 1** is left NOT BEGUN, priced as beyond.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
