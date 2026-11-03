# `r7663+71.2` — RESULT: campaign 91 ①, **no past light cone meets `𝓗⁺`, BUILT**, and the stronger `closure J⁻(O τ) ∩ 𝓗⁺ = ∅`. `prop:causal-alignment` gains an eighth conjunct with no new hypothesis. The registered stop, the closure step, was not hit. ⌗ `6371` lines in one probe (`187` new, band 100–700). ⌗ p `0.8` came true

*Against `PREDICTION.md` (`r7663+71.1`). 71 re-ran `lake env lean probes/ConeDisjoint.lean`. It exits 0 with no errors
and no warnings. All `70` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `62` are kept and `8`
are new. The forbidden-token grep is clean. The probe copies campaign 89's `ConformalBoundary.lean`.*

## The theorems

- `MSpacetime.cd_cone_disjoint [T2Space N] (hL) (hOD) (hmono) (hJM) (hHM) (hΘ : S.IsCauchyTemporalOn (S.D J) Θ) : ∀ τ, S.cone O τ ∩ S.H J = ∅`. It needs no `hadapt`.
- `cd_closure_Jpast_inter_H` is the stronger form, `closure J⁻(O τ) ∩ 𝓗⁺ = ∅`.
- `MSpacetime.cd_prop_causal_alignment` takes exactly `mx_prop_causal_alignment`'s hypotheses. It concludes its seven
  conjuncts and adds an eighth: `∀ τ, cone O τ ∩ ∂J⁻(𝒥⁺) = ∅`.

## The route

1. `cd_chr_of_mem_closure_Jpast`, the registered step 1: from `x ∈ closure J⁻(p)` and `y ≪ x`, conclude `y ≪ p`. It
   needs only `LocallyOneChart`, through the openness of `I⁺` and push-up.
2. `cd_mem_closure_sublevel`: such an `x` lies in the closure of `{y ∈ D | Θ y ≤ Θ p}`, because `Θ` increases along
   `≪` inside `D`.
3. `cd_closure_Jpast_subset_D`: campaign 87's `SublevelProper`, which is derived from the Cauchy property, puts that
   closure inside `D`. Since `D ∩ 𝓗⁺ = ∅`, the clause follows.

***Does it need the Cauchy hypothesis?*** No proof without it was found. Without it, the step `x ∈ closure J⁻(O τ) ⟹
x ∈ D` is the past-reflecting property, which a general spacetime lacks. No counterexample showing the hypothesis is
necessary was built. **For P1:** the clause rests on the Cauchy property of `Θ`, that is on `D`'s global hyperbolicity,
not only on the openness of `D` the proof cites.

## The witness

`NModel.cd_witness` uses `Pt` with `Θ₀ ∘ φ` and campaign 89's extension:
- every cone avoids `∂J⁻(𝒥⁺) = {U = 0}`;
- **every cone is non-empty** (`cd_frontier_nonempty`, by connectedness of `Pt`), so the disjointness is not vacuous.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
