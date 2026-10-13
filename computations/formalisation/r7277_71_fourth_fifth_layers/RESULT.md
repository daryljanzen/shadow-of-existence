# `r7277+71.5` — RESULT: the negative against the gate's framing does NOT fire. I20's statement goes through to its end with the connection a hypothesis; its instance goes through with ONE explicit connection for ONE metric. ON-path THEORY `0`. The THEORY-probed fraction is `6 / 6`, with `11` never probed

*Read against `PREDICTION.md` in this directory, pushed at `r7277+71.1` before any search or probe. The
pre-registration is not revised. Landed in pieces:*
- *`+71.2` — R1–R2;*
- *`+71.3` — R3;*
- *`+71.4` — R4;*
- *this result.*

*Raw runs: `PROBE_RUN_R1_R2.txt`, `PROBE_RUN_R3.txt`, `PROBE_RUN_R4.txt`.*

## ⛔ The reachable negative — NOT FIRED

***B4 is stated and proved with the connection a hypothesis.*** `charge_hasDerivAt` says: along any geodesic
of ANY torsion-free, `g`-compatible `cov`, for a conformal Killing `ξ` with factor `σ` and a symmetric `g`,

    Q′(t) = σ(γ t) · g(γ̇, γ̇),        Q(t) = g(ξ, γ̇).

- **B5 (`charge_const`):** `Q` is constant along a null geodesic. *I20's "along every null geodesic".*
- **B6 (`charge_deriv_ne_zero`):** `Q′ ≠ 0` where `σ ≠ 0` and `γ̇` is not null. *I20's "and along no other".*
- ***The geodesic does not force existence into the statement:*** "geodesic of `cov`" is a hypothesis on `γ`,
  and `cov` is a hypothesis.
- ***So "the port is the price of existence and not of the identities" stands, on five layers.***

***And the instance needed one connection, not the theorem.*** *R3 builds `covConf a` as a `CovariantDerivative`
on `ℝ × ℝ` from the Christoffel form of `a(η)²(−dη² + dx²)`, and proves it torsion-free and compatible. R4 then
proves `a · ω` constant along every null geodesic of it, and `1 + z = a_obs / a_em`. **That is I20's statement
to its end, on its metric, with no existence theorem anywhere.***

## The count

| | central | band | **measured** |
|---|---|---|---|
| A present (of 4) | 4 | 3–4 | **4** ✔ |
| B present (of 12) | 0 | 0–1 | **0** ✔ |
| present / 16 | 25 % | 19–31 % | **4 / 16 = 25 %** ✔ |
| absent THEORY, all | 3 | 2–5 | **3** ✔ — *B7, B11, B12* |
| **absent THEORY, ON** | **1** | 0–2 | **0** ✔ — *below central: R3 built* |
| R1 builds | 0.95 | — | **yes** |
| R2 builds, ≤ 200 lines | 0.75 | — | **yes, 78** (+3 to the copied B7) |
| R3 builds, ≤ 250 lines | **0.4** | — | **yes, 208** |
| R4 builds, ≤ 80 lines | 0.7 | — | **yes, 65** |
| the negative fires | 0.15 | — | **NOT FIRED** |

### A — 4 of 4 present (ON: A1, A3, A4)

| # | path | place |
|---|---|---|
| A1 | ON | `mfderiv` (`vel`, one line over it) |
| A2 | OFF | `exists_isMIntegralCurveAt_of_contMDiffAt` — `IntegralCurve/ExistUnique.lean` l.66 |
| A3 | ON | `HasDerivAt.fun_mul`, `HasDerivAt.fun_sum`, `is_const_of_deriv_eq_zero` |
| A4 | ON | the layer-3 probes, in the tree since `r7273+71.5` — *present in this project, not in `mathlib`* |

### B — 0 of 12 present

*Searched: `grep -rliE "geodesic"` over `Mathlib/Geometry` gives one file, `Group/WordMetric.lean`, which is a
word-metric geodesic in a group and not `D/dt γ̇ = 0`. `grep -rliE "isNull|null cone"` gives zero hits.*

| # | path | class | how |
|---|---|---|---|
| **B1** | **ON** | **DEF — measured (R1)** | `IsGeodesicAt cov γ t := covDerivAlong cov γ (vel γ) t = 0` |
| **B2** | **ON** | **DEF — measured (R1)** | `IsNullAt` |
| **B3** | **ON** | **DEF — measured (R1)** | `charge` |
| **B4** | **ON** | **DEF — measured (R2)** | `charge_hasDerivAt`, from B5, B7, B8 of layer 3 plus the symmetry of `g` |
| **B5** | **ON** | **DEF — measured (R2)** | `charge_const` |
| **B6** | **ON** | **DEF — measured (R2)** | `charge_deriv_ne_zero` |
| B7 | OFF | **THEORY** | geodesic existence is an ODE on `TM` for the spray. It needs the connection's coefficients to be smooth, which `Basic.lean` defers ("We will prove in a later file"). |
| **B8** | **ON** | **DEF — measured (R3)** | `covConf`, `covConf_torsion`, `covConf_compatible` |
| **B9** | **ON** | **DEF — measured (R4)** | `a_omega_const` |
| **B10** | **ON** | **DEF — measured (R4)** | `one_plus_z` |
| B11 | OFF | **THEORY** | null geodesics in every null direction: follows from B7 |
| B12 | OFF | **THEORY** | affine reparametrisation needs a chain rule for `covDerivAlong` under reparametrisation. Not probed, so classed by the rule. |

