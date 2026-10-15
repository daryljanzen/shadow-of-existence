# `r7351+71.6` — RESULT, stage B: the non-diagonal engine lands, and row 83 with it. ⌗ THE connection of the squashed `S⁵` has `R = 24 − 4t²` (at `y = 0`), the value the receipt quotes from O'Neill, now computed from a metric. ⌗ `467` lines against `350` (band 200–500, ⛔ stop `600`): in the band. ⌗ Compile time `239 s` against a registered `≈ 30` minutes, `7.6×` under: the registered multiplier `m = 4` was wrong by about `12×`. ⌗ Row 62 is not in this landing

*Scored against `PREDICTION.md` in this directory (pushed at `r7351+71.1`). It is not revised. Every new axiom line is
`[propext, Classical.choice, Quot.sound]`, with no `sorryAx` (`PROBE_RUN_STAGE_B.txt`). The engine file is not
touched: the new layer is in `probes/NonDiag.lean`.*

## ⛔ The stop, scored first

***Not fired.*** `467` lines in the file, under `600`.

## What was built

| piece | what it proves | lines |
|---|---|---|
| ***the non-diagonal layer*** (`section EngineG`) | see the list below | ***`200`*** |
| ***row 83*** (`section SquashedS5`) | see the list below | ***`234`***, of which `4` are generated literal tables |
| file header and `#print axioms` | | `33` |
| | ***stage B*** | ***`467`*** |

### The non-diagonal layer (`section EngineG`)

- `formG` is `Σᵢⱼ Gᵢⱼ(p) dxᵢdxⱼ` for any field of matrices on `ℝⁿ`.
- `lcGam_formG`: `lcGam = gamG`, `Γᵏ = Σ_l K_l·Gi_lk`, with the inverse `Gi` given ***only at the point***.
- `fderiv_lcGam_formG`: `∂_uΓ = Gi·(∂_uK − ∂_uG·Γ)`. It comes from differentiating `♭(Γ) = K`, so no derivative
  of the inverse is ever needed.
- `curvG_eq`: THE connection's curvature on constant fields is `curvG`.
- `gamG_right`: `Γ` is linear in its second slot.

### Row 83 (`section SquashedS5`)

- ***The metric.*** `GS` is the canonical variation of `S⁵ → ℂP²`, in a softmax chart:
  - `|zₐ|² = μₐ` with `μ = softmax(y₀, y₁, 0)`;
  - base `¼(Σμ dθ² − (Σμ dθ)²)`;
  - fibre `Σμ dφ² + (t² − 1)(Σμ dφ)²`.
- ***Its properties:*** `GS_nondeg` makes it positive definite on all of `ℝ⁵` for `t ≠ 0`, as an explicit sum of
  squares. `GiS_inv` checks the inverse at `y = 0`.
- ***The tables:*** `D1_tab` (125 cases), `D2_tab` (625), `Gam_tab` (125) and `Ric_tab` (25).
- ***`row83_squashed_S5`:*** `scalG (GiS t) (curv (lcConn …)) = 24 − 4t²`.

***Why the band held where campaign 5's port came in at the floor:*** the inverse metric is the one thing the
diagonal layers never needed.
- The lever was to require `G⁻¹` only at the point, as numbers, and to get `∂Γ` from `♭(Γ) = K`. Without it the
  layer would have needed `∂(G⁻¹)` as a field.
- The chart was the other half. In the obvious charts (angles, or `μ` directly) the metric is not smooth and
  nondegenerate on all of `ℝ⁵`, so a cutoff with positive-definiteness on a ball would have been owed.
- In natural parameters the base is the Fisher metric `diag μ − μμᵀ`, smooth and positive definite everywhere, so
  no cutoff is owed.

## Row 83, and the caveats beside the score

- ***What is proved:***
  - The metric is THE Levi-Civita one (`lcConn`, through `ndOf`), on the whole chart `ℝ⁵`, with
    nondegeneracy discharged globally (`GS_nondeg`).
  - At `y = 0` (`μ = (⅓, ⅓, ⅓)`) its scalar curvature, contracted with the inverse metric, is `24 − 4t²` for every
    `t ≠ 0`. At `t = 1` that is the round `S⁵`'s `20`.
- ***The receipt's referent:*** the receipt quotes `R_t = 24 − 4t²` from O'Neill's formula for a Riemannian
  submersion, and does not compute it from a metric (`r7341`). It is now computed from one, and it agrees.
- ***Open half, named:*** the value is proved at ONE point.
  - It is constant because the metric is `SU(3)`-homogeneous. That is not proved.
  - The sympy cross-check (not a proof) gives `24 − 4t²` at every point of the chart.
  - Census: `DONE (chartable half)`, with this named as the open half.
- ***The tables are generated:*** `D1L`, `D2L`, `GamL` and `RicL` are literals produced by sympy. Each entry is then
  CHECKED by Lean against the metric (`D1_tab`, `D2_tab`, `Gam_tab`, `Ric_tab`), so a wrong entry would not
  compile. They are four long lines in the line count, and that is said rather than hidden.

## Compile time (`r7351` ②: the table-size axis)

| | registered | measured |
|---|---|---|
| wall, one file | `0.73 s × 625 × 4 ≈ 30` min | ***`239 s`*** |
| table cases | `625` | `950` (`125 + 625 + 125 + 25`, plus `25` for the inverse and `25` for symmetry) |
| per case | `0.73 s × m`, with `m = 4` | ***`≈ 0.25 s`***, so `m ≈ 0.34` |

***The registered multiplier was wrong, and in a direction the registration did not consider.***
- I priced the entries as carrying an inverse metric symbolically, hence `m = 4`. But a non-diagonal table AT A
  NUMERIC POINT has entries that are rational numbers, or polynomials in `t` alone.
- So the cost per case fell below the diagonal tables (whose entries carry free profiles and their derivatives),
  not above them.
- This is the per-case constant that `r7351` ① said grows with the entry, measured at the small end. Case count
  stays the axis, and the multiplier is the entry's expression size.
- *Settled at `r7351` ① and not reopened. `r7353` ⑤ asks for the sentence that retires the table-size question.
  It was written at `r7351+71.1` ①, and it stands.*

## The probabilities

| quantity | p | outcome |
|---|---|---|
| Stage B lands under its stop | `0.45` | ***yes***, `467` |
| row 83 is built from a metric | (registered as stage B's first instance) | ***yes, at a point*** |

## Row 62 is not in this landing

- It was priced at `0.4×` of 83, conditional on "the frame reduces to coordinates".
- Its object is a left-invariant FRAME on `S³` with a non-diagonal `exp(εH)`, expanded to `ε⁴` over jets, and its
  integrated seven are global on `S³` (`r7337`).
- `curvG` works in coordinates. Whether the frame reduces to them is the next question. Until then it stays
  `GENERIC-METRIC IDENTITY`.

## Census (moved in this push)

| status | after `r7351+71.4` | now |
|---|---|---|
| DONE | `43` | `43` |
| DONE (chartable half) | `11` | ***`12`*** (+ 83) |
| GENERIC-METRIC IDENTITY | `5` | ***`4`*** (6, 20, 58, 62) |
| real end | `20` | `20` |

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
