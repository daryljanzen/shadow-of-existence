# `r7667+71.4` — RESULT: campaign 93. ①(a) is **BUILT** on the 4D witness, with the other witnesses REPORTED (`RESULT_1.md`). ①(b) is priced, waiting on 69. The refresh is **done**: `r7667_71_inventory/INVENTORY.md`. ② **`cor:densities` 7a BUILT on the manifold**, with 7b BUILT and 7c BUILT IN PART as read, and the witness's black-hole region computed as `{U ≥ 0}`. 7d and 7e remain NOT BEGUN. ⌗ ② `169` new lines (band 40–400). ⌗ p: ①(a) `0.9` came true in part; refresh `0.95` came true; ② `0.9` came true

*Against `PREDICTION.md` (`r7667+71.1` and `.2`). 71 re-ran `lake env lean probes/Densities.lean`. It exits 0 with no
errors and no warnings. All `78` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`. The
forbidden-token grep is clean. `check_no_sorry.py` reports ALL 29 THEOREMS COMPILE. The probe copies campaign 91's
`ConeDisjoint.lean`.*

## ② `cor:densities` on the manifold

All of these hold in a conformal extension with `hOD` and `hI`, and none takes a Cauchy hypothesis.

***The clauses.***
- **7a — BUILT.** `dn_BH_inter_slice : (M ∖ ι⁻¹ J̃⁻(𝒥⁺)) ∩ slice J Θ τ = ∅`, for every `Θ` and `τ`.
  - Route: `slice ⊆ D = ι⁻¹ Ĩ⁻(𝒥⁺) ⊆ ι⁻¹ J̃⁻(𝒥⁺)`.
- **7b — BUILT.** Two forms:
  - `dn_slice_inter_frontier` needs only `LocallyOneChart` on `Ñ`. The slice lies in the open
    `ι⁻¹ Ĩ⁻(𝒥⁺) ⊆ int ι⁻¹ J̃⁻(𝒥⁺)`, so it misses the frontier.
  - `dn_slice_inter_H` gives the form with `S.H J`.
- **7c — BUILT IN PART, as read.** `dn_subset_BH_inter_slice`: any set inside the black-hole region meets no slice.
  P1's "curvature singularity the horizon encloses" has no Lean notion, so this is 7c only on the reading "a
  singularity lies in the black-hole region".
- **The bundle.** `dn_cor_densities` gathers the four.

***The witness*** (`NModel.dn_witness`).
- On campaign 89's compactified `Pt`, the black-hole region is **exactly `{U ≥ 0}`**, using
  `dn_preimage_Jpast_scri`: `ι⁻¹ J̃⁻(𝒥⁺) = {U < 0}`.
- The region is non-empty (`p₀`), and every slice is non-empty.
- All four conclusions hold, so none of them is vacuous.

***Not begun.*** 7d (collapsing matter) and 7e (Oppenheimer–Snyder densities). There is no matter model.

## The inventory marks after this campaign

- 7a moves to **BUILT**.
- 6b-ii, "to the future", moves within BUILT IN PART: it is now general given `HasFutureGenerators`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
