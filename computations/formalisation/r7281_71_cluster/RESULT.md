# `r7281+71.5` — RESULT: the rule OVER-CLASSES — `3` of `4` build, so the bound moves down. Parallel transport and geodesic existence build on `E`; the flow's group law builds on a manifold. The flow `C¹` in its initial point does NOT build in `250` lines: it stopped on `flow_hasFDerivAt`, and smooth dependence stays THEORY

*Read against `PREDICTION.md` in this directory, pushed at `r7281+71.1` before any probe was written and before
any `mathlib` file was read for this order. The pre-registration is not revised. It has one flaw, found while
scoring and stated below with its fix. Landed in pieces:*
- *`+71.2` — T3a;*
- *`+71.3` — T2;*
- *`+71.4` — T1;*
- *this result, with T3b and T1's strengthened statement.*

*Raw runs: `PROBE_RUN_T3a.txt`, `PROBE_RUN_T2.txt`, `PROBE_RUN_T1.txt`, `PROBE_RUN_T3b.txt`.*

## ⛔ The negative — scored on the rule pushed at `+71.1`: **≥ 3 of 4 → the rule over-classes**

| probe | item | builds in budget | lines / budget | axioms |
|---|---|---|---|---|
| **T1** | `r7273` B9, parallel transport — **on `E`** | **yes** | **229 / 300** | `[propext, Classical.choice, Quot.sound]` |
| **T2** | `r7277` B7, geodesic existence — **on `E`** | **yes** | **159 / 300** | `[propext, Classical.choice, Quot.sound]` |
| **T3a** | `r7269` A5, the flow's group law — **on a manifold** | **yes** | **57 / 250** | `[propext, Classical.choice, Quot.sound]` |
| **T3b** | `r7269` A5, the flow `C¹` in `x` — on a manifold | **no** | **230 / 250**, stopped | `flow_hasFDerivAt`: `sorryAx` |

***`3` of `4`. By the rule fixed before the search, the DEF/PORT/THEORY rule over-classes, even where `mathlib`
says it defers, and the bound moves down.***

***What that does not license, said beside it and not rounded into it.***
- *The probe that failed is the one the order and I both named as the cluster's real need: smooth dependence
  on initial data.* ***At `250` lines it is THEORY by measurement, not by classification.***
- *The three that built did not need it:*
  - *T1 and T2 needed existence, which `mathlib` has locally;*
  - *T3a needed uniqueness, which `mathlib` has.*
- ⇒ ***The cluster was two things filed as one.***
  - *ODE existence and transport were over-classed: a local theorem plus `95` lines of gluing.*
  - *Smooth dependence is a real gap. Steps 1–3 of its textbook proof, and part (a) of step 4, took `202`
    lines before the core estimate began.*

## The count

| | central | band | **measured** |
|---|---|---|---|
| T1 builds, ≤ 300 lines | 0.45 | — | **yes, 229** |
| T2 builds, ≤ 300 lines | 0.4 | — | **yes, 159** |
| T3a builds, ≤ 250 lines | 0.5 | — | **yes, 57** |
| T3b builds, ≤ 250 lines | **0.1** | — | **no — 230 lines, stopped on `flow_hasFDerivAt`** |
| **builds, of 4** | **1.5** | 0–3 | **3** ✔ — *at the top of the band, a miss in the cheap direction for the third cycle running* |

## What each probe holds, in terms

- **T3a — `flow_add` (`FlowProbe.lean`).**
  - *Setting:* a `C¹` vector field `v` on a boundaryless manifold. `flow` is DEFINED from `mathlib`'s integral
    curves by choice: `exists_isMIntegralCurveAt_of_contMDiffAt_boundaryless`.
  - *Statement:* `flow (s + t) x = flow t (flow s x)` for `s` near `0`, then `t` near `0`.
  - *How:* local uniqueness (`isMIntegralCurveAt_eventuallyEq_of_contMDiffAt_boundaryless`) and the shift
    `IsMIntegralCurveAt.comp_add`.
  - *Built the first time it ran.*
