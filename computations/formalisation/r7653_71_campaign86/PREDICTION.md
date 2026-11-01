# `r7653+71.1` — PRE-REGISTRATION: campaign 86, `r7653`, route (b)'s local kit on a multi-chart `N`: openness of `I^±`, push-up, and the short steps, each through one point's own chart and reusing campaign 84's transfer. ⌗ `900` new lines in one probe (band 500–1800 new), ⛔ stop `2400` new. ⌗ p: openness of `I^±` `0.65`, short steps and the curve into a point `0.7`, push-up `0.4`, whole `0.35`. **Expected stop: push-up, at subdividing a manifold `CStep` that crosses charts into finitely many chart-local arcs** (a Lebesgue number on `[0,1]`), so that campaign 60's local push-up applies arc by arc. Second likeliest: restricting a `TStep_N` to a sub-interval and reparametrising it back to `[0,1]`

*Under `r7653`. The setting is campaign 85's `probes/ManifoldExtension.lean` (`LocallyOneChart`, `me_local_step`, the
gluing), plus campaign 84's transfer (`ch_tstep_iff`, `ch_curve_VN`/`NV`, `chartSp`). They are copied into a new probe,
`probes/ManifoldLocalKit.lean`. No Lean was written before this registration.*

## The pieces (`hL : LocallyOneChart S` throughout)

1. **Restriction.** `TStep_N x y`, restricted to `[s,1]` and reparametrised, is `TStep_N (γ s) y`, and likewise for
   `CStep`. So `x ≪ y` gives points `w ≪ y` on the last step that are arbitrarily close to `y`.
2. **Openness of `I⁺(x)` and `I⁻(x)` on `N`.**
   - For `y ∈ I⁺(x)`, take `w` on the last step, close to `y` and inside `y`'s `OneChart` patch.
   - Campaign 81's `tstep_end_eventually`, read in that chart and transferred by `ch_tstep_iff`, gives `TStep_N w y'`
     for all `y'` near `y`.
   - `I⁻` is the same in the reversed orientation.
   - **Consequence.** `IsOpen (D J)` on `N`, which is what campaign 85's `me_futCauchy_of_cauchy_N` needs for
     `U = D J`.
3. **Short steps.** A future step `TStep_N x (g x)` from every `x ∈ M`, near `q`, with `g` continuous. This is
   `me_local_step` with `T` replacing `−T`.
4. **The curve into a point.** In `q`'s chart, `γ t = φ_q⁻¹(φ_q q − εe^{−t} T_V)`, transferred to a future-inextendible
   curve in `N∖{q}`. Its points are `≪ q` and `≪` each other.
5. **Push-up on `N`** (`Cau x y`, `Chr y z` ⇒ `Chr x z`, and the dual).
   - By induction on the `CStep`s, it suffices to push up across one `CStep_N x y`.
   - Its image in `[0,1]` is covered by finitely many chart-local arcs, by a Lebesgue number for the cover by
     `{γ⁻¹(OneChart patch)}`.
   - Campaign 60's `local_pushup` is applied on each arc, from the end backwards.
   - This is the registered expected stop.
6. **Non-vacuity.** Each conclusion is exhibited on campaign 85's two-chart `NModel.Pt`. `IsOpen (D J)` is exhibited
   there too, and push-up on one `CStep` that crosses the chart boundary `t = 0`, if that is reachable.

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED, with the step that stopped.

***Reachable negative.*** If the subdivision is heavy, push-up is stated for `CStep`s that lie in one chart patch.
RESULT names the subdivision as the gap campaign 87 must close.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
