# `r7315+71.1` — PRE-REGISTRATION: B, the discharge sweep, run as proposed. Candidates are counted by `r7297`'s rule BEFORE any cost is fixed; the costs are fixed BEFORE any Lean is written; and the run stops at the first receipt over `200` lines. ⌗ My reading of the line's natural end: one seat finishes the CONNECTION layer, and the larger remainder is independent work that wants more hands

*Committed and pushed before `READINGS.tsv` is reopened for this order and before any `mathlib` file is read. The
order is `FOR_71.md` §`r7315`. It accepts `r7309+71.1`'s B unedited and asks one question, answered in the last
section.*

## The base, as it now stands

- **The port**, `288` lines: `lcConn` exists, is unique, is torsion-free, and is compatible with any nondegenerate
  `g`.
- **A**, `163` lines: `ContMDiffCovariantDerivative (lcConn …) ∞` on the model space for `C^∞` `B`, and K1 applies to
  it with no class carried.
- **Six receipts are discharged in full:** 42, 43, 92, 41, 29, 77. The cumulative cost is `857 / 6 ≈ 143` lines per
  discharge.

## The pieces, in order

| piece | content | fixed before |
|---|---|---|
| `+71.1` | this file: the rule, the stop, the negatives, and the count prediction | anything is read |
| `+71.2` | **`CANDIDATES.md`**: the candidate count by `r7297`'s rule, read from `READINGS.tsv`, each with its stand-in and a **predicted marginal cost**, ordered cheapest first | any `mathlib` file is read or any Lean is written |
| `+71.3 …` | one commit per landed candidate, pushed when green | — |
| last | the result and the reply | — |

## The candidate rule: `r7297`'s, unchanged

A receipt is a candidate when all three hold:
- it is one of the `97` statable;
- its stand-in carries a CONNECTION hypothesis: a geodesic equation, the covariant Killing equation, `∇_ξ ξ`, a
  curvature of `∇`;
- its metric fits in ONE chart of a model space, with an everywhere-nondegenerate form.

*The six discharged receipts are excluded. A first integral, a Lie-derivative statement, a pure ODE or a topological
statement carries no connection hypothesis and is not a candidate.*

- ***My prediction, carried from the proposal: `25` candidates (band 12–45).***

## ⛔ The stop rule, scored first: `r7297`'s, unchanged

| outcome | scored |
|---|---|
| a candidate lands with marginal `cᵢ ≤ 200` | take the next one |
| ***a candidate costs `cᵢ > 200`, or does not land within `2×` its predicted cost*** | ***STOP.*** *Every remaining candidate is reported as "statable, connection carried as a hypothesis", named, and not pursued.* |
| all candidates land at `≤ 200` each | ***the connection layer of the statable corpus is done on the model space*** |

- *Reported beside each candidate: the cumulative rate `(857 + Σcᵢ)/(6 + k)`, against the `150` line `r7297` fixed.*
- ***The symmetric negative, on the low side:*** *if the mean `cᵢ` over the landed candidates is under `60`, the port's
  marginal cost is dominated by restating each metric. **The connection is then no longer the cost, and the line's
  remaining work is "state the metric", which is not formalisation of the connection.** That is reported as what
  the sweep found, not as a success.*
- **The `C^∞`-profile cost from A:** a candidate's instance needs its profile functions to be `ContDiff ∞`. That line
  is counted in `cᵢ`. A candidate whose profile is not smooth on its chart does not land.

## My probabilities

| quantity | p |
|---|---|
| the count falls in 12–45 | 0.70 |
| the sweep reaches its last candidate without the stop firing | **0.35** |
| the first STOP falls on a metric with no everywhere-nondegenerate chart (a horizon in the chart) | 0.60 |
| the cumulative rate ends below `150` | 0.55 |
| the low-side negative fires (mean `cᵢ < 60`) | 0.15 |

## ⌗ The order's question: the line's natural end, and whether it wants more hands

***My reading, given before the sweep so that the sweep can falsify it.***

1. **The `~91` statable-not-stated split into two kinds with different costs.**
   - ***Connection-carrying, about `25` (B's candidates).*** These need the port's machinery: `NDMetric` on a chart,
     `g_inj`, `lcConn_apply`, and now A's instances. They cost about `120` lines each, and the cost sits in knowing
     that machinery's failure modes:
     - product-model inference;
     - `set` against unfolded terms;
     - the `TangentSpace` coercions.
   - ***The rest, about `66`.*** First integrals, Lie-derivative statements, ODE solutions, topology, and identities
     on named functions. None needs the connection. I expect them at `30`–`90` lines each, on plain `mathlib`
     analysis, with almost nothing of the port.
2. **The natural stopping point of B is a CLASS of metric, not a count.** I expect the stop to fire on the first
   named metric whose usual chart has a horizon or a coordinate singularity, so that `NDMetric`'s
   everywhere-nondegeneracy fails. There are two ways past it:
   - find a chart without the degeneracy, as C2/C4 did with `r = eˢ` and `η = 2 arctan eᵘ`;
   - weaken `NDMetric` to an open set, which is a change to the port and not a discharge.

   ***So I predict one seat finishes the connection layer up to that class in about four cycles (`25 × 120 ≈ 3000`
   lines, at r7297's pace of about five discharges a cycle), and the class itself is a port question to propose
   when it is met.***
3. **Whether it wants more hands: yes, for the second kind, and no, for the first.**
   - The ~66 statements that need no connection are independent theorems, and no seat needs the port to write them.
     They want more hands, and the foundation under them no longer moves (A closed it).
   - The ~25 connection-carrying ones want ONE hand. The cost is the machinery's idioms, and two seats learning them
     at once would pay twice.
   - ***The precondition for more hands is mechanical, and it is mine to supply:*** *the probe file is ~2200 lines in
     one module, and a second seat writing in it would conflict on every merge. **I would split the port and A into
     a `Port.lean` that others import, and put each statement in its own file.*** *That is not in B's scope. It is
     offered as the first piece of the next order if more hands are wanted, at about `50` lines of moves and no new
     proofs.*
4. ***What would show this reading wrong:***
   - the count coming in far above 25, which would make the connection layer the bulk of the work;
   - or the mean `cᵢ` under 60 (the low-side negative), which would make the connection layer cheap enough that the
     split is not worth making.

## What this does NOT do

- Nothing in the quote-pin stride.
- None of the four library absences.
- No change to the port or to A. Each candidate sits beside them.
- No weakening of `NDMetric`. If the stop fires on a degenerate chart, that is reported and proposed, not done.