- **T2 — `geodesic_exists` (`GeodesicExistProbe.lean`).**
  - *Setting:* a `cov` on `TE` whose Christoffel form is a `C¹` map `G : E → E →L E →L E`, with
    `∇_w (const u)(x) = G x w u`.
  - *Statement:* for any `x`, `v` there are `ε > 0` and `γ` with `γ 0 = x`, `vel γ 0 = v`, and
    `IsGeodesicAt cov γ t` for every `t ∈ (−ε, ε)`.
  - *How:* the first-order system `(x, v)′ = (v, −G(x)(v, v))` on `E × E`, through
    `ContDiffAt.exists_forall_mem_closedBall_exists_eq_forall_mem_Ioo_hasDerivAt₀`.
  - *`covDerivAlong_model` turns `D/dt` on `E` into `V′ + G(γ)(γ̇, V)`:* the frame of every trivialisation of
    `TE` is the constant basis (`model_localFrame`), and the frame coefficients are coordinates
    (`model_localFrameCoeff`).
- **T1 — `parallel_transport_exists` (`TransportProbe.lean`).**
  - *Setting:* the same `G`, continuous along a `C¹` curve `γ`; `T > 0`.
  - *Statement:* for any `v` there is `V`, continuous on `[0, T]`, with `V 0 = v` and `covDerivAlong cov γ V t
    = 0` on `(0, T)`.
  - *How:* `mathlib`'s Picard–Lindelöf is LOCAL. It needs `L · (time) ≤ a` on a ball of radius `a`, which a
    linear field meets only for times below about `1 / sup ‖A‖`.
    - `linear_step`: one Picard–Lindelöf step of fixed length `h` with `M h ≤ 1/2`.
    - `linear_glue`: two `Icc` solutions joined, via `HasDerivWithinAt.union`.
    - `linear_exists`: induction over `⌈T/h⌉` steps.
  - *`95` lines with their docstrings. That is the whole of what "`mathlib` has no parallel transport" cost on
    `E`.*
- **T3b — stopped (`SmoothFlowProbe.lean`).** The textbook route, in order:

  | step | what | status |
  |---|---|---|
  | 1 | `remainder_unif`: the first-order remainder of a `C¹` map is uniformly small on a ball | proved |
  | 2 | `local_flow`: the local flow, Lipschitz in `x` | proved — *`mathlib` has this* |
  | 3 | the linear ODE in `E →L E` (copied from T1), and `variational_exists`: `J′ = Df(φ) ∘ J`, `J 0 = id` | proved |
  | 4a | `flow_bounded`: the trajectories stay in one compact ball | proved |
  | **4** | **`flow_hasFDerivAt`: `y ↦ φ(t, y)` has derivative `J t` — Grönwall on the remainder** | **stated; stopped at line 230** |
  | 5 | continuity of `J` in `x` — a second Grönwall | not begun |
  | 6 | `C¹` on `E` | not begun |
  | 7 | the chart transfer to a manifold | not begun |

  - *The lemma it stopped on: `flow_hasFDerivAt`.* `norm_le_gronwallBound_of_norm_deriv_right_le` needs a
    right derivative at every point of `[0, t)`, including `0`. Step 3's interface exports `HasDerivAt` on
    `(0, τ)` only, so step 3 has to be re-opened before step 4 can close.
  - ***With 20 lines left, steps 4–7 do not fit.*** *My reading puts the whole at about `400` lines. That is
    an estimate, not a measurement.*

## ⚠ A flaw in my pre-registration, found while scoring — stated, and fixed in the probe

***T1's statement, as pushed at `+71.1` — "`V 0 = v` and `covDerivAlong cov γ V t = 0` for `t ∈ (0, T)`" — has a
trivial witness:*** `fun t => if t = 0 then v else 0`.
- *`0` solves a linear equation, and nothing in the wording ties `V 0` to the open interval.*
- *The probe as first landed (`+71.4`) exported exactly that wording. It constructed a genuine solution, but the
  statement did not show it.*
- ***Fixed here:*** `linear_exists` and `parallel_transport_exists` now also export `ContinuousOn V (Icc 0 T)`.
  That rules the witness out, and the probe still builds, at `229` lines.
- *T2 and T3a do not have the defect:*
  - *in T2, `vel γ 0 = v` and the geodesic equation at `0` pin the velocity;*
  - *in T3a, `flow` is a fixed definition, not an existential.*

