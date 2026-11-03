# `r7659+71.2` — RESULT: campaign 89, `r7659`, (B), **all three pieces BUILT, and no registered stop was hit**. P1's `𝓗⁺ = ∂J⁻(𝒥⁺)` is proved in a conformal extension from P1's own `I⁻(O) = I⁻(𝒥⁺)`. It is witnessed on `Pt` compactified by `arctan V`, with `𝒥⁺` a null line on the boundary of `ι(N)`. **`prop:causal-alignment` is now one Lean theorem with every clause on the manifold**, witnessed end to end. ⌗ `6184` lines in one probe (about `436` new, band 400–2500 new). ⌗ p: identification `0.7`, witness `0.4`, headline `0.6`: all came true

*Against `PREDICTION.md` (`r7659+71.1`). 71 re-ran `lake env lean probes/ConformalBoundary.lean`. It exits 0 with no
errors and no warnings. All `62` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `47` are kept
from campaign 88 and `15` are new. The forbidden-token grep is clean. `check_no_sorry.py` reports ALL 29 THEOREMS
COMPILE. The probe copies campaign 88's `ManifoldCones.lean`. Lean does not parse `S̃` as an identifier, so the code
writes `St`.*

## The definition

`structure ConformalExtension (S : MSpacetime E N) (St : MSpacetime E Ñ)` has these fields:
- `ι`, with `IsOpenEmbedding ι` and `ContMDiff 1 ι`;
- `Ω > 0`, with `g̃(Dι v, Dι w) = Ω² g(v, w)`;
- `Dι(T)` future-timelike on `M`;
- `ι '' M ⊆ M̃`.

## ① The identification — BUILT

`theorem mx_H_eq_boundary (hL : S.LocallyOneChart) (hLt : St.LocallyOneChart) (X : ConformalExtension S St) (h𝒥 : 𝒥 ⊆ St.M) (hOD) (hmono) (hJM) (hI : S.IpastSet (range O) = X.ι ⁻¹' St.IpastSet 𝒥) : S.H (range O) = frontier (X.ι ⁻¹' St.JpastSet 𝒥) ∧ S.H J = frontier (X.ι ⁻¹' St.JpastSet 𝒥)`

***Route.*** As registered.
- `mx_frontier_JpastSet` gives `∂J⁻(A) = closure I⁻(A) ∖ I⁻(A)` on any manifold spacetime, from `mh_hint`, `mh_hcl`
  and `mk_isOpen_D`. It is applied once to `S` and once to `St`.
- The open embedding is pulled back with Mathlib's `IsOpenMap.preimage_frontier_eq_frontier_preimage` and
  `IsOpenMap.preimage_closure_eq_closure_preimage`.

***Used, as stated in advance.*** Of the extension's fields, only `ι` and `isOpenEmbedding` are used. The conformal,
smoothness and orientation fields make the object P1's, but they play no part in the identification. The step's
substance is push-up in `Ñ`.

## ② The witness — BUILT

***The map.***
- `ι = ψ ∘ (U, V ↦ U, arctan V) ∘ φ` on `Pt`, with `minkN` on both sides.
- `mx_ι_isOpenEmbedding` and `mx_ι_contMDiff` hold. **The registered expected stop was not hit:** `Pt` has a global
  chart.
- `mx_dι_eq`: `Dι = diag(1, 1/(1+V²))`, so `Ω² = 1/(1+V²)`.
- `mx_witnessExt` proves every field of the structure.

***`𝒥⁺` and its past.***
- `𝒥⁺ = ψ '' {U < 0, v = π/2}`. It lies in the frontier of `ι(N)` and in `M̃`, and is non-empty.
- `I⁻_Ñ(𝒥⁺) = {U < 0, V < π/2}`. **The second stop was not hit:** `I⁻` is computed in `Ñ`, so no curve needs to stay
  inside `ι(N)`.
- Its preimage is `D`, so `hI` holds.

***The witness theorem.*** `mx_witness_boundary` gives `𝓗⁺ = ∂J⁻(𝒥⁺) = {U = 0}`, a non-empty set.

## ③ The headline whole — BUILT

***`mx_prop_causal_alignment [T2Space N]`.***
- **Hypotheses:** ①'s, plus `hHM : 𝓗⁺ ⊆ M`, `hΘ : IsCauchyTemporalOn (D J) Θ` and `hadapt`. These are inherited from
  campaigns 87–88; none is new.
- **Conclusion,** with `𝓗⁺ := ∂J⁻(𝒥⁺)`:
  - `S.H J = 𝓗⁺`;
  - properness;
  - `KLi = KLs = 𝓗⁺` for the slices;
  - `KLi = KLs = 𝓗⁺` for the past cones;
  - at every `q ∈ 𝓗⁺`, campaign 80's rate condition gives alignment, `(dΘ(n))⁻¹ dΘ → −g_q(ℓ₀, ·)`.

***`mx_witness_headline`.*** It instantiates every clause on `Pt` with `Θ₀ ∘ φ`. The tangency clause is instantiated at
`p₀`. Campaign 88's `mc_witness_tangency_holds` covers every horizon point in `p₀`'s chart.

## Limits, stated

- In the witness, `Ñ` and `N` are the same type, `Pt`, and `Pt` has one global chart. A witness with `Ñ` a genuine
  compactification, such as a diamond with its corners, is not built. Neither is the flat cylinder.
- The identification uses only the topology of the open embedding. That is how P1's step reads: `∂J⁻ = ∂I⁻` under
  push-up, applied in `Ñ`.

**For 69: `prop:causal-alignment` is formalised whole.** On a smooth Hausdorff spacetime with a conformal extension
whose `𝒥⁺` has `I⁻(O) = I⁻(𝒥⁺)`, and an adapted Cauchy time function on `D`:
- the slices accumulate exactly on `∂J⁻(𝒥⁺)`, and the time function is proper;
- the observer's past cones converge to `∂J⁻(𝒥⁺)`;
- under P1's rate condition, the slices align with the generators.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
