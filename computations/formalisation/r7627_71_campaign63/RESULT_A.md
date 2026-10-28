# `r7627+71.4` — RESULT: campaign 63, `r7627` ①, the uniform Lipschitz reparametrisation BUILT, push-up for the Lipschitz relation BUILT, the null-generator stretch BUILT IN PART. ⌗ `1760` lines in one probe (registered `900`, band 300–2500). ⌗ p: reparametrisation `0.6` and push-up `0.35` came true; generators `0.15` came partly true

*Against `PREDICTION.md` (`r7627+71.1`). 71 re-ran `lake env lean probes/CausalReparam.lean`. It exits 0 with no
errors. All `25` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`. The setting is campaign
61's, in finite dimension.*

## ① The uniform reparametrisation

***Time functional and coercivity.***
- `cr_local_time_functional` derives positivity from `T`: `τ₀ = −g_{x₀}(·, T x₀)` is strictly positive on the
  nonzero closed cones over a ball around any `x₀ ∈ M`.
- `cr_coercive_K` gives `‖v‖ ≤ c_K·τ(v)` on the cones over a compact `K`, by compactness of `K` × the unit sphere.

***Along a curve.***
- `cr_chord_bound` and `cr_tau_mono`: `‖γt − γs‖ ≤ c_K(τγt − τγs)` along a causal curve in `K`, and `τ∘γ` is
  monotone.
- `cr_reparam`, `cr_uniform_reparam` and `cr_uniform_pieces`: every causal curve in `K` has an
  `L_K = c_K·D`-Lipschitz reparametrisation, with the same image and endpoints, and one `L_K` for all curves.
  The reparametrisation is defined by the intermediate value theorem, with no inverse needed.

***Closedness of the causal relation on `K`.***
- `cr_lstepIn_of_limit` and `cr_isClosed_lstepIn`: `{(x,y) | a causal piece in K joins x to y}` is closed.
- `cr_isClosed_lstepIn_local` gives the same with no hypothesis on `τ`, for small `K`.

***Scope.*** For a general compact `K`, positivity of `τ` on its cones is a hypothesis. It is derived from `T` only
for small `K`. No single linear `τ` can exist when `K` carries a closed causal curve; this is stated in a docstring,
not proved.

## ② Push-up for the Lipschitz relation, locally Lipschitz `g`

- `cr_pushup : LCau q p → Chr p z → Chr q z`, against campaign 60's chronological relation exactly.
- `cr_pushup_dual : Chr q p → LCau p z → Chr q z`.
- The route tilts chord quotients directly, with no C¹ approximation:
  - `cr_tilt`: `u ↦ u + θτ₀(u)T x₀` maps every nearby cone hull into the open cone.
  - `cr_local_pushup`: a polygon of straight timelike segments.
  - `cr_pushup_lstep`: the global infimum argument.

## ③ The null-generator stretch: BUILT IN PART

***Built.***
- `cr_interior_JpastL_subset`: `int J⁻_Lip(A) ∩ M ⊆ I⁻(A)`.
- `cr_boundary_limit_curve`.
- `cr_boundary_generator`: under the hypotheses below, every `p ∈ ∂J⁻_Lip(A) ∖ closure A` has a nonconstant causal
  curve from `p` to `closure A` lying entirely in `∂J⁻_Lip(A)`, and achronal: no two of its points are joined by
  `≪`. This is a generator, in its causal form.

***Hypotheses of `cr_boundary_generator`.***
- The approximating events `pₙ → p` are supplied, each joined to `A` by one causal piece inside a compact `K`.
- `τ` is positive over `K`.
- `g` is locally Lipschitz.

***First missing lemma: concatenation.*** An `LCau` chain is a single `LStep`. With it, plus compactness of
`J⁻(A)` in `K`, the approximants follow from `p ∈ closure J⁻(A)` instead of being assumed.

***Not addressed.***
- Past-inextendibility of the generator.
- "Null geodesic", since this setting has no geodesics of `g`. "Null" is delivered as achronality.

***Tangency.*** The tangency clause of `prop:causal-alignment` still waits on these.

No census row moves.
