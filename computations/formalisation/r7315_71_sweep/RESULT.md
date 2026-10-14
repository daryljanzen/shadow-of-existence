# `r7317+71.5` — RESULT: B DISCHARGES `17` RECEIPTS IN `1354` LINES, `≈ 80` A RECEIPT, AND THE CUMULATIVE RATE FALLS FROM `143` TO `96`. ⛔ THE REGISTERED STOP NEVER FIRED: NO CANDIDATE COST OVER `200`. B STOPS AT CANDIDATE `19` BY THIS SEAT'S DECISION, because what row 2 still needs is the `4D` engine `r7317` orders as its own pre-registered item. ⌗ My predicted stop, at candidate `10` on a new chart, was wrong: it landed at `119`

*Scored against `PREDICTION.md` and `CANDIDATES.md` in this directory. Both were pushed at `r7315+71.1` and `+71.2`,
before any `mathlib` file was read for B or any Lean was written. Neither is revised.*

*The code is the `r7315` sections `SweepB1`–`SweepB18` of `lean/probes/CurvatureProbe.lean`. Each candidate has its
own commit and its own `PROBE_RUN_B<k>.txt`. **Every `#print axioms` line in the file rests on
`[propext, Classical.choice, Quot.sound]`, and there is no `sorryAx` anywhere.***

***Unit: Lean lines that build, counted as `git diff --stat` insertions on that candidate's commit, blank lines
included, as at `r7295`, `r7297` and A.***

## ⛔ The stop rule, scored first

| outcome | measured |
|---|---|
| a candidate costs `cᵢ > 200` | ***never.*** *The largest is `B9` at `182`, against `180` predicted* |
| a candidate does not land within `2×` its prediction | ***never*** |
| all `37` candidates land at `≤ 200` each | ***no:*** *B stopped at candidate `19`, by decision (below)* |
| ⛭ symmetric negative: mean `cᵢ` over the landed is `< 60` | ***does not fire.*** *The mean is `1354/17 = 79.6`* |

***The decision, and why it is not the registered rule.***
- Candidate `19` is row 2: "`Weyl² = 0` on FRW, for `k = +1, 0, −1` and a free `a(t)`".
- **`k = 0` is done** (`frw_weyl`, `38` lines, `+71.4`).
- **`k = +1` is the closed `S³` slicing**, which fails the chart clause (see the misclassification below).
- **`k = −1` can be charted** with horospherical coordinates. Its coefficients then depend on two coordinates, and
  that needs THE connection's curvature for a diagonal metric whose coefficients depend on more than one coordinate.
  That is the `4D` engine.
- *`r7317` ② orders that engine as **its own pre-registered item**. Building it inside B to measure row 2 would mean
  pre-registering the engine after its cost is already known.*
- ⇒ ***I stop B here, so that the engine's pre-registration is blind.*** *If 66 would rather have row 2 measured
  inside B, the engine gets built under B's stop, and its pre-registration loses its blindness. That is one line to
  order.*

## The predictions

| quantity | predicted | measured | |
|---|---|---|---|
| candidate count | 25 (12–45) | **37** | in band, high (already scored at `+71.2`) |
| stop at candidate | **10** (row 44, a new chart, `250`) | ***not by rule*** — `B10` landed at **`119`** | ***wrong*** |
| Σ cᵢ, candidates 1–9 | 890 | **566** | low |
| cumulative rate at the stop | `(857 + 890)/15 ≈ 116` | ***`(857 + 1354)/23 ≈ 96.1`*** over 17 discharges | low, and falling |
| p(reach the last candidate) | 0.35 | *not reached; stopped by decision* | — |
| p(stop on a degenerate-chart metric) | 0.6 | ***half right:*** *the chart clause did bite, as a misclassification of `S³` halves (below), not as a cost* | — |

| # | row | lines | predicted | | # | row | lines | predicted |
|---|---|---|---|---|---|---|---|---|
| 1 | 99 | 41 | 50 | | 10 | 44 | 119 | 250 |
| 2 | 109 | 30 | 60 | | 11 | 78 | 173 | 220 |
| 3 | 11 | 32 | 70 | | 12 | 55 | 79 | 300 |
| 4 | 34 | 143 | 140 | | 13 | 8 | 142 | 250 |
| 5 | 36 | 57 | 60 | | 14 | 76 | 49 | 250 |
| 6 | 103 | 20 | 120 | | 15 | 22 | 134 | 300 |
| 7 | 32 | 39 | 150 | | 16 | 0 | ***0*** (see below) | 300 |
| 8 | 38 | 22 | 60 | | 17 | 4 (chartable half) | 78 | 300 |
| 9 | 56 | 182 | 180 | | 18 | 5 (chartable half) | 14 | 300 |
| | | | | | 19 | 2 (k = 0 of three cases) | 38, ***not landed*** | 350 |

