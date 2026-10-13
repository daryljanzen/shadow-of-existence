# `r7311+71.3` — RESULT: A LANDS. `ContMDiffCovariantDerivative (lcConn …) ∞` is PROVED on the model space for every `C^∞` symmetric nondegenerate metric, in `163` lines plus one import, against `250` central and a stop at `600`. ⌗ It is not under `120`, so the symmetric negative does not fire. The `C²` packaging is UNNECESSARY: K1 applies to THE connection as it stands

*Read against `PREDICTION.md` in this directory, pushed at `r7311+71.1` before any `mathlib` file was read for this
order. The pre-registration is not revised. The code landed at `+71.2`; this is the result.*

*Run: `PROBE_RUN_A1_A4.txt`. The code is the `r7311` section of `lean/probes/CurvatureProbe.lean`, `SmoothLC`. All
`72` `#print axioms` lines in the file rest on `[propext, Classical.choice, Quot.sound]`. There is no `sorryAx`
anywhere.*

## ⛔ The rule, scored first

| outcome | measured | scored |
|---|---|---|
| A1–A4 build in `≤ 600` lines | **`163`** (+1 import line) | ***A LANDS*** |
| a smooth-`♭⁻¹` lemma absent from `mathlib`, costing `> 150` | **absent? no.** *`ContinuousLinearMap.IsInvertible.contDiffAt_map_inverse` is there* | does not fire |
| ⛭ symmetric negative: A in `< 120` lines | `163` | ***does not fire*** |

*`2 × 250 = 500` is reported beside: met.*

| piece | statement | lines | predicted (band) |
|---|---|---|---|
| **A1** | `ndOf`, `koszK`, `lcGam`, and **`lcConn_const`**: `lcConn (const b) x a = ♭⁻¹ K(x)(a, b)` | **68** | 110 (60–250) |
| **A2** | **`flat_isInvertible`** (nondegeneracy plus equal finrank gives an equivalence) and **`lcGam_smooth`** | **29** | 80 (30–250) — *one below the band* |
| **A3** | **`lcConn_contMDiffCov`**, and its instances **`pg_contMDiffCov`**, **`dg_contMDiffCov`**, **`diag4_contMDiffCov`** | **50** | 40 (20–100) |
| **A4** | **`pg_curv_smul_left`**: K1's `R(fX, Y)Z = f R(X, Y)Z` for THE PG connection, with no class hypothesis | **15** | 20 (10–60) |
| **total** | | ***163*** | 250 (120–600) |

| probability (pre-registered) | p | outcome |
|---|---|---|
| A lands `≤ 600` | 0.60 | **yes** |
| within `2×` central | 0.55 | **yes** |
| under `120` | 0.10 | **no** |
| smooth inverse present in `mathlib` | 0.75 | **yes** |
| A4: `C²` packaging unnecessary | 0.60 | **yes** |
| general manifold reached | 0.15 | **no** — *not attempted* |

***Again under the central estimate, as the port and the discharges were, and this time inside its band.*** *The saving is in A2, where I budgeted for a port and `mathlib` already carried the step.*

## What it holds, in terms

- **A1.**
  - On a model space `E`, any differentiable symmetric nondegenerate field `B` gives an `NDMetric` (`ndOf`).
  - THE connection's value on constant fields is `Γ(a, b) = ♭⁻¹ K(a, b)`, with
    `K(a, b)(v) = ½[(DB·a)(b,v) + (DB·b)(v,a) − (DB·v)(a,b)]`.
  - Proved by testing against `B x` and using `lcConn_apply`. No Christoffel symbol is written out.
- **A2.**
  - `♭ = B x` is a continuous linear equivalence. It is injective by nondegeneracy and surjective because
    `finrank E = finrank (E →L ℝ)`, and it becomes an equivalence by `ContinuousLinearEquiv.ofBijective`.
  - `x ↦ ♭⁻¹` is `C^∞` by `mathlib`'s inversion lemma.
  - `lcGam` is then `C^∞`, checked pointwise through `contDiff_clm_apply_iff`.
- **A3.**
  - K2's `contMDiffCov_model` turns that into `mathlib`'s class.
  - With `C^∞` profiles it holds on C2/C3's Painlevé–Gullstrand metric, on C4's interior chart and on C5's diagonal
    `ℝ⁴` family.
- **A4.**
  - `curv_smul_left` applies to `lcConn` of `pgMetric`, with the instance supplied by A3 and nothing assumed.
  - ***So `r7295`'s caveat 2 is discharged on the model space:*** *"the curvature of THE Levi-Civita connection is
    `C^∞`-linear" now carries no hypothesis there.*

## Beside the score, said and not rounded

1. ***The model space only.*** *Every metric this line has put in the tree is on a model space (`ℝ²`, `ℝ⁴`, `E`),
   so this covers all six discharges. On a general manifold the class is still a hypothesis. Bridging it is
   `mathlib`'s bundle smoothness API, which is not attempted and not owed.*
2. ***`C^∞` is now a hypothesis on the PROFILES.***
   - The six discharges asked only for differentiability (`hAd`, `hw`, …).
   - The instances ask for `ContDiff ℝ ∞` of `A`, `w`, `c`, `b`, `cᵢ`.
   - Every named profile in the six (`exp`, `wSdS`, `2 arctan eᵘ`'s coefficients, constants) is smooth. That is
     said here and not proved per profile.
3. ***A4 is one K1 lemma on one metric.*** *`curv_smul_middle` and `curv_smul_right` take the same instance and the
   same argument. They are not written out.*
4. ***The `NDMetric.mdiff` field is unchanged.*** *`ndOf` proves it from `Differentiable ℝ B`, so on the model space
   it is no longer an assumption either.*

## For B, which this result unblocks

*B, the discharge sweep, now prices each receipt against a base with no carried connection hypothesis on the model
space, which is the order the proposal asked for. **It is pre-registered when ordered, and not before.***

## The order's other constraints

- Nothing in the quote-pin stride.
- No change to L1/L2 or to the six discharges. Everything here sits beside them.
