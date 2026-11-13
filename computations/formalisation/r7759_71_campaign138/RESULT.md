# `r7759+71.2` — RESULT: campaign 138, **P7's last four cored rows BUILT (1, 6, 3d, 7c). P7 is closed: 15 of 15.** ⌗ `329` new lines (band 400–750, **under by 71**), at p(all four) `0.5`

*The registration is `PREDICTION.md`. The probe is `probes/Framework.lean` (619 lines), with the new rows appended.*

## Verification
- `lake env lean probes/Framework.lean` gives **0 errors and 0 warnings**.
- **27 axiom lines** (16 from earlier, 11 new), every one `[propext, Classical.choice, Quot.sound]`.
- The forbidden-token grep is clean, imports are `Mathlib` only, and `check_no_sorry.py` reports ALL 29.
- No options are set.

## Rows

| Row | Statement (Lean) | Mark |
|---|---|---|
| 1 | `fw_rs_tendsto`: the tortoise `r* = r + 2M log(r/2M − 1)` → `−∞` at `r → 2M⁺`. `fw_no_intersection`: every path `r ↦ t(r)` on `(2M, r₀)` with `dt/dr ≤ −k/f` (`k > 0`) has `t → +∞` as `r → 2M⁺`, so no finite exterior time reaches the horizon. The proof: `t + k r*` is antitone. `fw_timelike_slope`: every radial timelike geodesic has slope `−(E/f)/√(E² − f) ≤ −1/f`, so it is covered with `k = 1`. Ingoing null rays have slope exactly `−1/f` | **BUILT** (chart form) |
| 6 | `fw_sinh23`: `r = A sinh^{2/3}(3τ̃/2α)` (`Real.rpow`, `A³ = 2Mα²`) satisfies the bead `r³ = 2Mα² sinh²(3τ̃/2α)` and, at every `τ̃ > 0`, has a derivative with `(dr/dτ̃)² = 2M/r + r²/α²` | **BUILT** |
| 3d | `fw_H`: the oriented future horizon of the waist point `(0, αn)` is `dS₄ ∩ {X₀ > 0, X₀ = x·n}`. `fw_H_null`: its normal is null. `fw_horizon_inj`: `n ↦ ℋ⁺(n)` is injective on unit vectors (in particular `ℋ⁺(n) ≠ ℋ⁺(−n)`), witnessed by `(t, tn + α n^⊥)` with `t` large | **BUILT** |
| 7c | `fw_τ`, explicit: `−(2α/3)i arcsin((|r|/r₀)^{3/2})` on `[−r₀, 0]`, and `(2α/3)(arcosh(…) − iπ/2)` beyond. `fw_τ_bead`: it solves the bead on all of `r ≤ 0`. `fw_τ_bound`: `|Im τ̃| ≤ πα/3`, with equality exactly for `r ≤ −r₀`. `fw_τ_cont`: `τ̃` is continuous on `(−∞, 0]`, the pieces agreeing at `−r₀` | **BUILT** |

**Witnesses** (`fw_witness2`):
- the bead at `M = ½`, `α = 1`;
- the bound inside the lap (`r = −½`) and its equality beyond it (`r = −2`);
- `ℋ⁺(e₀) ≠ ℋ⁺(e₁)`;
- `r* → −∞` at `M = 1`.

**Against the registration:**
- **Rows 1 and 6 were reproved, not ported, as registered in advance.** P2's `sr_future_diverges` (manifold-level, in
  `CircleChart.lean`) is not copied. Row 1 here is its chart-form content.
- **None of the named stops held.** The 7c gluing closed by `ContinuousOn.union_of_isClosed`.
- **7c's `τ̃` is one continuous choice of branch.** That it is *the* analytic continuation of the real `sinh^{2/3}`
  law through `r = 0` is the paper's reading. The formal content is the explicit solution, its continuity, and the
  bound.
- **Size:** 329 lines against a band of 400–750.

**P7 tally: closed.**
- **15 of 15 cored rows BUILT:** 1, 3a, 3b, 3c, 3d, 6, 7a, 7b, 7c, 8a–8e, 9.
- 14 statements have no formal core.
- **Not formalised:** the surjectivity of `p ↦ ℋ_c⁺(p)`, and the ontological readings.
- None of it touches P7's rate remark.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
