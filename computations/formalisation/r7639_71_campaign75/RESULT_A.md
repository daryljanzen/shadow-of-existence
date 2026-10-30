# `r7639+71.3` — RESULT: campaign 75, `r7639` ①, **the registered answer stands: P1's `prop:causal-alignment` does not need properness.** Properness, and the slice lower limit `𝓗⁺ ⊆ KLi(S_τ)`, are BUILT from the Cauchy property, with no `SublevelProper`, no `LocConnAt` and no continuity hypothesis. Hence `KLi(S_τ) = KLs(S_τ) = 𝓗⁺`. The Cauchy property is used in its future-inextendible form. ⌗ `834` lines in one probe (about `350` new, band 150–2000 new). ⌗ p: slice lower limit with no added hypothesis `0.75` came true; properness derived `0.7` came true; curve inextendible inside campaign 60's two-sided definition `0.4` did not come true (registered reachable negative taken)

*Against `PREDICTION.md` (`r7639+71.1`). 71 re-ran `lake env lean probes/CauchyProperness.lean`. It exits 0 with no
errors and no warnings. All `16` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`. The forbidden-token
grep is clean. The probe is campaign 74's, copied in under `ShadowProbe.CauchyPropernessProbe` with the prefix `cp_`.
Campaign 74's cone limits and its `LocConnAt` lower limit are not copied, since this probe supersedes them.*

## The steps, as registered

1. **`I⁻(q) ⊆ D`** — BUILT.
   - `cp_isOpen_Ifut`: `I⁺(x)` is open. This is new, via `tstep_end_eventually`.
   - `cp_Ipast_subset_D`: for `q ∈ closure D`, `I⁻(q) ⊆ D`.
   - `cp_Ipast_subset_D_of_H`: the same for `q ∈ 𝓗⁺`, under campaign 72's `hcl`.
2. **A future-inextendible timelike curve of `D` into `q`** — BUILT.
   - `cp_curve` gives `γ t = q − ε e^{−t} T(q)`.
   - It is a `FutInextCurve` of `Dsp` with `γ → q`, each `γ t ≪ q`, and `γ t ≪ γ t'` for `t < t'`.
3. **`Θ → ∞` along it** — BUILT, from the future form of the Cauchy property.
4. **Properness** — BUILT.
   - `cp_blowup_cauchy` and `cp_tendsto_atTop_H_cauchy` give it pointwise at `𝓗⁺`.
   - `cp_sublevelProper` gives campaign 74's `SublevelProper J Θ` itself, under `hint`.
5. **The slice lower limit** — BUILT.
   - `cp_mem_KLi_slice`, `cp_slice_lower_limit` and `cp_slice_lower_limit_seq` assume no properness, no local
     connectedness and no continuity.
   - No intermediate value theorem was needed. The Cauchy property hits each level on the tail of the curve, and `Θ`
     increases strictly along the curve.

## The final theorems

- `cp_slice_kuratowski` gives `KLi(S_τ) = KLs(S_τ) = 𝓗⁺`.
- `cp_causal_alignment` gives properness together with those two equalities.
- **Hypotheses:**
  - the observer hypotheses `hOD` and `hmono`, and `hadapt`;
  - `hcl` and `hint`;
  - `(Dsp J).FutCauchyTemporal Θ`;
  - `hHM : 𝓗⁺ ⊆ M`.
- Campaign 74's Schwarzschild example is withdrawn in the docstring. As registered, it lies outside the hypotheses.

## The gaps, stated

***The Cauchy property is used in its future form.***
- `FutCauchyTemporal Θ` says: `Θ` is temporal, and every future-inextendible causal curve of `D` attains every level
  `≥ Θ(γ 0)`.
- This is the registered reachable negative, not campaign 60's two-sided `IsCauchyTemporal`.
- The bridge between them is not formalised. It is the standard fact that every future-inextendible causal curve extends
  to an inextendible one.

***`hHM : 𝓗⁺ ⊆ M` is an added hypothesis.***
- It is needed because frontiers are taken in the chart, and `T` is timelike only on `M`.
- P1 has `𝓗⁺ ⊆ M`, so the hypothesis holds in the paper's setting.

**For 69: P1's sentence stands as written. No properness clause is needed.**

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
