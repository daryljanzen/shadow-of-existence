# P1's 6b-ii priced for real: a phased plan (`r7807+71.1`)

*A plan, per r7807. **The target** is the hypothesis `HasFutureGenerators` (`GeneratorStretch.lean` l.6373), which
`gs_future_stretch` takes and discharges only on the 4D witness: through every `q ∈ 𝓗⁺ = ∂J⁻(J)` passes a curve
`γ : [0, ∞) → N` that is merely **continuous**, starts at `q`, stays in `𝓗⁺ ∩ J⁺(q)`, and leaves every compact set.
In general this is the standard theorem that the null generators of an achronal boundary are future-inextendible.
It was ruled to wait at r7669 and priced at 2500–6000 lines.*

## The proof being formalised
For `q ∈ ∂J⁻(J)`, take `pₙ → q` with `pₙ ∈ J⁻(J)` and causal curves from `pₙ` toward `J`. By the **limit-curve
theorem** a subsequence converges to a causal curve through `q`. It lies in the closure of `J⁻(J)`. No point of it is
in `I⁻(J)`, since otherwise push-up would put `q` there. So it lies in `∂J⁻(J)`, and it is future-inextendible because
`J` is at infinity. "Leaves every compact set" then needs **non-imprisonment**.

This is the continuous-metric causality theory of Chruściel–Grant (2012) and Sämann (2016), which suits P1's setting:
a `C¹` metric on a manifold.

## What Mathlib already supplies
- Arzelà–Ascoli: `BoundedContinuousFunction.arzela_ascoli`, `arzela_ascoli₂`.
- Compactness of closed balls in finite dimension (`ProperSpace`), and uniform limits.
- Lipschitz maps, and Rademacher's theorem (`Analysis/Calculus/Rademacher.lean`, `LipschitzWith.ae_differentiableAt`).
- Monotonicity from derivatives (`monotoneOn_of_deriv_nonneg`), the mean-value inequality, and ODE existence
  (Picard–Lindelöf).
- **Not in Mathlib:** any Lorentzian or causal notion, convex normal neighbourhoods, or exponential maps. The probes'
  kit (`MSpacetime`, `Cau`/`Chr` as chains of `C¹` causal arcs, push-up on `N`) supplies the causal part.

## A hypothesis the general theorem cannot do without
**Finite dimension.** P1's `rem:formalised` works over an arbitrary real normed model space. The limit-curve theorem
is false there: bounded sets are not compact, and Arzelà–Ascoli fails. Every phase below therefore assumes a
finite-dimensional (proper) model space. This narrows P1's generality; it is not a gap in Mathlib.

## The phases

| Phase | What it builds | New lines | p |
|---|---|---|---|
| **1** | **Cone curves in a chart.** In a finite-dimensional normed space `E`, a closed convex cone `K` that is uniformly timelike for a linear `τ` (`τ v ≥ c‖v‖` on `K`). `K`-curves have increments `γ t − γ s ∈ K` for `s ≤ t`. They are Lipschitz in the `τ`-parameter, and closed under pointwise limits. **The local limit-curve theorem:** a sequence of `τ`-parametrised `K`-curves on `[a, b]` with converging starts has a subsequence converging uniformly to a `K`-curve | 300–550 | 0.55 |
| 2 | **The kit's causal arcs are locally cone curves**, and the limit-curve theorem on `N`. With the metric continuous in a chart, a `C¹` causal arc lies, locally, in a constant cone slightly wider than the light cone, which is a Phase-1 cone. Patching charts gives Lipschitz causal curves on `N` and a global limit-curve theorem, in an auxiliary metric | 900–1800 | 0.35 |
| 3 | **Inextendibility and non-imprisonment.** Limits of curves running to `J` are future-inextendible. Under a **global temporal function on `M`** (the extra hypothesis r7669 named), a future-inextendible causal curve leaves every compact set | 600–1400 | 0.4 |
| 4 | **The achronal-boundary argument.** For `q ∈ ∂J⁻(J) \ J`, the limit curve lies in `∂J⁻(J)` and in the closure of `J⁺(q)`. This needs push-up for Lipschitz causal curves with a `C¹` metric | 700–1500 | 0.3 |
| 5 | **Landing in `HasFutureGenerators` as stated.** Its `S.Cau q (γ t)` is the kit's chain relation. Either: (a) show that Lipschitz-causal and piecewise-`C¹`-causal reachability agree for `C¹` metrics, which is the hardest step and not in any library; or (b) restate `HasFutureGenerators` and `gs_future_stretch` with the closure of `J⁺(q)`, if the stretch proof uses only that | (a) 1500–3000; (b) 300–700 | (a) 0.2; (b) 0.6 |

**Total:** about 2800–6000 lines by route (b), in line with r7669's price.

**Beyond Mathlib entirely:** none of the phases needs mathematics Mathlib lacks at the foundations. Rademacher,
Arzelà–Ascoli and ODE existence are all there. Phase 5(a) is research-grade formalisation rather than beyond, and
route (b) avoids it. The only true restriction is finite dimension.

**Phase 1** is registered in `PREDICTION.md` and built in `probes/LimitCurve.lean` (`lc_`).

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
