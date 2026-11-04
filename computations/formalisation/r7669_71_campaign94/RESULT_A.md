# `r7669+71.3` — RESULT: campaign 94, both pieces **BUILT**, and no registered stop was hit. ① 1b and 2iv-a on ruling 2: the along-the-connection theorem with `Δτ = ∫ n |dt(γ′)|`, the positive-lapse companion forcing `p = q`, and the Rindler-horizon witness with `p ≠ q`. ② `lem:killing` stage 1 (`RESULT_2.md`). ⌗ ① `442` lines in one probe (about `380` new, band 120–800). ② `436` new lines. ⌗ p `0.85` and `0.75`: both came true

*Against `PREDICTION.md` (`r7669+71.1`). 71 re-ran `lake env lean probes/AlongConnection.lean`. It exits 0 with no
errors and no warnings. All `8` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`. The
forbidden-token grep is clean. `check_no_sorry.py` reports ALL 29 THEOREMS COMPILE. The probe imports Mathlib and
copies only `MSpacetime`, `gE`, `vel` and the flat `gM`.*

## ① The along-the-connection form

***`AdaptedSplitting S γ`.*** On `[0, 1]` it gives:
- `h s`, `n s ≥ 0` (which may vanish) and `dt s`;
- `g_{γ s} = h s − (n s)² dt s ⊗ dt s`;
- `h s (γ′, γ′) ≥ 0`.

Here `Δx = ∫₀¹ √h(γ′, γ′)` and `Δτ = ∫₀¹ n |dt(γ′)|`. It holds for an `MSpacetime` on any manifold.

***`ac_metric_singularity_along` — BUILT.***
- **Hypotheses:** (a) `g(γ′, γ′) = 0` on `[0, 1]`; (b) `Δx = 0`; and continuity of `h(γ′, γ′)`.
- **Conclusion:** `Δτ = 0`, `n · dt(γ′) = 0` on `[0, 1]`, and `h(γ′, γ′) = 0` on `[0, 1]`.
- The registered stop, `Δx = 0 ⟹ h(γ′, γ′) = 0` pointwise, goes through by `intervalIntegral.integral_pos`.

***`ac_lapse_pos_forces_point` — BUILT, on the manifold.***
- **Added hypotheses:** `n > 0`, and `h` positive definite on `ker dt`.
- **Conclusion:** (a) and (b) force `γ′ = 0` on `[0, 1]`, and so `γ 1 = γ 0`.
- **The supporting lemma:** `ac_const_of_vel_zero` shows that zero `mfderiv` velocity makes `γ` constant, by a
  chart-local mean value theorem and the connectedness of `[0, 1]`. It needs no Hausdorff assumption.
- **Non-vacuity:** `ac_lapse_pos_nonvacuous` gives the standard `t`-splitting.

***`Model.ac_witness`, on the Rindler horizon — BUILT.***
- **The curve and the field:** `γ(s) = (0, e^s)` on `U = 0`, and `χ = V∂_V − U∂_U`.
- **What it shows:**
  - `g(χ, χ) = UV`;
  - `χ(γ s) = γ′(s)`, which is null and non-zero;
  - the lapse `n = |χ| = 0`;
  - `dt = dV/V`, with `∫₀¹ dt(γ′) = 1`, so `λ = log V` separates the endpoints;
  - (a) and (b) hold, and `Δτ = 0`;
  - **`γ 0 = (0, 1) ≠ (0, e) = γ 1`.**
- **`χ` is Killing:** `ac_boost_generator` and `ac_boost_isometry` give the boost flow `(e^{−t}U, e^t V)`, which
  generates `χ` and preserves `g`.

***`ac_witness_no_positive_lapse`.*** Along this curve, no splitting with positive lapse satisfies the hypotheses,
by the companion and `p ≠ q`.

***So 1b and 2iv-a move to BUILT***, on 69's ruling: `Δτ` is the adapted frame's temporal leg.

## ② `lem:killing` stage 1 — see `RESULT_2.md`

4b–4d stay BUILT IN PART, and the gap is now one flow box.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
