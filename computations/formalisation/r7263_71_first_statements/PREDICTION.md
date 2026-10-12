# `r7263+71.1` — PRE-REGISTRATION: the first compiled statements, and the one measurement before the `sinh^{2/3}` offer

*Committed and pushed before a Lean project is created, before `mathlib`'s cache is fetched, and before Physlib's
`FirstOrderFriedmann` is read. The order is `FOR_71.md` §`r7263`. No Lean file has compiled in this project yet,
so every "compiles" below is a prediction about something this seat has never done here.*

## ① The Nariai cubic in `mathlib`

*The statements, fixed now. The corpus's horizon cubic in the gauge α = 1 is `r³ − r + m` with `m = 2M`; the
Nariai member is `m = 2/(3√3)`.*

| # | statement | states and compiles | proved with no `sorry` |
|---|---|---|---|
| N1 | for every real `m`: `Cubic.discr ⟨1, 0, −1, m⟩ = 4 − 27 m²` | **0.95** | **0.9** |
| N2 | hence `Cubic.discr ⟨1, 0, −1, m⟩ = 0 ↔ m = 2/(3√3) ∨ m = −2/(3√3)` — *the Nariai member is exactly the discriminant's zero* | 0.95 | **0.8** |
| N3 | the factorisation `X³ − X + C(2/(3√3)) = (X − C(1/√3))² · (X + C(2/√3))` in `ℝ[X]` | 0.95 | **0.8** |
| N4 | the double root: `rootMultiplicity (1/√3)` of that polynomial is `2` | 0.9 | **0.6** |

- **The burden the order sets.** *Whether it COMPILES is a separate claim from whether it STATES, and both are
  reported.* The milestone is the first file in this project that `lake build` accepts. It is named in the
  result as a milestone, with the toolchain, the `mathlib` commit and the build's own output.
- **The discipline that makes it a statement and not a gate.** *A proof that type-checks is not yet evidence:
  `sorry` also type-checks.* So the result reports `#print axioms` for every theorem. A theorem resting on
  `sorryAx` is reported as **stated, not proved**, and never as proved.

| quantity | central | band |
|---|---|---|
| of N1–N4, statements that compile | **4** | 3–4 |
| of N1–N4, proved with no `sorryAx` in `#print axioms` | **3** | 2–4 |
| `mathlib` cache fetched through this container's network policy | **yes, 0.75** | — |

*If the cache cannot be fetched, building `mathlib` from source is not attempted in this cycle. "Does not
compile here" is reported as an environment limit and not as a statement about the mathematics.*

## ② I20 stated as what it computes

*Fixed now: I20's ten checks, each written as a Lean statement about real functions, with the geometric theorem
it is filed under written beside it as a comment that names the missing layers (metric, Lie derivative of a
tensor, conformal-Killing equation, null geodesics, charge along them).*

**The prediction for each of I20's ten checks, by what its Lean form will look like:**

| I20 check | predicted Lean form |
|---|---|
| ① `L_ξ g = 2(a′/a) g` | a non-trivial identity about `deriv`, proved — **the one check that carries content** |
| ② not exact Killing | a statement needing a witness: `∃ a, deriv a ≠ 0` at a point — **trivial once a witness is given** |
| ③ `ξ·p = −C` constant | `deriv (fun η ↦ −(a η)² · (C / (a η)²)) = 0` under `a ≠ 0` — **true by `field_simp`, because the input is the conclusion** |
| ④–⑤ `ω = C/a`, `a·ω = C` | the same shape — **definitional** |
| ⑥ `1 + z = a_obs/a_em` | `(C/a_e)/(C/a_o) = a_o/a_e` — **`field_simp`** |
| ⑦ `ln(1+z) = ∫H dt` | **`Real.log_div`, with `H` appearing nowhere in the statement — visibly so** |
| ⑧–⑩ the massive control | a computation needing a concrete witness for the non-vanishing — **the claim is true, and the Lean form forces the witness the receipt's `!= 0` never supplied** |

| quantity | central | band |
|---|---|---|
| of the ten, statements whose proof is `rfl`, `field_simp`/`ring` on the asserted input, or a single library lemma | **6** | 4–8 |
| of the ten, statements that need a witness the receipt never supplied | **3** | 2–4 |
| of the ten, statements that carry geometric content as computed | **1** | 1–2 |

⛔ **The reachable negative, as the order states it.** *If ① cannot be written as a statement about functions
without also writing the Lie derivative of a metric, then the identity cannot be separated from the theorem.
In that case the 82 per cent is not a gap between two claims but one claim stated loosely.* **My prediction:
it separates (0.8).** ① is a statement about `deriv` of the components, and the formula that makes those
components a Lie derivative is exactly the missing layer 2, written as a comment. If it does not separate, I
say so and the finding narrows.

## ③ The one measurement before the `sinh^{2/3}` offer

*Question, as ordered: does Physlib's `FirstOrderFriedmann` stand on a non-stub base, or would stating the law
against it mean building the `FLRW` type first?*

- **Prediction: non-stub (0.75).** I expect `FirstOrderFriedmann` to be a `Prop` on functions `Time → ℝ` and
  constants. It would then be independent of `def FLRW : Type := sorry`, so the law is statable against it as
  it stands.
- **The measurement:** read its definition and every name it depends on, back to `mathlib` or to a `sorry`.
  If any dependency reaches `sorry`, the answer is "stub", and the offer is a foundations project wearing a
  one-result disguise.

*The scope of ③ is the definition and its dependencies only: nothing is stated against it this cycle, because
the offer is not ordered.*
