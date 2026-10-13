# `r7295+71.4` — RESULT: the PORT is WORTH IT, and it is DONE in its core — L1 (uniqueness, 75 lines) and L2 (existence, 213 lines) both build for a symmetric NONDEGENERATE metric of ANY signature, and no step needed positivity. `288` lines against a threshold of `200 × N ≈ 2600`. ⌗ But it discharges in FULL only receipt 42 so far, below the `6` I predicted: the port turns "a connection" into "THE connection", and each named metric must still be put in the tree to use it

*Read against `PREDICTION.md` in this directory, pushed at `r7295+71.1` before any `mathlib` file was read for this
order. The pre-registration is not revised. Landed in pieces:*
- *`+71.2` — L1, and its discharge on `covConf`;*
- *`+71.3` — L2;*
- *this result.*

*Run: `PROBE_RUN_L1_L2.txt`, which supersedes `PROBE_RUN_L1.txt`. The port is the `r7295` sections of
`lean/probes/CurvatureProbe.lean`. All `49` theorems in the file rest on `[propext, Classical.choice, Quot.sound]`.*

## ⛔ The negative — scored on the rule pushed at `+71.1`

| stage | statement | builds | lines | declarations | positivity needed? |
|---|---|---|---|---|---|
| **L1** (l.1081–1155) | `koszul`; **`lc_unique`**: two torsion-free connections compatible at `x` with a symmetric nondegenerate `g` agree at `x` on fields `C¹` there | **yes** | **75** | **3** | **no** |
| L1's discharge (l.1157–1252) | **`covConf_isLeviCivita`**: any torsion-free connection compatible with `a(η)²(−dη² + dx²)` at `p` IS `covConf a` there | **yes** | 96 *(incl. R3's 65 copied)* | 5 | no |
| **L2** (l.1254–1466) | **`lcConn M m`**, a `mathlib` `CovariantDerivative`: `lcConn_torsion`, `lcConn_compat`, and with L1, **`lcConn_unique`** | **yes** | **213** | **21** | **no** |

| rule row | measured | scored |
|---|---|---|
| L1 builds within `2×` its central budget (`≤ 300`) | 75 | ***L1 WORTH IT*** |
| L2: `P < 200 × N` | `P` = **288** *(L1 + L2, MEASURED: L2 finished)*; `N` ≈ **13** → threshold ≈ **2600** | ***L2 WORTH IT***, by a factor of about `9` |
| a step needs positivity with no nondegenerate replacement | **none** | — |

| quantity | predicted | **measured** |
|---|---|---|
| L1 builds in budget | 0.75 | **yes** |
| L1 lines | 150 (80–300) | **75** — *below the band* |
| L1 declarations | 8 (5–15) | **3** — *below the band* |
| L2 lines | 500 (250–1200) | **213** — *below the band* |
| L2 declarations | 35 (20–80) | **21** ✔ |
| `N`, distinct named metrics | 12 (6–25) | **≈ 13** ✔ *(by reading, ±2; method below)* |
| L2 worth it | 0.6 | **yes** |
| a step needs positivity | 0.35 | **no** |
| receipts L1 discharges | 6 (3–12) | ***1*** — *below the band* |

***Again a costed THEORY item went cheaper than I predicted: two of three line figures came in below their bands.***
*The re-costing at `r7273` was `≈ 51` declarations. The port came to `24` (L1 3 + L2 21), because three of its pieces
were REPLACED rather than ported — see the next section.*

## What was ported, what was replaced — against `r7273`'s `51`

| `r7273` piece | decl. | here |
|---|---|---|
| `LeviCivita.lean` core: Koszul, uniqueness, `leviCivitaAuxInner`, its two tensorialities, the dual, the connection, compatibility, torsion | 24 | **PORTED.** *`inner` → `g`; `inner_self_eq_zero` → nondegeneracy tested on `FiberBundle.extend` (`g_inj`); `real_inner_comm` → `NDMetric.symm`.* `24` → `24` *(3 + 21)* |
| `CovariantDerivative/Metric.lean` | 10 | **REPLACED** by `IsCompatAt`, R3's pointwise compatibility. *Not ported.* |
| `IsContMDiffRiemannianBundle` and the `inner_bundle` smoothness API | 14 | **REPLACED** by the field `NDMetric.mdiff`: `g(Y, Z)` is differentiable along differentiable fields. *A hypothesis on `g`, not a lemma.* |
| a metric-without-norm bundle class | 2 | **REPLACED** by `NDMetric`, a structure on `Π x, T_x →L T_x →L ℝ`. |
| a continuous `toDual` | 1 | **NOT NEEDED.** *`mathlib`'s `BilinForm.toDual` of a nondegenerate form, a `LinearEquiv`, composed and made continuous by `LinearMap.toContinuousLinearMap` (finite dimension).* |

