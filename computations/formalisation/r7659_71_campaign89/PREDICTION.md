# `r7659+71.1` — PRE-REGISTRATION: campaign 89, `r7659`, (B), the conformal extension. P1's `𝓗⁺ = ∂J⁻(𝒥⁺)` is proved from `I⁻(O) = I⁻(𝒥⁺)` for `𝒥⁺` on the boundary of `N` inside a conformal extension `Ñ`, witnessed on `Pt` compactified by `arctan V`, and the headline is assembled whole. ⌗ `900` new lines in one probe (band 400–2500 new), ⛔ stop `3500` new. ⌗ p: the identification `0.7`; the witness `0.4`; the whole headline `0.6` given both. **Re-priced before any Lean, against campaign 88's `1500–3000` lines at p `0.35`; reason below. Expected stop: the witness's `ι` as a `ContMDiff` open embedding of `Pt` into `Pt`, through the `nullH` chart.** Second likeliest: `I⁻_Ñ(𝒥⁺)` on the witness, where curves may leave `ι(N)`

*Under `r7659`. A new probe, `probes/ConformalBoundary.lean`. It copies campaign 88's `ManifoldCones.lean`. No Lean was
written before this registration.*

## The re-pricing, stated before any Lean

Campaign 88 priced (B) at p `0.35` and `1500–3000` lines. That price assumed the identification needs curves carried
through `ι`, with causal character invariant under the conformal map. Scoping finds it does not:
- the frontier of `J⁻` equals the closure of `I⁻` minus `I⁻`, wherever push-up holds;
- push-up holds in `Ñ` by campaign 86's kit applied to `Ñ`;
- an open embedding commutes with closure and interior under preimage.

The curve-level question returns only in the witness, where `I⁻_Ñ(𝒥⁺)` is computed. Hence the new price.

## The definition

`structure ConformalExtension (S : MSpacetime E N) (S̃ : MSpacetime E Ñ)` carries:
- `ι : N → Ñ`, an open embedding, `ContMDiff` of class `1`;
- `Ω : N → ℝ` with `0 < Ω`, and `S̃.g (ι x) (Dι v) (Dι w) = Ω x ^ 2 * S.g x v w`, where `Dι = mfderiv ι x`;
- the time orientations agree: `Dι (T x)` is future-timelike for `S̃` on `M`;
- `ι '' S.M ⊆ S̃.M`.

`𝒥⁺ ⊆ frontier (range ι) ∩ S̃.M`. P1's sets inside `N` are:
- `I⁻(𝒥⁺) := ι ⁻¹' S̃.IpastSet 𝒥⁺`;
- `J⁻(𝒥⁺) := ι ⁻¹' S̃.JpastSet 𝒥⁺`.

***Stated in advance:*** the conformal clauses belong to the definition, so that it is P1's object. The identification
is expected to use only the open embedding, so RESULT will say which clauses were used.

## ① The identification

`mx_H_eq_boundary (hL : S.LocallyOneChart) (hL̃ : S̃.LocallyOneChart) (X : ConformalExtension S S̃) (h𝒥 : 𝒥⁺ ⊆ S̃.M) (hOD) (hmono) (hJM) (hI : S.IpastSet (range O) = ι ⁻¹' S̃.IpastSet 𝒥⁺) : S.H (range O) = frontier (ι ⁻¹' S̃.JpastSet 𝒥⁺)`.

***Route.***
- On `N`: `frontier J⁻(O) = closure D ∖ D`, by `mh_hint`, `mh_hcl` and `D` open.
- On `Ñ`: `frontier J̃⁻(𝒥⁺) = closure Ĩ⁻(𝒥⁺) ∖ Ĩ⁻(𝒥⁺)`, by the same two results applied to `S̃`.
- Pull back by the open embedding, then use `hI`.

## ② The witness

- `Ñ = Pt` with `minkN`, and `N = Pt`.
- `ι = φ⁻¹ ∘ (id × arctan) ∘ φ`, so `ι(N) = {(φ ·).2 ∈ (−π/2, π/2)}`.
- `Ω² = 1/(1 + V²)`.
- `𝒥⁺ = φ⁻¹ {(u, π/2) : u < 0}`, which lies in the frontier of `ι(N)`.
- `I⁻_Ñ(𝒥⁺) = φ⁻¹ {u < 0, v < π/2}`, so its preimage is `D = {U < 0}`, and `hI` holds.
- Then `{U = 0} = ∂J⁻(𝒥⁺)`.

## ③ The headline whole

`mx_prop_causal_alignment` states every clause of `prop:causal-alignment` with `𝓗⁺ := frontier J⁻(𝒥⁺)`:
- accumulation (`mh_causal_alignment_gh_N`);
- cone convergence (`mc_cone_kuratowski_N`);
- tangency (`mc_tangency_at_N`).

It is witnessed end to end on `Pt` with `Θ₀ ∘ φ`.

***Fallback, as 69 ordered.*** If ② stalls, ① and ③ land with the witness's `hI` stated as a hypothesis, and the gap is
named. If ① stalls, (A) lands as a stated hypothesis.

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED, with the step that stopped. Non-vacuity is shown on
`Pt`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
