# `r7323+71.5` — RESULT: of the six remaining engine rows, THREE land and THREE are chart-excluded. The three that land average `90` lines an instance (`62`, `47`, `162`), inside the registered band (`60`–`170`), with E5 at `32` on top. ⛔ The per-instance stop never fired: the dearest row, 75, came in at `162` against a stop of `200`. ⌗ The miss is in the rows, not the price: I registered one exclusion as p `0.35`, and three of the six (47, 102, 94) turned out to be foliations of a static SPHERE

*Scored against `PREDICTION.md` in this directory (pushed at `r7323+71.1`, before any receipt of the six rows was
opened and before any Lean). It is not revised. The code is in the sections `Inst_R52`, `Inst_R79`,
`Engine4D_E5` and `Inst_R75` of `lean/probes/CurvatureProbe.lean`. **All `127` `#print axioms` lines rest on
`[propext, Classical.choice, Quot.sound]`, and there is no `sorryAx`.** Unit: `git diff --stat` insertions, one
commit per instance.*

## ⛔ The stop rule, scored first

| condition | measured |
|---|---|
| any ONE instance over `200` | ***no*** — the largest is row 75 at `162` |
| TWO IN A ROW over `170` | ***no*** |
| ⛭ symmetric negative: the first three instances each under `60` | ***no*** — `62`, `47`, `162` |

## The rows

| order | row | predicted | measured | |
|---|---|---|---|---|
| 1 | 52, the open leaf: `³R = −6/A²` in a horospherical chart, and the point on the hyperboloid | 70 | ***62*** | under; E3's setup was reused whole |
| 2 | 79, static ⇒ `K_ab = 0` on every `t`-leaf; flat FRW `K_ij = aȧ δ_ij`, `K = 3H` | 90 | ***47*** | under; Christoffel-level, no curvature needed |
| 3 | 47, foliation shear from `K` | 60 | ***excluded (0)*** | `S²` foliation |
| 4 | 102, extrinsic-curvature shear, closed form | 80 | ***excluded (0)*** | the same `S²` foliation |
| 5 | 94, umbilic locus | 90 | ***excluded (0)*** | the same `S²` foliation |
| 6 | 75, full `(t, z)` Gowdy-dS: `R_μν − Λg_μν` = the four Gowdy equations | E5 `50` + `170` | ***E5 `32` + `162` = `194`*** | both under; inside their bands |
| | ***the three that land*** | `330` registered for them, + E5 `50` | ***`271`*** + E5 `32` = ***`303`*** | under |

## The probabilities, registered and scored

| quantity | p | outcome |
|---|---|---|
| all six instances land without the stop firing | 0.55 | ***no*** — the stop never fired, but three rows are excluded |
| the per-instance mean lands inside `60`–`170` | 0.70 | ***yes*** — `90.3` |
| at least one of 47, 102, 94 needs no curvature | 0.75 | ***not tested*** — all three are excluded before any Lean |
| at least one row is excluded on the chart clause | 0.35 | ***yes — three*** |
| row 75 alone (E5 + instance) exceeds `200` | 0.45 | ***no*** — `194` |
| symmetric negative | 0.10 | ***no*** |

## ⌗ The cost model, tested on the rows it did not see

*The model was `20 (setup) + 17 × profiles (+3 if composite) + 15 (statement) + 20 (full contraction) + 10 (a
linear_combination close)`, fitted to E3 and E4.*

- ***Row 52*** — model `52`, measured `62`. Close. It reused E3's `FoF`, `GoF` and nonvanishing whole, which cut its
  setup to almost nothing; the hyperboloid lemma added about `10`.
- ***Row 79*** — no profile model applies. ***It needed no curvature at all.*** The static vanishing is one
  `simp` on `gamD`, and the FRW half reused `B15`'s `lcGam_T`. *That is the driver the model lacked: whether the claim
  is curvature or connection.*
- ***Row 75*** — model `20 + 4 × 20 + 25 + 10` ≈ `135` for the instance, measured `162`.
  - The extra is the two-variable bookkeeping. First partials have to be stated as `v⁰∂₀ + v¹∂₁` before the
    Christoffel vector can be expanded; the first build failed on exactly that.
  - Independence and symmetry facts for three functions came to about `20` more.
- ***So the model holds for curvature rows, given one more driver (+`25`–`30` per extra coordinate the profiles depend
  on). Connection rows are cheaper than any curvature row.***

## ⛔ Beside the score, said and not rounded

1. ***`CANDIDATES.md` had misclassified rows 47, 102 and 94 as `ℝ⁴`.***
   - Each receipt is about the constant-`r` foliation of a static spherically symmetric metric. The `S²` is in the
     object the claim is ABOUT, so no change of chart reaches it.
   - Row 79's SdS half is excluded the same way. Its static vanishing is proved instead for every chartable static
     diagonal metric, which contains every chartable member of that family.
   - The correction is appended to `CANDIDATES.md` at `r7323+71.3`. Candidates now number `33`.
   - *This is the second time an `ℝ⁴` label hid a sphere (the first was the `S³` halves at `r7319`). ***A stand-in
     cannot carry the chart clause; only the receipt can.***
2. ***Row 52 is stated in a different chart from its receipt.*** The receipt uses `sinh²χ dΩ²`, which is excluded. Lean
   states it in the horospherical chart, which is the same leaf. ***The induced-metric derivation from the 5D
   embedding is not formalised***; only membership on the hyperboloid is.
3. ***Row 75's statement is exactly the receipt's four checks***, with the factors as identities rather than as
   "derivative-free":
   - `R e^{2γ−4ψ} E_xx = WAVE`;
   - `e^{2γ} E_yy = −R(WAVE − AREA)`;
   - `E_tz = MOMENTUM/R`;
   - `E_tt + E_zz = ENERGY/R`.
   - `ψ, γ, R` are arbitrary smooth functions whose `x`- and `y`-partials vanish everywhere, which is the receipt's
     `(t, z)` dependence.
4. ***Build time.*** The probe builds in about `5½` minutes on a normal run. One run took `15`; that was the machine,
   and the next two were back at `5½`. *A scratch copy without E3/E4 built in under `2`, which is how row 75 was
   iterated.*

## ⌗ The engine route, as `r7317` ③ framed it, with what is now measured

| | lines |
|---|---|
| engine core (E1 + E2) | `134` |
| E3 row 2, E4 row 74 | `88` + `137` |
| E5 | `32` |
| rows 52, 79, 75 | `62` + `47` + `162` |
| ***all eight engine rows, as far as they can go*** | ***`662`*** — five rows landed, three excluded |

*Registered at `r7317`: engine-first `≈ 510`, separately `≈ 1,700`. Re-estimated at `r7319`: `≈ 1,030`. **The
measured route is `662` for the five rows that exist on `ℝ⁴`.** Three rows the estimates priced cannot be built on a
chart at all, so the `≈ 1,700` is not a comparable number for them.*

## Not done

- Rows 47, 102 and 94 wait on the port change named at `r7315` (an `NDMetric` on an open set, or a product with `S²` as
  a manifold). That is not ordered.
- The `21` calibration keys stay off the critical path. Nothing has been routed from `cc66`'s frame, so nothing was
  declined.
- Nothing in the quote-pin stride.