**Absent: 12 — 9 DEF by measurement, 0 PORT, 3 THEORY, all 3 OFF the path.**

### What the probes hold, in terms

- **R2:** pointwise in `t`.
  - `g` symmetric and `C¹` (`hg`), `ξ` `C¹`, and `cov` torsion-free and compatible — all hypotheses.
  - The frame coefficients of `ξ ∘ γ` and of `γ̇` differentiable at `t` (`CoeffDiffAt`) — a hypothesis.
  - `charge_const` asks for all of these for every `t`, on all of `ℝ`.
- **R3:** `a` differentiable everywhere (for `covConf` to be one object) and nonzero where compatibility is
  used.
- **R4:** the hypotheses are on `γ` — differentiable, a null geodesic, with differentiable frame coefficients
  (`hvc`), and the same for `ξ ∘ γ` (`hξc`).
  - *`hξc` is a property of the constant field `∂_η` that could be discharged (its coefficients are constant).
    **It is carried as a hypothesis rather than proved, and it is said here.***
  - `ω = a · η̇` is the comoving frequency, `−g(u, γ̇)` for `u = ∂_η / a`, by definition.
- **No existence theorem** — of a connection, a geodesic or a null geodesic — **appears anywhere.**

### How it got built — the cost, said as what it was

*About fifteen elaboration rounds across R1–R4: three for R1–R2, about ten for R3, two for R4. Every one was
the coercion discipline, and one new instance of it is worth naming:*
- ***on `ℝ × ℝ`, `mathlib`'s `MDiffAt`/`CMDiffAt`/`T%` notation infers the PRODUCT model
  `𝓘(ℝ,ℝ).prod 𝓘(ℝ,ℝ)`, while a `CovariantDerivative 𝓘(ℝ, ℝ×ℝ) …` fixes `𝓘(ℝ, ℝ×ℝ)`.*** *Statements that
  have to meet must spell the model out. That is now written into R3 and R4 where it bites.*
- *`d%` is `mvfderiv`, and `mvfderiv_eq_fderiv` is the simp lemma that turns it into `fderiv`.*

***No round stopped on a missing lemma.***

## ② The THEORY-probed fraction — as ordered, with denominators

*The record is in the tree: four RESULTs and four PREDICTIONs.*

**(a) Strict — classed THEORY in a RESULT, later probed:** ***1 / 1 built.***
- `r7269`'s B6 (Killing ⇔ `∇X` skew), proved as `r7273`'s Q2.

**(b) Pre-registered — named as the expected THEORY in a PREDICTION, then probed:** ***5 / 5 built.***
- `r7269`'s B8, the I20 instance (P3);
- `r7273`'s along-curve cluster B6, B7, B8 (Q4, Q5);
- `r7277`'s B8, the explicit connection (R3).

*Counting the cluster as one item instead: 3 / 3.*

**(a) ∪ (b), distinct items: `6 / 6` built.**

**(c) The population — every item ever classed THEORY in a RESULT: `12`. Never probed: `11`.**

| layer | THEORY, never probed |
|---|---|
| 1 | B3 (index locally constant), B9 (volume density) |
| 2 | A5 (flow), B3 (flow form of `𝓛`), B7 (Killing subalgebra), B9 (flow isometries) |
| 3 | B9 (parallel transport), B10 (curvature tensor) |
| 4–5 | B7 (geodesic existence), B11 (null geodesics in every direction), B12 (reparametrisation) |

***What the fraction can and cannot say.***
- *`6 / 6` is not a rate of the population. The probed items were the ON-path ones, where the effort went,
  and the 11 unprobed are not like them.*
- ***Seven of the eleven share one missing foundation:***
  - *A5, B3 and B9 of layer 2;*
  - *B9 of layer 3;*
  - *B7, B11 and B12 here.*
  - *All are flows, transport or ODE existence on a manifold. All need smooth dependence on initial data, or
    smoothness of `∇`, which `mathlib` itself defers.*
  - *That cluster looks like real theory, and nothing here measured it.*
- ⇒ ***The data support "the 82 per cent is an upper bound on the obstruction". They do not support "an
  artefact of the classification":*** *every probed THEORY item went cheap, and the unprobed ones are
  concentrated in one identifiable gap. **Probing two or three of that cluster under a budget is what would
  decide it.***

## The order's other constraint

***The Levi-Civita port is not begun.*** *Nothing touches `LeviCivita.lean`, `Metric.lean` or the layer-1 probe.
R3 is a formula for one metric on a vector space, proved there.*
