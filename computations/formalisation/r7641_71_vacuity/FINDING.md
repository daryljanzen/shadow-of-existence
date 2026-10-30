# `r7641+71.1` — FINDING: the `Θ`-hypotheses of campaigns 74 and 75 cannot hold when `𝓗⁺ ≠ ∅`, so their slice theorems are vacuous. `probes/VacuityCheck.lean` proves `False` from them, on the standard axioms. The paper argument is untouched; the Lean repair is campaign 78.

*Found by 71 while reading the definitions for `r7641`, before registering campaigns 77–79. Reported at once.*

***The cause.*** Campaign 60's `IsTemporal Θ` (copied by campaigns 72, 74 and 75) requires `ContDiff ℝ 1 Θ` on the
whole chart `V`, even when applied to `Dsp J`, whose `M` is `D`. So `Θ` is continuous at every horizon point.

***The proof.***
- Campaign 75's `cp_tendsto_atTop_H_cauchy` proves `Θ → ∞` along `𝓝[D] q` for `q ∈ 𝓗⁺`.
- `cp_vacuous` (`probes/VacuityCheck.lean`, campaign 75's file plus one theorem) derives `False` from `hcl`, `hHM`,
  `FutCauchyTemporal Θ` and `q ∈ 𝓗⁺`.
- `#print axioms` reads `[propext, Classical.choice, Quot.sound]`.
- Campaign 74's `SublevelProper` together with a continuous `Θ` contradicts `q ∈ closure D \ D` in the same way.

***What is affected.***
- **Vacuous whenever `𝓗⁺ ≠ ∅`:** campaign 75's properness, slice lower limit and `cp_causal_alignment`, and campaign
  74's slice lower limit.
- **Presumably unsatisfiable:** campaign 60's `ExteriorGH`, on the same grounds, once campaign 78's two-sided ⇒ future
  step is in.

***What is not affected.***
- Campaign 72's cone limits (`hc_kuratowski`, no `Θ`), and campaigns 73, 76 and 77 (no `Θ`).
- The paper argument of campaign 75, which never needed `Θ` defined on `𝓗⁺`.

***The repair*** (campaign 78): `IsTemporal Θ := ContDiffOn ℝ 1 Θ M ∧ …`. Campaign 79's model shows the repaired
hypotheses are satisfiable with `𝓗⁺ ≠ ∅`.

**For 69: until campaign 78 lands, "P1's sentence stands" (`r7639+71.3`) rests on the paper argument, not on the
Lean.** The verification that RESULT reported (build, axioms) was correct as far as it went, but it did not test
whether the hypotheses can hold. That check is now part of 71's verification of every probe.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
