# `r7277+71.1` — PRE-REGISTRATION: layers 4 and 5 — the null geodesic and the charge conserved along it — with the connection a hypothesis; and the THEORY-probed fraction

*Committed and pushed before any search and before any probe is written. The order is `FOR_71.md` §`r7277`.
Same instrument as `r7273+71.1`.*

***What I already know, and so cannot predict blind.*** *From `r7273+71.2`–`+71.5`:*
- *`vel`, `covDerivAlong`, `IsCompatible`;*
- *`lieDerivForm_eq_cov` (B4), `conformalKilling_cov` (B5), `covDerivAlong_comp` (B8) and
  `covDerivAlong_compat` (B7), all proved with the connection a hypothesis;*
- *`mathlib` has integral curves of a vector field but no geodesic, no parallel transport and no covariant
  derivative along a curve.*

## The path, fixed now

*`I20`'s statement, to its end: **"for a conformal Killing field `ξ` the charge `g(ξ, γ̇)` is conserved along
every null geodesic `γ` and along no other; on the null cone that charge is `a·ω`, so `1 + z = a_obs/a_em`."**
The derivative of the charge along any geodesic is `σ · g(γ̇, γ̇)`. Zero on null geodesics gives "every"; nonzero
where `σ ≠ 0` and `γ` is not null gives "no other". **An item is ON when that sentence, or its instance on
`a(η)²(−dη² + dx²)`, cannot be stated or proved without it.***

## The list, fixed now — sixteen items

| # | needed | path | what would count as PRESENT |
|---|---|---|---|
| A1 | velocity of a curve | ON | `mfderiv` (as `vel`) |
| A2 | existence of integral curves (ODE) on a manifold | OFF | `exists_isMIntegralCurveAt_of_contMDiffAt` |
| A3 | product and chain rules for real functions along `γ`, and "zero derivative on an interval ⇒ constant" | ON | `HasDerivAt.mul`, `is_const_of_deriv_eq_zero` or equivalent |
| A4 | the layer-3 probes B5, B7, B8 | ON | in the tree since `r7273+71.5` (not in `mathlib`) |
| B1 | `IsGeodesic cov γ`: `D/dt γ̇ = 0` | **ON** | a definition |
| B2 | `IsNull g γ`: `g(γ̇, γ̇) = 0` | **ON** | a definition |
| B3 | the charge `Q(t) = g(ξ(γ t), γ̇ t)` | **ON** | a definition |
| B4 | **the derivative of the charge: `Q′(t) = σ(γ t) · g(γ̇, γ̇)` along any geodesic, for any torsion-free compatible `cov`** | **ON** | a theorem |
| B5 | conservation: `Q` constant along a null geodesic on an interval | **ON** | a theorem |
| B6 | "and along no other": `Q′(t) ≠ 0` where `σ ≠ 0` and `g(γ̇,γ̇) ≠ 0` | **ON** | a corollary |
| B7 | geodesic existence through a point with a given velocity | OFF | a theorem |
| B8 | **a torsion-free connection compatible with `a(η)²(−dη² + dx²)` on `ℝ × ℝ`, constructed explicitly** (Christoffel symbols of a 2D conformally flat metric) | **ON** — *the instance needs one connection for this one metric, not the general existence* | a `CovariantDerivative` with both properties proved |
| B9 | the instance: `Q = −a·ω` on `ℝ × ℝ`, `ω` the comoving frequency, so `a·ω` is constant along a null geodesic | **ON** | a theorem |
| B10 | `1 + z = a_obs/a_em` from B9 | **ON** | a corollary |
| B11 | null geodesics exist in every null direction | OFF | a theorem |
| B12 | affine reparametrisation of geodesics | OFF | a theorem |

***ON: A1, A3, A4, B1–B6, B8, B9, B10 — twelve items.***

## The rule, unchanged

- **DEF:** a definition over PRESENT machinery, or a theorem proved by a probe within budget (DEF by
  measurement).
- **PORT:** proved in a neighbouring setting, transferred by replacing named ingredients.
- **THEORY:** neither.

## Probes, fixed now — `lean/probes/GeodesicProbe.lean` (R1–R2, R4) and `lean/probes/ConformalLCProbe.lean` (R3), imported by nothing

| probe | items | budget |
|---|---|---|
| R1 | B1, B2, B3 as definitions | — |
| R2 | B4, then B5 and B6, connection a hypothesis | **200 lines** |
| R3 | B8: Christoffel symbols of `a(η)²(−dη² + dx²)` as a `CovariantDerivative` on `ℝ × ℝ`, with torsion `0` and `IsCompatible` proved | **250 lines** |
| R4 | B9, B10 | 80 lines, given R2 and R3 |

*R2 copies the layer-3 definitions it needs, because probes are not a library. **The Levi-Civita port is not
begun.** R3 constructs one connection for one metric on a vector space, from a formula, and proves its two
properties there. It is not the general existence theorem, and it touches neither `LeviCivita.lean` nor
`Metric.lean`.*

## Predictions

| quantity | central | band |
|---|---|---|
| A present (of 4) | **4** | 3–4 |
| B present (of 12) | **0** | 0–1 |
| present / 16 | **4 / 16 = 25 %** | 19–31 % |
| absent THEORY, all | **3** | 2–5 — *B7, B11, and one of B8 or B12* |
| **absent THEORY, ON** | **1** | 0–2 — *B8, if R3 does not build within budget* |
| R1 builds | **0.95** | — |
| R2 builds in 200 lines | **0.75** | — |
| R3 builds in 250 lines | **0.4** — *a `CovariantDerivative` needs `add` and `leibniz` proved for a formula, then torsion and compatibility* | — |
| R4 builds, given R2 and R3 | **0.7** | — |

## ⛔ The reachable negative — the order's, against the gate's framing

***It fires iff B4 cannot be stated and proved with the connection a hypothesis*** — that is, iff the geodesic
forces existence into the statement rather than into a "the". *Then "the port is the price of existence and not
of the identities" is withdrawn, and the result says so in its first line.*
- **My probability that it fires: 0.15.** *B4 is one line on paper from B5, B7 and B8, all in the tree.*
- *B8 is scored in the ON-path THEORY count, not in this negative: an explicit connection for one metric is not
  the general existence theorem. **If R3 fails, the result names the lemma it stopped on, and it is ON-path
  THEORY.***

## ② The THEORY-probed fraction — definitions fixed now

*Over the three merged layers (`r7267+71.2`, `r7269+71.2`, `r7273+71.5`) and this one:*
- **(a) strict:** items a RESULT classed THEORY that a later probe proved, over items a RESULT classed THEORY
  that any probe attempted.
- **(b) pre-registered:** items a PREDICTION named as its expected THEORY and then probed, by whether the probe
  built.
- **(c) the population:** every item ever classed THEORY in a result, with how many were never probed.

*Reported as fractions with their denominators, as ordered. **No prediction:** it is a count of what the record
says, and the record is in the tree.*
