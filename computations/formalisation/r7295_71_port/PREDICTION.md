# `r7295+71.1` — PRE-REGISTRATION: the Levi-Civita PORT begun — in two stages (uniqueness by the Koszul formula, then existence), with costs in lines and declarations, what each stage discharges first, and the symmetric negative: when the port is reported as not worth its cost

*Committed and pushed before any `mathlib` file is read for this order. The order is `FOR_71.md` §`r7295`.*

***What I already know, and so cannot predict blind.***
- *From `r7273+71.5` ②, a costing by reading at that revision: `≈ 51` declarations.*
  - *`LeviCivita.lean`: 24.*
  - *`CovariantDerivative/Metric.lean`: 10.*
  - *Bundle-level smoothness API in `VectorBundle/Riemannian.lean`: 14.*
  - *A metric-without-norm bundle class: 2.*
  - *A continuous `toDual`: 1.*
  - *All of it lives in a `RiemannianBundle` context, an inner product on each fibre, so **positive definite**.*
- *The tree as of `r7293`:*
  - *every layer from 2 to 5 takes the connection as a HYPOTHESIS;*
  - *`covConf a` is the one explicit connection, torsion-free and compatible with `a(η)²(−dη² + dx²)` (R3, `r7277`);*
  - *K3's `toDual`/`dualBasis` over a fibre, for a nondegenerate `BilinForm`;*
  - *S2 uses `torsion_eq_zero_iff`.*
- *I have not read `LeviCivita.lean` or `Metric.lean` since `r7273`, and I read nothing of `mathlib` for this order
  before this file is pushed.*

## What "the port" is, fixed now

*The corpus's metrics are Lorentzian. `mathlib`'s Levi-Civita theorem is for an inner product. So the port is
**the Levi-Civita theorem for a smooth, symmetric, NONDEGENERATE field of bilinear forms `g` on `TM`, of any
signature**: a torsion-free covariant derivative compatible with `g` exists and is unique. "Port" means adapting
`mathlib`'s proof where its steps survive the loss of positivity, and writing new steps where they do not. Both
are counted, separately.*

## Two stages — because uniqueness alone already discharges something

| stage | statement | why first | cost: lines (central, band) | declarations |
|---|---|---|---|---|
| **L1 — uniqueness** | two torsion-free covariant derivatives on `TM`, both compatible with a nondegenerate `g`, agree: the **Koszul formula** determines `g(∇_X Y, Z)`, and nondegeneracy gives `∇_X Y` | It needs no existence. With R3, it makes `covConf a` ***THE*** Levi-Civita connection of `a(η)²(−dη² + dx²)` | **150** (80–300) | **8** (5–15) |
| **L2 — existence** | for smooth nondegenerate symmetric `g`: define `∇_X Y` at `x` as the `g`-dual of the Koszul form, and prove it is a `CovariantDerivative` (additive, Leibniz), torsion-free and `g`-compatible | It is what "the geodesics of `g`" needs for a metric with no explicit Christoffel form in the tree | **500** (250–1200) | **35** (20–80) |

*Scope of this cycle: **L1 to a result, and L2 begun**, landed in pieces. L2 may well not finish this cycle. If
it does not, the result says where it stands, by declaration and by line.*

## What the port discharges first — fixed now, by a rule

*A statement is DISCHARGED when its "for a connection `cov` (hypothesis)" becomes "for the Levi-Civita connection
of `g`", for the metric `g` it names, with no connection hypothesis left.*

- **L1 discharges, as soon as it builds** (with R3's compatibility of `covConf`, `r7277`), for the programme's 2D
  metric `a(η)²(−dη² + dx²)`:
  - `curv_conf`, `scal_conf` (K4: `R = 2 (log a)″/a²`);
  - `einstein_conf` (F1);
  - `hessConf_eq`, `box_conf` (F2);
  - `sff_conf` (S3);
  - and I20's instance (`r7277`: `a·ω` constant along null geodesics).
  - ***These are "of `covConf`" today, and become "of the metric".***
- **L2 discharges** the general statements K1–K3, F1–F3, S2 and the geodesic layers, for any smooth
  nondegenerate `g`. ***These are the `97` in general form.***
  - *A receipt is discharged in full only when its NAMED metric is also in the tree as a smooth nondegenerate
    field. For metrics other than `covConf`'s, that is per metric, and it is not this order.*
- ***The receipt-level count is read in the result, by this rule, from `r7285`'s `READINGS.tsv`:*** *the number
  of the `97` whose stand-in names the programme's 2D conformal metric (discharged by L1), and the number that
  need L2. **My prediction: L1 discharges `6` receipts (band 3–12); L2 is needed by the other `91`.***

## ⛔ The negative — symmetric, fixed now: when the port is reported as NOT worth its cost

*The alternative to the port is the R3 pattern: one explicit Christoffel form per named metric, with its
torsion-freeness and compatibility proved by hand. R3 cost about `200` lines for one 2D metric.*

| outcome | scored |
|---|---|
| **L1 builds within `2×` its central budget (`≤ 300` lines)** | L1 is **WORTH IT**: one theorem turns every `covConf` instance into a statement about the metric |
| **L1 does not build within `300` lines, or stops on a lemma that needs positivity** | ***the port is NOT worth its cost at L1***, named by the lemma. *Uniqueness is the cheapest piece, and if it fails, existence will too.* |
| **L2: its projected total `P` lines stays below `200 × N`**, `N` the number of DISTINCT named metrics across the `97` (counted in the result from `READINGS.tsv`) | L2 is **WORTH IT** against per-metric explicit forms |
| **L2: `P ≥ 200 × N`, or a step needs positivity with no nondegenerate replacement** | ***L2 is NOT worth its cost***: ship L1, and state the named metrics by explicit Christoffel forms instead. *Reported as the fourth instrument built, measured and not shipped.* |

- *`P` is measured if L2 finishes, or projected from the declarations done and the declarations left, at the
  measured lines per declaration, if it does not. The result says which.*
- ***My predictions:***
  - *L1 builds within budget: **0.75**;*
  - *`N` = **12** (band 6–25), so the threshold is about `2400` lines;*
  - *L2 is worth it: **0.6**;*
  - *some step of `mathlib`'s proof needs positivity in an essential way: **0.35**. I expect the norm and continuity
    API to be the place: `toDual` for a form that is not an inner product.*

## What this order does NOT do

- *It does not take a prefix in the quote-pin stride.*
- *It does not state any named metric beyond `covConf`'s.*
- *It does not build the `C²` tensorial packaging. That is the other piece of WORK named at `r7293`, and it is not
  this order.*
