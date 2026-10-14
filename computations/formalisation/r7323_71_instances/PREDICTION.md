# `r7323+71.1` — PRE-REGISTRATION: the per-instance price, re-set from the two instances I measured (E3 `88`, E4 `137`) and not from the recipe. ⌗ Central `110` a row, band `60`–`170`; ⛔ stop on any one instance over `200`, or on two in a row over `170`. Six rows remain, taken cheapest first: 52, 79, 47, 102, 94, then 75 last, because it needs a two-variable recipe that is priced on its own

*Orders: `FOR_71.md` §`r7323` ③. Written after the engine's RESULT (`../r7317_71_engine/RESULT.md`) and before any
Lean for this item. **No receipt of the six rows has been opened.** Each row is known here only by its one-line
stand-in in `../r7285_71_restate/READINGS.tsv` and its row in `../r7315_71_sweep/CANDIDATES.md`. Unit: Lean lines that
build, as `git diff --stat` insertions, as in B and in the engine.*

## ① What the two measured instances spent their lines on

I read this off the probe file's sections `Engine4D_E3` and `Engine4D_E4`. Each line is counted in one bucket.

| bucket | E3 (open FRW, `Weyl² = 0`) | E4 (homogeneous Gowdy-dS, `G + Λg`) |
|---|---|---|
| setup: the profile definitions, smoothness, nonvanishing | ≈ 17 | ≈ 19, plus `exp_derivs` ≈ 13 |
| ***derivative facts: each coefficient's first and second derivatives*** | ***≈ 32, for 2 profiles (`a²`, `e^{2w}`)*** | ***≈ 58, for 3 profiles (`e^{2(γ−ψ)}` in both signs, `e^{2ψ}`, `R² e^{−2ψ}`)*** |
| component table (needed only for a full 256-term contraction) | ≈ 20 (`oR`, 24 entries, and its proof) | — |
| statement, recipe and closing | ≈ 19 | ≈ 37 (a two-part statement, and a `linear_combination` close) |
| a corollary (`Ċ₀`) | — | ≈ 10 |
| **total** | **88** | **137** |

***What drives the spread, named because it predicts the next instance:***
1. ***The number of distinct nontrivial coefficient profiles, and how deeply each one is composed.***
   - A plain power or exponential of one coordinate costs about `16` lines (E3).
   - A product or an exponent of a difference costs about `19`–`20` (E4's `R² e^{−2ψ}` is the dearest).
2. ***Whether the claim is a full contraction*** (`Riem²`, `Weyl²`, Gauss–Bonnet). That needs a component table, about
   `20` lines. A few named components (`G_tt`, `G_zz`, a trace) do not.
3. ***The shape of the statement.*** A single scalar identity closes with `field_simp; ring`. A pair of field equations
   with an exponential to cancel needs a stated `linear_combination`, about `+10`.

***The cost model, fitted to these two and to nothing else:***
`cost ≈ 20 (setup) + 17 × (profiles, +3 for each composite one) + 15 (statement) + 20 (if a full contraction) + 10 (if a
linear_combination close)`.
*It gives E3 ≈ `20 + 34 + 15 + 20` = `89` and E4 ≈ `20 + 13 + 60 + 15 + 10 + 10` = `128`. It is fitted, so it will
reproduce these two. The test is the next six.*

## ② The per-instance band and the stop rule — on the price of one row, not the total

| | value |
|---|---|
| ***central, per instance*** | ***`110`*** — the mean of the two, rounded down a little, because the remaining rows are mostly lighter (§③) |
| ***band, per instance*** | ***`60`–`170`*** |
| ⛔ ***STOP*** | ***any ONE instance over `200`, or TWO IN A ROW over `170`.*** Then I report the rows not taken, with what the overrun was spent on, and wait for an order |
| ⛭ symmetric negative | ***the first three instances each under `60`.*** Then the price was E3's and E4's metrics, not the recipe, and I say so |

*The stop is per instance, as `r7323` ③.2 asks, because a stop on the total cannot fire until the work is done, which B
showed. `200` is about `1.5 ×` the dearer measured instance. Two in a row over `170` would mean the model in ① is
missing a driver.*

## ③ The six rows, cheapest first, each with its prediction from the model

| order | row | stand-in (from `READINGS.tsv`) | what it should need | predicted |
|---|---|---|---|---|
| 1 | 52 | open slicing as a hyperboloid embedding, 3-curvature *(the closed case is excluded: `S³`)* | the open slice in the horospherical chart is `E3`'s `e^{2w}` profile with `a ≡ 1`; its curvature is read through the 4D engine on the static product. One profile, a scalar | **70** |
| 2 | 79 | `K_ab = 0` on the leaves, and the leaf scalar curvature | `K = 0` is Christoffel-level (`lcGam_diag4`, `∂_t g = 0`). The leaf curvature goes through Gauss with `K = 0`: `³R = R + 2 R_{ab} n^a n^b`, from `scalC`/`ricC`. One or two profiles | **90** |
| 3 | 47 | shear of a foliation from the extrinsic curvature | ***Christoffel-level only:*** `K_ij = −Γ^n_ij / √|g_nn|` on a coordinate leaf, then its trace-free part. No curvature at all | **60** |
| 4 | 102 | extrinsic-curvature shear, closed form | as 47, with a named sheared metric; two profiles | **80** |
| 5 | 94 | umbilic locus of a foliation | as 47: `K` proportional to the induced metric, solved for where it holds. Christoffel-level, with a locus to characterise | **90** |
| 6 | 75 | the Einstein tensor of the full `(t, z)` Gowdy-dS metric = the wave and constraint equations | ***needs the coefficients in TWO coordinates, which are not separable products.*** That is an engine extension, E5: a two-variable recipe (`dC1`/`dC2` facts for `c(p⁰, p¹)`, with mixed partials). Priced on its own, then the instance | **E5: `50`** (30–100) **+ instance: `170`** |
| | | | ***six instances*** | ***`560`*** (and E5 `50`) |

***Three registered risks, said before they happen:***
1. ***Rows 47, 102 and 94 may not need the 4D engine at all.*** The connection is enough for them, and that is
   `B13`'s `lcGam_diag4`. If so, they are reported as Christoffel instances, and that is the finding: three of the eight
   "engine rows" never needed curvature.
2. ***If a row's metric has an `S²` factor*** (47's "any static sphere" may be one), it fails `CANDIDATES.md`'s chart
   clause. It is then excluded and reported at cost `0`, as row 0 was, not built.
3. ***Row 75 carries the model's biggest uncertainty.*** Two-variable composite profiles (`e^{2(γ−ψ)}` with
   `γ = γ(t, z)`) bring mixed partials the model in ① has never seen. That is why it goes last, and why its stop is
   checked on the instance alone, with E5 counted separately.

## ④ My probabilities

| quantity | p |
|---|---|
| all six instances land without the stop firing | 0.55 |
| the per-instance mean lands inside `60`–`170` | 0.70 |
| at least one of 47, 102, 94 needs no curvature (Christoffel-level only) | 0.75 |
| at least one row is excluded on the chart clause | 0.35 |
| row 75 alone (E5 + instance) exceeds `200` | 0.45 |
| symmetric negative (the first three each under `60`) | 0.10 |

## Not done here, and kept off the path

- ***The `21` calibration keys stay off the critical path***, as `r7323` ③.3 and `70` have it.
- ***Anything `70` routes me from `cc66`'s frame I decline***, per `r7323` ③.4: a second seat reading those keys would
  make it a between-seat read.
- Nothing in the quote-pin stride.
