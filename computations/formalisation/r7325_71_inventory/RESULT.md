# `r7325+71.3` — RESULT: the row list is NOT nearly spent, because most of what the chart clause excluded was never really out of reach. Of the 29 chart-excluded rows and halves, 24 are POINTWISE claims on a 4D metric with a sphere factor. B's own near-point convention (already used in B1, B4–B10) plus E5 reaches them on the engine as it stands. ⛔ Five are not: two need the engine in another dimension, and three (65, 66, 67) are GLOBAL claims on `S³`, which are the real obstruction. ⌗ Next campaign: reopen the 24 behind one cutoff lemma, ≈ `2,900` lines. A second seat is worth seating for that, and for that only

*Scored against `PREDICTION.md` in this directory (pushed at `r7325+71.1`, before any file was re-read for this item).
It is not revised. The list is `ROWS.tsv` (`+71.2`), with all `111` rows and a status and a next step for each. A
census, so every band below is failable at its own size, as the registration said.*

## ① The census — `r7325` ②.1

| status | rows | |
|---|---|---|
| ***DONE*** | ***29*** | 24 whole; 5 by their chartable half (0, 2, 4, 5, 79) |
| ***ENGINE-REACHABLE now*** | ***3*** | 1, 3, 98: diagonal instances on the existing engine |
| ***CHART-EXCLUDED → REOPENABLE*** | ***18 rows + 6 halves*** | pointwise, 4D, a sphere factor: the near-point convention + E5 |
| NEEDS A DIMENSION CHANGE | 3 | 108 (`ℝ⁵`), 35 (general `D`), 83 (squashed `S⁵`) |
| GENERIC-METRIC IDENTITY | 6 | 7, 58, 20, 6, 19, 71: index algebra over an arbitrary metric, a separate item |
| NO-CONNECTION, NOT DONE | 32 | statable now; nothing to discharge, and plain analysis and algebra |
| ***REAL OBSTRUCTION*** | ***3*** | 65, 66, 67: global or spectral claims on `S³` |
| LIBRARY GAP | 17 | spectral 9, spinors 3, the LC volume form 4, `G/H` 1 |
| **total** | **111** | |

***No row left this list by looking unpromising.*** *Each one is done, or reachable by a named route, or stopped at a
named obstruction.*

## ② What the chart clause cost, and whether the obstruction is real — `r7325` ②.2

- ***Count:*** `20` whole rows and `6` halves among the connection-carrying rows, plus the `3` `S³` rows on the
  no-connection list. That makes ***`29` row-units***, against `27` registered (band 22–32).
- ***One cause: yes.*** Every one has a compact sphere factor in the metric or in its leaf: `S²` (SdS, LTB, TOV,
  Kantowski–Sachs, Nariai, `dS₂ × S²`, the constant-`r` foliations), `S³` (the closed slicing, its frame jets), `S⁵`
  (squashed), `S^{D−2}` (Tangherlini). ***The standard coordinates on a sphere degenerate somewhere, and the
  `CANDIDATES.md` clause demanded a profile that never vanishes on all of `ℝ⁴`.***
- ***Is the obstruction real? For 24 of 29, NO — and not even a library change is needed. That is the finding, and it
  is NOT what I registered.***
  - ***What I registered:*** a chart-free, pointwise formulation would reach them, so the gap is a LIBRARY gap: an
    `NDMetric` on an open set, the `r7315` port change.
  - ***What the files show:*** B already decided this question the other way, nine times. `B1`, `B4`–`B8`, `B10`,
    `B13` and `B14` take "metric profiles equal to the named one NEAR THE POINT, plus everywhere-nonvanishing and
    smooth". `B10` does it for SdS's `f`, which vanishes at both horizons.
  - A `sin²θ` that vanishes at the poles is the same situation as an `f` that vanishes at a horizon: one more profile
    with zeros away from the point.
  - What kept these rows out was the extra coordinate. An `S²` profile depends on `(r, θ)`, so the cheap separable
    recipe does not reach it. ***E5, built at `r7323`, removes exactly that.***
  - ***So the clause excluded what the convention plus a multi-coordinate recipe reaches.*** CANDIDATES was written
    at `r7315`, before E5 existed, and it applied the chart clause more strictly than B's own instances did.
- ***The five that are not reopened, and why:***
  - 35 and 83 are pointwise, but in dimension `D` and `5`. The engine is written over `Fin 4`. That is a dimension
    change, not a chart change.
  - ***65, 66, 67 are GLOBAL on `S³`:*** a TT-mode frequency shift, an integrated cubic vertex, and the TT spectrum with
    eigenvalue `6`. They need analysis on `S³` as a compact manifold: integration and a spectrum. ***That obstruction
    is real, and it is the library gap.***
- ***The convention's one caveat, carried since B:*** "whether such a global profile exists is not proved for each
  named metric". ***It can be proved ONCE.*** For a profile `f` smooth and nonzero near `p`, a bump `χ` (`mathlib`'s
  `ContDiffBump`) supported where `f ≠ 0` gives `χf + (1 − χ)·sign f(p)`. That is smooth, nowhere zero, and equal to
  `f` near `p`. One lemma, about `60`–`100` lines, closes the caveat for every row that uses the convention, B's
  included.

