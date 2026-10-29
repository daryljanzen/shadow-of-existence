# `r7633+71.4` — RESULT: campaign 70, `r7633` ②, Christoffel symbols and pregeodesics BUILT, the corner-cutting lemma BUILT for C² causal curves (needing only a C¹ metric), and the tangency clause BUILT IN PART: a C² causal curve in `𝓗⁺` is a null pregeodesic. ⌗ `704` lines in one probe (registered `900`, band 300–3000). ⌗ p: `①` `0.7` and corner-cutting `0.3` came true; tangency `0.1` came partly true

*Against `PREDICTION.md` (`r7633+71.2`). 71 re-ran `lake env lean probes/CornerCutting.lean`. It exits 0 with no
errors. All `18` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`. Only `g ∈ C¹` is used, not
C².*

## ① Christoffel symbols and pregeodesics

- `ct_nondegenerate`: `g_x` is nondegenerate on `M`. This is proved from the Lorentzian structure, not assumed.
- `ct_flat_surjective`: the musical map `♭` is onto.
- `Γ` is defined as `♭⁻¹` of the Koszul covector:
  - `ct_christoffel_koszul` gives the defining identity
    `g(Γ(u,v),w) = ½(Dg(u)(v,w) + Dg(v)(u,w) − Dg(w)(u,v))`;
  - `ct_christoffel_unique` and `ct_christoffel_symm` give uniqueness and symmetry.
- `acc = γ″ + Γ(γ′,γ′)`. A curve is a pregeodesic when `acc ∥ γ′`.
- `ct_metric_compat`: `(g(γ′,γ′))′ = 2g(γ′, acc)`.
- `ct_first_variation`: the first variation of `g(γ_ε′,γ_ε′)`.

## ② The corner-cutting lemma

***`ct_corner_cutting`.*** Let `γ` be C², future-causal on `[a,b]`, and not a pregeodesic at some interior `t₀`.
Then `γ(s) ≪ γ(t)` for some `a < s < t₀ < t < b`. `ct_corner_cutting_null` is the registered null form.

***Proof.***
1. Take `Z₀ ⊥ γ′` with `g(acc, Z₀) > 0`.
2. Tilt it by `T`, so that `h = g(γ′, Z)` changes sign at `t₀`.
3. Set `W = (r−s)(t−r)Z`. Then the first variation is negative on the whole closed interval.
4. A compactness argument makes `γ + εW` future-timelike for one small `ε > 0`, with the endpoints fixed. That is a
   timelike step.

No push-up is used. The sign control the registration named as the likely stop did not stop it.

## ③ The tangency clause: BUILT IN PART

***Built.***
- `ct_H_achronal`: `𝓗⁺ = ∂J⁻(J)` is achronal.
- `ct_achronal_null` and `ct_achronal_pregeodesic`: an achronal C² causal curve is null and a pregeodesic.
- **`ct_H_generator_null_pregeodesic`**: a C² causal curve lying in `𝓗⁺` is a null pregeodesic.

***REPORTED.***
- **The generators' C² regularity.** Campaign 69 gives Lipschitz generators that are null a.e. The first missing
  lemma is corner-cutting for curves that are only a.e. differentiable, i.e. for Lipschitz causal curves: such a
  curve in `∂J⁻(S) ∖ S`, reparametrised, is a C² null geodesic.
- **The accumulation `∂J⁻(O(τ)) → 𝓗⁺`**, for example in the Hausdorff sense on compact sets. This was not
  attempted. Campaign 61's limit-curve lemma and campaign 67's closedness are available for it, so the missing
  piece is the convergence argument itself, not the limit-curve theorem the build report named.

No census row moves.
