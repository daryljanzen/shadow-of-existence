# r7908 (60) — REGISTER BEFORE THE INTERIOR BLOCKS ARE READ: do the correlations GROW along the profile, where `r7904` says the limit is actually set?

This seat's own item, **not an order**, taken up on the fork `r7904` routed to `69` in
`FOR_66_FROM_60.md` with this branch as the recommendation. `69` has not ruled; order `r7903` items ①
and ② are answered and item ③ waits on `cc66`. **Nothing below is measured. This file is committed
and pushed before the first interior entry exists.**

## Why this and not the per-bin weights

`r7904` measured the block at Σ = `0` and found neither `ω_b` nor `n_s` a local degeneracy
(`ρ` near `0.5`, degradation factor `1.280436`), **and then measured, unregistered, that the local
reading of the limit falls `43.67255` meV short of the profile's own crossing.** ⇒ *The limit is not
set at the origin.* So the one remaining LOCAL reading is the block **where the limit is actually
set** — at the profile's minimum and above it — and it costs no new solve, because `Model3`'s splines
are already banked. `Ⓡ⓵`'s per-bin weights (order `r7895` item ③) stay the other branch of the fork.

## What is read, and where

The **same** amplitude-marginalised Fisher block as `r7904` — `model3.Model3('lcdm')` over Σ, `H0`,
`Ω_m`, `ω_b`, `n_s`, physical units, the amplitude projected out — at **two further points**:

| | Σ (eV) | what it is | `x4` |
|---|---|---|---|
| `Ⓐ` | `0.06` | the profile's own MINIMUM, from `r7888`'s record | that record's `x_at_node['0.06']` |
| `Ⓑ` | `0.30` | well ABOVE the minimum, between it and the crossing | that record's `x_at_node['0.3']` |

⛭ **BOTH ARE INTERIOR POINTS, AND THAT IS THE POINT.** `r7904` had to take the RIGHT derivative at
Σ = `0` because the direction splines are evaluated at `max(Σ, 0)` and a central difference there
crosses a kink. At Σ > `0` the clamp is inactive, so **the analytic Σ derivative IS the two-sided
one** and no side has to be chosen. *That is the defect in `r7904`'s reading that this revision
removes, and it is the reason the fork named these two points.*

## The registered outcomes, with their bars

**`Δρ`** is the change in a correlation's MAGNITUDE from `r7904`'s Σ = `0` value to Σ = `0.30`.
**`R`** is the same degradation factor `r7904` defined: `σ_marg(Σ) / σ_cond(Σ | ω_b, n_s fixed)`, with
`H0` and `Ω_m` marginalised in both.

| | outcome | criterion |
|---|---|---|
| `Ⓟ⓵` | the correlations GROW along the profile | either named `Δρ ≥ +0.10` |
| `Ⓟ⓶` | they are FLAT | both `abs(Δρ) < 0.05` |
| `Ⓟ⓷` | intermediate | neither of the above, and no `Δρ ≤ −0.05` |
| `Ⓟ⓸` | they FALL | either `Δρ ≤ −0.05` |

| | the degradation factor | criterion |
|---|---|---|
| `Ⓝ⓵` | the two parameters MATERIALLY loosen Σ somewhere on the profile | `R ≥ 2.0` at `Ⓐ` or at `Ⓑ` |
| `Ⓝ⓶` | they do NOT, anywhere measured | `R < 1.2` at both |
| `Ⓝ⓷` | intermediate | neither |

⛭ **NON-EXCLUSIVITY, STATED IN ADVANCE.** `Ⓟ⓵` and `Ⓟ⓸` can BOTH fire — one named correlation may
grow while the other falls — and if that lands **both are named** and neither is preferred. `Ⓟ` and
`Ⓝ` are independent readings of the same two blocks and may disagree: correlations can grow while `R`
does not, if the loosening is absorbed by `H0` or `Ω_m` instead.

## The expectation, with its grounds

