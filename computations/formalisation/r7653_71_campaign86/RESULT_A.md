# `r7653+71.2` — RESULT: campaign 86, route (b)'s local kit on a multi-chart `N`. **All six pieces BUILT, and the registered expected stop was not hit.** Push-up on `N` needed no Lebesgue subdivision: campaign 60's `sInf` argument runs on `[0,1]` directly, once `I^±` is open on `N`. `IsOpen (D J)` on `N` is built, which is the piece campaign 85's Cauchy result was waiting for. ⌗ `2139` lines in one probe (about `765` new, band 500–1800). ⌗ p: openness `0.65`, short steps and curve `0.7`, push-up `0.4`, whole `0.35`: all came true

*Against `PREDICTION.md` (`r7653+71.1`). 71 re-ran `lake env lean probes/ManifoldLocalKit.lean`. It exits 0 with no
errors. All `23` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`. The forbidden-token grep is clean.
Campaigns 84 and 85 are copied in and trimmed: the `V` side with campaign 60's push-up, the transfer, `LocallyOneChart`
and `NModel`.*

## The pieces (`hL : LocallyOneChart S`)

1. **Restriction.**
   - `mk_vel_affine` gives the velocity of an affine reparametrisation.
   - `mk_tstep_sub` and `mk_cstep_sub`: a sub-arc `[a,b]` of a step is a step.
   - `mk_tstep_restrict`: every point of a `TStep_N` is `≪` its endpoint, and its start is `≪` every point.
2. **Openness.**
   - `mk_patch`: every `p ∈ M` has an open `OneChart` patch.
   - `mk_isOpen_Ifut` and `mk_isOpen_Ipast`: `I⁺(x)` and `I⁻(z)` are open on `N`.
   - **`mk_isOpen_D`:** `D J` is open for every `J`.
   - `mk_Ipast_subset_D`: for `q ∈ closure D`, `I⁻(q) ⊆ D`. This is campaign 75's step 1, now on `N`.
3. **The short future step.** `mk_local_step_fut`, through a new two-sided tube lemma, `safe2_uniform`.
4. **The curve into a point.** `mk_curve_into` gives a curve with `c t → q`, `c t ≪ q`, `c t ≪ c t'`, future-timelike
   `mfderiv` velocity, and `c t ≠ q`.
   - `mk_curve_inext_punctured` and `mk_curve_inext_D` make it future-inextendible in `M ∖ {q}`, or in `D J` for
     `q ∈ closure D ∖ D`.
   - **An added hypothesis.** Both take `[T2Space N]`, used only for uniqueness of the limit. The registration did not
     list it; P1's spacetimes are Hausdorff.
5. **Push-up on `N`.** `mk_pushup` gives `Cau x y → Chr y z → Chr x z`, and `mk_pushup'` the dual. Both hold for causal
   steps crossing any number of charts.
   - **The route.** At `s = inf {t | α t ≪ z}`, the local push-up (`mk_pushup_patch`, campaign 60's `pushup_cstep` in
     that patch's chart, with `g` locally Lipschitz because it is C¹) is taken in `α s`'s own patch. Openness of
     `I⁻(z)` then forces `s = 0`. The dual uses `sSup` and `I⁺`.
   - **No subdivision is needed.** The registered expected stop did not arise, and nothing is left for campaign 87 on
     push-up.
6. **Non-vacuity.** On campaign 84's two-chart `NModel.Pt`:
   - `mk_witness_kit` exhibits each conclusion of pieces 1–4.
   - `mk_witness_pushup` pushes up across the chart boundary `t = 0`, with endpoints whose preferred charts differ
     (`mk_witness_sides`).
   - **The witness's limit, stated.** On `Pt` the patch of any `t ≥ 0` point is all of `Pt`. So the witness does not
     force a genuinely multi-patch use of the `sInf` argument.

## Route (b), after this

***Campaign 87, the assembly.*** The chain on `N`: properness, `hint`/`hcl`, the slice limits and Kuratowski, and the
headline on any `LocallyOneChart` `T2` manifold. It needs one end-to-end witness that also discharges campaign 85's open
Cauchy hypothesis, now with `IsOpen (D J)` in hand.

***The pricing holds.*** About `765` of the registered `900` lines were used.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