## ③ The Lean line's next campaign — `r7325` ②.3, my judgement

***The line is NOT approaching the end of what it can state.*** That end exists. It is the `17` library-gap rows plus
the `3` global `S³` rows: ***`20` of `111`, 18 %***, which need spectral theory, spinors, a volume form, `G/H`, or
analysis on a compact manifold. The rest is reachable now:

| campaign | rows | price | why this order |
|---|---|---|---|
| ***1. the cutoff lemma + one `S²` pilot*** (row 45, the SdS Kretschmann) | the gate for 24 | ≈ `80` + `≈ 150` | it proves the convention once and prices an `S²` instance before anything is promised |
| ***2. reopen the chart-excluded*** | 18 rows + 6 halves | ≈ `130` a row with two-coordinate profiles and a Kretschmann table; ≈ `60` for the three foliation rows; ≈ `90` a half → ***≈ `2,900`*** | the largest reachable block, and the engine's own work |
| 3. the three engine rows left | 1, 3, 98 | ≈ `90` each → `270` | cheap; they can ride with 2 |
| 4. the no-connection rows | 32 | unpriced; most look like real analysis at tens of lines | no engine needed, so a different seat's natural work |
| 5. the dimension change, `Fin n` | 108, 35, 83 | a port of the engine core, ≈ `150`–`250`, then instances | only after 2 |
| 6. generic-metric identities | 7, 58, 20, 6, 19, 71 | a separate item: index algebra over a non-diagonal `g` | not priced here |

*Against what I registered:* I expected to recommend the port change (p 0.6). ***I do not, because the files show it
is not needed.*** The convention reaches every row the port would reach, at no port cost, and the open-set
`NDMetric` buys nothing these pointwise rows need.

## ④ A second seat — `r7325` ②.4

***Worth seating for campaign 2, and for nothing smaller.***
- ***Why it pays:*** the 24 units are independent of each other. Each is one metric's values and partials pushed
  through a recipe that has now been priced four times. With a cutoff lemma and a pilot in place, the instance price
  is known to within the `60`–`170` band. At ≈ `2,900` lines, one seat takes several cycles, and two seats halve it
  with no coordination between rows.
- ***What it would need from me, before it starts:*** the cutoff lemma, the pilot (row 45) as a template, and the
  split. I would take the Kretschmann rows, which share the table pattern. The second seat would take the Einstein-
  tensor rows (13, 48, 49, 51, 54) and the three foliation rows.
- ***What it would cost me to support:***
  - the lemma and the pilot, ≈ `230` lines that are on the path anyway;
  - one practical change: the probe is a single file that takes `5½` minutes to build. A second seat should work in
    its own file. That means splitting `CurvatureProbe.lean` into an importable module, the engine and E5, plus
    instance files. *That is packaging, not mathematics, and I would price it at the start.*
- ***Not worth seating*** for campaigns 3–6. Rows 1, 3 and 98 are three instances. The no-connection rows need no
  engine and no template from me. The dimension port and the generic identities are single-author design work.

## The predictions, scored

| # | quantity | registered | measured | |
|---|---|---|---|---|
| L-1 | engine-reachable rows left | 8 (3–14) | ***3*** | in, at the bottom of the band |
| L-2 | chart-excluded row-units | 27 (22–32) | ***29*** (26 connection-carrying + 3 `S³`) | in |
| L-3 | library-gap rows | 17 (14–20) | ***17*** | exact |
| L-4 | no-connection rows not done | 30 (20–35) | ***35*** (32 + the 3 global `S³`) | in, at the top of the band |
| L-5 | one cause | yes (p 0.75) | ***yes*** — a compact sphere factor | as predicted |
| L-6 | a chart-free formulation reaches them; the gap is a library gap | yes (p 0.7) | ***partly wrong:*** 24 of 29 are reached WITHOUT any library change (the existing convention + E5); 3 are a real library gap; 2 need a dimension change | the kind is right, the mechanism is wrong |

| probability | p | outcome |
|---|---|---|
| I recommend the port change | 0.6 | ***no*** — it is not needed |
| I recommend a second seat | 0.35 | ***yes, for campaign 2 only*** |
| I report the line as approaching the end of what it can state | 0.3 | ***no*** — that end is 20 of 111 rows, and 91 are done or reachable |

## Beside the score

1. ***The reopening claim is a reading, not a build.*** No `S²` instance has been run. The pilot (row 45) is what
   tests it. If it fails, it will be on the profile's `θ`-dependence through E5, and I will say so.
2. ***`CANDIDATES.md` is not corrected here***, because the reopening is a proposal until the pilot lands. If it lands,
   its exclusions become "reopened by the convention" by an appended note, as before.
3. ***Row 3*** has a chartable half (Bianchi I shear sector) still open. It is counted ENGINE-REACHABLE, and its closed
   half is counted with the reopenable halves.
4. *Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