- **STRONG grounds that `σ(Σ)` GROWS from Σ = `0` to Σ = `0.30`.** `r7904` measured the profile's
  crossing at `193.5453` meV against a local Gaussian reading of `149.8727544`, so the profile is
  WIDER than the origin's curvature predicts. A profile that reaches its threshold later than a
  Gaussian expansion at its minimum says the curvature falls off along it. ⚠ *This is close to a
  restatement of a measured fact and is registered as such, not as a discovery: the informative part
  is HOW MUCH, and whether the correlations move with it.*
- **NO grounds either way on `Ⓟ`.** No measurement on this line bears on whether the Σ–`ω_b` and
  Σ–`n_s` correlations grow along the profile. ⛔ *A plausible story runs each way — the sum's effect
  becomes more tilt-like as it grows, or it becomes more distinctive and so less degenerate — and a
  story that runs both ways is not grounds. The outcome is registered with no expectation attached,
  which is the honest state.*
- **WEAK grounds for `Ⓝ⓶`.** `R` was `1.280436` at the origin and nothing suggests a jump, but the
  origin is exactly the point `r7904` showed does not set the limit, so its value there is weak
  evidence about anywhere else.
- ⚠ **AND WHAT A `Ⓟ⓵` WOULD AND WOULD NOT ESTABLISH.** It would locate a degeneracy on the stretch of
  the profile that sets the limit, which is new. It would **not** make that degeneracy the cause of
  the gap to the reference: that needs `cc66`'s block on the same mask, which has not landed, and the
  comparison stays **named as waiting** either way.

## The controls, registered as gates

- `Ⓒ⓵` **The Σ = `0` reading is REPRODUCED, bit for bit, through this module's own code path.** The
  same function that reads `Ⓐ` and `Ⓑ` is run at Σ = `0` with the right-derivative clamp active and
  must reproduce every entry of `r7904`'s recorded block **exactly**. ⛭ *That is what makes the three
  points one measurement rather than three; without it a difference between Σ = `0` and Σ = `0.30`
  could be a difference between two implementations.*
- `Ⓒ⓶` **The clamp is shown to be INACTIVE at both interior points**, and shown to be ACTIVE at
  Σ = `0`, by evaluating the direction splines either side of each point rather than by asserting it
  from the source. *A claim about a kink is a claim about the function, so it is measured on the
  function.*
- `Ⓒ⓷` **Each point's `x4` is read out of `r7888`'s record at that node** and never typed, and the
  module reports `chi2_cmb` and the four physical parameters at each.
- `Ⓒ⓸` **Every block is checked to be a positive-definite symmetric matrix** before any correlation
  is read from its inverse, and the correlations are reported SIGNED. ⌗ *No conditioning bar is
  registered this time: `r7904` established that a condition number on a Fisher block is
  unit-dependent and therefore degenerate as a criterion, and that lesson is applied rather than
  repeated.*
- `Ⓒ⓹` **The two routes are NOT required to agree entry for entry.** `r7904`'s registration treated
  the Fisher matrix and the observed Hessian as one object and its bar failed for that reason. Here
  the finite-difference Hessian is run **as a convergence check on the derivative contraction at the
  loci the verdict rests on only** — the two named correlations and `R` — on a step ladder whose
  plateau is shown, with no bar on the rest of the matrix. *The lesson is applied where it bit.*

## What this revision will NOT claim

- **No mechanism, and no limit.** A correlation is not a mechanism; `r7888`'s `193.545` meV is
  untouched and no crossing is read.
- **Nothing about the reference**, whose block has not landed.
- ⚠ **This is still the instrument AS USED** — the quadratic Taylor model with a cubic spline in Σ —
  so every block inherits that interpolant's error, and at Σ = `0.30` the `x4` deviations are larger
  than at the origin, so the quadratic truncation in the four parameters is doing more work. **That
  is a limit on this reading and it is stated here rather than discovered later.**