***The pre-registration named `toDual` as where positivity would bite. It did not: finite dimension makes any linear
map continuous, and nondegeneracy makes `toDual` an equivalence.***

## What the port discharges — by the rule pushed at `+71.1`

*The rule: a statement is DISCHARGED when its "for a connection `cov` (hypothesis)" becomes "for the Levi-Civita
connection of `g`", for the metric it names, with no connection hypothesis left.*

- **L1, on the programme's 2D metric (`covConf_isLeviCivita`).** These are now theorems about `a(η)²(−dη² + dx²)`
  itself:
  - `curv_conf`, `scal_conf` (`R = 2 (log a)″/a²`);
  - `einstein_conf`;
  - `hessConf_eq`, `box_conf`;
  - `sff_conf`;
  - I20's `a·ω` constant along null geodesics. *That lives in its own probe file, on its own copy of `covConf`;
    the same uniqueness theorem applies there, but the import is not built.*
  - ***At receipt level: 1 — receipt 42 (I20).*** *No other reading in `READINGS.tsv` names the 2D conformal
    metric. The FRW receipts (2, 14, 72) are 4D. **I predicted `6`; it is `1`.** The instance theorems are many, and
    the receipts they stand in for are one.*
- **L2, in general form.** For any `NDMetric`, `lcConn` replaces the connection hypothesis in K1–K3, F1–F3, S2 and
  the geodesic layers.
  - ***In full, it discharges `0` more receipts this cycle.*** *A receipt is discharged in full only when its NAMED
    metric is in the tree as an `NDMetric`. None is yet, not even `covConf`'s: `gConf a` is nondegenerate only where
    `a ≠ 0`, and `NDMetric` asks for everywhere.*
  - *What remains per metric is no longer a connection — R3's `≈ 200` lines. It is an `NDMetric`: symmetric
    (one `ring`), nondegenerate, and `mdiff`. That is a few lines of `HasFDerivAt` products on a chart. Not built.*

***`N` ≈ 13, read from `READINGS.tsv` over the `97` statable:***
- *de Sitter (with its slicings and quadric);*
- *Schwarzschild–de Sitter;*
- *FRW (flat, closed, open);*
- *LTB;*
- *Nariai, `dS₂ × S²`;*
- *Tangherlini–de Sitter;*
- *the pp-wave / Brinkmann / plane wave;*
- *Gowdy–de Sitter;*
- *Kantowski–Sachs;*
- *the round `S³`;*
- *the squashed `S⁵`;*
- *a TOV interior;*
- *the 2D conformal metric.*

*Families, not charts. `±2` on how the generic "maximally symmetric" and "matter source" readings are counted.
**Any `N ≥ 2` passes the rule.***

## Beside the score, said and not rounded

1. ***`NDMetric.mdiff` is a hypothesis carried as a structure field.*** *`mathlib` derives the smoothness of
   `⟪Y, Z⟫` from `IsContMDiffRiemannianBundle`, about 16 declarations of bundle API. Here it is assumed of `g`. For a
   metric written on a chart it is a lemma per metric. ***The port moves the hypothesis from the connection to the
   metric. It does not remove it.***
2. ***The deferred smoothness is NOT discharged.*** *K1's curvature identities carry
   `[ContMDiffCovariantDerivative cov ∞]` (`r7287`). For `lcConn` that class is not proved. On a chart it would be
   K2's `contMDiffCov_model` applied to `lcConn`'s Christoffel form, which is not built. So **"the curvature of THE
   Levi-Civita connection is `C^∞`-linear" still carries that one class as a hypothesis**, while the connection
   itself does not.*
3. ***L1's uniqueness is on fields `C¹` at `x`.*** *`mathlib`'s needs only differentiable. That follows from
   stating compatibility in R3's `CMDiffAt 1` form, so that `covConf` discharges it unchanged. It is weaker than
   `mathlib`'s, and enough for every use here.*
4. ***Compatibility here is pointwise (`IsCompatAt`), not `mathlib`'s bundle-level `IsMetricCompatible`.*** *Bridging
   the two is the `Metric.lean` part, not ported.*
5. ***L1's discharge copies R3's torsion and compatibility proofs (65 lines)*** *from `ConformalLCProbe.lean` into
   this file, because probes import nothing. Counted in the discharge, not in L1.*

## The order's other constraints

- *No prefix in the quote-pin stride was taken.*
- *No named metric beyond `covConf`'s was stated.*
- *The `C²` tensorial packaging was not built.*
