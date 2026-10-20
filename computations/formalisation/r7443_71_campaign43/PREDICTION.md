# `r7443+71.29` — PRE-REGISTRATION: campaign 43, the local piece `r7453` ③ⓒ prices. The general transgression identity `∂_μK^μ = −√−g *RR` on the engine's indefinite Levi-Civita connection. ⌗ `550` lines (band 300–1000), ⛔ stop `1500`. ⌗ p `0.45`

*Under `r7453` ③ⓒ and `r7443` ②, step 4. The piece is named and priced in `r7453_71_gap_class/CLASS.md`. It serves
rows 89 (Part 8) and 96 (Part 3). Both receipts measure the ratio `∂K/(√−g *RR) = −1` on one explicit member;
row 96's build (`member_divergence`) proves it on that member only. No Lean was written before this registration.*

## ① The piece: `probes/Transgression.lean`

- ***Algebraic layer.*** For ANY `Γ : Fin 4 → Matrix (Fin 4) (Fin 4) ℝ` with first and second derivatives
  `∂Γ`, `∂²Γ` (`∂²Γ` symmetric in its two derivative slots), and `F_{μν} = ∂_μΓ_ν − ∂_νΓ_μ + [Γ_μ, Γ_ν]`:
  `ε^{μνρσ} tr(F_{μν}F_{ρσ}) = 4 ∂_μ[ε^{μνρσ} tr(Γ_ν∂_ρΓ_σ + ⅔Γ_νΓ_ρΓ_σ)]`.
  This is to be proved from trace cyclicity, the antisymmetry of `ε` and Schwarz symmetry, ***without expanding
  into components***. The quartic term vanishes by cyclicity against `ε`'s sign on a 4-cycle.
- ***Bridge.*** On the engine's `lcConn` for any smooth nondegenerate metric on `ℝ⁴`, with
  `(Γ_ν)^a_b = Γ^a_{νb}` (row 96's `chrLC`):
  - `F` is the engine's `curv`;
  - the left side is `−√−g *RR`, up to the sign and the factor fixed by row 69's `pontryaginLC` and row 96's
    `csLC`. ***The sign is whatever the receipts' `−1` is; it is not chosen.***
  - Result: `Σ_μ ∂_μ csLC^μ = −√−det g · pontryaginLC` at every point.
- ***Corollaries.*** Row 96's `member_divergence` re-derived from the general identity. The ratio `−1` holds for
  every metric with `*RR ≠ 0`, not just on the member.

***Caveats, registered.***
- This is the identity in coordinates on `ℝ⁴`. It is not the coordinate-free `d CS = tr(R ∧ R)`.
- Covariance of `K` (a non-tensor) is not claimed.

***Failable.***
- BUILT: algebraic layer, bridge and corollary.
- BUILT IN PART: the algebraic layer without the bridge. The likeliest gap is matching index placement and
  `√−g` to the engine's `curv` and `pontryaginLC`.
- REPORTED: neither.

p `0.45` for BUILT. ***Risk:*** elaboration cost of the `ε`-sums over 24 permutations if cyclicity cannot be used
abstractly.

***Census:*** none moves on this campaign alone. It is a foundation. Rows 89 and 96 cite it; row 96 is already
`DONE` on its member.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
