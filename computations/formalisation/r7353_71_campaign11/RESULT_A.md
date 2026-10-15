# `r7353+71.14` — RESULT: campaign 11 BUILT. ⌗ Row 58 is DONE. The Legendre transform is proved as a supremum on the positive kinetic form, and fails without it. The per-mode Euler–Lagrange equation `φ̈ + 3(ȧ/a)φ̇ + σ(μ²/a²)φ = 0` is proved, not read off. The derived sign gives `ω² = μ²/a² > 0` at every level, and the other sign `< 0`. ⌗ `120` lines against `100` (band 50–180, ⛔ stop `220`): in the band. ⌗ `13 s`, no table

*Scored against `PREDICTION.md` in this directory (pushed at `r7353+71.13`). It is not revised. Every axiom line is
`[propext, Classical.choice, Quot.sound]`, with no `sorryAx` (`PROBE_RUN_A.txt`). New file:
`probes/Legendre58.lean`.*

## ⛔ The stop, scored first

***Not fired.*** `120` lines, under `220`.

## What was built, against the four registered statements

| # | theorem | what it proves | registered |
|---|---|---|---|
| 1 | `row58_legendre`, `row58_hamiltonian` | for `α > 0`, `sup_v (pv − (α/2)v² − W) = p²/(2α) − W`, attained at `v = p/α` | ✔ |
| 1′ | `row58_legendre_needs_sign` | for `α < 0` the set is not bounded above: no transform | *added* |
| 2 | `row58_euler_lagrange` | `d/dt(∂L/∂φ̇) − ∂L/∂φ = (a³/4κ)(φ̈ + 3(ȧ/a)φ̇ + σ(μ²/a²)φ)` through `HasDerivAt` | ✔ |
| 2′ | `row58_euler_lagrange_iff`, `Lper_dv`, `Lper_dx` | the EL equation holds iff the bracket is `0`; the partials are the actual derivatives of `L` | ✔ |
| 3 | `row58_sign` | `μ² = m² − 1`, `m ≥ 2`: `σ = +1` gives `ω² > 0`, `σ = −1` gives `ω² < 0` | ✔ |
| 4 | `row58_measure_power` | `det(a²M) = (a³)² det M` for `3 × 3` | ✔ |

- ***`1′` is not in the registration.*** It is reported as an addition, not scored. It is where the receipt's phrase
  "positive kinetic term — the whole input the Legendre transform needs" becomes a theorem: with the opposite sign
  of `α` there is nothing to transform.
- ***The decisive step (2)*** came out with no convention left implicit:
  - the friction `3ȧ/a` is the derivative of the `a³` in the momentum;
  - the frequency's sign is `σ`, the sign the Legendre step put on the potential.

## Caveats beside the score

- ***Input, not derived:*** the per-mode coefficient `−μ²/4` is `r7034`'s second-order level sum divided by the
  degeneracy. The receipt uses it without re-deriving it, and so does this.
- ***Not built:*** the `a⁻²` from the curvature's dimension. That is the scalar curvature's scaling under a constant
  rescaling. It needs the engine, which probes cannot import. The `a³` from the measure is built (4).
- ***The truncation:*** `exp` is the receipt's `NORD = 3` truncation, through rows 58's earlier pieces
  (`r7353+71.2`, `+71.12`).
- ***The EL theorem's generality:*** it is stated for any velocity function `φd` with derivative `φdd`. The physical
  case `φd = φ′` is an instance. Nothing in the proof needs that, so it is not assumed.

## Compile time

| | registered | measured |
|---|---|---|
| wall | under a minute (no table) | ***`13 s`*** |

## The probabilities

| quantity | p | outcome |
|---|---|---|
| campaign 11 BUILT under its stop | `0.7` | ***yes***, `120` |

## Census (moved in this push)

Row 58: `DONE (chartable half)` → ***`DONE`***, with the three caveats above in its text, as registered. ***Counts,
checked before the commit:*** DONE ***`46`***, halves ***`11`***, generic-metric `2` (20, 62), library gap `17`,
no-connection `32`, real obstruction `3`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