## The scope cut, classed by reading as pre-registered

- **T1 on a manifold — PORT.**
  - *Ingredients replaced:* (i) frame-independence of `covDerivAlong` across trivialisations, never stated in
    this project; (ii) gluing chart pieces in time, which `linear_glue` already does.
  - *Nothing new is needed: the ODE in each chart is T1's.*
- **T2 on a manifold — PORT.**
  - *Geodesic existence is local, so one chart suffices.*
  - *Ingredient replaced:* that, on a chart's domain, `covDerivAlong` equals the model formula `V′ + Γ(γ)(γ̇,
    V)`. That is (i) again, plus the Christoffel form of `cov` in the chart being `C¹`. That second part is
    what `Basic.lean` defers, so on a manifold it is a hypothesis, as `G` is here.

## The seven of the cluster, after this

| item | before | after | by |
|---|---|---|---|
| `r7269` A5, the flow | THEORY | **split**: group law **DEF** (T3a); `C¹` in `x` **THEORY** (T3b stopped) | measurement |
| `r7269` B3, the flow form of `𝓛` | THEORY | **THEORY** — *needs `D_x φ_t`, i.e. T3b* | reading, on a measured gap |
| `r7269` B9, flow isometries | THEORY | **THEORY** — *needs `D_x φ_t`, i.e. T3b* | reading, on a measured gap |
| `r7273` B9, parallel transport | THEORY | **DEF** on `E` (T1); **PORT** on a manifold | measurement; reading |
| `r7277` B7, geodesic existence | THEORY | **DEF** on `E` (T2); **PORT** on a manifold | measurement; reading |
| `r7277` B11, null geodesics in every null direction | THEORY | **DEF** on `E` — *T2 with `v` null, kept null by compatibility (`r7273` B7)* | reading; not built |
| `r7277` B12, affine reparametrisation | THEORY | **THEORY** — *not an ODE item; unprobed* | rule |

## ② The THEORY-probed fraction — the `r7277` definitions, updated

- **(a) Strict — classed THEORY in a RESULT, later probed, counted by probe: `4 / 5` built.**
  - *Built:* `r7269` B6 (`r7273` Q2); T1; T2; T3a.
  - *Not built:* T3b.
- **(b) Pre-registered — named as the expected THEORY in a PREDICTION, then probed: `5 / 5`, unchanged.**
- **(a) ∪ (b), distinct probes: `9 / 10`.**
- **(c) The population — ever classed THEORY in a RESULT: `12`. Never probed: `8`** (was `11`; A5, `r7273` B9 and
  `r7277` B7 are now probed).

***What the fraction can now say.***
- *`9 / 10` has its first failure in it, and the failure is where the classification said the theory was.*
- *So "an upper bound on the obstruction" stands, and the order's symmetric reading gives the direction:*
  ***the bound moves down.*** *Existence and transport on a vector space were never theory.*
- *It does not move to zero. One named piece, smooth dependence on initial data, is THEORY by measurement.*
- *How far the `82` per cent moves is not a count this layer can give.* `111` of `135` receipts were never
  mapped to cluster items, and this result does not map them.

## How it got built

- *T3a built the first time it ran.*
- *T2 and T1 each took several elaboration rounds.*
  - *The model-space frame lemmas cost the most, by the `TangentSpace`/`E` coercion as before.*
  - *Then:*
    - *the namespaced `ContDiffAt.exists_…_hasDerivAt₀`;*
    - *`Metric.mem_closedBall`;*
    - *`NNReal` coercions in `IsPicardLindelof.mul_max_le`;*
    - *one `0 = 0` across `TangentSpace` and `E`, closed by `rfl`.*
- ***No round in T1–T3a stopped on a missing lemma.*** *The one structural gap was that Picard–Lindelöf is local,
  and gluing closed it.*
- ***T3b stopped on budget, not on a missing lemma.*** *Every step it reached was provable from `mathlib`. The
  route is long, because the variational equation and two Grönwall estimates are not in `mathlib`.*

## The order's other constraint

***The Levi-Civita port is not begun.*** *Every probe takes the connection as a hypothesis, through its Christoffel
form `G`. Nothing touches `LeviCivita.lean`, `Metric.lean` or an earlier probe.*
