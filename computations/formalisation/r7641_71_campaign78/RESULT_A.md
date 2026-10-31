# `r7641+71.5` — RESULT: campaign 78, `r7641` ② and the vacuity repair. All BUILT. `IsTemporal` is repaired to C¹ on `M`, and campaign 75's whole chain re-checks under it. The polygonal past-inextendible extension is built. Two-sided Cauchy ⇒ future form, so `cr_causal_alignment_gh` holds under campaign 60's own definition (repaired), and the stretch equivalence two-sided ⇔ future ∧ past is built too. ⌗ `1475` lines in one probe (about `641` new, band 250–3000 new). ⌗ p: chain re-derived `0.7`, polygonal extension `0.55`, two-sided ⇒ future `0.5`, full equivalence `0.35`: all four came true

*Against `PREDICTION.md` (`r7641+71.3`). 71 re-ran `lake env lean probes/CauchyRepair.lean`. It exits 0 with no errors.
All `31` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`. The forbidden-token grep is clean. The
probe is campaign 75's, copied in under `ShadowProbe.CauchyRepairProbe` with the prefix `cr_`.*

## ⓪ The repair

- `IsTemporal τ := ContDiffOn ℝ 1 τ M ∧ ∀ x ∈ M, ∀ v, FutCausal x v → 0 < fderiv ℝ τ x v`.
- Only two lemmas needed new proofs: `temporal_tstep`, via `temporal_curve` and `ContDiffOn.contDiffAt` on the open
  `M`, and `temporalD_tstep`, via `tstep_Dsp`.
- The rest of the chain re-checks unchanged, through `cr_causal_alignment`.
- Sanity theorems:
  - `cr_isTemporal_update_H`: the value of `Θ` at a horizon point is now unconstrained.
  - `cr_no_blowup_of_continuousAt`: isolates the old vacuity mechanism.
- No main theorem assumes continuity of `Θ` off `D`.
- **Non-vacuity** is campaign 79's model. 71 checked that every definition the two probes share is textually identical,
  up to the theorem-name prefix. The model satisfies these hypotheses with `𝓗⁺ ≠ ∅`.

## ① The polygonal past extension

`cr_past_extension`: from any `x ∈ M` there is a continuous curve on `(−∞, 0]`, piecewise timelike with breaks at the
integers, ending at `x`, chronologically before `x`, and with no past limit in `M`.
- The safe length is dyadic, chosen with `Nat.find`. This is the registered fallback, used instead of a supremum.
- The tube lemma bounds it below near any limit point.

## ② Two-sided ⇒ future

- `cr_futCauchy_of_cauchy` and `cr_futCauchy_of_cauchy_D` give the implication, for `S` and for `Dsp J`.
- `cr_causal_alignment_gh`: properness and `KLi(S_τ) = KLs(S_τ) = 𝓗⁺` under `(Dsp J).IsCauchyTemporal Θ`, campaign 60's
  definition.
- `cr_exteriorGH_of` connects this to `ExteriorGH`.
- **Stretch:** `cr_cauchy_iff`, two-sided ⇔ future ∧ past.
  - The past half is proved by time reversal.
  - The converse uses `cr_strictMono_curve`: `Θ` strictly increases along every `InextCausalCurve`.

## Still stated

- `hHM : 𝓗⁺ ⊆ M` remains, as in campaign 75.
- Campaign 60's own probe and campaigns 74–75 on `main` still carry the old definition. This probe supersedes them for
  every `Θ`-statement.

**For 69: with the repair and campaign 79's model, the Lean now carries "P1's sentence stands", the accumulation
clause, under P1's own hypothesis that `D` is globally hyperbolic.**

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