***Measured `1354` over the 17 landed, against `3,060` predicted for the same 17.*** *The rate FELL along the
sweep, as `r7317` ruled at candidate 8, and for the reason it gave: **each candidate builds something the next one
reads.***
- `B4` → `B5`–`B8`;
- `B11` → `B12`;
- `B13` → `B14`;
- `B15` → `B16`, `B17`, `B18`.

## ⛭ What B built that a later order can reuse — five engines, inside B and paid for there

| engine | what it gives, for THE Levi-Civita connection | built in |
|---|---|---|
| `diagF` / `diag_curv` | `g(R(∂_r,∂_φ)∂_φ,∂_r)` for any `e(r)dr² + h(r)dφ²` | `B4` |
| `diag3F` / `lcGam_diag3` | Christoffel form, any diagonal `ℝ³` metric depending on `r` | `B10` |
| `ppF` / `lcGam_pp` / `pp_ricci` / `pp_riemann` | the pp-wave for ANY `H(u,x,y)`: Christoffel, Ricci, Riemann in closed form | `B11`, `B12` |
| `lcGam_diag4` / `boxD` | Christoffel form for ANY diagonal `ℝ⁴` metric; `□` as the trace of the Hessian | `B13` |
| `curv_T` / `ricC` / `scalC` / `ric2C` / `riem2C` | the curvature of `Σ qᵢ(t) dxᵢ²` in closed form, and its contractions | `B15` |

*Plus one general lemma: `killing_lie` (`B9`), the Killing operator on a model space as `ξ(g) + g(Dξ·,·) + g(·,Dξ·)`.*

## ⛔ A misclassification in `CANDIDATES.md`, found during the run and reported here, not corrected there

***Rows 0, 4, 5 and 2 (and 3 and 72, still unattempted) each name P10's CLOSED synchronous slicing
`a = α cosh(T/α)` on `S³`, beside a chartable object.***
- The `S³` half fails the candidate rule's chart clause, exactly like the `16` rows `CANDIDATES.md` excluded. I
  classified these rows by their chartable half and missed it.
- **Row 0:** its chartable half, the maximally symmetric invariants in `D = 4`, is `B15`'s result. It adds **0**
  lines and is not counted as a discharge. The `S³` slicing half is chart-excluded.
- **Rows 4 and 5:** the chartable half is P15's flat layer (`B16`, `B17`); the `S³` half is excluded.
- **Row 2:** `k = +1` is excluded; `k = 0` is done; `k = −1` waits on the engine.
- *Corrected count: the chart-excluded group is `16` plus these halves. No row is wholly moved.*

## Not discharged — 18 candidates, each "statable, connection carried as a hypothesis"

| needs | rows |
|---|---|
| the `4D` engine (coefficients in more than one coordinate, or non-diagonal) | 2 (`k = −1`), 74, 75, 79, 47, 102, 94, 52 |
| the engine, plus the closed `S³` half excluded | 3, 72 |
| `B15`'s engine as it stands (time-only diagonal) | 1 (Bianchi I shear), 98 (de Sitter's Einstein condition) |
| a generic metric: index algebra, not a computation | 7, 58, 20, 6, 19, 71 |
| `ℝ⁵` | 108 |

*Rows 1 and 98 look cheap on `B15`'s engine. They come after row 2 in the cheapest-first order, so they are left
for the engine item rather than taken out of order.*

## Beside the score, said and not rounded

1. ***Profiles equal near a point.*** `B1` and `B4`–`B8` (and `B10`, `B13`, `B14`) take metric profiles equal to the
   named one near the point, plus everywhere-nonvanishing and smooth. ***Whether such a global profile exists is not
   proved for each named metric.*** *I expect a cut-off construction to give one in every case; that is an expectation, not a proof.*
2. ***`B10` takes the Lyapunov exponent in the receipt's form***, `λ² = −(r²f/2)(f/r²)″`. The radial geodesic equation
   `r̈ = −(L²/2)(f/r²)′` is THE connection's. The linearisation and the change to coordinate time are not derived.
3. ***`B13` shows the mode solves the scalar `□` of the connection.*** It does not derive the reduction of the TT
   tensor equation to that scalar.
4. ***`B9` does not prove that the Killing algebra is exactly five-dimensional.*** That would need the dimension of
   the solution space of `f̈ = Af`.
5. ***`B12`'s VSI is the Kretschmann contraction only.*** "Every polynomial invariant vanishes" is not proved.
6. ***`B15` and the contractions use a diagonal `g`.*** `riem2C` and `ric2C` are the raised contractions for a
   diagonal metric, not general definitions.
7. ***Counting:*** `B16`'s commit also carries `frw_scal`, which `B18` reuses. It is counted once, in `B16`.

## What this did NOT do

- Nothing in the quote-pin stride.
- No change to L1/L2, A, or the six earlier discharges. Everything sits beside them.
- The engine is not built. It is proposed and pre-registered in `../r7317_71_engine/PREDICTION.md`, per `r7317` ②.
