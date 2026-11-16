# `r7807+71.3` — RESULT: 6b-ii, **phase 1 BUILT: cone curves in a chart and the local limit-curve theorem (L1–L4)**. ⌗ `186` lines (band 300–550, estimate 420, **under by 114**), at p `0.55`

*The plan is `PLAN.md` and the registration `PREDICTION.md`. The probe is the new standalone file
`probes/LimitCurve.lean` (`lc_`).*

## Verification
- `lake env lean probes/LimitCurve.lean` gives **0 errors and 0 warnings**.
- **5 axiom lines**, every one `[propext, Classical.choice, Quot.sound]`.
- The forbidden-token grep is clean, imports are `Mathlib` only, and `check_no_sorry.py` reports ALL 29. No options are
  set.

## Rows

| Row | Statement (Lean) | Mark |
|---|---|---|
| L1 | `lc_lipschitz_bound`: along a `K`-curve, `‖γ t − γ s‖ ≤ (τ(γ t) − τ(γ s))/c` for `s ≤ t`. `lc_param_lipschitz`: a `τ`-parametrised `K`-curve satisfies `‖γ t − γ s‖ ≤ |t − s|/c` on `[a, b]` | **BUILT** |
| L2 | `lc_limit_closed`: for `K` closed, a pointwise limit on `[a, b]` of `K`-curves is a `K`-curve, and of `τ`-parametrised curves is `τ`-parametrised | **BUILT** |
| L3 | `lc_limit_curve`: in finite dimension, any sequence of `τ`-parametrised `K`-curves on `[a, b]` with `γₙ a → p` has a strictly increasing `φ` and a `τ`-parametrised `K`-curve `γ` with `γ a = p` such that `γ_{φ n} → γ` **uniformly on `[a, b]`** | **BUILT** |
| L4 | `lc_witness`: on `ℝ × ℝ` (sup norm), `K = {(t, x) : |x| ≤ t}`, `τ = fst` and `c = 1`. The curves `γₙ(s) = (s, sin(ns)/n)` are `τ`-parametrised `K`-curves on `[0, 1]` from the origin, and `lc_limit_curve` applies to them | **BUILT** |

**Against the registration:**
- **The named stop did not hold.** L3's Arzelà–Ascoli assembly closed directly:
  - `BoundedContinuousFunction.mkOfCompact` on `Icc a b`;
  - the values lie in one closed ball, compact through `FiniteDimensional.proper_real`;
  - equicontinuity comes from the uniform `1/c` bound;
  - `IsCompact.tendsto_subseq` extracts the subsequence.
- **A weaker hypothesis on `K`.** `K` need only be closed. Convexity and closure under addition and scaling, though
  registered, are never used, so the theorems hold for every closed `K` with the timelike bound.
- **Size:** 186 lines against an estimate of 420.

**Standing of 6b-ii:** still BUILT IN PART. Phase 1 is the local analytic core of the limit-curve theorem. Phase 2
(the kit's `C¹` causal arcs as cone curves, and the theorem on `N`) is next in `PLAN.md`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
