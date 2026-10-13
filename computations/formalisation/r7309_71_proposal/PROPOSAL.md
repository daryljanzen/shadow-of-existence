# `r7309+71.1` — PROPOSAL: the formalisation line, in two items. A: the smoothness class on THE connection, the one hypothesis the port still carries. B: a discharge sweep over every statable receipt that carries a connection hypothesis, run at the marginal-rate rule that `r7297` already tested. ⛔ Not proposed: any of the four library absences. Each is a mathlib-scale build for at most nine receipts

*This answers `FOR_71.md` §`r7309`, and `r7303`'s standing ask. It is a proposal, so nothing is built and no `mathlib`
file has been read for it. If an item is ordered, it gets its own pre-registration, pushed before any `mathlib` file
is read. The figures below are that pre-registration's starting point, and they will not be revised after reading.*

***Unit: lines of Lean that build, counted as at `r7295`/`r7297`.*** *Axioms are quoted. PROVED means
`[propext, Classical.choice, Quot.sound]`.*

## Where the line stands, in its own numbers

| | measured |
|---|---|
| the port, L1 + L2 | `288` lines; `lcConn` exists, is unique, and is torsion-free and compatible, for any nondegenerate `g` |
| discharges in full | `6` receipts: 42, 43, 92, 41, 29, 77 |
| marginal cost per discharge | `66`–`166`, against the hand route's `≈ 200` |
| cumulative cost | `857 / 6 ≈ 143` lines per discharge |
| statable, of `111` | `97` |
| unstatable | `14`: spectral `9`, spin `3`, volume form `1`, `G/H` `1` |

*What `lcConn` still carries is the one hypothesis named in `r7295`'s caveat 2. K1's curvature identities ask for
`[ContMDiffCovariantDerivative cov ∞]`, and for `lcConn` that class is not proved. So "the curvature of THE
Levi-Civita connection is `C^∞`-linear" is still stated under a hypothesis, while the connection itself is not.*

## A — the smoothness class on `lcConn`. Proposed FIRST

- **What it is:** for an `NDMetric` whose `g` is `C^∞`, `lcConn` is `C^∞`. In this tree that means
  `ContMDiffCovariantDerivative (lcConn M m) ∞`, on a model-space chart first and through `mathlib`'s bundle API
  if that is in reach.
- **What it buys:** K1–K3 and F1–F3 apply to `lcConn` with no class left to assume. The `97` then rest on no
  carried hypothesis about the connection.
  - *My prediction: this also makes the "`C²` tensorial packaging" named at `r7293` unnecessary for every receipt
    in the tree. The `C^∞` statements already built would apply as they stand.*
  - *That prediction is scored in A's result.*
- **Cost:** **`250` lines** (band 120–600).
  - Route: on a chart, `lcConn`'s Christoffel form is `g⁻¹` times first derivatives of `g`. That is smooth because
    matrix inversion is smooth on the invertible matrices, and K2's `contMDiffCov_model` already turns a smooth
    Christoffel form into the class.
- **Probability it lands within `2×` budget:** **0.55**.
- **⛔ Stop rule:** I stop and report A as not worth its cost if either of these happens:
  - it exceeds `600` lines;
  - a step needs a smoothness lemma for `BilinForm.toDual` that `mathlib` lacks and that would itself be a port of
    `r7295`'s size.
  - *Then the class stays a named hypothesis, and B runs under it, as the six discharges already do.*

## B — the discharge sweep. Proposed SECOND, and only after A's verdict

- **Candidates, by `r7297`'s rule, unchanged:** statable; the stand-in carries a connection hypothesis; the metric
  fits in one chart of a model space.
  - Counted FIRST from `READINGS.tsv`, before any cost is measured.
  - *My prediction: **`25`** more candidates (band 12–45). The rest of the `97` are first integrals, Lie-derivative
    statements, pure ODEs or topology, which have nothing to discharge.*
- **Order:** cheapest predicted first.
- **Cost:** about **`120` lines per discharge** (band 60–250), from `r7297`'s measured `66`–`166` and the same
  proof shape:
  - `NDMetric` on a chart;
  - `g_inj` against a test field;
  - `lcConn_apply`;
  - `ring` or `linear_combination`.
- **⛔ Stop rule: the one `r7297` registered and never fired.** Take candidates in order and STOP at the first one
  that does either of these:
  - costs more than `200` marginal lines, which is the hand route;
  - does not land within `2×` its central budget.
  - *From that point the port is no cheaper per receipt than building each connection by hand. **The remaining
    receipts are then reported as "statable, connection carried as a hypothesis", and not pursued.***
- **Cumulative check, reported beside every candidate:** `(857 + Σcᵢ)/(6 + k)`, against the `150` line `r7297`
  fixed.
- **Probability the sweep reaches its last candidate without the stop rule firing:** **0.35**.
  - *I expect the stop rule to fire on a metric with no globally nondegenerate chart, like `covConf`'s `gConf`
    where `a = 0`. There `NDMetric`'s everywhere-nondegeneracy would have to be weakened, and that is a change to
    the port, not a discharge.*

## ⛔ What I am NOT proposing, and why

| absence | receipts | why not |
|---|---|---|
| homogeneous space `G/H` as a manifold | 1 (receipt 80) | a smooth structure on a quotient by a closed subgroup is a `mathlib`-scale build. My estimate is over `2000` lines for one receipt, and that receipt has a statable hyperboloid stand-in (`r7293` caveat 1) |
| the volume form | 1 (receipt 46) | THEORY since `r7267` |
| spin geometry | 3 | Clifford bundles and spinor connections; absent in `mathlib` and `Physlib` |
| spectral theory, heat kernel | 9 | absent in both, and the largest of the four builds |

***On my numbers, each is worse than `200 × receipts` by an order of magnitude. That is the same comparison the
port was scored on (`200 × N` at `r7295`).*** *If an order wants one of them anyway, it gets its own pre-registration,
with that comparison as its negative.*

## The whole line, as one decision

| outcome | read |
|---|---|
| A lands, B runs to its last candidate under `200` each | the formalisation of the statable corpus is **done in its connection layer**. What is left is the four absences, which are reported and not built |
| A lands, B's stop rule fires at candidate `k` | `k` discharges, and a named metric class the port does not reach cheaply. Reported as that |
| A's stop rule fires | the smoothness class stays a hypothesis. B runs under it, and the result says so on every line |

*Both items are on `CurvatureProbe.lean`'s existing machinery. **Nothing in the quote-pin stride.***
