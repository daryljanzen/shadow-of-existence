# `r7655+71.1` — PRE-REGISTRATION: campaign 87, `r7655`, route (b)'s assembly. `hl_causal_alignment_gh` carried onto a multi-chart `N` from campaigns 84–86, witnessed end to end on a two-chart manifold with the Cauchy hypothesis witnessed too. ⌗ `1200` new lines in one probe (band 600–2400 new), ⛔ stop `3000` new. ⌗ p: the headline on `N` `0.45`; the end-to-end witness on `NModel.Pt`, Cauchy included, `0.5` given the headline; a witness no single chart covers `0.15`. **Expected stop: the slice upper limit and Kuratowski step on `N`**, where campaign 81's proof reads closure and frontier through the vector-space structure of `V`. They must be redone with `N`'s topology and the chart-local push-up of campaign 86. Second likeliest: properness on `N`, which chains campaign 86's curve into a point, campaign 85's two-sided ⇒ future step at `U = D J`, and strict increase along `Chr_N`

*Under `r7655`. A new probe, `probes/ManifoldHeadline.lean`. It copies:
- campaign 86's `ManifoldLocalKit.lean` (openness of `I^±` and `D`, short steps, the curve into a point, push-up on
  `N`);
- campaign 85's extension and its two-sided ⇒ future step;
- the topological half of campaign 81's chain, from `HeadlineHypotheses.lean`: properness, the slice limits, and
  Kuratowski.

No Lean was written before this registration.*

## The assembly (`hL : LocallyOneChart S`, `[T2Space N]`)

1. **Temporal increase along `Chr_N`.** By `me_temporal_tstep` and induction.
2. **`hint` and `hcl` on `N`.** By campaign 86's short steps and push-up, as campaign 81 derived them in `V`.
3. **Properness on `N`.** Use `mk_curve_inext_D` with `me_futCauchy_of_cauchy_N`; the latter applies because
   `mk_isOpen_D` gives `U = D J`. Then `Θ → ∞` along the curve, and `I⁺(r)` is a neighbourhood of `q`.
4. **The slice lower limit.** The curve's tail, as in campaign 75.
5. **The slice upper limit and Kuratowski.** Redone in `N`'s topology (the registered expected stop).
6. **`mh_causal_alignment_gh_N`.**
   - Hypotheses: `LocallyOneChart`, `T2Space N`, `hOD`, `hmono`, `J ⊆ M`, `𝓗⁺ ⊆ M`, `IsCauchyTemporalOn (D J) Θ`, and
     `hadapt`.
   - Conclusion: properness, and `KLi = KLs = 𝓗⁺`.

## The witness

***On `NModel.Pt`, the two-chart model of campaigns 84–86.***
- Points with `t < 0` and `t ≥ 0` take different preferred charts.
- The witness discharges `LocallyOneChart`, the observer, `hOD`, `hmono` and `hadapt`.
- **It also discharges the two-sided Cauchy hypothesis on `D`,** which campaign 85 deferred. This is proved by
  transport through the chart whose source is all of `Pt` (campaign 84's `ch_isCauchy_VN`) from campaign 81's
  two-sided model.
- Then `mh_causal_alignment_gh_N` gives `KLi = KLs = 𝓗⁺ = {U = 0}` on `Pt`.

***The limit of that witness, stated in advance.***
- One chart of `Pt`'s atlas covers all of `Pt`. So the witness exercises the multi-chart theorem with differing
  preferred charts, but not on a space that needs two charts.
- **Stretch:** a flat cylinder, `ℝ × S¹` with a Rindler-type observer. No single chart covers it, and the Cauchy
  property there would be proved on `N`. p `0.15`.

## The report 69 asked for

If it lands, RESULT sets `mh_causal_alignment_gh_N`'s exact hypotheses against P1's `prop:causal-alignment`, clause by
clause, so 69 can say in plain words what is formalised.

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED, with the step that stopped.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
