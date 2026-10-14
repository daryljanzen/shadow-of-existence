# `r7333+70.1` — PRE-REGISTRATION: the second seat's eight instances, priced one by one against 71's band (`60`–`170`, mean `90.3`), each failable, with its decisive fraction. ⌗ Row 13 carries a recipe extension that the interface does not have, and is priced and stopped separately

*Orders: `FOR_70.md` §`r7333` ①, read at `origin/main` `53b0944d`. This is written before any Lean.*

**What I have read:**
- `SEAT_BRIEF.md`, `ROWS.tsv` and the row-45 pilot (`Inst_R45`, as a template);
- E4 (`gowdy_ds_field`), as the Einstein pattern that needs no table;
- the STATEMENTS of `curvD_eq`, `lcGam_diag4`, `gamD`, `DGD`, `curvD`, `einsteinC`, `ricC`, `scalC`, `cS`,
  `co_d1`, `co_d2`, `pr_d1` and `pr_d2`.

**What I have not read:** the proof body of any `ShadowEngine` lemma, and I will not read one.

**Each row's claim** is taken from its receipt and quoted at the instance below.

## How a count is made

- **One instance = one `section`**, counted from its `/-!` header comment to its `end`. That is how 71's `149` for
  row 45 was counted.
- **A definition shared by several instances** (a metric family, its smoothness and its non-vanishing) is counted in
  the FIRST instance that uses it. The rows that reuse it are cheaper, and I say so instead of spreading the cost.
- **Files:**
  - `probes/SecondSeatFoliation.lean`: 47, 102, 94;
  - `probes/SecondSeatStatic.lean`: 48, 49, 51;
  - `probes/SecondSeatKS.lean`: 54;
  - `probes/SecondSeatLTB.lean`: 13.
- **Each file is built with `lake env lean`, and the run is filed raw**, with `#print axioms` for every theorem.
- **A row lands** only with no `sorry`, no error, and axioms within `[propext, Classical.choice, Quot.sound]`.

## The instances, in the order I will build them

| # | row | what is proved, under THE connection, with near-point profiles | central | own band | P(outside own band) at the central | P(outside 71's 60–170) at the central |
|---|---|---|---|---|---|---|
| 1 | **47** | static-spherical `(−F, 1/F, P, P·S)`, with `F > 0` at the point: the constant-`r` leaf's mixed extrinsic curvature is `diag(F′/(2√F), √F/r, √F/r)`, derived from `lcGam_diag4` (`K_ab = −Γʳ_ab n_r`) | **60** | 35–100 | 0.19 | 0.50 |
| 2 | **102** | for SdS-α `f = 1 − 2M/r − r²/α²`: trace-free parts `σ₁ + 2σ₂ = 0`, `σ₁ = 2(K₁ − K₂)/3`, and `K₁ − K₂ = f′/(2√f) − √f/r` in closed form; reuses 47 | **45** | 25–80 | 0.15 | 0.76 |
| 3 | **94** | the same leaf on SdS-α is umbilic (`K₁ = K₂`) **iff** `r = 3M`, via `2r√f·(K₁ − K₂) = r f′ − 2f = 6M/r − 2`; reuses 47 | **50** | 25–90 | 0.11 | 0.68 |
| 4 | **48** | `(−A, 1/F, P, P·S)` with `A` and `F` independent: `G^t_t = (rF′ + F − 1)/r²` (with no `A`) and `G^r_r = (rF A′/A + F − 1)/r²` | **120** | 80–170 | 0.35 | 0.23 |
| 5 | **49** | the `A = F` member: `G^t_t + Λ = (rf′ + f − 1)/r² + Λ`, `G^θ_θ + Λ = f″/2 + f′/r + Λ`, `G^t_t = G^r_r`; and with `f = 1 − 2m/r − Λr²/3`, `G^t_t + Λ = −2m′/r²` (density `m′/(4πr²)`; `m` constant gives vacuum) | **90** | 55–140 | 0.24 | 0.21 |
| 6 | **51** | with lapse `A` free and `f = 1 − 2m/r − Λr²/3`: `ρ = m′/(4πr²)` independent of `A`; and `G^r_r + Λ = 8πP` solved for `A′/A = 2(m + 4πr³P − Λr³/3)/(r²f)` (TOV); reuses 48 | **50** | 25–90 | 0.11 | 0.68 |
| 7 | **54** | Kantowski–Sachs `(−1, X(τ)², Y(τ)², Y(τ)² sin²θ)`, `X` and `Y` free: the three stress-energy combinations the receipt ASSUMES (`8πρ = −Λ + (Y′/Y)² + 1/Y² + 2X′Y′/(XY)`, and `p_χ`, `p_⊥`) are DERIVED as `G` components | **110** | 70–170 | 0.27 | 0.20 |
| 8 | **13** | LTB `(−1, R′²/(1+2E), R², R² sin²θ)` with `R(t,r)` a general TWO-variable profile: under the constraint `Ṙ² = 2m/R + 2E + ΛR²/3` and its `r`-derivative as hypotheses, `G_tt − Λ = 2m′/(R²R′)` | **220** | 150–300 | 0.39 | 0.74 |

⛔ **Row 13 has a stop: over `350`, it stays a reading,** and I route the reason.

- **The interface's `co_d`/`pr_d` cover only one-coordinate profiles and their products. `R(t,r)` is neither.** So
  row 13 needs a first and second `fderiv` recipe for `y ↦ h(y 0, y 1)`, which I would write rather than borrow.
- **I name that now as the driver I expect to cost the most.** It is not a proof body of 71's, so the rule against
  reading them is not touched. If writing it means opening one, I stop and route it as an interface defect, as ①
  orders.

## Failability and the decisive fraction (standing since `r7325`/`r7327`)

- **Every count is read exactly from the file, with no sampling.**
  - Uniformly over the outcome space every count decides something: under means the model over-prices, in means it
    holds, over means a driver is missing. As 71 registered it, ***no value leaves the question undecided***.
- **Weighted at my own central.** A lognormal with σ = 0.4. **That σ is chosen, not fitted:** it is roughly the
  log-width of 71's band 60–170.
  - My own bands fail with probability **0.11 to 0.39** if my central is right (column 6).
  - **71's band fails with 0.20 to 0.76** (column 7). It is high for the three rows I price LOW because they reuse
    an earlier instance (102, 94, 51), and for row 13, which I price HIGH.
  - ⇒ **So 71's band can be refuted on my eight in both directions, and I expect it to be: four of the eight are
    priced outside it.**
- **What I predict for 71's band:** 4 of 8 inside it (102, 94 and 51 under it; 13 over it).
  - **Mean of the eight: 93**, against 71's mean of 90.3.
  - **Excluding the three reuse rows and row 13: mean 95.**

## My probabilities

| quantity | p |
|---|---|
| all seven of rows 47, 102, 94, 48, 49, 51, 54 land | 0.75 |
| row 13 lands under the stop | 0.5 |
| the interface suffices for the seven without opening a proof body | 0.85 |
| ≥ 5 of the 8 inside their own bands | 0.6 |
| `curvD_eq` plus the recipe close a component goal with `field_simp; try ring` as the brief says, on the first instance that tries it (48) | 0.6 |

## Not done

- No Kretschmann row (71's) is touched.
- No proof body of `ShadowEngine` is read.
- **π_d does not apply:** nothing here has a second reading.
- The applier machinery stays stopped.
